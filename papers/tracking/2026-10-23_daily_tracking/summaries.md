# Researcher Tracking - 2026-10-23 (daily)

Total new tracked papers: 1
Highlighted papers: 1

## 1. Harnessing Language Models as Optimization Modeling Agents

- Authors: Yunxiang Luo, Xin Xu, Tianhao Chen, Zhixi Xiong, Peiqi Jiang, Fan Zhang, Wei Shao, Xuejian Gao, Yuwei Fan, Can Yang
- Source hits: arxiv
- Matched researchers: Can Yang
- Matched groups: N/A
- Confidence: medium (author_alias)
- Topic keywords: agentic workflow, large language model
- Journal/source: arxiv
- Publication date: 2026-10-22
- Article: http://arxiv.org/abs/2610.30917v1

Large language models (LLMs) can translate natural-language optimization problems into solver programs, but reliably producing correct formulations and implementations remains challenging. Existing approaches improve optimization modeling through agentic workflows or task-specific post-training. This raises a practical question: can a lightweight harness using a single model role achieve competitive performance without additional training? We introduce OPTICYCLE and OPTISTATE, two lightweight inference harnesses for optimization modeling, and evaluate them on nine benchmarks comprising 2,634 problems using 11 Qwen variants spanning 0.6B-27B parameters. Our results show that execution-guided revision consistently improves macro accuracy over direct generation for all evaluated models, with gains of up to 49.46 percentage points. Despite their simplicity, both harnesses outperform six adapted agentic workflows in same-model comparisons and four evaluated post-trained optimization models at comparable model sizes, without additional training. Explicit formulation state provides further but model-dependent improvements, suggesting that additional structure is not universally beneficial.
