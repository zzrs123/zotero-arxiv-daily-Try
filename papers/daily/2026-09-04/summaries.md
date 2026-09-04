# Paper Daily Reading - 2026-09-04

## 1. Subcellularly Resolved Single-Cell Embedding Learning with Transcriptomic data, Protein Structure and Localization Information

- Authors: Zhen Zhou, Jiachen Li, Yuan Liu, Xiaoyong Pan, Hong-Bin Shen
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-02
- DOI: Unavailable
- Categories: q-bio.GN, cs.AI
- Relevance: 3.8831837173548864
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.02344v1
- PDF: https://arxiv.org/pdf/2609.02344v1
- Local PDF: pdf/2026-09-04_01_Subcellularly Resolved Single-Cell Embedding Learning with Transcriptomic data, Protein Structure and Localization Infor.pdf

Existing cell embedding methods predominantly rely on transcriptomic or proteomic measurements and represent each cell as a holistic entity, thereby overlooking the subcellular localization of individual molecules. Moreover, they rarely incorporate protein structural information, despite its fundamental role in determining molecular interactions and functions. In this work, we propose a multimodal framework for learning subcellularly resolved cell embeddings by jointly leveraging RNA expression profiles, protein sequence representations, and protein structural information. Specifically, we employ a cross-attention architecture to integrate transcriptomic, sequence, and structural modalities and model their interactions within distinct subcellular compartments. The resulting embeddings represent each cell through its fine-grained subcellular organization, capturing both molecular expression patterns and the functional properties of the associated proteins. By learning cell representations at subcellular resolution, our framework preserves spatially organized biological information while integrating complementary signals across multiple molecular levels. To the best of our knowledge, this is the first framework that produces subcellularly resolved cell embeddings by jointly incorporating transcriptomic information, protein sequence representations, and protein structural knowledge within a unified cross-modal learning paradigm.

## 2. Spectral Initialization and Scheduled Graph Smoothness for Uncertain Knowledge Graph Completion

- Authors: Md Abrar Jahin, Taufikur Rahman Fuad, Jay Pujara, Craig A. Knoblock
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-02
- DOI: Unavailable
- Categories: cs.LG, cs.AI
- Relevance: 3.3844760665280385
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.02519v1
- PDF: https://arxiv.org/pdf/2609.02519v1
- Local PDF: pdf/2026-09-04_02_Spectral Initialization and Scheduled Graph Smoothness for Uncertain Knowledge Graph Completion.pdf

Uncertain knowledge graphs (UKGs) extend knowledge graphs by assigning each triple a continuous confidence score. Since most possible triples lack observed confidences, recent methods rely on semi-supervised learning to generate pseudo-labels. These methods initialize entity embeddings without using the confidence-weighted graph, discarding its global community and hub structure. We introduce QUEST, which adds no trainable parameters to the standard confidence-distribution learning pipeline. First, QUEST initializes entity embeddings using the smallest non-trivial eigenvectors of the confidence-weighted graph Laplacian, incorporating community and hub structure before training. Second, QUEST applies an unbiased mini-batch Dirichlet energy regularizer to enforce early-stage structural consistency. On two UKG datasets, QUEST improves confidence prediction and link prediction on six of eight metric-dataset pairs over prior methods and matches the previous best on the remaining two, while removing the instability spike observed on dense graphs. These results indicate that spectral structural priors combined with a graph Dirichlet energy regularizer improve accuracy, training stability, and checkpoint reliability in UKG completion.

## 3. PEARL: Path-Entity Aligned Relational Learning with Contextual Subgraphs for Inductive Knowledge Graph Completion

- Authors: Yunchi Yang, Longlong Li, Cunquan Qu
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-02
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 3.369174410605561
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.02216v1
- PDF: https://arxiv.org/pdf/2609.02216v1
- Local PDF: pdf/2026-09-04_03_PEARL_ Path-Entity Aligned Relational Learning with Contextual Subgraphs for Inductive Knowledge Graph Completion.pdf

Inductive knowledge graph completion (IKGC) aims to predict missing links involving entities unseen during training, requiring models to learn transferable relational and structural patterns. Existing subgraph- and path-based approaches often encode relational paths independently of their surrounding query subgraphs, although the predictive relevance of a path may vary across structural contexts. We propose PEARL, a Path-Entity Aligned Relational Learning framework that models paths as context-conditioned reasoning signals. PEARL constructs a query-specific contextual subgraph from the union of the query entities' neighborhoods and uses a large language model (LLM)-guided retriever to distill semantically relevant paths. It then builds a bipartite interaction graph over paths, contextual entities, and a global subgraph representation, allowing path embeddings to adapt to local and global structural evidence. To suppress noise introduced by the enlarged context, PEARL employs a dual-view contrastive objective that promotes representation consistency under stochastic contextual perturbations. Experiments on WN18RR, FB15k-237, and NELL-995 show that PEARL obtains the best average Hits@10 among the compared IKGC methods on all three benchmarks. Ablation studies, efficiency analyses, and case studies further validate the contributions of contextual subgraph modeling, semantic path retrieval, path-entity interaction, and contrastive regularization.

## 4. Codebook Agent: Amortized Topology Design for LLM Multi-Agent Systems

- Authors: Jinxi Yu, Yubei Li, Eric Hanchen Jiang, Zhi Zhang, Dong Liu, Wenxiao Zhao, Levina Li, Kai-Wei Chang, Ying Nian Wu
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-02
- DOI: Unavailable
- Categories: cs.AI, cs.LG, cs.MA
- Relevance: 3.3593059448313483
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.02264v1
- PDF: https://arxiv.org/pdf/2609.02264v1
- Local PDF: pdf/2026-09-04_04_Codebook Agent_ Amortized Topology Design for LLM Multi-Agent Systems.pdf

Adapting the communication topology of an LLM multi-agent system to each query improves both accuracy and efficiency, yet current designers treat this as conditional graph generation: a variational, autoregressive, or diffusion decoder searches the $N \times N$ adjacency space, and a graph-network proxy trained on utility and a structural cost such as edge count ranks the sampled candidates. We argue that this formulation is misaligned with the problem. Empirically, topologies that survive a reward filter collapse to about six distinct graphs even when the codebook capacity grows from 8 to 64; edge count is negatively correlated with measured token consumption (Pearson $r \approx -0.4$), so sparsifying the graph makes inference more expensive; and a message-passing scorer over agent-profile nodes is adjacency-invariant whenever agents share a profile---the default configuration of published benchmarks---so it cannot rank candidates at all in that regime. These three facts motivate Codebook Agent: a vector-quantized autoencoder compresses successful topologies into a query-independent 16-entry codebook; a reward-weighted MLP maps the query embedding to a distribution over codes; and an MLP proxy that reads the flattened adjacency, regressed on measured utility and per-task normalized token cost, reranks the top decoded candidates in a single batched forward pass. With no iterative search and no message passing at test time, Codebook Agent is the most accurate method on all six benchmarks we compare (84.6 average against 83.0 for the strongest prior designer), emits a topology in 2.4 ms, and uses 21.9--33.2% fewer LLM tokens.

