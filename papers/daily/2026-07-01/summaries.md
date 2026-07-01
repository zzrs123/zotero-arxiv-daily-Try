# Paper Daily Reading - 2026-07-01

## 1. GLIP: Graph and LLM Joint Pretraining for Graph-Level Tasks

- Authors: Haoxin Sun, Yiqing Lin, Yajun Huang, Chenhui Dong, Mingjun Li, Zhongzhi Zhang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-06-29
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.9159526361583543
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2606.29773v1
- PDF: https://arxiv.org/pdf/2606.29773v1
- Local PDF: pdf/2026-07-01_01_GLIP_ Graph and LLM Joint Pretraining for Graph-Level Tasks.pdf

Graphs are widely used to model relational systems, with applications in domains such as social networks, finance, and biomedicine. Graph neural networks (GNNs) have become a mainstream approach for learning graph representations. With the rise of large language models (LLMs), recent studies have attempted to combine GNNs with LLMs. However, most existing works concentrate on node-level and edge-level tasks, while graph-level tasks, which require capturing more complex structural and feature information, remain relatively underexplored. Moreover, graph pretraining is a widely adopted strategy to alleviate the challenge of label scarcity. Most existing approaches are designed solely for GNNs such as GraphCL, leaving LLMs uninvolved in the process. To address these limitations, we propose GLIP, a Graph-LLM JoInt Pretraining framework for graph-level tasks. GLIP first performs graph augmentation to construct positive and negative pairs and introduces a multi-token selection strategy to identify patches informative in both structure and features. It further leverages a diffusion-based projector to enrich them with contextual information, enabling GLIP to capture signals from both global and local perspectives. Finally, GLIP employs a joint objective that integrates the LLM's semantic judgments with a contrastive alignment loss, ensuring consistent supervision at both the semantic and structural levels. After pretraining, GLIP is fine-tuned with limited labeled data for downstream tasks, and extensive experiments show that it outperforms state-of-the-art methods on graph-level classification and reasoning tasks. Our source code is publicly available at https://anonymous.4open.science/r/GLIP.

## 2. scKDGM: KAN-guided Dynamic Graph Masked Learning for Single-Cell RNA-seq Clustering

- Authors: Jun Tang, Pengwei Hu, Sicong Gao, Jie Guo, Lun Hu, Xin Luo
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-06-26
- DOI: Unavailable
- Categories: cs.LG, q-bio.GN
- Relevance: 3.7126007272480077
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2606.28459v1
- PDF: https://arxiv.org/pdf/2606.28459v1
- Local PDF: pdf/2026-07-01_02_scKDGM_ KAN-guided Dynamic Graph Masked Learning for Single-Cell RNA-seq Clustering.pdf

Single-cell RNA sequencing (scRNA-seq) clustering is essential for identifying cell types, but high dimensionality, sparsity, dropout, and technical noise hinder robust expression representation and cell graph construction. Existing masked autoencoders mainly use expression recovery for feature reconstruction, while graph clustering methods usually depend on fixed KNN graphs and do not feed recovered expression back into graph optimization. We propose scKDGM, a KAN-guided dynamic graph masked learning framework for scRNA-seq clustering. scKDGM uses graph-aware distribution preserving gene masking (GDP-Mask) to perturb cell identity, a KAN-based TAKGCN encoder to learn masked-view representations, mask-guided expression recovery to construct a dynamic graph, and cross-view contrastive learning to transfer recovery signals into topology updates. A ZINB loss models overdispersion and zero inflation. Experiments on 12 real scRNA-seq datasets show that scKDGM outperforms 10 baselines in average NMI and ARI.

## 3. Curvature-Guided Sheaf Diffusion for Unsupervised Community Detection on Heterophilic Graphs

- Authors: Feifan Wang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-06-29
- DOI: Unavailable
- Categories: cs.LG, cs.AI
- Relevance: 3.520893331598355
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2606.30249v1
- PDF: https://arxiv.org/pdf/2606.30249v1
- Local PDF: pdf/2026-07-01_03_Curvature-Guided Sheaf Diffusion for Unsupervised Community Detection on Heterophilic Graphs.pdf

Detecting communities in heterophilic graphs -- where connected nodes often belong to different classes -- is hard for unsupervised methods: classical modularity and spectral methods are feature agnostic, while deep graph-clustering methods rely on contrastive or generative machinery that is opaque. We propose Curvature-Guided Sheaf Diffusion (CGSD), a fully unsupervised community-detection algorithm that uses the discrete Forman--Ricci curvature of each edge as its single topological signal, propagated through every stage of an end-to-end pipeline. CGSD makes three concrete contributions: (i)~a curvature-gated sheaf-diffusion encoder that gates edge messages by $σ(κ_e)$ and is trained from three label-free structural losses (modularity, anti-collapse, curvature-weighted reconstruction); (ii)~a curvature-aware spectral clusterer (CSpec) that re-weights the $k$-NN affinity of the embedding by $σ(ακ_{e^*})$ before Ng--Jordan--Weiss; and (iii)~a unified label-free evaluation against nine truly-unsupervised baselines. On five heterophilic benchmarks (Cora, Cornell, Texas, Wisconsin, Chameleon), CGSD wins outright on Wisconsin and Chameleon and is competitive on the remaining three against nine unsupervised baselines. The gain over the strongest baseline is driven by the clusterer, not the encoder: on the same embedding, CSpec improves mean NMI from $0.091$ with $K$-Means to $0.107$ ($+15\%$, paired $t$-test $p=0.008$). The mechanism is interpretable: intra-community and inter-community curvature distributions are visibly separated. Code is open-sourced at https://github.com/woodywff/cgsd.

## 4. SemFlowRAG: Directed Semantic Flow from Abstraction to Evidence for Complex Reasoning

- Authors: Houyuan Qin, Rong Wu, Qinyuan Qin, Botian Shi, Jingjing Qu, Yang Sun, Pinlong Cai
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-06-26
- DOI: Unavailable
- Categories: cs.IR, cs.AI
- Relevance: 3.472197517799973
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2606.28447v1
- PDF: https://arxiv.org/pdf/2606.28447v1
- Local PDF: pdf/2026-07-01_04_SemFlowRAG_ Directed Semantic Flow from Abstraction to Evidence for Complex Reasoning.pdf

