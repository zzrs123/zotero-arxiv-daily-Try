# Paper Daily Reading - 2026-07-21

## 1. Toward Federated Multimodal Graph Foundation Models: A Topology-Aware Multimodal Alignment Framework

- Authors: Xunkai Li, Guohao Fu, Yuming Ai, Zhengyu Wu, Hongchao Qin, Rong-Hua Li, Guoren Wang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-17
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.792936874240305
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.15687v1
- PDF: https://arxiv.org/pdf/2607.15687v1
- Local PDF: pdf/2026-07-21_01_Toward Federated Multimodal Graph Foundation Models_ A Topology-Aware Multimodal Alignment Framework.pdf

Multimodal-attributed graphs (MAGs), whose nodes carry modalities such as images and text alongside topological structure, now pervade applications including social platforms, e-commerce, and biomedical networks, offering richer semantic signals than single-modality graphs. In practice, such graphs are fragmented across privacy-restricted silos owned by different platforms and institutions, so learning a broadly transferable model over them demands collaborative training that never exposes raw data. This places the task at the intersection of multimodal graph learning and federated learning, yet existing methods cover only one side of it. To address the challenges from these two perspectives, we propose FedGAMMA, casting federated multimodal graph foundation learning as a two-stage semantic-structural alignment problem of federated pre-training and prompt-based fine-tuning. During pre-training, a shared-private semantic enhancer disentangles cross-modal commonality from modality-specific information, aligning it through optimal transport, a topology-aware graph fusion module decouples semantic and structural views via semantic residual graphs and dual positional encodings, and a dual-channel affinity-aware aggregation mechanism estimates client similarity from feature and graph centroids without exposing raw data. During fine-tuning, FedGAMMA adapts the pretrained encoder through lightweight graph-aware prompts, a shared prompt pool with controlled exploration, and channel-wise prompt synchronization. Experiments on twelve multimodal graph datasets show FedGAMMA consistently surpassing a broad range of baselines across downstream tasks, with gains of up to 12.96%. FedGAMMA further outperforms competitive baselines accross multi-domain datasets on multiple tasks with up to 5.71% under few-shot learning scenario.

## 2. FloREN: Decoding Immune Regulatory Networks through Interpretable Graph Transformer Patient Representations.

- Authors: Clemente-Larramendi, I., Hillion, S., Cornec, D., Jamin, C., Foulquier, N.
- Source: biorxiv
- Venue type: preprint
- Journal: biorxiv
- Publication status: preprint
- Publication date: 2026-07-20
- DOI: 10.64898/2026.07.12.738088
- Categories: bioinformatics
- Relevance: 3.625134511107842
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://www.biorxiv.org/content/10.64898/2026.07.12.738088v1.full.pdf
- PDF: https://www.biorxiv.org/content/10.64898/2026.07.12.738088v1.full.pdf
- Local PDF: pdf/2026-07-21_02_FloREN_ Decoding Immune Regulatory Networks through Interpretable Graph Transformer Patient Representations.pdf

Single-cell RNA sequencing (scRNA-seq) enables detailed characterization of cellular heterogeneity, yet understanding the full cellular and regulatory environment of complex tissues remains challenging. In the era of large single-cell atlases, this technology has become increasingly accessible, and datasets have grown in scale and statistical power. As a result, sample representation methods have emerged as a promising strategy to summarize patient-level biological variation. However, most existing approaches rely on unsupervised learning frameworks with ambiguous biological interpretability. Here we present a Framework for Learning Over REgulatory-Embedding Networks (FloREN), a supervised and interpretable sample representation method. FloREN models single-cell data as a heterogeneous network integrating cells and genes together with gene regulatory and cell-cell communication relationships. Through condition-aware embeddings and interpretable attention networks, FloREN enables improved sample stratification and biomarker discovery. In addition, the framework supports downstream analyses that found specific immune network mechanisms in immune-mediated inflammatory diseases (IMIDs).

## 3. MGDT: MLLM-Guided Diffusion Transformer with Relation-Adaptive Mixture-of-Experts for Multimodal Knowledge Graph Completion

- Authors: Xu Hou, Meiyu Liang, Wei Huang, Yawen Li, Zhe Xue, Wu Liu, Guanhua Ye, Lei Shi, Kangkang Lu
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-17
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 3.4839055694440546
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.15592v1
- PDF: https://arxiv.org/pdf/2607.15592v1
- Local PDF: pdf/2026-07-21_03_MGDT_ MLLM-Guided Diffusion Transformer with Relation-Adaptive Mixture-of-Experts for Multimodal Knowledge Graph Complet.pdf

Multimodal Knowledge Graph Completion (MKGC) requires inferring missing entities from structural, textual, and visual cues. Existing diffusion-based MKGC methods usually denoise directly on raw multimodal features. Such a design forces the denoiser to simultaneously perform relation-dependent cue selection, cross-modal semantic alignment, and structure-aware entity generation, which introduces noisy and semantically inconsistent conditions for diffusion and consequently leads to suboptimal completion performance. To address this limitation, we propose MGDT: MLLM-Guided Diffusion Transformer with Relation-Adaptive Mixture-of-Experts (MGDT), a novel MKGC framework built on an align-then-diffuse paradigm. MGDT first employs a Relation-Adaptive Semantic Routing Mixture-of-Experts (RASR-MoE) module to select relation-relevant multimodal semantic transformation paths and suppress irrelevant modality interference. MGDT then uses a frozen Multimodal Large Language Model (MLLM) as a semantic anchor to align the routed multimodal representations into a unified latent space and reduce cross-modal semantic heterogeneity. Finally, a Knowledge Graph Diffusion Transformer (KGDT) performs graph-conditioned denoising generation in the aligned space to produce the missing entity representation. Experiments on three benchmark datasets show that MGDT consistently outperforms strong baselines.

## 4. EBD-DTI: Episodic Bridge Diffusion for Zero-Shot Cold-Start Drug-Target Interaction Prediction

- Authors: Liu, J., Le, J., Wei, C., Liu, M., Yin, Z.
- Source: biorxiv
- Venue type: preprint
- Journal: biorxiv
- Publication status: preprint
- Publication date: 2026-07-20
- DOI: 10.64898/2026.07.14.738384
- Categories: bioinformatics
- Relevance: 3.4085751913644042
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://www.biorxiv.org/content/10.64898/2026.07.14.738384v1.full.pdf
- PDF: https://www.biorxiv.org/content/10.64898/2026.07.14.738384v1.full.pdf
- Local PDF: pdf/2026-07-21_04_EBD-DTI_ Episodic Bridge Diffusion for Zero-Shot Cold-Start Drug-Target Interaction Prediction.pdf