## 5. DiffIE: Diffusion-based Open Information Extraction

- Authors: Konstantin Fedorov, Valentin Malykh
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-02
- DOI: Unavailable
- Categories: cs.CL, cs.AI
- Relevance: 3.31974684810599
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.02315v1
- PDF: https://arxiv.org/pdf/2609.02315v1
- Local PDF: pdf/2026-09-04_05_DiffIE_ Diffusion-based Open Information Extraction.pdf

A single sentence often expresses multiple valid relational triplets, which makes Open Information Extraction (OpenIE) fundamentally a multi-output task. Existing neural systems handle this by autoregressive generation, which is flexible but slow and prone to redundancy, or by fixed-slot prediction, which is efficient but couples the extraction budget to training. We introduce DIFFIE which instead treats the stochasticity of conditional discrete diffusion as the extraction mechanism itself: independent reverse-diffusion trajectories over per-token role tags produce a pool of candidate triplets, which are clustered under lenient matching and ranked to form the output. Both the pool size and the number of returned extractions are inference-time choices, decoupling the extraction budget from training and exposing test-time compute as a tunable axis. DIFFIE achieves the new state of the art in CaRB (1-1) both F1 and AUC, and outperforms the strongest rule-based system (ClausIE) in BenchIE; it also remains competitive in standard CaRB and WiRe57 evaluations, giving the best average score among systems that report all four benchmarks. Ablations show that uniform discrete diffusion outperforms absorbing state diffusion in our setting, and that a matched non-diffusion stochastic tagger does not reproduce its gains. Our results indicate that diffusion stochasticity is an effective mechanism for structured prediction tasks with multiple valid outputs.

## 6. Oracle, will I ever learn? A study of prediction convergence and complementarity across link prediction models

- Authors: Guillaume Méroué, Fabien Gandon, Pierre Monnin
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-02
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.2628524750403587
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.02638v1
- PDF: https://arxiv.org/pdf/2609.02638v1
- Local PDF: pdf/2026-09-04_06_Oracle, will I ever learn_ A study of prediction convergence and complementarity across link prediction models.pdf

Knowledge graphs have become an important source of structured knowledge for Web applications, including search, question answering, and recommender systems. In these applications, link prediction can serve either as a prediction task itself or as a means to enrich incomplete knowledge graphs for downstream tasks. Interestingly, different link prediction models, or even different training runs of the same model, can produce substantially different predictions for the same query. This suggests a variability in the capture of the underlying knowledge by models, thus raising a fundamental question: to what extent do different models capture complementary knowledge, and how much of this knowledge could be recovered by combining them? We propose to measure model complementarity through the performance of an oracle that, for each query, selects the best prediction among a considered set of models, hence providing an upper bound on the performance achievable through model combination. Across several architectures and benchmarks, we find a substantial gap between individual models and their oracle, revealing that different models capture complementary knowledge. Yet, this complementarity rapidly saturates as more models are added, leaving a persistent subset of queries unsolved even by a large number of models. These findings reveal both the potential of model complementarity and a fundamental limit to what current link prediction models can collectively recover; thereby highlighting the need for further research to build robust Web applications.

## 7. SSAKG 2.0: An Open-Source Package for Structural Associative Sequence Memory and Context-Based Retrieval

- Authors: Przemysław Stokłosa, Janusz A. Starzyk, Paweł Raif
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-01
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 3.239800395096249
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.01849v1
- PDF: https://arxiv.org/pdf/2609.01849v1
- Local PDF: pdf/2026-09-04_07_SSAKG 2.0_ An Open-Source Package for Structural Associative Sequence Memory and Context-Based Retrieval.pdf

This article presents SSAKG 2.0, an open-source software package for constructing and operating Structural Sequential Associative Knowledge Graphs (SSAKGs). An SSAKG represents objects as graph vertices and ordered sequences as structural patterns of graph connections. The resulting sparse graph is used as an associative memory in which complete sequences can be reconstructed from a partial, unordered context.
  Version 2.0 introduces new algorithms that exploit individual bits of computer memory to efficiently search graph connections. The package is implemented in Python, while performance-critical graph operations are implemented in C and exposed through a Python interface. This hybrid implementation provides a flexible high-level programming environment while reducing the memory and computational overhead associated with large sparse graphs.
  The algorithms were evaluated using randomly generated numerical sequences, sequences derived from sentences in the NLTK corpus, and mRNA sequences. The experiments demonstrate the ability of the package to store and reconstruct sequences from partial contexts and provide a basis for evaluating the effects of graph density, sequence length, and memory size on retrieval performance.
  SSAKG 2.0 is distributed under the Apache 2.0 open-source license. The package includes documentation and reproducible examples and is publicly available through GitHub and the Python Package Index (PyPI).

## 8. Seed-Anchored Budget-Bounded Graph Rendering for Question Answering on Industry-Standard Power-Grid Information and Exchange Models

- Authors: Jayakumar Manoharan, Yamini Sehgal
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-02
- DOI: Unavailable
- Categories: eess.SY, cs.AI, cs.IR
- Relevance: 3.180385165794318
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.02011v1
- PDF: https://arxiv.org/pdf/2609.02011v1
- Local PDF: pdf/2026-09-04_08_Seed-Anchored Budget-Bounded Graph Rendering for Question Answering on Industry-Standard Power-Grid Information and Exch.pdf

Large language model question answering over power-grid models must respect a fixed context budget. We introduce seed-anchored graph rendering, a deterministic method that prioritizes query-local graph evidence without adding method-specific tuned or learned parameters beyond the shared hop bound and context budget. The method provides a checkable condition under which predefined seed-local answer-bearing render units are preserved in a greedy bounded-context prefix. We evaluate the approach on Common Information Model (CIM) network models exchanged through the Common Grid Model Exchange Standard (CGMES). On two budget-binding CGMES encodings, naive descriptions-first rendering retains local evidence for every single-hop item but only 0.12 and 0.00 of multi-hop items, whereas seed-anchored rendering retains all such evidence. On a preregistered fresh 100-item bank from the SmallGrid topology family, accuracy rises from 0.450 to 0.970 under a fixed 8,000-character context budget. Under a common retrieval and rendering pipeline, the standards-native seed-anchored graph matches or exceeds extracted graph representations produced by LightRAG, Microsoft GraphRAG, and HippoRAG, while avoiding LLM graph-construction tokens. The results are specific to the evaluated CIM/CGMES models, reader, and context budget; they concern budget-bounded retrieval rather than general question answering.

