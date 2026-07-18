# Paper Daily Reading - 2026-07-18

## 1. SciCustom: A Framework for Custom Evaluation of Scientific Capabilities in Large Language Models

- Authors: Yiyang Gu, Junwei Yang, Junyu Luo, Ye Yuan, Bin Feng, Yingce Xia, Shufang Xie, Kaili Liu, Bohan Wu, Qi Shi, Haoran Li, Beier Xiao, Zhiping Xiao, Xiao Luo, Weizhi Zhang, Philip S. Yu, Zequn Liu, Ming Zhang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.895692924626967
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.2117/
- PDF: https://aclanthology.org/2026.acl-long.2117.pdf
- Local PDF: pdf/2026-07-18_01_SciCustom_ A Framework for Custom Evaluation of Scientific Capabilities in Large Language Models.pdf

Large language models (LLMs) are increasingly applied to scientific research, yet existing evaluations often fail to reflect the fine-grained capabilities required in practice. Most benchmarks are manually curated or domain-generic, limiting scalability and alignment with real scientific use cases. In this paper, we propose a new framework named SciCustom to address the problem. It enables the custom construction of benchmarks from large-scale scientific data to evaluate application-specific scientific capabilities in LLMs. SciCustom first organizes scientific knowledge into ontology-grounded knowledge units with controlled granularity and trains a tagger to map large-scale data instances into this knowledge space. Given a custom requirement, relevant knowledge units are identified via voting-based multi-model consensus. These units enable relevance-aware benchmark retrieval via binary search, followed by proxy subset selection and data-grounded benchmark generation for efficient evaluation. Experiments in chemistry and healthcare demonstrate that SciCustom reveals fine-grained differences in LLM scientific capabilities that standard benchmarks overlook, while requiring neither expert annotation nor synthetic question generation. This work provides a scalable and application-aware foundation for benchmarking scientific capabilities in LLMs.

## 2. ToolScope: An Agentic Framework for Vision-Guided and Long-Horizon Tool Use

- Authors: Mengjie Deng, Guanting Dong, Zhicheng Dou
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.895174136679766
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.11/
- PDF: https://aclanthology.org/2026.findings-acl.11.pdf
- Local PDF: pdf/2026-07-18_02_ToolScope_ An Agentic Framework for Vision-Guided and Long-Horizon Tool Use.pdf

Recently, large language models (LLMs) have demonstrated remarkable problem-solving capabilities by autonomously integrating with external tools for collaborative reasoning. However, due to the inherently complex and diverse nature of multimodal information, enabling multimodal large language models (MLLMs) to flexibly and efficiently utilize external tools during reasoning remains an underexplored challenge. In this work, we introduce ToolScope, an agentic framework designed to unify global planning with local multimodal perception, adopting a specialized Perceive tool to mitigates visual context degradation in long-horizon VQA task. ToolScope comprises three primary components: the Global Navigator, the Agentic Executor, and the Response Synthesizer. The Global Navigator functions as a "telescope”, offering high-level strategic guidance. The Agentic Executor operates iteratively to augment MLLM with local perception through the integration of external tools—Search, Code, and Perceive. Finally, the Response Synthesizer consolidates and organizes the reasoning process into a coherent, user-friendly output. We evaluate ToolScope on four VQA benchmarks across diverse domains, including VQA 2.0, ScienceQA, MAT-Search and MathVista. It demonstrates strong generalization capabilities, achieving an average performance improvement of up to +6.69% across all datasets. Our code is available at https://github.com/dengmengjie/ToolScope.

## 3. C 2 DLM: Causal Concept-Guided Diffusion Large Language Models

- Authors: Kairong Han, Nuanqiao Shan, Ziyu Zhao, Zijing Hu, Xinpeng Dong, Ye Jun Jian, Lujia Pan, Fei Wu, Kun Kuang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.8933480094426898
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.40/
- PDF: https://aclanthology.org/2026.findings-acl.40.pdf
- Local PDF: pdf/2026-07-18_03_C 2 DLM_ Causal Concept-Guided Diffusion Large Language Models.pdf

Autoregressive (AR) language models and Diffusion Language Models (DLMs) constitute the two principal paradigms of large language models. However, both paradigms suffer from insufficient reasoning capabilities. Human reasoning inherently relies on causal knowledge and thought, which are reflected in natural language. But in the AR paradigm, language is modeled as next token prediction (a strictly left-to-right, token-by-token order), whereas natural language itself exhibits more flexible causal structures. In the DLM paradigm, the attention mechanism is fully connected, which entirely disregards causal order. To fill this gap, we propose the Causal Concept-Guided Diffusion Language Model (C 2 DLM). Starting from DLM’s fully connected attention, C 2 DLM first obtains a concept-level causal graph from the teacher model, and then explicitly guides attention to learn causal relationships between concepts. By focusing on causal relationships and avoiding interference from difficult subgoals involving causal inversion, C 2 DLM achieves a 12% improvement and a 3.2× training speedup on the COT-OrderPerturb task, along with an average gain of 1.31% across six downstream reasoning tasks. Code and data are available here.

## 4. EvoNarrator: Modeling Scientific Evolution for Feasible Hypothesis Generation

- Authors: Xiaoying Le, Pengfei Qian, Yuanzhao Zhai, Xu Zhang, Qian Liu, Feng Dawei, Bo Ding
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.890300903334786
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.544/
- PDF: https://aclanthology.org/2026.acl-long.544.pdf
- Local PDF: pdf/2026-07-18_04_EvoNarrator_ Modeling Scientific Evolution for Feasible Hypothesis Generation.pdf

