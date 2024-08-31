---
title: "IAPv4 ocean temperature and ocean heat content gridded dataset"
collection: publications
category: manuscripts
permalink: /publication/2024_IAPv4_Cheng
excerpt: 'This paper is about the release of theIAP temperature grid data (version 4)'
date: 2024-08-01
venue: 'Earth System Science Data'
paperurl: 'https://doi.org/10.5194/essd-2024-42'
citation: 'Cheng, L., Pan, Y., Tan, Z., Zheng, H., Zhu, Y., Wei, W., Du, J., Yuan, H., Li, G., Ye, H., Gouretski, V., Li, Y., Trenberth, K., Abraham, J., Jin, Y., Reseghetti, F., Lin, X., Zhang, B., Chen, G., Mann, M., and Zhu, J., 2024: IAPv4 ocean temperature and ocean heat content gridded dataset, Earth Syst. Sci. Data.'
---

Ocean observational gridded products are vital for climate monitoring, ocean and climate research, model evaluation, and supporting climate mitigation and adaptation measures. This paper describes the 4th version of the Institute of Atmospheric Physics (IAPv4) ocean temperature and ocean heat content (OHC) objective analysis product. It accounts for recent developments in quality control (QC) procedures, climatology, bias correction, vertical and horizontal interpolation, and mapping and is available for the upper 6000 m (119 levels) since 1940 (more reliable after ∼ 1957) for monthly and 1°× 1°temporal and spatial resolutions. IAPv4 is compared with the previous version, IAPv3, and with the other data products, sea surface temperatures (SSTs), and satellite observations. It has a slightly stronger long-term upper 2000 m OHC increase than IAPv3 for 1955–2023, mainly because of newly developed bias corrections. The IAPv4 0–2000 m OHC trend is also higher during 2005–2023 than IAPv3, mainly because of the QC process update. The uppermost level of IAPv4 is consistent with independent SST datasets. The month-to-month OHC variability for IAPv4 is desirably less than IAPv3 and the other OHC products investigated in this study, the trend of ocean warming rate (i.e., warming acceleration) is more consistent with the net energy imbalance at the top of the atmosphere than IAPv3, and the sea level budget can be closed within uncertainty. The gridded product is freely accessible at https://doi.org/10.12157/IOCAS.20240117.002 for temperature data and at https://doi.org/10.12157/IOCAS.20240117.001 for ocean heat content data.



【Chinese Version中文版】

链接：https://iap.cas.cn/gb/xwdt/kyjz/202408/t20240805_7240679.html

​	准确的全球海洋温度和热含量格点观测数据集对于海洋和气候科学研究、气候监测及业务化应用具有重要意义。由中国科学院大气物理研究所（以下简称“大气所”）牵头，联合中国科学院计算机网络信息中心、中国科学院海洋研究所、崂山实验室、中国科学院南海海洋研究所、美国国家大气研究中心、意大利国立地球物理与火山学研究所、新西兰奥克兰大学等机构，在《Earth System Science Data》期刊上正式发布了第四代的全球海洋温度和热含量格点观测数据集（IAPv4）（Cheng* et al. 2024）。IAPv4数据集具有全球海洋1° × 1°分辨率，覆盖海洋1~6000米（119层），时间跨度自1940至今（月平均）。

​	相对于国际同类以及上一个版本的IAPv3数据集，IAPv4数据集在多个技术层面实现了显著提升，包括原始观测数据的质量控制、偏差订正和格点化技术（表1）。其技术优势体现在：1）IAPv4采用了自主研发的CODC-QC数据质量控制系统对数据错情进行标注（Tan et al.,2023），其准确率较国际主流的质控技术有较大提升，提高了观测数据的准确性。2）针对不同类型的观测仪器分别采用了新的偏差订正方案，确保了观测数据的无偏性。针对XBT（抛弃式探温仪）、MBT（机械式探温仪）、OSD（南森瓶）、APB（动物携带的传感器）四种类型仪器，分别采用了大气所牵头提出的CH14校正方案（Cheng et al.,2014）、GC20方案（Gouretski* and Cheng,2020）、GBC22方案（Gouretski*,Boyer and Cheng*,2022）、GRC24方案（Gouretski*,Roquet and Cheng*,2024）进行了偏差订正，这是目前国际上最完整地订正了仪器系统性偏差的数据集。3）IAPv4改进了大气所过去提出的基于动态样本的集合最优插值方法，对数据进行更准确的空间格点化重建，该格点化方法在以往国内、外的独立验证中均体现出显著的优势；4）IAPv4实现了在国产超算系统上的并行化快速构建，为国产超算系统对推动海洋科学研究，提升算力利用率提供了新的示例。

