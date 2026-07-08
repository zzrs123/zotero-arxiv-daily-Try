# Paper Daily Reading - 2026-07-08

## 1. PhenoNEST: A Neuro-Symbolic Framework for Ontology-Aware Multimodal Plant Phenotyping and Trait Discovery

- Authors: Jayant Ghadge, Soumyashree Kar, Surya S. Durbha
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-03
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.5898569006637793
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.03245v1
- PDF: https://arxiv.org/pdf/2607.03245v1
- Local PDF: pdf/2026-07-08_01_PhenoNEST_ A Neuro-Symbolic Framework for Ontology-Aware Multimodal Plant Phenotyping and Trait Discovery.pdf

High-throughput plant phenotyping generates valuable data that often remains trapped in unstructured text and isolated RGB images. To bridge this semantic gap, we propose a framework for constructing a multimodal granular Knowledge Graph (KG) to monitor genotype-phenotype interactions across time and experiments. In this work, we focus on wheat Triticum aestivum as a representative target crop to validate our methodology across complex canopy environments. Our pipeline first distills noisy field notes to extract entities and relations, dynamically constructing the KG by converting unique instances into hierarchical class entities via RDF-typing. These graph nodes are then aligned with standardized ontologies (PO, RO, WTO) using PlantDeBERTa. To visually ground the constructed graph, a Vision-Language Model paired with a wheat-segmentation ViT generates attention-based softmaps, linking specific KG entities directly to image pixels. We introduce a central observation node Plant_Obs_Id to connect these multimodal subgraphs temporally. Evaluated on 500 curated WisWheat samples using Pointing Game accuracy, Visual Word Sense Disambiguation (VWSD), and rank-based metrics, our neuro-symbolic approach successfully maps complex field observations to a structured graph. This enables automated field note auditing, temporal stress monitoring, and precise spatial trait localization for wheat breeders.

## 2. Geometric Causal Models

- Authors: Eli N. Weinstein, David M. Blei
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-06
- DOI: Unavailable
- Categories: stat.ML, cs.LG, q-bio.BM
- Relevance: 3.525459049819214
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.05153v1
- PDF: https://arxiv.org/pdf/2607.05153v1
- Local PDF: pdf/2026-07-08_02_Geometric Causal Models.pdf

Scientists often seek to draw causal inferences from structured data that is not independently and identically distributed, such as spatial data, network data, or molecular data. We develop geometric causal models (GCMs), a framework for causal inference from dependent data that exploits underlying symmetries of the data generating process. For example, in spatial data, we consider processes that are symmetric under translations, or in graph data, symmetric under permutations of the nodes. We show how symmetries, formalized with group theory, can enable causal identification and estimation. We deploy ergodic theory for amenable groups to establish identification, and combine geometric deep learning with scalable Bayesian inference for estimation. We recover i.i.d. causal models and do-calculus when the data is a sequence and the symmetry is permutation equivariance, and find novel types of causal models when we use alternate structures and symmetries. As an example, we construct a causal model that satisfies the symmetries of DNA. This GCM enables new estimators for the effects of genetic variation, combining deep functional genomics models to describe outcomes and DNA language models to describe propensities. We illustrate on semisynthetic data.

## 3. HASSL: Hierarchy-Aware Self-Supervised Learning Framework for Single Cell Microscopy

- Authors: Julius Riel, Vishwa Mohan Singh, Sai Anirudh Aryasomayajula, Anuun Chinbat, Hannes Leonhard, Moritz Ladenburger, Frederik Alexander, Vishisht Choudhary, Fabio Laredo, Giacomo Masserdotti, Thorben Prein, Carsten Marr, Amirhossein Kardoost
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-05
- DOI: Unavailable
- Categories: cs.CV, cs.AI
- Relevance: 3.4768165196653023
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.04353v1
- PDF: https://arxiv.org/pdf/2607.04353v1
- Local PDF: pdf/2026-07-08_03_HASSL_ Hierarchy-Aware Self-Supervised Learning Framework for Single Cell Microscopy.pdf

Hierarchical structure is common in image data, where fine-grained clusters often merge into larger, coarser semantic groups. In biological cell images, current self-supervised learning models often suppress this hierarchy, as coarse factors such as imaging modality can obscure finer morphological attributes in the latent space. We propose a hierarchy-aware self-supervised training framework to address this problem. Our method combines two components: a distillation framework with a segmentation teacher to improve morphological awareness in the latent space, and a hierarchy-aware contrastive loss based on HDBSCAN to improve decision boundaries between closely related subtypes at different hierarchical levels. Together, these components reduce the tendency of self-supervised learning to overemphasize coarse factors and instead align embeddings with semantic and morphological cues. This yields biologically meaningful sub-clusters driven by fine morphological detail. We train and evaluate our method on a curated corpus of 2.3 million single cells aggregated from 20 microscopy datasets, both labeled and unlabeled, covering 208 cell classes. Our method improves over baseline and counterpart methods, increasing average top-K accuracy by 2.8%, top-9 retrieval on the dataset with the deepest hierarchy by 6.3%, and downstream F1-score for biologically relevant drug classification from perturbed cell morphology by 7.8%.

## 4. KARMA: Knowledge graph-based Automated Reasoning Materialization and Alignment

- Authors: Jinkyeong Choi, Chaebin Jeong, Donghyeon Park
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-03
- DOI: Unavailable
- Categories: cs.CL, cs.AI, cs.LG
- Relevance: 3.3813959956966326
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.03166v1
- PDF: https://arxiv.org/pdf/2607.03166v1
- Local PDF: pdf/2026-07-08_04_KARMA_ Knowledge graph-based Automated Reasoning Materialization and Alignment.pdf

Template-based contrastive synthesis is scalable, but its candidates often differ only in a few entity-slots while sequence-level optimization spreads supervision over mostly shared templates. We formalize this as the Resolution Mismatch Problem and propose KARMA, which enumerates schema-constrained paths over domain knowledge graphs and verbalizes them into slot-aligned contrastive candidates. Slot-Parallel Alignment (SPA) then applies a decoupled slot-level objective to route preference supervision to discriminative entity-slots, with slot-aware masked attention serving as an optional packed-evaluation implementation. Across biomedical, computer-science, and chemistry benchmarks, KARMA outperforms base LLM and same-data SFT baselines, and compares favorably with sequence and token-level preference methods.

