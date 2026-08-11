# Paper Daily Reading - 2026-08-11

## 1. CellWorld: From Gene-Level Reconstruction to Latent Cell Prediction in Spatial Transcriptomics Foundation Models

- Authors: Haiping Liu, Qian Zhao, Lijing Lin, Jingyuan Sun, Hongpeng Zhou
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-07
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 3.7695909532869996
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.06659v1
- PDF: https://arxiv.org/pdf/2608.06659v1
- Local PDF: pdf/2026-08-11_01_CellWorld_ From Gene-Level Reconstruction to Latent Cell Prediction in Spatial Transcriptomics Foundation Models.pdf

This paper shows that latent-space predictive pretraining can provide a scalable route to foundation models for spatial transcriptomics. Existing spatial transcriptomics foundation models primarily reconstruct masked gene identities or expression values, potentially encouraging the reproduction of assay-specific technical variation and limiting representation transferability. To avoid directly reconstructing such variation, we shift the prediction target from observed gene measurements to latent cell representations and introduce CellWorld, which predicts the latent representations of masked cells from visible spatial context and a limited partial-expression hint. We pretrain four CellWorld variants, spanning 5.74M to 94.56M trainable parameters, on a corpus of 46 million human cells. Our controlled scaling experiments show that performance improves with model capacity, particularly on spatial tasks, while spatial transfer depends more on sufficient optimization and broad biological source diversity than on cell count alone. Across four held-out datasets, even CellWorld-Small, with 5.74M trainable parameters, outperforms every baseline on all 11 linear-probe benchmarks and all seven fine-tuned spatial benchmarks. Most notably, a frozen CellWorld-Large pretrained on only 5\% of the corpus with broad biological source coverage outperforms every fully fine-tuned baseline across all seven spatial benchmarks. Code is available at https://github.com/UoM-HealthAI/CellWorld.

## 2. Towards Multi-Label Graph Foundation Models: from Single-Vector Representation Learning to Multi-Semantic Basis Learning

- Authors: Dongxiao He, Jiayu Zhang, Jitao Zhao, Yi Wang, Di Jin
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-31
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 3.6831882883303346
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.06394v1
- PDF: https://arxiv.org/pdf/2608.06394v1
- Local PDF: pdf/2026-08-11_02_Towards Multi-Label Graph Foundation Models_ from Single-Vector Representation Learning to Multi-Semantic Basis Learning.pdf

Multi-label node classification is an important yet challenging task in graph learning, where nodes exhibit multiple semantics simultaneously. Existing methods for multi-label node classification can effectively model multiple labels, while only considering in-domain scenarios where the model needs to be trained and tested within the same graph domain, resulting in limited cross-domain generalization. Recently, Graph Foundation Models (GFMs) have emerged as a promising paradigm for learning transferable graph representations across diverse graph domains and downstream tasks. However, existing GFMs are built upon single-label assumption, where all nodes are arbitrarily regarded as containing only one class of semantic and embedded into a single representation. For multi-label nodes, such a representation essentially approximates multiple semantics with a single point in the representation space, inevitably leading to semantic entanglement and making simultaneous discrimination of multiple labels difficult. To address these limitations, we propose a Multi-Semantic Basis Graph Foundation Model (MSB-GFM), a framework for cross-domain multi-label node classification. Specifically, we introduce a multi-semantic basis representation learning paradigm that models each multi-label node as an adaptive composition of semantic bases, thereby enabling flexible representational capacity for modeling multiple semantics. Furthermore, we develop a semantic-structure dual-channel architecture with domain adversarial training for effective cross-domain knowledge transfer. Extensive experiments demonstrate the effectiveness of our model.

## 3. Interpretable Unsupervised Community Detection with LLM-Symbolized Structured Processes

- Authors: Aoting Zeng, Kai Wang, Jianwei Wang, Yuxiang Sun, Yizhang He, Wenjie Zhang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-02
- DOI: Unavailable
- Categories: cs.AI, cs.LG
- Relevance: 3.6754150456903
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.06402v1
- PDF: https://arxiv.org/pdf/2608.06402v1
- Local PDF: pdf/2026-08-11_03_Interpretable Unsupervised Community Detection with LLM-Symbolized Structured Processes.pdf

Community detection is a fundamental task in graph analytics that aims to identify cohesive groups of entities with similar behaviors or interests. Classic objective-driven methods struggle with complex graph structures, while deep-learning approaches improve performance at the expense of interpretability and rely on labeled data and training. Large language models (LLMs), with strong reasoning capabilities and world knowledge, are promising for interpretable, label-free community detection. To leverage these strengths, we propose LUCID, an LLM-guided, interpretable, training-free, and unsupervised community detection method. Inspired by phase-transition kinetics in natural systems, where complex structures emerge through initialization, merging, refinement, and selection, LUCID is designed as a four-stage pipeline. Within this pipeline, the LLM induces formal rules that translate implicit knowledge into explicit and interpretable logical structures. Specifically, (1) the Local-View Community Initialization stage encodes local graph structures using k-ego contexts and unsupervised node roles; (2) the Multi-factor Community Merge stage uses LLM-induced rules to iteratively merge local communities; (3) the Multi-grain Community Refinement stage applies LLM-induced coarse-to-fine rules in parallel to reduce boundary noise; and (4) the Global-view Community Selection stage identifies high-quality communities based on topological compactness and boundary clarity. Extensive experiments on real-world datasets demonstrate that LUCID, as an unsupervised approach, achieves state-of-the-art performance and consistently outperforms leading unsupervised and semi-supervised baselines.

## 4. MolBioKG: Grounding Out-of-Graph Molecules in Biomedical Knowledge Graphs via Multi-Resolution Structural Anchoring

- Authors: Yiming Zhang, Hikaru Shindo, Shuan Chen, Kaushalya Madhawa, Jun Jin Choong, Yuna Oikawa, Takashi Fujiwara, Keisuke Ozawa
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-07
- DOI: Unavailable
- Categories: cs.AI, cs.LG
- Relevance: 3.6195475500745196
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.06713v1
- PDF: https://arxiv.org/pdf/2608.06713v1
- Local PDF: pdf/2026-08-11_04_MolBioKG_ Grounding Out-of-Graph Molecules in Biomedical Knowledge Graphs via Multi-Resolution Structural Anchoring.pdf

