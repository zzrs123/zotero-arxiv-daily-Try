# Paper Daily Reading - 2026-07-22

## 1. Harmonised benchmarking of foundation models for single-cell and spatial transcriptomics reveals context-dependent generalisation

- Authors: Sally Chen, Roxana Zahedi, Lucy Chhuo, Ricky Nguyen, Marjan BaghGolshani, Amin Beheshti, Mark Grosser, Min Yang, Nona Farbehi, Nigel Lovell, Ahmadreza Argha, Fatemeh Vafaee, Youqiong Ye, Hamid Alinejad-Rokny
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-19
- DOI: Unavailable
- Categories: q-bio.GN, q-bio.CB
- Relevance: 3.7718504431744333
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.17227v1
- PDF: https://arxiv.org/pdf/2607.17227v1
- Local PDF: pdf/2026-07-22_01_Harmonised benchmarking of foundation models for single-cell and spatial transcriptomics reveals context-dependent gener.pdf

Single-cell and spatial foundation models promise transferable biological representations, yet their generality remains largely untested across modalities, biological domains and analytical tasks. We benchmarked six representative models, Nicheformer, CellPLM, scGPT-spatial, GenePT, scELMo and Novae, using a harmonised framework spanning scRNA-seq, spatial transcriptomics and Perturb-seq. We evaluated zero-shot and continually pretrained clustering, supervised annotation, marker-gene concordance and perturbation prediction. Model performance was strongly conditional: expression-trained cell-level transformers best resolved many cell-identity tasks, spatial and graph-aware models better preserved tissue architecture, and language-derived gene embeddings were competitive for selected perturbation-response metrics. No model dominated across tasks, and rankings shifted with modality, preprocessing, tokenisation, biological prior, domain shift and metric choice. This benchmark provides practical guidance for model selection and argues that future models should be judged by biological generalisation, interpretability and perturbation-grounded validity, not by scale or leaderboard performance alone.

## 2. SAGA: Synthetic Agentic Graph Architecture for Temporal Benchmark Generation

- Authors: Jiacheng Ding, Xiaofei Zhang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-19
- DOI: Unavailable
- Categories: cs.DB, cs.AI
- Relevance: 3.749480345236016
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.17288v1
- PDF: https://arxiv.org/pdf/2607.17288v1
- Local PDF: pdf/2026-07-22_02_SAGA_ Synthetic Agentic Graph Architecture for Temporal Benchmark Generation.pdf

High quality temporal graph benchmarks with rich semantics and ground-truth anomaly labels are essential for training graph neural networks, yet remain scarce due to privacy constraints and annotation costs. We present SAGA (Synthetic Agentic Graph Architecture), a system for generating large-scale, semantically rich temporal graphs via a four-phase pipeline. Our Skeleton-First, Semantics-Second architecture decouples structure from semantics: (S) an O(1)-per-edge skeleton generator produces power-law graphs; (A) a dispatcher partitions causally ordered time blocks for parallel execution; (G) LLM agents inject domain semantics using RAG-based rule bases across four domains; and (A) a state alignment engine resolves conflicts via temporal replay, yielding anomaly labels as natural byproducts. Unlike structural generators (e.g., LDBC SNB, Kronecker/R-MAT) or purely LLM-based approaches, SAGA achieves structural realism, semantic richness, and automatic anomaly labeling in a unified framework. On a single H100 GPU with vLLM batching, SAGA generates 500,000 temporal edges with controlled anomalies in under 90 minutes, scaling to 100,000 nodes while maintaining clustering coefficients above 0.99. The system supports real-time pipeline visualization, interactive multi-domain tuning (Finance/AML, Network/IDS, Cyber/APT, Transportation), and a CLI for large-scale GPU-based experiments.

## 3. Node4All: Learning Node Representation Beyond Datasets

- Authors: Dooho Lee, Jaemin Yoo
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-19
- DOI: Unavailable
- Categories: cs.LG, cs.SI
- Relevance: 3.7183639502509145
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.17272v1
- PDF: https://arxiv.org/pdf/2607.17272v1
- Local PDF: pdf/2026-07-22_03_Node4All_ Learning Node Representation Beyond Datasets.pdf

Node representation learning has advanced rapidly, yet most existing methods rely on per-dataset training and hyperparameter tuning. This dataset-specific optimization comes from the difficulty of designing reusable graph models that generalize across diverse graph datasets. In this work, we introduce Node4All, a node representation learner applicable to arbitrary graph datasets without any dataset-specific optimization.
  Node4All is built on two complementary ideas. At the architectural level, we introduce the Channel Graph Transformer (CGT), which enables a single fixed parameterization to process arbitrary graph datasets. At the learning level, we propose a self-supervised learning based on a series of synthetic graphs. Together, these components enable generalization beyond individual datasets, which is infeasible with existing architectures and learning frameworks. We extensively evaluate Node4All on node classification across 25 benchmarks against 21 baselines, covering both supervised and self-supervised methods. Despite all baselines being trained and optimized for each dataset, a single Node4All, applied uniformly across the datasets, achieves a competitive ranking of 5th among 21 baselines. Moreover, Node4All supports one-shot and in-context learning with an appropriate predictor and outperforms recent graph foundation models (GFMs) in these settings. These results demonstrate that Node4All not only achieves reusability across arbitrary graph datasets, but also remains an effective solution in practice. Code and model checkpoints are available in https://github.com/dooho00/node4all.

## 4. A Survey on GNN-based Link Prediction: Techniques, Applications, and Challenges

- Authors: Chengcheng Sun, Yajie Song, Cheng Zhai, Jiayun Tian, Jia Yang, Xiaobin Rui, Jian Zhang, Zhixiao Wang, Philip S. Yu
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-04-29
- DOI: 10.1002/widm.70093
- Categories: cs.AI, cs.LG, cs.SI
- Relevance: 3.6432899451871092
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.16198v1
- PDF: https://arxiv.org/pdf/2607.16198v1
- Local PDF: pdf/2026-07-22_04_A Survey on GNN-based Link Prediction_ Techniques, Applications, and Challenges.pdf

Graph Neural Networks (GNNs) have emerged as the leading paradigm for link prediction, enabling the inference of missing connections and the anticipation of potential future links. However, existing reviews lack systematic exploration specifically targeting underlying GNN architectures and diverse graph structures. To address this critical gap, this paper provides a comprehensive review of GNN-based link prediction from a novel and dedicated GNN perspective. We propose an innovative taxonomy that categorizes recent advancements based on techniques and applications. From a technique perspective, we focus on key GNN encoder architectures, including GCN-based, GAE-based, GAT-based, and GFormer-based methods, discussing their strengths and limitations. From an application perspective, we highlight prominent use cases of link prediction in knowledge graphs and recommendation systems, demonstrating their real-world impact. In addition, we examine the current challenges and discuss promising future directions.

## 5. Autonomous mechanistic discovery of colorectal cancer vulnerabilities via multi-scale AI swarms

