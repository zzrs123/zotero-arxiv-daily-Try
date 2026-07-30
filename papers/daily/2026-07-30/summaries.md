# Paper Daily Reading - 2026-07-30

## 1. CHARM: A Multimodal Graph Foundation Model with Hierarchical Context Modeling for Zero-Shot Transfer

- Authors: Ankang Yang, Jitao Zhao, Di Jin, Yuxiao Huang, Dongxiao He
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-28
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 3.6416060836712534
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.26023v1
- PDF: https://arxiv.org/pdf/2607.26023v1
- Local PDF: pdf/2026-07-30_01_CHARM_ A Multimodal Graph Foundation Model with Hierarchical Context Modeling for Zero-Shot Transfer.pdf

Graph foundation models (GFMs) have emerged as a promising paradigm for transferring knowledge across graph domains and tasks. Real-world graphs associate nodes with text, images, and other modalities, making multimodal graphs essential for representing complex entities and relations. Moreover, collecting labels and adapting models for every new graph domain is costly and often infeasible, motivating zero-shot transfer. Unfortunately, zero-shot transfer on multimodal graphs remains underexplored. Existing GNN-based graph foundation models typically require downstream adaptation, whereas LLM-based graph methods mainly address unimodal graphs or tasks within a single domain. This setting presents two key challenges. First, models must generalize knowledge from individual modalities while capturing transferable cross-modal relations. Second, without target-domain fine-tuning, node representations remain entangled with domain-specific structures and modality-specific characteristics, obscuring shared concepts in unseen domains. To address these challenges, we propose CHARM, a multimodal graph foundation model with hierarchical context modeling for zero-shot transfer. CHARM replaces isolated raw nodes with hierarchical graph contexts that capture multimodal semantics and cross-modal relations. These contexts map domain-specific node patterns to shared high-level concepts, reducing reliance on target-domain supervision or adaptation. A modality-aware graph context encoder integrates multimodal information with graph structure and converts the resulting representations into graph tokens for a large language model . Experiments show consistent improvements on zero-shot multimodal graph tasks.

## 2. IRIS: Reusable Identity Representations from Frozen LLMs for Entity Alignment

- Authors: Xinran Liu, Shengtao Li, Shouqian Shi, Ge Wang, Xin-Wei Yao
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-28
- DOI: Unavailable
- Categories: cs.CL, cs.AI
- Relevance: 3.3244515475266976
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.25579v1
- PDF: https://arxiv.org/pdf/2607.25579v1
- Local PDF: pdf/2026-07-30_02_IRIS_ Reusable Identity Representations from Frozen LLMs for Entity Alignment.pdf

Entity alignment (EA) identifies entities across knowledge graphs (KGs) that refer to the same real-world object. Conventional EA methods mainly exploit explicit graph structures and textual fields, which often provide insufficient semantic understanding to recognize the same entity under heterogeneous descriptions and distinguish it from semantically similar entities. Although large language models (LLMs) offer deeper entity understanding, existing LLM-based EA methods largely use this capability for auxiliary generation or candidate-conditioned decisions. Consequently, such understanding is not distilled into a stable and directly comparable identity space, leaving alignment tied to specific KG pairs or candidate sets and requiring repeated processing as the matching context changes. To address these limitations, we propose IRIS (Identity Representations from Internal States), a training-free framework that constructs for each entity an iris-like signature encoding its distinctive and stable identity characteristics. IRIS derives these signatures by eliciting identity-oriented contextual representations from a frozen LLM, thereby forming a shared space in which each entity is encoded once and can be aligned across different KGs through direct similarity comparison, without pair-dependent representation construction or candidate-wise LLM inference. Across four established EA benchmarks and two frozen LLM backbones, the best IRIS variants achieve Hits@1 scores of 100.00, 99.38, 98.31, and 97.99 on D-Y-15K V2, DBP-WIKI, ICEWS-WIKI, and ICEWS-YAGO, respectively.

## 3. TRWH: A Text-Driven Random Walk Heterogeneous GNN for Semantic-Aware Sparse Recommendation

- Authors: He Ma, Chen Liu
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-28
- DOI: Unavailable
- Categories: cs.AI, cs.MM
- Relevance: 3.318504048434394
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.25471v1
- PDF: https://arxiv.org/pdf/2607.25471v1
- Local PDF: pdf/2026-07-30_03_TRWH_ A Text-Driven Random Walk Heterogeneous GNN for Semantic-Aware Sparse Recommendation.pdf

Graph Neural Networks (GNNs) and Large Language Models (LLMs) have each advanced recommendation systems by modeling structural and semantic signals, respectively. However, integrating their complementary strengths remains challenging, particularly in sparse settings where maintaining semantic precision is critical. We propose TRWH (Text-driven Random Walk Heterogeneous Graph Neural Network), a novel framework that fuses LLM-generated textual profiles with heterogeneous graph structures through strategic random walk augmentation. TRWH consists of three core components: (1) Embedding Creation, which produces user and item representations using both Word2Vec and LLM-based profiling; (2) a Heterogeneous Graph Neural Network (HeteroGNN) that propagates information across multi-relational edges; and (3) Random Walk-based Path Construction, which enriches sparse graphs with second-order user-user and item-item links. Experiments on the Amazon-2023 Fashion (2M users, 825K items) and Beauty (631K users, 112K items) datasets demonstrate that TRWH achieves substantial performance gains over state-of-the-art methods, including 80.0% RMSE and 52.6% MAE reductions on Fashion, and 25.7% and 10.8% improvements on Beauty. Notably, while random walks improve performance with traditional embeddings, they can dilute the nuanced representations learned by LLMs, underscoring the importance of adaptive integration strategies.

## 4. HeAD-CP: Heterophily-Aware Diffused Conformal Prediction Sets for Graph Neural Networks

- Authors: Phan Binh Nguyen Lam, Nguyen Thai Anh
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-28
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.3080024423340824
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.25273v1
- PDF: https://arxiv.org/pdf/2607.25273v1
- Local PDF: pdf/2026-07-30_04_HeAD-CP_ Heterophily-Aware Diffused Conformal Prediction Sets for Graph Neural Networks.pdf