## 5. Causal ASCEND: Scalable Two-tier Causal Discovery on High Dimensional Multi-omics Data

- Authors: Stephen Asiedu, David Watson
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-05
- DOI: Unavailable
- Categories: stat.ML, cs.LG, q-bio.GN
- Relevance: 3.37216652938631
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.04527v1
- PDF: https://arxiv.org/pdf/2607.04527v1
- Local PDF: pdf/2026-07-08_05_Causal ASCEND_ Scalable Two-tier Causal Discovery on High Dimensional Multi-omics Data.pdf

Biological systems exhibit a hierarchical structure, characterised by directed flow from upstream regulators to downstream effects. Although this ordering provides a natural scaffold for causal inference, most causal discovery and GRN methods either ignore the tiered organisation or condition on all upstream variables, which becomes infeasible for high-dimensional omics data. We present ASCEND (Ancestral Scalable Causal discovEry via iNherited Descent), a constraint-based framework that leverages known two-tiered structure to enable genome-scale causal discovery. ASCEND introduces a divide-and-conquer strategy that maintains dynamically updated ancestral conditioning sets for each downstream variable, dramatically reducing the number of conditional independence tests required, and achieves polynomial-time complexity where traditional approaches face exponential blow-up. Through extensive simulations and real biological data, we demonstrate that ASCEND accurately recovers ancestral relationships, scales properly and much faster, and outperforms existing gene regulatory network inference methods in both causal precision and computational efficiency. The algorithm's ability to resolve directionality makes it particularly suited for integrating multi-omic data where upstream regulators (e.g., SNPs, methylation sites) and downstream responses (e.g., gene expression) are measured jointly.

## 6. Knowledge-Informed Local Causal Discovery of Optimal Adjustment Sets

- Authors: Seong Woo Ahn, Alessandro Leite, José Lucas De Melo Costa, Fabrice Popineau, Bich-Liên Doan, Arpad Rimmel
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-05
- DOI: Unavailable
- Categories: cs.LG, stat.ML
- Relevance: 3.351391694058647
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.04447v1
- PDF: https://arxiv.org/pdf/2607.04447v1
- Local PDF: pdf/2026-07-08_06_Knowledge-Informed Local Causal Discovery of Optimal Adjustment Sets.pdf

Local causal discovery is a scalable alternative to global structure learning. However, it can struggle to identify valid adjustment sets in data-scarce settings because of finite-sample uncertainty, incomplete local neighborhoods, and unresolved Markov equivalence. Although many application domains provide structured background knowledge, its integration into local causal discovery remains limited. We propose b-LOAD, a knowledge-informed extension of the LOAD algorithm for local discovery of optimal adjustment sets. b-LOAD incorporates prior edge constraints directly into the local structure-learning procedure and uses Meek's rules to expand the discovery frontier dynamically, yielding a knowledge-constrained partially directed graph over the relevant local subgraph. This strategy helps prevent structurally relevant nodes introduced by prior knowledge from being excluded by local search. We prove that, under sound background knowledge, the procedure monotonically refines the admissible equivalence class and can enlarge the set of identifiable causal queries, enabling recovery of optimal adjustment sets that are not identifiable from observational conditional-independence information alone. Empirically, b-LOAD improves downstream causal effect estimation relative to purely data-driven and standard knowledge-augmented baselines, particularly in data-scarce and structurally complex regimes. Results on real-world biological networks show that locally targeted prior knowledge provides the largest gains and remains beneficial under moderate structural noise. These findings position b-LOAD as a scalable approach for converting fragmented domain knowledge into more reliable causal-effect estimation.

## 7. Language Models Represent and Transform Concepts with Shared Geometry

- Authors: Zhimin Hu, Lanhao Niu, Sashank Varma
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-05
- DOI: Unavailable
- Categories: cs.CL, cs.AI
- Relevance: 3.3421868168181676
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.04525v1
- PDF: https://arxiv.org/pdf/2607.04525v1
- Local PDF: pdf/2026-07-08_07_Language Models Represent and Transform Concepts with Shared Geometry.pdf

How concepts are represented in neural networks is a fundamental question in machine learning. The dominant view treats concept representations as stationary geometric objects. Yet concepts appear in context, and context transforms them. Drawing from neural population geometry, we formalize concept representations as point-cloud manifolds and contextual transformations as vector fields, and instantiate this framework in large language models. Across six model families of varying scales, we find that context moves each concept differently. The variance in these displacements is semantically organized, correlating with lexical concreteness and density. Importantly, both the concepts being transformed and this variance structure are shared across models: displacement structure transported from one model predicts held-out displacements in others significantly above chance. Together, these findings show that models share a common geometry not only in how concepts are represented, but more importantly in how context transforms them, a structure with richer organization than prior work has recognized.

## 8. GeoFlow: Geo-Aware Modeling of Inter-Area Relationships in Origin-Destination Flow Prediction and Generation

- Authors: Zherui Huang, Guanjie Zheng, Hao Xue, Linghe Kong
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-06
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.329245893742094
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.05257v1
- PDF: https://arxiv.org/pdf/2607.05257v1
- Local PDF: pdf/2026-07-08_08_GeoFlow_ Geo-Aware Modeling of Inter-Area Relationships in Origin-Destination Flow Prediction and Generation.pdf

Origin-destination (OD) flow modeling underpins urban planning and mobility analysis, but prevailing graph-based methods often neglect salient geographic attributes, limiting their ability to model long-range and multi-area dependencies. In this paper, we introduce GeoFlow, a novel framework that (i) augments area representations with geospatial attributes, including relative positions, k-hop and geodesic distances, (ii) employs a specialized geometric-intrinsic fusion encoder design that combines graph attention for intrinsic area signals with coordinate-aware encoders for global structure, and (iii) adopts an axial-global attention decoder to capture OD-specific competitive dependencies. For OD flow generation, GeoFlow is paired with flow matching models to produce more authentic and diverse mobility samples. Empirically, GeoFlow achieves superior performance in predictive accuracy, while substantially improving generative fidelity and diversity. Ablation and analytical studies confirm the contribution of each component. Code is available at https://github.com/ZheruiHuang/GeoFlow.

