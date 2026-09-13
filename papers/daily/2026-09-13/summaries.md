# Paper Daily Reading - 2026-09-13

## 1. TalkLoRA: Communication-Aware Mixture of Low-Rank Adaptation for Large Language Models

- Authors: Lin Mu, Haiyang Wang, Li Ni, Lei Sang, Zhize Wu, Peiquan Jin, Yiwen Zhang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.7074840762982513
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.840/
- PDF: https://aclanthology.org/2026.acl-long.840.pdf
- Local PDF: pdf/2026-09-13_01_TalkLoRA_ Communication-Aware Mixture of Low-Rank Adaptation for Large Language Models.pdf

Low-Rank Adaptation (LoRA) enables parameter-efficient fine-tuning of Large Language Models (LLMs), and recent Mixture-of-Experts (MoE) extensions further enhance flexibility by dynamically combining multiple LoRA experts. However, existing MoE-augmented LoRA methods assume that experts operate independently, often leading to unstable routing, expert dominance. In this paper, we propose TalkLoRA, a communication-aware MoELoRA framework that relaxes this independence assumption by introducing expert-level communication prior to routing. TalkLoRA equips low-rank experts with a lightweight Talking Module that enables controlled information exchange across expert subspaces, producing a more robust global signal for routing. Theoretically, we show that expert communication smooths routing dynamics by mitigating perturbation amplification while strictly generalizing existing MoELoRA architectures. Empirically, TalkLoRA consistently outperforms vanilla LoRA and MoELoRA across diverse language understanding and generation tasks, achieving higher parameter efficiency and more balanced expert routing under comparable parameter budgets. These results highlight structured expert communication as a principled and effective enhancement for MoE-based parameter-efficient adaptation.

## 2. Why Large Language Models can Secretly Outperform Embedding Similarity in Information Retrieval

- Authors: Matei Benescu, Ivo Pascal de Jong
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.707220308596725
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-srw.5/
- PDF: https://aclanthology.org/2026.acl-srw.5.pdf
- Local PDF: pdf/2026-09-13_02_Why Large Language Models can Secretly Outperform Embedding Similarity in Information Retrieval.pdf

With the emergence of Large Language Models (LLMs), new methods in Information Retrieval are available in which relevance is estimated directly through language understanding and reasoning, instead of embedding similarity. We argue that similarity is a short-sighted interpretation of relevance, and that LLM-Based Relevance Judgment Systems (LLM-RJS) (with reasoning) have potential to outperform Neural Embedding Retrieval Systems (NERS) by overcoming this limitation. Using the TREC-DL 2019 passage retrieval dataset, we compare various LLM-RJS with NERS, but observe no noticeable improvement. Subsequently, we analyze the impact of reasoning by comparing LLM-RJS with and without reasoning. We find that human annotations also suffer from short-sightedness, and that false-positives in the reasoning LLM-RJS are primarily mistakes in annotations due to short-sightedness. We conclude that LLM-RJS do have the ability to address the short-sightedness limitation in NERS, but that this cannot be evaluated with standard annotated relevance datasets.

## 3. MONETA: Multimodal Industry Classification through Geographic Information with Multi Agent Systems

- Authors: Arda Yüksel, Gabriel Thiem, Susanne Walter, Patrick Felka, Gabriela Alves Werb, Ivan Habernal
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.706679579223672
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.674/
- PDF: https://aclanthology.org/2026.acl-long.674.pdf
- Local PDF: pdf/2026-09-13_03_MONETA_ Multimodal Industry Classification through Geographic Information with Multi Agent Systems.pdf

Industry classification schemes are integral parts of public and corporate databases as they classify businesses based on economic activity. Due to the size of the company registers, manual annotation is costly, and fine-tuning models with every update in industry classification schemes requires significant data collection. We replicate the manual expert verification by using existing or easily retrievable multimodal resources for industry classification. We present MONETA, the first multimodal industry classification benchmark with text (Website, Wikipedia, Wikidata) and geospatial sources (OpenStreetMap and satellite imagery). Our dataset enlists 1,000 businesses in Europe with 20 economic activity labels according to EU guidelines (NACE). Our training-free baseline reaches 62.10% and 74.10% with open and closed-source Multimodal Large Language Models (MLLM). We observe an increase of up to 22.80% with the combination of multi-turn design, context enrichment, and classification explanations. We will release our dataset and the enhanced guidelines.

## 4. BioTool: A Comprehensive Tool-Calling Dataset for Enhancing Biomedical Capabilities of Large Language Models

- Authors: Xin Gao, Ruiyi Zhang, Meixi Du, Peijia Qin, Pengtao Xie
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.7063581841836006
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.2138/
- PDF: https://aclanthology.org/2026.acl-long.2138.pdf
- Local PDF: pdf/2026-09-13_04_BioTool_ A Comprehensive Tool-Calling Dataset for Enhancing Biomedical Capabilities of Large Language Models.pdf

Despite the success of large language models (LLMs) on general-purpose tasks, their performance in highly specialized domains such as biomedicine remains unsatisfactory. A key limitation is the inability of LLMs to effectively leverage biomedical tools, which clinical experts and biomedical researchers rely on extensively in daily workflows. While recent general-domain tool-calling datasets have substantially improved the capabilities of LLM agents, existing efforts in the biomedical domain largely rely on in-context learning and restrict models to a small set of tools. To address this gap, we introduce BioTool, a comprehensive biomedical tool-calling dataset designed for fine-tuning LLMs. BioTool comprises 34 frequently used tools collected from the NCBI, Ensembl, and UniProt databases, along with 7,040 high-quality, human-verified query–API call pairs spanning variation, genomics, proteomics, evolution, and general biology. Fine-tuning a 4-billion-parameter LLM on BioTool yields substantial improvements in biomedical tool-calling performance, outperforming cutting-edge commercial LLMs such as GPT-5.1. Furthermore, human expert evaluations demonstrate that integrating a BioTool-fine-tuned tool caller significantly improves downstream answer quality compared to the same LLM without tool usage, highlighting the effectiveness of BioTool in enhancing the biomedical capabilities of LLMs. The full dataset and evaluation code are available at https://github.com/gxx27/BioTool .