Biomedical knowledge graphs (KGs) accelerate drug discovery, but standard pipelines assume query molecules already exist as graph entities, leaving unregistered molecules disconnected. We address this cold-start challenge, termed the out-of-graph molecule problem, by introducing MolBioKG. This two-layer system grounds unseen molecules in biomedical evidence via multi-resolution structural anchoring. It connects an index of 2.74 million molecules (represented by scaffolds, fragments, functional groups, and fingerprints) to a 9.6-million-edge KG. Given only a SMILES string, MolBioKG retrieves structurally related graph entities and traverses their biomedical neighborhoods without task-specific training. It features two inference mechanisms: static multi-anchor retrieval using Reciprocal Rank Fusion, and Adapt-KG, a tool-using LLM policy for adaptive traversal. Evaluated across in-graph link recovery, complex multi-hop reasoning, and out-of-graph generalization, MolBioKG outperforms strong baselines. Notably, it raises Hits@10 from 0.585 to 0.876 in multi-hop reasoning and out-of-graph target recall from 0.145 to 0.269, all while ensuring predictions retain traceable structural anchors and source-attributed KG evidence.

## 5. Control-Anchored Residual Flow Matching Conditioned on Gene Geometry for Virtual Cell Perturbation Modeling

- Authors: Quanquan Li, Yihe Chi, Liuyang Song, Hongbo Zhang, Jingyu Li, Xidong Xi, Conghua Wei, Yijie Sun, Yu Chen, Xin Liu, Qi Hu, Jing Ke, Guitao Cao
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-07
- DOI: Unavailable
- Categories: q-bio.MN, cs.AI
- Relevance: 3.4767606267688715
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.06824v1
- PDF: https://arxiv.org/pdf/2608.06824v1
- Local PDF: pdf/2026-08-11_05_Control-Anchored Residual Flow Matching Conditioned on Gene Geometry for Virtual Cell Perturbation Modeling.pdf

A central task in virtual cell modeling is predicting single-cell transcriptional responses to unseen genetic perturbations and drug combinations, and biological networks provide valuable priors on gene relationships. Existing graph-based models commonly use the same network to structure gene representations and mediate intergene interactions, thereby implicitly treating stable associations as perturbation-response pathways. Gene Ontology and control-derived coexpression networks encode relatively stable relationships rather than intervention-specific response directions or magnitudes. We therefore propose GeneGeoFlow, which conditions a control-anchored residual flow on gene-wise geometry derived from biological networks to learn intervention-specific transcriptional responses. GeneGeoFlow derives multi-scale spectral coordinates from Gene Ontology and control-derived coexpression networks. A perturbation-conditioned, gene-wise gating module selects relevant structural scales and network sources, yielding intervention-specific gene geometry. The resulting geometry conditions a control-anchored residual flow without explicitly propagating target-derived signals along the graph. Condition-wise optimal transport couples unpaired control and perturbed populations for training, while a Delta-correlation objective aligns the predicted and observed condition-level expression-shift directions. GeneGeoFlow achieves Pearson Delta scores of 0.8979 on the Norman additive benchmark and 0.9088 on five held-out drug combinations in the fixed ComboSciPlex test split. These results support perturbation-conditioned gene geometry as an effective structural prior for intervention-specific response prediction, without conflating stable gene relationships with response propagation.

## 6. FUSE: Feature-Wise Unified Specialization with Cross-Column Exchange for Mixed-Type Tabular Flow Matching

- Authors: Suman Cha, Seongchan Lee, Dohyun Ko, Hyunjoong Kim
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-07
- DOI: Unavailable
- Categories: cs.LG, cs.AI
- Relevance: 3.318562381970044
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.07294v1
- PDF: https://arxiv.org/pdf/2608.07294v1
- Local PDF: pdf/2026-08-11_06_FUSE_ Feature-Wise Unified Specialization with Cross-Column Exchange for Mixed-Type Tabular Flow Matching.pdf

Generating mixed-type tabular data requires jointly modeling diverse feature distributions and their complex cross-column dependencies. Variational flow matching handles distinct endpoints via factorized distributions, yet leaves feature-specific processing and cross-column interactions implicit within a shared backbone. We introduce Feature-wise Unified Specialization with cross-column Exchange (FUSE) to explicitly separate these roles. FUSE applies separate adaptive mixture modules to numerical and categorical features, allowing each feature to combine shared specialized subnetworks, while joint attention preserves information exchange across all columns. We also characterize the excess population risk from restricted conditioning contexts and bound the continuous Wasserstein generation error by endpoint-prediction risk. Comprehensive experiments on eight tabular datasets demonstrate that FUSE achieves strong and consistent performance across distributional fidelity and downstream utility metrics.

## 7. Representation-driven Endoscopic Visual Embedding Alignment for Latent Generation

- Authors: Francisco Caetano, Tim J. M. Jaspers, Haiko Middeljans, Martijn R. Jong, Rixta A. H. van Eijck van Heslinga, Floor Slooter, Albert J. de Groof, Jacques J. Bergman, Peter H. N. De With, Fons van der Sommen
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-07
- DOI: Unavailable
- Categories: cs.CV, cs.AI
- Relevance: 3.2429150843688586
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.07176v1
- PDF: https://arxiv.org/pdf/2608.07176v1
- Local PDF: pdf/2026-08-11_07_Representation-driven Endoscopic Visual Embedding Alignment for Latent Generation.pdf

Developing foundation generative models for endoscopy is limited by the gap between natural and clinical images and the computational cost of training large Diffusion Transformers. Although representation alignment has improved efficiency in general computer vision, its role within the highly specialized endoscopic image space remains unclear. We introduce REVEAL (Representation-driven Endoscopic Visual Embedding Alignment), the largest generative foundation model for endoscopy to date, trained on GastroNet-5M (GN-5M), a multicenter dataset of 5 million endoscopic frames. Instead of depending on out-of-domain priors, REVEAL employs encoders pretrained directly on the endoscopic distribution to align diffusion latents with domain-specific visual features, preserving fine textures and intricate anatomical structures. Beyond image generation, REVEAL also serves as a powerful feature extractor; in multiple benchmarks, it delivers performance that is competitive with, and in several cases exceeds, endoscopic foundation models such as EndoViT and Endo-FM, specifically tuned for classification tasks, while demonstrating strong representation robustness under realistic imaging corruptions. REVEAL produces high-fidelity images and maintains robust structural coherence in latent-space edits such as inpainting and outpainting. This high-capacity backbone lowers the computational threshold for building specialized clinical tools, offering an open, versatile foundation for conditional synthesis, segmentation, and out-of-distribution detection in future intelligent gastroenterology systems.