## 9. Localized LoRA-MoE: Block-wise Low-Rank Experts With Adaptive Routing

- Authors: Babak Barazandeh, Subhabrata Majumdar, Vinay Prithyani, George Michailidis
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-06
- DOI: Unavailable
- Categories: cs.LG, cs.AI, cs.CL
- Relevance: 3.3131244073445885
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.05114v1
- PDF: https://arxiv.org/pdf/2607.05114v1
- Local PDF: pdf/2026-07-08_09_Localized LoRA-MoE_ Block-wise Low-Rank Experts With Adaptive Routing.pdf

Large Language Models (LLMs) and high-dimensional perception networks increasingly rely on parameter-efficient fine-tuning (PEFT) to adapt to diverse operational contexts. However, standard methods like LoRA are structurally limited by a monolithic bottleneck, making them highly susceptible to gradient warfare. Interleaved multi-task streams may trigger destructive optimization feedback, collapsing adapter weights into unspecialized averages. While recent spatial partitioning methods have introduced block-wise isolation, they remain trapped in static topologies, unable to adapt to dynamic task-switching or environmental sensor failure. In this work, we introduce Localized LoRA-MoE, a unified framework that fuses localized spatial blocking with dynamic, context-conditioned routing. We propose and evaluate two novel architectural paradigms: Block-Wise LoRA-MoE (Centralized Macro-Routing), which modulates the entire structural grid via a monolithic context signal, and Cell-Wise LoRA-MoE (Decentralized Micro-Routing), which empowers every coordinate cell in the matrix grid with autonomous, localized expert gating. Through a comprehensive suite of benchmarks, ranging from high-dimensional SVD matrix simulations and real-world tabular transformations to spatial vision perception under sensor degradation, we demonstrate that both architectures resolve optimization deadlocks inherent in static baselines. Our empirical results establish that decentralized cell-level gating achieves complete statistical parity with an omniscient global coordinator, providing a robust "gradient firewall" that protects surviving pathways from fault-propagated corruption. Our proposals consistently outperform static baselines, offering a scalable and parameter-efficient solution for dynamic model adaptation across granular coordinate fields and shifting operational regimes.

## 10. Tensor-Train Joint Modeling for Few-Step Discrete Diffusion

- Authors: Byoungkwon Kim, Minhyuk Sung
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-04
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.3026110409416622
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.03788v1
- PDF: https://arxiv.org/pdf/2607.03788v1
- Local PDF: pdf/2026-07-08_10_Tensor-Train Joint Modeling for Few-Step Discrete Diffusion.pdf

Discrete diffusion promises orders-of-magnitude faster generation than autoregressive (AR) models for sequential discrete data, yet its full potential of few-step generation has remained out of reach due to a fundamental structural limitation. The conditional-independence assumption underlying current discrete diffusion models introduces a systematic parallelization bias that compounds with the number of tokens unmasked per step, becoming severe in the few-step regime that fast generation requires. We address this with the first framework for explicit joint distribution modeling in discrete diffusion via tensor decomposition, which represents the conditional clean distribution as a low-rank tensor with controllable expressivity. The framework supports both Canonical Polyadic (CPD) and Tensor-Train (TTD) decompositions, and we identify a structural bias of TTD toward dependencies between nearby tokens, formalized through Oseledets' theorem relating TT-rank to unfolding-matrix rank, which is well-suited to sequential data such as natural language and line notations for molecular data. To enable efficient generation, we present an iterative marginal inference procedure with specialization for predetermined position schedules. Our framework integrates into pretrained MDMs through lightweight fine-tuning, yielding substantial improvements in few-step generation at a fraction of the cost of training from scratch.

## 11. Steering Optimisation Trajectories in Diffusion Representation Learning

- Authors: Rajat Rasal, Avinash Kori, Tian Xia, Ben Glocker
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-06
- DOI: Unavailable
- Categories: cs.CV, cs.AI
- Relevance: 3.300792489394078
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.05319v1
- PDF: https://arxiv.org/pdf/2607.05319v1
- Local PDF: pdf/2026-07-08_11_Steering Optimisation Trajectories in Diffusion Representation Learning.pdf

We study why diffusion autoencoders can achieve similar image quality while learning substantially different latent structures. We trace this behaviour to optimisation dynamics; we analyse curves of image reconstruction against latent representation quality, revealing trajectories that organise around two distinct regimes early in training. Models in the reconstruction regime prioritise image fidelity early, whereas those in the disentanglement regime improve reconstruction and disentanglement more gradually. We hypothesise that this behaviour can be influenced by targeting shortcut pathways in the diffusion U-Net and controlling early noise-level exposure, thereby shaping the reconstruction-disentanglement trade-off during training. To steer optimisation toward stronger representations, we introduce SteeringDRL, combining gated residual U-Nets with a simple noise-level exposure curriculum for training. Across disentanglement benchmarks, SteeringDRL improves representation quality and reduces seed sensitivity. Our method further extends to spatial disentanglement in object-centric learning, improving segmentation quality on synthetic and real-world datasets.

## 12. Poisson-Gamma Modeling of Inter-Relational Dependencies in Dynamic Knowledge Graphs

- Authors: Nan Fang, Yijun Wang, Hao Liao, Sikun Yang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-03
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.2854908949375465
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.02872v1
- PDF: https://arxiv.org/pdf/2607.02872v1
- Local PDF: pdf/2026-07-08_12_Poisson-Gamma Modeling of Inter-Relational Dependencies in Dynamic Knowledge Graphs.pdf

Dynamic knowledge graphs are ubiquitous in today's AI applications, as we represent molecular structures, social relationships, and language information using these graph models. As knowledge graphs evolve over time and are often noisy and incomplete, modeling their temporal and relational dependencies becomes crucial for downstream tasks. To address these challenges, this paper proposes PGRE (Poisson-Gamma Relational Evolution), a probabilistic model for modeling inter-relational dependencies in dynamic knowledge graphs. PGRE represents multi-relational temporal links via a Poisson-Bernoulli formulation. It introduces Gamma-distributed latent variables to capture entity-factor associations and cross-relation dependencies mediated by shared latent communities. A Gamma Markov process further models the temporal evolution of these latent variables, enabling principled characterization of relational dynamics. Experiments on benchmark datasets show that PGRE achieves competitive performance in link prediction, particularly in sparse settings, while revealing meaningful relational evolution patterns in dynamic knowledge graphs.