Conformal prediction (CP) provides distribution-free uncertainty quantification, and its extension to graphs is an active research direction. Diffused Adaptive Prediction Sets (DAPS) is a widely used graph-aware diffusion baseline, propagating Adaptive Prediction Sets (APS) non-conformity scores along edges with a uniform coefficient $λ$. We identify a fundamental shortcoming of this design: the uniform low-pass diffusion presupposes graph homophily and proves detrimental on heterophilic graphs, enlarging the mean prediction-set size by up to 10.6% relative to plain APS. To mitigate this, we propose HeAD-CP, a family of node-wise diffusion variants whose coefficients are determined by a label-free local-homophily estimate derived from the GNN softmax. Three variants, namely signed-$γ$, edge-compatibility, and a DAPS-baseline-with-correction, are most effective at extreme heterophily, intermediate heterophily, and moderate-to-high homophily, respectively, and all preserve the marginal coverage guarantee. On ten benchmarks, the HeAD-CP family stays at or below plain APS on every dataset, while DAPS exceeds APS on six. The post-hoc oracle over the family improves over DAPS on 8/10 datasets at $p<0.01$ (paired Wilcoxon), with the largest gains on heterophilic graphs (10.3% on Texas); on the two homophilic datasets where DAPS still wins (CiteSeer, PubMed), it retains a marginal advantage of at most 0.002, statistically insignificant on CiteSeer ($p=0.23$). Designing a calibrated label-free selector that approaches this oracle is the main outstanding empirical question.

## 5. Crystalis: Progressive Nucleation and Semantic Annealing for Coordinated Multi-View Visualization Generation

- Authors: Dazhen Deng, Zhaoping He, Xin Qian, Xiaotong Wang, Zi Ying, Yingcai Wu
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-06-07
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 3.3008014658163543
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.24766v1
- PDF: https://arxiv.org/pdf/2607.24766v1
- Local PDF: pdf/2026-07-30_05_Crystalis_ Progressive Nucleation and Semantic Annealing for Coordinated Multi-View Visualization Generation.pdf

Large language models (LLMs) can generate individual charts, but coordinated multi-view visualizations (CMVs), where views share data flows and cross-view interactions, remain out of reach. Tight field-level coupling among data transformations, visual encodings, and interaction coordinations causes errors in one component to silently invalidate others. Rather than pursuing end-to-end analytical quality, which depends on model capability, domain knowledge, and user expertise, we target a foundational question: can LLMs reliably produce structurally correct CMVs, and what abstractions make this possible? We present Crystalis, a framework built on query-centric CMV modeling that decomposes a CMV into structured queries over a dependency graph spanning three component types (Data, Visualization, Interaction) and three abstraction levels (requirement, specification, executable object). Two complementary mechanisms operate over this structure: progressive nucleation crystallizes each query vertically from requirement to object along the dependency order, while semantic annealing enforces horizontal consistency across queries at each level through layered logical checks. On a 12-task benchmark across five frontier LLMs, Crystalis achieves up to 75% end-to-end success, substantially outperforming an agentic coding baseline (8.3% E2E with the same foundation model), and a user study with 12 practitioners confirms the usability of the decomposition and iterative refinement workflow.

## 6. UDIST: unsupervised disentanglement of shape and texture for multi-scale phenotypic profiling in 2D microscopy

- Authors: Bosch, B. M., Terpstra, M. L., Smith, M. B., van der Steen, K. H., Jonker, C. T. H., Ovcinnikovs, V., Wesselink, T. H., Janssen, A. F. J., Winkel, L., Huigen, E. M. A., Lefferts, J. W., Mastrobattista, E., Elstak, E. D., van den Berg, C. A. T., Beekman, J. M., van Beuningen, S. F. B.
- Source: biorxiv
- Venue type: preprint
- Journal: biorxiv
- Publication status: preprint
- Publication date: 2026-07-29
- DOI: 10.64898/2026.07.26.740036
- Categories: bioinformatics
- Relevance: 3.1744167941477945
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://www.biorxiv.org/content/10.64898/2026.07.26.740036v1.full.pdf
- PDF: https://www.biorxiv.org/content/10.64898/2026.07.26.740036v1.full.pdf
- Local PDF: pdf/2026-07-30_06_UDIST_ unsupervised disentanglement of shape and texture for multi-scale phenotypic profiling in 2D microscopy.pdf

Microscopy-based phenotypic profiling relies increasingly on autonomous, unsupervised feature extraction, yet no existing method explicitly separates shape from texture into dedicated and independent latent subspaces by architectural design. Therefore texture, encoding critical biological information such as protein distribution and intracellular organisation, remains inaccessible as an independent feature domain in standard unsupervised approaches. This represents a fundamental limitation that prevents unbiased phenotypic analysis across biological scales. Here we introduce UDIST (Unsupervised Disentanglement of Shape and Texture), a sequential dual variational autoencoder (VAE) framework that tackles this fundamental limitation by explicitly decoupling shape from texture into independent, non-overlapping latent subspaces at the single-object level. By training two VICReg-regularised VAEs on principal-axis-aligned objects, UDIST separates binary shape from continuous texture information into rotation-invariant feature spaces, enabling separate downstream analysis of both domains. We validated UDIST across biological scales, from nuclei and single cells to patient-derived intestinal organoids, using both fluorescence and brightfield imaging, revealing phenotypic differences previously hidden by morphological variation and enabling the independent analysis of shape and texture in downstream analyses including clustering and similarity measurements. UDIST provides a versatile, label-free, and unsupervised tool for multi-scale phenotypic profiling in high-content microscopy and screening.

## 7. MODUS: Decoder-Only Any-to-Any Modeling of Diverse Modalities

- Authors: Mingqiao Ye, Zhaochong An, Zhitong Gao, Xian Liu, François Fleuret, Chuan Li, Amir Zadeh, Serge Belongie, Afshin Dehghan, Jesse Allardice, David Mizrahi, Oğuzhan Fatih Kar, Roman Bachmann, Amir Zamir
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-28
- DOI: Unavailable
- Categories: cs.CV, cs.AI, cs.LG
- Relevance: 3.174066789182661
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.25948v1
- PDF: https://arxiv.org/pdf/2607.25948v1
- Local PDF: pdf/2026-07-30_07_MODUS_ Decoder-Only Any-to-Any Modeling of Diverse Modalities.pdf

Any-to-any models predict any modality from any combination of others within a single network, a formulation used in multimodal vision and vision-language models, and increasingly in scientific domains such as ecology and astronomy. Existing any-to-any models are typically trained from scratch using encoder-decoder or diffusion architectures, impacting their performance and preventing them from using strong pre-trained decoder-only models as a prior. In this work, we investigate decoder-only any-to-any multimodal modeling, which treats all modalities symmetrically and supports arbitrary modalities as inputs and outputs without modality-specific heads, losses, or task pipelines. Because every modality is both an input and an output of the same model, the resulting model, named Modus, can support a range of applications, such as chained generation through intermediate modalities or cross-modal self-verification by scoring the model's own outputs with another generated modality. Modus demonstrates strong out-of-the-box performance and is competitive with specialist and multitask baselines using a single model across various benchmarks. All materials are open-sourced at https://modus-multimodal.epfl.ch/.