## 8. SCALE: Scientific Concept Aggregation via LLMs and Embeddings for Fine-Grained Taxonomy Extension

- Authors: Daniele Raimondi, Feichi Lu, Oliver Grun, Mariia Eremina, Andrea Perlato
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-07
- DOI: Unavailable
- Categories: cs.DL, cs.AI
- Relevance: 3.1980328924941306
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.07254v1
- PDF: https://arxiv.org/pdf/2608.07254v1
- Local PDF: pdf/2026-08-11_08_SCALE_ Scientific Concept Aggregation via LLMs and Embeddings for Fine-Grained Taxonomy Extension.pdf

The increasing specialization of scientific research challenges existing classification systems, which provide effective representations of broad disciplines and research topics but often fail to capture the fine-grained conceptual structure of contemporary science. Author keywords offer greater specificity, but their fragmentation, redundancy, and terminological variability limit their use as stable units of knowledge organization. We introduce SCALE (Scientific Concept Aggregation via LLMs and Embeddings), a framework that extends the OpenAlex taxonomy with a new level of scientific Concepts below Topics. Rather than treating keywords as isolated descriptors, SCALE organizes semantically related terms into coherent and interpretable conceptual units and integrates them within the existing disciplinary hierarchy. The framework combines scientific text embeddings, large language models, and graph-based community detection to construct this additional layer at scale. The resulting taxonomy enables scientific literature to be read through an intermediate conceptual level between broad research topics and individual documents. This perspective provides a more detailed representation of how scientific knowledge is structured, specialized, and connected across disciplines. By transforming heterogeneous author terminology into reusable hierarchical units, SCALE offers a foundation for fine-grained scholarly classification, scientometric analysis, research monitoring, and future ontology development.

## 9. RoRA: Role-Oriented Regional Allocation for Visual Token Pruning in MLLMs

- Authors: Qiyanhui Lu, Han Wu, Rongjian Xu, Tingzhang Luo, Cheng Fan, Xinghao Chen, Minjing Dong, Jufeng Yang, Jianyuan Guo
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-07
- DOI: Unavailable
- Categories: cs.CV, cs.AI
- Relevance: 3.1972933595176634
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.07088v1
- PDF: https://arxiv.org/pdf/2608.07088v1
- Local PDF: pdf/2026-08-11_09_RoRA_ Role-Oriented Regional Allocation for Visual Token Pruning in MLLMs.pdf

Multimodal large language models (MLLMs) encode images as long visual token sequences, making prefilling and KV-cache storage expensive. Existing training-free pruning methods select tokens by importance, diversity, or spatial coverage, but treat retained tokens as interchangeable and do not explicitly track which object-related regions are already covered. We present RoRA, a training-free framework that casts visual token pruning as role-oriented regional evidence allocation. Given a fixed budget, RoRA partitions tokens into a protected semantic core, complementary context, and fine-grained detail. It first calibrates text-conditioned attention with a positional prior and a prompt-calibrated object prior, then builds Attention-Anchored Regions (AARs) from high-confidence anchors as lightweight proxies for covered object support. Context is explored mainly outside AARs, while a small AAR-guided budget restores local detail; pairwise similarity is used only for context-stage redundancy filtering. Under matched budgets, RoRA consistently outperforms strong training-free baselines across LLaVA and Qwen-VL families, retaining most of the unpruned accuracy even at aggressive pruning ratios, e.g., 96.5% of full performance at 88.9% pruning on LLaVA-1.5, and improving over D2Pruner by about 5% on Qwen3-VL at 75-90% pruning. At a 66.7% pruning ratio, RoRA requires only 0.7 ms for token selection and reduces end-to-end inference time by 24.6%, corresponding to a 1.33x speedup over unpruned inference on an NVIDIA H800.

## 10. Fluid-DiT: Graph-Free Diffusion Transformers for Fluid Flow Simulations Learning

- Authors: Shentong Mo, Guolin Ke
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-07
- DOI: Unavailable
- Categories: cs.LG, cs.AI, cs.CE
- Relevance: 3.1927308784132222
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.07161v1
- PDF: https://arxiv.org/pdf/2608.07161v1
- Local PDF: pdf/2026-08-11_10_Fluid-DiT_ Graph-Free Diffusion Transformers for Fluid Flow Simulations Learning.pdf

Simulating complex fluid flows requires capturing full equilibrium distributions rather than just mean trajectories, yet high-fidelity solvers remain computationally prohibitive. Recent advances, such as Diffusion Graph Networks (DGNs), have combined diffusion models with graph neural networks to sample equilibrium states directly from unstructured meshes, enabling distributional accuracy even from short simulations. However, graph-based diffusion approaches suffer from hand-crafted architectural constraints, limited receptive fields in message passing, and costly multi-scale designs, which restrict scalability to larger and more complex domains. We propose Fluid-DiT, a Graph-Free Diffusion Transformer that replaces graph message passing with attention-based denoising, eliminating explicit graph design while preserving the ability to model distributions of chaotic flows. Our framework introduces a latent-space formulation that disentangles geometric fidelity from distributional learning, reducing high-frequency artifacts and accelerating sampling. By leveraging the transformer's global receptive field, Fluid-DiT naturally captures both local flow structures and long-range correlations without requiring hierarchical graph coarsening. On canonical benchmarks including laminar cylinder wakes, ellipse-flow systems, and turbulent 3D wing experiments, Fluid-DiT consistently outperforms graph-based diffusion baselines in both sample quality and distributional accuracy, achieving higher $R^2$ correlations and lower Wasserstein distances. Moreover, it generalizes robustly from short, incomplete trajectories to unseen Reynolds numbers and geometries, demonstrating strong scalability.

## 11. GPTKB 2.0: Browsing, Querying, and Auditing a Disambiguated LLM-Derived Knowledge Base

- Authors: Yujia Hu, Tuan-Phong Nguyen, Simon Razniewski
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-07
- DOI: Unavailable
- Categories: cs.CL, cs.AI, cs.DB
- Relevance: 3.1335926297027203
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.06992v1
- PDF: https://arxiv.org/pdf/2608.06992v1
- Local PDF: pdf/2026-08-11_11_GPTKB 2.0_ Browsing, Querying, and Auditing a Disambiguated LLM-Derived Knowledge Base.pdf