## 5. RACC: Regret-Aware Confidence Calibration for Consistent Masked Discrete Diffusion Decoding

- Authors: Qinglin Zeng, Jusheng Zhang, Jing Yang, Ningyuan Liu, Keze Wang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.705699612118653
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1138/
- PDF: https://aclanthology.org/2026.findings-acl.1138.pdf
- Local PDF: pdf/2026-09-13_05_RACC_ Regret-Aware Confidence Calibration for Consistent Masked Discrete Diffusion Decoding.pdf

Masked Discrete Diffusion Models (MDMs) enable parallel generation via iterative refinement. However, we identify a critical decisional mismatch. The MDM architecture is inherently dynamic and capable of sensing context shifts. In contrast, prevailing decoding paradigms remain static and myopic. They treat each denoising step as an isolated snapshot, effectively discarding valuable temporal feedback that signals logical conflicts. To bridge this gap, we propose Regret-Aware Confidence Calibration (RACC). This training-free framework aligns decoding decisions with the model’s latent self-correction capabilities. RACC introduces a momentum anchor to track confidence trajectories. When a token’s probability drops abruptly below its historical trend, the system triggers a “regret” signal. Unlike expensive re-masking or lookahead search, RACC utilizes this signal to proactively demote unstable candidates. Extensive experiments on reasoning benchmarks, such as HumanEval and GSM8K, demonstrate that RACC significantly improves generation consistency. Crucially, RACC achieves these gains with zero additional inference overhead, effectively balancing decoding quality and efficiency.

## 6. Feedback to Reasoning: LLM-Assisted Molecular Optimization with Domain Feedback and Historical Reasoning

- Authors: Wenhan Gao, Xiran Fan, Chin-Chia Michael Yeh, Jiarui Sun, Yuzhong Chen, Menghai Pan, Mahashweta Das, Yi Liu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.705594172249959
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.619/
- PDF: https://aclanthology.org/2026.findings-acl.619.pdf
- Local PDF: pdf/2026-09-13_06_Feedback to Reasoning_ LLM-Assisted Molecular Optimization with Domain Feedback and Historical Reasoning.pdf

The success of large language models (LLMs) across domains highlights their potential in scientific tasks, with molecular optimization being a promising frontier. Traditionally, this optimization relies on iterative expert feedback to refine molecules toward desired properties, a process well aligned with LLMs’ strengths. As an experience-driven task, molecular optimization depends critically on the domain feedback and accumulation of historical knowledge. However, none of the existing methods fully leverages such feedback and historical knowledge with reasoning traces and chemical insights. In this work, we propose F2R: Feedback to Reasoning, a conversational molecular optimization pipeline that enables LLMs to accumulate and retrieve past actions, rationales, and feedback. Like humans, LLMs can generate imperfect reasoning; F2R is the first framework to use detailed domain feedback to critique and improve this reasoning. This transforms LLMs from passive text generators into agentic experts that learn both actions and reasoning from experience. Consequently, F2R shows remarkable performance.

## 7. AutoJudger: An Agent-Driven Framework for Efficient Benchmarking of MLLMs

- Authors: Xuanwen Ding, Chengjun Pan, Zejun Li, Jiwen Zhang, Siyuan Wang, Zhongyu Wei
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.7054271144494315
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.685/
- PDF: https://aclanthology.org/2026.acl-long.685.pdf
- Local PDF: pdf/2026-09-13_07_AutoJudger_ An Agent-Driven Framework for Efficient Benchmarking of MLLMs.pdf

Evaluating multimodal large language models (MLLMs) is becoming increasingly expensive as benchmarks grow in scale and cross-modality complexity. Inspired by structuralism in cognitive psychology, we tackle this difficulty with an adaptive evaluation framework for efficient benchmarking, namely AutoJudger . Instead of passively scoring on a fixed test set, AutoJudger treats evaluation as an interview-like process by keeping a hypothesized ability structure of the evaluated model and actively selecting the informative questions so as to refine these ability boundaries. Specifically, AutoJudger has three core components: ability decomposition to organize evaluation along meaningful capability dimensions, ability estimation to maintain an up-to-date quantitative profile of the model competence, and adaptive question selection to choose the most informative questions. To operationalize this paradigm, we introduce A 2 -Judger , a novel MLLM-based A gentic instantiation of A uto Judger equipped with semantic-aware retrieval and dynamic memory. Experiments on four representative multimodal benchmarks show that A 2 -Judger significantly improves sample efficiency while maintaining reliable evaluation results.

## 8. Retrieval Heads are Dynamic

- Authors: Yuping Lin, Zitao Li, Yue Xing, Pengfei He, Yingqian Cui, Yaliang Li, Bolin Ding, Jingren Zhou, Jiliang Tang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.7051712167188056
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.715/
- PDF: https://aclanthology.org/2026.acl-long.715.pdf
- Local PDF: pdf/2026-09-13_08_Retrieval Heads are Dynamic.pdf

