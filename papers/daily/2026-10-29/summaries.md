# Paper Daily Reading - 2026-10-29

## 1. Graph Representation Learning via Adaptive Expectile Aggregation

- Authors: Tianyi Zhu, Wei Lan
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-27
- DOI: Unavailable
- Categories: stat.ML, cs.LG
- Relevance: 3.763681283992033
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.37450v1
- PDF: https://arxiv.org/pdf/2610.37450v1
- Local PDF: pdf/2026-10-29_01_Graph Representation Learning via Adaptive Expectile Aggregation.pdf

Graph neural networks (GNNs) rely critically on neighborhood aggregation, yet conventional mean aggregation may fail to capture class-relevant distributional information, particularly in heterophilic graphs. We propose ExpectileGCN, an adaptive graph aggregation framework that introduces a learnable expectile level to capture neighborhood information beyond the mean. The proposed operator continuously adjusts aggregation between minimum- and maximum-type behaviors, with mean aggregation as a special case. A differentiable approximation based on sigmoid smoothing and fixed-point iterations enables end-to-end optimization. Theoretically, we establish stability properties and transductive generalization guarantees for ExpectileGCN. We further investigate its classification risk under heterophilic neighborhood models. For informative neighborhoods, we show that expectile aggregation can exploit class-dependent scale differences to achieve a classification advantage over mean aggregation. Under a local asymptotic regime with diminishing per-neighbor label informativeness, we establish that this advantage can persist in terms of limiting classification risk. Experiments on homophilic and heterophilic benchmark graphs demonstrate strong predictive performance and improved robustness under feature corruption and structural perturbations.

## 2. Concorde: Geometry-Aware Link Prediction via Decoupled Energy Minimization

- Authors: Ege Demirci, Ambuj Singh
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-26
- DOI: Unavailable
- Categories: cs.LG, cs.AI
- Relevance: 3.7108661143290704
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.36204v1
- PDF: https://arxiv.org/pdf/2610.36204v1
- Local PDF: pdf/2026-10-29_02_Concorde_ Geometry-Aware Link Prediction via Decoupled Energy Minimization.pdf

Link prediction remains difficult in sparse graphs, where diffusion heuristics lack connectivity and geometric methods suffer spectral instability when coupling learned representations with diffusion operators. We introduce Concorde, an energy-based framework that resolves this by decomposing link likelihood into three structurally decoupled branches: (i) a parameter-free spectral anchor that establishes permutation-invariant topological stability; (ii) a mixed-curvature residual on a learnable $\mathbb{H}^{d_h}_{c_h} \times \mathbb{S}^{d_s}_{c_s}$ product manifold, regularized by a feature-aware Ollivier-Ricci curvature proxy; and (iii) a continuous vector field on the tangent bundle of hyperbolic space for non-local structural alignment across topological gaps. The branches are fused via learned gating and trained with an N-pair ranking loss aligned with retrieval-style evaluation. Across five benchmarks spanning sparse, dense, featureless, and attributed regimes, Concorde establishes state-of-the-art early retrieval precision, nearly doubling P@10% over leading baselines in sparse settings.

## 3. Prospector: learning a compact graph traversal policy for scientific reasoning

- Authors: Haiqian Yang, Markus J. Buehler
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-27
- DOI: Unavailable
- Categories: cs.AI, cond-mat.mtrl-sci, cs.CL, cs.LG
- Relevance: 3.3762701936470925
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.37121v1
- PDF: https://arxiv.org/pdf/2610.37121v1
- Local PDF: pdf/2026-10-29_03_Prospector_ learning a compact graph traversal policy for scientific reasoning.pdf

Scientific reasoning in specialized engineering fields depends on knowledge scattered across the literature, often proprietary and absent from frontier LLM training data. In such domains, frontier models tend to give generic answers. Knowledge graphs (KGs) can ground LLM reasoning. Because a graph is too large to provide in full, typical LLM+KG systems preselect a portion, deciding relevance before reasoning begins. Here we train a compact model, Prospector, to reason over a domain knowledge graph by traversing it step by step, seeking evidence in light of what it has already found. Prospector calls a small set of tools one at a time to progressively build its context, and answers with a chain of evidence that can be checked edge by edge against what its tools retrieved from the graph. On a knowledge graph built from the semiconductor-manufacturing literature, Prospector approaches the strongest off-the-shelf models given the same graph and tools, and it far exceeds off-the-shelf models answering closed-book or from a pre-selected portion of the graph. Although trained only on the semiconductor graph, Prospector transfers to unseen knowledge graphs from three other distinct fields: bio-inspired materials, per- and polyfluoroalkyl substances (PFAS) and materials properties. Served on a single GPU, Prospector answers faster and at a fraction of the cost of a hosted service, while keeping proprietary data on the owner's hardware. We find that the policy's latent state is indicative of its next move on both seen and unseen graphs, and modulating the latent state can steer the policy from one behavior mode to another. These results suggest a practical LLM + KG paradigm for scientific and engineering reasoning over private data, in which a compact model trained on a graph from published literature transfers its traversal to unseen graphs that stay with their owners.

## 4. Mitigating bias in spatial transcriptomic pipelines via human feedback with CSDE

- Authors: Pierre Boyeau, Stephen Bates, Can Ergen, Michael I. Jordan, Nir Yosef
- Source: openalex
- Venue type: journal
- Journal: Genome biology
- Publication status: published
- Publication date: 2026-10-27
- DOI: https://doi.org/10.1186/s13059-026-04302-9
- Categories: Single-cell and spatial transcriptomics, Gene expression and cancer classification, Cell Image Analysis Techniques
- Relevance: 3.3520072722442453
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://doi.org/10.1186/s13059-026-04302-9
- PDF: Unavailable
- Local PDF: Not downloaded

Abstract Biological discovery from large-scale assays requires extensive preprocessing, during which raw outputs (e.g., images, sequences) are processed into structured forms amenable to analysis. In spatial transcriptomics, differential expression analysis depends on cell segmentation, gene expression quantification, and cell-type annotation, all prone to systematic errors. We introduce corrected spatial differential expression (CSDE), building on prediction-powered inference to leverage a small set of expert-validated cells to correct for preprocessing bias. Across three case studies, CSDE yields more reliable differential expression estimates than the prevalent approach neglecting preprocessing.

## 5. Euclidean Crowding-Driven Adaptive Euclidean-Hyperbolic Graph Learning