We present a web demo for exploring a large-scale disambiguated knowledge base (KB) materialized from a large language model (LLM). GPTKB 2.0 contains 38.4M triples over 1.6M canonical entities, together with 207.6K consolidated relations and 66K consolidated classes. Unlike prior LLM-derived knowledge bases that largely identify entities by surface strings, GPTKB 2.0 performs context-guided disambiguation during recursive KB construction, separating homonyms and merging synonymous mentions as facts are elicited. The demo makes this process inspectable: users can browse entities, follow links across the KB, and audit the provenance of individual facts, including surface forms, candidate matches, source triples, and disambiguation decisions. The interface further supports structured SPARQL queries, natural-language questions translated to SPARQL, and entity linking from user-provided text to canonical GPTKB 2.0 entries. GPTKB 2.0 is available at https://gptkb.org/, with the full KB downloadable for offline use.

## 12. An Agentic Hybrid Top-Down and Bottom-Up Approach to Knowledge Graph Generation

- Authors: Emma Jouffroy, Warren Jouanneau, Marc Palyart
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-07
- DOI: Unavailable
- Categories: cs.CL, cs.AI
- Relevance: 3.1069694906376806
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.07023v1
- PDF: https://arxiv.org/pdf/2608.07023v1
- Local PDF: pdf/2026-08-11_12_An Agentic Hybrid Top-Down and Bottom-Up Approach to Knowledge Graph Generation.pdf

Organizing thousands of unstandardized, multilingual expertise declarations is a persistent challenge for Human Resources (HR) platforms, directly impacting downstream tasks like accurate talent matching. To address this, we propose a hybrid knowledge graph generation pipeline that grounds a Large Language Model (LLM) in the Wikidata multilingual Knowledge Graph (KG) while employing an agentic reflexion pattern to synthesize emerging concepts and their associated metadata. Unlike rigid top-down methods or fragmented bottom-up approaches, our system anchors recognized concepts to stable Knowledge Graph entities while dynamically creating new nodes and relational metadata for unrecognized skills. Executed across five stages, entity reconciliation, multilingual canonicalization, active curation, deduplication, and the iterative recovery of unmapped concepts, the system autonomously adapts to rapidly evolving, noisy skill mentions across five European languages. Ultimately, this pipeline provides a highly scalable, explicable, and self-healing framework for generating a comprehensive skills knowledge graph, from which a structured taxonomy is derived, using unstructured, noisy text.

## 13. Mind the Gap: A Dual Knowledge Graph Framework for Unified Multi-task User Intent Inference

- Authors: Tzu-Cheng Peng, Chien Chin Chen, Chih-Hao Ku, Yung-Chun Chang
- Source: arxiv
- Venue type: preprint
- Journal: Proceedings of the Pacific Asia Conference on Information Systems (PACIS 2026), Paper 12, 2026
- Publication status: preprint
- Publication date: 2026-08-07
- DOI: Unavailable
- Categories: cs.AI, cs.CL
- Relevance: 3.1032906855561073
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.06752v1
- PDF: https://arxiv.org/pdf/2608.06752v1
- Local PDF: pdf/2026-08-11_13_Mind the Gap_ A Dual Knowledge Graph Framework for Unified Multi-task User Intent Inference.pdf

This paper proposes DKG-MTI, a dual knowledge graph framework for unified multi-task user intent inference from online travel reviews. Existing approaches often rely on hierarchical pipelines that suffer from error propagation or retrieval methods that ignore structural relationships in domain knowledge. To address these limitations, we introduce an inference-only knowledge augmentation framework that dynamically constructs a User-Specific Intent Knowledge Graph from each review and aligns it with a Global Hotel Knowledge Graph through structure-aware semantic smoothing. The aligned knowledge is combined with the original review and processed by a large language model to simultaneously predict aspect ratings and generate reverse user intent statements. Experiments on TripAdvisor reviews show that DKG-MTI consistently outperforms strong LLM and retrieval-based baselines in both classification and intent generation tasks, demonstrating the effectiveness of structure-aware knowledge alignment for scalable and explainable intent inference.

## 14. Geo-Spatial Concept Probing of Large Language Models: Abstraction, Compositionality, and Grounding

- Authors: Karim Radouane, Jose G Moreno, Lynda Tamine
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-07
- DOI: Unavailable
- Categories: cs.CL, cs.AI, cs.IR, cs.LG
- Relevance: 3.1020322010658132
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.07353v1
- PDF: https://arxiv.org/pdf/2608.07353v1
- Local PDF: pdf/2026-08-11_14_Geo-Spatial Concept Probing of Large Language Models_ Abstraction, Compositionality, and Grounding.pdf

Understanding concepts is fundamental to generalization. Despite their impressive performance on a wide range of tasks, Large Language Models (LLMs) still struggle with genuine concept understanding. Prior work has evaluated conceptual understanding in LLMs using natural-language benchmarks or narrowly scoped synthetic tasks, but these settings often conflate multiple skills or lack precise control over the underlying concepts and their properties. To support controlled probing of concepts in LLMs, we design tests on their core properties: abstraction, compositionality, and groundness. We set up a concept-centric benchmark, targeting spatial concepts such as direction, distance, topology, and their compositions, and use question answering tasks serving as a proxy. We conduct extensive experiments across multiple LLM architectures and training regimes to analyze how model scale and design impact conceptual understanding. The results reveal clear limitations in current LLMs and provide insights into the factors shaping their ability to acquire and compose structured concepts. Our findings shed light on how concept-based LLMs can be redesigned for improved information access and knowledge management. The code will be available at https://github.com/rd20karim/concept-probing.

## 15. Every Cache Entry Earns Its Place: Global Allocation of Resolution and Coverage for KV Cache Compression

- Authors: Haolin Tian, Yuzhe Liu, Tonghan Wang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-07
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.023124523540597
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.07001v1
- PDF: https://arxiv.org/pdf/2608.07001v1
- Local PDF: pdf/2026-08-11_15_Every Cache Entry Earns Its Place_ Global Allocation of Resolution and Coverage for KV Cache Compression.pdf