Predicting drug-target interactions (DTI) for entirely unseen drugs or proteins---the cold-start problem---remains a critical challenge in computational drug discovery. While sequence-based methods naturally support zero-shot generalization, they often ignore relational topology, and existing graph-based approaches either rely on global diffusion that blurs the boundary between inductive and transductive evaluation or require a few known interaction samples at test time (few-shot). We present EBD-DTI, a framework that enables zero-shot inference in graph-based DTI models without requiring any known interactions for unseen entities. The key innovation is episodic cold-start training: at each epoch, a random subset of training entities is masked and treated as pseudo-cold, forcing the model to learn cold-start inference with explicit gradient supervision. A bridge-conditioned local subgraph, together with multi-hop diffusion, provides cold entities with relational context from their nearest observed neighbors. Experiments on three benchmarks (BioSNAP, BindingDB, and DrugBank) demonstrate that EBD-DTI achieves competitive or superior performance compared to state-of-the-art methods under strict zero-shot evaluation, with episodic training improving AUC by up to 12%.

## 5. From Diffusion to Reaction-Diffusion: A Dynamical-Systems View of Oversmoothing in Hypergraph Neural Networks

- Authors: Zhiheng Zhou, Mengyao Zhou, Yancheng Chen, Dengyi Zhao, Xingqin Qi, Guiying Yan
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-17
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.3329672530105787
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.15773v1
- PDF: https://arxiv.org/pdf/2607.15773v1
- Local PDF: pdf/2026-07-21_05_From Diffusion to Reaction-Diffusion_ A Dynamical-Systems View of Oversmoothing in Hypergraph Neural Networks.pdf

Higher-order couplings enhance the expressive power of hypergraph neural networks (HGNNs), but they also intensify representation collapse in deep propagation due to strong multi-way feature mixing. This work investigates hypergraph oversmoothing from a dynamical-systems perspective and develops a reaction--diffusion framework for depth-resistant hypergraph learning. By defining hypergraph gradient and divergence operators, we interpret message passing as an incidence-level diffusion process. The analysis of pure diffusion shows that its continuous semiflow exponentially contracts the null-mode-free component of node representations and drives the Dirichlet energy to zero, revealing hypergraph oversmoothing as an intrinsic transverse-energy dissipation phenomenon. Motivated by this analysis, we propose Hypergraph Neural Reaction--Diffusion (HNRD), which introduces a reaction mechanism acting on the transverse component to compensate diffusion-induced dissipation and stabilize discriminative variations. We establish global well-posedness of the proposed dynamics and prove that the null-mode-free Dirichlet energy remains bounded away from zero. A forward-Euler discretization provides a practical HNRD layer with a stability condition for deep propagation. Experiments on benchmark and synthetic heterophilic hypergraphs demonstrate that HNRD consistently improves over representative hypergraph baselines. Depth, robustness, and efficiency analyses further show that HNRD preserves stable performance and nonzero Dirichlet energy under deep propagation and perturbations. These results provide a principled dynamical framework for designing deep hypergraph architectures that maintain higher-order expressiveness without representation collapse.

## 6. Toward a mechanistic understanding of inference in visual cortex and diffusion models

- Authors: Zeyu Yun, Alexander Belsten, Dasheng Bi, Zahra Kadkhodaie, Yubei Chen, Bruno A. Olshausen
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-17
- DOI: Unavailable
- Categories: q-bio.NC, cs.AI
- Relevance: 3.3090270169646905
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.15693v1
- PDF: https://arxiv.org/pdf/2607.15693v1
- Local PDF: pdf/2026-07-21_06_Toward a mechanistic understanding of inference in visual cortex and diffusion models.pdf

We describe a model of perceptual inference in primary visual cortex (V1) equivalent to a minimal diffusion model whose function can be readily understood from its parameters. The model is based on sparse coding with a non-factorial prior over latent variables in the form of an unconstrained, pairwise interaction matrix, extending standard sparse coding inference to a general recurrent dynamical system. We efficiently train these recurrent dynamics using a denoising score-matching objective and implicit differentiation. After training on natural images, the learned interaction matrix mirrors the structure of horizontal connections in superficial layers of V1 that link neurons of similar orientation tuning. This model exhibits exceptionally good denoising performance, restoring image features such as extended contours amid extreme visual ambiguity, nearly matching the behavior of standard, black-box diffusion architectures in generalization regime. Owing to the model's simplicity, the network's Jacobian can be decomposed directly in terms of the interaction matrix between latent variables, revealing mechanistically how the recurrent dynamics assign high probability over a continuous family of natural structural deformations. Intriguingly, within this circuit, a large fraction of latent variables learn to disconnect from visual input altogether, essentially forming a hierarchical representation that appears to enforce global consistency among image features. Together, the model and results bridge two distinct domains: for neuroscience, it generates concrete, testable hypotheses regarding functional connectivity in recurrent neural circuits during perceptual inference tasks; for machine learning, it elucidates the internal mechanisms learned by diffusion models that allow them to generate infinitely many novel images from a finite training set.

## 7. multiScaleAC: Cell-Cell interaction with Moran's I as a function of kernel bandwidth

- Authors: Soupir, A. C., Hayes, M. T., Manley, B. J., Wang, X., Wrobel, J., Peres, L. C., Fridley, B. L.
- Source: biorxiv
- Venue type: preprint
- Journal: biorxiv
- Publication status: preprint
- Publication date: 2026-07-20
- DOI: 10.64898/2026.07.14.738306
- Categories: bioinformatics
- Relevance: 3.0950510130825837
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://www.biorxiv.org/content/10.64898/2026.07.14.738306v1.full.pdf
- PDF: https://www.biorxiv.org/content/10.64898/2026.07.14.738306v1.full.pdf
- Local PDF: pdf/2026-07-21_07_multiScaleAC_ Cell-Cell interaction with Moran's I as a function of kernel bandwidth.pdf

