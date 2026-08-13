# Paper Daily Reading - 2026-08-13

## 1. PIANO: Probabilistic Inference Autoencoder Networks for multi-Omics enables robust generative modeling of gene expression and scales single-cell integration to 100 million cells

- Authors: Wang, N., Cardenas, C., Nieto Caballero, V. E., Turner, D., Feinberg, H., Yuan, D., Scott, N., DeBerardine, M., Dan, S., Caceres, L., Schembri, J., Yao, Z., Lee, C., Pillow, J. W., Krienen, F. M.
- Source: biorxiv
- Venue type: preprint
- Journal: biorxiv
- Publication status: preprint
- Publication date: 2026-08-12
- DOI: 10.64898/2026.08.06.743394
- Categories: bioinformatics
- Relevance: 3.550191826136068
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://www.biorxiv.org/content/10.64898/2026.08.06.743394v1.full.pdf
- PDF: https://www.biorxiv.org/content/10.64898/2026.08.06.743394v1.full.pdf
- Local PDF: pdf/2026-08-13_01_PIANO_ Probabilistic Inference Autoencoder Networks for multi-Omics enables robust generative modeling of gene expressio.pdf

Single-cell RNA technologies enable the routine acquisition of transcriptomic atlases. However, these molecular profiles are influenced by overlapping sources of variation. Since these covariates confound comparisons, data integration is the first step in most analyses. Three challenges remain: correcting strong batch effects, scaling to millions of cells, and modeling how covariates influence gene expression. To address these challenges, we developed PIANO: Probabilistic Inference Autoencoder Networks for multi-Omics, a deep learning framework whose central feature is a generative model of gene expression data. Additionally, PIANO achieves robust integrations and trains 10x faster than previous methods. PIANO accurately integrates single-cell data across species and across single-cell and spatial transcriptomics modalities. As practical applications, PIANO models spatially-resolved gene expression during Alzheimer's disease progression in human brains and integrates over 100 million cancer cells to model drug perturbations. In summary, PIANO's integration and generative modeling capabilities will empower novel insights for countless future studies.

## 2. ProTAGAD: A Foundation Model for TAG Anomaly Detection with Decoupled Topological and Textual Prototypes

- Authors: Ziyan Wang, Liwen Wu, Cheng Xie, Song Gao, Zhenli He, Xin Jin
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-11
- DOI: Unavailable
- Categories: cs.LG, cs.AI
- Relevance: 3.4418724222504733
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.10699v1
- PDF: https://arxiv.org/pdf/2608.10699v1
- Local PDF: pdf/2026-08-13_02_ProTAGAD_ A Foundation Model for TAG Anomaly Detection with Decoupled Topological and Textual Prototypes.pdf

Text-Attributed Graphs (TAGs), endowed with abundant textual content along with topological structures, have emerged as a versatile backbone for real-world anomaly detection spanning large language model security, social network moderation, and cyber threat identification. Unlike conventional Graph Anomaly Detection (GAD), which relies primarily on structural irregularities, TAG anomaly detection must jointly leverage both topological patterns and fine-grained textual semantics to capture nuanced anomalous behaviors. The current GNN-based anomaly detectors adopt holistic message-passing schemes that indiscriminately fuse structural proximity and textual semantics during propagation, leading to deep cross-modality coupling. This entanglement acts as a noise amplifier, obscuring subtle anomalous signals and directly giving rise to the Blurred-Anomaly-Boundary (BAB) issue by rendering normal-anomalous decision boundaries poorly separable. This challenge is further amplified for graph foundation models that require robust cross-domain generalization. To bridge this gap, we introduce a novel foundation model for TAG anomaly detection featuring decoupled topological and textual prototypes. Our framework constructs dual prototype banks to independently model structural normality and semantic consistency, effectively isolating anomaly cues that are otherwise diluted during coupled aggregation. Extensive experiments across 14 diverse benchmark datasets demonstrate that our method consistently achieves state-of-the-art performance in cross-domain settings. Notably, the ablation studies further corroborate the prevalence of the BAB issue in conventional coupled TAG anomaly detectors, and show that our decoupled prototype design effectively mitigates this challenge.

## 3. Impact of data quality on deep learning prediction of spatial transcriptomics from histology images

- Authors: Caleb Hallinan, Calixto‐Hope G. Lucas, Jean Fan
- Source: openalex
- Venue type: journal
- Journal: Genome biology
- Publication status: published
- Publication date: 2026-08-11
- DOI: https://doi.org/10.1186/s13059-026-04236-2
- Categories: Single-cell and spatial transcriptomics, AI in cancer detection, Gene expression and cancer classification
- Relevance: 3.390189067988411
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://doi.org/10.1186/s13059-026-04236-2
- PDF: Unavailable
- Local PDF: Not downloaded

Abstract Background Spatial transcriptomic technologies enable high-throughput quantification of gene expression at specific locations across tissue sections, facilitating insights into the spatial organization of biological processes. However, high costs associated with these technologies have motivated the development of deep learning methods to predict spatial gene expression from inexpensive hematoxylin and eosin-stained histology images. While most efforts have focused on modifying model architectures to boost predictive performance, the influence of training data quality remains largely unexplored. Results Here, we investigate how variation in molecular and image data quality stemming from differences in spatial transcriptomic technologies impact deep learning-based gene expression prediction from histology images. To identify the aspects of data quality that impact predictive performance, we conduct in silico ablation experiments, which show that increased sparsity and noise in molecular data degrade predictive performance, while in silico rescue experiments via imputation provide only limited improvements that fail to generalize beyond the test set. Likewise, reduced image resolution can degrade predictive performance and further impacts model interpretability. We further demonstrate that these data quality-driven effects are reproducible across multiple spatial transcriptomics technologies and tissues, and remain consistent when using alternative feature extractors and model architectures. Conclusions Overall, our results show how improving data quality provides an orthogonal strategy to tuning model architecture in spatial transcriptomics-based predictive modeling, highlighting the need to account for technology-specific limitations that directly impact data quality when developing predictive methodologies.

## 4. FITTER: Vocabulary-Agnostic Cross-Domain Inference on Temporal Knowledge Graphs

- Authors: Jiaxin Pan, Mojtaba Nayyeri, Osama Mohammed, Daniel Hernandez, Rongchuan Zhang, Cheng Cheng, Steffen Staab
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-11
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 3.347046687379101
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.10668v1
- PDF: https://arxiv.org/pdf/2608.10668v1
- Local PDF: pdf/2026-08-13_04_FITTER_ Vocabulary-Agnostic Cross-Domain Inference on Temporal Knowledge Graphs.pdf