As large language models (LLMs) process increasingly long contexts, KV cache storage and repeated access have become a major bottleneck. Existing KV cache compression methods rely on predefined, fixed compression rules and are typically developed around either token eviction or merging. As a result, cache resources can neither flow freely across layers, heads, and context slots, nor be jointly allocated to balance local resolution and information coverage. Therefore, we propose GraceKV, a global approach for the allocation of resolution and coverage in KV cache compression, and formulate the compression process as a global resource allocation problem under a fixed cache budget. GraceKV treats each layer-KV head-slot combination as an atomic unit and builds a prototype tree. Leaf nodes correspond to token-level KV entries, while each internal node uses a single prototype to compress the KV space covered by its children. A set of non-overlapping nodes in the tree forms the representation of an atomic unit. Adding the root of a new tree expands information coverage, whereas splitting a selected node improves local resolution. All candidate actions compete globally for a shared cache budget. Finally, the nodes retained across all trees form the compressed KV cache. This process adaptively determines the allocation of cache resources among atomic units globally and the balance between resolution and coverage. GraceKV requires no additional training, and the entire compression and inference process is performed on the GPU. Systematic experiments across diverse long-context tasks and compression ratios show that GraceKV ranks first in 24 of 32 settings and remains robust up to 128-fold compression. These results validate the effectiveness of global budget allocation in coordinating information coverage and local resolution.

## 16. AgentPatch: Coarse-to-Fine Weak-Task Repair for Merging Agentic Multimodal Large Language Models

- Authors: Zibo Shao, Baochen Xiong, Chengdong Xu, Linhui Xiao, Kaichen Li, Haoran Gong, Yan Li, Yaguang Song, Xiaoshan Yang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-07
- DOI: Unavailable
- Categories: cs.AI, cs.CV
- Relevance: 2.9776013225381464
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.06699v1
- PDF: https://arxiv.org/pdf/2608.06699v1
- Local PDF: pdf/2026-08-11_16_AgentPatch_ Coarse-to-Fine Weak-Task Repair for Merging Agentic Multimodal Large Language Models.pdf

Agentic multimodal large language models (MLLMs) extend multimodal perception and reasoning with planning, tool use, and interaction in dynamic environments. Yet current models are specialized for particular tools or environments, complicating consolidation into a single generalist. We formulate Agentic MLLM Merging and identify two challenges: asymmetric capability preservation, whereby capabilities with different interaction complexity are retained unevenly, producing weak tasks after merging, and behavior-critical forgetting, whereby losing decisive actions can derail long-horizon execution. We propose AgentPatch, a training-free coarse-to-fine repair framework. It selects a stable merged backbone, restores diluted weak-task-specific signals through Weak-Task Unique Residual Recovery, and applies an Agent-Guided Behavior-Critical Patch that recovers decisive behaviors under explicit capability protection. AgentPatch produces a single static checkpoint without routing or ensembles. Experiments across six agentic and multimodal benchmarks show that AgentPatch improves diverse merged backbones, alleviates weak-task degradation, and better balances weak-task recovery with the preservation of complementary search and agentic visual processing capabilities. Code is available at https://github.com/ziboshao/AgentPatch.

## 17. EntropyMoE: Entropy-Aware Sparse Expert Routing for Tokenizer-Free LLMs

- Authors: Bo Liu, Muxuab Yu, Yu Zhang, Pengfei Gao, Yongping Zhang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-31
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 2.9719500495953683
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.06398v1
- PDF: https://arxiv.org/pdf/2608.06398v1
- Local PDF: pdf/2026-08-11_17_EntropyMoE_ Entropy-Aware Sparse Expert Routing for Tokenizer-Free LLMs.pdf

Recent byte-level large language models (LLMs) have made tokenizer-free modeling increasingly competitive by grouping bytes into dynamically sized patches. However, existing byte-patch architectures still apply the same dense feed-forward computation to every patch. This uniform computation cannot adapt model capacity to variations in patch semantics and granularity. We address this limitation with EntropyMoE, a Mixture-of-Experts (MoE) architecture designed for dynamic byte patches. EntropyMoE replaces the dense feed-forward modules in the global patch Transformer with Top-K expert layers. Each dynamic patch serves as the basic unit of expert routing, and its byte coverage determines its contribution to workload accounting. The router selects experts directly from patch entropy, using the same granularity signal that underlies dynamic patch construction to organize sparse computation. Patch entropy and length jointly define the feature space for regulating expert specialization. Experiments show that EntropyMoE achieves the lowest held-out bits-per-byte among matched dense and sparse baselines while maintaining comparable downstream accuracy. These results establish patch entropy as an effective routing coordinate for sparse conditional computation and extend Mixture-of-Experts modeling beyond tokenizer-based representations.

## 18. GeoBenchLLM: A Comprehensive Benchmark for Evaluating LLMs on Geo-Related Tasks

- Authors: Rodrigo Ferreira Rodrigues, Karim Radouane, Jose G Moreno, Lynda Tamine
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-07
- DOI: Unavailable
- Categories: cs.AI, cs.CL, cs.IR, cs.LG
- Relevance: 2.9663183939021027
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.07411v1
- PDF: https://arxiv.org/pdf/2608.07411v1
- Local PDF: pdf/2026-08-11_18_GeoBenchLLM_ A Comprehensive Benchmark for Evaluating LLMs on Geo-Related Tasks.pdf

In the context of geodata, existing Large Language Models have often been studied in a homogeneous setting, which has considerably limited insights into their generalization capabilities. In this paper, we present \benchName, a comprehensive benchmark for probing LLMs on geo-related tasks. We leverage a careful selection of twelve publicly available datasets from diverse geo-related tasks and domains, and evaluate a set of LLMs on geo-spatial and temporal understanding using our benchmark. Our results show that reasoning and size have a strong impact on overall performance. GeoBenchLLM is publicly available at https://github.com/Rfr2003/GeoBenchLLM.

## 19. ArchEGraph: A Large-Scale Graph Dataset for Geometry-Topology-Physics Aligned Building Energy Modeling

- Authors: Yihui Li, Yihui Chen, Kaidi Zha, Xiaoyue Yan, Zhexuan Yu, Shiqi Dai, Jun Xiao, Jun Yin, Ramon Elias Weber, Borong Lin
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-07
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 2.9426634258634534
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.06772v1
- PDF: https://arxiv.org/pdf/2608.06772v1
- Local PDF: pdf/2026-08-11_19_ArchEGraph_ A Large-Scale Graph Dataset for Geometry-Topology-Physics Aligned Building Energy Modeling.pdf

