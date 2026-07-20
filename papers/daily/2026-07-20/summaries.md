# Paper Daily Reading - 2026-07-20

## 1. End-to-End Optimization of LLM-Driven Multi-Agent Search Systems via Heterogeneous-Group-Based Reinforcement Learning

- Authors: Guanzhong Chen, Shaoxiong Yang, Chao Li, Wei Liu, Jian Luan, Zenglin Xu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.8904354840123037
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1399/
- PDF: https://aclanthology.org/2026.acl-long.1399.pdf
- Local PDF: pdf/2026-07-20_01_End-to-End Optimization of LLM-Driven Multi-Agent Search Systems via Heterogeneous-Group-Based Reinforcement Learning.pdf

Large language models (LLMs) are versatile, yet their deployment in complex real-world settings is limited by static knowledge cutoffs and the difficulty of producing controllable behavior within a single inference. Multi-agent search systems (MASS), which coordinate specialized LLM agents equipped with search tools, mitigate these issues via task decomposition and retrieval-augmented problem solving. However, optimizing LLMs for agent-specific roles remains labor-intensive with prompt engineering or supervised fine-tuning, motivating automated end-to-end training. Existing multi-agent reinforcement learning (MARL) methods such as Multi-Agent Proximal Policy Optimization (MAPPO) typically depend on large critic networks to evaluate joint actions, leading to instability and high memory costs. We introduce Multi-Agent Heterogeneous Group Policy Optimization (MHGPO), which updates policies by estimating relative advantages across heterogeneous groups of multi-agent rollouts, shifting the optimization focus from local agent performance to global system success. We further study three group rollout sampling strategies to trade off sample efficiency and optimization quality. Experiments show that MHGPO captures implicit inter-agent dependencies and consistently outperforms strong baselines in both task performance and computational efficiency.

## 2. ToolOmni: Enabling Open-World Tool Use via Agentic learning with Proactive Retrieval and Grounded Execution

- Authors: Shouzheng Huang, Meishan Zhang, Baotian Hu, Min Zhang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.8898189558384897
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1736/
- PDF: https://aclanthology.org/2026.acl-long.1736.pdf
- Local PDF: pdf/2026-07-20_02_ToolOmni_ Enabling Open-World Tool Use via Agentic learning with Proactive Retrieval and Grounded Execution.pdf

Large Language Models (LLMs) enhance their problem-solving capability by utilizing external tools. However, in open-world scenarios with massive and evolving tool repositories, existing methods relying on static embedding retrieval or parameter memorization of tools struggle to align user intent with tool semantics or generalize to unseen tools, respectively, leading to suboptimal accuracy of open-world tool retrieval and execution. To address these, we present ToolOmni, a unified agentic framework that enables LLMs for open-world tool use by proactive retrieval and grounded execution within a reasoning loop. First, we construct a cold-start multi-turn interaction dataset to instill foundational agentic capabilities via Supervised Fine-Tuning (SFT). Then, we introduce open-world tool learning based on a Decoupled Multi-Objective GRPO algorithm, which simultaneously optimizes LLMs for both tool retrieval accuracy and execution efficacy in online environments. Extensive experiments demonstrate that ToolOmni achieves state-of-the-art performance both in retrieval and execution, surpassing strong baselines by a significant margin of +10.8% in end-to-end execution success rate, while exhibiting exceptional robustness and generalization capabilities.

## 3. From Query to Logic: Ontology-Driven Multi-Hop Reasoning in LLMs

- Authors: Haonan Bian, Yutao Qi, Rui Yang, Yuanxi Che, Jiaqian Wang, Heming Xia, Ranran Zhen
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.886894578120348
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.687/
- PDF: https://aclanthology.org/2026.findings-acl.687.pdf
- Local PDF: pdf/2026-07-20_03_From Query to Logic_ Ontology-Driven Multi-Hop Reasoning in LLMs.pdf

Large Language Models (LLMs), despite their success in question answering, exhibit limitations in complex multi-hop question answering (MQA) tasks that necessitate non-linear, structured reasoning. This limitation stems from their inability to adequately capture deep conceptual relationships between entities. To overcome this challenge, we present ORACLE (Ontology-driven Reasoning And Chain for Logical Elucidation), a training-free framework that combines LLMs’ generative capabilities with the structural benefits of knowledge graphs. Our approach operates through three stages: (1) dynamic construction of question-specific knowledge ontologies using LLMs, (2) transformation of these ontologies into First-Order Logic (FOL) reasoning chains, and (3) systematic decomposition of the original query into logically coherent sub-questions. Extensive experiments across a diverse set of models and standard MQA benchmarks demonstrate that our framework achieves competitive performance while producing more interpretable reasoning chains.

## 4. SharVeT: Similarity-aware Parameter Sharing with Vector-based Tuning for Efficient LLM Compression

- Authors: Jeongin Yun, Jaeri Lee, Jongjin Kim, Minjun Kim, Jinho Song, U Kang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.8843354186510757
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.2213/
- PDF: https://aclanthology.org/2026.acl-long.2213.pdf
- Local PDF: pdf/2026-07-20_04_SharVeT_ Similarity-aware Parameter Sharing with Vector-based Tuning for Efficient LLM Compression.pdf

How can we share parameters within large language models to significantly reduce memory costs while preserving accuracy? While parameter sharing is a promising solution to the memory overhead of large language models, existing methods rely on naive grouping and fail to correct sharing-induced discrepancies. We propose an accurate and efficient parameter sharing framework, SharVeT (Similarity-aware sharing with Vector-based Tuning), which performs similarity-based grouping to ensure accurate sharing, allocates parameters adaptively to preserve diversity within each group, and applies lightweight refinement with knowledge distillation to correct sharing-induced discrepancies. Experiments show that SharVeT outperforms existing sharing methods, achieving up to 32.1% lower perplexity and 23.3% higher few-shot reasoning accuracy.

## 5. WebAggregator: Enhancing Compositional Reasoning Capabilities of Deep Research Agent Foundation Models