Over the last decade, spatial transcriptomic technology has transformed our understanding of tissue architecture including cell-cell interactions within the tumor immune microenvironment. A specific use-case of increasing interest is leveraging the spatial statistical relationship of genes whose protein products are known to be involved in ligand-receptor interactions. One methodological limitation of this approach has been the requirement to choose one radius around a cell as a parameter that can come with selection biases. Rather, interactions between cells vary in strength across a range of spatial scales that single-radius choice may miss. To fill this gap we developed `multiScaleAC` to extended Moran's I, a correlation measure that accounts for locations of values, by employing a Gaussian kernel applied to locations and varying the bandwidth parameter h. The resulting Moranis I\left(h\right) then can be compared between samples using functional data analysis. In the current study, we used simulations to show that our framework has well controlled Type I error due to the use of permutations for assessing significant interactions. We also demonstrate that `multiScaleAC` has high statistical power to identify a significant interaction when a true interaction is simulated (1.00 at bandwidths greater than 5) and increasing power as bandwidth increases when negative interaction is simulated. We found `multiScaleAC` largely captures similar significant ligand-receptor profiles in 8 Visium samples of colon tissue using the same bandwidth as `spatialDM` but without removing low-weight spots from the weight matrix (73.7% - 87.2%). Applying the `multiScaleAC` framework to our previous single-cell spatial transcriptomics data (COL4A1-ITGAV in the stromal compartment of clear cell renal cell carcinoma) followed by functional principal component analysis, we found functional principal component 1 to represent global interaction elevation/depression. Associating functional principal component 1 scores with immunotherapy exposure showed significantly higher scores in stromal tissues exposed to immunotherapy than those naive to immunotherapy, indicating an overall higher interaction of cell expressing COL4A1-ITGAV. These findings recapitulate our previous study while reducing bias in neighbor selections. We believe this is the first study to apply a functional extension of Moran's I in combination with functional data analysis to understand cell-cell interaction over spatial scales.

## 8. GDTR: Layer-wise Settling Depth Reveals Biological Grammar in Genomic Foundation Models

- Authors: Cho, Y., Kang, J., Park, S., Kim, S.
- Source: biorxiv
- Venue type: preprint
- Journal: biorxiv
- Publication status: preprint
- Publication date: 2026-07-20
- DOI: 10.64898/2026.07.14.738370
- Categories: bioinformatics
- Relevance: 3.0868333977538254
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://www.biorxiv.org/content/10.64898/2026.07.14.738370v1.full.pdf
- PDF: https://www.biorxiv.org/content/10.64898/2026.07.14.738370v1.full.pdf
- Local PDF: pdf/2026-07-21_08_GDTR_ Layer-wise Settling Depth Reveals Biological Grammar in Genomic Foundation Models.pdf

Genomic foundation models capture sequence regularities, yet existing interpretability tools rarely ask where in the layer stack a biological grammar becomes stable. We introduce GDTR, the Genomic Deep-Thinking Ratio, a training-free residual-stream lens that assigns each nucleotide token a settling depth : the first layer at which its representation stabilizes against the post-final-norm reference. On Evo 2 7B, splice donor and acceptor sites settle approximately two layers earlier than intronic contexts; enhancer-like cCREs show a smaller but measurable shift; and a chromosome 22 calibration transfers to held-out chromosome 17. Perturbing canonical splice donors shows that the signal is bidirectional: disrupting the central GT motif deepens settling, whereas shuffling the flanking grammar makes the preserved motif settle earlier. Differential GDTR further reveals consequence-associated peak-disruption depths across ClinVar variants, with synonymous substitutions peaking deepest but showing broad class overlap. GDTR therefore provides a layer-wise interpretability axis for genomic foundation models, complementary to existing prediction and variant-scoring tools.

## 9. A Label-Free Multi-Metric Pipeline for Benchmarking Single-Cell RNA-Sequencing Clustering and Testing the Reproducibility of Cell-Type Heterogeneity

- Authors: Yousef, Z., Simone, J., Klein, D., Cho, H., Bhuyan, A., Bhatt, P., Wu, J., Wang, H., Cai, L.
- Source: biorxiv
- Venue type: preprint
- Journal: biorxiv
- Publication status: preprint
- Publication date: 2026-07-20
- DOI: 10.64898/2026.07.17.739160
- Categories: bioinformatics
- Relevance: 3.060074000733548
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://www.biorxiv.org/content/10.64898/2026.07.17.739160v1.full.pdf
- PDF: https://www.biorxiv.org/content/10.64898/2026.07.17.739160v1.full.pdf
- Local PDF: pdf/2026-07-21_09_A Label-Free Multi-Metric Pipeline for Benchmarking Single-Cell RNA-Sequencing Clustering and Testing the Reproducibilit.pdf

A discovered sub-population from single-cell transcriptomic data is only meaningful if it is reproducible, yet clustering is usually done with one method on one embedding and rarely tested. We present a label-free, multi-metric pipeline that reframes clustering as an auditable, methods-blind decision and separates two notions of stability that are commonly conflated: reproducibility under cell resampling (bootstrap) and reproducibility under re-embedding (retraining the representation). The pipeline evaluates seven clustering configurations across cluster counts using five non-redundant quality metrics. As a whole-dataset control on a mouse retinal atlas, it recovers an eight-cell-type annotation at 96.3% accuracy (adjusted Rand index, ARI = 0.91) without labels. We then validate the discovery mode on two cell types with opposite ground truth. On bipolar cells, which have well-established subtypes, the pipeline accepts the sub-structure: across-embedding reproducibility rises with cluster number to a high plateau (mean pairwise ARI ~0.93 near the ~15 known bipolar subtypes), with quality metrics improving in parallel. On rod photoreceptors, treated as homogeneous, it rejects over-clustering: the metric-selected partition passes a bootstrap-stability check but is not reproducible when the embedding is retrained (mean pairwise ARI = 0.69), and the metrics do not improve with cluster number. On synthetic data, the test recovers real structure down to a 5% subpopulation while rejecting null data (high sensitivity and specificity). Bootstrap stability alone is therefore insufficient evidence for sub-population; the across-embedding test discriminates real sub-structure from over-clustering and applies to any cell type as a reproducible alternative to single-method, single-embedding clustering.

## 10. Verbalizable Representations Form a Global Workspace in Language Models

- Authors: Wes Gurnee, Nicholas Sofroniew, Adam Pearce, Mateusz Piotrowski, Isaac Kauvar, Runjin Chen, Anna Soligo, Paul Bogdan, Euan Ong, Rowan Wang, Ben Thompson, David Abrahams, Subhash Kantamneni, Emmanuel Ameisen, Joshua Batson, Jack Lindsey
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-16
- DOI: Unavailable
- Categories: cs.CL, cs.AI, cs.LG
- Relevance: 2.987846094043917
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.15495v1
- PDF: https://arxiv.org/pdf/2607.15495v1
- Local PDF: pdf/2026-07-21_10_Verbalizable Representations Form a Global Workspace in Language Models.pdf