Accurate estimation of building energy use is essential for achieving carbon neutral and sustainable buildings. To better understand the influence of design decisions on building energy use and calibrate machine learning models that can give architects and engineers rapid design feedback, large-scale datasets are needed that explicitly map building geometry to performance. We present ArchEGraph, a large-scale benchmark dataset that represents buildings as heterogeneous graphs with aligned geometry, topology, weather, and zone-level thermal loads. The dataset contains 5,481 buildings and 49,326 validated building-weather simulation cases. In total, it includes over 133,000 space nodes and 1.44 million face nodes, reflecting substantial geometric and topological complexity. Based on ArchEGraph, we define two benchmark tasks: (i) graph reconstruction from polygonal meshes, aiming to recover topological structure from geometric representations; and (ii) topology-informed load prediction, which leverages graph structure and temporal weather conditions to forecast zone-level response time series. We further introduce standardized evaluation protocols for both tasks and conduct cross-building and cross-climate generalization experiments to assess model robustness. ArchEGraph provides a unified testbed for studying geometry-topology-physics coupling in building energy modeling, enabling the development and evaluation of scalable and generalizable surrogate models.

## 20. Debias in Text, Believe Your Eyes: Text-Anchored Cross-Modal Transfer for Visual Counter-Commonsense Reasoning

- Authors: Chen Ling, Hanqian Li, Dongnan Liu, Keyu Qian, Jungang Li, Xinglong liu, Shiyi Wang, Xin Dong, Pengcheng Zhu, Wei Zhou, Linjian Mo, Nai Ding
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-07
- DOI: Unavailable
- Categories: cs.CV, cs.AI
- Relevance: 2.9325398562470752
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.06938v1
- PDF: https://arxiv.org/pdf/2608.06938v1
- Local PDF: pdf/2026-08-11_20_Debias in Text, Believe Your Eyes_ Text-Anchored Cross-Modal Transfer for Visual Counter-Commonsense Reasoning.pdf

The visual reasoning ability of multimodal large language models (MLLMs) is crucial for downstream applications, particularly counter-commonsense reasoning, which requires models to reason beyond common assumptions. Recent studies mainly improve visual counter-commonsense reasoning by enhancing visual inputs, following the assumption that failures originate from insufficient visual grounding. However, our empirical analysis reveals that the bottleneck is not visual perception. MLLMs already capture the relevant visual evidence, and the correct answer exists in their decoding space. Instead, the shared language decoder resolves prior--evidence conflicts by favoring dominant language priors, especially for low-frequency factual scenarios. Motivated by this, we first propose a text-anchored data construction pipeline, whose core component, Fact-Frequency Distillation (FFD), estimates the prior strength of commonsense facts and distills verified counter-commonsense scenarios into a high-quality text corpus. Building upon this corpus, we introduce TACT, a text-anchored post-training framework that debiases the shared language decoder without requiring any visual training data. TACT routes evidence-following and prior-driven reasoning trajectories into different optimization stages, enabling the decoder to resolve prior--evidence conflicts. Across counter-commonsense visual benchmarks, TACT substantially improves visual reasoning while preserving general capabilities, demonstrating effective text-to-vision cross-modal transfer.

## 21. The Sparsity Whisperer

- Authors: Linghao Kong, Inimai Subramanian, Micah Adler, Dan Alistarh, Dan Gutfreund, Nir Shavit
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-06
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 2.920353914719022
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.06630v1
- PDF: https://arxiv.org/pdf/2608.06630v1
- Local PDF: pdf/2026-08-11_21_The Sparsity Whisperer.pdf

Pruning reduces the inference cost of large language models, but existing criteria primarily preserve large activations or reconstruct layer outputs. We argue that this overlooks a key computation performed by particularly sparsity-sensitive neurons in the MLP up and gate projections: separating similar inputs into dissimilar outputs. This suggests that effective pruning should preserve not only activations, but also the differences between outputs more broadly. We introduce a family of difference-informed pruning methods built upon this principle. Wisp is a first-order, update-free method that scores weights using input-difference norms, and Wisp+ refines this score neuronwise using the input pairs each neuron separates most strongly. Finally, Whisper is a second-order method that uses a lightly regularized difference Hessian as its reconstruction objective. Across Llama 2 and 3.1 models from 7B to 405B parameters, our second-order variant consistently improves over strong reconstruction-based baselines, while our update-free variants improve over activation-aware baselines, especially in constrained settings. The improvements over Wanda and SparseGPT extend to structured sparsity, downstream evaluations, and other model families. Augmenting stronger techniques such as RIA and ALPS with our difference-informed criteria yields further improvements, shifting the overall accuracy-runtime frontier outward at negligible additional cost. These results suggest that preserving output differences is a broadly useful and composable signal for post-training LLM sparsification.

## 22. Retrofitting Linear Attention into Diffusion Language Models

- Authors: Jinha Kim, Younghun Roh, Jaeyeon Kim
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-06
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 2.8467939005858782
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.06628v1
- PDF: https://arxiv.org/pdf/2608.06628v1
- Local PDF: pdf/2026-08-11_22_Retrofitting Linear Attention into Diffusion Language Models.pdf

Diffusion language models (dLLMs) offer a promising alternative to autoregressive models by accelerating inference through parallel decoding. Recent dLLMs commonly use blockwise semi-autoregressive decoding, generating blocks autoregressively while denoising tokens within each active block in parallel. However, despite KV caching, each denoising step still attends to all previous blocks, repeatedly incurring prefix-attention cost. Motivated by this bottleneck, we ask whether dLLM inference can be further accelerated by linearizing attention over previous blocks. We introduce block-hybrid attention, which retains exact softmax attention within the active denoising block while applying linear attention over previous blocks. We show that this hybrid attention can be retrofitted into a pretrained dLLM with minimal post-training: LLaDA-Hybrid replaces 6 of the 20 attention layers in LLaDA~2.1, a 16B open-source dLLM, largely following LoLCAT (Zhang et al, 2024). The conversion takes only approximately 60 hours while preserving benchmark performance: 72.0% vs. 75.6% on HumanEval, 63.0% vs. 57.7% on MBPP+, and 86.7% vs. 88.3% on CMATH. With a Triton implementation, LLaDA-Hybrid achieves up to $1.7\times$ higher decoding throughput and supports more concurrent requests before exhausting memory, showing that pretrained dLLMs can be efficiently linearized for faster inference. Our code is available at: https://github.com/Diuven/LLaDA-Hybrid.