- Authors: Rui Wang, Ce Zhang, Jun-Yu Ma, Jianshu Zhang, Hongru Wang, Yi Chen, Boyang Xue, Tianqing Fang, Zhisong Zhang, Hongming Zhang, Haitao Mi, Dong Yu, Kam-Fai Wong
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.883924145851584
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1124/
- PDF: https://aclanthology.org/2026.acl-long.1124.pdf
- Local PDF: pdf/2026-07-20_05_WebAggregator_ Enhancing Compositional Reasoning Capabilities of Deep Research Agent Foundation Models.pdf

The hallmark of Deep Research agents lies in compositional reasoning, the capacity to aggregate distributed, heterogeneous information into coherent logical insights. However, current agentic systems are often retrieval-heavy but reasoning-light, where success is predominantly determined by simple entity-seeking rather than the multi-step aggregation of scattered evidence. To address this, we propose a data synthesis pipeline WebAggregator, designed to shift the agentic paradigm from retrieval-centric to compositional aggregation. Our approach first employs Proactive Explorer to collect interconnected knowledge, then Compositional Logic Proposer to weave knowledge into complex questions using over 12 composition guidelines derived from a rigorous deconstruction of the Deep Research problem setting. Fine-tuning on this corpus fundamentally transforms agent behavior, fostering deliberate composition reasoning and reduced tool redundancy. The resulting WebAggregator-32B surpasses GPT-4.1 and matches Claude-3.7-Sonnet on GAIA, WebWalkerQA, and XBench. To address the lack of benchmarks that emphasize both reasoning and retrieval, we introduce the WebAggregatorQA testbed, which reveals that even with perfect retrieval, top-tier models still underperformed. These results demonstrate that compositional reasoning, not retrieval, is the true performance ceiling for next-generation research agents.

## 6. RAG over Tables: Hierarchical Memory Index, Multi-Stage Retrieval, and Benchmarking

- Authors: Jiaru Zou, Dongqi Fu, Sirui Chen, Xinrui He, Zihao Li, Yada Zhu, Jiawei Han, Jingrui He
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.8829131544361717
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1902/
- PDF: https://aclanthology.org/2026.findings-acl.1902.pdf
- Local PDF: pdf/2026-07-20_06_RAG over Tables_ Hierarchical Memory Index, Multi-Stage Retrieval, and Benchmarking.pdf

Retrieval-Augmented Generation (RAG) enhances Large Language Models (LLMs) by integrating them with an external knowledge base to improve the answer relevance and accuracy. In real-world scenarios, beyond pure text, a substantial amount of knowledge is stored in tables, and user questions often require retrieving answers that are distributed across multiple tables. Retrieving knowledge from a table corpora (i.e., various individual tables) for a question remains nascent, for (i) how to understand intra- and inter-table knowledge effectively, (ii) how to filter unnecessary tables and retrieve the most relevant tables efficiently, (iii) how to organize complex retrieved contexts for LLMs’ reasoning, and (iv) how to evaluate the corresponding performance in a realistic setting. Facing the above challenges, in this paper, we first propose a table-corpora-aware RAG framework, named T-RAG, which consists of the hierarchical memory index, multi-stage retrieval, and graph-aware context organization for effective and efficient table knowledge retrieval and inference. Then, we develop a multi-table question answering benchmark named MultiTableQA, which spans 3 different task types, 57,193 tables, and 23,758 questions in total, and the sources are all from real-world scenarios. Based on MultiTableQA, we perform a comprehensive comparison of table retrieval methods, RAG-based approaches, and table-to-graph representation learning methods. T-RAG consistently achieves state-of-the-art accuracy, recall, and runtime performance, with improvements of up to 9.4%. Moreover, T-RAG yields an average inference gain of 11.8% across different downstream backbone LLMs. Our code and data are available at https://github.com/jiaruzouu/T-RAG.

## 7. OctoTools: A Multi-Agent Framework with Extensible Tools for Complex Reasoning

- Authors: Pan Lu, Bowen Chen, Sheng Liu, Rahul Thapa, Joseph Boen, James Zou
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.880953416923483
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1/
- PDF: https://aclanthology.org/2026.acl-long.1.pdf
- Local PDF: pdf/2026-07-20_07_OctoTools_ A Multi-Agent Framework with Extensible Tools for Complex Reasoning.pdf

Solving complex reasoning tasks may involve visual understanding, domain knowledge retrieval, numerical calculation, and multi-step reasoning. Existing methods augment large language models (LLMs) with external tools but are restricted to specialized domains, limited tool types, or require additional training data. In this paper, we introduce OctoTools, a training-free, user-friendly, and easily extensible multi-agent framework designed to tackle complex reasoning across diverse domains. OctoTools introduces standardized tool cards to encapsulate tool functionality, a planner for both high-level and low-level planning, and an executor to carry out tool usage. We validate OctoTools’ generality across 16 diverse tasks (including MathVista, MMLU-Pro, MedQA, and GAIA-Text), achieving substantial average accuracy gains of 9.3% over GPT-4o. Furthermore, OctoTools also outperforms AutoGen, GPT-Functions, and LangChain by up to 10.6% when given the same set of tools. Through comprehensive analysi, ablations, and robustness tests with compact backbones and noisy tool environments, OctoTools demonstrates advantages in task planning, effective tool usage, and multi-step problem solving. Code, demos, and visualization are publicly available at https://octotools.github.io/ .

## 8. Unlocking Implicit Experience: Synthesizing Tool-Use Trajectories from Text

- Authors: Zhihao Xu, Rumei Li, Jiahuan Li, Rongxiang Weng, Jingang Wang, Xunliang Cai, Xiting Wang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.8806319690106945
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.452/
- PDF: https://aclanthology.org/2026.acl-long.452.pdf
- Local PDF: pdf/2026-07-20_08_Unlocking Implicit Experience_ Synthesizing Tool-Use Trajectories from Text.pdf

