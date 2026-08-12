# Paper Daily Reading - 2026-08-12

## 1. Neural Message Passing on Structural Interaction Graphs for Fully-Inductive Graph Neural Networks

- Authors: Omer Yom Tov, Avigdor Gal
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-09
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.959547498756903
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.08567v1
- PDF: https://arxiv.org/pdf/2608.08567v1
- Local PDF: pdf/2026-08-12_01_Neural Message Passing on Structural Interaction Graphs for Fully-Inductive Graph Neural Networks.pdf

A central obstacle in building graph foundation models is the input heterogeneity in terms of feature space dimensionality, semantics, and structure. Such heterogeneity limits the capability of graph neural networks to generalize to new graphs with unseen feature spaces. We address the transferability challenge with SIGIL, a framework that maps any attributed graph to a unified representation space of fixed dimension. Given a graph, SIGIL lifts it to a structural interaction graph, where nodes are the input feature dimensions and weighted, typed edges encode feature alignment across multiple orders of the graph's connectivity. A relational message-passing network embeds each feature dimension into a shared space, transforming the original node features, of arbitrary dimensionality, into representations transferable to any downstream graph. By construction, SIGIL is equivariant to permutations of nodes, feature dimensions, and labels. Additionally, when the input features are one-hot indicators of discrete relations, SIGIL recovers and strictly generalizes existing foundation models for knowledge graph reasoning. A single SIGIL model, pretrained on one graph, delivers strong fully-inductive link prediction. Also, SIGIL can be used to implement existing knowledge graph foundation models. As such, SIGIL unifies several existing regimes in graph foundation model design under a single framework

## 2. HOPPER: Learnable Hop Extraction for Linearized Graph Sequence Models

- Authors: Isuru Herath, Arin Gopakumar, Sharan Sahu
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-10
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.7847524256482346
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.09031v1
- PDF: https://arxiv.org/pdf/2608.09031v1
- Local PDF: pdf/2026-08-12_02_HOPPER_ Learnable Hop Extraction for Linearized Graph Sequence Models.pdf

Graph neural networks typically propagate information through repeated message-passing layers, coupling the distance over which information travels with the number of nonlinear transformations applied. This coupling can make deep architectures difficult to optimize and can lead to over-smoothing, over-squashing, and the loss of long-range information. Linearized Graph Sequence Models (LGSMs) address this issue by separating information depth from processing depth and treating the successive propagation states of each node as a sequence. However, existing LGSMs construct these sequences using fixed graph operators, limiting their ability to adapt propagation to the input graph, node features, and downstream task. We introduce HOPPER, an end-to-end learnable extension of LGSM that learns how hop sequences should be extracted before they are processed by a modern state-space model. Our framework supports feature-conditioned, structure-aware, graph- and hop-adaptive propagation mechanisms while preserving permutation equivariance. Standard adjacency-based and non-backtracking LGSM sequences arise as special cases of our proposed extractor family. We show that HOPPER is state-of-the-art or competitive across the ECHO-Synth benchmark, and that varying the maximum neighborhood size of message backtracking cancellation (i.e. structural memory window) can optimize accuracy on the LRIM physics-based long-range dependency benchmark. These results demonstrate that learnable sequence extraction provides a flexible and effective approach to long-range graph representation learning.

## 3. Enhancing pan-cancer spatial transcriptomics at single-cell resolution with stPainter

- Authors: Yuhang Yang, Yiming Luo, Kai Zhang, Zaixi Zhang, Haoxin Peng, Chenlin Cao, Qi Liu, Bin Ma, Yang Chen, Lin Shen, Enhong Chen
- Source: openalex
- Venue type: journal
- Journal: Nature Communications
- Publication status: published
- Publication date: 2026-08-10
- DOI: https://doi.org/10.1038/s41467-026-76552-x
- Categories: Single-cell and spatial transcriptomics, Cancer Genomics and Diagnostics, Mathematical Biology Tumor Growth
- Relevance: 3.6433355118705215
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://doi.org/10.1038/s41467-026-76552-x
- PDF: Unavailable
- Local PDF: Not downloaded

Subcellular spatial transcriptomics can resolve tissue architecture at cellular scale, but sparse gene panels and limited detection sensitivity constrain downstream analysis. Existing enhancement methods often require tissue-matched single-cell RNA sequencing (scRNA-seq) references and dataset-specific retraining. Here we show that stPainter, a conditional generative model pretrained on a pan-cancer scRNA-seq atlas, can enhance spatial transcriptomics data without matched references or retraining. Using a latent diffusion architecture guided by Stochastic Differential Equations (SDE), stPainter reconstructs expanded expression profiles from sparse measurements and produces latent representations for clustering and cell-state analysis. When we apply stPainter upon 6 spatial transcriptomics datasets of different cancer types, we demonstrate that our model empowers downstream biological analyses, including fine-grained subpopulation clustering and pathway enrichment. Comparison with spatially resolved proteomics (CODEX) provided independent support for regional agreement between imputed cellular compositions and protein-level tissue organization. These results establish stPainter as a scalable approach for analyzing tumor microenvironments without auxiliary sequencing data. This study presents stPainter, a pan-cancer pretrained model that enhances sparse spatial transcriptomics data and supports analysis of cellular organization across tumor tissues without matched single-cell references.

## 4. Rethinking Learning-Based Influence Maximization: Simple Neural Surrogates and Native Discrete Search

- Authors: Yiqiao Liao, Parinaz Naghizadeh
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-09
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.5588490707783733
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.08406v1
- PDF: https://arxiv.org/pdf/2608.08406v1
- Local PDF: pdf/2026-08-12_04_Rethinking Learning-Based Influence Maximization_ Simple Neural Surrogates and Native Discrete Search.pdf

Existing learning-based influence maximization frameworks rely heavily on complex neural architectures and continuous optimization over seed representations. We challenge this paradigm with SIMBA, a diffusion-model-agnostic framework pairing a lightweight neural surrogate with direct discrete search. SIMBA introduces three key components: 1) uniformly anchored node embeddings that eliminate initialization noise and encourage learning driven by graph topology and diffusion pattern, 2) a shallow two-layer graph neural network surrogate predicting final infection states, and 3) batched multi-swap simulated annealing that explores combinatorial seed space without gradients or continuous relaxation. By shifting compute from complex representation learning to effective discrete search, SIMBA drastically cuts time-to-solution while achieving superior influence spread and data efficiency. Our code is available at https://github.com/yl489/rethink-IM.

## 5. VOICE: A Vision-Omics Foundation Model Integrating Direct and Retrieval-Based Prediction of In-situ Single-Cell Gene Expression