## 9. Import What You Need: Learning When and How to Augment EHR Graphs with External Knowledge

- Authors: Chen Chen, Mohsen Nayebi Kerdabadi, Dongjie Wang, Mei Liu, Zijun Yao
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-01
- DOI: Unavailable
- Categories: cs.LG, cs.AI
- Relevance: 3.1321977011233337
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.01839v1
- PDF: https://arxiv.org/pdf/2609.01839v1
- Local PDF: pdf/2026-09-04_09_Import What You Need_ Learning When and How to Augment EHR Graphs with External Knowledge.pdf

Longitudinal prediction from electronic health records (EHRs) is limited by the sparsity and irregularity in patient trajectories, and knowledge augmentation with external knowledge graphs (KGs) offers a promising way to alleviate these issues. However, most existing methods perform fixed, context-agnostic topology augmentation by adding the same KG nodes and edges regardless of a patient's evolving state. We propose ReTA, a Reinforcement learning-based dynamic Topology Augmentation framework that casts KG import as a per-visit, budget-aware policy. ReTA first constructs an offline refined pool of KG-grounded templates, then learns a policy to select one augment action per visit from three options: Soft Import, which enriches node features without modifying graph topology, Hard Import, which grafts a compact KG subgraph onto the visit graph to create message-passing shortcuts, and Skip, which leaves the visit unaugmented when the base encoder is already confident. To stabilize learning, ReTA employs a decoupled encoder that processes semantic and structural signals in separate channels and fuses them via adaptive gating. Experiments on MIMIC-III and MIMIC-IV across diagnosis prediction, mortality, and readmission show that ReTA consistently outperforms strong baselines while remaining efficient, transfers across datasets and knowledge graphs, and yields interpretable augmentation patterns. The robust gains under sparse supervision highlight the advantage of ReTA's dynamic decision to import knowledge, boosting accuracy while curbing costs.

## 10. MethyAnno: An Interpretable Automated Annotation Method Leveraging Multi‐Scale Information and Metric Learning Framework for scDNAm Data

- Authors: Yuhang Jia, Siyu Li, Songming Tang, 顾克菊, Shengquan Chen
- Source: openalex
- Venue type: journal
- Journal: Advanced Science
- Publication status: published
- Publication date: 2026-09-01
- DOI: https://doi.org/10.1002/advs.77524
- Categories: Epigenetics and DNA Methylation, Single-cell and spatial transcriptomics, Machine Learning in Bioinformatics
- Relevance: 3.0978660235650746
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://doi.org/10.1002/advs.77524
- PDF: Unavailable
- Local PDF: Not downloaded

Single-cell DNA methylation (scDNAm) sequencing provides unique insights into epigenetic heterogeneity and cell-specific regulatory landscapes. However, accurate cell type annotation for scDNAm data remains challenging, as the distinct data distribution of scDNAm hinders the adaptation of annotation methods from other omics, and specialized annotation tools for scDNAm are currently lacking. Here, MethyAnno is proposed as an interpretable deep metric learning framework that leverages multi-scale information for accurate cell type annotation of scDNAm data. Additionally, MethyAnno enables generalized category discovery in open-set scenarios by utilizing density-based clustering to automatically estimate the number of novel cell types, while simultaneously deciphering cell-type-specific epigenetic signatures for biological interpretability. Extensive experiments demonstrate that MethyAnno excels in cross-dataset annotation and novel type discovery, showing exceptional robustness in few-shot scenarios for rare cell types. Moreover, interpretability analysis in the human brain dataset correctly recovers the genetic link between Sst interneurons and epilepsy heritability, the association of OPC cells with Alzheimer's disease, as well as the regulatory role of Pvalb cells in synaptic plasticity. Taken together, these findings establish MethyAnno as a robust and biologically interpretable tool for accurate cell type annotation and downstream epigenetic analysis.

## 11. NE-R1: Enhancing Named Entity Recognition Model via Reinforcement Learning

- Authors: Meixuan Chen, Hehan Li, Ruizhi Zhao, Xin Lu, peizhi xu, Liwei Qian, LI Meifang, shuanglong li, Hanmeng Liu, Xin Pei, Yanbiao Ma
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-02
- DOI: Unavailable
- Categories: cs.CL, cs.AI
- Relevance: 3.0034169161373336
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.02366v1
- PDF: https://arxiv.org/pdf/2609.02366v1
- Local PDF: pdf/2026-09-04_11_NE-R1_ Enhancing Named Entity Recognition Model via Reinforcement Learning.pdf

Named Entity Recognition (NER) has achieved substantial progress since the advent of large language models (LLMs). Nevertheless, the recognition of long-tail and domain-specific entities remains challenging due to the deficiency in parametric knowledge. Retrieval-augmented generation (RAG) offers a promising remedy by injecting external knowledge, but it also introduces noise and unnecessary cost when dealing with familiar cases. In this paper, we propose NE-R1, a novel framework for adaptive retrieval-augmented NER. We design a "retrieval-on-demand" mechanism for NER. Then we integrate it into models by a two-stage training method: (1) multi-task instruction tuning initialization; (2) end-to-end RL optimization with CoT. To achieve reasonable selection between parameterized and external knowledge, we design a multi-dimensional reward considering both accuracy and retrieval benefit. NE-R1 achieves state-of-the-art performance on various benchmarks, with an average F1 score gain of 2.52% in in-domain evaluation and 1.18% in zero-shot cross-domain evaluation.

## 12. DocHop: Benchmarking Out-of-domain Multi-hop Reasoning in Information-Dense Documents

- Authors: Zhuoran Yu, Le Thien Phuc Nguyen, Jaden Park, Xinyi Gu, Zexue He, Soochahn Lee, Rogerio Feris, Yong Jae Lee
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-02
- DOI: Unavailable
- Categories: cs.AI, cs.CV, cs.LG
- Relevance: 2.9876017607255934
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.02059v1
- PDF: https://arxiv.org/pdf/2609.02059v1
- Local PDF: pdf/2026-09-04_12_DocHop_ Benchmarking Out-of-domain Multi-hop Reasoning in Information-Dense Documents.pdf