Retrieval-Augmented Generation (RAG) enhanced by Knowledge Graphs has shown promise in complex multi-hop reasoning tasks. However, existing graph-based retrieval methods typically rely on flat, undirected topologies. During the retrieval process, the probability flow often gets trapped in high-degree abstract concept nodes which we define as ``probability black holes'', leading to semantic drift and noise accumulation. To address this, we propose SemFlowRAG, a framework that reconstructs the flat retrieval space into a corpus-adaptive semantic gradient graph. This data-driven self-organization enables a hierarchical structure to emerge naturally from the data distribution, capturing the intrinsic semantic granularity of the corpus to suppress structural noise. By quantifying the semantic abstractness of entities through the embedding variance of their associated passages, we transform static undirected edges into directed semantic constraints. Furthermore, we design an abstractness-guided directed PageRank algorithm that forces the retrieval trajectory to follow a ``high-to-low semantic abstractness'' gradient. This mechanism ensures layer-by-layer evidence convergence, smoothly guiding the retrieval process from abstract concepts to specific document evidence. Extensive experiments on complex QA datasets demonstrate that SemFlowRAG effectively mitigates the ``probability black holes'' issue, outperforming existing baselines in both retrieval and downstream reasoning performance.

## 5. LeanRAG: Knowledge-Graph-Based Generation with Semantic Aggregation and Hierarchical Retrieval

- Authors: Yaoze Zhang, Rong Wu, Pinlong Cai, Xiaoman Wang, Guohang Yan, Song Mao, Ding Wang, Botian Shi
- Source: openalex
- Venue type: conference
- Journal: Proceedings of the AAAI Conference on Artificial Intelligence
- Publication status: formally_published
- Publication date: 2026-03-14
- DOI: https://doi.org/10.1609/aaai.v40i41.40789
- Categories: Topic Modeling, Advanced Graph Neural Networks, Information Retrieval and Search Behavior
- Relevance: 3.422292027401543
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://doi.org/10.1609/aaai.v40i41.40789
- PDF: https://ojs.aaai.org/index.php/AAAI/article/download/40789/44750
- Local PDF: Not downloaded

Retrieval-Augmented Generation (RAG) plays a crucial role in grounding Large Language Models by leveraging external knowledge, whereas the effectiveness is often compromised by the retrieval of contextually flawed or incomplete information. To address this, knowledge graph-based RAG methods have evolved towards hierarchical structures, organizing knowledge into multi-level summaries. However, these approaches still suffer from two critical, unaddressed challenges: high-level conceptual summaries exist as disconnected ``semantic islands'', lacking the explicit relations needed for cross-community reasoning; and the retrieval process itself remains structurally unaware, often degenerating into an inefficient flat search that fails to exploit the graph's rich topology. To overcome these limitations, we introduce LeanRAG, a framework that features a deeply collaborative design combining knowledge aggregation and retrieval strategies. LeanRAG first employs a novel semantic aggregation algorithm that forms entity clusters and constructs new explicit relations among aggregation-level summaries, creating a fully navigable semantic network. Then, a bottom-up, structure-guided retrieval strategy anchors queries to the most relevant fine-grained entities and then systematically traverses the graph's semantic pathways to gather concise yet contextually comprehensive evidence sets. The LeanRAG can mitigate the substantial overhead associated with path retrieval on graphs and minimize redundant information retrieval. Extensive experiments on four challenging QA benchmarks with different domains demonstrate that LeanRAG significantly outperforms existing methods in response quality while reducing 46% retrieval redundancy.

## 6. Beyond Visual Similarity: Rule-Guided Multimodal Clustering with explicit domain rules

- Authors: Kishor Datta Gupta, Mohd Ariful Haque, Marufa Kamal, Ahmed Rafi Hasan, Md. Mahfuzur Rahman, Roy George
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.4000411412860245
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.alvr-main.16/
- PDF: https://aclanthology.org/2026.alvr-main.16.pdf
- Local PDF: pdf/2026-07-01_06_Beyond Visual Similarity_ Rule-Guided Multimodal Clustering with explicit domain rules.pdf

Traditional clustering techniques often rely solely on similarity in the input data, limiting their ability to capture structural or semantic constraints that are critical in many domains. We introduce the Domain-Aware Rule-Triggered Variational Autoencoder (DART-VAE), a rule-guided multimodal clustering framework that incorporates domain-specific constraints directly into the representation learning process. DART-VAE extends the VAE architecture by embedding explicit rules, semantic representations, and data-driven features into a unified latent space, while enforcing constraint compliance through rule-consistency and violation penalties in the loss function. Unlike conventional clustering methods that rely only on visual similarity or apply rules as post-hoc filters, DART-VAE treats rules as first-class learning signals. The rules are generated by LLMs, structured into knowledge graphs, and enforced through a loss function combining reconstruction, KL divergence, consistency, and violation penalties. Experiments on aircraft and automotive datasets demonstrate that rule-guided clustering produces more operationally meaningful and interpretable clusters—for example, isolating UAVs, unifying stealth aircraft, or separating SUVs from sedans—while improving traditional clustering metrics. However, the framework faces challenges: LLM-generated rules may hallucinate or conflict, excessive rules risk overfitting, and scaling to complex domains increases computational and consistency difficulties. By combining rule encodings with learned representations, DART-VAE achieves more meaningful and consistent clustering outcomes than purely data-driven models, highlighting the utility of constraint-guided multimodal clustering for complex, knowledge-intensive settings.

## 7. Measuring Graph-to-Graph Semantic Similarity in Knowledge Graphs: An Empirical Evaluation of Knowledge Graph Embeddings

- Authors: Seungryeol Baek, Wooseok Sim, Hogun Park
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-06-28
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 3.3895364364389993
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2606.29180v1
- PDF: https://arxiv.org/pdf/2606.29180v1
- Local PDF: pdf/2026-07-01_07_Measuring Graph-to-Graph Semantic Similarity in Knowledge Graphs_ An Empirical Evaluation of Knowledge Graph Embeddings.pdf

