# Paper Daily Reading - 2026-10-22

## 1. VGL-stGen: Learning a shared multimodal model for lung histology and spatial transcriptomics

- Authors: Haenara Shin, Dongjoo Lee, Sungwoo Bae, Kwon Joong Na, Daeseung Lee, Hongyoon Choi
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-20
- DOI: Unavailable
- Categories: cs.CV, cs.AI, q-bio.QM
- Relevance: 3.8574977959399326
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.28266v1
- PDF: https://arxiv.org/pdf/2610.28266v1
- Local PDF: pdf/2026-10-22_01_VGL-stGen_ Learning a shared multimodal model for lung histology and spatial transcriptomics.pdf

VGL-stGen is a multimodal large language model adapted from a pretrained medical vision-language model using paired lung H&E and spatial transcriptomics with single-cell references. Training integrates image-expression and expression-cell-type pairs, and gene-conditioned pseudo-labels transfer transcriptomic cell-type supervision to histology images. One deployed checkpoint supports thirteen evaluated tasks spanning tissue and cell-type classification, gene prediction and conditional expression completion from combinations of histology, cell identity and observed gene expression. Task-specific decoding produces categorical labels, gene lists and structured expression levels. For conditional completion, fixing queried gene identities and predicting their levels autoregressively improves structured prediction. Controlled adaptation shows that restricting supervision to requested expression-level tokens can further improve image-conditioned completion. Image-permutation experiments indicate that correctly paired histology adds information beyond observed expression. External classification relies partly on computational references with shared annotation lineage, and some H&E sources were exposed during cancer training or model development. Within these conditions, VGL-stGen demonstrates how a medical vision-language backbone can learn from spatial transcriptomics and histology to connect tissue morphology and molecular states through shared generative modeling.

## 2. Spatially Informed and Direction Sensitive Representation Learning for Spatial Transcriptomics

- Authors: Azim Dehghani Amirabad, Ali Khodabandeh Yalabadi, Artem Moskalev, Yun-Ching Chen, Mehdi Pirooznia, Scott Oloff, Rui Liao
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-20
- DOI: Unavailable
- Categories: q-bio.QM, cs.AI
- Relevance: 3.8484161419368834
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.28579v1
- PDF: https://arxiv.org/pdf/2610.28579v1
- Local PDF: pdf/2026-10-22_02_Spatially Informed and Direction Sensitive Representation Learning for Spatial Transcriptomics.pdf

Cellular states are shaped by both intrinsic gene expression programs and the spatial microenvironment in which cells reside. Spatial transcriptomics makes this context measurable, but effective representation learning requires capturing both spatially informative molecular signals and intercellular organization. Existing approaches address these challenges only partially: conventional gene selection can overlook spatially structured signals, while methods for encoding cell-cell relationships often either reduce a cell's microenvironment to proximity alone, discarding direction, or rely on absolute coordinates tied to an arbitrary tissue frame. Consequently, cells with similar neighbor distances but distinct spatial organization may receive overly similar representations, despite experiencing different biological contexts that shape their cellular states. We introduce Tessera, a spatial representation learning framework that addresses both molecular selection and cellular context. Tessera combines spatially informed gene selection with a geometric inductive bias that contextualizes each cell within its local tissue environment. By modeling relative cell-cell relationships, Tessera is translation-invariant while preserving direction, allowing neighboring cells to contribute differently according to their spatial context and cellular state. Across held-out tissues and technologies, Tessera outperforms existing spatial foundation models in representation quality and generalizes zero-shot to contexts up to $16\times$ larger than those seen during training.

## 3. Learning Inter-Graph Interactions Between Heterogeneous Substructures of Chemical Systems

- Authors: Gyoung S. Na
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-20
- DOI: Unavailable
- Categories: cs.LG, cs.AI
- Relevance: 3.250695803232919
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.27614v1
- PDF: https://arxiv.org/pdf/2610.27614v1
- Local PDF: pdf/2026-10-22_03_Learning Inter-Graph Interactions Between Heterogeneous Substructures of Chemical Systems.pdf

Complex chemical systems containing heterogeneous substructures are common in real-world applications. Various physical phenomena of the complex chemical systems are derived from the interactions between the heterogeneous substructures. However, existing graph representation learning methods for inter-graph interactions assumed graph-level interactions between homogeneous structures, such as organic molecules and inorganic crystalline materials. We propose a data descriptor of the complex chemical systems and a graph neural network for learning inter-graph interactions between organic and inorganic compounds. We applied the proposed method to predict the physical properties of hybrid solar cell materials containing heterogeneous substructures, which have received significant attention for sustainable energy resources. By learning heterogeneous inter-graph interactions, the proposed method achieved state-of-the-art accuracy in predicting band gaps of 1,682 hybrid solar cell materials.

## 4. Efficient Edge-aware Attention Network for Graph Generation

- Authors: Vincent Jung, Alba Carballo-Castro, Yiming Qin, Lonneke van der Plas, Pascal Frossard
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-20
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.2153201834069245
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.28618v1
- PDF: https://arxiv.org/pdf/2610.28618v1
- Local PDF: pdf/2026-10-22_04_Efficient Edge-aware Attention Network for Graph Generation.pdf

Graph generative models commonly use graph-specific Transformer architectures to jointly update node and edge features. However, these architectures do not directly benefit from recent hardware-aware attention implementations, limiting their scalability. The adaptation is, however, non-trivial: edge and graph-level features must be injected into pairwise attention scores, graph masks must be respected, and dynamic edge updates remain a major source of quadratic memory usage. We propose an edge-aware attention layer for graph generation that incorporates structural information through head-wise score modulation, while updating edge representations with a lightweight residual mechanism that retains attention-score dependent edge updates. This layer can be effectively implemented using PyTorch's FlexAttention. We achieve similar generation quality to our baseline while reducing peak GPU memory by around 65% and substantially improving training and sampling throughput. These results suggest that the proposed architecture is a practical step toward scalable graph foundation models.

## 5. MaD-RSI: Model-as-Data for Recursive Self-Improvement of Agent Harnesses

