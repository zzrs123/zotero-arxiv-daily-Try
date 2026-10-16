# Paper Daily Reading - 2026-10-16

## 1. Towards a Data-Centric Understanding of Spatial Reasoning in Multimodal Large Language Models

- Authors: Mahdieh Mallahnezhad, Masoud Jafaripour, Mohamadali Tofigh, Sheila Schoepp, Osmar R. Zaiane
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-13
- DOI: Unavailable
- Categories: cs.CV, cs.AI, cs.CL
- Relevance: 3.4591834186679025
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.19108v1
- PDF: https://arxiv.org/pdf/2610.19108v1
- Local PDF: pdf/2026-10-16_01_Towards a Data-Centric Understanding of Spatial Reasoning in Multimodal Large Language Models.pdf

Multimodal Large Language Models (MLLMs) have been widely applied in embodied agents and robotics for vision tasks. However, MLLMs suffer from limitations in spatial reasoning and perception. Post-training techniques have shown promise for improving these capabilities; yet, there are limited data-driven surveys of such approaches. In this survey, we consider approaches to fine-tuning pretrained MLLMs for spatial reasoning tasks, ranging from supervised to reinforcement learning, with an emphasis on the datasets used. We investigate themes of dataset construction, data modality and annotation, and evaluation of the resulting models. Based on these themes, we categorize research into three groups: dataset design, dataset construction and evaluation. We find four main methods for constructing fixed spatial annotations: rules and templates, LLM prompting, procedural generation, and human-in-the-loop. We also observe substantial variation in evaluation approaches, including different scoring methods, tolerance metrics, and benchmark types. Finally, we identify opportunities for future research in unified dynamic annotation, efficient spatial reasoning, standardization of evaluation, expanded spatial range, and human-centered spatial interactions.

## 2. Sparse Autoencoders Are a Shared Coordinate System for Symbolic Matching

- Authors: Xiaocong Yang, Xuanyu Meng, Yuji Zhang, Jiawei Han, ChengXiang Zhai
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-14
- DOI: Unavailable
- Categories: cs.LG, cs.AI, cs.CL, cs.SC
- Relevance: 3.372546162170285
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.19636v1
- PDF: https://arxiv.org/pdf/2610.19636v1
- Local PDF: pdf/2026-10-16_02_Sparse Autoencoders Are a Shared Coordinate System for Symbolic Matching.pdf

Large language models (LLMs) hold broad knowledge in one set of weights, but lack interpretability and trustworthy reasoning, especially in high-stakes use cases. A neuro-symbolic model, with its interpretable architecture and System 2 reasoning capacity, is a promising alternative if built at the scale of LLMs; however, its symbolic backbone is usually constructed with human effort, so existing neuro-symbolic models are bottlenecked by the scope of the symbol component and usually domain-specific. A data-driven method could instead build a larger symbolic system by aligning and merging existing ones. We target its first, foundational step: matching units across these heterogeneous systems. Our method, SAE-IDF, encodes a symbol in its native context into a sparse code with a sparse autoencoder (SAE), re-weights each dimension by its rarity and matches across systems. On 12 tasks across 6 kinds of symbolic system, SAE-IDF outperforms the same LLM's dense baseline on all tasks with Gemma-2-9B and all but one with Llama-3.1-8B, by up to 45 points, consistently across SAE layers and configurations. SAE-IDF is also interpretable: every dimension of the sparse code has a human-readable meaning, so each match decomposes into named concepts (features). Our work paves the way to a universal symbolic backbone.

## 3. OrionMoE-v1.0: A Mixture-of-Experts Foundation Model for Tabular In-Context Learning

- Authors: Mohamed Bouadi, Nassim Bouarour, Aditya Tanna, Vinay Kumar Sankarapu
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-14
- DOI: Unavailable
- Categories: cs.LG, cs.AI
- Relevance: 3.3149810283277525
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.20418v1
- PDF: https://arxiv.org/pdf/2610.20418v1
- Local PDF: pdf/2026-10-16_03_OrionMoE-v1.0_ A Mixture-of-Experts Foundation Model for Tabular In-Context Learning.pdf

Tabular foundation models enable in-context learning by predicting unseen observations from a labeled support table without task-specific parameter updates. Despite recent advances, most existing approaches rely on dense architectures that apply the same transformations across features and datasets. We introduce OrionMoE-Small, a compact tabular foundation model that combines distribution-aware representations with dataset-conditioned sparse mixture-of-experts computation. Built on a dual-axis Transformer architecture, OrionMoE-Small selectively activates experts along the feature axis, with routing decisions informed by both individual feature representations and the broader dataset context. This design enables adaptive allocation of computation across heterogeneous tabular problems while retaining a shared computational pathway across tasks. OrionMoE-Small is pretrained entirely on synthetic classification tasks generated from a structured causal prior and performs downstream prediction without gradient-based adaptation. Experiments across multiple tabular benchmarks demonstrate competitive performance against substantially larger foundation models, with particularly strong results on small-context and high-dimensional datasets. Further analysis reveals favorable relative performance under class imbalance and highlights the importance of feature composition.

## 4. Generative Representation Learning for Scalable Latent Tokenization

- Authors: Alan Baade, Kyle Sargent, Vincent Sitzmann, Eric Ryan Chan, Justin Johnson, Li Fei-Fei, Gordon Wetzstein
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-14
- DOI: Unavailable
- Categories: cs.LG, cs.CV
- Relevance: 3.3015660323706664
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.20533v1
- PDF: https://arxiv.org/pdf/2610.20533v1
- Local PDF: pdf/2026-10-16_04_Generative Representation Learning for Scalable Latent Tokenization.pdf

We introduce an approach for self-supervised representation learning designed to be used as a tokenizer for generative modeling. Our objective supervises a representation loss by factorizing the pointwise mutual information of the data, which we estimate by taking information differences between conditional predictions from a learned generative model. We justify our algorithm theoretically and empirically, demonstrating that our generative approach to representation learning avoids dimensional collapse and feature suppression in cases where commonly used methods like DINO and LeJEPA fail. Moreover, we show our representation learning technique is scalable; expending more compute leads to predictably better latent tokenization. For the first time, we perform a careful analysis of the combined flop efficiency of tokenizer and generative model and demonstrate that our approach is a compute-optimal improvement over direct diffusion for pixel-space generation, obtaining an FID-50K of 2.18 with JiT-L. Applied to ImageNet and the text-to-image dataset GPIC, we show tokenizer encoder scaling laws for diffusability, where extrapolating our approach achieves representations in 7x fewer FLOPs than DINOv2 on ImageNet and 8x fewer FLOPs than WebSSL on GPIC.

