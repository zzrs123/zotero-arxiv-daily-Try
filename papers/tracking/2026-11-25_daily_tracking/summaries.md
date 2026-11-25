# Researcher Tracking - 2026-11-25 (daily)

Total new tracked papers: 1
Highlighted papers: 1

## 1. DiffAnchor: Anchor-Space Diffusion for Monocular 3D Hand Pose Estimation

- Authors: Changlong Jiang, Youci Tang, Haohong Kuang, Hang Xu, Jinghong Zheng, Ran Wang, Zhenghong Yu, Chen Feng, Xiaofeng Yue, Yang Xiao
- Source hits: arxiv
- Matched researchers: Hang Xu
- Matched groups: N/A
- Confidence: medium (author_alias)
- Topic keywords: diffusion
- Journal/source: arxiv
- Publication date: 2026-11-24
- Article: http://arxiv.org/abs/2611.32513v1

Accurate and efficient monocular 3D hand pose estimation is an important perception capability for embodied human interaction and dexterous manipulation. Recent diffusion-based methods model pose uncertainty by iteratively denoising 3D joint coordinates. However, directly diffusing the final joints requires the generative process to simultaneously explore plausible poses and recover precise coordinates, often relying on additional denoising steps or multiple hypotheses and consequently increasing inference cost. In this work, we propose DiffAnchor, a few-step anchor-space diffusion framework that diffuses anchors rather than joints. Our key insight is that stochastic exploration does not need to operate directly on the final output. Instead, diffusion searches for informative intermediate anchors that serve as local 3D regressors, while anchor-to-joint offset prediction and weighted aggregation complete precise joint localization. Specifically, fixed context anchors provide stable global references, whereas noisy dynamic anchors are iteratively refined toward informative joint regions. An importance-guided anchor selection and replenishment mechanism further retains useful anchors, removes ineffective ones, and explores insufficiently covered regions. This design reduces the precision burden of the diffusion process and enables accurate prediction using only a few denoising steps and a single hypothesis. Extensive experiments on HO-3D V2, NYU, ICVL, and InterHand2.6M demonstrate state-of-the-art performance on the first three benchmarks and competitive performance on challenging interacting-hand estimation, while maintaining inference efficiency comparable to deterministic regression baselines.