- Authors: Xin Luo, Yicheng Tao, Haoxuan Zeng, Suyuan Wang, Chenzi Ouyang, Meiqi Zhu, Kai Liu, Shuibing Chen, Jie Liu
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-08
- DOI: Unavailable
- Categories: cs.CV, q-bio.GN
- Relevance: 3.517415824977107
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.08366v1
- PDF: https://arxiv.org/pdf/2608.08366v1
- Local PDF: pdf/2026-08-12_05_VOICE_ A Vision-Omics Foundation Model Integrating Direct and Retrieval-Based Prediction of In-situ Single-Cell Gene Exp.pdf

Spatial transcriptomics can resolve gene expression at single-cell resolution, but it is costly, limited to targeted panels of a few hundred to a few thousand genes, and applicable to only a small number of samples. H&E imaging, by contrast, is cheap and collected routinely at scale. This makes predicting single-cell expression directly from morphology a practical way to bring molecular analysis to large tissue archives. We therefore present VOICE, a multimodal foundation model that predicts single-cell gene expression from H&E images using paired Xenium data. VOICE first aligns cell centered H&E morphology from a pathology foundation model with single-cell expression embeddings from a transcriptome foundation model, trained using contrastive learning over 23 million cells. Next it predicts expression through two branches. One branch directly regresses expression from morphology. The other branch retrieves measured expression from similar reference cells, recovering genes that do not have morphological signal. Because genes vary in morphological predictability, VOICE fuses the two branches with a per-gene weight. After training, VOICE generalizes to heldout patients, slides, and partially overlapping gene panels from Xenium, and it consistently outperforms prior single-cell expression prediction methods on seven metrics.

## 6. Who Built This Model? Tracing LLM Lineage via Spectral Fingerprints in Weight Space

- Authors: Yiwei Chen, Bingqi Shang, Sijia Liu
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-07
- DOI: Unavailable
- Categories: cs.AI, cs.LG
- Relevance: 3.414396240991767
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.07786v1
- PDF: https://arxiv.org/pdf/2608.07786v1
- Local PDF: pdf/2026-08-12_06_Who Built This Model_ Tracing LLM Lineage via Spectral Fingerprints in Weight Space.pdf

Open-weight large language models (LLMs) are increasingly developed through complex, multi-stage pipelines, leading to intricate lineage relationships that reflect model origin, ownership, and evolution. Understanding these relationships is important for model provenance, governance, and supply-chain integrity. In this work, we investigate the notion of LLM "biometrics" (analogous to human biometrics) to ask whether LLMs exhibit intrinsic fingerprints in weight space alone, without access to input data, that reveal their origin and lineage. We formulate this as a lineage discrimination problem, distinguishing among independent-origin, same-series, and shared-base models. To characterize these relationships, we propose a unified geometric fingerprinting framework that analyzes weight matrices from two complementary perspectives: (i) spectral energy, captured by singular value distributions to encode global magnitude patterns, and (ii) subspace alignment, quantified via subspace deviations to capture directional geometry. Our analysis uncovers a clear hierarchy of structural similarity in weight space: spectral energy reliably distinguishes independently trained models and different model families, while subspace alignment enables fine-grained discrimination among closely related models, including variations in dataset scale and post-training procedures. Extensive experiments on over 110 diverse open-weight LLM pairs demonstrate that weight-space geometry provides a robust and interpretable signal for model lineage, enabling coarse-grained regime separation and fine-grained discrimination within shared-base models.

## 7. DoGMA: A Central-Dogma-Guided Foundation Model for Multi-Omics Alignment and Multi-Task Learning in Oncology

- Authors: Junfei Ling, Bangzheng Pu, Bingsen Xue, Tianle Li, Ruying Hu, Cheng Jin
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-08
- DOI: Unavailable
- Categories: cs.LG, cs.AI
- Relevance: 3.3994056068387044
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.08148v1
- PDF: https://arxiv.org/pdf/2608.08148v1
- Local PDF: pdf/2026-08-12_07_DoGMA_ A Central-Dogma-Guided Foundation Model for Multi-Omics Alignment and Multi-Task Learning in Oncology.pdf

Attention mechanisms have been widely utilized in modern deep learning, and many existing multi-omics models inherit their conventional use to allow unrestricted bidirectional interactions. However, the fundamental logic of life is directional. Existing designs often overlook the directionality suggested by the central dogma, potentially limiting transfer across heterogeneous cancers, downstream tasks, and incomplete modality settings.In this work, we present DoGMA, a central-dogma-guided foundation model for pan-cancer multi-omics analysis, arguing that robust transfer requires representations with domain-specific inductive bias. Concretely, we build it on a Transformer-MoE architecture where directed attention biases inter-omics communication toward central-dogma information flow. We further pretrain our model with masked hierarchical omics reconstruction to guide it toward learning central-dogma-consistent interactions. Across diverse downstream tasks, including cancer representation learning, survival prediction, and metastasis prediction, DoGMA consistently demonstrates strong predictive performance. Ablations and analyses further suggest that the performance gains arise from the synergy between central-dogma-guided directed attention and reconstruction-based pretraining, which together promote more biologically consistent cross-omics information exchange. Overall, DoGMA demonstrates that domain-specific inductive biases can improve the robustness and transferability of multi-omics foundation models, offering new insights into the design of attention mechanisms for multi-omics representation learning.

## 8. Moirai: single-cell trajectory inference grounded in gene-level expression dynamics

- Authors: Fijn, A. H. B., S. Jeuken, G.
- Source: biorxiv
- Venue type: preprint
- Journal: biorxiv
- Publication status: preprint
- Publication date: 2026-08-11
- DOI: 10.64898/2026.08.05.742709
- Categories: bioinformatics
- Relevance: 3.251792929105525
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://www.biorxiv.org/content/10.64898/2026.08.05.742709v1.full.pdf
- PDF: https://www.biorxiv.org/content/10.64898/2026.08.05.742709v1.full.pdf
- Local PDF: Not downloaded

Underlying the development of multicellular organisms is the process of cell differentiation, which is governed by the concerted and sequential change in gene expression. Various methods have been developed that employ scRNA-seq data to infer the position of a cell along a pseudo-temporal axis and identify relevant genes involved in the process. These trajectory inference methods typically rely on global transcriptomic changes and mathematical methods. However, overemphasis on large-scale transcriptomic changes may impair sensitivity to identify branching points and convergent trajectories, which are rather governed by small-scale transcriptional events. Motivated by this, we developed Moirai, a graph-based trajectory inference method that identifies gene expression patterns that change dynamically over a developmental continuum and leverages these to define a common pseudotime axis between all cells. In doing so, Moirai shifts the focus to individual gene dynamics, which enhances its ability to detect putative branching points that are masked by global transcriptomic similarities. We apply Moirai to four developmental datasets, where we demonstrate its ability to recover gene expression patterns of genes with a known involvement in the respective developmental process, motivating their use for defining a cell's pseudotime. We furthermore show that Moirai can robustly infer gene expression patterns across different embedding approaches, highlighting the value of moving the focus of the inference process to the small-scale transcriptional dynamics.