- Authors: Yu Cui, Hong He, Ruiqing Yue, Sicheng Pan, Zhuoyu Sun, Yifei Liu, Ting Li, Wenzhuo Zhu, Baohan Huang, Haibin Zhang, Cong Zuo
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-20
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 3.197237634671919
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.28201v1
- PDF: https://arxiv.org/pdf/2610.28201v1
- Local PDF: pdf/2026-10-22_05_MaD-RSI_ Model-as-Data for Recursive Self-Improvement of Agent Harnesses.pdf

Recursive self-improvement (RSI) of agent harnesses has emerged as an effective approach to enhancing the capabilities of large language model (LLM) agents. By searching the harness space for a specific LLM on a given dataset, RSI can discover a harness tailored to the capabilities and behavioral characteristics of that model. However, such optimization often creates a strong coupling between the learned harness and its target LLM, limiting generalization across models and requiring substantial computational resources to adapt to new LLMs. Moreover, existing RSI methods typically optimize a harness using feedback from a single model and evaluate its generalization to other models only after training. This paradigm treats model differences primarily as a criterion for evaluating generalization rather than as valuable evidence for optimization. In this paper, we introduce a new perspective that treats models as data and places the harness at the center of optimization. Building on this perspective, we propose \textsc{MaD-RSI}, a framework that directly optimizes a shared harness across multiple heterogeneous LLMs by incorporating their diverse failure trajectories into the training process. Rather than assessing model differences only after optimization, \textsc{MaD-RSI} leverages these differences as training evidence to guide the self-improvement of a shared harness. Furthermore, we introduce a new evaluation framework with two complementary metrics designed to assess the effectiveness of harness optimization across models. Experiments across multiple datasets and LLMs demonstrate that \textsc{MaD-RSI} improves generalization over existing approaches while reducing training costs.

## 6. Brain2Vec: A Self-Supervised 3D Foundation Model for Structural Brain MRI

- Authors: Spiros Maggioros, Guray Erus, Gareth Harman, George Aidinis, Alexander Getka, Aristeidis Sotiras, Christos Davatzikos
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-20
- DOI: Unavailable
- Categories: cs.CV, cs.AI, cs.LG
- Relevance: 3.175195691995313
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.28411v1
- PDF: https://arxiv.org/pdf/2610.28411v1
- Local PDF: pdf/2026-10-22_06_Brain2Vec_ A Self-Supervised 3D Foundation Model for Structural Brain MRI.pdf

Deep learning models have become essential tools in medical imaging, yet training them end-to-end for diverse tasks remains challenging due to limited labeled data and computational constraints. To address this, we introduce Brain2Vec, a foundation model pre-trained on 74,425 T1-weighted Magnetic Resonance Imaging (MRI) scans pooled from multiple studies. Brain2Vec can serve both as a weight initialization backbone for fine-tuning downstream tasks and as a standalone feature extractor. We evaluated Brain2Vec in three tasks: downstream predictive performance, convergence speed, and embedding quality. Using Brain2Vec's pretrained weights as initialization and fine-tuning on labeled data for a brain age prediction task, results demonstrate improved final accuracy and faster convergence compared to random initialization. Additionally, its frozen embeddings outperform anatomically defined volumetric features on four of five downstream classification tasks and perform competitively with a state-of-the-art foundation model pre-trained on substantially more data. Lastly, we show that Brain2Vec encodes information primarily from a spatially localized and neuroanatomically meaningful set of brain regions, and that manipulating a subset of latent features produces monotonic, region-specific effects on the reconstructed anatomy. Brain2Vec code and trained models are available as an open-source package on https://github.com/CBICA/Brain2Vec. Users can apply Brain2Vec locally by installing the package, or directly through the NiChart cloud platform https://cloud.neuroimagingchart.com, where Brain2Vec features can be derived without requiring local installation or specialized infrastructure.

## 7. Causal Discovery for Linear Models with Latent Confounding via Multi-domain Identifiable Representation Learning

- Authors: Danru Xu, Aapo Hyvärinen, Sara Magliacane
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-20
- DOI: Unavailable
- Categories: cs.LG, cs.AI
- Relevance: 3.149520602135479
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.28134v1
- PDF: https://arxiv.org/pdf/2610.28134v1
- Local PDF: pdf/2026-10-22_07_Causal Discovery for Linear Models with Latent Confounding via Multi-domain Identifiable Representation Learning.pdf

Causal discovery with latent confounding is particularly challenging, but a common setting in real-world data. In this work, we focus on linear causal models with latent confounding, represented by acyclic directed mixed graphs (ADMGs). Existing methods that fully identify ADMGs typically assume non-Gaussianity or graphical constraints, such as bow-freeness. In contrast, we propose Linear ADMG Learning (LinADMG), a framework for learning ADMGs for linear causal models through identifiable representation learning. Rather than relying on non-Gaussianity or bow-freeness, LinADMG leverages multi-domain settings to identify the noise variables. We show that the identifiability of the noise variables is sufficient for recovering all direct causal relations, and that, under an additional latent-confounding no-cancellation condition, LinADMG can identify the whole ADMG. We implement LinADMG with four identifiable representation learning approaches from the literature and validate the methods on simulated and semisynthetic datasets.

## 8. Continual Concept Personalization in Diffusion Models via Residual-Space Adaptation

- Authors: Yuzhi Liu, Enis Simsar, Giulia Lanzillotta, Thomas Hofmann
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-20
- DOI: Unavailable
- Categories: cs.CV, cs.LG
- Relevance: 3.135269178172275
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.28567v1
- PDF: https://arxiv.org/pdf/2610.28567v1
- Local PDF: pdf/2026-10-22_08_Continual Concept Personalization in Diffusion Models via Residual-Space Adaptation.pdf

Text-to-image personalization aims to equip pretrained diffusion models with the ability to learn user-specific concepts from only a few reference images. Existing methods, however, typically train each concept independently or assume that all concepts are available simultaneously. In practical applications, concepts often arrive sequentially, requiring models to continually learn new subjects, objects, or styles while minimizing interference with previously acquired concepts. We address this continual concept personalization setting by extending residual-space adaptation to the stochastic adaptation process of pretrained diffusion models. Our work achieves the highest concept fidelity among competing continual personalization methods while maintaining near-zero forgetting. Beyond these empirical gains, the learned residual-space dynamics reveal where adaptation capacity is concentrated within the diffusion model. Restricting adaptation to the identified layers by our method preserves nearly the same performance while reducing the number of trainable parameters by up to 72\%, demonstrating that residual-space dynamics can identify the layers that contribute most to continual concept personalization and directly guide more parameter-efficient adaptation.

