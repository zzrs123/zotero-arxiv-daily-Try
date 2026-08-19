# Paper Daily Reading - 2026-08-19

## 1. PaSTel: Anchoring Histology in Spatial Transcriptomics via Multi-Scale Hierarchical Bio-Prior Contrastive Pretraining

- Authors: Azim Dehghani Amirabad, Junchao Zhu, Pushpak Pati, Walid Abdelmoula, Tommaso Mansi, Rui Liao
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-14
- DOI: Unavailable
- Categories: cs.CV, cs.AI
- Relevance: 3.9653515052903914
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.14924v1
- PDF: https://arxiv.org/pdf/2608.14924v1
- Local PDF: pdf/2026-08-19_01_PaSTel_ Anchoring Histology in Spatial Transcriptomics via Multi-Scale Hierarchical Bio-Prior Contrastive Pretraining.pdf

Spatial transcriptomics (ST) links tissue morphology with molecular programs, motivating multimodal pretraining methods that align histology images with gene expression. However, existing approaches suffer from two key limitations: spatially informative gene selection is often dominated by ubiquitous housekeeping genes, leading to weakly discriminative representations, and independent spot-patch alignment fails to capture spatial dependencies that are critical for tissue organization. To address these challenges, we introduce PaSTel, a hierarchical multimodal pretraining framework that integrates biological priors at three levels. At the spot level, TF-IDF reweighting is used to identify spatially informative genes; at the functional level, curated KEGG pathways serve as anchors for encoding global biological semantics; and at the regional level, spatial clustering aggregates neighboring spots to model meso-scale tissue structure. Across multiple downstream tasks, PaSTel consistently outperforms existing vision and vision-omics encoders, demonstrating that incorporating multiscale biological priors yields more informative and transferable representations for spatial transcriptomics.

## 2. Path2ST: Hierarchical Cell-Tissue Grounded Cross-Modal Translation for Spatial Transcriptomics

- Authors: Ruochen Liu, Wei Lou
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-11
- DOI: Unavailable
- Categories: cs.CV, cs.AI, cs.CL
- Relevance: 3.619085402413776
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.14710v1
- PDF: https://arxiv.org/pdf/2608.14710v1
- Local PDF: pdf/2026-08-19_02_Path2ST_ Hierarchical Cell-Tissue Grounded Cross-Modal Translation for Spatial Transcriptomics.pdf

Predicting spatial gene expression from hematoxylin and eosin (H\&E)-stained images offers a cost-effective alternative to spatial transcriptomics (ST). However, existing methods treat H\&E images as generic visual inputs and ignore their intrinsic biological hierarchy, where spatially organized cell types collectively form functional tissue microenvironments that govern local gene expression programs. To bridge this gap, we formulate H\&E-to-ST prediction as a cross-modal semantic translation task and propose Path2ST, a hierarchically grounded autoregressive framework featuring three key components: (i) a Hierarchical Cell-Tissue Conditioning mechanism that fuses explicit and implicit cellular features with tissue-level semantic representations to construct hierarchical conditioning signals; (ii) a Scale-Adaptive Autoregressive Generation process over a hierarchical semantic vocabulary, enabling coarse-to-fine, biologically consistent expression synthesis; and (iii) SpectraLoss, a full-spectrum objective that jointly enforces ordinal fidelity, models transcriptional bursts, and aligns semantic structures with cell types. Extensive experiments on three datasets demonstrate state-of-the-art performance, validating that Path2ST generates highly accurate and spatially coherent transcriptomic profiles. The related code is released at https://github.com/RuochenLiu23/Path2ST.

## 3. A Unified Geometric Framework for Developmental Analysis of Spatial Transcriptomic Data

- Authors: Mary Chriselda Antony Oliver, Kaitlyn Hohmeier, Tuyen Tran, Alejandra Castillo, Caroline Moosmüller, Shiying Li
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-15
- DOI: Unavailable
- Categories: stat.ML, cs.LG, math.MG
- Relevance: 3.433571284445663
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.15306v1
- PDF: https://arxiv.org/pdf/2608.15306v1
- Local PDF: pdf/2026-08-19_03_A Unified Geometric Framework for Developmental Analysis of Spatial Transcriptomic Data.pdf

High-throughput single-cell and spatial transcriptomic technologies provide high-resolution snapshots of heterogeneous cellular states, but their destructive nature prevents repeated measurements of the same cells over time. Consequently, temporal and spatial dynamics must be inferred from independently sampled, unaligned cell populations, making it challenging to reconstruct developmental trajectories. Optimal transport (OT) offers a geometric framework for aligning cell populations and inferring developmental trajectories, but many existing approaches focus on modeling the evolution of distributions of cells in gene expression space rather than the relational structure encoded by gene expression networks. To address this limitation, we introduce a geometric framework for analyzing the spatiotemporal evolution of gene expression networks through embeddings in Gromov--Wasserstein (GW) space. By representing each developmental stage as a graph combining gene expression and spatial proximity, our approach enables comparisons of network structure across time, continuous interpolation between developmental stages via GW geodesics, and quantification of network-level changes using Ollivier-Ricci curvature. We evaluate our framework on a spatiotemporal transcriptomic \textit{Drosophila} dataset and show that GW geodesic interpolations reproduce main trends in curvature dynamics observed in empirical gene expression networks. Agreement with higher-order Co-Optimal Transport (COOT) distances, which jointly represent spatial and temporal information, further validates the framework and suggests that hypernetwork representations successfully record salient biological changes across time. In general, our approach provides a unified geometric approach to study dynamically evolving biological networks.

## 4. Noesis: Bidirectional Graph-RAG with Adaptive Parallelism and Cross-Knowledge-Base Semantic Discovery

- Authors: Nicola Cogotti
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-16
- DOI: 10.5281/zenodo.21874580
- Categories: cs.IR, cs.AI
- Relevance: 3.4297049536577933
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.15919v1
- PDF: https://arxiv.org/pdf/2608.15919v1
- Local PDF: pdf/2026-08-19_04_Noesis_ Bidirectional Graph-RAG with Adaptive Parallelism and Cross-Knowledge-Base Semantic Discovery.pdf

Retrieval-Augmented Generation over knowledge graphs (Graph-RAG) has emerged as a powerful paradigm for grounding large language models in domain-specific corpora. However, existing systems face persistent limitations: (1) static chunking fragments long documents, losing cross-section semantic connections; (2) ingestion pipelines do not scale adaptively; and (3) multi-domain deployments require either a monolithic knowledge base that dilutes retrieval precision or manual user routing. We present Noesis, a decoupled Graph-RAG architecture addressing these limitations through four algorithms: (a) Bidirectional Graph Traversal with a Graph-Feedback Context Resolver simulating human reading with degrading memory; (b) an AIMD Concurrency Controller adapted from TCP congestion control, achieving 23x speedup with zero OOM events; (c) Moesis, domain-aware selective quantization for MoE models achieving 6.3x speedup on 12 GB consumer GPUs; and (d) Mesh, cross-KB semantic routing with runtime structural discovery enabling small on-premises models to perform multi-hop cross-domain reasoning. On HotpotQA (1,000 questions), Noesis achieves 59.5 EM / 74.7 F1, surpassing GraphRAG by +27.8 EM while using a 35B on-premises model for graph construction rather than GPT-4o. Source text verification on a 193-page document confirms 90% precision on long-range causal edges inaccessible to chunk-independent extraction.

