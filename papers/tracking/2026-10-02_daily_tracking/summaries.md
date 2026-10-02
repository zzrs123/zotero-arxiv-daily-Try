# Researcher Tracking - 2026-10-02 (daily)

Total new tracked papers: 3
Highlighted papers: 3

## 1. Wavelet Flow Matching for Time Series

- Authors: Lucas Poinsignon, Jorge da Silva Gonçalves, Samuel Ruipérez-Campillo, Julia E. Vogt
- Source hits: arxiv
- Matched researchers: Jorge Goncalves
- Matched groups: N/A
- Confidence: medium (author_alias)
- Topic keywords: flow matching
- Journal/source: arxiv
- Publication date: 2026-09-30
- Article: http://arxiv.org/abs/2609.39374v1

Synthetic time series are increasingly used for data augmentation, privacy-preserving data sharing, and downstream model development, yet faithfully reproducing both multi-scale temporal structure and cross-channel dependencies remains challenging. We study multivariate time-series generation through flow matching in the wavelet domain. By operating on multilevel discrete wavelet coefficients rather than directly in the time domain, the model represents coarse structure and progressively finer details at separate scales. Their naturally different variances further induce an implicit coarse-to-fine generative process without requiring an explicit multi-scale schedule. Since the transform acts independently on each channel, we pair it with a channel-token transformer whose attention directly models cross-channel dependencies. Across seven benchmark datasets and four sequence lengths, our method is best or tied on a majority of dataset-metric combinations, with the largest and most consistent improvements in Context-FID and discriminative score.

## 2. EWAM: Emergent Depth-Wise Specialization in a Unified Embodied Model -- From Semantic Understanding through Visual Foresight to Action

- Authors: Hao Wang, Jiajun Wen, Jingzhi Liu, Shuoshuo Xue, Zhiliang Chen, Min Lin, Yicheng Chang, Xiaoyu Guo, Yukang Zhuo, Zheng Chong, Yunshuang Nie, Jian Zhang, Weijia Liufu, Qingman Wu, Heming Xu, Bingchang Song, Dantong Wu, Zhiyuan Wang, Hang Xu, Jianhua Han, Bokui Chen, Shen Zhao, Rui Li, Xiaodan Liang
- Source hits: arxiv
- Matched researchers: Hang Xu
- Matched groups: N/A
- Confidence: medium (author_alias)
- Topic keywords: N/A
- Journal/source: arxiv
- Publication date: 2026-09-30
- Article: http://arxiv.org/abs/2609.39973v1

Vision-language-action (VLA) policies emphasize semantic understanding, whereas world-action models (WAMs) learn predictive representations of environment dynamics. Systems that expose a policy to both sources often still concentrate action computation on a single expert. We present EWAM, an action-centric unified embodied model whose asymmetric joint attention lets action tokens read semantic, current-visual, predicted-future, and action information at every layer while the perceptual experts retain their distinct roles. Without layer-wise supervision, EWAM develops an emergent depth-wise specialization: action queries attend mainly to vision-language features in shallow layers, to predicted future frames in intermediate layers, and to action tokens themselves in deep layers. This handoff replicates across tasks and is stable across denoising steps. Checkpoint tracking and causal interventions show that it is learned and that action generation depends on it. EWAM is pretrained in two separate regimes, one on cross-embodiment robot trajectories and one on human egocentric video. In simulation and real-robot experiments, it surpasses existing VLA, WAM, and hybrid baselines. Human egocentric data improve both cross-embodiment transfer and real-robot robustness, and subtask-phase supervision improves long-horizon completion. Together, these results suggest that unified embodied learning can induce an ordered internal progression from semantic understanding, through visual foresight, to action formation.

## 3. Shared Weights, Selected Computations: How Looped Transformers Route What Each Loop Does

- Authors: Jiaju Wu, Yi Hu, Muhan Zhang
- Source hits: arxiv
- Matched researchers: Muhan Zhang
- Matched groups: N/A
- Confidence: medium (author_alias)
- Topic keywords: N/A
- Journal/source: arxiv
- Publication date: 2026-09-30
- Article: http://arxiv.org/abs/2609.39892v1

Looped Transformers repeatedly apply the same set of Transformer layers, giving them a recurrent architecture for latent computation. Their strong performance on iterative reasoning and length-generalization tasks suggests an appealing explanation: recurrence may provide an inductive bias that lets the model reuse a learned algorithm across loops. However, weight sharing alone does not imply that every loop performs the same operation. This raises a basic question: is each loop actually repeating the same computation, and if not, what routes the shared parameters to different operations?
  We study this question using graph walks as a test case. In the model's native trajectories, decoded predictions can advance by different numbers of graph steps or remain at a reached target, showing that recurrent progress need not follow a fixed one-loop-one-step pattern. We then show that a frozen loop can be steered toward different transitions by modifying its entering hidden state: a learned linear layer $J$ selects the desired transition without changing the shared Transformer layers.
  To test how this steering works, we use activation patching and find that attention patterns can recover its effects and switch the selected transition. Across five matched pairs of graph models, changing intermediate supervision during backbone training changes which transitions $J$ can induce. This suggests that $J$ selects computations learned by the backbone rather than creating new algorithms. Together, these results show that the hidden state can control shared computation, with attention routing as a causal pathway.
