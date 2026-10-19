# Paper Daily Reading - 2026-10-19

## 1. Decomposing multi-scale dynamic regulation from single-cell multiomics with scMagnify

- Authors: Xufeng Chen, Xi Yan, Bihan Shen, Heqi Wang, Z Tang, Yan Zang, Ping Lin, Haibing Zhang, Yu Li, Hong Li
- Source: openalex
- Venue type: journal
- Journal: Nature Communications
- Publication status: published
- Publication date: 2026-10-17
- DOI: https://doi.org/10.1038/s41467-026-78441-9
- Categories: Gene Regulatory Network Analysis, Single-cell and spatial transcriptomics, Genomics and Chromatin Dynamics
- Relevance: 3.3939823024127493
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://doi.org/10.1038/s41467-026-78441-9
- PDF: https://www.nature.com/articles/s41467-026-78441-9_reference.pdf
- Local PDF: pdf/2026-10-19_01_Decomposing multi-scale dynamic regulation from single-cell multiomics with scMagnify.pdf

Deciphering the highly coupled regulatory circuits that drive cellular dynamics remains a fundamental goal in biology. However, capturing the multi-scale time-lagged dynamics and combinatorial regulatory logic of gene regulation remains challenging. Here we present scMagnify, a deep-learning-based framework that leverages chromatin accessibility and gene expression via Granger causality to reconstruct and decompose multi-scale gene regulatory networks (GRNs). Diverse benchmarks demonstrate scMagnify’s favorable performance. scMagnify employs tensor decomposition to identify combinatorial TF modules and their activation profiles across multiple time-lags. We applied scMagnify to human hematopoiesis and mouse pancreas development, where it recovered known lineage-driving regulators and provided further insights into the combinatorial logic underlying cell fate decisions. Furthermore, in the context of kidney injury, scMagnify’s intercellular communication module mapped key signaling-to-transcription cascades linking microenvironment cues to pathological epithelial cell changes. In summary, scMagnify provides a robust computational framework for dissecting the multi-scale regulatory logic that governs complex biological processes in development and disease. Chen and colleagues present scMagnify, a framework that uses single-cell multi-omic data to reconstruct and decompose time-lagged gene regulatory networks. The study analyses regulatory programs associated with development and disease.

## 2. Identifying Collective Intelligence Factor in LLM Agent Groups for Generalizable Multi-Agent System Design

- Authors: Zhilun Zhou, Zihan Liu, Jiahe Liu, Yihan Wang, Qingyu Shao, Fengli Xu, Depeng Jin, Yong Li
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.619684248725979
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.624/
- PDF: https://aclanthology.org/2026.findings-acl.624.pdf
- Local PDF: pdf/2026-10-19_02_Identifying Collective Intelligence Factor in LLM Agent Groups for Generalizable Multi-Agent System Design.pdf

Large language model (LLM)-based multi-agent systems (MASs) have shown impressive performance in solving a wide range of complex problems. However, previous studies mainly focus on designing customized MAS for specific tasks, while a critical research problem remains unclear: Do LLM agent groups exhibit a form of “general intelligence” that reflects their general ability across various tasks? Researchers have found a Collective Intelligence (CI) factor in human groups that captures their general capability. Inspired by this, in this study, we aim to investigate whether an analogous CI factor also exists in LLM agent groups, which is crucial for building generalizable MAS. Motivated by human cognitive psychology experiments, we construct 108 LLM agent groups with diverse group sizes, LLM compositions, and communication topologies. We systematically evaluate these groups across a wide range of tasks and analyze their performances. Our results demonstrate that an Artificial Collective Intelligence (ACI) factor can be extracted from LLM agent groups to predict the generalization performance on new tasks. Inspired by this, we train a model to predict the ACI based on the features of MAS, and show that it can be used as a plug-in to enhance the generalization ability of MAS optimization methods.

## 3. Controlling What You Share: Assessing Language Model Adherence to Privacy Preferences

- Authors: Guillem Ramírez, Alexandra Birch, Ivan Titov
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.6158812972737877
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1990/
- PDF: https://aclanthology.org/2026.findings-acl.1990.pdf
- Local PDF: pdf/2026-10-19_03_Controlling What You Share_ Assessing Language Model Adherence to Privacy Preferences.pdf

Large language models (LLMs) are primarily accessed via commercial APIs, but this often requires users to expose their data to service providers. In this paper, we explore how users can stay in control of their data by using privacy profiles: simple natural language instructions that say what should and should not be revealed. We build a framework where a local model uses these instructions to rewrite queries, only hiding details deemed sensitive by the user, before sending them to an external model, thus balancing privacy with performance. To support this research, we introduce PEEP, a multilingual dataset of real user queries annotated to mark private content and paired with synthetic privacy profiles, alongside PROFIT, a training procedure that enables effective and efficient use of the pipeline. Experiments with lightweight local LLMs show that, after training, they not only achieve markedly better privacy preservation but also match or exceed the performance of much larger few-shot models.

## 4. Forge: Quality-Aware Reinforcement Learning for NP-Hard Optimization in LLMs

- Authors: Xiaozhe Li, Xinyu Fang, Shengyuan Ding, Yang Li, Linyang Li, Haodong Duan, Qingwen Liu, Kai Chen
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.6141916165340042
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1413/
- PDF: https://aclanthology.org/2026.findings-acl.1413.pdf
- Local PDF: pdf/2026-10-19_04_Forge_ Quality-Aware Reinforcement Learning for NP-Hard Optimization in LLMs.pdf