## 8. Domain-Prior-Regularized Graph Modeling for Anomaly Detection in Cyber-Physical Systems

- Authors: Youngseok Hwang, Joonsung Kwon, Geonwoo Lee, Hyunwoo Park
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-25
- DOI: Unavailable
- Categories: cs.LG, cs.AI
- Relevance: 3.1414436539897044
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.23197v1
- PDF: https://arxiv.org/pdf/2607.23197v1
- Local PDF: pdf/2026-07-30_08_Domain-Prior-Regularized Graph Modeling for Anomaly Detection in Cyber-Physical Systems.pdf

Anomaly detection on multivariate sensor time series is critical for industrial monitoring of cyber-physical systems (CPS), where even subtle deviations from normal behavior can indicate process disruption. Recent graph-based approaches have made significant progress, but they often struggle in small-scale physical systems with scarce labeled anomalies and limited normal data. In such settings, graph-based models tend to capture spurious correlations and produce unstable sensor topologies. We propose DPR-GM (Domain-Prior-Regularized Graph Modeling), a forecasting-based framework that incorporates system design knowledge into graph construction. DPR-GM leverages a large language model (LLM) to extract directed physical couplings between sensor pairs from system documentation, which are encoded as a binary domain adjacency matrix serving as a structural gate over sensor relations. This gate is then modulated by Pearson correlations estimated from normal training data. The anomaly score is further weighted by sensor-level reliability derived from the coefficient of variation. All graph and weighting components are fixed prior to training and add no learnable parameters. On the SKAB benchmark, DPR-GM outperforms graph-based, statistical, and deep learning baselines across F1, AUROC, and AUPRC, showing that domain-structured graph priors are a practical alternative to fully learned topologies in data-scarce CPS.

## 9. OrganLens: Organ-Specific Representation Learning for CT Foundation Models

- Authors: Zhixuan Ge, Anqi Li, Sadeer Al-Kindi, Hanwen Xu, Wei Qiu
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-28
- DOI: Unavailable
- Categories: cs.CV, cs.AI
- Relevance: 3.119863921148909
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.25164v1
- PDF: https://arxiv.org/pdf/2607.25164v1
- Local PDF: pdf/2026-07-30_09_OrganLens_ Organ-Specific Representation Learning for CT Foundation Models.pdf

A CT examination captures multiple organs, but many biomedical questions concern abnormalities, prognosis, or longitudinal change in a specific organ. These questions require a separate representation for each organ within the same CT volume. Existing CT foundation models commonly produce a single volume-level representation, while recent anatomy-aware methods either encode pre-separated organ volumes or explicitly disentangle images into organ token groups. The former may remove clinically relevant surrounding context, while the latter does not condition a shared encoder on a selected organ before its features are formed. We introduce OrganLens for organ-specific representation learning through self-supervision. An organ identity conditions a shared CT encoder, while organ-specific distillation and anatomy-mask supervision shape features for anatomy-weighted pooling into organ-specific representations. At inference, the shared model produces 11 organ-specific representations without external segmentation masks. We evaluate OrganLens on CT-RATE, RAD-ChestCT, INSPECT, and NLST across diverse acquisitions and downstream evaluations. Relative to CT-pretrained DINOv2, heart representations raise CT-RATE cardiomegaly AUROC from 0.910 to 0.953, while lung representations improve the Harrell C-index for NLST lung-cancer mortality by 14.2\%. The global representation reaches INSPECT Recall@10 of 33.09\% and 32.04\% for text-to-image and image-to-text retrieval, respectively. Across organ-related tasks, anatomically matched representations provide stronger task-relevant signal, while the global representation retains broad utility. OrganLens offers a scalable approach to organ-specific CT representation learning with a shared encoder. More broadly, it provides the medical research community with a reusable framework for studying organ-specific disease across cohorts and clinical endpoints.

## 10. Beyond Counts: A Distributional Robustness Margin For Pathology Foundation Models

- Authors: Clément Grisi, Jeroen van der Laak, Geert Litjens
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-28
- DOI: Unavailable
- Categories: cs.CV, cs.AI
- Relevance: 3.0835084423920627
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.25497v1
- PDF: https://arxiv.org/pdf/2607.25497v1
- Local PDF: pdf/2026-07-30_10_Beyond Counts_ A Distributional Robustness Margin For Pathology Foundation Models.pdf

Pathology foundation models are approaching clinical deployment, yet remain vulnerable to systematic non-biological variation across centres. Differences in tissue preparation, staining and scanning are strongly encoded in their representations, enabling shortcut learning and weakening generalisation across cohorts and institutions. The Robustness Index (RI) quantifies whether local representation geometry is dominated by biology or by non-biological variation, but its count-based formulation discards distance information. We show that adding distance weights changes little because the deeper limitation lies in RI's pooled, fixed-neighbourhood design, which obscures sample-level heterogeneity and effectively evaluates only a model-dependent subset of samples. We introduce the Cross-confounder Robustness Margin (CRoMa), a sample-resolved measure that directly compares distances to cross-confounder biological matches and same-confounder biological distractors. CRoMa recasts robustness as a cohort-wide margin distribution rather than a single pooled score. We evaluated frozen representations from 20 tile-level encoders across three benchmarks and 4 slide-level encoders on a fourth. Rankings by median CRoMa were broadly consistent across datasets, while the underlying distributions revealed substantial within-model heterogeneity. Every tile encoder retained a confounder-dominated lower tail, whose prevalence and severity varied markedly across models. These distinct robustness profiles frame model selection as a Pareto trade-off between typical and lower-tail robustness. Higher CRoMa was also associated with smaller shortcut-induced performance drops after supervised adaptation. By turning representation geometry into a distributional robustness readout that anticipates downstream shortcut susceptibility, CRoMa provides a principled basis for robustness assessment and model selection.

## 11. Gradient-Based Latent Decomposition Reveals Mechanisms of Feature Degradation in Weakly Supervised Mammography

- Authors: Vinceline Bertrand, Ionut Cardei
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-24
- DOI: Unavailable
- Categories: cs.CV, cs.LG
- Relevance: 3.0709810738403984
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.24835v1
- PDF: https://arxiv.org/pdf/2607.24835v1
- Local PDF: pdf/2026-07-30_11_Gradient-Based Latent Decomposition Reveals Mechanisms of Feature Degradation in Weakly Supervised Mammography.pdf

