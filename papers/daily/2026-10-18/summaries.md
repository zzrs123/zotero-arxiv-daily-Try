# Paper Daily Reading - 2026-10-18

## 1. CellDiffusion: Enhancing scRNA-seq data integration with accurate inference of cell-cell association

- Authors: Yuchen Liu, Ziying Huang, Simon L. Lu, Lei Jiang, Zedong Lin, Jou-Hsuan Lee, Vijaya B. Kolachalama, Rong Li, Dong He Xu, Juexin Wang, Heng Pan, Chao Zhang
- Source: openalex
- Venue type: journal
- Journal: Science Advances
- Publication status: published
- Publication date: 2026-10-16
- DOI: https://doi.org/10.1126/sciadv.aed4155
- Categories: Single-cell and spatial transcriptomics, Gene expression and cancer classification, Bioinformatics and Genomic Networks
- Relevance: 3.662019036194881
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://doi.org/10.1126/sciadv.aed4155
- PDF: Unavailable
- Local PDF: Not downloaded

Integrating single-cell transcriptomic datasets across laboratories, conditions, and technologies remains challenging because of cell type–specific batch effects and heterogeneous biological compositions. Current methods often fail to separate genuine biological variation from technical noise, misaligning distinct cell populations or leaving batch effects uncorrected. To address these challenges, we present CellDiffusion, an unsupervised graph-based model that propagates cellular features through a diffusion process to strengthen meaningful cell-cell associations in data integration. By learning a cell-cell attention network, CellDiffusion adaptively identifies corresponding populations across batches. Our approach applies cell-specific correction in data integration, generating cell embeddings that align cells across batches while preserving intrinsic cell types and developmental trajectories. We validate CellDiffusion across various datasets, including the human endometrium, one of the most dynamic and complex tissues featuring extensive cellular and molecular changes with the menstrual cycle. This framework also improves other essential analyses such as label transfer, clustering, and trajectory inference. CellDiffusion represents a powerful paradigm for accurate single-cell transcriptomic integrative analysis.

## 2. Dendritic computation bridges neuroscience and foundation models

- Authors: Man Yao, Yuqi Pan, Yiran Zhong, Shijie Mei, Zhen Qin, Kexin Wang, Jiakui Hu, Siyu Ding, Tianxiang Hu, Yanbin Huang, Guoqi Li, Lei Deng, Zhong Zheng, Mingqiang Huang, Xuyang Shen, Ning-long Xu, Yachuang Hu, Yuhong Chou, Peng Zhou, Guoliang Sun, Ning Qiao, Junjie Yan, Bo Xu, Guoqi Li
- Source: openalex
- Venue type: journal
- Journal: Nature Communications
- Publication status: published
- Publication date: 2026-10-15
- DOI: https://doi.org/10.1038/s41467-026-77929-8
- Categories: Neural Networks and Applications, Neural dynamics and brain function, Advanced Memory and Neural Computing
- Relevance: 2.969229712338181
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://doi.org/10.1038/s41467-026-77929-8
- PDF: https://www.nature.com/articles/s41467-026-77929-8_reference.pdf
- Local PDF: pdf/2026-10-18_02_Dendritic computation bridges neuroscience and foundation models.pdf

A prevailing view holds that although neuroscience historically inspired AI, its role in the recent evolution of AI, driven by the scaling of foundation models, is minor. We challenge this perspective by establishing a biological analogy between simplified dendritic neuron models and the attention mechanisms central to AI foundation models. We show that AI attention mechanisms bear direct mappings to internal neuronal complexities arising from dendritic organization, rather than to the mere inter-neuronal connections of simple point neurons. This re-conceptualization not only offers a neuroscience-informed perspective for understanding core AI methodologies beyond their formulation as abstract mathematical operations, but also paves the way for neuro-inspired foundation models that leverage neuroscientific insights to sustainably advance modern AI beyond scaling laws. As an example of this paradigm, we introduce a dendritic-inspired complexity framework, and design a hybrid-attention foundation model with dendritic-inspired sparse computation, which enhances memory capacity while reducing computational demands. Our model supports a 50M context window-equivalent to roughly 40 volumes of Shakespeare-demonstrating superior long-term memory capabilities. This work pioneers a paradigm that harnesses intra-neuronal dynamics to drive sustained advances in modern AI, while also offering a potential route to understanding dendritic computational mechanisms. How insights from neuroscience can inform future AI foundation models is an active area of exploration. Here, the authors show that AI attention mechanisms resemble dendritic computations within individual neurons rather than interactions between neurons, inspiring a dendritic-inspired model with improved long-term memory and reduced computational cost.

## 3. EquivPruner: Boosting Efficiency and Quality in LLM-Based Search via Action Pruning

- Authors: Jiawei Liu, Qisi Chen, Jianshu Zhang, Quan Liu, Defu Lian
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.627459874290877
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.100/
- PDF: https://aclanthology.org/2026.acl-long.100.pdf
- Local PDF: pdf/2026-10-18_03_EquivPruner_ Boosting Efficiency and Quality in LLM-Based Search via Action Pruning.pdf

Large Language Models (LLMs) excel at complex reasoning through search algorithms, yet current strategies often suffer from massive token consumption due to redundant exploration of semantically equivalent steps. Existing semantic similarity methods struggle to accurately identify such equivalence in domain-specific contexts like mathematical reasoning. To address this, we propose EquivPruner , a simple yet effective approach that identifies and prunes semantically equivalent actions during LLM reasoning search. We also introduce MathEquiv, the first dataset we created for mathematical statement equivalence, which enables the training of a lightweight equivalence detector. Extensive experiments across various models and tasks demonstrate that EquivPruner significantly reduces token consumption, improving searching efficiency and often bolstering reasoning accuracy. For instance, when applied to Qwen2.5-Math-7B-Instruct on GSM8K, EquivPruner reduced token consumption by 48.1% while also improving accuracy. Our code is available at https://github.com/Lolo1222/EquivPruner .

