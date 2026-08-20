# Paper Daily Reading - 2026-08-20

## 1. DMT-Dens: Density-preserving manifold visualization for biological data

- Authors: Ruizhe Wang, Yixuan Dong, Bolin Yang, Bingo Wing-Kuen Ling, Fuji Yang, Zelin Zang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-18
- DOI: Unavailable
- Categories: q-bio.QM, cs.AI
- Relevance: 3.5128559683090845
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.17571v1
- PDF: https://arxiv.org/pdf/2608.17571v1
- Local PDF: pdf/2026-08-20_01_DMT-Dens_ Density-preserving manifold visualization for biological data.pdf

Motivation: Low-dimensional embeddings are widely used to explore cell-state heterogeneity in single-cell and other high-dimensional biological data. Although many methods preserve local neighborhoods, they may distort the apparent sampling density of processed observations, altering the visual contrast between dense and sparse regions and complicating the interpretation of rare, transitional, or continuous cell-state populations. Results: We present DMT-Dens, a parametric manifold-visualization method built on a latent-token Transformer encoder. The model integrates rank-based manifold alignment with hard-pair aggregation. To preserve density, it optimizes a loss based on the Pearson correlation between k-nearest-neighbor log-radius estimates in the processed input and two-dimensional embedding spaces. Benchmark evaluations demonstrate strong density preservation, particularly on biological datasets, while retaining competitive label separability. Availability: Source code, data-processing scripts, and resolved experiment configurations are available at https://github.com/Ruizhe-wang/DMT-Dens.

## 2. Causal Local States: Scalable Simultaneous Causal Network Inference and Forecasting for Dynamical Systems

- Authors: Jonas Braun, Fabian Fischbach, Daniel Köglmayr, Sebastian Baur, Christoph Räth
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-18
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.4462101126190148
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.17452v1
- PDF: https://arxiv.org/pdf/2608.17452v1
- Local PDF: pdf/2026-08-20_02_Causal Local States_ Scalable Simultaneous Causal Network Inference and Forecasting for Dynamical Systems.pdf

Machine learning methods predict many real-world systems with remarkable accuracy, but they are typically treated as black boxes that offer no insight into which interactions drive the dynamics. Causal discovery methods reconstruct the interaction network from observational data, but without regard to whether the inferred structure supports prediction. Existing approaches combining both tasks rely on a single global hyperparameter, such as a causal threshold or a fixed neighborhood size, which cannot recover the structure of heterogeneous systems. Here we introduce causal local states (CLS), a framework that simultaneously infers an approximate Granger-causal interaction network and forecasts the system dynamics. For each node independently, we select the smallest set of neighbors that allows a predictive model to forecast the node near-optimally, and the resulting neighborhoods are then combined for a forecast of the full system. On three benchmarks of increasing difficulty, we achieve reconstruction of the underlying networks with high fidelity and forecasts on par with a model that is supplied with the true network, providing a step toward explainable and scalable forecasting of complex systems.

## 3. scDNM-VAE enables directly inspectable deep clustering of single-cell RNA-seq data through signed dendritic gating

- Authors: Melih Agraz, Deniz Karapinar, Aysel Topsir, Qianying Cao, Erol Egrioglu, Gaurav Choudhary
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-18
- DOI: Unavailable
- Categories: q-bio.QM, q-bio.GN
- Relevance: 3.38581712901171
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.17228v1
- PDF: https://arxiv.org/pdf/2608.17228v1
- Local PDF: pdf/2026-08-20_03_scDNM-VAE enables directly inspectable deep clustering of single-cell RNA-seq data through signed dendritic gating.pdf

Deep clustering models for single-cell RNA sequencing often assign cells through latent or centroid-based mechanisms that are difficult to inspect. We introduce scDNM-VAE (single-cell Dendritic Neuron Model Variational Autoencoder), a deep clustering framework that combines a variational autoencoder with a dendritic neuron-inspired head. Cluster assignments are governed by learnable signed synaptic weights and thresholds: the weight sign determines the direction of a gate's response to a latent coordinate, its magnitude controls steepness, and the weight-threshold pair determines the transition location. The trained clustering function can therefore be inspected directly without fitting a post-hoc explanation model.
  We benchmark scDNM-VAE on four datasets spanning immune, cortical, cardiac, and hematopoietic cells against scVI followed by KMeans and an MLP-DEC ablation. scDNM-VAE performs better than scVI on PBMC3k, comparably on the Human Heart Cell Atlas and Paul15, and worse on Zeisel, while producing biologically coherent marker-gene signatures. Ablating each cluster's three highest-magnitude synaptic dimensions causes numerically greater reassignment than random-dimension ablation across all datasets, but the margins are modest and negligible on Zeisel. These results show that signed dendritic gating supports competitive clustering with a parameter-inspectable decision function, while indicating that decision-relevant information is distributed across the latent space.

## 4. Domain-Adapted Molecular Language Models for Efficient Search of Make-on-Demand Libraries

- Authors: Henrik Wille, Luis-Finley Schütz, Felix Strieth-Kalthoff
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-18
- DOI: Unavailable
- Categories: cs.LG, cs.AI, cs.CL
- Relevance: 3.3167106359251597
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.17567v1
- PDF: https://arxiv.org/pdf/2608.17567v1
- Local PDF: pdf/2026-08-20_04_Domain-Adapted Molecular Language Models for Efficient Search of Make-on-Demand Libraries.pdf

Pretrained molecular language models are increasingly used as molecular encoders for learning structure-property relationships. However, their practical suitability for molecular discovery within and beyond their pretraining domain remains unclear. Herein, we systematically benchmark four molecular language models across six virtual molecular libraries spanning drug discovery, organic materials, and catalysis. Native molecular language model embeddings show substantial variation in discovery performance across libraries, whereas molecular fingerprints provide a consistently strong and robust baseline. Consistent with a potential domain-representation mismatch, we show that explicit domain adaptation substantially improves representation performance. Fine-tuning molecular language model encoders on structures from the target virtual library consistently improves sample efficiency, with several adapted encoders emerging as the top-performing representations across the benchmark tasks. These results show that molecular representation quality depends strongly on the target domain and that explicit adaptation can improve the practical utility of molecular foundation models. More broadly, our findings establish domain-adapted molecular representations as a promising strategy for sample-efficient adaptive decision making in virtual screening and self-driving laboratories.

## 5. General Semantic Knowledge Infusion for Spatio-Temporal Traffic Forecasting

- Authors: Mattis thor Straten, Yannick Wolker, Steffen Strohm, Prathvish Mithare, Ralf Krestel, Matthias Renz
- Source: arxiv
- Venue type: preprint
- Journal: M. t. Straten, et al. "General Semantic Knowledge Infusion for Spatio-Temporal Traffic Forecasting," 2026 27th IEEE International Conference on Mobile Data Management (MDM), Athens, Greece, 2026, pp. 44-51
- Publication status: preprint
- Publication date: 2026-08-18
- DOI: 10.1109/MDM71479.2026.00016
- Categories: cs.LG
- Relevance: 3.2644834341256805
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.17440v1
- PDF: https://arxiv.org/pdf/2608.17440v1
- Local PDF: pdf/2026-08-20_05_General Semantic Knowledge Infusion for Spatio-Temporal Traffic Forecasting.pdf

Although Graph Neural Networks (GNNs) have made significant advances in spatio-temporal traffic forecasting, their performance is limited when they rely solely on sensor proximity or road-network topology. This paper presents a spatio-temporal prediction framework, developed to incorporate knowledge in various forms. This framework aims to improve sensor-level, contextual understanding of the environment. A general-purpose knowledge graph (e.g., Wikidata) is used to create semantic subgraphs around traffic sensors and generate knowledge graph embeddings that capture meaningful relationships, such as nearby points of interest, administrative hierarchies, and the functional roles of locations. These embeddings are then fused with conventional traffic sensor graphs to provide additional adjacency matrices informed by semantics. This allows GNNs to learn the semantic context beyond physical connectivity. This study differs from previous research in two key ways. Firstly, rather than proposing a novel GNN architecture, it demonstrates the general impact of external knowledge on prediction accuracy. Secondly, experiments with well-established traffic forecasting approaches show that external knowledge provides additional information that street network data alone cannot convey. The results show that integrating data from general-purpose knowledge graphs and sensor networks through data fusion can enhance the prediction accuracy of traffic forecasting models, and offers a potential pathway toward improved interpretability.

## 6. Lymphocyte Mimicry Correction via Region-Level Tissue Reasoning and Unbalanced Optimal Transport

- Authors: Xiang Li, Yuqi Wang, Casey C. Heirman, Jihye Heo, Kyle J. Lafata
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-17
- DOI: Unavailable
- Categories: cs.CV, cs.LG
- Relevance: 3.2053295532784247
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.17151v1
- PDF: https://arxiv.org/pdf/2608.17151v1
- Local PDF: pdf/2026-08-20_06_Lymphocyte Mimicry Correction via Region-Level Tissue Reasoning and Unbalanced Optimal Transport.pdf

Cell mimicry arises when different cell types appear morphologically similar. Human pathologists resolve this ambiguity using surrounding tissue context, whereas current vision models either lack contextual reasoning (cell foundation models) or cannot operate at the cell level (pathology MLLMs). We present Loki-OT, which propagates region-level tissue reasoning to individual cell predictions via Unbalanced Optimal Transport, using MLLM-derived density priors as soft guidance for ambiguous cell reassignment. Loki-OT is motivated by the observation that pretrained cell foundation model features already encode discriminative information, including tissue context, but standard cell-level supervision fails to use tissue context effectively. The resulting transport plan is distilled into a lightweight student MLP classifier that learns context-aware decision boundaries within the pretrained feature space. On the independent TCGA-BRCA cohort, Loki-OT achieved lower patient-level MAE than the fully supervised in-domain PanopTILs classifier and improved F1 in epithelium-rich mimicry tissues, using 278 weak region-level MLLM estimates built on a general-domain cell foundation model. Code: https://github.com/xiangli980/Lymphocyte_Mimicry_Correction_via_Loki_OT

## 7. Causal Discovery in Equal Variance Linear Gaussian DAGs via SURE-Tuned Ridge Regression

- Authors: Sambit Mishra, Urbashi Mitra
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-17
- DOI: Unavailable
- Categories: cs.LG, eess.SP, stat.ML
- Relevance: 3.192994877131726
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.17132v1
- PDF: https://arxiv.org/pdf/2608.17132v1
- Local PDF: pdf/2026-08-20_07_Causal Discovery in Equal Variance Linear Gaussian DAGs via SURE-Tuned Ridge Regression.pdf

Recovering the directed acyclic graph (DAG) of a structural equation model (SEM) from observational data is a central problem in causal discovery. The iterative gradient descent and per-problem hyperparameter tuning of continuous-optimization methods are poorly suited to two practically important regimes: the sample-limited regime, where the number of samples is comparable to or smaller than the number of nodes in the DAG, and the compute-limited regime. This work proposes SURE-Ridge, a non-iterative, closed-form estimator for equal variance linear Gaussian SEM. The method performs parallel node-wise regressions with regularization parameters chosen adaptively by Stein's unbiased risk estimate (SURE), and applies an adaptive thresholding procedure to extract a DAG from the resulting soft adjacency matrix. Numerical results show that SURE-Ridge achieves the lowest structural Hamming distance in the small-sample regime and the lowest run time across all sample sizes tested, compared with NOTEARS, DAGMA, and GBNSL baselines.

## 8. Margin-Regularized Structured Semantic Alignment for Brain-Language Correspondence

- Authors: Jiaqi Wang, Huawen Hu, Shu Zhang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-17
- DOI: Unavailable
- Categories: cs.CL, cs.LG
- Relevance: 3.1896818135799014
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.16975v1
- PDF: https://arxiv.org/pdf/2608.16975v1
- Local PDF: pdf/2026-08-20_08_Margin-Regularized Structured Semantic Alignment for Brain-Language Correspondence.pdf

