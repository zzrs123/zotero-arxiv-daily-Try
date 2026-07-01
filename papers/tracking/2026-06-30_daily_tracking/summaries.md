# Researcher Tracking - 2026-06-30 (daily)

Total new tracked papers: 2
Highlighted papers: 2

## 1. ActiveVital: Geometry-Aware Embodied Vital Signs Monitoring for Home Healthcare Robots

- Authors: Yuxuan Hu, Shihao Li, Yang Xiao, Gen Li, Feng Xu, Jianfei Yang
- Source hits: arxiv
- Matched researchers: Yuxuan Hu
- Matched groups: N/A
- Confidence: medium (author_alias)
- Topic keywords: N/A
- Journal/source: arxiv
- Publication date: 2026-06-29
- Article: http://arxiv.org/abs/2606.30275v1

Home robots require reliable vital signs monitoring to support long-term companionship and safety in daily environments, yet obtaining respiration and heart rate without physical contact remains challenging in unconstrained home settings. Millimeter-wave (mmWave) radar offers a promising solution due to its phase sensitivity to sub-millimeter motions. However, mmWave measurements are fundamentally constrained by observation geometry, since only the radial component of motion is observable. Consequently, arbitrary robot-human orientations often introduce angular misalignment that destabilizes vital signs estimation. To address this limitation, we reformulate vital signs monitoring from passive signal recovery to active geometric regulation. We propose ActiveVital, a vision-guided sensing framework that treats sensing geometry as an explicit control variable for robots. It localizes the chest anchor via visual keypoints and converts alignment errors into control commands. This steers the robot-mounted radar toward near-normal incidence to the thoracic surface, maximizing radial observability within a perception-action loop. A differential phase enhancement module further stabilizes signal extraction under motion. Experiments show that ActiveVital reduces respiration interval error from 0.87 s to 0.14 s and heart rate error from 13.59 bpm to 2.22 bpm, achieving accuracy comparable to controlled static sensing while remaining robust under unconstrained robot-human configurations.

## 2. Algebraic Subgraph Counting

- Authors: Qiuyu Guo, Jianye Yang, Wenjie Zhang, Hanchen Wang, Ying Zhang, Xuemin Lin
- Source hits: arxiv
- Matched researchers: Hanchen Wang
- Matched groups: N/A
- Confidence: medium (author_alias)
- Topic keywords: N/A
- Journal/source: arxiv
- Publication date: 2026-06-28
- Article: http://arxiv.org/abs/2606.29128v1

Subgraph isomorphism counting is a fundamental problem in graph analytics, which aims to find the number of subgraph isomorphisms of a query graph in a data graph. The candidate tree-based framework provides a promising foundation for subgraph counting tasks, offering a unified counting paradigm that can be extended beyond tree patterns. However, supporting subgraph isomorphism within this framework remains challenging, as it requires handling both the non-tree edge constraint and the injective mapping constraint. Although existing solutions employ sampling or learning techniques to address these constraints in this framework, they still either suffer from inherent sampling failures or rely heavily on supervision. In this paper, we propose ASC, an algebraic subgraph counting approach built on the candidate tree-based counting framework. In our method, the non-tree edge constraint is directly incorporated into the candidate tree-based counting process through a matrix-based computation method, enabling subgraph homomorphism counting with high accuracy in polynomial time. Based on the resulting subgraph homomorphism count, we further apply a local sampling method to address the injective mapping constraint, thereby obtaining the final subgraph isomorphism count. Extensive experiments show that ASC can achieve substantially better and more stable performance over the baselines across various datasets, while scaling to billion-edge graphs. Most impressively, as a non-learning method, ASC can even achieve more than an order of magnitude higher average accuracy than the state-of-the-art learning-based method FlowSC with similar efficiency. This paper is the full version of the work accepted at SIGMOD 2027. The code is available at https://github.com/EricaGuoQiuyu/AlgebraicSubgraphCounting.
