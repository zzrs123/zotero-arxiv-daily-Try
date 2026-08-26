# Paper Daily Reading - 2026-08-26

## 1. ReCoG: Reciprocal Co-Evolution for Multimodal Graph Learning

- Authors: Rui Xue, Tianfu Wu
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-24
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 4.0521393501094325
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.22786v1
- PDF: https://arxiv.org/pdf/2608.22786v1
- Local PDF: pdf/2026-08-26_01_ReCoG_ Reciprocal Co-Evolution for Multimodal Graph Learning.pdf

Multimodal graph learning requires jointly training over graph structure and heterogeneous node attributes, yet existing methods largely decouple these processes: prior multimodal graph neural networks (GNNs) focus on aligning modalities in a shared embedding space while operating on fixed or weakly adapted graph structures, and graph structure learning approaches infer topology from unimodal node representations without accounting for multimodal interactions. This separation fundamentally limits the ability of GNNs to capture semantically meaningful relationships in multimodal settings, where observed edges are often noisy, incomplete, or misaligned with underlying semantics. We propose ReCoG (Reciprocal Co-Evolution for Multimodal Graph Learning), a new learning paradigm that tightly couples graph structure learning and multimodal representation learning through end-to-end reciprocal interaction. Concretely, ReCoG integrates (i) a multimodal graph refiner that infers and corrects edges using cross-modal semantic evidence, and (ii) a coupled cross-modal message passing mechanism that performs joint intra- and inter-modality propagation over the refined graph. This unified design yields greater expressiveness than decoupled or two-stage formulations and allows dynamic interaction between topology and representation learning. Across diverse benchmarks for node classification and link prediction, ReCoG consistently outperforms strong multimodal graph structure learning baselines, including graph foundation models. Our results demonstrate that reciprocal co-evolution of structure and semantics is important for effective multimodal graph learning, challenging the prevailing separation between topology and representation learning.

## 2. Uncovering Cellular Resolution in scRNAseq via Unbiased Cell and Gene Network Analysis

- Authors: Olga lanzetta, Luisa Cutillo, Bailey Andrew, Claudia Angelini
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-24
- DOI: Unavailable
- Categories: q-bio.MN, stat.AP
- Relevance: 3.79535237478956
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.22982v1
- PDF: https://arxiv.org/pdf/2608.22982v1
- Local PDF: pdf/2026-08-26_02_Uncovering Cellular Resolution in scRNAseq via Unbiased Cell and Gene Network Analysis.pdf

Conventional annotation of single-cell RNA-sequencing (scRNA-seq) data relies heavily on manual, marker-based thresholding, an approach that can obscure subtle transcriptomic gradients and collapse functionally distinct cell states into broad, heterogeneous populations. Here we apply the Gaussian multi-Graphical Model (GmGM) framework, which jointly infers cell-cell and gene-gene dependency structure from a single scRNA-seq data matrix, to a 10x Genomics PBMC dataset. Ten independent GMGM-Leiden clustering runs were integrated into a robust consensus partition using a soft cluster ensemble approach and benchmarked against reference cell-type annotations. This strategy yielded stable cluster partitions that resolve biologically meaningful sub-populations not distinguished by the reference annotation. In parallel, for each cluster, gene co-expression modules were extracted from the fitted model via consensus Leiden clustering across resolutions, evaluated using standard network metrics, and validated functionally with the Network Enrichment Analysis Test (NEAT), which confirmed non-random enrichment signal. A module-scoring procedure linked network topology to per-cell, per-cluster expression signatures, and a novel extension of GmGM, recovering a shared cell-cell network together with population-specific gene networks in a single model run, was demonstrated in a case study on the CD4+ T-cell population. These results indicate that GmGM provides a unified, reproducible framework for joint cell clustering and gene-network inference, capable of revealing cellular structure beyond that captured by conventional pipelines.

## 3. Beyond benchmarking: an expert-guided consensus approach to spatially aware clustering

- Authors: Jieran Sun, Kirti Biharie, Peiying Cai, Niklas Müller‐Bötticher, Paul Kießling, Meghan A. Turner, Søren Helweg Dam, Florian Heyl, Sarusan Kathirchelvan, Martin Emons, Samuel Gunz, Sven Twardziok, Amin El‐Heliebi, Martin Zacharias, SpaceHack 2.0 participants, Søren Helweg Dam, Fadhl Alakwaa, Shahul Alam, Maria Calleja, Yuzhou Chang, Thomas Chartrand, Nigel S. Chou, Estella Y. Dong, Michael Fletcher, George Gavriilidis, Alexander Kanitz, Sameesh Kher, Louis Kümmerle, Francesca A. Luongo, Qirong Mao, Giorgia Moranzoni, Mar M. Moreno, Anastasiia Okhtienko, Lena Perry, Lucie Pfeiferová, Daryna Pikulska, Shyam Prabhakar, Rasool Saghaleyni, Zaira Seferbekova, Vipul Singhal, Divya Sitani, Charlotte Soneson, Sebastian Tiesmeyer, Marco Varrone, Siao-Han Wong, Liya Zaygerman, Teresa Zulueta-Coarasa, Roland Eils, Marcel Reinders, Raphaël Gottardo, Christoph Kuppe, Brian Long, Ahmed Mahfouz, Mark D. Robinson, Naveed Ishaque
- Source: openalex
- Venue type: journal
- Journal: Nature Methods
- Publication status: published
- Publication date: 2026-08-24
- DOI: https://doi.org/10.1038/s41592-026-03194-8
- Categories: Single-cell and spatial transcriptomics, Delphi Technique in Research, Gene expression and cancer classification
- Relevance: 3.6747529422820246
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://doi.org/10.1038/s41592-026-03194-8
- PDF: Unavailable
- Local PDF: Not downloaded

Spatial omics technologies have revolutionized the study of tissue architecture and cellular heterogeneity by integrating molecular profiles with spatial localization. In spatially resolved transcriptomics, delineating higher-order anatomical structures is critical for understanding how cellular organization affects tissue and organ function. Since 2020, more than 50 spatially aware clustering (SAC) methods have been developed for this purpose. However, the reliability of current benchmarks is undermined by their narrow focus on Visium and brain tissue datasets, as well as incorrect interpretation of manual annotation as ground truth. Here, we present SACCELERATOR, a community-driven, extensible framework that standardizes data formatting, method integration, and metric evaluation, and is designed to rapidly incorporate new methods and datasets. SACCELERATOR currently includes 22 SAC methods applied to 15 datasets spanning 9 technologies and diverse tissue types. Our analysis revealed substantial limitations in the generalizability and reproducibility of SAC methods across tissues and platforms. We also demonstrate that anatomical labels commonly used as ground truths are often biased, potentially error-prone, and, in some cases, unsuitable for benchmarking efforts. Rather than scoring and comparing methods, we propose a consensus-guided workflow that aggregates clustering results to generate consensus representations. Descriptive spatial metrics highlight areas of high entropy where method disagreement is highest, enabling targeted feedback for tissue experts. Applied to brain and cancer datasets, this approach uncovered biologically meaningful patterns overlooked by individual methods and manual annotations. Our results underscore the need for iterative, expert-in-the-loop analysis and reveal that traditional evaluation metrics do not always capture the subjective qualities of results. By improving tissue annotation and addressing key benchmarking limitations, SACCELERATOR provides a robust foundation for advancing spatial omics research.