Large Language Models (LLMs) have achieved remarkable success on reasoning benchmarks through Reinforcement Learning with Verifiable Rewards (RLVR), excelling at tasks such as math, coding, logic and puzzles. However, existing benchmarks evaluate only correctness, overlooking optimality—the ability to find the best solutions under constraints. We propose , the first comprehensive framework for training and evaluating LLMs on NP-hard optimization problems through quality-aware RLVR. provides three key components: a scalable training infrastructure with instance generators, quality verifiers, and optimal baselines across 10 tasks; a rigorous benchmark with 1,000 instances evaluating both feasibility (Success Rate) and quality (Quality Ratio); and quality-aware rewards enabling continuous improvement beyond binary correctness. Training on Qwen2.5-7B-Instruct-1M with 15K examples achieves 93.1% SR and 46.6% QR, significantly outperforming GPT-4o (29.6% SR, 14.6% QR). Beyond optimization, training on transfers to diverse tasks: mathematics (+2.2%), logic (+1.2%), knowledge (+4.1%), and instruction-following (+6.1%). Our analysis reveals quality-aware rewards improve solutions by 28.8% over binary rewards, and task diversity drives generalization more than data quantity—offering insights into RLVR scaling for complex reasoning.

## 5. ToxReason: A Benchmark for Mechanistic Chemical Toxicity Reasoning via Adverse Outcome Pathway

- Authors: Jueon Park, WonJune Jang, Chanhwi Kim, Yein Park, Jaewoo Kang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.6139047044664854
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.977/
- PDF: https://aclanthology.org/2026.findings-acl.977.pdf
- Local PDF: pdf/2026-10-19_05_ToxReason_ A Benchmark for Mechanistic Chemical Toxicity Reasoning via Adverse Outcome Pathway.pdf

Recent advances in large language models (LLMs) have enabled molecular reasoning for property prediction. However, toxicity arises from complex biological mechanisms beyond chemical structure, necessitating mechanistic reasoning for reliable prediction. Despite its importance, current benchmarks fail to systematically evaluate this capability. LLMs can generate fluent but biologically unfaithful explanations, making it difficult to assess whether predicted toxicities are grounded in valid mechanisms. To bridge this gap, we introduce ToxReason, a benchmark grounded in the Adverse Outcome Pathway (AOP) that evaluates organ-level toxicity reasoning across multiple organs. ToxReason integrates experimental drug–target interaction evidence with toxicity labels, requiring models to infer both toxic outcomes and their underlying mechanisms from Molecular Initiating Event (MIE) to Adverse Outcome (AO). Using ToxReason, we evaluate toxicity prediction performance and reasoning quality across diverse LLMs. We find that strong predictive performance does not necessarily imply reliable reasoning. Furthermore, we show that reasoning-aware training improves mechanistic reasoning and, consequently, toxicity prediction performance. Together, these results underscore the necessity of integrating reasoning into both evaluation and training for trustworthy toxicity modeling.

## 6. ProCeedRL: Process Critic with Explorative Demonstration Reinforcement Learning for LLM Agentic Reasoning

- Authors: Jingyue Gao, Yanjiang Guo, Chen Xiaoshuai, Jianyu Chen
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.613167415174171
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.800/
- PDF: https://aclanthology.org/2026.findings-acl.800.pdf
- Local PDF: pdf/2026-10-19_06_ProCeedRL_ Process Critic with Explorative Demonstration Reinforcement Learning for LLM Agentic Reasoning.pdf

Reinforcement Learning (RL) significantly enhances the reasoning abilities of large language models (LLMs), yet applying it to multi-turn agentic tasks remains challenging due to the long-horizon nature of interactions and the stochasticity of environmental feedback.We identify a structural failure mode in agentic exploration: suboptimal actions elicit noisy observations into misleading contexts, which further weaken subsequent decision-making, making recovery increasingly difficult.This cumulative feedback loop of errors renders standard exploration strategies ineffective and susceptible to the model’s reasoning and the environment’s randomness.To mitigate this issue, we propose ProCeedRL : Pro cess C ritic with E xplorativ e D emonstration RL, shifting exploration from passive selection to active intervention.ProCeedRL employs a process-level critic to monitor interactions in real time, incorporating reflection-based demonstrations to guide agents in stopping the accumulation of errors.We find that this approach significantly exceeds the model’s saturated exploration performance, demonstrating substantial exploratory benefits.By learning from exploratory demonstrations and on-policy samples, ProCeedRL significantly improves exploration efficiency and achieves superior performance on complex deep search and embodied tasks.

## 7. PathBuilder: A Quality-Controlled LLM System for Personalized Learning Pathways

- Authors: Jasper Meynard Arana, John Andrew Mañacop, John Allen Manacop, Roy Andrew Garcia, Keith Rick Piniera, Kristine Ann M. Carandang, Ethan Robert Casin, Christian Alis, Christopher Monterola
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.6131242749780084
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-demo.50/
- PDF: https://aclanthology.org/2026.acl-demo.50.pdf
- Local PDF: pdf/2026-10-19_07_PathBuilder_ A Quality-Controlled LLM System for Personalized Learning Pathways.pdf

Large language models (LLMs) enable scalable content generation for personalized learning, but reliability and pedagogical alignment remain open challenges. We present PathBuilder, a web-based system that integrates expert-validated assessment, retrieval-augmented generation (RAG), and an LLM-as-a-Judge validation loop within a closed instructional pipeline. The system uses a 17,758-item curriculum-aligned question bank, including 1,018 expert-approved LLM-generated items, to construct diagnostic and post-tests for fine-grained learner profiling. In a real-world deployment with 179 registered users (75 matched learners), PathBuilder achieved a mean absolute gain of 37.9 percentage points, Hake’s normalized gain of 0.760, and a large effect size (Cohen’s d = 0.98). A controlled study of the judge mechanism showed consistent high-quality instructional outputs with a 100% threshold pass rate. These results demonstrate that structured curriculum alignment combined with retrieval grounding and automated validation can support reliable LLM-based personalization in deployed learning systems. A live demonstration of PathBuilder is available at https://demo.pathbuilderedu.com .

## 8. Detecting RAG Extraction Attack via Dual-Path Runtime Integrity Game

- Authors: Yuanbo Xie, Yingjie Zhang, Yulin Li, Shouyou Song, Xiaokun Chen, Zhihan Liu, Liya Su, Tingwen Liu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.6130751848496874
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.385/
- PDF: https://aclanthology.org/2026.acl-long.385.pdf
- Local PDF: pdf/2026-10-19_08_Detecting RAG Extraction Attack via Dual-Path Runtime Integrity Game.pdf