Out of everything the human brain processes, only a small fraction is consciously accessible, in the sense of being available for verbal report, deliberate control, and flexible reasoning. In this paper, we present evidence that an analogous functional distinction has emerged in large language models. Using a new interpretability technique, the Jacobian lens, we identify the representations a model is poised to verbalize at any point in its processing. These representations, which we collectively call the J-space, exhibit the functional properties characteristic of a global workspace: their contents can be reported, deliberately summoned and held, used to carry the intermediate steps of silent reasoning, and passed as arguments to arbitrary downstream computations, while automatic processing such as text parsing and routine inference proceeds without them. The J-space also has structural signatures that global workspace theory associates with conscious access: it carries coherent content only in an intermediate band of layers, holds on the order of tens of concepts at a time, and is broadcast by the model's weights more widely than other representations. These properties make it a practical window into a model's unspoken thinking. In alignment audits, it reveals strategic deliberation, evaluation awareness, and trained-in misaligned dispositions that never appear in the model's outputs. We find that post-training installs the Assistant's point of view in the workspace, and we introduce counterfactual reflection training, which improves behavior by training only what a model would say if interrupted and asked to reflect. These results indicate that language models maintain a small, privileged set of representations bearing some of the functional hallmarks of conscious access, and that decoding these representations sheds light on ongoing cognitive processes.

## 11. Knowledge-Centric Agents for Workflow Generation

- Authors: Zhendong Li, Lei Sun, Ruibo Ming, He Zhang, Danda Pani Paudel, Luc Van Gool, Jinjin Gu
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-17
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 2.954380223740774
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.15845v1
- PDF: https://arxiv.org/pdf/2607.15845v1
- Local PDF: pdf/2026-07-21_11_Knowledge-Centric Agents for Workflow Generation.pdf

Workflow generation in visual creation systems such as ComfyUI demands not only syntactic accuracy but also expert-level reasoning over modular compositions. Existing large language model (LLM) approaches often treat this as a direct text-to-JSON generation task, struggling with structural brittleness and lacking the experiential knowledge required for effective design. We argue that successful workflow generation requires modeling knowledge itself, including its structure, hierarchy, and reasoning dynamics. To this end, we propose a knowledge-centric framework that learns to invert, inject, and infer with knowledge across multiple abstraction levels. We first perform knowledge inversion to distill hierarchical representations, ranging from full pseudo-codes and skeletons to high-level strategies, from large collections of real-world workflows. We then conduct knowledge injection through supervised fine-tuning, teaching the model to reason from task descriptions to strategies and from strategies to executable structures. During inference, the model performs reversible reasoning to synthesize executable workflows, augmented by self-refinement for structural coherence. Extensive experiments demonstrate that our method produces workflows with richer node diversity, more coherent structures, and higher execution success rates than existing systems, establishing a new foundation for knowledge-driven, agentic workflow generation.

## 12. DPNeXt: A Lightweight Multi-Scale Feature Fusion Framework for Efficient ViT-Based Multi-Task Dense Prediction

- Authors: Jehun Kang, Jungha Wang, Youngjun Hwang, David Hyunchul Shim
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-17
- DOI: Unavailable
- Categories: cs.CV, cs.AI, cs.RO
- Relevance: 2.939948864697496
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.16012v1
- PDF: https://arxiv.org/pdf/2607.16012v1
- Local PDF: pdf/2026-07-21_12_DPNeXt_ A Lightweight Multi-Scale Feature Fusion Framework for Efficient ViT-Based Multi-Task Dense Prediction.pdf

Multi-Task Learning (MTL) in robotics perception systems supports comprehensive 3D spatial scene understanding by integrating semantic segmentation and depth estimation. While Vision Foundation Models (VFMs) are increasingly adopted as robust feature encoders, existing decoding strategies present a critical bottleneck. To address this, we propose DPNeXt, a streamlined multi-scale feature fusion decoder and efficient alternative to the standard Dense Prediction Transformer (DPT). DPNeXt uses dual depthwise separable inverted bottlenecks to improve frozen VFM utilization through fusion-centric decoding and independent task modularization. To further mitigate negative inductive transfer between tasks, we introduce the Multi-Task Boundary Guidance (MTBG) strategy. Unlike prior boundary-aware methods that add fusion modules or gating, MTBG applies symmetric boundary-focused supervision to encourage geometric consistency without extra annotation or inference cost. Experiments on Cityscapes show that DPNeXt-S outperforms prior state-of-the-art (SOTA) MTL models, while DPNeXt-B further improves the overall performance and achieves the best results among the compared methods. On NYUv2, DPNeXt-B also achieves the best semantic segmentation and depth estimation results among the compared methods while requiring substantially fewer trainable parameters than prior large-scale MTL models. Compared with the standard DPT, DPNeXt-S reduces trainable parameters by 78.6% and achieves the fastest inference speed among the compared models on resource-constrained laptop hardware. The source code, model checkpoints, and a demo video will be made available at https://github.com/kangjehun/DPNeXt.

## 13. DPCGS: a computational framework for linking GWAS to single-cell transcriptomics in complex traits and diseases

- Authors: Liu, C., Shen, B., Li, J., Zhu, R., Yang, P., Wu, B., Xuan, Y., Yang, S., Yuan, B., Yang, N., Ma, L., Liu, Q., Dai, S., Zhang, Y.
- Source: biorxiv
- Venue type: preprint
- Journal: biorxiv
- Publication status: preprint
- Publication date: 2026-07-20
- DOI: 10.64898/2026.07.14.738331
- Categories: bioinformatics
- Relevance: 2.874595829868184
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://www.biorxiv.org/content/10.64898/2026.07.14.738331v1.full.pdf
- PDF: https://www.biorxiv.org/content/10.64898/2026.07.14.738331v1.full.pdf
- Local PDF: pdf/2026-07-21_13_DPCGS_ a computational framework for linking GWAS to single-cell transcriptomics in complex traits and diseases.pdf

Complex traits and diseases arise from the interplay between genetic variation and cellular heterogeneity, making it essential to understand how genetic risk manifests at the cellular level. However, connecting genome-wide association studies (GWAS) to specific cell populations remains challenging due to cellular complexity and the prevalence of noncoding variants. Here, we present DPCGS, a computational framework that systematically integrates GWAS summary statistics with single-cell RNA-sequencing (scRNA-seq) data to identify trait-associated cell populations, genes, and regulatory programs. DPCGS is based on the principle that GWAS-prioritized genes should exhibit elevated expression in relevant cells compared with matched controls. Benchmark analyses with simulated datasets showed that DPCGS consistently outperforms existing methods, achieving higher accuracy and sensitivity in detecting trait-relevant cells. Applications to diverse scRNA-seq datasets further validated its robustness, revealing oligodendrocytes and astrocytes as key subpopulations in Alzheimer's disease and macrophages and B cells in asthma. These analyses also highlighted potential molecular regulators, including CD74, FOS, FLI1, and AP-1 transcription factors. Together, these findings establish DPCGS as a versatile framework for dissecting the cellular and molecular basis of complex traits and diseases, with broad implications for biomarker discovery and therapeutic development.