- Authors: Christopher Baker, Tianyu Ren, Karen Rafferty, Hui Wang, Simon McDade
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-06-28
- DOI: Unavailable
- Categories: cs.LG, cs.AI
- Relevance: 3.4600053819979877
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.16262v1
- PDF: https://arxiv.org/pdf/2607.16262v1
- Local PDF: pdf/2026-07-22_05_Autonomous mechanistic discovery of colorectal cancer vulnerabilities via multi-scale AI swarms.pdf

The acceleration of automated scientific discovery has been fundamentally bottlenecked by the epistemic gap between the semantic reasoning of large language models (LLMs) and the deterministic physics of mammalian biology. While recent multi-agent frameworks have achieved autonomous hypothesis generation and in vitro experimental analysis, they lack the mathematically grounded, causal constraints required for multi-scale clinical translation. Furthermore, while algorithmic clinical digital twins successfully forecast biological states, they rely on black-box latent spaces, sacrificing mechanistic interpretability for predictive accuracy. Here, we introduce the Multi-Scale Autonomous Discovery Engine (Octopus), a neuro-symbolic architecture that unites zero-leakage, local LLM swarms with strict algorithmic physics engines. Rather than stopping at isolated cellular assays, the system autonomously generated therapeutic hypotheses against in vitro CRISPR dependency data (CCLE), traced dynamic causal cascades using mechanistic interpretability (XGBoost SHAP vectors), and orthogonally translated the emergent vulnerabilities in silico to predict in vivo mammalian tumor trajectory (PDX) and human overall survival (Marisa). In a fully unsupervised sweep of colorectal cancer transcriptomes, the pipeline autonomously identified Insulin-like Growth Factor 2 (IGF2) as a strictly bounded vulnerability to 5-Fluorouracil resistance. The discovery maintained significance after rigorous Benjamini-Hochberg false discovery rate correction (q=0.0292, Log-Rank p=0.0007 ) and successfully predicted significant in vivo tumor volume shrinkage in an independent mouse cohort (Mann-Whitney p=0.0373). By bridging the chasm between multi-agent reasoning and mathematically bounded clinical survival, this framework establishes a verifiable, zero-leakage paradigm for automated, end-to-end biomedical discovery.

## 6. TVGL-CFM:Generating and Forecasting Time-Varying Trajectories of Dynamic Networks with Conditional Flow Matching

- Authors: Om Roy, Yashar Moshfeghi, Keith Malcolm Smith
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-18
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.4551168274500683
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.16894v1
- PDF: https://arxiv.org/pdf/2607.16894v1
- Local PDF: pdf/2026-07-22_06_TVGL-CFM_Generating and Forecasting Time-Varying Trajectories of Dynamic Networks with Conditional Flow Matching.pdf

Many complex systems such as brain networks, financial markets, and gene-regulatory circuits are described not by a fixed graph but by one that changes over time. A standard way to summarise such structure at each instant is the sparse precision (inverse-covariance) matrix, and the time-varying graphical lasso (TVGL) turns a multivariate signal into a smooth chain of these matrices. We introduce TVGL-CFM, a single model that learns the distribution of such chains and can both generate new, realistic time-varying network trajectories for a given class and forecast how an observed trajectory will continue. Each precision matrix lives on a curved space of positive-definite matrices, but a log-Euclidean chart flattens an entire trajectory into an ordinary vector space, so a simple conditional flow-matching model can be trained and sampled there while every decoded matrix is guaranteed to be a valid precision matrix. For forecasting we start the flow not from noise but from a rough extrapolation of the recent history, so the model only has to learn a small correction. Across EEG motor-imagery, chaotic systems, and gene-expression data, TVGL-CFM generates trajectories that keep the class-discriminative structure of real data, and it forecasts future connectivity more accurately than raw-signal baselines. Generating the structured precision trajectory directly is therefore more faithful than generating raw signals and estimating connectivity afterwards.

## 7. A Weisfeiler-Leman Characterization of Global-Attention Graph Transformers for Mixed-Integer Linear Programs

- Authors: Md Abrar Jahin, Craig A. Knoblock, Jay Pujara
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-20
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.4468974669643466
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.17570v1
- PDF: https://arxiv.org/pdf/2607.17570v1
- Local PDF: pdf/2026-07-22_07_A Weisfeiler-Leman Characterization of Global-Attention Graph Transformers for Mixed-Integer Linear Programs.pdf

Graph foundation models (GFMs) with global attention are increasingly used to represent mixed-integer linear programs (MILPs), aiming to capture structure beyond the locality of standard graph neural networks. We study their expressive power through graph isomorphism testing, asking which MILP instances they map to identical representations. We prove that a broad class of hierarchical graph transformers combining global linear attention, edge-weighted cross-attention, and bipartite message passing is bounded by the one-dimensional Weisfeiler-Leman (1-WL) test: under any parameter setting, 1-WL-equivalent MILP graphs receive identical graph embeddings. Our compositional proof shows that each architectural component is a symmetric multiset function and thus preserves 1-WL equivalence. We validate this characterization across ten diverse graph encoders, including Graphormer-, GraphGPS-, Set-Transformer-, and Gasse-style models. Across model capacities, graph scales, and pooling operators, every tested encoder maps 1-WL-equivalent non-isomorphic graph pairs to numerically identical embeddings. Consequently, graph invariants that vary within a 1-WL equivalence class cannot be recovered from these representations. We further show that expressiveness beyond 1-WL arises from input encoding rather than attention: random-walk positional encodings separate the constructed pairs, while additional constructions expose the limits of this remedy. These results characterize the expressive power of global-attention GFMs and provide an encoder-agnostic diagnostic for detecting 1-WL-induced representation equivalence.

## 8. GeneSpeak-FP: Target and Compound Retrieval from Observed Cell-Level Perturbation Signatures

- Authors: Kseniia Vaniushkina, Jeongmin Lim, Jinyong Park
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-20
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.4235465046088565
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.17671v1
- PDF: https://arxiv.org/pdf/2607.17671v1
- Local PDF: pdf/2026-07-22_08_GeneSpeak-FP_ Target and Compound Retrieval from Observed Cell-Level Perturbation Signatures.pdf

Large-scale single-cell perturbation atlases make it possible to ask an inverse question: given an observed transcriptional response, which annotated targets and compounds in a fixed library are most consistent with that response? We present \model, a Transformer retrieval model for this closed-library setting. Each input is a cell-level perturbation signature formed by contrasting one treated cell with a cell-line-specific mean DMSO reference. The encoder maps the signature to a target-retrieval vector and a molecular-embedding vector, trained jointly with supervised target losses and structure--transcriptome alignment. We evaluate on Tahoe-100M conditions with mapped target annotations using a within-compound stratified 90/10 condition-pair split of 10,505 training and 1,168 validation drug--cell-line pairs. Because compounds and cell lines can occur in both partitions, the experiment measures held-out condition-pair retrieval rather than generalization to unseen compounds or cellular contexts. In a Monte Carlo evaluation over 38,400 sampled validation cells, \model\ achieved target Recall@10 of 0.408 and Recall@20 of 0.544, together with compound Hit@1 of 0.129, Hit@10 of 0.343, and mean reciprocal rank of 0.205 over a 379-compound bank. A separate diagnostic evaluation produced nearly identical values for the main model and large gains over a random-vector control and post-hoc bag-of-genes controls. These results demonstrate that a single multi-task model can recover both mapped target annotations and recorded compound identities from observed cell-level responses in the evaluated Tahoe-100M closed-library setting. Generalization to unseen compounds and cellular contexts remains to be established.