Weakly supervised hierarchical models exhibit a persistent asymmetry: coarse lesion-type features are preserved under reconstruction while fine-grained malignancy cues degrade---a pattern with direct consequences for the clinical reliability of breast cancer screening pipelines. We introduce gradient-based orthogonal latent decomposition for hierarchical Variational Autoencoders~(H-VAEs) to mechanistically explain this asymmetry. The latent space is partitioned into a task-aligned component~($z_1$), shaped by coarse supervisory gradients, and an orthogonal residual~($z_{\text{res}}$) capturing remaining representational capacity. On~3,550 mammographic Regions of Interest~(ROIs) from CBIS-DDSM, only~$\sim$4.4\% of latent magnitude aligns with supervisory gradients, leaving~$\sim$95.6\% in the orthogonal residual upon which fine-grained pathology prediction primarily depends. The model achieves Stage-1~AUC~0.866 and Stage 2~AUC~0.552, with a reconstruction stability gap of $Δ_{\text{diag}}=5\%$ ($p=0.005$) and a classification gap of $Δ_{\text{AUC}}=0.314$ ($p{<}0.001$). Latent ablation confirms that features for both tasks reside heavily in~$z_{\text{res}}$, structurally explaining why reconstruction degrades pathology stability disproportionately. Comparisons with Multi-Instance Learning~(MIL) and Multi-Task Learning~(MTL) confirm generalization across architectures and modalities. These findings reveal that in high-dimensional spaces, a single coarse supervisory signal isolates only a sparse 1D latent direction, forcing critical fine-grained features into the vulnerable residual subspace.

## 12. Transfer Learning in High-Dimensional Clustering: Minimax Thresholds and Applications in Single-Cell Data

- Authors: Abhinav Chakraborty, Sagnik Nandy
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-27
- DOI: Unavailable
- Categories: math.ST, stat.ME, stat.ML
- Relevance: 3.061224730529799
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.25031v1
- PDF: https://arxiv.org/pdf/2607.25031v1
- Local PDF: pdf/2026-07-30_12_Transfer Learning in High-Dimensional Clustering_ Minimax Thresholds and Applications in Single-Cell Data.pdf

Clustering is a fundamental problem in statistics, with applications across many scientific disciplines. In many modern applications involving clustering, the primary dataset (the target data) is accompanied by related datasets (the source data). Transferring information from such sources may improve clustering accuracy in the target, making transfer learning for clustering practically important. Despite recent progress, the conditions under which source data improve target clustering remain unclear in high-dimensional settings, even for the canonical Gaussian mixture model. In this paper, we study the clustering problem in a two-community Gaussian mixture model where relatedness is captured by the geometric alignment of the target and source cluster means. We develop a minimax-optimal transfer-assisted clustering procedure and characterize, up to logarithmic factors, the phase transition for consistent target clustering in terms of the signal-to-noise ratios, sample sizes, ambient dimension, and degree of alignment between the datasets. The technique is also extended to adaptively choose between the target-only or the source assisted clustering depending on the target signal strength. Furthermore, we also extend our techniques to accommodate multiple communities and and multiple source datasets. Extensive simulations and an analysis of a human lung single-cell RNA-sequencing atlas demonstrate the practical effectiveness of our methods.

## 13. From Training to Deployment: Post-Hoc Causal Feature Identification via Sensitivity Ratios

- Authors: Athanasios Vlontzos, Giorgos Papanastasiou, Bernhard Kainz, Sotirios Tsaftaris
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-28
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 3.0519774377958204
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.25546v1
- PDF: https://arxiv.org/pdf/2607.25546v1
- Local PDF: pdf/2026-07-30_13_From Training to Deployment_ Post-Hoc Causal Feature Identification via Sensitivity Ratios.pdf

Given a model that is already trained, which features does it rely on causally versus spuriously? Existing methods require access to the training procedure and cannot answer this post-hoc. We introduce the \textbf{Normalised Sensitivity Ratio~(NSR)}, a post-hoc, model-agnostic diagnostic for this question under a structured-shift regime: environments differ primarily in the mean of spurious features while the causal mechanism and causal marginals remain stable, as in multi-site clinical data or multi-batch genomics. Within this regime, causal features induce constant model sensitivity across environments while spurious features track shift. NSR formalises this as the squared coefficient of variation of per-environment sensitivity. Under a linear structural causal model (SCM) with $K\ge3$ non-degenerate environments, NSR achieves exact identification (Theorem~1). We fully characterise failure: weak shifts ($O(\varepsilon^4)$ collapse), degenerate geometry, and proxy attenuation ($O((1-α)^4)$), giving practitioners quantitative criteria for assessing whether the regime holds. Finite-sample rates are $O_p(n^{-1})$ under the null and $O_p(n^{-1/2})$ under the alternative. Experiments confirm all theoretical predictions on synthetic data (area under the ROC curve [AUROC] $= 1.000$ under conditions satisfying the regime), show consistent rankings across five model families (Kendall $τ\ge0.529$), and recover six of eight causal features on bike-sharing data (Precision@7 $= 0.75$) without modifying any trained model.

## 14. When Does Deep Representation Learning Help Single-Cell Clustering? A Sensitivity-Aware Diagnostic Benchmark for Biomedical AI Pipelines

- Authors: Nguyen Thanh Phong, Truong Viet Vu, Nguyen Ha Thu, Tran An Ky, Tran Hoang Thong, Le Pham Thuy Hien, Nguyen Thai Anh
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-28
- DOI: Unavailable
- Categories: cs.LG, q-bio.GN
- Relevance: 3.0382481336882305
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.25288v1
- PDF: https://arxiv.org/pdf/2607.25288v1
- Local PDF: pdf/2026-07-30_14_When Does Deep Representation Learning Help Single-Cell Clustering_ A Sensitivity-Aware Diagnostic Benchmark for Biomedi.pdf

Single-cell ribonucleic acid sequencing (scRNA-seq) is a foundational technology for precision-medicine workflows that contribute to United Nations Sustainable Development Goal 3 on Good Health and Well-being, and unsupervised clustering is the analytical step that turns raw expression matrices into interpretable cell populations. Practitioners therefore face a recurring engineering decision: is an additional deep representation stage worth its compute and tuning cost, or do classical principal component analysis (PCA) pipelines already suffice? We address this question with a diagnostic benchmark of nine clustering pipelines on ten real datasets (90-5,685 cells, 19,046-41,480 genes, 4-11 cell types), augmented by a partial scVI V2 specialized comparison on seven datasets. The protocol integrates Optuna hyperparameter search, repeated-run robustness, Friedman/Wilcoxon-Holm/TOST testing, and Sobol total-order sensitivity analysis. The contrastive autoencoder achieved the highest mean Adjusted Rand Index (0.7872), but Holm-corrected tests did not establish dominance over the strongest baselines. Per-dataset analysis reveals three reproducible regimes: probabilistic variational autoencoder (VAE) variants help on the smallest datasets, deep autoencoders win on mid-scale data with multi-batch or many-type structure, and classical PCA pipelines remain competitive when linear projection already captures the dominant variation. Sobol indices identify learning rate ($S_T=0.70$) and latent dimensionality ($S_T=0.56$) as the dominant variance contributors, indicating where limited tuning budgets should be allocated. The contribution is therefore a dataset-aware and compute-conscious decision framework for biomedical AI pipelines supporting sustainable healthcare analytics, rather than a universal superiority claim.