## 13. Attention Dynamics in Diffusion Models: A Visual Analytics Framework for Human-AI Collaboration

- Authors: Yiran Xiao, George Legrady
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-06-28
- DOI: Unavailable
- Categories: cs.CV, cs.AI, cs.HC
- Relevance: 3.284011497733761
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.02563v1
- PDF: https://arxiv.org/pdf/2607.02563v1
- Local PDF: pdf/2026-07-08_13_Attention Dynamics in Diffusion Models_ A Visual Analytics Framework for Human-AI Collaboration.pdf

Diffusion-based text-to-image models can synthesize complex and highly structured visual content, yet the emergence and evolution of semantic structure remain difficult to interpret. Many existing workflows rely on aggregated attention or scalar summaries that separate temporal change from image-space evidence. To address this gap, we present a visual analytics framework for exploring attention dynamics in diffusion models: the step-indexed evolution of token-level cross-attention maps, their temporal concentration, and their spatial relationships. Our approach enables structured analysis of attention behavior across generation steps by integrating quantitative measures with data-driven stage identification in an interactive workflow. Case studies on a structured 60-prompt Stable-Diffusion-class benchmark illustrate recurring, interpretable patterns within this setting and show how linked temporal and spatial views facilitate the observation and discussion of generative processes, supporting more effective human-AI collaboration.

## 14. Predicting Therapeutic Outcome via Aligning Patient-Specific Knowledge Graph and Gene-Level Perturbation Representations

- Authors: Dongmin Bang, Sugyun An, Inyoung Sung, Ilho Yun, Sun Kim, Sangseon Lee
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-06
- DOI: Unavailable
- Categories: cs.LG, cs.AI, q-bio.QM
- Relevance: 3.2701263996980185
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.04557v1
- PDF: https://arxiv.org/pdf/2607.04557v1
- Local PDF: pdf/2026-07-08_14_Predicting Therapeutic Outcome via Aligning Patient-Specific Knowledge Graph and Gene-Level Perturbation Representations.pdf

Accurate prediction of patient-specific therapeutic response from pre-treatment transcriptomes is hindered by the scarcity of matched clinical response labels and post-treatment molecular profiles. Preclinical transfer-learning models can simulate drug-induced expression changes but are often hard to interpret and unstable, whereas knowledge-graph methods provide mechanistic context yet remain static and fail to capture drug-induced transcriptomic perturbation dynamics. We propose PREDIKTOR, a patient-centered multi-view framework that aligns a personalized network view with a transferable transcriptomic perturbation view to predict clinical drug response. For each patient, we construct an individualized gene regulatory network from tumor expression using DysRegNet and augment it with drug-target links from DrugBank; a graph neural encoder yields a drug-centric, mechanistically grounded embedding. In parallel, a frozen condition-specific gene-gene attention model pretrained on LINCS L1000 generates a simulated post-perturbation transcriptomic profile for the same patient-drug pair. We align the two views in a shared latent space via a CLIP-style contrastive objective with drug-context hard negatives, then concatenate the representations for end-to-end response classification. On TCGA, PREDIKTOR consistently outperforms state-of-the-art baselines under patient-, drug-, and tissue-split evaluations, and transfers zero-shot to the I-SPY2 trial, improving AUROC by 5.6% over competing methods. The aligned embeddings yield stable gene and pathway attributions that recover known mechanisms, supporting actionable and interpretable precision oncology.

## 15. CoFEND: A Cross-Modal Fusion End-to-End Network for Cold-Start Drug-Drug Interaction Prediction

- Authors: Di Wu, Hongyi Sun, Haichao Xu, Jia Chen, Zhong Chen, Jie Yang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-03
- DOI: 10.1145/3770855.3817946
- Categories: cs.LG
- Relevance: 3.2523589254771235
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.02928v1
- PDF: https://arxiv.org/pdf/2607.02928v1
- Local PDF: pdf/2026-07-08_15_CoFEND_ A Cross-Modal Fusion End-to-End Network for Cold-Start Drug-Drug Interaction Prediction.pdf

Cold-start drug-drug interaction (DDI) prediction for new drugs is critical for minimizing unexpected adverse drug reactions. The key challenge is to capture similarity between new and known drugs. However, such similarity is closely associated with complex relationships and mechanisms among drugs, enzymes, transporters, molecular structures, and other biomedical entities. Existing methods have three limitations in capturing such similarity: (1) only partial relationships and mechanisms are considered, which overlooks cross-modal information and yields incomplete or biased similarity modeling; (2) similarity computation between new and known drugs is conducted separately across modalities and performed offline for cold-start DDI prediction, leading to misalignment between similarity computation and DDI prediction; and (3) existing interpretability analyses are typically single-modality and focus primarily on key determinants of the perpetrator drug, while the underlying causes of susceptibility for the victim drug are seldom investigated. To address these issues, this paper proposes a novel Cross-Modal-Fused End-to-End Learning Network (CMF-ELN) with three components. First, diverse multimodal information is leveraged to construct four types of drug-centered knowledge graphs, enabling comprehensive similarity modeling under reconstruction-based supervision. Second, a four-channel graph autoencoder is designed to fuse cross-modal similarity within an end-to-end learning framework. Finally, a two-stage interpretability scheme is devised to precisely localize key factors for both perpetrator and victim drugs. Extensive experiments on two real datasets demonstrate that CMF-ELN achieves significantly higher prediction accuracy and more comprehensive interpretability of mechanisms than its peers.

## 16. Back to Basics: Improving Molecular Understanding in LLMs via SMILES-Graph Translation

