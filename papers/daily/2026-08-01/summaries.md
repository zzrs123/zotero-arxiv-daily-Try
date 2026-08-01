# Paper Daily Reading - 2026-08-01

## 1. TopoFormer: Topology Meets Attention for Graph Learning

- Authors: Md Joshem Uddin, Astrit Tola, Cuneyt Gurcan Akcora, Baris Coskunuzer
- Source: arxiv
- Venue type: preprint
- Journal: ICLR 2026
- Publication status: preprint
- Publication date: 2026-07-30
- DOI: Unavailable
- Categories: cs.LG, math.AT
- Relevance: 4.096407831348497
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.28259v1
- PDF: https://arxiv.org/pdf/2607.28259v1
- Local PDF: pdf/2026-08-01_01_TopoFormer_ Topology Meets Attention for Graph Learning.pdf

We introduce Topoformer, a lightweight and scalable framework for graph representation learning that encodes topological structure into attention-friendly sequences. At the core of our method is Topo-Scan, a novel module that decomposes a graph into a short, ordered sequence of topological tokens by slicing over node or edge filtrations. These sequences capture multi-scale structural patterns, from local motifs to global organization, and are processed by a Transformer to produce expressive graph-level embeddings. Unlike traditional persistent homology pipelines, Topo-Scan is parallelizable, avoids costly diagram computations, and integrates seamlessly with standard deep learning architectures. We provide theoretical guarantees on the stability of our topological encodings and demonstrate state-of-the-art performance across graph classification and molecular property prediction benchmarks. Our results show that Topoformer matches or exceeds strong GNN and topology-based baselines while offering predictable and efficient compute. This work opens a new path for parallelizable and unifying approaches to graph representation learning that integrate topological inductive biases into attention frameworks.

## 2. What Makes Graph Unified? Principles and Generative Sliding-Window Transformer for Graph Foundation Models

- Authors: Dongxiao He, Siqi Liu, Jitao Zhao, Yawen Li, Yi Wang, Di Jin
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-30
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.834913062311262
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.27966v1
- PDF: https://arxiv.org/pdf/2607.27966v1
- Local PDF: pdf/2026-08-01_02_What Makes Graph Unified_ Principles and Generative Sliding-Window Transformer for Graph Foundation Models.pdf

Graph Foundation Models (GFMs) have recently emerged as a promising paradigm for general-purpose graph learning, aiming to learn reusable knowledge that generalizes across diverse graph domains and downstream tasks, reducing the need for specific model development. Achieving this goal requires reconciling the substantial heterogeneity in node features, graph structures, and semantic information across domains. Among them, heterogeneous node features constitute a fundamental input-level barrier, as their dimensionality and semantics vary substantially across datasets. Existing studies typically project or map heterogeneous node features into a fixed-dimensional space, often implicitly equating dimensional uniformity with effective feature unification. Yet dimensional consistency alone does not ensure that the unified features preserve informative semantics and capture transferable patterns that can support cross-domain knowledge transfer. To bridge this conceptual gap, we distill four desiderata for cross-domain graph feature unification: formal uniformity, cross-domain transferability, information preservation, and backbone compatibility. Guided by these principles, we propose SliGFM, a graph foundation model built upon topology-aware sliding-window feature encoding and generative reconstruction. SliGFM orders feature dimensions by topological smoothness and scans the reordered features with a shared sliding-window feature encoder, transforming heterogeneous features into a common space of ordered fixed-dimensional feature tokens. This formulation enables a smoothness-aware transformer to capture transferable relational patterns among feature tokens within each node, while the generative reconstruction objective encourages preservation of the original feature information.

## 3. MUL-T: Decoding Spatial Cellular Architecture in Multiplexed Tissue Images

- Authors: Farzaneh Seyedshahi, Kai Rakovic, Adalberto Claudio Quiros, John LeQuesne, Ke Yuan
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-30
- DOI: Unavailable
- Categories: cs.AI, cs.CV
- Relevance: 3.7283780832925597
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.28030v1
- PDF: https://arxiv.org/pdf/2607.28030v1
- Local PDF: pdf/2026-08-01_03_MUL-T_ Decoding Spatial Cellular Architecture in Multiplexed Tissue Images.pdf

Understanding tissue organisation in multiplexed imaging requires modelling both cellular phenotypes and their spatial context. Existing approaches typically rely on handcrafted features, such as marker intensity statistics or cell-type proportions, which often fail to scale or generalise across cohorts with heterogeneous marker panels. We introduce MUL-T, a lightweight transformer framework that reframes tissue architecture as a masked contextual prediction task over discrete cell tokens. By learning contextualised [CLS] embeddings without task-specific supervision, the model captures higher-order cellular interactions while remaining computationally efficient. We evaluate MUL-T on several clinically relevant downstream tasks, including core-level tumour pattern classification, patient-level grading, PD-L1 positivity prediction, and cross-dataset treatment response prediction. Across tasks, MUL-T consistently outperforms classical feature-based baselines and achieves performance comparable to a foundation ViT model, despite substantially fewer parameters and lower training cost.

## 4. GLM-RAG: Graph Language Models for Graph-Based Retrieval-Augmented Generation

- Authors: Maya Arseven, Anette Frank, Beni Egressy, Johann Higl, Moritz Plenz
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-30
- DOI: Unavailable
- Categories: cs.AI, cs.CL, cs.IR
- Relevance: 3.6516715148225583
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.28397v1
- PDF: https://arxiv.org/pdf/2607.28397v1
- Local PDF: pdf/2026-08-01_04_GLM-RAG_ Graph Language Models for Graph-Based Retrieval-Augmented Generation.pdf

Retrieval-augmented generation (RAG) over knowledge graphs requires retrievers that can effectively capture both graph structure and semantic information. Recent approaches have explored graph neural network (GNN)-based retrievers to model graph topology in multi-hop reasoning tasks. In parallel, graph language models (GLMs) have emerged as a promising paradigm that integrates graph reasoning and the semantic capabilities of language models. In this work, we introduce a GLM-based retriever and investigate the comparative strengths of GLM-based, GNN-based, and traditional vector-search-based retrievers in single- and multi-hop RAG settings, and with a particular focus on transferability to unseen domains. Our findings suggest that finetuned GLM retrievers generalize better out of domain, achieving SOTA on two multi-hop benchmarks. On in-domain multi-hop QA datasets they remain comparable to prior work, with promising scaling as parameters and subgraph coverage increase. GNN-based retrievers achieve higher graph coverage with an efficient training setup, whereas the vector-search baseline excels at single-hop datasets.

## 5. An embedding-based framework enables statistical testing of gene-set function hypotheses inferred by large language models