## 15. Multimodal Hybrid Retrieval-Augmented Generation for Scientific Document Understanding using Open-Source SLMs

- Authors: Alexandru-Andrei Saucă, Ana-Luiza Rusnac
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-06
- DOI: Unavailable
- Categories: cs.IR, cs.AI
- Relevance: 2.9966549657797152
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.24799v1
- PDF: https://arxiv.org/pdf/2607.24799v1
- Local PDF: pdf/2026-07-30_15_Multimodal Hybrid Retrieval-Augmented Generation for Scientific Document Understanding using Open-Source SLMs.pdf

Large Language Models tend to hallucinate when answering domain-specific ques tions from scientific documents without prior fine-tuning. Currently, methods such as Retrieval-Augmented Generation partially solve this problem but face different challenges: limited context knowledge, difference between sparse and dense retrieval, and retrieval noise. This paper presents an Advanced Multimodal Retrieval-Augmented Generation system that aims to solve those challenges and im prove the accuracy of information extraction. The proposed architecture introduces a multimodal ingestion pipeline that leverages an open-source Vision-Language Model (Qwen2-VL-2B-Instruct) to generate textual summaries of tables and fig ures. The retrieval phase integrates HNSW-based semantic search with GIN-based lexical search, unified through Reciprocal Rank Fusion and refined using Cross Encoder reranking to minimize retrieval noise. To ensure conversational coherence across multi-turn interactions, a Query Condenser module is employed. Evaluation is conducted by independently assessing the ingestion, retrieval and generation stages using the MMLongBench benchmark, a BeIR-format synthetic dataset and the DeepEval framework. Moreover, results demonstrate a 157% improvement in retrieval quality over a Naive-RAG baseline, with only 50 ms additional la tency, while Qwen2-VL-2B-Instruct achieved results comparable to cloud-based models in BERTScore. These findings validate that open-source optimized SLMs, paired with advanced retrieval strategies, can provide competitive performance for document understanding without relying on cloud-based models.

## 16. Chart-Supported or Model-Supplied? Examining MLLM-Generated Claims for Accessible Visualization

- Authors: Ishrat Jahan Eliza, Md Dilshadur Rahman
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-27
- DOI: Unavailable
- Categories: cs.AI, cs.HC, cs.MA, cs.SE
- Relevance: 2.9771159935671854
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.25021v1
- PDF: https://arxiv.org/pdf/2607.25021v1
- Local PDF: pdf/2026-07-30_16_Chart-Supported or Model-Supplied_ Examining MLLM-Generated Claims for Accessible Visualization.pdf

Multimodal large language models (MLLMs) can connect visualization patterns to external causes, consequences, and domain knowledge, but the evidential basis of these interpretations is often unclear. We present an exploratory study of 102 visualizations from four sources, three MLLMs, and four input conditions that vary access to the image, source-specific accessible chart context, and withheld-context framing. Across 1,224 descriptions, we analyze model-attributed DIRECT, DERIVED, and SPECULATIVE labels and conduct an automated audit of numeric agreement. Accessible chart context shifted Gemini and GPT toward DIRECT claims and improved numeric agreement for some models. Adding the image to the full context did not yield a consistent numeric benefit, and the withheld-context prompt did not reliably increase cautious language. The prompt-defined Real-World Significance section remained predominantly SPECULATIVE. These results motivate accessible description systems that distinguish claims supported by supplied evidence from model-supplied interpretation

## 17. Tools Are Not Islands: Set-Level Tool Retrieval for LLM Agents via Query-Conditioned Hyperedge Prediction

- Authors: Xinyi Hong, Pinjun Dong, Xinyang Yu, Binyan Jiang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-28
- DOI: Unavailable
- Categories: cs.LG, cs.AI, cs.IR
- Relevance: 2.970664124665079
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.25718v1
- PDF: https://arxiv.org/pdf/2607.25718v1
- Local PDF: pdf/2026-07-30_17_Tools Are Not Islands_ Set-Level Tool Retrieval for LLM Agents via Query-Conditioned Hyperedge Prediction.pdf

Large language model (LLM) agents increasingly rely on invoking external tools to complete real-world tasks. Tool retrieval, which selects a small task-relevant subset from a library of thousands of tools before the agent acts, has therefore become a critical component of LLM agent pipelines. However, existing retrievers either score each tool in isolation or assemble the tool set sequentially, so the joint utility of a candidate set is never evaluated as a whole. In this paper, we propose HYSET, short for HYperedge-based SEt-level Tool retrieval. Our contributions are threefold: (i) we formulate tool retrieval as query-conditioned hyperedge prediction on a tool co-invocation hypergraph, under which the tool set itself becomes the unit of scoring and most existing retrieval paradigms reduce to restricted instances; (ii) we capture size-dependent tool compatibility through cardinality-specific interactions; and (iii) we design HYSET as a pre-selection module requiring no modification to the downstream agent. Experiments on ToolBench demonstrate that HYSET consistently outperforms state-of-the-art baselines in both tool retrieval performance and end-to-end task success. Beyond the in-domain setting, HYSET further supports zero-shot/few-shot transfer, generalizing to held-out tools/categories and unseen domains with minimal supervision.

## 18. Can Deep Generative Models Reproduce Non-Stationary Gaussian Random Fields?

- Authors: Daniel Kua, Yan Song
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-28
- DOI: Unavailable
- Categories: stat.ML, cs.LG
- Relevance: 2.9651360395903934
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.25929v1
- PDF: https://arxiv.org/pdf/2607.25929v1
- Local PDF: pdf/2026-07-30_18_Can Deep Generative Models Reproduce Non-Stationary Gaussian Random Fields.pdf

Deep generative models (DGMs) are widely used for complex high-dimensional data and increasingly applied to spatial and spatio-temporal modeling. Their generated samples implicitly represent the learned data distribution and associated uncertainty. However, for real-world data, assessing whether DGMs have learned the underlying process is difficult because the ground truth is unknown and evaluation often relies on observations alone. We evaluate representative DGMs, flow matching (FM), DDPM, score-SDE, and VAE, on a known non-stationary Gaussian random field. This paper provides comprehensive metrics to assess recovery of the ground-truth mean and covariance structures, with oracle samples and a stationary control as references. All four models recover the mean surface, while their covariance recovery differs across model families: DDPM and score-SDE recover the covariance structure reasonably well, FM exhibits mildly attenuated non-stationarity and slight variance under-dispersion, and VAE has difficulty recovering the covariance structure. An experiment on ERA5 temperature anomalies further demonstrates how the framework can support the validation and development of DGMs for complex real-world spatio-temporal data.