Recent studies have identified “retrieval heads” in Large Language Models (LLMs) responsible for extracting information from input contexts. However, prior works largely rely on static statistics aggregated across datasets, identifying heads that perform retrieval on average. This perspective overlooks the fine-grained temporal dynamics of autoregressive generation. In this paper, we investigate retrieval heads from a dynamic perspective. Through extensive analysis, we establish three core claims: (1) Dynamism: Retrieval heads vary dynamically across timesteps; (2) Irreplaceability: Dynamic retrieval heads are specific at each timestep and cannot be effectively replaced by static retrieval heads; and (3) Correlation: The model’s hidden state encodes a predictive signal for future retrieval head patterns, indicating an internal planning mechanism. We validate these findings on the Needle-in-a-Haystack task and a multi-hop QA task, and quantify the differences on the utility of dynamic and static retrieval heads in a Dynamic Retrieval-Augmented Generation framework. Our study provides new insights into the internal mechanisms of LLMs.

## 9. GR1: Reinforcement-Enhanced LLM for Geoscience Reasoning

- Authors: Yule Xie, Jiaxin Ding, Cheng Deng, Shiqing Gao, Junran Zhang, Sibo Zhang, Zeyuan Wang, Ke Wu, Xin Ding, Luoyi Fu, Meng Jin, Xinbing Wang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.704692856636537
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1140/
- PDF: https://aclanthology.org/2026.findings-acl.1140.pdf
- Local PDF: pdf/2026-09-13_09_GR1_ Reinforcement-Enhanced LLM for Geoscience Reasoning.pdf

Reinforcement learning (RL) has recently shown remarkable ability to enhance reasoning in large language models (LLMs), yet its potential in scientific domains beyond mathematics remains largely unexplored. Geoscience questions couple broad factual knowledge with multi-step inference and often rely on visual evidence such as maps, cross-sections, and diagrams, making them a challenging but verifiable testbed for RL-based reasoning. To enable this study, we introduce GeoMC-10K, a dataset of 10,000 geoscience multiple-choice questions spanning physical to human geography and high-school to professional levels; over 30% of the questions are image dependent. To support text-only RL on these multimodal questions, we design GeoM2T, a multi-agent framework that converts multimodal questions into descriptive text while preserving answerability and difficulty. Fine-tuning LLaMA-3.1-8B and Qwen-3-8B with Group Relative Policy Optimization (GRPO), incorporating a factual reward mechanism, yields GR1, which achieves absolute accuracy improvements of 5.9% and 13.3%, respectively, and it generalizes to out-of-distribution geoscience benchmarks. Together, GeoMC-10K, GeoM2T, and GR1 establish a scalable benchmark and baseline for RL-enhanced geoscience reasoning.

## 10. CuBridge: An LLM-Based Framework for Understanding and Reconstructing High-Performance Attention Kernels

- Authors: Xing Ma, Yangjie Zhou, Wu Sun, Zihan Liu, Jingwen Leng, Yun Lin, Shixuan Sun, Minyi Guo, Jin Song Dong
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.704575943089007
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.500/
- PDF: https://aclanthology.org/2026.acl-long.500.pdf
- Local PDF: pdf/2026-09-13_10_CuBridge_ An LLM-Based Framework for Understanding and Reconstructing High-Performance Attention Kernels.pdf

Efficient CUDA implementations of attention mechanisms are critical to modern deep learning systems, yet supporting diverse and evolving attention variants remains challenging. Existing frameworks and compilers trade performance for flexibility, while expert-written kernels achieve high efficiency but are difficult to adapt. Recent work explores large language models (LLMs) for GPU kernel generation, but prior studies report unstable correctness and significant performance gaps for complex operators such as attention.We present CuBridge, an LLM-based framework that adapts expert-written attention kernels through a structured lift–transfer–lower workflow. CuBridge starts from expert-written CUDA attention kernels and lifts them into an executable intermediate representation that makes execution orchestration explicit while abstracting low-level CUDA syntax. Given a user-provided PyTorch specification, CuBridge generates and verifies a target IR program, then reconstructs optimized CUDA code via reference-guided lowering. Across diverse attention variants and GPU platforms, CuBridge consistently produces correct kernels and substantially outperforms general frameworks, compiler-based approaches, and prior LLM-based methods.

## 11. Multi-Granularity Semantic Revision for Large Language Model Distillation

- Authors: Xiaoyu Liu, Yun Zhang, Wei Li, Simiao Li, Xudong Huang, Hanting Chen, Yehui Tang, Jie Hu, Zhiwei Xiong, Yunhe Wang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.7043517478537913
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.212/
- PDF: https://aclanthology.org/2026.acl-long.212.pdf
- Local PDF: pdf/2026-09-13_11_Multi-Granularity Semantic Revision for Large Language Model Distillation.pdf

Knowledge distillation is crucial for compressing Large Language Models (LLMs), enabling smaller student models to learn from larger teacher models. However, existing LLM distillation methods overly rely on student-generated outputs, which may introduce generation errors and misguide the distillation process. Moreover, existing distillation loss functions struggle to align the most informative part due to the complex output distributions of LLMs. To address these problems, we propose a multi-granularity semantic revision method for LLM distillation. At the sequence level, we propose a sequence correction and re-generation (SCRG) strategy. SCRG identifies error tokens by calculating the semantic cognitive difference between teacher and student outputs, corrects them using teacher-generated tokens, and re-generates the sequence to minimize errors. At the token level, we design a distribution adaptive clipping Kullback-Leibler (DAC-KL) loss, which uses a learnable sub-network to focus on semantically dense areas of the teacher’s output, reducing the impact of redundant information. At the span level, we utilize span priors to compute probability correlations within sequences, ensuring consistency between teacher and student outputs to enhance semantic information transfer. Extensive experiments on models ranging from 0.1B to 13B parameters demonstrate the effectiveness of our approach compared to existing methods.