- Authors: Yanhao Tan, Li-Ju Wang, T.W. Liang, Ying-Ju Lai, Chien-Hung Shih, Yibing Guo, Tyler M. Yasaka, George C. Tseng, Yu‐Chiao Chiu
- Source: openalex
- Venue type: journal
- Journal: Nature Communications
- Publication status: published
- Publication date: 2026-07-30
- DOI: https://doi.org/10.1038/s41467-026-75972-z
- Categories: Bioinformatics and Genomic Networks, Biomedical Text Mining and Ontologies, Machine Learning in Bioinformatics
- Relevance: 3.388345270851494
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://doi.org/10.1038/s41467-026-75972-z
- PDF: Unavailable
- Local PDF: Not downloaded

Abstract Emerging large language models (LLMs) can infer gene functions directly from gene lists, enabling hypothesis generation without predefined gene sets. However, these LLM-derived predictions are qualitative, and principled statistical validation is lacking. Here, we develop an embedding-based statistical framework that transforms gene and function descriptions into vector representations, enabling statistical testing of gene-gene and gene-function relationships and quantitative prioritization of de novo functional hypotheses inferred by LLMs. We benchmark seven state-of-the-art embedding models using curated and retrieval-augmented literature-derived gene descriptions across diverse biological contexts. OpenAI’s text-embedding-3-large and Google’s gemini-embedding-001 perform best, capturing gene-gene functional relationships in 88.7-92.5% of Gene Ontology biological processes and approximately 98.6% of canonical pathways. In gene-function association analyses, these models achieve high sensitivity (95.2-98.4%) and specificity (72.7-84.3%). Through contamination analysis and evaluation using experimentally informed protein assembly gene sets, our framework distinguishes biologically meaningful LLM-inferred hypotheses from noise, outperforming confidence-based inference and conventional enrichment analysis. We further develop the open-source R package DEGEmbedR and demonstrate its utility for interpreting a drug perturbation-derived differentially expressed gene (DEG) signature lacking significant conventional enrichment results. Together, these results establish LLM-derived embeddings as a quantitative foundation for functional genomics and the statistical validation of LLM-based gene function inference.

## 6. Kohn-Sham Spectral Embedding on Sparse Graphs at the Nishimori Temperature for Image Classification

- Authors: V. S. Usatyuk, D. A. Sapozhnikov, S. I. Egorov
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-30
- DOI: Unavailable
- Categories: cs.LG, cs.CV, cs.IT
- Relevance: 3.3355896047581703
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.28428v1
- PDF: https://arxiv.org/pdf/2607.28428v1
- Local PDF: pdf/2026-08-01_06_Kohn-Sham Spectral Embedding on Sparse Graphs at the Nishimori Temperature for Image Classification.pdf

We introduce Kohn--Sham Spectral Embedding (KSSE), a physics-inspired energy-based model replacing dense CNN classifiers with a sparse-graph spectral embedding evaluated at the Nishimori temperature of an associated Random-Bond Ising Model. By mapping pre-trained features onto quasi-cyclic low-density parity-check graphs and constructing a regularized Laplacian acting as a Kohn--Sham Hamiltonian, we solve $D$ independent channel spectral problems in $\mathcal{O}(N\log N + k^2_{\text{mode}} N)$ time via FFT on circulant blocks (leveraging Pontryagin self-duality of $\mathbb{Z}/p\mathbb{Z}$) and low-order Rayleigh refinement. Graph topology is optimized using \emph{star-domain surgery}: rather than destroying information-carrying codewords by removing frustrated cycles, we construct edge shifts creating local convexity around codewords while bounding residual frustration to $ρ(B_γ)\leq 1+δ$. Multi-scale fractal analysis ($D_2$ spectrum) and fractal learning-rate landscape certifies a landscape transition from rough regimes ($D_2>3$) to star-domain basins ($D_2<1$), enabling Rayleigh refinement with $k_{\text{mode}}=5$ modes. We prove six theoretical results: a generalized Ihara--Bass identity linking belief propagation to the Laplacian; trapping-set eigenvalue correspondence; additive channel separability with an explicit exchange-correlation bound; a surgery theorem bounding frustration with attractor width $Ω(1/\sqrt{d_{\min}})$; a quasi-stationarity perturbation bound; and a fixed-point convergence theorem. In a transductive protocol on ImageNet-1000 with frozen EfficientNet-B4 features ($D=1792$), KSSE achieves \textbf{88.93\%} Top-1 accuracy using $\approx 21.24$M parameters, outperforming Swin-L (197M, 86.4--87.3\%) and matching ViT-H/14 (632M, 88.0--89.5\%) under standard inductive setups, while reducing model footprint by $10\times$ and $30\times$, respectively.

## 7. Fully Inductive Cardinality Estimation

- Authors: Tim Schwabe, Lukas Ketzer, Maribel Acosta
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-30
- DOI: Unavailable
- Categories: cs.DB, cs.LG
- Relevance: 3.2727667596252252
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.28311v1
- PDF: https://arxiv.org/pdf/2607.28311v1
- Local PDF: pdf/2026-08-01_07_Fully Inductive Cardinality Estimation.pdf

Query optimization of Basic Graph Patterns (BGP) SPARQL queries over Knowledge Graphs (KG) requires accurate cardinality estimation. Recently published learned estimators outperform statistics- and sampling-based approaches, but share a limitation preventing their adoption in real-world triplestores: they are transductive and require retraining when the underlying graph changes or when applied to new graphs. We present FICE (Fully Inductive Cardinality Estimation), the first learned cardinality estimator for BGP queries over KGs that generalizes to entirely unseen graphs (including unseen relations), without any retraining. FICE is a graph neural network (GNN) with two coupled components. First, an encoder GNN over a factor-graph view of the KG produces entity and relation embeddings. We prove that BGP cardinality is a local function of the 2-hop neighborhood around bound terms in this view, motivating the local message-passing encoder. A decoder GNN then composes these embeddings along the join topology of the query to predict log-cardinality. The encoder and decoder are trained jointly, making the embeddings specialized for cardinality estimation. FICE is trained using neighborhood sampling to scale to KGs with millions of triples, and decouples embedding generation from cardinality decoding to enable estimation latency below a millisecond. Compared to learned and non-learned baselines over 10 KGs, FICE reduces the overall median q-error from 13.54 (for the best competitor) to 5.34 and dominates all approaches in tail behavior.

## 8. Beyond Classification: Pathology Foundation Models as Detection Encoders for Mitotic Figures