## 9. Compositional Cross-Modality Translation via Whole-Volume Multitask Latent Flow Matching

- Authors: Daniele Molino, Alessio Zoboli, Camillo Maria Caruso, Valerio Guarrasi, Paolo Soda
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-08
- DOI: Unavailable
- Categories: cs.CV, cs.AI
- Relevance: 3.220033302810961
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.08135v1
- PDF: https://arxiv.org/pdf/2608.08135v1
- Local PDF: pdf/2026-08-12_09_Compositional Cross-Modality Translation via Whole-Volume Multitask Latent Flow Matching.pdf

Cross-modality medical image translation can reduce the burden of multi-modal acquisitions, yet the field remains constrained by two coupled limitations: methods operate on 2D slices or 3D patches rather than whole volumes, and train a separate model for each translation task. Both stem from a single cause, the absence of a sufficiently strong volumetric prior, which forces generative models to learn anatomical appearance and cross-modality mapping simultaneously, an ill-posed problem at the scale of available paired datasets. We propose to decouple these objectives. A large-scale pretrained 3D variational autoencoder provides a compact latent representation of volumetric appearance, reducing translation to a conditional flow-matching problem. This compression makes whole-volume processing tractable, while a resolution-aware sampling strategy preserves native anatomical scale. We train a single model jointly across inter-modality (MRI$\to$CT, CBCT$\to$CT) and intra-modality (MRI$\to$MRI) tasks over three multi-center datasets. Across all tasks, whole-volume processing outperforms its patch-based counterpart, and the multi-task model matches task-specific baselines while replacing $N$ networks with one. Crucially, joint training unlocks capabilities inaccessible to task-specific approaches: zero-shot generalization to anatomical regions unseen during training, within 0.15 SSIM of the fully supervised model, and compositional cross-dataset translation along paths never directly supervised. These results suggest that combining a strong volumetric prior with multitask training is a scalable route toward synthesis systems that generalize beyond their training distribution. Code is available at https://github.com/arco-group/Whole-Volume-Latent-FM.

## 10. Multi-Relational Knowledge Graph Enhanced Embedding for Trajectory-User Linking

- Authors: Zhifeng Chu, Bin Wang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-09
- DOI: Unavailable
- Categories: cs.LG, cs.CV
- Relevance: 3.215413272292552
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.08646v1
- PDF: https://arxiv.org/pdf/2608.08646v1
- Local PDF: pdf/2026-08-12_10_Multi-Relational Knowledge Graph Enhanced Embedding for Trajectory-User Linking.pdf

Trajectory-User Linking (TUL) aims to identify the owner of an anonymous trajectory from a set of candidate users, providing a basis for user mobility analysis and personalized location-aware services. Existing methods often learn Point of Interest (POI), temporal, and semantic features independently, make limited use of structural knowledge shared across trajectories, and compress structural and sequential information before classification. To address these issues, we propose Multi-Relational Knowledge Graph Enhanced Embedding for Trajectory-User Linking (MakeTUL), which, to the best of our knowledge, is the first attempt to introduce knowledge graph representation learning into TUL. MakeTUL organizes visit-time, POI-category, and transfer-speed information as typed relations in a multi-relational mobility knowledge graph, allowing heterogeneous mobility semantics to jointly constrain the learned embeddings. The resulting POI representations are further enriched with high-order co-occurrence patterns extracted from the trajectory collection, providing structural prior knowledge for sparse and overlapping trajectories. By integrating these prior-enhanced representations with temporal, category, and transfer information, the trajectory sequence learning module captures ordered mobility patterns, while a dual-branch classification layer preserves and combines global structural evidence and sequential evidence at the decision level.

## 11. Multimodal Model Diffing for Feature Discovery and Control

- Authors: Hunar Batra, Lachin Naghashyar, Ashkan Khakzar, Philip Torr, Christian Schroeder de Witt, Constantin Venhoff, Ronald Clark
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-10
- DOI: Unavailable
- Categories: cs.CV, cs.AI, cs.CL, cs.LG
- Relevance: 3.171174236730576
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.09928v1
- PDF: https://arxiv.org/pdf/2608.09928v1
- Local PDF: pdf/2026-08-12_11_Multimodal Model Diffing for Feature Discovery and Control.pdf

Multimodal Large Language Models (MLLMs) exhibit strong visual understanding, yet the internal features that cause these behaviors remain difficult to identify, audit, or control. While applicable to post-hoc inspection, hidden states that are decomposed into interpretable feature directions using sparse autoencoders (SAEs) neither readily isolate which features are changed by multimodal training, nor are they directly useful for targeted control. We introduce MMDiff, a multimodal model-diffing framework that trains multimodal SAEs and turns them into feature-level interfaces for discovering and controlling multimodal behavior. MMDiff supports three uses: (i) feature isolation, by diffing a base-LM SAE against its multimodal-adapted counterpart to identify features altered by multimodal training; (ii) task-specific feature detection, via per-token contrastive firing analysis that isolates causal features; and (iii) feature-level control, by causally removing or steering the discovered feature directions. We train multimodal SAEs for three MLLM families, LLaVA-MORE, PaliGemma 2, and InternVL3.5, and evaluate on visual-spatial understanding, multimodal safety, and OCR. MMDiff discovers sparse, causally specific features whose removal selectively degrades target behaviors by an average of 12% on spatial tasks and 17% on OCR, and reduces attack success rate by 24% on multimodal safety attacks, with no impact on VQA performance. Steering these features improves spatial and OCR accuracy by +3.6% and +1.8% on average over a standard single-layer steering baseline. These results show that multimodal SAEs can serve not only as interpretability tools, but as mechanisms for auditing, steering, and controlling MLLMs behavior toward safer and more capable generations.

## 12. AnchorR: A QuPath and R interface for collaborative exploration of spatial transcriptomics and histology

- Authors: Morris, C. A., Bastian, W. C., Cui, Y., Kurago, Z., Douglass, E. F.
- Source: biorxiv
- Venue type: preprint
- Journal: biorxiv
- Publication status: preprint
- Publication date: 2026-08-11
- DOI: 10.64898/2026.08.05.742985
- Categories: bioinformatics
- Relevance: 3.1342052987526903
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://www.biorxiv.org/content/10.64898/2026.08.05.742985v1.full.pdf
- PDF: https://www.biorxiv.org/content/10.64898/2026.08.05.742985v1.full.pdf
- Local PDF: Not downloaded