Retrieval-Augmented Generation (RAG) systems augment large language models with external knowledge, yet introduce a critical security vulnerability: RAG Knowledge Base Leakage, wherein adversarial prompts can induce the model to divulge retrieved proprietary content. Recent studies reveal that such leakage can be executed through adaptive and iterative attack strategies (named RAG extraction attack), while effective countermeasures remain notably lacking. To bridge this gap, we propose CanaryRAG, a runtime defense mechanism inspired by stack canaries in software security. CanaryRAG embeds carefully designed canary tokens into retrieved chunks and reformulates RAG extraction defense as a dual-path runtime integrity game. Leakage is detected in real time whenever either the target or oracle path violates its expected canary behavior, including under adaptive suppression and obfuscation. Extensive evaluations against existing attacks demonstrate that CanaryRAG provides robust defense, achieving substantially lower chunk recovery rates than state-of-the-art baselines while imposing negligible impact on task performance and inference latency. Moreover, as a plug-and-play solution, CanaryRAG can be seamlessly integrated into arbitrary RAG pipelines without requiring retraining or structural modifications, offering a practical and scalable safeguard for proprietary data.

## 9. From 1,000,000 Users to Every User: Scaling Up Personalized Preference for User-level Alignment

- Authors: Jia-Nan Li, Jian Guan, Songhao Wu, Wei Wu, Rui Yan
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.6129469346616574
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1391/
- PDF: https://aclanthology.org/2026.acl-long.1391.pdf
- Local PDF: pdf/2026-10-19_09_From 1,000,000 Users to Every User_ Scaling Up Personalized Preference for User-level Alignment.pdf

Large language models (LLMs) have traditionally been aligned through one-size-fits-all approaches that assume uniform human preferences, fundamentally overlooking the diversity in user values and needs. This paper introduces a comprehensive framework for scalable personalized alignment of LLMs. We establish a systematic preference space characterizing psychological and behavioral dimensions, alongside diverse persona representations for robust preference inference in real-world scenarios. Building upon this foundation, we introduce AlignX, a large-scale dataset of over 1.3 million personalized preference examples, and develop two complementary alignment approaches: in-context alignment directly conditioning on persona representations and preference-bridged alignment modeling intermediate preference distributions. Extensive experiments demonstrate substantial improvements over existing methods, with an average 17.06% accuracy gain across four benchmarks while exhibiting a strong adaptation capability to novel preferences, robustness to limited user data, and precise preference controllability. These results validate our approach toward user-adaptive AI systems.

## 10. Multi-View Attention Multiple-Instance Learning Enhanced by LLM Reasoning for Cognitive Distortion Detection

- Authors: Jun Seo Kim, Hyemi Kim, Woo Joo OH, Hongjin Cho, Hochul Lee, Hye Hyeon Kim
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.612914714783618
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1691/
- PDF: https://aclanthology.org/2026.acl-long.1691.pdf
- Local PDF: pdf/2026-10-19_10_Multi-View Attention Multiple-Instance Learning Enhanced by LLM Reasoning for Cognitive Distortion Detection.pdf

Cognitive distortions have been closely linked to mental health disorders, yet their automatic detection remains challenging due to contextual ambiguity, co-occurrence, and semantic overlap. We propose a novel framework that combines Large Language Models (LLMs) with a Multiple-Instance Learning (MIL) architecture to enhance interpretability and expression-level reasoning. Each utterance is decomposed into Emotion, Logic, and Behavior (ELB) components, which are processed by LLMs to infer multiple distortion instances, each with a predicted type, expression, and model-assigned salience score. These instances are integrated via a Multi-View Gated Attention mechanism for final classification. Experiments on Korean (KoACD) and English (Therapist QA) datasets demonstrate that incorporating ELB and LLM-inferred salience scores improves classification performance, especially for distortions with high interpretive ambiguity. Our results suggest a psychologically grounded and generalizable approach for fine-grained reasoning in mental health NLP. The dataset and implementation details are publicly accessible.

## 11. DeepPrune: Parallel Scaling without Inter-trace Redundancy

- Authors: Shangqing Tu, Yaxuan Li, Yushi Bai, Lei Hou, Juanzi Li
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.6127986808938806
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.656/
- PDF: https://aclanthology.org/2026.findings-acl.656.pdf
- Local PDF: pdf/2026-10-19_11_DeepPrune_ Parallel Scaling without Inter-trace Redundancy.pdf

Parallel scaling has emerged as a powerful paradigm to enhance reasoning capabilities in large language models (LLMs) by generating multiple Chain-of-Thought (CoT) traces simultaneously. However, this approach introduces significant computational inefficiency due to inter-trace redundancy —our analysis reveals that over 80% of parallel reasoning traces yield identical final answers, representing substantial wasted computation. To address this critical efficiency bottleneck, we propose DeepPrune , a novel framework that enables efficient parallel scaling through dynamic pruning. Our method features a specialized judge model trained with oversampling techniques to accurately predict answer equivalence from partial reasoning traces, achieving 0.7072 AUROC on equivalence prediction across unseen reasoning models. This is combined with an online greedy clustering algorithm that dynamically prunes redundant paths while preserving answer diversity. Comprehensive evaluations across three challenging benchmarks (AIME 2024, AIME 2025, and GPQA) and multiple reasoning models demonstrate that DeepPrune achieves remarkable token reduction ranging from 65.73% to 88.50% compared to conventional consensus sampling, while maintaining competitive accuracy within 3.4 percentage points. Our work establishes a new standard for efficient parallel reasoning, making high-performance reasoning more efficient. Our code and data are here: https://github.com/THU-KEG/DeepPrune/

## 12. AutoL2S: Auto Long-Short Reasoning for Efficient Large Language Models

- Authors: Feng Luo, Yu-Neng Chuang, Guanchu Wang, Hoang Anh Duy Le, Shaochen Zhong, Hongyi Liu, Jiayi Yuan, Yang Sui, Vladimir Braverman, Vipin Chaudhary, Xia Hu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.6127677876669186
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.831/
- PDF: https://aclanthology.org/2026.findings-acl.831.pdf
- Local PDF: pdf/2026-10-19_12_AutoL2S_ Auto Long-Short Reasoning for Efficient Large Language Models.pdf

