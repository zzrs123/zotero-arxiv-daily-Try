# Paper Daily Reading - 2026-09-03

## 1. SemanticST: A Scalable Multi‐Contextual Graph Learning Framework for Uncovering Spatial Niches and Robust Multi‐Sample Integration in Spatial Transcriptomics

- Authors: Roxana Zahedi, Ahmadreza Argha, Nona Farbehi, Ivan Bakhshayeshi, Thantrira Porntaveetus, Youqiong Ye, Nigel H. Lovell, Hamid Alinejad‐Rokny
- Source: openalex
- Venue type: journal
- Journal: Advanced Science
- Publication status: published
- Publication date: 2026-08-31
- DOI: https://doi.org/10.1002/advs.77003
- Categories: Single-cell and spatial transcriptomics, Gene expression and cancer classification, Cell Image Analysis Techniques
- Relevance: 4.277761143741729
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://doi.org/10.1002/advs.77003
- PDF: Unavailable
- Local PDF: Not downloaded

Spatial transcriptomics (ST) analysis is often hindered by technical limitations and methodological biases that let dominant signals overshadow subtle but crucial biological patterns, such as rare cell types and fine-grained heterogeneity. This is especially true for high-complexity datasets from platforms like Xenium. We present SemanticST, a graph neural network (GNN) framework that addresses this challenge through a fundamentally different design. SemanticST is the first GNN method to implement mini-batch training, enabling scalable analysis of massive ST datasets (validated on Xenium). Crucially, it employs a multi-semantic graph fusion strategy that learns disentangled biological representations across tissue, using a min-cut loss that requires neither graph corruption nor contrastive sampling. Benchmarking across diverse tissues (e.g., brain, embryo, tumor) confirms consistent superiority. It achieves up to 20% higher ARI/NMI on the gold-standard brain cortex and uniquely delineates all mouse olfactory bulb layers and hippocampal sub-regions. In high-resolution breast cancer data, SemanticST identifies computationally plausible spatial domains, including a candidate rare triple receptor-positive region and a FOXC2-enriched EMT-associated domain, from Xenium alone. Furthermore, SemanticST provides superior, robust multi-sample integration on established benchmarks. SemanticST offers an essential, scalable framework for translating spatial complexity into biologically informative and testable hypotheses.

## 2. Hidden relationships in a document-derived property graph: top-k chunk embeddings and inverse-distance weighting over a dynamically evolving ontology

- Authors: Bilge Kaan Karamete, Hunter Casten
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-31
- DOI: Unavailable
- Categories: cs.CE, cs.LG
- Relevance: 3.5448413075514806
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.00387v1
- PDF: https://arxiv.org/pdf/2609.00387v1
- Local PDF: pdf/2026-09-03_02_Hidden relationships in a document-derived property graph_ top-k chunk embeddings and inverse-distance weighting over a.pdf

Large language models extracting knowledge graphs from text capture only explicitly stated facts, often leaving semantically related entities disconnected across documents. We present an additive, engine-neutral second pass that discovers these latent ties without altering extracted facts. Each document is chunked and embedded once; top-k nearest- neighbor queries across existing chunks yield candidate node pairs via entity membership maps. Candidate pairs are scored using Shepard inverse-distance weighting with a rescaled chord distance metric, avoiding the threshold-collapsing flaw of affine cosine scoring behind a k-NN gate. Un-gated per-pair accumulators form a commutative monoid, ensuring the pipeline is strictly order-independent and scales incrementally without recomputing prior documents. Implemented across FalkorDB, Kinetica, ArangoDB, and Neo4j, our method shows that 768- and 240-dimensional embeddings retain 92% and 72% edge fidelity against a 3072-D baseline while achieving a 25x faster top-k formulation.

## 3. A Network Science Perspective on Evaluating Deep Graph Generative Models

- Authors: Tianrui Mao, Abele Malan, Megha Khosla, Lydia Chen, Huijuan Wang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-01
- DOI: Unavailable
- Categories: cs.SI, cs.AI
- Relevance: 3.437678008755065
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.01015v1
- PDF: https://arxiv.org/pdf/2609.01015v1
- Local PDF: pdf/2026-09-03_03_A Network Science Perspective on Evaluating Deep Graph Generative Models.pdf

Traditional network models from network science, such as the Erdos-Renyi and configuration models, generate random networks that reproduce few selected topological properties observed in real-world networks. Deep graph generative models emerge as a data-driven approach, leveraging deep neural network architectures to learn complex structural distributions directly from real-world networks to generate more realistic synthetic networks. Because real social contact networks cannot be shared due to privacy risks, synthetic networks serve as an alternative for developing and evaluating epidemic mitigation strategies. In this work, we evaluate deep graph generative models as well as the configuration from a network science perspective by assessing both the topological similarity between generated and real-world networks and their utility in identifying effective node immunization strategies to sup- press epidemic/misinformation spreading. It is found that two deep graph generative models produce synthetic networks that closely resemble the structural properties of real-world networks, enabling them to identify effective immunization strategies.

## 4. Are You Thinking What I am Thinking? : Examining Conceptual Separation in Neural Architectures

- Authors: Jaee Ponde, Roshni Agarwal, Subhashis Banerjee
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-01
- DOI: Unavailable
- Categories: cs.LG, cs.AI
- Relevance: 3.4295695240885893
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.00764v1
- PDF: https://arxiv.org/pdf/2609.00764v1
- Local PDF: pdf/2026-09-03_04_Are You Thinking What I am Thinking_ _ Examining Conceptual Separation in Neural Architectures.pdf