## 9. scTIDE: Deciphering Critical Transitions Through Cell‐Perturbed Manifold Graphs and Optimal Transport Conditional Flow Matching

- Authors: Jiayuan Zhong, Bowen Niu, Yongbo Yu, Shiyang Nie, Xuerong Gu, Pei Chen, Rui Liu
- Source: openalex
- Venue type: journal
- Journal: Advanced Science
- Publication status: published
- Publication date: 2026-07-20
- DOI: https://doi.org/10.1002/advs.76606
- Categories: Single-cell and spatial transcriptomics, Topological and Geometric Data Analysis, Gene Regulatory Network Analysis
- Relevance: 3.353653447150645
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://doi.org/10.1002/advs.76606
- PDF: Unavailable
- Local PDF: Not downloaded

A tipping point marks the threshold or critical state where a biological system shifts from one stable state to another. Deciphering critical transitions and their associated signaling molecules is essential for elucidating complex biological processes and for enabling timely interventions to avert or postpone catastrophic deteriorations. However, existing critical-state detection methods rely mainly on Euclidean-space statistics, which may overlook nonlinear dynamical behavior among molecules and distribution-based molecular patterns, leading to limited robustness and performance in high-dimensional, sparse, and noisy single-cell data. In this study, we introduce single-cell Tipping-point Identification via Distributional Embedding (scTIDE), a framework that integrates manifold-based graph representations with optimal-transport conditional flow matching (OT-CFM) to capture intrinsic topological structure and identify critical transitions at the individual-cell level. Specifically, for a given cell, scTIDE quantifies distributional differences between a distribution derived from the reference manifold graph and a perturbed distribution inferred from the cell-perturbed manifold graph using OT-CFM, thereby identifying critical stages and key signaling molecules. The reliability and effectiveness of our model are demonstrated through synthetic models and eight distinct single-cell datasets, where it outperforms existing methods. Moreover, scTIDE reveals possible critical transitions for unseen cells and visualizes the intricate biological progression.

## 10. Enhancing Super‐Resolution Spatial Transcriptomics Data by Transfer Learning

- Authors: Xiaoyu Li, Lihua Zhang, Wenwen Min
- Source: openalex
- Venue type: journal
- Journal: Advanced Science
- Publication status: published
- Publication date: 2026-07-20
- DOI: https://doi.org/10.1002/advs.76601
- Categories: Single-cell and spatial transcriptomics, Cell Image Analysis Techniques, Domain Adaptation and Few-Shot Learning
- Relevance: 3.336040215616123
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://doi.org/10.1002/advs.76601
- PDF: Unavailable
- Local PDF: Not downloaded

High-definition spatial transcriptomics (ST) technologies such as Visium HD enable subcellular tissue characterization but remain constrained by their limited accessibility due to high costs and technical complexity. Existing super-resolution methods predominantly rely on an image-guided paradigm, premised on the assumption that gene expression strictly mirrors histological morphology. However, this assumption breaks down for genes with complex spatial distributions lacking distinct visual correlates, often leading to biological artifacts. To address this, we introduce SpotZoomer, a framework that formulates resolution enhancement as a knowledge transfer problem via generative domain adaptation. It leverages public high-definition ST data as a "teacher" to learn intrinsic spatial expression priors, which are then transferred to coarse spot data to reconstruct high-fidelity gene profiles that capture molecular details beyond the reach of morphological guidance alone. Extensive benchmarking across 19 datasets demonstrates the substantial value of the reference-based paradigm implemented by SpotZoomer over the reference-free image-only paradigm, achieving improved reconstruction accuracy and biological fidelity while complementing rather than displacing reference-free methods in settings where high-resolution priors are unavailable. SpotZoomer thus provides a scalable, data-driven strategy for upgrading standard ST resources to subcellular resolution.

## 11. Think, Plan, Paint: Layout-Aware Reasoning for Controllable Image Generation in Unified Models

- Authors: Junhao Liu, Jian-Wei Zhang, Tao Huang, Miles Yang, Zhao Zhong, Liefeng Bo
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-17
- DOI: Unavailable
- Categories: cs.CV, cs.AI, cs.LG
- Relevance: 3.2977314386282286
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.16409v1
- PDF: https://arxiv.org/pdf/2607.16409v1
- Local PDF: pdf/2026-07-22_11_Think, Plan, Paint_ Layout-Aware Reasoning for Controllable Image Generation in Unified Models.pdf

Unified Multimodal Large Language Models (MLLMs) offer a promising paradigm for unifying visual understanding and generation, yet they still struggle to follow complex spatial instructions and logical constraints in controllable image generation. To address this gap, we present ATLAS, a unified framework that equips MLLMs with a human-like "Think, Plan, and Paint" paradigm. We adopt layout as the shared representation that connects the three stages, enabling the model to reason about spatial requirements, plan explicit object arrangements, and render the final image. We further improve plan-to-image fidelity with reinforcement-learning-based layout alignment. We instantiate ATLAS at 7B and 80B scales, achieving state-of-the-art performance among MLLMs on image generation benchmarks and an average 65.31% improvement over existing layout-based unified MLLMs. On spatially related tasks, ATLAS obtains an average 23.06% gain over the base models. Through the same layout interface, ATLAS also supports instruction-guided editing and multimodal grounding. We further introduce ATLAS-Reasoning, a benchmark for evaluating generation under complex spatial instructions.

## 12. An automated platform for spatial functional modeling and fingerprint analysis of tissue molecular landscapes

- Authors: Hajihosseini, M., Patino-Martinez, E., Ghosal, R., Kaplan, M. J., Pyne, S.
- Source: biorxiv
- Venue type: preprint
- Journal: biorxiv
- Publication status: preprint
- Publication date: 2026-07-21
- DOI: 10.64898/2026.07.15.738836
- Categories: bioinformatics
- Relevance: 3.2643717364791174
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://www.biorxiv.org/content/10.64898/2026.07.15.738836v1.full.pdf
- PDF: https://www.biorxiv.org/content/10.64898/2026.07.15.738836v1.full.pdf
- Local PDF: pdf/2026-07-22_12_An automated platform for spatial functional modeling and fingerprint analysis of tissue molecular landscapes.pdf

