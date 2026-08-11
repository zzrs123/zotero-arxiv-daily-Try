# Researcher Tracking - 2026-08-11 (daily)

Total new tracked papers: 2
Highlighted papers: 2

## 1. Graphing the Everyday: A Neurosymbolic Approach to Eliciting Routines for Just-In-Time Adaptive Interventions

- Authors: Shakyani Jayasiriwardene, Blake Mountford, Meican Ma, Niels van Berkel, Nicholas Koemel, Matthew Ahmadi, Jorge Goncalves, Emmanuel Stamatakis, Zhanna Sarsenbayeva
- Source hits: arxiv
- Matched researchers: Jorge Goncalves
- Matched groups: N/A
- Confidence: medium (author_alias)
- Topic keywords: knowledge graph, large language model
- Journal/source: arxiv
- Publication date: 2026-08-10
- Article: http://arxiv.org/abs/2608.09294v1

Just-In-Time Adaptive Interventions (JITAIs) increasingly rely on conversational agents to elicit user routines, yet translating fluid human dialogue into rigid schedule data remains a significant challenge. We conducted a qualitative investigation of a neurosymbolic pipeline, combining Large Language Models (LLMs) with a Neo4j knowledge graph, to map unstructured verbal narratives into actionable interventions. Through human-centric evaluation using natural-language playbacks, we identified a critical "mental-model gap," where the linear extraction of LLMs clashes with hierarchical, non-linear human storytelling, causing severe entity fragmentation. Furthermore, we articulate an "ecological mismatch," demonstrating that algorithmic schedule availability frequently ignores the user's fluctuating psychological receptivity and physical energy levels. To resolve these tensions, we propose actionable design heuristics, including routine piggybacking, adaptive negotiation, and scalable transparency. Ultimately, these guidelines provide a foundational framework for evolving rigid schedule-trackers into empathetic, context-aware proactive agents capable of supporting long-term health behavior change.

## 2. DUET: A Diversity-Quality Duet of Distillation Experts for Two-Step Video Generation

- Authors: Zian Li, Litong Gong, Borui Liao, Pengfei Liu, Xinyu Wang, Xinyuan Wei, Yifan Gao, Tiezheng Ge, Muhan Zhang
- Source hits: arxiv
- Matched researchers: Muhan Zhang
- Matched groups: N/A
- Confidence: medium (author_alias)
- Topic keywords: diffusion
- Journal/source: arxiv
- Publication date: 2026-08-10
- Article: http://arxiv.org/abs/2608.09637v1

Diffusion models have enabled high-quality video generation in recent years, but the high cost of iterative sampling hinders their practical deployment. Few-step distillation alleviates this cost, yet exposes a quality--diversity trade-off between its two dominant paradigms: trajectory-level distillation (e.g., sCM) favors diversity, whereas distribution-level distillation (e.g., DMD) favors quality. Targeting extreme two-step video generation, we introduce DUET, which reconciles the two paradigms through a noise-level duet of experts: an sCM expert takes the high-noise step to lay out diverse structure, and a DMD expert takes the low-noise step to refine appearance detail. Since the two experts are trained independently with their native objectives, DUET sidesteps the optimization difficulties of loss-level combinations and delivers quality and diversity jointly rather than trading one for the other. We further identify the relay interface and the high-noise stage as the remaining bottlenecks, and address them with RL-guided expert adaptation, yielding DUET+. With the Wan2.1-T2V-1.3B backbone, DUET lifts the two-step quality of sCM close to the level of DMD while retaining nearly all of its structural diversity---about twice that of DMD---and DUET+ further improves overall quality while preserving this diversity advantage. Together, these results establish noise-level expert specialization as a simple, effective paradigm for reconciling diversity and quality in two-step video generation.