## 5. STRATA: Self-Maintaining Structured Experience Graphs for Self-Evolving Language Agents

- Authors: Guanhua Zhu, Hanwen Li, Zhi Wei, Mengnan Du, Chenxi Yuan
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-14
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 3.2385377647978486
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.19386v1
- PDF: https://arxiv.org/pdf/2610.19386v1
- Local PDF: pdf/2026-10-16_05_STRATA_ Self-Maintaining Structured Experience Graphs for Self-Evolving Language Agents.pdf

Large language model (LLM) agents can self-evolve at test time by accumulating experience: retrieving relevant memories before acting and writing new lessons back afterwards. Yet most are single-level: trajectories, distilled workflows and reasoning items all land in one undifferentiated pool indexed by embedding similarity, with no typed abstraction hierarchy. They never forget or deduplicate, and are prone to negative transfer, where a superficially similar but directionally opposite experience is recalled and its concrete steps are copied verbatim, actively harming the agent. We introduce STRATA, a structured, outcome-grounded, self-maintaining memory that organizes experience into a three-layer graph of atomic skills and code snippets, task workflows and generalized meta-frameworks, connected by typed edges. STRATA maintains itself through five mechanisms sharing one similarity geometry: a multi-dimensional similarity that scores retrieval by operation and target; a typed reflector crystallizing procedures from successes and pitfalls from failures; community detection that induces meta-frameworks; pressure-triggered garbage collection with articulation-point protection; and contrast edges that flag confusable, direction-opposite experiences. Across four interactive benchmarks (AppWorld, WebArena, ALFWorld, ScienceWorld), two frozen backbones and seven baselines, STRATA attains the best average score while simultaneously using the lowest latency and fewest environment steps of any memory-augmented method, and 44% fewer lines of injected memory than the most context-hungry baseline. We isolate two failure modes of prior memories: single-level memory degrades sharply as the task set grows, and single-level concrete memories suffer catastrophic negative transfer, which contrast edges repair, lifting ScienceWorld from 78.7 to 96.7 within the same system.

## 6. Discovering Undisclosed Concepts in LoRA Adapters for Diffusion-Based AIGC Models

- Authors: Yupeng Qiu, Han Fang, Dhananjai Sharma, Ee-Chien Chang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-13
- DOI: Unavailable
- Categories: cs.AI, cs.LG
- Relevance: 3.2313248476520675
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.18990v1
- PDF: https://arxiv.org/pdf/2610.18990v1
- Local PDF: pdf/2026-10-16_06_Discovering Undisclosed Concepts in LoRA Adapters for Diffusion-Based AIGC Models.pdf

Low-Rank Adaptation (LoRA) has made diffusion model personalization affordable and widely shareable, but it also creates moderation risks when harmful or problematic content is not faithfully disclosed. Hence, it is desired to develop a mechanism that, given a LoRA adapter, discovers the concept it was trained to generate, so as to support downstream investigation. We characterize the target concept through the conditioning input that most clearly exposes what the LoRA has learned. Such an input should induce coherent LoRA outputs that are distinctive from those of the base model and strongly align with the learned LoRA subspace. We therefore formulate concept discovery as searching for the conditioning input that jointly maximizes output coherence, LoRA-induced distinctiveness, and subspace alignment. Even with a clear objective, however, optimizing it over an open-ended input space is prohibitively expensive, since reliable evaluation of coherence and distinctiveness requires repeated diffusion rendering. Crucially, we observe that an input need not be rendered to determine whether it is promising. Its alignment with the learned LoRA subspace provides a lightweight signal for localizing promising candidates before visual verification. Based on this insight, we develop a two-stage framework for text-to-image LoRAs. Subspace-Guided Evolutionary Search (SGES) uses render-free subspace alignment to explore candidate prompts and retain a compact shortlist, while Paired Visual Identification (PVI) renders only these candidates and compares the LoRA and base-model outputs to identify those exhibiting coherent and distinctive generation behavior. This design enables efficient and reliable discovery of previously unknown concepts encoded in LoRA adapters.

## 7. Learning Across Temporal Graph Representation Silos

- Authors: Minwoo Yu, Young-guk Ha
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-14
- DOI: Unavailable
- Categories: cs.LG, cs.AI
- Relevance: 3.2123836111736157
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.19576v1
- PDF: https://arxiv.org/pdf/2610.19576v1
- Local PDF: pdf/2026-10-16_07_Learning Across Temporal Graph Representation Silos.pdf

Temporal graph data are recorded in different representations, but whether these differences also determine the scope of learned knowledge reuse remains unclear. This study investigates whether predictive structure learned from relational histories can be reused between continuous-time dynamic graphs (CTDGs) and temporal knowledge graphs (TKGs). Bidirectional reuse emerges while retaining distinct input and prediction interfaces and independent vocabularies, and sources with the same representation are not always more useful. Controlled reorganizations of source histories show that the organization contributing to reuse varies across source-target conditions. We show that learned aspects of Relational Dynamics, the predictive structure present in relational histories, can be reused across conventional representation boundaries. Independently pretrained TKG and CTDG learners can also be fused at the score level to improve prediction on a third dataset without entity or relation-semantic alignment. Two proofs of concept in recommendation and security detection illustrate that external temporal sources without direct alignment can also become useful pretraining resources.

## 8. Graph-Based Orchestration of Heterogeneous AI Models: A Control Node Approach to Composite Intelligence

- Authors: G. Michael Youngblood, Filip Dvořák, Slavo Švancár, Tomáš Balyo, Michal Ficek, Martin Dousek
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-13
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 3.2026918341077995
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.19136v1
- PDF: https://arxiv.org/pdf/2610.19136v1
- Local PDF: pdf/2026-10-16_08_Graph-Based Orchestration of Heterogeneous AI Models_ A Control Node Approach to Composite Intelligence.pdf