Temporal knowledge graphs are central to many uses of the Semantic Web, but existing completion methods assume the entities, relation names, and timestamps to be reasoned about are already known at training time, restricting each model to a single graph and vocabulary. We propose FITTER, the first fully-inductive structural model for temporal knowledge graph link prediction that supports cross-domain transfer: the inference graph may contain entirely unseen entities, relation names, and timestamps drawn from a different domain. FITTER represents each predicate by its interaction patterns with others and time through encodings of relative rather than absolute ordering; message-passing fuses local and global temporal context to produce vocabulary-agnostic embeddings. We prove the temporal encoding is time-shift invariant and evaluate FITTER on cross-domain, cross-graph transfer over six temporal knowledge graph benchmarks of diverse domains, granularities, and time spans. FITTER consistently outperforms inductive baselines without retraining, indicating that vocabulary-agnostic structural learning is a viable foundation for inference over the heterogeneous knowledge graphs of the Semantic Web.

## 5. Multi-Granular Rationale-Guided Molecular LLM for Property Prediction

- Authors: Junwoo Park, Minyoung Shin, Cheol Soon Lee, Sujee Lee
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-11
- DOI: Unavailable
- Categories: cs.AI, cs.LG
- Relevance: 3.228962335626852
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.10480v1
- PDF: https://arxiv.org/pdf/2608.10480v1
- Local PDF: pdf/2026-08-13_05_Multi-Granular Rationale-Guided Molecular LLM for Property Prediction.pdf

Large language models (LLMs) are widely applied across chemical tasks, such as molecular property prediction, which underpins drug discovery. Molecular LLMs represent a molecule through several modalities, notably a 1D SMILES sequence or a 2D molecular graph. Both encode molecular information implicitly, so the contribution of individual substructures remains opaque. Retrieval and augmentation methods add context, but from external sources. However, the cues chemists reason over are the internal substructures that drive a property up or down. We propose MR-MoL, a multi-granular rationale-guided molecular LLM that supplies this evidence directly. A fine-tuned GNN scores each substructure through masking, and the most influential ones are serialized as a ranked, direction-tagged rationale that the LLM reads alongside the SMILES sequence and molecular graph. The rationale spans three levels of granularity: Murcko scaffolds with their side chains, BRICS fragments, and functional groups. This is, to our knowledge, the first method to expose GNN-derived attributions to an LLM as evidence for property prediction. On eight MoleculeNet tasks, MR-MoL achieves the best overall results among generalist models and narrows the gap to specialist models tuned for each task. Five diagnostics further confirm that the model reads the rationale rather than merely benefiting from its presence. Its direction, rank, and substructure each shape the prediction, and its attributions reproduce known structure-property relationships.

## 6. P3CA: Encoder-Agnostic Interpretation of Vision Foundation Model Embeddings via Spatial Probing

- Authors: Amoon Jamzad, Dilakshan Srikanthan, Faranak Akbarifar, Nooshin Maghsoodi, Parvin Mousavi
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-10
- DOI: Unavailable
- Categories: cs.CV, cs.LG
- Relevance: 3.2020968739189892
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.10131v1
- PDF: https://arxiv.org/pdf/2608.10131v1
- Local PDF: pdf/2026-08-13_06_P3CA_ Encoder-Agnostic Interpretation of Vision Foundation Model Embeddings via Spatial Probing.pdf

Vision foundation models are increasingly used as reusable encoders in medical image computing, yet their high-dimensional spatial embeddings are difficult to inspect beyond downstream task performance or global dimensionality reduction. We propose position-prompted PCA (P3CA), an encoder-agnostic method for local probing of channel-rich spatial tensors. Given a user-selected spatial prompt, P3CA estimates the feature normalization and dominant covariance directions within that region, then applies the resulting projection to the full tensor to visualize where locally informative directions are expressed. This produces a region-conditioned representation lens without modifying the encoder, retraining, or requiring task-specific labels. We implement P3CA in EmbedVision, an interactive 3D Slicer-based workflow, and evaluate it across natural images, colorectal pathology foundation-model embeddings, and spatial transcriptomic tensors. Across these settings, prompted projections reveal local structure suppressed by global PCA, improve prompt-matched pathology discrimination from frozen three-dimensional projections, and support comparison between learned and measured spatial representations.

## 7. Diffract: Spectral View of LLM Domain Adaptation

- Authors: Nikita Borodin, Maria Krylova, Artem Zabolotnyi, Dmitry Aspisov, Egor Shikov, Nikita Tyuplyaev, Oleg Travkin, Roman Alferov, Dmitry Vinichenko
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-11
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.1801829534316175
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.10850v1
- PDF: https://arxiv.org/pdf/2608.10850v1
- Local PDF: pdf/2026-08-13_07_Diffract_ Spectral View of LLM Domain Adaptation.pdf

We study continual pre-training (CPT) as a mechanism for adapting general-purpose large language models to specialized domains: mathematics, instruction, code, and natural text. Using singular value decomposition of weight matrices, we find that CPT leaves singular value spectra largely invariant, with adaptation driven mainly by changes in singular vectors. An analysis of attention-head projection matrices reveals strong, domain-dependent head heterogeneity, which we exploit to define a head importance criterion: up to 60% of head updates can be removed without measurable quality loss. Selectively rewinding low-importance heads to their pre-trained state improves benchmark accuracy by up to 4% versus the fully trained baseline. Finally, we identify domain connectivity - linear interpolation between CPT checkpoints yields smooth domain-quality interpolation without notable degradation on either domain - and release Diffract, an open-source toolkit for scalable spectral analysis of billion-parameter models.

## 8. Interpreting Language Model Hidden States at Scale

- Authors: Jordan Pettyjohn, Mansi Sakarvadia, Nathaniel Hudson, Daniel McKenzie, Kyle Chard, Ian Foster
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-10
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 3.1692230698940156
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.10260v1
- PDF: https://arxiv.org/pdf/2608.10260v1
- Local PDF: pdf/2026-08-13_08_Interpreting Language Model Hidden States at Scale.pdf

Lens methods interpret large language models (LLMs) by mapping intermediate activations to the output vocabulary, revealing how next-token predictions develop through the network. Trained lenses remain expensive: affine-translator parameters grow quadratically with model width, while exact, full-vocabulary Kullback--Leibler (KL) training dominates memory. Consequently, prior trained lenses have been applied to models of at most 20B parameters and remain tied to particular component types. We present OmniLens, which applies a single lens family to any model-width activation, whether residual stream, attention, or MLP, and combines two independent scaling techniques. First, low-rank translators make per-lens parameter growth linear in model width and reduce trainable parameters by up to 98.4%. Second, Subset-KL materializes only selected vocabulary logits: its Top-k mode cuts peak training memory by up to 70%, while its importance-sampled variant retains unbiased stochastic gradients for the full KL. These savings enable a dense ensemble of 482 lenses for LLaMA-3.3-70B, providing 6x the coverage of a residual-stream design at the same depth. Model-wide coverage then reveals what single-component lenses cannot: the components where a behavior is most visible need not be those where intervention is most effective, and the most effective interventions lie outside the attention heads examined by prior lens studies. Across three case studies (prompt-injection detection, multi-hop memory injection, and toxicity localization), OmniLens reproduces key published results at substantially lower cost.