## 4. A Scalable Vector Graphics Latent Space

- Authors: Leonardo Zini, Elia Frigieri, Lorenzo Baraldi
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-22
- DOI: Unavailable
- Categories: cs.CV, cs.AI
- Relevance: 3.4804345653319313
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.21893v1
- PDF: https://arxiv.org/pdf/2608.21893v1
- Local PDF: pdf/2026-08-26_04_A Scalable Vector Graphics Latent Space.pdf

Scalable Vector Graphics are a fundamental medium for resolution-independent visual content, yet the deep learning community lacks a continuous, dense, and invertible latent space for vector representations, the kind of foundational building block that Variational Autoencoders and their descendants have long provided for raster images. We introduce SLS (SVG Latent Space), a Transformer-based autoencoder that learns compact dense representations of individual SVG paths, the atomic visual elements from which any SVG image can be composed. By modeling SVG commands, coordinate data, and visual properties within a unified BPE-based token vocabulary, SLS learns fixed-size latent representations that jointly capture structure and appearance, and can be decoded back into valid, style-consistent SVG paths with high fidelity. The resulting embedding space is robust, invertible, and structured: embeddings lie on a unit hypersphere, enabling efficient similarity search, composition, and downstream conditioning through simple vector-space operations. Finally, we demonstrate that SLS generalizes across diverse tasks reducing their FLOPs by over 150 times compared to token-based approaches, and establishing a general-purpose latent foundation for vector graphics research.

## 5. Who Should Teach? Confidence-Aware Dual-Teacher Learning for Few-Shot Node Classification on Text-Attributed Graphs

- Authors: Hojin Kim, Sujin Yoon, Sungsu Lim, Dongwon Lee, David Yoon Suk Kang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-22
- DOI: Unavailable
- Categories: cs.LG, cs.SI
- Relevance: 3.479281787886308
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.22127v1
- PDF: https://arxiv.org/pdf/2608.22127v1
- Local PDF: pdf/2026-08-26_05_Who Should Teach_ Confidence-Aware Dual-Teacher Learning for Few-Shot Node Classification on Text-Attributed Graphs.pdf

Text-Attributed Graphs (TAGs) integrate graph structures and node-associated textual attributes, and recent studies have increasingly leveraged Large Language Models (LLMs) to improve TAG learning in few-shot settings. However, existing approaches typically utilize LLM-derived information uniformly across all nodes, despite substantial variations in its reliability, while also incurring considerable monetary costs. We argue that the most appropriate source of supervision may differ across nodes, as Graph Neural Networks (GNNs) and LLMs exhibit complementary strengths in exploiting structural and semantic information, respectively. To this end, we propose CoTeach, a Confidence-aware dual-teacher learning framework that dynamically selects the more reliable teacher for each node. Experimental results demonstrate that CoTeach consistently improves few-shot node classification performance while reducing unnecessary LLM utilization and associated monetary costs.

## 6. Think with Structured Grounding: Perceptual Reinforcement Learning for Chart and Visual-Tabular Understanding

- Authors: Changjiang Jiang, Qiannian Zhao, Lei Xin, Jinxiang Xie, Preslav Nakov, Zhuohan Xie
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-23
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 3.4107852768510716
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.22429v1
- PDF: https://arxiv.org/pdf/2608.22429v1
- Local PDF: pdf/2026-08-26_06_Think with Structured Grounding_ Perceptual Reinforcement Learning for Chart and Visual-Tabular Understanding.pdf

Multimodal Large Language Models (MLLMs) capable of thinking with images often rely on external tools for fine-grained perception. However, this reliance introduces significant inference latency and fails to effectively resolve the spatial-structural gap-a fundamental challenge in text-dense and structurally relational visuals (e.g., charts and visual tables) where strict relative spatial arrangements bind textual elements. Without external tools, standard MLLMs struggle with such fine-grained visual reasoning tasks. To address these issues, we propose Think with Structured Grounding (TwSG), a novel fine-grained image perception framework designed to internalize complex images's tool-use capabilities within the model. TwSG distills the benefits of multi-step reasoning and micro-cropping into a single efficient forward pass during inference. Specifically, we use an MLLM to identify key regions guided by ground-truth answers, and then prompt a teacher model to generate high-quality visual question-answering (VQA) data. These fine-grained, region-based supervisory signals are subsequently distilled back into the full-image representation. Our training pipeline consists of two stages: (1) a cold-start supervised fine-tuning (SFT) phase using multi-turn data with focused area descriptions to foster complex reasoning and error recovery; and (2) a reinforcement fine-tuning (RFT) phase driven by a novel process reward mechanism, TL-GRPO, which encourages strategic reasoning. Extensive experiments across various MLLM architectures demonstrate that TwSG reduces inference latency while substantially improving accuracy and robustness, endowing models with native fine-grained region description and flexible reasoning capabilities.

## 7. Joint Causal Structure and Cluster Discovery Using Variational Inference

- Authors: Avni Rajpal, Anubhav Kumar, Rishabh Karnad, Mohammad Emtiyaz Khan, P. K. Srijith
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-23
- DOI: Unavailable
- Categories: cs.LG, cs.AI, stat.ML
- Relevance: 3.326722780511808
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.22212v1
- PDF: https://arxiv.org/pdf/2608.22212v1
- Local PDF: pdf/2026-08-26_07_Joint Causal Structure and Cluster Discovery Using Variational Inference.pdf

Causal discovery aims to understand the relationships between individual random variables. In many applications, such as brain imaging and climate modeling, it is more meaningful to consider interactions among groups of variables. Existing methods assume that knowledge of such groups or clusters is explicitly available when modeling interactions. However, in practice, these clusters as well as the causal relationships among them, are latent. In this paper, we present a novel approach based on variational inference to simultaneously infer both the latent clusters and causal structures. We learn an approximate posterior over clusters and graph-structure by considering variational distributions based on categorical and Bernoulli models respectively. We derive variational lower bounds and estimation techniques to learn variational and model parameters. The effectiveness of our proposed methods for cluster and causal discovery are demonstrated on both synthetic and real data sets.