Enabling Large Language Models (LLMs) to effectively utilize tools in multi-turn interactions is essential for building capable autonomous agents. However, acquiring diverse and realistic multi-turn tool-use data remains a significant challenge. In this work, we propose a novel text-based paradigm. We observe that textual corpora naturally contain rich, multi-step problem-solving experiences, which can serve as an untapped, scalable, and authentic data source for multi-turn tool-use tasks. Based on this insight, we introduce GEM, a data synthesis pipeline that enables the generation and extraction of multi-turn tool-use trajectories from text corpora through a four-stage process: relevance filtering, workflow tool extraction, trajectory grounding, and complexity refinement. To reduce the computational cost, we further train a specialized Trajectory Synthesizer via supervised fine-tuning. This model distills the complex generation pipeline into an efficient, end-to-end trajectory generator. Experiments demonstrate that our GEM-32B achieve a 14.9% improvement on the BFCL V3 Multi-turn benchmark. Our models partially surpass the performance of models trained on -bench (Airline and Retail) in-domain data, highlighting the superior generalization capability derived from our text-based synthesis paradigm. Notably, our Trajectory Synthesizer matches the quality of the full pipeline while significantly reducing inference latency and costs.

## 9. ARK: Answer-Centric Retriever Tuning via KG-augmented Curriculum Learning

- Authors: Jiawei Zhou, Hang Ding, Haiyun Jiang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.8803378071894485
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.371/
- PDF: https://aclanthology.org/2026.acl-long.371.pdf
- Local PDF: pdf/2026-07-20_09_ARK_ Answer-Centric Retriever Tuning via KG-augmented Curriculum Learning.pdf

Retrieval-Augmented Generation (RAG) has emerged as a powerful framework for knowledge-intensive tasks, yet its effectiveness in long-context scenarios is often bottlenecked by the retriever’s inability to distinguish sparse yet crucial evidence. Standard retrievers, optimized for query-document similarity, frequently fail to align with the downstream goal of generating a precise answer. To bridge this gap, we propose a novel fine-tuning framework that optimizes the retriever for Answer Alignment. Specifically, we first identify high-quality positive chunks by evaluating their sufficiency to generate the correct answer. We then employ a curriculum-based contrastive learning scheme to fine-tune the retriever. This curriculum leverages LLM-constructed Knowledge Graphs (KGs) to generate augmented queries, which in turn mine progressively challenging hard negatives. This process trains the retriever to distinguish the answer-sufficient positive chunks from these nuanced distractors, enhancing its generalization. Extensive experiments on 10 datasets from the Ultradomain and LongBench benchmarks demonstrate that our fine-tuned retriever achieves state-of-the-art performance, improving 14.5% over the base model without substantial architectural modifications and maintaining strong efficiency for long-context RAG. Our work presents a robust and effective methodology for building truly answer-centric retrievers.

## 10. TLoRA: Task-aware Low Rank Adaptation of Large Language Models

- Authors: Weicheng Lin, Yi Zhang, Jiawei Dang, Liang-Jie Zhang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.8798382045664606
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1348/
- PDF: https://aclanthology.org/2026.acl-long.1348.pdf
- Local PDF: pdf/2026-07-20_10_TLoRA_ Task-aware Low Rank Adaptation of Large Language Models.pdf

Low-Rank Adaptation (LoRA) has become a widely adopted parameter-efficient fine-tuning method for large language models, with its effectiveness largely influenced by the allocation of ranks and scaling factors, as well as initialization. Existing LoRA variants typically address only one of these factors, often at the cost of increased training complexity or reduced practical efficiency.In this work, we present Task-aware Low-Rank Adaptation (TLoRA), a unified framework that jointly optimizes initialization and resource allocation at the outset of training. TLoRA introduces a data-driven initialization strategy that aligns the LoRA A matrix with task-relevant subspaces by performing singular value decomposition on the product of pre-trained weights and input activation covariance. After this, the A matrix is frozen, and only the B matrix is trained. Furthermore, TLoRA employs a sensitivity-based importance metric to adaptively allocate ranks and scaling factors across layers under a fixed parameter budget.We conduct extensive experiments that demonstrate TLoRA consistently performs excellently across various tasks, including natural language understanding, commonsense reasoning, math reasoning, code generation, and chat generation, while significantly reducing the number of trainable parameters. Our code are available at https://github.com/Rambo-Yi/TLora/tree/main

## 11. Rethinking Scale: Deployment Trade-offs of Small Language Models under Agent Paradigms

- Authors: Xinlin Wang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.8798372356389508
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-industry.123/
- PDF: https://aclanthology.org/2026.acl-industry.123.pdf
- Local PDF: pdf/2026-07-20_11_Rethinking Scale_ Deployment Trade-offs of Small Language Models under Agent Paradigms.pdf

Despite the impressive capabilities of large language models, their substantial computational costs, latency, and privacy risks hinder their widespread deployment in real-world applications. Small Language Models (SLMs) with fewer than 10 billion parameters present a promising alternative; however, their inherent limitations in knowledge and reasoning curtail their effectiveness. Existing research primarily focuses on enhancing SLMs through scaling laws or fine-tuning strategies while overlooking the potential of using agent paradigms, such as tool use and multi-agent collaboration, to systematically compensate for the inherent weaknesses of small models. To address this gap, this paper presents the first large-scale, comprehensive study of <10B open-source models under three paradigms: (1) the base model, (2) a single agent equipped with tools, and (3) a routing-based multi-agent system with collaborative capabilities.Our results show that structured agent frameworks (combining step-by-step reasoning and tool use) substantially improve effectiveness over direct prompting, with single-agent systems achieving the best balance between performance and cost. In contrast, routing-based multi-agent setups introduce additional coordination overhead with limited gains under small-model constraints.Our findings highlight the importance of agent-centric design for efficient and trustworthy deployment in resource-constrained settings.

## 12. Skill Weaving: Efficient LLM Improvement via Modular Skillpacks