## 23. Toward a Causal Data Management Ecosystem for Decision Making and Agentic AI

- Authors: Dazhuo Qiu, Yingli Zhou, Amedeo Pachera, Angela Bonifati, Andrea Mauri
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-07
- DOI: Unavailable
- Categories: cs.DB, cs.AI, eess.SY
- Relevance: 2.8444200550940058
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.07214v1
- PDF: https://arxiv.org/pdf/2608.07214v1
- Local PDF: pdf/2026-08-11_23_Toward a Causal Data Management Ecosystem for Decision Making and Agentic AI.pdf

Modern AI is no longer a single model but an ecosystem: classical ML predictors, deep and multimodal models, large language models, and agents, each trained and tuned over different data sources and each producing outputs at scale that become inputs to the others. Operating such an ecosystem is fundamentally a data integration problem - the knowledge it depends on is fragmented across dozens of heterogeneous, independently governed sources that must be reconciled and continually maintained. Yet integration alone is not enough. The predictions these systems make are shaped by many interacting factors, and the events, decisions, and variables that drive an outcome are routinely entangled with the ones that merely accompany it; treated as a basis for action, such correlational signals invite confounded decisions. This becomes acute once agents act autonomously: to be trustworthy and reliable, an agent must anticipate the consequences of its actions, not merely extrapolate from what has co-occurred before. Causal reasoning is what closes this gap, distinguishing the drivers of an outcome from its correlates, and enabling prescriptive and counterfactual analysis over the ecosystem's data. We therefore argue that the integrated ecosystem needs an explicit causal layer, and we propose to build it as a shared, persistent, queryable Causal World System (CWS).

## 24. Multi-Level Modeling of Large Language Model Inference Latency and Energy via Hybrid Analytical--Machine-Learning Predictors

- Authors: Saeid Shokoufa, Mohammad Erfan Sadeghi, Mehdi Kamal, Massoud Pedram
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-07
- DOI: Unavailable
- Categories: cs.LG, cs.AI
- Relevance: 2.8400682316095436
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.06723v1
- PDF: https://arxiv.org/pdf/2608.06723v1
- Local PDF: pdf/2026-08-11_24_Multi-Level Modeling of Large Language Model Inference Latency and Energy via Hybrid Analytical--Machine-Learning Predic.pdf

The rapid scaling of Large Language Models (LLMs) has significantly increased computational cost, energy consumption, and inference latency, making accurate estimation essential for sustainable artificial intelligence deployment and hardware-aware design. In this work, we introduce Hybrid Modeling for Energy and Latency of LLMs (HYMELL), a hybrid three-level framework for estimating LLM inference latency and energy by combining analytical modeling with machine learning (ML). HYMELL models LLM execution through a three-level hierarchy: analytical estimation of primitive operations, ML prediction of higher-level components, and an end-to-end model that captures system-level overheads across both prefill and decode phases. The framework supports diverse architectures, including dense and mixture-of-experts (MoE) feed-forward networks (FFNs), as well as multi-head attention (MHA) and grouped-query attention (GQA) mechanisms. Evaluated on an NVIDIA H100 graphics processing unit (GPU), HYMELL achieves high predictive accuracy; notably, for LLaMA 3 8B, it attains less than 5% error for both prefill and decode phases. By predicting execution costs directly from architectural parameters, it enables fast, hardware-free design space exploration and energy-efficient optimization.

## 25. Understanding Differentiable Embeddings Through Differential and Integral Geometry

- Authors: Xinyu Zhang, Klaus Mueller
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-07
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 2.814341024041029
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.06809v1
- PDF: https://arxiv.org/pdf/2608.06809v1
- Local PDF: pdf/2026-08-11_25_Understanding Differentiable Embeddings Through Differential and Integral Geometry.pdf

How can an analyst decide whether a nonlinear dimensionality reduction embedding can be trusted? Existing diagnostics provide only partial answers: projection glyphs characterize local sensitivity, map-continuity scores measure local conditioning, and transport-based analyses reveal path-dependent inconsistencies. However, these methods appear unrelated and provide no common framework for understanding when they agree or not. We show that they are all derived from a single geometric object induced by every differentiable embedding, whether defined implicitly through optimization or explicitly by a learned mapping. This framework provides two complementary geometric views of an embedding. The differential view explains local behavior: its first-order term recovers projection glyphs, while its second-order curvature quantifies how far their linear approximation remains reliable. The integral view follows the same geometry along high dimensional paths and determines whether an embedding depends only on the current state or also on the path taken to reach it. We further show that map-continuity is a prerequisite for the other analyses. The framework is theoretically complete for diagnostics derived from the embedding geometry, and we prove the integral view irreducible: no amount of local measurement at any number of points, to any order of derivative, reproduces what it detects. Classical rank-based metrics form a complementary class based on finite-scale neighborhood relationships. Experiments on synthetic and real datasets validate theoretical predictions, demonstrate accurate curvature-based trust estimates on single-cell embeddings, and show that the integral analysis distinguishes single-valued embeddings from path-dependent optimization-based embeddings in ways that existing pointwise diagnostics cannot.

## 26. MAXS: Meta-Adaptive Exploration with LLM Agents

- Authors: Jian Zhang, Zhiyuan Wang, Zhangqi Wang, Yu He, Haoran Luo, li Yuan, Lingling Zhang, Rui Mao, Qika Lin, Jun Liu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.7912066432502924
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.670/
- PDF: https://aclanthology.org/2026.findings-acl.670.pdf
- Local PDF: pdf/2026-08-11_26_MAXS_ Meta-Adaptive Exploration with LLM Agents.pdf