## 9. AdaGeneBudget: Cell-Adaptive Gene-Token Allocation for Efficient Single-Cell Foundation Models

- Authors: Kim, D., Hwang, U.
- Source: biorxiv
- Venue type: preprint
- Journal: biorxiv
- Publication status: preprint
- Publication date: 2026-08-12
- DOI: 10.64898/2026.08.06.743174
- Categories: bioinformatics
- Relevance: 3.119985467309578
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://www.biorxiv.org/content/10.64898/2026.08.06.743174v1.full.pdf
- PDF: https://www.biorxiv.org/content/10.64898/2026.08.06.743174v1.full.pdf
- Local PDF: pdf/2026-08-13_09_AdaGeneBudget_ Cell-Adaptive Gene-Token Allocation for Efficient Single-Cell Foundation Models.pdf

Single-cell foundation models (scFMs) represent each cell using sequences of gene-associated tokens, making embedding extraction increasingly costly as the number of cells and expressed genes grows. Existing input policies typically rely on fixed input budgets, with retained genes determined by random subsampling, model-native ranking, or a fixed dataset-level highly variable gene (HVG) panel. However, they do not jointly determine, for each cell, which genes to retain and how many tokens to allocate. We introduce AdaGeneBudget, a training-free gene-token selection method that combines each gene's expression with reference-derived inverse detection frequency and retains the shortest ranked prefix that captures a target fraction of the cell's expression-specificity score mass. The resulting cell-specific budget is bounded by predefined minimum and maximum lengths, requires no cell-type labels, and leaves the pretrained backbone unchanged. We evaluated AdaGeneBudget in a frozen-backbone inference setting using pretrained scGPT and Geneformer models on Kang and PBMC reference-mapping tasks, with an additional scPRINT comparison against its official HVG policy and an expressed-only HVG control. Across four scGPT and Geneformer backbone-dataset pairs, AdaGeneBudget substantially reduced mean gene-token counts and peak GPU memory while increasing embedding-extraction throughput by up to 4.63x. Despite this compression, it preserved native-level aggregate annotation utility and consistently outperformed token-matched random selection. AdaGeneBudget also preserved fine-grained and low-support cell identities and retained lineage-marker programs and stimulation-associated pathway genes under compression. In scPRINT, both HVG controls achieved higher annotation macro-F1, whereas AdaGeneBudget more faithfully preserved the stimulation-induced embedding direction. These results establish biologically informed, cell-adaptive gene-token allocation as a practical complement to architectural and systems-level efficiency methods for applying existing scFMs to new datasets. They also suggest a cell-adaptive input-allocation principle for future models operating under finite token budgets.

## 10. MultiModal Code-Switching: Interleaving Visual Objects into Language for Explicit Object-Level Alignment

- Authors: Changhao Xiang, Shangyu Xing, Zhen Wu, Jianbing Zhang, Xinyu Dai
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-11
- DOI: Unavailable
- Categories: cs.CV, cs.CL, cs.LG
- Relevance: 3.102811911400453
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.11167v1
- PDF: https://arxiv.org/pdf/2608.11167v1
- Local PDF: pdf/2026-08-13_10_MultiModal Code-Switching_ Interleaving Visual Objects into Language for Explicit Object-Level Alignment.pdf

Existing Multimodal Large Language Models (MLLMs) predominantly rely on image-text pairs for modality alignment pretraining, mapping global image representations to long textual descriptions. However, this image-level alignment suffers from referential ambiguity: models struggle to infer the correspondences between multiple visual objects and textual entities from the global representation, leading to data inefficiency and suboptimal semantic grounding. To address this, we propose MultiModal Code-Switching (MMCS), a novel pretraining paradigm that provides explicit object-level supervision. Inspired by the linguistic phenomenon of code-switching, MMCS interleaves vision and language by replacing textual entities with their corresponding visual objects, enforcing local vision-language grounding. We further develop a scalable data synthesis pipeline to generate a pretraining dataset of 773K samples with accurate object-entity correspondences. Experiments show that MMCS is highly data-efficient: with only 50K samples, it matches or surpasses models trained on 600K image-text pairs. Furthermore, MMCS consistently improves visual grounding and perception capabilities across varying model scales.

## 11. Spatial multi omics enables single cell transcriptome metabolome inference

- Authors: shen, x., ZHANG, X.-Y.
- Source: biorxiv
- Venue type: preprint
- Journal: biorxiv
- Publication status: preprint
- Publication date: 2026-08-12
- DOI: 10.64898/2026.08.06.743252
- Categories: bioinformatics
- Relevance: 3.076713875539096
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://www.biorxiv.org/content/10.64898/2026.08.06.743252v1.full.pdf
- PDF: https://www.biorxiv.org/content/10.64898/2026.08.06.743252v1.full.pdf
- Local PDF: pdf/2026-08-13_11_Spatial multi omics enables single cell transcriptome metabolome inference.pdf

Joint single cell transcriptomic metabolomic profiling remains technically intractable. Here we present CHIMERA (Cell-level Hybrid Inference of Metabolome Embedded on RNA Atlas), a data-driven framework that learns transcriptome to metabolome mappings from spatially paired multi omics data and transfers them to unpaired scRNAseq. CHIMERA generates quantitative, database independent single cell metabolite abundances and, by pairing them with the measured transcriptome of the same cells, enables joint co embedding of genes and metabolites for the discovery of differential metabolites and co regulated gene metabolite modules. Using 10x Visium paired with MALDI MSI from murine liver sections and a matched scRNAseq reference, CHIMERA achieves a per-metabolite median Pearson r = 0.285 with positive cross-section generalization. On an independent Liver Cell Atlas Western diet cohort, CHIMERA recovers metabolic reprogramming that recapitulate published non-alcoholic fatty liver disease pathophysiology. Applied to a Rarres2 (chemerin) knock down hepatocellular carcinoma model, CHIMERA uncovers metabolic heterogeneity among tumour associated macrophages, resolving four metabolic subclusters (MC-0 to MC-3); Rarres2 appears to drive macrophage polarization from an LAM-like MC-3 state toward Spp1+ like MC-0/MC-2 by modulating a co-regulated gene metabolite module a dual omics phenotype undetectable by either modality alone. CHIMERA is the first data-driven framework for quantitative single cell metabolome inference, opening joint transcriptomic metabolomic analyses inaccessible to either experimental or knowledge based computational approaches.