A Knowledge Graph (KG) represents facts as structured triples and is widely used to organize relational knowledge across diverse domains. Just as textual information ranges from words and sentences to complete documents, KG information can be interpreted at multiple levels, from entities, relations, and triples to subgraphs and entire KGs. However, existing KG embedding methods mainly focus on entities, relations, and triples, leaving graph-level semantics largely unaddressed. Conventional graph-level methods, which typically compare graphs based on structural patterns, are also insufficient because structural similarity alone cannot guarantee semantic similarity between KGs. To evaluate how well different methods capture such graph-level semantic information, we study graph-to-graph semantic similarity, which determines whether a pair of KGs represents semantically corresponding underlying information. To obtain reliable ground-truth correspondences, we construct a semantic matching dataset by modifying text documents, extracting KGs from both original and modified documents, and transferring their known correspondences to KG pairs. We compare text-based, structure-based, and KG embedding-based approaches on each dataset. For the KG embedding-based approach, we introduce two scoring functions: \textit{EmbPairSim}, which uses maximal pairwise entity similarity, and \textit{AvgEmbSim}, which uses a frequency-weighted centroid. Experiments on WikiText-2 and CC-News show that \textit{EmbPairSim} achieves up to 5.3 pp higher MRR than Sentence-BERT while using substantially fewer parameters. These results suggest that KGE representations can serve as compact and effective signals for graph-to-graph semantic similarity in KGs. Our code is available at https://github.com/SeungRyeolBaek/KG-to-KG-Semantic-Similarity.

## 8. Hierarchy-Aware Hyperbolic and Semantic Reranking for Ontology-Based Phenotype Linking

- Authors: Thomas Labbe, Moussa Baddour, Axel Bonesteve, Paul Rollier, Marie De Tayrac, Olivier Dameron
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.3362424842298752
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.bionlp-1.5/
- PDF: https://aclanthology.org/2026.bionlp-1.5.pdf
- Local PDF: pdf/2026-07-01_08_Hierarchy-Aware Hyperbolic and Semantic Reranking for Ontology-Based Phenotype Linking.pdf

Extracting structured knowledge from unstructured text is a fundamental challenge in machine learning, particularly for concepts organized within complex hierarchical ontologies. In genomics, identifying phenotypes from clinical narratives is crucial for diagnostic precision, yet current methods struggle with contextual interpretation and subtle clinical descriptions. We present a hierarchy-aware workflow for ontology-based phenotype linking that combines semantic and hierarchical signals. Our approach integrates Large Language Models for span detection with retrieval and a hybrid reranking strategy using both Euclidean (semantic) and hyperbolic (hierarchical) embeddings trained on the Human Phenotype Ontology. We show that while hyperbolic embeddings alone do not outperform standard semantic retrieval, they provide complementary structural signals that improve performance over strong baselines when combined with Euclidean representations. In particular, the hybrid approach outperforms existing state-of-the-art methods and yields more hierarchically coherent predictions, especially in settings involving implicit phenotype mentions. Experiments on a public benchmark (ID-68) and a newly released clinical dataset (CHU-50), publicly released with code and data, highlight both performance gains and improved alignment with ontology structure. We further introduce a hierarchy-aware evaluation framework that reflects clinical relevance beyond exact-match metrics.

## 9. AnTenA: Actionable and Explainable Tensor Analysis System with Large Language Models

- Authors: Dawon Ahn, Auder Der, Evangelos E. Papalexakis
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-06-27
- DOI: Unavailable
- Categories: cs.CL, cs.LG
- Relevance: 3.3312868134846116
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2606.28708v1
- PDF: https://arxiv.org/pdf/2606.28708v1
- Local PDF: pdf/2026-07-01_09_AnTenA_ Actionable and Explainable Tensor Analysis System with Large Language Models.pdf

Accurately explaining hidden patterns in multi-aspect data has typically been done by leveraging labels and/or accompanying auxiliary metadata. However, labels and auxiliary data may be inaccurate (e.g. nonstandard, inconsistent), insufficient (e.g. static tabular metadata for time-dependent recordings), or unavailable. %
We propose \fullmethod (\method), which leverages the knowledge of large language models (LLMs) to explain the hidden patterns in human narratives. \method uses task-agnostic and task-specific prompts to explain extracted co-clustered latent patterns from tensor decomposition. To evaluate these explanations, we test the LLMs on forward and backward inference tasks. % Our demo system is available at https://github.com/dawonahn/ECML_PKDD_AnTenA.

## 10. Unlocking the Visual Record of Materials Science: A Large-Scale Multimodal Dataset from Scientific Literature

- Authors: Subham Ghosh, Shubham Tiwari, Mohammad Ibrahim, Abhishek Tewari
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-06-29
- DOI: Unavailable
- Categories: cs.CV, cond-mat.mtrl-sci, cs.AI
- Relevance: 3.2815401988476056
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2606.29667v1
- PDF: https://arxiv.org/pdf/2606.29667v1
- Local PDF: pdf/2026-07-01_10_Unlocking the Visual Record of Materials Science_ A Large-Scale Multimodal Dataset from Scientific Literature.pdf

The materials science literature encodes decades of experimental knowledge in figures, yet this visual record remains locked away and inaccessible to AI at scale. The core difficulty is structural: most scientific figures are compound, with a single caption describing multiple sub-panels simultaneously, making direct image-text pairing unreliable. We present MatMMExtract, an end-to-end open-source pipeline that resolves this by decomposing compound figures into individual sub-panels and generating structured, grounded annotations using a large language model guided by a curated materials science taxonomy. Applied to 14,810 open-access articles, MatMMExtract produces MatSciFig; 391,606 panel-level image-text pairs from 180,571 figures, each annotated with a sub-caption, a two-level visualisation category spanning 19 classes and over 100 subtypes, and a scientific summary. To enable accurate panel localisation, we introduce MaterialScope, a domain-specific detection dataset of 2,811 manually annotated materials science figures, on which a fine-tuned YOLO12-m detector achieves mAP_50 of 0.9227. Among six benchmarked language models, Gemini 3.1 Flash Lite delivers the best cost-quality trade-off for annotation generation, with 82% of outputs rated good and a hallucination rate of 4.8%. A dual-encoder retrieval baseline on MatSciFig achieves a 4.4 times improvement in R@1 over zero-shot CLIP, demonstrating the dataset's immediate utility for vision-language learning. All resources are released openly to the community.

## 11. Impact of molecular multimodality on neural network models for prediction tasks related to drug discovery