- Authors: Zhuo Li, Guodong DU, Zesheng Shi, Weiyang Guo, Weijun Yao, Yuan Zhou, Jiabo Zhang, Jing Li
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.8791882107427416
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1989/
- PDF: https://aclanthology.org/2026.findings-acl.1989.pdf
- Local PDF: pdf/2026-07-20_12_Skill Weaving_ Efficient LLM Improvement via Modular Skillpacks.pdf

In this work, we introduce SkillWeave, a modular improvement framework that enables large language models to specialize under fixed memory budgets. SkillWeave partitions full capabilities of a general-purpose model into domain-specific skillpacks—lightweight, domain-specific delta modules—that reorganize and refine the model’s internal knowledge. To ensure deployment efficiency, SkillWeave incorporates SkillZip, a compression component that transforms specialized parameters into lightweight, inference-ready skillpacks. Together, these components allow SkillWeave to achieve strong multi-domain performance and inference-efficient execution. On multi-task and agentic benchmarks, a 9B SkillWeave model outperforms task-specific baselines and even surpasses a 32B monolithic LLM, while achieving up to 4× speedup.

## 13. Reasoning for Hierarchical Text Classification: The Case of Patents

- Authors: Lekang Jiang, Wenjun Sun, Stefan Goetz
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.8786970716980322
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.541/
- PDF: https://aclanthology.org/2026.findings-acl.541.pdf
- Local PDF: pdf/2026-07-20_13_Reasoning for Hierarchical Text Classification_ The Case of Patents.pdf

Hierarchical text classification (HTC) assigns documents to multiple levels of a pre-defined taxonomy. Automated patent subject classification represents one of the hardest HTC scenarios because of professional difficulties and extensive labels. Prior approaches only output a flat label set, which offers little insight into the reason behind predictions. Therefore, we propose Reasoning for Hierarchical Classification (RHC), a novel framework that reformulates HTC as a step-by-step reasoning task to sequentially deduce hierarchical labels. RHC trains large language models (LLMs) in two stages: a cold-start stage that aligns outputs with chain-of-thought (CoT) reasoning format and a reinforcement learning (RL) stage to enhance multi-step reasoning ability. RHC demonstrates four advantages in our experiments. (1) Effectiveness: RHC surpasses previous baselines and outperforms the supervised fine-tuning counterparts by approximately 3% in accuracy and macro F1. (2) Explainability: RHC produces natural-language justifications before prediction to facilitate human inspection. (3) Scalability: RHC scales favorably with model size with larger gains compared to standard fine-tuning. (4) Applicability: Beyond patents, we further demonstrate that RHC achieves state-of-the-art performance on other widely used HTC benchmarks, which highlights its broad applicability.

## 14. Disentangling Reasoning Logic to Resolve Explicit Knowledge Conflicts

- Authors: Xianda Zheng, Zijian Huang, Meng-Fen Chiang, Jiamou Liu, Yuan Fang, Michael J. Witbrock, Kaiqi Zhao
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.8783218731811244
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1451/
- PDF: https://aclanthology.org/2026.acl-long.1451.pdf
- Local PDF: pdf/2026-07-20_14_Disentangling Reasoning Logic to Resolve Explicit Knowledge Conflicts.pdf

Explicit knowledge conflicts, where retrieved contexts contain contradictory information, have become increasingly prevalent as Large Language Models (LLMs) integrate diverse data sources. The core challenge lies in the complexity of entangled narratives and the heterogeneity of conflict cases, which impose excessive demands on the reasoning capabilities of standard models. To address this, we propose K nowledge C onflict R easoning ( KCR ), a framework that adjudicates conflicts by structuring the underlying logic. KCR first disentangles conflicting contexts into distinct sets of reasoning traces, utilizing both textual and graph-based representations, to simplify comprehension. It then employs a Reinforcement Learning with Verifiable Rewards (RLVR) paradigm, guiding the model to internalize a reasoning process that maximizes logical consistency while actively suppressing spurious reasoning paths derived from contradictory contexts. Extensive experiments demonstrate that KCR yields substantial improvements: a KCR-enhanced 7B model surpasses the performance of baselines equipped with top-tier closed-source models such as GPT-4o and GPT-5.1.

## 15. When Agents Look the Same: Quantifying Distillation-Induced Similarity in Tool-Use Behaviors

- Authors: Chenghao Yang, Yuning Zhang, Zhoufutu Wen, Tao Gong, Jiaheng Liu, Qi Chu, Nenghai Yu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.8778821735155082
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.478/
- PDF: https://aclanthology.org/2026.acl-long.478.pdf
- Local PDF: pdf/2026-07-20_15_When Agents Look the Same_ Quantifying Distillation-Induced Similarity in Tool-Use Behaviors.pdf

Model distillation is a primary driver behind the rapid progress of LLM agents, yet it often leads to behavioral homogenization. Many emerging agents share nearly identical reasoning steps and failure modes, suggesting they may be distilled echoes of a few dominant teachers. Existing metrics, however, fail to distinguish mandatory behaviors required for task success from non-mandatory patterns thatreflect a model’s autonomous preferences. We propose two complementary metrics to isolate non-mandatory behavioral patterns: Response Pattern Similarity (RPS) for verbal alignment and Action Graph Similarity (AGS) for tool-use habits modeled as directed graphs. Evaluating 18 models from 8 providers on 𝜏 -Bench and 𝜏 2 -Bench against Claude Sonnet 4.5 (thinking), we find that within-family model pairs score 5.9 pp higher in AGS than cross-family pairs, and that Kimi-K2 (thinking) reaches 82.6% S node and 94.7% S dep , exceeding Anthropic’s own Opus 4.1. A controlled distillation experiment further confirms that AGS distinguishes teacher-specific convergence from general improvement. RPS and AGS capture distinct behavioral dimensions (Pearson r = 0.491), providing complementary diagnostic signals for behavioral convergence in the agent ecosystem.Our code is available at https://github.com/Syuchin/AgentEcho .

