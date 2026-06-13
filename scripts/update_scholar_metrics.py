#!/usr/bin/env python3
"""Update cached Google Scholar profile metrics for the static site."""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen


PROFILE_URL = "https://scholar.google.com/citations"
SERPAPI_URL = "https://serpapi.com/search"
DEFAULT_OUTPUT = Path("assets/data/scholar-metrics.json")


def parse_number(value: str) -> int:
    return int(value.replace(",", "").strip())


def load_existing(path: Path) -> dict:
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}


def has_valid_metrics(payload: dict) -> bool:
    metrics = payload.get("metrics", {})
    return all(isinstance(metrics.get(key), int) for key in ("citations", "h_index", "i10_index"))


def fetch_profile_html(user_id: str, timeout: int) -> str:
    url = f"{PROFILE_URL}?{urlencode({'user': user_id, 'hl': 'en'})}"
    request = Request(
        url,
        headers={
            "User-Agent": (
                "Mozilla/5.0 (compatible; zqtzt.github.io scholar metrics cache; "
                "+https://zqtzt.github.io/)"
            ),
            "Accept-Language": "en-US,en;q=0.9",
        },
    )
    with urlopen(request, timeout=timeout) as response:
        return response.read().decode("utf-8", errors="replace")


def fetch_serpapi_payload(user_id: str, api_key: str, timeout: int) -> dict:
    url = f"{SERPAPI_URL}?{urlencode({'engine': 'google_scholar_author', 'author_id': user_id, 'hl': 'en', 'api_key': api_key})}"
    request = Request(url, headers={"Accept": "application/json"})
    with urlopen(request, timeout=timeout) as response:
        payload = json.loads(response.read().decode("utf-8", errors="replace"))

    if payload.get("error"):
        raise ValueError(payload["error"])

    status = payload.get("search_metadata", {}).get("status")
    if status and status.lower() != "success":
        raise ValueError(f"SerpApi search status: {status}")

    return payload


def extract_serpapi_metrics(payload: dict) -> dict[str, int]:
    table = payload.get("cited_by", {}).get("table", [])
    metrics: dict[str, int] = {}

    for row in table:
        if not isinstance(row, dict):
            continue
        for label, values in row.items():
            if not isinstance(values, dict) or "all" not in values:
                continue

            normalized = label.lower().replace("-", "_")
            if "citation" in normalized:
                metrics["citations"] = int(values["all"])
            elif normalized in {"h_index", "indice_h"} or normalized.endswith("_h"):
                metrics["h_index"] = int(values["all"])
            elif "i10" in normalized:
                metrics["i10_index"] = int(values["all"])

    if len(metrics) < 3 and len(table) >= 3:
        # SerpApi preserves Google Scholar's metric order even when labels are localized.
        for target, row in zip(("citations", "h_index", "i10_index"), table[:3]):
            if target in metrics or not isinstance(row, dict):
                continue
            values = next((value for value in row.values() if isinstance(value, dict) and "all" in value), None)
            if values is not None:
                metrics[target] = int(values["all"])

    missing = [key for key in ("citations", "h_index", "i10_index") if key not in metrics]
    if missing:
        raise ValueError(f"Missing SerpApi Scholar metrics: {', '.join(missing)}")

    return metrics


def extract_metrics(html: str) -> dict[str, int]:
    pattern = re.compile(
        r'<td class="gsc_rsb_sc1">(?P<label>Citations|h-index|i10-index)</td>\s*'
        r'<td class="gsc_rsb_std">(?P<all>[\d,]+)</td>\s*'
        r'<td class="gsc_rsb_std">(?P<recent>[\d,]+)</td>',
        re.IGNORECASE,
    )
    raw_metrics = {match.group("label").lower(): parse_number(match.group("all")) for match in pattern.finditer(html)}

    required = {
        "citations": "citations",
        "h-index": "h_index",
        "i10-index": "i10_index",
    }
    missing = [label for label in required if label not in raw_metrics]
    if missing:
        raise ValueError(f"Missing Scholar metrics: {', '.join(missing)}")

    return {target: raw_metrics[label] for label, target in required.items()}