## 12. ReLTEx: Reliable LLM-based Taxonomy Expansion

- Authors: Zeinab Ghamlouch, Mehwish Alam
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-11
- DOI: Unavailable
- Categories: cs.CL, cs.AI
- Relevance: 3.04075074739385
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.10970v1
- PDF: https://arxiv.org/pdf/2608.10970v1
- Local PDF: pdf/2026-08-13_12_ReLTEx_ Reliable LLM-based Taxonomy Expansion.pdf

Recent advances in Large Language Models (LLMs) have demonstrated strong capabilities in generating semantically relevant concepts and relations, making them promising tools for taxonomy enrichment. However, directly relying on LLM-generated expansions often leads to noisy, redundant, or hierarchically inconsistent structures, limiting their reliability for automated taxonomy expansion. In this paper, we present ReLTEx, a framework for reliable LLM-based taxonomy expansion. ReLTEx combines LLM-driven candidate generation with structure-aware validation and recursive expansion control to improve the consistency and quality of generated taxonomies by reducing hallucinations. We evaluate the proposed framework using benchmark taxonomies under a masked taxonomy expansion setting and compare multiple validation strategies. Experimental results, supported by both adapted evaluation metrics and human evaluation, demonstrate that ReLTEx produces more reliable and semantically coherent taxonomy expansions.

## 13. The Gaussian-Multinoulli Restricted Boltzmann Machine: A Potts Model Extension of the GRBM

- Authors: Nikhil Kapasi, Mohamed Elfouly, William Whitehead, Luke Theogarajan
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2025-05-16
- DOI: Unavailable
- Categories: cs.LG, cs.AI
- Relevance: 3.0227917742014894
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2505.11635v2
- PDF: https://arxiv.org/pdf/2505.11635v2
- Local PDF: pdf/2026-08-13_13_The Gaussian-Multinoulli Restricted Boltzmann Machine_ A Potts Model Extension of the GRBM.pdf

Many real-world tasks, from associative memory to symbolic reasoning, benefit from discrete, structured representations that standard continuous latent models can struggle to express. We introduce the Gaussian-Multinoulli Restricted Boltzmann Machine (GM-RBM), a generative energy-based model that extends the Gaussian-Bernoulli RBM (GB-RBM) by replacing binary hidden units with q-state categorical (Potts) units, yielding a richer latent state space for multivalued concepts. We provide a self-contained derivation of the energy, conditional distributions, and learning rules, and detail practical training choices (contrastive divergence with temperature annealing and intra-slot diversity constraints) that avoid state collapse. To separate architectural effects from sheer latent capacity, we evaluate under both capacity-matched and parameter-matched setups, comparing GM-RBM with GB-RBM configured to have the same number of possible latent assignments. On analogical recall and structured memory benchmarks, GM-RBM achieves competitive, and in several regimes improved, recall at equal capacity with comparable training cost, despite using only Gibbs updates. The discrete q-ary formulation is also amenable to efficient implementation. These results clarify when categorical hidden units provide a simple, scalable alternative to binary latents for discrete inference within tractable RBMs.

## 14. Curate Before You Connect: Identity and Ontology Tagging in a Production Knowledge Graph

- Authors: Vaibhav Dangaich, Kevin Lewis, Kundeshwar Pundalik
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-11
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 3.0143769203088278
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.10644v1
- PDF: https://arxiv.org/pdf/2608.10644v1
- Local PDF: pdf/2026-08-13_14_Curate Before You Connect_ Identity and Ontology Tagging in a Production Knowledge Graph.pdf

Extraction produces candidate entities and relationships; writing them into a graph is where identity is decided, and identity decisions are destructive in a way extraction errors are not. A wrong type can be corrected later, but two records merged under one identity cannot be separated once their properties have been combined, and the merge leaves no error behind. This paper describes the ingestion and ontology-tagging layer that turns a validated extraction stream into a knowledge graph of 537,157 entities and 2,198,567 relationships drawn from 98,795 government documents. We describe a record-identity ladder that decides sameness from identifier columns, name columns, display names and type-scoped position rather than from name similarity. The ladder governs de-duplication within parsed tables, while the graph write applies a coarser canonical-name key, so records sharing a canonical name merge automatically on exact equality. We argue rather than demonstrate that this is where the automation line belongs: no identity benchmark is reported, and the over-merges the key permits are undetectable by construction. That policy, under which entity resolution only ever flags candidates, followed an incident in which two surface forms of one name were merged, corrupting a correct record and deleting eight entities from an unrelated document. We then describe multi-class ontology tagging and an evidence asymmetry we did not anticipate: an entity name is an instance label rather than a type assertion, so matching name fragments against a class index invents classifications. Requiring anchored evidence cut role assignments on an enriched sample from 36 to 4, all confirmed correct. We quantify the graph's conformance debt, show secondary classifications compensating for a mis-parented primary class, and describe a curation queue grown to 48,403 pending proposals against 775 human decisions.

## 15. Hierarchical Compositionality for An Assistive AI Agent

- Authors: Tianyi Fu, Mohan Sridharan
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-11
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 3.0070212322731997
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.10330v1
- PDF: https://arxiv.org/pdf/2608.10330v1
- Local PDF: pdf/2026-08-13_15_Hierarchical Compositionality for An Assistive AI Agent.pdf

AI agents are increasingly being developed to assist humans in various applications, and Large Language Models and other deep network architectures are considered to be state of the art for such agents. These methods are impressive stochastic predictors, but they are resource-hungry, opaque, and known to make arbitrary decisions in novel situations due to the narrow set of underlying representation and processing choices. Our work seeks to explore the design of architectures for such AI agents based on core principles that can be traced back to the early pioneers of AI but are not fully utilized in modern AI methods. We do so in this paper in the context of the core problem of AI agents addressing ambiguity in the objects being referred to by the human participants. Humans address such ambiguity by heuristically leveraging compositional knowledge of domain context and the preferences of the other human participants. Drawing inspiration from this observation, we describe an architecture that embeds the principle of hierarchical compositionality and uses simple heuristics to achieve the desired disambiguation. Specifically, domain objects are represented in terms of primitive attributes drawn from human-validated semantic feature norms, and a hierarchical combination of attributes and concepts automatically identified from a limited observed history of interactions of an assistive agent with specific users. The assistive agent then achieves the desired disambiguation by reasoning with knowledge of this compositional hierarchy; axioms governing domain dynamics; and models of semantic compatibility, session salience, and user-specific thematic preference, requesting human clarification when necessary. Experiments show that our approach consistently outperforms state of the art data-driven baselines, supporting adaptation to specific user profiles.

## 16. More Accurate, Less Human: Gestalt Grouping in Vision Models