- Authors: Hao Chen, Jian Sun, Chuan Shi, Hongying Zhang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-27
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.3464732643034423
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.37373v1
- PDF: https://arxiv.org/pdf/2610.37373v1
- Local PDF: pdf/2026-10-29_05_Euclidean Crowding-Driven Adaptive Euclidean-Hyperbolic Graph Learning.pdf

Hyperbolic graph representation learning has emerged as a powerful paradigm for modeling hierarchical data. Unlike Euclidean space, which exhibits polynomial volume growth, hyperbolic space grows exponentially with radius, naturally accommodating tree-like structures without the geometric distortion known as Euclidean crowding. Despite strong empirical performance, the theoretical mechanisms underlying hyperbolic embeddings remain poorly understood. In this work, we provide a geometric quantifcation research for Euclidean crowding, a generalization-theoretic explanation for the superiority of hyperbolic space on hierarchical data, and further develop an adaptive Euclidean-hyperbolic fusion learning framework toward bridging this gap. Specifically, we \textbf{first} establish a geometric quantification of Euclidean crowding by analyzing layer-wise minimum separation in node embeddings, proving that fixed-dimensional Euclidean embeddings of tree-like graphs inevitably exhibit layer-wise crowding that leads to weaker margin-based generalization bounds. \textbf{Second}, we provide a generalization-bound for the superiority of hyperbolic geometry on hierarchical data. \textbf{Third}, we propose EH-Fusion, a geometry-adaptive framework that lifts Euclidean GNN representations into hyperbolic space via exponential mapping and adaptively fuses both geometries based on node-level neighborhood expansion patterns. Extensive experiments validate our theoretical insights and demonstrate the effectiveness of EH-Fusion on benchmark datasets.

## 6. SpectRAG: Weighted Chunk Graphs for Token-Budgeted Context Selection in Multi-Hop Retrieval-Augmented Generation

- Authors: Zafer Sahinoglu, Abdulazeez Mohammed, Buse Yaren Kazangirler, Cahit Berkay Kazangirler
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-27
- DOI: Unavailable
- Categories: cs.AI, cs.CL, cs.IR
- Relevance: 3.326675490286462
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.36991v1
- PDF: https://arxiv.org/pdf/2610.36991v1
- Local PDF: pdf/2026-10-29_06_SpectRAG_ Weighted Chunk Graphs for Token-Budgeted Context Selection in Multi-Hop Retrieval-Augmented Generation.pdf

Retrieval-augmented generation (RAG) systems ground large language models (LLMs) by retrieving external evidence and conditioning generation on the retrieved context. Although dense retrieval is effective for local semantic matching, independently ranked retrieval can return redundant passages, miss cross-chunk dependencies, and provide incomplete evidence for multi-hop reasoning. We propose SpectRAG, a spectral graph-augmented retrieval framework that combines hybrid candidate seeding, weighted chunk graph construction, graph-based expansion, spectral relevance propagation, and token-budgeted context selection. Document chunks are represented by dense semantic embeddings and graph-spectral coordinates derived from a weighted chunk graph whose edges encode semantic similarity, document adjacency, section hierarchy, shared entities, citation links, and similarity between LLM-generated utility questions. At query time, SpectRAG builds a high-recall seed set using exact inner-product search and hybrid relevance signals, expands it over the chunk graph, re-scores candidates using graph proximity and spectral information, and assembles the final context under a fixed token budget. The goal is not merely to retrieve individually similar chunks, but to construct a context that is relevant, diverse, structurally connected, and sufficient for grounded reasoning. Experiments on MultiHopRAG, UltraDomain, and long-document question-answering settings show that SpectRAG improves broad evidence recovery and achieves competitive generation quality against dense, hybrid, HyDE, LightRAG, and NaiveRAG baselines. The results further indicate that graph-spectral structure is particularly useful for inference-oriented and cross-document retrieval, while highlighting trade-offs in early precision, computational cost, and domain-dependent performance.

## 7. GAS-PFN: Graph-Aware Spatiotemporal Prior-Data Fitted Networks for Zero-Shot Traffic Forecasting

- Authors: Joseph Natter, Long Vu, Yifan Zhang, Bobin Deng, Kun Suo, Rui Wu
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-27
- DOI: Unavailable
- Categories: cs.LG, cs.AI, cs.NE
- Relevance: 3.271657310173911
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.37598v1
- PDF: https://arxiv.org/pdf/2610.37598v1
- Local PDF: pdf/2026-10-29_07_GAS-PFN_ Graph-Aware Spatiotemporal Prior-Data Fitted Networks for Zero-Shot Traffic Forecasting.pdf

Traffic forecasting requires modeling complex temporal dynamics and the spatial dependencies imposed by road topology. Supervised graph-based models achieve strong performance, but are often trained for a particular dataset and sensor graph, making deployment to new or evolving networks costly. Prior-Data Fitted Networks (PFNs) offer a zero-shot alternative by learning in-context inference from synthetic task priors, which provide an explicit mechanism for encoding domain-specific assumptions. Existing forecasting PFNs, however, do not explicitly represent the graph-structured dependencies governing traffic dynamics. To combine graph-aware traffic modeling with zero-shot adaptation, we introduce the Graph-Aware Spatiotemporal Prior-Data Fitted Network (GAS-PFN). GAS-PFN incorporates sampled road topology into its synthetic task prior through random-walk diffusion, teaching the model to learn graph-coupled dynamics during pretraining. Its co-designed inference architecture uses two mask-conditioned passes through a shared Transformer backbone to separately model sensor-specific temporal dynamics and spatiotemporal interactions among neighboring sensors before integrating their representations for prediction. This design enables GAS-PFN to use target-network structure and context without parameter updates. Across six benchmarks at the 90-minute horizon, GAS-PFN reduces MSE by 34.0% on average relative to TimePFN, its closest PFN-based predecessor. It also reduces MSE by 27.7% on average relative to four recent industry-developed general-purpose zero-shot forecasters. In this comparison, all models receive 90 minutes of contiguous recent history, and any additional context is drawn from each dataset's chronological training split. These results indicate that aligning PFN priors and inference architectures with graph structure improves in-context learning for zero-shot traffic forecasting.

## 8. Attention as Lattice Gauge Theory: Relations Interact Only Through Wilson Loops

- Authors: Aakash Sarkar, Ananya Mukherjee, Motoshige Sato
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-27
- DOI: Unavailable
- Categories: cs.LG, cs.AI, physics.comp-ph
- Relevance: 3.1496494970396456
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.37656v1
- PDF: https://arxiv.org/pdf/2610.37656v1
- Local PDF: pdf/2026-10-29_08_Attention as Lattice Gauge Theory_ Relations Interact Only Through Wilson Loops.pdf