Reasoning-capable large language models (LLMs) achieve strong performance on complex tasks but often exhibit overthinking after distillation, generating unnecessarily long chain-of-thought (CoT) reasoning even for simple inputs and incurring high inference cost. However, naively shortening reasoning length can degrade reasoning accuracy, as concise reasoning may be insufficient for certain inputs and lacks explicit supervision. We propose Auto Long-Short Reasoning (AutoL2S), a distillation framework that empowers non-reasoning LLMs to think thoroughly but only when necessary. AutoL2S first learns a lightweight switching token with verified long-short CoTs to enable instance-wise long-short reasoning selection. Then it leverages long-short reasoning rollouts induced by switching tokens within a GRPO-style loss to improve reasoning efficiency while maintaining accuracy. Experiments demonstrate that AutoL2S effectively reduces reasoning length up to 71% with minimal accuracy loss, yielding markedly better trade-off in token length and inference time while preserving accuracy. The code is available at https://github.com/amandaluof/AutoL2S .

## 13. ProFit: Leveraging High-Value Signals in SFT via Probability-Guided Token Selection

- Authors: Tao Liu, Taiqiang Wu, Runming Yang, Shaoning Sun, Junjie Wang, Yujiu Yang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.612745483517041
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.755/
- PDF: https://aclanthology.org/2026.findings-acl.755.pdf
- Local PDF: pdf/2026-10-19_13_ProFit_ Leveraging High-Value Signals in SFT via Probability-Guided Token Selection.pdf

Supervised fine-tuning (SFT) is a fundamental post-training strategy to align Large Language Models (LLMs) with human intent. However, traditional SFT often ignores the one-to-many nature of language by forcing alignment with a single reference answer, leading to the model overfitting to non-core expressions. Although our empirical analysis suggests that introducing multiple reference answers can mitigate this issue, the prohibitive data and computational costs necessitate a strategic shift: prioritizing the mitigation of single-reference overfitting over the costly pursuit of answer diversity. To achieve this, we reveal the intrinsic connection between token probability and semantic importance: high-probability tokens carry the core logical framework, while low-probability tokens are mostly replaceable expressions. Based on this insight, we propose ProFit , which selectively masks low-probability tokens to prevent surface-level overfitting. Extensive experiments confirm that ProFit consistently outperforms traditional SFT baselines on general reasoning and mathematical benchmarks

## 14. Sparse-RL: Breaking the Memory Wall in LLM Reinforcement Learning via Stable Sparse Rollouts

- Authors: Sijia Luo, Xiaokang Zhang, Yuxuan Hu, Bohan Zhang, Ke Wang, Jinbo Su, Mengshu Sun, Lei Liang, Jing Zhang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.6123229043161666
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.2000/
- PDF: https://aclanthology.org/2026.acl-long.2000.pdf
- Local PDF: pdf/2026-10-19_14_Sparse-RL_ Breaking the Memory Wall in LLM Reinforcement Learning via Stable Sparse Rollouts.pdf

Reinforcement Learning (RL) has become essential for eliciting complex reasoning capabilities in Large Language Models (LLMs). However, the substantial memory overhead of storing Key-Value (KV) caches during long-horizon rollouts acts as a critical bottleneck, often prohibiting efficient training on limited hardware. While existing KV compression techniques offer a remedy for inference, directly applying them to RL training induces a severe policy mismatch, leading to catastrophic performance collapse. To address this, we introduce Sparse-RL, which empowers stable RL training under sparse rollouts. We show that instability arises from a fundamental policy mismatch among the dense old policy, the sparse sampler policy, and the learner policy. To mitigate this issue, Sparse-RL incorporates Sparsity-Aware Rejection Sampling and Importance-based Reweighting to correct the off-policy bias introduced by compression-induced information loss. Experimental results show that Sparse-RL reduces rollout overhead compared to dense baselines while preserving the performance. Furthermore, Sparse-RL inherently implements sparsity-aware training, significantly enhancing model robustness during sparse inference deployment.

## 15. DeReA: Improving Idiom Translation with Detect-Retrieve-Arbitrate Reasoning

- Authors: Rongqing Jiang, Xuebo Liu, Shengxin Liu, Yutong Wang, Min Zhang, Shimin Tao, Daimeng Wei, Min Zhang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.612175450865845
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.299/
- PDF: https://aclanthology.org/2026.acl-long.299.pdf
- Local PDF: pdf/2026-10-19_15_DeReA_ Improving Idiom Translation with Detect-Retrieve-Arbitrate Reasoning.pdf

Idiom translation remains a formidable challenge for Large Language Models (LLMs), as the constraints of static parametric memory and the noise in sentence-level retrieval often lead to literal misinterpretations. To address this, we propose DeReA, a detect-retrieve-arbitrate framework. The system employs a preference-aligned detector to identify idiomatic spans by reasoning over semantic conflicts between literal and contextual meanings. Subsequently, an idiom-centric translator invokes a fine-tuned embedding model to efficiently retrieve canonical definitions from an external knowledge base. The translator then utilizes a dual-path arbitration mechanism to select the optimal rendering by weighing the retrieval-augmented translations against direct translation. To evaluate our framework, we introduce LoMI, a high-difficulty benchmark with low data contamination. Experimental results demonstrate that DeReA significantly enhances performance across various model scales, improving GPT-5-mini by over 5.2 points in both idiomatic quality and consistency according to LLM-based metrics. Furthermore, evaluations on an emerging slang dataset from Urban Dictionary validate the potential of our approach in handling novel and evolving linguistic data. Our code is available at https://github.com/jrongqing/DeReA .

## 16. Beyond Static Benchmarks: Synthesizing Harmful Content via Persona-based Simulation for Robust Evaluation

- Authors: Huije Lee, Jisu Shin, Hoyun Song, Changgeon Ko, Jong C. Park
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.6121020672732875
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1741/
- PDF: https://aclanthology.org/2026.acl-long.1741.pdf
- Local PDF: pdf/2026-10-19_16_Beyond Static Benchmarks_ Synthesizing Harmful Content via Persona-based Simulation for Robust Evaluation.pdf