With the rapid advancement of large language models, brain-language decoding has achieved remarkable progress. However, it remains unclear whether decoded content genuinely reflects neural representations or is largely reconstructed by the language model itself. This ambiguity limits interpretability and hinders the investigation of intrinsic brain-language correspondence. To address this challenge, we propose MD-SigLIP. This margin-regularized structured semantic alignment framework directly aligns brain embeddings with text embeddings in a shared semantic space, enabling retrieval-based decoding. This formulation enables explicit modeling of the correspondence between neural representations and language semantics. Building upon duplicate-aware sigmoid contrastive learning, we introduce a listwise margin-regularized term that enforces structured ranking constraints between positive semantic clusters and negative samples. By modeling multi-positive semantic structure and margin-based ordering simultaneously, the method captures the manifold organization of language embeddings reflected in neural signals. Experiments demonstrate state-of-the-art retrieval performance under both full-vocabulary and subset evaluation settings.

## 9. Single-cell foundation models benefit from cross-modal training: adding proteomics data beats parameter scaling

- Authors: Burq, M., Stepec, D., Kim, C., Cimermancic, P.
- Source: biorxiv
- Venue type: preprint
- Journal: biorxiv
- Publication status: preprint
- Publication date: 2026-08-19
- DOI: 10.64898/2026.08.14.744845
- Categories: bioinformatics
- Relevance: 3.185295848022684
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://www.biorxiv.org/content/10.64898/2026.08.14.744845v1.full.pdf
- PDF: https://www.biorxiv.org/content/10.64898/2026.08.14.744845v1.full.pdf
- Local PDF: Not downloaded

Leading cellular foundation models have been trained on hundreds of millions of single-cell transcriptomes, with progress increasingly driven by larger datasets and model scaling. Here, we asked whether adding a proteomics modality can improve gene-level and cell-level representations beyond scaling RNA-only models. We introduce cross-modal continued pretraining, fine-tuning a published single-cell model (Tahoe-x1) on a large corpus of proteomic profiles. Training a 70M-parameter Tahoe-x1 model for a single epoch on 48843 proteomic samples from 440 diverse mass-spectrometry studies matched or exceeded 1B- and 3B-parameter RNA-only models across most of the original Tahoe-x1 evaluation benchmarks. This shows that with the right training recipe, heterogeneous proteomics data can improve the learned representations of single-cell RNAseq samples, demonstrating strong out-of-distribution generalization. Cross-modal pretraining also improves transfer to a held-out protein perturbation benchmark, where scaling the RNA-only model does not provide comparable benefits. These results demonstrate that careful targeted curation of proteomics data can provide larger benefits than increasing the model size alone and suggest that multimodal pretraining is a promising path toward more informative biological foundation models.

## 10. Network Denoising Revisited: A Ricci-Flow-Inspired Graph Diffusion Method

- Authors: Ye Fang, Chuan-Xian Ren
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-04
- DOI: Unavailable
- Categories: cs.SI, cs.LG
- Relevance: 3.1785171042345968
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.16923v1
- PDF: https://arxiv.org/pdf/2608.16923v1
- Local PDF: pdf/2026-08-20_10_Network Denoising Revisited_ A Ricci-Flow-Inspired Graph Diffusion Method.pdf

Networks provide a fundamental representation of relationships among entities. However, real-world networks are often corrupted by noise caused by measurement errors and inherent stochasticity, hindering the discovery of meaningful structure. Most denoising methods rely on similarity-driven diffusion and ignore the non-Euclidean geometry of graphs, where local variations induce heterogeneous information transport. This motivates a geometric revisit of network denoising. In this work, we propose Ricci-Diffusion, a curvature-guided graph diffusion method inspired by Ricci flow. Specifically, Ricci-Diffusion exhibits a Ricci-flow-like evolution, in which relative edge-level curvature modulates local transport in the diffusion kernel and guides edge-weight updates toward a more regular graph geometry. We further provide a theoretical analysis showing that curvature can distinguish graph structures that common similarity-driven diffusion kernels fail to separate, and that curvature induces first-order corrections in one-step diffusion updates. The resulting diffusion process explicitly characterizes transport heterogeneity across local geometries and admits theoretical convergence to a stable denoised network. Results on real-world and synthetic graphs show that curvature-guided updates and curvature homogenization improve structure recovery and downstream performance.

## 11. MoRAX: Mobility-based Representation Augmentation for Geospatial Foundation Models

- Authors: Ya Wen, Jixuan Cai, Yulun Zhou, Alec Kirkley
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-18
- DOI: Unavailable
- Categories: cs.LG, cs.SI
- Relevance: 3.1142095272494985
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.17848v1
- PDF: https://arxiv.org/pdf/2608.17848v1
- Local PDF: pdf/2026-08-20_11_MoRAX_ Mobility-based Representation Augmentation for Geospatial Foundation Models.pdf

Geospatial Foundation Models (GFMs) are emerging as a powerful paradigm for learning semantically rich and geographically consistent visual and physical representations. However, their reliance on Earth-observation (EO) data leaves information about human activity largely underrepresented. Human mobility data reveals the functional and relational structure between regions that is missing from EO data, but is often limited only to the city where it is observed, making it challenging to use for transferable urban representation learning. We introduce MoRAX, a lightweight framework for augmenting geospatial embeddings with functional structure derived from human mobility. MoRAX preserves the coverage and consistency of a GFM while providing information about the functional connectivity among urban regions, permitting zero-shot deployment in unseen cities with or without available mobility data. Across four target cities spanning two countries, the MoRAX teacher model, which observes mobility, consistently outperforms GFMs and strong urban representation baselines in eight socioeconomic and environmental prediction tasks. Meanwhile, the student model, which never takes mobility data as input, approaches the teacher in performance on most tasks. Transfer results across countries further demonstrate that modulation conditioned on mobility flows provides a general mechanism for grounding geospatial foundations in the human dimension of cities.

## 12. Structure-Internalized Rule Language Model for Faithful Knowledge Graph Reasoning

- Authors: Xingrui Zhuo, Jiapu Wang, Manzong Huang, Gongqing Wu, Xindong Wu
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-18
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 3.1084785422177537
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.17443v1
- PDF: https://arxiv.org/pdf/2608.17443v1
- Local PDF: pdf/2026-08-20_12_Structure-Internalized Rule Language Model for Faithful Knowledge Graph Reasoning.pdf

Knowledge Graph Reasoning (KGR) aims to discover latent facts by leveraging the structural evidence available in KGs, posing a challenge to the structural semantic understanding capability of KGR models. Recent studies have demonstrated that Large Language Models (LLMs) can achieve remarkable progress on KGR tasks via flexible in-context learning. However, the inherent representation inconsistency between KG structural context and LLM parametric knowledge remains inadequately addressed. This limitation prevents LLMs from effectively perceiving reasoning evidence that aligns with KG constraints, which undermines both the effectiveness and faithfulness of reasoning. We refer to this problem as reasoning evidence perception drift of LLMs over KGs. To address this problem, we propose a Structure-Internalized Rule Language Model (SIRLM), which centers on structural rule generation to couple the parametric learning of structural knowledge with the faithfulness evaluation of reasoning logic, enabling LLMs to anchor tightly to KG-grounded evidence. Specifically, we first design a Structure-Internalized Rule Generator (SIRG), which incorporates an in-context learning block augmented with a structural relation memory to coordinate structural and parametric knowledge. Furthermore, we equip SIRG with a KG tokenizer based on structural invariance learning and a neuro-symbolic reasoner based on rule-constrained message propagation. These components provide SIRG with learnable structural representations and faithful rule-execution feedback, respectively. Our SIRLM can be seamlessly integrated into standard LLM training paradigms, such as SFT and GRPO. Extensive experiments against 17 state-of-the-art KGR methods on 36 datasets demonstrate the significant superiority of SIRLM.

## 13. Pathology Transport: Optimal-Transport Explanations for Clinical Data, and When Their Heatmaps (Fail to) Localize Disease

- Authors: Lalit Kumar
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-18
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.1046587393658664
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.17370v1
- PDF: https://arxiv.org/pdf/2608.17370v1
- Local PDF: pdf/2026-08-20_13_Pathology Transport_ Optimal-Transport Explanations for Clinical Data, and When Their Heatmaps (Fail to) Localize Diseas.pdf

Generative models promise a route to explainable clinical AI: rather than probe a classifier, model the distributions of healthy and diseased patients and read explanations off the geometry between them. We build such a system - an optimal-transport rectified flow trained between two clinical distributions - and use it to ask a pointed question the field too rarely tests: do the resulting explanation heatmaps actually localize disease? On tabular tumour biomarkers (Breast Cancer Wisconsin) a single flow yields per-patient counterfactuals, an unsupervised malignancy score (AUROC 0.91; 0.93 +/- 0.01 across five seeds), and a label-free attribution that agrees with a supervised classifier (r ~ 0.5) - a compact, honest interpretability engine, though it never out-predicts logistic regression. Moving to chest X-rays, we show the transport heatmap is a population-level signal, not a localiser; a reconstruction-based, identity-preserving variant does localize synthetic lesions (pointing game 0.52), yet on real RSNA radiologist boxes it collapses to chance while only supervised Grad-CAM stays above it. The central result is a synthetic-to-real gap: label-free heatmaps that look compelling on planted lesions are not evidence of real localisation. We contribute a reusable optimal-transport recipe for generative explanations and a controlled benchmark for stress-testing whether they localize.

## 14. Method Choice, Not Biology, Determines In Silico Perturbation Results: A Systematic Evaluation of Eight Methods Across Four Datasets

- Authors: Wenjie, G., Wu, S., Hu, G., Yang, Z., Wang, Z., Cai, J., Mao, J.
- Source: biorxiv
- Venue type: preprint
- Journal: biorxiv
- Publication status: preprint
- Publication date: 2026-08-19
- DOI: 10.64898/2026.08.11.744106
- Categories: bioinformatics
- Relevance: 3.085104993521741
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://www.biorxiv.org/content/10.64898/2026.08.11.744106v1.full.pdf
- PDF: https://www.biorxiv.org/content/10.64898/2026.08.11.744106v1.full.pdf
- Local PDF: Not downloaded

Most in silico perturbation methods for single-cell transcriptomics have been validated only on individual datasets, leaving their reliability and generalizability unknown. Through systematic cross-method, cross-dataset benchmarking of eight methods spanning six mathematical frameworks across four datasets, we find that six of eight methods--including widely used VAE-based and tensor decomposition approaches--fail to produce detectable transcription factor (TF)-to-pathway signals. Only CellOracle and DDIM consistently detected TF-to-glycolysis directional regulation. Cross-pathway analysis in PBMC monocytes revealed biologically coherent TF-pathway associations beyond glycolysis (SPI1[-&gt;]glycolysis 4.4x enrichment, FOS[-&gt;]AP-1 targets 4.4x), with SOX9 serving as a biological specificity control (no pathway enrichment). Method choice alone could reverse biological conclusions: DDIM and scTenifoldKnk rankings were significantly anti-correlated ({rho}=-0.811, p=0.027). CRISPRi Perturb-seq validation in K562 cells confirmed TF knockdown suppresses glycolysis gene expression (JUN {delta}=-1.72, CEBPB {delta}=-1.59, SPI1 {delta}=-1.57, FOS {delta}=-0.70), but CellOracle-predicted perturbation directions did not match experimental directions (40.9% agreement, not different from chance), revealing a fundamental gap between steady-state correlation and causal perturbation. Diagnostic analyses using VAE latent space profiling, correlation distribution comparison, and gene-gene graph analysis identified distinct failure modes in unsuccessful methods: VAE latent space competition (STAT3 signal-to-noise 0.44 vs. SPI1 4.25), correlation noise (TF-glycolysis |r|=0.038 indistinguishable from background |r|=0.047), and graph non-specificity (0.84x enrichment). A controlled ablation experiment showed that adding a GRN prior to DDIM did not improve target recall (delta=0 for all TFs), confirming that performance differences are multi-factorial. These findings establish preliminary guidance for method selection, including cross-pathway validation, direction-aware benchmarking, and minimum data requirements ([&ge;]500 cells, [&ge;]1,000 HVGs).

## 15. From Corpora to Co-Evolving Capabilities: Capability-Centric Data Design for Generalist Image Generation

- Authors: Xingjian Wang, Zhao Wang, Taihang Hu, Jun Zheng, Qing Jin, Qinye Zhou, Zhengtao Wu, Yongchao Du, Zuan Gao, Chao Lin, Yefeng Shen, Xiaoli Xu, Zhengze Xu, Hao Yan, Yuhang Yu, Mingzhou Zhang, Mengting Chen
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-18
- DOI: Unavailable
- Categories: cs.CV, cs.AI
- Relevance: 3.059532721805152
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.18076v1
- PDF: https://arxiv.org/pdf/2608.18076v1
- Local PDF: pdf/2026-08-20_15_From Corpora to Co-Evolving Capabilities_ Capability-Centric Data Design for Generalist Image Generation.pdf