## 16. Safe-SAIL: Towards a Fine-grained Safety Landscape of Large Language Models via Sparse Autoencoder Interpretation Framework

- Authors: Jiaqi Weng, Han Zheng, Hanyu Zhang, Ej Zhou, Qinqin He, Jialing Tao, Hui Xue, Zhixuan Chu, Xiting Wang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.8768509726560394
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.944/
- PDF: https://aclanthology.org/2026.findings-acl.944.pdf
- Local PDF: pdf/2026-07-20_16_Safe-SAIL_ Towards a Fine-grained Safety Landscape of Large Language Models via Sparse Autoencoder Interpretation Framew.pdf

Sparse autoencoders (SAEs) enable interpretability research by decomposing entangled model activations into monosemantic features. However, under what circumstances SAEs derive most fine-grained latent features for safety—a low-frequency concept domain—remains unexplored. Two key challenges exist: identifying SAEs with the greatest potential for generating safety domain-specific features, and the prohibitively high cost of detailed feature explanation. In this paper, we propose **Safe-SAIL**, a unified framework for interpreting SAE features in safety-critical domains to advance mechanistic understanding of large language models. Safe-SAIL introduces a pre-explanation evaluation metric to efficiently identify SAEs with strong safety domain-specific interpretability, and reduces interpretation cost by 55% through a segment-level simulation strategy. Building on Safe-SAIL, we train a comprehensive suite of SAEs with human-readable explanations and systematic evaluations for 1,758 safety-related features spanning four domains: pornography, politics, violence, and terror. Using this resource, we conduct empirical analyses and provide insights on the effectiveness of Safe-SAIL for risk feature identification and how safety-critical entities and concepts are encoded across model layers. All models, explanations, and tools are publicly released in an open-source toolkit at https://anonymous.4open.science/r/Safe-SAIL/.

## 17. Not All Citations Are Equal:Entropy-Guided Citation Selection for Noise-Resistant Medical LLM

- Authors: Minyu Gao, Hanlin Xiao, Ruoyu Wang, Shuai Yang, YeXuan Zhang, Xin Wu, Xingyu Liu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.876435100216121
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1727/
- PDF: https://aclanthology.org/2026.findings-acl.1727.pdf
- Local PDF: pdf/2026-07-20_17_Not All Citations Are Equal_Entropy-Guided Citation Selection for Noise-Resistant Medical LLM.pdf

Retrieval-Augmented Generation (RAG) provides external knowledge support for large language models (LLMs) in medical applications, but retrieved contexts often contain noisy or conflicting evidence that can degrade reasoning. We observe that when internal and external knowledge disagree, models systematically prefer external citations, inadvertently injecting retrieval noise. Our analyses further show that only a subset of retrieved citations consistently improves outcomes; these effective citations exhibit markedly lower token-level entropy, linking citation entropy to model accuracy. Building on these findings, we propose a complete pipeline consisting of a training-free multi-turn reasoning framework and a post-training methodology. The training-free framework elicits internal thought, external thought, and fusion thought, and applies conflict detection and explicit denoising for complex queries. For post-training, we distill structured supervised fine-tuning (SFT) data and apply GRPO with an entropy-based citation reward that encourages selective citation of beneficial external knowledge while penalizing noisy citations. Experiments across diverse benchmarks demonstrate consistent gains in noise-resistant medical reasoning, with larger improvements on harder cases.

## 18. CogNet-KG: Empowering Tutoring Dialogues with a Cognitively-Structured Knowledge Graph for STEM Learning

- Authors: Ding Yu, Yu Lu, Tengju Li, Shasha Xiong, Shengquan Yu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.875920449573104
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.639/
- PDF: https://aclanthology.org/2026.findings-acl.639.pdf
- Local PDF: pdf/2026-07-20_18_CogNet-KG_ Empowering Tutoring Dialogues with a Cognitively-Structured Knowledge Graph for STEM Learning.pdf

Educational knowledge graph (EKG) is a critical component of intelligent tutoring systems that is structured around cognitive principles and provides support for interactive teaching. Most existing EKGs usually rely on simplistic relations, bind with single subjects, and lack integration with explicit learning objectives. In this paper, we introduce CogNet-KG, a novel and cognitively-structured large-scale knowledge graph for STEM learning. CogNet-KG models nearly 500 core concepts across five subjects with various cognitively-grounded relations corresponding to specific learning objectives, thereby encoding a rich cognitive schema for guiding more effective teaching. Based on this structure, we then construct a high-quality tutoring dialogue dataset CogDialogue-QA by leveraging adaptive instructional strategies. Additionally, we train CogTutor-LM, a specialized tutorial LLM that internalizes this structured pedagogical reasoning. Overall evaluation demonstrates that CogTutor-LM generates responses with significantly greater instructional coherence and more appropriate pedagogical guidance compared to baselines, validating the effectiveness of our graph-driven approach to fostering knowledge integration and stimulating students’ thinking. The datasets are publicly available at https://github.com/KCAIED/CogNet-KG.

## 19. MIND: From Passive Mimicry to Active Reasoning through Capability-Aware Multi-Perspective CoT Distillation

- Authors: Jin Cui, Jiaqi Guo, Jiepeng Zhou, Ruixuan Yang, Jiayi Lu, Jiajun Xu, Jiangcheng Song, Boran Zhao, Pengju Ren
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.8753536337577916
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.2020/
- PDF: https://aclanthology.org/2026.acl-long.2020.pdf
- Local PDF: pdf/2026-07-20_19_MIND_ From Passive Mimicry to Active Reasoning through Capability-Aware Multi-Perspective CoT Distillation.pdf