## 4. Enhancing Multimodal Large Language Models for Ancient Chinese Character Evolution Analysis via Glyph-Driven Fine-Tuning

- Authors: Rui Song, Lida Shi, Ruihua Qi, Yingji Li, Hao Xu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.6254254253602536
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1043/
- PDF: https://aclanthology.org/2026.acl-long.1043.pdf
- Local PDF: pdf/2026-10-18_04_Enhancing Multimodal Large Language Models for Ancient Chinese Character Evolution Analysis via Glyph-Driven Fine-Tuning.pdf

In recent years, rapid advances in Multimodal Large Language Models (MLLMs) have increasingly stimulated research on ancient Chinese scripts. As the evolution of written characters constitutes a fundamental pathway for understanding cultural transformation and historical continuity, how MLLMs can be systematically leveraged to support and advance text evolution analysis remains an open and largely underexplored problem. To bridge this gap, we construct a comprehensive benchmark comprising 11 tasks and over 130,000 instances, specifically designed to evaluate the capability of MLLMs in analyzing the evolution of ancient Chinese scripts. We conduct extensive evaluations across multiple widely used MLLMs and observe that, while existing models demonstrate a limited ability in glyph-level comparison, their performance on core tasks-such as character recognition and evolutionary reasoning-remains substantially constrained. Motivated by these findings, we propose a glyph-driven fine-tuning framework (GEVO) that explicitly encourages models to capture evolutionary consistency in glyph transformations and enhances their understanding of text evolution. Experimental results show that even models at the 2B scale achieve consistent and comprehensive performance improvements across all evaluated tasks. To facilitate future research, we publicly release both the benchmark and the trained models.

## 5. R-Search: Empowering LLM Reasoning with Search via Multi-Reward Reinforcement Learning

- Authors: Qingfei Zhao, Ruobing Wang, Dingling Xu, Daren Zha, Ma Bowen, Zhichun Wang, Shijie Jia, Limin Liu, Xin Wang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.6254119292789992
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1896/
- PDF: https://aclanthology.org/2026.findings-acl.1896.pdf
- Local PDF: pdf/2026-10-18_05_R-Search_ Empowering LLM Reasoning with Search via Multi-Reward Reinforcement Learning.pdf

Large language models (LLMs) have notably progressed in multi-step and long-chain reasoning. However, extending their reasoning capabilities to encompass deep interactions with search remains a non-trivial challenge, as models often fail to identify optimal reasoning–search interaction trajectories, resulting in suboptimal responses. We propose R-Search, a novel reinforcement learning framework for Reasoning–Search integration, designed to enable LLMs to autonomously execute multi-step reasoning with deep search interaction, and learn optimal reasoning–search interaction trajectories via multi-reward signals, improving response quality in complex logic- and knowledge-intensive tasks. R-Search guides the LLM to dynamically decide when to search or reason, while globally integrating key evidence to enhance deep knowledge interaction between reasoning and search. During RL training, R-Search provides multi-type rewards to jointly optimize the reasoning–search trajectory. Experiments on seven datasets show that R-Search significantly outperforms mainstream RAG baselines.

## 6. Fundamental Reasoning Paradigms Induce Out-of-Domain Generalization in Language Models

- Authors: Mingzi Cao, Xingwei Tan, Mahmud Elahi Akhter, Marco Valentino, Maria Liakata, Xi Wang, Nikolaos Aletras
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.6250139231643344
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1653/
- PDF: https://aclanthology.org/2026.findings-acl.1653.pdf
- Local PDF: pdf/2026-10-18_06_Fundamental Reasoning Paradigms Induce Out-of-Domain Generalization in Language Models.pdf

Deduction, induction, and abduction are fundamental reasoning paradigms, core for human logical thinking. Although improving Large Language Model (LLM) reasoning has attracted significant research efforts, the extent to which the fundamental paradigms induce generalization has yet to be systematically explored. In this study, we shed light on how the interplay between these core paradigms influences LLMs’ reasoning behavior. To this end, we first collect a new dataset of reasoning trajectories from symbolic tasks, each targeting one of the three fundamental paradigms, to abstract from concrete world knowledge. Then, we investigate effective ways for inducing these skills into LLMs.We experiment with a battery of methods including simple fine-tuning, and more complex approaches to increase model depth, or transform a dense model to a mixture-of-experts. We comprehensively evaluate induced models on realistic out-of-domain tasks, that are entirely formulated in natural language and contain real-world knowledge. Our results reveal that our approach yields strong generalizability with substantial performance gains (up to 14.60) across realistic tasks.

## 7. You Only Need One Single Token to Refine Safety Alignment

- Authors: Wenqian Yu, Shuo Chen, Zhijiang Li, Zhipeng Wang, Jindong Gu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.6245812064990193
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.662/
- PDF: https://aclanthology.org/2026.findings-acl.662.pdf
- Local PDF: pdf/2026-10-18_07_You Only Need One Single Token to Refine Safety Alignment.pdf

Large language models (LLMs) face a critical alignment challenge: balancing safety with helpfulness. Excessive safety can lead to over-refusal, where models reject harmful-looking yet benign queries, severely limiting utility.Existing training-free interventions offer an efficient way to mitigate over-refusal without re-training, but suffer from high inference overhead and architecture dependency. Our work explores a complementary direction: rather than applying post-hoc corrections to model outputs, our goal is to intrinsically reshape the distributions of harmful and benign samples within the model’s decision space. In this paper, we argue that a lightweight training-based approach can more effectively distinguish between harmful and benign samples. We propose Single Token Alignment (STA), which optimizes only a single-token prefix (e.g., 4,096 parameters) while keeping the base model frozen. To address the inherent challenge of achieving robust refinement through such a minimal parameter interface, STA employs a mixed weighting mechanism integrated with its optimization objective. This mechanism incorporates hard weighting via stringent data filtering to provide clear, unbiased learning signals, and soft weighting through a focal mechanism to prioritize challenging cases.Extensive experiments across 9 models and 10 datasets demonstrate that STA achieves a superior safety-helpfulness balance for LLMs, MLLMs, and reasoning models, offering a highly efficient and generalizable solution for refining safety alignment.