Static benchmarks for harmful content detection face limitations in scalability and diversity, and may also be affected by contamination from web-scale pre-training corpora. To address these issues, we propose a framework for synthesizing harmful content, leveraging persona-guided large language model (LLM) agents. Our approach constructs two-dimensional user personas by integrating demographic identities and topical interests with situational harmful strategies, enabling the simulation of diverse and contextually grounded harmful interactions. We evaluate the framework along three dimensions: harmfulness, challenge level, and diversity. Both human and LLM-based evaluations confirm that our framework achieves a high harmful generation success rate. Experiments across multiple detection systems reveal that our synthetic scenarios are more challenging to detect than those in existing benchmarks. Furthermore, a multi-faceted analysis confirms that our approach achieves linguistic and topical diversity comparable to human-curated datasets, establishing our framework as an effective tool for robust stress-testing of harmful content detection systems.

## 17. Analyzing and Internalizing Complex Policy Documents for LLM Agents

- Authors: Jiateng Liu, Zhenhailong Wang, Xiaojiang Huang, Yingjie Li, Xiang Li, Chenlei Guo, Xing Fan, Ruhi Sarikaya, Heng Ji
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.6120569064962424
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.767/
- PDF: https://aclanthology.org/2026.acl-long.767.pdf
- Local PDF: pdf/2026-10-19_17_Analyzing and Internalizing Complex Policy Documents for LLM Agents.pdf

Large language model agents rely on in-context policy documents encoding diverse business rules. As businesses scale, these documents grow, creating substantial computational overhead and motivating internalization methods that embed policy into model priors. Prior work focuses on generic prompts, but we find agentic policies span multiple complexity levels and demand heavier reasoning, posing greater challenges. We introduce an agentic benchmark generator with Controllable Complexity in agent policy across four levels, enabling systematic evaluation of agents under increasing complexity and providing a testbed for policy internalization. Our analysis shows that workflow-governing policy specifications are the hardest to reason over, and that SFT on gold trajectories with chain-of-thought is data-hungry and struggles at high complexity. We propose Category-Aware Policy Continued Pretraining, an automated pipeline that analyzes policies, extracts key specifications, categorizes them into factual, behavioral, and conditional types, and isolates those driving workflow complexity. This enables targeted “therapy” by synthesizing specialized training data for each type and improving internalization via an autoregressive pretraining loss. Extensive experiments show our synthetic data and objective consistently improve performance. Combined with SFT, our method outperforms the baseline across different settings, especially in data-sparse and high-complexity regimes, with gains up to 41% and 22% on Qwen-3-32B. Overall, we achieve 97.3% prompt reduction on our benchmark, and on 𝜏 -Bench we further improve performance while reducing prompt requirements with very limited SFT data.

## 18. Mixture-of-Minds: Multi-Agent Reinforcement Learning for Table Understanding

- Authors: Yuhang Zhou, Mingrui Zhang, Ke Li, Mingyi Wang, Qiao Liu, Qifei Wang, Jiayi Liu, Fei Liu, Serena Li, Weiwei LI, Mingze Gao, Abhishek Kumar, Xiangjun Fan, Zhuokai Zhao, Lizhu Zhang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.6116707518248305
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.112/
- PDF: https://aclanthology.org/2026.acl-long.112.pdf
- Local PDF: pdf/2026-10-19_18_Mixture-of-Minds_ Multi-Agent Reinforcement Learning for Table Understanding.pdf

Understanding and reasoning over tables is a critical capability for many real-world applications. Large language models (LLMs) have shown promise on this task, but current approaches remain limited. Fine-tuning based methods strengthen language reasoning; yet they are prone to arithmetic errors and hallucination. In contrast, tool-based methods enable precise table manipulation but rely on rigid schemas and lack semantic understanding. These complementary drawbacks highlight the need for approaches that integrate robust reasoning with reliable table processing. In this work, we propose MIXTURE-OF-MINDS, a multi-agent framework that decomposes table reasoning into three specialized roles: planning, coding, and answering. This design enables each agent to focus on a specific aspect of the task while leveraging code execution for precise table manipulation. Building on this workflow, we introduce a self-improvement training framework that employs Monte Carlo Tree Search (MCTS) rollouts to generate pseudo-gold trajectories and optimize agents with reinforcement learning (RL). Extensive experiments show that MIXTURE-OF-MINDS delivers substantial gains, reaching 62.13% on TableBench and surpassing GPT-o3-mini. These results demonstrate the promise of combining structured multi-agent workflows with RL to advance table understanding.

## 19. Focusing Condition: Inference-Time Self-Contrastive Steering Elicits Better Conditional Text Embeddings in LLMs

- Authors: Zifeng Cheng, Lingyun Qian, Zhiwei Jiang, Cong Wang, Yafeng Yin, Fei Shen, Ao Zhou, Qing Gu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.611575682514142
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.50/
- PDF: https://aclanthology.org/2026.acl-long.50.pdf
- Local PDF: pdf/2026-10-19_19_Focusing Condition_ Inference-Time Self-Contrastive Steering Elicits Better Conditional Text Embeddings in LLMs.pdf

Extracting conditional text embeddings from large language models (LLMs) is a promising paradigm, as it requires neither additional data nor fine-tuning. Existing methods incorporate conditions into prompts to guide LLMs to focus on specific aspects and elicit conditional text embeddings. However, relying solely on prompts often fails to produce high-quality conditional text embeddings, as they remain entangled with general text embeddings, ultimately degrading their quality. To this end, we propose an inference-time, plug-and-play Self-Contrastive Steering (SCS) method that constructs unconditional general text embeddings and uses them to refine conditional text embeddings, making them more focused on the target condition. Specifically, we modify the attention mask and positional encodings to mask the condition, thereby obtaining unconditional text embeddings and intervening in the multi-head self-attention computation process. Notably, our method is highly efficient, requiring only a single additional multi-head self-attention computation at inference time. Extensive experiments on clustering, Semantic Textual Similarity, and triplet alignment datasets demonstrate that our method can seamlessly improve the performance of existing prompt-based methods across different LLMs in a training-free and plug-and-play manner.

