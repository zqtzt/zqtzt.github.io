#!/usr/bin/env python3
"""Update cached Google Scholar profile metrics for the static site."""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen


PROFILE_URL = "https://scholar.google.com/citations"
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


def build_payload(user_id: str, output: Path, timeout: int) -> dict:
    existing = load_existing(output)
    now = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    profile_url = f"{PROFILE_URL}?{urlencode({'user': user_id, 'hl': 'en'})}"

    try:
        html = fetch_profile_html(user_id, timeout)
        metrics = extract_metrics(html)
        return {
            "status": "ok",
            "source": "Google Scholar",
            "profile_id": user_id,
            "profile_url": profile_url,
            "updated_at": now,
            "metrics": metrics,
            "message": "Updated automatically from the Google Scholar public profile.",
        }
    except (HTTPError, URLError, TimeoutError, ValueError) as exc:
        previous_metrics = existing.get("metrics", {})
        return {
            "status": "error",
            "source": "Google Scholar",
            "profile_id": user_id,
            "profile_url": profile_url,
            "updated_at": existing.get("updated_at"),
            "last_attempted_at": now,
            "metrics": previous_metrics,
            "message": f"Automatic update failed: {exc}",
        }


def main() -> int:
    parser = argparse.ArgumentParser(description="Cache Google Scholar metrics as JSON.")
    parser.add_argument("--user", default="Bha1c94AAAAJ", help="Google Scholar profile user id.")
    parser.add_argument("--output", default=str(DEFAULT_OUTPUT), help="Output JSON path.")
    parser.add_argument("--timeout", default=20, type=int, help="Network timeout in seconds.")
    args = parser.parse_args()

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    payload = build_payload(args.user, output, args.timeout)
    output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    if payload["status"] != "ok":
        print(payload["message"], file=sys.stderr)
        return 0

    print(f"Updated Scholar metrics: {payload['metrics']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