Multimodal Large Language Models (MLLMs) have achieved strong performance on structured visual understanding tasks such as chart and document question answering. However, existing benchmarks typically evaluate these domains in isolation, leaving underexplored a key capability: whether models can use textual context to determine how chart evidence should be selected, interpreted, and aggregated. We introduce DocHop, a benchmark for integrated chart--context reasoning in document-style images. In DocHop, the document narrative specifies multi-step compositional constraints, while charts provide the corresponding data values. Questions are grounded on a semantic reference label defined in the narrative, requiring models to resolve target entities from context before aggregating evidence across multiple charts. To enable systematic evaluation, we construct DocHop via a stochastic logic-first generation pipeline with controllable reasoning depth and visual density, covering 2,074 examples across six task categories. Experiments on a wide range of proprietary and open-source MLLMs show a substantial gap to human performance: annotators achieve over 90% accuracy, while the best model reaches only 62.83%. Reasoning-enhanced models consistently show improved results, but performance degrades as reasoning complexity increases. Overall, DocHop provides a controlled testbed for challenging multi-hop document reasoning.

## 13. SEAL: Reinforcing Global Safety in Mixture-of-Experts through Shared Expert ALignment

- Authors: Qingyu Meng, Yiwei Zha, Jiahuan Pei, Koen Hindriks, Herbert Bos, Min Chen
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-02
- DOI: Unavailable
- Categories: cs.LG, cs.AI, cs.CR
- Relevance: 2.968730572327348
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.02293v1
- PDF: https://arxiv.org/pdf/2609.02293v1
- Local PDF: pdf/2026-09-04_13_SEAL_ Reinforcing Global Safety in Mixture-of-Experts through Shared Expert ALignment.pdf

Mixture-of-Experts (MoE) is a scaling architecture for large language models that activates only a small subset of expert modules per token, enabling massive parameter growth with nearly constant computation. Recent Hybrid MoE architecture adds \textit{shared experts} to capture consistently useful representations, further improving stability and generalization. MoE now powers many flagship open-source and commercial models, yet remains vulnerable to adversarial attacks. Specifically, sparse routing introduces a structural vulnerability: MoE safety hinges on which experts are activated, and adversaries can subvert this selection through jailbreak prompts, malicious fine-tuning, and weight-level pruning of safety-critical neurons. Existing defenses primarily focus on hardening the router, but an adversary may still manipulate or bypass the routing trajectory due to the routing process's nondeterministic nature, thereby collapsing the defense. To cope with this problem, we first identify theoretically and empirically that shared expert, an always-activated component containing a small proportion of safety-critical neurons, can overcome the uncertainty of sparsely activated routing path and serve as a router-independent anchor to enhance global safety alignment. Based on this insight, we propose SEAL, a training-time parameter-efficient defense that produces a plug-and-play adapter attached to shared expert, and SEAL++, a variant that adds an orthogonal constraint preserving pre-existing safety subspaces during training. We evaluate SEAL and SEAL++ across six attack scenarios that combine three adversarial inputs (harmful prompting, jailbreak, malicious fine-tuning) with and without neuron pruning. SEAL reduces attack success rate (ASR) by up to 60\%, at a capability cost of at most 1.4\% on a five-benchmark average. Additionally, SEAL can seamlessly integrate with router-level ......

## 14. Differential analysis of image-based chromatin tracing data with Dory

- Authors: Zhaoxia Ma, Liu Mp, Shengyuan Wang, Siyuan Wang, Chongzhi Zang
- Source: openalex
- Venue type: journal
- Journal: Genome biology
- Publication status: published
- Publication date: 2026-09-03
- DOI: https://doi.org/10.1186/s13059-026-04264-y
- Categories: Genomics and Chromatin Dynamics, Genomic variations and chromosomal abnormalities, Single-cell and spatial transcriptomics
- Relevance: 2.9222002701119267
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://doi.org/10.1186/s13059-026-04264-y
- PDF: Unavailable
- Local PDF: Not downloaded

Spatial organization of the genome plays a vital role in defining cell identity and regulating gene expression. The three-dimensional (3D) genome structure can be measured by sequencing-based techniques such as Hi-C usually on the cell population level or by imaging-based techniques such as chromatin tracing at the single-cell level. Chromatin tracing is a multiplexed DNA fluorescence in situ hybridization (FISH)-based method that can directly map the 3D positions of genomic loci along individual chromosomes at single-molecule resolution. However, few computational tools are available for statistical differential analysis of chromatin tracing data, which are inherently high-dimensional, highly variable and contain many missing values. Here, we present Dory, a statistical method for identifying differential spatial patterns between two groups of chromatin traces. Dory quantifies pairwise spatial distances among genomic regions in a chromatin trace and applies multi-level statistical tests to detect significant structural differences between the two groups of traces. It produces a differential score matrix highlighting region pairs with significant distance difference. Applying Dory to multiple chromatin tracing datasets, we found that the detected chromatin structural changes were associated with alterations in A/B compartments and promoter-enhancer interactions correlated with differential gene expression. Dory is a robust and user-friendly computational tool for quantitative analysis of imaging-based 3D genome data that enables systematic exploration of chromatin architecture and its roles in gene regulation.

## 15. Linear Fusion MultiDiffusion for Fast Training-Free Spherical Panorama Generation

- Authors: Akio Hayakawa, Yusuke Mukuta, Tatsuya Harada
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-02
- DOI: Unavailable
- Categories: cs.CV, cs.LG
- Relevance: 2.89731007156282
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.01997v1
- PDF: https://arxiv.org/pdf/2609.01997v1
- Local PDF: pdf/2026-09-04_15_Linear Fusion MultiDiffusion for Fast Training-Free Spherical Panorama Generation.pdf

We propose LF-MultiDiffusion, a training-free panorama generation method that extends MultiDiffusion to support linear projections between target and reference image spaces. Our key idea is to reformulate latent aggregation as a regularized least-squares problem and solve it efficiently with a Krylov-based iterative solver inside the denoising loop. This formulation enables denser and more natural mappings than prior training-free methods, yielding more stable generation with far fewer perspective views. As a result, LF-MultiDiffusion reduces the number of image generator evaluations during denoising and significantly improves inference efficiency. Experiments show that LF-MultiDiffusion achieves better visual quality, text alignment, and panoramic consistency than the strongest training-free baseline, while providing a 15.36$\times$ speedup. Our project page is available at: https://ahykw.github.io/lfmd.

## 16. NeoMME: A Single-Tower Multimodal-Native Multilingual Foundation Encoder for Efficient Fine-Tuning and Inference

- Authors: Aurélien Lac, Tony Wu
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-31
- DOI: Unavailable
- Categories: cs.IR, cs.AI, cs.CV
- Relevance: 2.8849749827900064
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.01657v1
- PDF: https://arxiv.org/pdf/2609.01657v1
- Local PDF: pdf/2026-09-04_16_NeoMME_ A Single-Tower Multimodal-Native Multilingual Foundation Encoder for Efficient Fine-Tuning and Inference.pdf