We present a graph-based framework for Composite AI systems that integrate multiple AI techniques to address complex problems. We describe an architecture using specialized control nodes to orchestrate diverse models including planning, machine learning, constraint programming, and large language models. The system employs directed acyclic graphs and behavior trees to manage model relationships and execution sequencing. Our methodology encompasses data connectors, computational services, and a containerized deployment framework supporting hierarchical, sequential, and concurrent model composition patterns. Through case studies, we demonstrate how this architecture enables the creation of composite systems that leverage the strengths of multiple AI techniques within a unified operational schema, overcoming the limitations of single-model approaches.

## 9. Why don't Graph Transformers attend to the same token?

- Authors: Alexandre Bismuth
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-14
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.1939600288848125
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.19324v1
- PDF: https://arxiv.org/pdf/2610.19324v1
- Local PDF: pdf/2026-10-16_09_Why don't Graph Transformers attend to the same token.pdf

In large language models (LLMs), attention concentrates heavily on the first token. This 'attention sink' is believed to protect deep models against over-mixing. Even though graph transformers face a related pressure, we find that a SoTA graph transformer, GRIT, rarely forms sinks on molecules, and that it sinks less when trained on larger graphs, the opposite of the trend in LLMs. In principle, a graph can prevent sinks: we prove and show empirically that its symmetry and locality limit the attention any node can receive. On molecules, however, with distinguishable atoms and global attention, neither limit prevents sinks; what stops them lies in the model. We find that the attention scoring function is the main cause. Replacing GRIT's gated logit with a dot product raises its sink rate from 0.09 to 0.68 on identical graphs. In Graph Transformers using dot-product attention, removing the sink gives about the same error as removing a random node, while GRIT's most-attended nodes matter to its predictions. Attention sinks are therefore a property of dot-product attention rather than of Transformers. In our experiments, they form when dot-product scoring has a distinguishable node to concentrate on.

## 10. TEX-MEX: Similarity-Guided Temporal Contrastive Learning for Time Series

- Authors: Aditya Radhakrishnan, Maxwell A. Xu, Wanting Mao, Santosh Kumar, Harish Haresamudram, James M. Rehg
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-14
- DOI: Unavailable
- Categories: cs.LG, cs.AI
- Relevance: 3.0913443307333255
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.19557v1
- PDF: https://arxiv.org/pdf/2610.19557v1
- Local PDF: pdf/2026-10-16_10_TEX-MEX_ Similarity-Guided Temporal Contrastive Learning for Time Series.pdf

Contrastive learning for time series depends on deciding which pairs of inputs should be treated as similar and dissimilar. Because few augmentations reliably preserve meaning in time series, prior methods have relied on two disjoint notions of similarity between windows: structural similarity, which relates windows with similar morphology, and temporal similarity, which relates windows that occur close together in time. We introduce TEX-MEX, to our knowledge the first approach to unify the two into a single relationship. Given a random batch of windows drawn across the dataset, TEX-MEX uses the encoder to identify which windows are structurally similar or dissimilar to each other. It then pulls each window toward the temporally shifted versions of similar windows and pushes it away from those of dissimilar ones, learning what typically accompanies similar windows in time. Across PPG, EEG, ECG, accelerometry, and continuous glucose monitoring, TEX-MEX broadly achieves state-of-the-art performance against contrastive, reconstructive, JEPA-based, and modality-specific approaches, establishing it as a strong general SSL objective. We further train a 560K-parameter PPG foundation model that achieves state-of-the-art performance across a broad range of downstream benchmarks while being roughly 50x smaller than the next-best unimodally pretrained PPG foundation model in our evaluation. We will release this foundation model open-source and open-weight to the community to support future work and practical applications.

## 11. A Two-Level Clinical Novelty Prioritization Framework for Disease Trajectories Discovered from Longitudinal Electronic Health Records

- Authors: Jin-Jia Zheng, Vincent S. Tseng
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-14
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.0738679432053226
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.20512v1
- PDF: https://arxiv.org/pdf/2610.20512v1
- Local PDF: pdf/2026-10-16_11_A Two-Level Clinical Novelty Prioritization Framework for Disease Trajectories Discovered from Longitudinal Electronic H.pdf

Graph-based analysis of electronic health records (EHRs) yields disease-trajectory catalogs, but structural support does not establish semantic novelty. We present a two-level framework to prioritize 99,527 branching motifs previously discovered by an upstream patient-disjoint, train-only MIMIC-IV v3.1 pipeline and frozen after validation-based catalog selection. The framework separates path-level and node-to-endpoint semantic sparsity from reliability-adjusted clinical priority. Three deterministic textualizations per motif or node-target pair were embedded with BAAI/bge-small-en-v1.5 and calibrated against 166,972 pre-2023 PubMed references using mean top-20 cosine distance. Positive recombination occurred in 8.63% of motifs and had negligible effect on global ranking, whereas specificity and support/GNN reliability terms changed clinical-priority ordering. Robustness analyses across neighbor counts, templates, encoders, generic-label taxonomies, score settings, PrimeKG, and corrected density-based RND showed that broad ordering was more stable than hard top-k membership. A semantic-dose analysis did not support a monotonic relation between score and forecasting benefit after endpoint and token-count adjustment (1.96 days per SD; 95% CI, -0.75 to 4.68). In the frozen catalog-q90 high-semantic subgroup, branch-enhanced forecasting reduced conditional event-time MAE by 20.1 days (95% CI, 13.3-27.0) and sMAPE by 2.37 percentage points (95% CI, 1.81-2.93), while discrimination and endpoint-ranking differences were inconclusive. Corrected RND showed low tail agreement with the primary score (Spearman rho = 0.430; q90 Jaccard = 0.125) despite a similar aggregate timing association. These findings support representation-aware, uncertainty-aware literature-relative prioritization of discovered trajectories rather than causal discovery or clinician-adjudicated novelty.

## 12. TopicMerge: A Divide and Conquer Approach to Topic Modeling

- Authors: Matthew Raffel, Lizhong Chen, Sai Munikoti, Sameera Horawalavithana
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-14
- DOI: Unavailable
- Categories: cs.CL, cs.LG
- Relevance: 3.041789034381295
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.19323v1
- PDF: https://arxiv.org/pdf/2610.19323v1
- Local PDF: pdf/2026-10-16_12_TopicMerge_ A Divide and Conquer Approach to Topic Modeling.pdf