Large-scale image generation has benefited from advances in data scale, quality, rebalancing, and recaptioning, yet conventional pipelines typically optimize task-specific datasets in isolation. A central challenge is not only how to curate each task-specific corpus, but also how to organize heterogeneous supervision according to the dependencies among generative capabilities. We present a \textbf{capability-driven data infrastructure} that couples capability-specific supervision construction with capability-aligned curriculum scheduling. Its three specialized yet interoperable data engines build complementary relational supervision for text-image grounding, inter-image transformation, and image-knowledge association, while caption experts align T2I and editing supervision across tasks and granularities. A multi-stage curriculum jointly evolves task composition, visual-concept distribution, data quality, and image resolution along the dependency order of capability acquisition, with capability-aware evaluation closing the loop through targeted retrieval, expert construction, and gap-aware resampling. At scale, the framework curates a 440M-image T2I corpus, 120M editing pairs, and over 27M image-entity pairs. With this infrastructure, we train multimodal diffusion models at two scales from scratch, with 3B and 6B sizes respectively. We conduct quantitative evaluation on CPI-Bench, along with qualitative evaluations across diverse text-to-image and editing scenarios. Experimental results present broad visual coverage, versatile rendering, and effective transfer across generative capabilities.

## 16. Signature Recontextualization: Mapping perturbational signatures across biological contexts

- Authors: Chen, A. D., Girke, T., Monti, S.
- Source: biorxiv
- Venue type: preprint
- Journal: biorxiv
- Publication status: preprint
- Publication date: 2026-08-19
- DOI: 10.64898/2026.08.14.744937
- Categories: bioinformatics
- Relevance: 3.047924997493446
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://www.biorxiv.org/content/10.64898/2026.08.14.744937v1.full.pdf
- PDF: https://www.biorxiv.org/content/10.64898/2026.08.14.744937v1.full.pdf
- Local PDF: Not downloaded

Perturbational transcriptomics is a powerful tool for understanding gene function and drug effects, yet predicting how perturbations manifest across different biological contexts remains a central challenge, limiting translation from model systems to clinically relevant tissues. Despite growing interest in this problem, benchmarking efforts have been hindered by inconsistent evaluation tasks, heterogeneous metrics, and limited assessment across perturbation types and biological systems. Here, we introduce a benchmarking framework for cross-context perturbation-signature prediction (a task we define as signature recontextualization), grounded in explicit definitions of the prediction task, target-data availability, and evaluation metrics centered on signature recovery. The framework evaluates prediction performance across three target-context data regimes: (1) control only, where only control profiles from the target context are measured; (2) low coverage, where a limited subset of perturbations in the target context are measured; and (3) high coverage, where most perturbations in the target context are measured. This design enables systematic assessment of how prediction performance depends on target-context sample size while providing a standardized basis for comparing methods. We evaluate newly developed projection-based (projectCor) and network-based (netProp) methods alongside deep learning-based foundation models (scGPT, STACK) and statistical baselines. The benchmark spans four diverse perturbational datasets: CRISPR knockdowns and drug perturbations in cell lines, plus in vivo chemical perturbations in rat tissues from DrugMatrix, extending evaluation beyond isolated cell-line models to tissue-level responses. Across tasks, projection and network propagation approaches show strong flexibility across perturbation types and biological contexts, and in several cases match or exceed the performance of deep learning and foundation models, suggesting that model complexity does not inherently improve cross-context generalization. We further show that perturbation predictability varies substantially with pathway conservation, transcriptional response strength, and baseline similarity between source and target contexts. All datasets, methods, and evaluation utilities are released as an open-source R package (sigRecon), providing a foundation for reproducible benchmarking and future method development.

## 17. When to Review: Spaced Repetition for Continual Pre-Training of Language Models

- Authors: Alankar Atreya, Devesh Batra, Yoages Kumar Mantri, Geremy Bantug, Greig A Cowan, Raad Khraishi
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-18
- DOI: Unavailable
- Categories: cs.AI, cs.LG
- Relevance: 3.035120206851864
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.17530v1
- PDF: https://arxiv.org/pdf/2608.17530v1
- Local PDF: pdf/2026-08-20_17_When to Review_ Spaced Repetition for Continual Pre-Training of Language Models.pdf

Continual pre-training of large language models must acquire new information without erasing old knowledge. Existing replay methods often choose a global old/new mixture and sample uniformly, ignoring that examples differ in how quickly they are forgotten. We formulate continual pre-training as adaptive review scheduling: the training loop should decide not only how much history to replay, but which examples should return at each step. We introduce Spaced Repetition Training (SRT), a continual learning framework inspired by cognitive science, which schedules sample-rehearsal using the SuperMemo-2 (SM-2) algorithm. SRT maintains per-example review state, maps per-example perplexity to a recall-quality signal, and schedules historical examples for retention and new examples for consolidation while leaving the model, objective, and optimizer unchanged. On temporally separated Wikipedia and code corpora, SRT improves the stability-plasticity trade-off, recovering 5 to 37 percentage points of old-knowledge accuracy lost by naive continual pre-training across model scales while preserving or improving new-knowledge acquisition. At larger scale, SRT preserves broad benchmark performance that naive continual pre-training and uniform replay substantially degrade. Experiments with vision and tabular data further suggest that the scheduling principle extends beyond language when paired with an appropriate recall signal.

## 18. Recirculation

- Authors: Michael C. Mozer, Shoaib Ahmed Siddiqui, Danny Sawyer, Sunny Sanyal, Rosanne Liu
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-18
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.0045712037487613
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.17981v1
- PDF: https://arxiv.org/pdf/2608.17981v1
- Local PDF: pdf/2026-08-20_18_Recirculation.pdf

We describe an inference-time architectural enhancement for off-the-shelf foundation models that markedly reduces perplexity and boosts accuracy across generation and reasoning tasks. Our approach incurs essentially no additional latency during generation, though it requires serial processing in the prefill phase. Motivated by the fundamental limitation that state updates in feedforward transformers are bounded by model depth, our technique, recirculation, introduces a specific form of recurrence that allows the model to act as a dynamical system and track belief states. We distinguish this technique from chain-of-thought computation---which is better reserved for complex inferences rather than basic state tracking---as well as from popular depth-recurrence techniques (looping) and the costly training of recurrent transformers. We also propose and evaluate an adaptive variant of recirculation which requires only light tuning of hyperparameters while freezing the original model weights. Relative to the off-the-shelf baseline, adaptive recirculation achieves remarkable gains on the Gemma3 family, including a 23% reduction in perplexity on a suite of datasets, a 21% increase in accuracy on GSM8k, and reliable improvements in accuracy on other downstream tasks. Our training-free approach succeeds by leveraging the model itself to inform architectural modifications, suggesting a route to architectural evolution guided by a trained network's properties rather than forced, arbitrary design choices.

## 19. Synthesizing Feature Extractors: An Agentic Approach for Algorithm Selection

- Authors: Hai Xia, Carlos Ansótegui, Stefan Szeider
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-17
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 3.0020750973766033
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.17170v1
- PDF: https://arxiv.org/pdf/2608.17170v1
- Local PDF: pdf/2026-08-20_19_Synthesizing Feature Extractors_ An Agentic Approach for Algorithm Selection.pdf

Algorithm selection for constraint satisfaction problems requires extracting features that capture problem structure. Manually designing feature extractors demands deep domain expertise and quickly becomes a bottleneck when new problem classes appear. We present an automated approach that uses Large Language Models (LLMs) in an agentic check--fix--verify loop to synthesize executable Python scripts that act as interpretable, problem-specific feature extractors. Given a high-level MiniZinc model and an instance, the LLM agent generates code that constructs a typed graph representation and computes structural properties such as graph density, variable clustering, and constraint tightness. We evaluate our approach on three combinatorial problems (vehicle routing, car sequencing, fixed-length error-correcting codes) with a portfolio of five state-of-the-art solvers. The synthesized extractors yield algorithm selectors that consistently outperform both expert-curated mzn2feat features (up to $8.3$ percentage points (pp) test-set accuracy on FLECC) and the best transformer-based trans2feat variants. In the meanwhile, the synthesized feature extractors remain inspectable.

## 20. Abra: Scaling Diffusion Image Training

- Authors: Kyle Chickering, Wei-An Lin, Swayam Bhanded, Dan Saunders, Akshat Tripathi, Jiaming Song, Shyamal Buch, Xinchen Yan
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-18
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 2.9915564799521843
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.17286v1
- PDF: https://arxiv.org/pdf/2608.17286v1
- Local PDF: pdf/2026-08-20_20_Abra_ Scaling Diffusion Image Training.pdf

Compute-optimal scaling laws guide the training of frontier language models yet remain largely unexplored for visual generation. We present a systematic scaling law study for text-to-image diffusion models using Abra, a controlled family of flow-matching transformers trained across three orders of magnitude worth of compute ($10^{19}$ to $10^{22}$ FLOPs), reaching significantly larger compute budgets than previous works. We demonstrate that diffusion models scale just as predictably as language models but require far more data to train optimally: compute optimality occurs at approximately $200$ image tokens per parameter, ten times the Chinchilla compute-optimal prescription for LLMs. We show that unlike language models, diffusion models are robust to overtraining and that practitioners should err on the side of more data rather than a larger model. Finally, we show that this predictability extends beyond training loss to generative quality metrics, optimal CFG settings, representation quality, and even the shape of the training curves, which collapse onto a universal form.

## 21. Understanding the Surprising Generalization Properties of Tabular Foundation Models

- Authors: Nour Shaheen, Junwei Ma, Alex Labach, Frank Hutter, Valentin Thomas, Anthony L. Caterini
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-18
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 2.9776980402264694
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.17957v1
- PDF: https://arxiv.org/pdf/2608.17957v1
- Local PDF: pdf/2026-08-20_21_Understanding the Surprising Generalization Properties of Tabular Foundation Models.pdf

Tabular Foundation Models (TFMs) increasingly rely on in-context learning, where a model receives labelled examples at inference time and predicts labels for new inputs without updating its weights. Existing TFMs are typically trained on either massive synthetic corpora or very large collections of real datasets. In contrast, we show that surprisingly strong transfer can emerge from self-supervised pre-training on just a single real table. In this setting, we also find that tables tend to be either broadly useful or broadly poor regardless of downstream prediction task, and that the strongest predictor of usefulness is the number of features rather than the number of instances. This leads to a task-centric interpretation of tabular pre-training: the number and the quality of tasks are essential for the pre-training of TFMs.
  We show that the same task-centric perspective can help corpus design at scale: fine-grained column-level pre-processing consistently improves downstream performance, while no improvements are observed when we filter or deduplicate at the dataset level.
  Finally, we offer a new perspective for how TFMs generalize: we believe that tabular in-context generalization is largely retrieval-based, and good models are those that learn to identify relevant examples in the provided context and aggregate them well. The mechanics of TFMs have been relatively understudied; our task-centric, retrieval-based perspective offers a new framework to guide future model and corpus design.

## 22. Encoded but Not Actionable: Auditing the Decode-Generate-Steer Gap in Frozen LLMs for Geometric Constraints

- Authors: Man Liang, Xinzhao Cheng, Faizan Wajid
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-18
- DOI: Unavailable
- Categories: cs.CL, cs.AI
- Relevance: 2.9460963975210985
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.17843v1
- PDF: https://arxiv.org/pdf/2608.17843v1
- Local PDF: pdf/2026-08-20_22_Encoded but Not Actionable_ Auditing the Decode-Generate-Steer Gap in Frozen LLMs for Geometric Constraints.pdf

Large language models (LLMs) have demonstrated strong performance on structured reasoning tasks, but what they encode and whether it informs model behavior remain unclear. We investigate this question through geometric reasoning, using parametric CAD constraints as a controlled testbed for separating local pairwise relations from sketch-level constraint status. By probing the hidden states of six frozen decoder-only LLMs, we examine four properties: linear decodability, forced-choice generation, activation-level influence, and behavioral steerability. Pretraining substantially improves the decoding of local geometric relations, and this advantage persists after accounting for positional cues with shuffled-order controls. In contrast, sketch-level DOF status is already highly decodable from randomly initialized representations and improves only modestly with pretraining, indicating that much of its probe performance is available without learned weights. Further analyses show that decodable information is not always actionable. Generation often fails to express this information, and on the two intervention-tested backbones, activation-restoration effects at the patched entity position vanish while decodability persists across depth. Mean-difference steering also does not reliably control outputs. These results show that decodability, generation, activation-level influence, and steerability can diverge in the tested setting. The audit provides a controlled way to distinguish failures to encode geometric structure from failures to express or control encoded information.