- Authors: Wenda Wang, Jinjia Feng, Zhewei Wei
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-03
- DOI: Unavailable
- Categories: cs.LG, cs.AI, q-bio.BM
- Relevance: 3.235358185878028
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.03007v1
- PDF: https://arxiv.org/pdf/2607.03007v1
- Local PDF: pdf/2026-07-08_16_Back to Basics_ Improving Molecular Understanding in LLMs via SMILES-Graph Translation.pdf

Recent advances in molecular large language models have led to strong performance on molecular understanding and generation tasks, yet these gains often come without reliable structural grounding. In particular, existing approaches conflict with the chemistry principle that structure determines function: despite their downstream success, current molecular LLMs perform poorly on basic structure recognition, suggesting that they fail to capture molecular graphs from canonical SMILES. To remedy this, we propose MolBasic, a structure-first framework that strengthens structural comprehension via SMILES-Graph translation. MolBasic is built around a multi-level structure perception benchmark, where bidirectional SMILES-Graph conversion serves as the core task to align sequential and topological representations. On top of this foundation, we employ a progressive learning scheme with a standardized Chain-of-Thought (CoT) to steer models from structure acquisition toward higher-level molecular reasoning. Experiments show that MolBasic substantially improves structural understanding and yields robust gains on downstream tasks, including property prediction and objective optimization, supporting our structure-first paradigm.

## 17. Additive Causal Construction for Transferable and Reconfigurable Cross-System Learning in Multi-Source Image Fusion

- Authors: Zhizhong Fu, Wei Zhou, Zhaoyang Jiang, Yulong Lin, Yifu Hou, Xiaorong Ding, Qiang Yan, Yifan Chen
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-06-30
- DOI: Unavailable
- Categories: cs.CV, cs.AI
- Relevance: 3.2304151833082315
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.02572v1
- PDF: https://arxiv.org/pdf/2607.02572v1
- Local PDF: pdf/2026-07-08_17_Additive Causal Construction for Transferable and Reconfigurable Cross-System Learning in Multi-Source Image Fusion.pdf

In multi-source image fusion scenarios, heterogeneous inputs are typically driven by distinct generative mechanisms and can be viewed as a composition of multiple causal systems. However, cross-system discrepancy (CSD) and cross-system entanglement (CSE) commonly arise during the fusion process, often leading to significant performance degradation under out-of-distribution (OOD) predictions. To address the CSD and CSE issues, we propose the additive causal construction (ACC) framework, which characterizes information fusion at two levels: firstly, it establishes causal "anchors" shared among multiple systems through intervention consistency to enable causal graph transferability (CGT); and secondly, it formalizes the fusion process as causal construction and models the reliability of constructed paths through uncertainty quantification to ensure causal graph reconfigurability (CGR). Building upon this, we revisit the traditional causal representation learning (CRL) with ACC and propose ACC-CRL as a learnable instantiation of the framework. The method explores joint causal content representations across systems via content-mechanism decoupling, and performs response alignment under shared anchors to mitigate CSD. Furthermore, it incorporates structural uncertainty to adaptively regulate the fusion process, thereby suppressing unstable CSE. We conduct systematic experiments on synthetic data (ColorMNIST) and real-world multi-center medical imaging tasks (microvascular invasion (MVI) prediction). The results demonstrate that the proposed method significantly improves OOD generalization while maintaining in-distribution (ID) performance, validating the effectiveness and robustness of the ACC-CRL strategy based on mechanism alignment and uncertainty modeling in open environments.

## 18. Conditional Diffusion Guided Knowledge Transfer for Multi-Domain Knowledge Graph Completion

- Authors: Jiawei Sheng, Taoyu Su, Xixun Lin, Xiaodong Li, Tingwen Liu
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-03
- DOI: 10.1145/3774904.3792252
- Categories: cs.CL, cs.AI
- Relevance: 3.2167014104863245
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.03154v1
- PDF: https://arxiv.org/pdf/2607.03154v1
- Local PDF: pdf/2026-07-08_18_Conditional Diffusion Guided Knowledge Transfer for Multi-Domain Knowledge Graph Completion.pdf

Multi-domain knowledge graph completion (MKGC) aims to improve missing triple prediction in a target KG by transferring knowledge from other support KGs. Existing methods typically enforce consistency constraints on equivalent entities across KGs to transfer knowledge, which risks suppressing domain-specific contextual information of entities. This design can also compromise entity representation information from all KG domains, impeding performance improvements, especially in low-resource data scenarios. To address this, we pioneer a generation-based paradigm for MKGC and propose DMKGC, a conditional diffusion-guided knowledge transfer framework. Our key insight is to treat each KG as a partial view of the entity entire information, and generate informative domain-general entity embeddings through diffusion models conditioned on support KGs. Particularly, we first initialize domain-agnostic entity embeddings as prior entity embeddings, and then encode them within individual KGs. Afterward, we fuse equivalent entities from support KGs as the conditional diffusion generation guidance. We leverage the prior entity embeddings as the proxy generation objective, which ensures this conditional generation to be unbiased towards any conditioned KGs. Simultaneously, we also train the generated embeddings to be predictive across KGs, thus preserving domain-specific information. Extensive experiments on 14 KGs in 3 benchmarks demonstrate a 4.3\% average MRR improvement in tail entity prediction over state-of-the-art methods, with sustained gains in low-resource data settings.

## 19. A Fair Benchmarking of Deep Relational Database Learning Models

- Authors: Kazi F. Akhter, Bharath Ajendla, Manar D. Samad
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-04
- DOI: Unavailable
- Categories: cs.DB, cs.AI
- Relevance: 3.188967501732826
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.03659v1
- PDF: https://arxiv.org/pdf/2607.03659v1
- Local PDF: pdf/2026-07-08_19_A Fair Benchmarking of Deep Relational Database Learning Models.pdf