- Authors: Sudhanva Manjunath Athreya, Sai Phani Kumar Malladi
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-10
- DOI: Unavailable
- Categories: cs.CV, cs.LG
- Relevance: 2.9793459020518887
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.10195v1
- PDF: https://arxiv.org/pdf/2608.10195v1
- Local PDF: pdf/2026-08-13_16_More Accurate, Less Human_ Gestalt Grouping in Vision Models.pdf

Human vision organizes what it sees into wholes: same-colored points group into series, similar marks cohere into categories, and shapes complete into recognizable objects. These are the Gestalt operations that visualization design builds on. Whether vision models organize visual content this way has not been systematically tested. We introduce a behavioral battery that scores models against human data from prior perception studies on four grouping tasks: mark-color odd-one-out, color-series counting, silhouette recognition, and object odd-one-out. We apply it to 45 models across five training families: supervised, self-supervised, and contrastive vision-language encoders, open-weight VLMs, and closed foundation models. The battery reveals that agreement with human responses captures aspects of perceptual organization that conventional performance metrics fail to distinguish, with several closed models exhibiting substantially lower alignment than their benchmark accuracy would suggest. Scoring against published perception data therefore gives visualization research a reusable yardstick, requiring no new user study, for auditing whether the models now entering visualization pipelines organize what they see the way their human audience does.

## 17. Uncertainty-Aware Deep Learning for Genomics Applications: Insights from an Empirical Study

- Authors: Sepideh Saran, Mahsa Ghanbari, Uwe Ohler
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-11
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 2.9686835202296855
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.11054v1
- PDF: https://arxiv.org/pdf/2608.11054v1
- Local PDF: pdf/2026-08-13_17_Uncertainty-Aware Deep Learning for Genomics Applications_ Insights from an Empirical Study.pdf

Deep learning models have emerged as the standard computational tool for a wide range of applications in genomics. Yet, uncertainty quantification (UQ) -- and more specifically, the reliability of different uncertainty estimates in this domain -- has received little systematic attention. This work presents an empirical analysis of UQ in deep learning models, focusing on genomics applications. In a series of experiments, we contrast Deep Ensembles, Bayesian Neural Networks, and Monte Carlo-dropout methods. We assess their ability to quantify uncertainty in different scenarios, accounting for common dataset characteristics in two genomic application areas and modalities: sequence-to-activity models, and single-cell expression analysis. Our systematic comparison framework provides guidelines for the applicability and reliability of UQ methods in genomics, highlighting their strengths and limitations in different scenarios. We show that Bayesian Neural Networks are better at capturing uncertainty caused by strong class imbalance and out-of-distribution data in genomics, despite their computational disadvantages. Moreover, we show how uncertainty scores can be used to select high-quality predictions in protein-RNA interactions.

## 18. megaMine: a scalable, rule-based framework for mining gene-cancer-drug evidence from biomedical literature

- Authors: JUNAID, M., Prazanowska, K. H., Jeong, H.-E., Ryu, Y., Choi, J., An, J.-Y., Lim, S. B.
- Source: biorxiv
- Venue type: preprint
- Journal: biorxiv
- Publication status: preprint
- Publication date: 2026-08-12
- DOI: 10.64898/2026.08.06.743392
- Categories: bioinformatics
- Relevance: 2.9600920003099613
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://www.biorxiv.org/content/10.64898/2026.08.06.743392v1.full.pdf
- PDF: https://www.biorxiv.org/content/10.64898/2026.08.06.743392v1.full.pdf
- Local PDF: Not downloaded

The rapid expansion of the oncology literature has outpaced manual curation of clinically relevant gene-cancer-drug associations and oncogenic driver evidence. Existing automated approaches often lack transparency or are difficult to scale across heterogeneous data sources. To address this gap, we developed megaMine, a transparent, rule-based, and context-aware literature-mining framework that integrates therapeutic and driver evidence from PubMed, PubTator, and Europe PMC by combining entity recognition, hierarchical heuristics, and contextual labeling. In therapy mode, megaMine was applied to approximately 100,000 oncology articles published between 2015 and 2025, yielding more than 23,000 structured sentence-level evidence records, with standardized annotations for drug response, resistance, and study context. Internal evaluation of context labels showed strong separability between efficacy and non-efficacy evidence using ridge logistic regression (AUROC = 0.915; AUPRC = 0.941). Benchmarking against NCI/OncoKB-supported drug-cancer associations showed that curated clinical associations had higher megaMine composite evidence scores than unlabeled comparison pairs [median (IQR): 25.6 (9.07-72.5) vs. 3.61 (1.69-8.69); Wilcoxon rank-sum test, P < 2.2 x 10^-16]. In driver mode, megaMine retrieved mutation- and biomarker-related evidence from an ERBB-focused gastric cancer query, generating 750 evidence rows from 200 PMIDs. These results demonstrate that deterministic and interpretable approaches can support scalable evidence extraction for downstream applications such as knowledge graph construction and literature-based evidence synthesis.

## 19. Power law graph attention: exact generalization of scaled dot-product attention, empirical collapse at inference

- Authors: Burc Gokden
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-10
- DOI: Unavailable
- Categories: cs.LG, cs.CL
- Relevance: 2.916580597844413
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.10288v1
- PDF: https://arxiv.org/pdf/2608.10288v1
- Local PDF: pdf/2026-08-13_19_Power law graph attention_ exact generalization of scaled dot-product attention, empirical collapse at inference.pdf

The Large Language Model from Power Law Decoder Representations (PLDR-LLM) and its attention, Power Law Graph Attention (PLGA), replace the fixed bilinear form of scaled dot-product attention (SDPA) with a learned, input-generated bilinear operator $G_{LM}$, built from a positive tensor $A_{LM}$ by elementwise power laws. The architecture is fully specified, verified against pinned reference releases; claims are labeled theorem, conditional theorem, measurement, or conjecture. Unconditionally: PLGA contains SDPA exactly at $G_{LM}=I$; $A_{LM}$ and $A_P$ are strictly entrywise positive, with Perron-Frobenius structure on $A_{LM}$; the DAG regularizer has the NOTEARS walk-counting form and positivity obstructs exact acyclicity; and, under nonresonance (satisfied by standard rotary frequencies), a commutant criterion identifies which operators preserve relative-position dependence. An inference-collapse theorem: exact input invariance of deductive outputs collapses inference to generalized SDPA with a constant operator. Measured invariance: relative fluctuations of $10^{-6}$ and below; perturbation bounds quantify but do not certify cached inference; the assembled proxy misses the decoding margin. A conditional three-stage mechanism (rotary twirl, concentration, row-map contraction) is measured on a released checkpoint. Blockwise training and scoring under the global Gram are stated with explicit target exposure; on tested samples, block and sequential scoring select identical answers and agree on the published TruthfulQA probability-mass metric within $5\times 10^{-5}$ per item. Self-organized criticality enters as a phenomenological framework with an intrinsic order parameter; open claims become falsifiable conjectures. Selected proof cores are machine-checked in Lean 4.