## 5. Celldega: Integrated Toolkit for Visualization and Analysis of Spatial Data

- Authors: Fernandez, N., Ishar, J., Wang, H., Saad, A. B., Lipinski, M., Farhi, S. L.
- Source: biorxiv
- Venue type: preprint
- Journal: biorxiv
- Publication status: preprint
- Publication date: 2026-08-18
- DOI: 10.64898/2026.08.13.744672
- Categories: bioinformatics
- Relevance: 3.41057190888659
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://www.biorxiv.org/content/10.64898/2026.08.13.744672v1.full.pdf
- PDF: https://www.biorxiv.org/content/10.64898/2026.08.13.744672v1.full.pdf
- Local PDF: Not downloaded

Spatial-transcriptomics integrates high-dimensional single-cell data with microscopy to reveal cellular states, communication, and tissue organization. Analyzing this data requires a combination of multi-modal data processing, high-dimensional data analysis, spatial analysis, and integrated visualization. However, computational analysis is increasingly becoming a bottleneck as approaches mature and dataset sizes increase. Additionally, visualization can be challenging as open-source visualization tools struggle to scale to large datasets (exceeding 1 billion transcripts), and commercial visualization tools are costly, closed source, and inflexible. We present Celldega, an open-source Python and JavaScript library for scalable, interactive visualization and analysis of spatial-omics data. Celldega integrates custom analyses, performs neighborhood analysis, implements an efficient visualization-specific file format, and enables interactive exploration in notebooks and web galleries. We demonstrate Celldega across multiple technologies, tissues, and datasets, including 3D reconstructions of the developing whole mouse head comprising over four million cells. Finally, we demonstrate how Celldega can be utilized throughout the entire lifecycle of spatial data analysis, from quality control to building a public shareable gallery.

## 6. RagGAD: Rationale-Aware Conditional Gaussian Mixture Normalizing Flow for Unsupervised Graph Anomaly Detection

- Authors: Junxin Lu, Jing Zhao, Shiliang Sun
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-17
- DOI: Unavailable
- Categories: cs.LG, cs.AI
- Relevance: 3.4093942094846703
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.16018v1
- PDF: https://arxiv.org/pdf/2608.16018v1
- Local PDF: pdf/2026-08-19_06_RagGAD_ Rationale-Aware Conditional Gaussian Mixture Normalizing Flow for Unsupervised Graph Anomaly Detection.pdf

Graph anomaly detection aims to identify nodes that deviate from normal behavioral patterns within graphs. However, existing methods largely rely on the homophily assumption, which makes it difficult to distinguish spurious affinities and to capture the diverse behaviors of normal nodes,limiting their robustness in complex real-world scenarios. To address this problem, we propose RagGAD, an unsupervised graph anomaly detection framework based on rationale-aware conditional Gaussian mixture normalizing flow. RagGAD introduces an adaptive rationale disentangler to disentangle stable rationales from spurious correlations within node interrelationships, and further decomposes stable rationales into robust and fragile components. The learned rationales capture underlying interaction patterns that characterize normal behaviors under varying conditions, while anomalies emerge as deviations associated with unstable or spurious correlations. To model the intricate distributions of normal and abnormal nodes, RagGAD integrates rationale-non-rationale Gaussian mixture modeling with a robust-fragile rationale mixture learning strategy. By mitigating spurious homophilic correlations and embracing the heterogeneity of normal patterns, RagGAD identifies anomalies as low-density regions within a structure-aware distribution space. Extensive experiments on multiple benchmark datasets demonstrate that RagGAD outperforms state-of-the-art methods.

## 7. The Trade-off Between Covariate Dependence and Latent Structure in Representation Learning

- Authors: Małgorzata Łazęcka, Ewa Szczurek
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-17
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.4062141988288626
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.16245v1
- PDF: https://arxiv.org/pdf/2608.16245v1
- Local PDF: pdf/2026-08-19_07_The Trade-off Between Covariate Dependence and Latent Structure in Representation Learning.pdf

Disentangled representation learning seeks latent representations whose indicidual dimensions each align with a distinct covariate. Unsupervised approaches typically target latent dimension independence, yet this gives no guarantee that the resulting dimensions align with semantically meaningful covariates. Supervised approaches structure the latent space using observed covariates, but under correlated covariates they cannot simultaneously control one-to-one latent-covariate alignment and latent independence. We introduce a unified, supervised framework that couples latent dimension-covariate dependence with constraints on the latent structure. Within this framework, we show an inherent trade-off, where enforcing latent independence or exclusive one-to-one latent-covariate dependence comes at a provable cost in latent-covariate alignment. We prove that the resulting disentanglement regimes are ordered by the strength of that alignment. Each regime admits a closed-form transformation of the latent space. We apply these transformations post-hoc to realign the representations of pretrained models such as CLIP, DINOv2, and ViT, and we fold them into the inference of informed factor analysis (iFA), a probabilistic model with covariate-informed factors. On simulated and real multi-omics data, we show that both post-hoc alignment and iFA enable controllability of structured latent representations.

## 8. Hypergraph-based Multimodal Retrieval-Augmented Generation with Incremental Refinement

- Authors: Shenao Chen, Yidan Xu, Xiangmin Han, Rundong Xue, Duanpo Wu, Yuhan Gao, Chenggang Yan, Yue Gao
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-17
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 3.3995033783873656
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.16628v1
- PDF: https://arxiv.org/pdf/2608.16628v1
- Local PDF: pdf/2026-08-19_08_Hypergraph-based Multimodal Retrieval-Augmented Generation with Incremental Refinement.pdf

Modern Multimodal Retrieval-Augmented Generation (M-RAG) systems are fundamentally limited by the binary connectivity paradigm of traditional simple graphs, which fails to capture the intricate, high-order correlations among heterogeneous entities, such as the N-ary relationships between a visual chart, its scattered textual descriptions, and underlying numerical data. Furthermore, existing refinement strategies often rely on exhaustive, full-page reconstruction to align cross-modal information, leading to prohibitive computational redundancy and the introduction of contextual noise in long-form document processing. In this paper, we propose Hyper-M2RAG, a novel framework that redefines multimodal document retrieval through High-order Hypergraph Representation Learning. We first formalize the document structure as a Multimodal Hypergraph, utilizing hyperedges as unified semantic containers to encapsulate multi-way associations across text, images, and tables, thereby transcending point-to-point modeling. To mitigate semantic fragmentation caused by physical pagination, we introduce an Anchor-driven Incremental Refinement mechanism. Rather than performing a global sweep, our approach identifies boundary-crossing anchor nodes and reconstructs their local hyper-topology using one-hop neighborhood contexts. This targeted refinement effectively bridges cross-page knowledge gaps with minimal computational footprints. Extensive evaluations on multimodal benchmarking datasets demonstrate that Hyper-M2RAG significantly outperforms state-of-the-art methods in both retrieval precision and generation coherence. Our code is available at https://github.com/ShenAoChen2001/MMHRAG.