## 12. Verbal-R3: Verbal Reranker as the Missing Bridge between Retrieval and Reasoning

- Authors: Sangkwon Park, Donghun Kang, Jisoo Mok, Sungroh Yoon
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.703697198871292
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1712/
- PDF: https://aclanthology.org/2026.acl-long.1712.pdf
- Local PDF: pdf/2026-09-13_12_Verbal-R3_ Verbal Reranker as the Missing Bridge between Retrieval and Reasoning.pdf

The conventional Retrieval-Augmented Generation (RAG) paradigm of injecting raw retrieved texts into the Large Language Model (LLM)’s context often results in suboptimal integration of retrieved information. This paper proposes to bridge retrieval results and the LLM’s reasoning ability through Verbal Annotations, analytic narratives that explicitly articulate the logical connection between a search query and retrieved contexts. Our empirical investigation reveals the potential of Verbal Annotations to substantially enhance the LLM’s ability to generate accurate, contextually-grounded responses. Motivated by this finding, we introduce Verbal-R3, a novel agentic RAG framework that consists of a Generator and a Verbal Reranker. The Generator performs iterative retrieval and reasoning, while the Verbal Reranker returns relevance scores and Verbal Annotations to guide the reasoning and answering process of the Generator. The inference process of Verbal-R3 is further refined through relevance-guided test-time scaling, which efficiently allocates test-time compute for effective trajectory expansion. Verbal-R3 achieves state-of-the-art performance on complex Question Answering benchmarks, validating the effectiveness of the proposed framework.

## 13. Long-Chain Reasoning Distillation via Adaptive Prefix Alignment

- Authors: Zhenghao Liu, Zhuoyang Wu, Xinze Li, Yukun Yan, Shuo Wang, Zulong Chen, Yu Gu, Ge Yu, Maosong Sun
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.703434387893436
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.822/
- PDF: https://aclanthology.org/2026.acl-long.822.pdf
- Local PDF: pdf/2026-09-13_13_Long-Chain Reasoning Distillation via Adaptive Prefix Alignment.pdf

Large Language Models (LLMs) have demonstrated remarkable reasoning capabilities, particularly in solving complex mathematical problems. Recent studies show that distilling long reasoning trajectories can effectively enhance the reasoning performance of small-scale student models. However, teacher-generated reasoning trajectories are often excessively long and structurally complex, making them difficult for student models to learn. This mismatch leads to a gap between the provided supervision signal and the learning capacity of the student model. To address this challenge, we propose Prefix-ALIGNment distillation (P-ALIGN), a framework that fully exploits teacher CoTs for distillation through adaptive prefix alignment. Specifically, P-ALIGN adaptively truncates teacher-generated reasoning trajectories by determining whether the remaining suffix is concise and sufficient to guide the student model. Then, P-ALIGN leverages the teacher-generated prefix to supervise the student model, encouraging effective prefix alignment. Experiments on multiple mathematical reasoning benchmarks demonstrate that P-ALIGN outperforms all baselines by over 3%. Further analysis indicates that the prefixes constructed by P-ALIGN provide more effective supervision signals, while avoiding the negative impact of redundant and uncertain reasoning components. All codes are available at https://github.com/NEUIR/P-ALIGN .

## 14. Beyond Single-Shot: Multi-step Tool Retrieval via Query Planning

- Authors: Wei Fang, James R. Glass
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.7030781498673537
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.2090/
- PDF: https://aclanthology.org/2026.findings-acl.2090.pdf
- Local PDF: pdf/2026-09-13_14_Beyond Single-Shot_ Multi-step Tool Retrieval via Query Planning.pdf

LLM agents operating over massive, dynamic tool libraries rely on effective retrieval, yet standard single-shot dense retrievers struggle with complex requests. These failures primarily stem from the disconnect between abstract user goals and technical documentation, and the limited capacity of fixed-size embeddings to model combinatorial tool compositions. To address these challenges, we propose ToolQP, a lightweight framework that models retrieval as iterative query planning. Instead of single-shot matching, ToolQP decomposes instructions into sub-tasks and dynamically generates queries to interact with the retriever, effectively bridging the semantic gap by targeting the specific sub-tasks required for composition. We train ToolQP using synthetic query trajectories followed by optimization with Reinforcement Learning with Verifiable Rewards (RLVR). Experiments demonstrate that ToolQP achieves state-of-the-art performance, exhibiting superior zero-shot generalization, robustness across diverse retrievers, and significant improvements in downstream agentic execution.

## 15. LLM-Driven Multi-Perspective Location Completion for Next Location Prediction

- Authors: Pengxiang Lan, Enneng Yang, Yuliang Liang, Jianzhe Zhao, Linying Jiang, Guibing Guo
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.7027909767436373
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.267/
- PDF: https://aclanthology.org/2026.findings-acl.267.pdf
- Local PDF: pdf/2026-09-13_15_LLM-Driven Multi-Perspective Location Completion for Next Location Prediction.pdf

Next location prediction aims to infer the next location users are likely to visit based on their historical check-in data. However, existing methods assume that check-in data is complete, overlooking the subjective nature of users’ check-in behavior, leading to inaccurate capture of user preferences. Recently, Large Language Models (LLMs) have offered a promising approach to location completion due to their extensive world knowledge. Nevertheless, our experiments reveal that LLMs struggle to interpret raw geographic coordinate information. To address these challenges, we propose LaMDA, an LLM-driven Multi-perspective Data Augmentation framework that employs dual completion agents to complement user mobility behaviors. Driven by our empirical findings that natural language descriptions align more closely with real-world geographic logic, LaMDA translates geographic coordinates into text to enhance spatial reasoning. Leveraging these semantic descriptions, LaMDA constructs dual agents to complement user mobility: “Micro-Level Completion” fills short-term omissions, while “Macro-Level Completion” infers unrecorded locations based on periodic preferences. Reliability is ensured through tailored real-world point-of-interest (POI) pools and a self-verification mechanism. Finally, a collaborative dual-graph module leverages this augmented data for fine-grained preference modeling. Extensive experiments on three real-world datasets demonstrate that LaMDA significantly outperforms state-of-the-art methods.