Scientific discovery evolution does not emerge in isolation but stems from the structural deepening and recombination of existing functionalities. However, current automated hypothesis generation methods, constrained by the statistical co-occurrence nature of Large Language Models (LLMs), lack perception of temporal causality and the "evolutionary patterns" inherent in scientific development. Consequently, they often yield superficial combinations that are logically infeasible. To address this, we propose EvoNarrator, a framework for hypothesis generation based on evolutionary narratives. We first extract structured P-M-L-F (Problem, Method, Limitation, Future Work) quadruples from citation networks. Subsequently, we introduce the SocketMatch mechanism, which eliminates logical disconnects between methods and problems by assessing their deep semantic compatibility. Finally, utilizing three macro patterns—Chain, Divergence, and Convergence—we constrain the generation process within historically logical derivation paths. Furthermore, double-blind expert reviews yielded an average score of 4.80/5.00 across novelty, feasibility, theoretical, and Logical. Additionally, hindcasting experiments validated its predictive foresight. Crucially, ablation studies indicate that integrating evolutionary patterns facilitates a paradigm shift from conservative incrementalism to theoretically grounded structural innovation. The code is available at https://github.com/xiyii-star/EvoNarrator.

## 5. Open Vision Reasoner: Transferring Linguistic Cognitive Behavior for Visual Reasoning

- Authors: Wei, Yana, Zhao, Liang, Sun, Jianjian, Lin, Kangheng, yin, jisheng, Hu, Jingcheng, Zhang, Yinmin, Yu, En, Lv, Haoran, Weng, Zejia, Wang, Jia, Han, Qi, Ge, Zheng, Zhang, Xiangyu, Jiang, Daxin, Patel, Vishal
- Source: neurips
- Venue type: conference
- Journal: NeurIPS 2025
- Publication status: formally_published
- Publication date: 2026-04-23
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.8896337508837098
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://proceedings.neurips.cc/paper_files/paper/2025/hash/06d86daa7001b7ea755ac4c80dc93497-Abstract-Conference.html
- PDF: https://proceedings.neurips.cc/paper_files/paper/2025/file/06d86daa7001b7ea755ac4c80dc93497-Paper-Conference.pdf
- Local PDF: pdf/2026-07-18_05_Open Vision Reasoner_ Transferring Linguistic Cognitive Behavior for Visual Reasoning.pdf

The remarkable reasoning capability of large language models (LLMs) stems from cognitive behaviors that emerge through reinforcement with verifiable rewards. This work investigates how to transfer this principle to Multimodal LLMs (MLLMs) to unlock advanced visual reasoning. We introduce a two-stage paradigm built on Qwen2.5-VL-7B: a massive linguistic cold-start fine-tuning, followed by multimodal reinforcement learning (RL) spanning nearly 1,000 steps—surpassing all previous open-source efforts in scale. This pioneering work reveals three fundamental insights: 1) Behavior transfer emerges surprisingly early in cold start due to linguistic mental imagery. 2) Cold start broadly memorizes visual behaviors, while RL critically discerns and scales up effective patterns. 3) Transfer strategically favors high-utility behaviors such as visual reflection. Our resulting model, Open-Vision-Reasoner (OVR), achieves state-of-the-art performance on a suite of reasoning benchmarks, including 95.3% on MATH500, 51.8% on MathVision and 54.6% on MathVerse. We release our model, data, and training dynamics to catalyze the development of more capable, behavior-aligned multimodal reasoners.

## 6. Diagnosing and Remedying Representation Deficiencies for Deterministic Reasoning in KGQA

- Authors: Gewen Liang, Mufan Xu, Kehai Chen, Wei Wang, Yuwei Wang, Muyun Yang, Tiejun Zhao, Min Zhang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.8891545678295665
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.2086/
- PDF: https://aclanthology.org/2026.acl-long.2086.pdf
- Local PDF: pdf/2026-07-18_06_Diagnosing and Remedying Representation Deficiencies for Deterministic Reasoning in KGQA.pdf

Large language models (LLMs) have demonstrated increasingly strong reasoning capabilities, achieving remarkable progress in knowledge graph question answering (KGQA). However, a key challenge in such systems is non-deterministic reasoning, where the model indecisively activates multiple semantically related knowledge graph edges for a given query, frequently leading to incorrect answers. To address this issue, we propose Diagnosing and Remedying Representation Deficiencies for Deterministic Reasoning in KGQA (DR2). DR2 identifies and localizes non-deterministic reasoning behaviors, uncovering the underlying semantic representation deficiencies in LLMs. Building on this diagnosis, we design abductive reasoning-based preference learning, which promotes fine-grained semantic discrimination and mitigates non-deterministic reasoning errors. Experimental results demonstrate that the proposed DR2 significantly outperforms several strong baselines, achieving state-of-the-art performance on the widely used WebQSP and CWQ benchmarks.

## 7. SARA: Selective and Adaptive Retrieval-augmented Generation with Context Compression

- Authors: Yiqiao Jin, Kartik Sharma, Vineeth Rakesh, Yingtong Dou, Menghai Pan, Mahashweta Das, Srijan Kumar
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.888555980934319
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.661/
- PDF: https://aclanthology.org/2026.acl-long.661.pdf
- Local PDF: pdf/2026-07-18_07_SARA_ Selective and Adaptive Retrieval-augmented Generation with Context Compression.pdf

Retrieval-augmented generation (RAG) extends large language models (LLMs) with external knowledge, but it must balance limited effective context, redundant retrieved evidence, and the loss of fine-grained facts under aggressive compression. Pure compression-based approaches reduce input size but often discard fine-grained details essential for factual accuracy. We propose SARA, a hybrid RAG framework that targets answer quality under fixed token budgets by combining natural-language snippets with semantic compression vectors. SARA retains a small set of passages in text form to preserve entities and numerical values, compresses the remaining evidence into interpretable vectors for broader coverage, and uses those vectors for iterative evidence reranking. Across 9 datasets and 5 open-source LLMs spanning 3 model families (Mistral, Llama, and Gemma), SARA consistently improves answer relevance (+17.71), answer correctness (+13.72), and semantic similarity (+15.53), demonstrating the importance of integrating textual and compressed representations for robust, context-efficient RAG.