## 9. POI Recommendation with LLM-Augmented Multi-Graph Learning and Contrastive Alignment

- Authors: Burak Tamer, Wolfram Höpken, Zehui Wang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-17
- DOI: Unavailable
- Categories: cs.IR, cs.LG
- Relevance: 3.37829162933522
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.16407v1
- PDF: https://arxiv.org/pdf/2608.16407v1
- Local PDF: pdf/2026-08-19_09_POI Recommendation with LLM-Augmented Multi-Graph Learning and Contrastive Alignment.pdf

Point-of-interest (POI) recommendation models based on graph neural networks achieve strong performance by propagating collaborative signals over user-item interactions, yet they struggle with the cold-start problem, where items with few or no interactions are not represented. In this paper, we propose LLM-augmented Multi-Graph Contrastive Learning (LLM-MGCL), a multi-graph neural network that uses semantic and spatial information about items to extend the LightGCN backbone with two auxiliary item-item graphs: a semantic graph constructed from sentence embeddings of LLM-generated photo summaries and keywords, and a geographic graph derived from Haversine distances between business locations. Item embeddings are propagated over all three graphs in parallel, fused additively, and aligned across views through a bidirectional InfoNCE contrastive objective that connects behavioral, semantic, and spatial representations of the same items. Experiments on the Yelp Multimodal Recommendation Dataset show that LLM-MGCL outperforms classical collaborative filtering, matrix factorization, and interaction-only graph neural network baselines. It improves Recall@20 by 52.0% and NDCG@20 by 64.8% over LightGCN while performing on par with the strongest contrastive baseline, Self-supervised Graph Learning (SGL), which is also affected by the cold-start problem. An ablation study reveals that the cross-view contrastive alignment (CA) is the primary driver of these gains, with the best performance achieved when all three graphs are combined. Our results suggest that externally grounded, LLM-derived item knowledge can effectively compensate for missing collaborative signal and mitigate the item cold-start problem in POI recommendation.

## 10. scE2TM improves single-cell embedding interpretability and reveals cellular perturbation signatures

- Authors: Hegang Chen, Yuyin Lu, Yifan Zhao, Zhiming Dai, Fu Lee Wang, Qing Li, Yanghui Rao, Yue Li
- Source: openalex
- Venue type: journal
- Journal: Nature Communications
- Publication status: published
- Publication date: 2026-08-17
- DOI: https://doi.org/10.1038/s41467-026-76825-5
- Categories: Single-cell and spatial transcriptomics, Immune responses and vaccinations, Cell Image Analysis Techniques
- Relevance: 3.3731151323960473
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://doi.org/10.1038/s41467-026-76825-5
- PDF: Unavailable
- Local PDF: Not downloaded

Single-cell RNA sequencing reveals cellular heterogeneity, yet computational methods struggle to balance performance with biological interpretability. Embedded topic models provide interpretable cell representations, but may learn overly similar topics, resulting in redundancy and incomplete capture of biological variation. Single-cell foundation models create opportunities to harness external biological knowledge for guiding model embeddings. Here, we present scE2TM, an external knowledge-guided embedded topic model for interpretable scRNA-seq analysis. scE2TM implements embedding clustering regularization where each topic is encouraged to represent a distinct group of genes, enabling it to capture unique biological information. We show that across 20 datasets, scE2TM outperforms seven state-of-the-art methods in clustering performance. We perform an interpretability benchmark to show that scE2TM topics exhibit greater diversity and stronger consistency with biological pathways. When modelling interferon-stimulated peripheral blood mononuclear cells, we find that scE2TM simulates topic perturbations that shift control cells toward stimulated states, recapitulating experimental interferon responses. When tested on a melanoma dataset, scE2TM identifies malignant-specific topics and extrapolates them to unseen patient data, highlighting melanoma-associated gene programs linked to patient survival. Computational methods for scRNA-seq data struggle to balance performance with biological interpretability. Here the authors develop scE2TM, which improves data clustering, while learning biologically meaningful and interpretable gene programs, revealing insights into disease and patient prognosis.

## 11. GraphLoom: Reliability-Calibrated Graph Evidence Routing for Multimodal KG-RAG

- Authors: Zafar Ali, Asad Khan, Aalia Malik, Pavlos Kefalas
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-15
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 3.365295635674499
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.15056v1
- PDF: https://arxiv.org/pdf/2608.15056v1
- Local PDF: pdf/2026-08-19_11_GraphLoom_ Reliability-Calibrated Graph Evidence Routing for Multimodal KG-RAG.pdf

Multimodal retrieval-augmented generation (RAG) systems often rely on long unstructured contexts or aggressively expanded evidence graphs, which can introduce noisy evidence, weaken multi-hop reasoning, and increase unsupported generation. We present GraphLoom, a reliability-calibrated multimodal knowledge-graph RAG framework for compact and faithful evidence routing. Given a question and its associated multimodal input, GraphLoom constructs an instance-level multimodal knowledge graph from grounded scene descriptions, extracted relational triples, and external commonsense knowledge. Instead of injecting all retrieved evidence into the generator, GraphLoom performs reliability-aware subgraph retrieval with bounded expansion and selectively routes high-utility evidence through hierarchical graph memory slots and joint graph-sequence attention in a frozen language model. To improve robustness in complex reasoning settings, GraphLoom further combines interleaved retrieval with budgeted corrective retrieval, enabling adaptive multi-hop evidence refinement under noisy retrieval conditions. We evaluate GraphLoom on ScienceQA, MultiModalQA, and OK-VQA, including large distractor evidence pools that approximate noisy external knowledge retrieval. Experimental results show consistent gains in answer quality and evidence faithfulness over strong multimodal RAG, graph-retrieval, and open-source vision-language baselines, with improved retrieval quality on MultiModalQA and stable performance under noisy evidence pools. Additional analyses using MiniCheck-based verification, human evaluation, and latency profiling show that reliability-calibrated graph evidence routing provides an effective alternative to long-context multimodal evidence injection.

## 12. CoM$^3$eT: A foundation model for medical image analysis through federated, multidimensional context integration