## 8. DIFFA-2: A Practical Diffusion Large Language Model for General Audio Understanding

- Authors: Jiaming Zhou, Xuxin Cheng, Shiwan Zhao, Yuhang Jia, Cao Liu, Ke Zeng, Xunliang Cai, Yong Qin
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.624007227235348
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.235/
- PDF: https://aclanthology.org/2026.findings-acl.235.pdf
- Local PDF: pdf/2026-10-18_08_DIFFA-2_ A Practical Diffusion Large Language Model for General Audio Understanding.pdf

Autoregressive (AR) large audio language models (LALMs) such as Qwen-2.5-Omni have achieved strong performance on audio understanding and interaction, but scaling them remains costly in data and computation, and strictly sequential decoding limits inference efficiency. Diffusion large language models (dLLMs) have recently been shown to make effective use of limited training data, and prior work on DIFFA indicates that replacing an AR backbone with a diffusion counterpart can substantially improve audio understanding under matched settings, albeit at a proof-of-concept scale without large-scale instruction tuning, preference alignment, or practical decoding schemes. We introduce DIFFA-2, a practical diffusion-based LALM for general audio understanding. DIFFA-2 upgrades the speech encoder, employs dual semantic and acoustic adapters, and is trained with a four-stage curriculum that combines semantic and acoustic alignment, large-scale supervised fine-tuning, and variance-reduced preference optimization, using only fully open-source corpora. Experiments on MMSU, MMAU, and MMAR show that DIFFA-2 consistently improves over DIFFA and is competitive to strong AR LALMs under practical training budgets, supporting diffusion-based modeling is a viable backbone for large-scale audio understanding.

## 9. Leveraging Pretrained Language Models as Energy Functions for Glauber Dynamics Text Diffusion

- Authors: Tarun Kathuria, Sachin Kumar
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.623810377386354
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.2117/
- PDF: https://aclanthology.org/2026.findings-acl.2117.pdf
- Local PDF: pdf/2026-10-18_09_Leveraging Pretrained Language Models as Energy Functions for Glauber Dynamics Text Diffusion.pdf

We present a discrete diffusion-based generative model for text generation using Glauber dynamics from statistical physics. Our main insight is that instead of trying to train a discrete state space diffusion model using Glauber dynamics with a uniform transition kernel as the forward process, one can set up an “energy function” based on pretrained causal/masked language models, which, when viewed as the stationary distribution, allows us to significantly improve the quality of the generated text. Using UL2 as our pretrained models and modifying and incorporating it into our diffusion pipeline, we obtain significantly better perplexities than prior diffusion-based text generative models and are competitive with the perplexities of GPT-2-medium and GPT-2-large for comparable model sizes. Furthermore, our models outperform prior diffusion models and GPT-2 style auto-regressive models on some zero-shot common sense reasoning tasks as well as some planning/search tasks.

## 10. ReProbe: Efficient Test-Time Scaling of Multi-Step Reasoning by Probing Internal States of Large Language Models

- Authors: Jingwei Ni, Ekaterina Fadeeva, Tianyi Wu, Mubashara Akhtar, Jiaheng Zhang, Elliott Ash, Markus Leippold, Timothy Baldwin, See-Kiong Ng, Artem Shelmanov, Mrinmaya Sachan
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.6237822709625735
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.536/
- PDF: https://aclanthology.org/2026.acl-long.536.pdf
- Local PDF: pdf/2026-10-18_10_ReProbe_ Efficient Test-Time Scaling of Multi-Step Reasoning by Probing Internal States of Large Language Models.pdf

LLMs can solve complex tasks by generating long, multi-step reasoning chains. Test-time scaling (TTS) can further improve LLM performance by sampling multiple variants of intermediate reasoning steps, verifying their correctness, and strategically choosing the best steps for continuation. However, existing verification approaches, such as Process Reward Models (PRMs), are computationally expensive, limited to specific domains, and require large-scale human or model-generated annotations. We propose a lightweight alternative for step-level reasoning verification based on probing the internal states of LLMs. We train a transformer-based probe that uses the internal states of the frozen LLM to estimate the credibility of its reasoning steps during generation. Annotation can be generated either by another larger LLM (e.g., DeepSeek-R1) or in a self-supervised manner by the original model itself. The probes are both effective and lightweight, containing fewer than 10M parameters. Across multiple domains, including mathematics, planning, and general knowledge question answering, our probes match or even exceed the performance of PRMs that are up to 810× larger. Our findings suggest that the internal states of LLMs encode their confidence in reasoning processes and can serve as reliable signals for reasoning step verification, offering a promising direction towards scalable and generalizable TTS and introspective LLMs.

## 11. Process Reward Models Meet Planning: Generating Precise and Scalable Datasets for Step-Level Rewards

- Authors: Raffaele Pisano, Roberto Navigli
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.6232596597383666
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1292/
- PDF: https://aclanthology.org/2026.acl-long.1292.pdf
- Local PDF: pdf/2026-10-18_11_Process Reward Models Meet Planning_ Generating Precise and Scalable Datasets for Step-Level Rewards.pdf

Process Reward Models (PRMs) have emerged as a powerful tool for providing step-level feedback when evaluating the reasoning of Large Language Models (LLMs), which frequently produce chains of thought (CoTs) containing errors even when the final answer is correct. However, existing PRM datasets remain expensive to construct, prone to annotation errors, and predominantly limited to the mathematical domain.This work introduces a novel and scalable approach to PRM dataset generation based on planning logical problems expressed in the Planning Domain Definition Language (PDDL). Using this method, we generate a corpus of approximately one million reasoning steps across various PDDL domains and use it to train PRMs. Experimental results show that augmenting widely-used PRM training datasets with PDDL-derived data yields substantial improvements in both mathematical and non-mathematical reasoning, as demonstrated across multiple benchmarks.These findings indicate that planning problems constitute a scalable and effective resource for generating robust, precise, and fine-grained training data for PRMs, going beyond the classical mathematical sources that dominate this field.