## 23. TileMix: Tile-Centric Mixed-Precision Attention for LLM Inference Acceleration

- Authors: Hanzhi Zhang, Qiao Zhang, Qinglei Cao, Heng Fan, Yan Huang, Kewei Sha, Yunhe Feng
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-18
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 2.941305623440268
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.17336v1
- PDF: https://arxiv.org/pdf/2608.17336v1
- Local PDF: pdf/2026-08-20_23_TileMix_ Tile-Centric Mixed-Precision Attention for LLM Inference Acceleration.pdf

Long-context prefill in large language models (LLMs) incurs substantial computation and memory traffic because dense self-attention computes quadratic query-key scores. Existing methods either use a uniform low-precision path or select token interactions, leaving spatial precision routing over hardware-aligned score tiles outside fused dense attention. We introduce TileMix, a tile-centric precision-routing kernel that makes numerical precision an executable spatial decision over score-tile groups within fused dense attention. TileMix partitions the attention matrix into hardware-aligned score tiles, packs routing decisions into compact bitmasks, and dispatches each tile group through FP16 or INT8 score computation while both paths update a shared online-softmax state. Scalable precision grouping lets each routing bit govern multiple adjacent key tiles, preserving hardware-aligned compute tiles and compact metadata at long contexts. By routing all legal tile groups, TileMix preserves dense token connectivity, requires no training, and supports grouped-query attention, variable-length batches, and INT8 key/value caches. Across LongEval, LV-Eval, and A100 prefill benchmarks on LLaMA, Qwen, and Vicuna, TileMix recovers long-context quality lost under uniform INT8 and improves prefill throughput over FP16, yielding a controllable accuracy-efficiency frontier across model families. The implementation is available at https://github.com/HanzhiZhang-Ulrica/TileMix.

## 24. Efficient RLVR Scheduling via Graph-Structured Online Difficulty Estimation

- Authors: Zhizhao Liu, Zhiliang Tian, Xi Wang, Zhihua Wen, Yihang Xiong, Zhiquan Lai, Dongsheng Li
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-18
- DOI: Unavailable
- Categories: cs.LG, cs.AI, cs.CL
- Relevance: 2.8786992136503313
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.17941v1
- PDF: https://arxiv.org/pdf/2608.17941v1
- Local PDF: pdf/2026-08-20_24_Efficient RLVR Scheduling via Graph-Structured Online Difficulty Estimation.pdf

Reinforcement learning with verifiable rewards (RLVR) improves the reasoning capabilities of large language models but relies on costly rollout exploration. Assigning the same exploration budget to samples with different difficulty levels is inefficient: easy samples may receive redundant rollouts, whereas difficult but learnable samples may receive too little exploration. Existing adaptive schedulers address this mismatch through curriculum-based sample selection or non-uniform rollout allocation based on estimated sample difficulty. However, obtaining reliable online difficulty estimates remains challenging: dedicated probing adds substantial generation overhead, whereas history-based estimators face a cold start with no initial observations and stale feedback, and typically ignore relations among samples. To address these limitations, we propose a plug-and-play graph-based online difficulty estimator that shares rollout feedback across related samples and continuously updates their difficulty estimates, mitigating cold start and staleness without dedicated probing. Specifically, we first construct a difficulty-aware sample graph based on semantic and reasoning similarities. Based on this graph, we introduce latent difficulty states and use a Potts prior to encourage neighboring samples to share the same state. We then employ a state-level Beta-Binomial model to aggregate the rollout outcomes associated with each state. Finally, we use an online mean-field variational algorithm to continuously update the latent-state assignments and state-level difficulty as new feedback arrives. Our framework can be integrated into sample-selection and rollout-allocation schedulers, enabling difficulty-adaptive exploration without dedicated probing. Experiments across multiple base models, RL schedulers, and benchmarks demonstrate that our framework achieves better performance.

## 25. Mixture-of-Expert Blocks Contain Strong Hallucination Detection Signals

- Authors: Joao Fonseca, Rodrigo Rodrigues, Paolo Romano
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-18
- DOI: Unavailable
- Categories: cs.AI, cs.LG
- Relevance: 2.8773840863153377
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.17687v1
- PDF: https://arxiv.org/pdf/2608.17687v1
- Local PDF: pdf/2026-08-20_25_Mixture-of-Expert Blocks Contain Strong Hallucination Detection Signals.pdf

Despite their widespread use, Large Language Models (LLMs) remain limited by a fundamental problem: the generation of plausible but false content, known as hallucinations. Most existing detection methods operate at the answer or sentence level, yet per-token detection is essential for localizing hallucinated spans and enabling fine-grained interventions. In this paper, we explore the use of the Mixture-of-Experts (MoE) paradigm to address this gap. In MoE architectures, a single forward pass activates a sparse subset of experts (i.e., distinct feedforward networks per layer) via a routing mechanism, producing internal signals (e.g., router entropy, expert disagreement, and expert usage patterns) that are unavailable in dense architectures and have not been previously exploited for hallucination detection. To this end, we introduce InnerExpert, the first method to leverage these MoE-specific signals for per-token hallucination detection. InnerExpert combines routing-level and standard transformer signals into compact per-token feature vectors, classified by a lightweight detector trained on labels produced by an LLM-as-a-judge pipeline, which enables continuous model updates without manual annotation. Our results show that InnerExpert outperforms existing methods across five datasets and two MoE architectures, achieving up to 0.91 answer-level and 0.76 token-level AUROC, while requiring only a single forward pass.

## 26. Information Spreading in Diffusion Models from Effective Field Theory

- Authors: Navonil Neogi, Nabil Iqbal
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-14
- DOI: Unavailable
- Categories: hep-th, cond-mat.stat-mech, cs.LG
- Relevance: 2.867435073193052
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.14308v1
- PDF: https://arxiv.org/pdf/2608.14308v1
- Local PDF: pdf/2026-08-20_26_Information Spreading in Diffusion Models from Effective Field Theory.pdf

We study score-matching diffusion models with a convolutional architecture. We argue that the inductive bias of locality means that the machinery of effective field theory from physics can be usefully applied to describe the denoising dynamics. We apply this formalism first to a simple toy example which permits an analytical description, and thereafter to MNIST, and show that in both cases, the mutual information between two points grows in a manner predicted by a simple effective field theory of Brownian motion.

## 27. Cross-Model Memory Transfer via Target-Side Reader Adaptation

- Authors: Mingyuan Li, Guangsheng Yu, Xu Wang, Shaoxiong Ji
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-17
- DOI: Unavailable
- Categories: cs.CL, cs.AI
- Relevance: 2.8596916379277015
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.17050v1
- PDF: https://arxiv.org/pdf/2608.17050v1
- Local PDF: pdf/2026-08-20_27_Cross-Model Memory Transfer via Target-Side Reader Adaptation.pdf

Methods for improving knowledge use in large language models typically fall into two regimes. Non-parametric retrieval offers flexible access to external knowledge, but adds retrieval latency, context overhead, and only shallow integration with the backbone. Parametric adaptation is efficient at inference time, but entangles knowledge with model weights and can be hard to update, audit, or transfer. Engram-style hashed memory occupies a middle regime: it stores learned information in an external, addressable table, yet consumes that table through a small learned reader. This raises a basic question: when such a memory is moved across backbones, what matters more, the frozen memory itself or the target-side reader? We study this question through cross-model frozen-memory extraction, in which a memory trained on a source model is frozen and attached to a different target model, with only a lightweight reader trained. Ablations show that learned memory content and correct addressing both matter, but the transferred table becomes useful only through a reader aligned to the target model. In downstream question answering tasks, a dual-layer, four-branch reader nearly closes the gap between same-model and cross-model reuse, achieving an average score of 38.8 under our controlled evaluation protocol. Moreover, when the provider reader is directly compatible with the target interface, the frozen artifact can provide substantial utility without target-side training, while optional reader adaptation yields further improvement. These results suggest that Engram can serve as a reusable external knowledge artifact, provided that the target has access to a compatible reader interface; target-side adaptation can further improve alignment when direct reader reuse is insufficient.

## 28. Decoding the sequence determinants of locus-specific DNA methylation across human tissues

- Authors: Junru Jin, Ding Wang, Jianbo Qiao, Wenjia Gao, Yuhang Liu, Siqi Chen, Quan Zou, Shu Wu, Ran Su, Leyi Wei
- Source: openalex
- Venue type: journal
- Journal: Nature Communications
- Publication status: published
- Publication date: 2026-08-17
- DOI: https://doi.org/10.1038/s41467-026-76744-5
- Categories: Epigenetics and DNA Methylation, Genomics and Chromatin Dynamics, Machine Learning in Bioinformatics
- Relevance: 2.8451017382834776
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://doi.org/10.1038/s41467-026-76744-5
- PDF: https://www.nature.com/articles/s41467-026-76744-5_reference.pdf
- Local PDF: pdf/2026-08-20_28_Decoding the sequence determinants of locus-specific DNA methylation across human tissues.pdf

DNA methylation is a fundamental epigenetic modification that plays crucial roles in transcriptional regulation, cellular differentiation, and genome stability. However, how locus-specific DNA methylation is determined by intrinsic DNA sequence remains poorly understood. Here, we introduce Melody, a deep learning framework that predicts DNA methylation from 10-kb genomic sequences, enabling the integration of both local and long-range sequence signals. Across 39 human tissues, Melody accurately predicts methylation profiles and consistently outperforms existing state-of-the-art methods in whole-chromosome, hypomethylated-region, and cell-type-specific benchmarks. Melody also generalizes to methylation quantitative trait locus (meQTL) effect prediction and identifies regulatory sequence motifs associated with methylation variability. To extend prediction beyond profiled tissues, we further develop Melody-G, which incorporates single-cell RNA-seq foundation model embeddings to infer methylation states in previously unseen cell types from transcriptomic data. Together, Melody provides a unified framework for linking genomic sequence and cellular state to DNA methylation and offers new insights into the regulatory logic governing the human methylome. Here, the authors use genomic sequence to predict locus-specific DNA methylation across 39 human tissues with the deep learning model Melody. Their approach outperforms existing methods and extends to previously unseen cell types using transcriptomic data.

## 29. Highly Sensitive Spatial Host‐Microbiome Transcriptomics in FFPE Tissues via Iterative Hydrogel Expansion

- Authors: Shunji Zhang, Mengyuan Wang, Jiaye Chen, Yuyi Zhu, Bin Zhu, Ziye Xu, Yuan Liao, Yongcheng Wang
- Source: openalex
- Venue type: journal
- Journal: Advanced Science
- Publication status: published
- Publication date: 2026-08-17
- DOI: https://doi.org/10.1002/advs.77219
- Categories: Advanced biosensing and bioanalysis techniques, Single-cell and spatial transcriptomics, RNA Interference and Gene Delivery
- Relevance: 2.824968122644129
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://doi.org/10.1002/advs.77219
- PDF: Unavailable
- Local PDF: Not downloaded

Spatial transcriptomics (ST) of archival formalin-fixed paraffin-embedded (FFPE) tissues is fundamentally limited by a trade-off between spatial resolution and transcriptomic sensitivity due to severe molecular crowding and RNA degradation. Here, we present Ex-spRandom, a highly sensitive platform that overcomes this limitation by directly converting diverse, fragmented RNA biotypes into stably anchored cDNA through the integration of random-primed in situ cDNA synthesis chemistry with interpenetrating polymer network (IPN)-based tissue expansion chemistry. This physicochemical synergy physically decrowds the dense FFPE matrix, directly converting highly fragmented host and microbial RNAs into stably anchored cDNA. Consequently, Ex-spRandom improves spatial signal confinement while enabling the detection of nearly 10,000 median genes per 50-µm spatial bin. Leveraging this synergistic high resolution and sensitivity, the platform captures over 44,000 unique host genes, enabling the precise delineation of continuous neurodevelopmental trajectories in the complex embryonic eye. Furthermore, Ex-spRandom achieves simultaneous, spatial profiling of host epithelial architecture and microbial transcript signals in the colon, detecting over 150,000 unique microbial genes. Ultimately, this scalable platform establishes a framework for sensitive, cross-kingdom spatial profiling in archival FFPE tissues.