Relations compose through the entity they share - Alice is Bob's mother and Bob is Carol's father, so Alice is Carol's grandmother - and the order matters, since a father's mother is not a mother's father; verifying a composed relation means closing the loop. We show that if each entity's coordinate frame may be rotated independently (per-entity frame freedom), three things follow. In the pure-gauge sector, relations that share no cycle cannot interact at all. The only gauge-invariant score of a triangle is a class function of its holonomy $H = T_{ij} T_{jk} T_{ki}$ - a Wilson loop. And the only equivariant update of an edge is $U = Ψ(H)\, T_{ij}$ with $Ψ$ conjugation-equivariant. Edge attention by Wilson loops is therefore not one design among many but the unique form the symmetry permits. Three communities hold pieces of this form: the commuting-operator embeddings of knowledge graphs are its abelian (commuting) sector; AlphaFold's triangle update and the Edge Transformer have its shape - an edge updated through the third vertex - without its constraints; and lattice QCD builds it equivariantly on lattices. We instantiate the equivariant sub-family on general relational graphs as holonomy attention. With no training and composition alone, it infers unobserved $S_4$ relations on sparse graphs at 0.88 with a fifth of the edges corrupted, at or slightly below specialist synchronization algorithms, where every commutative architecture is capped at 0.083; its holonomy score flags corrupted triangles at AUC 0.99 where commuting scores are capped at 0.76 by a second selection rule, and it separates clusters without labels.

## 9. CaLLM: Continual Adaptation of LLMs via Non-Parametric Adapter Routing

- Authors: Bilge Celik, Anna Vettoruzzo, Joaquin Vanschoren
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-27
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.1416251947063274
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.36994v1
- PDF: https://arxiv.org/pdf/2610.36994v1
- Local PDF: pdf/2026-10-29_09_CaLLM_ Continual Adaptation of LLMs via Non-Parametric Adapter Routing.pdf

Continual adaptation of large language models (LLMs) to evolving task distributions while mitigating catastrophic forgetting remains an open problem. Existing strategies often struggle to scale or lack a robust mechanism for zero-shot task-to-expert assignment. We introduce CaLLM, a framework that resolves these tensions by combining metric-based meta-learning with modular parameter isolation via lightweight adapters. First, CaLLM projects each input batch into a task-agnostic embedding space to find its nearest prototype. It then routes the batch to the specific adapter specialized for that data distribution. This formulation provides (i)~controllable cross-task interference by design, (ii)~constant computational complexity regardless of task count, (iii)~seamless integration of novel distributions through prototype expansion, and (iv)~regime agnosticism as the local routing decision enables a unified approach to both online and offline settings. Our experiments demonstrate that this routing mechanism discovers semantically coherent task groupings while facilitating constructive interference between similar tasks, and keeping overhead at a minimum. Across diverse and fine-grained continual learning benchmarks, CaLLM consistently outperforms traditional isolation and replay methods, establishing prototype-based modular routing as a principled and scalable approach to lifelong adaptation of LLMs.

## 10. When Connectivity Misleads: Guiding Agentic Search with Contrastive Evidence Paths

- Authors: Junchen Li, Liang Xu, Rongzheng Wang, Qizhi Chen, Junhao Wen, Shuang Liang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-26
- DOI: Unavailable
- Categories: cs.IR, cs.AI
- Relevance: 3.127904909245258
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.36134v1
- PDF: https://arxiv.org/pdf/2610.36134v1
- Local PDF: pdf/2026-10-29_10_When Connectivity Misleads_ Guiding Agentic Search with Contrastive Evidence Paths.pdf

Search agents can use cross-document graphs to discover sources through multi-hop connections and choose subsequent actions based on candidate rankings and relationships within a limited observation window. However, documents may rank highly because their numerous connections make them easier to reach, without necessarily providing more valuable evidence. Graph diffusion methods such as Personalized PageRank (PPR) aggregate propagation contributions from multiple sources, allowing highly connected distractor nodes to crowd the observation window. Flat node scores also obscure cross-document evidence trails, limiting continued exploration. We propose Contrastive Evidence Paths (CEP), which scores candidates by their strongest individual paths on a query-conditioned document graph and calibrates these scores against the same graph's background visitation distribution to mitigate structural bias. CEP ranks candidates by the calibrated scores and retains the corresponding source paths. Building on CEP, we develop Structured Corpus Interaction (SCI), which organizes candidates and their connecting paths into a structured Map, enabling agents to verify source documents and pursue missing information through expansion from anchor documents. Experiments on BrowseComp-Plus and TREC-COVID show that SCI achieves state-of-the-art answer accuracy and nDCG@10 with the lowest generation cost. Compared with the strongest baselines by task performance, maximum reductions in tool calls and total generation costs exceed 50% and 40%, respectively. Further analysis confirms that SCI with CEP suppresses ranking inflation induced by structural connections and improves gold recall and exploration efficiency.

## 11. GraphRAGProv: GraphRAG Meets How-Provenance

- Authors: Wadie El Amrani, Luis Galárraga
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-27
- DOI: Unavailable
- Categories: cs.AI, cs.DB
- Relevance: 3.091326766911904
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.37237v1
- PDF: https://arxiv.org/pdf/2610.37237v1
- Local PDF: pdf/2026-10-29_11_GraphRAGProv_ GraphRAG Meets How-Provenance.pdf

GraphRAG systems often use knowledge graphs to retrieve relevant context for an LLM that produces the final answer. That makes answers more inscrutable and therefore less appealing for domains where transparency is paramount. We present GraphRAGProv, an architecture that executes SPARQL queries over source-grounded RDF graphs to compute answers and their how-provenance polynomials. These polynomials record which statement occurrences were used and how they were combined. Because each occurrence is linked to its source text, users can follow these links to check whether the extracted statements reflect the text and whether the query combines them to answer the question. Querying thereby becomes a way to inspect and evaluate the text-to-graph transformation. Our interactive demo examines 400 cases from two multi-hop QA benchmarks, revealing extraction and query errors even when the final answer is correct.

## 12. LLM Hallucination Detection via Low-rank Multilinear Decomposition

- Authors: Devansh Sharma, Faizul Rakib Sayem, Shahana Ibrahim
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-26
- DOI: Unavailable
- Categories: cs.CL, cs.LG
- Relevance: 3.074307384067687
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.36191v1
- PDF: https://arxiv.org/pdf/2610.36191v1
- Local PDF: pdf/2026-10-29_12_LLM Hallucination Detection via Low-rank Multilinear Decomposition.pdf