## 8. Mol-JEPA: A multimodal Joint Embedding Predictive Architecture for Molecules

- Authors: Florian Rottach, Sebastian Schieferdecker, William Rudman, Randall Balestriero, Carsten Eickhoff
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-23
- DOI: Unavailable
- Categories: cs.LG, cs.AI
- Relevance: 3.3110354582819843
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.22642v1
- PDF: https://arxiv.org/pdf/2608.22642v1
- Local PDF: pdf/2026-08-26_08_Mol-JEPA_ A multimodal Joint Embedding Predictive Architecture for Molecules.pdf

Despite recent advances in molecular foundation models, several limitations remain, such as chemically invalid augmentations, modality collapse, and incomplete representation of biochemical environments. To address these challenges, we present \textbf{Mol-JEPA}, a scalable framework for learning molecular world models. Rather than relying on suboptimal molecular perturbations, our model uses modality masking to exploit information from molecular structures, cellular phenotypes, binding affinities, ADMET profiles, quantum chemistry simulations and other drug discovery data. Across various benchmarks, we show that the representations learned by Mol-JEPA deliver strong performance, demonstrating the value of incorporating biochemical context through latent space prediction.

## 9. Bi-EZP: LLM-Guided Bilevel Program Evolution for Ensemble Zero-Cost Proxy Discovery

- Authors: Yutao Lai, Kezhao Lai, Hai-Lin Liu
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-22
- DOI: Unavailable
- Categories: cs.LG, cs.AI
- Relevance: 3.2047876480066826
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.21927v1
- PDF: https://arxiv.org/pdf/2608.21927v1
- Local PDF: pdf/2026-08-26_09_Bi-EZP_ LLM-Guided Bilevel Program Evolution for Ensemble Zero-Cost Proxy Discovery.pdf

Zero-cost proxies enable neural architecture search (NAS) to rank candidate networks from statistics computed at initialization, avoiding repeated training. However, different proxies capture different properties and often produce inconsistent rankings across search spaces. Ensemble proxies can combine complementary signals, but automated discovery must optimize both discrete aggregation structures and their continuous coefficients, making structural quality difficult to separate from parameter calibration. We propose Bi-EZP, a bilevel framework that decouples these decisions. At the upper level, a large language model generates executable aggregation programs over four complementary base proxies with program-specific parameter bounds. At the lower level, covariance matrix adaptation evolution strategy (CMA-ES) optimizes the continuous parameters of each fixed program on an inner training split. The calibrated programs are then evaluated using Kendall's rank correlation on a disjoint validation split, enabling evolutionary selection to favor structures that generalize beyond their calibration data. Experiments on NATS-Bench and Network Design Spaces evaluate ranking performance across heterogeneous search spaces, and DARTS experiments assess downstream architecture search. Results show that separating program discovery from numerical calibration provides an effective approach to automated ensemble zero-cost proxy construction. The source code is available at: https://anonymous.4open.science/r/Bi-EZP-318D

## 10. Hierarchy-Aware Semantic Losses for Knowledge Graph Link Prediction

- Authors: Filip Kronström, Ross D. King
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-24
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.2042132973584456
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.22981v1
- PDF: https://arxiv.org/pdf/2608.22981v1
- Local PDF: pdf/2026-08-26_10_Hierarchy-Aware Semantic Losses for Knowledge Graph Link Prediction.pdf

Knowledge graphs are often accompanied by ontological class hierarchies that encode valuable semantic information, yet many link prediction methods either ignore such hierarchies or incorporate them indirectly through additional graph edges. Recent work introduced hierarchy-aware graph neural networks (GNNs), which use semantic losses derived from box embeddings to encourage satisfaction of subclass relationships during GNN-based representation learning. While this approach has shown promise for biological regression tasks, its effectiveness for knowledge graph link prediction has not been investigated.
  In this paper we evaluate hierarchy-aware semantic losses on link prediction across three benchmark datasets: AIFB, CoDEx, and BioKG. We combine graph neural network encoders with box-embedding-based semantic losses that encourage learned representations to better satisfy ontology-derived class hierarchies, and compare this approach to both standard link prediction models and models incorporating subclass relations as graph edges. Across all datasets, hierarchy-aware semantic losses significantly improve mean reciprocal rank (MRR) and consistently outperform models that incorporate hierarchy information through additional subclass edges. Relative to the baseline GNN models, MRR improved by 7.6%, 2.4%, and 15.5% on AIFB, CoDEx, and BioKG, respectively. Furthermore, semantic losses consistently outperform the alternative of augmenting the graph with subclass edges.
  These results are consistent with ontology-derived class hierarchies providing complementary information to graph structure, and suggest that encouraging hierarchical consistency through semantic losses is an effective and comparatively parameter-efficient mechanism for improving knowledge graph link prediction.

## 11. Barycentric Fused Gromov-Wasserstein Balancing for Causal Inference under Multiple Treatments

- Authors: Yuki Murakami, Takumi Hattori, Kohsuke Kubota
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-22
- DOI: Unavailable
- Categories: stat.ME, cs.AI, cs.LG, stat.ML
- Relevance: 3.1719022543862057
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.22024v1
- PDF: https://arxiv.org/pdf/2608.22024v1
- Local PDF: pdf/2026-08-26_11_Barycentric Fused Gromov-Wasserstein Balancing for Causal Inference under Multiple Treatments.pdf

Estimating heterogeneous single and interaction treatment effects from observational data under multiple simultaneous treatments is crucial for decision-making. To mitigate estimation variance, previous studies balance representation distributions between every pair of treatment patterns. However, such pairwise balancing scales quadratically with the number of treatment patterns and fails to preserve consistent local proximity structures across patterns, which degrades counterfactual estimation. To address these challenges, we propose the Causal Inference for Heterogeneous Single and Interaction Treatment Effects Network (CIHSI-Net), a deep learning framework built on a novel Barycentric Fused Gromov-Wasserstein Balancing (BFG-WB) objective. BFG-WB aligns the representation distribution of each treatment pattern with a shared Wasserstein barycenter, achieving global alignment while reducing the computational complexity from quadratic to linear, and its Fused Gromov-Wasserstein discrepancy preserves the local proximity structures essential for reliable heterogeneous effect estimation. Simulation studies show that CIHSI-Net consistently outperforms state-of-the-art baselines, and an application to real-world marketing data demonstrates its practical utility in complex multi-treatment scenarios.

## 12. GET: Generative Embedding Translation for Medical Image Segmentation