## 8. KnowDR-REC: Auditing Knowledge-Conditioned Visual Grounding in Referring Expression Comprehension

- Authors: Guanghao Jin, Jingpei Wu, Tianpei Guo, Yiyi Niu, Weidong Zhou, Linyi Yang, Guoyang Liu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.887688364223815
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1923/
- PDF: https://aclanthology.org/2026.findings-acl.1923.pdf
- Local PDF: pdf/2026-07-18_08_KnowDR-REC_ Auditing Knowledge-Conditioned Visual Grounding in Referring Expression Comprehension.pdf

While Multimodal Large Language Models (MLLMs) have demonstrated the capacity for multi-modal reasoning, current Referring Expression Comprehension (REC) benchmarks lag behind, predominantly relying on intra-image cues and neglecting the integration of external world knowledge, which significantly impedes the evolution of REC towards real-world applications. This limitation obscures a model’s true capability to conduct textual reasoning (entity resolution), resolve spatial location (visual grounding), and verify reference validity (hallucination rejection). To address this, we introduce KnowDR-REC, a targeted audit benchmark comprising 1,042 positive triplets derived from real-world knowledge, along with rigorously matched negative samples. Unlike traditional datasets, we implement a controllable counterfactual evaluation mechanism that subjects textual expressions to single-factor perturbations (entity, relation, or time) to test sensitivity to fine-grained factual changes. Extensive evaluation of 18 state-of-the-art LMMs exposes a critical “binding hallucination,” revealing that current high performance is often built on fragile visual shortcuts rather than true understanding. KnowDR-REC thus serves as a pivotal diagnostic instrument, steering future research toward the genuine integration of perception and reasoning.

## 9. Verifiable Parameterization of Bayesian Networks from Scientific Literature: Unlocking Unstructured Empirical Evidence

- Authors: Jonas Gottal, Florian Matthes
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.8868185993863222
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.167/
- PDF: https://aclanthology.org/2026.findings-acl.167.pdf
- Local PDF: pdf/2026-07-18_09_Verifiable Parameterization of Bayesian Networks from Scientific Literature_ Unlocking Unstructured Empirical Evidence.pdf

Learning Bayesian Networks typically requires access to raw tabular data to estimate conditional probabilities. However, in many scientific domains, raw data is unavailable due to privacy concerns or general lack of access, while structured statistical summaries are increasingly accessible through large language models and published literature. We propose and evaluate five distinct strategies to reconstruct local conditional probability tables solely from statistical summaries in order to parameterize Bayesian Networks. Our comprehensive evaluation across mixed-type synthetic networks demonstrates that copula-based methods significantly outperform standard baselines, offering a viable path for knowledge integration from heterogeneous sources – unlocking the wealth of published knowledge for causal modeling while ensuring transparency and verifiability.

## 10. ToolPRM: Fine-Grained Inference Scaling of Structured Outputs for Function Calling

- Authors: Jianghao Lin, Yuanyuan Shi, Xin Peng, Renjie Ding, Hairui Wang, Yuxuan Peng, Bizhe Bai, Weixi Song, Fengshuo Bai, Huacan Chai, Weinan Zhang, Fei Huang, Ying Wen
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.886722903896569
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.855/
- PDF: https://aclanthology.org/2026.acl-long.855.pdf
- Local PDF: pdf/2026-07-18_10_ToolPRM_ Fine-Grained Inference Scaling of Structured Outputs for Function Calling.pdf

Large language models (LLMs) excel at function calling, but inference scaling has been explored mainly for unstructured generation. We propose an inference-scaling framework for structured outputs that combines fine-grained beam search with ToolPRM, a process reward model scoring each intra-call decision (function name and argument filling). We build the first fine-grained intra-call supervision dataset via function masking, rollout collection, and step-level annotation. ToolPRM outperforms outcome and coarse-grained reward models in predictive accuracy and yields consistent test-time gains on multiple function-calling benchmarks. We further show that structured generation follows “explore more but retain less”, since early JSON errors are unrecoverable.

## 11. HSGraphAgent: Knowledge-Graph-Guided Large Language Models for Harmonized System Code Classification

- Authors: Qiang Xia, Zijian Zhang, Ao Wang, Wenhan Wang, Xiangyu Wang, Jian Li
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.884894119562056
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.2072/
- PDF: https://aclanthology.org/2026.acl-long.2072.pdf
- Local PDF: pdf/2026-07-18_11_HSGraphAgent_ Knowledge-Graph-Guided Large Language Models for Harmonized System Code Classification.pdf

Harmonized System (HS) code classification is a hierarchically structured and regulation-constrained task, often complicated by short and noisy product descriptions. Misclassification can lead to tariff misapplication, regulatory violations, or delayed customs clearance, which in turn requires predictions to be both semantically appropriate and hierarchically valid. While large language models (LLMs) show strong semantic understanding, their unconstrained generation is poorly aligned with these requirements, often producing non-existent or hierarchically inconsistent codes. We propose HSGraphAgent a knowledge-graph-guided LLM framework that formulates HS classification as a stepwise, regulation-aware reasoning process over an explicit HS knowledge graph. By encoding hierarchical containment relations and regulatory exclusion rules, and enforcing them through a Select-Redirect mechanism, HSGraphAgent constrains inference to legally valid paths while producing explicit and traceable reasoning trajectories. Experiments on taxonomy-wide 4-digit and fine-grained 6-digit HS benchmarks demonstrate consistent improvements over direct generation and retrieval-augmented baselines, with particularly strong gains in fine-grained and regulation-sensitive classification settings.