Large language models (LLMs) frequently generate fluent yet factually incorrect responses, raising concerns about their reliability. Recent hallucination detectors increasingly exploit internal representations, but extracting informative signals from high-dimensional hidden states remains challenging. Existing approaches often rely on selected activations or pooling-based compression, potentially overlooking discriminative information distributed across Transformer layers, feature modes, and tokens. We propose LOTUS (Low-rank Order-statistic TUcker-based Subspace learning), a multilinear low-rank decomposition framework for hallucination detection that extracts compact representations from LLM hidden states while reducing dependence on labeled data. Our approach first summarizes variable-length token representations using complementary statistical descriptors that capture peak activations, activation distributions, and cross-layer changes. We then leverage low-rank multilinear decomposition to extract compact representations that capture the underlying structure of LLM hidden states, which are subsequently used to train a lightweight hallucination classifier. Experiments across multiple LLMs and question-answering benchmarks demonstrate improved hallucination detection performance over recent state-of-the-art baselines.

## 13. How Many and How Much? Contrastive Learning with Negative Samples for Knowledge Graph Embedding

- Authors: Sooho Moon, Yunyong Ko
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-27
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.0150914278823264
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.37389v1
- PDF: https://arxiv.org/pdf/2610.37389v1
- Local PDF: pdf/2026-10-29_13_How Many and How Much_ Contrastive Learning with Negative Samples for Knowledge Graph Embedding.pdf

Knowledge graph embedding (KGE), a fundamental technique for knowledge-centric Web and KG-augmented AI applications, is commonly trained through contrastive learning with negative samples to learn discriminative representations. Despite its empirical success, two crucial questions regarding negative samples remain underexplored: (Q1) how many negative samples should be used for each positive sample and (Q2) how much should each negative sample contribute to learning? To answer these questions, we propose RADAR, a novel contrastive learning framework for KGE models with two effective strategies, respectively: (1) Risk-aware negative budget allocation quantifies false-negative sampling risk by modeling an open-world KG as a stochastic partial observation of its closed-world counterpart and adaptively assigns a negative budget to each positive sample based on its risk; (2) Distribution-calibrated negative weighting assigns negative weights by calibrating the weighting strength for each positive based on two complementary characteristics of the negative-score distribution: dispersion and concentration. Extensive experiments on 3 real-world KGs with 4 KGE models reveal that RADAR achieves the best KGE performance on average across all model--KG combinations and reduces sampled false negatives by over 90% compared with conventional fixed-budget methods.

## 14. Provenance Signatures for Low Rank Adaptations of Image Diffusion Models

- Authors: Tobias Cheung, Mohan Dantam, Marc Juarez, Rik Sarkar
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-27
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.0007346625819697
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.36933v1
- PDF: https://arxiv.org/pdf/2610.36933v1
- Local PDF: pdf/2026-10-29_14_Provenance Signatures for Low Rank Adaptations of Image Diffusion Models.pdf

Diffusion models have revolutionized the generation of realistic artificial images. Efficient techniques such as Low Rank Adaptation (LoRA) can modify these models for particular use cases, making them more diverse and widely usable. At the same time, open base models may be adapted to deliver biased, harmful or illegal images in an online service. In this paper, we develop a protocol to detect when a service may be using an adaptation of an otherwise standard model. We describe the precise setup and threat model for this provenance question and define two different problems arising due the presence of multiple model families and multiple adaptations. In contrast to previous works that have considered model identification within lists of known candidate models, we consider the realistic open world scenario where the set of possible adaptations and alternative models are unknown. Using a hypothesis testing approach, our protocols can distinguish between the base model, a LoRA adaptation and other completely different families of models. For this test, we develop a black box signature of the models based only on intrinsic dimension of sets of images generated by the models.

## 15. Robust LLM Data Selection via Content-Invariant Gradient Attribution

- Authors: Jia Gu, Liang Pang, Huawei Shen
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-27
- DOI: Unavailable
- Categories: cs.LG, cs.AI
- Relevance: 2.9742277731984057
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.36755v1
- PDF: https://arxiv.org/pdf/2610.36755v1
- Local PDF: pdf/2026-10-29_15_Robust LLM Data Selection via Content-Invariant Gradient Attribution.pdf

Gradient-based data attribution has become an important tool for high-quality data selection in the instruction fine-tuning of large language models (LLMs), as it estimates the contribution of training examples through their influence on model optimization. However, we find that existing global gradient attribution methods suffer from surface-form bias: minor changes to semantically irrelevant details, such as wording or formatting, can produce highly inconsistent attribution scores even when the underlying content remains unchanged. To address this issue, we propose Content-Invariant Gradient Attribution (CIGA), a robust framework for instruction data selection. CIGA first identifies layers whose gradients are both influential for attribution and stable under semantics-preserving surface-form perturbations, thereby reducing formatting noise in gradient features. It then dynamically fuses these attribution signals with semantic representations of the input, combining optimization-level influence with content-level information. Extensive experiments across multiple benchmarks show that CIGA produces more stable rankings under surface-form perturbations while preserving downstream capabilities and improving average performance. CIGA also reduces attribution cost, offering a robust and efficient approach to data selection for LLM instruction tuning.

## 16. A note on data-efficient finetuning of vision foundation models

- Authors: Niclas Hergenröther, Antonio Orvieto
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-27
- DOI: Unavailable
- Categories: cs.CV, cs.LG
- Relevance: 2.93139343997015
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.37510v1
- PDF: https://arxiv.org/pdf/2610.37510v1
- Local PDF: pdf/2026-10-29_16_A note on data-efficient finetuning of vision foundation models.pdf

Adapting foundation models to a new task within or beyond the training domain is the de facto standard for building specialized machine learning models. Recently, Visual Prompting (VP) has emerged as a promising technique for efficient knowledge transfer. As new foundation model families~(like Mamba) get introduced and VP pipelines such as AutoVP reach greater maturity, we find a growing need for a systematic evaluation of current approaches. In this work, we assess the performance of the latest models, comparing them to earlier architectures and alternative fine-tuning methods, to better understand the progress, challenges and opportunities in the field of efficient fine-tuning under resource limitations. Towards this goal, this paper provides a concise empirical overview of the interactions among foundation model families (Attention-, Convolution-, and Mamba-based) and transfer paradigms: VP, Linear Probing (LP), Full Fine-tuning (FFT) and Low Rank Adaptation (LoRA). Our work builds up on previous findings by broadening the selection of evaluated models and techniques while tuning hyperparameters. In the interest of delivering practical guidelines for the user, we also explore application of prevalent regularization techniques to boost performance in the context of VP.