## 9. TriGeoBench: A Multimodal Mathematical Geometry Benchmark with Figures and TikZ

- Authors: Jing Wang, Yitong Yang, Hao Dou, Yaomin Wu, Shuting He, Tingfei Shen, Jia Wu, Jiaqi Li, Yinglin Wang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-20
- DOI: Unavailable
- Categories: cs.AI, cs.DB
- Relevance: 3.1235053420059544
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.27626v1
- PDF: https://arxiv.org/pdf/2610.27626v1
- Local PDF: pdf/2026-10-22_09_TriGeoBench_ A Multimodal Mathematical Geometry Benchmark with Figures and TikZ.pdf

Multimodal Large Language Models show strong vision-language capabilities, yet their geometry-centric reasoning remains insufficiently understood. Existing mathematical benchmarks typically rely on rasterized figures and cover limited geometric knowledge areas and response formats, making it difficult to assess whether models reason over geometric structures or exploit superficial visual patterns. We introduce TriGeoBench, a geometry-centric multimodal benchmark constructed from Chinese middle- and high-school mathematics examinations. TriGeoBench contains 7,000 question-answer pairs and 12,235 geometric figures with TikZ code, spanning plane geometry, solid geometry, analytic geometry, function, and vector geometry across diverse response formats. Each instance forms a {question-answer pair, image, TikZ} triplet: question-answer pairs are stored in LaTeX, images as RGB figures, and TikZ preserves geometric topology, symbolic annotations, and relational structure. We evaluate representative open- and closed-source MLLMs through image-to-TikZ and multimodal reasoning probes. Results reveal persistent fine-grained structure and image-text alignment challenges. Oracle experiments with human-curated reference TikZ suggest that accurate executable representations provide complementary geometric cues; they do not evaluate an end-to-end conversion pipeline. TriGeoBench offers a testbed for structure-aware mathematical reasoning.

## 10. ICLHerd: Herding-Based Data Selection for LLMs with In-Context Learning as a Proxy

- Authors: Yuqiao Wen, Lili Mou
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-19
- DOI: Unavailable
- Categories: cs.CL, cs.AI, cs.LG
- Relevance: 3.0981461864996573
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.27142v1
- PDF: https://arxiv.org/pdf/2610.27142v1
- Local PDF: pdf/2026-10-22_10_ICLHerd_ Herding-Based Data Selection for LLMs with In-Context Learning as a Proxy.pdf

Data selection plays a central role in modern large language model training, as the quality of training data strongly influences downstream performance. A common approach is to curate a development set that encodes the desired skills (e.g., reasoning or multilinguality) and select data that are similar to them. Existing methods compute similarity using cosine distance over either the model's hidden states or gradients. However, we observe that this max-similarity strategy induces a mode-seeking bias: the selected data clusters tightly around the development samples. To address this, we propose ICLHerd, a data selection framework that leverages the von Mises-Fisher kernel to balance mode-seeking with mode-averaging. We further introduce in-context learning as a validation proxy, enabling efficient hyperparameter search over the balance trade-off. Results show that ICLHerd outperforms existing LLM data selection algorithms, highlighting the importance of balancing mode-seeking and mode-averaging.

## 11. Beyond the Sequentiality Bottleneck: A Hybrid Diffusion-Autoregressive Framework for Efficient Multimodal Reasoning

- Authors: Wei Cai, Jian Zhao, Yuchen Yuan, Xuelong Li
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-20
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 3.0813838602395656
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.28584v1
- PDF: https://arxiv.org/pdf/2610.28584v1
- Local PDF: pdf/2026-10-22_11_Beyond the Sequentiality Bottleneck_ A Hybrid Diffusion-Autoregressive Framework for Efficient Multimodal Reasoning.pdf

Autoregressive models (ARMs) face a "Sequentiality Bottleneck" in reasoning, while diffusion language models (DLMs) offer parallelism but lack semantic coherence. To addresses both limitations, we propose Collaborative Reasoning Asymmetric Learning (CoRAL), a hybrid framework via an Asymmetric Planner-Executor (APE) architecture: a DLM Planner generates K diverse reasoning trajectories in parallel, while a large ARM Executor selects the optimal plan and synthesizes the final answer. To train the Planner effectively, we introduce Reward-Guided Denoising for CoT (RDC), which integrates outcome-based rewards into the diffusion process to steer it toward goal-directed reasoning. Experiments on vision-language benchmarks show that CoRAL significantly outperforms prior diffusion-based methods and achieves competitive performance against strong ARMs, achieving both superior efficiency and quality.

## 12. Automated Brick Schema Knowledge Graph Completion Across Buildings

- Authors: Daniel Ma, Jalil Huseynov, Xinyi Pan, Shaked Shalev, Zhang Chi, Ai Yamamoto, Sohei Arisaka
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-19
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.0679279901685708
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.27339v1
- PDF: https://arxiv.org/pdf/2610.27339v1
- Local PDF: pdf/2026-10-22_12_Automated Brick Schema Knowledge Graph Completion Across Buildings.pdf

The Brick schema represents building equipment, sensors, spaces, and the relationships between them as typed, multi-relational graphs, providing machine-readable metadata that supports generalizable control applications. Current methods for producing complete Brick models require extensive manual examination of building schematics and point lists. We observe that as Brick models are knowledge graphs, inferring missing relations is naturally posed as a knowledge graph completion problem. To the best of our knowledge, this is the first application of knowledge graph completion to Brick model generation. We compare three methods, gradient-boosted trees, Pairwise Brick Relation Ranking, and CompGCN, on the relations feeds, hasPart, and hasPoint, which account for the majority of the schematic-reading work in building a Brick model by hand. Models are evaluated on held-out MORTAR buildings and out-of-distribution Kaggle and Building Time Series data. Although CompGCN is the strongest performer on held-out buildings under metrics resistant to class imbalance, leading macro-F1 and AUPRC, no method generalizes uniformly across datasets or relations.

## 13. Dancing Diffusion: Learning Continuous Programs for Image Generation and Editing