- Authors: J. Raphael Schäfer, Kai Geissler, Till Nicke, Chiara Tappermann, Karoline Heber, Eike Petersen, Habib Mergan, Lars Ole Schwen, Nick Weiss, Annika Gerken, Jan Hendrik Moltz, Tom Bisson, Isil Dogan O, Tim-Rasmus Kiehl, Norman Zerbe, Sefer Elezkurtaj, Robin S. Mayer, Nadine Flinner, Peter Wild, Isabel Dahm, Felix Peisen, Heinrich von Busch, Robert Grimm, Sebastian Arndt, Lisa Siegler, Matthias Stefan May, Antje Prasse, Natalia Artysh, Fabian Kiessling, Johannes Lotz
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-17
- DOI: Unavailable
- Categories: cs.CV, cs.LG
- Relevance: 3.3646346690793965
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.16268v1
- PDF: https://arxiv.org/pdf/2608.16268v1
- Local PDF: pdf/2026-08-19_12_CoM$^3$eT_ A foundation model for medical image analysis through federated, multidimensional context integration.pdf

Medical foundation models improve generalization when training AI models with limited labeled data, but remain confined to a single specialty, such as pathology or radiology, and to either sparse or dense outputs, such as classification or segmentation. Here, we present CoM$^3$eT (Co-representation Multidimensional Multitask Medical Transformer), a medical vision foundation model that unifies pathology and radiology, sparse and dense predictions, and two- and higher-dimensional inputs by modeling multidimensional context with attention. CoM$^3$eT outperformed other medical foundation models in an open competition spanning five tomographic, four whole-specimen, and three two-dimensional datasets, covering sparse and dense prediction tasks as well as report generation. When adapted across diverse clinical applications, training fewer than 2.5% of parameters achieved performance comparable to full fine-tuning, enabling research without access to high-performance GPU clusters. Applied to federated learning across hospitals, this approach achieved performance comparable to pooled-data training over internet connections and with consumer-grade hardware.

## 13. TAHB: A Comprehensive Benchmark for Text-Attributed Hypergraph Learning

- Authors: David Yoon Suk Kang, JungHyun Kim, Juhyun Jeon, Sang-Wook Kim
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-15
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 3.359639102411351
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.15055v1
- PDF: https://arxiv.org/pdf/2608.15055v1
- Local PDF: pdf/2026-08-19_13_TAHB_ A Comprehensive Benchmark for Text-Attributed Hypergraph Learning.pdf

Hypergraphs effectively model higher-order groupwise relationships beyond pairwise interactions, while pretrained language models (PLMs) and large language models (LLMs) provide rich semantic understanding from textual attributes. However, research on combining language models with hypergraph learning remains limited due to the lack of public text-attributed hypergraph benchmarks. To address this limitation, we present TAHB (Text-Attributed Hypergraph Benchmark), the first public benchmark integrating hypergraph structures and raw textual attributes. TAHB contains 10 real-world datasets from four domains - e-commerce, academia, movies, and politics networks - enabling systematic evaluation of text-aware hypergraph representation learning. Experimental results show that TAHB preserves key structural properties of real-world hypergraphs and consistently reproduces performance tendencies observed in existing benchmarks. Furthermore, experiments under both LLM-as-Enhancer and LLM-as-Predictor settings demonstrate that LLM-enhanced textual semantics improve hypergraph learning performance, while structural and textual information jointly provide the best setting for LLM-based prediction. Our benchmark provides a foundation for future research at the intersection of hypergraph learning and language models.

## 14. KHiM-Mamba: Injecting Pathology Knowledge into Mamba via Hidden-State Modulation for Whole Slide Image Analysis

- Authors: Qixiang Zhang, Yi Li, Tianqi Xiang, Haonan Wang, Mengjiao Wei, Bo Xu, Xiaomeng Li
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-14
- DOI: Unavailable
- Categories: eess.IV, cs.CV, q-bio.QM
- Relevance: 3.344782825908414
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.14757v1
- PDF: https://arxiv.org/pdf/2608.14757v1
- Local PDF: pdf/2026-08-19_14_KHiM-Mamba_ Injecting Pathology Knowledge into Mamba via Hidden-State Modulation for Whole Slide Image Analysis.pdf

Whole slide image analysis is commonly formulated as multiple instance learning (MIL), where instance features are contextually updated and aggregated into a slide representation, a process we term slide encoding dynamics. Recently, selective state-space models (SSM) have emerged as promising MIL architectures due to their long-sequence modeling capability and linear complexity. However, existing SSM-based MIL methods rely solely on visual features during MIL. Meanwhile, in large-scale WSIs, where sparse diagnostically decisive regions are surrounded by abundant irrelevant information, such purely vision-driven selective dynamics can misallocate state updates and readouts, causing the evolving SSM state to accumulate task-irrelevant evidence and dilute critical diagnostic cues over long scan trajectories. In this work, we propose the Knowledge-Aware Hidden-State Modulation architecture (KHiM-Mamba), which innovatively regulates Mamba's core selective state-space mechanism with explicit knowledge priors, steering slide encoding dynamics toward diagnostically meaningful evidence accumulation. Specifically, we redesign the original SSM layer to perform knowledge modulation operations during the evolution of hidden states, thereby guiding what visual evidence is accumulated and retrieved from the hidden state at each encoding step. Furthermore, we additionally introduce a local-adaptive vocabulary retrieval module that uses large language models to assign each patch fine-grained, tissue-specific semantic descriptions, enabling precise modulation across diverse tasks. Experiments on 11 public benchmarks across 4 tasks show that KHiM-Mamba consistently achieves state-of-the-art performance.

## 15. Valhalla: A Layered Knowledge-State and Service-Governance Framework for Long-Term Scientific Knowledge Work

- Authors: Yuyang Zheng, Nan Li, Wenxia Deng, Lige Yan, Xiang Li, Si Chen
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-15
- DOI: Unavailable
- Categories: q-bio.NC, cs.AI
- Relevance: 3.339544035384142
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.15193v1
- PDF: https://arxiv.org/pdf/2608.15193v1
- Local PDF: pdf/2026-08-19_15_Valhalla_ A Layered Knowledge-State and Service-Governance Framework for Long-Term Scientific Knowledge Work.pdf

As large language model (LLM) agents are increasingly adopted in scientific research, external knowledge bases, knowledge graphs, and long-term memory have improved information retrieval and task continuity. However, most structured knowledge systems remain node-centric, representing files, concepts, results, and judgments as nodes and relations in a graph. While suitable for personal knowledge management, such structures often depend on individual organizational practices, limiting knowledge sharing, integration, and reorganization across users. This paper presents Valhalla, a layered knowledge-state and service-governance framework for long-term scientific knowledge work. Valhalla replaces flat graphs with layered encapsulation and stable semantic boundaries through a five-layer File-Resource-Entity-Relationship-Graph (FREG) model. File and Resource preserve source identity and provenance, Entity represents knowledge objects, Relationship captures semantic judgments, and Graph provides task-oriented knowledge views, enabling knowledge states from different researchers to be exchanged and reorganized under a unified structure. We further introduce a Router-Contract-Workflow service-governance architecture, inspired by the microkernel paradigm, to constrain how language models access, modify, and extend knowledge states while maintaining structural consistency and auditable operational boundaries. We implement a Valhalla prototype and validate knowledge ingestion, cross-member integration, and scientific writing support through an antibody-design review task comprising 26 paper resources, 80 knowledge entities, and 92 semantic relations. Rather than proposing a new knowledge-extraction algorithm, Valhalla offers a paradigm for organizing collaborative scientific knowledge, transforming individualized knowledge structures into transferable and reorganizable shared knowledge states.