## 20. Causal-Audit: Explicit and Auditable Graph-based Reasoning via Target-Aware Causal Chain Construction

- Authors: Su Lan, Xuefei Yin, Yanming Zhu, Alan Wee-Chung Liew
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.611028667094093
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.607/
- PDF: https://aclanthology.org/2026.findings-acl.607.pdf
- Local PDF: pdf/2026-10-19_20_Causal-Audit_ Explicit and Auditable Graph-based Reasoning via Target-Aware Causal Chain Construction.pdf

Causal and intervention-based question answering is fundamental to advancing large language models (LLMs) toward reasoning beyond surface-level correlations and understanding underlying causal mechanisms. However, existing LLM-based methods often rely on implicit language-level reasoning, resulting in opaque causal assumptions, unverifiable reasoning paths, and fragile predictions under complex interventions, particularly in context-free settings. In this paper, we propose an explicit and auditable causal reasoning framework for context-free intervention-based question answering. Our method formulates causal inference as structured reasoning over an explicit causal graph through four modular stages, rather than implicit end-to-end prediction. A key innovation is a target-aware causal graph construction strategy that treats the target variable as a core constraint during graph expansion, effectively suppressing irrelevant variables, spurious causal relations, and reasoning noise. We further introduce a path-level causal evidence aggregation mechanism that combines multiple causal paths while modeling both reinforcing and counteracting effects, enabling robust decision-making beyond single-chain reasoning. Extensive experiments on three benchmarks demonstrate that our framework consistently outperforms existing LLM-based methods while providing interpretable and auditable causal reasoning traces.

## 21. MM-PoisonRAG: Disrupting Multimodal RAG with Local and Global Knowledge Poisoning Attacks

- Authors: Hyeonjeong Ha, Qiusi Zhan, Jeonghwan Kim, Dimitrios Bralios, Saikrishna Sanniboina, Nanyun Peng, Kai-Wei Chang, Daniel Kang, Heng Ji
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.6107408184599192
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1558/
- PDF: https://aclanthology.org/2026.acl-long.1558.pdf
- Local PDF: pdf/2026-10-19_21_MM-PoisonRAG_ Disrupting Multimodal RAG with Local and Global Knowledge Poisoning Attacks.pdf

Retrieval-augmented generation (RAG) has become a common practice in multimodal large language models (MLLM) to enhance factual grounding and reduce hallucination. Yet, its reliance on retrieval exposes MLLMs to knowledge poisoning attacks, in which adversaries deliberately inject malicious multimodal content into external knowledge bases to steer models toward generating incorrect or even harmful responses. We present MM-PoisonRAG, a framework to systematically study the vulnerability of multimodal RAG under knowledge poisoning. Specifically, we design two novel attack strategies: Localized Poisoning Attack (LPA), which implants targeted, query-specific multimodal misinformation to manipulate outputs toward attacker-controlled responses, and Globalized Poisoning Attack (GPA), which uses a single, untargeted adversarial injection to broadly corrupt reasoning and collapse generation quality across all queries. Extensive experiments on diverse tasks, multimodal RAG components, and attacker access levels reveal severe vulnerabilities: LPA achieves up to 56% attack success rate even under restricted access, and transfers effectively across four different retrievers without re-optimizing the adversaries. GPA completely disrupts model generation to 0% accuracy with just one poisoned content. Moreover, both LPA and GPA bypass existing defenses, underscoring the fragility of multimodal RAG and establishing MM-PoisonRAG as a foundation for future research on securing RAG frameworks against multimodal knowledge poisoning.

## 22. CTRAP: Embedding Collapse Trap to Safeguard Large Language Models from Harmful Fine-Tuning

- Authors: Biao Yi, Tiansheng Huang, Baolei Zhang, Tong Li, Lihai Nie, Zheli Liu, Li Shen
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.6105078215904634
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.455/
- PDF: https://aclanthology.org/2026.acl-long.455.pdf
- Local PDF: pdf/2026-10-19_22_CTRAP_ Embedding Collapse Trap to Safeguard Large Language Models from Harmful Fine-Tuning.pdf

Fine-tuning-as-a-service, while commercially successful for Large Language Model (LLM) providers, exposes models to harmful fine-tuning attacks. As a widely explored defense paradigm against such attacks, unlearning attempts to remove malicious knowledge from LLMs, thereby essentially preventing them from being used to perform malicious tasks. However, we highlight a critical flaw: the inherent general adaptability of LLMs allows them to easily bypass selective unlearning by rapidly relearning or repurposing their general capabilities for harmful tasks. To address this fundamental limitation, we propose a paradigm shift: instead of selective removal, we advocate for inducing model collapse, effectively forcing the model to ”unlearn everything”, specifically in response to updates characteristic of malicious adaptation. This collapse directly neutralizes the very general capabilities that attackers exploit, tackling the core issue unaddressed by selective unlearning. We introduce the Collapse Trap (CTRAP) as a practical mechanism to implement this concept conditionally. Embedded during alignment, CTRAP pre-configures the model’s reaction to subsequent fine-tuning dynamics. If updates during fine-tuning constitute a persistent attempt to reverse safety alignment, the pre-configured trap triggers a progressive degradation of the model’s core language modeling abilities, ultimately rendering it inert and useless for the attacker. Crucially, this collapse mechanism remains dormant during benign fine-tuning, ensuring the model’s utility and general capabilities are preserved.

## 23. Beyond Prompt Engineering: A Systematic Analysis of Prompt Lexical Sensitivity and Its Impacts on Quality

- Authors: Qipeng Xie, Zi Liang, Jiafei Wu, Yufei Chen, Weizheng Wang, Wenao Ma, Zhong Ming, Haiqin Yang, Kaishun Wu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.6104119389360902
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.2084/
- PDF: https://aclanthology.org/2026.findings-acl.2084.pdf
- Local PDF: pdf/2026-10-19_23_Beyond Prompt Engineering_ A Systematic Analysis of Prompt Lexical Sensitivity and Its Impacts on Quality.pdf