- Authors: Cui Enhe, Jinyue Yang, Bojian Yin, Guoqi Li
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-20
- DOI: Unavailable
- Categories: cs.AI, cs.GR
- Relevance: 3.061846379387654
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.28003v1
- PDF: https://arxiv.org/pdf/2610.28003v1
- Local PDF: pdf/2026-10-22_13_Dancing Diffusion_ Learning Continuous Programs for Image Generation and Editing.pdf

Diffusion models generate samples through a multi-step denoising trajectory, yet condition every step on the same instruction, so the trajectory cannot be addressed at the level of individual operations. We introduce Dancing Diffusion, which assigns each span of timesteps a dedicated continuous condition block and thereby turns conditioning into a latent program. A compiler maps text features into this program, and a fixed pretrained generator executes its blocks over successive sampling intervals. The trajectory can then dance, keeping its executed history while its continuation is redirected. A shared prefix is executed once and reused, and a later operation is rewritten while content fixed by earlier operations is preserved. The compiler is trained through the images it produces, with visual feedback on both the requested change and the retained content. On SANA, reusing an executed prefix preserves markedly more of the scene than regenerating from noise at a similar strength of edit, learned conditions preserve more background than native prompt switching from the same saved state, and the learned program improves generation quality over native SANA. Later branches weaken the edit, which leaves semantic control over individual operations limited. By converting a single-instruction trajectory into a program of addressable operations, Dancing Diffusion lays a foundation for structured intermediate computation in diffusion models.

## 14. Detection of Memorization in Diffusion Models Through Thermodynamic Singularity

- Authors: Iljung Kim, Kangwoo Park, Yung-Kyun Noh, Daniel D. Lee
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-20
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.027649422620196
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.27754v1
- PDF: https://arxiv.org/pdf/2610.27754v1
- Local PDF: pdf/2026-10-22_14_Detection of Memorization in Diffusion Models Through Thermodynamic Singularity.pdf

In diffusion models, proper distributional learning entails reversing a diffusion process over underlying density functions, whereas a key failure is memorization, in which the reverse process instead learns diffusion from individual training samples. We provide an analytical characterization of such memorized reverse processes, along with a criterion that detects the associated thermodynamic singularity. The proposed criterion reliably distinguishes between properly learned and memorizing networks across a range of neural network models designed to promote or mitigate memorization.

## 15. VampPrior Unleashed

- Authors: Andrew A. Stirn, Abhejit Rajagopal, David A. Knowles, Grace Huynh
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-19
- DOI: Unavailable
- Categories: cs.LG, stat.ML
- Relevance: 3.0216026061339845
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.27322v1
- PDF: https://arxiv.org/pdf/2610.27322v1
- Local PDF: pdf/2026-10-22_15_VampPrior Unleashed.pdf

Deep latent variable models (DLVMs) underpin many modern analysis pipelines, for example in single-cell genomics, yet their prior distributions have received markedly little attention. The VampPrior approximates the optimal prior (the aggregate posterior) and often attains high model evidence. Here, we identify two key limitations of the VampPrior: it ties prior and posterior uncertainty to a single amortized covariance and clusters poorly due to its fixed uniform mixture weights. We unleash the VampPrior by decoupling its prior and posterior covariances, resolving the conflict of generating high prior and low posterior entropy with the same shared parameters and substantially improving model evidence. We then replace the uniform mixture with a Dirichlet process. When combined, our proposals provide higher model evidence than the VampPrior and robust non-parametric clustering. Augmenting single cell Variational Inference (scVI) with our prior improves single-cell integration and clustering across six atlases while significantly raising model evidence. Our approach changes only the prior and thus can be applied to any DLVM with a continuous latent space.

## 16. Semantic Observability for Autonomous Systems Diagnostics

- Authors: Jitendra Solanki, Anand Todkar, Ziran Min
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-20
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 2.9831713483661093
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.28611v1
- PDF: https://arxiv.org/pdf/2610.28611v1
- Local PDF: pdf/2026-10-22_16_Semantic Observability for Autonomous Systems Diagnostics.pdf

Modern distributed microservice deployments generate massive volumes of heterogeneous, multi-format observability logs across physically and logically partitioned infrastructure. Isolating root causes during cascading failures remains an arduous task for Site Reliability Engineers (SREs), bottlenecked by manual keyword filtering and disjointed temporal correlation across monitoring dashboards. We introduce Semantic Observability, an autonomous multi-agent framework that unifies disparate log streams into a dynamic, queryable Property Graph Database. By modeling physical infrastructure topologies, logical software dependencies, and chronological event sequences as attributed nodes and directed relations, it bridges the semantic gap inherent in flat, unstructured log repositories. Building on this unified substrate, we deploy a stateful multi-agent system orchestrated through Directed Cyclic Graphs (DCGs). The system autonomously navigates the topology, applying causal graph algorithms and temporal back-traversal to isolate the precise blast radius of anomalies. The pruned subgraph is then interpreted by a Large Language Model (LLM) reasoning engine to generate contextualized, code-level Root Cause Analyses (RCA) and actionable remediations. This paper establishes the foundational system architecture, formal relational ontology, and multi-agent control loops of Semantic Observability. We show conceptually how the framework eliminates ambient telemetry noise, reduces Mean Time to Resolution (MTTR), compresses LLM token consumption, and prevents structural hallucinations. We also specify an open-source validation framework on standard benchmarks (LogHub and Train-Ticket), laying the groundwork for a forthcoming companion paper on exhaustive quantitative evaluation and production benchmarking.

## 17. Stratified Sparse Attention: Reducing the Sparse-to-Dense Gap at Extreme Sparsity

- Authors: Sahil Joshi, Prithvi Dixit, Aryan Katiyar, Agniva Chowdhury, Joseph E. Gonzalez, Anshumali Shrivastava, Aditya Desai, Kumar Krishna Agrawal
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-20
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 2.9831241892659315
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.28441v1
- PDF: https://arxiv.org/pdf/2610.28441v1
- Local PDF: pdf/2026-10-22_17_Stratified Sparse Attention_ Reducing the Sparse-to-Dense Gap at Extreme Sparsity.pdf