While Large Language Models (LLMs) have emerged with remarkable capabilities in complex tasks through Chain-of-Thought (CoT) reasoning, practical resource constraints have sparked interest in transferring these abilities to smaller models. However, achieving both domain performance and cross-domain generalization remains challenging. Existing approaches typically restrict students to following a single golden rationale and treat different reasoning paths independently. Due to distinct inductive biases and intrinsic preferences, alongside the student’s evolving capacity and reasoning preferences during training, a teacher’s "optimal" rationale could act as out-of-distribution noise. This misalignment leads to a degeneration of the student’s latent reasoning distribution, causing suboptimal performance. To bridge this gap, we propose MIND, a capability-adaptive framework that transitions distillation from passive mimicry to active cognitive construction. We synthesize diverse teacher perspectives through a novel "Teaching Assistant" network. By employing a novel Feedback-Driven Inertia Calibration mechanism, this network utilizes inertia-filtered training loss to align supervision with the student’s current adaptability, effectively enhancing performance while mitigating catastrophic forgetting. Extensive experiments demonstrate that MIND achieves state-of-the-art performance on both in-distribution and out-of-distribution benchmarks, and our sophisticated latent space analysis further confirms the mechanism of reasoning ability internalization.

## 20. ARC: Active and Reflection-driven Context Management for Long-Horizon Information Seeking Agents

- Authors: Yilun Yao, Shan Huang, Elsie Dai, Zhewen Tan, Zhenyu Duan, Shousheng Jia, Yanbing Jiang, Tong Yang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.874790455241034
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.930/
- PDF: https://aclanthology.org/2026.findings-acl.930.pdf
- Local PDF: pdf/2026-07-20_20_ARC_ Active and Reflection-driven Context Management for Long-Horizon Information Seeking Agents.pdf

Large language models are increasingly deployed as research agents for deep search and long-horizon information seeking, yet their performance often degrades as interaction histories grow. This degradation, known as context rot, reflects a failure to maintain coherent and task-relevant internal states over extended reasoning horizons. Existing approaches primarily manage context through raw accumulation or passive summarization, treating it as a static artifact and allowing early errors or misplaced emphasis to persist. Motivated by this perspective, we propose ARC, which is the first framework to systematically formulate context management as an active, reflection-driven process that treats context as a dynamic internal reasoning state during execution. ARC operationalizes this view through reflection-driven monitoring and revision, allowing agents to actively reorganize their working context when misalignment or degradation is detected. Experiments on challenging long-horizon information-seeking benchmarks show that ARC consistently outperforms passive context compression methods, achieving up to an 11% absolute improvement in accuracy on BrowseComp-ZH with Qwen2.5-32B-Instruct.

## 21. LaMI: Augmenting Large Language Models via Late Multi-Image Fusion

- Authors: Guy Yariv, Idan Schwartz, Yossi Adi, Sagie Benaim
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.8747770318233417
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-short.3/
- PDF: https://aclanthology.org/2026.acl-short.3.pdf
- Local PDF: pdf/2026-07-20_21_LaMI_ Augmenting Large Language Models via Late Multi-Image Fusion.pdf

Commonsense reasoning often requires both textual and visual knowledge, yet Large Language Models (LLMs) trained solely on text lack visual grounding (e.g., "what color is an emperor penguin’s belly?"). Visual Language Models (VLMs) perform better on visually grounded tasks but face two limitations: (i) often reduced performance on text-only commonsense reasoning compared to text-trained LLMs, and (ii) adapting newly released LLMs to vision input typically requires costly multimodal training. An alternative augments LLMs with test-time visual signals, improving visual commonsense without harming textual reasoning, but prior designs often rely on early fusion and a single image, which can be suboptimal. We propose a late multi-image fusion method: multiple images are generated from the text prompt with a lightweight parallel sampling, and their prediction probabilities are combined with those of a text-only LLM through a late-fusion layer that integrates projected visual features just before the final prediction. Across visual commonsense and NLP benchmarks, our method significantly outperforms augmented LLMs on visual reasoning, matches VLMs on vision-based tasks, and, when applied to strong LLMs such as LLaMA 3, also improves NLP performance while adding only modest test-time overhead.

## 22. Sparrow: Text-Anchored Window Attention with Visual-Semantic Glimpsing for Speculative Decoding in Video LLMs

- Authors: Libo Zhang, Zhaoning Zhang, Hongwanyang, Peng Qiao, Dongsheng Li
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.874608383655012
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.450/
- PDF: https://aclanthology.org/2026.acl-long.450.pdf
- Local PDF: pdf/2026-07-20_22_Sparrow_ Text-Anchored Window Attention with Visual-Semantic Glimpsing for Speculative Decoding in Video LLMs.pdf

Although speculative decoding is widely used to accelerate Vision-Language Models (VLMs) inference, it faces severe performance collapse when applied to Video Large Language Models (Vid-LLMs). The draft model typically falls into the trap of attention dilution and negative visual gain due to key-value cache explosion and context window mismatches. We observe a visual semantic internalization phenomenon in Vid-LLMs, indicating that critical visual semantics are implicitly encoded into text hidden states during deep-layer interactions, which renders raw visual inputs structurally redundant during deep inference. To address this, we propose the Sparrow framework, which first utilizes visually-aware text-anchored window attention via hidden state reuse to fully offload visual computation to the target model, and leverages intermediate-layer visual state bridging to train the draft model with semantic-rich intermediate states, thereby filtering out low-level visual noise. Additionally, a multi-token prediction strategy is introduced to bridge the training-inference distribution shift. Experiments show that Sparrow achieves an average speedup of 2.82x even with 25k visual tokens, effectively resolving the performance degradation in long sequences and offering a practical solution for real-time long video tasks.

## 23. DOS: Dependency-Oriented Sampler for Masked Diffusion Language Models

- Authors: Xueyu Zhou, Yangrong Hu, Jian Huang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.8742347995332795
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.861/
- PDF: https://aclanthology.org/2026.findings-acl.861.pdf
- Local PDF: pdf/2026-07-20_23_DOS_ Dependency-Oriented Sampler for Masked Diffusion Language Models.pdf