## 12. Progressive Fine-Tuning for Cost-Effective Structured Attribute Generation in E-commerce

- Authors: Lakshman Kolasani, Fatemeh Taheri Dezaki
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.8844754430803654
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-industry.40/
- PDF: https://aclanthology.org/2026.acl-industry.40.pdf
- Local PDF: pdf/2026-07-18_12_Progressive Fine-Tuning for Cost-Effective Structured Attribute Generation in E-commerce.pdf

Large language models (LLMs) excel at structured information generation but face cost and latency challenges when deployed at scale in user-facing products. We present a parameter efficient supervised fine-tuning pipeline for adapting a small language model (SLM) to structured attribute generation in e-commerce product listing, enabling continuous model improvement with implicit user feedback without expensive manual annotation. Our approach involves completeness-deficit guided curation, which ranks samples by divergence between model predictions and catalog listing attributes, selecting the highest completeness gap examples for progressive fine-tuning. Our system is deployed on a large-scale product listing service, reducing inference costs by 98% and p90 latency by 70% using a fine-tuned SLM relative to the baseline LLM while preserving an 86.4% user acceptance rate, translating to significant monthly infrastructure savings.

## 13. RoadMapper: A Multi-Agent System for Roadmap Generation of Solving Complex Research Problems

- Authors: Jiacheng Liu, Zichen Tang, Zhongjun Yang, Xinyi Hu, Xueyuan Lin, Linwei Jia, Ruofei Bai, Rongjin Li, Shiyao Peng, Haocheng Gao, Haihong E
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.884141005439586
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.378/
- PDF: https://aclanthology.org/2026.findings-acl.378.pdf
- Local PDF: pdf/2026-07-18_13_RoadMapper_ A Multi-Agent System for Roadmap Generation of Solving Complex Research Problems.pdf

People commonly leverage structured content to accelerate knowledge acquisition and research problem solving. Among these, roadmaps guide researchers through hierarchical subtasks to solve complex research problems step by step. Despite progress in structured content generation, the roadmap generation task has remained unexplored. To bridge this gap, we introduce RoadMap, a novel benchmark designed to evaluate the ability of large language models (LLMs) to construct high-quality roadmaps for solving complex research problems. Based on this, we identify three limitations of LLMs: (1) lack of professional knowledge, (2) unreasonable task decomposition, and (3) disordered logical relationships. To address these challenges, we propose RoadMapper, an LLM-based multi-agent system that decomposes the research roadmap generation task into three key stages (i.e., initial generation, knowledge augmentation, and iterative "critique-revise-evaluate"). Extensive experiments demonstrate that RoadMapper can improve LLMs’ ability for roadmap generation, while enhancing average performance by more than 8% and saving 84% of the time required by human experts, highlighting its effectiveness and application potential.

## 14. Detecting Hallucinations in Retrieval-Augmented Generation via Semantic-level Internal Reasoning Graph

- Authors: Jianpeng Hu, Yanzeng Li, Jialun Zhong, Lei Zou, Wenfa Qi
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.884091151276879
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1385/
- PDF: https://aclanthology.org/2026.findings-acl.1385.pdf
- Local PDF: pdf/2026-07-18_14_Detecting Hallucinations in Retrieval-Augmented Generation via Semantic-level Internal Reasoning Graph.pdf

The Retrieval-augmented generation (RAG) system based on Large language model (LLM) has made significant progress. It can effectively reduce factuality hallucinations, but faithfulness hallucinations still exist. Previous methods for detecting faithfulness hallucinations either neglect to capture the models’ internal reasoning processes or handle those features coarsely, making it difficult for discriminators to learn. This paper proposes a semantic-level internal reasoning graph-based method for detecting faithfulness hallucination. Specifically, we first extend the layer-wise relevance propagation algorithm from the token level to the semantic level, constructing an internal reasoning graph based on attribution vectors. This provides a more faithful semantic-level representation of dependency. Furthermore, we design a general framework based on a small pre-trained language model to utilize the dependencies in LLM’s reasoning for training and hallucination detection, which can dynamically adjust the pass rate of correct samples through a threshold. Experimental results demonstrate that our method achieves better overall performance compared to state-of-the-art baselines on RAGTruth and Dolly-15k. Implementation available here: https://anonymous.4open.science/r/SIRG-1022.

## 15. Debate to Align: Reliable Entity Alignment through Two-Stage Multi-Agent Debate

- Authors: Cunda Wang, Ziying Ma, Po Hu, Weihua Wang, Feilong Bao
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.8840260214125646
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.297/
- PDF: https://aclanthology.org/2026.findings-acl.297.pdf
- Local PDF: pdf/2026-07-18_15_Debate to Align_ Reliable Entity Alignment through Two-Stage Multi-Agent Debate.pdf

Entity alignment (EA) aims to identify entities referring to the same real-world object across different knowledge graphs (KGs). Recent approaches based on large language models (LLMs) typically obtain entity embeddings through knowledge representation learning and use embedding similarity to identify an alignment-uncertain entity set. For each uncertain entity, a candidate entity set (CES) is then retrieved based on embedding similarity to support subsequent alignment reasoning and decision making. However, the reliability of the CES and the reasoning capability of LLMs critically affect the effectiveness of subsequent alignment decisions. To address this issue, we propose AgentEA, a reliable EA framework based on multi-agent debate. AgentEA first improves embedding quality through entity representation preference optimization, and then introduces a two-stage multi-role debate mechanism consisting of lightweight debate verification and deep debate alignment to progressively enhance the reliability of alignment decisions while enabling more efficient debate-based reasoning. Extensive experiments on public benchmarks under cross-lingual, sparse, large-scale, and heterogeneous settings demonstrate the effectiveness of AgentEA.