Multimodal models often build on architectures designed for generative vision-language modeling, typically combining separately pretrained vision encoders with causal language models. Visual document retrievers such as ColPali repurpose these models as encoders, carrying over the parameter and compute overhead of a VLM for a non-generative task.
  We introduce NeoMME, a family of 260M and 800M-parameter Multimodal and Multilingual bidirectional Encoders that process multilingual text and raw image patches in a single bidirectional Transformer encoder. Both models are pretrained from scratch with a masked discrete-diffusion text objective, conditioned on visible image patches for multimodal examples. Both support a 16,384-token context, enough to encode up to two standard 4K UHD images.
  To demonstrate its downstream capabilities, we fine-tune NeoMME with jointly trained dense and late-interaction heads. On the ViDoRe v3 benchmark, the resulting NeoMME-Retriever 260M outperforms all evaluated models strictly below 800M parameters with 0.523 nDCG@10, while NeoMME-Retriever 800M reaches 0.556. At a matched 2048x2048 image input size on an NVIDIA L40S, NeoMME-260M encodes pages with about 2x the throughput of ColModernVBERT. Hierarchical token pooling and asymmetric quantization compress late-interaction multimodal document embeddings by 255x while preserving over 95% of baseline nDCG@10. We contribute NeoMME to Hugging Face Transformers and release the pretrained backbone and retrieval-compatible checkpoints under Apache 2.0 at https://hf.co/collections/Hcompany/neomme.

## 17. Loom: Weaving Diagnostic Strands into Free-Text Consensus via Embedding-Space Reweighting

- Authors: Ron Begleiter, Katya Egert Berg, Gilad Saban, Gil Shabat
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-02
- DOI: Unavailable
- Categories: cs.AI, cs.CL, cs.LG
- Relevance: 2.8774298917786845
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.02649v1
- PDF: https://arxiv.org/pdf/2609.02649v1
- Local PDF: pdf/2026-09-04_17_Loom_ Weaving Diagnostic Strands into Free-Text Consensus via Embedding-Space Reweighting.pdf

Aggregating noisy, conflicting textual hypotheses into a reliable consensus is a fundamental challenge when deploying NLP systems in real-world industrial settings. While monolithic Large Language Model (LLM) agents offer unbounded expressivity for tasks like Root Cause Analysis (RCA), they suffer from context limits, compounding hallucinations, and prohibitive inference latency. Traditional weak supervision offers statistical rigor but is mathematically restricted to discrete classes. We present Loom, a generative consensus framework deployed for real-world RCA that bridges these paradigms. Loom aggregates open-form hypotheses emitted by modular heuristics (diagnostic templates dynamically populated with episode-specific entities, times, and metrics) by projecting them into a continuous embedding space, and resolves conflicting signals with an iterative centroid-based reweighting algorithm. The resulting consensus weights ground a single lightweight LLM synthesis step. Evaluated on the OpenRCA benchmark, Loom occupies the accuracy--efficiency Pareto frontier: it matches a state-of-the-art autonomous agent on Bank and Market-2 and trails on Market-1 and Telecom, while using a single LLM call per incident on all four datasets ($\sim$26$\times$ faster; $\sim$33$\times$ with an 8B-parameter synthesizer). We discuss our deployment experience, highlighting lessons learned regarding the trade-offs between agentic depth and inference latency, negative results in redundancy detection, and how deterministic consensus fosters trust among Subject Matter Experts~(SMEs).

## 18. GeoSPRINT: Geometric Redundancy-Aware Step Pruning for Inference in Diffusion Trajectories

- Authors: Arpita Joshi
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-02
- DOI: Unavailable
- Categories: cs.LG, cs.AI
- Relevance: 2.8771411545773082
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.02160v1
- PDF: https://arxiv.org/pdf/2609.02160v1
- Local PDF: pdf/2026-09-04_18_GeoSPRINT_ Geometric Redundancy-Aware Step Pruning for Inference in Diffusion Trajectories.pdf

Diffusion models achieve high sample quality but remain expensive at inference time because sampling requires many sequential neural function evaluations (NFEs). Existing acceleration methods either use fixed step-skipping schedules, adapt step sizes based on local numerical error, or require additional training. We introduce GeoSPRINT (Geometric Step Pruning for Inference in Trajectories), a training-free framework for constructing non-uniform sampling schedules from the geometry of denoising trajectories. GeoSPRINT detects geometrically redundant steps using a hyperplanarity test in latent space, implemented efficiently via QR factorization, and converts the resulting redundancy profile into a sampling schedule that allocates more steps to high-curvature regions of the trajectory. In addition, we introduce the trajectory projection score $α_{\mathrm{traj}}$, a residual-variance metric that quantifies trajectory straightness and serves as a model-free diagnostic for rectified flow quality. Across CIFAR-10 ($32{\times}32$), LSUN Church ($256{\times}256$), and Stable Diffusion v1.5 ($512{\times}512$ latent), GeoSPRINT consistently improves over uniform DDIM (Denoising Diffusion Implicit Models) schedules at matched NFE budgets. On CIFAR-10, GeoSPRINT improves FID (Fréchet Inception Distance) by 0.7-1.1 over DDIM across 49-89 NFEs and surpasses DPM-Solver++ at NFE${\geq}30$ despite using a first-order DDIM solver. On LSUN Church, it reduces FID from 1.48 to 1.26 at 52 steps, and on Stable Diffusion v1.5 it achieves up to 1.93 FID improvement over DDIM. These results show that trajectory geometry provides a useful global signal for allocating inference steps and that schedule quality can substantially improve diffusion sampling efficiency without retraining.

## 19. InstEditSeg: Instruction-Driven Image Editing for Polyp and Skin Lesion Segmentation

- Authors: Ziquan Liu, Zhewei Zhu, Xuyang Shi
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-02
- DOI: Unavailable
- Categories: cs.CV, cs.AI
- Relevance: 2.8667076097138184
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.02004v1
- PDF: https://arxiv.org/pdf/2609.02004v1
- Local PDF: pdf/2026-09-04_19_InstEditSeg_ Instruction-Driven Image Editing for Polyp and Skin Lesion Segmentation.pdf