Large Language Models (LLMs) often exhibit extreme sensitivity to surface-level prompt variations, where minor lexical perturbations trigger disproportionate performance fluctuations. Moving beyond black-box optimization or coarse-grained templates, we conduct the first analysis of n-gram token-level mechanisms, leveraging a large-scale dataset of 132,000 prompt variants. Our investigation uncovers the Scaling Law of Prompt Performance Stability: higher average performance is inherently associated with lower variance and greater stability. We identify that this robustness is driven by two linguistic pillars: Domain-Specific Terminology, which anchors semantic boundaries, and Explicit Action Directives, which formalize reasoning trajectories. By narrowing the model’s interpretative space, these patterns effectively “lock” the generation process. We operationalize these findings into an automated Prompt-Refining Agent that autonomously restructures queries via domain anchoring and operational constraints. Empirical results show a 40.7% reduction in performance variance for code generation, offering a statistically grounded framework for robust prompt engineering.

## 24. Role-Sensitive Neurons: A Neuron-Level Gain Control Mechanism for Confidence Steering

- Authors: Peiwen Huang, Chih-Hao Hsu, Tzu-Hung Huang, Shou-De Lin
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.6103850707853447
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.294/
- PDF: https://aclanthology.org/2026.findings-acl.294.pdf
- Local PDF: pdf/2026-10-19_24_Role-Sensitive Neurons_ A Neuron-Level Gain Control Mechanism for Confidence Steering.pdf

Role-playing prompts effectively steer Large Language Models (LLMs), yet the neural mechanism driving this behavioral shift remains unclear. In this work, we identify Role-Sensitive Neurons (RSNs)—a sparse sub-network (≈ 0.5% of all neurons) governing the transition from hesitation to action. Using a novel evaluation framework with explicit abstention (MMLU-E), we reveal a Confidence-Performance Decoupling: roles primarily modulate the model’s probabilistic “willingness to act” rather than its underlying knowledge representation. We demonstrate that RSNs function as a mechanistic gain control system: causal intervention on this subspace allows precise regulation of abstention behavior. Furthermore, cross-model transfer experiments confirm that these circuits are indigenous to pre-training, with Instruction Tuning (SFT) acting merely as a “signal sharpener” to refine latent gain dynamics. Finally, we identify a critical safety boundary: in knowledge-deficient models, amplifying RSNs induces “unwarranted certainty,” highlighting decisiveness as a tunable gain parameter distinct from epistemic truth.

## 25. EviReport: From Reasoned Outlines to Evidence Tracked Long-Form Reports

- Authors: Zihan Liu, Jianhui li, Zexin Wang, Fei Sun, Jingjing LI, Zheyuan Li, Ke Xiang, Hang Cui, Houhua Gong, Changhua Pei, Gaogang Xie
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.6103501732003656
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1397/
- PDF: https://aclanthology.org/2026.findings-acl.1397.pdf
- Local PDF: pdf/2026-10-19_25_EviReport_ From Reasoned Outlines to Evidence Tracked Long-Form Reports.pdf

Evidence-intensive analytical reports are expected to be fact-dense, quantitatively correct, and supported by figures. Yet one-shot long-form generation with large language models (LLMs) frequently produces fluent but under-supported drafts: core facts are missed, numbers drift, and key visuals are absent, making the report hard to trust. We propose EviReport, an evidence-tracked report-writing workflow that improves reliability by (i) organizing corpus evidence into compact, traceable units and retrieves query-relevant subgraphs into retrieval-ready packages (ii) leveraging a reasoning-focused LLM sketches a high-level plan for full coverage, then a chat-based LLM sharpens it into a detailed hierarchical outline with explicit scope and ordering (iii) rive generation with a facts-first iterative loop: extracting verifiable facts, composing strictly from those facts, then triggering gap-aware append queries to fill missing evidence To evaluate both correctness and completeness, we introduce EviReportBench, a benchmark instantiated on data-rich indicator reports that measures factual accuracy (claim verification), factual coverage (quiz-based evaluation), and visual evidence integration (image recall). Across 8 topics, experiments show that EviReport consistently outperforms strong baselines in factual coverage ( 2.16× ), factual accuracy (+8.9 points), and visual evidence integration (+34 points), approaching the quality of expert-written reports across multiple dimensions.

## 26. SFTMix: Elevating Language Model Instruction Tuning with Mixup Recipe

- Authors: Yuxin Xiao, Shujian Zhang, Marzyeh Ghassemi, Wenxuan Zhou
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.610213570144678
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.78/
- PDF: https://aclanthology.org/2026.acl-long.78.pdf
- Local PDF: pdf/2026-10-19_26_SFTMix_ Elevating Language Model Instruction Tuning with Mixup Recipe.pdf

To acquire instruction-following capabilities, large language models (LLMs) undergo instruction tuning, where they are trained on instruction-response pairs using next-token prediction (NTP). Efforts to improve instruction tuning often focus on higher-quality supervised fine-tuning (SFT) datasets, typically requiring data filtering with proprietary LLMs or human annotation. In this paper, we take a different approach by proposing SFTMix, a novel Mixup-based recipe that elevates LLM instruction tuning without relying on well-curated datasets. We observe that LLMs exhibit uneven confidence across the semantic representation space. We argue that examples with different confidence levels should play distinct roles in instruction tuning: Confident data is prone to overfitting, while unconfident data is harder to generalize. Based on this insight, SFTMix leverages training dynamics to identify examples with varying confidence levels. We then interpolate them to bridge the confidence gap and apply a Mixup-based regularization to support learning on these additional, interpolated examples. We demonstrate the effectiveness of SFTMix in both instruction-following and healthcare-specific SFT tasks, with consistent improvements across LLM families and SFT datasets of varying sizes and qualities. Extensive analyses across six directions highlight SFTMix’s compatibility with data selection, adaptability to compute-constrained scenarios, and scalability to broader applications.