Single-cell spatial transcriptomics can connect molecular cell states with tissue morphology, but this promise depends on accurate registration to histopathology. In serial sections, however, tissue borders often differ because of sectioning artifacts, staining variability, and field-of-view acquisition, limiting conventional area-based registration. We developed AnchorR, an expert-guided workflow for coarse-grained alignment of hematoxylin and eosin (H&E) images with CosMx Spatial Molecular Imaging data. Bioinformaticians first define and color-code cell types in Seurat, and pathologists then identify corresponding internal landmarks using QuPath overlays. AnchorR combines these paired landmarks to estimate affine transformations, quantify residual error, and support visual quality control and anchor refinement. Using six oral pre-cancerous tissue sections, we identified 60 cross-modal landmarks. Fitting each section independently reduced mean landmark error from 121.5 m with a single whole-slide transformation to 14.6 m. Cross-validation further showed that increasing the number of anchors improved robustness, with nine-anchor fits achieving approximately 20 m error, or about one cell diameter. AnchorR is designed to complement automated computer-vision methods by providing reliable tissue-level alignment when border mismatch makes global registration difficult. By creating a shared workspace for pathologists and bioinformaticians, it operationalizes an expert-in-the-loop approach and makes feature-based multimodal registration accessible without specialized computer-vision expertise or high-performance computing.

## 13. Imaginative Generative AI: Crossing the Entropy Wall into Worlds Beyond Imitation

- Authors: Hossein Goli, Farzan Farnia, Amin Gohari
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-10
- DOI: Unavailable
- Categories: cs.LG, cs.AI, cs.CV
- Relevance: 3.0932831932455427
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.09385v1
- PDF: https://arxiv.org/pdf/2608.09385v1
- Local PDF: pdf/2026-08-12_13_Imaginative Generative AI_ Crossing the Entropy Wall into Worlds Beyond Imitation.pdf

Generative AI models are primarily designed to imitate the data distribution, an objective that neither corrects diversity lost by a learned generator nor defines how generation should extend beyond the diversity of the data itself. We introduce Imaginative Generative AI (IGA), a framework that makes diversity part of the target-distribution design problem: among distributions close to a reference, IGA selects one whose spectral diversity reaches a prescribed level. Diversity is measured by the von Neumann entropy of the generated distribution's kernel covariance operator in a fixed representation space, providing a reference-free representation-guided measure of how broadly probability mass occupies embedding directions. The spectral entropy of the population data distribution defines an Entropy Wall. Below the wall, IGA performs diversity repair, recovering variation that a learned generator has lost while remaining within the diversity level of the data. Beyond the wall, the data distribution itself becomes infeasible, and IGA deliberately departs from it to produce distributions with greater representation-relative spectral diversity, an operational notion of imaginative generation. These regimes form a single regularization path from imitation to imagination and define an i.i.d. target distribution at each prescribed diversity level. We develop the theory of this entropy-constrained projection and show that, under a KL anchor to a pretrained generator, the optimum satisfies a self-consistent exponential-tilt relation. This characterization leads to IGA Guidance, a retraining-free inference-time method for score-based and diffusion models, including DDPM and DDIM samplers. Experiments on synthetic and vision benchmarks demonstrate diversity repair below the Entropy Wall and controlled spectral extrapolation beyond it.

## 14. Neurosymbolic Discovery of Algebraic Graph Constructions

- Authors: David Seka, Stefan Szeider
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-08
- DOI: Unavailable
- Categories: cs.AI, cs.LG, cs.SC, math.CO
- Relevance: 3.088561962680967
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.08118v1
- PDF: https://arxiv.org/pdf/2608.08118v1
- Local PDF: pdf/2026-08-12_14_Neurosymbolic Discovery of Algebraic Graph Constructions.pdf

There are several methods for searching for graphs with prescribed properties, such as SAT solvers and specialized generators. These methods return the result as raw data: an adjacency matrix or a string encoding. The raw data certifies that the graph exists, but it does not reveal any structural properties of the graph. We ask whether one can automatically discover a short algebraic description if only this raw data is provided. We look for a description such as a Cayley graph $\mathrm{Cay}(Γ, S)$ or a lexicographic product $C_5[K_3]$.
  We address this question with a neurosymbolic approach. We propose an agent that runs on a general-purpose large language model with no fine-tuning or per-target training. The model interleaves reasoning with calls to the computer algebra system SageMath: it analyzes the target graph, proposes and tests candidate constructions, and revises them until the output matches the target. The agent communicates with SageMath through a Model Context Protocol (MCP) server, which we release as a general-purpose bridge. Whether a construction matches the target is checked by a single exact isomorphism test, and therefore rests on the symbolic side and not on the model. We test the approach on a benchmark of 100 highly symmetric graphs, namely two-orbit graphs on up to 25 vertices; the benchmark was fixed in advance. Our agent could find verified algebraic constructions for all of them, without falling back to raw encodings. A strong template-enumeration baseline reaches only about $20\%$, and a catalog lookup could not identify any of these graphs. However, construction quality declines when symmetry is removed.
  As a concrete application, we identify the smallest known counterexample to the Bernhart-Kainen dispersability conjecture, a $16$-vertex graph that enumeration found as raw data. For this graph, our agent found an explicit algebraic construction.

## 15. LoRSA: Toward Generalizable Parameter-Efficient Fine-Tuning for Biomedical Downstream Tasks

- Authors: Saed Moradi, Benyamin Ghojogh, M. Hadi Sepanj, Yimin Yang, Ashirbani Saha
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-07
- DOI: Unavailable
- Categories: cs.CV, cs.AI, cs.LG
- Relevance: 3.0843646971639593
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.07749v1
- PDF: https://arxiv.org/pdf/2608.07749v1
- Local PDF: pdf/2026-08-12_15_LoRSA_ Toward Generalizable Parameter-Efficient Fine-Tuning for Biomedical Downstream Tasks.pdf

Parameter-efficient fine-tuning enables the adaptation of vision foundation models to biomedical tasks under limited computational resources, but a single low-rank update can constrain all task-specific changes to one narrow parameter subspace. This restriction may prevent the model from simultaneously representing globally shared task structure and localized residual directions required for generalization to unseen imaging domains. We introduce LoRSA, a global--residual adaptation framework that jointly learns a dense low-rank component and a dynamically structured-sparse low-rank component. The dense component captures globally coordinated task adaptation, while the structured component provides complementary residual corrections whose support evolves during training. We characterize the representational capacity, approximation properties, rank structure, and singular-subspace complementarity of this decomposition. We evaluate LoRSA for four-class breast-density classification using DINOv3-Base, with VinDr-Mammo as the source domain and MammosighTR and RSNA as unseen external domains. LoRSA remains competitive on the internal validation set and achieves the best external macro-F1 on both target datasets, improving upon the strongest competing method by 2.15 percentage points on MammosighTR and 3.09 percentage points on RSNA. Weight-matrix analysis further shows that approximately $92\%$ of the energy of each adaptation component lies outside the bilateral singular subspace of the other, indicating that the two components learn largely complementary update directions. These results suggest that organizing adaptation capacity into distinct global and residual paths can improve the external-domain generalization of parameter-efficiently adapted biomedical vision models.