Accurate segmentation of polyps and skin lesions is pivotal for clinical diagnosis, yet existing methods struggle with low contrast, ambiguous boundaries, and cross-domain distribution discrepancies. Discriminative networks and most diffusion-based segmentation approaches predict standalone binary masks, leaving the visual priors of large-scale pretrained generative models largely unexploited. We propose InstEditSeg, a unified generative framework that reformulates medical segmentation as an instruction-driven image editing problem. Instead of emitting a mask, the model renders a color-coded overlay on the original image, conditioned on a textual instruction, so that the edited output aligns with the natural image distribution learned by latent diffusion models and mitigates the domain gap between natural and medical imagery. To recover fine anatomical structures, we introduce DINOv3 as an auxiliary visual encoder and a DINO Feature Guidance Block that builds a multi-scale feature pyramid. The pyramid is fused into the diffusion U-Net by channel concatenation and zero-initialized convolution so that hierarchical discriminative priors can be injected without perturbing the pretrained weights. A dual-branch classifier-free guidance strategy requiring only two forward passes per denoising step reduces inference cost. On polyp and skin lesion benchmarks the framework achieves accuracy competitive with strong discriminative baselines, and it further demonstrates concrete advantages of the generative formulation: notably better cross-domain generalization on unseen data, more complete multi-lesion segmentation, instruction-conditioned task control, and sampling flexibility. We also analyze the strengths and limitations of the paradigm, including its color sensitivity and unsupported attribute-conditioned selection. Code is available at: https://github.com/wincharm001/InstEditSeg.

## 20. Do Large Language Models Capture the Diversity in their Training Data?

- Authors: Youqi Wu, Farzan Farnia
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-02
- DOI: Unavailable
- Categories: cs.CL, cs.AI, cs.LG
- Relevance: 2.8543201890668075
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.02275v1
- PDF: https://arxiv.org/pdf/2609.02275v1
- Local PDF: pdf/2026-09-04_20_Do Large Language Models Capture the Diversity in their Training Data.pdf

Large language models are trained to model conditional distributions over text, yet it remains inadequately understood whether they capture the full diversity of plausible outputs present in their training data. We study this question through an information-theoretic lens by comparing the conditional entropy of model-generated outputs with that of the corresponding training data. Given paired input-output samples, we use conditional entropy and its matrix-based analogue based on von Neumann entropy to measure output variability beyond what is explained by the conditioning input, without requiring multiple reference outputs for the same prompt. Across LLM families with publicly available training data, including OLMo, Pythia, and GPT-Neo, we consistently find that model-generated outputs exhibit lower conditional entropy than their training data, across different model scales, sequence lengths, and decoding strategies. We observe a similar conditional diversity gap beyond language modeling, including class-conditioned ImageNet generators and text-conditioned models trained on MS-COCO. To address this gap, we propose a post-hoc correction mechanism that generates multiple outputs for each input and reweights them through a matrix-entropy projection, increasing conditional diversity while remaining close to the original model distribution. We prove the concavity of the matrix-based conditional entropy functional, which makes the resulting entropy-constrained projection a convex optimization problem, and develop a scalable mirror-descent algorithm for its implementation. Our results reveal a systematic conditional diversity gap between modern generative models and their training data, and provide an information-theoretic framework for measuring and mitigating this gap.

## 21. IDEEA: training-free Input-Dependent stEEring via Activation cluster matching

- Authors: Zheng Wang, Muchen Li, Renjie Liao, Yan Leng
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-02
- DOI: Unavailable
- Categories: cs.CL, cs.LG
- Relevance: 2.8509642445628227
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.02089v1
- PDF: https://arxiv.org/pdf/2609.02089v1
- Local PDF: pdf/2026-09-04_21_IDEEA_ training-free Input-Dependent stEEring via Activation cluster matching.pdf

Steering aligns large language models (LLMs) by injecting a bias into selected activations at inference time, offering a far cheaper alternative to weight-update methods such as supervised fine-tuning or reinforcement learning. However, most existing training-free steering methods are input-independent: a single direction is fitted once and shared across all inputs. This is fundamentally limiting as different inputs occupy different regions of the activation space and admit different optimal steering directions toward the same target concept, much as the gradient with respect to a fixed loss varies from input to input. We close this gap with IDEEA (Input-Dependent stEEring via Activation cluster matching), a training-free framework for input-dependent steering. IDEEA clusters the positive and negative activation supports per attention head, and solves an optimal-matching problem to construct a set of cluster-conditional directions, all about the target concept. At inference time, it picks from this pool of directions and uses the one that best matches the input's own activation for steering. IDEEA aligns the model toward the target concept while preserving the input's original representation, evidence that activations encoding a concept occupy several distinct sub-regions of the representation space rather than a single one. IDEEA improves the truth $\times$ info rate in TruthfulQA by an average of 9.9% (up to 23.5%) over the best input-independent baseline.

## 22. Task-Level Natural Language Priors as Learning Signals for Low-Resource LLM Training

- Authors: Jian Gao, Xiao Zhang, Xun Zhu, Miao Li, Ji Wu
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-02
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 2.842159422081283
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.02244v1
- PDF: https://arxiv.org/pdf/2609.02244v1
- Local PDF: pdf/2026-09-04_22_Task-Level Natural Language Priors as Learning Signals for Low-Resource LLM Training.pdf

Large language models (LLMs) often struggle when low-resource training data are ambiguous or incomplete. Task-level natural-language priors can provide useful guidance in such settings, but existing approaches usually treat these priors as input context rather than as learning signals during training. We propose Prior-Guided Tuning (PGT), a training perspective that incorporates natural-language priors as auxiliary learning signals for low-resource LLM training. Under this perspective, we introduce Contrastive Prior Steering (CPS), which keeps the original supervised objective intact while adding positive and negative prior-conditioned auxiliary losses to encourage task-consistent learning and discourage plausible but misleading alternatives. Experiments on AmbiMath, Jigsaw, and MNLI/HANS show that CPS consistently improves over plain and prompt fine-tuning. On AmbiMath, CPS achieves 97.6% average exact-match accuracy. On Jigsaw, CPS improves average Macro F1 by 9.5 percentage points over standard fine-tuning, and with 1/10 of the experimental training data slightly exceeds full-data plain fine-tuning. On HANS, CPS improves non-entailment accuracy by 8.3 and 5.2 percentage points for LLaMA 3.1 8B and Qwen 2.5 7B, respectively, while maintaining comparable in-domain MNLI accuracy. These results support our central claim: task-level natural-language priors can provide useful guidance as auxiliary learning signals for low-resource LLM training. Our code and data will be publicly available.

## 23. SkillGLoW: Procedural-Family Skill Consolidation for Self-Improving Agents on Long-Horizon Task Streams

- Authors: Ao Yan, Xin Zhang, Jiawei Du, Joey Tianyi Zhou
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-02
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 2.8287962469462657
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.02217v1
- PDF: https://arxiv.org/pdf/2609.02217v1
- Local PDF: pdf/2026-09-04_23_SkillGLoW_ Procedural-Family Skill Consolidation for Self-Improving Agents on Long-Horizon Task Streams.pdf