- Authors: Sweta Banerjee, Alireza Teimoury, Nils Porsche, Alexandra K. Stoll, Viktoria Weiss, Niklas Hargarter, Jonas Ammeling, Thomas Conrad, Christoph Stroblberger, Christopher Kaltnecker, Robert Klopfleisch, Christof A. Bertram, Katharina Breininger, Marc Aubreville
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-30
- DOI: Unavailable
- Categories: cs.CV, cs.AI
- Relevance: 3.2601482199777845
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.28007v1
- PDF: https://arxiv.org/pdf/2607.28007v1
- Local PDF: pdf/2026-08-01_08_Beyond Classification_ Pathology Foundation Models as Detection Encoders for Mitotic Figures.pdf

Pathology foundation models (FMs) are models trained on vast amounts of typically unlabeled data and have been shown to yield regularized latent spaces that can be used effectively in downstream classification tasks. This is also true for the classification of mitotic figures vs. other cells. However, it is so far unclear if the latent space of current FMs provides features that are discriminant and spatially suitably resolved to also serve as a backbone for dense object detection paradigms. In this work, we investigate this question for common current pathology FMs (UNI, UNI2-h, Virchow, Virchow2, H-optimus-0, H-optimus-1) and compare their performance against a fully end-to-end trained baseline based on a ResNet50 architecture. We combine FM backbones with representatives of single stage, dual stage and self-attention-based detectors (RetinaNet, Faster R-CNN, Deformable DETR respectively) on the multi-domain MIDOG++ dataset, and on the TUPAC16 dataset as an out-of-domain case. We show that the H-optimus-0 and Virchow models yielded competitive performance, indicating that the latent spaces of current FMs, all trained on image-level self-supervision, are suitable for direct mitotic figure detection and may be slightly more robust on our out-of-domain test case. All code is made available publicly at https://github.com/DeepMicroscopy/FM4MFdet.

## 9. PathView-Bench: Can Multimodal Large Language Models Achieve Fine-grained Multiscale Understanding of Pathology Images?

- Authors: Zongyi Chen, Yu Liang, Jie Lin, Liansheng Wang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-30
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 3.236594369821475
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.28318v1
- PDF: https://arxiv.org/pdf/2607.28318v1
- Local PDF: pdf/2026-08-01_09_PathView-Bench_ Can Multimodal Large Language Models Achieve Fine-grained Multiscale Understanding of Pathology Images.pdf

Multimodal large language models (MLLMs) are increasingly used to analyze pathology images. However, dominant multimodal benchmarks in pathology mainly score final diagnostic answers, captions, or reports. These evaluations provide limited insight into whether a model understands the multiscale visual content needed for pathology reasoning and decision-making. We introduce PathVU, a vision-anchored benchmark for fine-grained and multiscale visual understanding in computational pathology. Built from 23 public pathology imaging datasets with human-supervised labels and spatial annotations, PathVU evaluates MLLM understanding in two fields of view: Region FOV for high-resolution local regions and Slide FOV for macro whole-slide views. By converting raw annotations into deterministic task targets, PathVU enables programmatic scoring of region localization, visual recognition, quantity estimation, spatial reasoning, and insufficient-context judgment. The benchmark contains 14 VQA-style tasks, 61,673 images, and 308,070 samples across 28 organs and 7,253,526 annotations. Evaluating 18 representative general-purpose, medical-domain, and pathology-oriented MLLMs, we observe substantial limitations even in advanced models on fine-grained visual tasks across multiscale pathology images. PathVU provides a reproducible basis for developing and evaluating pathology MLLMs with explicit multiscale visual understanding.

## 10. A Lightweight Foundation Model for Collider Physics with Multi-Domain Adaptation

- Authors: Liangyu Wu, Qibin Liu, Alexander Yue, Julia Gonski
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-29
- DOI: Unavailable
- Categories: cs.LG, hep-ph
- Relevance: 3.2204807426507056
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.27501v1
- PDF: https://arxiv.org/pdf/2607.27501v1
- Local PDF: pdf/2026-08-01_10_A Lightweight Foundation Model for Collider Physics with Multi-Domain Adaptation.pdf

We present a lightweight approach to foundation modeling (\textbf{NEXUS}) that leverages pre-trained learning from collider physics data towards out-of-domain tasks in other scientific datasets, using a fully connected autoencoder model with approximately 3 million parameters. The model pre-trains with no supervision over a large-scale collision dataset from the Large Hadron Collider modeled by charged particle track features. Downstream tasks for collider analyses, such as kinematic regression and event classification, are developed on pre-trained model weights and achieve improved accuracy with only small labeled datasets when compared to equivalent architectures trained from scratch. The benefits of pre-training are additionally investigated through latent space interpretation and application to other domains, including gravitational waves, flood forecasting, and neural activity. Furthermore, the relative computational simplicity of NEXUS is demonstrated compared to transformer approaches at comparable scale, opening the door to power-efficient inference and real-time or edge applications of foundation models in scientific experiments.

## 11. A Structured Knowledge Infrastructure for Domain-Specific Data Asset Discovery

- Authors: Mengdi Chen, Yuanxin Huang, Yulin Jiang, Wei Sun
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-30
- DOI: Unavailable
- Categories: cs.IR, cs.AI, cs.DB
- Relevance: 3.2106698966733918
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.27748v1
- PDF: https://arxiv.org/pdf/2607.27748v1
- Local PDF: pdf/2026-08-01_11_A Structured Knowledge Infrastructure for Domain-Specific Data Asset Discovery.pdf

Enterprise data analytics agents face two structural failures: generic RAG retrieves the wrong asset (Hit@10=19.1%) and delivers no usage knowledge to prevent metric misinterpretation---stemming from four root causes (C1--C4) ranging from semantic gap and entity ambiguity to schema drift and asset-usage gap. We present a two-layer solution deployed in the commercial advertising data warehouse at Xiaohongshu (5,300+ Hive tables, 14 domains). A three-tier dual-purpose knowledge base (179 documents, eight-section annotation template) serves both retrieval and generation, with a closed-loop refresh pipeline maintaining day-level freshness (one yes/no approval, 30s hot-reload). The Graph-Guided Retriever (GGR) uses a 2,859-node knowledge graph as a candidate gate with intent routing to deliver 71.6x token reduction. The Scene-Aware Ranker (SAR) applies 19-class entity recognition and explicit scenario annotations; negative knowledge alone contributes 25 percentage points of Hit@10 gain. On two 100-question benchmarks, Hit@10 rises from 19.1% to 96.6% (+77.5pp) and knowledge coverage from 56% to 77%, at 4.84--5.33s end-to-end latency.

## 12. Reasoning Consensus: Structural Ensembling of LLM Reasoning via Weighted DAG Aggregation