## 30. J-Miner: Recovering Executable Decision Knowledge from Language-Model Classifiers

- Authors: Yunfan Gao, Xinyi Huang, Tao Sheng, Haorui Song, Yun Xiong, Haofen Wang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-17
- DOI: Unavailable
- Categories: cs.LG, cs.CL
- Relevance: 2.8228957019034135
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.17063v1
- PDF: https://arxiv.org/pdf/2608.17063v1
- Local PDF: pdf/2026-08-20_30_J-Miner_ Recovering Executable Decision Knowledge from Language-Model Classifiers.pdf

Large language models can be fine-tuned into specialized classifiers that perform well across diverse text tasks and make complex judgments, but they typically expose only final labels, leaving the decision knowledge acquired through fine-tuning implicit within the model. We study how to mine this internal decision knowledge from a fine-tuned classifier and encode it in an executable representation that can be inspected, validated, and reused beyond the source classifier. We introduce J-Miner, which mines text-level named concepts by aggregating vocabulary-aligned internal signals across layers and token positions, and uses the classifier's own predictions to learn executable decision rules over them. This process distills local internal readouts into an explicit classifier-level knowledge representation. Across multiple classification tasks, J-Miner rules reproduce up to 98.3\% of source-classifier decisions and achieve 6.0--29.5 percentage points higher behavioral fidelity than equally compact rules learned from input words. Further analysis shows that the named concepts reflect internal semantic evidence associated with task decisions, while the learned rules consolidate these distributed signals into inspectable decision structures. The resulting decision knowledge also transfers to lightweight standalone students: using about 1/24 as many parameters as the source classifiers, they reconstruct and execute the representation from raw text while retaining 99.8\% of the source classifiers' mean task accuracy. These findings show that task-specific decision knowledge can be faithfully represented in an explicit, executable form and reused beyond the classifier in which it was learned.

## 31. BoYueGRN: Zero-shot causal discovery of directed gene regulatory networks from single-cell transcriptomes via amortized inference over synthetic structural causal models

- Authors: Wu, J., Shen, Y.-Q.
- Source: biorxiv
- Venue type: preprint
- Journal: biorxiv
- Publication status: preprint
- Publication date: 2026-08-20
- DOI: 10.64898/2026.08.15.745056
- Categories: bioinformatics
- Relevance: 3.723046542628265
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://www.biorxiv.org/content/10.64898/2026.08.15.745056v1.full.pdf
- PDF: https://www.biorxiv.org/content/10.64898/2026.08.15.745056v1.full.pdf
- Local PDF: Not downloaded

Gene regulatory network (GRN) inference from single-cell RNA-seq conventionally relies on per-dataset optimization. Existing tools must be refit for every new dataset, and the majority fail to infer causal regulatory directions. Here we present BoYueGRN, an amortized causal discovery framework trained exclusively on 10,000 synthetic structural causal models. For any unseen dataset, a single forward pass returns edge probabilities and regulatory directions, while TF-centric sliding windows with asymmetric fusion extend this fixed-size model to full-transcriptome coverage. BoYueGRN demonstrates strong zero-shot performance across BEELINE benchmarks. On two independent genome-wide CRISPRi Perturb-seq screens, directional accuracy on retained edges reaches 0.86 and 0.95. Reconstructed cell-type- and stage-specific GRN dynamics across five diseases spanning more than 270,000 cells yield experimentally testable biological hypotheses. BoYueGRN reframes directed GRN inference as a train-once, reuse-across-datasets paradigm. By decoupling network reconstruction from per-dataset optimization, this paradigm opens the door to systematic, atlas-scale mapping of regulatory dynamics across human diseases.

## 32. Relational Graph Convolutional Networks for Glioblastoma Biomarker Discovery via ceRNA and Copy Number Variation Analysis

- Authors: Khandelwal, S., Jarvis, N., Zhan, J.
- Source: biorxiv
- Venue type: preprint
- Journal: biorxiv
- Publication status: preprint
- Publication date: 2026-08-20
- DOI: 10.64898/2026.08.16.744525
- Categories: bioinformatics
- Relevance: 3.4219921590831124
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://www.biorxiv.org/content/10.64898/2026.08.16.744525v1.full.pdf
- PDF: https://www.biorxiv.org/content/10.64898/2026.08.16.744525v1.full.pdf
- Local PDF: Not downloaded

Glioblastoma (GBM) is a highly aggressive brain tumor with an extremely poor 5-year survival rate of 6.9%, largely attributable to the lack of reliable biomarkers. While competing endogenous RNA (ceRNA) and copy number variation (CNV) analyses offer unique biomarker identification potential, current approaches neglect the integration of multiple regulatory mechanisms for biomarker detection. To address this limitation, we applied relational graph convolutional networks (RGCNs) to ceRNA and CNV knowledge graphs through a novel late fusion ensemble architecture. The proposed architecture outperformed baseline models and identified five novel biomarkers, including hsa-miR-196a and hsa-miR-224. Kaplan-Meier survival analysis and Cox regression indicated that the identified genes hold significant prognostic and diagnostic power. The early stratification of the Kaplan-Meier curves indicates the potential these genes hold for patient survival prediction. The results illustrate that a late fusion RGCN ensemble effectively captures complex gene interactions, overcoming limitations of existing models and providing a framework for biomarker discovery. The novel biomarkers serve as prospective targets for future GBM therapeutic development and candidates for non-invasive diagnostic assays.

## 33. Self-Evolving Agents as Dynamic Graph Transformation: A Survey and New Perspective

- Authors: Yuanyuan Xu, Wenjie Zhang, Yin Chen, Xuemin Lin, Ying Zhang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-06-10
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 3.3001890772728135
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.18104v1
- PDF: https://arxiv.org/pdf/2608.18104v1
- Local PDF: pdf/2026-08-20_33_Self-Evolving Agents as Dynamic Graph Transformation_ A Survey and New Perspective.pdf

Large language model (LLM)-based agents are increasingly becoming self-evolving systems that persist across interactions, maintain memories, use tools, acquire skills, refine workflows, and coordinate with other agents. These capabilities make agent states structural and dynamic: entities, relations, attributes, dependencies, and execution structures change with new evidence, feedback, and environmental conditions. Existing graph-agent surveys typically treat graphs as support structures for agent functions rather than as evolving substrates, while self-evolving-agent surveys focus on agent-level mechanisms and rarely discuss graph topology evolution. Thus, the coupling between evolving agent state and dynamic graph topology remains underexplored. This survey connects these two research lines by framing \textit{agent evolution as dynamic graph transformation}. We model agent state as a dynamic graph, where memories, tools, skills, workflows, and inter-agent relations are represented as typed nodes, edges, and subgraphs updated through schema-constrained rewrites. Based on this formulation, we organize existing dynamic-graph-based methods for self-evolving agents into four taxonomies: node/feature evolution, edge/topology evolution, subgraph activation, and cross-component co-evolution. Building on this taxonomy, we propose dynamic graph learning as reusable infrastructure for self-evolving agents and map nine dynamic-graph-learning subfields to agent-evolution capabilities, discussing their adaptations and possible failure modes. Finally, we discuss five types of graph-aware evaluation and governance protocols from a dynamic-graph perspective, which complement end-task evaluation. The goal is to provide a compact structural lens for designing and governing self-evolving agents.

## 34. DART-SD: Diamond-topology Aware Retrieval and Tuning for Self-Distillation of Multi-Turn Tool-Calling Agents

- Authors: Hangrui Xu, Jiarui Wang, Yang Yang, Chuanbo Zhu, Fangda Chen, Ziqi Wu, Jingming Cai, Yan Song
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-19
- DOI: Unavailable
- Categories: cs.CL, cs.AI, cs.LG, cs.MA
- Relevance: 3.1991206597122246
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.18524v1
- PDF: https://arxiv.org/pdf/2608.18524v1
- Local PDF: pdf/2026-08-20_34_DART-SD_ Diamond-topology Aware Retrieval and Tuning for Self-Distillation of Multi-Turn Tool-Calling Agents.pdf

Equipping Large Language Models (LLMs) with multi-turn tool-calling capabilities is essential for building autonomous agents. However, progress is fundamentally limited by the reliance on full-length trajectory imitation. For tasks involving multiple order-independent sub-goals, the optimal solution space forms a vast combinatorial diamond lattice. Forcing this rich topology into monolithic trajectories causes a severe topological collapse, indiscriminately penalizing valid alternative explorations and severely degrading policy diversity. To address this, we propose DART-SD (Diamond-topology Aware Retrieval and Tuning for Self-Distillation), a novel framework that shifts the paradigm from global forcing to topology-guided localized correction. DART-SD first models the execution process as a converging Interaction-State Transition Graph (ISTG), faithfully capturing the inherent diamond topology of successful and failed exploratory paths. During autonomous rollouts, the framework identifies the Critical Topological Breakpoint (CTB) and retrieves success-supported recovery references. Finally, we introduce a progressive self-distillation paradigm through CTB-guided localized supervision, ensuring that the training loss is calculated exclusively on the generated recovery steps while strictly protecting the valid reasoning prefix from destructive gradient updates. Experiments on complex multi-turn tool-calling benchmarks demonstrate that DART-SD significantly outperforms traditional full-trajectory baselines.

## 35. Monroe: A Molecular Foundation Model for In-Context Probabilistic Inference

- Authors: Blazej Banaszewski, Andrew W. Fitzgibbon
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-19
- DOI: Unavailable
- Categories: cs.LG, q-bio.BM, q-bio.QM
- Relevance: 3.159150766499499
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.18982v1
- PDF: https://arxiv.org/pdf/2608.18982v1
- Local PDF: pdf/2026-08-20_35_Monroe_ A Molecular Foundation Model for In-Context Probabilistic Inference.pdf

Bioassay activity prediction is often data-limited because drug-discovery datasets rely on time-consuming and expensive wet-lab experiments for data generation and evaluation. This challenge has inspired recent research into molecular foundation models (MFMs), which aim to encode general-purpose chemical knowledge into molecular representations that generalize well in data-constrained scenarios. This paper presents Monroe, a new MFM with several innovations over the existing state of the art: increased scale allowing pre-training on over 81 million molecules from the PM6 quantum chemistry dataset; improved graph representation of stereochemistry; improved training losses including conformer denoising and embedding decorrelation; improved multi-task learning; and the use of a prior-data-fitted model (TabPFN) for downstream in-context prediction. Our evaluations use a principled pairwise comparison framework that measures statistically significant performance differences. Across established Polaris benchmarks, Monroe matches or exceeds existing MFMs, while on activity cliff benchmarks, designed to assess utility for molecular discovery, it achieves significant improvements over prior methods. Finally, ablation and transfer experiments show that PFN-based downstream predictors also substantially improve two leading existing models, MiniMol and CheMeleon, yielding new state-of-the-art variants we call MiniMol_PFN and CheMeleon_PFN, suggesting that our downstream adaptation strategy generalizes beyond Monroe. Source code is at github.com/blazejba/monroe.

## 36. Bridge Graphical Models: Coupling, Projection, and Current-Preserving Dynamics for Generative Modeling

- Authors: Tiantian Zhang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-06-16
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.0100618032523565
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.19144v1
- PDF: https://arxiv.org/pdf/2608.19144v1
- Local PDF: pdf/2026-08-20_36_Bridge Graphical Models_ Coupling, Projection, and Current-Preserving Dynamics for Generative Modeling.pdf

Continuous-time generative models are often built from endpoint-conditioned bridges, but generation requires a different object: a non-anticipative Markov decoder that only observes the current state and time. We identify this bridge-to-decoder compression as a structural bottleneck shared by diffusion models, flow matching, rectified flow, Schrödinger bridges, and field-based generative models. We introduce the \emph{Markovization gap}, the time-integrated conditional variance of the bridge velocity given the Markov state. It is the MMSE of predicting endpoint-conditioned motion from the information available to a sampler, and it measures an irreducible loss incurred before any neural network is trained. To make this bottleneck comparable across model families, we define \emph{Bridge Graphical Models} (BGMs), which separate endpoint coupling, bridge law, Markovian projection, and current-preserving dynamics representation as independent design choices. The same formalism also represents Poisson and electrostatic models as field-line bridge kernels with a corresponding field-line Markovization gap. Across synthetic, latent, and pixel-space pilots on CIFAR-10 and Fashion-MNIST, a feature-space proxy gap estimated in minutes before training ranks design choices in the same direction as downstream training loss and FID under fixed architecture, bridge, sampler, and compute. These results support the Markovization gap as a pre-training diagnostic for bridge and coupling design.