Spatial transcriptomics (ST) enables high resolution molecular profiling while preserving tissue architecture, creating new opportunities to investigate how disease-associated pathways are organized within tissues. However, existing analytical approaches largely focus on individual pathways or cell types and do not provide a unified framework for modeling spatially varying pathway interactions across tissue sections and anatomical planes. Here, we present an integrative framework, Spatial Fingerprints Analytics (SFinx), that combines reference-free deconvolution, pathway activity reconstruction, and Spatial Functional Data Analysis (SFDA) to map localized pathway activity and pathway phenotype interactions in complex tissues. Applying SFinx to10x Visium ST datasets from murine lupus nephritis, we reconstructed continuous spatial landscapes of pathway activity and disease-associated phenotypes across kidney sections. This approach identified anatomically restricted inflammatory domains characterized by coordinated activation of immune pathways and revealed substantial spatial heterogeneity in pathway crosstalk across renal compartments. Using generalized additive models with tensor-product splines, we quantified spatially varying associations between lupus nephritis and neutrophil activation pathways across tissue sections, uncovering regions with both positive and negative relationships that would be obscured by conventional bulk analyses. Multi-slice integration further demonstrated reproducible spatial interaction patterns while accounting for section-specific variability. Together, SFinx transforms mixed-spot transcriptomic measurements into interpretable spatial pathway landscapes and interaction maps, providing a general framework for identifying localized disease mechanisms. This approach reveals previously unrecognized spatial organization of inflammatory signaling in lupus nephritis and presents a broadly applicable strategy for studying spatially coordinated biological processes in autoimmune disorders, cancer, and neurodegenerative diseases.

## 13. Retrieval is Enough: Training-Free Interpretability with a Tool-Using Agent

- Authors: Sriram Balasubramanian, Soheil Feizi
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-17
- DOI: Unavailable
- Categories: cs.LG, cs.AI
- Relevance: 3.209073670315799
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.16448v1
- PDF: https://arxiv.org/pdf/2607.16448v1
- Local PDF: pdf/2026-07-22_13_Retrieval is Enough_ Training-Free Interpretability with a Tool-Using Agent.pdf

Interpretability methods for neural network activations span a wide cost spectrum, from cheap, training-free techniques (such as linear probes, PCA, SVD) to more expensive training-based ones (such as SAEs and activation oracles). Training-based methods are typically more powerful, in part because they leverage large activation datasets during training. This raises a natural question - do they actually surface insights that go beyond what is recoverable from the training dataset itself? To address this, we equip an LLM agent with a vector database of activations paired with their textual contexts, along with tools for manipulating activations - projecting out directions in latent space, computing activation differences and averages. The agent iteratively queries the database, forms hypotheses from the retrieved samples, and validates them by constructing linear probes. We call this method HARP, for Hypothesis-driven Agentic Retrieval and Probing. Despite not involving any training, HARP outperforms both activation oracles and SAE-based agents on concept discovery, concept detection, model steering, and secret elicitation. The training-free design also makes HARP substantially cheaper and more flexible: new datasets can be indexed on demand whenever existing ones prove insufficient. More broadly, our results suggest that current training-based methods do not yet extract insights beyond their training data, and motivate benchmarks that explicitly require interpretability methods to demonstrate such insights. We release our code at https://github.com/SriramB-98/HARP

## 14. Learning Spatio-Temporal Foundation Models from Pure Synthetic Data

- Authors: Yutong Feng, Shiyuan Piao, Yutong Xia, Xu Liu, Wenqi Fan, Fugee Tsung, See-Kiong Ng, Yuxuan Liang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-06-27
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.186309943040435
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.16251v1
- PDF: https://arxiv.org/pdf/2607.16251v1
- Local PDF: pdf/2026-07-22_14_Learning Spatio-Temporal Foundation Models from Pure Synthetic Data.pdf

Spatio-Temporal Foundation Models (STFMs) aim to learn generalizable representations of complex dynamical systems across space and time. However, existing approaches suffer from distributional bias in real-world pre-training data, structural bottlenecks of autoregressive or diffusion-based paradigms, and objectives that overemphasize point-wise reconstruction in noisy observation space.We propose \textbf{NeoST}, the first spatio-temporal foundation model pre-trained solely on procedurally generated synthetic systems. NeoST introduces a scalable synthetic pre-training corpus to mitigate real-world bias, a latent-space reasoning architecture that generates and iteratively refines multiple future trajectories without sequential error accumulation, and latent-space objectives that emphasize structural dynamics and enable inference-time correction under distribution shifts.Extensive experiments across diverse real-world benchmarks show that NeoST consistently outperforms existing STFMs in diverse real-world spatio-temporal systems, achieves superior long-horizon stability and inference efficiency.

## 15. BrainNext: A General-Purpose Self-Supervised Foundation Model for Brain MRI Analysis

- Authors: Moona Mazher, Abdul Qayyum, Steven A. Niederer, Daniel C. Alexander
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-20
- DOI: Unavailable
- Categories: cs.CV, cs.AI
- Relevance: 3.1072129729601023
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.17782v1
- PDF: https://arxiv.org/pdf/2607.17782v1
- Local PDF: pdf/2026-07-22_15_BrainNext_ A General-Purpose Self-Supervised Foundation Model for Brain MRI Analysis.pdf

Foundation models pretrained using self-supervised learning have transformed computer vision by learning transferable representations from large-scale unlabeled data. However, existing foundation models for neuroimaging remain limited by task-specific training, slice-based learning strategies, or relatively small pretraining datasets, restricting their generalizability across diverse brain MRI applications. In this work, we present BrainNext, a general-purpose self-supervised foundation model for volumetric brain MRI analysis. BrainNext combines masked autoencoder (MAE) pretraining with a native three-dimensional Bi-Directional xLSTM-UNet architecture to learn rich anatomical representations from 60,551 unlabeled brain MRI examinations spanning multiple MRI modalities. The pretrained model is subsequently adapted to downstream tasks through lightweight task-specific fine-tuning. We evaluate BrainNext on the Foundation Models for Medical Imaging (FOMO) 2025 Method Track, encompassing classification, segmentation, and brain-age estimation, where it achieved second place overall and ranked first in the meningioma segmentation task on the official FOMO 2025 challenge leaderboard, demonstrating strong transferability across heterogeneous neuroimaging tasks. These results highlight the potential of large-scale self-supervised pretraining to learn robust and transferable volumetric representations, establishing BrainNext as a scalable foundation model for diverse brain MRI applications.

## 16. Program Synthesis for Simulation-Based Inference: Joint Model Selection and Parameter Estimation

- Authors: Siddharth Mishra-Sharma
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-20
- DOI: Unavailable
- Categories: cs.LG, stat.ML
- Relevance: 3.0640609196622624
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.17540v1
- PDF: https://arxiv.org/pdf/2607.17540v1
- Local PDF: pdf/2026-07-22_16_Program Synthesis for Simulation-Based Inference_ Joint Model Selection and Parameter Estimation.pdf

Neural simulation-based inference enables parameter estimation for complex models, but typically requires the user to specify a simulator encoding a fixed model structure. We present a framework for joint model selection and parameter estimation that combines large language models for program synthesis with neural simulation-based inference. Given a natural language description of the system and data under investigation, an LLM proposes candidate simulator programs which are iteratively refined via feedback-driven mutation and evaluated using neural density estimation. The approach enables simulation-based inference over a pool of models, not just parameters within a fixed model. On benchmarks spanning deterministic dynamics, stochastic epidemic models, and dark matter substructure inference from gravitational-lensing images, the method identifies plausible model families from open-ended prompts, with accuracy that reflects the information content of the data and identifiability of candidate models.