## 14. Self-Supervised Direct Preference Optimization for Text-to-Image Diffusion Models

- Authors: Peng, Liang, Wu, Boxi, Cheng, Haoran, Zhao, Yibo, He, Xiaofei
- Source: neurips
- Venue type: conference
- Journal: NeurIPS 2025
- Publication status: formally_published
- Publication date: 2026-04-23
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.873628093970131
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://proceedings.neurips.cc/paper_files/paper/2025/hash/03600ae6c3392fd65ad7c3a90c6f7ce8-Abstract-Conference.html
- PDF: https://proceedings.neurips.cc/paper_files/paper/2025/file/03600ae6c3392fd65ad7c3a90c6f7ce8-Paper-Conference.pdf
- Local PDF: pdf/2026-07-21_14_Self-Supervised Direct Preference Optimization for Text-to-Image Diffusion Models.pdf

Direct preference optimization (DPO) is an effective method for aligning generative models with human preferences and has been successfully applied to fine‑tune text‑to‑image diffusion models. Its practical adoption, however, is hindered by a labor‑intensive pipeline that first produces a large set of candidate images and then requires humans to rank them pairwise. We address this bottleneck with self‑supervised direct preference optimization, a new paradigm that removes the need for any pre‑generated images or manual ranking. During training, we create preference pairs on the fly through self‑supervised image transformations, allowing the model to learn from fresh and diverse comparisons at every iteration. This online strategy eliminates costly data collection and annotation while remaining plug‑and‑play for any text‑to‑image diffusion method. Surprisingly, the on‑the‑fly pairs produced by the proposed method not only match but exceed the effectiveness of conventional DPO, which we attribute to the greater diversity of preferences sampled during training. Extensive experiments with Stable Diffusion 1.5 and Stable Diffusion XL confirm that our method delivers substantial gains.

## 15. Beyond Fully Random Masking: Attention-Guided Denoising and Optimization for Diffusion Language Models

- Authors: Jia Deng, Junyi Li, Xin Zhao, Jinpeng Wang, Hongyu Lu, Ji-Rong Wen
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.8705085253532223
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.2060/
- PDF: https://aclanthology.org/2026.acl-long.2060.pdf
- Local PDF: pdf/2026-07-21_15_Beyond Fully Random Masking_ Attention-Guided Denoising and Optimization for Diffusion Language Models.pdf

Diffusion large language models (dLLMs) offer an efficient alternative to autoregressive models through parallel decoding, yet existing post-training methods largely rely on random masking strategies that overlook intrinsic token dependencies. In this work, we present an empirical analysis of attention in dLLMs and show that tokens attending more strongly to revealed context exhibit greater generation stability and play a critical role in reasoning. Motivated by these findings, we propose AGDO, an attention-guided denoising and optimization framework that aligns both training and optimization with attention-derived dependencies. AGDO determines the denoising order based on attention structure and emphasizes attention-critical tokens during supervised fine-tuning and reinforcement learning. Experiments on mathematical and coding benchmarks demonstrate that AGDO consistently improves reasoning performance, outperforming state-of-the-art post-training methods for dLLMs.

## 16. Iterative Dual-Model Alignment for Story Evaluation

- Authors: Bruce Qin, Dan Goldwasser
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.8702006353695375
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.648/
- PDF: https://aclanthology.org/2026.acl-long.648.pdf
- Local PDF: pdf/2026-07-21_16_Iterative Dual-Model Alignment for Story Evaluation.pdf

Large language models (LLMs) can both evaluate and explain text quality; however, most existing evaluators operate as static classifiers and lack the ability to refine their reasoning through interaction. We propose an Iterative Alpha–Beta Learning framework that jointly trains two complementary 8B models: an Alpha ( 𝛼 ) classifier that assesses pairwise story engagement, and a Beta ( 𝛽 ) generator that produces structured, rubric-guided comparative explanations. The two models co-evolve within a closed feedback loop: 𝛼 provides probabilistic preference signals to guide 𝛽 ’s Direct Preference Optimization (DPO), while 𝛽 ’s improved explanations are reintegrated to retrain 𝛼 via a KL-based contrastive objective. This dual optimization enables mutual learning: 𝛼 gains interpretability and robustness from 𝛽 ’s textual rationales, while 𝛽 acquires stronger alignment and discriminative precision from 𝛼 ’s confidence deltas. Experiments on human-annotated story-pair datasets HANNA show that the proposed system consistently outperforms strong single-model baselines in both accuracy and explanation quality across multiple iterative rounds.

## 17. Combining Distantly Supervised Models with In Context Learning for Monolingual and Cross-Lingual Relation Extraction

- Authors: Vipul Kumar Rathore, Malik Hammad Faisal, Parag Singla, Mausam
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.8700936738136837
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.2109/
- PDF: https://aclanthology.org/2026.acl-long.2109.pdf
- Local PDF: pdf/2026-07-21_17_Combining Distantly Supervised Models with In Context Learning for Monolingual and Cross-Lingual Relation Extraction.pdf

Distantly Supervised Relation Extraction (DSRE) remains a long-standing challenge in NLP, where models must learn from noisy bag-level annotations while making sentence-level predictions. While existing state-of-the-art (SoTA) DSRE models rely on task-specific training, their integration with in-context learning (ICL) using large language models (LLMs) remains underexplored. A key challenge is that the LLM may not learn relation semantics correctly, due to noisy annotation.In response, we propose HYDRE – HY brid D istantly Supervised R elation E xtraction framework. It first uses a trained DSRE model to identify the top- k candidate relations for a given test sentence, then uses a novel dynamic exemplar retrieval strategy that extracts reliable, sentence-level exemplars from training data, which are then provided in LLM prompt for outputting the final relation(s).We further extend HYDRE to cross-lingual settings for RE in low-resource languages. Using available English DSRE training data, we evaluate all methods on English as well as a newly curated benchmark covering four diverse low-resource Indic languages - Oriya, Santali, Manipuri, and Tulu. HYDRE achieves up to 20 F1 point gains in English and, on average, 17 F1 points on Indic languages over prior SoTA DSRE models and naive prompting baselines. Detailed ablations exhibit HYDRE ’s efficacy compared to other prompting strategies.