## 16. InteracSPARQL : An Interactive System for SPARQL Query Refinement Using Natural Language Explanations

- Authors: Xiangru Jian, Zhengyuan Dong, M. Tamer Özsu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.88353226577732
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1480/
- PDF: https://aclanthology.org/2026.findings-acl.1480.pdf
- Local PDF: pdf/2026-07-18_16_InteracSPARQL _ An Interactive System for SPARQL Query Refinement Using Natural Language Explanations.pdf

Current approaches for Natural Language to SPARQL (NL2SPARQL) generation primarily rely on one-turn, training-intensive models. While effective in specific settings, these models often lack generalizability and fail to provide transparency or mechanisms for error recovery in realistic scenarios. Additionally, prior interactive works are largely outdated and incompatible with modern large language model (LLM) workflows. In this paper, we introduce InteracSPARQL, a training-free interactive refinement pipeline that acts as a plug-and-play enhancement for existing SPARQL generation systems. Our approach integrates a set of efficient entity and property lookup tools within a self-correction loop, guided by a novel hybrid Natural Language Explanation (NLE) module. This module combines rule-based Abstract Syntax Tree (AST) parsing with LLM semantic enrichment to produce explanations that are both structurally accurate and linguistically fluent. We evaluate InteracSPARQL on standard benchmarks (QALD-9 and QALD-10), showing that our tool-augmented self-refinement significantly boosts the accuracy of base models without fine-tuning. Furthermore, human evaluation confirms that our structured explanations substantially improve user understanding and ability to correct queries compared to unstructured baselines.

## 17. Reasoning with Ontology Graph: Toward Type-Constrained Knowledge Graph Question Answering

- Authors: Yongxue Shan, Jie Peng, Zixuan Dong, Fei Hu, Xiaodong Wang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.882370437626048
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.489/
- PDF: https://aclanthology.org/2026.acl-long.489.pdf
- Local PDF: pdf/2026-07-18_17_Reasoning with Ontology Graph_ Toward Type-Constrained Knowledge Graph Question Answering.pdf

Large language models (LLMs) have recently advanced knowledge graph question answering (KGQA), but current methods tend to rely on LLM-induced type systems with inconsistent granularity, or perform multi-hop reasoning without explicit target-type constraints. We introduce OntGQA, a type-constrained KGQA framework that reasons over a relation-centric ontology graph, where each relation is labeled with its head and tail entity types to provide a stable schema backbone. Built on this graph, OntGQA adopts a planner–judge architecture with generative backoff: a type planner proposes plausible head–tail type pairs, a judge verifies retrieved candidates and their paths, and a generator is invoked only when all candidates are rejected. By constraining both endpoints of reasoning in type space, OntGQA achieves state-of-the-art performance and produces ontology-grounded reasoning chains, with substantial Hit@1 gains (87.7%→91.5% on WebQSP and 67.6%→74.6% on CWQ).

## 18. MedCPI: A Construct–Personalize–Integrate Framework for KG-enhanced Clinical Prediction

- Authors: Hang Wang, Hang Dong, Lu Liu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.8819426866964593
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1215/
- PDF: https://aclanthology.org/2026.findings-acl.1215.pdf
- Local PDF: pdf/2026-07-18_18_MedCPI_ A Construct–Personalize–Integrate Framework for KG-enhanced Clinical Prediction.pdf

Electronic health records (EHRs) provide longitudinal evidence for clinical prediction, but EHR data are sparse, incomplete, and heterogeneous, which can limit robustness. Medical knowledge graphs (MKGs) have therefore been incorporated to support KG-enhanced clinical prediction by linking heterogeneous EHR codes to shared medical concepts via structured relations. However, existing KG-enhanced approaches remain limited in two aspects: (i) task-specific knowledge selection when extracting knowledge from a large multi-source MKG; and (ii) patient-level personalization and knowledge integration, where personalization is often weakly controlled and knowledge integration is not sufficiently aligned with longitudinal patient trajectories. To address these issues, we propose MedCPI, a unified Construct–Personalize–Integrate framework. MedCPI first performs task-guided schema induction and KG normalization to build a task-specific Concept MKG as a denoised knowledge pool, then constructs controlled patient-level PKGs via local expansion and short path search, and finally integrates PKG representations with time-aware EHR representations via cross-attention for prediction. Experiments on MIMIC-III and MIMIC-IV across four clinical prediction tasks show consistent improvements over strong EHR-only and KG-enhanced baselines. Ablations and additional analyses further validate the contribution of each stage and illustrate how MedCPI utilizes structured medical knowledge.

## 19. Are Emotion and Rhetoric Neurons in LLM? Neuron Recognition and Adaptive Masking for Emotion-Rhetoric Prediction Steering

- Authors: Li Zheng, Xin Zhang, Shuyi He, Fei Li, Chong Teng, Jiang-Ming Yang, Donghong Ji, Zhuang Li
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.8815303755458013
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.193/
- PDF: https://aclanthology.org/2026.acl-long.193.pdf
- Local PDF: pdf/2026-07-18_19_Are Emotion and Rhetoric Neurons in LLM_ Neuron Recognition and Adaptive Masking for Emotion-Rhetoric Prediction Steerin.pdf