## 17. scBOA: Bayesian optimization of single-cell analysis pipelines for robust annotation and discovery

- Authors: Qiang Su, Yi Long, Fuyu Duan, Qizhou Lian
- Source: openalex
- Venue type: journal
- Journal: Nature Communications
- Publication status: published
- Publication date: 2026-10-27
- DOI: https://doi.org/10.1038/s41467-026-78718-z
- Categories: Single-cell and spatial transcriptomics, Gene Regulatory Network Analysis, Cell Image Analysis Techniques
- Relevance: 2.9158006823706235
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://doi.org/10.1038/s41467-026-78718-z
- PDF: Unavailable
- Local PDF: Not downloaded

Accurate cell-type annotation in single-cell RNA sequencing is sensitive to upstream parameters often selected heuristically. We introduce scBOA, a two-stage framework that uses Bayesian optimization to select workflow parameters against a prespecified objective and reruns the selected configuration for reference-assisted analysis. Its configurable objectives combine annotation purity, marker concordance and transcriptomic cohesion, enabling fine-grained or conservative solutions. Optional extensions support low-confidence-cell refinement and multi-sample integration. Across simulations and fluorescence-activated cell sorting datasets of human peripheral blood mononuclear cells, pancreas and adult heart, we compare Gaussian-process scBOA with 14 alternative parameter-selection and clustering strategies. We show that performance depends on the objective, workflow, reference hierarchy and vocabulary, consensus-label construction and partition granularity. We find that scBOA is not uniformly superior, but shows strong aggregate performance when annotation targets align with biological structure. We apply a mouse Huntington’s disease dataset as an exploratory stress test of integration and reference mapping. Overall, we demonstrate that scBOA provides reproducible, objective-driven workflow optimization for reference-assisted single-cell analysis. Here, the authors introduce scBOA, a Bayesian optimization tool that helps researchers choose single-cell analysis settings for cell-type annotation. They perform benchmarking to show that performance depends on the dataset, reference and objective.

## 18. CoS-VQ: Coordinated Shared-Scale Vector Quantization for Large Language Models

- Authors: Zukang Xu, Zhixiong Zhao, Xing Hu, Zhe Jiang, Xin Si, Dawei Yang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-27
- DOI: Unavailable
- Categories: cs.LG, cs.AI
- Relevance: 2.912293403601223
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.37336v1
- PDF: https://arxiv.org/pdf/2610.37336v1
- Local PDF: pdf/2026-10-29_18_CoS-VQ_ Coordinated Shared-Scale Vector Quantization for Large Language Models.pdf

Large language models (LLMs) require substantial memory, motivating low-bit weight quantization for efficient deployment. Existing vector quantization (VQ) methods often improve accuracy by increasing the effective coding dimension, which can complicate independent lookup and local codeword updates. We propose CoS-VQ (Coordinated Shared-Scale Vector Quantization), which preserves low-dimensional codewords while jointly optimizing hard indices and their shared scale across positions. The key challenge is scale-induced coupling: the optimal scale depends on the entire codeword combination and, in turn, changes candidate rankings across positions, so pointwise updates can stall even after scale re-optimization. CoS-VQ collects candidates at multiple probe scales and constructs a tangent separable upper bound for the residual-aware quadratic objective. By reducing candidate comparisons to lower envelopes of lines over positive scales, it identifies finitely many representative intervals for joint index--scale updates without exhaustively enumerating codeword combinations. On Qwen3.8-27B, CoS-VQ outperforms QTIP and LLVQ on the evaluated language modeling, coding, and reasoning benchmarks. Ablations from the same initialization further show larger gains from joint updates than from scale-only refinement, highlighting joint selection as an alternative to increasing codeword dimensionality. The code is available at https://github.com/xzktx003/Cos_VQ.

## 19. From Structural Feedback to Prompt Policies: Learning Faithful Text-to-Image Prompt Editors

- Authors: Wentao Ye, Yali Ye, Zhiqing Xiao, Ru Peng, Xinpeng Ti, Liyao Li, Zhanming Shen, Peng Lu, Jie Zhang, Haobo Wang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-26
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 2.9022971935271413
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.36146v1
- PDF: https://arxiv.org/pdf/2610.36146v1
- Local PDF: pdf/2026-10-29_19_From Structural Feedback to Prompt Policies_ Learning Faithful Text-to-Image Prompt Editors.pdf

Prompt optimization should improve the image a user receives without changing the scene the user requested. Yet stylistic rewriting can weaken object attributes and relations even when global text--image similarity remains high. We propose StruPO, a structure-aware prompt editor that uses a calibrated scene graph as a shared representation for policy conditioning and image-grounded supervision. The graph exposes what should be preserved, while deletion, reordering, and insertion provide a token-aligned way to modify the prompt. This turns structural feedback from an external critique into a training signal for a reusable editing policy. Learning from that signal requires handling both uncertain grounding and stochastic image generation. StruPO retains grounding confidence through smooth reward shaping and averages multiple images for each edit before computing group-relative advantages. Experiments span three disjoint 2K-prompt test sets and four frozen generation backbones, with comparisons to learned prompt optimizers, iterative structural feedback, diffusion-model fine-tuning, and inference-time attention control. StruPO improves the faithfulness--aesthetics trade-off, with consistent gains in relational fidelity. Independent automatic evaluators and a 15-annotator study provide complementary evidence, and human preference margins increase with relation complexity. Controlled ablations connect these gains to graph conditioning, local editing, and image-grounded learning. The resulting policy produces reusable optimized text in one pass after graph calibration, without an iterative critique--rewrite loop.

## 20. PerceptRL: Making Visual Perception Rewardable in MLLMs from Answers to Interactions

- Authors: Tongkun Guan, Zhibo Yang, Mingkun Yang, Haocheng Wang, Wei Shen, Xiaokang Yang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-27
- DOI: Unavailable
- Categories: cs.CV, cs.AI
- Relevance: 2.899107513340282
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.37471v1
- PDF: https://arxiv.org/pdf/2610.37471v1
- Local PDF: pdf/2026-10-29_20_PerceptRL_ Making Visual Perception Rewardable in MLLMs from Answers to Interactions.pdf