Recent advancements in topic modeling have split into two main paths: efficient embedding-based methods that offer scalability but are often outperformed on standard clustering metrics, and Large Language Model (LLM) approaches that achieve state-of-the-art clustering performance but at the cost of prohibitive computational expense and poor scalability. This paper introduces TopicMerge, a novel multi-stage pipeline that bridges these approaches to achieve both state-of-the-art clustering performance and computational efficiency. TopicMerge first employs an efficient clustering pipeline to deliberately over-segment a document corpus into a large set of fine-grained, semantically pure micro-clusters, which are then given initial semantic labels. It then introduces a novel, iterative merging algorithm where an LLM, guided by local neighborhood context, arbitrates on consolidating candidate pairs. These approved merges are then selectively executed and semantically relabeled by the LLM, hierarchically building broader, more coherent topics. Extensive experiments on the Bills and Wiki datasets show that TopicMerge achieves state-of-the-art clustering performance while reducing required LLM calls by over 92% compared to document-level methods, offering a practical and scalable solution.

## 13. Are We Overthinking One-Step Generation?

- Authors: Woobin Park, Jaeyeon Kim, Yilun Du, Sitan Chen, Bohyung Han
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-14
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.020912046715681
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.20331v1
- PDF: https://arxiv.org/pdf/2610.20331v1
- Local PDF: pdf/2026-10-16_13_Are We Overthinking One-Step Generation.pdf

Diffusion and flow matching are now dominant frameworks for generative modeling in continuous domains, but they typically require multiple network evaluations at inference. This has motivated extensive research on one-step generative modeling primarily built on diffusion and flow, though existing approaches often rely on complex training machinery. In this work, we introduce Priming Models, a simple two-stage framework for training one-step generators. Motivated by the difficulty of distributional training from scratch, Priming Models are first trained on a reconstruction objective, e.g., pixel-space denoising at a fixed noise level, before undergoing feature-space distributional post-training. Our central scientific finding is that this simple reconstruction stage is already enough to entirely alleviate the difficulty of distributional training. Empirically, across class-conditional image generation, text-to-image generation, and world modeling, Priming Models significantly advance the Pareto frontier of training compute vs. generation quality. On ImageNet at $256 \times 256$ resolution, we achieve a state-of-the-art FID of $1.19$ among one-step generators using approximately one-tenth the training compute of prior methods with comparable FID. We open-source our codebase at https://github.com/JaeyeonKim01/priming.

## 14. Cortex: Consolidating Context into Parametric Memory

- Authors: Jintian Zhang, Feng He, Xinnian Liang, Ziwen Xu, Haoming Xu, Haojing Huang, Shuangzhi Wu, Ningyu Zhang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-14
- DOI: Unavailable
- Categories: cs.CL, cs.AI, cs.CV, cs.LG, cs.MA
- Relevance: 3.017804394530568
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.20399v1
- PDF: https://arxiv.org/pdf/2610.20399v1
- Local PDF: pdf/2026-10-16_14_Cortex_ Consolidating Context into Parametric Memory.pdf

Context can improve large language model performance, but these gains may be lost after context removal. Inspired by biological systems consolidation, we formulate Memory Consolidation (MC) as internalizing these gains while preserving non-target capabilities, connecting context-specified editing, skill learning, and behavioral steering under a common objective. We introduce a five-task-family testbed measuring consolidation and retention under single, batch, and sequential updates. We propose Cortex, which generates prospective queries to anticipate uses of context and distills context-conditioned outputs into mergeable low-rank or structural feed-forward network updates. Across 4B--120B dense and mixture-of-experts backbones, including both text-only and multimodal models, Cortex lies on the empirical consolidation--retention Pareto frontier in most evaluated settings. After 50 sequential factual edits on a 14B model, Cortex-Structural recovers 88.9% of the context-induced gain while retaining 99.8% of original non-target performance.

## 15. CktHGVAE: A Symmetric Design/State Heterogeneous Graph Variational Autoencoder for Transistor-level Analog/Mixed-signal Circuit Design and Analysis

- Authors: Shigeyasu Uno
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-14
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.0143719296269325
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.19508v1
- PDF: https://arxiv.org/pdf/2610.19508v1
- Local PDF: pdf/2026-10-16_15_CktHGVAE_ A Symmetric Design_State Heterogeneous Graph Variational Autoencoder for Transistor-level Analog_Mixed-signal.pdf

We propose CktHGVAE, a heterogeneous graph variational autoencoder for transistor-level analog/mixedsignal CMOS circuits that takes not only design variables but also state variables as its inputs and outputs. With a single hyperparameter configuration without topology-specific tuning, comparison between model-generated and SPICE-simulated circuit operational states gives median R2 values above 0.9 for typical single-ended voltage amplifiers and the CMOS inverter, and 0.81-0.96 for differential amplifiers with larger datasets. Latent-space optimization in the PCA-reduced latent space with Bayesian optimization, evolutionary search, random search, and quasi-exhaustive search is demonstrated for a common-source voltage amplifier with NMOS input and resistive load, where the objective function is defined as a penalty for deviation from required circuit specifications. For each search strategy, 93.3 - 100% of all design candidates suggested by the model satisfy the required circuit specifications at the decoder output, and SPICE simulations verify that 90 - 100% of them indeed satisfy the requirements. The model pretrained on a batch of topologies can be transferred to unseen topologies without retraining at all, with zero-shot reconstruction median R2 values of 0.72-0.90 in three of four scenarios, including transfer from single-ended to differential topologies, although the transfer fidelity depends on the choice of pretraining topologies. Our demonstrations suggest that the proposed model can potentially serve as a basis for AMS CMOS circuit design automation.

## 16. Learning Graph Energies for Finite-Time Generation

- Authors: Amartya Banerjee, Xingyu Xu, Caroline Moosmüller, Harlin Lee
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-14
- DOI: Unavailable
- Categories: cs.LG, cs.AI
- Relevance: 2.99103783122753
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.19946v1
- PDF: https://arxiv.org/pdf/2610.19946v1
- Local PDF: pdf/2026-10-16_16_Learning Graph Energies for Finite-Time Generation.pdf

