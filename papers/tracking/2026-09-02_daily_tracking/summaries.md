# Researcher Tracking - 2026-09-02 (daily)

Total new tracked papers: 2
Highlighted papers: 2

## 1. SPARK: Skeleton-Guided Reasoning Synthesis from Large-Scale Scientific Literature

- Authors: Yu Li, Wei Li, Xin Gao, Mengyuan Sun, Xiaoyang Wang, Qizhi Pei, Lijun Wu
- Source hits: arxiv
- Matched researchers: Xin Gao
- Matched groups: N/A
- Confidence: medium (author_alias)
- Topic keywords: N/A
- Journal/source: arxiv
- Publication date: 2026-08-31
- Article: http://arxiv.org/abs/2608.30214v1

Scientific reasoning remains challenging for open-source models, largely due to the lack of high-quality scientific reasoning data. Existing datasets are often dominated by factual recall or formulaic problem solving, with limited emphasis on mechanism understanding, evidence-grounded reasoning, and hypothesis evaluation. To address this, we introduce SPARK (Scientific Paper Abstracted Reasoning sKeleton), a paper-oriented synthesis framework built on Sci-Base, a large-scale corpus of research papers spanning 10 scientific disciplines. Instead of directly converting papers into question-answer pairs, SPARK treats the claim-evidence-derivation structure of a paper as the fundamental unit of reasoning synthesis. Specifically, SPARK (1) distills each paper into a compact reasoning skeleton capturing its central claims and supporting evidence, enabling self-contained question generation, and (2) synthesizes reasoning tasks from four scientific perspectives: mechanistic reasoning, hypothesis falsification, quantitative derivation, and boundary calibration. A final consistency verification stage further removes unsupported or contradictory outputs. Using this framework, we construct Spark-234K, a scientific reasoning dataset with substantially higher difficulty and diversity than existing resources. Experiments show that Spark-234K consistently outperforms existing scientific reasoning datasets while achieving stronger performance with significantly fewer training samples.

## 2. Certified Safety Radii in Forecast-Error Space for Wasserstein Distributionally Robust Small Signal Stability-Constrained AC Optimal Power Flow via Lifted Spectrahedral Containment

- Authors: Ziqi Zhang, Xi Chen
- Source hits: arxiv
- Matched researchers: Ziqi Zhang
- Matched groups: N/A
- Confidence: medium (author_alias)
- Topic keywords: N/A
- Journal/source: arxiv
- Publication date: 2026-08-31
- Article: http://arxiv.org/abs/2608.30201v1

Directly robustifying small-signal stability in AC optimal power flow is challenging since the stability boundary in the original uncertainty space is implicit, highly nonconvex, and changes with the operating decision. This paper exploits an alternative geometry. For a fixed model-specific stability certificate admitting suitable physical lifts, the small-signal stability requirement becomes an affine positive semidefinite constraint in the lifted variables, thereby defining a convex certified safe region. Instead of approximating the nonlinear instability boundary itself, we optimize a sample-wise safe radius in the original uncertainty space and certify, in the lifted space, that the entire power-flow image of the corresponding uncertainty ball is contained in the convex stability region. To this end, a componentwise Perron certificate guarantees existence, uniqueness, and Jacobian regularity of the target AC power-flow branch throughout each ball. An adjoint elimination then provides an exact affine-quadratic representation of the stability-relevant quantities, while rigorous matrix remainder bounds convert their nonlinear variation into finite robust PSD constraints. The resulting radii are certified lower bounds on the distances from empirical samples to failure and can therefore be coupled directly to the distance-based reformulation of a Wasserstein distributionally robust chance constraint, without directly approximating the instability boundary. Numerical studies demonstrate the effectiveness of the proposed framework.