## 12. The Agent’s First Day: Benchmarking Learning, Exploration, and Scheduling in the Workplace Scenarios

- Authors: Daocheng Fu, Jianbiao Mei, Rong Wu, Xuemeng Yang, Jia Xu, Ding Wang, Pinlong Cai, Yong Liu, Licheng Wen, Botian Shi
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.6230971789967192
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1505/
- PDF: https://aclanthology.org/2026.findings-acl.1505.pdf
- Local PDF: pdf/2026-10-18_12_The Agent’s First Day_ Benchmarking Learning, Exploration, and Scheduling in the Workplace Scenarios.pdf

The rapid evolution of Multi-modal Large Language Models (MLLMs) has advanced workflow automation; however, existing research mainly targets performance upper bounds in static environments, overlooking robustness for stochastic real-world deployment. We identify three key challenges: dynamic task scheduling, active exploration under uncertainty, and continuous learning from experience. To bridge this gap, we introduce TraineeBench, a dynamic evaluation environment that simulates a “trainee” agent continuously exploring a novel setting. Unlike traditional benchmarks, TraineeBench evaluates agents along three dimensions: (1) context-aware scheduling for streaming tasks with varying priorities; (2) prudent information acquisition to reduce hallucination via active exploration; and (3) continuous evolution by distilling generalized strategies from rule-based, dynamically generated tasks. Experiments show that cutting-edge agents have significant deficiencies in dynamic environments, especially in active exploration and continual learning. Our work establishes a framework for assessing agent reliability, shifting evaluation from static tests to realistic, production-oriented scenarios.

## 13. Breaking Block Boundaries: Anchor-based History-stable Decoding for Diffusion Large Language Models

- Authors: Shun Zou, Yong Wang, Zehui Chen, Lin Chen, Chongyang Tao, Feng Zhao, Xiangxiang Chu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.6227760479968376
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.945/
- PDF: https://aclanthology.org/2026.acl-long.945.pdf
- Local PDF: pdf/2026-10-18_13_Breaking Block Boundaries_ Anchor-based History-stable Decoding for Diffusion Large Language Models.pdf

Diffusion Large Language Models (dLLMs) have recently become a promising alternative to autoregressive large language models (ARMs). Semi-autoregressive (Semi-AR) decoding is widely employed in base dLLMs and advanced decoding strategies due to its superior performance. However, our observations reveal that Semi-AR decoding suffers from inherent block constraints, which cause the decoding of many cross-block stable tokens to be unnecessarily delayed. To address this challenge, we systematically investigate the identification of stable tokens and present three key findings: (1) naive lookahead decoding is unreliable, (2) token stability closely correlates with convergence trend, and (3) historical information is isolated. Building on these insights, we propose Anchor-based History-stable Decoding (AHD), a training-free, plug-and-play dynamic decoding strategy. Specifically, AHD monitors the stability trend of tokens in real time through dynamic anchors. Once a token reaches stability, it initiates early cross-block decoding to enhance efficiency and performance. Extensive experiments across language, vision-language, and audio-language domains demonstrate that AHD simultaneously improves both performance and inference efficiency. Notably, AHD effectively reverses the performance degradation typically observed in existing advanced decoding acceleration strategies. For instance, on the BBH benchmark, our approach reduces decoding steps by 80% while improving performance by 3.67%.

## 14. How Language Models Conflate Logical Validity with Plausibility: A Representational Analysis of Content Effects

- Authors: Leonardo Bertolazzi, Sandro Pezzelle, Raffaella Bernardi
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.6221343450658896
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.454/
- PDF: https://aclanthology.org/2026.findings-acl.454.pdf
- Local PDF: pdf/2026-10-18_14_How Language Models Conflate Logical Validity with Plausibility_ A Representational Analysis of Content Effects.pdf

Both humans and large language models (LLMs) exhibit content effects: biases in which the plausibility of the semantic content of a reasoning problem influences judgments regarding its logical validity. While this phenomenon in humans is best explained by the dual-process theory of reasoning, the mechanisms behind content effects in LLMs remain unclear. In this work, we address this issue by investigating how LLMs encode the concepts of validity and plausibility within their internal representations. We show that both concepts are linearly represented and strongly aligned in representational geometry, leading models to conflate plausibility with validity. Using steering vectors, we demonstrate that plausibility vectors can causally bias validity judgements, and vice versa, and that the degree of alignment between these two concepts predicts the magnitude of behavioral content effects across models. Finally, we construct debiasing vectors that disentangle these concepts, reducing content effects and improving reasoning accuracy. Our findings advance understanding of how abstract logical concepts are represented in LLMs and highlight representational interventions as a path toward more logical systems.

## 15. Fingerprinting LLMs via Prompt Injection

- Authors: Yuepeng Hu, Zhengyuan Jiang, Mengyuan Li, Osama Ahmed, Zhicong Huang, Cheng Hong, Neil Zhenqiang Gong
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.6217851359408186
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.541/
- PDF: https://aclanthology.org/2026.acl-long.541.pdf
- Local PDF: pdf/2026-10-18_15_Fingerprinting LLMs via Prompt Injection.pdf

Large language models (LLMs) are often modified after release through post-processing such as post-training or quantization, which makes it challenging to determine whether one model is derived from another. Existing provenance detection methods have two main limitations: (1) they embed signals into the base model before release, which is infeasible for already published models, or (2) they compare outputs across models using hand-crafted or random prompts, which are not robust to post-processing. In this work, we propose LLMPrint, a novel detection framework that constructs fingerprints by exploiting LLMs’ inherent vulnerability to prompt injection. Our key insight is that by optimizing fingerprint prompts to enforce consistent token preferences, we can obtain fingerprints that are both unique to the base model and robust to post-processing. We further develop a unified verification procedure that applies to both gray-box and black-box settings, with statistical guarantees. We evaluate LLMPrint on five base models and around 700 post-trained or quantized variants. Our results show that LLMPrint achieves high true positive rates while keeping false positive rates near zero. The code is publicly available at https://github.com/hifi-hyp/ACL-LLMPrint .