Energy-based models can represent distributions over discrete structures such as molecular graphs, but an energy that is accurate at equilibrium need not yield accurate samples when the sampler stops after a fixed number of steps. We introduce finite-horizon energy learning, which adapts the acceptance energy of a Metropolis--Hastings sampler to the distribution it returns after a prescribed number of steps, with initialization, proposals, and annealing schedule held fixed. For graph generation, a frozen pretrained model supplies initialization and proposals, and a learned energy governs acceptance. A training-only discriminator scores completed samples, and coupled continuations of the accepted and rejected branches of a proposal give an acceptance-gradient estimator that is unbiased for a fixed discriminator under stated conditions, without equilibrated negative samples or differentiation through discrete states. Generation uses the learned energy in the original single-trajectory sampler, without discriminator evaluations or reranking. On twelve pairwise binary targets with exactly evaluated terminal laws, learned energies have lower median terminal total variation than the equilibrium-correct energy in every tested short-horizon setting, and than its numerically tuned scalar multiple in most settings. On MOSES, a learned two-coefficient combination of pretrained Graph Energy Matching (GEM) potentials lowers FCD by 3.7--10.5\% relative to scale-calibrated GEM at matched sampling steps, with validity gains at the shortest budget and a sub-point validity trade-off at higher budgets.

## 17. A Graph-Based Analysis of Comparability, Scale, and Attribution in Private Transformer Inference

- Authors: Souvik Das, Ariful Azad, Nitesh Saxena
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-14
- DOI: Unavailable
- Categories: cs.CR, cs.LG
- Relevance: 2.9505275037520318
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.19607v1
- PDF: https://arxiv.org/pdf/2610.19607v1
- Local PDF: pdf/2026-10-16_17_A Graph-Based Analysis of Comparability, Scale, and Attribution in Private Transformer Inference.pdf

Rising privacy concerns around large language models have accelerated research in private Transformer inference (PTI). Synthesizing the empirical claims in this line of research, however, is hindered by multi-dimensional cryptographic progress and inconsistent evaluation contracts. In this work, we systematize the field by constructing an empirical graph of 62 PTI systems, mapping system attributes to node features and evaluation compatibility to edges. A three-tiered analysis of this graph illuminates the state of private inference. Node-level attribution shows that cryptographic progress drives performance gains across most systems, yet always co-occurs with other factors (model fidelity, hardware, cost accounting). Edge-level auditing shows that only 1 of 1891 candidate system pairs is directly comparable under shared assumptions. Finally, graph-level analysis shows that the scaling frontier of private inference has plateaued at 13B parameters and projects the cost of deploying current PTI techniques on production-scale Transformers. Overall, this graph-based framework equips the community to evaluate PTI claims transparently and channel technical speedups into deployment-scale private inference.

## 18. Spectral-MoE: Heterogeneous Per-Layer Expert Utilization in Dense-to-MoE Conversion

- Authors: Zachary Broveak, Christian Kubicka, Thierry Tambe
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-13
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 2.9191306252545557
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.19232v1
- PDF: https://arxiv.org/pdf/2610.19232v1
- Local PDF: pdf/2026-10-16_18_Spectral-MoE_ Heterogeneous Per-Layer Expert Utilization in Dense-to-MoE Conversion.pdf

Large language models impose substantial memory demands and arithmetic costs during inference. Dense-to-mixture-of-experts (MoE) conversion is a model optimization technique that aims to reduce these arithmetic costs. Dense-to-MoE conversion partitions pretrained feed-forward network (FFN) neurons into experts and selects a subset for each token. Leading methods fall into two categories: analytic methods produce a converted model quickly using heuristics, while learning methods produce a model much more slowly by optimizing via gradients. Both approaches, however, fix the same active expert count, or "utilization," at every layer. We introduce Spectral-MoE, which learns to allocate a utilization budget heterogeneously across layers. Its name draws a metaphor between separating a dense FFN into experts and separating a light beam into its spectrum. Spectral-MoE consists of two distinct approaches: a static approach that uses a single per-layer scalar which is shared across tokens, and a dynamic approach which emits a per-token schedule. We demonstrate that both allocators improve performance over uniform on both the analytic-based and learning-based SOTA dense-to-MoE methods. At 25% FFN utilization, dynamic allocation reduces WikiText-2 perplexity relative to uniform by 1.04, 2.96, and 2.71 points on the learned base for Llama-2-7B, Llama-3-8B, and Qwen2.5-7B, respectively. The corresponding reductions on the analytic base are 2.45, 6.26, and 2.17 points. On the learned base, dynamic allocation improves six-task mean accuracy over uniform by an average of 1.5, 4.2, and 3.6 percentage points across the three models at FFN utilizations of 12.5%, 25%, and 50%, respectively. These results establish per-layer expert utilization as a novel optimization axis in dense-to-MoE conversion.

## 19. Self-Conditioning Enables Deep Sequential Reasoning in Flow Matching

- Authors: Zeyang Zhang, Linxiang Gao, Meiqi Gu, Xingyan Chen, Minrui Luo, Kaifeng Lyu, Tianxing He
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-14
- DOI: Unavailable
- Categories: cs.CV, cs.LG
- Relevance: 2.9085938298197043
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.19628v1
- PDF: https://arxiv.org/pdf/2610.19628v1
- Local PDF: pdf/2026-10-16_19_Self-Conditioning Enables Deep Sequential Reasoning in Flow Matching.pdf

Recent work has explored visual reasoning through image generation, where models solve visual-reasoning problems by directly generating solution images. Intuitively, iterative samplers such as flow matching are well suited to this task, since each sampling step may resemble one reasoning step. However, in this work, from a circuit complexity perspective, we show that this intuition is misleading. We prove that as long as the model outputs satisfy certain mild regularity conditions, the trajectory of the vanilla flow-matching sampler can be simulated by a constant number of sequential rounds of parallel model evaluations. Consequently, additional sampling steps cannot increase the expressive power of a constant-depth backbone model under the standard complexity-theoretic model of transformers. We then reveal that self-conditioning, which conditions the model on the previous step's estimate of the final image, plays a previously unrecognized role in removing this bottleneck. Controlled experiments on diverse visual-reasoning tasks show that flow matching with self-conditioning achieves higher accuracy and greater reasoning depth than vanilla flow matching, and its performance improves with more sampling steps. Theoretically, we prove that with self-conditioning, a constant-depth backbone can achieve expressive power equivalent to that of space-bounded Turing machines. Our study suggests a design principle for future visual reasoning research: carry more information between sampling steps, so that additional steps translate into deeper reasoning.