![image-20240831215825036](/Users/zqtzt/Library/Application Support/typora-user-images/image-20240831215825036.png)

​                                  图 1. IAP海洋温度数据集计算得到的全球海洋热含量时间序列

​	IAPv4揭示出了海洋温度和热含量变化的一系列新特性，例如，图1为自1955年以来的全球海洋热含量变化测算，结果显示：1）自1955年以来海洋变暖速率比以往认为更快，主要是因为订正了海洋历史数据中新发现的系统性偏差；2）2005年以来的海洋变暖速率也比以往认为更快，主要是因为新的数据质量控制方案能够在保留更多真实数据的前提下识别出更多的错误的观测数据；3）自1993年以来，2000米以下深海变暖趋势以往认为的更强，主要是因为以往的重构方法具有“保守性”的系统性误差。因此，新数据集为进一步理解海洋和地球系统能量储存、输送和热量在多圈层的交换过程和机理提供了更为准确的数据基础。

论文也对新的数据集进行了一系列分析和评估，发现IAPv4能够准确再现过去半世纪的海洋温度和热含量的气候平均态、年际变率（如厄尔尼诺-南方涛动）、年代际变化以及长期趋势。例如，IAPv4可以更好的闭合地球系统能量收支（图2a）。新的测算发现，由于全球变暖导致的1960-2023年期间地球系统的净能量摄入中，有90.8%储存在海洋中，其余9.2%用于加热大气、加热陆地、融化海冰/冰盖/冰川（Cheng et al. 2024b）。

​	此外，基于IAPv4数据集，论文重新测算了海洋热膨胀导致的比容海平面变化。全球海平面上升主要由海水质量增加和海洋热膨胀两个因素导致，论文结合海水质量变化的最新测算，利用IAPv4测算了海洋变暖膨胀的贡献，发现海洋变暖膨胀的贡献比以往研究更强，可以更好地闭合过去半世纪以来的全球海平面收支（图2b）。

IAPv4格点数据集面向全球公开共享，可以通过中国科学院大气物理研究所海洋和气候团队网站（[www.ocean.iap.ac.cn](http://www.ocean.iap.ac.cn/)） 以及中国科学院海洋科学数据中心网站（温度：https://doi.org/10.12157/IOCAS.20240117.002； 热含量：https://doi.org/10.12157/IOCAS.20240117.001）免费获取。欢迎大家下载使用。

​	经过质量控制和偏差订正后的全球海洋温度剖面观测数据集（CODC-v1；Zhang et al. 2024）也面向全球公开共享，可以通过中国科学院海洋科学数据中心网站（http://dx.doi.org/10.12157/IOCAS.20230525.001）以及大气所海洋和气候团队网站（[www.ocean.iap.ac.cn](http://www.ocean.iap.ac.cn/)）免费下载使用。值得一提的是：CODC-v1观测数据集主要数据来源为NOAA的“全球海洋数据库”（WOD），除此之外，还新增了通过文献检索、国内公开共享数据集、国际合作等方式获取的85,990条未被WOD收录的数据，均已融合到IAPv4数据集中。

​	论文第一作者和通讯作者为中国科学院大气物理研究所成里京。合作作者包括中国科学院大气物理研究所海洋与气候团队的潘玉莹、**谭哲韬**、郑化毅、朱雨静、魏旺栩、杜娟、叶罕霖、V. Gouretski、朱江；中国科学院计算机网络信息中心原惠峰；生态环境部珠江南海局监测与科研中心李冠城；中国科学院海洋研究所李元龙、张斌、靳雨春；崂山实验室林霄沛；中国科学院南海海洋研究所陈更新；美国圣托马斯大学J. Abraham；美国国家大气研究中心K. E. Trenberth；意大利国立地球物理与火山学研究所F. Reseghetti；美国宾夕法尼亚大学M. E. Mann。

​	该研究得到了国家自然科学基金（42122046,42076202,42206208,42261134536）、中国科学院战略重点研究项目（XDB42040402）、新基石科学基金会、达摩院青橙奖等项目的资助。本文的计算得到“东方”超级计算系统、国家重大科技基础设施 “地球系统数值模拟装置”的支持与帮助。