## 19. ScalableRAG: High-Quality RAG at Zero Ingestion Cost

- Authors: Hilaf Hasson, Aditya Chakravarty, Jayant Thomas, Krishna Gogineni
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-27
- DOI: Unavailable
- Categories: cs.AI, cs.LG
- Relevance: 2.9618548541640575
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.25135v1
- PDF: https://arxiv.org/pdf/2607.25135v1
- Local PDF: pdf/2026-07-30_19_ScalableRAG_ High-Quality RAG at Zero Ingestion Cost.pdf

Recent advances in RAG aim to optimize for performance by paying high ingestion costs for knowledge ingestion: building knowledge graphs or extracting SQL tables. In this work we show that the operations that such knowledge bases allow can be replicated with zero ingestion costs (not even a vector database); in fact our solution, Zero-Ingestion ScalableRAG, handily out-performs all baselines (including knowledge graph approaches) in three out of the six corpora considered here, and only marginally missing maximum performance on the other three, with average accuracy across all six datasets 7.36% above the next most competitive baseline. It achieves this by keeping a workspace of document sets and values sets that it can write into and read from, allowing for on-the-fly aggregative reasoning in all situations where grouping is required on a primary key that is in one to one correspondence with a subset of the total document set.
  Capping the number of LLM calls by a constant independent of the corpus size, we also introduce Limited-Ingestion ScalableRAG, which does use a minimal vector database as well as an automated pattern discovery from a sample of documents, to further improve accuracy at scale. Our code is available at https://github.com/cohesity/ScalableRAG .

## 20. HiSkill: Empowering LLM Agents with Hierarchical Skill Graphs

- Authors: Yu Hao, Jinxuan Cai, Qi Zhang, Yawen Li, Zhiqiang Zhang, Chuan Shi, Cheng Yang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-28
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 2.956592652153522
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.25853v1
- PDF: https://arxiv.org/pdf/2607.25853v1
- Local PDF: pdf/2026-07-30_20_HiSkill_ Empowering LLM Agents with Hierarchical Skill Graphs.pdf

Skills have become an important abstraction for enabling large language model (LLM) agents to reuse past experience in long-horizon interactive tasks. However, existing trajectory-to-skill methods often produce flat collections of high-level textual skills that are stored and retrieved independently, leaving skill relations underutilized and maintaining a gap between high-level skills and executable actions. In this paper, we propose HiSkill, a hierarchical skill graph framework that organizes interaction trajectories into a directed graph with skill nodes, AtomicOp nodes, and typed edges. Specifically, the graph connects reusable high-level skills with executable action templates, while also capturing decomposition, temporal transition, compatibility, support, and recovery relations among them. At inference time, HiSkill retrieves a compact task-relevant subgraph and performs subgraph-guided task execution, where a symbolic task state, an active skill, and the retrieved subgraph guide the LLM agent to switch skills, select AtomicOps, and ground executable actions iteratively. Experiments on three interactive environments show that HiSkill outperforms state-of-the-art baselines while reducing inference token consumption, demonstrating the effectiveness of bridging high-level skills and executable action grounding through a hierarchical skill graph. Our data and code is available at https://github.com/BUPT-GAMMA/HiSkill.

## 21. OmniPhys: Knowledge-Graph-Driven Benchmarking and Collective Optimization for Physical Commonsense in Text-to-Image Generation

- Authors: Yajing Xu, Yarong Lan, Jiaoyan Chen, Yichi Zhang, Jeff Z. Pan, Mingchen Tu, Zhizhen Liu, Wen Zhang, Huajun Chen
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-28
- DOI: Unavailable
- Categories: cs.CV, cs.AI
- Relevance: 2.954062207545365
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.25641v1
- PDF: https://arxiv.org/pdf/2607.25641v1
- Local PDF: pdf/2026-07-30_21_OmniPhys_ Knowledge-Graph-Driven Benchmarking and Collective Optimization for Physical Commonsense in Text-to-Image Gene.pdf

While text-to-image models exhibit remarkable visual fidelity, they frequently violate fundamental physical commonsense. Existing benchmarks often rely on coarse-grained descriptions, failing to diagnose the mastery of specific physical principles. Moreover, the high stochasticity of generative processes causes current prompt optimization methods to suffer from gradient hallucinations, where optimizers are misled by transient visual artifacts rather than systemic flaws. To address these challenges, we introduce OmniPhys, a rigorous benchmark of 1,551 samples grounded in a Physical Knowledge Graph. By aligning PhET simulations with standard curricula, OmniPhys operationalizes a knowledge-to-scenario pipeline that performs diagnostic stress tests via a dual-path verification protocol. We further propose OmniPrompt, an iterative framework that treats physical alignment as a discrete optimization problem. For each query, OmniPrompt aggregates K stochastic images into a per-query feedback buffer. Across training, it further merges feedback from batches of B queries before each meta-policy update, filtering seed and query-local noise. Evaluations across 12 representative text-to-image models reveal universal physical bottlenecks. Results demonstrate that OmniPrompt significantly enhances physical consistency across diverse backbones, proving the transferability and efficacy of our evolved meta-policies. The code and data are available at https://github.com/zjukg/OmniPhys

## 22. Detecting Knowledge Inconsistencies Across Text, Tables, and Knowledge Graphs

- Authors: Fanfu Wei, Thibault Ehrhart, Raphaël Troncy
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-28
- DOI: Unavailable
- Categories: cs.CL, cs.AI
- Relevance: 2.9337605139593688
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.25959v1
- PDF: https://arxiv.org/pdf/2607.25959v1
- Local PDF: pdf/2026-07-30_22_Detecting Knowledge Inconsistencies Across Text, Tables, and Knowledge Graphs.pdf