## 20. From Relevance to Validity: Zero-Shot Tool Selection via Functional and Contextual Validation

- Authors: Xiaoxuan Dong, Jin Zhang, Zichen Yuan, Yue Zhou, Zihao Rao, Dexu Yu, Tingyong WU, Wenhao Deng, Junchen Fu, Pengwei Sun, Yang Ran, Bo Lan, Yongxin Ni, Youhua Li
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-14
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 2.8927044706628013
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.20388v1
- PDF: https://arxiv.org/pdf/2610.20388v1
- Local PDF: pdf/2026-10-16_20_From Relevance to Validity_ Zero-Shot Tool Selection via Functional and Contextual Validation.pdf

Large language model (LLM) agents increasingly face tasks from unseen domains and execution contexts, making zero-shot tool selection essential for identifying tools that can satisfy task requirements. Existing dominant methods mainly rely on relevance ranking, but semantic matching alone cannot ensure that a tool is functionally compatible or remains applicable in a new context. We preliminarily identify a \emph{transfer-validity gap}, where semantically relevant tools may still fail to satisfy functional or contextual requirements after transfer. To address this gap, we propose \methodname{}, a progressive validation framework that complements semantic relevance with endpoint-grounded functional compatibility and task-conditioned contextual evidence. Across cross-domain and cross-dataset transfer, \methodname{} consistently improves capability ranking, with larger gains under functional or contextual ambiguity. Ablation results further confirm the complementary contributions of functional and contextual validation.

## 21. When Does Depth Help? Understanding Layerwise Inference in Tabular Foundation Models

- Authors: Wenwen Gong, Haotian Gu, Zhen Yang, Jiaying Ma, Hanqing Zhang, Zhongshen Wang, Jingjun Wang, Shouyi Xu, Wei Wang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-14
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 2.8821316077313157
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.19814v1
- PDF: https://arxiv.org/pdf/2610.19814v1
- Local PDF: pdf/2026-10-16_21_When Does Depth Help_ Understanding Layerwise Inference in Tabular Foundation Models.pdf

Transformer-based tabular foundation models (TFMs) achieve state-of-the-art performance on small to medium-sized tabular prediction tasks while processing diverse inputs through a shared stack of layers. Recent layerwise analyses identify strong predictive performance in early TFM representations and substantial overlap in computation across layers. However, early predictive accessibility alone does not establish whether later layers are dispensable for every input, and aggregate accuracy can obscure which inputs benefit from additional computation. We study all 24 in-context-learning layers of TabPFN-3 across 272 classification datasets, combining representation geometry, prediction trajectories, truncation, and structural interventions, while also examining related representation dynamics in four additional TFMs. We uncover a pronounced expansion-compression trajectory, with stronger late dimensional contraction associated with larger increases in class-prototype separation. A targeted analysis of early-stabilizing samples shows that substantial representational changes persist after predicted classes stabilize, while locally ambiguous queries obtain larger accuracy gains from shallow to late layers than well-separated queries. Repeating a single pretrained block or perturbing layer order reduces predictive performance on average, constraining simple post-hoc substitutions in the frozen model. These findings distinguish predictive accessibility, class stability, and the benefits of continuing computation, supporting an input-dependent assessment of depthwise redundancy in TFMs.

## 22. RA$^2$: Retain-Anchored Attraction Preserves Forget-Adjacent Utility in LLM Unlearning

- Authors: Zinan Ling, Yang Xiao, Ruimeng Ye, Sijia Liu, Bo Hui
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-14
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 2.879058131470726
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.19385v1
- PDF: https://arxiv.org/pdf/2610.19385v1
- Local PDF: pdf/2026-10-16_22_RA$^2$_ Retain-Anchored Attraction Preserves Forget-Adjacent Utility in LLM Unlearning.pdf

Large Language Model (LLM) unlearning is often evaluated primarily by target suppression and clean retain utility. These metrics can miss a local failure mode: a model may perform well on standard retain prompts, yet degrade on benign reasoning when prompts lie near the forgotten domain. This phenomenon is termed forget-adjacent utility loss. A fundamental question is: where should forget representations go after they leave the removed behavior? Successful unlearning depends not only on whether forget-conditioned representations depart from the harmful computation, but also on the direction in which they are redirected afterward. We propose RA$^2$ (Retain-Anchored Attraction), a latent-space unlearning method that redirects forget-token states toward nearby retain-supported representations while preserving higher-layer behavior on retain data. On WMDP and MUSE, RA$^2$ yields higher forget-adjacent utility than strong unlearning baselines at similar broad-utility levels. These results show that the migration direction of forget representations materially affects benign behavior near the forget boundary. Our code is available at https://github.com/ZacLing/retain_anchored_attraction.

## 23. Weighted Adjoint Matching: Finetuning Flow Matching Models with Time-Dependent Control Cost

- Authors: Eliot Beyler, Francis Bach
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-14
- DOI: Unavailable
- Categories: stat.ML, cs.LG
- Relevance: 2.8603356498074373
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.20035v1
- PDF: https://arxiv.org/pdf/2610.20035v1
- Local PDF: pdf/2026-10-16_23_Weighted Adjoint Matching_ Finetuning Flow Matching Models with Time-Dependent Control Cost.pdf

We introduce Weighted Adjoint Matching, a method to finetune a pretrained diffusion or flow matching model given a differentiable reward. We derive it from Adjoint Matching, which reformulates finetuning as a stochastic optimal control problem with a quadratic control cost. Building on the observation that these models generate coarse features before fine details, we place a time-dependent weight on the control cost. A high cost early in the generative process preserves balance and diversity in the coarse features, which carry most of the semantics, while a low cost at the end lets the model increase the reward by refining details. We prove that our method is equivalent to maximizing the reward under time-varying Kullback--Leibler regularization on the generative paths. Experiments on Gaussian mixtures and on MNIST show a better tradeoff between reward and mode balance than Adjoint Matching.

## 24. Interlock: From Local Correctness to Task Completion in Long-Horizon Agents