## 16. Self-Evolving Neuro-Symbolic Skills for Tool-Augmented Spatial Reasoning

- Authors: Shi-Yu Tian, Zhuo-Xia Wang, Xuan-Yi Zhu, Zhi Zhou, Xinwei Yang, Kun-Yang Yu, Ming Yang, Yang Chen, Yu-Feng Li
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-08
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 3.067011916178068
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.07955v1
- PDF: https://arxiv.org/pdf/2608.07955v1
- Local PDF: pdf/2026-08-12_16_Self-Evolving Neuro-Symbolic Skills for Tool-Augmented Spatial Reasoning.pdf

Large vision-language models have achieved strong performance in multimodal reasoning, but they remain unreliable on fine-grained spatial tasks that demand both precise spatial perception and fine-grained geometric computation beyond end-to-end generation. Tool augmentation offers a natural solution, while existing methods either plan tool calls from scratch without explicit dependency constraints or rely on fixed pipelines that are redundant and generalize poorly across spatial tasks. An effective spatial reasoning agent should instead accumulate reusable experience and adaptively compose it for new problems. To this end, we propose NeSy-Spatial, a neuro-symbolic framework for self-evolving spatial skills. NeSy-Spatial abstracts tool interactions and geometric operations into typed executable atomic instructions and composes them into two complementary skill types: Tool-Use Skills for organizing tool execution and Geometry Skills for structured geometric reasoning. During inference, NeSy-Spatial retrieves and executes relevant skills in a closed-loop process. During evolution, it analyzes buffered successful and failed trajectories to refine skill structures and prune unreliable or inactive entries. Experiments on three spatial reasoning benchmarks show that NeSy-Spatial consistently improves reasoning accuracy with more precise tool utilization.

## 17. H2: A Dual Hybrid Semantic Data Lake Architecture for Medical Data Harmonization with Human-In-the-Loop verified, LLM Driven Metadata Annotation System

- Authors: Ioannis N. Tzortzis, Georgia Kapetadimitri, Agapi Davradou, Nefeli Kousta, Nikolaos Bakalos, Ioannis Rallis, Dimitrios Kalogeras, Nikolaos Doulamis, Anastasios Doulamis
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-08
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 3.0579688774355986
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.08056v1
- PDF: https://arxiv.org/pdf/2608.08056v1
- Local PDF: pdf/2026-08-12_17_H2_ A Dual Hybrid Semantic Data Lake Architecture for Medical Data Harmonization with Human-In-the-Loop verified, LLM Dr.pdf

Medical data, by its nature, exhibit a high degree of heterogeneity on multiple levels ranging from (a) different modalities like images, text and time series, (b) diverse tabular schemata introduced by institutions and (c) completely unstructured textual information data provided by healthcare professionals. Data lakes are often used in medical data storage to consolidate all heterogeneous diverse data in a single, central location, where it can be saved "as is", without the need to impose a schema like a data warehouse does. Despite their flexibility, though, data lakes are notorious for the "data swamp" failure. Thus, providing a reliable data harmonization mechanism through metadata, without compromising integrity or flexibility, is a real challenge. To this end, knowledge graphs have attracted attention since they provide a dynamic way to depict relationships without a rigid schema-on-write approach. Additionally, another rigorous task relies on the interoperability of data: application of appropriate ML techniques on such a diverse nature of data is not an easy task, as a domain expert must decide the efficacy of a method to a specific data type or dataset. Metadata annotation can aid by tagging applicable operations, however this requires manual intervention, not to mention the plethora of existing datasets which lack such information. To tackle both challenges, in this paper, we propose a semantic data lake architecture that promotes data harmonization and incorporates a generative annotation process (i.e. LLMs) of non-labeled metadata collections to support the application of meaningful ML techniques. Building on top of this approach, we create a higher level of knowledge, identifying suitability of data with respect to applicable ML operations based on their data nature...

## 18. A continually expandable foundation model for brain MRI

- Authors: Michail Mamalakis, Carmen Jimenez-Mesa, Yonghao Li, Hao Chen, Chao Li, Antonios Mamalakis, John Suckling, Richard Bethlehem, Stephen J. Price, Richard J. Gilbertson, Pietro Lio
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-08
- DOI: Unavailable
- Categories: cs.CV, cs.LG
- Relevance: 3.028140561531047
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.08319v1
- PDF: https://arxiv.org/pdf/2608.08319v1
- Local PDF: pdf/2026-08-12_18_A continually expandable foundation model for brain MRI.pdf

Brain magnetic resonance imaging (MRI) is central to neuroscience and clinical assessment, but models are commonly developed for individual diseases, populations or imaging protocols. Foundation models promise more general representations, yet they are usually pretrained once and can lose earlier capabilities when updated with new data. Here we show that Alcmaeon, a three-dimensional brain MRI foundation model pretrained without manual labels on more than 425,000 volumes and derived imaging maps, can be expanded sequentially across clinical domains. Alcmaeon combines volumetric encoding and latent diffusion generation with Graph-Blueprint Pruning (GBP), which protects network modules important to earlier domains while leaving the remaining capacity trainable. Across expansion from healthy ageing and neurodegeneration to developmental, psychiatric and tumour imaging, GBP showed less forgetting than sequential adaptation and elastic weight consolidation across voxel-level reconstruction measures, with its largest advantage after adaptation to tumour imaging. The blueprints provided an inspectable record of how model capacity was protected and reused. Representations from different model levels supported image synthesis, disease classification, survival modelling and postoperative prediction, although no single representation was optimal for every task. These findings provide a route towards brain MRI foundation models that can grow with emerging data while retaining earlier capabilities.

## 19. Counterfactual Benchmarking and Training for Factuality Consistency and Order-Robust Grounded Reasoning in LLMs over Heterogeneous Knowledge

- Authors: Shibo Chu, Yuze Liu, Tiehua Zhang, Zhishu Shen, Lianghua He, Haofen Wang, Zhijun Ding
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-08
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 3.00289539392512
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.07838v1
- PDF: https://arxiv.org/pdf/2608.07838v1
- Local PDF: pdf/2026-08-12_19_Counterfactual Benchmarking and Training for Factuality Consistency and Order-Robust Grounded Reasoning in LLMs over Het.pdf