## 16. Demystifying Oversmoothing in Sheaf Neural Networks: An Index-Theoretic Criterion

- Authors: Junwen Dong, Yuhan Peng, Hao Li, Huitao Feng, Kelin Xia
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-17
- DOI: Unavailable
- Categories: cs.LG, math.DG
- Relevance: 3.3026707196547562
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.16180v1
- PDF: https://arxiv.org/pdf/2608.16180v1
- Local PDF: pdf/2026-08-19_16_Demystifying Oversmoothing in Sheaf Neural Networks_ An Index-Theoretic Criterion.pdf

To combat oversmoothing in Graph Convolutional Networks, Sheaf Neural Networks (SNNs) were proposed as a generalization by equipping the graph with a sheaf structure and replacing the graph Laplacian with a sheaf Laplacian $\mathcal{L}$. Existing analyses connect sheaf diffusion to oversmoothing via the harmonic space ($\ker\mathcal{L}$), taking its absolute dimension as an indicator of anti-oversmoothing capacity. However, absolute dimension alone is not a reliable measure: certain sheaf configurations inflate $\dim \ker \mathcal{L}$ while their harmonic sections remain entirely constant, without enriching discriminative capacity. We instead introduce the first relative, geometric approach, yielding a precise characterisation of anti-oversmoothing capacity. Under natural conditions on stalk transportation and global sheaf structure, we establish an index-theoretic comparison criterion showing that one sheaf's harmonic space genuinely contains another's beyond trivial inflation. We illustrate this with a concrete instance and further introduce \textit{GyroSheaf}, a sheaf with curved gyrovector-space stalks, extending the criterion to the non-linear setting via local tangent-space linearization. Experiments across ten models confirm the theoretical criterion: sheaf models violating the criterion collapse despite possessing index jumps, while compliant models maintain depth-stable representations.

## 17. Schema-Agnostic Graph Reasoning Agent for Hybrid Knowledge Graphs

- Authors: Marius Dragic, Ruben Ifrah, Alexandre Rio
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-16
- DOI: Unavailable
- Categories: cs.AI, cs.CL, cs.DB
- Relevance: 3.296406524212064
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.15834v1
- PDF: https://arxiv.org/pdf/2608.15834v1
- Local PDF: pdf/2026-08-19_17_Schema-Agnostic Graph Reasoning Agent for Hybrid Knowledge Graphs.pdf

Tool-calling LLM agents navigate unfamiliar codebases with a handful of generic primitives for listing, reading and searching files (ls, cat, grep). A knowledge graph admits the same interface: listing neighbours, reading node content and searching descriptions are the same operations on a different substrate. Building on this correspondence, we present GRA, a Graph Reasoning Agent that explores hybrid knowledge graphs, whose nodes are either textual concepts or relational tables, with seven generic tools, discovering everything domain-specific at run time. On UFK-M (Unified Factory Knowledge Model), an industrial benchmark of 258 analytical questions whose gold answers are produced by executing validated SQL programs, GRA beats a full-context agent by 5.1 pp (88.4% vs. 83.3%), while reading under a third of its input tokens. A graph-free control shows the gain comes chiefly from selective agentic access rather than graph topology, and that the effect depends on a model able to drive tools reliably. Seeing less, the agent answers better: selective navigation over a structured substrate beats exhaustive context.

## 18. Mental Model Management: An Operator-Based Framework for LLM Memory

- Authors: Oliver Kramer
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-16
- DOI: Unavailable
- Categories: cs.AI, cs.NE
- Relevance: 3.291387565468611
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.15451v1
- PDF: https://arxiv.org/pdf/2608.15451v1
- Local PDF: pdf/2026-08-19_18_Mental Model Management_ An Operator-Based Framework for LLM Memory.pdf

Large language models process large amounts of information but usually lack an explicit mechanism for maintaining compact and evolving conceptual representations. We introduce Mental Model Management (3M), a framework in which knowledge is represented as mental models consisting of compact chunks. Rather than accumulating text passages, 3M continuously integrates new information into an existing conceptual representation. A set of operators extracts knowledge, retrieves relevant models, adds and updates chunks, reorganizes representations, detects inconsistencies, and derives new knowledge. We describe the main 3M operators and illustrate each operation using Evolution Strategies as a running example.

## 19. A Generative Virtual Tissue Model Enables Computational Design of Therapeutic Perturbation Strategies

- Authors: Lu, Y., Zhang, W., Chen, Y.-J., Yin, J., Chen, L., Fleisher, K., Gornet, J., Liu, R., Wang, Z. J., Poon, Y., You, Y., Thomson, M.
- Source: biorxiv
- Venue type: preprint
- Journal: biorxiv
- Publication status: preprint
- Publication date: 2026-08-18
- DOI: 10.64898/2026.08.12.743536
- Categories: bioinformatics
- Relevance: 3.269116228559504
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://www.biorxiv.org/content/10.64898/2026.08.12.743536v1.full.pdf
- PDF: https://www.biorxiv.org/content/10.64898/2026.08.12.743536v1.full.pdf
- Local PDF: Not downloaded

Computational design has transformed many fields of engineering, where simulators can explore millions of candidate design configurations before experimental development and testing. Therapeutic design in biomedicine has resisted computational design approaches because disease progression and therapeutic response emerge from interactions among many cell types within human tissue, governed by biochemical parameters that are largely unknown and potentially unknowable. Here, we introduce the Cell Interaction Foundation Model (CIFM), a virtual tissue model that forward-simulates the transcriptional dynamics of cells in human tissue under arbitrary therapeutic conditions based upon a spatial transcriptomic seed. CIFM is a geometric graph neural network trained by self-supervised masked-transcriptome prediction on millions of cellular microenvironments spanning human tissue types and disease states; generative, auto-regressive, monte-carlo play-out, then, simulates transcriptional dynamics under combinatorial perturbations from a spatial transcriptomic seed. We validate CIFM by showing accuracy gains in gene expression prediction and imputation, disease classification, recapitulation of perturbation responses in prostate cancer models, and recovery of T cell-tumor signaling measured in cell-cell sequencing experiments. Beyond such conventional tasks, CIFM enables target identification and therapeutic design through generative tissue simulation play-outs. Analyzing over 10^6 single and combinatorial perturbations, CIFM designs immunotherapy strategies for cancer and autoimmune disease that exploit combinatorial manipulation of signaling pathways to induce or suppress immune activation. Broadly, CIFM shows how generative artificial intelligence methods can be applied to model emergent behavior in highly interacting biological systems, yielding new approaches to fundamental understanding of tissue behavior as well as large-scale therapeutic design.