## 16. Meta-Reasoner: Dynamic Guidance for Optimized Inference-time Reasoning in Large Language Models

- Authors: Yuan Sui, Yufei He, Tri Cao, Sophia Simeng Han, Yulin Chen, Bryan Hooi
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.6216196800866536
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.649/
- PDF: https://aclanthology.org/2026.findings-acl.649.pdf
- Local PDF: pdf/2026-10-18_16_Meta-Reasoner_ Dynamic Guidance for Optimized Inference-time Reasoning in Large Language Models.pdf

Large Language Models (LLMs) often struggle with computational efficiency and error propagation in multi-step reasoning tasks. While recent advancements on prompting and post-training have enabled LLMs to perform step-wise reasoning, they still tend to explore unproductive solution paths without effective backtracking or strategy adjustment. In this paper, we propose Meta-Reasoner, a new framework that empowers LLMs to “think about how to think”. It optimizes the inference process by dynamically adapting reasoning strategies in real-time. Our approach employs contextual multi-armed bandits (CMABs) to learn an adaptive policy. It learns to evaluate the current state of LLM’s reasoning and determine optimal strategy that is most likely to lead to a successful outcome during inference, like whether to backtrack, switch to a new approach, or restart the problem-solving process. This meta-guidance helps avoid unproductive paths exploration during inference and hence improves computational efficiency. We evaluate Meta-Reasoner on math problems (e.g., Game-of-24, TheoremQA) and scientific tasks (e.g., SciBench). Results show that our method outperform previous SOTA methods by 9-12% in accuracy, while reducing inference time by 28-35% under the same compute budget. Additional experiments on creative writing demonstrate the generalizability of our approach to diverse reasoning-intensive tasks.

## 17. Semantic-Aware Logical Reasoning via a Semiotic Framework

- Authors: Yunyao Zhang, Xinglang Zhang, Junxi Sheng, Wenbing Li, Junqing Yu, Yi-Ping Phoebe Chen, Wei Yang, Zikai Song
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.6215670923329624
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.835/
- PDF: https://aclanthology.org/2026.acl-long.835.pdf
- Local PDF: pdf/2026-10-18_17_Semantic-Aware Logical Reasoning via a Semiotic Framework.pdf

Logical reasoning is a fundamental capability of large language models (LLMs). However, existing studies largely overlook the interplay between logical complexity and semantic complexity, limiting their robustness under abstract propositions, ambiguous contexts, and conflicting stances, which are central to human reasoning. We propose LogicAgent , a semiotic-square–guided framework that jointly addresses these two axes of difficulty. The semiotic square provides a principled structure for multi-perspective semantic analysis, and LogicAgent integrates automated deduction with reflective verification to manage logical complexity across deeper reasoning chains. To evaluate reasoning under coupled semantic and logical complexity, we introduce RepublicQA , a benchmark that contains abstract propositions with systematically constructed contrary and contradictory forms, providing a semantically rich setting for assessing logical reasoning in LLMs. Experiments show that LogicAgent achieves state-of-the-art performance on RepublicQA with a 6.25% average gain, and generalizes well to four mainstream logical reasoning benchmarks with an additional 7.05% improvement, highlighting the effectiveness of our semiotic-grounded multi-perspective reasoning in boosting LLMs’ logical performance.

## 18. GRPO-CARE: Consistency-Aware Reinforcement Learning for Multimodal Reasoning

- Authors: Yi Chen, Yuying Ge, Rui Wang, Yixiao Ge, Junhao Cheng, Ying Shan, Xihui Liu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.621482850639165
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.210/
- PDF: https://aclanthology.org/2026.findings-acl.210.pdf
- Local PDF: pdf/2026-10-18_18_GRPO-CARE_ Consistency-Aware Reinforcement Learning for Multimodal Reasoning.pdf

Recent reinforcement learning (RL) approaches, such as outcome-supervised GRPO, have advanced reasoning in Large Language Models (LLMs), yet their adaptation to multimodal LLMs (MLLMs) remains underexplored. Progress has been further limited by the lack of evaluation settings that jointly test perception and reasoning under controlled generalization challenges. To enable such analysis, we present SEED-Bench-R1 , a structured testbed featuring real-world video tasks and hierarchical evaluation across in-distribution, cross-environment, and cross-environment-task scenarios. Our analysis reveals that standard outcome-supervised GRPO often yields “logical incoherence”—achieving correct answers through flawed reasoning—due to its exclusive focus on final-answer rewards and rigid KL penalties. To address this, we propose GRPO-CARE , a consistency-aware RL framework that eliminates KL penalties while introducing a two-tiered reward system: a base reward for accuracy and an adaptive bonus for consistency. This bonus, derived from a slowly evolving reference model through group-relative likelihood calibration, rewards reasoning paths that logically support the final answer without requiring expensive process supervision. Experiments on SEED-Bench-R1 show that GRPO-CARE consistently outperforms standard GRPO, achieving a 6.7% gain on the hardest evaluation level and a 24.5% increase in reasoning consistency. Moreover, models trained with GRPO-CARE transfer effectively to diverse video understanding and even language-only reasoning benchmarks, validating its robustness and generality.

## 19. D-Artemis: A Deliberative Cognitive Framework for Mobile GUI Multi-Agents

- Authors: Hongze Mi, Yibo Feng, WenJie Lu, Yuqi Wang, Jinyuan Li, Song Cao, He Cui, Tengfei Tian, Xuelin Zhang, Haotian Luo, Di Sun, Jun Fang, Hua Chai, Naiqiang Tan, Gang Pan
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.621129839400968
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.681/
- PDF: https://aclanthology.org/2026.findings-acl.681.pdf
- Local PDF: pdf/2026-10-18_19_D-Artemis_ A Deliberative Cognitive Framework for Mobile GUI Multi-Agents.pdf

