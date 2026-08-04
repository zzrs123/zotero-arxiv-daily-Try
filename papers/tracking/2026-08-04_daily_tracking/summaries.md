# Researcher Tracking - 2026-08-04 (daily)

Total new tracked papers: 3
Highlighted papers: 3

## 1. GABench: A Comprehensive Benchmark for Evaluating LLM Agents on Graph Analysis Tasks

- Authors: Jiarui Tan, Zhongjian Zhang, YaBo Guo, Jiawei Liu, Yujie Xing, Muhan Zhang, Cheng Yang, Chuan Shi
- Source hits: arxiv
- Matched researchers: Chuan Shi, Muhan Zhang
- Matched groups: N/A
- Confidence: medium (author_alias)
- Topic keywords: large language model, llm agent
- Journal/source: arxiv
- Publication date: 2026-08-03
- Article: http://arxiv.org/abs/2608.01684v1

Large language model (LLM) agents are increasingly capable of planning, using tools, and interacting with external environments. They are typically supported by harnesses, which manage state and coordinate multi-step execution. Graph analysis provides a promising setting for evaluating their agentic capabilities, because it requires agents to access data and execute operations in a graph environment. However, existing graph benchmarks for LLMs provide limited coverage of graph tasks and graph types, making it difficult to comprehensively evaluate LLM agents. Moreover, they typically formulate graph analysis as text-based question answering, where graph information is directly provided in the prompt, limiting the evaluation of end-to-end agentic capabilities. To address these limitations, we introduce GABench, a comprehensive benchmark for agentic graph analysis. GABench spans three graph types and covers four graph analysis task categories: graph retrieval, graph theory, graph machine learning, and graph open-ended question answering. GABench also provides 84 executable tools for accessing graph data and performing diverse graph operations. Building on these tools, we develop an agentic graph analysis task generation pipeline and construct 10,400 tasks with verifiable ground truth.Using GABench, we evaluate a range of frontier LLMs and agent harnesses. Our experiments reveal three key findings: (1) Existing LLM agents still struggle with complex graph analysis tasks. (2) Harness choice significantly affects performance, yet existing harnesses remain limited on complex graph tasks. (3) Graph analysis depends more on tool-call quality than quantity. Our findings provide practical insights into the development and evaluation of LLM agents for graph analysis.

## 2. Rewriting or Reweighting? A Geometric Account in Language Models

- Authors: Juntong Wang, Shengkun Yang, Xiyuan Wang, Muhan Zhang
- Source hits: arxiv
- Matched researchers: Muhan Zhang
- Matched groups: N/A
- Confidence: medium (author_alias)
- Topic keywords: N/A
- Journal/source: arxiv
- Publication date: 2026-08-03
- Article: http://arxiv.org/abs/2608.01835v1

Post-training can substantially alter language-model behavior, yet aggregate behavior rates do not reveal whether training removes an existing mechanism, creates a new one, or changes how an inherited mechanism is used. We study this question through two mechanistically distinct failures, repetition as a decoding-attractor pathology and sycophancy as a preference-related alignment failure. We introduce behavioral manifold analysis, which isolates behavior-specific geometry by selecting sparse behavior-associated coordinates and lifting them into low-dimensional local charts. We construct these charts in two complementary spaces. ACT captures runtime activation states, while NOC quantifies how strongly the model routes functional information flow through the shared behavior-associated subspace. Across multiple model families, the resulting charts are highly compressed and partially alignable across architectures. Contribution-space charts expose a more architecture-robust shared core, whereas activation-space charts retain stronger family-specific structure. Tracking these charts through controlled post-training reveals a consistent asymmetry. Supervised fine-tuning substantially alters the inherited behavioral geometry, whereas reward optimization changes behavior while largely preserving the underlying chart. This geometric perspective provides a unified framework for understanding the mechanistic distinction between the two objectives. SFT tends to rewrite behavioral geometry, whereas reward optimization primarily reweights it. Code is available at https://github.com/ronglingze/Manifold-Analysis

## 3. WAM-Diff2: Hierarchical AR-to-Diffusion Distillation for Highly Efficient Autonomous Driving VLA

- Authors: Zhihao Zhu, Hanlin Shang, Mingwang Xu, Feipeng Cai, Zhuolin He, Yaoyi Li, Jianhua Han, Hang Xu, Siyu Zhu
- Source hits: arxiv
- Matched researchers: Hang Xu
- Matched groups: N/A
- Confidence: medium (author_alias)
- Topic keywords: diffusion
- Journal/source: arxiv
- Publication date: 2026-08-02
- Article: http://arxiv.org/abs/2608.01035v1

Vision-Language-Action (VLA) models have emerged as a prominent paradigm for end-to-end autonomous driving; however, their efficient deployment is severely constrained by high computational latency and exposure bias arising from sequential autoregressive decoding. Conversely, while specialized diffusion policies enable low-latency, parallel execution, training them from scratch typically yields narrow, single-task architectures that lack holistic visual-linguistic reasoning. Successfully transforming pre-trained autoregressive generalists into parallel diffusion models could combine multi-task cognitive intelligence with execution efficiency, yet this transition presents a formidable architectural challenge due to mismatched attention patterns (causal versus bidirectional) and divergent optimization objectives. To bridge this divide, we introduce WAM-Diff2, a multi-task discrete diffusion VLA framework powered by a three-stage hierarchical distillation strategy. By structuring the architectural shift through progressive block-wise adaptation, block-wise distillation, and model-wise cross-scale distillation, WAM-Diff2 preserves the underlying semantic foundations of the base model while accelerating inference. Extensive evaluations across driving understanding, perception, and planning benchmarks demonstrate that WAM-Diff2 effectively mitigates exposure bias and achieves performance parity with autoregressive baselines. Crucially, the autoregressive-to-diffusion transition yields a 2.8x decoding speedup, which scales to an ultimate 15.1x acceleration when combined with system-level optimizations including FlashInfer and CUDA Graphs.