## 20. Beyond Single Object: Learning 3D Relations with Large Language Models

- Authors: Kohsuke Ide, Ryousuke Yamada, Yue Qiu, Xianzheng Ma, Yoshihiro Fukuhara, Hirokatsu Kataoka, Yutaka Satoh
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-16
- DOI: Unavailable
- Categories: cs.CV, cs.AI, cs.CL
- Relevance: 3.1980829494135476
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.15710v1
- PDF: https://arxiv.org/pdf/2608.15710v1
- Local PDF: pdf/2026-08-19_20_Beyond Single Object_ Learning 3D Relations with Large Language Models.pdf

We address a fundamental gap in 3D-LLMs: existing models focus on single-object/scene description, struggling with detailed, inter-object comparison. We propose a framework for detailed object-level reasoning across multiple objects with three components: (1) MO3D (Multi-Object in 3D), an instruction dataset requiring fine-grained multi-object comparison; (2) Multi-3DLLM, using a minimal Patch-Interaction Transformer (PIT) that models inter-/intra-object relationships while preserving local geometry; (3) Mini-apps, two application-driven benchmarks (Shape Mating, Change Captioning) that probe geometric understanding for practical use. Recent 3D-LLMs and 2D-VLMs perform poorly on these tasks, lacking both comparison-centric design and geometric awareness. In contrast, Multi-3DLLM trained on our mixture data learns geometric reasoning, surpasses all baselines on MO3D, and provides positive transfer to single-object classification.

## 21. Large Discovery Models: Empirically-grounded Model-Based Open-Ended Search

- Authors: Zhongwei Yu, Yan Song, Xue Yan, Anjie Liu, Xingyu Lu, Yihang Chen, Huichi Zhou, Siyuan Guo, Luoyang Sun, Sihan Chen, Xiangning Yu, Jun Wang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-16
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.1946840994297943
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.15669v1
- PDF: https://arxiv.org/pdf/2608.15669v1
- Local PDF: pdf/2026-08-19_21_Large Discovery Models_ Empirically-grounded Model-Based Open-Ended Search.pdf

Scientific discovery often involves optimising expensive-to-evaluate objectives over vast, structured, and open-ended hypothesis spaces, such as molecules, protein sequences, and computer programs. Generative models such as large language models (LLMs) provide expressive priors over such spaces, but their likelihoods and self-assessments are unreliable proxies for the objectives and calibrated epistemic uncertainty, especially for novel candidates outside the observed data distribution. We introduce the Large Discovery Model (LDM), an empirically grounded recurrent architecture that couples a generative model with a Bayesian non-parametric reward surrogate model. The generative model proposes and refines candidate designs, while the surrogate predicts their performance and quantifies uncertainty, yielding an uncertainty-aware value that guides candidate generation, refinement, and selection. The discovery memory and the surrogate model are continually updated as each new experimental observation arrives. We evaluate LDM on three scenarios spanning different design modalities and objectives, including neural-network training, antibody design, and molecular optimisation. Compared to LLM-only reflection or traditional statistical search across these domains, LDM achieves a $2.4\times$ greater reduction in validation BPB, an $18.2\%$ relative decrease in binding energy, and more than $60\%$ relative gains in molecular multi-objective performance. These results suggests that LDM could serve as a general-purpose discovery engine for effective search over open-ended hypothesis spaces.

## 22. PertMind: Eliciting Emergent Biological Reasoning in LLM via Reinforcement Learning on Cellular Perturbation Data

- Authors: Zhenchao Tang, Xiaogang Xu, Tianxu Lv, Jiahui Guan, Jiale Zhou, Haohuai He, Zhi Song, Hanbo Huang, Jiehui Huang, Jiafei Wu, Zhe Liu
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-17
- DOI: Unavailable
- Categories: cs.LG, cs.AI, q-bio.QM
- Relevance: 3.184141938162907
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.16419v1
- PDF: https://arxiv.org/pdf/2608.16419v1
- Local PDF: pdf/2026-08-19_22_PertMind_ Eliciting Emergent Biological Reasoning in LLM via Reinforcement Learning on Cellular Perturbation Data.pdf

Large language models can describe mechanisms, yet scalable post-training still depends on costly, manually curated biological reasoning traces. Here we show that cellular perturbation atlases can instead become reinforcement-learning environments, where measured gene responses provide computable rewards for biological reasoning. We introduce PertMind, which combines trusted-trajectory supervised initialization with gene-, pathway-, and format-level reinforcement signals. Trained only on forward perturbation-response prediction, PertMind improved response inference in unseen cellular contexts while retaining general language capabilities. It also transferred without task-specific post-training to reverse perturbation identification, double-perturbation reasoning, phenotypic-screen prioritization, and biological-process interpretation. PertMind further generated biological profiles that supported competitive gene, cell, and donor representations across multiscale downstream tasks. These results support the hypothesis that reinforcement on experimental endpoints can concentrate reusable biological strategies already accessible to pretrained models. More broadly, perturbation-derived reinforcement learning offers a scalable route for transforming expanding experimental atlases into training environments for general-purpose biological reasoning.

## 23. Protein Structure Prediction: From Evolutionary Constraints to Generative Modeling

- Authors: Wengan He, Yongsheng Luo, Lihong Jiang, Wenhui Xu, Yu Li
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-17
- DOI: Unavailable
- Categories: cs.AI, cs.LG
- Relevance: 3.1070181882671877
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.16094v1
- PDF: https://arxiv.org/pdf/2608.16094v1
- Local PDF: pdf/2026-08-19_23_Protein Structure Prediction_ From Evolutionary Constraints to Generative Modeling.pdf

Accurate protein structure prediction is fundamental to structural biology because protein structure underlies molecular function and provides a basis for mechanistic interpretation. Recent advances in deep learning have transformed the field from multiple sequence alignment (MSA)-driven monomer folding into broader frameworks capable of modeling protein complexes and increasingly heterogeneous molecular systems. Existing reviews have summarized this progress from the perspectives of representative models, application domains, and protein design. Building on these efforts, this review focuses on the methodological evolution of the field itself. It examines recent developments through three closely related dimensions: representations and data, architectures and learning strategies, and confidence and evaluation. Within this perspective, the field is organized into four methodological phases and three cross-cutting transitions: from explicit evolutionary coupling features and early contact prediction to learned sequence representations in AlphaFold2, RoseTTAFold, and ESMFold; from protein-only monomer folding to increasingly integrated modeling of heterogeneous molecular systems in AlphaFold-Multimer, RoseTTAFoldNA, and AlphaFold3; and, more recently, from prediction-oriented structure inference to design-oriented generative modeling in RFdiffusion and related frameworks. This framework provides a clearer understanding of how methodological shifts have shaped the capabilities, limitations, and practical roles of recent models.