- Authors: Marcos Martínez Galindo, Marco Luca Sbodio, Mykhaylo Zayats, Rodrigo Ordonez-Hurtado, Raúl Fernández-Díaz, Vanessa Lopez Garcia, Hoang Thanh Lam
- Source: openalex
- Venue type: journal
- Journal: Nature Communications
- Publication status: published
- Publication date: 2026-06-29
- DOI: https://doi.org/10.1038/s41467-026-74487-x
- Categories: Computational Drug Discovery Methods, Machine Learning in Bioinformatics, Machine Learning in Materials Science
- Relevance: 3.263000862213712
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://doi.org/10.1038/s41467-026-74487-x
- PDF: Unavailable
- Local PDF: Not downloaded

The number of unimodal molecule representation constantly increases, and researchers investigate how to combine them. Intuitively, multimodal representations may provide complementary information and combining them promises better performance. In this work, we systematically explore how combining multiple molecular modalities affects the performance of downstream prediction tasks, providing a baseline for informed decision making. Our study covers 7 molecular modalities and combines them using intermediate and late fusion, and 2 neural network architectures (with or without using knowledge graphs). We conduct experiments with 3 benchmarks for drug-target binding affinity, and 22 molecule property prediction. In total, we train and evaluate over 1400 models. In summary, our results show that combining multiple modalities improve the performance provided that effective fusion strategies are chosen. Knowledge-enhanced representation learning further boosts model performance. Notably, we find that even the use of simple late-fusion approaches establishes state-of-the-art results for some tasks. Here, the authors examine whether combining multiple molecular data types improves drug discovery models, finding multimodal approaches boost predictions with effective fusion, and even simple late-fusion methods can reach state-of-the-art performance.

## 12. ScaleAware-JEPA: Latent Representation for Discovery in Multiscale Physical Fields

- Authors: Guang-Xing Li
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-06-29
- DOI: Unavailable
- Categories: cs.LG, astro-ph.IM, cs.CV, physics.comp-ph
- Relevance: 3.194964064522672
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2606.29723v1
- PDF: https://arxiv.org/pdf/2606.29723v1
- Local PDF: pdf/2026-07-01_12_ScaleAware-JEPA_ Latent Representation for Discovery in Multiscale Physical Fields.pdf

Continuous physical fields represent a large fraction of data under scientific investigation. Their multiscale structures are central to discovery, yet useful coordinates are not known in advance. Standard self-supervised methods define context and targets in fixed image coordinates, posing a predictive task misaligned with fields organized across a continuous scale hierarchy. We introduce ScaleAware-JEPA, a framework that constructs dense, label-free latent coordinates for continuous scalar fields. Constrained Diffusion Decomposition (CDD) separates each field into pixel-registered scale components and provides the scale coordinates that define the masking geometry. The resulting JEPA objective predicts hidden structure with a context footprint tied to the diffusion scale of each component rather than to an arbitrary patch size. Across MHD turbulence, interstellar molecular gas and urban nighttime-light structure, the learned geometry maps back to coherent morphology, forming dense structural atlases without labels or predefined segmentation rules. By tying latent prediction to the scale hierarchy of a field, ScaleAware-JEPA constructs latent coordinates through which complex physical patterns can be inspected before their relevant structures have been prescribed. Code is available at https://github.com/gxli/SA-JEPA.

## 13. Beyond Knowledge Graphs: PubMedBERT Embeddings as a Competitive Standalone Modality for Drug Re-purposing

- Authors: Rishik Kondadadi, John E. Ortega
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.1630983046860224
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.bionlp-1.13/
- PDF: https://aclanthology.org/2026.bionlp-1.13.pdf
- Local PDF: pdf/2026-07-01_13_Beyond Knowledge Graphs_ PubMedBERT Embeddings as a Competitive Standalone Modality for Drug Re-purposing.pdf

Drug repurposing methods rely heavily on knowledge graph (KG) embeddings, but building and curating these graphs takes considerable effort. We present two findings on the Hetionet drug-disease benchmark and an epilepsy ranking task. First, PubMedBERT text embeddings, fed through the same downstream classifiers and identical 10-fold splits as four re-trained KG baselines (TransE, ComplEx, DistMult, RotatE), reach AUROC $0.910$, above all four (best: RotatE, $0.854$); a Random Forest on the same vectors scores $0.880$. The comparison is asymmetric in one important way: PubMedBERT was pretrained on the literature Hetionet was curated from, so the result is best read as “text-with-literature-supervision vs.graph-only,” and a head-to-head with text-augmented KG methods (KG-BERT, TxGNN) is left as follow-up. Second, across all seven combinations of text, molecular (ECFP4), and gene expression (LINCS L1000) features, cross-attention fusion of weaker modalities into text consistently degrades performance, despite a gated mechanism intended to suppress unhelpful modalities; the residual path forces the strong modality to absorb noise. The model also ranks proconvulsants (amoxapine, flumazenil) near the top, because text embeddings encode strength of association with a disease but not its direction.

## 14. Low-cost concept-based localized explanations: How far can we get with training-free approaches?

- Authors: Darian Fernández-Gutiérrez, Rafael Bello, Marilyn Bello, Natalia Díaz-Rodríguez
- Source: arxiv
- Venue type: preprint
- Journal: 2026 IEEE International Conference on Artificial Intelligence (CAI), Granada, Spain, 2026, pp. 1405-1410
- Publication status: preprint
- Publication date: 2026-06-27
- DOI: 10.1109/CAI68641.2026.11536419
- Categories: cs.AI, cs.CL, cs.CV
- Relevance: 3.162453149655204
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2606.29069v1
- PDF: https://arxiv.org/pdf/2606.29069v1
- Local PDF: pdf/2026-07-01_14_Low-cost concept-based localized explanations_ How far can we get with training-free approaches.pdf

Concept-based Explainable AI (C-XAI) seeks human-understandable explanations grounded in semantic concepts, yet validation is limited by the scarcity of fine-grained concept annotations. We evaluate whether mid-scale Multimodal Large Language Models (MLLMs) can perform localized concept naming under strict zero-shot conditions by assigning labels to bounding-box regions at both object and part levels. We propose a reproducible zero-shot evaluation protocol for Concept Naming (CoNa) with (i) closed-set, category-constrained prompting for moderate vocabularies and (ii) Open-CoNa, an embedding-similarity-based strategy for large label spaces. Experiments with four MLLMs (7B-32B) show consistent performance trends across datasets, reaching 62%-88% object-level exact-match accuracy, highlighting the potential of training-free concept annotation from localized regions. We discuss limitations and failure modes and release a reproducible framework to support future low-cost C-XAI research.