## 17. Accurate and Efficient Long-Term Memory for LLM Agents

- Authors: Zicheng Zhao, Xinyang Guo, Luyao Lv, Menghan Wang, Ming Li, Shuaicheng Li
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-05-15
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 3.0599654630037953
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.16211v1
- PDF: https://arxiv.org/pdf/2607.16211v1
- Local PDF: pdf/2026-07-22_17_Accurate and Efficient Long-Term Memory for LLM Agents.pdf

LLM agents augmented with persistent memory can recall past interactions, but existing systems suffer from two limitations: flat, unstructured storage loses relational context needed for multi-hop and temporal reasoning, and reliance on expensive LLM-based classification makes them impractical for latency-sensitive deployment. Without mechanisms to validate new information against stored knowledge, these systems silently accumulate contradictions. We present MOSAIC (Memory-Organized Structured Agent for Information Collection), a structured, conflict-aware long-term memory framework for LLM agents that is substantially more accurate and efficient. MOSAIC introduces three key capabilities: (1) entity-typed graph storage with semantic classification preserving relational structure across events, personas, and relationships, enabling multi-hop and temporal reasoning over conversation history; (2) hash-accelerated dual-path retrieval replacing LLM-based classification with locality-sensitive hashing, achieving near-instantaneous lookup with negligible accuracy loss; and (3) active conflict detection at save time that cross-references new information against existing graph neighbors, triggering updates or deletions for contradictory entries. Evaluated on LoCoMo (long-conversation QA), HaluMem, and a novel clinical-guideline error compounding test, MOSAIC achieves 89.35% accuracy on LoCoMo (+27.21 pp over the best baseline), best HaluMem-Medium extraction F1(86.77%) and HaluMem-Long extraction F1 (85.84%), best QA correctness on both Medium and Long (73.10%, 70.75%), and detects 66% of injected factual conflicts-4.7 times higher than the best baseline (14%)-while hash-accelerated retrieval keeps average search latency at 0.58 s per question.

## 18. GigaPath-Flash and GigaTIME-Flash: Efficient Pathology Foundation Models for Whole-Slide and Tumor Microenvironment Analysis

- Authors: Naoto Usuyama, Jeya Maria Jose Valanarasu, Sicong Yao, Hanwen Xu, Jaspreet Bagga, Guanghui Qin, Robert E. Kramer, Cliff Wong, Soohee Lee, Hao Qiu, Theodore Zhengde Zhao, Racheli Ben Shimol, Angela Crabtree, Kevin Matlock, Eduardo Alejandro Lozano Garcia, Naiteek Sangani, Alberto Santamaria-Pang, Jason Entenmann, Alexandra Q. Bartlett, Bill J. Wright, Bernard A. Fox, Brian Piening, Sheng Zhang, Sheng Wang, Tristan Naumann, Carlo Bifulco, Hoifung Poon
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-20
- DOI: Unavailable
- Categories: cs.CV, cs.AI
- Relevance: 3.0429795485575784
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.18218v1
- PDF: https://arxiv.org/pdf/2607.18218v1
- Local PDF: pdf/2026-07-22_18_GigaPath-Flash and GigaTIME-Flash_ Efficient Pathology Foundation Models for Whole-Slide and Tumor Microenvironment Anal.pdf

Foundation models have emerged as a driving force in computational pathology, with the potential to transform cancer diagnosis, prognosis, and treatment selection by learning transferable representations from large-scale histopathology data. A growing landscape of pathology foundation models now spans diverse data sources, architectures, and downstream applications. However, most pretrained models operate only at the image-tile level, use restrictive licenses, and remain computationally expensive, limiting large-scale slide-level clinical and research use.
  Here, we introduce GigaPath-Flash and GigaTIME-Flash, efficient models for whole-slide pathology AI and spatial proteomics prediction. GigaPath-Flash combines a 22M-parameter ViT-S tile encoder with a 21M-parameter LongNet slide encoder, both pretrained on large-scale real-world histopathology data. Its compact tile encoder is distilled from the billion-parameter GigaPath (ViT-g) teacher and shared by both models. GigaPath-Flash retains 97% of GigaPath's average slide-level performance with 50x less compute. GigaTIME-Flash extends this backbone to predict the tumor immune microenvironment directly from routine H&E images. It surpasses the original CNN-based GigaTIME in prediction quality while running 6x faster and using 8x less GPU memory.
  Together with GigaPath and GigaTIME, these models form an open-weight, Apache-2.0-licensed family pretrained on large-scale real-world clinical data. By releasing all models and weights, we provide accessible building blocks for computational pathology, immuno-oncology, and precision health.

## 19. Natural Language Access to Domain-Specific Metadata: A Reusable Framework for LLM Query Generation

- Authors: Blake G. Fitch, Cato Elia Kurtz
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-20
- DOI: Unavailable
- Categories: cs.DB, cs.AI
- Relevance: 3.04255529851035
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.18029v1
- PDF: https://arxiv.org/pdf/2607.18029v1
- Local PDF: pdf/2026-07-22_19_Natural Language Access to Domain-Specific Metadata_ A Reusable Framework for LLM Query Generation.pdf

Researchers need to answer ad-hoc questions about the contents of domain-specific archives but often lack the expertise to write structured queries on the metadata. We show that when domain vocabulary and semantics are captured in a well-designed Web Ontology Language (OWL) ontology, Large Language Models (LLMs) can generate accurate structured queries zero-shot, without fine-tuning, retrieval augmentation, or multi-agent orchestration. We present the Natural Language Knowledge Graph Query (NLKGQ) system, a framework and development process that enables natural language access to metadata in such archives. The framework includes a web interface that helps researchers pose natural language questions, which a domain-agnostic harness translates to SPARQL via an LLM and executes against a knowledge graph. The development process begins with capturing domain vocabulary and semantics in a formal OWL ontology. Domain-specific code then extracts metadata from archive sources and imports it into a knowledge graph defined by the ontology. Both are designed for reuse across domains. We demonstrate the system on metadata derived from a large-scale neuroimaging research archive, evaluating multiple LLMs and ontology representations. The best configurations achieve 100% accuracy on a competence and regression question set developed with domain experts. An ablation study across eight ontology representations reveals that readable entity names and semantic annotations are the dominant factors in accuracy, more significant than model choice or prompt engineering. We also compare SPARQL to an auto-generated SQL database as query backends, showing that OWL's structural features provide a substantial advantage over SQL DDL for LLM-driven query generation. Our demonstration domain also requires local LLMs on modest institutional hardware to address privacy concerns for human subject data.

## 20. Topological Signatures of Context-Level Reliability in TabPFN