Large Language Model inference over long contexts is increasingly bottlenecked by the cost of attending to a growing Key-Value (KV) cache. Sparse attention reduces this cost by accessing only a fraction of the cache, but existing methods face a trade-off between deterministic retrieval, which captures high-scoring tokens but discards residual attention mass, and sampling, which improves coverage at the cost of higher variance. Hybrid methods combine top-$k$ retrieval with uniform sampling, yet still exhibit a substantial gap from dense attention at aggressive sparsity. We introduce \emph{Stratified Sparse Attention (SSA)}, a unified framework combining deterministic retrieval with score-guided sampling. SSA deterministically attends to high-scoring tokens while sampling the residual using proxy attention scores and correcting for their inclusion probabilities, thereby recovering attention mass beyond the retrieval set. SSA encompasses top-$k$, top-$p$, and hybrid top-$k$+sampling as special cases. Across RULER, LongBench, LOFT, and AIME, and five models ranging from 3B to 27B parameters, SSA consistently improves over the baselines at matched sparsity. On RULER-HARD with Ministral-3-8B, SSA improves accuracy over the strongest practical baseline from 81.8\% to 84.2\% at 32K and from 63.8\% to 69.3\% at 128K under $50\times$ attention sparsity, recovering 94\% and 85\% of dense-attention performance, respectively. With optimized CUDA kernels, SSA achieves up to $2.96\times$ decode speedup over FlashInfer at 1M context, demonstrating that its accuracy gains translate into practical long-context inference acceleration. We open-source our code at https://github.com/skylight-org/SSA-Paper-Code.

## 18. Binary Discrete Diffusion: Candidate-Set Diffusion for Logic and Planning Tasks

- Authors: Rodrigo Casado Noguerales, Dimitri von Rütte, Bernhard Schölkopf, Thomas Hofmann, Aran Raoufi
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-20
- DOI: Unavailable
- Categories: cs.LG, cs.AI, cs.CL, stat.ML
- Relevance: 2.9710745744816593
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.28543v1
- PDF: https://arxiv.org/pdf/2610.28543v1
- Local PDF: pdf/2026-10-22_18_Binary Discrete Diffusion_ Candidate-Set Diffusion for Logic and Planning Tasks.pdf

Discrete diffusion models iteratively denoise a noisy sequence of categorical data such as text, enabling any-order generation with self-correction and in-filling capabilities. This makes them promising candidates for reasoning, planning, and constrained-generation tasks like coding and math. Yet masked and uniform diffusion erase a token's identity in a single corruption event, so their noisy states cannot explicitly represent partially resolved uncertainty in which several alternatives remain plausible. We close this gap with Binary Discrete Diffusion, a family of continuous-time discrete-diffusion processes whose noisy state is a set of candidate tokens per position, represented as a binary membership vector. Binary diffusion changes candidate sets through additions and removals, allowing information to be lost and recovered gradually while the diffusion state itself represents partial uncertainty. On Sudoku-Extreme, Boxoban, and graph coloring, the symmetric formulation of binary diffusion consistently outperforms strong, well-tuned masked and uniform baselines under matched architectures and controlled training, sampling, and tuning budgets, with its largest gains on the hardest instances, while remaining competitive on language modeling (Text8, TinyStories, OpenWebText). These results support candidate sets as an effective intermediate representation for iterative reasoning and show that the corruption kernel can materially change the computation learned by the reverse model.

## 19. MoDDiT: Simple Token Routing in Diffusion Transformers

- Authors: Jarek Liesen, Matthew T. Jackson, Benjamin Ellis, Shimon Whiteson, Jakob N. Foerster
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-20
- DOI: Unavailable
- Categories: cs.CV, cs.AI
- Relevance: 2.954819578740935
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.28086v1
- PDF: https://arxiv.org/pdf/2610.28086v1
- Local PDF: pdf/2026-10-22_19_MoDDiT_ Simple Token Routing in Diffusion Transformers.pdf

Real-time video generation, interactive world models, and on-device image synthesis are almost a reality. Diffusion Transformers (DiT) achieve excellent sample quality, shifting the bottleneck to the throughput of the models themselves. Natural images are inherently sparse, as large portions of an image are often background, contribute little to the scene content, and are easy to denoise. DiTs fail to exploit this sparsity, as they process image tokens statically and uniformly. We propose MoDDiT, a simple architecture modification that learns to route tokens through both MLP and self-attention operations. By routing tokens through both blocks independently, MoDDiT allows for dynamic compute allocation in MLPs that varies across tokens, images, and denoising timesteps. Using MoDDiT to train image generation models from scratch significantly reduces computational costs of training and inference, processing as few as 12.5% of the tokens. By increasing sparsity and model depth, MoDDiT reduces costs and improves generation performance over unrouted baselines. The learned allocation is interpretable, revealing how computation varies with visual content and noise level. We also use MoDDiT to train video generation models, where allocation correlates with motion, and to distill a dense bidirectional video model into a sparse autoregressive student.

## 20. Sparse RL Relaxation for LLM Reasoning

- Authors: Jiabin Fan, Matthias Lindemann, Zita Marinho, André FT Martins, Lili Mou
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-19
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 2.935596737348656
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.27220v1
- PDF: https://arxiv.org/pdf/2610.27220v1
- Local PDF: pdf/2026-10-22_20_Sparse RL Relaxation for LLM Reasoning.pdf

Recent work has explored continuous representations in place of discrete tokens during Chain-of-Thought (CoT) reasoning, often referred to as soft CoT. This is motivated by the idea that a mixture of token embeddings can represent a superposition of multiple reasoning possibilities within a single step. However, it remains challenging to train large language models to realize this potential. Existing work has explored reinforcement learning (RL)-style training for soft CoT. However, these approaches treat soft tokens as actions in a Markov decision process rather than as differentiable intermediate computation steps. Thus, they do not propagate gradients across the soft tokens and miss out on the signal of how the choice of one soft token affects the next. In this paper, we propose a sparse relaxation method for RL (called SpaRLax), which leverages the differentiability of soft-CoT reasoning over time steps and makes training more stable and effective. We adopt an entmax sparsity method that adaptively determines the degree of softness, which truncates long-tail noise at confident steps while retaining multiple plausible candidates when uncertain. Across nine reasoning benchmarks, our method achieves the highest average performance compared with baseline methods. Further analyses validate the effective use of soft-token superposition in our approach, and also demonstrate the contribution of adaptive sparsity in our approach.