## 20. Cross-View Feature Matching: Survey, Benchmarking, and Foundation-Model Perspectives

- Authors: Songlin Du, Xiaoyong Lu, Zeyu Wu, Xiaobo Lu, Guobao Xiao, Bin Fan, Jiayi Ma, Takeshi Ikenaga
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-11
- DOI: Unavailable
- Categories: cs.LG, cs.CV
- Relevance: 2.9138457600550516
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.11093v1
- PDF: https://arxiv.org/pdf/2608.11093v1
- Local PDF: pdf/2026-08-13_20_Cross-View Feature Matching_ Survey, Benchmarking, and Foundation-Model Perspectives.pdf

Cross-view feature matching aims to establish reliable correspondences across images with large viewpoint variations. Over the past decade, the field has evolved from task-specific models toward increasingly unified and generalizable correspondence models, with recent progress further driven by the emergence of vision foundation models (VFMs). Despite these advances, existing studies remain highly diverse in their problem formulations, model architectures, training paradigms, and evaluation protocols, making it difficult to obtain a unified understanding of the field. In this survey, we present a unified review of cross-view feature matching. We first introduce a structured taxonomy covering feature extraction, single-type feature matcher, multi-type feature matcher, VFMs based methods, training strategy and robust estimation, providing a coherent framework for analysis and comparison. We further examine recent advances, distilling key design principles and highlighting the shift toward unified and generalizable correspondence models. We also provide a unified experimental benchmarking of representative state-of-the-art methods under consistent protocols, enabling fair and comprehensive performance comparisons. In addition, we discuss open challenges and future directions, including efficiency, robustness under extreme conditions, and cross-domain generalization. This survey aims to provide a comprehensive and structured reference for understanding the evolution, current landscape, and future development of cross-view feature matching in the era of vision foundation models.

## 21. Evidence-Grounded Trustworthy Multimodal Reasoning and Evaluation Benchmark in Complex Urban Scenes

- Authors: Zhaoyang Wei, Bowen Jiang, Xumeng Han, Jiashu Li, Xuehui Yu, Yuling Liu, Guorong Li, Zhenjun Han, Jianbin Jiao
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-11
- DOI: Unavailable
- Categories: cs.CV, cs.AI
- Relevance: 2.9087748773122035
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.10954v1
- PDF: https://arxiv.org/pdf/2608.10954v1
- Local PDF: pdf/2026-08-13_21_Evidence-Grounded Trustworthy Multimodal Reasoning and Evaluation Benchmark in Complex Urban Scenes.pdf

While Multimodal Large Language Models (MLLMs) demonstrate impressive performance in benign scenarios, their cognitive reliability deteriorates significantly in complex scenes under adverse conditions. In these settings, models often rely on implicit inference without sufficient visual evidence, leading to a disconnect between perception and reasoning. Meanwhile, existing outcome-oriented benchmarks evaluate only final predictions and fail to diagnose failures in the underlying reasoning process. To address this gap, the authors propose AD2-Bench, which introduces a Hierarchical Visual Diagnosis framework that decomposes reasoning into a structured Chain of Evidence (CoE). This fine-grained diagnosis reveals that robust multimodal reasoning fundamentally depends on accurate evidence acquisition. Building on this perspective, the authors formulate reasoning from a probabilistic viewpoint and identify two primary causes of reasoning failure: Spatial Ambiguity, where models fail to distinguish target objects from background clutter, resulting in localization errors; and Semantic Uncertainty, where degraded visual features lead to incorrect semantic interpretation, resulting in understanding errors. To overcome these evidence deficiencies, they further propose Evidence-grounded Visual Reasoning (EGVOR), which replaces implicit reasoning with the explicit generation of Evidence Atoms - structured spatial-semantic triplets that enforce tight alignment between localization and semantic understanding. The model is trained through a hierarchical curriculum that progresses from reflective supervision construction to reinforcement learning, where reducing reasoning variance is explicitly rewarded. Extensive experiments demonstrate that EGVOR substantially improves reasoning stability under adverse conditions, providing a more robust framework for trustworthy multimodal cognition.

## 22. STR-PG: A Topology-decoupled Pangenome Framework for Scalable Short-read Genotyping of Short Tandem Repeats

- Authors: YUAN, J., XUE, Z., TANG, H., LIU, Y., WANG, J.
- Source: biorxiv
- Venue type: preprint
- Journal: biorxiv
- Publication status: preprint
- Publication date: 2026-08-12
- DOI: 10.64898/2026.08.07.743532
- Categories: bioinformatics
- Relevance: 2.9007450011426905
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://www.biorxiv.org/content/10.64898/2026.08.07.743532v1.full.pdf
- PDF: https://www.biorxiv.org/content/10.64898/2026.08.07.743532v1.full.pdf
- Local PDF: Not downloaded

Short tandem repeats (STRs) are a rich and highly polymorphic source of human genetic variation, but representing and genotyping them in pangenome graphs remains challenging. Explicitly encoding each STR allele as a separate graph path results in increasingly complex local structures as cohort diversity increases, leading to larger index sizes and requiring significant resources for graph reconstruction when new alleles are introduced. Here, we propose STR-PGa topologically decoupled genome-wide framework that separates stable locus representation from scalable STR allele content. STR-PG uses topologically fixed pointer nodes to represent each target locus, while allele sequences, repeat counts, motif annotations, and population frequency metadata are stored in an external registry. Short reads are mapped to STR loci via syncmer-based flanking anchors, and genotyping is performed within a locus-specific candidate space using allele-level alignment likelihood and Bayesian inference. Newly supported alleles can be integrated through registry-level updates without the need to rebuild the graph structure. Evaluations using simulated whole-genome sequencing data, 1000 Genomes Project (1kGP) samples, and r real whole-exome sequencing data from matched whole-blood-cell controls demonstrate that STR-PG maintains accurate genotyping results across various STR classes, reproduces expected population structures, and substantially reduces the computational cost of integrating additional alleles. STR-PG provides a compact and scalable framework for population-scale STR analysis using short-read sequencing.

## 23. Continuous Interaction Diffusion: A Diffusion-Native Runtime for Asynchronous Tool-Augmented Reasoning

- Authors: Yuhang Cao
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-11
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 2.8728437030935456
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.10438v1
- PDF: https://arxiv.org/pdf/2608.10438v1
- Local PDF: pdf/2026-08-13_23_Continuous Interaction Diffusion_ A Diffusion-Native Runtime for Asynchronous Tool-Augmented Reasoning.pdf