- Authors: Md Maklachur Rahman, Md Hasan Al Banna, Saraf Anjum, Mahmudul Hasan, Tracy Hammond
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-23
- DOI: Unavailable
- Categories: eess.IV, cs.CV, cs.LG
- Relevance: 3.170929027844034
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.22619v1
- PDF: https://arxiv.org/pdf/2608.22619v1
- Local PDF: pdf/2026-08-26_12_GET_ Generative Embedding Translation for Medical Image Segmentation.pdf

Generative segmentation provides an alternative to direct pixel-wise prediction by operating on learned latent representations, but effective image-to-mask translation must preserve target structure while remaining computationally efficient. We propose Generative Embedding Translation (GET), a structured embedding-translation framework that progressively transforms image embeddings into mask embeddings within the frozen latent space of a Stable Diffusion VAE. GET uses a U-Net-style Embedding Translation Network with 1.07M trainable parameters, combining Mobile Bottleneck Convolutions, Subsampled Self-Attention, and Multi-scale Feature Enrichment for local modeling, global context, and multi-scale refinement. Across five medical segmentation datasets, GET outperforms generative, CNN, and Transformer baselines. Compared with the strongest generative baseline, GMS, GET improves average Dice and IoU by 0.93% and 1.26%, reduces HD95 by 0.81 pixels, and uses 31.41% fewer trainable parameters. Under bidirectional BUS-BUSI domain shift, GET further improves Dice and IoU by 3.51% and 3.39%, while reducing HD95 by 27.37 pixels. Our code is available at: https://github.com/maklachur/GET.

## 13. Clinical Graph-JEPA: Predictive Patient-State Knowledge Graphs for Cognitive Decision Support

- Authors: Kushagra Yadav, Nalin Prabhath, Amit Lamba, Goeun Han, Yining Mao
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-23
- DOI: Unavailable
- Categories: cs.LG, cs.AI
- Relevance: 3.162491809982119
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.22583v1
- PDF: https://arxiv.org/pdf/2608.22583v1
- Local PDF: pdf/2026-08-26_13_Clinical Graph-JEPA_ Predictive Patient-State Knowledge Graphs for Cognitive Decision Support.pdf

Clinical records contain rich evidence about patient state, but converting that evidence into reliable, structured knowledge graphs remains difficult because extraction errors, ontology mismatch, missing relations, and temporal ambiguity can propagate into downstream systems. We propose a clinical knowledge graph construction and refinement framework that combines multi-agent relation proposal, ontology-aware normalization, deterministic evidence scoring, and JEPA-based latent refinement. Rather than treating a clinical knowledge graph as a static extraction artifact, we treat it as a predictive patient-state representation. For each admission, the system constructs an evidence-scored graph from structured MIMIC-IV records and inferred clinical cross-links, then learns to recover held-out clinical relations from the observed graph context. We evaluate the refiner with leakage-free leave-one-out edge recovery (MRR and Hits@k) and held-out batch-mask evaluation (AUC and MRR). To isolate the contribution of discharge-note context, we compare a note-embedding-free configuration with a note-augmented configuration that injects real discharge-note representations only into note-grounded entities. Under the same cohort and evaluation protocol, entity-grounded note injection improves overall leave-one-out MRR by 31% relative improvement.

## 14. RIBOSPAN: A Long-Context RNA Foundation Model for Versatile RNA Modeling

- Authors: Ziyuan Wang, Bohao Tang, Fei Zhang, Shuo Han, Pengfei Liu
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-24
- DOI: Unavailable
- Categories: cs.LG, q-bio.GN
- Relevance: 3.144938989064433
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.22849v1
- PDF: https://arxiv.org/pdf/2608.22849v1
- Local PDF: pdf/2026-08-26_14_RIBOSPAN_ A Long-Context RNA Foundation Model for Versatile RNA Modeling.pdf

Full-length RNAs, particularly messenger RNAs, often exceed the context lengths used to pretrain existing RNA foundation models, limiting complete-transcript modeling at single-nucleotide resolution. We present RIBOSPAN, a 1.61-billion-parameter bidirectional RNA foundation model natively pretrained with context lengths up to 10,240 nt. RIBOSPAN combines dense bidirectional self-attention, single-nucleotide tokenization, and attention-isolated sequence packing to enable high-resolution modeling of complete long RNAs. We evaluate the model through nucleotide reconstruction, a controlled long-context representation benchmark, and frozen RNA-type representation analysis. Native 10K pretraining preserves strong reconstruction at 10,240 tokens, while continued pretraining with 40% masking improves recovery under heavy corruption while preserving representation quality. The long-context benchmark further shows that native 10K models maintain strong contextual responsiveness and context-specific representation separation while keeping perturbation-induced representation changes highly localized. Inference-time YaRN scaling recovers much of the contextual organization lost by direct extrapolation of short-context models, but induces substantially greater distal representation diffusion. Frozen-representation evaluations further demonstrate state-of-the-art RNA representation quality, with RIBOSPAN achieving the strongest overall performance across diverse RNA types and retaining a clear advantage on long RNAs. Building on the same backbone, we develop a multidimensionally conditioned discrete-diffusion framework for full-length mRNA generation and redesign, including synonymous-codon diffusion for protein-preserving CDS optimization. Together, RIBOSPAN establishes a powerful long-context foundation for transferable RNA representation learning and full-transcript mRNA design.

## 15. Compositional Chain-of-Relations for Faithful Knowledge Graph Question Answering with Large Language Models

- Authors: Chenhui Liu, Jianpeng Zhou, Jiahai Wang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-24
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 3.082126475393536
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.22762v1
- PDF: https://arxiv.org/pdf/2608.22762v1
- Local PDF: pdf/2026-08-26_15_Compositional Chain-of-Relations for Faithful Knowledge Graph Question Answering with Large Language Models.pdf

Knowledge graph question answering (KGQA) is a key task for evaluating KG-augmented Large Language Models (LLMs), and complex KGQA that requires multi-hop reasoning is especially challenging. Solving a complex query involves two coupled phases: candidate retrieval, which locates answer candidates over the KG, and constraint handling, which filters these candidates against the query constraints. Faithful reasoning requires grounding both phases in the KG. However, existing agent-based methods ground candidate retrieval through entity-centric exploration, while leaving constraint handling to the LLM's internal knowledge, which leads to two critical limitations. (1) Unreliable entity pruning: entity-centric exploration uses entities as search units and must prune them to a fixed-size subset at each hop. Because entity information in KGs is often incomplete and a fixed-size subset cannot retain all valid entities, such pruning inevitably drops valid entities and ultimately leads to wrong answers. (2) Ungrounded constraint handling: query constraints are resolved from the LLM's internal knowledge rather than the KG, leaving the final answers unverifiable and prone to hallucination. To address these limitations, this paper introduces a relation-centric exploration paradigm, which uses relations rather than entities as search units and thus avoids unreliable entity pruning. Built on this paradigm, this paper proposes Compositional Chain-of-Relations (CCoR), a simple and effective framework that grounds both phases in the KG with two relation chains: a main chain for candidate retrieval and a constraint chain that verifies query constraints through explicit KG exploration. Experiments on four KGQA benchmarks show that CCoR consistently improves accuracy, faithfulness, and efficiency over strong baselines, with more pronounced gains on complex queries.