## 24. Diagnosing and Mitigating Perception-Decision Misalignment in Omni-LLMs via Modality Subspace Activation

- Authors: Hongbo Jiang, Jie Li, Yunhang Shen, Tianyu Xie, Pingyang Dai
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-31
- DOI: Unavailable
- Categories: cs.LG, cs.CV
- Relevance: 3.103946427528151
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.14655v1
- PDF: https://arxiv.org/pdf/2608.14655v1
- Local PDF: pdf/2026-08-19_24_Diagnosing and Mitigating Perception-Decision Misalignment in Omni-LLMs via Modality Subspace Activation.pdf

Omni-Large Language Models (Omni-LLMs) power complex multi-modal reasoning in applications like World Action Models and autonomous agents. However, their strong performance often masks a profound Perceptual-Decision Misalignment (PDM), where decisions remain unfaithful to multi-modal perceptions. To diagnose this, we formalize Causal Modality Sensitivity (CMS), operationalized via a dual-lens framework: Answer Retention Rate (ARR) at the macro behavioral level, and Logit Angular Discrepancy (LAD) to track microscopic distribution shifts. We also curate CausalMSBench, a diagnostic dataset isolating language priors. Benchmarking reveals that popular Omni-LLMs exhibit critically low CMS, showing negligible distribution shifts even when key modalities are removed. To rectify this, we propose Modality Subspace Activation (MSA), a training-free inference-time framework that uses Singular Value Decomposition (SVD) to estimate modal activation strengths. MSA dynamically balances modal projections in the last hidden state, effectively restoring CMS across benchmarks.

## 25. Self-Routed Tensor Adapters for Parameter-Efficient Universal Visual Adaptation

- Authors: Suraj Yadav
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-17
- DOI: Unavailable
- Categories: cs.CV, cs.LG
- Relevance: 3.0735037191812986
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.16384v1
- PDF: https://arxiv.org/pdf/2608.16384v1
- Local PDF: pdf/2026-08-19_25_Self-Routed Tensor Adapters for Parameter-Efficient Universal Visual Adaptation.pdf