Large language models increasingly rely on external tools to access up-to-date information, perform computation, and interact with the outside world. For autoregressive models, tool use naturally fits the generation process: the model emits a tool call, waits for the result, and then continues generating. Diffusion language models (dLLMs), however, reason by repeatedly refining many parts of their output in parallel, making this stop-and-resume interaction pattern unnecessarily restrictive. It can force tool decisions before the model's reasoning has stabilized, delay useful observations until a discrete call finishes, and introduce redundant refinement and tool execution, potentially hurting both task accuracy and inference efficiency.
  We introduce Continuous Interaction Diffusion (CID), a diffusion-native model--runtime architecture that integrates tool interaction into iterative denoising. CID separates a model-read-only fact channel, a thought channel represented by a Typed Cognitive Tensor, and a display channel. Information needs can emerge before a textual or JSON call is fully serialized, allowing perceptual bindings to launch external reads while denoising continues. Returned results are projected into the evolving thought state and can revise earlier cognition and display regions. Persistent bindings reuse static results without repeated external execution and refresh changing sources when needed. CID is designed to expose evidence earlier, overlap tool latency with model computation, reduce duplicate external work, and preserve useful computation after new evidence arrives. We formalize the architecture, runtime, and training objectives, and define an evaluation protocol for task quality and end-to-end efficiency. This first paper focuses on read-only tools and makes no empirical performance claims.

## 24. Conditional Independence Tests for Constraint-Based Causal Discovery: A Survey

- Authors: Pavel Averin, Theodoros Moysiadis, Ioannis Katakis
- Source: arxiv
- Venue type: preprint
- Journal: Transactions on Machine Learning Research (07/2026)
- Publication status: preprint
- Publication date: 2026-08-11
- DOI: Unavailable
- Categories: stat.ML, cs.LG
- Relevance: 2.8581188429845716
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.11156v1
- PDF: https://arxiv.org/pdf/2608.11156v1
- Local PDF: pdf/2026-08-13_24_Conditional Independence Tests for Constraint-Based Causal Discovery_ A Survey.pdf

Conditional Independence (CI) tests are the statistical engine of constraint-based causal discovery: in algorithms such as PC (Peter-Clark) and FCI (Fast Causal Inference), skeleton pruning and key orientations follow directly from CI decisions. This survey reviews CI testing with emphasis on assumptions, robustness, and scalability in high-dimensional and mixed-type settings common in biomedical domains. The survey organizes widely used CI methods into six families: partial-correlation, contingency-table, regression, nearest-neighbor, kernel, and machine-learning-based. Special emphasis is provided on the robustness layers that address the limitations of these families. For each family, the survey examines when CI decisions reflect the data-generating distribution and when they fail. By this, we link test-level properties, including power decay with conditioning set size and asymmetric type I/II error consequences, to graph-level errors in skeleton recovery and v-structure orientation. The survey also compares adoption across major R and Python libraries and summarizes open challenges, including mixed-type CI testing without discretization, small-sample error control, and strategies for improving scalability of CI-testing.

## 25. Mapping and Measuring the Behavioral Evolution of Large Language Models

- Authors: Dong Qiao, Chris Ding, Jicong Fan
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-11
- DOI: Unavailable
- Categories: cs.LG, cs.CL
- Relevance: 2.856454980608008
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.11027v1
- PDF: https://arxiv.org/pdf/2608.11027v1
- Local PDF: pdf/2026-08-13_25_Mapping and Measuring the Behavioral Evolution of Large Language Models.pdf

Benchmark leaderboards summarize how well a language model performs, but not how its behavior relates to that of other models or changes across generations. We characterize the output behavior of 32 models from six families using their responses to a shared bank of 10{,}000 prompts. After embedding each response, we construct three complementary sentence-level dissimilarities: an aligned mean per-prompt distance, which is a pseudometric on observed model responses; a PCA-compressed summary of prompt-wise disagreement; and an alignment-free Gromov--Wasserstein discrepancy between models' internal response geometries. We use these constructions to study static organization and temporal change on a release-date axis through behavioral maps, family-wise drift, hierarchical clustering, cross-family convergence, and response-cloud dispersion. Across the three constructions, model families form coherent clusters, with \texttt{gpt-2} as a global outlier; cross-family distances decrease over time; and several recent reasoning-oriented models have comparatively compact response clouds. A token-level cross-check based on per-prompt Maximum Mean Discrepancy closely agrees with the sentence-level mean distance (Spearman $ρ=0.98$) and recovers the same qualitative findings. We organize these comparisons through a measure-theoretic lens making their alignment and invariance assumptions explicit. We also establish an architecture-agnostic sufficient condition linking behavioral similarity to inference-prompt coverage, small excess population log-loss, and similar effective target distributions---a possible training-side account rather than an empirical explanation of the observed trends. Our pipeline is label-free, and re-encoding every response with three further encoders---down to one $73\times$ smaller---preserves the rank geometry, the outliers, and the sign of the time trend.

## 26. DeMixNB: deconvolution of sparse-count RNA sequencing data for tumor cells using embedded negative binomial distributions

- Authors: Matthew D. Montierth, Hao Yan, Liyang Xie, Kinga Nemeth, Xiaoxi Pan, Ruonan Li, Caner Ercan, Peng Yang, Ansam Sinjab, Tieling Zhou, Fuduan Peng, Manisha Singh, Linghua Wang, Scott Kopetz, Humam Kadara, Yinyin Yuan, George A. Calin, Wenyi Wang
- Source: openalex
- Venue type: journal
- Journal: Genome biology
- Publication status: published
- Publication date: 2026-08-10
- DOI: https://doi.org/10.1186/s13059-026-04234-4
- Categories: Single-cell and spatial transcriptomics, Cancer Genomics and Diagnostics, MicroRNA in disease regulation
- Relevance: 2.82359615274978
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://doi.org/10.1186/s13059-026-04234-4
- PDF: Unavailable
- Local PDF: Not downloaded

Abstract Estimating tumor-specific transcript proportions from mixed bulk samples has potential to inform novel biology. However, estimation accuracy using existing methods in sparse-count data such as microRNA-seq and spatial transcriptomics has yet to be established. We generate a mixed small RNA benchmark dataset to demonstrate analytical challenges. To resolve them, we develop DeMixNB, a semi-reference-based deconvolution model assuming a sum of negative binomial distributions. Applications to miRNA-seq from 885 patients with breast cancer and 4,709 spatial spots from lung cancer generates clinical and mechanistic insights into tumor cell plasticity. This supports the important utility of DeMixNB to investigate cancer RNomes.

## 27. PerturbLDM: conditional latent diffusion for modelling single-cell perturbation responses

