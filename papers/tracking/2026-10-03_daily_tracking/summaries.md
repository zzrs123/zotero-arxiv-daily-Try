# Researcher Tracking - 2026-10-03 (daily)

Total new tracked papers: 3
Highlighted papers: 3

## 1. Higher-Order Molecular Grammars for Generative and Foundation Models in Chemistry

- Authors: Yiming Huang, Yujie Zeng, Vijay Prakash Dwivedi, Simone Foti, Jianmin Wang, Jure Leskovec, Tolga Birdal
- Source hits: arxiv
- Matched researchers: Jure Leskovec
- Matched groups: N/A
- Confidence: medium (author_alias)
- Topic keywords: foundation model
- Journal/source: arxiv
- Publication date: 2026-10-01
- Article: http://arxiv.org/abs/2610.02186v1

Molecular learning models are strongly shaped by their underlying representations. Yet standard sequential and graph formalisms struggle to explicitly encode higher-order topology, such as ring systems and recurring motifs. Existing higher-order representations can capture these structures directly, but they are often computationally demanding and difficult to decode into valid molecules. Here, we introduce Higher-order Grammar Representation (HGR), a principled, topology-aware framework that lifts molecules to combinatorial complexes and parses each complex into a compact sequence of production rules under a context-free higher-order grammar. By serialising higher-order topology into rule sequences, HGR makes these structures directly compatible with standard sequence models, avoiding the computational overhead of explicit higher-order encodings while preserving topological expressiveness. To reduce benchmark bias towards simple ring systems, we construct RingDiv, a ring-enriched benchmark containing 1.18 million molecules, including the curated RingDiv300k subset, and introduce the ring diversity index (RDI) to quantify ring-system coverage. In molecular generation, HGR-based models uniquely combine 100% validity by construction with leading distributional alignment, ranking first in FCD on all five generation benchmarks. In representation learning, HGR-FM achieves the highest mean AUC across seven MoleculeNet benchmarks under both transfer protocols, improving on the strongest baseline by 8.3 and 3.3 AUC points under probing and full fine-tuning, respectively. Collectively, these results establish HGR as an efficient higher-order representation for molecular generation and transferable representation learning.

## 2. VISTA: A Visual Harness for Reasoning in an Interactive World

- Authors: Qiushi Han, Keya Hu, Linlu Qiu, Cathy Wu, Kaiming He
- Source hits: arxiv
- Matched researchers: Kaiming He
- Matched groups: N/A
- Confidence: medium (author_alias)
- Topic keywords: N/A
- Journal/source: arxiv
- Publication date: 2026-10-01
- Article: http://arxiv.org/abs/2610.02200v1

We show that multimodal models possess strong reasoning abilities and that an appropriate harness can unlock their potential to solve tasks across diverse interactive environments. We introduce VISTA, a visual harness that gives a general-purpose multimodal model long-horizon vision. VISTA allows the model to directly perceive the environment through visual observations and maintains a lossless visual memory that preserves past observations in their original form. The model can actively retrieve these observations and reorganize its visual input as it reasons. On ARC-AGI-3, VISTA improves Claude Opus 5.0's Relative Human Action Efficiency score from 40.68 to a perfect 100.00, with the model completing all 25 public games using 57.4% fewer actions than first-time human participants. VISTA's simple design also allows it to extend naturally to diverse visual environments with minimal adaptation. Across three additional benchmarks covering a diverse range of visual games and puzzles, it substantially outperforms baselines using the same underlying model with minimal harnesses. Our results highlight VISTA's potential as a general-purpose visual harness for advancing multimodal agents in complex visual environments.

## 3. Which LLM to pick? Online Active Model Selection for Large Language Models

- Authors: Alessandro Turrin, Patrik Okanovic, Torsten Hoefler, Nezihe Merve Gürel
- Source hits: arxiv
- Matched researchers: Torsten Hoefler
- Matched groups: N/A
- Confidence: medium (author_alias)
- Topic keywords: large language model
- Journal/source: arxiv
- Publication date: 2026-10-01
- Article: http://arxiv.org/abs/2610.01592v1

Large Language Models (LLMs) are increasingly applied to process streaming data, with practitioners relying on benchmarks to select the best model even though these signals only approximate real performance. While oracle annotations can provide reliable feedback, they are often costly and difficult to obtain at scale. To address this challenge, we propose ONLINE LLM PICKER, the first framework for active model selection for LLMs in online settings. Given an arbitrary stream of queries and a limited annotation budget, ONLINE LLM PICKER selects the most informative prompts for annotation to identify the best LLM among candidate models. Across multiple tasks including 10 datasets, for over 130 language models, we show that ONLINE LLM PICKER saves annotation cost by up to 71.67% while reliably identifying the best or near-best model for the stream. We also show that using the returned model for sequential generation on unannotated prompts across the stream reduces regret by up to a factor of 2.51x, indicating that ONLINE LLM PICKER can identify the best or near-best model well before processing all streaming prompts.