## 18. Distilling LLM Reasoning into Dense Encoders: Bridging the Accuracy-Efficiency Gap in Recommendation

- Authors: Donghee Han, Daeyoung Roh, A Young Kim, Hwanjun Song, Mun Yong Yi
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.8700122183450127
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1130/
- PDF: https://aclanthology.org/2026.findings-acl.1130.pdf
- Local PDF: pdf/2026-07-21_18_Distilling LLM Reasoning into Dense Encoders_ Bridging the Accuracy-Efficiency Gap in Recommendation.pdf

Large Language Models (LLMs) have shown remarkable potential in recommendation systems but suffer from prohibitive inference latency. Existing distillation approaches typically target Small Language Models (SLMs) or Conventional Recommendation Models (CRMs), face a critical trade-off between computational cost and semantic reasoning capacity. To bridge this accuracy-efficiency gap, we introduce Reasoning-to-Encoder Distillation (R2END), a framework that establishes a text encoder as the optimal student architecture for scalable recommendation. Unlike methods that mimic token generation, R2END compresses the teacher’s reasoning into a dense vector space via a semantic alignment objective, effectively capturing user-item dynamics. Extensive experiments on four datasets demonstrate that R2END not only outperforms state-of-the-art baselines but also achieves drastically reduced latency, offering a sweet spot for recommendation.

## 19. ReGATE: Learning Faster and Better with Fewer Tokens in MLLMs

- Authors: Chaoyu Li, Yogesh Kulkarni, Pooyan Fazli
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.8696660669168272
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.2154/
- PDF: https://aclanthology.org/2026.acl-long.2154.pdf
- Local PDF: pdf/2026-07-21_19_ReGATE_ Learning Faster and Better with Fewer Tokens in MLLMs.pdf

The computational cost of training multimodal large language models (MLLMs) grows rapidly with the number of processed tokens. Existing efficiency methods mainly target inference via token reduction or merging, offering limited benefits during training. We introduce ReGATE (**Re**ference-**G**uided **A**daptive **T**oken **E**lision), an adaptive token pruning method for accelerating MLLM training. ReGATE adopts a teacher-student framework, in which a frozen teacher LLM provides per-token guidance losses that are fused with an exponential moving average of the student’s difficulty estimates. This adaptive scoring mechanism dynamically selects informative tokens while skipping redundant ones in the forward pass, substantially reducing computation without altering the model architecture. Across three representative MLLMs, ReGATE matches the peak accuracy of standard training on MVBench up to **2 × faster**, using only **38%** of the tokens. With extended training, it even surpasses the baseline across multiple multimodal benchmarks, cutting total token usage by over **41%**. Code and models will be released publicly.

## 20. Dynamic Long Context Reasoning over Compressed Memory via End-to-End Reinforcement Learning

- Authors: Zhuoen Chen, Dongfang Li, Meishan Zhang, Baotian Hu, Min Zhang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.8690847182474704
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.365/
- PDF: https://aclanthology.org/2026.acl-long.365.pdf
- Local PDF: pdf/2026-07-21_20_Dynamic Long Context Reasoning over Compressed Memory via End-to-End Reinforcement Learning.pdf

Large Language Models (LLMs) face severe challenges in long-context processing, including quadratic computational costs, information forgetting, and the context fragmentation inherent in Retrieval-Augmented Generation (RAG). We introduce LycheeMemory, a cognitively inspired framework that enables efficient long-context inference via chunk-wise compression and selective memory recall, rather than processing all raw tokens. LycheeMemory segments the input into chunks and encodes each into compressed KV-cache style representations using a Compressor. A Gate then dynamically selects relevant memory blocks, which a Reasoner iteratively processes with an evolving working memory to solve downstream tasks. The Compressor and Reasoner are jointly optimized via end-to-end reinforcement learning, while the Gate is trained separately as a classifier. Experimental results demonstrate that LycheeMemory achieves competitive accuracy (up to 82% in ablation variants) on multi-hop reasoning benchmarks (e.g., RULER-HQA), successfully extrapolates context length from 7K to 1.75M, and provides a favorable accuracy–efficiency trade-off against strong long-context baselines. Notably, compared to MemAgent, LycheeMemory achieves an average 2× reduction in peak GPU memory usage and a 6× speedup during inference.

## 21. FLARE: Fine-Grained Length-Aware Routing for Resource-Efficient Heterogeneous LLM Serving

- Authors: Yujia Fu, Heming Zhong, Dan Huang, Yutong Lu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.8683611352909595
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1018/
- PDF: https://aclanthology.org/2026.acl-long.1018.pdf
- Local PDF: pdf/2026-07-21_21_FLARE_ Fine-Grained Length-Aware Routing for Resource-Efficient Heterogeneous LLM Serving.pdf

With the rapid proliferation of large language models (LLMs), model pools have become increasingly heterogeneous in both capability and efficiency. Larger LLMs can improve quality but incur higher latency and cost, while smaller LLMs are the opposite, making per-query model selection crucial in practice. This has spawned LLM routers that dispatch each query to an appropriate model. Existing routers lack fine-grained resource awareness across deployment settings, which degrades efficiency metrics in real-world serving. To this end, We propose FLARE, a length-centric, resource-aware multi-LLM routing framework that uses length-based models to estimate per-query latency and cost. FLARE formulates routing as a discrete multi-objective optimization problem to achieve efficient trade-off. Experiments show that FLARE reduces latency and cost by up to 68% and 75% while maintaining competitive accuracy, and can be easily applied to new datasets and LLMs.

## 22. SlideAgent: Hierarchical Agentic Framework for Multi-Page Visual Document Understanding

- Authors: Yiqiao Jin, Rachneet Kaur, Zhen Zeng, Sumitra Ganesh, Srijan Kumar
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.868160025312502
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.677/
- PDF: https://aclanthology.org/2026.acl-long.677.pdf
- Local PDF: pdf/2026-07-21_22_SlideAgent_ Hierarchical Agentic Framework for Multi-Page Visual Document Understanding.pdf