Masked diffusion language models (MDLMs) have recently emerged as a new paradigm in language modeling, offering flexible generation dynamics and enabling efficient parallel decoding. However, existing decoding strategies for pre-trained MDLMs predominantly rely on token-level uncertainty criteria, while largely overlooking sequence-level information and inter-token dependencies. To address this limitation, we propose D ependency- O riented S ampler (DOS), a training-free decoding strategy that leverages inter-token dependencies to inform token updates during generation. Specifically, DOS exploits attention matrices from transformer blocks to approximate inter-token dependencies, emphasizing information from unmasked tokens when updating masked positions. Empirical results demonstrate that DOS consistently achieves superior performance on both code generation and mathematical reasoning tasks. Moreover, DOS can be seamlessly integrated with existing parallel sampling methods, leading to improved generation efficiency without sacrificing generation quality.

## 24. Internalizing Multi-Agent Reasoning for Accurate and Efficient LLM-based Recommendation

- Authors: Yang Wu, Haoze Wang, Qian Li, Jun Zhang, Huan Yu, Jie Jiang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.8740760579767
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.2134/
- PDF: https://aclanthology.org/2026.findings-acl.2134.pdf
- Local PDF: pdf/2026-07-20_24_Internalizing Multi-Agent Reasoning for Accurate and Efficient LLM-based Recommendation.pdf

Large Language Models (LLMs) are reshaping recommender systems by leveraging extensive world knowledge and semantic reasoning to interpret user intent. However, effectively integrating these capabilities with collaborative signals while avoiding prohibitive inference latency remains a critical bottleneck. To address this, we propose a trajectory-driven internalization framework to develop a Single-agent Trajectory-Aligned Recommender (STAR). Specifically, to internalize complex reasoning capabilities into a single efficient model, we first design a multi-agent teacher system capable of multi-turn tool usage and reflection. This teacher utilizes a Collaborative Signal Translation mechanism to explicitly convert latent behavioral patterns into descriptive natural language evidence to enhance reasoning accuracy. Subsequently, a trajectory-driven distillation pipeline transfers this agentic logic, including planning, tool usage, and self-reflection, into the compact STAR model. Extensive experiments demonstrate that STAR surpasses its teacher by 8.7% to 39.5% while eliminating iterative latency, paving the way for real-time, reasoning-enhanced recommendation.

## 25. Reusable Experiences: Latent Routing and Modular Composition in LLMs

- Authors: Shuai Ling, Lizi Liao, Dongmei Jiang, Weili Guan
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.8739514438053697
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1388/
- PDF: https://aclanthology.org/2026.acl-long.1388.pdf
- Local PDF: pdf/2026-07-20_25_Reusable Experiences_ Latent Routing and Modular Composition in LLMs.pdf

Large language models (LLMs) have remarkable capabilities, but adapting them to specialized domains poses a fundamental question: how should accumulated experience be represented and leveraged? Existing approaches represent experience either as explicit textual artifacts in prompts ( e.g. , retrieved documents or dialogues) or implicitly within model weights via fine-tuning ( e.g. , LoRA adapters). However, textual methods are limited by context windows and cannot internalize knowledge, while parametric fine-tuning yields one adapter per task with minimal cross-task skill reuse. We propose ReX ( Re usable e X perience), an experience-centric adaptation framework that treats latent experiences — recurring reasoning patterns and skills — as fundamental units for LLM specialization. Our method learns a shared Experience Bank of foundational skill vectors and uses a VAE-based encoder to map each input to a low-dimensional experience code. An Experience Router then dynamically composes the relevant skill vectors from this bank into a lightweight adapter for that input. By reusing skills across inputs, ReX enables implicit knowledge sharing across tasks without any explicit task identifiers. Experiments on multi-task NLP benchmarks show that this approach outperforms standard task-specific fine-tuning, yielding improved generalization through flexible skill reuse. Code is available at https://github.com/iLearn-Lab/ACL26-ReX .

## 26. Read As Human: Compressing Context via Parallelizable Close Reading and Skimming

- Authors: Jiwei Tang, Shilei Liu, Zhicheng Zhang, Qingsong Lv, Runsong Zhao, Tingwei Lu, Langming Liu, Haibin Chen, Yujin Yuan, Hai-Tao Zheng, Wenbo Su, Bo Zheng
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.8738034692008068
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1309/
- PDF: https://aclanthology.org/2026.acl-long.1309.pdf
- Local PDF: pdf/2026-07-20_26_Read As Human_ Compressing Context via Parallelizable Close Reading and Skimming.pdf

Large Language Models (LLMs) demonstrate exceptional capability across diverse tasks. However, their deployment in long-context scenarios is hindered by two challenges: computational inefficiency and redundant information. We propose RAM (Read As HuMan), a context compression framework that adopts an adaptive hybrid reading strategy, to address these challenges. Inspired by human reading behavior (i.e., close reading important content while skimming less relevant content), RAM partitions the context into segments and encodes them with the input query in parallel. High-relevance segments are fully retained (close reading), while low-relevance ones are query-guided compressed into compact summary vectors (skimming). Both explicit textual segments and implicit summary vectors are concatenated and fed into decoder to achieve both superior performance and natural language format interpretability. To refine the decision boundary between close reading and skimming, we further introduce a contrastive learning objective based on positive and negative query–segment pairs. Experiments demonstrate that RAM outperforms existing baselines on multiple question answering and summarization benchmarks across two backbones, while delivering up to a 12x end-to-end speedup on long inputs (average length 16K; maximum length 32K).

## 27. View-R1: Asymmetric Policy Optimization for Difficulty-Aware Multimodal Reinforcement Learning

- Authors: Minjie Hong, Zirun Guo, Jiabao Zhang, Zehan Wang, Ziang Zhang, Tao Jin, Zhou Zhao
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.872913535824461
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1538/
- PDF: https://aclanthology.org/2026.findings-acl.1538.pdf
- Local PDF: pdf/2026-07-20_27_View-R1_ Asymmetric Policy Optimization for Difficulty-Aware Multimodal Reinforcement Learning.pdf