- Authors: James Hu, Mahdi Ghelichi
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-20
- DOI: Unavailable
- Categories: cs.LG, cs.AI, stat.ML
- Relevance: 3.0383888859685158
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.17962v1
- PDF: https://arxiv.org/pdf/2607.17962v1
- Local PDF: pdf/2026-07-22_20_Topological Signatures of Context-Level Reliability in TabPFN.pdf

TabPFN is a transformer-based foundation model for tabular prediction that performs inference without task-specific training by conditioning on a support set and query inputs. Despite its strong empirical performance, its internal behavior on structurally difficult tabular geometries remains poorly understood. We study this behavior using zigzag persistent homology, treating TabPFN layer representations as evolving point clouds. We construct a controlled benchmark of synthetic tabular tasks with known true probabilities and varied intrinsic topology, including warped circles, tori, spheres, Hopf links, trefoil knots, and Swiss rolls. Across these tasks, we find that the topology of TabPFN's internal representation geometry is strongly associated with dataset-level reliability; for example, the zeroth homology group $H_0$ fragmentation count correlates positively with mean absolute residual across controlled tasks, and this association strengthens in a high-resolution warped circle case study at large sample size. Harder geometries induce a dual topological signature: increased $H_1$ loop activity and increased $H_0$ fragmentation, while the $H_1$ persistence becomes shorter-lived. These descriptors correlate with Bayes error, mean absolute residuals, and overconfidence. Our results suggest that zigzag persistence diagnoses the reliability of the inferred in-context task geometry and provides a context-level view of when TabPFN operates in topologically stressed regimes.

## 21. Semi-Supervised Conditional Diffusion via Label Augmentation

- Authors: Jin Su, Yuan Gao, Yong Zhou, Jian Huang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-18
- DOI: Unavailable
- Categories: stat.ML, cs.LG
- Relevance: 3.0133694672377356
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.16685v1
- PDF: https://arxiv.org/pdf/2607.16685v1
- Local PDF: pdf/2026-07-22_21_Semi-Supervised Conditional Diffusion via Label Augmentation.pdf

Conditional diffusion models have become a powerful and flexible framework for learning complex conditional distributions from labeled data. In practice, however, acquiring high-quality labels is costly and time-consuming, leaving large volumes of unlabeled data unused. To address this, we introduce label-augmented conditional diffusion (LACD), a simple and effective approach that incorporates unlabeled examples by assigning them a designated trivial label and performing joint denoising score matching over the augmented dataset. We provide sufficient conditions guaranteeing population-level identifiability of the target conditional distribution under this scheme. Moreover, we establish rigorous statistical guarantees: when sufficiently many unlabeled samples are available, the sampling distribution produced by LACD converges strictly faster than the purely supervised estimator in total variation distance, and at least as fast in Wasserstein-1 distance. Extensive experiments on synthetic, image, and tabular benchmarks corroborate our theory and show substantial gains in sample efficiency and generative performance compared with the purely supervised estimator.

## 22. ProtSyntax: a protein large language model for decoding post-translational modification syntax and function

- Authors: Lin, Y.
- Source: biorxiv
- Venue type: preprint
- Journal: biorxiv
- Publication status: preprint
- Publication date: 2026-07-21
- DOI: 10.64898/2026.07.18.739331
- Categories: bioinformatics
- Relevance: 2.998359552134392
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://www.biorxiv.org/content/10.64898/2026.07.18.739331v1.full.pdf
- PDF: https://www.biorxiv.org/content/10.64898/2026.07.18.739331v1.full.pdf
- Local PDF: pdf/2026-07-22_22_ProtSyntax_ a protein large language model for decoding post-translational modification syntax and function.pdf

Post-translational modifications (PTMs) regulate protein function through dependencies among residue chemistry, sequence context, three-dimensional microenvironments and modification states, yet most predictors model sites independently and do not connect modification propensity to functional consequences. Here we present ProtSyntax, a PTM-centered protein language model trained on 4.25 million examples spanning 40 PTM classes and supervised for kinase specificity, PTM crosstalk and enzyme kinetics. ProtSyntax integrates bidirectional long-range modeling with geometry-gated attention in a sparse mixture-of-experts architecture and uses adaptive multi-objective learning to couple residue-level PTM syntax to protein-level function. Across 40 PTM-site benchmarks, ProtSyntax improved mean MCC and AP by 12.7% and 10.7%, respectively, relative to the best-performing baselines. It also distinguished authentic sites from structurally incompatible motif decoys, transferred to rare PTMs, recovered crosstalk, linked PTM perturbations to enzyme-kinetic changes and identified disease-associated PTM disruptions. Together, ProtSyntax provides an interpretable framework for decoding PTM regulation across the proteome.

## 23. The Geometry of Semantic Space: A Continuous Geometric Framework for the Transformer Architecture

- Authors: Zhihua Liang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-19
- DOI: Unavailable
- Categories: cond-mat.dis-nn, cs.CL, cs.LG
- Relevance: 2.9866354193373157
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.17146v1
- PDF: https://arxiv.org/pdf/2607.17146v1
- Local PDF: pdf/2026-07-22_23_The Geometry of Semantic Space_ A Continuous Geometric Framework for the Transformer Architecture.pdf

We present a continuous geometric framework that models the discrete algebraic operations of the Transformer architecture as an integro-differential equation (IDE) on a semantic fiber bundle $\calE = \calM \times \R^d$. Beginning from a single geometric axiom -- that the token sequence forms a discrete $1$-manifold equipped with a canonical measure lattice -- we translate every core component of the modern Transformer (RMSNorm, RoPE, Softmax Attention, FFN, Residual Stream, SGD, Weight Decay) into a cohesive vocabulary of differential geometry, measure theory, and stochastic calculus. The resulting framework yields quantitative predictions spanning entropic optimal transport (Attention as a Schrödinger bridge) and non-equilibrium thermodynamics (SGD as Itô diffusion violating detailed balance). We conduct a six-part experimental campaign across five architectures (Qwen3, LLaMA\nobreakdash-3.1, Gemma\nobreakdash-3, GPT-2, Mistral) spanning $124$M to $8$B parameters. The empirical observables are quantitatively consistent with the geometric predictions: the $ε^{-1/2}$ Lipschitz scaling calibration at machine precision ($R^2 = 1.000$), the Lie--Trotter operator-splitting torsion, the symmetric ablation instability confirming the Dual-Law of Topological Stability, the $\calO(1/\sqrt{k})$ thermodynamic suppression of Poincaré recurrence on the RoPE torus, the thermodynamic context-limit phase transition, and the Non-Equilibrium Steady State parameter vortex -- verified across two optimizers (AdamW and Pure SGD) to exclude momentum artifacts. The results demonstrate that analyzing Transformers through the lens of continuous stochastic differential geometry provides a predictive descriptive vocabulary for the stability limits, context bounds, and optimization dynamics of Large Language Models.

## 24. An Explicit World Model Based on Data-First Ontology: DaoQL Multimodal Storage Validation and Counterfactual Reasoning Evaluation