Relational databases (RDBs) are the primary data infrastructure in many enterprises, yet recent deep learning methods designed for RDBs have been evaluated under inconsistent experimental protocols, making fair comparison difficult. We present one of the first systematic benchmarking studies of recently released deep learning methods for RDBs, evaluating them across five relational databases, with one classification and one regression task for each. We refactor all deep RDB models to allow the full range of experimental procedures to be applied consistently across all methods. Our findings indicate that the relational transformer (RT) approach delivers the strongest overall performance on both classification and regression tasks compared to the state-of-the-art graph-based modeling and learning of RDBs. Even for single-table learning tasks, deep learning methods designed for RDBs outperform the leading tabular foundation model, TabPFN 2.5. Extending learning from a single table (hop = 0) to multiple tables (hop = 1, 2) by connecting neighboring tables in relational databases enhances performance, but the additional benefit from higher hops diminishes as computational overhead grows. Deep RDB learning methods have the potential to challenge state-of-the-art tabular foundation models, especially on large-scale enterprise data. The source code for this benchmarking study is publicly available.

## 20. Spectral Signatures of Large Language Models

- Authors: Zhuoying Zhang, Ishan V. Prasad, Yuanzhe Hu, Zihang Liu, Hengrui Luo, Pu Ren, Yaoqing Yang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-03
- DOI: 10.1145/3770855.3818090
- Categories: cs.CL, cs.AI
- Relevance: 3.168920495012838
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.03377v1
- PDF: https://arxiv.org/pdf/2607.03377v1
- Local PDF: pdf/2026-07-08_20_Spectral Signatures of Large Language Models.pdf

The rapidly growing repository of publicly available large language models (LLMs) presents significant challenges for systematic management and quantification at scale, such as model lineage tracing, licensing, and evaluation. However, task-specific benchmarks are insufficient for this setting, as LLMs differ widely in architectures, scales, and training procedures. To address this challenge, we adopt spectral shape-based metrics for managing and quantifying LLMs based on Heavy-Tailed Self-Regularization theory. Our approach uses the shape information of the weight empirical spectral density as a compact spectral signature of each model. This signature captures intrinsic properties of pretrained models and remains robust during post-training, making it suitable for model-level analysis. In addition, this metric is data-free, computationally-efficient, and scale-invariant, enabling large-scale analysis in practice. Moreover, we curate a large and diverse model corpus consisting of major open-source LLM families, and use it to systematically benchmark spectral and non-spectral metrics across models and downstream tasks. We show that our spectral signature supports the tracking of the model lineage, the unsupervised clustering of similar models, and the quantification of the model performance. Overall, the proposed spectral signature provides a meaningful proxy for broad performance trends across LLMs, enabling efficient organization, comparison, and analysis of large model collections.

## 21. SNR-Adaptive Unified Diffusion for Multi-Task Medical Image Segmentation

- Authors: Jiahao Liu, Hang Wei, Shuai Wu
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-03
- DOI: Unavailable
- Categories: cs.CV, cs.AI
- Relevance: 3.1529908493185443
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.03103v1
- PDF: https://arxiv.org/pdf/2607.03103v1
- Local PDF: pdf/2026-07-08_21_SNR-Adaptive Unified Diffusion for Multi-Task Medical Image Segmentation.pdf

Clinical cardiac imaging pipelines currently deploy separate models for each dataset and modality, incurring redundant training costs and precluding knowledge sharing across anatomically related tasks. Consolidating semi-supervised learning, unsupervised domain adaptation, and domain generalisation into one model is therefore a practical necessity, yet naive joint training exposes a fundamental barrier: conflicting label semantics between datasets collapse LA Dice from 90.31\% to 83.38\%, while gradient imbalance across tasks of unequal complexity suppresses the weaker tasks throughout training. We present UniT-Diff, a unified diffusion segmentation framework that resolves these conflicts through three targeted mechanisms. An 11-channel task-specific output space physically partitions label categories, eliminating cross-task gradient sign reversal by construction. SNR-Adaptive Task Conditioning (SATC) scales the task token by the log signal-to-noise ratio of the current diffusion timestep, suppressing domain-specific bias during coarse denoising and restoring full task guidance as the signal clears. Task-Type-Aware Conditional Dropout (TTACD) permanently removes the task token for domain-generalisation inputs, routing them through a shared neutral pathway that draws on cross-dataset cardiac anatomy rather than source-vendor statistics. Under a single parameter set, UniT-Diff surpasses independently trained task-specific baselines on all three benchmarks simultaneously: +0.87\% on LA, +1.77\% on MMWHS, and +0.88\% on MNMS.

## 22. Folding, Reasoning, and Scaling with Open-source Drug Discovery Engine

- Authors: Aureka AI OpenDDE project
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-04
- DOI: Unavailable
- Categories: cs.AI, cs.CE, q-bio.BM
- Relevance: 3.138623621524202
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.03787v1
- PDF: https://arxiv.org/pdf/2607.03787v1
- Local PDF: pdf/2026-07-08_22_Folding, Reasoning, and Scaling with Open-source Drug Discovery Engine.pdf

Accurately modeling biomolecular interactions is a central bottleneck in biology and therapeutic discovery. Here, we introduce Open Drug Discovery Engine (OpenDDE), an open-source, all-atom biomolecular foundation model that uses co-folding as the entry point to a scalable AI-driven drug discovery engine. Rather than treating structure prediction as an isolated endpoint, OpenDDE is designed as a shared structural reasoning layer for modeling sequence-structure-function relationships across biomolecular complexes, enabling complex structure prediction today while providing a foundation for de novo design, affinity estimation, structure-conditioned optimization, and more. OpenDDE integrates advances in all-atom architecture, atomic latent reasoning, inference optimization, and large-scale data processing to achieve IsoDDE-level co-folding accuracy within a reproducible and openly accessible framework. We also identify two scaling-law directions for co-folding models, revealing practical routes for continued improvement through data, model, inference, and training scaling. By releasing training code, inference pipelines, checkpoints, and benchmarks, OpenDDE aims to democratize access to frontier biomolecular intelligence, accelerate global collaboration, and lay an open foundation for next-generation drug discovery systems that can move from predicting molecular structures toward designing, scoring, and optimizing therapeutic candidates for human health.

## 23. Target-Aware Interaction-Guided Reinforcement Learning for Black-Box Node Injection Attacks on Graph Neural Networks

- Authors: Yi Lan, Ye Yuan
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-05
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.1105452432654834
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.04091v1
- PDF: https://arxiv.org/pdf/2607.04091v1
- Local PDF: pdf/2026-07-08_23_Target-Aware Interaction-Guided Reinforcement Learning for Black-Box Node Injection Attacks on Graph Neural Networks.pdf