- Authors: Amruta Parulekar, Jinu Lee, Dilek Hakkani-Tür, Hari Sundaram
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-30
- DOI: Unavailable
- Categories: cs.CL, cs.AI, cs.LG
- Relevance: 3.201286446328371
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.27783v1
- PDF: https://arxiv.org/pdf/2607.27783v1
- Local PDF: pdf/2026-08-01_12_Reasoning Consensus_ Structural Ensembling of LLM Reasoning via Weighted DAG Aggregation.pdf

Large Language Models (LLMs) explore problems through chain-of-thought, but this exploration is buried in unstructured prose. On high-stakes tasks, users cannot tell which steps are well-supported, which alternatives were seriously considered, or how the final conclusion compares to those the model discarded. We propose a framework that ensembles the reasoning structure, not just the answers, of multiple LLMs by weighted merging of Directed Acyclic Graphs (DAGs) extracted from reasoning chains. We weight each step by how many traces independently attest to it, to return "Consensus Reasoning". Across six benchmarks spanning statutory interpretation, graduate-level science, narrative multi-hop reasoning, and first-order logic, our ensemble outperforms a matched-budget majority-vote baseline, with a maximum accuracy gain of 3.1% on MuSR-MM (narrative multi-hop reasoning). On a single model, the framework matches or exceeds self-consistency at the same trace budget while additionally exposing an inspectable consensus reasoning graph. Ensemble weights correlate with LLM-judge rankings of reasoning quality at Spearman $ρ= 0.30$-$0.51$, and consensus subgraphs are preferred over alternatives leading to the majority-vote answer in 54.4-65.4% of head-to-head comparisons across five of six datasets. We observe that our framework can also be used to analyze diverse reasoning perspectives for a problem.

## 13. A foundation model of numerical intelligence with cross-disciplinary generalization

- Authors: Chenghan Wu, Zongmin Yu, Liu Yang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-30
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 3.1821898082434963
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.28432v1
- PDF: https://arxiv.org/pdf/2607.28432v1
- Local PDF: pdf/2026-08-01_13_A foundation model of numerical intelligence with cross-disciplinary generalization.pdf

Intelligence is commonly understood as the ability to acquire and apply knowledge, adapt to unfamiliar situations and solve new problems. Large language models exhibit this capacity by inferring task-relevant knowledge from textual context and applying it to new tasks. Yet intelligence need not be confined to language. For scientific and social systems, we need models that acquire and apply knowledge from numerical context-an ability we call numerical intelligence. Here we introduce UNified In-Context Operator Networks (UNICON), a foundation model that exhibits numerical intelligence across disciplines. Using graph-based examples from a system as context, UNICON infers the predictive relation shared across them and applies it to queries from the same system. Across scientific and social systems, including those from disciplines absent from training, the same model approaches specialist performance without retraining. Combining UNICON with language-model agents yields further gains, enabling it to surpass state-of-the-art specialists in a discipline unseen in training. We further show that training-corpus diversity improves generalization to unseen disciplines. Together, these results establish UNICON as a foundation model of numerical intelligence and position it as a building block for a broader ecosystem of artificial intelligence.

## 14. SDO: Structure-Aware Data Organization for Efficient LLM Post-Training

- Authors: Jinliang Gao, Ning Yang, Hai Wang, Baili Xiao, Pin Lyu
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-29
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.1429709592590402
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.27273v1
- PDF: https://arxiv.org/pdf/2607.27273v1
- Local PDF: pdf/2026-08-01_14_SDO_ Structure-Aware Data Organization for Efficient LLM Post-Training.pdf

Post-training of large language models is expensive, and existing efficiency improvements mainly focus on selecting informative samples or designing training schedules. However, data organization itself is usually treated as a static preprocessing step: embedding-based grouping methods construct fixed partitions before training and cannot adapt to the evolving sample exposure during optimization. As a result, all samples receive similar exposure despite their different optimization needs, leading to redundant updates for some samples while leaving others under-optimized. To address this problem, we propose SDO (Structure-Aware Data Organization), a plug-and-play data organization framework with an exposure-driven feedback mechanism that organizes mini-batch composition and sample exposure according to representation-space structure. SDO operates epoch by epoch on frozen external embeddings, avoiding model warm-up training overhead: within each epoch, locality-aware batching forms coherent mini-batches via KNN neighborhood traversal; across epochs, exposure-balanced scheduling records per-sample participation and reduces the sampling probability of over-exposed samples to preserve long-term coverage. Across SFT, DPO, and GRPO, SDO accelerates convergence, with the largest gains observed in the early-to-mid phase, producing more coherent gradients and more balanced accuracy across question types without permanently excluding training samples.

## 15. Explorative Modeling: Unlocking a Third Pretraining Axis and End-to-End Generation

- Authors: Alexi Gladstone, Heng Ji, Yilun Du
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-29
- DOI: Unavailable
- Categories: cs.LG, cs.AI, cs.CL, cs.CV
- Relevance: 3.1312723077732367
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.27372v1
- PDF: https://arxiv.org/pdf/2607.27372v1
- Local PDF: pdf/2026-08-01_15_Explorative Modeling_ Unlocking a Third Pretraining Axis and End-to-End Generation.pdf

The deep learning revolution, kicked off by AlexNet, taught us that end-to-end training beats decomposing a problem into hand-designed stages. Generative modeling, however, has remained the exception-despite generative models being remarkably capable, they are still not trained end-to-end. This is because, at its core, generative modeling is about handling distributions with many modes, and existing scalable approaches handle this the same way, by factoring the generation procedure, which prevents end-to-end generation. In this work, we introduce Explorative Modeling, a new paradigm that instead factors the training loop, exploring K candidate matches between model generations and data, and training on the best, so predictions commit to modes rather than blurring them. We find Explorative Models (XMs) useful in two settings. First, increasing exploration adds a third pretraining axis beyond parameters and data for existing generative models-where scaling exploration monotonically improves performance across both continuous and discrete domains (images, video, and language). Notably, gains from exploration increase with scale, climbing from 7% to 36% as data scales and from 13% to 23% as models grow, with efficiency gains more than doubling at 3x the compute. Concretely, exploration improves FLOP efficiency by 4.1x, sample efficiency by 6.2x, parameter efficiency by 47%, lifts the strongest of image-generation recipes to a near-state-of-the-art 1.43 FID on ImageNet without guidance, enables scaling how end-to-end existing models are, and unlocks scaling generalization. Second, XMs enable end-to-end reconstructive generative modeling, matching diffusion on control tasks with 16-256x fewer inference steps. Together, these results establish XMs as both a new pretraining axis for existing generative models and a standalone end-to-end generative modeling paradigm.

## 16. A Mathematical Framework for Topological Causal Data Analysis