## 37. MedUAG: Unified Understanding and Generation for Medical Multimodal Models

- Authors: Zijie Meng, Yuncheng Zhang, Hualiang Wang, Yitian Tang, Xiaotang Gai, Chen Shen, Songtao Jiang, Shaosheng Cao, Jian Wu, Xian Wu, Zuozhu Liu
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-19
- DOI: Unavailable
- Categories: cs.CL, cs.AI
- Relevance: 3.009476379304477
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.18937v1
- PDF: https://arxiv.org/pdf/2608.18937v1
- Local PDF: pdf/2026-08-20_37_MedUAG_ Unified Understanding and Generation for Medical Multimodal Models.pdf

Recent Multimodal Large Language Models (MLLMs) are rapidly evolving into unified understanding and generation (UAG) frameworks. However, extending these unified paradigms to the medical domain is hindered by: the absence of comprehensive training and evaluation benchmarks, and the lack of broadly validated unified medical model. To address these gaps, we present a comprehensive foundation for medical UAG. First, we construct MedUAGCorpus, the largest unified medical understanding and generation dataset to date, comprising over 6 million instances across 14 imaging modalities. Second, we introduce MedUAGBench, a systematic benchmark that expands medical generation evaluation to 12 diverse tasks under standardized protocols. Finally, leveraging these resources, we develop MedUAG, an end-to-end trained unified medical model. Extensive experiments demonstrate that MedUAG achieves strong performance across a wide array of understanding and generation tasks, establishing a competitive baseline and paving the way for next-generation medical multimodal systems.

## 38. Prior-Conditioned Gaussian Discriminants for Generalizable AI-generated Image Detection

- Authors: Shashank Kotyan, Makoto Shing, Yuki Imajuku, Rujikorn Charakorn, Tarin Clanuwat
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-19
- DOI: Unavailable
- Categories: cs.CV, cs.AI
- Relevance: 2.9749630156517255
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.18523v1
- PDF: https://arxiv.org/pdf/2608.18523v1
- Local PDF: pdf/2026-08-20_38_Prior-Conditioned Gaussian Discriminants for Generalizable AI-generated Image Detection.pdf

Diffusion-based generators have made synthetic images ubiquitous, but detectors often fail under simultaneous shifts in generator, prompt/style, and source-domain. We study AI-generated image detection as a transfer system described by training prior, frozen encoder feature space, and decision rule, and ask when classifier head training adds value beyond what is already separable in modern features. As a controlled diagnostic, we fit a prior-conditioned Gaussian discriminant ladder: closed-form heads built from first- and second-order feature statistics under nested covariance assumptions. On Percept-Lens, a unified protocol over 39 public datasets (7.1 million images), the best rung is frequently competitive with, and sometimes exceeds, released AI-generated image detector heads when matched on both prior and encoder. We further quantify strong sensitivity to the training prior, data-efficiency of moment-based heads, and representation dependence of Gaussian shift metrics, motivating (prior, encoder, head)-level reporting and stronger analytical baselines for AIGI transfer.

## 39. GEAR: Generative Expansion and Real Anchoring for Two-Stage Distillation of Tabular Foundation Models

- Authors: Qi Qin, Jiajie Zhu, Dali Chen, Yuzhao Zhang, Jia-Xing Han, Yu Su, Peng Zhang, Ying Yan, Yifan Sun
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-19
- DOI: Unavailable
- Categories: cs.LG, stat.ME, stat.ML
- Relevance: 2.95089528155102
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.18849v1
- PDF: https://arxiv.org/pdf/2608.18849v1
- Local PDF: pdf/2026-08-20_39_GEAR_ Generative Expansion and Real Anchoring for Two-Stage Distillation of Tabular Foundation Models.pdf

Tabular foundation models (TFMs) achieve strong performance through in-context learning, but context-dependent inference imposes substantial latency and memory costs, hindering large-scale deployment. We propose GEAR (\emph{Generative Expansion and Real Anchoring}), a modular two-stage framework that distills TFMs into lightweight MLP or tree-based predictors that can be deployed on commodity CPUs. Stage 1 uses synthetic covariates solely as teacher-query locations and trains the student on soft TFM targets, expanding coverage beyond observed rows. Stage 2 re-anchors the student to the target distribution using real labels and out-of-fold teacher predictions, whitch avoids self-labeling leakage. We further derive a risk certificate characterizing the trade-off between generated-query volume and generator fidelity. Experiments on TALENT and TabArena demonstrate the broad applicability of GEAR. Two-stage MLPs outperform supervised MLPs by 1.81--2.00 AUC points on binary tasks and 1.19--1.35 points on multiclass tasks, with additional gains over real-data-only distillation of 1.76--2.19 and 2.09--2.40 points, respectively. On binary tasks, the gains also transfer to LightGBM and XGBoost, and all three student families outperform CatBoost, the strongest non-TFM baseline, in mean AUC. Ablations show gains beyond longer training or alternative warm starts, greater stability from staged than mixed optimization, and generator-dependent diminishing returns as query volume increases. Finally, GEAR reduces median inference time by 57--2866 times and peak prediction memory by 1.9--3.3 times, while retaining higher AUC than matched supervised baselines.

## 40. Simple, Safe, and Overlooked: Reclaiming Sustainable Domain Generalization with Statistical Color Matching

- Authors: Sebastian Doerrich, Francesco Di Salvo, Shyam Nandan Rai, Marco Lents, Christian Ledig
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-19
- DOI: Unavailable
- Categories: cs.CV, cs.LG, eess.IV
- Relevance: 2.9508002390030272
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.18915v1
- PDF: https://arxiv.org/pdf/2608.18915v1
- Local PDF: pdf/2026-08-20_40_Simple, Safe, and Overlooked_ Reclaiming Sustainable Domain Generalization with Statistical Color Matching.pdf

Hardware shifts, color variations, and changing patient characteristics between development and deployment routinely break trained medical image classifiers. Existing remedies fall short: standard color jittering provides insufficient diversity, while deep generative style transfer algorithms hallucinate features, destroy clinically relevant structures, and waste massive compute resources. To address this, we revisit classical statistical color matching and repurpose it as Colorist, a highly efficient data augmentation strategy that applies global mean-standard deviation matching directly in the RGB color space. We demonstrate that this training-free, fully interpretable approach safely generates structurally intact domain variations, outperforming deep generative models in structural fidelity and color alignment. Across out-of-distribution histopathology, peripheral blood, dermatology, and retinal datasets, it improves balanced accuracy by up to +9% over state-of-the-art domain generalization regularizers and by +13% over an unaugmented baseline. Moreover, by avoiding neural networks in the augmentation loop, Colorist preserves anatomical structure, minimizes carbon footprint, and integrates seamlessly into standard dataloaders. Together, these findings establish statistical matching as a safe, interpretable, yet overlooked alternative to deep architectures for clinical robustness. Source code is available at https://github.com/sdoerrich97/colorist.

## 41. Training Chemical Plausibility-Aware Large Language Models for Single-Step Retrosynthesis

- Authors: Bogdan Zagribelnyy, Ivan Ilin, Nikita Bondarev, Maksim Kuznetsov, Mathieu Reymond, Vladimir Aladinskiy, Alex Aliper, Alex Zhavoronkov
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-19
- DOI: Unavailable
- Categories: cs.LG, cs.AI, cs.CE, cs.CL
- Relevance: 2.9352904126698
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.18940v1
- PDF: https://arxiv.org/pdf/2608.18940v1
- Local PDF: pdf/2026-08-20_41_Training Chemical Plausibility-Aware Large Language Models for Single-Step Retrosynthesis.pdf

Single-step retrosynthesis is a central component of computer-aided synthesis planning, yet its intrinsically one-to-many nature is poorly captured by single-answer evaluation and benchmarking protocols. To address this, we introduce Top-K prompting as a robust training and inference paradigm to better capture diverse, plausible reaction predictions. We compile CREED-CCV-2+USPTO-XL, an ultra-large-scale dataset of ~45.6 million verified reactions to train the C3LM (Chemistry Constraint-Consistent Language Model). By integrating fine-tuning with ChemCensor-based and novelty-oriented rewards, our model achieves state-of-the-art performance on the OOD URSA-expert-2026 benchmark. Further analysis of reaction uniqueness shows that LLMs and conventional models explore complementary reaction spaces, motivating ensemble-based retrosynthesis systems. Overall, our results establish Top-K, plausibility-aware training as a practical new direction for robust future LLM-based synthesis planning.

## 42. Self-prompting and cross-model consensus enable reproducible data extraction from scientific literature with large language models

- Authors: Valentin Romanov, Monique Bax, Steven Niederer
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-19
- DOI: Unavailable
- Categories: cs.AI, cs.DB
- Relevance: 2.927466004019731
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.19025v1
- PDF: https://arxiv.org/pdf/2608.19025v1
- Local PDF: pdf/2026-08-20_42_Self-prompting and cross-model consensus enable reproducible data extraction from scientific literature with large langu.pdf

Accurately extracting nuanced, contextualized data from research articles is laborious and time intensive. Here, we investigate the performance of frontier, browser-based large language models (LLMs) to extract highly contextualized information. We demonstrate four escalating workflows, 1) given an expert curated prompt and research articles, most frontier LLMs perform well at data extraction, however can struggle with interpreting scientific context and nuance, 2) given simple instructions, LLMs can author their own prompts which were almost as eNective as expert-written prompts, 3) autonomous discovery of research literature was diNicult, agents either missed or hallucinated references, and 4) LLMs can create new datasets from published guidelines that closely match human-expert judges, but still require a human-in-the-loop. Together, these findings define an auditable division of labour in which experts specify the evidence standard, models cross-check repeated extractions and researchers resolve disputed cases, providing a practical route to scaling scientific data curation without relinquishing expert oversight.

## 43. Tensor Field Models

- Authors: Alexander Strunk, Roland Assam
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-19
- DOI: Unavailable
- Categories: cs.LG, math.DG
- Relevance: 2.815960582224611
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.18808v1
- PDF: https://arxiv.org/pdf/2608.18808v1
- Local PDF: pdf/2026-08-20_43_Tensor Field Models.pdf

This paper introduces Tensor Field Models (TFMs), realization-level Mathematical Structures in which a learned Operator maps a product of admissible component-section families to a prescribed family of time-dependent tangent sections on a Generative State Manifold. Analytic and dynamical restrictions are encoded through the choice of admissible families rather than imposed by the root definition. Constructed, component-separable, and Tensor Bundle TFMs provide structured refinements of this common object. In the conditional realizations considered here, a structured condition $c=(c_1,\ldots,c_n)$ is mapped componentwise to a reusable collection $\mathbf H_c=(H_{c_1}^{(1)},\ldots,H_{c_n}^{(n)})$. In the architectures evaluated here, the component representations remain distinct and are combined only by the Field Operator to produce the generated Vector Field. All learned models are trained using Flow Matching. Experiments show that TFMs can improve performance and that amortized sampling enabled by reusable condition representations can accelerate generation.

## 44. Learning-State-Aware Dynamic Generative Data Augmentation on Small-Scale Datasets

- Authors: Ting Xiang, Chenxi Deng, Jinhui Zhao, Bingting Jiang, Ke Zhang, Changjian Chen, Zhuo Tang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-19
- DOI: Unavailable
- Categories: cs.CV, cs.AI
- Relevance: 2.804874384084241
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.18907v1
- PDF: https://arxiv.org/pdf/2608.18907v1
- Local PDF: pdf/2026-08-20_44_Learning-State-Aware Dynamic Generative Data Augmentation on Small-Scale Datasets.pdf