- Authors: Zhanbo Li, Shifeng Wu, Xiangjin Meng, Wenjie Cai
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-19
- DOI: Unavailable
- Categories: cs.AI, cs.DB
- Relevance: 2.969718760531352
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.17269v1
- PDF: https://arxiv.org/pdf/2607.17269v1
- Local PDF: pdf/2026-07-22_24_An Explicit World Model Based on Data-First Ontology_ DaoQL Multimodal Storage Validation and Counterfactual Reasoning E.pdf

Large language models encode world models implicitly in neural weights, which exposes four structural risks in high-precision domains such as medicine and finance: hallucination, frozen knowledge, poor explainability, and poor modifiability. This paper proposes data-first ontology: LLMs are treated as reasoning and language engines, while deterministic knowledge is moved into an explicit multimodal database, DaoQL. We formalize an explicit world model and show that, under rule independence, deterministic evaluation, and fixed conflict resolution, explicit models provide a sufficient condition for composable counterfactual decomposability; implicit models lack atomic read/delta semantics and therefore provide no comparable architectural guarantee. The implemented system focuses on DaoQL's verified storage layer and explicit Eval path, integrating graph, column, vector, and full-text engines within one process. KVCache graph nodes, expert hot updates, and the DaoQL-Agent runtime remain future work. On an embedded same-machine setup, DaoQL reports graph BFS at 1.20 ms, HNSW at 83.1 us, and a Fluent hybrid query at 105.8 us; these results indicate engineering potential but must be interpreted with deployment-shape differences from client-server systems. Exploratory measurements on LDBC SNB SF1 and ANN-Benchmarks further show 34/34 query coverage with interactive-class queries mostly in the sub-millisecond to millisecond range, but only 1.8 QPS overall due to long-tail BI/IC queries; ANN-Benchmarks reaches Recall@10 >= 99% at thousand-level QPS after a bridge-edge protection fix. In a five-domain counterfactual experiment (n = 1250), DaoQL+GPT-4o achieves 94% composable counterfactual decomposability, 49 percentage points above GPT-4o alone. The paper explicitly separates provable structure, preliminary empirical evidence, and architectural roadmap claims.

## 25. CoCurve: Cross-Module Co-Pruning Curvature for Training-Free Structured LLM Pruning

- Authors: Zhiren Gong, Zihao Zeng, Zijie Wang, Tiantong Wang, Chau Yuen, Wei Yang Bryan Lim
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-20
- DOI: Unavailable
- Categories: cs.LG, cs.AI
- Relevance: 2.967954672360193
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.17568v1
- PDF: https://arxiv.org/pdf/2607.17568v1
- Local PDF: pdf/2026-07-22_25_CoCurve_ Cross-Module Co-Pruning Curvature for Training-Free Structured LLM Pruning.pdf

Structured pruning compresses large language models (LLMs) by removing whole computational units, such as attention heads and feed-forward (FFN) channel groups. Most training-free methods, however, rank these units independently, implicitly treating the loss from pruning a set as the sum of its individual losses. This view fails for Transformers, whose sublayers are coupled through a shared residual stream. Two individually weak units can thus be jointly indispensable, yet independent scoring is blind to such dependence and removes them together. We introduce CoCurve (Cross-Module Co-Pruning Curvature), a calibration-only, fine-tuning-free method that prunes attention and FFN units jointly. A second-order Taylor expansion of the token-level KL between the frozen model and its masked copy yields a single Fisher matrix whose diagonal is classical node saliency and whose off-diagonal entries are co-pruning curvature edges: the extra damage of removing two units together. Under a single-ablation additivity approximation this matrix reduces to a Gram product of single-unit ablation features, so the full M x M interaction is recovered from M forward passes, with no pairwise sweeps or gradients. Pruning then reduces to one budgeted quadratic program, solved in a single shot under a shared attention--FFN budget, with no labels, fine-tuning, or recovery.

## 26. ST-Veto: Spatio-Temporal Token Veto for Diffusion MLLMs via Taylor Prediction and Visual Grounding

- Authors: Keuntae Kim, Beomseok Lee, Hyunwoo Kim, Yong Suk Choi
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-20
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 2.965529609261796
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.17884v1
- PDF: https://arxiv.org/pdf/2607.17884v1
- Local PDF: pdf/2026-07-22_26_ST-Veto_ Spatio-Temporal Token Veto for Diffusion MLLMs via Taylor Prediction and Visual Grounding.pdf

Vision Language Models (VLMs) achieve strong reasoning with Chain-of-Thought (CoT) prompting but incur high sequential-generation cost, error accumulation, and limited self-correction. Diffusion Multimodal Large Language Models (dMLLMs) unmask tokens in an order-agnostic process, improving efficiency and enabling iterative refinement, yet their reasoning and how to enhance it remain underexplored. We propose a training-free method, Spatio-Temporal Token Veto (ST-Veto), which leverages the ability to observe all token positions at each diffusion step. Rather than relying only on current-step confidence, ST-Veto vetoes temporally unstable tokens via second-order Taylor prediction of confidence dynamics and filters weakly grounded tokens using image-attention mass, swapping them with safer candidates. Across multiple dMLLMs and multimodal reasoning benchmarks, ST-Veto consistently outperforms standard decoding policies and prior VLM reasoning methods, improving accuracy by up to 9% with no additional training or generation cost. Analyses show that ST-Veto steers generation toward higher-confidence, better-grounded paths.

## 27. OrientSAM: Mitigating Camera-Centric Shortcut in Multimodal Spatial Reasoning via Orientation-Aware Spatial Alignment

- Authors: Wenxiao Fan, Hang Yin, Kan Li
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-20
- DOI: Unavailable
- Categories: cs.AI, cs.CV, cs.MM
- Relevance: 2.965368159221031
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.17657v1
- PDF: https://arxiv.org/pdf/2607.17657v1
- Local PDF: pdf/2026-07-22_27_OrientSAM_ Mitigating Camera-Centric Shortcut in Multimodal Spatial Reasoning via Orientation-Aware Spatial Alignment.pdf

Multimodal large language models (MLLMs) still struggle with spatial reasoning that requires perspective transformation. In particular, they often rely on camera-centric cues rather than reasoning from the reference object's viewpoint, leading to systematic errors in non-camera reference settings. In this paper, we first analyze this failure mode and show that object orientation is a key factor underlying such camera-centric shortcut behavior. To address this issue, we propose OrientSAM, an orientation-aware spatial alignment framework for multimodal models. OrientSAM injects explicit orientation information into multimodal representations through orientation-aware tokens and Fourier-based angle encoding, and further adopts a curriculum learning strategy to progressively improve perspective-aware reasoning. In addition, we build a spatial data construction pipeline to generate orientation-aware spatial supervision from large-scale images. Experiments on Spatial-MM, ViewSpatial, and 3DSRBench show that OrientSAM consistently outperforms strong baselines, especially on non-camera-view, person-centric, and orientation-sensitive tasks. The results further demonstrate that explicit orientation modeling is important for mitigating camera-centric shortcut behavior and enabling more robust allocentric spatial reasoning in multimodal models.