Fine-grained visual perception remains a bottleneck during post-training of multimodal large language models (MLLMs), as perceptual errors can constrain gains from reasoning-focused optimization. Although image-caption pre-training improves perception, its influence can weaken as subsequent stages change data mixtures and objectives. Continuing caption supervision during post-training is challenging because subjective, information-dense descriptions complicate verifiable reward design. We present PerceptRL, which strengthens perception at two complementary levels. Perception RL uses a multi-agent pipeline to extract verified errors from dense image captions and convert the corresponding visual facts into QA pairs with fixed answer labels and rule-based rewards. Chain QA links correlated errors, while multiple-choice QA combines unrelated errors. A specialized route targets high-error domains with tailored verification, and a domain-agnostic general route covers errors beyond these domains. Perception Agentic RL addresses fine-grained and dense cases unresolved by single-turn Perception RL through multi-turn inspection with visual tools. We observe coordinate drift even in models trained to use tools, where incorrect crops or annotations distort evidence and propagate errors. Coordinate Injection corrects spatial operations in cold-start trajectories, while a grounding-aware process reward supervises intermediate spatial fidelity alongside final-answer correctness. Training proceeds through shared cold-start SFT, single-turn Perception RL, and multi-turn Perception Agentic RL. Across seven benchmarks under a shared tool-use protocol, PerceptRL achieves 71.6% average accuracy, surpassing the base model with the same tools and the strongest evaluated frontier VLM by 15.7 and 5.2 percentage points, respectively.

## 21. VideoLVR: Latent Visual Reasoning over Grounded Video Evidence

- Authors: Shilong Li, Xingyuan Bu, Hao Shi, Yun Xing, Weixin Feng, Qiangpeng Yang, Shilei Wen
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-27
- DOI: Unavailable
- Categories: cs.CV, cs.AI
- Relevance: 2.8916037065791595
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.37613v1
- PDF: https://arxiv.org/pdf/2610.37613v1
- Local PDF: pdf/2026-10-29_21_VideoLVR_ Latent Visual Reasoning over Grounded Video Evidence.pdf

Chain-of-thought reasoning has substantially advanced video understanding in multimodal large language models (MLLMs). However, language-based reasoning traces do not provide a reliable mechanism for models to revisit relevant visual evidence, leading to visual forgetting and impairing their ability to reason over video content. Existing approaches maintain visual grounding during reasoning in two main ways: they either refer to evidence using textual coordinates, which specify symbolic locations rather than the visual content itself, or reinsert cropped regions or frames into the multimodal context, preserving visual details at the cost of substantial context expansion. To address these limitations, we introduce VideoLVR, which constructs latent visual evidence from local regions at relevant video moments, thereby providing visual support for intermediate reasoning steps. To supervise latent visual evidence generation, we introduce a visual token prediction objective that formulates visual token reconstruction as prediction over a vocabulary derived from the input video, thereby unifying visual evidence reconstruction and text generation within the same token prediction framework. This shared prediction framework enables MLLMs to reason over interleaved text tokens and latent visual states while integrating evidence from different moments. We further extend VideoLVR to reinforcement learning by treating sampled visual tokens as actions alongside text tokens and jointly optimizing the policy using final-answer rewards. By efficiently revisiting task-relevant visual information during reasoning, VideoLVR improves video understanding without substantially expanding the multimodal context. Experiments on multiple video benchmarks demonstrate its effectiveness, especially on tasks requiring fine-grained visual evidence.

## 22. An Incremental Knowledge-Graph Learner Digital Twin for Evidence-Grounded Early Warning

- Authors: Ngoc Luyen Le, Marie-Hélène Abel, Bertrand Laforge
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-27
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 2.8862067442871977
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.36820v1
- PDF: https://arxiv.org/pdf/2610.36820v1
- Local PDF: pdf/2026-10-29_22_An Incremental Knowledge-Graph Learner Digital Twin for Evidence-Grounded Early Warning.pdf

Early-warning models in learning analytics can identify learners at risk of failure or withdrawal, but the resulting alerts are often only weakly connected to inspectable learning evidence. A risk score may indicate that intervention is needed without showing which traces, assessment events, or temporal patterns justify the alert. This paper introduces an incremental Learner Digital Twin for evidence-grounded early warning, implemented as a lightweight knowledge graph. The twin is updated at temporal checkpoints by replaying learning traces and assessment records, and it serves both as a feature-extraction substrate and as an explanation-grounding substrate. Predictive features are derived through graph-mediated queries, while features, attributions, alerts, evidence items, and raw records are represented as queryable graph entities. The framework is instantiated and evaluated on a public learning-analytics benchmark under a temporal protocol. The results show that graph-mediated feature extraction preserves the predictive behavior of equivalent raw-table features across model families and checkpoints. Generated alerts are materialized as evidence chains linking risk decisions to feature attributions, evidence items, and raw platform records. The study shows that early-warning prediction can be routed through a semantic and provenance-aware representation while preserving predictive performance and adding traceability, verifiability, and evidence-grounded explanation.

## 23. Comparative analysis of end-to-end learning and foundation models for clinical-grade prostate pathology

- Authors: Nita Mulliqi, Anders Blilie, Xiaoyi Ji, Kelvin Szolnoky, Henrik Olsson, Sol Erika Boman, Matteo Titus, Geraldine Martinez Gonzalez, Julia Anna Mielcarz, Masi Valkonen, Einar G. Gudlaugsson, Svein Reidar Kjosavik, J. Asenjo, Marcello Gambacorta, Paolo Libretti, Marcin Braun, Radzisław Kordek, Roman Łowicki, Kristina Hotakainen, Päivi O. Väre, Bodil Ginnerup Pedersen, Karina Dalsgaard Sørensen, Benedicte Parm Ulhøi, Pekka Ruusuvuori, Brett Delahunt, Hemamali Samaratunga, Toyonori Tsuzuki, Emiel A. M. Janssen, Lars Egevad, Martin Eklund, Kimmo Kartasalo
- Source: openalex
- Venue type: journal
- Journal: Nature Communications
- Publication status: published
- Publication date: 2026-10-26
- DOI: https://doi.org/10.1038/s41467-026-78996-7
- Categories: AI in cancer detection, Artificial Intelligence in Healthcare and Education, Radiomics and Machine Learning in Medical Imaging
- Relevance: 2.8717696548038907
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://doi.org/10.1038/s41467-026-78996-7
- PDF: https://www.nature.com/articles/s41467-026-78996-7_reference.pdf
- Local PDF: pdf/2026-10-29_23_Comparative analysis of end-to-end learning and foundation models for clinical-grade prostate pathology.pdf