Accurate comprehension and controllable generation of emotion and rhetoric are pivotal for enhancing the reasoning capabilities of large language models (LLMs). Existing studies mostly rely on external optimizations, lacking in-depth exploration of internal representation mechanisms, thus failing to achieve fine-grained steering at the neuron level. A handful of works on neurons are confined to emotions, neglecting rhetoric neurons and their intrinsic connections. Traditional neuron masking also exhibits counterintuitive phenomena, making reliable verification of neuron functionality infeasible. To address these issues, we systematically investigate the neurons representation mechanisms and inherent associations of 6 emotion categories and 4 core rhetorical devices. We propose a neuron identification framework that integrates multi-dimensional screening, and design an adaptive masking method incorporating dynamic filtering, attenuation masking, and feedback optimization, enabling reliable functional validation of neuron functionality. Through neuron regulation, we achieve directed induction of non-target sentences and enhancement of emotion tasks via rhetoric neurons. Experiments on 5 commonly used datasets validate the effectiveness of our method, providing a novel paradigm for the fine-grained steering of emotion and rhetoric expressions in LLMs.

## 20. Discovering a Shared Logical Subspace: Steering LLM Logical Reasoning via Alignment of Natural-Language and Symbolic Views

- Authors: Feihao Fang, My T. Thai, Yuanyuan Lei
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.881489858592254
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1806/
- PDF: https://aclanthology.org/2026.acl-long.1806.pdf
- Local PDF: pdf/2026-07-18_20_Discovering a Shared Logical Subspace_ Steering LLM Logical Reasoning via Alignment of Natural-Language and Symbolic Vie.pdf

Large Language Models (LLMs) still struggle with multi-step logical reasoning. Existing approaches either purely refine the reasoning chain in natural language form or attach a symbolic solver as an external module. In this work, we instead ask whether LLMs contain a shared internal logical subspace that simultaneously aligns natural-language and symbolic-language views of the reasoning process. Our hypothesis is that this logical subspace captures logical reasoning capabilities in LLMs that are shared across views while remaining independent of surface forms. To verify this, we employ Canonical Correlation Analysis on the paired residual activations from natural-language and symbolic-language reasoning chains, learning a low-dimensional subspace with maximum cross-view correlation. Furthermore, we design a training-free approach that steers LLMs reasoning chain along this logical subspace, thereby leveraging the complementary reasoning signals from both views. Experiments on four logical reasoning benchmarks demonstrate the effectiveness of our approach, improving accuracy by up to 11 percentage points and generalizing well on out-of-domain problems.

## 21. The Mechanics of Interference: Defusing Distractors in RAG via Sparse Autoencoder Interventions

- Authors: Christian Giannetti, Giovanni Trappolini, Nicola Tonellotto, Fabrizio Silvestri, Pietro Lio
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.8814402126509897
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.583/
- PDF: https://aclanthology.org/2026.findings-acl.583.pdf
- Local PDF: pdf/2026-07-18_21_The Mechanics of Interference_ Defusing Distractors in RAG via Sparse Autoencoder Interventions.pdf

Large language models exhibit a critical vulnerability to distractor interference in retrieval-augmented contexts: they fail to prioritize relevant, factually correct documents over topically similar but misleading content. We introduce Lat-Defuse, a mechanistic framework that corrects this failure mode through targeted interventions in the model’s latent space. Using Sparse Autoencoders (SAEs), our method operates in an interpretable feature space and formulates correction as constrained counterfactual optimization. On Gemma-2 and Llama-3 model families across three QA benchmarks (BioASQ, Natural Questions, PopQA), our method achieves recovery rates of up to 94% on distractor-vulnerable samples. Successful correction through sparse modifications reveals distractor interference as a localized, systematically addressable phenomenon, opening directions toward universal distractor robustness in LLMs.

## 22. EDSD: Entropy-Driven Design for Faster Speculative Decoding

- Authors: Longkai Cheng, Ximing Wang, Jiangcai Zhu, Kailai Shao, Chao Chen, Haixiang Hu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.8811105146445852
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.2145/
- PDF: https://aclanthology.org/2026.acl-long.2145.pdf
- Local PDF: pdf/2026-07-18_22_EDSD_ Entropy-Driven Design for Faster Speculative Decoding.pdf

Speculative decoding has emerged as a promising paradigm for accelerating large language model inference by leveraging a lightweight draft model to generate multiple candidate tokens. However, existing methods often incur substantial training overhead to mitigate information misalignment between autoregressive draft model training and decoding. To address this challenge, we propose EDSD, an Entropy-Driven Speculative Decoding framework that uses entropy as a unified, interpretable signal for both draft model training and architectural design. EDSD drives the draft model to progressively align with the target model in an easy-to-hard manner while establishing token-level alignment as a dominant design principle. Extensive experiments on seven LLMs demonstrate that EDSD improves training efficiency by 24.8%, increases the average acceptance length by 4.0%, and achieves a 4.1% speedup compared to state-of-the-art methods. Furthermore, EDSD improves robustness to system prompt variations by more than 5x. Our findings establish entropy-driven alignment as an effective and principled foundation for efficient speculative decoding.

## 23. Attribution-Based Analysis and Optimization of Modular Agentic Workflows

- Authors: Yingxuan Yang, Bo Huang, Siyuan Qi, Chao Feng, Haoyi Hu, Yuxuan Zhu, Jinbo Hu, Haoran Zhao, Ziyi He, Xiao Liu, ZongYu Wang, Muning Wen, Lin Qiu, Xuezhi Cao, Xunliang Cai, Yong Yu, Weinan Zhang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.8807076423392015
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.359/
- PDF: https://aclanthology.org/2026.findings-acl.359.pdf
- Local PDF: pdf/2026-07-18_23_Attribution-Based Analysis and Optimization of Modular Agentic Workflows.pdf