Large language models (LLMs) have increasingly supported response generation grounded in user-provided knowledge spanning heterogeneous structures. However, existing benchmarks provide limited assessment of whether LLMs can faithfully perform multi-hop reasoning chains across such knowledge contexts while remaining robust to variations in their input order. We introduce TKFQA, a factuality consistency benchmark comprising 10,130 question-answering (QA) pairs grounded in tables, texts, and knowledge graphs (KGs). Each example is constructed from an explicit counterfactual reasoning chain, enabling the joint evaluation of answer correctness, reasoning-chain accuracy, and robustness to different input-order. An extensive evaluation of 14 open- and closed-source LLMs reveals that state-of-the-art models exhibit limited reasoning-chain accuracy and remain sensitive to variations in the input order of heterogeneous knowledge contexts. To address these limitations, we propose ORLF, an LLM-agnostic training framework that models cross-context topological relations through knowledge-specific latent vectors. ORLF integrates context-wise position encoding, a latent-bridge attention mask, and topological knowledge bias to preserve knowledge-specific bias and encode topological semantics. Experiments across four LLM backbones show that ORLF outperforms competitive training-free and LoRA-based baselines, improving average Exact Match and Reasoning-Chain Accuracy by 2.15% and 4.29%, respectively, while reducing order-induced performance standard deviation by 0.04% to 3.01%.

## 20. Multi-Branch Policy Optimization for Multimodal Large Language Models

- Authors: Shuai Lyu, Yuning Gong, Ruiling Gao, Xiaoran Shang, Zhonghong Ou, Ping Zong, Yifan Zhu, Yuan Sun, Yang Qin, Peng Hu
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-05
- DOI: 10.1145/3767308.3836564
- Categories: cs.CV, cs.AI
- Relevance: 3.0007900228700803
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.07581v1
- PDF: https://arxiv.org/pdf/2608.07581v1
- Local PDF: pdf/2026-08-12_20_Multi-Branch Policy Optimization for Multimodal Large Language Models.pdf

Group-based reinforcement learning methods for multimodal large language models typically rely on trajectory-level credit assignment that applies a single advantage to all tokens in a response. However, multimodal reasoning involves substantially higher perceptual uncertainty than text-only settings, where the model must repeatedly re-examine visual information to verify intermediate interpretations, and different visual groundings can lead to divergent reasoning paths, making such uniform credit assignment particularly inadequate and causing relative advantages to progressively degenerate toward zero. To address these challenges, we propose Multi-Branch Policy Optimization (MBPO), a tree-based framework that constructs reasoning trees at vision-language decision boundaries, enabling sibling branches to explore diverse visual hypotheses and assigning segment-level credit through branch-relative advantages. We further introduce a temporal replay buffer to reuse informative segments while controlling policy staleness. Experiments on several multimodal reasoning benchmarks show that MBPO outperforms representative baselines, improving both learning signal quality and optimization efficiency. The code is publicly available at https://github.com/ShuaiLyu0110/MBPO.

## 21. MOSAIC: Adversarial Co-evolution of Specialist Heuristics and Problem Instances for LLM-based Automated Heuristic Design

- Authors: Oguzhan Gungordu, Siheng Xiong, Faramarz Fekri
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-31
- DOI: Unavailable
- Categories: cs.NE, cs.AI
- Relevance: 2.989590061227241
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.07544v1
- PDF: https://arxiv.org/pdf/2608.07544v1
- Local PDF: pdf/2026-08-12_21_MOSAIC_ Adversarial Co-evolution of Specialist Heuristics and Problem Instances for LLM-based Automated Heuristic Design.pdf

Automated heuristic design (AHD) with large language models (LLMs) has produced strong heuristics for combinatorial optimization problems (COPs). Yet existing frameworks optimize for average performance on a small fixed dataset and steer the search with "verbal gradients" distilled from scalar better/worse feedback. No single heuristic dominates across instance distributions, and scalar feedback tells the LLM whether a heuristic improved, but not where in the instance space or why. We propose MOSAIC, a grid-based framework that adversarially co-evolves problem instances and specialist heuristics inside a Quality-Diversity (QD) archive indexed by structural instance features. Instances evolve to expose weaknesses of the current heuristics, and heuristics evolve to eliminate them by specializing to the newly exposed regions. Each archive cell keeps a specialist heuristic, representative instances, and insights explaining what works in its region, forming a persistent memory that accumulates over the evolutionary search. For each heuristic pair sampled from distant grid regions, an LLM-guided evolutionary loop generates discriminative instances, and a decision tree identifies the feature-space regions where each heuristic wins. A reflection LLM then contrasts the two heuristics to produce multi-directional insights that persist in those regions and guide crossover and mutation. The archive is simultaneously a co-evolved benchmark of discriminative instances and a pool of region specialist heuristics, from which greedy selection extracts a compact complementary portfolio. Across COPs, test sizes, and LLM backbones, the portfolio consistently outperforms state-of-the-art LLM-based AHD methods, and the co-evolved instances attain higher feature-space coverage and stronger heuristic discrimination than evolutionary instance-generation baselines.

## 22. MMArch: Benchmarking Multimodal Reasoning Grounded in Architectural Evidence

- Authors: Chenxu Du, Kang An, Tengyue Wang, Zhongyu Yang, Xinqi Yang, Yuanchi Zhu, Hebao Zhu, Ziliang Wang, Faqiang Qian, Yunli Yang, Qibing Ren
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-10
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 2.978834747794953
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.09281v1
- PDF: https://arxiv.org/pdf/2608.09281v1
- Local PDF: pdf/2026-08-12_22_MMArch_ Benchmarking Multimodal Reasoning Grounded in Architectural Evidence.pdf

Multimodal large language models (MLLMs) perform strongly on engineering imagery, yet existing benchmarks mostly test drawing recognition, information extraction, or compliance checking, leaving open whether models can combine distributed visual evidence with engineering principles to reach a conclusion. We introduce MMArch, a benchmark for architecture and civil engineering spanning ten subdomains and built entirely from figures in peer-reviewed papers. Its $1{,}212$ short-answer items are produced by a decoupled planner--writer pipeline and validated through automated screening, a blind adversarial audit, and expert review, so that answering requires perceiving the relevant evidence, identifying the governing principle, and applying it, not exploiting textual or single-figure shortcuts. Evaluating $18$ open-weight and proprietary MLLMs against a domain-expert panel, we find a wide gap: the strongest open-source model attains about $30\%$ and the best proprietary system $52\%$, while human experts reach $95\%$, more than forty points ahead. Our error analysis shows that failures concentrate in applying principles and combining evidence across figures rather than in locating it, pointing to substantial headroom for future research. Code and data are available at https://dcx-swjtu.github.io/MMArch/.

## 23. KGCaRe: Explainable Complex Conditional Question Answering using Automatic Knowledge Graph Construction and Context Retrieval with LLMs

- Authors: Ghanshyam Verma, Simanta Sarkar, Devishree Pillai, Hotaka Shiokawa, Yourong Xu, Fiona Veazey, Peter Hubbert, Hui Su, Paul Buitelaar
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-10
- DOI: Unavailable
- Categories: cs.CL, cs.AI
- Relevance: 2.9703818914337123
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.09779v1
- PDF: https://arxiv.org/pdf/2608.09779v1
- Local PDF: pdf/2026-08-12_23_KGCaRe_ Explainable Complex Conditional Question Answering using Automatic Knowledge Graph Construction and Context Retr.pdf