## 16. Toward Effective and Reliable LLM Agents via Dynamic Ontology

- Authors: Xiaohui Zhang, Zequn Sun, Chengyuan Yang, Yuanning Cui, Lingbing Guo, Wei Hu
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-24
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 3.061348367179761
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.22974v1
- PDF: https://arxiv.org/pdf/2608.22974v1
- Local PDF: pdf/2026-08-26_16_Toward Effective and Reliable LLM Agents via Dynamic Ontology.pdf

Large language model (LLM) agents rely heavily on knowledge encoded in model parameters or presented as unstructured context. In domain-specific tasks, this leaves important semantic connections implicit. This often results in incomplete evidence use and brittle multi-step decisions. Ontologies offer a way to externalize domain concepts and relations as machine-interpretable structures, but constructing task-usable ontologies traditionally requires substantial effort from domain experts and is difficult to scale. Automatic construction is also challenging: an ontology that appears semantically plausible may not contain the relational structures needed for actual decision making. We present OaK, an ontology-as-a-kernel framework that dynamically constructs and refines task-oriented ontologies for LLM agents. Given task requirements and training data, OaK constructs an ontology and its knowledge graph, generates task-adaptation functions for graph reasoning, and uses judge feedback to iteratively refine both. By making relevant concepts and relations explicit, the ontology grounds knowledge retrieval and multi-step decision making. We evaluate OaK on TravelPlanner, CRMArenaPro, and ToolQA. Results show that OaK improves standard LLM agents, strengthens evidence grounding, and boosts the reliability of multi-step reasoning.

## 17. CD-LoRA: Consistency-Driven Low-Rank Adaptation for Multi-Task Fine-Tuning

- Authors: Qian Zha, Jinda Liu, Yuan Wu, Yi Chang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-22
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.0457090255585144
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.21909v1
- PDF: https://arxiv.org/pdf/2608.21909v1
- Local PDF: pdf/2026-08-26_17_CD-LoRA_ Consistency-Driven Low-Rank Adaptation for Multi-Task Fine-Tuning.pdf

While Multi-Task Learning (MTL) is essential for adapting Large Language Models (LLMs) to diverse domains, prevailing LoRA-based methods rely on complex routing mechanisms that partition task-specific knowledge. In this work, we reveal that such routing-based designs are prone to a training-inference discrepancy, where stochastic routing decisions under distribution shifts compromise inference stability. Driven by a second-order Taylor analysis that exposes the instability induced by routing variance, we challenge the training-inference discrepancy and propose Consistency-Driven Low-Rank Adaptation (CD-LoRA). By eliminating routers entirely, CD-LoRA employs a consistency-driven alignment mechanism to enforce representation congruence across tasks in a shared low-rank space. This paradigm fosters robust, task-agnostic features without explicit partitioning overhead. Extensive experiments show that CD-LoRA consistently outperforms state-of-the-art multi-adapter baselines, offering a simpler, router-free, and more stable solution for multi-task PEFT. The code is available at the anonymous link https://github.com/zhaqian21/CD-LoRA.

## 18. Reservoir of Importance: Learning Semi-Structured Sparsity with Differentiable Subset Sampling

- Authors: Ha Dinh, Xuan Duy Ta, Khoat Than, Khac-Hoai Nam Bui
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-24
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.030662322822024
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.23048v1
- PDF: https://arxiv.org/pdf/2608.23048v1
- Local PDF: pdf/2026-08-26_18_Reservoir of Importance_ Learning Semi-Structured Sparsity with Differentiable Subset Sampling.pdf

Semi-structured $N$:$M$ sparsity has emerged as a practical direction for accelerating large language models (LLMs). However, existing learnable-mask approaches incur substantial parameter and memory overhead, limiting their scalability to large models and aggressive sparsity regimes. In this work, we revisit semi-structured pruning from a perspective that reconciles efficiency with scalability. We propose Reservoir of Importance (RoI), a lightweight semi-structured pruning framework that learns sparsity masks through differentiable subset sampling. Unlike prior methods that model full categorical distributions over all feasible $N$:$M$ patterns, RoI introduces a compact-logit parameterization for sparsity mask learning and performs sampling without replacement to select masks, thereby reducing trainable parameters from combinatorial complexity to $\mathcal{O}({M})$. As a result, RoI requires 1.5-8.75$\times$ fewer learnable parameters and significantly lower memory cost, while remaining fully aligned with hardware-friendly sparsity patterns. Extensive evaluations across multiple scales of the Qwen2.5 LLM family (0.5-7B parameters) demonstrate that RoI achieves competitive performance with strong memory efficiency, stability, and scalability to more aggressive $N$:$M$ sparsity patterns, offering a practical path toward efficient LLM deployment.

## 19. ProxyFormer: A Dual-Stream Proxy Architecture for Ultra-Long Context and High-Resolution Generation

- Authors: Zhongpan Tang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-24
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.0303962636383064
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.23463v1
- PDF: https://arxiv.org/pdf/2608.23463v1
- Local PDF: pdf/2026-08-26_19_ProxyFormer_ A Dual-Stream Proxy Architecture for Ultra-Long Context and High-Resolution Generation.pdf

The quadratic growth of attention computation and key-value (KV) cache with respect to sequence length is a central bottleneck for ultra-long-context language models and high-resolution generative models. We propose ProxyFormer, a general dual-stream architecture built upon proxy tokens. In each layer, fine-grained local features are compressed bottom-up into a small set of proxy states; expensive global interactions are performed only in the compressed proxy space; the globally contextualized proxies are then decompressed and injected top-down back into the local stream. Because the local stream persists across layers, fine-grained information that is not captured by one compression step remains accessible for later refinement, alleviating the irreversible information loss of conventional one-shot compression. We further introduce factorized multi-level compression/decompression, layer-wise dynamic compression ratios, asymmetric dual embeddings, and a proxy-only KV-cache inference scheme. On a 16GB GPU with batch size 1, a standard decoder-only model can train sequences of only about 20K tokens, whereas ProxyFormer with a compression ratio of 64 extends the trainable sequence length to about 0.7M. A model trained with a 64K window retains 92%-95% retrieval accuracy on a multi-needle retrieval task with 1,048,576 tokens, and a model trained with an 8K window exceeds 94% accuracy when extrapolated to 256K tokens. Preliminary image-generation experiments demonstrate the feasibility of ProxyFormer for both pixel-space and latent-space flow matching.