- Authors: Hugo Gobato Souto, Ioannis Diamantis
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-30
- DOI: Unavailable
- Categories: stat.ME, math.ST, stat.ML
- Relevance: 3.1280228501121514
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.28161v1
- PDF: https://arxiv.org/pdf/2607.28161v1
- Local PDF: pdf/2026-08-01_16_A Mathematical Framework for Topological Causal Data Analysis.pdf

Many modern outcomes, including images, point clouds, networks, and spatial fields, are structured objects for which \(Y^1-Y^0\) may be undefined or scientifically inadequate. We introduce \emph{Topological Causal Data Analysis} (TCDA), a framework separating the observation space, causal-model class, topological representation, and causal query. Topology does not define interventions; it supplies stable, shape-sensitive summaries after causal assumptions have been specified. We distinguish outcome-level TCDA, which transforms individual potential outcomes, from distribution-level TCDA, which transforms interventional outcome laws, and characterize when outcome and distribution level contrasts agree. Building on recent outcome-level theory, we formulate identification and doubly robust representations for Banach-space-valued summaries. At the distribution level, we identify targets through the standard causal \(g\)-formula and derive stability-transfer bounds and plug-in consistency. We also place target-specific topological ignorability within the framework, clarifying when a covariate-standardized coarse effect can be identified without identifying the full interventional laws. Finally, we delimit the role of observational topology in causal discovery: it can assist diagnosis on restricted model classes but cannot by itself identify causal structure.

## 17. RefineSVG: Visual Feedback-Driven Reinforcement Learning for Image-to-SVG Generation

- Authors: Shaobo Liu, Feiqiao Mao, Shuaishuai Zhou, Yan Zhan, Weiqi Tan, Zhiqiong Lu, Zhengping Liang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-30
- DOI: Unavailable
- Categories: cs.CV, cs.AI
- Relevance: 3.1092371605153346
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.27699v1
- PDF: https://arxiv.org/pdf/2607.27699v1
- Local PDF: pdf/2026-08-01_17_RefineSVG_ Visual Feedback-Driven Reinforcement Learning for Image-to-SVG Generation.pdf

We propose RefineSVG, a single-step closed-loop visual feedback framework that enables multimodal large language models (MLLMs) to perform high-fidelity image-to-SVG generation through self-correction. Existing MLLM-based approaches rely on single-pass open-loop inference, where the model receives visual input only once and must generate thousands of SVG code tokens without intermediate verification. This paradigm inevitably leads to geometric drift, error accumulation, and visual hallucination on complex images. RefineSVG overcomes this limitation by invoking an external rendering engine after an initial SVG generation pass to compare the rendered output against the target image. The comparison yields a multi-dimensional visual residual map (Diff-Map) that is fed back to the model as a ReAct-style correction signal, driving a targeted correction step. To support this render-observe-correct interaction, we further introduce an SVG-oriented semantic vocabulary that compresses token sequences by over 52%. A progressive training pipeline spanning supervised fine-tuning, rejection-sampling cold-start data construction, and end-to-end agentic reinforcement learning aligns the model with closed-loop visual correction. Extensive experiments show that RefineSVG consistently outperforms existing baselines in reconstruction fidelity, structural accuracy, and code efficiency.Code is available at https://github.com/liuxiaobo66/RefineSVG.

## 18. Baikal: Structured Search for Deep Research over Data Lakes

- Authors: Dhruv Agarwal, Rishitha Guttapalle Mohan, Aarti Kumari, Ashi Sinha, Athulya Anil, Kavitha Srinivas, Horst Samulowitz, Andrew McCallum
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-30
- DOI: Unavailable
- Categories: cs.AI, cs.CL, cs.LG
- Relevance: 3.0904643268655136
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.27726v1
- PDF: https://arxiv.org/pdf/2607.27726v1
- Local PDF: pdf/2026-08-01_18_Baikal_ Structured Search for Deep Research over Data Lakes.pdf

Deep research over data lakes requires an LLM agent to investigate evidence across thousands of heterogeneous tables and passages to synthesize a report. Existing methods perform iterative retrieval and generation, letting accumulated context determine what to investigate next, which can overexploit locally promising evidence and fail to cover distinct semantic regions under a fixed budget. To address this, we cast deep research over data lakes as a budgeted search problem and present Baikal - a framework that clusters heterogeneous evidence into semantic regions, then searches over them adaptively to balance exploration and exploitation. Within each selected region, Baikal generates and investigates region-grounded subquestions, using finding quality as rewards to update region-level value estimates and guide search under policies ranging from random and LLM-guided selection to Bayesian $ε$-greedy and UCB. We evaluate Baikal on 15 queries each over HybridQA and TAT-QA data lakes containing 10,993 and 2,757 tables, respectively, together with 227K Wikipedia passages and 13K financial report passages. We assess research quality with a new rubric covering groundedness, relevance, diversity, and utility, and use GPT-5-mini to score Baikal and strong baselines, including DeepSearcher and an OpenCode research agent with retrieval and clustering variants. Across both data lakes, Baikal performs strongly under several region-selection policies; its best configuration improves report scores over the strongest baselines by 28% on HybridQA and 36% on TAT-QA. Our analyses attribute these gains to organizing and exploring semantic evidence regions, which improves groundedness and diversity and yields more useful findings under the same subquestion budget. These results demonstrate the value of structured semantic exploration for systematic research and discovery over heterogeneous data lakes.

## 19. Shapes from Examples: Foundations of Shape Learning in Recursive SHACL

- Authors: Bente Gortworst, Cem Okulmus, Magdalena Ortiz, Anni-Yasmin Turhan
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-30
- DOI: Unavailable
- Categories: cs.AI, cs.LO
- Relevance: 3.0871311129013157
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.27934v1
- PDF: https://arxiv.org/pdf/2607.27934v1
- Local PDF: pdf/2026-08-01_19_Shapes from Examples_ Foundations of Shape Learning in Recursive SHACL.pdf

SHACL shapes enable data graph validation, making automatic shape learning essential for knowledge graph applications. We investigate the well-known fitting approach to this task: given sets P and N of positive and negative example nodes from an input graph, compute a shape expression C, possibly using shape names defined in a recursive shape catalogue, that validates at every node in P and none in N. We focus on the case where C is written in a core fragment of SHACL corresponding to the Description Logic ELI. For the catalogue, we consider the well-founded, stable, and supported semantics. We address fitting existence and most specific fitting computation, establish tight exponential-time upper bounds for both problems, and obtain polynomial bounds for relevant special cases.

## 20. Integrative spatial profiling of 3D genome organization and gene expression in tissue