## 16. Generating Effective CoT Traces for Mitigating Causal Hallucination

- Authors: Yiheng Zhao, Jun Yan
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.702274974491235
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.264/
- PDF: https://aclanthology.org/2026.findings-acl.264.pdf
- Local PDF: pdf/2026-09-13_16_Generating Effective CoT Traces for Mitigating Causal Hallucination.pdf

Although large language models (LLMs) excel in complex reasoning tasks, they suffer from severe causal hallucination in event causality identification (ECI), particularly in smaller models ( ≤ 1.5B parameters). A promising approach to address this issue is to fine-tune them with Chain-of-Thought (CoT) traces. However, there is currently a lack of CoT trace dataset available for ECI. In this paper, we first investigate the essential criteria that effective CoT traces should possess to mitigate causal hallucination in smaller models. We then design a pipeline to generate CoT traces that meet these criteria. Moreover, since there is currently no metric for quantifying causal hallucination, we also introduce a new metric, the Causal Hallucination Rate (CHR), to quantify causal hallucination, guide the formulation of effective CoT trace criteria, and validate the effectiveness of our pipeline. Our experiments show that fine-tuning with the CoT traces generated by our pipeline not only substantially reduces causal hallucination in smaller LLMs but also improves mean accuracy. Moreover, the fine-tuned models exhibit strong cross-dataset and cross-difficulty generalization, as well as robustness under intentionally misleading intervention prompts.

## 17. Learn to Relax with Large Language Models: Solving Constraint Optimization Problems via Bidirectional Coevolution

- Authors: Beidan Liu, Zhengqiu Zhu, Chen Gao, Tianle Pu, Yong Zhao, Wei Qi, Quanjun Yin
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.702074994009114
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.48/
- PDF: https://aclanthology.org/2026.acl-long.48.pdf
- Local PDF: pdf/2026-09-13_17_Learn to Relax with Large Language Models_ Solving Constraint Optimization Problems via Bidirectional Coevolution.pdf

Large Language Model (LLM)-based optimization has recently shown promise for autonomous problem solving, yet most approaches still cast LLMs as passive constraint checkers rather than proactive strategy designers, limiting their effectiveness on complex Constraint Optimization Problems (COPs). To address this, we present AutoCO, an end-to-end Automated Constraint Optimization method that tightly couples operations-research principles of constraint relaxation with LLM reasoning. A core innovation is a unified triple-representation that binds relaxation strategies, algorithmic principles, and executable codes. This design enables the LLM to synthesize, justify, and instantiate relaxation strategies that are both principled and executable. To navigate fragmented solution spaces, AutoCO employs a bidirectional global–local coevolution mechanism, synergistically coupling Monte Carlo Tree Search (MCTS) for global relaxation-trajectory exploration with Evolutionary Algorithms (EAs) for local solution intensification. This continuous exchange of priors and feedback explicitly balances diversification and intensification, thus preventing premature convergence. Extensive experiments on three challenging COP benchmarks validate AutoCO’s consistent effectiveness and superior performance, especially in hard regimes where current methods degrade. Results highlight AutoCO as a principled and effective path toward proactive, verifiable LLM-driven optimization.

## 18. ToolScope: Enhancing LLM Agent Tool Use through Tool Merging and Context-Aware Filtering

- Authors: Marianne Menglin Liu, Daniel Garcia, Fjona Parllaku, Vikas Upadhyay, Syed Fahad Allam Shah, Dan Roth
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.7020567779767344
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1573/
- PDF: https://aclanthology.org/2026.acl-long.1573.pdf
- Local PDF: pdf/2026-09-13_18_ToolScope_ Enhancing LLM Agent Tool Use through Tool Merging and Context-Aware Filtering.pdf

Large language model (LLM) agents rely on external tools to solve complex tasks, but real-world toolsets often contain redundant tools with overlapping names and descriptions, introducing ambiguity and reducing selection accuracy. LLMs also face strict input context limits, preventing efficient consideration of large toolsets. To address these challenges, we propose ToolScope, which includes: (1) ToolScopeMerger with Auto-Correction to automatically audit and fix tool merges, reducing redundancy, and (2) ToolScopeRetriever to rank and select only the most relevant tools for each query, compressing toolsets to fit within context limits without sacrificing accuracy. Evaluations on three state-of-the-art LLMs and three open-source tool-use benchmarks show gains of 8.38% to 38.6% in tool selection accuracy, demonstrating ToolScope’s effectiveness in enhancing LLM tool use.

## 19. StepHint: Multi-level Stepwise Hints Enhance Reinforcement Learning to Reason

- Authors: Kaiyi Zhang, Ang Lv, Jinpeng Li, Yongbo Wang, Feng Wang, Haoyuan hu, Rui Yan
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.700916865046907
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1755/
- PDF: https://aclanthology.org/2026.acl-long.1755.pdf
- Local PDF: pdf/2026-09-13_19_StepHint_ Multi-level Stepwise Hints Enhance Reinforcement Learning to Reason.pdf