Graphical User Interface (GUI) agents aim to automate a wide spectrum of human tasks by emulating user interaction. Despite rapid advancements, current approaches are hindered by several critical challenges: data bottleneck in end-to-end training, high cost of delayed error detection, and risk of contradictory guidance. Inspired by the human cognitive loop of Thinking, Alignment, and Reflection, we present D-Artemis—a novel deliberative framework in this paper. D-Artemis leverages a fine-grained, app-specific tip retrieval mechanism to inform its decision-making process. It also employs a proactive Pre-execution Alignment stage, where Thought-Action Consistency (TAC) Check module and Action Correction Agent (ACA) work in concert to mitigate the risk of execution failures. A post-execution Status Reflection Agent (SRA) completes the cognitive loop, enabling strategic learning from experience. Crucially, D-Artemis enhances the capabilities of general-purpose Multimodal large language models (MLLMs) for GUI tasks without the need for training on complex trajectory datasets, demonstrating strong generalization. D-Artemis achieves SOTA among open-source general models on AndroidWorld (75.8%) and ScreenSpot-V2 (96.8%). Extensive ablation studies further demonstrate the significant contribution of each proposed component.

## 20. Budget-Aware Anytime Reasoning with LLM-Synthesized Preference Data

- Authors: Xuanming Zhang, Shwan Ashrafi, Aziza Mirsaidova, Amir H. Rezaeian, Miguel Ballesteros, Lydia Chilton, Zhou Yu, Dan Roth
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.6203820980308024
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.417/
- PDF: https://aclanthology.org/2026.findings-acl.417.pdf
- Local PDF: pdf/2026-10-18_20_Budget-Aware Anytime Reasoning with LLM-Synthesized Preference Data.pdf

We study the reasoning behavior of large language models (LLMs) under limited computation budgets. In such settings, producing useful partial solutions quickly is often more practical than exhaustive reasoning, which incurs high inference costs. Many real-world tasks, such as trip planning, require models to deliver the best possible output within a fixed reasoning budget. We introduce an anytime reasoning framework and the Anytime Index, a metric that quantifies how effectively solution quality improves as reasoning tokens increase. To further enhance efficiency, we propose an inference-time self-improvement method using LLM-synthesized preference data, where models learn from their own reasoning comparisons to produce better intermediate solutions. Experiments on NaturalPlan (Trip), AIME, and GPQA datasets show consistent gains across Grok-3, GPT-oss, GPT-4.1/4o, and LLaMA models, improving both reasoning quality and efficiency under budget constraints.

## 21. DocSplit: A Comprehensive Benchmark Dataset and Evaluation Approach for Document Packet Recognition and Splitting

- Authors: Md Mofijul Islam, Md Sirajus Salekin, Nivedha Balakrishnan, Vincil C. Bishop III, Niharika Jain, Spencer Romo, Bob Strahan, Boyi Xie, Diego A. Socolinsky
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.619925137902536
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-industry.12/
- PDF: https://aclanthology.org/2026.acl-industry.12.pdf
- Local PDF: pdf/2026-10-18_21_DocSplit_ A Comprehensive Benchmark Dataset and Evaluation Approach for Document Packet Recognition and Splitting.pdf

Document understanding in real-world applications often requires processing heterogeneous, multi-page document packets containing multiple documents stitched together. Despite recent advances in visual document understanding, the fundamental task of document packet splitting, which involves separating a document packet into individual units, remains largely unaddressed. We present the first comprehensive benchmark dataset, DocSplit , along with novel evaluation metrics for assessing the document packet splitting capabilities of large language models. DocSplit comprises five datasets of varying complexity, covering diverse document types, layouts, and multimodal settings. We formalize the DocSplit task, which requires models to identify document boundaries, classify document types, and maintain correct page ordering within a document packet. The benchmark addresses real-world challenges, including out-of-order pages, interleaved documents, and documents lacking clear demarcations. We conduct extensive experiments evaluating multimodal LLMs on our datasets, revealing significant performance gaps in current models’ ability to handle complex document splitting tasks. The DocSplit benchmark datasets and proposed novel evaluation metrics provide a systematic framework for advancing document understanding capabilities essential for legal, financial, healthcare, and other document-intensive domains. We release the datasets and evaluation code to facilitate future research in document packet processing.

## 22. Polynomial Expansion Rank Adaptation: Enhancing Low-Rank Fine-Tuning with High-Order Interactions

- Authors: Wenhao Zhang, Lin Mu, Li Ni, Peiquan Jin, Yiwen Zhang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.6198315853193765
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.650/
- PDF: https://aclanthology.org/2026.findings-acl.650.pdf
- Local PDF: pdf/2026-10-18_22_Polynomial Expansion Rank Adaptation_ Enhancing Low-Rank Fine-Tuning with High-Order Interactions.pdf

Low-rank adaptation (LoRA) is a widely used strategy for efficient fine-tuning of large language models (LLMs), but its strictly linear structure fundamentally limits expressive capacity. The bilinear formulation of weight updates captures only first-order dependencies between low-rank factors, restricting the modeling of nonlinear and higher-order parameter interactions.In this paper, we propose Polynomial Expansion Rank Adaptation (PERA), a novel method that introduces structured polynomial expansion directly into the low-rank factor space.By expanding each low-rank factor to synthesize high-order interaction terms before composition, PERA transforms the adaptation space into a polynomial manifold capable of modeling richer nonlinear coupling without increasing rank or inference cost.We provide theoretical analysis demonstrating that PERA offers enhanced expressive capacity and more effective feature utilization compare to existing linear adaptation approaches.Empirically, PERA consistently outperforms state-of-the-art methods across diverse benchmarks. Notably, our experiments show that incorporating high-order nonlinear components—particularly square terms—is crucial for enhancing expressive capacity and maintaining strong and robust performance under various rank settings.

## 23. CHOIR: Harmonizing Structured Persona Diversity for Robust Collaborative LLM Reasoning