- Authors: Guo, P., Cui, Y., He, J., Waldman, A. J., Zhu, J., Chen, Y., Huang, Z., Zhou, J., Phillips-Cremins, J. E., Deng, Y.
- Source: biorxiv
- Venue type: preprint
- Journal: biorxiv
- Publication status: preprint
- Publication date: 2026-07-31
- DOI: 10.64898/2026.07.28.741242
- Categories: genomics
- Relevance: 3.0775255550992284
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://www.biorxiv.org/content/10.64898/2026.07.28.741242v1.full.pdf
- PDF: https://www.biorxiv.org/content/10.64898/2026.07.28.741242v1.full.pdf
- Local PDF: pdf/2026-08-01_20_Integrative spatial profiling of 3D genome organization and gene expression in tissue.pdf

The interplay between 3D genome architecture and transcriptional activity is fundamental to gene regulation. However, existing methodologies cannot simultaneously measure these modalities within intact tissues, limiting our understanding of how genome organization coordinates transcriptional programs across diverse cell types and spatial microenvironments. Here, we introduce Spatial Hi-C-RNA, a spatial multi-omics technology that enables the genome-wide co-mapping of chromatin conformation and transcriptome directly from the same tissue section at near-single-cell resolution. Applied to the mouse embryo and adult brains, Spatial Hi-C-RNA generated high-resolution tissue maps revealing that chromatin organization and gene expression jointly define spatially coherent domains aligned with histological structures. While concordant features were observed across modalities, distinct domain patterns also emerged, indicating that chromatin structure and transcription each contribute complementary layers of spatial regulation. We further demonstrated the robustness and biological insight of Spatial Hi-C-RNA in human melanoma, where both modalities delineated tumor boundaries and microenvironmental niches. Notably, chromatin maps revealed fine-scale tumor subdomains undetectable by transcriptomic profiling alone, highlighting the added resolution provided by spatial chromatin architecture. Integrated analysis revealed that multiscale 3D genome features, from A/B compartments and topologically associating domains to chromatin loops, are closely coupled with domain- and cell-type-specific transcriptional programs. In addition, Spatial Hi-C-RNA resolves spatiotemporal dynamics underlying embryonic lineage specification and tumor progression. Together, these capabilities extend the spatial omics landscape beyond transcriptome and epigenome profiling to the level of chromatin organization, establishing an integrative framework for understanding tissue biology across development and disease.

## 21. RepBench: Compiling Benchmarks into Capability Representations for Large Language Models

- Authors: Yanshi Li, Xueru Bai, Shuman Liu, Long Zhang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-30
- DOI: Unavailable
- Categories: cs.CL, cs.AI
- Relevance: 3.0644693157287994
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.28008v1
- PDF: https://arxiv.org/pdf/2607.28008v1
- Local PDF: pdf/2026-08-01_21_RepBench_ Compiling Benchmarks into Capability Representations for Large Language Models.pdf

Representation engineering reads and steers capability directions in large language models, yet methods are typically evaluated on paper-specific synthetic data. The resulting measurements are difficult to compare or reproduce and may reflect surface patterns rather than capabilities. We present RepBench, a benchmark-grounded data layer for capability-aligned representation probing. Crawling 13,427 benchmark papers yields a taxonomy of 182 capability clusters in 13 families; harvesting 353 public benchmark datasets yields 46,149 audited probe texts covering 94 capabilities, each supported by at least two independent benchmarks. This multi-benchmark design reduces dependence on any single source: raw per-text vectors exhibit no natural cluster granularity, whereas benchmark-pooled capability vectors show an interior clustering optimum at a small number of clusters on all 12 evaluated models, with low agreement to the human taxonomy. Under cross-benchmark transfer evaluation across twelve models completed by all four readouts, difference-in-means attains the highest model-level mean on ten models, while logistic regression wins the most capability-model cells. This disagreement shows that the readout method and aggregation criterion are meaningful evaluation dimensions. The pipeline, corpus, and evaluation code are released as a reusable closed-loop workflow.

## 22. Divergence Decoding: Training-Free Capability Fusion

- Authors: Yimi Wang, Hao Li, Shuo Yang, He Cao, Dechen Zhang, Ziang Wu, Zhiyuan Yan, Fanyang Mo, Li Yuan
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-28
- DOI: Unavailable
- Categories: cs.AI, cs.LG
- Relevance: 3.0569801480155476
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.27248v1
- PDF: https://arxiv.org/pdf/2607.27248v1
- Local PDF: pdf/2026-08-01_22_Divergence Decoding_ Training-Free Capability Fusion.pdf

While large language models excel in reasoning, these generalists often lack knowledge for specialized scientific domains. Conversely, domain models~(specialists), while knowledgeable, suffer from specialization side-effects including diminished logic and reduced robustness.To address this dilemma, we introduce Divergence Decoding, a training-free framework for capability fusion. It reconstructs the "draft-and-verify" skeleton of speculative decoding into an adaptive routing mechanism. The core is using Jensen-Shannon divergence to monitor the distributional disagreement between the two models at each token. When the specialist exhibits significant divergence, our method identifies it as a potential reasoning risk and instantaneously routes control to the generalist. This allows the dynamic injection of general reasoning while preserving domain expertise, achieving inference-time policy composition of the generalist and the specialist.We evaluate Divergence Decoding across diverse model families (Qwen and Llama series) on challenging scientific benchmarks (GPQA, ChemBench, and ChemCoTBench). Experimental results demonstrate that Divergence Decoding outperforms both the domain-specialized and general-purpose models, effectively surpassing the performance of most single-model baseline. This suggests that Divergence Decoding provides a general, training-free paradigm for fusing diverse LLM capabilities through adaptive inference-time collaboration.

## 23. Latent-Kernel Discrete Flow Maps for Few-Step Generation

- Authors: Mansoor Ahmed, Yue-Tsz Fan, Hemanth Venkateswara, Murray Patterson
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-29
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.0395161226902405
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.27529v1
- PDF: https://arxiv.org/pdf/2607.27529v1
- Local PDF: pdf/2026-08-01_23_Latent-Kernel Discrete Flow Maps for Few-Step Generation.pdf