LLM agents increasingly self-improve by writing and reusing textual skills, kept either as one global document or as a flat pool of per-task entries, though most of the evidence comes from domains with structurally similar tasks. On long-horizon workloads where each task demands a different solution, the two forms fail in opposite ways: the document collapses into generic discipline, while the pool inflates and its entries stay bound to the instance that wrote them. We argue the missing unit of reuse is the solving procedure shared by a cluster of related tasks, and build SkillGLoW (Global-Local Weave) around it: the local skills a task writes from its own execution are aggregated into procedural families and compressed into de-instantiated global priors, while the instance detail they hold is regenerated per task rather than stored; a commit gate admits a prior only when real execution shows it does not degrade the deployed library. Across four benchmarks (mathematical reasoning, terminal automation, software repair, and embodied control) and three models, the priors gain 17.2 points (hard) over the no-skill baseline on average, with positive gains in all 12 continual-improvement runs, and 18.0 with local regeneration, while the library holds one prior per procedural family, 3.6x more compact than the per-task pool. Under the same protocol GLoW leads a published single-document optimizer on 15 of 21 cells. Unmodified, the library lifts success on unseen ALFWorld tasks from 73.9% to 83.9%, evidence that what transfers is procedure rather than task memory.

## 24. Ranked by the Matcher: A Reproducibility Audit of Knowledge Graph Extraction from Threat Reports

- Authors: Safayat Bin Hakim, Houbing Herbert Song
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-01
- DOI: Unavailable
- Categories: cs.CR, cs.AI, cs.CL
- Relevance: 2.8243557334153673
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.01671v1
- PDF: https://arxiv.org/pdf/2609.01671v1
- Local PDF: pdf/2026-09-04_24_Ranked by the Matcher_ A Reproducibility Audit of Knowledge Graph Extraction from Threat Reports.pdf

Security teams and researchers choose knowledge-graph extraction tooling for threat reports on the strength of published triple-F1 scores, yet those scores depend on how predicted triples are matched to gold annotations. We could reimplement the stated matching rule for only five of twelve inspected systems. Re-scoring ten system outputs on shared documents under eight protocols reverses eleven of forty-five pairwise orderings; one fixed prediction set spans 0.16-0.70 F1. On GRID's external 378-item calibration set, no mechanical matcher (lexical, embedding, or entailment) agrees with multi-reviewer adjudication above 71%, whereas an LLM judge reaches 86%. To separate component effects from matcher rewards, we build CTIForge, whose deterministic validation layer can vary while extraction is held byte-identical. Across seven tested deployment configurations, validation raises precision for all four hosted backbones and lowers it for all three offline backbones. Because backbone, decoding, and backend-specific prompting covary, this is a descriptive split rather than an isolated serving effect. It coincides with a roughly 2.8-fold increase in actions explicitly disputing entity type, consistent with hand-written rules encoding the conventions of the extractor against which they were developed. We release the pipeline, protocol suite, and per-triple audit records.

## 25. SCX Router: Streaming Zero-Shot Model Selection with a Decoder-KV Classifier and a Real-World Task Ontology

- Authors: Ihor Stepanov, Aleksandr Smechov, Mykhailo Shtopko, Dmytro Vodianytskyi, Oleksandr Lukashov
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-02
- DOI: Unavailable
- Categories: cs.AI, cs.CL
- Relevance: 2.8046168791510873
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.02292v1
- PDF: https://arxiv.org/pdf/2609.02292v1
- Local PDF: pdf/2026-09-04_25_SCX Router_ Streaming Zero-Shot Model Selection with a Decoder-KV Classifier and a Real-World Task Ontology.pdf

The rapid proliferation of large language models (LLMs) and the growing diversity of their applications presents a unique optimization opportunity: selecting the right model for the task, while optimizing for speed, cost, and quality at a per-task level. However, inference endpoints can vary widely in quality, price, latency, context support, tool use, domain expertise, and reasoning behavior. This heterogeneity makes manual heuristics difficult to maintain and unlikely to achieve consistently favorable speed--cost--quality trade-offs on their own. We introduce \router{}, a lightweight GLiClass-based router that assigns a suitability score to each inference-time model label without autoregressive generation. The released 0.6B-parameter checkpoint combines a Qwen3 decoder with a shallow bidirectional scorer. Its decoder-KV execution path preserves a text-only key--value cache across a session, encodes only new dialogue turns, and evaluates transient candidate-label tokens without adding them to the persistent cache. The same checkpoint also predicts task type, difficulty, reasoning mode, and expected output length, and supports custom zero-shot labels. For task generation, we construct a task ontology with 23 families, 115 task types, 345 routable subtypes, 1,173 synthetic examples, and an orthogonal axis of 30 domains. Using this structure, we generate 150,000 verifier-scored tasks and 15,000 open-ended tasks. We then train the Qwen3 decoder on these tasks, while explicitly separating learned request prediction from per-task policies for attributes such as eligibility, cost, cache reuse, safety, and sovereignty. Across six LiveBench subsets, the router outperforms the mean candidate; on the selected 1,000-task subset, it achieves an aggregate top-1 score of 0.707 versus 0.696 for the strongest fixed model, with benchmark-dependent gains.

## 26. CAT-Flow: Curvature-Adaptive sTeps for Flow Matching

- Authors: Qinchan Li, Pedro Cisneros-Velarde, Keru Fu, Samuel Antunes Miranda, Sharan Vaswani, Hao Zhang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-01
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 2.779193140317493
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.01746v1
- PDF: https://arxiv.org/pdf/2609.01746v1
- Local PDF: pdf/2026-09-04_26_CAT-Flow_ Curvature-Adaptive sTeps for Flow Matching.pdf

Flow Matching has emerged as a leading framework for generative modeling, powering state-of-the-art systems such as FLUX and Stable Diffusion 3.5. However, the iterative nature of its ODE-based sampling process creates a fundamental efficiency bottleneck: the quality of generated samples is highly sensitive to the choice of step-sizes, and current models typically require 20 to 30 steps for good quality. In this work, we propose two lightweight, training-free algorithms, CAT-OV and CAT-OT that adapt step-sizes at inference time based on a novel connection between Flow Matching sampling and gradient flow. Our algorithms are computed efficiently by not requiring additional neural function evaluations. Specifically, CAT-OT estimates curvature over time via a finite-difference approximation of the time-derivative of the vector field, while CAT-OV approximates curvature over the state space via a gradient of the vector field. Under suitable conditions, both methods have truncation error bounds of constant order. Empirically, CAT-OV and CAT-OT outperform existing step-size heuristics in image quality metrics across four text- to-image Flow Matching models, reducing the number of generation steps required to reach comparable quality by up to 40%.

## 27. CoMerge: Conflict-Driven Preference Optimization for Multi-Task Model Merging

