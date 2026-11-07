# Researcher Tracking - 2026-11-07 (daily)

Total new tracked papers: 3
Highlighted papers: 3

## 1. WAM-Sim0.1: World Anchored Memory Meets Online RL for Consistent and Realistic Driving Simulation

- Authors: Jiahao Cui, Jiaye Li, Wenhao Zhang, Yaoyi Li, Shan Luan, Quanhui Tang, Jianhua Han, Lin Cheng, Hang Xu, Siyu Zhu
- Source hits: arxiv
- Matched researchers: Hang Xu
- Matched groups: N/A
- Confidence: medium (author_alias)
- Topic keywords: N/A
- Journal/source: arxiv
- Publication date: 2026-11-05
- Article: http://arxiv.org/abs/2611.07939v1

Autoregressive driving world models systematically suffer from structural drift, identity drift, and quality decay over long rollout horizons due to transient conditioning signals that lack persistent state. We present WAM-Sim, a driving world model anchored by a persistent hierarchical memory and optimized via online flow-matching RL. WAM-Sim structures persistent context across three temporal and semantic scales: pose-aligned structural tokens encoding persistent road topology, read-only scene tokens supplying geolocated background appearance, and write-once instance tokens preserving individual traffic participant identities across occlusions and chunk boundaries. To restore visual sharpness and physical plausibility degraded by multi-scale conditioning, we introduce an online post-training framework that optimizes self-generated rollouts via flow-matching RL guided by hierarchy-aligned visual rewards and a vision-language model physical judge. The invariant memory empirically confines policy optimization within the anchored context, helping suppress semantic collapse and reward hacking, while online RL systematically enforces physical commonsense and fine-grained visual fidelity. On the nuScenes benchmark, WAM-Sim achieves a superior generation fidelity (FID=3.47, FVD=25.72) and strong downstream perception performance (24.16 mAP, 71.23 road mIoU). On minute-scale rollouts of self-collected data, WAM-Sim substantially mitigates structural and identity drift, preserving high scene similarity and subject identity coherence across extended horizons. Project page: https://fudan-generative-vision.github.io/WAM-Sim.

## 2. Multimodal Information Interactions Bottleneck for Multimodal Self-Supervised Learning

- Authors: Liangjian Wen, Jiangtao Zheng, Jiang Duan, Qun Dai, Yong Dai, Jianzhuang Liu, Jun Wang, Shu-Dong Huang, Xinwang Liu, Zenglin Xu, Zhao Kang
- Source hits: arxiv
- Matched researchers: Xinwang Liu
- Matched groups: N/A
- Confidence: medium (author_alias)
- Topic keywords: N/A
- Journal/source: arxiv
- Publication date: 2026-11-05
- Article: http://arxiv.org/abs/2611.07718v1

Multimodal self-supervised learning is challenged by heterogeneity, unequal informativeness, and complex information interactions across multimodal data sources such as images, text, audio, and tabular data. While contrastive methods effectively align shared semantics, they typically rely on strong multi-view redundancy assumptions, overlooking modality-specific and synergistic information, thus leading to suboptimal representations. We propose the Multimodal Information Interactions Bottleneck (MIIB), a principled framework grounded in Partial Information Decomposition that explicitly encodes redundant, unique, and synergistic information within multimodal interactions. MIIB employs a dual-path model architecture for modality-specific encoding and multimodal fusion, optimized using surrogate tractable entropy-based objectives that enforce minimal sufficient representations without requiring explicit mutual information estimation. By leveraging variational bounds and score-based entropy estimation, MIIB efficiently captures complex cross-modal interactions while suppressing superfluous information. Experiments across diverse benchmarks demonstrate consistent improvements over state-of-the-art multimodal self-supervised methods. Code is available at https://github.com/wanglingzaishi/MIIB.

## 3. Towards Generalist Graph-Level Anomaly Detection

- Authors: Junjun Pan, Yixin Liu, Yu Zheng, Fuyi Li, Alan Wee-Chung Liew, Shirui Pan
- Source hits: arxiv
- Matched researchers: Yixin Liu
- Matched groups: N/A
- Confidence: medium (author_alias)
- Topic keywords: N/A
- Journal/source: arxiv
- Publication date: 2026-11-05
- Article: http://arxiv.org/abs/2611.07706v1

Graph-level anomaly detection (GLAD) aims to identify graphs that deviate significantly from the majority. While recent advances have achieved competitive performance, existing approaches mainly follow a dataset-specific paradigm, requiring substantial in-domain data and training cost when applied to new application scenarios. This limits their scalability and practicality in real-world applications where labeled data is scarce and diverse domains are continuously emerging. In this paper, we investigate the problem of generalist GLAD, which seeks to learn a single unified model capable of detecting anomalous graphs across multiple domains with minimal supervision on the target data. This problem introduces key challenges, including learning transferable patterns from heterogeneous graph datasets and effective adaptation under limited supervision. To address these challenges, we propose GenGLAD, a generalist GLAD approach that leverages discriminative subgraph extraction as the core mechanism to learn transferable anomaly knowledge and enable efficient adaptation to new domains. Specifically, GenGLAD employs a graph neural network-based discriminative subgraph extraction model to learn the anomaly-discriminative substructures that distinguish anomalous and normal graphs across diverse domains. During the test-time adaptation phase, multi-dimensional discrepancies between the extracted subgraph and multi-level contextual information are calculated to characterize anomalies from multiple perspectives. For efficient adaptation, a lightweight scoring module is introduced to automatically decide the most informative signals, improving robustness against misleading patterns. Extensive experiments on diverse benchmark datasets demonstrate that the proposed approach achieves strong performance, superior generalization ability, and improved data efficiency compared to existing methods.