Discrete diffusion and flow-matching models denoise a sequence over many steps, but to keep each step cheap, they factorize the transition across positions and decide every token independently. This makes few-step generation challenging for text when the target couples two positions, such as a subject and a verb that must agree. An independent update commits to them separately, and many function evaluations are spent repairing the mismatch. Existing few-step methods buy back the lost correlation by distilling or rectifying a slow teacher, and so inherit the teacher's quality ceiling. We ask instead whether a model can express correlated steps natively, and answer with Latent-Kernel Discrete Flow Maps (LKF), a from-scratch flow-map kernel that is a mixture of M factorized components tied by a single shared latent. Conditioned on the latent, each component is cheap, and the mixture is summed over the latent in closed form for small M. We show that a single step places mass on correlated completions with the same sampling time complexity as a factorized model, since one latent is drawn per sequence and reused across the entire denoising trajectory. We also show that the Masked Diffusion Language Model (MDLM) is a special case of our LKF model at M=1. The experiments for unconditional text generation on the One-Billion-Word (LM1B) and WikiText-103 benchmarks show that our LKF model learns strongly heterogeneous components and improves generative perplexity by 2.1x to 3.3x over the likelihood baselines without losing diversity. The gain grows with M, and at M=8, it surpasses distilled and rectified few-step samplers. The source code is available at: https://github.com/mansoor181/lkf.git

## 24. Prox: Training-Free FFN Activation Sparsity via Approximate Intermediate-Channel Salience in LLMs

- Authors: Jinyi Liu, Wei Chen, Pengyu Chen, Xinyi Yuan, Minghe Bai, Guoquan Wu, Jun Wei
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-30
- DOI: Unavailable
- Categories: cs.LG, cs.CL
- Relevance: 3.0335824003921097
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.27591v1
- PDF: https://arxiv.org/pdf/2607.27591v1
- Local PDF: pdf/2026-08-01_24_Prox_ Training-Free FFN Activation Sparsity via Approximate Intermediate-Channel Salience in LLMs.pdf

Feed-forward networks (FFNs) dominate memory traffic and computation in large language model (LLM) inference, making them a primary target for activation sparsification. However, existing training-free methods suffer substantial model-quality degradation at high sparsity due to limitations in their channel-selection strategies. We observe that the SwiGLU intermediate state provides a highly effective channel-selection signal, but obtaining it requires costly dense computation. To address this, we present \emph{Prox}, a two-stage training-free framework for sparse SwiGLU FFNs. Prox hinges on the key insight: sparse execution requires only the channel mask induced by the intermediate state, which can be constructed from the magnitude ranking of its entries rather than their exact values. Specifically, Stage 1 uses input sparsity and quantized proxy weights to construct a shared mask; Stage 2 computes the selected channels exactly, enabling sparse execution of all three projections. Across ten LLMs from six model families, Prox outperforms training-free baselines at all sparsity levels, achieves up to a $1.99\times$ end-to-end decoding speedup at 70\% FFN sparsity, and is compatible with quantization and sparse attention.

## 25. DeepResearch Agent System

- Authors: Yong Huang, Yulu Huang, for the team Collaboration
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-30
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 3.032646852628745
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.27562v1
- PDF: https://arxiv.org/pdf/2607.27562v1
- Local PDF: pdf/2026-08-01_25_DeepResearch Agent System.pdf

The DeepResearch Agent System is a large language model system engineered for deep information retrieval, multi-step reasoning, and autonomous research tasks. Built upon a sparse activation architecture with 30 billion total parameters of which only 3 billion are activated per token, the system achieves state-of-the-art performance on multiple agent search benchmarks while delivering 3.2 times faster inference compared to dense counterparts of equivalent scale. The system supports a 128K-token context window with hierarchical attention mechanisms that yield 18.7% accuracy and 23.4% recall improvements over standard long-context approaches. A dual-mode reasoning engine provides both a ReAct paradigm for basic multi-step problem solving and an IterResearch mode for high-performance iterative research with up to 20 reasoning steps, collectively delivering a 31.2% accuracy improvement over single-pass baselines. Multi-tool coordination integrates retrieval, computation, web search, and file parsing modules to achieve 92.1% tool-use accuracy. A reinforcement learning optimization framework based on the GRPO algorithm provides token-level policy gradients that improve training stability by 35% and accelerate convergence by 42%. An automated data synthesis pipeline with seed-based expansion achieves a 92.5% usability rate. Benchmark results include 87.3% on Humanity's Last Exam, 85.3% on BrowserComp Chinese, and 91.2% on WebWalkerQA. The system is fully open-sourced, including data synthesis, training, and inference code, and supports applications in academic research, business analysis, R&D support, and education.

## 26. MANTA: Multi-Agent Network Topology Adaptation for Self-Evolving Multi-Agent Systems

- Authors: Mao-xun Huang, Jerry Wang, Yi-Cheng Lai, Zhengxin Zhang, Claire Cardie, Hen-Hsen Huang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-30
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 3.026319279860129
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.28527v1
- PDF: https://arxiv.org/pdf/2607.28527v1
- Local PDF: pdf/2026-08-01_26_MANTA_ Multi-Agent Network Topology Adaptation for Self-Evolving Multi-Agent Systems.pdf

Large language model-based multi-agent systems improve complex problem solving through task decomposition, agent specialization, information exchange, and intermediate validation. However, existing systems typically treat communication topology as a fixed design choice or an offline optimization target. We introduce MANTA, a framework for Multi-Agent Network Topology Adaptation that enables communication structures to self-evolve at inference time. Before execution, MANTA initializes a task-conditioned topology from prior structural experience. During deployment, it monitors collaboration traces and applies bounded structural updates when the current organization becomes insufficient. These updates can modify agent roles, communication links, execution order, information visibility, and validation pathways while preserving the task interface and agent budget. We evaluate MANTA against representative single-agent and multi-agent baselines on five benchmarks spanning information seeking, tool use, planning, workflow execution, and mathematical reasoning. MANTA achieves the highest average score of 74.0, outperforming the strongest baseline by 5.8 percentage points and obtaining the best result on PlanCraft. These results show that inference-time self-improvement can extend to the architecture of collaboration itself.

## 27. Interpretable Representation via LLM-Driven Generative Disentanglement for Local-Life Service Recommendation

- Authors: Long Zhang, Hao Jiang, Sheng Yu, Fei Pan, Peng Jiang, Kun Gai
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-30
- DOI: Unavailable
- Categories: cs.IR, cs.AI
- Relevance: 3.014421832126166
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.27944v1
- PDF: https://arxiv.org/pdf/2607.27944v1
- Local PDF: pdf/2026-08-01_27_Interpretable Representation via LLM-Driven Generative Disentanglement for Local-Life Service Recommendation.pdf