## 20. SAFE-G: Structure-aware Faithful Evidence-guided Generation for Knowledge-based Visual Question Answering

- Authors: Long Shu, Shuochen Liu, Wei Chen, Junda Lin, Zhi Zheng, Huijun Hou, Tong Xu
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-22
- DOI: Unavailable
- Categories: cs.CV, cs.AI
- Relevance: 3.0292253266479063
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.21796v1
- PDF: https://arxiv.org/pdf/2608.21796v1
- Local PDF: pdf/2026-08-26_20_SAFE-G_ Structure-aware Faithful Evidence-guided Generation for Knowledge-based Visual Question Answering.pdf

Knowledge-based Visual Question Answering (KB-VQA) aims to answer queries that necessitate reasoning over external knowledge sources beyond the visual content. Typically, current methods fuse multimodal features to retrieve external information, subsequently leveraging Multimodal Large Language Models (MLLMs) to derive answers from the retrieved evidence. However, these methods often struggle to capture structural associations within complex contexts to effectively filter noise. Furthermore, they frequently fail to ensure that the reasoning process remains strictly faithful to the retrieved evidence. To address these challenges, we propose SAFE-G, a Structure-Aware Faithful Evidence-guided Generation framework, which enables precise evidence localization and trustworthy reasoning. Specifically, we first employ a coarse-grained hybrid search fusing visual and textual modalities to recall candidate documents, and subsequently implement a structure-aware fine-grained graph retrieval that captures structural dependencies to filter noise and pinpoint precise evidence. Moreover, we introduce a reinforcement learning (RL) strategy with an evidence-grounded reward that assigns credit to correct answers only when the selected evidence is correct. This strict alignment constraint compels the model to anchor its response in the retrieved context, effectively enhancing its capability to locate evidence via multimodal features and perform faithful reasoning. Extensive experiments on the Encyclopedic-VQA and InfoSeek benchmarks demonstrate that SAFE-G outperforms prior methods by a margin of 8.9% and 3.5%, substantially enhancing the overall reasoning accuracy. Our source code is publicly available at: https://github.com/MINE-USTC/SAFE-G.

## 21. ADMIL: Attention-Distilled Multiple Instance Learning for Selective Foundation Model Inference in Pathology

- Authors: Duncan Stothers, Ren-Chin Wu, William Lotter
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-22
- DOI: Unavailable
- Categories: cs.CV, cs.AI, cs.LG
- Relevance: 3.014830330286223
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.22066v1
- PDF: https://arxiv.org/pdf/2608.22066v1
- Local PDF: pdf/2026-08-26_21_ADMIL_ Attention-Distilled Multiple Instance Learning for Selective Foundation Model Inference in Pathology.pdf

Attention-based multiple instance learning (ABMIL) using pathology foundation model embeddings is effective for slide-level tasks, but exhaustive inference requires applying a large image encoder to every foreground tile despite the subsequent attention distribution often concentrating over a small subset of informative regions. We introduce ADMIL (Attention-Distilled Multiple Instance Learning), a selective-compute framework that distills an ABMIL teacher's attention into a lightweight tile-selection model, PriorNet. Using an EfficientNet architecture, PriorNet learns the teacher attention distribution from raw tile pixels with KL divergence; at inference, it scores the foreground pool, selects the top-K tiles, and invokes the expensive foundation model only on that subset before a selected-bag ABMIL student predicts the slide label. Across BRACS, PANDA, and CAMELYON16, ADMIL matches full-teacher headline performance at K=4, 8, and 128 tiles, respectively, avoiding >98% of foundation model (Virchow2) tile embeddings and model inference FLOPs. Random and teacher-attention oracle controls show that this result depends on task-relevant selection rather than tile-count reduction alone. Quantitative and qualitative analyses suggest that PriorNet recovers the teacher's tile ordering with high fidelity while focusing on task-relevant morphological regions. ADMIL shows that nearly all expensive tile encodings can be removed without sacrificing slide-level performance, providing a potential path for more efficient deployment in clinical settings where latency and compute costs are key considerations.

## 22. Read Less, Solve More: Token-Efficient Sparse Reading for AI Agents

- Authors: Zedong Liu, Jiaan Wu, Xinyang Ma, Le Xu, Kai Wang, Yuanchao Hu, Dingwen Tao, Guangming Tan
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-23
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 3.011600070073721
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.22237v1
- PDF: https://arxiv.org/pdf/2608.22237v1
- Local PDF: pdf/2026-08-26_22_Read Less, Solve More_ Token-Efficient Sparse Reading for AI Agents.pdf

Long-horizon agents increasingly rely on repeated access to external artifacts, yet current reading interfaces often expose entire objects even when only sparse evidence is needed. This over-reading increases token and latency costs and can dilute task-relevant evidence, while existing context-reduction methods mainly intervene after broad content has already entered the trajectory. We present SparseRead, a training-free, model-transparent reading layer that controls content admission before unnecessary evidence reaches the model context. SparseRead combines a regime-aware Read Gate, extensible Reader Backends, and a stateful protocol for bounded, source-anchored evidence acquisition with explicit refinement, verification, stopping, and fallback. Across six frontier models, including Claude Opus 5, and five workload scenarios, SparseRead reduces token volume by up to 92.9% and wall time by up to 89.0%, while preserving or improving task quality. Its consistent gains across three agent frameworks further demonstrate broad portability.

## 23. Cross-Domain, Multi-Task Data-to-Text Generation without In-Domain Training Data

- Authors: Yifei Song, Kun Efimov-Zhang, Claire Gardent
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-24
- DOI: Unavailable
- Categories: cs.CL, cs.AI
- Relevance: 3.0082764502631774
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.23391v1
- PDF: https://arxiv.org/pdf/2608.23391v1
- Local PDF: pdf/2026-08-26_23_Cross-Domain, Multi-Task Data-to-Text Generation without In-Domain Training Data.pdf

Structured data exists in many forms (tables, knowledge graphs, charts, and time series), and converting it into text may involve different generation tasks. However, most prior work on data-to-text (D2T) generation has focused on specific tasks and datasets, relying either on task-specific training data or on the zero-shot capabilities of large language models. We study cross-domain D2T generation in a setting where neither in-domain training text nor test references are available, and where domains, generation goals, and input structures vary substantially. We compare data-driven knowledge distillation (DDKD) against zero-shot inference and fine-tuning on out-of-domain D2T data, and introduce structure-preserving augmentation via structural subsampling and perturbation. Experiments on five benchmarks show that, at constant model size (1.7B parameters), DDKD consistently outperforms both fine-tuning and zero-shot inference. Moreover, the resulting small models outperform a much larger finetuned model on two of the five domains, achieving comparable performance on the remaining three. We further construct QUINTD-5, a fivefold extension of QUINTD-1, and show that simply scaling real target-domain inputs yields only modest gains, whereas our augmentation strategy remains more effective and more cost-efficient for cross-domain distillation.

