# Researcher Tracking - 2026-07-10 (daily)

Total new tracked papers: 4
Highlighted papers: 4

## 1. Learning social norms enhances compatibility in dynamic human-AI coordination

- Authors: Yi Yang, Siyuan Liu, Xin Gao, Huamu Sun, Chao Liu, Qing Zhou, Bingbing Nie
- Source hits: arxiv
- Matched researchers: Xin Gao
- Matched groups: N/A
- Confidence: medium (author_alias)
- Topic keywords: ai agent, large language model
- Journal/source: arxiv
- Publication date: 2026-07-08
- Article: http://arxiv.org/abs/2607.07021v1

Humans continuously coordinate with others in dynamic interactions, often through implicit, hard-to-quantify social norms that act as shared tacit expectations among interacting agents. As AI agents, including large language models (LLMs), become embedded in daily life, they increasingly participate in such interactions and reshape social interaction structures. Yet they often fail to coordinate with humans in an effective, considerate, and natural manner. We hypothesize that this gap arises because existing approaches align model behavior with human demonstrations without explicitly quantifying the underlying norms that generate such behavior. We selected pedestrian-vehicle interaction as a representative dynamic interaction and developed a simplified experimental platform that captures its key interactive features. From 3,456 dynamic human interactions collected via this platform, we identified three principles underlying human social norms: outcome predictability, value alignment, and advantage awareness. Incorporating these principles into AI agents significantly improves human-AI coordination. In the closed-loop interaction task with humans, the social-norm-informed LLM achieved a nearly fourfold higher total score than the baseline strategy and outperformed human-human interactions by 43%. These findings indicate that formalizing tacit social norms into explicit, quantifiable principles can enable AI agents to achieve mutually beneficial coordination in dynamic interactions, supporting their more natural integration into human society.

## 2. SpaCellAgent: A Self-Evolving LLM-Based Multi-Agent Framework for Trajectory Analysis

- Authors: Songhan Wang, Haoang Chi, He Li, Zhiheng Zhang, Jiayan Yuan, Cheems Wang, Hao Peng, Xinwang Liu, Wenjing Yang
- Source hits: arxiv
- Matched researchers: Xinwang Liu
- Matched groups: N/A
- Confidence: medium (author_alias)
- Topic keywords: algorithm, computational, framework, inference, large language model, method, model, single-cell, single-cell-computation
- Journal/source: arxiv
- Publication date: 2026-07-08
- Article: http://arxiv.org/abs/2607.07467v1

Spatial and Single-cell transcriptomics are transformative in deciphering cellular dynamics. As the fundamental paradigm for reconstructing cell developmental paths, trajectory inference (TI) is critical. However, existing methods require extensive manual intervention and proficiency in heterogeneous tools, posing a significant barrier to efficient TI analysis. To bridge this gap, we propose SpaCellAgent, an autonomous large language model (LLM) multi-agent framework that automates end-to-end spatiotemporal analysis and narrative generation. SpaCellAgent utilizes a multi-agent architecture for strategic workflow planning, a dynamic tool-orchestration engine for adaptive algorithm selection, and a self-evolution module that iteratively refines performance through feedback. We evaluate SpaCellAgent on six heterogeneous datasets encompassing complex temporal developmental trajectories, diverse sequencing platforms, and spatially-resolved tissue architectures. SpaCellAgent consistently demonstrates over 40\% improvement in analytical efficiency while maintaining expert-aligned performance. By converting natural language specifications into optimized analytical workflows and fully automating the pipeline, SpaCellAgent democratizes advanced spatiotemporal modeling and establishes a scalable, agent-driven paradigm for computational biology. The code and materials are available at https://github.com/LittleXH-shw/SpaCellAgent.

## 3. MMAgent-R$^2$: Learning to Rerank and Reject for Agentic mRAG

- Authors: Tao Zhang, Ziqi Zhang, Zongyang Ma, Yuxin Yang, Bing Li, Chunfeng Yuan, Kang Rong, Fengyun Rao, Jing Lyu, Weiming Hu
- Source hits: arxiv
- Matched researchers: Ziqi Zhang
- Matched groups: N/A
- Confidence: medium (author_alias)
- Topic keywords: N/A
- Journal/source: arxiv
- Publication date: 2026-07-08
- Article: http://arxiv.org/abs/2607.07383v1

Knowledge-based Visual Question Answering (KB-VQA) requires models to retrieve visual entities matching the query image from large-scale encyclopedic knowledge bases and answer related questions. Existing multimodal Retrieval Augmented Generation (mRAG) methods rely on global visual features to match candidate entities, yet when the knowledge base contains numerous visually similar entities, the retriever struggles to distinguish them, populating the candidate set with visually similar but factually mismatched distractors. Since subsequent processing steps such as noise filtering are also confined to this fixed candidate set, errors from failed retrieval inevitably propagate to the final answer. To address these challenges, we propose MMAgent-R$^2$, an agentic mRAG framework that integrates visual reranking and active rejection as its internal verification mechanism. Visual reranking directly compares query and candidate images, capturing discriminative details beyond textual descriptions to precisely identify the target entity among similar candidates; active rejection discards unreliable results and retrieves additional candidates when no confident match is found, moving beyond the fixed candidate pool. We design a composite reward function with step-level verification rewards and achieve joint optimization of external retrieval, internal verification, and answer generation via GRPO training. Experiments on InfoSeek, E-VQA, and MMhops demonstrate that \ours{} achieves state-of-the-art performance, with particularly notable advantages in challenging retrieval scenarios and complex multi-image multi-hop reasoning tasks.

## 4. UniRef-UAV: A Multimodal Benchmark for Universal Referring in UAV Imagery

- Authors: Haibin Tian, Huichao Xie, Xuelin Qian, Ruitao Lu, Junwei Han, Dingwen Zhang
- Source hits: arxiv
- Matched researchers: Junwei Han
- Matched groups: N/A
- Confidence: medium (author_alias)
- Topic keywords: N/A
- Journal/source: arxiv
- Publication date: 2026-07-09
- Article: http://arxiv.org/abs/2607.08267v1

Unmanned aerial vehicles (UAVs) increasingly rely on visual grounding capabilities to localize task-relevant targets from diverse instructions in complex aerial scenes. Existing referring expression comprehension (REC) benchmarks and methods, however, are largely built around text-only queries and single-object outputs, which limits their applicability to practical UAV scenarios involving reference images, multimodal instructions, absent targets, and multiple valid target instances. To address this gap, we introduce \emph{Universal Referring}, a generalized UAV referring task that jointly expands the query modality and the output cardinality. We construct \emph{UniRef-UAV}, a multimodal benchmark that supports text-only, image-only, and text+image queries with modality-dependent target cardinality, where text-only and text+image queries admit no-target, single-target, and multi-target grounding while image-only queries focus on existence-aware single-instance grounding. It also provides in-domain and cross-domain evaluation protocols for visual-query generalization. We further present \emph{UAV-URNet}, a detection-style baseline that maps heterogeneous queries into a shared query space and predicts variable-size target sets through set prediction. Extensive experiments show that UAV-URNet provides a stable and reproducible baseline with more consistent no-target discrimination and a more lightweight, reproducible implementation than large general-purpose MLLMs. Additional domain analysis, query-representation analysis, and ablation studies demonstrate that multimodal queries help reduce visual-query ambiguity and promote a more unified query--target alignment space. The annotations, visual query crops/images, train/validation/test splits, evaluation scripts, and baseline code will be made publicly available to facilitate reproducible research.