Small-scale image classification is often limited by the scarcity of training data. Generative data augmentation (GDA) based on pretrained generative models has emerged as an effective solution. However, existing methods rely on task-agnostic augmentation strategies that overlook downstream model needs. Although recent dynamic GDA methods incorporate model feedback to guide augmentation, they still struggle to reliably determine sample-specific augmentation strengths and adapt augmentation strategies to different image regions while balancing image diversity and class semantics.
  To address these issues, we propose learning-state-aware dynamic generative data augmentation (LSADA). Specifically, LSADA constructs a learning state for each sample based on its current loss and loss-decrease rate, which is then mapped to a sample-specific augmentation strength. Furthermore, LSADA introduces a decoupled data augmentation and diffusion fusion strategy that applies strength-controlled transformations to class-relevant regions and generates diverse class-irrelevant regions, progressively fusing them to improve image diversity while preserving class semantics. Experiments on nine public datasets show that LSADA outperforms the existing SOTA dynamic GDA method by an average of 4.5% on six natural image datasets and 2.5% on three medical image datasets.

## 45. Outputs of generative diffusion models are often unattributable

- Authors: Zheng Dai, David K. Gifford
- Source: openalex
- Venue type: journal
- Journal: Nature Communications
- Publication status: published
- Publication date: 2026-08-18
- DOI: https://doi.org/10.1038/s41467-026-75667-5
- Categories: Cell Image Analysis Techniques, Generative Adversarial Networks and Image Synthesis, Music Technology and Sound Studies
- Relevance: 2.782192281891387
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://doi.org/10.1038/s41467-026-75667-5
- PDF: Unavailable
- Local PDF: Not downloaded

Abstract Modern generative diffusion models work by replicating the statistical patterns of large training datasets. Developing a method to attribute generated outputs to influential training data would greatly advance our understanding of and ability to regulate these models, leading to much work towards this goal. But is this possible? Here, we show that models trained with enough data often generate samples that are unattributable. We establish this through a large-scale analysis of what-if scenarios, revealing that we can often omit any sample or creator from the training data without affecting a generated sample. Our study focuses on diffusion models, which has become the dominant model for generating audiovisual media, and is also prevalent in many scientific applications including protein structure modeling and therapeutic discovery. Central to our analysis is a model ablation methodology that allows efficient removal of training examples from a trained model without the need to retrain.

## 46. CoopQ: Cooperative Game Inspired Layerwise Mixed Precision Quantization for LLMs

- Authors: Junchen Zhao, Ali Derakhshan, Jayden Hyman, Junhao Dong, Sangeetha Abdu Jyothi, Ian Harris
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.771270994951566
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.373/
- PDF: https://aclanthology.org/2026.findings-acl.373.pdf
- Local PDF: pdf/2026-08-20_46_CoopQ_ Cooperative Game Inspired Layerwise Mixed Precision Quantization for LLMs.pdf

Large Language Models (LLMs) promise impressive capabilities, yet their multi-billion parameter scale makes on-device or low-resource deployment prohibitive. Mixed precision quantization offers a compelling solution, but existing methods struggle when the average precision drops below four bits, as they rely on isolated, layer-specific metrics that overlook critical inter-layer interactions affecting overall performance. To address these limitations, we first frame the mixed-precision quantization problem as a cooperative game among layers and introduce Shapley-based Progressive Quantization Estimation (SPQE) to efficiently obtain accurate Shapley estimates of layer sensitivities and inter-layer interactions. Leveraging the SPQE estimates, we propose Cooperative Game Inspired Mixed-Precision Quantization (CoopQ) which translates these Shapley estimates into a binary quadratic optimization formulation, assigning either 2 or 4-bit precision to layers under strict memory constraints. Comprehensive experiments conducted on Llama-3, Gemma-2, and Qwen models across three independent PTQ backends (Quanto, HQQ, GPTQ) demonstrate CoopQ’s scalability and consistently superior performance compared to methods relying solely on isolated metrics. Across average precisions spanning 4 bit down to 2 bit, CoopQ cuts Perplexity by 20 – 80 % relative to the best baseline, with the margin growing as the bit-width tightens.

## 47. GeometryZero: Advancing Geometry Solving via Group Contrastive Policy Optimization

- Authors: Yikun Wang, Yibin Wang, Dianyi Wang, Zimian Peng, Qipeng Guo, Dacheng Tao, Jiaqi Wang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.768804889359483
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1392/
- PDF: https://aclanthology.org/2026.findings-acl.1392.pdf
- Local PDF: pdf/2026-08-20_47_GeometryZero_ Advancing Geometry Solving via Group Contrastive Policy Optimization.pdf

Recent progress in large language models (LLMs) has boosted mathematical reasoning, yet geometry remains challenging where auxiliary construction is often essential. Prior methods either underperform or depend on very large models (e.g., GPT-4o), making them costly. We argue that reinforcement learning with verifiable rewards (e.g., GRPO) can train smaller models to couple auxiliary construction with solid geometric reasoning. However, naively applying GRPO yields unconditional rewards, encouraging indiscriminate and sometimes harmful constructions. We propose Group Contrastive Policy Optimization (GCPO), an RL framework with two components: (1) Group Contrastive Masking, which assigns positive/negative construction rewards based on contextual utility, and (2) a Length Reward that encourages longer reasoning chains. On top of GCPO, we build GeometryZero, an affordable family of geometry reasoning models that selectively use auxiliary construction. Experiments on Geometry3K and MathVista show GeometryZero consistently outperforms RL baselines (e.g., GRPO, ToRL).

## 48. Is Chain-of-Thought Reasoning of LLMs a Mirage? A Data Distribution Lens

- Authors: Chengshuai Zhao, Zhen Tan, Pingchuan Ma, Dawei Li, Bohan Jiang, Yancheng Wang, Yingzhen Yang, Huan Liu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.7686855820796867
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.749/
- PDF: https://aclanthology.org/2026.findings-acl.749.pdf
- Local PDF: pdf/2026-08-20_48_Is Chain-of-Thought Reasoning of LLMs a Mirage_ A Data Distribution Lens.pdf

Chain-of-Thought (CoT) prompting has been shown to be effective in eliciting structured reasoning (i.e., CoT reasoning) from large language models (LLMs). Regardless of its popularity, recent studies expose its failures in some reasoning tasks, raising fundamental questions about the nature of CoT reasoning. In this work, we propose a data distribution lens to understand when and why CoT reasoning succeeds or fails. We hypothesize that CoT reasoning reflects a structured inductive bias learned from in-distribution data, enabling models to conditionally generate reasoning trajectories that approximate those observed during training. As such, the effectiveness of CoT reasoning is fundamentally governed by the nature and degree of distribution discrepancy between training data and test queries. Guided by this lens, we dissect CoT reasoning via three dimensions: task, length, and format. To test the hypothesis, we introduce DataAlchemy, an abstract and fully controllable environment that trains LLMs from scratch and systematically probes them under various distribution conditions. Through rigorous controlled experiments, we reveal that CoT reasoning is a brittle mirage when it is pushed beyond training distributions, emphasizing the ongoing challenge of achieving genuine and generalizable reasoning.

## 49. LycheeCluster: Efficient Long-Context Inference with Structure-Aware Chunking and Hierarchical KV Indexing

- Authors: Dongfang Li, Zixuan Liu, Gang Lin, Baotian Hu, Min Zhang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.767879881623049
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.376/
- PDF: https://aclanthology.org/2026.findings-acl.376.pdf
- Local PDF: pdf/2026-08-20_49_LycheeCluster_ Efficient Long-Context Inference with Structure-Aware Chunking and Hierarchical KV Indexing.pdf

The quadratic complexity of the attention mechanism and the substantial memory footprint of the Key-Value (KV) cache present severe computational and memory challenges for Large Language Models (LLMs) processing long contexts. Existing retrieval-based methods often compromise semantic integrity through fixed-size chunking and suffer from inefficient linear scanning. In this paper, we propose LycheeCluster, a novel method for efficient KV cache management. LycheeCluster preserves local semantic coherence via boundary-aware chunking and constructs a recursive hierarchical index rooted in the triangle inequality. This design transforms cache retrieval from a linear scan into a theoretically bounded, logarithmic-time pruning process, while a lazy update strategy supports efficient streaming generation. Experiments demonstrate that LycheeCluster achieves up to a 3.6 × end-to-end inference speedup with negligible degradation in model performance, outperforming state-of-the-art KV cache management methods (e.g., Quest, ClusterKV).

## 50. Chain-of-Thought as a Lens: Evaluating Structured Reasoning Alignment between Human Preferences and Large Language Models

- Authors: Boxuan Wang, Zhuoyun Li, Xinmiao Huang, Xiaowei Huang, Yi Dong
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.7678484894633555
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1834/
- PDF: https://aclanthology.org/2026.acl-long.1834.pdf
- Local PDF: pdf/2026-08-20_50_Chain-of-Thought as a Lens_ Evaluating Structured Reasoning Alignment between Human Preferences and Large Language Model.pdf

This paper primarily demonstrates a method to quantitatively assess the alignment between multi-step, structured reasoning in large language models and human preferences. We introduce the Alignment Score, a semantic-level metric that compares a model-produced chain of thought traces with a human-preferred reference by constructing semantic-entropy-based matrices over intermediate steps and measuring their divergence. Our analysis shows that Alignment Score tracks task accuracy across models and hop depths, and peaks at 2-hop reasoning. Empirical results further indicate that misalignment at greater reasoning depths is driven mainly by alignment errors such as thematic shift and redundant reasoning. Viewing chain sampling as drawing from a distribution over reasoning paths, we empirically demonstrate a strong and consistent correlation between Alignment Score and accuracy, readability, and coherence, supporting its use as a diagnostic signal. The code is available.

## 51. Multi-Constraint State Tracking with Negation: A Diagnostic Benchmark for LLM World Modeling

- Authors: Ayan Sar, Pranav Singh Puri, Sumit Aich, Anurag Kaushish, Tanupriya Choudhury, Ajith Abraham
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.767833676076194
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-srw.119/
- PDF: https://aclanthology.org/2026.acl-srw.119.pdf
- Local PDF: pdf/2026-08-20_51_Multi-Constraint State Tracking with Negation_ A Diagnostic Benchmark for LLM World Modeling.pdf

Large Language Models (LLMs) achieve strong performance on a wide range of reasoning benchmarks, yet it remains unclear whether they can reliably maintain and update internal representations of an evolving world described in natural language. In particular, existing evaluations inadequately probe state tracking under multiple interacting constraints and largely overlook the role of negated actions, despite their ubiquity in real-world language. We address this gap by introducing MCST, a diagnostic benchmark for multi-constraint state tracking that evaluates an LLM’s ability to maintain consistent world models across sequences of actions involving inventory changes, spatial movement, temporal ordering, and systematic negation. MCST comprises 100,847 questions spanning 12 real-world domains, with five calibrated difficulty levels, nine question types, and controlled integration of negated actions. The benchmark further incorporates culturally diverse entity names to enable analysis of cross-cultural robustness. We evaluate 14 SOTA LLMs across multiple model families using a unified evaluation protocol. Our results reveal substantial limitations: even the strongest models exhibit sharp performance degradation as difficulty increases, with accuracy dropping below 35% at the highest level. Most notably, we identify negation as a dominant failure mode, causing accuracy reductions of 23-32% across models. We release MCST and the full evaluation framework to support future research on state tracking and reasoning in language models and is available at GitHub.

## 52. ETR: Entropy Trend Reward for Efficient Chain-of-Thought Reasoning

- Authors: Xuan Xiong, Huan Liu, Li Gu, Zhixiang Chi, Yue Qiu, Yuanhao YU, Yang Wang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.7677262840114936
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.799/
- PDF: https://aclanthology.org/2026.acl-long.799.pdf
- Local PDF: pdf/2026-08-20_52_ETR_ Entropy Trend Reward for Efficient Chain-of-Thought Reasoning.pdf

Chain-of-thought (CoT) reasoning improves large language model performance on complex tasks, but often produces excessively long and inefficient reasoning traces. Existing methods shorten CoTs using length penalties or global entropy reduction, implicitly assuming that low uncertainty is desirable throughout reasoning. We show instead that reasoning efficiency is governed by the trajectory of uncertainty. CoTs with dominant downward entropy trends are substantially shorter. Motivated by this insight, we propose E ntropy T rend R eward ( ETR ), a trajectory-aware objective that encourages progressive uncertainty reduction while allowing limited local exploration. We integrate ETR into Group Relative Policy Optimization (GRPO) and evaluate it across multiple reasoning models and challenging benchmarks. ETR consistently achieves a superior accuracy–efficiency trade-off, improving DeepSeek-R1-Distill-7B by +9.9% accuracy while reducing CoT length by 67% across four benchmarks.