Universal visual representations require adaptation mechanisms that adapt across heterogeneous domains without fragmenting knowledge into domain-specific modules. Parameter-efficient fine-tuning adapts frozen visual foundation models efficiently, but standard low-rank adapters use a fixed subspace for all inputs, which can be restrictive when domains differ in style, background, and semantic context. MoE-based adapters improve specialization through multiple expert pathways, but often rely on external routers and large expert banks, adding parameters and separating routing from adaptation. We propose \textbf{Self-Routed Tensor Adapters}, a compact framework for multi-domain visual adaptation. SRTA projects each input into a low-rank space, computes routing weights from this representation using a learnable domain matrix, and uses these weights to blend slices of a shared Tucker core. This produces a sample-specific adaptation matrix without an external gating network, allowing shared visual factors to be reused while supporting domain-aware specialization. To strengthen pathway learning, we introduce a progressive depth-weighted routing objective that supervises routing decisions across adapter layers. Across five heterogeneous multi-domain visual classification benchmarks, SRTA achieves competitive or slightly stronger average accuracy than MoE-style PEFT baselines while using substantially fewer trainable parameters. At rank 64, SRTA uses 2.77M parameters in the 4-domain setting compared with 9.52M for MoLoRA, and 3.00M in the 6-domain setting compared with 14.31M. Overall, SRTA offers an effective accuracy-parameter trade-off for adapting visual foundation models toward universal multi-domain representations. \href{https://github.com/surajyadav-research/SRTA}{GitHub}

## 26. Benchmarking DNA foundation models for zero-shot variant effect prediction shows the importance of context, training, and architecture

- Authors: Ilaria Alfisi, Francesca Ciapi, Marta Baragli, Alberto Magi
- Source: openalex
- Venue type: journal
- Journal: Genome biology
- Publication status: published
- Publication date: 2026-08-17
- DOI: https://doi.org/10.1186/s13059-026-04238-0
- Categories: Genomics and Rare Diseases, Genetic Associations and Epidemiology, Genomics and Phylogenetic Studies
- Relevance: 3.050252778855832
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://doi.org/10.1186/s13059-026-04238-0
- PDF: Unavailable
- Local PDF: Not downloaded

In this study, we systematically evaluate the performance of several DNA foundation models (NT, DNABERT, HyenaDNA and Evo 2) in predicting the functional impact of genetic variants using Zero-shot scoring, a method that does not require task-specific fine-tuning. We assess the models’ sensitivity to sequence alterations introduced by Single Nucleotide Variants (SNVs), comparing their ability to capture both local and extended contextual effects. Using pathogenic, benign, and uncertain SNVs from ClinVar, we show that large multi-species NT models outperform other architectures in detecting functional consequences, not only at the SNV site but also in adjacent regions. These models exhibit superior discriminative power across variant categories, especially when aggregating Zero-shot scores over multiple surrounding tokens. Conversely, models trained solely on human sequences or relying on a next-token prediction objective, such as DNABERT, HyenaDNA, and Evo 2, exhibit limited contextual awareness and a reduced ability to differentiate variant effects. Our findings highlight the critical importance of model size, training objective, and training data diversity in shaping model performance. Furthermore, we discuss current limitations in modeling long-range dependencies in genomic sequences and suggest that innovations in transformer architectures, such as sparse attention or memory-augmented models, may provide viable paths toward scalable, genome-wide variant effect prediction.

## 27. MELD: A Protocol for Merging Knowledge Across Distributed Agentic Memories

- Authors: Lauri Lovén, Jaakko Sauvola, Jukka Riekki, Sasu Tarkoma
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-17
- DOI: Unavailable
- Categories: cs.DC, cs.AI, cs.MA
- Relevance: 3.0256718694036944
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.16357v1
- PDF: https://arxiv.org/pdf/2608.16357v1
- Local PDF: pdf/2026-08-19_27_MELD_ A Protocol for Merging Knowledge Across Distributed Agentic Memories.pdf

Autonomous agents share a transport and can call each other's tools, but they cannot share what they know: no protocol lets two agents' memories reconcile a fact phrased two ways, link related facts held apart, or reconcile contradictory knowledge without silently discarding either claim. We present MELD, a self-managing coherence mechanism for a federation of agent memories whose run-time model is the knowledge graph itself. Each brain admits every incoming claim through a five-outcome procedure (insert, merge, relate, conflict, or reject), decided from three signals (scoped claim-key identity, embedding similarity, and a natural-language-inference verdict) under context and freshness gates, and acting through exactly one auditable, authenticated Patch, the only object that mutates state. A binding onto standard publish/subscribe transport with a per-claim status CRDT keeps sovereign brains coherent in claim status without a coordinator: self-healing after partitions and under lossy routing, and self-protecting against silent rewrite by a peer, under a benign-fault model. MELD does not adjudicate truth; a detected contradiction is preserved for later adjudication, never silently resolved. On HotpotQA distractor, distributed merge is recall-non-inferior to a centralized store under a pre-specified equivalence test and recall-superior to naive union at about 11% less live storage; the merge classifier separates at AUC 0.968 with a 0.013 false-merge rate on adjudicated candidate pairs; the status CRDT reconverges in 30/30 real partition-heal trials where last-writer-wins manages 11/30; and semantic routing delivers about 3x fewer messages at matched recall. We evaluate on a real computing continuum spanning an operator-grade 5G edge, national HPC, and a local tier, with empirically calibrated thresholds.

## 28. Development of a universal imaging “phenome” using shape, appearance and motion (SAM) features and the SAM Phenotype Observation Tool (SPOT)

- Authors: Felix Zhou, Adam Norton-Steele, Lewis Marsh, Helen M. Byrne, Heather A. Harrington, Xin Lü
- Source: openalex
- Venue type: journal
- Journal: Nature Communications
- Publication status: published
- Publication date: 2026-08-17
- DOI: https://doi.org/10.1038/s41467-026-75505-8
- Categories: Cell Image Analysis Techniques, Single-cell and spatial transcriptomics, Digital Imaging for Blood Diseases
- Relevance: 2.9935850385062794
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://doi.org/10.1038/s41467-026-75505-8
- PDF: Unavailable
- Local PDF: Not downloaded

Abstract Cells are plastic, highly heterogeneous and change over time. High-content timelapse imaging promises to reveal dynamic cell behaviors, enabling more accurate identification of cell state and cell fate prediction for biological hypothesis generation and perturbation screens. To empower live-cell imaging based screening, we report the development of (1) a Shape, Appearance, Motion (SAM) “phenome”; a universal set of 2185 image-derived features that act as a image-“transcriptome” to comprehensively quantify an object’s instantaneous phenotype; (2) the SAM-Phenotype-Observation-Tool (SPOT), for image-“sequencing” analysis of phenomes. We validate the effectiveness of unbiased SAM-SPOT workflow on publicly available computer vision and 2D single cell imaging datasets. Importantly, we demonstrate that SAM-phenome outperforms features generated by deep learning AI models trained on &gt;1 million fixed single cell and &gt;5000 single cell video frames, respectively. SAM-phenome and SPOT deliver high-throughput, object-treatment-agnostic, comprehensive screening readouts of dynamics, promising to advance novel molecular target discovery and new medicine development.

## 29. Multi-Agent Closed-Loop Reasoning for Organic Structure Elucidation from Multimodal Spectra

- Authors: Bingsen Xue, Zhuojun Jiang, Jianhao Zhang, Mingcheng Gu, Yizhe Yuan, Yongtai Zhuo, Yifan Zhang, Li Wang, Ya Su, Yue Yuan, Jiang Liu, Xueqian Kong, Cheng Jin
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-12
- DOI: Unavailable
- Categories: physics.chem-ph, cs.AI
- Relevance: 2.993077584584441
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.14720v1
- PDF: https://arxiv.org/pdf/2608.14720v1
- Local PDF: pdf/2026-08-19_29_Multi-Agent Closed-Loop Reasoning for Organic Structure Elucidation from Multimodal Spectra.pdf

Following the molecular discovery and synthesis revolutions, scalable automated structure elucidation from routine spectroscopic data remains an outstanding challenge. Despite decades of computational efforts, no existing system achieved reliable reasoning over unseen spectra. Here, we propose MACROS, a multi-agent system automating structure elucidation by emulating expert iterative hypothesis-testing. Trained on 100M simulated and 1.6M experimental spectra-molecule pairs, it natively supports arbitrary combinations of routine spectroscopic techniques. It achieves unprecedented zero-shot generalization to diverse real-world samples, correctly identifying synthetic compounds, natural products and metabolites above 500 Da with 1D NMR. Remarkably, MACROS spontaneously recovers textbook spectroscopic correlations from unassigned data and exhibits emergent chemical intuition such as a ring-first parsing preference, learning fundamental chemical principles rather than memorizing database patterns. MACROS augments chemists via collaboration to deliver sixfold faster, 40% more accurate elucidation. MACROS establishes a scalable foundation for fully automated structure elucidation, and catalyzes accelerated molecular discovery toward autonomous laboratories.

## 30. Assessing the Reliability of LLM-Generated Phenotype-Genotype Associations Through External Validation

- Authors: Sun, C., Xin, Y., Zeng, S., Sunthankar, S. D., Su, W.-C., Lynn, J., Mundo, S., Babanejad, M., Feng, Q., Wei, W.-Q.
- Source: biorxiv
- Venue type: preprint
- Journal: biorxiv
- Publication status: preprint
- Publication date: 2026-08-18
- DOI: 10.64898/2026.08.13.744701
- Categories: bioinformatics
- Relevance: 2.986813755044758
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://www.biorxiv.org/content/10.64898/2026.08.13.744701v1.full.pdf
- PDF: https://www.biorxiv.org/content/10.64898/2026.08.13.744701v1.full.pdf
- Local PDF: Not downloaded

Background: Phenotype-genotype associations underpin precision medicine by enabling disease prevention, early diagnosis, risk stratification, therapeutic target discovery, and personalized treatment. However, the rapid growth of scientific evidence has made manual curation of these associations increasingly labor-intensive, time-consuming, and incomplete. Large Language Models (LLMs) offer a potential path to scalable genomic generation and synthesis of this knowledge, but their ability to accurately identify phenotype-genotype associations and the extent to which these outputs are supported by established genomic knowledge bases remain unclear. Materials and Methods: Four LLMs, Claude Sonnet 4.6, DeepSeek V4 Flash, Gemini 3 Flash Preview, and GPT-5.5, were benchmarked on six zero-shot task categories covering forward and reverse phenotype-gene and phenotype-SNP generation. A total of 4,196 associations were identified from curated inputs and evaluated through a multistage external verification pipeline comprising phenotype normalization, ontology mapping, genomic identifier validation against Ensembl, and evidence verification using both the GWAS Catalog and OMIM. Associations were assigned a fused evidence level of strong, moderate, weak, or none. Results: Overall, 74.19% of generated associations were matched to at least one external genomic knowledge base; 9.15% received strong support and 54.46% moderate support. Phenotype-gene associations were more verifiable than phenotype-SNP associations (strong or moderate: 67.19% vs 54.06%). Among existing associations, Claude Sonnet 4.6 achieved the highest overall strong or moderate rate (69.2%), followed by GPT-5.5 (65.1%), DeepSeek V4 Flash (61.7%), and Gemini 3 Flash Preview (56.9%). Conclusion: LLMs can support scalable generation of candidate phenotype-genotype associations. Performance varied substantially by relation type and was lower for SNP-level and rare disease associations, highlighting both the limitations of current genomic resources and the need for rigorous validation pipelines. Key words: large language model; clinical genomics; phenotype-genotype association; external validation; genomic knowledge base