## 15. TopoAgent: An Agentic Framework for Automated Topology Learning in Medical Imaging

- Authors: Guangyu Meng, Pengfei Gu, Xueyang Li, Yiyu Shi, Erin Wolf Chambers, Danny Z. Chen
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-06-29
- DOI: Unavailable
- Categories: cs.CV, cs.AI
- Relevance: 3.161058870416541
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2606.29763v1
- PDF: https://arxiv.org/pdf/2606.29763v1
- Local PDF: pdf/2026-07-01_15_TopoAgent_ An Agentic Framework for Automated Topology Learning in Medical Imaging.pdf

Topological data analysis (TDA), particularly persistent homology (PH), captures geometric structural properties in medical images (e.g., connected components, loops, shape characteristics), which conventional pixel-level deep learning approaches often neglect. While many topological descriptors are known for converting persistence diagrams (PDs) or raw images into topological feature vectors, existing methods mostly default to a single fixed descriptor (e.g., persistence images), leaving the diversity of topological representations largely unexplored. To the best of our knowledge, there is no known large language model (LLM)-based agentic framework that can automatically determine the most suitable topological descriptors for a given image dataset and produce the corresponding topological feature vectors for downstream tasks. To fill this gap, we propose \textbf{TopoAgent}, an LLM-based agentic framework that automates topology learning for medical image analysis.TopoAgent operates through a Perception--Reasoning--Action--Reflection loop supported by 21 domain-specific tools and dual memory that accumulates experience across runs. Its skill set is distilled from systematic evaluation of 15 topological descriptors across 26 datasets with six classifiers. TopoAgent analyzes input images and their topological characteristics, reasons about which topological descriptors best suit the input, and determines the optimal descriptor and its configuration, all without task-specific training.

## 16. Dynamic Graph Navigation via Triplet Chains for Structure-Aware Retrieval-Augmented Generation

- Authors: Feng Zhao, Yufei Wu, Xianggan Liu, Ruilin Zhao
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.1545055195295415
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1360/
- PDF: https://aclanthology.org/2026.findings-acl.1360.pdf
- Local PDF: pdf/2026-07-01_16_Dynamic Graph Navigation via Triplet Chains for Structure-Aware Retrieval-Augmented Generation.pdf

Retrieval-Augmented Generation (RAG) was proposed to address the hallucination question of large language models (LLMs). However, the traditional RAG framework has certain limitations: for simple questions, the search results often introduce a large amount of irrelevant information; while for complex questions, the lengthy reference knowledge provided by the retrieval lacks structural information. Therefore, we proposed a structure-aware RAG, which achieves noise removal in retrieval through multi-chain graph navigation reasoning(Trig-Nav). This method constructs question triple reasoning chains and reference knowledge graphs with text attributes, allowing the system to retrieve three types of knowledge along different paths based on the requirements of LLM. It provides LLM with multi-angle and structured information input and significantly reduces noise. We conducted a comprehensive evaluation of Trig-Nav, comparing it with baseline methods across multiple datasets.Compared to traditional RAG, there is an average improvement of 6% in effectiveness. The results showed that Trig-Nav significantly enhances the model’s performance, validating the effectiveness of this approach.

## 17. SocraticKG: Knowledge Graph Construction via QA-Driven Fact Extraction

- Authors: Sanghyeok Choi, Woosang Jeon, Kyuseok Yang, Taehyeong Kim
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.1520293420204126
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1951/
- PDF: https://aclanthology.org/2026.findings-acl.1951.pdf
- Local PDF: pdf/2026-07-01_17_SocraticKG_ Knowledge Graph Construction via QA-Driven Fact Extraction.pdf

Constructing Knowledge Graphs (KGs) from unstructured text provides a structured framework for knowledge representation and reasoning, yet current LLM-based approaches struggle with a fundamental trade-off: factual coverage often leads to relational fragmentation, while premature consolidation causes information loss. To address this, we propose SocraticKG, an automated KG construction method that introduces question-answer pairs as a structured intermediate representation to systematically unfold document-level semantics prior to triple extraction. By employing 5W1H-guided QA expansion, SocraticKG captures contextual dependencies and implicit relational links typically lost in direct KG extraction pipelines, providing explicit grounding in the source document that helps mitigate implicit reasoning errors. Evaluation on the MINE benchmark demonstrates that our approach effectively addresses the coverage-connectivity trade-off, achieving superior factual retention while maintaining high structural cohesion even as extracted knowledge volume substantially expands. These results highlight that QA-mediated semantic scaffolding plays a critical role in structuring semantics prior to KG extraction, enabling more coherent and reliable graph construction in subsequent stages.

## 18. LLMRouterBench: A Massive Benchmark and Unified Framework for LLM Routing

- Authors: Hao Li, Yiqun Zhang, Zhaoyan Guo, Chenxu Wang, Shengji Tang, Qiaosheng Zhang, Yang Chen, Biqing Qi, Peng Ye, Lei Bai, Zhen Wang, Shuyue Hu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.14782969591332
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1881/
- PDF: https://aclanthology.org/2026.findings-acl.1881.pdf
- Local PDF: pdf/2026-07-01_18_LLMRouterBench_ A Massive Benchmark and Unified Framework for LLM Routing.pdf

Large language model (LLM) routing assigns each query to the most suitable model from an ensemble. We introduce LLMRouterBench, a large-scale benchmark and unified framework for LLM routing. It comprises over 400K instances from 21 datasets and 33 models. Moreover, it provides comprehensive metrics for both performance-oriented and performance-cost trade-off routing, and integrates 10 representative routing baselines. Using LLMRouterBench, we systematically re-evaluate the field. While confirming strong model complementarity—the central premise of LLM routing—we find that many routing methods exhibit similar performance under unified evaluation, and several recent approaches, including commercial routers, fail to reliably outperform a simple baseline. Meanwhile, a substantial gap remains to the Oracle, driven primarily by persistent model-recall failures. We further show that backbone embedding models have limited impact, that larger ensembles exhibit diminishing returns compared to careful model curation, and that the benchmark also enables latency-aware analysis. All code and data are available at https://github.com/ynulihao/LLMRouterBench.

## 19. Orthogonal Representation Editing: Decoupling Semantic Entanglement in Batch Knowledge Editing of LLMs