Agentic workflows solve complex tasks by orchestrating modular components (e.g., planning, reasoning, action, reflection) built on top of LLM backbones. A practical but underexplored question is model allocation: given a fixed workflow decomposition and a pool of candidate LLMs, which components should be upgraded (and with which models) to upgrade task performance, and how can we attribute gains to individual upgrades and their interactions?We present ShapleyFlow, a cooperative game theoretic framework that models component upgrades as players and evaluates component coalitions to compute Shapley values. This yields interaction-aware attribution and supports Shapley-guided configuration recommendation for model allocation under a fixed workflow structure.We further introduce CapaBench, a benchmark of 1,500+ tasks across seven domains (shopping, navigation, ticketing, mathematics, operating systems, robotic coordination, and automated theorem proving).Across 9 representative LLMs and all 2 4 upgrade coalitions in a 4-component workflow, ShapleyFlow provides (i) principled, interaction-aware attribution for modular workflows and (ii) actionable model-allocation recommendations that improve over strong single-model baselines.

## 24. Locate, Steer, and Improve: A Practical Survey of Actionable Mechanistic Interpretability in Large Language Models

- Authors: Hengyuan Zhang, Zhihao Zhang, Ercong Nie, Mingyang Wang, Zunhai Su, Yiwei Wang, Qianli Wang, Shuzhou Yuan, Xufeng Duan, Qibo Xue, Zeping Yu, Chenming Shang, Xiao Liang, Jing Xiong, Hui Shen, Chaofan Tao, Zhengwu Liu, Senjie Jin, Zhiheng Xi, Dongdong Zhang, Sophia Ananiadou, Tao Gui, Ruobing Xie, Hayden Kwok-Hay So, Hinrich Schuetze, Xuanjing Huang, Qi Zhang, Ngai Wong
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.879820342379753
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.502/
- PDF: https://aclanthology.org/2026.findings-acl.502.pdf
- Local PDF: pdf/2026-07-18_24_Locate, Steer, and Improve_ A Practical Survey of Actionable Mechanistic Interpretability in Large Language Models.pdf

Mechanistic Interpretability (MI) has emerged as a vital approach to demystify the opaque decision-making of Large Language Models (LLMs). However, existing reviews primarily treat MI as an observational science, summarizing analytical insights while lacking a systematic framework for actionable intervention. To bridge this gap, we present a practical survey structured around the pipeline: "Locate, Steer, and Improve." We formally categorize Localizing (diagnosis) and Steering (intervention) methods based on specific Interpretable Objects to establish a rigorous intervention protocol. Furthermore, we demonstrate how this framework enables tangible improvements in Alignment, Capability, and Efficiency, effectively operationalizing MI as a practical engineering toolkit for model optimization. The curated paper list of this work is available at https://anonymous.4open.science/r/Act-MI-F068.

## 25. SCALE: Upscaled Continual Learning of Large Language Models

- Authors: Jin-woo Lee, Junhwa Choi, Bongkyu Hwang, Jinho Choo, Bogun Kim, Jeongseon Yi, Joonseok Lee, DongYoung Jung, Jaeseon Park, Kyoungwon Park, Suk-hoon Jung
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.8787198637842875
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.2037/
- PDF: https://aclanthology.org/2026.findings-acl.2037.pdf
- Local PDF: pdf/2026-07-18_25_SCALE_ Upscaled Continual Learning of Large Language Models.pdf

We revisit continual pre-training for large language models and argue that progress now depends less on scaling parameters than on scaling the right structure. We introduce SCALE, a width upscaling architecture that inserts lightweight expansions into linear modules while freezing all pre-trained parameters, preserving residual and attention topologies and increasing capacity without perturbing the base model’s original functionality. SCALE follows two principles: Persistent Preservation, which maintains the base model’s behavior via preservation-oriented initialization and freezing of the pre-trained weights, and Collaborative Adaptation, which trains only selected expansion components to acquire new knowledge with minimal interference. We instantiate these ideas as SCALE-Preserve (preservation-first), SCALE-Adapt (adaptation-first), and SCALE-Route, an optional routing extension that performs token-level routing between preservation and adaptation heads. On a controlled synthetic biography benchmark, SCALE reduces the severe forgetting seen in depth expansion while still learning new knowledge. In continual pre-training on a Korean corpus, SCALE variants forget less on English evaluations and achieve competitive gains on Korean benchmarks, yielding the best overall stability-plasticity trade-off. We further analyze when preservation holds provably and why combining preservation and adaptation stabilizes optimization relative to standard continual learning.

## 26. GROLE: Instance-Level Group Relative Optimization for LoRA Experts in Incremental Learning

- Authors: Yongyi Liao, Wencan Lai, Jun Fang, Jinjin Guo, Xiaohui Zhang, Zhiyuan Liu, Chao Liu, Pengzhang Liu, Qixia Jiang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.8779673284347185
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1952/
- PDF: https://aclanthology.org/2026.findings-acl.1952.pdf
- Local PDF: pdf/2026-07-18_26_GROLE_ Instance-Level Group Relative Optimization for LoRA Experts in Incremental Learning.pdf

While Large Language Models (LLMs) demonstrate remarkable zero-shot generalization, adapting them to downstream tasks or shifting data distributions often requires continual fine-tuning—a process prone to catastrophic forgetting and limited knowledge transfer. This challenge is especially pronounced in online Incremental Learning (IL) settings, where task boundaries are blurred, and data arrives in a non-stationary stream. To address these issues, we propose GROLE (Group Relative Optimization for LoRA Experts), a novel approach that incrementally constructs a pool of frozen, task-specific Low-Rank Adaptation (LoRA) experts. At its core, GROLE employs a lightweight, instance-level expert selector optimized through a group relative reinforcement learning objective, which dynamically combines relevant experts to maximize adaptability without compromising stability. Extensive experiments across diverse incremental learning benchmarks show that GROLE consistently outperforms state-of-the-art methods, particularly in task-free and blurred-boundary settings, achieving an optimal balance between plasticity and robustness.

## 27. Moneyball with LLMs: Analyzing Tabular Summarization in Sports Narratives