Answering complex conditional questions using Large Language Models (LLMs) and Retrieval-Augmented Generation (RAG) remains a challenge, particularly in domain-specific contexts where general-purpose LLMs and RAG tend to underperform. We hypothesize that augmenting RAG with unstructured and structured knowledge, extracted from both documents and knowledge graphs (KGs), can improve reasoning and answer accuracy for such tasks.
  To test this, we propose KGCaRe, a hybrid approach that combines neural retrieval with symbolic reasoning over LLM-generated KGs. KGCaRe constructs a KG from documents using a multi-prompt extraction strategy and stores it in a graph database. Simultaneously, the documents are embedded into a vector store to enable neural retrieval. KGCaRe performs innovative iterative graph traversal guided by the LLM to extract relevant triples, prune irrelevant information, and uses additional clue entities to traverse the graph again if the initial traversal does not provide satisfactory context to generate the answer. The relevant triples extracted from the KG in path form, along with semantically retrieved text passages, are then fed into custom KGCaRe prompts to generate answers to the complex conditional questions with explanations.
  We evaluate KGCaRe on two complex conditional QA datasets. Our results on these datasets show that KGCaRe consistently outperforms existing baselines, including Vanilla LLM, Code Prompt, Text Prompt, Think-on-Graph, Vanilla RAG, and HybridContextQA, across multiple LLMs such as Mistral, Mixtral, GPT-3.5, and GPT-4o. We publicly release the software pipeline that we developed to implement the proposed KGCaRe approach.

## 24. GALA: Graph-Augmented LLM Agents for Root Cause Analysis and Incident Response in Microservices

- Authors: Yifang Tian, Yaming Liu, Zichun Chong, Zihang Huang, Yiran Li, Hans-Arno Jacobsen
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-10
- DOI: Unavailable
- Categories: cs.SE, cs.AI
- Relevance: 2.960939887674976
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.08968v1
- PDF: https://arxiv.org/pdf/2608.08968v1
- Local PDF: pdf/2026-08-12_24_GALA_ Graph-Augmented LLM Agents for Root Cause Analysis and Incident Response in Microservices.pdf

Microservice root cause analysis (RCA) requires correlating failures across heterogeneous telemetry within complex service dependency graphs. Existing methods often rely on a single telemetry modality; recent LLM-based approaches can suffer from unconstrained exploration and hallucination; and most systems stop at fault ranking without producing actionable incident response. We present GALA+, a graph-augmented LLM agentic framework centered on graph-guided investigation, which uses service dependencies to bound exploration and refine diagnosis through localized multi-modal evidence. For initial hypothesis generation, GALA+ combines complementary telemetry signals with STRIX, a novel trace- and graph-structure-aware scoring module. GALA+ then produces ranked diagnoses, incident summaries, and stratified action recommendations. We further introduce SURE-Score, a human-guided evaluation framework co-developed with industry SRE experts for assessing RCA-specific output quality beyond conventional text similarity metrics. On two microservice benchmarks, GALA+ consistently achieves the strongest overall results, surpassing the best LLM-based baseline by more than 25 percentage points in AC@1, while also receiving the highest ratings from both SURE-Score and independent human SRE evaluation.

## 25. Systematic assessment of the biological impact of cellular deconvolution on downstream analyses of disease transcriptomes

- Authors: Mitra, S., Ibrahim, M., Narayanan, M.
- Source: biorxiv
- Venue type: preprint
- Journal: biorxiv
- Publication status: preprint
- Publication date: 2026-08-11
- DOI: 10.64898/2026.08.05.742993
- Categories: bioinformatics
- Relevance: 2.959674117457678
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://www.biorxiv.org/content/10.64898/2026.08.05.742993v1.full.pdf
- PDF: https://www.biorxiv.org/content/10.64898/2026.08.05.742993v1.full.pdf
- Local PDF: Not downloaded

Background Cellular deconvolution methods estimate cell type proportions from bulk RNA seq data, typically using single cell RNA seq derived signatures, enabling separation of disease associated transcriptional changes into composition driven and cell intrinsic effects. However, these approaches depend on model assumptions and the stability of cell type signatures, and it remains unclear how deconvolution related uncertainties influence downstream analyses and biological conclusions. Results We systematically evaluated the effect of cell type correction on disease relevant transcriptomic insights, using Alzheimer's disease (AD) as a model and the Mount Sinai Brain Bank cohort as a primary dataset. Applying dtangle, selected after comparison with another deconvolution approach, we estimated cell type proportions across four brain regions and assessed how correction reshaped differential gene expression and pathway enrichment. Cell type correction (CTC) markedly altered differentially expressed gene (DEG) profiles in a region dependent manner: the superior temporal gyrus lost all significant signals, while the frontal pole gained DEGs with improved cross region concordance. At the pathway level, correction shifted enrichment from synaptic loss and immune activation toward suppression of stress response and immune regulatory programs, suggesting that composition changes partly obscure cell intrinsic regulatory signals. Overlap with AD genome wide association study loci and replication in an independent cohort indicated that cell intrinsic changes are more consistently validated than composition driven changes. Notably, KCNN2 and RIMS1, not currently recognized as canonical AD biomarkers, emerged as robust transcriptional signatures, potentially reflecting both compositiondriven and cell intrinsic dysregulation and warranting further investigation. Conclusions Parallel evaluation of uncorrected and CTC analyses distinguishes composition driven from cell intrinsic transcriptional effects and highlights robust disease signatures in heterogeneous tissues such as the brain.

## 26. NL2SHACL-Bench: A Benchmark Suite for Natural Language to SHACL Translation

- Authors: Yuchen Zhou, Niels Bobet, Maribel Acosta
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-24
- DOI: Unavailable
- Categories: cs.AI, cs.CL, cs.DB
- Relevance: 2.948009661415659
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.07530v1
- PDF: https://arxiv.org/pdf/2608.07530v1
- Local PDF: pdf/2026-08-12_26_NL2SHACL-Bench_ A Benchmark Suite for Natural Language to SHACL Translation.pdf

SHACL is a core technology for validating the conformance of RDF knowledge graphs (KGs). Yet, authoring SHACL shapes requires technical expertise that most domain experts lack. Translating natural language requirements into SHACL (NL2SHACL) would lower this barrier. However, there is no dedicated benchmark for NL2SHACL, and evaluating generated shapes requires methods beyond string comparison, as semantically equivalent shapes can differ in serialisation and structure. To tackle these challenges, we present NL2SHACL-Bench, a benchmark suite for natural language to SHACL translation. Using NL2SHACL-Bench, we evaluate four state-of-the-art large language models (LLMs) for this task. Our results show that current LLMs are highly capable of generating syntactically valid SHACL, but still struggle to produce semantically equivalent constraints for complex logical and structural patterns. This indicates that NL2SHACL-Bench provides a meaningful basis for measuring advances in the NL2SHACL state of the art.