- Authors: Wenhao Yu, Zhicong Lu, Bo Lv, Fangyin Ma, Kaiwen Wei, Shihao Yang, Nayu Liu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.14431323091331
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1892/
- PDF: https://aclanthology.org/2026.findings-acl.1892.pdf
- Local PDF: pdf/2026-07-01_19_Orthogonal Representation Editing_ Decoupling Semantic Entanglement in Batch Knowledge Editing of LLMs.pdf

Knowledge editing aims to efficiently update factual information in Large Language Models (LLMs) without full retraining. However, existing methods still suffer from performance degradation in batch knowledge editing. We identify that semantic representation entanglement, such as overlapping concepts and shared syntactic patterns, accumulates interference in the representation space and reduces editing precision. To bridge this gap, in this paper, we propose Orthogonal Representation Editing (ORE), which performs edits in the hidden representation space of LLMs by constructing a general semantic subspace and enforcing orthogonal constraints on edit vectors, effectively decoupling semantic entanglement. Furthermore, we introduce a gated non-linear representation head to enable adaptive learning of editing locations and precise control over knowledge injection. Extensive experiments show that ORE outperforms existing methods and achieves superior performance in cross-lingual knowledge editing scenarios. We release our code at https://github.com/YVVH/ORE.

## 20. Can LLMs See Without Pixels? Benchmarking Spatial Intelligence from Textual Descriptions

- Authors: Zhongbin Guo, Zhen Yang, Yushan Li, Xinyue Zhang, Wenyu Gao, Jiacheng Wang, Chengzhi Li, Xiangrui Liu, Ping Jian
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.13636695393954
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.90/
- PDF: https://aclanthology.org/2026.findings-acl.90.pdf
- Local PDF: pdf/2026-07-01_20_Can LLMs See Without Pixels_ Benchmarking Spatial Intelligence from Textual Descriptions.pdf

Recent advancements in Spatial Intelligence (SI) have predominantly relied on Vision-Language Models (VLMs), yet a critical question remains: does spatial understanding originate from visual encoders or the fundamental reasoning backbone? Inspired by this question, we introduce **SiT-Bench**, a novel benchmark designed to evaluate the SI performance of Large Language Models (LLMs) without pixel-level input, comprises over 3,800 expert-annotated items across five primary categories and 17 subtasks, ranging from egocentric navigation and perspective transformation to fine-grained robotic manipulation. By converting single/multi-view scenes into high-fidelity, coordinate-aware textual descriptions, we challenge LLMs to perform symbolic textual reasoning rather than visual pattern matching. Evaluation results of state-of-the-art (SOTA) LLMs reveals that while models achieve proficiency in localized semantic tasks, a significant "spatial gap" remains in global consistency. Notably, we find that explicit spatial reasoning significantly boosts performance, suggesting that LLMs possess latent world-modeling potential. Our proposed dataset SiT-Bench serves as a foundational resource to foster the development of spatially-grounded LLM backbones for future VLMs and embodied agents.

## 21. PseudoGD: Enhancing Spatial Reasoning in Vision-Language Models through Pseudo Geometric Knowledge Distillation

- Authors: Gwanghee Lee, Yeeun Choi, Kyoungson Jhang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.1342012961427557
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1539/
- PDF: https://aclanthology.org/2026.findings-acl.1539.pdf
- Local PDF: pdf/2026-07-01_21_PseudoGD_ Enhancing Spatial Reasoning in Vision-Language Models through Pseudo Geometric Knowledge Distillation.pdf

Recent Large Vision-Language Models (LVLMs) have shown remarkable success in general semantic understanding. However, they still struggle with 3D spatial reasoning tasks, such as estimating metric distances or understanding precise relative positions. Previous works, like SpatialVLM, tried to address this by using synthesized spatial VQA dataset. However, they are fundamentally limited because their vision encoders are biased toward 2D patterns learned from image-text pairs. In this paper, we argue that this lack of 3D awareness is a critical bottleneck that cannot be solved by data scaling alone. To address this, we propose Pseudo Geometric Distillation (PseudoGD), a framework designed to help vision encoders internalize 3D geometric information using only standard 2D images. PseudoGD explicitly injects metric scale and structural context into the encoder through a Joint Training strategy. This approach optimizes geometric learning and spatial VQA tasks together, ensuring that the Large Language Model (LLM) aligns well with the improved visual features in real-time. Extensive experiments on the OmniSpatial benchmark demonstrate that PseudoGD achieves State-of-the-Art (SOTA) performance across various model architectures. Notably, significant improvements in Hypothetical Perspective Taking and Locate tasks prove that our model has effectively learned a physical sense of space.

## 22. Thought-Action Graph Reasoning: Faithful and Efficient Reasoning of Large Language Models via Reusing Past Experience

- Authors: Zhixiao Qi, Feng Huang, Yunqi Zhang, Shijie Zhang, Qingqing Sun, Yongfeng Huang, Minghu Jiang, Shuai Chen, Tianyi Zhang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.126746740693118
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1572/
- PDF: https://aclanthology.org/2026.findings-acl.1572.pdf
- Local PDF: pdf/2026-07-01_22_Thought-Action Graph Reasoning_ Faithful and Efficient Reasoning of Large Language Models via Reusing Past Experience.pdf

Large language models (LLMs) often hallucinate in question answering (QA) tasks due to a lack of factual knowledge. While integrating knowledge graphs (KGs) with LLMs has alleviated this issue, existing methods suffer from poor generalization or low reasoning efficiency, and critically, they overlook the learning and reuse of reasoning paths from past experiences. To address these challenges, we introduce Thought-Action Graph (TAG), a structured repository of reasoning experiences. TAG decomposes successful LLM-KG interaction trajectories into fine-grained semantic operators, which are stored in TAG constructed by the thought layer and action layer. Building upon TAG, we propose a novel KGQA paradigm — TAG-Reasoning (TAGR). TAGR first retrieves and assembles reasoning blueprints from TAG, and then guides LLM to efficiently execute on KG according to them. Through this approach, TAGR transforms the computationally expensive online exploration process of LLMs into an offline process of TAG retrieval and assembly. Experimental results on multiple KGQA benchmarks demonstrate that TAGR significantly outperforms state-of-the-art methods across key metrics, while drastically reducing the number of LLM calls and generated tokens. This work opens new avenues for building continual learning, efficient, and faithful KGQA systems.

## 23. C$^{2}$R: Cross-sample Consistency Regularization Mitigates Feature Splitting and Absorption in Sparse Autoencoders

