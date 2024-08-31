---
title: "A new ocean data quality control system reveals a stronger ocean warming rate"
collection: publications
category: manuscripts
permalink: /publication/2023_CODCQC_Tan
excerpt: 'This paper is about the development of the ocean data quality control algorithm (CODC-QC)'
date: 2023-02-01
venue: 'Deep Sea Research Part I: Oceanographic Research Papers'
paperurl: 'https://doi.org/10.1016/j.dsr.2022.103961'
citation: 'Tan Z, Cheng L*, Gouretski V, Zhang B, Wang Y, Li F, Liu Z, and Zhu J., 2023: A new automatic quality control system for ocean profile observations and impact on ocean warming estimate. Deep Sea Research Part I: Oceanographic Research Papers, 194, 103961'
---

Over the past century, more than 16 million ocean temperature profiles had been collected by various instruments. There is an increasing demand for the high-quality, global-distributed *in-situ* data to support scientific research, governmental and non-governmental organizations, industry, fisheries, individuals, and policy makers.

However, each instrumentation provides data of different accuracy, different quality, and different completion of the metadata. Before using this raw data to do the scientific research, the quality control (QC) process is compulsory to ensure data accuracy and availability. In early years, the QC was usually performed manually by the experts. However, the manual QC of large datasets (for example, 16 million profiles in global ocean datasets) is not feasible because of the manpower and time cost. Therefore, how to identify outliers efficiently, quickly, and automatically in an AutoQC system is still a research priority.

 A recent research study published in *Deep-Sea Research Part I* on January 2023 provides a new climatological range-based automatic quality control system for ocean temperature *in-situ* profiles (namely CODC-QC: CAS Ocean Data Center - Quality Control system). The CODC-QC includes 14 distinct quality checks to identify outliers. “We developed this new QC system is to provide a quality-homogenous database, with reducing human-workload and time-consuming on manual QC as well as adapting the increasing volume of daily real-time data flow on observing system and large data centers.”, said TAN Zhetao, the first author from the Institute of Atmospheric Physics (IAP) at the Chinese Academy of Sciences (CAS).

Unlike many existing QC procedures, no assumption is made of a Gaussian distribution law in the new approach as the statistical distribution of the oceanic variables (e.g., temperature and salinity) are typically skewed. Instead, the 0.5% and 99.5% quantiles are used as thresholds in CODC-QC to define the local climatological ranges. In addition, these thresholds are time-varying, which aims at erroneously excluding real data during the ‘extreme events’. The above strategies are used in local climatological range check for both temperature and vertical temperature gradient, in which the anisotropic feature of water properties is accounted for, and the topography barriers adjustment of water mass are made.

Besides, the performance of CODC-QC system was evaluated using two expert/manual QC-ed benchmark datasets. This evaluation demonstrated the effectiveness of the proposed scheme in removing spurious data and minimizing the percentage of mistakenly flagged good data.

Finally, CODC-QC was also applied to the global World Ocean Database (WOD18) including 16, 804, 361 temperature profiles from 1940 to 2021. Based on the statistics of temperature outliers, 7.97% of measurements were rejected, in which XBT data takes the highest rejection rate (15.44%) whereas the Argo profiling float takes the lowest rejection rate (2.39%). “We suggest a dependency of the quality of temperature observations on the instrumentation type.”, said GOURETSKI Viktor, one of co-author and researcher for the IAP/CAS.

The paper also applies the CODC-QC system to the study of monitoring global ocean warming. “We found that the application of the CODC-QC system leads to a 15% difference for linear trend of the global 0–2000m ocean heat content changes within 1991–2021 compared to the application of WOD-QC (NOAA/NCEI), implying a non-negligible source of error in ocean heat content estimate.”, said CHENG Lijing, the corresponding author of this study, and a professor at IAP/CAS.

The quality-controlled (by CODC-QC) and bias-corrected ocean *in-situ* profile data of CAS-Ocean Data Center, Global Ocean Science Database (CODC-GOSD) are now freely accessible at http://www.ocean.iap.ac.cn/ and https://www.casodc.com/data/. Besides, the CODC-QC is freely available from Github (https://github.com/zqtzt/CODCQC) as an Open-Source Python package (CODCQC) under the Apache-2.0 License.



***Citation:***

**Tan Z**, Cheng L*, Gouretski V, Zhang B, Wang Y, Li F, Liu Z, and Zhu J., 2023: A new automatic quality control system for ocean profile observations and impact on ocean warming estimate. Deep Sea Research Part I: Oceanographic Research Papers, 194, 103961, https://doi.org/10.1016/j.dsr.2022.103961