## 24. AgentWeave: Routing Before Reasoning for Efficient Function Calling in Tool-Rich Language Models

- Authors: Saurav Singla, Aarav Singla, Advik Gupta, Parnika Gupta
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-24
- DOI: Unavailable
- Categories: cs.AI, cs.CL
- Relevance: 2.9970938384292496
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.23078v1
- PDF: https://arxiv.org/pdf/2608.23078v1
- Local PDF: pdf/2026-08-26_24_AgentWeave_ Routing Before Reasoning for Efficient Function Calling in Tool-Rich Language Models.pdf

Large language models increasingly operate over large collections of tools, functions, APIs, and specialized agents. As the candidate action space grows, a function-calling model must process more schemas, consume more prompt tokens, and distinguish among increasingly similar or irrelevant alternatives. We study a complementary systems strategy: reduce the candidate set before language-model inference while leaving the downstream model unchanged. We introduce AgentWeave, a deterministic pre-inference routing layer that constructs a bounded model-visible action space using eligibility, requirement, capability, and routing signals. We evaluate AgentWeave with a frozen BFCL-derived routing-pressure protocol using the public MadeAgents/Hammer2.1-1.5b model. On 48 fresh BFCL V4 multiple-function tasks, AgentWeave achieves 6/48 (12.5%) native BFCL successes, whereas all-tools, deterministic random top-8, and semantic top-8 baselines each achieve 0/48. The paired success difference is +12.5 percentage points with a 10,000-resample paired bootstrap 95% confidence interval of +4.17 to +22.92 points and exact McNemar p=0.03125. Relative to all-tools exposure, AgentWeave presents 70.18% fewer tools, uses 61.70% fewer input tokens, and exhibits 50.95% lower mean local-model latency. The result is deliberately narrow: this is a BFCL-derived routing-pressure study rather than an official full BFCL leaderboard score, and absolute task success remains low. The evidence nevertheless shows that candidate-space construction can materially affect a fixed model's function-calling behavior and motivates evaluating routing as a distinct stage before model reasoning.

## 25. Object-Uni: A Unified Model for Object-Centric Spatial Understanding and Controllable Generation

- Authors: Mining Tan, Yinuo Wang, Ziqi Zhou, Weize Quan, Sifei Li, Jingdong Chen, DanDan Zheng, Libin Wang, Weiming Dong
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-24
- DOI: Unavailable
- Categories: cs.CV, cs.AI
- Relevance: 2.9970568818026044
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.22757v1
- PDF: https://arxiv.org/pdf/2608.22757v1
- Local PDF: pdf/2026-08-26_25_Object-Uni_ A Unified Model for Object-Centric Spatial Understanding and Controllable Generation.pdf

Unified models for visual understanding and generation have made rapid progress, yet they still lack the ability to understand and manipulate the spatial states of object instances. Existing models can describe objects in natural language, but they struggle to precisely represent continuous object poses and generate geometrically consistent images under target viewpoints. To mitigate this, we propose \emph{Object-Uni}, a unified model for object-centric spatial understanding and controllable generation. Specifically, we formulate object-centric spatial intelligence as a unified problem connecting pose perception, spatial reasoning, pose-conditioned generation, and object-centric novel view synthesis. We treat object pose as an explicit geometric variable shared by understanding and generation, rather than merely a prediction label or control signal. To make pose usable by multimodal large language models, we propose a viewpoint-based orientation abstraction that maps orientation into structured viewpoint descriptions while preserving continuous geometric supervision. We further construct an object-centric spatial benchmark (UniSpatial-80K) and train a unified model with an object-token-grounded pose anchor to associate each instance with its pose state. Experiments show that our model improves object-level pose understanding and pose-controllable generation, moving unified models from describing objects toward manipulating spatial states.

## 26. Resilient Concurrent Causal Discovery for Topological Event Sequences

- Authors: Jiyu Tian, Junhao Dong, Mingchu Li, Lingling Fang, Liming Chen, Andreas Holzinger, Zheng Yan, Yew Soon Ong
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-22
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 2.987452148505807
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.21815v1
- PDF: https://arxiv.org/pdf/2608.21815v1
- Local PDF: pdf/2026-08-26_26_Resilient Concurrent Causal Discovery for Topological Event Sequences.pdf

Causal discovery on topological event sequences is crucial for ensuring the reliability of networks. However, existing methods struggle to capture the complex causal relationships arising from concurrent events and lack robustness to incomplete event sequences. To address these issues, we propose a resilient concurrent causal discovery method, termed RCCD, enabling robust learning of causal graphs from topological event sequences. Specifically, we first introduce an influence-aware hyperedge causal attention mechanism, which incorporates event duration into the embedding representation, aggregates concurrent event features via hyperedge causal convolution, and injects network prior knowledge to capture the complex many-to-one causal interactions. Furthermore, we design a masked-based alternating causal optimization framework, which forces the model to recover masked event types based on context through self-supervised mask reconstruction, thereby enhancing the resilience of the predictor to missing data. To validate the effectiveness of our method, we conduct extensive experiments on both simulated and real-world telecommunication network datasets. Experimental results demonstrate that the proposed method significantly outperforms existing state-of-the-art methods in both accuracy and robustness, making it more suitable for real-world telecommunication network environments.

## 27. Graph Representation Learning of Lightweight IoT Ciphers

- Authors: Jonathan Cook, Sabih ur Rehman, M. Arif Khan
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-24
- DOI: Unavailable
- Categories: cs.LG, cs.CR
- Relevance: 2.977677602116386
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.23054v1
- PDF: https://arxiv.org/pdf/2608.23054v1
- Local PDF: pdf/2026-08-26_27_Graph Representation Learning of Lightweight IoT Ciphers.pdf