- Authors: Ritam Upadhyay, Naman Ahuja, Rishabh Baral, Aparna Garimella, Vivek Gupta
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.877660937844863
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.2072/
- PDF: https://aclanthology.org/2026.findings-acl.2072.pdf
- Local PDF: pdf/2026-07-18_27_Moneyball with LLMs_ Analyzing Tabular Summarization in Sports Narratives.pdf

Large language model (LLM) approaches to tabular summarization rely on extensive prompt engineering, decomposition pipelines, or entity-level intermediate representations to achieve strong performance. While effective, these strategies are computationally expensive and offer limited insight into how well models maintain state over long, evolving narratives. We introduce SporTabSet, a diagnostic benchmark for long-context tabular summarization across two complementary sports domains that require tracking multiple entities and aggregating statistics under domain-specific rules. Using SporTabSet, we systematically evaluate decomposition-based strategies across several long context LLMs. Results show that although decomposition substantially improves accuracy and numerical fidelity, gains stem mainly from dissecting multi-entity interference rather than improved local arithmetic. Robustness experiments further reveal high sensitivity to surface-level cues with structured failures, including hallucination, omission, and role confusion. Together, these findings identify consistent multi-entity memory as a key bottleneck in long-context table generation, motivating diagnostic evaluation as a prerequisite for scalable, efficient, and reliable tabular summarization models.

## 28. Vision-Language Introspection: Mitigating Overconfident Hallucinations in MLLMs via Interpretable Bi-Causal Steering

- Authors: Shuliang Liu, Songbo Yang, Dong Fang, Sihang Jia, Yuqi Tang, Lingfeng Su, Ruoshui Peng, Yibo Yan, Xin Zou, Xuming Hu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.8775866374808157
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1784/
- PDF: https://aclanthology.org/2026.acl-long.1784.pdf
- Local PDF: pdf/2026-07-18_28_Vision-Language Introspection_ Mitigating Overconfident Hallucinations in MLLMs via Interpretable Bi-Causal Steering.pdf

Object hallucination critically undermines the reliability of Multimodal Large Language Models (MLLMs), often stemming from a fundamental failure in cognitive introspection—where models blindly trust linguistic priors over specific visual evidence. Existing mitigations remain limited: contrastive decoding approaches operate superficially without rectifying internal semantic misalignments, while current latent steering methods rely on static vectors that lack instance-specific precision. We introduce Vision-Language Introspection (VLI), a training-free inference framework that simulates a metacognitive self-correction process. VLI first performs Attributive Introspection to diagnose hallucination risks via probabilistic conflict detection and localize the causal visual anchors. It then employs Interpretable Bi-Causal Steering to actively modulate the inference process, dynamically isolating visual evidence from background noise while neutralizing blind confidence through adaptive calibration. VLI achieves state-of-the-art performance on advanced models, reducing object hallucination rates by 12.67% on MMHal-Bench and improving accuracy by 5.8% on POPE.

## 29. Render-of-Thought: Rendering Textual Chain-of-Thought as Images for Visual Latent Reasoning

- Authors: Yifan Wang, Shiyu Li, Peiming Li, Xiaochen Yang, Zheng Wei, Yang Tang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.877223353656715
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.2097/
- PDF: https://aclanthology.org/2026.acl-long.2097.pdf
- Local PDF: pdf/2026-07-18_29_Render-of-Thought_ Rendering Textual Chain-of-Thought as Images for Visual Latent Reasoning.pdf

Chain-of-Thought (CoT) prompting has achieved remarkable success in unlocking the reasoning capabilities of Large Language Models (LLMs). Although CoT prompting enhances reasoning, its verbosity imposes substantial computational overhead. Recent works often focus exclusively on outcome alignment and lack supervision on the intermediate reasoning process. These deficiencies obscure the analyzability of the latent reasoning chain. To address these challenges, we introduce **Render-of-Thought (RoT)**, the first framework to reify the reasoning chain by rendering textual steps into images, making the latent rationale explicit and traceable. Specifically, we leverage the vision encoders of existing Vision Language Models (VLMs) as semantic anchors to align the vision embeddings with the textual space. This design ensures **plug-and-play** implementation without incurring additional pre-training overhead. Extensive experiments on mathematical and logical reasoning benchmarks demonstrate that our method achieves 3-4 × token compression and substantial inference acceleration compared to explicit CoT. Furthermore, it demonstrates a competitive efficiency-accuracy Pareto exploration compared to other methods, validating the feasibility of this paradigm. Our code is available at https://github.com/TencentBAC/RoT

## 30. PDR: A Plug-and-Play Positional Decay Framework for LLM Pre-training Data Detection

- Authors: Jinhan Liu, Yibo Yang, Ruiying Lu, Piotr Piękos, Yimeng Chen, Peng Wang, Dandan Guo
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.876164868035854
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.562/
- PDF: https://aclanthology.org/2026.acl-long.562.pdf
- Local PDF: pdf/2026-07-18_30_PDR_ A Plug-and-Play Positional Decay Framework for LLM Pre-training Data Detection.pdf

Detecting pre-training data in Large Language Models (LLMs) is crucial for auditing data privacy and copyright compliance, yet it remains challenging in black-box, zero-shot settings where computational resources and training data are scarce. While existing likelihood-based methods have shown promise, they typically aggregate token-level scores using uniform weights, thereby neglecting the inherent information-theoretic dynamics of autoregressive generation. In this paper, we hypothesize and empirically validate that memorization signals are heavily skewed towards the high-entropy initial tokens, where model uncertainty is highest, and decay as context accumulates. To leverage this linguistic property, we introduce Positional Decay Reweighting (PDR), a training-free and plug-and-play framework. PDR explicitly reweights token-level scores to amplify distinct signals from early positions while suppressing noise from later ones. Extensive experiments show that PDR acts as a robust prior and can usually enhance a wide range of advanced methods across multiple benchmarks.