- Authors: Xiangjue Dong, Cong Wang, Maria Teleki, Millennium Bismay, Ruihong Huang, James Caverlee
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.6190986073775924
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.2175/
- PDF: https://aclanthology.org/2026.acl-long.2175.pdf
- Local PDF: pdf/2026-10-18_23_CHOIR_ Harmonizing Structured Persona Diversity for Robust Collaborative LLM Reasoning.pdf

Persona-assigned Large Language Models can adopt diverse roles, enabling personalized and context-aware reasoning. However, even minor demographic perturbations in personas, such as simple pronoun swaps, can alter reasoning trajectories, leading to divergent sets of correct answers on reasoning benchmarks. We explore the potential of these variations as a constructive resource to improve LLM reasoning performance. We propose CHOIR (Collaborative Harmonization fOr Inference Robustness), a test-time framework that harmonizes a set of demographically perturbed, persona-conditioned reasoning signals into a unified prediction. CHOIR orchestrates a collaborative decoding process among counterfactual personas perturbed across dimensions of gender, race, religion, disability, and age, dynamically balancing agreement and divergence in their reasoning paths to improve performance. Experiments demonstrate that CHOIR consistently enhances LLM reasoning across model architectures, scales, and tasks. Improvements reach up to 20.1% for individual groups and 15.1% on average, and we show that CHOIR remains effective even when base personas are suboptimal.

## 24. Diff4TST: Masked Diffusion Language Model for Text Style Transfer

- Authors: Xinchen Ma, Gaole He, Yunshi Lan, Weining Qian
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.6188930824351515
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.306/
- PDF: https://aclanthology.org/2026.acl-long.306.pdf
- Local PDF: pdf/2026-10-18_24_Diff4TST_ Masked Diffusion Language Model for Text Style Transfer.pdf

Despite recent progress in LLMs for text style transfer, most existing methods rely on costly task-specific training and offer limited control over separating stylistic modification from content preservation. We propose Diff4TST, a diffusion-based language model that formulates text style transfer as an explicit copy-and-edit process. Built upon masked diffusion language models, Diff4TST introduces a style-aware noise schedule that selectively perturbs stylistic tokens while preserving content-bearing tokens during supervised fine-tuning.At inference time, we further introduce a generate-then-refine strategy that iteratively improves style compliance via gradient-based token re-masking, without reinforcement learning or external reward models. Extensive experiments on both fine-grained and polarity-based benchmarks show that Diff4TST achieves substantially improved style accuracy and controllability while maintaining strong content preservation and fluency. These results suggest diffusion-based language models as a principled and effective alternative to autoregressive pipelines for text style transfer.

## 25. On the Hidden Objective Biases of Group-based Reinforcement Learning

- Authors: Aleksandar Fontana, Marco Simoni, Giulio Rossolini, Paolo Mori, Andrea Saracino
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.6187469614470342
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-short.11/
- PDF: https://aclanthology.org/2026.acl-short.11.pdf
- Local PDF: pdf/2026-10-18_25_On the Hidden Objective Biases of Group-based Reinforcement Learning.pdf

Group-based reinforcement learning methods, like Group Relative Policy Optimization (GRPO), are widely used nowadays to post-train large language models. Despite their empirical success, they exhibit structural mismatches between reward optimization and the underlying training objective. In this paper, we present a theoretical analysis of GRPO style methods by studying them within a unified surrogate formulation. This perspective reveals recurring properties that affect all the methods under analysis: (i) non-uniform group weighting induces systematic gradient biases on shared prefix tokens; (ii) interactions with the AdamW optimizer make training dynamics largely insensitive to reward scaling; and (iii) optimizer momentum can push policy updates beyond the intended clipping region under repeated optimization steps. We believe that these findings highlight fundamental limitations of current approaches and provide principled guidance for the design of future formulations.

## 26. GUI0: Self-Evolving Foundational GUI Agents in Super App Ecosystems

- Authors: Xinyi Wang, Wei Dai, Kyle Qiao, Ke Wang, Peng Chen, Gang Cao, Kangqin, Zhongpu Wang, Xiaode Zhang, Yanming Liu, Jihao Gu, Jingtao Xu, Gong Zhi
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.6180364297414007
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.2052/
- PDF: https://aclanthology.org/2026.acl-long.2052.pdf
- Local PDF: pdf/2026-10-18_26_GUI0_ Self-Evolving Foundational GUI Agents in Super App Ecosystems.pdf

Automated interaction with graphical user interfaces (GUIs) is central to General Artificial Intelligence yet remains challenging within Super App ecosystems, characterized by non-standard rendering and absent accessibility metadata. While GUI agents often rely on explicit accessibility trees or static imitation, they are less explored for dynamic environments marked by sparse feedback and implicit visual cues. We present GUI0, a framework synergizing autonomous data synthesis with dual-agent co-evolution. GUI0 establishes a domain-aware foundation model via synthesized corpora and employs curriculum-driven reinforcement learning, where a curriculum agent generates boundary tasks to optimize an actor agent.Empirical results demonstrate three key advantages: (1) State-of-the-art performance on the SuperAPP benchmark, outperforming Gemini-2.5-Pro and Claude-4-Sonnet; (2) universal efficacy across diverse base models, consistently yielding substantial improvements on both Qwen2.5-VL and GUI-Owl variants; and (3) robust zero-shot generalization to standard GUIs (e.g., +62.7% on ScreenSpot Pro).

## 27. CORD: Bridging the Audio–Text Reasoning Gap via Weighted On-policy Cross-modal Distillation

- Authors: Hu Jing, Danxiang Zhu, Xianlong Luo, Dan Zhang, Shuwei He, Yishu Lei, Shikun Feng, Hai-Tao Zheng, Jingzhou HE, Yu Sun, Hua Wu, Haifeng Wang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.6176634420306084
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1581/
- PDF: https://aclanthology.org/2026.findings-acl.1581.pdf
- Local PDF: pdf/2026-10-18_27_CORD_ Bridging the Audio–Text Reasoning Gap via Weighted On-policy Cross-modal Distillation.pdf