Wikipedia and Wikidata are widely used for information access, LLM pre-training, and retrieval-augmented generation. Their knowledge is deeply connected but scattered across text, tables, and knowledge graphs. This raises a practical question: when these modalities disagree, how can we detect and explain the conflict? We study this problem as \emph{modality-level inconsistency detection}. We first introduce a taxonomy of cross-modal knowledge inconsistencies, covering information granularity differences, direct conflicts, temporal changes, and KG incompleteness. We then present \textsc{Kontrast}, an automatic framework that uses Text-to-SPARQL and LLM reasoning to compare table-based answers with KG evidence and categorize the resulting inconsistencies. Experiments on various Table-QA datasets show that cross-modal inconsistencies are common and informative. They reveal not only true knowledge conflicts, but also missing KG structure and temporal mismatches while being limited by Text-to-SPARQL errors and noise. Our analysis shows that text, tables, and KGs can complement and correct one another through systematic comparison. \textsc{Kontrast} provides a practical tool for large-scale knowledge auditing and establishes a benchmark for future work on cross-modal knowledge consistency. Code and data are available at https://github.com/ECLADATTA/KONTRAST.

## 23. FORGE: Frame Orthogonality in Relevance Geometry for Long-Form Video Understanding

- Authors: Ghazal Kaviani, Ghassan AlRegib
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-28
- DOI: Unavailable
- Categories: cs.CV, cs.LG
- Relevance: 2.932574616432726
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.25266v1
- PDF: https://arxiv.org/pdf/2607.25266v1
- Local PDF: pdf/2026-07-30_23_FORGE_ Frame Orthogonality in Relevance Geometry for Long-Form Video Understanding.pdf

Multimodal large language models (MLLMs) have enabled long-form video understanding at a scale that was not previously possible. However, the density of relevant content decreases sharply as video sequence length increases, and exposing the model to more irrelevant content measurably reduces its accuracy. In this paper, we address the problem of maximizing query-relevant information in a frame subset selected at inference time, without training. FORGE (Frame Orthogonality in Relevance Geometry) is a model-agnostic method that induces a query-conditioned geometry on a pretrained multimodal embedding space, unifying relevance and diversity into a single objective. In this space, frames that cover independent query-relevant directions are far apart, and selecting the subset of maximum information captures diverse query-relevant content within the budget. Experiments on Video-MME and LongVideoBench at budgets of 16, 32, and 64 frames show that FORGE improves the unified keyframe selection score by 11.0-15.3 points over the strongest training-free baseline and up to doubles keyframe recall (0.415 vs. 0.204 at K=64 on Video-MME). The gains extend to question answering, where accuracy improves in every evaluated setting across eight open-source MLLMs spanning 4B to 32B parameters, by up to 8.7 points over uniform sampling and 5.2 points over the strongest baseline. Our findings suggest that aligning the embedding space with the query's high-dimensional structure is a promising direction for inference-time video understanding.

## 24. MemSFT: Mitigating Alignment Tax with an External Parametric Memory

- Authors: Jiarui Wang, Xiang Shi, Jiaqi Cao, Rubin Wei, Xiquan Wang, Hao Sun, Jingzhi Wang, Zhiqi Yang, Qipeng Guo, Bowen Zhou, Zhouhan Lin
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-28
- DOI: Unavailable
- Categories: cs.LG, cs.CL
- Relevance: 2.9216542754829082
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.25614v1
- PDF: https://arxiv.org/pdf/2607.25614v1
- Local PDF: pdf/2026-07-30_24_MemSFT_ Mitigating Alignment Tax with an External Parametric Memory.pdf

Adapting Large Language Models (LLMs) to specialized domains often incurs an alignment tax, as fine-tuning on domain-specific tasks can cause catastrophic forgetting and substantially degrade performance on general tasks. We propose MemSFT, which mitigates the alignment tax by decoupling domain specialization from backbone parameter updates through a plug-and-play parametric memory. The memory is trained to imitate the behavior of a non-parametric retriever operating over domain data, thereby memorizing knowledge and patterns that would otherwise be accessed through retrieval. Once trained on a specific domain, the memory can be reused across LLMs of different sizes. During generation, a learned router dynamically fuses the output distributions of the memory and backbone at each decoding step, allowing domain expertise to be invoked selectively. Across biology, geoscience, and law, evaluations with models ranging from Qwen3-8B to Qwen3-235B-A22B show that MemSFT consistently improves domain performance with negligible degradation in general performance, whereas full SFT suffers severe forgetting on general tasks. Overall, our results demonstrate a practical path to decoupling general model capabilities from domain-specific knowledge at the parameter level, thereby equipping LLMs with new specialized capabilities without compromising their general capabilities.

## 25. LEPO: Latent Reasoning Policy Optimization for Large Language Models

- Authors: Yuyan Zhou, Jiarui Yu, Hande Dong, Zhezheng Hao, Hong Wang, Jianqing Zhang, Qiang Lin
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.9088590212860286
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.707/
- PDF: https://aclanthology.org/2026.findings-acl.707.pdf
- Local PDF: pdf/2026-07-30_25_LEPO_ Latent Reasoning Policy Optimization for Large Language Models.pdf

Recently, latent reasoning has been introduced into large language models (LLMs) to leverage rich information within a continuous space.However, without stochastic sampling, these methods inevitably collapse to deterministic inference, failing to discover diverse reasoning paths.To bridge the gap, we inject controllable stochasticity into latent reasoning via Gumbel-Softmax, restoring LLMs’ exploratory capacity and enhancing their compatibility with Reinforcement Learning (RL).Building on this, we propose L atent R e asoning P olicy O ptimization ( LEPO ), a novel framework that applies RL directly to continuous latent representations.Specifically, in rollout stage, LEPO maintains stochasticity to enable diverse trajectory sampling, while in optimization stage, LEPO constructs a unified gradient estimation for both latent representations and discrete tokens.

## 26. VCORE: Variance-Controlled Optimization-based Reweighting for Chain-of-Thought Supervision

- Authors: Xuan Gong, Senmiao Wang, Hanbo Huang, Ruoyu Sun, Shiyu Liang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.89588983443772
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1298/
- PDF: https://aclanthology.org/2026.acl-long.1298.pdf
- Local PDF: pdf/2026-07-30_26_VCORE_ Variance-Controlled Optimization-based Reweighting for Chain-of-Thought Supervision.pdf

Supervised fine-tuning (SFT) on long chain-of-thought (CoT) trajectories has emerged as a crucial technique for enhancing the reasoning abilities of large language models (LLMs). However, the standard cross-entropy loss treats all tokens equally, ignoring their heterogeneous contributions across a reasoning trajectory. This uniform treatment leads to misallocated supervision and weak generalization, especially in complex, long-form reasoning tasks. To address this, we introduce V ariance- C ontrolled O ptimization-based RE weighting (VCORE), a principled framework that reformulates CoT supervision as a constrained optimization problem. By adopting an optimization-theoretic perspective, VCORE enables a principled and adaptive allocation of supervision across tokens, thereby aligning the training objective more closely with the goal of robust reasoning generalization. Empirical evaluations demonstrate that VCORE achieves the strongest overall average performance, with especially clear gains on lower-capacity models. Across both in-domain and out-of-domain settings, VCORE achieves substantial performance gains on mathematical and coding benchmarks, using models from the Qwen3 series (4B, 8B, 32B) and LLaMA-3.1-8B-Instruct. Moreover, we show that VCORE serves as a more effective initialization for subsequent reinforcement learning, establishing a stronger foundation for advancing the reasoning capabilities of LLMs.