Large Language Model (LLM) Agents exhibit inherent reasoning abilities through the collaboration of multiple tools.However, during agent inference, existing methods often suffer from (i) locally myopic generation, due to the absence of lookahead, and (ii) trajectory instability, where minor early errors can escalate into divergent reasoning paths. These issues make it difficult to balance global effectiveness and computational efficiency. To address these two issues, we propose meta-adaptive exploration with LLM agents (MAXS)[ https://github.com/exoskeletonzj/MAXS ], a meta-adaptive reasoning framework based on LLM Agents that flexibly integrates tool execution and reasoning planning. MAXS employs a lookahead strategy to extend reasoning paths a few steps ahead, estimating the advantage value of tool usage, and combines step consistency variance and inter-step trend slopes to jointly select stable, consistent, and high-value reasoning steps. Additionally, we introduce a trajectory convergence mechanism that controls computational cost by halting further rollouts once path consistency is achieved, enabling a balance between resource efficiency and global effectiveness in multi-tool reasoning. We conduct extensive empirical studies across three base models (MiMo-VL-7B, Qwen2.5-VL-7B, Qwen2.5-VL-32B) and five datasets, demonstrating that MAXS consistently outperforms existing methods in both performance and inference efficiency. Further analysis confirms the effectiveness of our lookahead strategy and tool usage.

## 27. RecMem: Recurrence-based Memory Consolidation for Efficient and Effective Long-Running LLM Agents

- Authors: Zijie Dai, Shiyuan Deng, Sheng Guan, Yizhou Tian, Xin Yao, Xiao Yan, James Cheng
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.7881814454748657
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1619/
- PDF: https://aclanthology.org/2026.findings-acl.1619.pdf
- Local PDF: pdf/2026-08-11_27_RecMem_ Recurrence-based Memory Consolidation for Efficient and Effective Long-Running LLM Agents.pdf

Memory systems often organize user-agent interactions as retrievable external memory and are crucial for long-running agents by overcoming the limited context windows of LLMs. However, existing memory systems invoke LLMs to process every incoming interaction for memory extraction, and such an eager memory consolidation scheme leads to substantial token consumption. To tackle this problem, we propose RecMem by rethinking when memory consolidation should be conducted. RecMem stores incoming interactions in a subconscious memory layer and encode them using lightweight embedding models for retrieval. LLMs are only invoked to extract episodic and semantic memory when sustained recurrence are observed for semantically similar interactions. Such recurrence-based consolidation works because these interactions correspond to a semantic cluster with rich information and thus are worth extraction and summarization. To improve accuracy, RecMem also incorporates a semantic refinement mechanism that recovers the fine-grained facts omitted by memory extraction. Experiments show that RecMem reduces the memory construction token cost of three SOTA memory systems by up to 87% while exceeding their accuracy.

## 28. Knowledge Vector of Logical Reasoning in Large Language Models

- Authors: Zixuan Wang, Yuanyuan Lei
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.787864919368693
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.2021/
- PDF: https://aclanthology.org/2026.acl-long.2021.pdf
- Local PDF: pdf/2026-08-11_28_Knowledge Vector of Logical Reasoning in Large Language Models.pdf

Logical reasoning serves as a central capability in LLMs and includes three main forms: deductive, inductive, and abductive reasoning. In this work, we study the knowledge representations of these reasoning types in LLMs and analyze the correlations among them. Our analysis shows that each form of logical reasoning can be captured as a reasoning-specific knowledge vector in a linear representation space, yet these vectors are largely independent of each other. Motivated by cognitive science theory that these subforms of logical reasoning interact closely in the human brain, as well as our observation that the reasoning process for one type can benefit from the reasoning chain produced by another, we further propose to refine the knowledge representations of each reasoning type in LLMs to encourage complementarity between them. To this end, we design a complementary subspace-constrained refinement framework, which introduces a complementary loss that enables each reasoning vector to leverage auxiliary knowledge from the others, and a subspace constraint loss that prevents erasion of their unique characteristics. Through steering experiments along reasoning vectors, we find that refined vectors incorporating complementary knowledge yield consistent performance gains. We also conduct a mechanism-interpretability analysis of each reasoning vector, revealing insights into the shared and specific features of different reasoning in LLMs.

## 29. OMHBench: Benchmarking Balanced and Grounded Omni-Modal Multi-Hop Reasoning

- Authors: Seunghee Kim, Ingyu Bang, Seokgyu Jang, Changhyeon Kim, Sanghwan Bae, Jihun Choi, Richeng Xuan, Taeuk Kim
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.7871864397267867
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.911/
- PDF: https://aclanthology.org/2026.findings-acl.911.pdf
- Local PDF: pdf/2026-08-11_29_OMHBench_ Benchmarking Balanced and Grounded Omni-Modal Multi-Hop Reasoning.pdf

Multimodal Large Language Models (MLLMs) have increasingly supported omni-modal processing across text, vision, and speech. However, existing evaluation frameworks for such models suffer from critical limitations, including modality shortcuts and biased reasoning paths. To address these challenges, we propose OMHBench, a novel benchmark designed to rigorously evaluate omni-modal multi-hop reasoning. It consists of 6,144 questions with balanced reasoning paths that are jointly grounded across all three modalities. Extensive evaluation of 13 state-of-the-art models reveals that (1) a large performance gap exists between proprietary and open-source MLLMs and (2) even proprietary models exhibit high sensitivity to reasoning path variations, resulting in asymmetric omni-modal grounding. Notably, models struggle when processing the speech modality, underscoring the need for balanced, multi-hop evaluation of omni-modal intelligence.

## 30. Self-Guided Alignment: Adaptive Preference Sensing for Multi-Objective Generation

- Authors: Ning Wang, Zhanyang Liu, Taotao Zhou, Xinrui Zhang, Zongru Shao, Haojie Zhou
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.786853161973583
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.2184/
- PDF: https://aclanthology.org/2026.acl-long.2184.pdf
- Local PDF: pdf/2026-08-11_30_Self-Guided Alignment_ Adaptive Preference Sensing for Multi-Objective Generation.pdf

Aligning Large Language Models (LLMs) with diverse and potentially conflicting human values necessitates navigating complex multi-objective landscapes. However, existing prompt-conditioned approaches face a critical training-inference discrepancy: they rely on ground-truth scores during training while requiring manual user-specification at inference. We introduce prediction of implicit preferences to bridge this gap while reducing user burden. To this end, we propose Self-Guided Alignment (SGA), a framework that transforms passive reward dependency into an intrinsic adaptive sensing capability. It employs a dual-head architecture to unify preference internalization with conditional generation, enabling the model to learn a latent mapping between raw prompts and preference profiles. Through adaptive preference sensing, the model autonomously predicts the latent preference score to self-guide the generation, thereby eliminating the need for manual specification at inference. Extensive experiments across diverse model scales demonstrate that SGA often outperforms state-of-the-art baselines, achieving superior multi-objective trade-offs and improved preference alignment. Code is available at https://github.com/python-yyds/SGA .