Large Audio Language Models (LALMs) have garnered significant research interest. Despite being built upon text-based large language models (LLMs), LALMs frequently exhibit a degradation in knowledge and reasoning capabilities. We hypothesize that this limitation stems from the failure of current training paradigms to effectively bridge the acoustic-semantic gap within the feature representation space. To address this challenge, we propose CORD, a unified alignment framework that performs online cross-modal self-distillation. Specifically, it aligns audio-conditioned reasoning with its text-conditioned counterpart within a unified model. Leveraging the text modality as an internal teacher, CORD performs multi-granularity alignment throughout the audio rollout process. At the token level, it employs on-policy reverse KL divergence with importance-aware weighting to prioritize early and semantically critical tokens. At the sequence level, CORD introduces a judge-based global reward to optimize complete reasoning trajectories via Group Relative Policy Optimization (GRPO). Empirical results across multiple benchmarks demonstrate that CORD consistently enhances audio-conditioned reasoning and substantially bridges the audio–text performance gap with only 80k synthetic training samples, validating the efficacy and data efficiency of our on-policy, multi-level cross-modal alignment approach.

## 28. AGGC: Adaptive Group Gradient Clipping for Stabilizing Large Language Model Training

- Authors: Zhiyuan Li, Yuan Wu, Yi Chang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.617447720096303
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.339/
- PDF: https://aclanthology.org/2026.findings-acl.339.pdf
- Local PDF: pdf/2026-10-18_28_AGGC_ Adaptive Group Gradient Clipping for Stabilizing Large Language Model Training.pdf

To stabilize the training of Large Language Models (LLMs), gradient clipping is a nearly ubiquitous heuristic used to alleviate exploding gradients. However, traditional global norm clipping erroneously presupposes gradient homogeneity across different functional modules, leading to an adverse “spill-over” effect where volatile parameters force unnecessary scaling on stable ones. To overcome this, we propose Adaptive Group-wise Gradient Clipping (AGGC). AGGC partitions parameters into groups based on functional types and regulates each according to its historical behavior using an Exponential Moving Average (EMA). Specifically, it constructs an adaptive interval to simultaneously mitigate gradient explosion and vanishing, while employing a time-dependent scheduling mechanism to balance exploration and convergence. Experiments on LLaMA 2-7B, Mistral-7B, and Gemma-7B models demonstrate that AGGC-enhanced LoRA consistently outperforms standard LoRA and frequently exceeds Full Fine-Tuning performance. Specifically, on the GSM8K benchmark, Mistral-7B fine-tuned with AGGC-enhanced LoRA achieves 72.93% accuracy, surpassing the 69.5% of vanilla LoRA. AGGC also contributes to the stability of Reinforcement Learning with Verifiable Rewards (RLVR), leading to improved logical deduction in Qwen 2.5 and Llama 3.2 models. Experimental results demonstrate that AGGC effectively addresses the limitations of traditional gradient clipping methods, particularly in overcoming gradient heterogeneity, by utilizing a modular, adaptive clipping strategy to stabilize the training process. Due to its lightweight design, AGGC can be seamlessly integrated into existing post-training pipelines with negligible overhead.

## 29. How Controllable Are Large Language Models? A Unified Evaluation across Behavioral Granularities

- Authors: Ziwen Xu, Kewei Xu, Haoming Xu, Haiwen Hong, Longtao Huang, Hui Xue, Ningyu Zhang, Yongliang Shen, Guozhou Zheng, Huajun Chen, Shumin Deng
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.617249118112981
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1443/
- PDF: https://aclanthology.org/2026.acl-long.1443.pdf
- Local PDF: pdf/2026-10-18_29_How Controllable Are Large Language Models_ A Unified Evaluation across Behavioral Granularities.pdf

Large Language Models (LLMs) are increasingly deployed in socially sensitive domains, yet their unpredictable behaviors, ranging from misaligned intent to inconsistent personality, pose significant risks. We introduce SteerEval, a hierarchical benchmark for evaluating LLM controllability across three domains: language features, sentiment, and personality. Each domain is structured into three specification levels: L1 (what to express), L2 (how to express), and L3 (how to instantiate), connecting high-level behavioral intent to concrete textual output. Using SteerBench, we systematically evaluate contemporary steering methods, revealing that control often degrades at finer-grained levels. Our benchmark offers a principled and interpretable framework for safe and controllable LLM behavior, serving as a foundation for future research.

## 30. Fine-tuning vs. In-context Learning in Large Language Models: A Formal Language Learning Perspective

- Authors: Bishwamittra Ghosh, Soumi Das, Till Speicher, Qinyuan Wu, Mohammad Aflah Khan, Deepak Garg, Krishna P. Gummadi, Evimaria Terzi
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.6165664012602106
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1932/
- PDF: https://aclanthology.org/2026.acl-long.1932.pdf
- Local PDF: pdf/2026-10-18_30_Fine-tuning vs. In-context Learning in Large Language Models_ A Formal Language Learning Perspective.pdf

Large language models (LLMs) operate in two fundamental learning modes – fine-tuning (FT) and in-context learning (ICL) – raising key questions about which mode yields greater language proficiency and whether they differ in their inductive biases. Prior studies comparing FT and ICL have yielded mixed and inconclusive results due to inconsistent experimental setups. To enable a rigorous comparison, we propose a formal language learning task – offering precise language boundaries, controlled string sampling, and no data contamination – and introduce a discriminative test for language proficiency, where an LLM succeeds if it assigns higher generation probability to in-language strings than to out-of-language strings.Empirically, we find that: (a) FT has greater language proficiency than ICL on in-distribution generalization, but both perform equally well on out-of-distribution generalization. (b) Their inductive biases, measured by the correlation in string generation probabilities, are similar when both modes partially learn the language but diverge at higher proficiency levels. (c) Unlike FT, ICL performance differs substantially across models of varying sizes and families and is sensitive to the token vocabulary of the language. Thus, our work demonstrates the promise of formal languages as a controlled testbed for evaluating LLMs, behaviors that are difficult to isolate in natural language datasets. Our source code is available at https://github.com/bishwamittra/formallm .