- Authors: Linji Hao, Yanji He, Zihan Wang, Hansi Yang, Jiayuan Zhang, Hongyan Hao, Qi Gu, Yan Feng, Han Wu
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-14
- DOI: Unavailable
- Categories: cs.CL, cs.AI
- Relevance: 2.850169510086538
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.19686v1
- PDF: https://arxiv.org/pdf/2610.19686v1
- Local PDF: pdf/2026-10-16_24_Interlock_ From Local Correctness to Task Completion in Long-Horizon Agents.pdf

Large language model agents increasingly undertake long-horizon tasks in complex environments characterized by fragmented evidence, partially completed states, and dependencies across resources and artifacts. Existing agents may satisfy individual requirements while failing to maintain these relationships, producing locally correct but incomplete outcomes. These failures arise because task completion depends on relationships among environmental evidence, consequential decisions, and required effects. To address this completion gap, we propose Interlock, a framework for task synthesis that represents each task as a typed completion graph. Grounding edges connect public evidence to decisions, coupling hyperedges impose joint constraints across components, and realization edges connect decisions to all required downstream effects. Interlock compiles this graph into a resettable workspace, a public request, and an evaluation rubric. A source-coverage review checks whether the original requirements survive generation, while a public-input review checks whether the rubric is supported by the materials available to the solver. An agent-as-judge inspects execution artifacts and runs verification scripts, retaining trajectories judged to satisfy all mandatory requirements. To evaluate training utility, we fine-tune two Qwen3.6 backbones on their own accepted trajectories. Across the two backbones, training improves AutomationBench task pass rates by 4.00-4.50 percentage points, JobBench weighted scores by 3.20-6.64 points, and Harvey LAB criterion pass rates by 3.89-4.16 percentage points. These results demonstrate the training utility of the synthesized experience across external task environments.

## 25. Continual pretraining Prostate MRI ViT Encoder for task alignment

- Authors: Bilal A. Sidiqi, Yipei Wang, Shaheer U. Saeed, Shiqi Huang, Daniel C. Alexander, Yipeng Hu
- Source: arxiv
- Venue type: preprint
- Journal: 2026 IEEE 23rd International Symposium on Biomedical Imaging (ISBI)
- Publication status: preprint
- Publication date: 2026-10-14
- DOI: Unavailable
- Categories: cs.CV, cs.LG
- Relevance: 2.8366462605834197
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.20217v1
- PDF: https://arxiv.org/pdf/2610.20217v1
- Local PDF: pdf/2026-10-16_25_Continual pretraining Prostate MRI ViT Encoder for task alignment.pdf

Building foundation models for MRI has emerged as a promising direction for advancing medical image analysis and improving accessibility of task specific models. Existing approaches primarily focus on effective pretraining strategies and evaluating their performance across diverse downstream tasks. While these methods show performance gains, limited attention has been given to understanding task alignment between pretraining and downstream objectives. Unlike language models, where the two stages are naturally aligned, such alignment is less evident in vision based applications. Motivated by this gap, we explore continual pretraining. Specifically, continually pretraining a pretrained ViT encoder using Low-Rank Adaptation (LoRA) on a prostate segmentation task to enhance task alignment and downstream performance. We further perform layer-wise representational analysis using Centered Kernel Alignment (CKA) to assess representational shifts and their correlation with task outcomes. Our experiments show improved performance in 3 of 6 downstream tasks and comparable results in the others. Our Feature analysis reveals that, for segmentation tasks, continually pretrained encoder features exhibit greater similarity to those of the finetuned encoder than the original pretrained encoder, correlating with observed performance gains.

## 26. Scellmate enables contamination aware curation and host mobilome linkage analysis of large SAG datasets

- Authors: Yan-Ren Wang, Xiaoqing Xu, Xi Chen, Yulin Zhang, Wenshan Zheng, Tong Zhang
- Source: openalex
- Venue type: journal
- Journal: Nature Communications
- Publication status: published
- Publication date: 2026-10-13
- DOI: https://doi.org/10.1038/s41467-026-78527-4
- Categories: Genomics and Phylogenetic Studies, Microbial Community Ecology and Physiology, Single-cell and spatial transcriptomics
- Relevance: 2.83599464287407
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://doi.org/10.1038/s41467-026-78527-4
- PDF: Unavailable
- Local PDF: Not downloaded

Single-cell genomics enables cell-resolved insights into in-situ microbial communities, yet single amplified genomes (SAGs) are often fragmented, taxonomically ambiguous, and prone to contamination, limiting their biological interpretation. Here, we present Scellmate, a scalable, semi-supervised framework that integrates whole-SAG curation, species-level taxonomic anchoring and SAG–mobilome linkage analysis for large-scale SAG datasets. Following benchmarking of its SAG curation and SAG–eMGE linkage modules using in silico and four-strain mock SAG datasets, respectively, Scellmate was applied to 11,976 sewage-derived SAGs. This approach yielded 4,198 SAGs passing Scellmate’s whole-SAG curation, which captured pronounced heterogeneity masked by bulk methods. At the species level, we resolved extensive hidden diversity within abundant taxa such as Aliarcobacter that was unresolved by matched metagenome-assembled genomes; at the strain level, we pinpointed a distinct Agathobacter rectalis cluster carrying specialized carbon-utilization pathways, suggesting niche differentiation. Leveraging these curated SAGs, we identified 6,474 host–mobilome linkages across 2,378 SAGs; these linkages not only showed high concordance with host-association data within the Integrated Microbial Genomes (IMG) system but also significantly expanded species-level host assignments. Furthermore, we detected frequent inter-species sharing patterns of diverse cryptic plasmids within the order Bacteroidales. Together, this work demonstrates that high-throughput single-cell genomics, empowered by the robust framework, resolves fine-scale heterogeneity and host–mobilome dynamics, advancing culture-independent microbiome research. In this study, the authors develop a computational framework, Scellmate, that curates and analyzes large-scale microbial single-cell datasets from complex environments, and show that this helps to reveal microbial diversity and infer microbe–plasmid and microbe–phage associations in sewage.

## 27. CASI: Credit Assignment via Set Intervention for Agentic Retrieval