Reinforcement learning with verifiable rewards (RLVR) is a promising approach for improving the complex reasoning abilities of large language models (LLMs). However, current RLVR methods face two significant challenges: the near-miss reward problem, where a small mistake can invalidate an otherwise correct reasoning process, greatly hindering training efficiency; and exploration stagnation, where models tend to focus on solutions within their ”comfort zone”, lacking the motivation to explore potentially more effective alternatives. To address these challenges, we propose StepHint, a novel RLVR algorithm that utilizes multi-level stepwise hints to help models explore the solution space more effectively. StepHint partitions valid reasoning chains into reasoning steps using our proposed adaptive partitioning method. The initial few steps are used as hints, and simultaneously, multiple-level hints (each comprising a different number of steps) are provided to the model. This approach directs the model’s exploration toward a promising solution subspace while preserving its flexibility for independent exploration. By providing hints, StepHint mitigates the near-miss reward problem, thereby improving training efficiency. Additionally, the external reasoning pathways help the model develop better reasoning abilities, enabling it to move beyond its ”comfort zone” and mitigate exploration stagnation. StepHint outperforms competitive RLVR enhancement methods across six mathematical benchmarks and two out-of-domain benchmarks.

## 20. Optimizing User Profiles via Contextual Bandits for Retrieval-Augmented LLM Personalization

- Authors: Linfeng Du, Ye Yuan, Zichen Zhao, Fuyuan Lyu, Emiliano Penaloza, Xiuying Chen, Zipeng Sun, Jikun Kang, Laurent Charlin, Xue Liu, Haolun Wu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.7008387650650527
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1467/
- PDF: https://aclanthology.org/2026.acl-long.1467.pdf
- Local PDF: pdf/2026-09-13_20_Optimizing User Profiles via Contextual Bandits for Retrieval-Augmented LLM Personalization.pdf

Large language models (LLMs) excel at general-purpose tasks, yet adapting their responses to individual users remains challenging. Retrieval augmentation provides a lightweight alternative to fine-tuning by conditioning LLMs on user history records, and existing approaches typically select these records based on semantic relevance. We argue that relevance serves as an unreliable proxy for utility: a record may be semantically similar to a query yet fail to improve generation quality or even degrade it due to redundancy or conflicting information. To bridge this gap, we propose PURPLE, a contextual bandit framework that oPtimizes UseR Profiles for LLM pErsonalization. In contrast to a greedy selection of the most relevant records, PURPLE treats profile construction as an order-sensitive generation process and utilizes a Plackett-Luce ranking model to capture complex inter-record dependencies. By training with semantically rich feedback provided by the likelihood of the reference response, our method aligns retrieval directly with generation quality. Extensive experiments on nine personalization tasks demonstrate that PURPLE consistently outperforms strong heuristic and retrieval-augmented baselines in both effectiveness and efficiency, establishing a principled and scalable solution for optimizing user profiles.

## 21. Continual Safety Alignment via Gradient-Based Sample Selection

- Authors: Thong Bach, Dung Nguyen, Thao Minh Le, Truyen Tran
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.700718519572799
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.942/
- PDF: https://aclanthology.org/2026.findings-acl.942.pdf
- Local PDF: pdf/2026-09-13_21_Continual Safety Alignment via Gradient-Based Sample Selection.pdf

Large language models require continuous adaptation to new tasks while preserving safety alignment. However, fine-tuning on even benign data often compromises safety behaviors. We investigate which training samples cause alignment drift through a data-centric lens. Our experiments show samples contribute unequally: high-gradient samples cause greater safety degradation and drive models toward pretrained distributions, while moderate-gradient samples enable task learning with minimal alignment loss. This connects to the elasticity phenomenon—high-gradient samples activate the reversion force pulling models toward pretrained behavior. We propose gradient-based sample selection that filters high-gradient samples during fine-tuning. Across multiple model families on continual domain tasks, our method substantially improves alignment preservation while maintaining competitive task performance, without requiring curated safe data or architectural modifications.

## 22. Activation Decomposition and Steering for LLM Backdoor Remediation

- Authors: Lingfeng Zhong, Qiongkai Xu, Usman Naseem
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.6999536696618405
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.2025/
- PDF: https://aclanthology.org/2026.acl-long.2025.pdf
- Local PDF: pdf/2026-09-13_22_Activation Decomposition and Steering for LLM Backdoor Remediation.pdf

Existing works on defending against LLM backdoor attacks rely on either auxiliary models or safety-related datasets for defending against backdoor attacks on large language models, which are not always available. To address these challenges, we propose our we propose our Contrastive-Selective Activation Decomposition and Steering (CS-ADS), which contrasts relatively more benign and poisoned settings to decompose the feature vectors for steering without relying on additional auxiliary models or datasets. With such disentangled vectors for remediation, our method can achieve feasible defense qualities even better than dataset-based contrastive steering strategies. This novel decomposition-based solution is motivated by the key insight that feature representations of prompt pairs can encode the same benign semantics in different proportions, even when both prompt pairs are similarly backdoored. Such discrepancies allow our method to identify effective remediation directions for steering the generation process, thereby preventing undesired outputs. We evaluate CS-ADS against multiple state-of-the-art backdoor attacks, and experimental results show that CS-ADS provides effective defense across settings.

## 23. Safeguarding LLM Fine-tuning via Push-Pull Distributional Alignment

- Authors: Haozhong Wang, Zhuo Li, Yibo Yang, He Zhao, Hongyuan Zha, Dandan Guo
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.699872891915003
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1083/
- PDF: https://aclanthology.org/2026.acl-long.1083.pdf
- Local PDF: pdf/2026-09-13_23_Safeguarding LLM Fine-tuning via Push-Pull Distributional Alignment.pdf

