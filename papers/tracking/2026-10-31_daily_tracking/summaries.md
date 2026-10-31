# Researcher Tracking - 2026-10-31 (daily)

Total new tracked papers: 1
Highlighted papers: 1

## 1. Learning Safe Flow Matching Robot Policies from Binary Feasibility Oracles

- Authors: Jianming Ma, Rongjun Jin, Yizhi Chen, Yue Gao
- Source hits: arxiv
- Matched researchers: Yue Gao
- Matched groups: N/A
- Confidence: medium (author_alias)
- Topic keywords: flow matching, foundation model
- Journal/source: arxiv
- Publication date: 2026-10-29
- Article: http://arxiv.org/abs/2610.40075v1

Robot foundation models increasingly rely on flow-based action generation for general-purpose manipulation, yet the generated actions are not guaranteed to satisfy physical constraints such as joint limits and collision avoidance. This problem is especially challenging when the feasible set cannot be described analytically and is accessible only through black-box feasibility oracles. We study this practical oracle-only setting and propose an oracle-guided differentiable safeguard for safe flow-matching robot policies. The safeguard uses binary feasibility queries to correct unsafe updates in the forward pass, while extracting local boundary information to provide constraint-aware learning signals in the backward pass. Combined with discrete-time flow matching, the same safeguard is used during training and inference, enabling forward--backward aligned policy learning without explicit or differentiable constraint models. Experiments on obstacle-aware robotic manipulation demonstrate 100% constraint satisfaction while preserving task performance.