Abstract Foundation models (FMs) using self-supervised pre-training are widely advocated as a universal solution for pathology, yet their advantages over task-specific (TS) models remain unclear. Here we show, using over 100,000 prostate biopsies from 6268 patients across 15 sites, that while FMs demonstrate utility in data-scarce scenarios, their performance converges with—and is in some cases surpassed by—TS models with sufficient labeled training data. Concordance with pathologists’ grading reaches quadratic Cohen’s kappas of 0.91 (95% CI 0.90-0.92; all models) on internal and 0.87 (0.86-0.88; TS), 0.86 (0.84-0.87; UNI FM) and 0.85 (0.84-0.86; Virchow2 FM) on external cohorts at full training. Task-specific training markedly reduces misgrading, misdiagnosis of challenging morphologies, and technical variability. Notably, FMs consume up to 35 times more energy. We advocate for considering both FMs and end-to-end learning for robust, resource-efficient, and clinically applicable AI pathology.

## 24. HELICS: Biobank-scale Conditional Synthetic Genome Generation via Latent Flow Matching

- Authors: Ahmad Abdel-Azim, Xihong Lin
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-26
- DOI: Unavailable
- Categories: q-bio.GN, cs.LG
- Relevance: 2.8573768555362955
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.36361v1
- PDF: https://arxiv.org/pdf/2610.36361v1
- Local PDF: pdf/2026-10-29_24_HELICS_ Biobank-scale Conditional Synthetic Genome Generation via Latent Flow Matching.pdf

Individual-level genotype data underpin genetic discovery, disease-risk modeling, and therapeutic development, yet many critical settings remain data-limited, including underrepresented ancestries, rare or imbalanced disease cohorts, and restricted-access biobanks. Conditional synthetic genome generation would support privacy-aware benchmarking, simulation, and data augmentation, but requires learning an ultra-high-dimensional discrete distribution over hundreds of thousands to tens of millions of correlated single-nucleotide polymorphisms (SNPs), or sites of DNA variation. We introduce HELICS: High-fidelity gEneration via Latent Interpolant Conditional Synthesis, a phasing-free latent flow matching framework for genome-wide SNP-level generation from biobank-scale genotype data. HELICS tokenizes chromosomes with convolutional autoencoders, reducing >600K SNPs to 4,096 continuous latent tokens, and trains a transformer parameterized conditional flow matching model over the concatenated multi-chromosome latent representation. Trained on over 417K genomes in the UK Biobank, HELICS generates genome-wide common-variant synthetic cohorts without haplotype phasing and achieves stronger fidelity to real genotypes than existing haplotype-based simulators, including high allele-frequency agreement in external evaluation and superior preservation of local and long-range SNP correlation structure. Conditioning on ancestry and genetic liability summaries enables targeted generation across genetic risk profiles; in perturbation analyses, by increasing the conditioned disease trait liability, HELICS induces SNP-level dosage changes in generated genomes that are highly correlated with published association weights. HELICS provides a scalable generative modeling framework for SNP-level genome data and a path toward conditional synthetic cohorts for data-limited genetic studies.

## 25. TDLM: Adaptive Temporal Integration for Diffusion Language Models

- Authors: Bohang Sun, Max Zhu, Francesco Caso, Christopher Irwin, Jialin Yu, Pietro Liò
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-27
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 2.8572904643889774
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.36940v1
- PDF: https://arxiv.org/pdf/2610.36940v1
- Local PDF: pdf/2026-10-29_25_TDLM_ Adaptive Temporal Integration for Diffusion Language Models.pdf

Masked diffusion language models repeatedly compute representations for unresolved tokens, but conventional denoisers do not explicitly retain these representations for reuse across steps. We introduce Temporal Self-Conditioning Diffusion Language Model (TDLM), which lets each unresolved position attend to its own history of hidden representations within a frozen denoiser. This gives later predictions access to computation already performed. Training uses self-generated trajectories and a simple cross-entropy objective for tokens revealed between consecutively sampled decoding steps, while causal temporal attention permits parallel evaluation during training. On LLaDA, the temporal modules add only approximately 0.84% trainable parameters. Across LLaDA and Dream, the main comparison shows up to 7.15$\times$ faster generation than the corresponding original diffusion language model, with competitive answer quality on the evaluated tasks. These results motivate temporal memory as a practical way to make more effective use of repeated denoising computation.

## 26. Look Only When Needed: Certificate-Guided Visual Routing for Efficient Diffusion VLMs

- Authors: Donghyeon Cho, Joowon Kim, Seungho Shin, Eunho Yang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-27
- DOI: Unavailable
- Categories: cs.CV, cs.AI, cs.LG
- Relevance: 2.854195993373143
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.36671v1
- PDF: https://arxiv.org/pdf/2610.36671v1
- Local PDF: pdf/2026-10-29_26_Look Only When Needed_ Certificate-Guided Visual Routing for Efficient Diffusion VLMs.pdf

Diffusion vision-language models (DVLMs) process their entire input at every denoising step. Since visual tokens make up 89-97% of this input on the benchmarks we study, most of the decoding computation is spent repeatedly processing the same image. Visual token pruning methods partially relieve this burden by removing part of the visual tokens, but they lose the removed information and still process the remaining image at every step. To measure how often the image is actually needed, we compare LLaDA-V's predictions with and without the image at every decoding step and find that removing the image changes a token being unmasked at only 22.8% of steps on average and at as few as 7.9%. We therefore propose LOWN, a decoding method that decides at every step whether to process the image and how many tokens to unmask. LOWN predicts the masked tokens without the image and processes the image only when this prediction disagrees with the last image-conditioned prediction. Agreement certifies the earlier prediction for reuse, and the number of certified tokens sets how many are unmasked in that step. We further observe that the need for the image differs across benchmarks, so LOWN's adaptive decision is needed rather than a fixed schedule. Without training or a tuned threshold, LOWN retains 99.6% of LLaDA-V's score on ten benchmarks at 35.3% of the decoding FLOPs on average. LOWN also generalizes across LLaDA-based DVLMs, composes orthogonally with visual token pruning, and runs under key-value caching for further efficiency gains. Code and project page are available at https://hyeon9698.github.io/LOWN/

## 27. Recall or Relearn? A Mixture of In-Context Experts for Recurring Concept Drift

- Authors: Zhangkai Wu, Xu Zhang, Zhihong Cui, Yiqi Wang, Yi Zhang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-27
- DOI: Unavailable
- Categories: cs.LG, cs.IR
- Relevance: 2.8460003795664752
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.36585v1
- PDF: https://arxiv.org/pdf/2610.36585v1
- Local PDF: pdf/2026-10-29_27_Recall or Relearn_ A Mixture of In-Context Experts for Recurring Concept Drift.pdf

