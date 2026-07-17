# Researcher Tracking - 2026-07-17 (daily)

Total new tracked papers: 1
Highlighted papers: 1

## 1. Information-Theoretic Adaptive Cooling for Deterministic MPPI via Entropy Feedback

- Authors: Shuqi Wang, Wenrong Sun, Tao Han, Yue Gao, Xiang Yin
- Source hits: arxiv
- Matched researchers: Yue Gao
- Matched groups: N/A
- Confidence: medium (author_alias)
- Topic keywords: N/A
- Journal/source: arxiv
- Publication date: 2026-07-15
- Article: http://arxiv.org/abs/2607.14245v1

This paper investigates deterministic optimal control using Model Predictive Path Integral (MPPI) control, a sampling-based and derivative-free framework well suited for systems with complex dynamics and nonsmooth objectives. In deterministic MPPI, the temperature must be driven to zero to recover the true optimum, yet the design of an effective cooling schedule remains a fundamental challenge. Existing methods typically rely on predefined open-loop schedules, which limit the efficiency and robustness of the algorithm. To overcome this limitation, we propose an Information-Theoretic Adaptive Cooling (ITAC) framework that uses the Shannon entropy of the importance weights as an online feedback signal to regulate the temperature. The proposed mechanism adapts the cooling rate to the current sampling state, enabling fast progress when the weights are diffuse and cautious cooling when they become concentrated. We prove asymptotic convergence of the resulting scheme to the deterministic optimum, and further derive a critical entropy threshold that leads to a smooth barrier against premature weight collapse. Experiments on nonsmooth signal temporal logic motion-planning tasks show that ITAC improves sampling efficiency and achieves substantially faster convergence than state-of-the-art baselines without sacrificing the derivative-free nature of MPPI.
