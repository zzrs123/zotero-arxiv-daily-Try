# Researcher Tracking - 2026-11-26 (daily)

Total new tracked papers: 3
Highlighted papers: 3

## 1. Spatial Transcriptomics Prediction from Histology via Topology-Informed Graph Attention and Gene-Semantics Conditioning

- Authors: Yuqi Cheng, Boshuai Zhang, Ziqi Zhang, Xiuwei Zhang
- Source hits: arxiv
- Matched researchers: Xiuwei Zhang, Ziqi Zhang
- Matched groups: N/A
- Confidence: medium (author_alias)
- Topic keywords: framework, inference, model, spatial transcriptomics, spatial-omics-computation
- Journal/source: arxiv
- Publication date: 2026-11-25
- Article: http://arxiv.org/abs/2611.33792v1

Spatial transcriptomics (ST) profiles gene expression with spatial context but remains costly, motivating models that infer expression from H&E images. Existing approaches face three key limitations: (i) a single patch embedding is often insufficient: morphologically similar regions can exhibit distinct expression due to spatial context, while naive neighborhood aggregation can over-smooth boundaries; (ii) conventional fixed, gene-indexed output heads treat genes independently and cannot directly support strict zero-shot prediction for unseen genes; and (iii) common metrics under-measure spatial pattern fidelity and boundary resolution. To address these challenges, we propose TIGEM, a topology-informed, gene-conditioned framework for histology-to-ST inference. TIGEM learns topology-aware spot representations by regularizing graph attention with tissue-level topology and morphology cues to avoid cross-compartment smoothing, and uses gene semantic modulation to replace gene-indexed heads, enabling zero-shot prediction for unseen genes. We also introduce Graph Spectral Correlation (GSC) to evaluate spatial pattern fidelity and boundary resolution complement to PCC/MSE. Across three large-scale ST datasets, TIGEM achieves overall state-of-the-art performance and significantly improved boundary prediction resolution, and further demonstrates the ability to predict expression patterns for genes unseen during training, extending prior zero-shot histology-to-ST efforts with topology-aware spatial propagation and PLM-based gene conditioning.

## 2. Agentic Reinforcement Learning with Immediate and Prospective Credit Assignment for Medical Visual Reasoning

- Authors: Yuqi Cheng, Rui Meng, Yijin Li, Chandra Sekhar Reddy Edula, Xiuwei Zhang
- Source hits: arxiv
- Matched researchers: Xiuwei Zhang
- Matched groups: N/A
- Confidence: medium (author_alias)
- Topic keywords: N/A
- Journal/source: arxiv
- Publication date: 2026-11-25
- Article: http://arxiv.org/abs/2611.33777v1

Medical visual question answering (VQA) requires acquiring useful evidence and deciding where to look next. Yet final-answer rewards do not reveal which observations support answering or guide subsequent inspection. We introduce MedPACT, an agentic reinforcement learning framework that learns selective observation policies through immediate answer support and prospective guidance. Our content-controlled estimator compares next actions induced by real and matched alternative observations under a shared real-observation history, isolating how observed content improves subsequent decisions. We combine both forms of credit within GRPO, assigning observation credit to the corresponding tool-call tokens alongside trajectory-level outcome supervision. MedPACT uses a single vision-language model and image-question-answer supervision, with credit estimation confined to training. Experiments with 4B and 8B backbones on six medical VQA benchmarks demonstrate improved accuracy, strong out-of-distribution generalization, and substantially lower inference costs. Case studies further illustrate how MedPACT avoids repeated observations and uses acquired evidence to guide subsequent inspection, demonstrating real-world practice potential.

## 3. CriticalScenes: Scalable Photorealistic Critical-Scenario Generation for Closed-Loop Driving Adaptation

- Authors: Alexandros Theocharous, Holger Caesar, Ziqi Zhang
- Source hits: arxiv
- Matched researchers: Ziqi Zhang
- Matched groups: N/A
- Confidence: medium (author_alias)
- Topic keywords: N/A
- Journal/source: arxiv
- Publication date: 2026-11-24
- Article: http://arxiv.org/abs/2611.33255v1

Safety-critical interactions are rare in recorded driving data, leaving end-to-end driving planners with limited exposure to evasive behaviour during training. This lack of critical supervision can lead to unsafe behaviour and, in rare instances, collisions. To address this gap, we introduce CriticalScenes, a reconstruction-based framework that transforms ordinary recorded driving scenes into photorealistic safety-critical interactions with corresponding collision-avoidance supervision. Across 53 reconstructed source scenes, 979 of 1,060 attempted interactions yield feasible threat trajectories (92.4\%), while the inserted threat actors remain detectable in more than 95\% of non-occluded observations within 5--35\,m. Experiments with two structurally different end-to-end planners show that the generated supervision improves critical-scenario planning, while closed-loop transfer varies across planner architectures. SparseDrive achieves a 46.5\% relative reduction in collision rate on an independent photorealistic closed-loop benchmark, whereas UniAD shows only a modest closed-loop improvement despite substantial open-loop gains. The results further highlight the importance of closed-loop evaluation, as improvements in open-loop trajectory prediction do not necessarily translate into equivalent safety gains.