## 27. Different Feedback, Different Updates: Selective Self-Learning from User Interactions for Large Language Models

- Authors: Xuanchen Li, Haitao Li, Yujia Zhou, Qingyi Pan, Heng Wang, Yiqun Liu, Min Zhang, Qingyao Ai
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-10
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 2.9428457954786955
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.09109v1
- PDF: https://arxiv.org/pdf/2608.09109v1
- Local PDF: pdf/2026-08-12_27_Different Feedback, Different Updates_ Selective Self-Learning from User Interactions for Large Language Models.pdf

User feedback offers natural supervision for persistent LLM improvement, but a single message may support multiple behavioral changes with different scopes of generalization. We introduce SLIFT, a selective self-learning framework built on a task-relative view of user feedback. SLIFT decomposes each feedback message into atomic components and interprets each component relative to the original task as Fix, Spec, or Null: requirements for task validity, compatible condition-specific refinements, or content with no reliable positive update direction. To incorporate each change at the appropriate scope, SLIFT trains two complementary LoRA adapters on a shared frozen backbone: a Generalist that consolidates Fix requirements into default behavior through feedback-conditioned self-distillation, and a Specialist that observes only the task and Generalist response to supply residual guidance for applicable, unmet Spec refinements. Null components induce no positive update. Across backbones, SLIFT achieves strong performance on both MemoryBench and WildFB, with targeted analyses further examining its underlying mechanisms. We release our code at https://anonymous.4open.science/r/SLIFT.

## 28. Towards Researcher Agents for Knowledge-Graph Question Answering

- Authors: Tommaso Soru, Abdulsobur Oyewale
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-07
- DOI: Unavailable
- Categories: cs.AI, cs.DB
- Relevance: 2.9275738639505464
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.07700v1
- PDF: https://arxiv.org/pdf/2608.07700v1
- Local PDF: pdf/2026-08-12_28_Towards Researcher Agents for Knowledge-Graph Question Answering.pdf

Translating a natural-language question into a SPARQL query that can be executed against a large knowledge graph requires resolving lexical ambiguity, grounding surface terms in the target ontology, and producing graph patterns that are both syntactically valid and semantically faithful. We present an agentic text-to-SPARQL system that goes one step beyond static tool-using agents: a researcher agent that, after each round of inference on a validation set, proposes and tests changes to its own prompts, rules, and tool-orchestration code. We instantiate the loop on DBpedia, evolve nine successive versions of the agent driven by a low-cost reasoning model, and deploy the best-performing configuration with two stronger backbone models. The study yields three observations: (i) self-improvement converges quickly and then achieves 0.22 overall accuracy on the 2025 DBpedia validation set; (ii) the bottleneck is consistently in basic-graph-pattern predicate selection, not in SPARQL syntax or modifiers; and (iii) several benchmark items appear to penalise correct queries due to property ambiguity in DBpedia, suggesting that future Text-to-SPARQL benchmarks should be scored using a combination of machine translation and information retrieval metrics.

## 29. When Is a Steerable Concept Representation Real? Measurement Confounds in a Cross-Family Audit of Neuroscience Parallels in LLMs

- Authors: Yuqi Wu, Shengming Zhao, Jie Chen
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-08
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 2.922610791459025
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.08159v1
- PDF: https://arxiv.org/pdf/2608.08159v1
- Local PDF: pdf/2026-08-12_29_When Is a Steerable Concept Representation Real_ Measurement Confounds in a Cross-Family Audit of Neuroscience Parallels.pdf

Large language models (LLMs) are increasingly reported to exhibit human-like neural and cognitive signatures, including concept cells, mental number lines, and cognitive maps. These claims often rely on linear probing and activation steering applied to a single model, yet both methods are highly sensitive to measurement choices. A reported parallel may therefore reflect the model, the measurement procedure, or both. We audit four representative neuroscience-inspired paradigms across 17 models from five families, spanning $0.6$B to $72$B parameters. Our main experiment examines the causal steerability of concept directions. With raw activation units and a fixed layer and coefficient, steerability appears to increase with model scale, resembling an emergent capability. However, this pattern is produced by an uncalibrated pipeline rather than by a claim established in the steering literature. The trend depends jointly on raw units, the readout metric, and the operating point; correcting any one of these removes it. With residual-norm-comparable interventions and held-out operating-point selection, concept steering remains significant at every scale, but shows no significant trend across the Qwen3 series, although the confidence interval does not rule out a moderate positive slope. The remaining results are mixed. A linear geographic world map is consistently decodable in every tested checkpoint up to $72$B. Number magnitude is strongly encoded, but whether individual neurons appear bell-shaped or monotonic depends on the selection criterion. Language-specific structure is localizable, but the direction of the cross-lingual asymmetry reverses under a different attribution method. These results suggest that the main constraint on AI neuroscience is not a lack of phenomena, but a lack of comparable measurements and adequate controls. We release the protocol, stimuli, and code.

## 30. Triple Expert Learning from Noisy Labels for Semi-Supervised Vision Foundation Model Adaptation

- Authors: Xuanyu Liu, Zheng Fang, Hongyang He, Yundi Hong, Daizong Liu
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-10
- DOI: Unavailable
- Categories: cs.CV, cs.AI
- Relevance: 2.9185502728335857
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.09052v1
- PDF: https://arxiv.org/pdf/2608.09052v1
- Local PDF: pdf/2026-08-12_30_Triple Expert Learning from Noisy Labels for Semi-Supervised Vision Foundation Model Adaptation.pdf

Semi-supervised adaptation of vision foundation models (VFMs) commonly freezes the pretrained backbone and updates lightweight modules such as LoRA. However, pseudo-labels have mixed reliability, and a single LoRA adapter must absorb reliable, ambiguous, and noisy gradients in the same low-rank space. This can make VFM adaptation sensitive to pseudo-label noise. We propose \textbf{TriNoL}, a \textbf{Tri}ple-expert learning framework from \textbf{No}isy \textbf{L}abels for semi-supervised VFM adaptation. TriNoL routes unlabeled samples into three confidence regions and assigns them to three LoRA experts: a Positive Expert for high-confidence pseudo-labels, an Alignment Expert for medium-confidence ambiguous samples, and a Negative Expert for low-confidence noisy samples. The VFM backbone remains frozen, and only the LoRA experts and classifier head are updated. By separating different pseudo-label reliability regions into specialized adaptation paths, TriNoL improves robustness to noisy supervision while keeping the training cost low.