## 21. Convergent Performance, Divergent Mechanisms in LoRA-Adapted Vision Foundation Models for Brain MRI

- Authors: Cecilia Diana-Albelda, Fiona Kekwick, Raghav Mehta, Aleksandra Kulbaka, Paul M. Matthews, Jesus Bescos, Álvaro García-Martín, Wenjia Bai, Bernhard Kainz
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-20
- DOI: Unavailable
- Categories: cs.CV, cs.LG
- Relevance: 2.931524678315368
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.28255v1
- PDF: https://arxiv.org/pdf/2610.28255v1
- Local PDF: pdf/2026-10-22_21_Convergent Performance, Divergent Mechanisms in LoRA-Adapted Vision Foundation Models for Brain MRI.pdf

Adapting Vision Foundation Models (VFMs) to medical imaging via LoRA has become standard practice, yet model selection is guided almost entirely by downstream task metrics, treating backbones with similar performance as interchangeable. We investigate whether equal performance implies equal internal representational shift. We analyse four ViT-B/16 backbones, DINOv3, SigLIP2, MerMED-FM, and BiomedCLIP, pre-trained with different objectives (self-distillation vs. contrastive vision-language) and on different data domains (natural vs. medical images). We adapt each to brain tumour segmentation and evaluate on six datasets covering both segmentation and Alzheimer's disease classification. Using attention divergence, weight-change analysis, and activation patching, we find that the four models converge to similar segmentation performance (mean Dice 78-81%) through markedly different internal dynamics, yet diverge in cross-task transfer: segmentation adaptation improves Alzheimer's disease classification for DINOv3 but degrades it for the other three backbones. We reveal a dissociation between modification magnitude and causal importance: the most heavily modified layers are not the causally relevant ones, with early-to-mid layers identified as sufficient for segmentation recovery. Restricting LoRA to these layers matches or approaches full-layer segmentation while reducing classification degradation in the three affected backbones, providing a mechanistically grounded strategy that is more parameter-efficient and more robust than standard full-layer adaptation.

## 22. RAG-NIMBF: A Non-Invasive, Modular Benchmarking Framework for Automated RAG Configuration Analysis

- Authors: Niclas Hart, Nicolas Weeger
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-20
- DOI: Unavailable
- Categories: cs.SE, cs.AI
- Relevance: 2.8841502674023385
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.27816v1
- PDF: https://arxiv.org/pdf/2610.27816v1
- Local PDF: pdf/2026-10-22_22_RAG-NIMBF_ A Non-Invasive, Modular Benchmarking Framework for Automated RAG Configuration Analysis.pdf

Retrieval-Augmented Generation (RAG) has become the dominant paradigm for grounding the outputs of large language models (LLM) in external knowledge. However, practitioners are faced with a vast configuration space comprising chunking, embedding, retrieval, reranking, prompting and generation models, and there is limited guidance on how these components interact. We present RAG-NIMBF, a modular benchmarking framework that attaches to existing RAG pipelines as a non-invasive evaluation layer. It evaluates the configuration space through controlled ablation with end-to-end experiment tracking. The evaluation combines LLM-based answer quality scores, retrieval correctness measures, and runtime indicators. This study validates the framework across multiple generation models on the SQuAD dataset. This process reveals non-obvious interactions and demonstrates how the experiments are tracked. The findings indicate that the retrieval balance of relevance and diversity substantially enhances the relevance and coverage of retrieved context in comparison to a conventional similarity search, with MMR raising nDCG@5 by +4 to +11 percentage points across the swept models. More detailed prompt instructions meaningfully increase how faithfully generated answers stick to the retrieved evidence, especially for capable and reasoning models (+10 to +13pp on Qwen3.6-27B, GPT-4o-mini and Qwen3.5-think, but negligible on the 20B generator). Overall, RAG-NIMBF transforms the configuration space of RAG into reproducible, comparable experiments. By attaching to existing production pipelines in a non-invasive way, it enables practitioners to systematically evaluate and improve deployed systems without disrupting existing workflows. This replaces ad hoc choices with evidence-based decisions.

## 23. ChartEvo: Self-Evolving Agent Harnesses for Long-Tail Chart Reasoning

- Authors: Qi Wang, Peijie Wang, Jun Cao, Haoyang Tong, Xiao-Hui Li, Fei Yin, Cheng-Lin Liu
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-20
- DOI: Unavailable
- Categories: cs.AI, cs.CV
- Relevance: 2.8823853451947694
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.28282v1
- PDF: https://arxiv.org/pdf/2610.28282v1
- Local PDF: pdf/2026-10-22_23_ChartEvo_ Self-Evolving Agent Harnesses for Long-Tail Chart Reasoning.pdf

Multimodal large language models (MLLMs) have substantially advanced chart understanding and reasoning, yet their performance remains highly uneven across chart types. While modern MLLMs perform well on common charts, their accuracy drops sharply on long-tail charts with diverse visual structures and reasoning requirements. Tool-augmented agents can improve complex chart reasoning by introducing specialized visual capabilities, but manually engineering strategies and tools for the heterogeneous and evolving long tail is difficult to scale. We introduce \textbf{ChartEvo}, a recursive self-improvement framework that enables chart agents to adapt to underperforming chart types through experience-driven harness-level self-improvement. ChartEvo jointly evolves reusable chart-specific Skills and executable Tools, while learning reusable local tool-call chains to compose evolved capabilities and control the inference overhead of tool-augmented reasoning. On long-tail charts from ChartBench and ChartX, ChartEvo improves accuracy over its base MLLM, Qwen3.7-Plus, by \textbf{45.6\%} and \textbf{32.5\%}, respectively, demonstrating the effectiveness of recursive self-improvement for long-tail chart adaptation.

## 24. Dynamic System Inspired Continuous Large Language Model for AI4Science Tasks

- Authors: Zhaoxin Fan, Zheng Zhu, Yuqing Ma, Faguo Wu, Jian Yang, Wenjun Wu
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-18
- DOI: Unavailable
- Categories: cs.LG, cs.CL
- Relevance: 2.8567255033239154
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.26959v1
- PDF: https://arxiv.org/pdf/2610.26959v1
- Local PDF: pdf/2026-10-22_24_Dynamic System Inspired Continuous Large Language Model for AI4Science Tasks.pdf

