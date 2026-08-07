# Researcher Tracking - 2026-08-07 (daily)

Total new tracked papers: 2
Highlighted papers: 2

## 1. Multivariate Time Series Forecasting needs Cross Variable Loss

- Authors: Kuiye Ding, Yifan Hu, Hanchen Wang, Hao Xue
- Source hits: arxiv
- Matched researchers: Hanchen Wang
- Matched groups: N/A
- Confidence: medium (author_alias)
- Topic keywords: N/A
- Journal/source: arxiv
- Publication date: 2026-08-06
- Article: http://arxiv.org/abs/2608.05742v1

Multivariate time series forecasting presents unique challenges because future variables often co-evolve under shared system dynamics. While existing studies mainly focus on cross-variable dependencies in historical observations, dependencies among future values are much less explored. Specifically, modern forecasting models largely follow the Direct Forecasting (DF) paradigm, generating multi-step forecasts with point-wise objectives that do not explicitly constrain cross-variable structure. In this work, we show that the DF objective is mismatched in the presence of cross-variable and lagged dependencies, revealing an objective gap. To address this issue, we propose \textbf{C}ross-\textbf{V}ariable \textbf{Loss} (CvLoss), a plug-in structural regularizer that constrains forecast residuals on a cross-variable graph. CvLoss penalizes inconsistent edge-wise residual differences over forecast patches, encouraging consistency across both synchronous and asynchronous interactions. Our experiments show that CvLoss consistently improves competitive forecasting models, outperforms representative learning objectives, and is compatible with a variety of forecasting backbones.

## 2. BioM-JEPA: joint-embedding prediction of graph-connected gene blocks in single cells

- Authors: Yuhao Wang, Zelin Zang, Yuxuan Liu, Zhen Lei, Stan Z. Li
- Source hits: arxiv
- Matched researchers: Stan Z. Li
- Matched groups: N/A
- Confidence: medium (author_alias)
- Topic keywords: genetic perturbation, model, perturbation, representation learning, single cell, single-cell, single-cell-computation, single-cell-perturbation
- Journal/source: arxiv
- Publication date: 2026-08-06
- Article: http://arxiv.org/abs/2608.05928v1

Single-cell transcriptomes are sparse observations of coordinated biological programmes, yet most self-supervised models learn by reconstructing individual genes. Here we present BioM-JEPA, a joint-embedding predictive architecture that instead predicts aggregate representations of graph-connected gene blocks defined by protein-association and corpus-derived coexpression evidence. A student network infers each target-block representation from the remaining genes in a cell, while a slowly updated teacher supplies the corresponding target from the full observed gene set. Under the reported extraction procedure, block-level prediction produced embeddings with higher effective rank and weaker association with detected-gene depth in the tested diagnostics than token-prediction, random-block and reconstruction controls. Across CellBench tasks, frozen BioM-JEPA embeddings retained expression, pathway and neighbourhood information and achieved the lowest aggregate perturbation-response error among the evaluated models. Representation diagnostics were also consistent with canonical pancreatic programmes and compositional relationships between genetic perturbations. Linear attention avoids constructing a quadratic gene-by-gene attention matrix; in a matched one-epoch hPancreas experiment at batch size 8, BioM-JEPA provided 5.75-fold higher fine-tuning throughput and 3.76-fold higher held-out embedding throughput than scFoundation. Together, these results support graph-connected gene blocks as useful prediction units for JEPA-style representation learning in single-cell biology.