SIMON and SIMECK belong to a family of Lightweight Cryptographic Algorithms (LCAs) based on the Feistel block cipher, designed for Internet of Things (IoT) devices. As with all Feistel ciphers, they are susceptible to differential cryptanalysis, necessitating rigorous resilience evaluations. While state-of-the-art techniques leverage heuristics and sampling to improve efficiency, little work has applied Machine Learning (ML) guided Graph Representation Learning (GRL) to efficiently identify and visualise high-probability differential clusters. We address this gap by introducing an efficient feature engineering strategy that extracts four differential attributes from a partial Difference Distribution Table (pDDT), revealing structural information concealed in raw differential data. Utilising the enriched features, we construct and compare three ML-guided directed graphs for SIMON$32$ and SIMECK$32$ using K-Nearest Neighbour (KNN), Decision Trees (DT), and Random Forests (RF). To the best of our knowledge, our framework produces the first graph-based visualisation of the differential clustering effect, in which high-probability single-bit differentials form geometrically close clusters in the learned embedding. All three models achieve a precision of $1.0$ in identifying high-probability differentials, confirming zero false positives. KNN achieves the strongest cluster separation, the highest F1 score and the lowest graph construction time of approximately $2.3$ seconds, while DT and RF produce optimal paths with near-perfect regression. The results are consistent across both LCAs, demonstrating the applicability of the framework to other AND-rotation LCA families.

## 28. Self-Supervised Graph Representation Learning for In-The-Wild Wearable and Smartphone based Emotion Recognition

- Authors: Ioannis N. Ziogas, Leontios J. Hadjileontiadis, Ahsan H. Khandoker, Aamna Al Shehhi
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-23
- DOI: 10.1109/ICASSP49660.2025.10888648
- Categories: cs.LG, cs.AI, eess.SP
- Relevance: 2.9522603064163984
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.22387v1
- PDF: https://arxiv.org/pdf/2608.22387v1
- Local PDF: pdf/2026-08-26_28_Self-Supervised Graph Representation Learning for In-The-Wild Wearable and Smartphone based Emotion Recognition.pdf

Wearable and smartphone-based emotion recognition (WER) remains a challenging setting in affective computing, due to the notorious difficulty and bias associated with in-the-wild label collection. The high inter-and intra-subject emotional variability motivates us to explore WER modeling through graph node classification in a limited resources learning scheme powered by Self-Supervised Learning (SSL) graph masking augmentation tasks. We employ a subgraph sampling approach during training, utilizing labeled and unlabeled data, along with supervised, semi-supervised, and SSL mechanisms in a multi-task inductive graph neural network architecture. Our evaluations on K-EmoPhone through leave-one-group-out cross-validation in the binary arousal and valence tasks yield average accuracy gains of 4.3% and 7.8%, compared to the full resource setting, utilizing only 20% and 25% of the labels, respectively. Our model analysis sheds light on the relation of SSL graph augmentations to emotional arousal and valence and justifies the approach of SSL-driven subgraph training for in-the-wild WER.

## 29. SchemaRouter: Field-Aware Tool Routing for Efficient Heterogeneous Agentic RAG

- Authors: Yong-eun Cho
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-03
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 2.946654312577902
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.21375v1
- PDF: https://arxiv.org/pdf/2608.21375v1
- Local PDF: pdf/2026-08-26_29_SchemaRouter_ Field-Aware Tool Routing for Efficient Heterogeneous Agentic RAG.pdf

Heterogeneous agentic retrieval-augmented generation (RAG) systems increasingly orchestrate external APIs, internal databases, vector stores, and graph stores. Exposing all tool descriptions to an LLM agent, or selecting tools only by vector similarity, causes two costly failures: over-fetching, which increases payload size, token use, and latency, and under-fetching, which omits fields needed to answer the query.
  We present SchemaRouter, a lightweight routing layer that represents tools, endpoints, parameters, response fields, domain concepts, units, provenance, and license policies as a schema graph. Given a query, SchemaRouter emits an executable tool plan specifying which tools to call and which fields to retrieve. A small LLM extracts intent, concepts, and source constraints, while field selection is deterministic over the graph through intent-group projection and concept-field matching with an alias layer.
  On a materials-science benchmark of 110 queries, SchemaRouter achieves answer accuracy of 0.71, matching fetch-everything within overlapping confidence intervals and exceeding prompt-all's 0.66, though their intervals overlap. It uses 227 retrieved-context tokens versus 2,066 for fetch-everything and achieves 2.7x lower end-to-end latency than prompt-all. It also obtains the best tool-exact rate of 0.93 and parameter validity of 1.0. SchemaRouter grounds provenance and license information in 62 percent of answers, compared with approximately 0 percent for all baselines.
  We also find that minimizing selected-field count is counterproductive: it reduces answer accuracy to 0.56 with negligible token savings, while recall-preserving projection restores top accuracy. SchemaRouter improves efficiency, schema-size-independent scaling, and verifiable provenance/license-grounded answering at competitive accuracy.

## 30. How Architecture and Training Affect TPC Representations Across Experiments

- Authors: Tyler Wheeler, Michelle P. Kuchera, Raghuram Ramanujan, William Sieland, Ryan Krupp, Daniel Bazin, Connor L. Cross, Hoi Yan Ian Heung, Andrew J. Jones, Ruchi Mahajan, Saiprasad Ravishankar, Pranjal Singh, Benjamin Votaw, Chris Wrede
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-22
- DOI: Unavailable
- Categories: cs.LG, cs.CV, nucl-ex, physics.ins-det
- Relevance: 2.93360262671328
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.21756v1
- PDF: https://arxiv.org/pdf/2608.21756v1
- Local PDF: pdf/2026-08-26_30_How Architecture and Training Affect TPC Representations Across Experiments.pdf

Deep-learning efforts have increasingly shifted toward foundation model approaches. In experimental physics, this allows models and learned representations to be reused beyond the experiments in which they were developed. This work evaluates the reusability of representations across experiments and detector systems using probes on frozen encoders. These probes reveal task-relevant structure before downstream adaptation, complementing fine-tuning. Together with random-weight controls, they distinguish contributions from architecture and encoder training that downstream performance alone cannot resolve.
  Time projection chamber (TPC) data provide a useful testbed because events from TPC systems can be represented as variable-length sparse tensors, while detector geometries, event topologies, and scientific tasks can differ substantially. We investigate whether fixed-dimensional TPC event representations can be reused across classification tasks, experiments, and detector systems. Sparse ResNet and PointNet-style encoders produce 512-dimensional embeddings for four datasets from the GADGET II TPC and AT-TPC. Randomly initialized encoders isolate the contribution from architecture before supervised training. We then train each encoder on a classification task, freeze its parameters, and train a linear or nonlinear probe for each downstream task. We find that this architecture-induced structure remains useful across experiments and detector systems. The randomly initialized PointNet-style representation is highly informative on several tasks. The two architectures organize their embedding spaces differently, but neither exhibits a large, systematic loss of utility cross-detector. These results show that architecture is a major source of task-relevant structure in TPC embeddings and should be treated explicitly when assessing representation learning and developing reusable detector models.