Scientific foundation models increasingly operate on continuous phenomena, yet still use discrete residual computation. We ask whether pretrained residual transformations can support additional latent computation without expanding the backbone. To test this possibility, we introduce Continuum-LM, which reuses these transformations as dynamical operators in a continuous-depth language model. Its hidden states evolve through an ordinary differential equation evaluated by higher-order numerical integration, with solver order and step size controlling computation. Across eight scientific tasks, Continuum-LM trains stably and improves mean exact-match accuracy by 7.77 and 10.96 percentage points over discrete counterparts at the 0.6B and 1.7B scales, respectively. At 0.6B, it also outperforms an Ouro-style recurrent control under matched parameter and residual-function evaluation budgets. Together, these results support extensible computational depth through parameter reuse, identifying continuous hidden-state evolution as a practical design dimension for scientific language models beyond parameter scaling.

## 25. Manifold-Informed Neural Networks for Low-Label ECG Electrolyte Inference

- Authors: Juntang Wang, Hao Wu, Yihan Wang, Dongmian Zou, Shixin Xu
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-20
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 2.8439213319081547
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.28322v1
- PDF: https://arxiv.org/pdf/2610.28322v1
- Local PDF: pdf/2026-10-22_25_Manifold-Informed Neural Networks for Low-Label ECG Electrolyte Inference.pdf

Physics-informed neural networks (PINNs) supervise on the residual of a known differential operator. Many high-stakes inference problems admit no such operator: clinical signals, behavioral measurements, materials properties. We introduce the Manifold-Informed Neural Network (MINN), a PINN-parallel paradigm that replaces the physics operator residual with a manifold operator residual: a discrete Poisson equation $\mathbf{L}_G \mathbf{H} = s_φ(\mathbf{x}, \mathbf{m})$ on a $k$-nearest-neighbor graph in the learned latent space, with a learned, task-aware source. The construction is a structural parallel to PINNs (squared operator residual plus label data, in place of operator residual plus boundary data); the $s{=}0$ limit recovers the homogeneous Laplace equation $\mathbf{L}_G\mathbf{H}=\mathbf{0}$ (classical manifold regularization solves the same equation but minimizes the Dirichlet energy $\operatorname{tr}(\mathbf{H}^\top\mathbf{L}_G\mathbf{H})$, a different penalty form). The source $s_φ$ takes input features and auxiliary metadata directly, breaking the homogeneous smoothness prior that limits classical Laplacian penalties; gated Feature-wise Linear Modulation separately fuses metadata into the prediction branch. We evaluate MINN on three-class classification of potassium, calcium, and magnesium from 12-lead ECGs in MIMIC-IV-ECG, against twelve baselines spanning supervised and tabular methods, ECG foundation models, and manifold/graph approaches. MINN attains the highest K$^+$ Macro-F1 of 0.61 (best baseline 0.55), with consistent gains on Ca$^{2+}$ and Mg$^{2+}$ and a 31% relative improvement at 1% labeled data. Six targeted ablations show that the inhomogeneous Poisson formulation, not graph smoothing alone, drives the gain.

## 26. Shaped SAEs: Expanding the Toolkit for Mechanistic Interpretability

- Authors: Oveys Delafrooz Noroozi, Bhagyashree Puranik, Upamanyu Madhow
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-19
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 2.8434352867514074
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.27375v1
- PDF: https://arxiv.org/pdf/2610.27375v1
- Local PDF: pdf/2026-10-22_26_Shaped SAEs_ Expanding the Toolkit for Mechanistic Interpretability.pdf

Sparse autoencoders (SAEs) seek to decompose the dense activations of large language models (LLMs) into sparse, potentially interpretable features using a learned overcomplete dictionary. In this work, we ask whether it is possible to enhance the semantic selectivity of the learned dictionary atoms by linearly \emph{shaping} the dense activations prior to learning an SAE. We explore rank-reducing transformations based on the recently introduced J-space corresponding to the averaged Jacobian from the current layer to the LLM output, projecting activations onto the ``live'' subspace spanned by eigenmodes of the Jacobian with larger singular values (which we expect to be more semantically relevant). We also introduce a new approach for training SAEs in which (a)~an affine shaping transformation is learned along with the dictionary atoms, (b)~the atom selection mechanism is based on the TopK projections along the one-dimensional subspace spanned by the atoms, and (c)~reconstruction is carried out using the same atoms. We call this approach a Matched Filter SAE (MF-SAE) based on analogies with communication theory. The promise of shaping is demonstrated via evaluations against dense activations and state-of-the-art SAEs on benchmarks including SAEBench and SAE Probes.

## 27. DStill: Trajectory Consistency Distillation for Accelerated One-Step Drafting in Block Diffusion Speculative Decoding

- Authors: Shreyas Kulkarni, Uttam Gurram, Madhav Kanda, Krishna Teja Chitty Venkata, Shichu Chen, Kartik Balasubramaniam, Supriyo Chakraborty, Sambit Sahu
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-19
- DOI: Unavailable
- Categories: cs.CL, cs.LG
- Relevance: 2.832530241663687
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.27379v1
- PDF: https://arxiv.org/pdf/2610.27379v1
- Local PDF: pdf/2026-10-22_27_DStill_ Trajectory Consistency Distillation for Accelerated One-Step Drafting in Block Diffusion Speculative Decoding.pdf

Block-diffusion speculative decoding accelerates large language model inference by drafting multiple tokens in parallel. However, one-step drafting in discrete diffusion is limited by token factorization error: each token is predicted from the same masked block, without conditioning on the tokens selected at other positions in that step. This can produce inconsistent drafts and reduce acceptance length. Iterative refinement mitigates this limitation by conditioning later predictions on previously committed tokens, though additional passes increase drafting cost. To address this trade-off between draft fidelity and inference latency, we introduce DStill, a two-stage framework that distills a target-conditioned drafter's own multi-step refinement into one-step drafting. We first train the drafter to complete partially revealed blocks, then use its refinement trajectories to train a student to predict the final completion in one pass. Using a curriculum that gradually transitions from partial to fully masked inputs, we successfully transfer the multi-step refinement capabilities into one step. Across reasoning, math, code benchmarks on three model families DStill improves acceptance length by up to 28% and speedup by up to 25% over one-step DFlash, achieving up to 6.45x speedup over auto-regressive decoding.