The inherent safety alignment of Large Language Models (LLMs) is prone to erosion during fine-tuning, even when using seemingly innocuous datasets. While existing defenses attempt to mitigate this via data selection, they typically rely on heuristic, instance-level assessments that neglect the global geometry of the data distribution and fail to explicitly repel harmful patterns. To address this, we introduce Safety Optimal Transport (SOT), a novel framework that reframes safe fine-tuning from an instance-level filtering challenge to a distribution-level alignment task grounded in Optimal Transport (OT). At its core is a dual-reference “push-pull” weight-learning mechanism: SOT optimizes sample importance by actively pulling the downstream distribution towards a trusted safe anchor while simultaneously pushing it away from a general harmful reference. This establishes a robust geometric safety boundary that effectively purifies the training data. Extensive experiments across diverse model families and domains demonstrate that SOT significantly enhances model safety while maintaining competitive downstream performance, achieving a superior safety-utility trade-off compared to baselines.

## 24. RIMRULE: Improving Tool-Using Language Agents via MDL-Guided Rule Learning

- Authors: Xiang Gao, Yuguang Yao, Qi Zhang, Kaiwen Dong, Avinash Baidya, Ruocheng Guo, Hilaf Hasson, Kamalika Das
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.699853190210226
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1599/
- PDF: https://aclanthology.org/2026.acl-long.1599.pdf
- Local PDF: pdf/2026-09-13_24_RIMRULE_ Improving Tool-Using Language Agents via MDL-Guided Rule Learning.pdf

Large language models (LLMs) often struggle to use tools reliably in domain-specific settings, where APIs may be idiosyncratic, under-documented, or tailored to private workflows. This highlights the need for effective adaptation to task-specific tools. We propose RIMRULE, a neuro-symbolic approach for LLM adaptation based on dynamic rule injection. Compact, interpretable rules are distilled from failure traces and injected into the prompt during inference to improve task performance. These rules are proposed by the LLM itself and consolidated using a Minimum Description Length (MDL) objective that favors generality and conciseness. Each rule is stored in both natural language and a structured symbolic form, supporting efficient retrieval at inference time. Experiments on tool-use benchmarks show that this approach improves accuracy on both seen and unseen tools without modifying LLM weights. It outperforms prompting-based adaptation methods and complements finetuning, offering an interpretable layer of inference-time generalization. Moreover, rules learned from one LLM can be reused to improve others, including long reasoning LLMs, highlighting the portability of symbolic knowledge across architectures.

## 25. Towards Efficient Large Language Model Serving: A Survey on System-Aware KV Cache Optimization

- Authors: Jiantong Jiang, Peiyu Yang, Rui Zhang, Feng Liu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.6992057286078577
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1916/
- PDF: https://aclanthology.org/2026.findings-acl.1916.pdf
- Local PDF: pdf/2026-09-13_25_Towards Efficient Large Language Model Serving_ A Survey on System-Aware KV Cache Optimization.pdf

Despite the rapid advancements of large language models (LLMs), LLM serving systems remain memory-intensive and costly. The key-value (KV) cache, which stores KV tensors during autoregressive decoding, is crucial for enabling low-latency, high-throughput LLM inference serving. In this survey, we focus on system-aware KV infrastructure for serving LLMs (abbreviated as sKis). We revisit recent work from a system behavior perspective, organizing existing efforts into three dimensions: execution and scheduling (temporal), placement and migration (spatial), and representation and retention (structural). Furthermore, we analyze cross-behavior co-design affinity and behavior-objective links, highlighting future opportunities. Our work systematizes a rapidly evolving area, providing a foundation for understanding and innovating KV cache designs in modern LLM serving infrastructure.

## 26. Graph of Trace: Visualizing Execution Traces of Scientific Agents

- Authors: Tianci Gao, Haoxuan Li, Jian He Li, Tianxiang Zhao, Shi Runze, Weiran Wang, Zezhao Wu, Lu Mi
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.6990735534298125
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-demo.29/
- PDF: https://aclanthology.org/2026.acl-demo.29.pdf
- Local PDF: pdf/2026-09-13_26_Graph of Trace_ Visualizing Execution Traces of Scientific Agents.pdf

Scientific AI agents can autonomously carry out complex research workflows, yet these unfolded workflows often remains difficult for humans to inspect and review, limiting interpretable, controllable and effective human–AI collaboration. To address this challenge, we present a monitoring and visualization framework that records fine-grained execution events and organizes them into a directed graph that make agent workflows explicit as they proceed. The system records intermediate steps (e.g. tool calls and code executions), and renders them as real-time updated visual traces that expose workflow structure. This allows users to examine how results are produced, identify where failures emerge, and better understand agent behavior across different stages of the research process.We conduct an evaluation on complex research tasks with domain experts of interdisciplinary background in AI, neuroscience and biology. Experts report that structured traces visualization improves understanding of agent workflows, perceived interpretability, and usability for analysis and further interaction.

## 27. METER: Evaluating Multi-Level Contextual Causal Reasoning in Large Language Models

- Authors: Pengfeng Li, Chen Huang, Chaoqun Hao, Hongyao Chen, Xiao-Yong Wei, Wenqiang Lei, See-Kiong Ng
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.698932796536027
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1668/
- PDF: https://aclanthology.org/2026.acl-long.1668.pdf
- Local PDF: pdf/2026-09-13_27_METER_ Evaluating Multi-Level Contextual Causal Reasoning in Large Language Models.pdf