- Authors: Mingjie Zheng, Zihao Chen, Wenqing Chen, Weile Yuan, Zhixuan Chu, Jianxing Yu, Zibin Zheng
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-02
- DOI: Unavailable
- Categories: cs.AI, cs.CL
- Relevance: 2.7519600735340184
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.02273v1
- PDF: https://arxiv.org/pdf/2609.02273v1
- Local PDF: pdf/2026-09-04_27_CoMerge_ Conflict-Driven Preference Optimization for Multi-Task Model Merging.pdf

Model merging provides an efficient paradigm for constructing multi-task large language models (LLMs) without full model retraining, yet it remains challenged by parameter interference. While existing methods aim to preserve the capabilities of individual expert models and mitigate interference, they generally do not directly learn from the potentially degraded behaviors exposed by naive merging. In this paper, we propose a conflict-driven preference optimization framework for model merging (CoMerge), which reformulates model merging as a preference optimization problem. The approach utilizes a self-supervised, conflict-driven strategy that leverages the defects of naive merging methods (e.g., task arithmetic) as hard negative samples to construct preference pairs without external annotations. By applying preference optimization to refine lightweight, tensor-wise merging coefficients, CoMerge enables the model to mitigate parameter-space conflicts while preserving task-specific capabilities. Extensive experiments show that CoMerge achieves an average normalized performance of 0.9968 on MergeBench, outperforming all evaluated data-free and data-driven model-merging baselines. Furthermore, on Llama-3.1-8B-Instruct, CoMerge yields marked improvements on conflict-sensitive tasks such as instruction following and safety, while remaining highly competitive with full-parameter fine-tuning despite optimizing only 1,445 scalar coefficients.

## 28. Morphology signal in whole slide image foundation models can automatically triage slides

- Authors: Ayushi Sinha, Shashank Yadav, Benjamin Holmes, Pravat Das, Aaron W. Bogan, James S. Lewis, Santiago Romero-Brufau, Andrew Y. K. Foong, Scott H. Kaufmann, Kathryn M. Van Abel, David M. Routman, Michael R. Lucas
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-02
- DOI: Unavailable
- Categories: cs.CV, cs.LG
- Relevance: 2.7457555999250087
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.01987v1
- PDF: https://arxiv.org/pdf/2609.01987v1
- Local PDF: pdf/2026-09-04_28_Morphology signal in whole slide image foundation models can automatically triage slides.pdf

Patient exams in the cancer diagnosis and staging process typically generate several whole slide images (WSIs). One of the initial steps in training models on WSI data is identifying one or a few slides containing tumor or other diagnostic biomarkers necessary for downstream prediction tasks such as estimating recurrence risk or progression-free survival. This step requires tedious manual curation by experienced pathologists. Many published datasets make the artificial assumption of 1 slide per patient. Alternatively, all slides per patient may be used for model training, which may dilute the signal from the few slides containing tumor or other relevant information. In this paper, we present a pipeline to overcome these challenges using publicly available WSI foundation models (FMs). Our evaluations show that ranking WSIs based on predictions from zero-shot classification using WSI FMs accurately identifies slides with the most tumor, indicating that WSI FMs contain sufficient morphology signal to automatically triage slides. We also present a formulation for ranked evaluation to benchmark FM performance in slide triage. We show, on multiple datasets, that tumor slides are identified in the top-2 ranked slides for patients with up to 43 slides.

## 29. Scaling Law for Multimodal Large Language Model Supervised Fine-Tuning

- Authors: YiFan Zhang, Tao Yu, Feng Li, Chaoyou Fu, Yibo Hu, Kun Wang, Qingsong Wen, Zhang Zhang, Liang Wang, Rong Jin
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.7404225226740446
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.603/
- PDF: https://aclanthology.org/2026.acl-long.603.pdf
- Local PDF: pdf/2026-09-04_29_Scaling Law for Multimodal Large Language Model Supervised Fine-Tuning.pdf

The supervised fine-tuning (SFT) stage is crucial for multimodal large language models (MLLMs), yet a comprehensive scaling law to guide the optimal model-data configuration remains lacking. In this paper, we make an initial attempt to address this gap. First, we theoretically demonstrate that directly computing the optimal computation frontier for MLLM-SFT, as we can for traditional LLMs, is a challenging task. This complexity arises because MLLM-SFT is influenced by a broader range of factors, including model size, LLM pre-training tokens, and MLLM SFT tokens. To tackle this issue, we propose two scaling laws based on LLM paradigms: one applicable when training data volumes are well defined by researchers, and another for cases where models are sourced from open communities with unknown training data. Through theoretical modeling and approximations, we provide researchers with valuable recommendations for optimal resource allocation. Furthermore, we establish a strong correlation ( R 2 = 0.98 ) between training loss and downstream performance, enabling accurate performance estimation without the need for exhaustive benchmarking. To validate our scaling laws, we construct a testbed of 60 models ranging from 50 million to 8 billion parameters, totaling 1,560 checkpoints. Each checkpoint is evaluated on than 10 MLLM benchmarks, ensuring robust fitting of our formulations.

## 30. MedKInstruct: A Multimodal Knowledge Graph Based Framework for Multi-Hop and Hard-Negative Instruction Data Synthesis in MedVQA

- Authors: Yinan Wu, Jihang Jin, Xuhao Bao, Weiyan Zhang, Hanjing Yan, Tong Ruan, ChunMing Wang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.7385697538277913
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1391/
- PDF: https://aclanthology.org/2026.findings-acl.1391.pdf
- Local PDF: pdf/2026-09-04_30_MedKInstruct_ A Multimodal Knowledge Graph Based Framework for Multi-Hop and Hard-Negative Instruction Data Synthesis in.pdf

Medical visual question answering (MedVQA) requires models to provide accurate answers given a medical image and a corresponding question. Recently, instruction tuning of general large vision–language models (LVLMs) has become a dominant paradigm for this task, enabling open-ended predictions and effective integration of multimodal information. However, existing methods synthesize instruction data from image–caption pairs that primarily focus on visual attributes, rather than knowledge-level QA generation. This situation limits the model’s ability to learn relevant medical knowledge during training, thereby restricting its performance on MedVQA. Hence, this paper proposes MedKInstruct, which incorporates a multimodal medical knowledge graph (MMKG) to assist LVLMs in synthesizing knowledge-intensive instruction data. Additionally, we design an MMKG path–based reward function to train a stronger MedVQA model through reinforcement learning. Experimental results on the public datasets Slake and VQA-RAD show that MedKInstruct outperforms previous methods by 4.16% and 4.50%. The source code is available at the following link: https://github.com/Sonder-hang/MedKinstruct