## 28. LoRASpace: A Pool-Wide Shared Substrate for Static and Dynamic Multi-LoRA Composition

- Authors: Thamirawaran Sathiyalogeswaran, Navindu De Silva, Chamikara Siriwardane, W. K. Alwis, Jason Mars, Udaya Sampath K. Perera Miriya Thanthrige, Ranga Rodrigo
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-20
- DOI: Unavailable
- Categories: cs.CV, cs.LG
- Relevance: 2.8288029239640045
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.27444v1
- PDF: https://arxiv.org/pdf/2610.27444v1
- Local PDF: pdf/2026-10-22_28_LoRASpace_ A Pool-Wide Shared Substrate for Static and Dynamic Multi-LoRA Composition.pdf

Low-rank adaptation (LoRA) attaches small low-rank matrices to a frozen backbone, and public repositories host many LoRAs per backbone, each for a different concept or task. Combining several LoRAs in one generation forces a trade-off. Merging their weights into one update needs a single forward pass, but LoRAs trained for different concepts interfere and quality drops. Running each LoRA in its own forward pass (composite) preserves quality, but inference time grows linearly with the number of active LoRAs. We study a property of LoRA pools overlooked by prior multi-LoRA work. In real LoRA pools, the stacked low-rank factors need far fewer directions than their summed ranks. Using singular value decomposition, we find the minimal subspace that keeps 99% of the factor energy. On three diffusion pools, only 46% to 57% of the summed LoRA ranks is needed, and the subspace grows sub-linearly with pool size. A 48-LoRA sub-pool of LoRA-Hub on FLAN-T5 tasks shows comparable overlap (62%), while the diversity-curated LoRA-Retriever benchmark sits near the no-overlap baseline (96%), so pool composition rather than modality predicts where compression is large. We build on this overlap with LoRASpace, a training-free method that computes the subspace once per pool and reuses it in two inference modes, a static mode at merge cost and a dynamic mode for input-dependent routing. On the diffusion pools, static LoRASpace matches composite quality at merge cost, and dynamic LoRASpace is more than 6x faster than composite with six active LoRAs on a 17-LoRA pool, mainly because it runs one backbone pass instead of six. In an ablation, static variants at the same rank match LoRASpace, so the quality gain does not depend on the pool-wide basis. On the near-orthogonal LoRA-Retriever benchmark, compression is small and gains come from coupling with external retrieval.

## 29. SliMOO: Interpretable Multi-Objective Evolutionary Search for LLM Depth Pruning

- Authors: Guanchen Li, Yixing Xu, Xuanwu Yin, Dong Li, Emad Barsoum
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-20
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 2.8277839970977245
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.27812v1
- PDF: https://arxiv.org/pdf/2610.27812v1
- Local PDF: pdf/2026-10-22_29_SliMOO_ Interpretable Multi-Objective Evolutionary Search for LLM Depth Pruning.pdf

As large language models (LLMs) grow more powerful, their scale makes them costly to serve. Depth pruning offers a practical route to efficiency by directly reducing memory and latency without hardware-specific support. However, we observe that transformer layers exhibit markedly different task-dependent layer contributions, whereas existing depth-pruning methods ignore this heterogeneity and thus tend to optimize for a narrow domain or benchmark rather than preserve broad capability. This suggests that LLM depth pruning should be formulated as a multi-objective optimization problem rather than a single-score ranking problem.
  We propose SliMOO, an interpretable multi-objective evolutionary search framework for LLM depth pruning. SliMOO first uses single-layer removal probing to construct a task-layer importance map, which provides an interpretable view of task-shared and task-specific layers and serves as a search prior. It then performs a Pareto-aware evolutionary search for pruning masks, where candidates are generated under the guidance of the task-layer prior, scored by their deviation from the dense model on each task, and retained through NSGA-II environmental selection. Across the Llama-3.1 and Qwen3 model families, SliMOO consistently achieves stronger multi-task trade-offs than rule-based, greedy, and scalarized baselines. For example, on Llama-3.1-70B at 25% sparsity, it improves the math-domain average from 24.33% to 34.40% and the code-domain average from 35.03% to 39.14%. Code will be made available at https://github.com/AMD-AGI/SliMOO.

## 30. Africa-Papers: A 10-Billion-Token Multi-Domain Academic Corpus for African Foundation Language Models

- Authors: Mich-Seth Owusu
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-20
- DOI: Unavailable
- Categories: cs.CL, cs.AI
- Relevance: 2.8255599918909047
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.28173v1
- PDF: https://arxiv.org/pdf/2610.28173v1
- Local PDF: pdf/2026-10-22_30_Africa-Papers_ A 10-Billion-Token Multi-Domain Academic Corpus for African Foundation Language Models.pdf

Large Language Models (LLMs) depend fundamentally on the diversity, depth, and factual rigor of their pre-training corpora. However, contemporary foundational pre-training datasets (such as The Pile, S2ORC, and Dolma) exhibit a severe structural omission: African scientific, medical, legal, and agricultural scholarship constitutes less than 0.5% of global pre-training tokens. Consequently, state-of-the-art models suffer from systematic failure modes when reasoning about tropical epidemiology, localized smallholder agro-ecologies, regional economic governance, and indigenous linguistic structures. To resolve this representation deficit and advance African intellectual sovereignty in artificial intelligence, we introduce Africa-Papers, the largest curated multi-domain Pan-African academic pre-training corpus to date. Comprising over 844,807 full-text papers spanning 10.15 billion tokens across 879 Parquet shards, Africa-Papers unifies four primary scientific streams: (1) continental peer-reviewed journals indexed in DOAJ across 31 African nations, (2) the CGIAR CGSpace agricultural repository, (3) African-authored and African-focused STEM/AI preprints on arXiv, and (4) open-access international publications by scholars affiliated with African institutions indexed via OpenAlex. The entire corpus is processed into layout-aware, clean Markdown preserving section hierarchies, mathematical equations, and tabular data, accompanied by exact BPE token counts and a standardized 8-domain taxonomy. We release Africa-Papers openly on the Hugging Face Hub under the AfriSpeech organization to accelerate continual pre-training and domain evaluation for foundation models globally.