While large language models (LLMs) have advanced ID-based recommendation through Semantic ID (SID) modeling, existing SID generation frameworks largely follow a single-representation-then-quantization paradigm. This design faces two bottlenecks: semantic entanglement mixes heterogeneous attributes, such as geography, brand, and category, causing information loss during quantization, low-quality SIDs, and severe collisions; moreover, black-box representation learning provides neither explicit attribute semantics nor clear geographic or semantic meanings for SID positions. These limitations weaken both retrieval reliability and the ability to diagnose or control SID generation. We propose Interpretable Representation via LLM-Driven Generative Disentanglement for Local-Life Service Recommendation (LGRID). LGRID introduces a generative disentanglement paradigm through an Encode -> Disentangle -> Align -> Quantize pipeline. It first uses joint LLM encoding to preserve cross-attribute geographic-semantic dependencies, rather than encoding fields independently. A Structured Disentangled Block then routes hidden states into attribute-aligned slots for geographic and semantic factors. Synergistic Alignment Learning makes these slots both generatively decodable and discriminative for retrieval, while Dual-Stream Residual Quantization separately discretizes the two streams into compact SIDs with explicit attribute correspondence. This design yields interpretable SIDs with positions grounded in item attributes and local-service semantics. Experiments on Kuaishou and Foursquare show that LGRID consistently outperforms strong SID baselines, achieving up to a 5.44 percent relative AUC gain. It also achieves over 99 percent attribute-decoding accuracy for coarse geographic fields and reduces the full-SID collision rate to 39.9 percent, compared with 97.0 percent for LGSID.

## 28. SciDataSailor: Deep Scientific Data Exploring

- Authors: Jiyong Rao, Yicheng Qiu, Chi Zhang, Chunfeng Song, Runkai Zhao
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-29
- DOI: Unavailable
- Categories: cs.AI, cs.CL
- Relevance: 2.9752568880990222
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.28098v1
- PDF: https://arxiv.org/pdf/2607.28098v1
- Local PDF: pdf/2026-08-01_28_SciDataSailor_ Deep Scientific Data Exploring.pdf

Scientific datasets are commonly organized as hierarchical repositories containing heterogeneous and interdependent files, making their inspection, integration, and analysis labor-intensive and reliant on domain expertise. Although large language model (LLM) agents have advanced substantially in planning, reasoning, and tool use, existing research has largely overlooked their ability to interact with real scientific data assets through executable environments. We introduce Deep Scientific Data Exploration, an agentic task paradigm in which agents navigate repositories, interpret heterogeneous files and schemas, execute analyses, integrate cross-file evidence, and produce conclusions grounded in executed observations. To operationalize this paradigm, we present SciDataSailor, a framework for synthesizing tool-interactive trajectories by balancing broad exploration with targeted exploitation. SciDataSailor instantiates trajectory synthesis as Monte Carlo Tree Search (MCTS) with four task-specific mechanisms: difficulty-stratified exploration seeds, dual-feedback first-play urgency, hierarchical strategy-to-tool action generation, and entropy-guided branching. Using this framework, we construct SciDataSailor-SFT-2K for supervised fine-tuning and SciDataSailor-Bench for evaluation, with the latter comprising 627 meta-information summarization tasks and 586 scientific question-answering tasks across 27 datasets spanning the life, earth, and physical sciences.

## 29. LAST: The Last Query Token Guides Visual Token Pruning for Edge-Cloud Collaborative MLLM Inference

- Authors: Feng Yang, Xinrui Ju, Keyang Zhang, Xiandong Meng, Rongqun Lin, Howard Leung, Shiqi Wang, Haoliang Li, Chris Xing Tian
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-30
- DOI: Unavailable
- Categories: cs.CV, cs.AI
- Relevance: 2.9508192146521357
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.27952v1
- PDF: https://arxiv.org/pdf/2607.27952v1
- Local PDF: pdf/2026-08-01_29_LAST_ The Last Query Token Guides Visual Token Pruning for Edge-Cloud Collaborative MLLM Inference.pdf

Multimodal foundation models are reshaping edge-cloud visual intelligence from task-specific feature pipelines into token-based interfaces, where edge devices encode visual inputs into tokens for a general-purpose cloud MLLM. However, dense visual-token sequences increase cloud-side inference costs. Existing pruning methods mainly target centralized inference: vision-driven methods can operate before cloud execution but are typically query-agnostic, whereas query-guided methods often rely on internal states of the target MLLM and cannot determine token relevance before transmission. Compact guidance models offer an alternative, but existing designs may require costly attention aggregation or auxiliary generation. We propose LAST, a training-free framework for query-dependent visual token pruning in edge-cloud collaborative MLLM inference. LAST uses a compact edge-side VLM as a guidance proxy and derives a lightweight importance signal from the last query token's attention to visual tokens. Under causal attention, the last query token can attend to the full visual sequence and the entire query context, enabling query-aware pruning without cloud-model access, autoregressive generation, or costly aggregation over multiple query positions. LAST then retains a diverse set of query-relevant visual tokens under a fixed token budget. We evaluate LAST on 11 multimodal benchmarks under multiple token budgets against pruning methods with different guidance strategies. Experiments show that LAST consistently achieves the strongest performance, preserving 95.4% of the full-token accuracy while retaining only 12.5% of the visual tokens, with low edge-side selection overhead and reduced cloud-side computation.

## 30. Bridging Inference-Time Scaling and Episodic Memory with Action-Centric Graphs

- Authors: Xu Zheng, Chaohao Lin, Zhuomin Chen, Weijieying Ren, Haifeng Chen, Wei Cheng, Dongsheng Luo
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-29
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 2.9075915093050715
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.27415v1
- PDF: https://arxiv.org/pdf/2607.27415v1
- Local PDF: pdf/2026-08-01_30_Bridging Inference-Time Scaling and Episodic Memory with Action-Centric Graphs.pdf

Recent advancements in inference-time scaling have significantly unlocked the complex reasoning capabilities of Large Language Models~(LLMs). However, for agents, these approaches suffer from a critical inefficiency, operating in a stateless manner and engaging in redundant search processes. Existing memory mechanisms largely rely on the reasoning capabilities of LLMs, leading to prohibitive computational costs. In this paper, we propose a novel framework, \textit{GAMER}~(Graph-based Action-centric Memory with Episodic Reasoning), that bridges the gap between inference scaling and episodic memory. Our approach models historical reasoning as a dynamic \textit{Action-Centric Graph}. By decoupling the memory mechanism from LLMs, our method can save token/money usage by providing less memory context than memory mechanism baselines. To extract knowledge from the graph effectively, we use a dual-stream Temporal Difference learning mechanism to estimate the positive~(suggestion) and negative~(avoidance) value of action nodes based on past successes and failures. During the inference phase, this learned value function optimizes decision-making bi-directionally, so that positive values provide action suggestions, while negative values indicate high-risk actions. By performing efficient searches on the graph, our method significantly improves the efficiency of inference scaling. Experiments on multiple benchmarks demonstrate that \textit{GAMER} achieves superior performance by \textbf{20.81\%/6.17\%} for success/progress rate compared to vanilla baselines.