- Authors: Haoran Jin, Xiting Wang, Shijie Ren, Hong Xie, Defu Lian
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-06-29
- DOI: Unavailable
- Categories: cs.LG, cs.AI
- Relevance: 3.126441636637758
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2606.30609v1
- PDF: https://arxiv.org/pdf/2606.30609v1
- Local PDF: pdf/2026-07-01_23_C$^{2}$R_ Cross-sample Consistency Regularization Mitigates Feature Splitting and Absorption in Sparse Autoencoders.pdf

Sparse Autoencoders (SAEs) are widely used to interpret large language models by decomposing activations into sparse, human-understandable features, but scaling to large dictionaries exposes fundamental challenges. Systematic studies reveal pervasive feature splitting that fragments coherent concepts into non-atomic latents and widespread feature absorption that creates arbitrary exceptions in general features, severely compromising latent reliability. These issues stem from inconsistent latent assignment across samples: without cross-sample constraints, per-sample optimization often allows a single underlying concept to be inconsistently distributed across multiple redundant or interfering latents. To address this, we introduce C$^2$R (\underline{\textbf{C}}ross-sample \underline{\textbf{C}}onsistency \underline{\textbf{R}}egularization). C$^2$R explicitly encourages that each semantic feature is consistently represented by a unified latent across the batch by penalizing the co-activation of directionally similar latents. Comprehensive evaluation demonstrates that C$^2$R effectively mitigates both splitting and absorption while, crucially, preserving reconstruction fidelity, providing a principled solution that enhances latent interpretability without degrading model performance. Source code is available at https://github.com/hr-jin/Cross-sample-Consistency-Regularization.

## 24. RCTEA: Richness-guided Co-training for Temporal Entity Alignment

- Authors: Jiayun Li, Wen Hua, Shiqi Fan, Fengmei Jin, Haiyang Jiang, Xue Li
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.122833419407729
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1958/
- PDF: https://aclanthology.org/2026.findings-acl.1958.pdf
- Local PDF: pdf/2026-07-01_24_RCTEA_ Richness-guided Co-training for Temporal Entity Alignment.pdf

Temporal Entity Alignment (TEA), which aims to identify equivalent entities across Temporal Knowledge Graphs (TKGs), is crucial for integrating knowledge facts from multiple sources. However, existing TEA models often fail to capture the orthogonal yet complementary effect between structural and temporal features, and typically overlook the importance of information richness—a key factor for effective message passing in the neural feature encoders. To address these limitations, we propose a RCTEA framework that jointly models both structural and temporal aspects of the TKGs for entity alignment. Specifically, we design a richness-guided attention mechanism along with an adaptive weighting strategy to facilitate effective feature fusion. To ensure robust alignment despite noisy entity contexts, we introduce a dual-view neighborhood consensus algorithm that jointly refines the feature encoders to enforce local structural consistency of the predicted alignments. Extensive experiments demonstrate the superiority of RCTEA, achieving state-of-the-art performance on public TEA benchmarks.

## 25. StructKV: Preserving the Structural Skeleton for Scalable Long-Context Inference

- Authors: Zhirui Chen, Peiyang Liu, Ling Shao
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.12168329806303
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.621/
- PDF: https://aclanthology.org/2026.findings-acl.621.pdf
- Local PDF: pdf/2026-07-01_25_StructKV_ Preserving the Structural Skeleton for Scalable Long-Context Inference.pdf

As Large Language Models (LLMs) scale to support context windows exceeding one million tokens, the linear growth of Key-Value (KV) cache imposes severe memory capacity and bandwidth bottlenecks, constraining the efficiency of long-context inference. Existing compression approaches typically prioritize tokens based on local saliency metrics to decouple prefill computation from decoding memory. However, these methods often rely on local saliency snapshots at a specific layer, thereby systematically discarding tokens that act as global information hubs across the network depth but appear temporarily dormant at the specific layer selected for pruning. To address this limitation, we propose StructKV , a structure-aware KV cache compression framework that introduces three core innovations: First, Global In-Degree Centrality aggregates attention patterns across the network depth to identify global information hubs. Second, Dynamic Pivot Detection utilizes information-theoretic metrics to adaptively locate the optimal layer for compression. Finally, Structural Propagation Decoupling separates the computational budget from the memory storage budget. Experimental results on the LongBench and RULER benchmarks demonstrate that StructKV effectively preserves long-range dependencies and retrieval robustness.

## 26. Self-Evolving Multi-Agent Systems via Textual Backpropagation

- Authors: Xiaowen Ma, Yunpu Ma, Chenyang Lin, Sikuan Yan, Jinhe Bi, Zixuan Cao, Yijun Tian, Volker Tresp, Hinrich Schuetze
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.119028192411199
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.483/
- PDF: https://aclanthology.org/2026.findings-acl.483.pdf
- Local PDF: pdf/2026-07-01_26_Self-Evolving Multi-Agent Systems via Textual Backpropagation.pdf

Leveraging multiple Large Language Models (LLMs) has proven effective for addressing complex, high-dimensional tasks, but current approaches often rely on static, manually engineered multi-agent configurations. To overcome these constraints, we present the Agentic Neural Network ( ANN ), a framework that conceptualizes multi-agent collaboration as a layered neural network architecture. In this design, each agent operates as a node, and each layer forms a cooperative team focused on a specific subtask. The proposed framework follows a two-phase optimization strategy: (1) Forward Phase - Drawing inspiration from neural network forward passes, tasks are dynamically decomposed into subtasks, and cooperative agent teams with suitable aggregation methods are constructed layer by layer. (2) Backward Phase - Mirroring backpropagation, we refine both global and local collaboration through iterative feedback, allowing agents to self-evolve their roles, prompts, and coordination. This neuro-symbolic approach enables our framework to create new or specialized agent teams post-training, delivering notable gains in accuracy and adaptability. Across seven benchmark datasets, ANN surpasses leading multi-agent baselines under the same configurations, showing consistent performance improvements.

## 27. Bayesian Active Learning with Gaussian Processes Guided by LLM Relevance Scoring for Dense Passage Retrieval