Multimodal Large Language Models (MLLMs) are powerful at integrating diverse data but often struggle with complex reasoning. Reinforcement learning (RL) can enhance reasoning, yet it may cause performance degradation on general tasks and overthinking in MLLMs. We propose Asymmetric Policy Optimization (APO), which separates responses into positive and negative groups. For positive samples, Difficulty-Adaptive Divergence Shaping (DADS) dynamically adjusts the KL weight to stabilize training and preserve knowledge. For negative samples, Suboptimal Trajectory Complexity Regularization (STCR) penalizes overly long responses to reduce overthinking. Applied to Qwen2.5-VL, our model View-R1 achieves a 10.55% improvement in reasoning and outperforms larger models (7–11B) while not only maintaining but also slightly improving performance on general tasks. These results highlight the effectiveness and broad applicability of our DADS and STCR techniques for advancing complex multimodal reasoning in MLLMs. Our code is available at https://github.com/Collab-Gen/View-R1.

## 28. Filling the Long Tail: Structure-Aware Curriculum-Gap Completion for Medical Education with LLMs

- Authors: Wenjie Lin
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.872040557008313
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-srw.83/
- PDF: https://aclanthology.org/2026.acl-srw.83.pdf
- Local PDF: pdf/2026-07-20_28_Filling the Long Tail_ Structure-Aware Curriculum-Gap Completion for Medical Education with LLMs.pdf

Medical education resources are dense for common diseases but often sparse for under-covered conditions, atypical presentations, and fine-grained concept distinctions. This creates curriculum gaps that are difficult to repair manually, especially in long-tail domains where structured teaching materials are limited. We introduce Curriculum-Gap Completion (CGC), a new task for Large Language Model (LLM)-based medical education in which a model reconstructs missing educational units from a partially specified curriculum graph. Given topic nodes, pedagogical relations, and structured teaching slots, the model predicts omitted concepts, restores missing instructional links, and completes automatically verifiable teaching content. We instantiate this setting in a long-tail medical case study (hyperhidrosis) and evaluate five LLMs under three methods: direct prompting, retrieval-augmented prompting, and our proposed Structure-Aware Curriculum-Gap Completion (SACGC) framework. Across models, SACGC achieves the strongest overall performance, with the largest gains on structurally demanding masking settings. Ablation results show that explicit graph structure is the most important component, while schema constraints provide additional benefit. These findings suggest that LLMs are better suited for reconstructing an under-specified educational structure than for unrestricted medical tutoring, and they motivate CGC as a new natural language processing (NLP) problem for healthcare education.

## 29. Are We Using the Right Benchmark: An Evaluation Framework for Visual Token Compression Methods

- Authors: Chenfei Liao, Wensong Wang, Zichen Wen, Xu Zheng, Yiyu Wang, Haocong He, Yuanhuiyi Lyu, Lutao Jiang, Xin Zou, Yuqian Fu, Bin Ren, Linfeng Zhang, Xuming Hu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.871616010735499
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.195/
- PDF: https://aclanthology.org/2026.acl-long.195.pdf
- Local PDF: pdf/2026-07-20_29_Are We Using the Right Benchmark_ An Evaluation Framework for Visual Token Compression Methods.pdf

Recent efforts to accelerate inference in Multimodal Large Language Models (MLLMs) have largely focused on visual token compression. The effectiveness of these methods is commonly evaluated by measuring the accuracy drop on existing MLLM benchmarks before and after compression. However, these benchmarks are originally designed to assess general perception and reasoning abilities, rather than the specific challenges posed by visual token compression, leading to a fundamental task mismatch. In this work, we uncover a counterintuitive yet consistent phenomenon: simple image downsampling outperforms many advanced visual token compression methods across multiple widely used benchmarks. Through a comprehensive empirical study spanning eight popular benchmarks and multiple state-of-the-art compression techniques, we show that (i) current benchmarks contain substantial noise (task-irrelevant samples) for evaluating visual token compression, and (ii) downsampling can act as an effective data filter that distinguishes between simple and difficult samples with respect to compression sensitivity. Motivated by these findings, we propose VTC-Bench, an evaluation framework that explicitly leverages downsampling as a discriminator to denoise existing benchmarks, enabling a fairer and more meaningful additional assessment of visual token compression methods.

## 30. MoA: Heterogeneous Mixture of Adapters for Parameter-Efficient Fine-Tuning of Large Language Models

- Authors: Jie Cao, Tianwei Lin, Bo Yuan, Rolan Yan, Hongyang He, Wenqiao Zhang, Juncheng Li, Dongping Zhang, Siliang Tang, Yueting Zhuang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.871594225039067
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.965/
- PDF: https://aclanthology.org/2026.acl-long.965.pdf
- Local PDF: pdf/2026-07-20_30_MoA_ Heterogeneous Mixture of Adapters for Parameter-Efficient Fine-Tuning of Large Language Models.pdf

Recent studies integrate Low-Rank Adaptation (LoRA) and Mixture-of-Experts (MoE) to further enhance the performance of parameter-efficient fine-tuning (PEFT) methods in Large Language Model (LLM) applications. Existing methods employ homogeneous MoE-LoRA architectures composed of LoRA experts with either similar or identical structures and capacities. However, these approaches often suffer from representation collapse and expert load imbalance, which negatively impact the potential of LLMs. To address these challenges, we propose a heterogeneous Mixture-of-Adapters (MoA) approach. This method dynamically integrates PEFT adapter experts with diverse structures, leveraging their complementary representational capabilities to foster expert specialization, thereby enhancing the effective transfer of pre-trained knowledge to downstream tasks. MoA supports two variants: (i) Soft MoA achieves fine-grained integration by performing a weighted fusion of all expert outputs; (ii) Sparse MoA activates adapter experts sparsely based on their contribution, achieving this with negligible performance degradation. Experimental results demonstrate that heterogeneous MoA outperforms homogeneous MoE-LoRA methods in both performance and parameter efficiency. Our project is available at https://github.com/DCDmllm/MoA .