## 28. Constraint-Anchored Reasoning Traces

- Authors: Zehua Cheng, Wei Dai, Jiahao Sun
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-18
- DOI: Unavailable
- Categories: cs.AI, cs.CV
- Relevance: 2.9595001154379785
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.16727v1
- PDF: https://arxiv.org/pdf/2607.16727v1
- Local PDF: pdf/2026-07-22_28_Constraint-Anchored Reasoning Traces.pdf

Autoregressive multimodal large language models (MLLMs) suffer from error snowballing: a single incorrect inference early in a chainof-thought (CoT) trace corrupts all downstream reasoning. We find that in state-of-the-art open-source MLLMs, once the first error occurs, the reasoning cascades into failure across all remaining steps in 65% of such cases (a metric we term the snowball rate). Existing mitigations-sampling multiple chains, post-hoc self-verification, or full program synthesis-either lack symbolic grounding, catch errors too late, or sacrifice the flexibility of natural language reasoning. We propose Constraint-Anchored Reasoning Traces (CART), a neuro-symbolic framework that trains MLLMs to interleave natural language reasoning steps with symbolic constraint assertions: lightweight, machine-checkable statements about visual content (e.g., count(red_objects) = 3). A dual-pronged Constraint Propagation Module-combining a learned neural grounding head with Boolean Constraint Propagation-continuously verifies these anchors against extracted visual features and checks their mutual logical consistency. When a contradiction is detected, a backtrack controller halts generation and reverts to the last consistent checkpoint, preventing error propagation. A variable-frequency emission mechanism allows the model to adaptively control anchor density, avoiding trace bloat. We construct 218K training instances by augmenting GQA, CLEVR-CoGenT, and VCR with ground-truth constraint annotations derived from scene graphs, and fine-tune open-source MLLMs (LLaVA-NeXT, Qwen2-VL) via LoRA. On five benchmarks, CART reduces the snowball rate from 0.65 to 0.14, improves GQA accuracy by +4.6 percentage points over trainingonly baselines, and achieves 89.1 F1 on POPE-all with at most 18% inference overhead.

## 29. GeneAutomate: A Browser-Based, Integer-Indexed Platform for Dual-Gene-List Functional Annotation and Interactive Network Visualization

- Authors: Singh, R. P., Kumar, A.
- Source: biorxiv
- Venue type: preprint
- Journal: biorxiv
- Publication status: preprint
- Publication date: 2026-07-21
- DOI: 10.64898/2026.07.16.738882
- Categories: bioinformatics
- Relevance: 2.9273327586760396
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://www.biorxiv.org/content/10.64898/2026.07.16.738882v1.full.pdf
- PDF: https://www.biorxiv.org/content/10.64898/2026.07.16.738882v1.full.pdf
- Local PDF: pdf/2026-07-22_29_GeneAutomate_ A Browser-Based, Integer-Indexed Platform for Dual-Gene-List Functional Annotation and Interactive Network.pdf

Comparative interpretation of two gene lists, for example, two treatment arms, two tissues, or a discovery and a validation cohort, is a routine task in functional genomics. While several tools offer dual-list comparison (e.g., EnrichmentMap, RRHO packages), they typically require local software installation, R/Bioconductor, or manual reconciliation of separate single-list outputs. Most widely used web-based enrichment tools (DAVID, g:Profiler, Enrichr, ShinyGO, WebGestalt) are built around the analysis of a single gene list at a time, and those that support comparison often lack interactive, publication-ready visualization or depend on server-side query latency. Here we present GeneAutomate, a browser-based tool purpose-built for side-by-side comparison of two gene lists. GeneAutomate performs Over-Representation Analysis (ORA) against Gene Ontology (GO) and Reactome using an exact hypergeometric test with Benjamini-Hochberg false discovery rate correction, and Gene Set Enrichment Analysis (GSEA) when ranked (log2 fold-change) input is supplied, alongside Protein-Protein Interaction (PPI) subgraph extraction from BioGRID physical interactions. All reference data (Gene Ontology, Reactome, BioGRID, and NCBI/Ensembl identifier cross-references) are pre-compiled offline into a single integer-indexed database of approximately 32 MB for Homo sapiens, in which every gene identifier Ensembl ID, Entrez ID, official symbol, or alias is resolved to one canonical integer prior to any user query. This design removes live database round-trips from the runtime path, enabling fast, at-your-desk enrichment without installation or a server-side per-query bottleneck. The tool renders thirteen interactive, D3.js- and Cytoscape.js-based comparative visualizations, including a Rank-Rank Hypergeometric Overlap (RRHO) heatmap, a GO-slim "Radar/Spider" functional fingerprint, and chord/edge-bundled cross-talk diagrams that are, to our knowledge, not offered as an integrated set by any existing academic or commercial ORA/GSEA platform. GeneAutomate is an unfunded, individual student project developed with feedback from a professor, and is in its final stage of development. It requires no installation or login. We describe the tool's architecture, statistical methods, and comparative feature set relative to established academic tools (DAVID, ShinyGO, g:Profiler, Enrichr, WebGestalt, STRING, PANTHER, GeneMANIA, Cytoscape, clusterProfiler, GSEA, Metascape) and commercial platforms (IPA, MetaCore, Pathway Studio, iPathwayGuide, Partek Pathway), and we state candidly the current version's limitations, which are planned to be the added in next version: single-species (human-only) coverage, no upstream regulator analysis, and comparison currently limited to two (occasionally three) concurrent lists. GeneAutomate is available at https://geneautomate.tech/.

## 30. SelectInfer: Selective Neuron Loading and Computation for On-Device LLMs

- Authors: Huzaifa Shaaban Kabakibo, Eric Schniedermeyer, Artem Burchanow, Lin Wang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-20
- DOI: Unavailable
- Categories: cs.LG, cs.AI
- Relevance: 2.9241923690568954
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.18081v1
- PDF: https://arxiv.org/pdf/2607.18081v1
- Local PDF: pdf/2026-07-22_30_SelectInfer_ Selective Neuron Loading and Computation for On-Device LLMs.pdf

Large Language Models (LLMs) have demonstrated remarkable capabilities across a range of Natural Language Processing (NLP) tasks, but their high computational and memory demands pose significant challenges for deployment on resource-constrained edge devices. Existing approaches to model compression and optimization often rely on coarse-grained pruning or quantization, which can compromise accuracy or require re-training and fine-tuning. In this work, we introduce SelectInfer, a neuron-level optimization framework that enables efficient LLM inference on edge devices through selective neuron loading and computation. By profiling and identifying both task-specific and general-purpose neurons using an offline LLM profiler, SelectInfer implements two key optimizations: selective loading, which reduces memory footprint by selectively loading a subset of neurons that were identified to be most important during the offline stage, and selective computation, which dynamically computes only the most relevant neurons at runtime. Evaluation across multiple datasets shows that SelectInfer achieves significant reductions in memory footprint and computation while preserving task performance, making it a practical step towards enabling LLM deployment on edge devices