Multi-page visual documents such as manuals, brochures, presentations, and posters convey key information through layout, colors, icons, and cross-slide references. While multimodal large language models (MLLMs) offer opportunities in document understanding, current systems struggle with complex, multi-page visual documents, particularly in fine-grained reasoning over elements and pages. We introduce SlideAgent, a versatile agentic framework for understanding multi-modal, multi-page, and multi-layout documents, especially slide decks. SlideAgent employs specialized agents and decomposes reasoning into three specialized levels–global, page, and element–to construct a structured, query-agnostic representation that captures both overarching themes and detailed visual or textual cues. During inference, SlideAgent selectively activates specialized agents for multi-level reasoning and integrates their outputs into coherent, context-aware answers.Extensive experiments show that SlideAgent significantly improves accuracy over both proprietary (+7.9%) and open-source models (+9.8%).

## 23. Follow the Path: Reasoning over Knowledge Graph Paths to Improve Large Language Model Factuality

- Authors: Mike Zhang, Johannes Bjerva, Russa Biswas
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.8680346346139984
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.561/
- PDF: https://aclanthology.org/2026.findings-acl.561.pdf
- Local PDF: pdf/2026-07-21_23_Follow the Path_ Reasoning over Knowledge Graph Paths to Improve Large Language Model Factuality.pdf

We introduce fs1, a simple yet effective method that improves the factuality of reasoning traces by sourcing them from large reasoning models and grounding them by conditioning on knowledge graph (KG) paths. We fine-tune eight instruction-tuned Large Language Models (LLMs) on 3.9K factually grounded reasoning traces and rigorously evaluate them on six complex open-domain question-answering (QA) benchmarks encompassing 23.9K questions. Our results demonstrate that our fs1-tuned model consistently outperforms instruction-tuned counterparts with parallel sampling by 6-14 absolute points (pass@). Our detailed analysis shows that fs1 considerably improves model performance over more complex questions (requiring 3 or more hops on KG paths) and numerical answer types compared to the baselines. Furthermore, in single-pass inference, we notice that smaller LLMs show the most improvements. While prior works demonstrate the effectiveness of reasoning traces primarily in the STEM domains, our work shows strong evidence that anchoring reasoning to factual KG paths is a critical step in transforming LLMs for reliable knowledge-intensive tasks.

## 24. Projecting Out the Malice: A Global Subspace Approach to LLM Detoxification

- Authors: Zenghao Duan, Zhiyi Yin, Zhichao Shi, Liang Pang, Shaoling Jing, Zihe Huang, Jiayi Wu, Yu Yan, Jingcheng Deng, Huawei Shen, Xueqi Cheng
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.8677640179806585
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1652/
- PDF: https://aclanthology.org/2026.acl-long.1652.pdf
- Local PDF: pdf/2026-07-21_24_Projecting Out the Malice_ A Global Subspace Approach to LLM Detoxification.pdf

Large language models (LLMs) exhibit exceptional performance but pose inherent risks of generating toxic content, restricting their safe deployment. While traditional methods (e.g., alignment) adjust output preferences, they fail to eliminate underlying toxic regions in parameters, leaving models vulnerable to adversarial attacks. Prior mechanistic studies characterize toxic regions as "toxic vectors" or "layer-wise subspaces", yet our analysis identifies critical limitations: i) Removed toxic vectors can be reconstructed via linear combinations of non-toxic vectors, demanding targeting of entire toxic subspace; ii) Contrastive objective over limited samples inject noise into layer-wise subspaces, hindering stable extraction. These highlight the challenge of identifying robust toxic subspace and removing them. Therefore, we propose GLOSS (GLobal tOxic Subspace Suppression), a lightweight method that mitigates toxicity by identifying and eliminating this global subspace from FFN parameters. Experiments on LLMs (e.g., Qwen3) show GLOSS achieves SOTA detoxification while preserving general capabilities without requiring large-scale retraining.

## 25. DICA: Dual-Indicator Guided Contrastive Alignment in Multimodal Large Language Models

- Authors: Hao Yang, Jin Wang, Xuejie Zhang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.867608055163915
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1933/
- PDF: https://aclanthology.org/2026.findings-acl.1933.pdf
- Local PDF: pdf/2026-07-21_25_DICA_ Dual-Indicator Guided Contrastive Alignment in Multimodal Large Language Models.pdf

Human visual reasoning typically follows a coarse-to-fine attention process, starting from global scene understanding and gradually focusing on question-relevant regions. However, multimodal large language models may deviate from this pattern due to attention drift and the underutilization of visual evidence, which can lead to hallucinations. To mitigate these issues, this study proposes a Dual-Indicator Guided Contrastive Alignment (DICA), which tracks two information-theoretic indicators during inference: Visual Attention Entropy (VAE), which reflects the concentration of visual attention, and Output Image Correlation (OIC), which measures the dependence of generated outputs on the visual input. An abnormal increase in VAE or a decrease in OIC corresponds to different failure modes, which trigger targeted contrastive alignment to restore visual grounding. Experimental results across multiple benchmarks demonstrate that DICA consistently outperforms existing approaches and substantially reduces hallucinations, highlighting the effectiveness of indicator-driven intervention in improving multimodal inference reliability. The code is publicly available at https://github.com/BGWH123/DICA/.

## 26. GFT: From Imitation to Reward Fine-Tuning with Unbiased Group Advantages and Dynamic Coefficient Rectification

- Authors: Wangjie Gan, Miao Pan, Linbo Xi, Wenqi Zhang, Jintao Chen, Jianwei Yin, Xuhong Zhang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.8674457640617286
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1444/
- PDF: https://aclanthology.org/2026.findings-acl.1444.pdf
- Local PDF: pdf/2026-07-21_26_GFT_ From Imitation to Reward Fine-Tuning with Unbiased Group Advantages and Dynamic Coefficient Rectification.pdf

Large language models are typically post-trained using supervised fine-tuning (SFT) and reinforcement learning (RL), yet effectively unifying efficient knowledge injection with robust generalization remains challenging. In this work, we provide a training-dynamics analysis showing that SFT can be interpreted as a special case of policy gradient optimization with an extremely sparse implicit reward and unstable inverse-probability weighting, which together lead to single-path dependency, entropy collapse, and gradient explosion. Motivated by this diagnosis, we propose Group Fine-Tuning (GFT), a unified post-training framework that addresses these intrinsic limitations through two mechanisms: Group Advantage Learning, which constructs diverse response groups and derives normalized contrastive supervision to alleviate reward sparsity, and Dynamic Coefficient Rectification, which adaptively bounds inverse-probability weights to stabilize optimization while preserving efficient knowledge injection. Experiments demonstrate that GFT consistently surpasses SFT-based methods and yields policies that integrate more smoothly with subsequent RL training.Our code is publicly available athttps://github.com/ZJU-OmniAI/GFT.