Graph Neural Networks (GNNs) have achieved remarkable performance in graph representation learning, yet their inherent vulnerability to adversarial attacks poses severe security risks. Especially, black-box node injection attacks have become a major threat to GNNs since they inject malicious nodes without altering the original graph topology. However, they typically decouple the generation of malicious node features and edge connections, thereby resulting in suboptimal attack efficacy under stringent budgets. To address this critical issue, this study proposes a novel Target-aware Interaction-guided Reinforcement learning for Black-box node injection Attacks on GNNs (TIRBA), which formulates the attack as a Markov Decision Process and jointly optimizes node feature generation and edge construction in a heterogeneous action space. Firstly, TIRBA designs a target-aware interaction encoder to fuse information of node features and edges. Further, it introduces a class-center guidance mechanism to utilize prior class distribution information, thereby guiding efficient exploration of the high-dimensional feature space. Finally, a topology difference-aware state value evaluation is adopted to explicitly capture local structural anomalies caused by injected nodes, thereby stabilizing the reinforcement learning training process. Experimental results demonstrate that the proposed TIRBA significantly outperforms state-of-the-art black-box node injection attack methods.

## 24. TRIAGE: Trustworthy Retrieval Instrumentation And Graph Evaluation

- Authors: Axel TahmasebiMoradi, Lucas Schott, Martin Royer
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-03
- DOI: Unavailable
- Categories: cs.IR, cs.AI, cs.CL
- Relevance: 3.1077821045435416
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.03447v1
- PDF: https://arxiv.org/pdf/2607.03447v1
- Local PDF: pdf/2026-07-08_24_TRIAGE_ Trustworthy Retrieval Instrumentation And Graph Evaluation.pdf

Knowledge graphs (KGs) that underpin Graph-based Retrieval-Augmented Generation (Graph-RAG) are increasingly built automatically by LLM-driven extraction rather than curated by experts. Proper evaluation would require instrumenting all pertinent stages: extraction, graph construction, and inference, coherently enough to localize failures, so that a failure at one stage is not discovered as a wrong answer at the end. We introduce TRIAGE, a stage-aware instrumentation framework for automated, document-grounded graph-RAG that asks not only whether the underlying graph can be trusted but at what cost it can be queried. TRIAGE attaches stage-specific, independently interpretable metrics to three stages: the KG Implementation (triple confidence, source coverage, and schema and canonicalization checks), the KG Validation by expert (graph-level structural quality, with correctness and completeness computed only as offline calibration when a reference is available), and the KG Usage (retrieval coverage, faithfulness, and retrieval cost); the deployed metrics need no gold annotations, the gold-requiring ones serving only as offline calibration. At usage time these metrics form a diagnostic chain of necessary conditions whose first broken link localizes the failure, and the diagnosis maps to the stage levers that can remedy it: extraction, graph and schema, or retrieval. TRIAGE is a theoretical framework with a proof of concept and a reproducible evaluation protocol.

## 25. Diffusion learning reveals viable parameter manifolds and compensation geometry in biological dynamical systems

- Authors: Ruilin Zhang, Louis Tao, Zhuo-Cheng Xiao
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-04
- DOI: Unavailable
- Categories: q-bio.QM, cs.LG, nlin.CD, q-bio.NC
- Relevance: 3.0971829902387316
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.03671v1
- PDF: https://arxiv.org/pdf/2607.03671v1
- Local PDF: pdf/2026-07-08_25_Diffusion learning reveals viable parameter manifolds and compensation geometry in biological dynamical systems.pdf

Models of complex systems often have many parameters, yet are constrained by far fewer experimentally accessible observables: similar activity can emerge from coordinated parameter changes. We formalize these compatible parameter sets as \emph{viable parameter manifolds}: the inverse images of a system's target dynamical behaviors under a parameter-to-feature map. The relevant codimension is not the number of reported features, but the effective rank of that map at the target scale. Co-varying features lower the codimension, while poor conditioning, high curvature, or regime mixing degrade learnability. We train conditional score-based diffusion models on simulated parameter--feature pairs and use them as amortized samplers of prior-weighted viable sets. In the Lorenz system, scalar trajectory statistics generate thin viable sheets, and two-feature conditioning localizes a transition-adjacent corridor. In the Izhikevich neuron model, four firing descriptors lie close to a nearly two-dimensional family of features, and the learned inverse images reveal distinct regular and irregular compensation geometries. In a recent ODE reduction of finite spiking networks, the same framework reveals excitatory--inhibitory compensation, timescale--coupling tradeoffs, and input-dependent viable manifolds across 4--12 parameter dimensions. In this view, robustness, compensation, and hidden parameter dependencies are organized as inverse geometry, with diffusion models providing practical tools for sampling, visualizing, and interrogating that geometry.

## 26. TACTIC-KG: Toward Small Agent Teams for Cyber Threat Intelligence Knowledge Graph Construction

- Authors: Mouhamed Amine Bouchiha, Gregory Blanc
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-06
- DOI: Unavailable
- Categories: cs.CR, cs.AI, cs.LG, cs.MA
- Relevance: 3.084134920964586
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.05001v1
- PDF: https://arxiv.org/pdf/2607.05001v1
- Local PDF: pdf/2026-07-08_26_TACTIC-KG_ Toward Small Agent Teams for Cyber Threat Intelligence Knowledge Graph Construction.pdf

Cyber Threat Intelligence (CTI) reports are predominantly unstructured, heterogeneous, and noisy, which limits their direct usability for automated analysis and reasoning. Cybersecurity Knowledge Graphs (CSKGs) provide a structured representation of adversarial entities, actions, and relations, but constructing such graphs from free-text CTI remains a challenge. Recent approaches rely on monolithic Large Language Models (LLMs) to perform end-to-end extraction and completion, leading to high cost, limited controllability, and unstable performance. This paper introduces TACTIC-KG, an agentic framework for CSKG construction that decomposes the task into modular, specialized LLM agents responsible for extraction, typing, verification, and curation. Using lightweight models (3B--8B), TACTIC-KG improves stability, recall, and graph consistency while reducing deployment cost. We implement and evaluate TACTIC-KG against recent state-of-the-art systems. Experiments on human-annotated CTI reports show that agent specialization consistently outperforms larger monolithic in-context-learning (ICL) baselines in extraction F1-score, typing accuracy, and structural graph similarity.