## 53. Breaking the Evaluation Paradox: Evaluating High-Entropy Search with Computationally Irreducible Constraints

- Authors: Juntao Wu, Wei Wen, Xianting Huang, Shuai Pang, Ruizhi Qiao, Xing Sun, Ke Wang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.7675351992483392
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1406/
- PDF: https://aclanthology.org/2026.findings-acl.1406.pdf
- Local PDF: pdf/2026-08-20_53_Breaking the Evaluation Paradox_ Evaluating High-Entropy Search with Computationally Irreducible Constraints.pdf

Evaluating the exhaustive search capabilities of large language models (LLMs) is plagued by a fundamental paradox: verifying completeness requires complete ground truth, yet high-entropy enumeration tasks make such ground truth impossible for humans to create. This causes benchmarks to systematically penalize models for outperforming their human annotators. Despite rapid progress in web-search and deep research agents—which now issue hundreds of queries, traverse diverse sites, and synthesize long reports—evaluation still largely relies on partially annotated answer sets, LLM-based judges, or single-answer questions that avoid genuinely exhaustive search scenarios.We break this paradox by shifting the evaluation paradigm from simulating a messy reality to constructing computationally pure challenges. We introduce VERITAS (Verifiable Traversal Assessment for Search), a framework built on the principle of computationally irreducible constraints. By introducing novel, non-optimizable constraints, we create verifiable, sparse-answer search tasks that are computationally equivalent to exhaustive enumeration. These constraints are easy to verify but impossible for LLMs or search engines to optimize, forcing agents to genuinely traverse the entire search space. VERITAS can automatically generate a virtually infinite number of test cases with perfect ground truth and precise difficulty control, with marginal instance cost dominated by hash computations. This provides not only a robust benchmark for evaluating systematic exploration under uncertainty but also a scalable method for generating training data to improve these crucial, yet underdeveloped, capabilities.

## 54. CRISP: Persistent Concept Unlearning via Sparse Autoencoders

- Authors: Tomer Ashuach, Dana Arad, Aaron Mueller, Martin Tutek, Yonatan Belinkov
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.7665829603199175
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.82/
- PDF: https://aclanthology.org/2026.acl-long.82.pdf
- Local PDF: pdf/2026-08-20_54_CRISP_ Persistent Concept Unlearning via Sparse Autoencoders.pdf

As large language models (LLMs) are increasingly deployed in real-world applications, the need to selectively remove unwanted knowledge while preserving model utility has become paramount. Recent work has explored sparse autoencoders (SAEs) to perform precise interventions on monosemantic features. However, most SAE-based methods operate at inference time, which does not create persistent changes in the model’s parameters. Such interventions can be bypassed or reversed by malicious actors with parameter access. We introduce CRISP, a parameter-efficient method for persistent concept unlearning using SAEs. CRISP automatically identifies salient SAE features across multiple layers and suppresses their activations. We experiment with two LLMs and show that our method outperforms prior approaches on safety-critical unlearning tasks from the WMDP benchmark, successfully removing harmful knowledge while preserving general and in-domain capabilities. Feature-level analysis reveals that CRISP achieves semantically coherent separation between target and benign concepts, allowing precise suppression of the target features.

## 55. Training-Free Test-Time Contrastive Learning for Large Language Models

- Authors: Kaiwen Zheng, Kai Zhou, Jinwu Hu, Te Gu, Mingkai Peng, Fei Liu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.766287844722031
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1482/
- PDF: https://aclanthology.org/2026.findings-acl.1482.pdf
- Local PDF: pdf/2026-08-20_55_Training-Free Test-Time Contrastive Learning for Large Language Models.pdf

Large language models (LLMs) demonstrate strong reasoning capabilities, but their performance often degrades under distribution shift. Existing test-time adaptation (TTA) methods rely on gradient-based updates that require white-box access and need substantial overhead, while training-free alternatives are either static or depend on external guidance. In this paper, we propose Training-Free Test-Time Contrastive Learning ( TF-TTCL ), a training-free adaptation framework that enables a frozen LLM to improve online by distilling supervision from its own inference experiences. Specifically, TF-TTCL implements a dynamic “Explore-Reflect-Steer” loop through three core modules: 1) Semantic Query Augmentation first diversifies problem views via multi-agent role-playing to generate different reasoning trajectories; 2) Contrastive Experience Distillation then captures the semantic gap between superior and inferior trajectories, distilling them into explicit textual rules; and 3) Contextual Rule Retrieval finally activates these stored rules during inference to dynamically steer the frozen LLM toward robust reasoning patterns while avoiding observed errors. Extensive experiments on closed-ended reasoning tasks and open-ended evaluation tasks demonstrate that TF-TTCL consistently outperforms strong zero-shot baselines and representative TTA methods under online evaluation. Code is available at https://github.com/KevinSCUTer/TF-TTCL .

## 56. Collaborative Chain-of-Agents for Parametric-Retrieved Knowledge Synergy

- Authors: Yi Jiang, Sendong Zhao, Jianbo Li, Haochun Wang, Lizhe Zhang, Yan Liu, Bing Qin
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.7662374126084943
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.167/
- PDF: https://aclanthology.org/2026.acl-long.167.pdf
- Local PDF: pdf/2026-08-20_56_Collaborative Chain-of-Agents for Parametric-Retrieved Knowledge Synergy.pdf

Retrieval-Augmented Generation (RAG) enhances Large Language Models (LLMs), especially for knowledge-intensive tasks. Despite its advantages, current RAG methods often struggle to fully exploit knowledge during generation. In particular, the synergy between the model’s internal parametric knowledge and external retrieved knowledge remains limited. Retrieved contents may sometimes mislead generation, while certain generated content can guide the model toward more accurate outputs. In this work, we propose Collaborative Chain-of-Agents, a framework designed to enhance explicitly synergy over both parametric and retrieved knowledge. Specifically, we first introduce CoCoA-zero, a multi-agent RAG framework that first performs conditional knowledge induction and then reasons answers. Building on this, we develop CoCoA, a long-chain training strategy that synthesizes extended multi-agent reasoning trajectories from CoCoA-zero to fine-tune the LLM. This strategy enhances the model’s capability to explicitly integrate and jointly leverage parametric and retrieved knowledge. Experimental results demonstrate the superiority of CoCoA in open-domain QA and multi-hop QA.

## 57. AI Agents for the Science of Science: A Survey of Tasks, Architectures, Evaluations, and Challenges

- Authors: Yixuan Liu, Yicheng Zhang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.7657892957518353
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1804/
- PDF: https://aclanthology.org/2026.findings-acl.1804.pdf
- Local PDF: pdf/2026-08-20_57_AI Agents for the Science of Science_ A Survey of Tasks, Architectures, Evaluations, and Challenges.pdf

The Science of Science (SciSci) examines how scientific knowledge is generated, evaluated, and transformed by utilizing large-scale scholarly and bibliometric data. As these data grow in scale and complexity, analysis has increasingly relied on statistical, network-based, machine learning methods, and is now seeing growing involvement of AI agents. This emerging class of such agents, ranging from multi-agent simulations of scientific behavior to tool-augmented systems for empirical analysis, is beginning to reshape how SciSci research is conducted. In this survey, we propose a task-centered taxonomy, distinguishing agents as simulations , which model citation, collaboration, and community dynamics, from agents as tools , which assist empirical analysis and scientific workflows. We review agent architectures, learning mechanisms, evaluation, and SciSci benchmarks, and examine open challenges related to reliability, data quality, and bias. Our survey aims to clarify the landscape of AI agents in SciSci and to support the development of reliable and scientifically useful AI systems for studying science and scientific communities.

## 58. HiGMem: A Hierarchical and LLM-Guided Memory System for Long-Term Conversational Agents

- Authors: Shuqi Cao, Jingyi He, Fei Tan
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.7657693227564106
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1690/
- PDF: https://aclanthology.org/2026.findings-acl.1690.pdf
- Local PDF: pdf/2026-08-20_58_HiGMem_ A Hierarchical and LLM-Guided Memory System for Long-Term Conversational Agents.pdf

Long-term conversational large language model (LLM) agents require memory systems that can recover relevant evidence from historical interactions without overwhelming the answer stage with irrelevant context. However, existing memory systems, including hierarchical ones, still often rely solely on vector similarity for retrieval. It tends to produce bloated evidence sets: adding many superficially similar dialogue turns yields little additional recall, but lowers retrieval precision, increases answer-stage context cost, and makes retrieved memories harder to inspect and manage. To address this, we propose HiGMem (Hierarchical and LLM-Guided Memory System), a two-level event-turn memory system that allows LLMs to use event summaries as semantic anchors to predict which related turns are worth reading. This allows the model to inspect high-level event summaries first and then focus on a smaller set of potentially useful turns, providing a concise and reliable evidence set through reasoning, while avoiding the retrieval overhead that would be excessively high compared to vector retrieval.On the LoCoMo10 benchmark, HiGMem achieves the best F1 on four of five question categories and improves adversarial F1 from 0.54 to 0.78 over A-Mem, while retrieving an order of magnitude fewer turns. Code is publicly available at https://github.com/ZeroLoss-Lab/HiGMem .

## 59. MASS: Deep Research for Social Sciences with Memory-Augmented Social Simulation

- Authors: Yongrui Liu, Deyi Xiong
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.765667598674252
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.988/
- PDF: https://aclanthology.org/2026.findings-acl.988.pdf
- Local PDF: pdf/2026-08-20_59_MASS_ Deep Research for Social Sciences with Memory-Augmented Social Simulation.pdf

Deep Research agents powered by Large Language Models (LLMs) have exhibited extraordinary potential in automated paper writing tasks. However, existing systems rely heavily on literature retrieval and synthesis through internet and local knowledge bases, often resulting research lacking insight and creativity in social science. To address this issue, we propose "Memory-Augmented Social Simulation (MASS)”, an innovative paradigm that leverages highly realistic and research-oriented social simulations to the creativity and empirical founding of LLMs-generated research. Specifically, MASS integrates three core components—dynamic goal-path planning with multi-level social norm restraint to guide the simulation, a multi-disciplinary behavior dataset for agent memory cold-start, and a structured forgetting mechanism inspired by the Ebbinghaus curve. Together, these ensure simulation authenticity and provide a robust empirical foundation for generating innovative scholarly papers. Experimental results demonstrate the effectiveness of our method, showing a 6.81% improvement in generation overall quality over foundation LLMs and 17.19% gain in Insight over strong baselines. Dataset and codes will be released.

## 60. MemTR: Enhancing Tool-Calling Reliability via Uncertainty-Triggered FFN-Space Retracing

- Authors: Hongtao Duan, Lu Jiang, Minying Zhang, Xiaobing Zhu, Tianpeng Bu, Hao Jiang, Xinyu Wei, Lulu hu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.765603865668915
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.973/
- PDF: https://aclanthology.org/2026.findings-acl.973.pdf
- Local PDF: pdf/2026-08-20_60_MemTR_ Enhancing Tool-Calling Reliability via Uncertainty-Triggered FFN-Space Retracing.pdf

Tool calling requires Large Language Models (LLMs) to generate structured decisions including tool names and schema-constrained arguments, where small decoding mistakes can cause hard failures. Existing methods either rely on costly tool-use training data or only constrain syntax, leaving tool selection and argument value errors largely unsolved. We analyze tool calling failures through a Where–When lens: (Where) failures correlate with persistent uncertainty in late transformer layers, (When) uncertainty concentrates on content-bearing tokens (tool names and argument values) rather than schema tokens. Based on this, and motivated by evidence that transformer Feed Forward Networks (FFNs) act as key–value style memories that store and retrieve factual or associative mappings, we propose Memory Space Tool Retracing (MemTR), a weight-free decoding-time method that retrieves relevant tool evidence from the tool library and mixes it into the FFN-output at the uncertain layer, treating FFNs as key–value memories. Through extensive experiments on various model families (Qwen, Llama, and xLAM) and benchmarks (BFCL, ACEBench, APIBank), MemTR reduces tool calling failures by 2%–9% with only 1%–2% runtime overhead, without any fine-tuning or additional tool-use training data.