- Authors: Yu, L., Hsieh, K.-L., Chu, Y., Lan, Q., Zhao, X., Hsu, Y.-C., Wood, C. S., Rasmy, L., Pilie, P. G., Zhi, D., Zhao, Z., Jiang, X., Dai, Y.
- Source: biorxiv
- Venue type: preprint
- Journal: biorxiv
- Publication status: preprint
- Publication date: 2026-08-12
- DOI: 10.64898/2026.08.07.743610
- Categories: bioinformatics
- Relevance: 2.8176876062855865
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://www.biorxiv.org/content/10.64898/2026.08.07.743610v1.full.pdf
- PDF: https://www.biorxiv.org/content/10.64898/2026.08.07.743610v1.full.pdf
- Local PDF: Not downloaded

Single-cell perturbation profiling maps intervention-induced phenotypes, yet experiments measure only a fraction of the perturbation-context space. Learning context-dependent perturbation effects could enable response prediction beyond measured conditions. Here we introduce PerturbLDM, a latent-diffusion framework for conditional generation of single-cell transcriptional responses. Following Tahoe-100M pretraining, it outperformed leading methods across 13,942 held-out combinations of observed drugs, doses and cell lines, with higher matched-control effect correlation than an additive marginal baseline in 95.2% of conditions. The Tahoe-100M-pretrained model was further used to rank PANACEA compounds by pathway similarity, placing shared-mechanism pairs among nearest neighbours. In smaller datasets, PerturbLDM generated a mid-gestational fetal-colon state with 67% lower gene-wise error than Squidiff, retaining the balance between absorptive and BEST4/OTOP2-like epithelial programmes. In PBMCs, it captured six of seven interferon and antiviral programmes and the interferon-associated FAO-OXPHOS programme more accurately than scGen. Together, these results support conditional response generation across data scales and biological settings.

## 28. MEGA: Self-Evolving Agent Optimization Infrastructure via Wisdom Graph

- Authors: Jung Hwan Lee, Kyu Ho Lee, Gwang Hoon Yoo
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-11
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 2.8131042615708353
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.10504v1
- PDF: https://arxiv.org/pdf/2608.10504v1
- Local PDF: pdf/2026-08-13_28_MEGA_ Self-Evolving Agent Optimization Infrastructure via Wisdom Graph.pdf

As coding agents increasingly handle implementation, the central challenge shifts from building individual agents to building an infrastructure that systematically improves them. Current approaches optimize agent systems without accumulating transferable knowledge, accumulate knowledge without compositional reasoning over it, and lack a mechanism for that knowledge to self-evolve through operational evidence. MEGA (Meta Evaluation-Grounded Adaptation) addresses these gaps as a self-evolving infrastructure: each optimization cycle produces durable assets, compositional reasoning over those assets guides subsequent optimization, and operational evidence refines both the accumulated wisdom and the reasoning that governs it. Layer 1 distills reusable wisdom from agent sessions through behavioral-pattern clustering and empirical A/B validation, transforming each process into a durable asset. Layer 2 decomposes these assets into atomic PCR (Primary-Context-Resultant) units within a typed Wisdom Graph and performs deductive, abductive, and inductive reasoning to expand implicit relations; it then assembles context-specific execution plans through compositional retrieval that surfaces bridging knowledge unreachable by embedding similarity alone. Layer 3 performs multi-agent collaborative optimization over heterogeneous agent workflows (code nodes, LLM calls, and tool-using agents), attributing improvement effects to specific strategy changes through controlled evaluation that eliminates data variance. Evidence fed back from Layer 3 drives the self-evolution of both the curation strategies that govern wisdom composition and the optimization trajectories accumulated across runs. The result is an infrastructure in which optimizing an agent system and evolving the knowledge that guides optimization are one and the same process.

## 29. Actionable Hallucination Detection: Translating Latent Uncertainty into Agentic Critique

- Authors: Sanidhya Vijayvargiya, Rahul Lokesh
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-11
- DOI: Unavailable
- Categories: cs.LG, cs.AI
- Relevance: 2.7933486938867578
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.10430v1
- PDF: https://arxiv.org/pdf/2608.10430v1
- Local PDF: pdf/2026-08-13_29_Actionable Hallucination Detection_ Translating Latent Uncertainty into Agentic Critique.pdf

Large Language Models (LLMs) deployed as AI agents frequently exhibit user specification-grounding failures, executing hallucinated, undesired actions to force a resolution rather than expressing uncertainty. Existing detection methods fail to provide actionable, real-time correction as they either do not localize the hallucinations, or incur prohibitive inference latency. We introduce the Latent Critic, a lightweight low-rank adapter (LoRA) that operates concurrently with a frozen base LLM's generation to actively restructure the transformer's residual stream---amplifying latent grounding signals and translating them into localized, natural language feedback within a single sequence. By refining the base model's native uncertainty signals, this manipulation of the latent space enables reliable, granular detection without the overhead of secondary inference loops. Mechanistic analysis via activation patching and layer-wise probing shows that this rank-invariant behavior restructures pre-existing uncertainty geometry into a linearly separable representation that transfers more reliably than base model representations alone. Using tool-calling as an instantiation of granular hallucinations, we validate the detection and downstream improvements enabled by the Latent Critic architecture across Qwen and Llama-based models. Demonstrating superior real-time efficacy, our approach significantly outperforms equivalent-scale fine-tuned external detectors, semantic entropy baselines, and passive internal probes in isolating hallucinations, achieving 0.966 AUROC and >80% accuracy in localization (e.g., ungrounded: date). When deployed in a closed-loop ReAct environment, the Critic acts as a negligible latency guardrail, intercepting hallucinations before execution to prevent undesired actions while simultaneously leveraging this specific localized feedback to enable efficient agent self-correction.

## 30. Can Bayesian Optimization Efficiently Find a Strong Single Expert in Neural Thickets?

- Authors: Nigel Bastian Cendra, Abdelhamid Ezzerg, Fernando Julio Cendra, Jeremias Knoblauch, Jakob Zeitler
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-11
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 2.7902427610127774
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.10867v1
- PDF: https://arxiv.org/pdf/2608.10867v1
- Local PDF: pdf/2026-08-13_30_Can Bayesian Optimization Efficiently Find a Strong Single Expert in Neural Thickets.pdf

Gradient-free post-training has emerged as a compelling alternative to gradient-based optimization for large language models (LLMs), but existing approaches remain costly. We ask whether structured search can identify a strong single expert under a modest evaluation budget. Motivated by evidence that useful weight updates lie in low-dimensional subspaces, we apply Bayesian optimization within a random linear embedding of weight space. Our method requires no backpropagation and uses a Gaussian process surrogate to guide candidate evaluations efficiently. Across several reasoning benchmarks with Qwen2.5-Instruct models from 0.5B to 3B parameters, Bayesian optimization using five times less candidate evaluations matches or exceeds RandOpt. These results show that surrogate-guided search can substantially reduce the evaluation cost of gradient-free post-training while producing stronger deployable single experts.