- Authors: Junyoung Kim, Anton Korikov, Jiazhou Liang, Justin Cui, Yifan Simon Liu, Qianfeng Wen, Mark Zhao, Scott Sanner
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.1159481293255227
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.481/
- PDF: https://aclanthology.org/2026.findings-acl.481.pdf
- Local PDF: pdf/2026-07-01_27_Bayesian Active Learning with Gaussian Processes Guided by LLM Relevance Scoring for Dense Passage Retrieval.pdf

While Large Language Models (LLMs) exhibit exceptional zero-shot relevance modeling, their high computational cost necessitates framing passage retrieval as a budget-constrained global optimization problem. Existing approaches passively rely on first-stage dense retrievers, which leads to two limitations: (1) failing to retrieve relevant passages in semantically distinct clusters, and (2) failing to propagate relevance signals to the broader corpus. To address these limitations, we propose Bayesian Active Learning with Gaussian Processes guided by LLM relevance scoring (BAGEL), a novel framework that propagates sparse LLM relevance signals across the embedding space to guide global exploration. BAGEL models the multimodal relevance distribution across the entire embedding space with a query-specific Gaussian Process (GP) based on LLM relevance scores. Subsequently, it iteratively selects passages for scoring by strategically balancing the exploitation of high-confidence regions with the exploration of uncertain areas. Extensive experiments across four benchmark datasets and two LLM backbones demonstrate that BAGEL effectively explores and captures complex relevance distributions and outperforms LLM reranking methods under the same LLM budget on all four datasets.

## 28. EvoMemKG: An Evolvable Memory Agent for Multi-hop Knowledge Graph Reasoning

- Authors: Shiyu Tian, Shuyue Xing, Zhuoxin Han, Caixia Yuan, Xiaojie Wang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.114148461108592
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1587/
- PDF: https://aclanthology.org/2026.findings-acl.1587.pdf
- Local PDF: pdf/2026-07-01_28_EvoMemKG_ An Evolvable Memory Agent for Multi-hop Knowledge Graph Reasoning.pdf

Integrating knowledge graphs (KGs) with large language models (LLMs) enhances factual accuracy and interpretability in question answering. However, existing agent-based methods rely on static memory mechanisms that fail to address the combinatorial explosion of search spaces in multi-hop reasoning and lack continuous learning capabilities. To overcome these limitations, we propose EvoMemKG, an agent framework with a dynamic, evolvable memory mechanism specifically designed for KG reasoning. EvoMemKG features a dual-layer memory architecture: (1) a working memory that losslessly compresses retrieved triplets through clustering to manage exploration states, effectively linearizing the exponential state space expansion; and (2) an experience memory that abstracts historical reasoning paths into reusable, generalized strategies, enabling cross-task knowledge transfer and self-evolution. We further introduce a double-loop workflow that orchestrates the LLM, memory layers, and KG environment to enable end-to-end autonomous reasoning. Extensive evaluations on three KGQA datasets across two KGs demonstrate that EvoMemKG achieves state-of-the-art performance without requiring additional training or specialized tools. Notably, it achieves improvements of up to 20% over the strong baseline on complex multi-hop queries, validating the effectiveness of our dynamic memory approach.

## 29. Towards Self-Evolving Agents: Enabling Autonomy through Interactive Experience Refinement

- Authors: Cheng Yang, Xuemeng Yang, Licheng Wen, Daocheng Fu, Jianbiao Mei, Rong Wu, Pinlong Cai, Yufan Shen, Nianchen Deng, Jia Xu, Botian Shi, Yu Qiao, Haifeng Li
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.1092718425005703
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1522/
- PDF: https://aclanthology.org/2026.findings-acl.1522.pdf
- Local PDF: pdf/2026-07-01_29_Towards Self-Evolving Agents_ Enabling Autonomy through Interactive Experience Refinement.pdf

Large Language Models often struggle with complex, multi-step operational tasks because they remain static during inference and cannot learn from past experience. To address this, we propose MUSE, a framework that enables iterative self-improvement through a hierarchical Memory Module. MUSE organizes cross-domain insights to facilitate the orchestration of long-horizon workflows. The core of our approach is an autonomous post-execution critique mechanism: after completing each sub-task, the system analyzes its operational logs and distills raw execution data into structured, reusable knowledge. This allows the agent to evolve dynamically rather than relying on fixed parameters. Evaluated on the rigorous TAC productivity benchmark, MUSE achieves new state-of-the-art results, significantly outperforming previous methods using only the streamlined Gemini-2.5 Flash model. Our analysis demonstrates that MUSE’s performance scales with the accumulation of insights and exhibits strong cross-task transferability, marking a key step toward autonomous systems capable of lifelong learning in professional environments. Demo videos can be found in our supplementary materials.

## 30. Beyond Neural Incompatibility: Cross-Scale Knowledge Transfer in Large Language Models through Latent Semantic Alignment

- Authors: Jian Gu, Aldeida Aleti, Chunyang Chen, Hongyu Zhang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.105645966147078
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1101/
- PDF: https://aclanthology.org/2026.findings-acl.1101.pdf
- Local PDF: pdf/2026-07-01_30_Beyond Neural Incompatibility_ Cross-Scale Knowledge Transfer in Large Language Models through Latent Semantic Alignment.pdf

Large Language Models (LLMs) encode substantial knowledge in their parameters, which can be located, traced, and analyzed. Despite recent progress in neural interpretability, it is still unclear how to transfer such knowledge in a fine-grained manner, namely parametric knowledge transfer (PKT). A central challenge is to make cross-scale transfer effective and efficient when source and target models differ in architecture and parameterization. Existing methods that directly reuse layer parameters are therefore strongly limited by neural incompatibility. In this paper, we identify latent semantic alignment as the key prerequisite for cross-scale knowledge transfer. Instead of directly moving layer parameters, our approach uses activations as the transfer medium. SemAlign has two stages: an layer attribution stage that attributes task-relevant source layers and selects exactly one source layer for each target layer, and a semantic alignment stage that pairs them from shallow to deep and optimizes the target with source-side supervisory hidden states. The alignment is carried out in latent space. In the current realization, training follows a shallow-to-deep frontier schedule: at each stage, only the current target layer is trainable, the layer objective is a Fisher-weighted quadratic surrogate on target-space aligned logits, and the final output layer keeps KL distillation. The transferred object nonetheless remains the aligned representation itself. Evaluations on four benchmarks demonstrate the efficacy of our method. Further analysis reveals the key factors that ease cross-scale knowledge transfer and provides insights into the nature of latent semantic alignment.