## 27. When Thinking Before Retrieval Hurts: TraceBound Diagnostics for Adaptive Knowledge-Graph Retrieval

- Authors: Partha Sarathi Purkayastha
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-06
- DOI: Unavailable
- Categories: cs.IR, cs.AI, cs.CL
- Relevance: 2.892698652802613
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.24800v1
- PDF: https://arxiv.org/pdf/2607.24800v1
- Local PDF: pdf/2026-07-30_27_When Thinking Before Retrieval Hurts_ TraceBound Diagnostics for Adaptive Knowledge-Graph Retrieval.pdf

Adaptive retrieval promises to make knowledge-graph question answering more robust by letting a controller search, inspect neighborhoods, revise actions, and stop when evidence is sufficient. We study this premise by introducing TraceBound, a lightweight profile- and trace-conditioned diagnostic protocol for an ARK-style retriever on text-rich knowledge graphs. TraceBound exposes a compact query profile before retrieval, issues short trace hints after observable failure symptoms, and logs trajectory counters, while keeping graph data, tools, gold labels, and ranking metrics fixed. Across STaRK validation and held-out subsets, the added conditioning improves inspectability but consistently reduces retrieval quality under open-weight controllers. Paired trajectory analysis localizes the degradation to repeated calls, zero-result calls, and misallocated exploration budget, while stricter interaction budgets shorten trajectories without repairing the policy. The result diagnoses the common failure mode in that "thinking before retrieval'' must be evaluated as a control problem over action selection, not as a prompt-format change.

## 28. GLIDE: Guided Layerwise Hybrid Attention for Efficient LLM Inference

- Authors: Vimal William, Ravi Tandon, Jyotikrishna Dass
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-06-26
- DOI: Unavailable
- Categories: cs.AI, cs.CL, cs.LG
- Relevance: 2.8794508693441188
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.24788v1
- PDF: https://arxiv.org/pdf/2607.24788v1
- Local PDF: pdf/2026-07-30_28_GLIDE_ Guided Layerwise Hybrid Attention for Efficient LLM Inference.pdf

As Large Language Models scale to increasingly long contexts, the memory I/O and computational overhead of the Key-Value (KV) cache during decoding emerges as the primary throughput bottleneck. To address this, we propose GLIDE, a Guided Layerwise Hybrid Attention that strategically integrates sliding-window softmax attention with linear recurrent aggregation. GLIDE is motivated by layer-wise heterogeneity: early layers exhibit high sensitivity to softmax removal, while deeper layers demonstrate redundancy and tolerate aggressive replacement by linear alternatives. Leveraging this insight, GLIDE introduces a layer-wise adaptive mechanism wherein each layer balances an efficient linear recurrence with a variable-sized softmax window. Unlike uniform hybrid approaches, GLIDE non-uniformly compresses the softmax footprint across the model, reducing aggregate KV cache I/O while preserving expressive power where most vital. Empirical evaluations demonstrate the GLIDE achieves superior performance-efficiency tradeoffs, reducing end-to-end latency for long-context generation without compromising quality.

## 29. From Storage to Experience: A Survey on the Evolution of LLM Agent Memory Mechanisms

- Authors: Jinghao Luo, Yuchen Tian, Chuxue Cao, Ziyang Luo, Hongzhan Lin, Kaixin Li, Chuyi Kong, Ruichao Yang, Jing Ma
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.8770895888177934
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.2069/
- PDF: https://aclanthology.org/2026.findings-acl.2069.pdf
- Local PDF: pdf/2026-07-30_29_From Storage to Experience_ A Survey on the Evolution of LLM Agent Memory Mechanisms.pdf

Large Language Model (LLM)-based agents have fundamentally reshaped artificial intelligence by integrating external tools and planning capabilities. While memory mechanisms have emerged as the architectural cornerstone of these systems, current research remains fragmented, oscillating between operating system engineering and cognitive science. This theoretical divide prevents a unified view of technological synthesis and a coherent evolutionary perspective. To bridge this gap, this survey proposes a novel evolutionary framework for LLM agent memory mechanisms, formalizing the development process into three stages: Storage (trajectory preservation), Reflection (trajectory refinement), and Experience (trajectory abstraction). We first formally define these three stages before analyzing the three core drivers of this evolution: the necessity for long-range consistency, the challenges in dynamic environments, and the ultimate goal of continual learning. Furthermore, we specifically explore two transformative mechanisms in the frontier Experience stage: proactive exploration and cross-trajectory abstraction. By synthesizing these disparate views, this work offers robust design principles and a clear roadmap for the development of next-generation LLM agents.

## 30. HEALing Entropy Collapse: Enhancing Exploration in Few-Shot RLVR via Hybrid-Domain Entropy Dynamics Alignment

- Authors: Zhanyu Liu, Qingguo Hu, Ante Wang, Chenqing Liu, Zhishang Xiang, Hui Li, Delai Qiu, Jinsong Su
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.8701383297851746
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1418/
- PDF: https://aclanthology.org/2026.acl-long.1418.pdf
- Local PDF: pdf/2026-07-30_30_HEALing Entropy Collapse_ Enhancing Exploration in Few-Shot RLVR via Hybrid-Domain Entropy Dynamics Alignment.pdf

Reinforcement Learning with Verifiable Reward (RLVR) has proven effective for training reasoning-oriented large language models, but existing methods largely assume high-resource settings with abundant training data. In low-resource scenarios, RLVR is prone to more severe entropy collapse, which substantially limits exploration and degrades reasoning performance. To address this issue, we propose H ybrid-domain E ntropy dynamics AL ignment (HEAL), a framework tailored for few-shot RLVR. HEAL first selectively incorporates high-value general-domain data to promote more diverse exploration. Then, we introduce Entropy Dynamics Alignment (EDA), a reward mechanism that aligns trajectory-level entropy dynamics between the target and general domains, capturing both entropy magnitude and fine-grained variation. Through this alignment, EDA not only further mitigates entropy collapse but also encourages the policy to acquire more diverse exploration behaviors from the general domain. Experiments across multiple domains show that HEAL consistently improves few-shot RLVR performance. Notably, using only 32 target-domain samples, HEAL matches or even surpasses full-shot RLVR trained with 1K target-domain samples.