Contextual causal reasoning is a critical yet challenging capability for Large Language Models (LLMs). Existing benchmarks, however, often evaluate this skill in fragmented settings, failing to ensure context consistency or cover the full causal hierarchy. To address this, we pioneer METER to systematically benchmark LLMs across all three levels of the causal ladder under a unified context setting. Our extensive evaluation of various LLMs reveals a significant decline in proficiency as tasks ascend the causal hierarchy. To diagnose this degradation, we conduct a deep mechanistic analysis via both error pattern identification and internal information flow tracing. Our analysis reveals two primary failure modes: (1) LLMs are susceptible to distraction by causally irrelevant but factually correct information at lower level of causality; and (2) as tasks ascend the causal hierarchy, faithfulness to the provided context degrades, leading to a reduced performance. We belive our work advances our understanding of the mechanisms behind LLM contextual causal reasoning and establishes a critical foundation for future research. Our code and dataset are available at https://github.com/SCUNLP/METER .

## 28. LLM-KT: Enhancing Large Language Models with Knowledge Tracing via Multi-Level Plug-and-Play Alignment

- Authors: Ziwei Wang, Jie Zhou, Qin Chen, Bo Jiang, Qingchun Bai, Liang Dou, Liang He
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.698908783436748
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1781/
- PDF: https://aclanthology.org/2026.findings-acl.1781.pdf
- Local PDF: pdf/2026-09-13_28_LLM-KT_ Enhancing Large Language Models with Knowledge Tracing via Multi-Level Plug-and-Play Alignment.pdf

Knowledge Tracing (KT) is a pivotal task in personalized education, aiming to predict students’ future performance based on their historical interactions. While prior work has focused on learning behavioral sequences using question IDs or surface-level textual features, these methods often fail to capture complex behavioral patterns due to a lack of deep reasoning capabilities and world knowledge. To address this, we propose LLM-KT, a novel framework that integrates the reasoning power of Large Language Models (LLMs) with the sequential modeling strengths of traditional KT methods via multi-level plug-and-play alignment. Specifically, for task-level alignment, we design a plug-and-play instruction to leverage the rich knowledge and reasoning capacity of LLMs for the KT objective. For modality-level alignment, we introduce two mechanisms to integrate representations learned by traditional methods: (1) a Semantic History Projector that flexibly inserts compressed context embeddings into LLMs using question- and concept-specific tokens to capture long-term history; and (2) a Behavioral Dynamics Projector that enhances LLMs with sequential interaction patterns via a sequence adapter. Extensive experiments on four standard datasets demonstrate that LLM-KT achieves state-of-the-art performance, significantly outperforming over 20 competitive baselines.

## 29. RL-PLUS: Countering Capability Boundary Collapse of LLMs in Reinforcement Learning with Hybrid-policy Optimization

- Authors: Yihong Dong, Xue Jiang, Yongding Tao, Huanyu Liu, Kechi Zhang, Lili Mou, Rongyu Cao, Yingwei MA, Jue Chen, Binhua Li, Zhi Jin, Fei Huang, Yongbin Li, Ge Li
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.698766538275557
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1994/
- PDF: https://aclanthology.org/2026.acl-long.1994.pdf
- Local PDF: pdf/2026-09-13_29_RL-PLUS_ Countering Capability Boundary Collapse of LLMs in Reinforcement Learning with Hybrid-policy Optimization.pdf

Reinforcement Learning with Verifiable Reward (RLVR) has significantly advanced the complex reasoning abilities of Large Language Models (LLMs). However, it struggles to break through the inherent capability boundaries of the base LLM, due to its essentially on-policy strategy coupled with LLM’s immense action space and sparse reward. Critically, RLVR can lead to the capability boundary collapse, narrowing the LLM’s problem-solving scope. To address this problem, we propose R-PLUS, a novel hybrid-policy optimization approach for LLMs that synergizes internal exploitation with external data to achieve stronger reasoning capabilities and surpass the boundaries of base models. R-PLUS integrates two core components, i.e., Multiple Importance Sampling to address distributional mismatch from external data, and Exploration-Based Advantage Function to guide the model towards high-value, unexplored reasoning paths. We provide both theoretical analysis and extensive experiments to demonstrate the superiority and generalizability of our approach. Compared with existing RLVR methods, R-PLUS achieves 1) state-of-the-art performance on six math reasoning benchmarks; 2) superior performance on six out-of-distribution reasoning tasks; 3) consistent and significant gains across diverse model families, with average relative improvements up to 69.2%. Moreover, the analysis of Pass@k curves indicates that R-PLUS effectively resolves the capability boundary collapse problem.

## 30. MultiDx: A Multi-Source Knowledge Integration Framework towards Diagnostic Reasoning

- Authors: Yimin Deng, Zhenxi Lin, Yejing Wang, Guoshuai Zhao, Pengyue Jia, Zichuan Fu, Derong Xu, Yefeng Zheng, Xiangyu Zhao, Li Zhu, Xian Wu, Xueming Qian
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.698621520290772
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1646/
- PDF: https://aclanthology.org/2026.findings-acl.1646.pdf
- Local PDF: pdf/2026-09-13_30_MultiDx_ A Multi-Source Knowledge Integration Framework towards Diagnostic Reasoning.pdf

Diagnostic prediction and clinical reasoning are critical tasks in healthcare applications. While large language models have shown strong capabilities in commonsense reasoning, they still struggle with diagnostic reasoning due to limited domain knowledge. Existing approaches often rely on internal model knowledge or static knowledge bases, which are insufficient to support the knowledge demands of diagnostic reasoning. Moreover, these methods focus solely on the accuracy of final predictions, overlooking alignment with standard clinical reasoning trajectories. To this end, we propose MultiDx, a two-stage diagnostic reasoning framework that performs differential diagnosis by analyzing evidence collected from multiple knowledge sources. Specifically, it first generates suspected diagnoses and reasoning traces by leveraging knowledge from web search, SOAP-formatted case, and clinical case database. Then it integrates multi-perspective evidence through matching, voting, and differential diagnosis to generate the final prediction. Extensive experiments demonstrate the effectiveness of our approach.