- Authors: Xinyi Cheng, Tianfu Zhang, Jiwen Li, Xuesen Zhang, Shihao Yu, Pengfei Zhu, Renhuan, Heda Wang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-14
- DOI: Unavailable
- Categories: cs.AI, cs.IR, cs.LG
- Relevance: 2.811058992127741
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.20293v1
- PDF: https://arxiv.org/pdf/2610.20293v1
- Local PDF: pdf/2026-10-16_27_CASI_ Credit Assignment via Set Intervention for Agentic Retrieval.pdf

Large language models increasingly generate multiple retrieval actions jointly, while downstream systems often provide only one reward for the resulting set. Broadcasting this reward provides a valid score-function gradient estimator for the expected set-level objective, but does not determine a coalition-dependent within-set attribution. We introduce CASI (Credit Assignment via Set Intervention for Agentic Retrieval), which constructs the missing counterfactual information through snapshot-grounded set intervention: generate and retrieve once, hold replayable snapshot components fixed, and evaluate alternative subsets under common conditions. Shapley aggregation converts these marginals into within-set credit, which bounded zero-sum advantage shaping incorporates into policy optimization. For m >= 4, singleton, leave-one-out, and full-set endpoints do not generally determine the Shapley allocation; under additive set values, extra coalition evaluations are redundant. In a five-action sponsored-search setting, exhaustive auction replay over 1,200 requests reveals substantial coalition dependence. Under the training-time evaluator, CASI achieves the highest median cosine similarity to a replay-defined Shapley reference among evaluated credit rules; under a sensitivity backend, CASI does not outperform Singleton. Across five independent training runs, CASI-trained policies achieve higher held-out auction-replay set value than Singleton- or Broadcast-trained policies. In a randomized seven-day production A/B test on 10% of traffic, the CASI-trained policy yields an observed 3.51% lift in the primary advertiser-value metric over production control.

## 28. Generalizing Identifiability Results in Causal Discovery from Complete Data to Missing Data Settings

- Authors: Matteo Ceriscioli, Shohei Shimizu, Mallika Gupta, Karthika Mohan
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-13
- DOI: Unavailable
- Categories: stat.ML, cs.AI, cs.LG, stat.ME
- Relevance: 2.8019375869419205
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.19211v1
- PDF: https://arxiv.org/pdf/2610.19211v1
- Local PDF: pdf/2026-10-16_28_Generalizing Identifiability Results in Causal Discovery from Complete Data to Missing Data Settings.pdf

While causal discovery methods have matured for complete data, such algorithms for handling missing values remain limited. We establish general sufficient conditions under which causal graphs remain identifiable (i.e., uniquely determined from the available data distribution) under various missingness categories, including Missing Not At Random, and provide a framework to extend correctness guarantees from causal discovery algorithms for complete data to missing data settings. Our results show that identifiability of causal graphs with no unobserved confounders is preserved when (1) missingness mechanisms do not causally interact, (2) no variable directly causes its own missingness, and (3) either faithfulness holds for missingness mechanisms, or they follow generalized linear models. Guided by these theoretical results, we introduce two asymptotically correct algorithms for Additive Noise Models (ANMs) that recover the underlying causal graph and provide consistent parameter estimates.

## 29. Rationale Distribution Distillation via Flow Matching for Distributional Continuous Latent Reasoning

- Authors: Mingyeong Kim, Gyusang Cho, Juho Lee, Giung Nam
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-14
- DOI: Unavailable
- Categories: cs.CL, cs.AI
- Relevance: 2.7999159479744575
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.19871v1
- PDF: https://arxiv.org/pdf/2610.19871v1
- Local PDF: pdf/2026-10-16_29_Rationale Distribution Distillation via Flow Matching for Distributional Continuous Latent Reasoning.pdf

Sampling multiple chain-of-thought rationales from a language model can uncover correct solutions missed by a single attempt. However, these rationales are typically lengthy, making repeated autoregressive generation costly. Continuous latent reasoning offers a compact alternative, but point-valued methods condition repeated answer sampling on a single rationale, which can limit exploration of diverse paths and answer coverage. We thus propose rationale distribution distillation (RDD), training a conditional flow over fixed-length latent sequences by distilling from multiple textual reasoning paths. Furthermore, we expand the distillation targets through within-query mixup, interpolating between complete latent rationales for the same query. The flow nonautoregressively generates the entire latent sequence, and a frozen language model autoregressively decodes answers from sampled rationale contexts. Empirically, the resulting distributional reasoner achieves higher answer coverage than the evaluated point-valued latent reasoning baselines, particularly on advanced mathematical tasks.

## 30. ListQA: A Benchmark for Evaluating List-Formatted Factual Knowledge Retrieval in Large Language Models

- Authors: Mayank Kulkarni, Rakesh Vaideeswaran
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-13
- DOI: Unavailable
- Categories: cs.AI, cs.CL
- Relevance: 2.794123160148099
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.19165v1
- PDF: https://arxiv.org/pdf/2610.19165v1
- Local PDF: pdf/2026-10-16_30_ListQA_ A Benchmark for Evaluating List-Formatted Factual Knowledge Retrieval in Large Language Models.pdf

Many real-world questions demand not a single fact but an organized collection of them, yet existing factual knowledge benchmarks almost exclusively target single answer retrieval. We introduce ListQA, a benchmark of 9,045 human-curated, cross-validated questions (audited error rate of 1.7%) that require LLMs to recall multiple facts and compose them into structured lists of 3-10 elements. Questions range from flat lists ("Which NCAA teams went undefeated between 2000 and 2024?") to hierarchical lists with sub-attributes ("...and what was their record and result?"), spanning eight categories across 60+ countries. An evergreen design (explicit temporal constraints or historically immutable facts) keeps ground truth valid without periodic updates. For evaluation, we frame element matching as a linear sum assignment problem: optimal bipartite matching paired with LLM-based semantic grading jointly captures factual accuracy, hallucination, and format compliance. We benchmark 34 models (8 families, 42 configurations across standard and thinking enabled inference) and find: the best standard-inference model scores below 37% LLM-Judge-F1, multi-faceted questions are harder across the board, and providing the source Wikipedia page lifts scores dramatically, confirming that models can organize facts but struggle to retrieve them from parameters alone. Extended analyses cover base vs. instruction-tuned checkpoints and token efficiency. We release the dataset and evaluation code.