## 27. How Fragile Is Vision-Language Alignment? Mapping Concept Disruption Under Text-to-Image Personalization

- Authors: Mujtaba Hasan
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.866905161082221
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.alvr-main.27/
- PDF: https://aclanthology.org/2026.alvr-main.27.pdf
- Local PDF: pdf/2026-07-21_27_How Fragile Is Vision-Language Alignment_ Mapping Concept Disruption Under Text-to-Image Personalization.pdf

Text-to-image diffusion models learn a mapping from natural language to visual structure, but how robust is this mapping to perturbation? We use personalization—fine-tuning a model to learn a new face, object, or style—as a controlled stress test to probe the fragility of learned vision-language alignment. We find that fine-tuning for one concept systematically shifts the model’s ability to faithfully render unrelated concepts, and that this disruption follows structured, predictable patterns. To measure this fragility, we construct Concept Entanglement Maps: per-prompt, per-model disruption matrices that reveal which concepts are most affected and why. Using Stable Diffusion v1.5 as a controlled testbed, we evaluate 15 subjects across three personalization methods on 200 prompts and report three findings about the organization of vision-language alignment: (1) aggregate disruption is larger for vision-backbone and cross-attention perturbations than for text-embedding perturbations, despite the latter directly modifying the language representation; (2) abstract and compositional language is significantly more fragile than concrete, object-specific language; and (3) disruption does not follow semantic proximity—personalizing for a face does not preferentially disrupt other face-related prompts ( p = 1.0 ), suggesting that alignment vulnerability is organized globally rather than purely by semantic category. These findings expose a structural vulnerability in current text-to-image personalization: the same cross-attention mechanism that enables compositional generalization also creates pathways through which local fine-tuning can propagate as global alignment shift.

## 28. A Syntactic and Semantic Probe into Language Evolution based on Large Language Models

- Authors: Hao Pang, Changcheng Li, Yingxue Liu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.8668631753444487
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.2095/
- PDF: https://aclanthology.org/2026.findings-acl.2095.pdf
- Local PDF: pdf/2026-07-21_28_A Syntactic and Semantic Probe into Language Evolution based on Large Language Models.pdf

Language evolution is cognitively motivated by the reduction of communicative effort. Current research exploring this reported tendency has been constrained by the heavy reliance on manually annotated resources (e.g., dependency parsing) as well as a narrow focus (e.g., syntax as the single metric). To transcend these limitations, we propose two measures: Attention-based Structural Distance (ASD) and Semantic Space Distance (SSD). ASD is a parser-free measure of syntactic locality derived from the attention mechanism of pretrained large language models (LLM), while SSD is a measure of lexical distances that quantify the degree of separation between different parts of speech in the word vector space. Based on multiple diachronic and multilingual corpora, our experiments show a significant decrease of ASD while an increase of SSD, which implies a language developmental trend towards structural compactness and semantic divergence. Our research pioneers a novel lens grounded in LLM for studying language evolution, which has two major contributions. Linguistically, our study corroborates the hypothesized law of human language evolution by demonstrating that its development optimizes syntactic locality as well as functional semantic discriminability. Cognitively, our study shows that human and LLMs share common characteristics in language processing, lending support to the potential of employing LLMs in the study of human cognition.

## 29. ModeX: Evaluator-Free Best-of-N Selection for Open-Ended Generation

- Authors: Hyeong Kyu Choi, Sharon Li
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.8666503900901166
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.655/
- PDF: https://aclanthology.org/2026.acl-long.655.pdf
- Local PDF: pdf/2026-07-21_29_ModeX_ Evaluator-Free Best-of-N Selection for Open-Ended Generation.pdf

Selecting a single high-quality output from multiple stochastic generations remains a fundamental challenge for large language models (LLMs), particularly in open-ended tasks where no canonical answer exists. While Best-of- N and self-consistency methods show that aggregating multiple generations can improve performance, existing approaches typically rely on external evaluators, reward models, or exact string-match voting, limiting their applicability and efficiency. We propose Mode Extraction (ModeX), an evaluator-free Best-of- N selection framework that generalizes majority voting to open-ended text generation by identifying the modal output representing the dominant semantic consensus among generated texts. ModeX constructs a similarity graph over candidate generations and recursively applies spectral clustering to select a representative centroid, without requiring additional inference or auxiliary models. We further instantiate this selection principle as ModeX Decoding, a drop-in decoding scheme with early pruning for efficiency. Across open-ended tasks—including text summarization, code generation, and mathematical reasoning—our approaches consistently outperform standard single- and multi-path baselines, providing a computationally efficient, drop-in solution for robust open-ended text generation.

## 30. OFFSIDE: Benchmarking Unlearning Misinformation in Multimodal Large Language Models

- Authors: Hao Zheng, Zirui Pang, Ling Li, Zhijie Deng, Yuhan Pu, Zhaowei Zhu, Xiaobo Xia, Jiaheng Wei
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.8663441859485927
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.613/
- PDF: https://aclanthology.org/2026.findings-acl.613.pdf
- Local PDF: pdf/2026-07-21_30_OFFSIDE_ Benchmarking Unlearning Misinformation in Multimodal Large Language Models.pdf

Advances in Multimodal Large Language Models (MLLMs) intensify concerns about data safety, making Machine Unlearning (MU), the selective removal of harmful/private information, a critical necessity. However, existing MU benchmarks for MLLMs are limited by a lack of image diversity, coarse-grained unlearning target, and insufficient evaluation scenarios, which fail to capture the complexity of real-world applications. To facilitate the development of MLLMs unlearning and alleviate the aforementioned limitations, we introduce OFFSIDE, a novel benchmark for evaluating misinformation unlearning in MLLMs. This manually curated dataset contains 15.68K records for 80 players, providing a comprehensive framework with four test sets to assess forgetting efficacy, generalization, utility, and robustness. OFFSIDE supports advanced unlearning targets, such as fine-grained unlearning and visual rumor removal. Our extensive evaluation of multiple baselines not only extends key findings from LLM MU to MLLM MU: (1) unlearned rumors can be easily recovered through relearning and (2) all methods are vulnerable to prompt attacks, but also introduces novel insights in the context of MLLM: (1) unimodal methods fail to handle multimodal rumors, (2) unlearning efficacy is primarily driven by catastrophic forgetting statistically, and (3) all methods struggle with visual rumors (rumors embedded in images). These results expose significant vulnerabilities in current approaches, highlighting the need for more robust multimodal unlearning solutions.