def build_payload(
    user_id: str,
    output: Path,
    timeout: int,
    manual_metrics: dict[str, int] | None = None,
    serpapi_key: str | None = None,
) -> dict:
    existing = load_existing(output)
    now = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    profile_url = f"{PROFILE_URL}?{urlencode({'user': user_id, 'hl': 'en'})}"

    if manual_metrics is not None:
        return {
            "status": "ok",
            "source": "Google Scholar",
            "provider": "Manual cache update",
            "profile_id": user_id,
            "profile_url": profile_url,
            "updated_at": now,
            "metrics": manual_metrics,
            "message": "Updated manually from the Google Scholar public profile.",
        }

    try:
        if serpapi_key:
            metrics = extract_serpapi_metrics(fetch_serpapi_payload(user_id, serpapi_key, timeout))
            provider = "SerpApi Google Scholar Author API"
        else:
            html = fetch_profile_html(user_id, timeout)
            metrics = extract_metrics(html)
            provider = "Google Scholar public profile"

        return {
            "status": "ok",
            "source": "Google Scholar",
            "provider": provider,
            "profile_id": user_id,
            "profile_url": profile_url,
            "updated_at": now,
            "metrics": metrics,
            "message": f"Updated automatically from {provider}.",
        }
    except (HTTPError, URLError, TimeoutError, ValueError) as exc:
        if has_valid_metrics(existing):
            print(f"Scholar fetch failed; keeping previous cached metrics: {exc}", file=sys.stderr)
            return existing

        return {
            "status": "error",
            "source": "Google Scholar",
            "provider": "SerpApi Google Scholar Author API" if serpapi_key else "Google Scholar public profile",
            "profile_id": user_id,
            "profile_url": profile_url,
            "updated_at": existing.get("updated_at"),
            "last_attempted_at": now,
            "metrics": existing.get("metrics", {}),
            "message": f"Automatic update failed: {exc}",
        }


def main() -> int:
    parser = argparse.ArgumentParser(description="Cache Google Scholar metrics as JSON.")
    parser.add_argument("--user", default="Bha1c94AAAAJ", help="Google Scholar profile user id.")
    parser.add_argument("--output", default=str(DEFAULT_OUTPUT), help="Output JSON path.")
    parser.add_argument("--timeout", default=20, type=int, help="Network timeout in seconds.")
    parser.add_argument("--citations", type=int, help="Manual total citations value from Google Scholar.")
    parser.add_argument("--h-index", dest="h_index", type=int, help="Manual h-index value from Google Scholar.")
    parser.add_argument("--i10-index", dest="i10_index", type=int, help="Manual i10-index value from Google Scholar.")
    parser.add_argument(
        "--serpapi-key",
        default=os.environ.get("SERPAPI_API_KEY") or os.environ.get("SERPAPI_KEY"),
        help="SerpApi API key. Defaults to SERPAPI_API_KEY or SERPAPI_KEY.",
    )
    args = parser.parse_args()

    manual_values = [args.citations, args.h_index, args.i10_index]
    if any(value is not None for value in manual_values) and not all(value is not None for value in manual_values):
        parser.error("--citations, --h-index, and --i10-index must be provided together.")

    manual_metrics = None
    if all(value is not None for value in manual_values):
        manual_metrics = {
            "citations": args.citations,
            "h_index": args.h_index,
            "i10_index": args.i10_index,
        }

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    payload = build_payload(args.user, output, args.timeout, manual_metrics, args.serpapi_key)
    output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    if payload["status"] != "ok":
        print(payload["message"], file=sys.stderr)
        return 0

    print(f"Updated Scholar metrics: {payload['metrics']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