## 27. Order-based Causal Discovery for Multistage Processes

- Authors: Eun-Yeol Ma, Junsub Jung, Heeyoung Kim
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-04
- DOI: Unavailable
- Categories: cs.LG, cs.AI
- Relevance: 3.0787578670914026
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.03971v1
- PDF: https://arxiv.org/pdf/2607.03971v1
- Local PDF: pdf/2026-07-08_27_Order-based Causal Discovery for Multistage Processes.pdf

Causality has become an increasingly important tool for gaining a deeper understanding of complex systems. Among various causal analysis methods, causal discovery, which identifies causal relationships among variables from data, has been widely used to uncover underlying causality in diverse processes. However, while multistage processes are prevalent in many fields, existing causal discovery methods may produce counterintuitive results, given the known process knowledge, and may not be computationally efficient for handling large datasets typical of multistage processes. To address this gap, we propose a novel causal discovery method called Order-based Causal Discovery for Multistage Processes (OCDM). OCDM is designed to infer the causal structure of multistage data while preserving their inherent hierarchical and sequential structure by explicitly incorporating process knowledge into the causal discovery process. Specifically, we propose a structural knowledge-informed order-inferring algorithm that infers the causal order of variables by incorporating information about the stage from which each variable originates, based on an order-based causal discovery framework naturally suited for inherently ordered multistage data. Furthermore, to eliminate spurious edges from the initial causal graph generated based on the inferred causal order, we introduce a novel pruning technique using stochastic gated neural networks, which offers greater computational efficiency compared to existing methods. Through experiments on various datasets, we demonstrate that OCDM effectively infers the causal structure of multistage processes, outperforming existing methods.

## 28. Context-Constrained Transfer Learning for Tabular Foundation Models via Data Distillation

- Authors: Yijun Lin, Sai Li
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-06
- DOI: Unavailable
- Categories: stat.ML, cs.LG
- Relevance: 3.0632140516614625
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.04809v1
- PDF: https://arxiv.org/pdf/2607.04809v1
- Local PDF: pdf/2026-07-08_28_Context-Constrained Transfer Learning for Tabular Foundation Models via Data Distillation.pdf

Tabular Foundation Models (TFMs) have demonstrated strong empirical performance as black-box inference engines through in-context learning. However, their use in transfer learning is limited by two obstacles: strict context-size constraints and sensitivity to distribution shifts between source and target tasks. Directly pooling heterogeneous source data can therefore lead to negative transfer. To address these challenges, we propose Context-Constrained Transfer Learning via ANchoring and DIstillation (TL-ANDI), a posterior-aware distillation framework for TFMs. TL-ANDI constructs a compact source context by solving a budget-constrained optimal transport problem whose cost jointly measures target covariate coverage and posterior compatibility. The selected anchor samples are then equipped with locally distilled labels and combined with a residual calibration step using target data.

## 29. Cellular Adaptation to Signal Fluctuations as Learning

- Authors: Tuan Minh Pham, David Saad
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-03
- DOI: Unavailable
- Categories: q-bio.MN, cond-mat.dis-nn, nlin.AO
- Relevance: 3.058184549416519
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.03545v1
- PDF: https://arxiv.org/pdf/2607.03545v1
- Local PDF: pdf/2026-07-08_29_Cellular Adaptation to Signal Fluctuations as Learning.pdf

Cells represent one of the most fundamental units of life. Underlying their robust performance against environmental variability, such as temporal fluctuations of chemical signals, between different cell types, is a dynamical interrelation between the two components of an intracellular pathway: a gene-regulatory network and its upstream signal transducers. To understand how a single cell utilizes this feedback to self-regulate its gene-expressions, we develop a multiscale model of the pathway's components, in which the adaptive variables responsible for signal interpretation follow a feedback-induced learning process. We then derive a macroscopic theory capturing the covariations between these components - so-called collective modes. Our theory shows how cells can achieve robust output against signal fluctuations via self-regulation rather than simple noise suppression. Such robustness corresponds to a transition from random- to structured collective modes beyond a critical adaptation rate.

## 30. Biological Motifs for Agentic Control

- Authors: Bogdan Banu
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-05
- DOI: Unavailable
- Categories: cs.AI, q-bio.CB
- Relevance: 3.02916204109939
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.04240v1
- PDF: https://arxiv.org/pdf/2607.04240v1
- Local PDF: pdf/2026-07-08_30_Biological Motifs for Agentic Control.pdf

The transition of Large Language Models (LLMs) from passive generators to autonomous agents has introduced significant challenges in reliability, security, and state management. Current agentic architectures are often constructed ad-hoc, prone to hallucination cascades, infinite loops, and prompt injection attacks. This paper argues that many of these failure modes can be analyzed using control motifs long studied in systems biology, provided the comparison is made at the level of typed interfaces and coordination structure rather than literal biological mechanism.
  We develop a typed interface correspondence between Gene Regulatory Networks and agentic software systems using polynomial functors and wiring diagrams. Five biological motifs are mapped to composable software design patterns: Coherent Feed-Forward Loops for noise suppression, Adaptive Immunity for layered security, Mitochondrial Signaling for resource governance, Endosymbiosis for neuro-symbolic integration, and Morphogen Diffusion for spatially varying coordination. An epistemic topology layer derives Kripke-style knowledge operators from the wiring diagram's observation structure and proves four predictive theorems for multi-agent scaling.
  The core contributions are: (1) the Agentic Operad, a typed syntax for agent composition with provable error suppression bounds for feed-forward topologies; (2) an epistemic topology with four theorems (error amplification, sequential penalty, parallel acceleration, and tool density scaling) whose qualitative predictions are consistent with published multi-agent benchmarks; and (3) a six-layer progression from structure through development, grounded in autonomous learning frameworks and convergence proxies from the empirical literature. A reference implementation with 1,813 tests and 116 examples illustrates practical feasibility.