Tabular foundation models (TFMs) are being applied to Web data streams such as network intrusion detection, where they adapt by updating the labelled rows of their context without retraining. When a past concept returns after leaving the context, a TFM faces a recall-or-relearn decision between restoring stored rows of the concept and relearning it from new labels. We propose MICE (Mixture of In-Context Experts), a training-free learner that cuts the stream into segments at detected changes. It merges a closed segment into a stored context when the TFM's estimated additional error on the segment is within a tolerance, under a capacity limit on stored contexts. A fast level weights the stored contexts and first-in-first-out (FIFO) windows by the log-loss of their predictions on the last labelled batch. We show that, with pure stored contexts and a margin condition, this fast level gains over relearning, in expected accuracy, the normalised positive area between the stored context's accuracy and the TFM's learning curve, up to a first-batch term. A slow level mixes the fast level's prediction with that of the FIFO window of the last labelled rows and bounds the discounted half-Brier regret of MICE against this window at every time. Learning curves measured beforehand predict the ordering of the observed recall gains. MICE outperforms reset, which empties the context at detected drifts, on grid streams with random boundary phases. Merging keeps fewer experts than pools that store every segment, and with fixed segmentation a time-matched snapshot pool matches MICE on the shifted grid. On real streams, MICE has the highest mean accuracy of all policies we compare.

## 28. Clearing the FoG: Training KG Agents to Retrieve the Evidence Behind Their Answers

- Authors: Zongyuan Sun, Shuai Zhao, Yingjun Du, Ke Shu, Ziyue Zhu, Haoran Luo
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-27
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 2.811812974176995
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.37405v1
- PDF: https://arxiv.org/pdf/2610.37405v1
- Local PDF: pdf/2026-10-29_28_Clearing the FoG_ Training KG Agents to Retrieve the Evidence Behind Their Answers.pdf

Large language models (LLMs) can answer many factual questions correctly, but a correct answer is not necessarily a supported one. For an LLM agent, a knowledge graph (KG) plays two roles: as a source of answers, it supplies facts that the model lacks; as a source of evidence, it supplies the supporting triples that make an answer traceable and auditable. However, existing KG agents treat the KG only as a source of answers: their training data carries answers but not evidence, and their training rewards check the answer but not the retrieved evidence, so agents often answer correctly without retrieving the supporting triples. We propose FoG, a framework that trains KG agents to retrieve the evidence behind their answers. FoG consists of evidence-grounded synthesis, a KG interaction agent, and an evidence-coverage process reward (ECPR): the synthesis recursively hides explicit entities behind verifiable sub-questions, so that every question carries its supporting triples by construction; the agent records the triples returned by the KG; and ECPR credits each supporting triple to the turn that first retrieves it. Experiments on three KGQA benchmarks demonstrate that FoG enables 3B--4B open-source agents to outperform substantially larger baselines in answer accuracy and evidence coverage, with zero-shot cross-KG transfer.

## 29. Systematic Morphometric Brain Autoencoding for Representation Learning in Neurodegenerative Diseases

- Authors: Nuria Balbás-Esteban, Albert Belenguer-Llorens, Elaheh Moradi, Jussi Tohka, Vanessa Gómez-Verdejo, Carlos Sevilla-Salcedo
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-27
- DOI: Unavailable
- Categories: cs.CV, cs.LG
- Relevance: 2.8106115008956793
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.37074v1
- PDF: https://arxiv.org/pdf/2610.37074v1
- Local PDF: pdf/2026-10-29_29_Systematic Morphometric Brain Autoencoding for Representation Learning in Neurodegenerative Diseases.pdf

Early identification of neurodegenerative disorders using structural T1-weighted MRI is essential for timely clinical intervention, yet supervised deep learning models often struggle to generalize due to limited annotations and scanner-induced distribution shift. Self-supervised learning offers a promising alternative; however, existing approaches are largely adapted from natural image paradigms, relying on contrastive objectives or generic masked reconstruction with voxel-wise losses, which may not fully capture the distributed morphometric patterns associated with neurodegeneration.
  We introduce SYMBA (SYstematic Morphometric Brain Autoencoding), a self-supervised pretraining framework specifically designed for structural brain MRI. SYMBA integrates anatomically constrained masking, a multi-scale structural similarity (MS-SSIM) reconstruction objective, and a progressive curriculum that transitions from local anatomical detail to global brain morphology. These components explicitly incorporate neuroanatomical structure into the self-supervised objective rather than relying on generic image priors.
  Pretrained on 6,953 T1-weighted MRI scans from nine heterogeneous cohorts, SYMBA is evaluated using frozen linear probing on two independent unseen datasets, enabling a strict assessment of out-of-distribution generalization. Across multiple clinical tasks, SYMBA consistently outperforms recent neuroimaging foundation models, achieving 0.930 AUROC for Alzheimer's disease classification, 0.772 for mild cognitive impairment conversion prediction, and strong performance in amyloid status prediction. In low-label regimes, SYMBA demonstrates high sample efficiency, reaching approximately 0.90 AUROC for AD/CN classification using only six labeled subjects.

## 30. Scaling Laws for Tool-Use Agents via Controllable Environment Synthesis

- Authors: Andrew Szot, Samira Abnar, Omar Attia, Abbas Kazerouni, Michael Kirchhof, Cheng-Yu Hsieh, Raviteja Vemulapalli, Alexander Toshev
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-27
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 2.8071819240138405
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.37648v1
- PDF: https://arxiv.org/pdf/2610.37648v1
- Local PDF: pdf/2026-10-29_30_Scaling Laws for Tool-Use Agents via Controllable Environment Synthesis.pdf

We explore how to build performant large language model (LLM) tool-use agents that complete complex, multi-step tasks. Specifically, we study how data composition in synthetically generated tool-use environments affects the training of such agents. To do so, we propose the SynthAPI pipeline, which explicitly controls the diversity of generated environments along the axes of tools, tasks, and the databases on which the tools operate. By systematically varying SynthAPI's generation controls in 458,752 tasks across 849 trained models of four different sizes, we derive a scaling law that predicts downstream tool-use agent generalization based on the scale and composition of the synthesized environments. These predictable relationships reveal several lessons for scaling tool-use agent data. As data budgets grow, scaling tool and database diversity becomes more effective than increasing the number of tasks, and increasing data complexity yields larger gains. Scaling according to these findings yields agents that outperform models trained on data from prior work in large-scale tool-use agent and synthetic environment generation across four evaluation benchmarks.