Neural networks are increasingly employed to identify both well-defined and ambiguous concepts, yet output-level metrics reveal little about how those concepts are represented internally. Our study asks if these networks exhibit \textit{conceptual separation}: if examples of the same concept form coherent representations, and whether related concepts lie closer together in the representation space. We examine this conceptual organisation in Convolutional Neural Networks (CNNs) and Large Language Models (LLMs) through geometric and distributional analysis of their internal activations. In CNNs, familiar ImageNet concepts form coherent and semantically ordered representations, while this coherence weakens for unseen concepts and suffers within-class domain shift. In LLMs, clearly distinct domains remain well separated, related subdomains move closer together, and the distinction between ambiguous topics collapses at both the mean and covariance level. These results suggest that conceptual separation can reveal structure that output accuracy alone cannot, and may serve as a useful diagnostic of how robustly a model represents the concepts it is asked to identify. Code and data available on \href{https://github.com/JaeeRoshniCapstoneProject/Are-You-Thinking-What-I-m-Thinking-Examining-Conceptual-Separation-in-Neural-Architectures}{GitHub}.

## 5. ISO-RAG: Isoperimetric Noise Control for Retrieval-Augmented Generation

- Authors: Siyuan Zhang, Hanchen Wang, Dong Wen, Ying Zhang, Wenjie Zhang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-01
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 3.35287349512565
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.00513v1
- PDF: https://arxiv.org/pdf/2609.00513v1
- Local PDF: pdf/2026-09-03_05_ISO-RAG_ Isoperimetric Noise Control for Retrieval-Augmented Generation.pdf

Retrieval-Augmented Generation (RAG) mitigates large language models (LLMs) hallucinations, yet conventional dense retrieval struggles with the complex reasoning paths of multi-hop question answering (QA). Graph-based RAG captures multi-step relationships but suffers from severe semantic drift and high online latency due to noisy global graph traversals. Thus, we propose ISO-RAG (ISOperimetric Retrieval-Augmented Generation), a geometry-aware RAG framework. By projecting the underlying knowledge graph into a hyperbolic Poincare ball to precompute node-wise isoperimetric profiles, ISO-RAG prunes spurious edges during retrieval, restricting the search space to a strictly localized subgraph. This topological purification regulates Personalized PageRank (PPR) diffusion driving the retrieval process, ensuring exact and low-latency convergence. Experiments on multi-hop QA benchmarks demonstrate that ISO-RAG outperforms state-of-the-art baselines by average absolute gains of 10.0% in retrieval recall and 4.3% in downstream exact match, achieving a superior accuracy-efficiency trade-off by fundamentally eliminating the latency bottleneck of global traversals. Our source code is available at https://github.com/ZaiizaiZHANG/ISO-RAG.

## 6. S^3martCirc: Self-supervised Smart Circuit Discovery

- Authors: Wendy Zheng, Yinhan He, Liang Wu, Jundong Li
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-01
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 3.3450910199125716
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.00755v1
- PDF: https://arxiv.org/pdf/2609.00755v1
- Local PDF: pdf/2026-09-03_06_S^3martCirc_ Self-supervised Smart Circuit Discovery.pdf

Large Language Models (LLMs) have demonstrated remarkable performance across diverse tasks, from text summarization to question answering. Despite these capabilities, their black-box nature obscures internal decision-making processes. Mechanistic interpretability (MI) aims to address this by reverse-engineering neural networks into human-understandable algorithms. Current MI approaches for LLMs typically follow a two-stage paradigm: first identifying important components (circuit discovery), where components are typically individual nodes such as an attention head or feedforward neuron, and second determining the role they play in a certain task (functional interpretation). However, this sequential approach overlooks a fundamental insight: a component's importance and its functional role are inherently codependent. Unifying these stages presents two key challenges: (1) functional roles are often tied to specific nodes or components, limiting generalization, and (2) their identification relies on subjective interpretation rather than quantifiable metrics. To address these challenges, we propose S^3martCirc (Self-supervised Smart Circuit Discovery), a unified framework that simultaneously discovers circuits and interprets functionality. S^3martCirc abstracts node behavior into two general computational roles that generalize across tasks and defines a quantitative metric for assigning them, enabling importance and functional role to be discovered jointly rather than in sequence. Extensive experiments show that our framework outperforms existing methods in circuit discovery.

## 7. Operationalizing open-ended biological discovery across single-cell representations

- Authors: Ningxuan Zhang, Ziwei Wang, Ning Xie, Na Liu
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-01
- DOI: Unavailable
- Categories: q-bio.QM
- Relevance: 3.3221309898623765
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.00681v1
- PDF: https://arxiv.org/pdf/2609.00681v1
- Local PDF: pdf/2026-09-03_07_Operationalizing open-ended biological discovery across single-cell representations.pdf

Single-cell studies are typically initiated from predefined research questions, leaving much of the biological information encoded within existing data unexplored. We formalize open-ended discovery as an analytical paradigm, in which data-derived signals are identified before biological context is interrogated and subsequently evaluated according to their potential to justify prospective experimental investment. Here we develop PROSPECTor, an end-to-end framework that searches for reproducible biological structures across conventional expression representations and diverse foundation-model embeddings, translating robust signals into quantitatively testable candidate hypotheses. Projection into unseen datasets then evaluates their generalizability and phenotype association, providing a scalable screen for candidates that warrant prospective validation. Supported signals emerged from different representation spaces and search strategies. PROSPECTor-nominated hypotheses were then examined in independent biological settings: fibroblast extracellular-matrix programmes demonstrated transferability to an independent mouse cohort with an intervention context, while a patient-resolved gastric-cancer T-cell programme recurred across single-cell, bulk and spatial cohorts. PROSPECTor establishes an auditable framework for systematically revisiting single-cell datasets across expanding representation spaces, turning retrospective collections into prospective resources for biological discovery that can motivate new research questions.

## 8. From Confusion to Clarity: Confusion-Aware Retrieval and Knowledge Injection for Text Classification

- Authors: Manish Gupta, Chaitanya Giri, Jayasimha Talur
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-01
- DOI: Unavailable
- Categories: cs.CL, cs.AI
- Relevance: 3.2589435650380736
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.01564v1
- PDF: https://arxiv.org/pdf/2609.01564v1
- Local PDF: pdf/2026-09-03_08_From Confusion to Clarity_ Confusion-Aware Retrieval and Knowledge Injection for Text Classification.pdf

Large language models (LLMs) struggle to classify text into taxonomies with many semantically similar labels, as the distinctions are domain-specific and not captured by pre-training. To handle large label spaces, a common approach retrieves top-$K$ candidate labels by embedding similarity and prompt the LLM to choose among them. However, top-$K$ retrieval reduces the number of candidates but does not help the model tell similar ones apart. When two similar labels both appear as candidates, the model lacks the signal to choose correctly between them. We propose a framework that (1) identifies which label pairs the model struggles to distinguish, (2) expands the candidate set to include confusable labels, and (3) generates targeted rules to differentiate between similar candidates. The framework requires no fine-tuning, and the generated rules transfer to smaller, cheaper models. On three benchmarks (WOS, Flipkart, LEDGAR), our approach improves Macro F1 by up to 10.0pp over retrieval baselines, with smaller models (2B--20B) gaining up to 11.5pp via cross-model transfer.

## 9. Automated Tree Knowledge Graph Construction using Ontology Expansion and Retrieval from Vietnamese History Textbooks

- Authors: Ket Doan Nguyen, Minh N. H. Nguyen
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-01
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 3.249797365555857
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.00763v1
- PDF: https://arxiv.org/pdf/2609.00763v1
- Local PDF: pdf/2026-09-03_09_Automated Tree Knowledge Graph Construction using Ontology Expansion and Retrieval from Vietnamese History Textbooks.pdf

Hierarchical Knowledge graph (KG)-based retrieval augmented generation (RAG) has emerged as a powerful approach for supporting large language models with structured knowledge. However, there are primary challenges: (i) the lack of methods for automatic KG construction using ontology expansion for low-resource languages such as Vietnamese, (ii) the absence of systematic evaluation for knowledge retrieval strategies leveraging the hierarchical structures. In this paper, we propose an end-to-end pipeline for KG construction and retrieval strategies evaluation. In the KG construction, we employ a three-phase hybrid relation extraction pipeline: intra-batch deduplication via Union-Find, approximate cross-batch search, and LLM extraction with a centroid filter that reduces prompts combined with a five-step dual-LLM validator to prevent bloated ontology. A two-tier architecture consists of unmergeable structural nodes to preserve the document structure and mergeable content nodes. The retrieval evaluation consists of three graph traversal strategies: Top-Down, Horizontal, and Bottom-Up, which are evaluated on a synthetically generated benchmark of 1,210 Vietnamese queries from 109 subgraphs, categorized by five query directions. In this paper, we construct the tree knowledge graph from Vietnamese high school History textbooks (nearly 400 pages) to produce 750 nodes and 4,341 semantic edges with controlled ontology growth from 40 to 41 types. Among experimental graph traversal strategies, the Top-Down strategy with structure surpasses the vector baseline by 4.7 percentage points in NDCG@10. As a result, tree-structural information provides valuable information beyond flat cosine similarity but degrades performance when the query does not require structural context.

## 10. Pre-carved Niches: The Formation Dynamics of Modular Task Partitions in Early LLM Training

- Authors: Guangqi Li, Yongxin Li
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-01
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.241094526876788
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.01170v1
- PDF: https://arxiv.org/pdf/2609.01170v1
- Local PDF: pdf/2026-09-03_10_Pre-carved Niches_ The Formation Dynamics of Modular Task Partitions in Early LLM Training.pdf

Large language models exhibit a modular internal organization that mirrors well-studied functional networks of the human brain, but how this organization forms during training is unknown: prior work has characterized finished models, not the formation process. We track formation step by step: we train a Pythia-410M model from scratch (two trajectories, bf16 and fp32) and run attribution patching at every step, alongside probes for gradient norms, effective updates, weight norms, and first-order loss decomposition across 14 tasks in four cognitive domains. Three findings. First, the modular map is pre-carved: before any learning, the dominant task pair already overlaps at ~3.6x the attribution substrate (a task-independent baseline), and its layer-0 concentration is an architecture-level constant on this model family. Second, the partition locks in through two sharp jumps whose amplitudes do not track the learning-rate schedule (the second reaching 20.4 sigma quiet-window / 6.2 sigma global), accompanied by gradient-level relative deprivation--winners receive 2.25->2.73x the loser's gradient supply, 9.5-11.5 standard deviations below a random control--that does not propagate to updates or weights. Third, deviation from the substrate appears only in the domain being learned, consistent with the hypothesis that modularity tracks learning. We close by separating the feature-level account we can defend from the mechanistic questions we cannot, and we pre-register the scale-threshold hypothesis behind our ongoing 2.8B experiments.

## 11. Modelpedia: A Catalog of Model Findings for the Meta-Science of AI

- Authors: Franciszek Bernat, Dawid Płudowski, Michał Jan Włodarczyk, Luca Longo, Jianlong Zhou, Andreas Holzinger, Riccardo Guidotti, Wojciech Samek, Przemysław Biecek
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-01
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.2276424741793974
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.01090v1
- PDF: https://arxiv.org/pdf/2609.01090v1
- Local PDF: pdf/2026-09-03_11_Modelpedia_ A Catalog of Model Findings for the Meta-Science of AI.pdf

Scientific knowledge about AI models is produced faster than the community can organize it. Every few months a new foundation model reshapes the field and hundreds of papers, blogs, and technical reports document how each behaves or fails. Yet, these findings remain scattered and effectively unretrievable. To address this gap we present Modelpedia, an automated, LLM-assisted framework that extracts findings about models from published papers, links it to the model, dataset, method, and concept it concerns, and aggregates the result into a searchable public catalog. Applying the prototype to accepted ICLR 2024 and 2025 papers, we extract over a thousand findings and, treating the catalog itself as an object of study, run a meta-analysis of how the community investigates models. Now, we invite the community to explore, contribute to, and build on the open catalog, and to help establish model findings as a shared foundation for the meta-science of AI.

## 12. Do General NLP Embeddings Capture Ontological Reasoning?

- Authors: Hamed Babaei Giglou, Jennifer D'Souza, Sören Auer
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-31
- DOI: Unavailable
- Categories: cs.CL, cs.AI
- Relevance: 3.184472303971495
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.00177v1
- PDF: https://arxiv.org/pdf/2609.00177v1
- Local PDF: pdf/2026-09-03_12_Do General NLP Embeddings Capture Ontological Reasoning.pdf

General-purpose NLP embedding models perform well on linguistic tasks, but their ability to capture symbolic ontological structure remains unclear. We introduce AVA, a systematic framework for evaluating whether embeddings distinguish logic-sensitive relational semantics in ontologies and knowledge graphs. AVA comprises 171,007 contrastive triplets derived from 163 heterogeneous ontologies using hierarchy inversion, relation substitution, and disjointness injection. Each triplet contains an ontology statement, a semantically equivalent paraphrase, and a logic-sensitive hard negative with contradictory relational meaning. We evaluate more than 25 state-of-the-art embedding models and find substantial limitations: the best model achieves only 0.739 triplet accuracy, while hard negative accuracy falls to 0.135. Fine-tuning improves discrimination by a large margin but transfers poorly to downstream Semantic Web tasks, including taxonomy discovery and ontology alignment. Further analysis suggests that improvements stem partly from perturbation-specific pattern recognition rather than robust ontological understanding. These findings reveal a persistent gap between linguistic representation learning and ontology-level discrimination, challenging the assumption that strong NLP benchmark performance translates to Semantic Web competence.

## 13. EGT-KG: Evidence-Grounded Typed KG Retrieval for Practical Scientific QA with Small Language Models

- Authors: Muran Yu, Jiechao Gao, Yuandong Pan, Barney H. Miao, Andrew C. Lesh, Kincho H. Law, Jie Wang, Michael D. Lepech
- Source: arxiv
- Venue type: preprint
- Journal: EMNLP Industry track 2026
- Publication status: preprint
- Publication date: 2026-08-31
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 3.1635702533726375
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.00479v1
- PDF: https://arxiv.org/pdf/2609.00479v1
- Local PDF: pdf/2026-09-03_13_EGT-KG_ Evidence-Grounded Typed KG Retrieval for Practical Scientific QA with Small Language Models.pdf

For emerging scientific research domains, local Small Language Models (SLMs) are becoming more attractive, as they offer stronger privacy control and more stable deployment pipelines than Large Language Models. However, in practice, scientific question-answering on SLMs often operates under inevitable constraints: small literature collections, fragmented evidence, limited context window and reasoning abilities. We propose the Evidence-Grounded Typed Knowledge Graph (EGT-KG), a retrieval framework to improve information retrieval with local SLMs. We assessed three question-answering settings: a vanilla Retrieval-Augmented Generation (RAG) workflow and two EGT-KG workflows: an automatically generated relation schema (AS) and an expert-defined relation schema (ES). Our experiments were evaluated with a six-dimensional evaluation framework (S3CRF: Soundness, Correctness, Completeness, Conciseness, Relevance, Fluency) on a Biopolymer-bound Soil Composite literature benchmark, showing that EGT-KG outperforms the vanilla RAG method in most settings, with the best improvement from llama3:8b: a Final Score of 70.37 (+14.67%) and 68.82 (+12.14%) by AS/ES EGT-KG variants.

## 14. Topological Steering

- Authors: Benoît Guérand, Tan Minh Nguyen
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-01
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.16130143302217
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.00597v1
- PDF: https://arxiv.org/pdf/2609.00597v1
- Local PDF: pdf/2026-09-03_14_Topological Steering.pdf

With the rapid rise of large language models (LLMs), controlling undesirable model behaviors has become increasingly important. Existing behavioral control methods typically intervene directly in activation or feature space, but such approaches can be sensitive to outliers, distributional shifts, noise, and other local perturbations. Motivated by Topological Data Analysis (TDA), which captures global rather than purely local structure, we propose Topological Steering, a new framework for steering LLM behavior through the topological representation of activation spaces. Using persistence diagrams, our method connects activation-based steering with TDA and enables more robust behavioral control. We show that Topological Steering consistently modifies LLM behavior across multiple model families and model sizes.

## 15. H2Table: Hierarchical Hypergraph-Enhanced Large Language Models for Complex Table Reasoning

- Authors: Jia Ling, Yangfan Wang, Chen Tang, Haoming Tan, Yang Yang, Yi Guan, Jingchi Jiang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-01
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 3.1532283990974563
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.01216v1
- PDF: https://arxiv.org/pdf/2609.01216v1
- Local PDF: pdf/2026-09-03_15_H2Table_ Hierarchical Hypergraph-Enhanced Large Language Models for Complex Table Reasoning.pdf

Tables are ubiquitous across diverse domains, yet reasoning over them remains a significant challenge for modern large language models (LLMs). Current approaches typically linearize tables into sequences, inherently overlooking their intrinsic two-dimensional and hierarchical structure. To address this, we propose H2Table (Hierarchical Hypergraph-Enhanced Table Reasoning), a novel framework that represents complex tables as hierarchical nested hypergraphs. To process this representation, we design a tailored hypergraph encoder to facilitate message passing between hyperedges (headers) and nodes (cells), thereby perceiving the semantic entailment relationships between them within complex tables. Furthermore, we introduce a set of learnable query vectors acting as a lightweight bridge to extract representative structural embeddings from the encoder into the LLM. Experimental results demonstrate that our approach effectively handles complex table question answering tasks with hierarchical nested headers. Notably, on the HiTab dataset, H2Table achieves an average improvement of 22.88% over state-of-the-art baselines on highly complex tables with a nesting depth of four. Our code is available at: https://github.com/lila120/h2table.

## 16. Denoising Diffusion Generative Models Secretly Calculate Attentions

- Authors: Farzan Haddadi, Leila Monfared, Ebrahim Rezaii, Mohammadreza Malek-Mohammadi, Pejman Zakalvand, Narges Mokhtari
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-01
- DOI: Unavailable
- Categories: cs.AI, cs.CV, cs.LG, cs.NE
- Relevance: 3.1484191500362058
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.00885v1
- PDF: https://arxiv.org/pdf/2609.00885v1
- Local PDF: pdf/2026-09-03_16_Denoising Diffusion Generative Models Secretly Calculate Attentions.pdf

Denoising diffusion models are the dominant architecture for image generation, whereas most natural language generation and modeling are primarily handled by well-known transformer architectures employing attention mechanism. Here, we show that diffusion models also inherently use an attention mechanism very similar to that of transformers. Therefore, attention emerges as a universal machine learning principle, based on a general training objective. We also show similarities in basic functional principle of auto-encoders and attention-based models. These equivalences allows us to interchange these designs based on practical requirements. As an example, we can reformulate the diffusion framework to reduce the lengthy training process and computation-intensive image generation. Using this approach, a simplified algorithm is proposed for image generation which is based on attention mechanism. Results show that the attention-based implementation achieves comparable performance with significantly less effort and computational resources.

## 17. RW-LoRA: Communication-Efficient Decentralized LoRA Fine-Tuning via Random Walks

- Authors: Xingran Chen, Rohit Bhagat, Ghadir Ayache, Rawad Bitar, Yanmin Gong, Salim El Rouayheb
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-31
- DOI: Unavailable
- Categories: cs.LG, cs.AI
- Relevance: 3.127079314575454
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.00078v1
- PDF: https://arxiv.org/pdf/2609.00078v1
- Local PDF: pdf/2026-09-03_17_RW-LoRA_ Communication-Efficient Decentralized LoRA Fine-Tuning via Random Walks.pdf

Parameter-efficient fine-tuning methods such as LoRA have become a standard approach for adapting large foundation models. Adopting fine-tuning to distributed settings faces several challenges. Most existing distributed LoRA methods rely on centralized aggregation, and gossip-based decentralized LoRA requires repeated synchronization among multiple model copies. Both methods incur significant communication overhead and introduce errors due to simultaneous aggregation of multiple model updates. In this paper, we take a different perspective and propose a random-walk-based LoRA fine-tuning scheme. Instead of maintaining multiple model replicas, a single model token traverses the network and is updated sequentially using local fine-tuning objectives. This design eliminates the need for global synchronization, substantially reduces communication and computation costs, and avoids aggregation errors. We provide rigorous convergence guarantees for non-convex objectives under standard assumptions. Through empirical results on multiple NLP tasks and graph topologies, we show that the proposed method achieves competitive task performance with substantially less communication and computation than gossip-based LoRA.

## 18. The zbMATH Open Knowledge Graph: Tracing Centuries of Mathematical Research

- Authors: Yuni Susanti, Moritz Schubotz
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-01
- DOI: Unavailable
- Categories: cs.DL, cs.AI
- Relevance: 3.0244021858293535
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.00969v1
- PDF: https://arxiv.org/pdf/2609.00969v1
- Local PDF: pdf/2026-09-03_18_The zbMATH Open Knowledge Graph_ Tracing Centuries of Mathematical Research.pdf

We present the zbMATH Open Knowledge Graph, a large-scale RDF knowledge graph (KG) covering more than 250 years of mathematical scholarship. Unlike existing scholarly knowledge graphs that primarily capture bibliographic metadata and citation structures, the zbMATH Open KG integrates expert-curated semantic content, including reviews, keywords, subject classifications, software references, and disambiguated authorship. This combination of domain-specific representation of mathematical knowledge and extensive temporal coverage supports analyses that require fine-grained exploration of mathematical concepts, research fields, and scholarly relationships over time. The resulting graph comprises 34 million entities and 168 million RDF triples represented using established Semantic Web vocabularies, supporting interoperability and FAIR data principles. We further demonstrate its capabilities through query-driven historically grounded scholarly exploration use cases, illustrating how the knowledge graph can surface relationships and patterns that may be difficult to identify from bibliographic and citation information alone. The zbMATH Open KG provides an open semantic infrastructure for studying the development of mathematical knowledge and tracing scholarly connections across centuries of scholarship.

## 19. Breaking the Structural Identity: Personalized Federated LoRA Fine-tuning under Rank Heterogeneity

- Authors: Lei Wang, Jieming Bian, Letian Zhang, Jie Xu
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-01
- DOI: Unavailable
- Categories: cs.LG, cs.AI
- Relevance: 3.003124084599235
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.00632v1
- PDF: https://arxiv.org/pdf/2609.00632v1
- Local PDF: pdf/2026-09-03_19_Breaking the Structural Identity_ Personalized Federated LoRA Fine-tuning under Rank Heterogeneity.pdf

Large Language Models (LLMs) have achieved remarkable success across diverse domains, but their adaptation to privacy-sensitive, distributed datasets remains a challenge. While Federated Learning (FL) combined with Low-Rank Adaptation (LoRA) provides a resource-efficient paradigm for collaborative fine-tuning, practical deployments are hindered by the dual challenges of resource heterogeneity and data heterogeneity. Existing rank-heterogeneous methods primarily focus on bridging dimension mismatches for aggregation but typically provide a unified global model for all clients sharing the same rank, failing to capture client-specific features in non-IID scenarios. In this paper, we propose FedRoRA (Federated Rank-wise Personalized LoRA), a novel framework that enables fine-grained personalization within rank-heterogeneous federations. FedRoRA decouples adaptation into shared global directions and personalized rank-wise magnitudes governed by learnable diagonal scales. On the server side, it extracts a global subspace via singular value decomposition (SVD) and redistributes client-specific initializations through a personalized projection and top-$k$ selection mechanism. Extensive experiments on NLU and NLG benchmarks demonstrate that FedRoRA consistently outperforms state-of-the-art methods.

## 20. Context Window Failures in Relational Foundation Models

- Authors: Denis Oliveira Correa, Francisco Galuppo Azevedo
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-31
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.0023124976883757
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.00460v1
- PDF: https://arxiv.org/pdf/2609.00460v1
- Local PDF: pdf/2026-09-03_20_Context Window Failures in Relational Foundation Models.pdf

Recent Relational Deep Learning architectures have been proposed as foundation models for multi-table relational data, yet they impose constrained neighborhood budgets that force row truncation when an entity has many related records. We introduce Animus, a synthetic financial dataset in which predicting customer income requires aggregating up to tens of thousands of transactions. On the raw representation, three recently proposed models (RT, Griffin, RelGT) achieve $R^2 \le 0.18$; a single, routine, temporal pre-aggregation step recovers $R^2$ up to $0.65$. This questions whether current relational foundation models are ready for high-cardinality real-world data.

## 21. Athena: Vulnerability-Affected Library Identification via Knowledge Graph Completion

- Authors: Phong Trinh Duy, Trang Dang Yen, Hung Nguyen-Huu, Bach Le, Quyet-Thang Huynh, Dieu Hoang Vu, David Lo, Thanh Le-Cong
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-01
- DOI: Unavailable
- Categories: cs.SE, cs.AI, cs.CR
- Relevance: 2.9990772940319985
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.01187v1
- PDF: https://arxiv.org/pdf/2609.01187v1
- Local PDF: pdf/2026-09-03_21_Athena_ Vulnerability-Affected Library Identification via Knowledge Graph Completion.pdf

A single vulnerability in a widely used library can cascade through millions of dependent applications, yet more than half of vulnerability database entries contain missing or incorrect affected-library information. Existing automated approaches neglect the relational structure of vulnerability databases, treating identification as an isolated text retrieval problem. In this paper, we propose Athena, the first graph-based approach for vulnerability affected library identification. Athena models vulnerability databases as a knowledge graph and reformulates the identification problem as knowledge graph completion (KGC). It comprises three key modules: a Modeling module that constructs a security knowledge graph integrating CVEs, libraries, CWE weakness types, CPE products, and software ecosystems; a Completion module that applies a modular KGC backbone to predict missing affected libraries for a given CVE via link prediction; and a Re-ranking module that retrieves KGC candidates and rescores them using a fine-tuned LLM augmented with knowledge graph embeddings, jointly leveraging structural and textual information. Our experiments on VulLib demonstrate that Athena significantly outperforms four state-of-the-art baselines, achieving a 32% improvement in Avg. F1 over the best baseline (i.e., VulLibGen). Notably, our KGC backbone with only 110M parameters already surpasses VulLibGen's best configuration at 7B parameters, demonstrating the effectiveness of graph-based modeling; the re-ranking module then provides substantial further gains, consistently outperforming the best baseline across all evaluated LLM backbones.

## 22. Zero-Shot Respiratory Sound Classification through LLM-Augmented Audio-Text Alignment

- Authors: Mustafa Talha İlerisoy, Hung Manh Pham, Mathias Funk, Mykola Pechenizkiy, Aaqib Saeed
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-30
- DOI: Unavailable
- Categories: cs.CL, cs.AI, cs.SD
- Relevance: 2.984354825822807
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.00055v1
- PDF: https://arxiv.org/pdf/2609.00055v1
- Local PDF: pdf/2026-09-03_22_Zero-Shot Respiratory Sound Classification through LLM-Augmented Audio-Text Alignment.pdf

Self-supervised respiratory encoders lack semantic grounding in clinical domain needed for zero-shot inference, limiting their utility without task-specific labeled data. We propose a framework that aligns these encoders with medical terminology in a shared latent space turning them into a zero-shot-capable foundation model. To address paired data scarcity, we use a medical LLM to synthesize structured reports from metadata, creating dense semantic anchors for contrastive learning. Our training combines a sigmoid-based contrastive loss with encoder's native SSL objective and similarity-aware negative sampling to sharpen pathological boundaries. Across 9 tasks on 6 datasets, our method achieves a 61.3% mean zero-shot AUC, surpassing CLAP (51.4%) and Qwen2-Audio (54.9%) while reaching the highest linear probing AUC (71.6%) with only 43% of data used by full-scale baselines, showing that structured semantic alignment outperforms large-scale, general-purpose models in clinical diagnostics.

## 23. Restrict, Don't Retrain: Inference-Time VLM Guidance for Zero-Shot Aerial Segmentation

- Authors: Teresa DiMeola, Charles Walter, Hong Xiao
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-01
- DOI: Unavailable
- Categories: cs.CV, cs.AI
- Relevance: 2.9612689060415165
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.00628v1
- PDF: https://arxiv.org/pdf/2609.00628v1
- Local PDF: pdf/2026-09-03_23_Restrict, Don't Retrain_ Inference-Time VLM Guidance for Zero-Shot Aerial Segmentation.pdf

Global welfare often depends on the correct interpretation of aerial and satellite imagery. Acting on such imagery (mapping flooded ground, crop extent, or damaged infrastructure) demands pixel-level segmentation to ensure perfect class localization. Pretrained general foundation models, when applied directly, often miss important features and cannot always find all the classes belonging to a given scene, overlooking smaller objects that matter most. We use a single consumer-grade GPU running a vision-language model (VLM) to supply this missing guidance, improving segmentation while producing structured, auditable evidence that drives the result and can be inspected on its own. We fuse three approaches: the frozen foundation model that labels every pixel, and two queries to a VLM, one to choose the classes that matter, and one to locate the small objects the base model misses. Evaluating across four aerial datasets, we see consistent gains at each stage where the base model is competent.

## 24. Vision-Language-Guided Pseudo-Labels for Unsupervised Domain Adaptation in Semantic Segmentation for Waste Sorting

- Authors: Udo Schlegel, Shubhangi, Gabriel Dax, Sai Rahul Kaminwar, Florian Karl, Thomas Seidl
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-01
- DOI: Unavailable
- Categories: cs.CV, cs.AI, cs.LG
- Relevance: 2.945701932529251
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.00898v1
- PDF: https://arxiv.org/pdf/2609.00898v1
- Local PDF: pdf/2026-09-03_24_Vision-Language-Guided Pseudo-Labels for Unsupervised Domain Adaptation in Semantic Segmentation for Waste Sorting.pdf

Obtaining labeled data for semantic segmentation in applied settings (e.g., autonomous driving, industrial waste sorting) is expensive and often infeasible at scale. We present a cross-modal pseudo-labeling pipeline that enables unsupervised domain adaptation without any target-domain annotations. The pipeline is built on two core foundation models: SAM generates class-agnostic region proposals, and EVA-CLIP assigns semantic labels based on region-text similarity, with confidence filtering ensuring that only reliable pseudo-labels are used for self-training a segmentation model. As an optional extension, BLIP provides language-grounded verification for ambiguous regions, thereby improving pseudo-label quality without altering the overall pipeline. Evaluated on two domain shifts, synthetic-to-real autonomous driving and, with a primary focus, lab-to-factory industrial waste sorting, the pipeline consistently improves over source-only baselines. Our results demonstrate that pseudo-label quality, not quantity, is a decisive factor in self-training under domain shift, and that cross-modal language grounding offers a practical path to reliable automatic annotation in deployment-critical applications.

## 25. Can LLMs Use Relational Transformer Embeddings?

- Authors: Francisco Galuppo Azevedo, Clarissa Lima Loures
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-31
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 2.9444483422835743
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.00457v1
- PDF: https://arxiv.org/pdf/2609.00457v1
- Local PDF: pdf/2026-09-03_25_Can LLMs Use Relational Transformer Embeddings.pdf

Injecting frozen relational-encoder embeddings as soft tokens into a large language model (LLM) is a conceptually appealing fusion strategy: the encoder handles multi-table structure, the LLM handles language and reasoning, and no lossy text serialization is required. We test this hypothesis concretely by injecting embeddings from a frozen Relational Transformer (RT) into Qwen3.5-4B via a learned MLP projection and LoRA adaptation, trained first with supervised fine-tuning (SFT) on chain-of-thought reasoning traces and then with group-based reinforcement learning (GSPO). We evaluate across 10 binary classification tasks on 6 relational databases from RelBench, under four supervision regimes: single-task (ST), within-dataset (WD), cross-dataset (CD), and all-task (ALL). The hybrid model does not consistently outperform standalone RT: it is frequently below random, highly sensitive to serialization format and relational-token budget, and unstable under RL training. We report these negative results and analyze the failure modes, arguing that soft-token fusion requires stronger alignment objectives and schema-aware design before it can serve as a reliable route to relational prediction.

## 26. Geometry-aware Latent Autoregressive Generative Model for PDEs in Complex Domains

- Authors: Zi Wang, Minghui Xu, Tapan Mukerji
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-31
- DOI: Unavailable
- Categories: cs.LG, cs.AI
- Relevance: 2.92631628685253
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.00297v1
- PDF: https://arxiv.org/pdf/2609.00297v1
- Local PDF: pdf/2026-09-03_26_Geometry-aware Latent Autoregressive Generative Model for PDEs in Complex Domains.pdf

Solving multiphysics partial differential equations (PDEs) remains a major challenge in scientific computing, especially for highly complex $μ$m-scale tortuous geometries critical to energy and chemical engineering. We address this challenge by proposing a Geometry-aware Latent Autoregressive generative Model for PDEs (GeoLAMP) for solving physics within highly irregular and tortuous structures. GeoLAMP introduces a dual-encoder architecture on graph representations to jointly capture global topology and fine-scale geometric features, enabling an effective transition from real-space fields to compact latent representations. In the latent space, we propose a causal self-attention transformer with flow matching to model temporal dynamics, allowing stable and scalable block-wise autoregressive prediction. A flexible decoder reconstructs high-resolution physical fields on arbitrary points. We establish three multiphysics benchmark datasets in complex geometries, covering reactive flow, heat convection, and elasticity. GeoLAMP consistently achieves the most stable autoregression performance on these datasets, maintaining low errors throughout the entire rollout horizon. Our results provide a systematic study of geometry-aware learning for PDEs in $μ$m-scale complex geometries and offer new insights into block-wise time marching of latent autoregressive PDE modeling via a flow matching framework.

## 27. Vision Is Not Overhead: One-Pass Block Drafting for Lossless Speculative Decoding in Vision-Language Models

- Authors: Jungseob Lee, Seongtae Hong, Dongyub Jude Lee, Chanjun Park, Jaehyung Seo, Sugyeong Eo, Heuiseok Lim
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-31
- DOI: Unavailable
- Categories: cs.AI, cs.CL, cs.CV
- Relevance: 2.9217482733802616
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.00355v1
- PDF: https://arxiv.org/pdf/2609.00355v1
- Local PDF: pdf/2026-09-03_27_Vision Is Not Overhead_ One-Pass Block Drafting for Lossless Speculative Decoding in Vision-Language Models.pdf

Speculative decoding accelerates generation without changing its output, yet on vision-language models (VLMs) it has been caught in a self-defeating cycle. The drafter stays autoregressive, so it must stay small. A small drafter cannot afford the image at every step, so vision is compressed, pruned, or hidden. A drafter cut off from the image is then least reliable exactly where the image makes text predictable. We present GLANCE, the first one-pass block drafter that is lossless on an unmodified VLM target, and it breaks the cycle at both ends. A block-diffusion head reads the target's already-fused vision-language state, so vision costs the drafter nothing, and fills a whole block in one forward pass, so depth costs no sequential steps. A wide candidate tree is verified in one target pass, and every audited prompt reproduces greedy decoding exactly. Grounded workloads reward this most, entering a verbatim-copy regime whose long runs cost an autoregressive drafter a pass for every token and a block drafter one in total. Under one engine and one round budget, GLANCE decodes up to 2.93x faster than autoregression, from one draft pass a round where the production EAGLE3-VL head takes eight, and accepts 2.7x longer blocks than an EAGLE-3 head trained on the same corpus. One law organizes these results. Accepted length is set by the target's next-token entropy, with a fitted slope that steepens with grounding across all five tasks. The law transfers across targets and modalities and names its own boundary, since free-running text still favors a chain. Our code is available at https://github.com/js-lee-AI/GLANCE.

## 28. Escaping Redundant Reasoning: Structure-Aware Search for Inference-Time LLMs

- Authors: Lu Cheng
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-01
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 2.894011588075145
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.00738v1
- PDF: https://arxiv.org/pdf/2609.00738v1
- Local PDF: pdf/2026-09-03_28_Escaping Redundant Reasoning_ Structure-Aware Search for Inference-Time LLMs.pdf

Inference-time search with large language models (LLMs) often concentrates on a small set of structurally or semantically similar trajectories, leaving alternatives underexplored---a failure mode we call \textit{reasoning basin collapse}. We introduce BASIN, a training-free, structure-aware selection method that groups reasoning states into basins and penalizes repeated visits to the same strategy, thereby reallocating search across genuinely distinct reasoning paths under a fixed compute budget. Under matched inference budgets, BASIN improves over Tree of Thoughts (ToT) by up to $+22$pp on Game of 24 and $+6.7$pp on MuSR. A quality-aware variant, QA-BASIN, further improves robustness by preserving high-quality basins when unconditional diversification over-explores. To explain when basin-aware selection helps, we introduce the redundancy gap $Δ$, which measures how differently search concentrates for correct versus incorrect predictions: standard ToT often operates near $Δ\approx 0$, while BASIN consistently shifts $Δ$ positive. More broadly, BASIN suggests structure-aware selection as a simple and general approach to improving inference-time reasoning. Code can be found at https://github.com/GitHubLuCheng/basin.

## 29. A Multi-Branch Feature Fusion Approach for Health Misinformation Detection and Propagation

- Authors: Mkululi Sikosana, Sean Maudsley-Barton, Oluwaseun Ajao
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-31
- DOI: Unavailable
- Categories: cs.LG, cs.SI
- Relevance: 2.8889791360322272
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.00403v1
- PDF: https://arxiv.org/pdf/2609.00403v1
- Local PDF: pdf/2026-09-03_29_A Multi-Branch Feature Fusion Approach for Health Misinformation Detection and Propagation.pdf

This paper presents a multi-branch fusion framework for detecting and characterising the propagation of health misinformation in online social networks (OSNs). Grounded in the Elaboration Likelihood Model (ELM) and the Theory of Planned Behaviour (TPB), the model fuses transformer-based semantics with rhetorical cues, stance representations, and psychologically motivated proxies in a unified multi-task architecture. In addition to binary classification, we introduce the Cognitive Propagation Score (CPS), an interpretable post-hoc auxiliary score computed from psychologically motivated, text-derived cues capturing argument complexity, emotional intensity, and content-derived virality potential, to support diffusion-risk reasoning when engagement ground truth is incomplete or unavailable. Experiments on three benchmark datasets, Constraint, COVID--19\_FNIR, and Monkeypox, show strong classification performance, achieving ROC--AUC up to 0.9999 on COVID--19\_FNIR, while propagation-oriented ranking achieves near-perfect agreement when engagement-derived supervision is available (Monkeypox, Spearman's $ρ= 0.9952$) and similarly high ranking alignment under proxy-based supervision on COVID--19\_FNIR ($ρ= 0.9954$). Compared with representative literature baselines, the fusion model improves detection on Constraint and COVID--19\_FNIR, while Monkeypox remains more challenging, reflecting domain- and signal-specific differences. Ablation analysis further indicates that psychological and rhetorical branches provide complementary gains beyond semantic embeddings. Overall, the framework bridges cognitive theory and neural modelling to improve transparency and to support scalable misinformation monitoring, with future work required to validate CPS against human-centred diffusion judgements.

## 30. Faster Than Flash: Exploiting Attention Sparsity for Efficient Long-Context Decoding

- Authors: Zhigeng Liu, Zhiyuan Ning, Ruixiao Li, Xiaoran Liu, Yuerong Song, Min Zhang, Ziwei He, Xipeng Qiu
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-31
- DOI: Unavailable
- Categories: cs.LG, cs.AI
- Relevance: 2.8832660060918256
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.00097v1
- PDF: https://arxiv.org/pdf/2609.00097v1
- Local PDF: pdf/2026-09-03_30_Faster Than Flash_ Exploiting Attention Sparsity for Efficient Long-Context Decoding.pdf

The development of long-context Large Language Models (LLMs) is constrained by the memory bandwidth bottleneck and quadratic complexity of the attention mechanism during decoding. To overcome the inherent trade-offs between the memory overhead of metadata-based metrics and the computational inefficiency of adaptive selection strategies, we present Faster Flash Decoding (FFD), a novel hardware-algorithm co-design framework designed to break the memory wall in long-context decoding. FFD integrates the selector and computer into a fully fused kernel, replacing external metadata indices with content-aware scanning via low-bit quantization. Furthermore, we introduce the top-delta strategy, which dynamically filters blocks to achieve distribution-adaptive sparsity without global synchronization. Offering a training-free and plug-and-play solution, FFD also enables the reuse of scanning results for computation, achieving up to 11.6x kernel-level speedup and scaling to 256K context length, with 2.37x end-to-end throughput improvement. Empirical validation on RULER and LongBench confirms that FFD maintains model accuracy while delivering high-ratio sparsity, with code available at https://github.com/qluoluo/faster-flash-decoding