## 27. InfiAgent: An Infinite-Horizon Framework for General-Purpose Autonomous Agents

- Authors: Chenglin Yu, Yuchen Wang, Songmiao Wang, Hongxia Yang, Li Ming
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.6097347536178095
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1787/
- PDF: https://aclanthology.org/2026.findings-acl.1787.pdf
- Local PDF: pdf/2026-10-19_27_InfiAgent_ An Infinite-Horizon Framework for General-Purpose Autonomous Agents.pdf

LLM agents can reason and use tools, but they often break down on long-horizon tasks due to unbounded context growth and accumulated errors. Common remedies such as context compression or retrieval-augmented prompting introduce trade-offs between information fidelity and reasoning stability. We present InfiAgent, a general-purpose framework that keeps the agent’s reasoning context strictly bounded regardless of task duration by externalizing persistent state into a file-centric state abstraction. At each step, the agent reconstructs context from a workspace state snapshot plus a fixed window of recent actions. Experiments on DeepResearch and an 80-paper literature review task show that, without task-specific fine-tuning, InfiAgent with a 20B open-source model is competitive with larger proprietary systems and maintains substantially higher long-horizon coverage than context-centric baselines. These results support explicit state externalization as a practical foundation for stable long-horizon agents.

## 28. Balancing Fidelity and Plasticity: Aligning Mixed-Precision Fine-Tuning with Linguistic Hierarchies

- Authors: Changhai Zhou, Shiyang Zhang, Yuhua Zhou, Jun Gao, Qian Qiao, Shichao Weng, Weizhong Zhang, Cheng Jin
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.6095810696355928
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.779/
- PDF: https://aclanthology.org/2026.findings-acl.779.pdf
- Local PDF: pdf/2026-10-19_28_Balancing Fidelity and Plasticity_ Aligning Mixed-Precision Fine-Tuning with Linguistic Hierarchies.pdf

Deploying and fine-tuning Large Language Models (LLMs) on resource-constrained edge devices requires navigating a strict trade-off between memory footprint and task performance. Existing quantization-aware fine-tuning methods typically decouple weight precision and adapter capacity, overlooking that a layer’s ability to adapt is constrained by the information preserved in its frozen weights. Layers that are highly sensitive to quantization—whether due to representational specialization or accumulated error propagation—can become bottlenecks that adapter rank alone cannot recover. To address this issue, we introduce QR-Adaptor , a unified framework that jointly optimizes per-layer quantization bit-width and LoRA rank. We formulate resource allocation as a multi-objective discrete search guided by empirical layer-wise sensitivity, and implement it with a three-stage pipeline comprising KL-based sensitivity profiling, evolutionary exploration, and Bayesian refinement. Extensive experiments across LLaMA and Qwen models, including modern instruction tuning on OpenOrca and comparisons with strong PEFT baselines such as QDoRA, show that QR-Adaptor establishes a strong Pareto frontier: under a strict 4-bit memory budget, it matches or approaches 16-bit baselines while using substantially less memory.

## 29. Learning on Imbalanced Noisy Data via Debiased Sample Selection and LLM-Driven Annotation

- Authors: Bo Yuan, Yulin Chen, Yin Zhang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.6091464312705313
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1526/
- PDF: https://aclanthology.org/2026.findings-acl.1526.pdf
- Local PDF: pdf/2026-10-19_29_Learning on Imbalanced Noisy Data via Debiased Sample Selection and LLM-Driven Annotation.pdf

Learning with Noisy Labels (LNL) is a challenge where the collected training set can contain incorrect or corrupted labels. Most existing solutions distinguish clean samples from noisy samples and query human experts on noisy samples for denoising. However, these solutions often operate under the unrealistic assumption that the distribution of classes is uniform, overlooking the skewed and imbalanced distributions frequently encountered in real-world scenarios. In this case, we empirically reveal that previous solutions suffer from both selection bias and training bias, leading to distinguish clean samples from noisy samples hardly. In this paper, our work introduces the imbalanced learning with noisy labels (i-LNL) task, which seeks to let the model learn from noisy labels within imbalanced distributions. A new benchmark (ImbaLNL-Bench) comprised of some synthetic and real-world datasets is created to provide a thorough representation of practical use cases. Besides, we propose an innovative collaborative learning framework DeCo for i-LNL tasks. Specifically, we first conduct debiased sample selection, consisting of a robust expert model and a debiased-enhanced threshold strategy, to better separate clean samples from noisy samples, especially for the tail classes. Then we feed selected clean samples to active annotator large language models (LLMs) for re-annotating noisy samples using in-context learning, which can better reduce human effort. Ultimately, we employ distinct loss functions adept at managing subsets with varying degrees of label noise. Extensive experimental results on synthetic and real-world datasets show the effectiveness and superiority of our method.

## 30. Beyond Hard Masks: Progressive Token Evolution for Diffusion Language Models

- Authors: Linhao Zhong, Linyu Wu, Bozhen Fang, Tianjian Feng, Chenchen Jing, Wen Wang, Jiaheng Zhang, Hao Chen, Chunhua Shen
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.6089055811982185
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.315/
- PDF: https://aclanthology.org/2026.acl-long.315.pdf
- Local PDF: pdf/2026-10-19_30_Beyond Hard Masks_ Progressive Token Evolution for Diffusion Language Models.pdf

Diffusion Language Models (DLMs) offer a promising alternative for language modeling by enabling parallel decoding through iterative refinement. However, most DLMs rely on hard binary masking and discrete token assignments, which hinder the revision of early decisions and underutilize intermediate probabilistic representations. In this paper, we propose EvoToken-DLM, a novel diffusion-based language modeling approach that replaces hard binary masks with evolving soft token distributions. EvoToken-DLM enables a progressive transition from masked states to discrete outputs, supporting revisable decoding. To effectively support this evolution, we introduce continuous trajectory supervision, which aligns training objectives with iterative probabilistic updates. Extensive experiments across multiple benchmarks show that EvoToken-DLM consistently achieves superior performance, outperforming strong diffusion-based and masked DLM baselines. Our code is available at https://github.com/aim-uofa/EvoTokenDLM .
