# Paper Daily Reading - 2026-06-28

## 1. AnyGraph: Graph Foundation Model in the Wild

- Authors: Lianghao Xia, Chao Huang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 4.037045235835997
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.44/
- PDF: https://aclanthology.org/2026.findings-acl.44.pdf
- Local PDF: pdf/2026-06-28_01_AnyGraph_ Graph Foundation Model in the Wild.pdf

The ubiquity of text-attributed graph data has highlighted the need for graph learning models with exceptional generalization across diverse textual and structural contexts. Current approaches struggle to extract generalizable insights from heterogeneous graph data, requiring extensive fine-tuning and limiting versatility across domains. In this work, we propose AnyGraph, a unified graph foundation model designed to handle key challenges: i) Structure Heterogenity - addressing distribution shift in graph structural patterns; ii) Feature Heterogenity - handling diverse textual representations; iii) Fast Adaptation - efficiently adapting to new graph-text domains. We build AnyGraph upon a Graph Mixture-of-Experts (MoE) architecture with a lightweight expert routing mechanism that effectively manages cross-domain distribution shift. Extensive experiments on 38 diverse datasets demonstrate AnyGraph’s strong zero-shot performance across domains with significant distribution shift, validating its fast adaptation ability and scaling law emergence. Our model is open-sourced and available at: https://github.com/HKUDS/AnyGraph.

## 2. ResSAT: enhancing spatial transcriptomics prediction from H&amp;E-stained histology images with an interactive spot transformer

- Authors: Anqi Liu, Yue Zhao, Woong-ki Kim, Hui Shen, Zhengming Ding, Hong‐Wen Deng
- Source: openalex
- Venue type: journal
- Journal: Genome biology
- Publication status: published
- Publication date: 2026-06-26
- DOI: https://doi.org/10.1186/s13059-026-04168-x
- Categories: Single-cell and spatial transcriptomics, Cell Image Analysis Techniques, Domain Adaptation and Few-Shot Learning
- Relevance: 3.7886888959172813
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://doi.org/10.1186/s13059-026-04168-x
- PDF: Unavailable
- Local PDF: Not downloaded

Spatial transcriptomics has revolutionized RNA quantification with spatial resolution. Hematoxylin and eosin (H&E) images, the gold standard in medical diagnosis, offer insights into tissue structure, correlating with gene expression patterns. We introduce ResSAT (Residual networks with Spatial encoding—self-Attention Transformer), a framework for predicting spatially resolved transcriptomic profiles from H&E images by integrating image features, spatial locations, and self-attention transformer-based spot interactions. Benchmarking on 10 × Visium datasets, ResSAT outperforms existing methods and preserved biologically meaningful spatial patterns, promising reduced spatial transcriptomics profiling costs and rapid acquisition of numerous profiles.

## 3. Graph-Assisted Large Language Models: A Perspective on Mitigating Intrinsic Limitations

- Authors: Haitong Luo, Fali Wang, Weiyao Zhang, Xianren Zhang, Zhiwei Zhang, Tianxiang Zhao, Minhua Lin, Jiahao Zhang, Hui Liu, Xianfeng Tang, Qi He, Suhang Wang, Xuying Meng, Yujun Zhang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.584874010280863
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.945/
- PDF: https://aclanthology.org/2026.findings-acl.945.pdf
- Local PDF: pdf/2026-06-28_03_Graph-Assisted Large Language Models_ A Perspective on Mitigating Intrinsic Limitations.pdf

Large language models (LLMs) have made progress in knowledge-intensive tasks, reasoning and planning, and collaborative problem solving, yet they exhibit intrinsic limitations such as knowledge cutoff, single-threaded reasoning that hinders finer-grained branch and aggregation, and rigid collaboration mechanisms that struggle to coordinate specialized capabilities. Graphs, with their ability to represent relational knowledge and complex dependencies, offer a natural means to address these limitations: they provide structured, high-density knowledge for augmenting or correcting LLMs’ generation; enable revisitable inference by organizing intermediate steps as graphs; and support dynamic coordination among experts or agents in collaborative settings. Motivated by these developments, we present the first systematic survey of graph-assisted LLMs from the perspective of how graph structures mitigate LLMs’ limitations. We introduce a taxonomy spanning *Graph-Assisted Knowledge Augmentation*, *Graph-Assisted Reasoning and Planning*, and *Graph-Assisted LLM Collaboration*, and analyze representative methods, summarize common design patterns, and outline open challenges and future directions for advancing LLMs with graph-based enhancements. The collected papers are available in [link here](https://github.com/FairyFali/Graph4LLM-Survey).

## 4. AROMA: Augmented Reasoning Over a Multimodal Architecture for Virtual Cell Genetic Perturbation Modeling

- Authors: Wang Zhenyu, Geyan Ye, Wei Liu, Man Tat Alexander Ng
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.5657965637284734
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1594/
- PDF: https://aclanthology.org/2026.findings-acl.1594.pdf
- Local PDF: pdf/2026-06-28_04_AROMA_ Augmented Reasoning Over a Multimodal Architecture for Virtual Cell Genetic Perturbation Modeling.pdf

Virtual cell modeling predicts molecular state changes under genetic perturbations in silico, which is essential for biological mechanism studies. However, existing approaches suffer from unconstrained reasoning, uninterpretable predictions, and retrieval signals that are weakly aligned with regulatory topology. To address these limitations, we propose AROMA, an Augmented Reasoning Over a Multimodal Architecture for virtual cell genetic perturbation modeling. AROMA integrates textual evidence, graph-topology information, and protein sequence features to model perturbation-target dependencies, and is trained with a two-stage optimization strategy to yield predictions that are both accurate and interpretable. We also construct two knowledge graphs and a perturbation reasoning dataset, PerturbReason, containing more than 498k samples, as reusable resources for the virtual cell domain. Experiments show that AROMA outperforms existing methods across multiple cell lines, and remains robust under zero-shot evaluation on an unseen cell line, as well as in knowledge-sparse, long-tail scenarios. Overall, AROMA demonstrates that combining knowledge-driven multimodal modeling with evidence retrieval provides a promising pathway toward more reliable and interpretable virtual cell perturbation prediction. Model weights are available at https://huggingface.co/blazerye/AROMA. Code is available at https://github.com/blazerye/AROMA.

## 5. PanoramaRAG: Enabling Consistent Global Topic Awareness in Graph-Based RAG

- Authors: Ding Deng, Xiang Li, Yaqing Zhang, Meng Li, Xiting Wang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.558081953920377
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1998/
- PDF: https://aclanthology.org/2026.findings-acl.1998.pdf
- Local PDF: pdf/2026-06-28_05_PanoramaRAG_ Enabling Consistent Global Topic Awareness in Graph-Based RAG.pdf

Graph-based Retrieval-Augmented Generation (RAG), which models relationships between fine-grained semantic units as a graph, effectively facilitates multi-hop reasoning to enhance large language model generation. However, its design focuses on local relationships, resulting in suboptimal performance for tasks that require global context, and the separation of query refinement from indexing limits the system’s ability to capture high-level implicit relationships within the graph. This paper proposes a **Panorama**-guided **RAG** paradigm (PanoramaRAG) that integrates a light yet comprehensive “panorama” of the corpus to guide all stages of the retrieval process. This hub bridges the knowledge graph, language models, and queries in a computationally efficient manner, applicable to both open-source and closed-source models. Experimental results demonstrate that our method exhibits strong performance across five datasets and a variety of tasks.

## 6. Colorful Talks with Graphs: Human-Interpretable Graph Encodings for Large Language Models

- Authors: Angelo Zangari, Peyman Baghershahi, Sourav Medya
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.5431956137869203
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.2049/
- PDF: https://aclanthology.org/2026.findings-acl.2049.pdf
- Local PDF: pdf/2026-06-28_06_Colorful Talks with Graphs_ Human-Interpretable Graph Encodings for Large Language Models.pdf

Graph problems are fundamentally challenging for large language models (LLMs). While LLMs excel at processing unstructured text, graph tasks require reasoning over explicit structure, permutation invariance, and computationally complex relationships, creating a mismatch with the representations of text-based models. Our work investigates how LLMs can be effectively applied to graph problems despite these barriers. We introduce a human-interpretable structural encoding strategy for graph-to-text translation that injects graph structure directly into natural language prompts. Our method involves computing a variant of Weisfeiler–Lehman (WL) similarity classes and maps them to human-like color tokens rather than numeric labels. The key insight is that semantically meaningful and human-interpretable cues may be more effectively processed by LLMs than opaque symbolic encoding. Experimental results across multiple graph algorithms and predictive tasks show significant improvements from our method on both synthetic and real-world datasets. By capturing both local and global-range dependencies, our method enhances LLM performance, especially on graph tasks that require reasoning over global graph structure.

## 7. Exploring Graph Learning Tasks with Pure LLMs: A Comprehensive Benchmark and Investigation

- Authors: Yuxiang Wang, Xinnan Dai, Wenqi Fan, Yao Ma
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.536427008909736
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.389/
- PDF: https://aclanthology.org/2026.findings-acl.389.pdf
- Local PDF: pdf/2026-06-28_07_Exploring Graph Learning Tasks with Pure LLMs_ A Comprehensive Benchmark and Investigation.pdf

In recent years, large language models (LLMs) have emerged as promising candidates for graph tasks. Many studies leverage natural language to describe graphs and apply LLMs for reasoning, yet most focus narrowly on performance benchmarks without fully comparing LLMs to graph learning models or exploring their broader potential. In this work, we present a comprehensive study of LLMs on graph learning tasks, evaluating both off-the-shelf and instruction-tuned models across a variety of scenarios. Beyond accuracy, we discuss data leakage concerns and computational overhead, and assess their performance under few-shot/zero-shot settings, domain transfer, structural understanding, and robustness. Our findings show that LLMs, particularly those with instruction tuning, greatly outperform traditional graph learning models in few-shot settings, exhibit strong domain transferability, and demonstrate excellent generalization and robustness. Our study highlights the broader capabilities of LLMs in graph learning and provides a foundation for future research.

## 8. SGG-R 3 : From Next-Token Prediction to End-to-End Unbiased Scene Graph Generation

- Authors: Jiaye Feng, Qixiang Yin, Yuankun Liu, Tong Mo, Weiping Li
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.52299174832418
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.992/
- PDF: https://aclanthology.org/2026.findings-acl.992.pdf
- Local PDF: pdf/2026-06-28_08_SGG-R 3 _ From Next-Token Prediction to End-to-End Unbiased Scene Graph Generation.pdf

Scene Graph Generation (SGG) structures visual scenes as graphs of objects and their relations. While Multimodal Large Language Models (MLLMs) have advanced end-to-end SGG, current methods are hindered by both a lack of task-specific structured reasoning and the challenges of sparse, long-tailed relation distributions, resulting in incomplete scene graphs characterized by low recall and biased predictions. To address these issues, we introduce SGG-R 3 , a structured reasoning framework that integrates task-specific Chain-of-Thought (CoT)-guided supervised fine-tuning (SFT) and reinforcement learning (RL) with group sequence policy optimization (GSPO), designed to engage in three sequential stages to achieve end-to-end unbiased scene graph generation. During the SFT phase, we propose a relation augmentation strategy by leveraging an MLLM and refined via embedding similarity filtering to alleviate relation sparsity. Subsequently, a stage-aligned reward scheme optimizes the procedural reasoning during RL. Specifically, we propose a novel dual-granularity reward which integrates fine-grained and coarse-grained relation rewards, simultaneously mitigating the long-tail issue via frequency-based adaptive weighting of predicates and improving relation coverage through semantic clustering. Experiments on two benchmarks show that SGG-R 3 achieves superior performance compared to existing methods, demonstrating the effectiveness and generalization of the framework.

## 9. MAKI: Multi-layer Aligned Knowledge Injection for Structure-aware Knowledge Graph Completion with Large Language Models

- Authors: Zhiwen Xie, Xin Wang, Guangyou Zhou, Derek F. Wong
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.4880724735547277
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1423/
- PDF: https://aclanthology.org/2026.findings-acl.1423.pdf
- Local PDF: pdf/2026-06-28_09_MAKI_ Multi-layer Aligned Knowledge Injection for Structure-aware Knowledge Graph Completion with Large Language Models.pdf

Recent advances in large language models (LLMs) have shown strong potential for knowledge graph completion (KGC). However, existing LLM-based approaches often struggle to effectively capture the structural information in knowledge graphs (KGs), leading to suboptimal reasoning performance. To address this challenge, we propose a Multi-layer Aligned Knowledge Injection (MAKI) model, a novel method that tightly integrates structured KG information into LLMs through multi-layer alignment. Specifically, we first leverage LLMs to encode the textual information of entities and relations, obtaining their semantic representations across multiple hidden layers. We then introduce a multi-layer aligned structure learning module, which uses graph neural networks (GNNs) to learn relational structures while aligning with the corresponding LLM layers to bridge the gap between structural and semantic spaces. Finally, a gated fusion mechanism is used to inject the structured knowledge into the LLM for reasoning over candidate triples. Experimental results on various benchmark datasets demonstrate that the proposed MAKI outperforms existing state-of-the-art methods.

## 10. EHRAG: Bridging Semantic Gaps in Lightweight GraphRAG via Hybrid Hypergraph Construction and Retrieval

- Authors: Yifan Song, Xingjian Tao, Zhicheng Yang, Yihong Luo, Jing Tang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.476559391450892
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1233/
- PDF: https://aclanthology.org/2026.findings-acl.1233.pdf
- Local PDF: pdf/2026-06-28_10_EHRAG_ Bridging Semantic Gaps in Lightweight GraphRAG via Hybrid Hypergraph Construction and Retrieval.pdf

Graph-based Retrieval-Augmented Generation (GraphRAG) enhances LLMs by structuring corpus into graphs to facilitate multi-hop reasoning. While recent lightweight approaches reduce indexing costs by leveraging Named Entity Recognition (NER), they rely strictly on structural co-occurrence, failing to capture latent semantic connections between disjoint entities. To address this, we propose EHRAG, a lightweight RAG framework that constructs a hypergraph capturing both structure and semantic level relationships, employing a hybrid structural-semantic retrieval mechanism. Specifically, EHRAG constructs structural hyperedges based on sentence-level co-occurrence with lightweight entity extraction and semantic hyperedges by clustering entity text embeddings, ensuring the hypergraph encompasses both structural and semantic information. For retrieval, EHRAG performs a structure-semantic hybrid diffusion with topic-aware scoring and personalized pagerank (PPR) refinement to identify the top-k relevant documents. Experiments on four datasets show that EHRAG outperforms state-of-the-art baselines while maintaining linear indexing complexity and zero token consumption for construction. Code is available at https://github.com/yfsong00/EHRAG.

## 11. Synapse: Empowering LLM Agents with Episodic-Semantic Memory via Spreading Activation

- Authors: Hanqi Jiang, Junhao Chen, Yi Pan, Ling Chen, Weihang You, Yifan Zhou, Ruidong Zhang, Yohannes Abate, Tianming Liu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.474867453933696
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1108/
- PDF: https://aclanthology.org/2026.findings-acl.1108.pdf
- Local PDF: pdf/2026-06-28_11_Synapse_ Empowering LLM Agents with Episodic-Semantic Memory via Spreading Activation.pdf

While Large Language Models (LLMs) excel at generalized reasoning, standard retrieval-augmented approaches fail to address the disconnected nature of long-term agentic memory. To bridge this gap, we introduce Synapse (Synergistic Associative Processing Semantic Encoding), a unified memory architecture that transcends static vector similarity. Drawing from cognitive science, Synapse models memory as a dynamic graph where relevance emerges from spreading activation rather than pre-computed links. By integrating lateral inhibition and temporal decay, the system dynamically highlights relevant sub-graphs while filtering interference. We implement a Triple Hybrid Retrieval strategy that fuses geometric embeddings with activation-based graph traversal. Extensive evaluations on the LoCoMo benchmark show that Synapse significantly outperforms state-of-the-art methods in complex temporal and multi-hop reasoning tasks, offering a robust solution to the "Contextual Tunneling" problem.

## 12. SCOPE: Preserving Modality-Specific Cues to Mitigate Modality Laziness in Multimodal Learning

- Authors: Jingfan Yang, Rui Zhang, Liang Hong, Ke Yuan
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.4708946364000184
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1453/
- PDF: https://aclanthology.org/2026.findings-acl.1453.pdf
- Local PDF: pdf/2026-06-28_12_SCOPE_ Preserving Modality-Specific Cues to Mitigate Modality Laziness in Multimodal Learning.pdf

Multimodal learning aims to learn unified multimodal representations from heterogeneous modalities and supports many natural language processing tasks. However, multimodal models often exhibit modality laziness: over-relying on a dominant modality and under-exploiting complementary signals. Existing approaches typically strengthen unimodal training or rebalance modality contributions, but they may still emphasize shared semantics and overlook modality-specific cues. To address this, we propose SCOPE, a unified framework for learning complete multimodal representations, achieving Shared-and-COmplementary cue PrEservation. Firstly, SCOPE uses a mutual information-guided disentanglement module to separate shared semantics from modality-specific cues and mitigate representation collapse. Secondly, SCOPE aligns modalities by enforcing structural consistency between modality-wise semantic graphs, avoiding brittle point-wise matching. Finally, SCOPE performs balanced fusion via structure-aware diffusion attention to integrate shared and complementary cues without feature homogenization. Experiments on four benchmark datasets show that SCOPE consistently outperforms SOTA baselines, achieving up to 27.10% accuracy improvement.

## 13. TopoRAG: Graph-based RAG via Topology-aware Approximate Nearest Neighbor Search

- Authors: Tianhao Wu, Siqiang Luo
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.4548513716558493
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1703/
- PDF: https://aclanthology.org/2026.findings-acl.1703.pdf
- Local PDF: pdf/2026-06-28_13_TopoRAG_ Graph-based RAG via Topology-aware Approximate Nearest Neighbor Search.pdf

Retrieval-augmented generation (RAG) has become a core technique for improving the factuality and reasoning ability of large language models. Recent efforts extend RAG with graph-structured knowledge, enhancing retrieval to capture relational context beyond isolated text chunks. However, many graph-based RAG systems rely on a two-stage pipeline: (i) classical approximate nearest neighbor (ANN) search to identify top- k entities in the embedding space, (ii) heuristic neighbor expansion which augments the retrieved set by traversing immediate neighbors. This design underutilizes graph topology during retrieval and often introduces noisy or high-degree neighbors, leading to suboptimal evidence selection. In this paper, we propose TopoRAG, a retrieval framework that directly integrates structural constraints into ANN search via a diameter-constrained formulation. By selecting entities whose induced subgraph satisfies a diameter bound, TopoRAG enables topology-aware and noise-controlled graph retrieval. Experiments show that our approach consistently improves precision and significantly reduces context redundancy compared to existing methods.

## 14. Beyond Topology: Generative Node Importance Estimation via Structure-Guided Semantic Reasoning

- Authors: Kuofei Fang, Siyan Wu, Yu Guo, Bin Wu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.415418712709613
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.664/
- PDF: https://aclanthology.org/2026.findings-acl.664.pdf
- Local PDF: pdf/2026-06-28_14_Beyond Topology_ Generative Node Importance Estimation via Structure-Guided Semantic Reasoning.pdf

Node Importance Estimation (NIE) in Knowledge Graphs (KGs) aims to quantify the significance of entities, serving as a pivotal instrument for deciphering the latent mechanisms of social dynamics. However, existing methods are often confined to supervised paradigms and rely heavily on topological aggregation, resulting in limited generalization capability. To address these challenges, we propose GenNIE, the first end-to-end generative reasoning framework for NIE. Specifically, GenNIE leverages Large Language Models (LLMs) integrated with topological information to generate precise importance scores for entities in KGs. Furthermore, GenNIE introduces a Global-Structural Graph Perception mechanism to empower the LLMs with holistic graph cognition. Extensive experiments demonstrate the performance superiority of GenNIE and its robust generalization across diverse domains. Our code is available at https://github.com/CoffeyF/GenNIE.git.

## 15. Not All Modalities at Once: Dynamic Dropout and Bidirectional Fusion for Robust Multi-modal Knowledge Graph Completion

- Authors: Jiashun Peng, Fu Zhang, Hongzhi Chen, Jingwei Cheng, Yingsong Ning, Xiaoke Wang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.4101635070564313
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.890/
- PDF: https://aclanthology.org/2026.findings-acl.890.pdf
- Local PDF: pdf/2026-06-28_15_Not All Modalities at Once_ Dynamic Dropout and Bidirectional Fusion for Robust Multi-modal Knowledge Graph Completion.pdf

Multi-modal Knowledge Graph Completion (MKGC) aims to infer missing links in multimodal knowledge graphs by leveraging structured triples together with auxiliary modalities such as text and images. Existing MKGC methods typically train with all modalities available, implicitly assuming consistent complementarity; however, this practice often induces modality dependence and modality competition under heterogeneous noise, which can hinder robust multi-modal fusion and limit overall performance.To address these issues, we propose **MDBGF**, a **M**odality **D**ropout and **B**idirectional **G**ated **F**usion framework for MKGC. MDBGF introduces a *dynamic, probability-based modality dropout* schedule. When the dropout is activated, MDBGF drops either the textual or visual modality during training while always preserving the structural information, encouraging the model to reduce over-reliance on any single auxiliary modality and to learn complementary cues under missing-modality conditions. When the dropout is not activated (i.e., all modalities are present), we further design a *bidirectional gated fusion* mechanism that enables mutual modulation between textual and visual modalities, enhancing cross-modal interaction and flexible fusion. In addition, we propose an *adaptive proportional hybrid negative sampling* strategy to strengthen MDBGF’s discriminative ability on hard negatives. Experiments on three benchmarks show that MDBGF consistently outperforms existing baselines and achieves new state-of-the-art results. Our code is available at https://anonymous.4open.science/r/MDBGF-AHNS.

## 16. Beyond Unimodal Shortcuts: MLLMs as Cross-Modal Reasoners for Grounded Named Entity Recognition

- Authors: Jinlong Ma, Yu Zhang, Xuefeng Bai, Kehai Chen, Yuwei Wang, Zeming Liu, Jun Yu, Min Zhang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.3962319311980327
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.2162/
- PDF: https://aclanthology.org/2026.findings-acl.2162.pdf
- Local PDF: pdf/2026-06-28_16_Beyond Unimodal Shortcuts_ MLLMs as Cross-Modal Reasoners for Grounded Named Entity Recognition.pdf

Grounded Multimodal Named Entity Recognition (GMNER) aims to extract text-based entities, assign them semantic categories, and ground them to corresponding visual regions. In this work, we explore the potential of Multimodal Large Language Models (MLLMs) to perform GMNER in an end-to-end manner, moving beyond their typical role as auxiliary tools within cascaded pipelines.Crucially, our investigation reveals a fundamental challenge: MLLMs exhibit modality bias , including visual bias and textual bias, which stems from their tendency to take unimodal shortcuts rather than rigorous cross-modal verification.To address this, we propose Modality-aware Consistency Reasoning ( MCR ), which enforces structured cross-modal reasoning through Multi-style Reasoning Schema Injection (MRSI) and Constraint-guided Verifiable Optimization (CVO). MRSI transforms abstract constraints into executable reasoning chains, while CVO empowers the model to dynamically align its reasoning trajectories with Group Relative Policy Optimization (GRPO).Experiments on GMNER and visual grounding tasks demonstrate that MCR effectively mitigates modality bias and achieves superior performance compared to existing baselines.

## 17. Structured and Abstractive Reasoning on Multi-modal Relational Knowledge Images

- Authors: Yichi Zhang, Zhuo Chen, Lingbing Guo, Wen Zhang, Huajun Chen
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.395380353519399
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.761/
- PDF: https://aclanthology.org/2026.findings-acl.761.pdf
- Local PDF: pdf/2026-06-28_17_Structured and Abstractive Reasoning on Multi-modal Relational Knowledge Images.pdf

Understanding and reasoning with abstractive information from the visual modality presents significant challenges for current multi-modal large language models (MLLMs). Among the various forms of abstractive information, Multi-Modal Relational Knowledge (MMRK), which represents abstract relational structures between multi-modal entities using node-edge formats, remains largely under-explored. In particular, STructured and Abstractive Reasoning (STAR) on such data has received little attention from the research community. To bridge the dual gaps in large-scale high-quality data and capability enhancement methodologies, this paper makes the following key contributions: (i). An automatic STAR data engine to synthesize images with MMRK to build multi-modal instructions with reliable chain-of-thought thinking for various STAR tasks and (ii). A comprehsive two-stage training framework, accompanied by knowledge-informed GRPO and a suite of evaluation protocols tailored to different STAR tasks. Based upon these contributions, we introduce STAR-64K, a dataset comprising 64K high-quality multi-modal instruction samples, and conduct experiments across 8 open-source MLLMs. Experimental results show that our two-stage enhancement framework enables smaller 3B/7B models to significantly outperform GPT-4o in STAR. Additionally, we provide in-depth analysis regarding the effectiveness of various designs, data transferability, and scalability.

## 18. A Graph Talks, But Who’s Listening? Rethinking Evaluations for Graph-Language Models

- Authors: Soham Petkar, Hari Aakash K, Anirudh Vempati, Akshit Sinha, Ponnurangam Kumaraguru, Chirag Agarwal
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.3818877801882348
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1624/
- PDF: https://aclanthology.org/2026.findings-acl.1624.pdf
- Local PDF: pdf/2026-06-28_18_A Graph Talks, But Who’s Listening_ Rethinking Evaluations for Graph-Language Models.pdf

Recent research has extensively explored the graph-reasoning capabilities of Large Language Models (LLMs) through textual descriptions. However, benchmarks specifically designed for Graph-Language Models (GLMs), which integrate Graph Neural Networks (GNNs) with LLMs, remain significantly underdeveloped. In this work, we first demonstrate that existing GLM evaluations, largely repurposed from unimodal node and edge level tasks, fail to assess true multimodal integration. Our analysis reveals that strong performance on these benchmarks is achievable using textual or structural features in isolation, bypassing the need for joint reasoning. To bridge this gap, we introduce CLEGR (Compositional Language-Graph Reasoning), a benchmark explicitly designed to evaluate multimodal reasoning over graph topology and textual semantics. Evaluation of representative GLMs on CLEGR shows that they exhibit significant performance degradation on CLEGR tasks and unimodal soft-prompted LLMs perform on par with complex multimodal GLMs. These findings collectively highlight limitations in the graph reasoning capabilities of existing GLMs and provide a foundation for advancing the community toward explicit multimodal reasoning involving graph structure and language.

## 19. From Implicit Graph Encoding to Explicit Evidence: A Training-Free LLM Framework for Temporal Knowledge Graph Reasoning

- Authors: Guo Tang, Ke Cheng, Huiming Fan, Heng Chang, Wenxiang Zheng, Xianhao Ou, Junjia Xiang, Ming Liu, Yujun Zhou, Li Lanyu, Bing Qin
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.375955427881767
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.266/
- PDF: https://aclanthology.org/2026.findings-acl.266.pdf
- Local PDF: pdf/2026-06-28_19_From Implicit Graph Encoding to Explicit Evidence_ A Training-Free LLM Framework for Temporal Knowledge Graph Reasoning.pdf

Temporal Knowledge Graph (TKG) forecasting faces significant challenges due to distribution shifts and poor inductive generalization in parametric models. While Large Language Models (LLMs) offer potent semantic reasoning, existing LLM-based approaches struggle with implicit modality alignment and suboptimal graph linearization, failing to capture complex topologies without retraining. To bridge this gap, we propose ExE-LLM, a training-free, test-time adaptive framework that reframes TKG prediction as explicit evidence-driven reasoning. Our core philosophy is to decouple topological calculation from semantic reasoning: a heuristic module translates latent graph signals into natural language evidence, enabling the LLM to perform multi-source judgment. ExE-LLM incorporates a task-aware scheduler for test-time adaptation, a heuristic synthesizer for explicit modality alignment, and a self-diagnosis module for iterative optimization. Extensive experiments on four benchmarks demonstrate that ExE-LLM achieves SOTA performance in inductive settings, significantly outperforming fully trained graph neural networks without updating LLM parameters. The source code is available at https://github.com/JENLISA4EVER/ExE-LLM.

## 20. UniGeM: Unifying Data Selection and Mixing via Geometric Exploration and Mining

- Authors: Changhao Wang, Yunfeiyu, Xinhao Yao, Jiaolong Yang, Lu Yu, Junpeng Fang, Chaobo Li, Riccardo Cantoro, Qing Cui, Jun Zhou
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.3746526446338256
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1037/
- PDF: https://aclanthology.org/2026.findings-acl.1037.pdf
- Local PDF: pdf/2026-06-28_20_UniGeM_ Unifying Data Selection and Mixing via Geometric Exploration and Mining.pdf

The scaling of Large Language Models (LLMs) is increasingly limited by data quality. Most methods handle data mixing and sample selection separately, which can break the structure in code corpora. We introduce UniGeM, a framework that unifies mixing and selection by treating data curation as a manifold approximation problem without training proxy models or relying on external reference datasets. UniGeM operates hierarchically: Macro-Exploration learns mixing weights with stability-based clustering; Micro-Mining filters high-quality instances by their geometric distribution to ensure logical consistency. Validated by training 8B and 16B MoE models on 100B tokens, UniGeM achieves 2.0 × data efficiency over a random baseline and further improves overall performance compared to SOTA methods in reasoning-heavy evaluations and multilingual generalization.

## 21. GLA: Grounding Large Language Models in Molecular Hierarchy for Chemical Understanding

- Authors: Yingxu Li, Jingjie Zeng, Zekun Wang, Hongfei Lin, Liang Yang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.37298053504508
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1515/
- PDF: https://aclanthology.org/2026.findings-acl.1515.pdf
- Local PDF: pdf/2026-06-28_21_GLA_ Grounding Large Language Models in Molecular Hierarchy for Chemical Understanding.pdf

Conventional Euclidean geometries lead to structural distortion and entangle core pharmacophoric identities with peripheral groups. Existing molecule-language models, relying on linear or uniform encodings, often obscure the hierarchical organization of chemical semantics. To address this, we propose Geometric-Language Alignment (GLA), a framework integrating intrinsic molecular topology into large language models. GLA employs a mixed-curvature encoder that adaptively learns geometric representations through a gating mechanism. These representations are aligned with text via a dual-view contrastive objective and injected into a frozen language model. Experiments on cross-modal retrieval, captioning, and property prediction benchmarks show GLA consistently improves performance over baselines, suggesting that modeling geometric heterogeneity enhances the grounding between molecular structure and chemical language.

## 22. GraphLoRA: Structure-Aware Low-Rank Adaptation for Large Language Model Recommendation

- Authors: Lin Mu, Guoji Wang, Li Ni, Lei Sang, Zhize Wu, Peiquan Jin, Yiwen Zhang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.354535010537197
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.645/
- PDF: https://aclanthology.org/2026.findings-acl.645.pdf
- Local PDF: pdf/2026-06-28_22_GraphLoRA_ Structure-Aware Low-Rank Adaptation for Large Language Model Recommendation.pdf

Large Language Models (LLMs) have shown strong potential for recommendation (LLMRec) due to their powerful reasoning and generalization abilities. However, effectively aligning the textual semantics modeled by LLMs with the collaborative signals remains a key challenge. Existing methods either translate collaborative information into textual prompts or inject pre-trained embeddings into the LLM, both of which treat structural information as static input and fail to capture high-order relational dependencies.To bridge this gap, we propose GraphLoRA, a novel framework that generalizes low-rank adaptation from independent to structure-aware propagation. GraphLoRA embeds a trainable graph message-passing network within the low-rank adaptation pathway, enabling structural signals to propagate through the parameter space.This design allows collaborative topology to explicitly guide parameter updates, fostering deep integration between graph-structured and textual semantic information. Extensive experiments on multiple benchmarks demonstrate that GraphLoRA not only outperforms state-of-the-art LLM-based recommendation methods but also achieves superior generalization, effectively balancing structural reasoning capability with computational efficiency.

## 23. ZoomRAG: Hierarchical Random-walk Zooming across Multi-scale Information Graphs for Fast and Accurate RAG

- Authors: Xianming Hu, Jingyang Chen, Bin Tang, Yihe Liu, Yihong Huang, Hongbo Zhao, Nuoyi Chen, Jie Zhang, Ping Li, Kai Zhang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.3527417878949004
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1643/
- PDF: https://aclanthology.org/2026.findings-acl.1643.pdf
- Local PDF: pdf/2026-06-28_23_ZoomRAG_ Hierarchical Random-walk Zooming across Multi-scale Information Graphs for Fast and Accurate RAG.pdf

Retrieval-Augmented Generation is a powerful tool for NLP applications. Yet, it is challenging to encode large knowledge bases as compact offline structures while simultaneously achieving accurate, low-latency online retrieval. We propose **ZoomRAG**, a coarse-to-fine, hierarchical graph inference method to tackle the challenges. ZoomRAG formulates the retrieval task as random walks across multi-scale relational graphs. *At the coarse level*, it constructs a global relational graph and performs a query-initiated random walk to quickly locate a few relevant documents over the entire corpus. *At the finer level*, it “zooms into” the selected documents to capture fine-grained semantic and temporal relations, and conducts a second random walk to pinpoint salient evidence chunks for generation. This coarse-to-fine strategy substantially reduces offline indexing costs and accelerates online retrieval. Moreover, random-walk based topological reasoning over rich, multi-scale relational structures enables ZoomRAG to effectively aggregate multi-hop evidence while suppressing noise. Finally, we address the difficulty of handling concurrent RAG queries by **algorithm-parallel ZoomRAG**. Overall, ZoomRAG avoids building expensive knowledge graphs while achieving 2.2% – 4.9% absolute gains in accuracy over SOTA RAG models, with an average online retrieval latency per-query as low as 0.019 secs by processing hundreds of queries concurrently.

## 24. CLaRE-ty Amid Chaos: Quantifying Representational Entanglement to Predict Ripple Effects in LLM Editing

- Authors: Manit Baser, Alperen Yildiz, Dinil Mon Divakaran, Mohan Gurusamy
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.3286226223999287
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1469/
- PDF: https://aclanthology.org/2026.findings-acl.1469.pdf
- Local PDF: pdf/2026-06-28_24_CLaRE-ty Amid Chaos_ Quantifying Representational Entanglement to Predict Ripple Effects in LLM Editing.pdf

The static knowledge representations of large language models (LLMs) inevitably become outdated or incorrect over time. While model-editing techniques offer a promising solution by modifying a model’s factual associations, they often produce unpredictable ripple effects, which are unintended behavioral changes that propagate even to the hidden space. In this work, we introduce CLaRE, a lightweight representation-level technique to identify where these ripple effects may occur. Unlike prior gradient-based methods, CLaRE quantifies entanglement between facts using forward activations from a single intermediate layer, avoiding costly backward passes. To enable systematic study, we prepare and analyse a corpus of 11,427 facts drawn from three existing datasets. Using CLaRE, we compute large-scale entanglement graphs of this corpus for multiple models, capturing how local edits propagate through representational space. These graphs enable stronger preservation sets for model editing, audit trails, efficient red-teaming, and scalable post-edit evaluation. In comparison to baselines, CLaRE achieves an average of 62.2% improvement in Spearman correlation with ripple effects while being 2.74× faster, and using 2.85× less peak GPU memory. Besides, CLaRE requires only a fraction of the storage needed by the baselines to compute and preserve fact representations. Our entanglement graphs and corpus are available at https://github.com/manitbaser/CLaRE.

## 25. Emergence and Localisation of Semantic Role Circuits in LLMs

- Authors: Nura Aljaafari, Danilo Carvalho, Andre Freitas
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.3235809956930575
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1964/
- PDF: https://aclanthology.org/2026.findings-acl.1964.pdf
- Local PDF: pdf/2026-06-28_25_Emergence and Localisation of Semantic Role Circuits in LLMs.pdf

Despite displaying semantic competence, large language models’ internal mechanisms that ground abstract semantic structure remain insufficiently characterised. To investigate whether and how LLMs develop causally functional representations of semantic roles, we introduce a causal-temporal methodology combining contrastive minimal pairs, edge-attribution circuit discovery, and training-time tracking. Our analysis reveals that LLMs encode semantic roles through highly localised circuits (89–92% attribution within 28 nodes) that emerge gradually via structural refinement rather than phase transitions. These circuits exhibit moderate cross-scale conservation (24–51% component overlap) alongside high spectral similarity, with larger models reusing similar components while rewiring connections. These findings suggest that LLMs form compact, causally isolated mechanisms for abstract semantic structure that exhibit partial transfer across scales and architectures.

## 26. Graph-GRPO: Stabilizing Multi-Agent Topology Learning via Group Relative Policy Optimization

- Authors: Yueyang Cang, Xiaoteng Zhang, Erlu Zhao, Zehua Ji, Yuhang Liu, Yuchen He, Zhiyuan Ning, Chen Yijun, Wenge Que, Li Shi
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.3182058248456063
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1010/
- PDF: https://aclanthology.org/2026.findings-acl.1010.pdf
- Local PDF: pdf/2026-06-28_26_Graph-GRPO_ Stabilizing Multi-Agent Topology Learning via Group Relative Policy Optimization.pdf

Optimizing communication topology is fundamental to the efficiency and effectiveness of Large Language Model (LLM)-based Multi-Agent Systems (MAS). While recent approaches utilize reinforcement learning to dynamically construct task-specific graphs, they typically rely on single-sample policy gradients with absolute rewards (e.g., binary correctness). This paradigm suffers from severe gradient variance and the credit assignment problem: simple queries yield non-informative positive rewards for suboptimal structures, while difficult queries often result in failures that provide no learning signal. To address these challenges, we propose Graph-GRPO, a novel topology optimization framework that integrates Group Relative Policy Optimization. Instead of evaluating a single topology in isolation, Graph-GRPO samples a group of diverse communication graphs for each query and computes the advantage of specific edges based on their relative performance within the group. By normalizing rewards across the sampled group, our method effectively mitigates the noise derived from task difficulty variance and enables fine-grained credit assignment. Extensive experiments on reasoning and code generation benchmarks demonstrate that Graph-GRPO significantly outperforms state-of-the-art baselines, achieving superior training stability and identifying critical communication pathways previously obscured by reward noise.

## 27. Interactive Semantic Parsing with Reinforcement Learning for Knowledge Graph Reasoning

- Authors: Yurun Song, Xiangqing Shen, Jianfei Yu, Rui Xia
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.3150674584843376
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1023/
- PDF: https://aclanthology.org/2026.findings-acl.1023.pdf
- Local PDF: pdf/2026-06-28_27_Interactive Semantic Parsing with Reinforcement Learning for Knowledge Graph Reasoning.pdf

While large language models (LLMs) have achieved remarkable success, their reliability in knowledge-intensive tasks is often compromised by factual hallucinations. Integrating Knowledge Graphs (KGs) addresses this issue; however, existing approaches typically rely on simple graph traversal.This paradigm decouples topological navigation from logical operations (e.g., temporal filtering, aggregation), leading to imprecise retrieval and heavy post-processing burdens.Although semantic parsing offers a solution by grounding reasoning in logical forms, it traditionally suffers from a dependency on scarce supervised annotations.To bridge this gap, we propose Interactive Semantic Parsing, a framework that formulates reasoning as the sequential generation of executable logical clauses. This design allows logical constraints to be dynamically interleaved with graph search, while optimizing via reinforcement learning with only final answer feedback eliminates the need for gold program annotations.To tackle the sparse reward challenge in the vast symbolic space, we introduce a distance-aware process reward to evaluate intermediate steps based on their topological proximity to the answer.Experimental results on WebQSP and CWQ demonstrate that our method achieves state-of-the-art performance, particularly on complex queries, validating the effectiveness of our dense reward signal in enabling robust reasoning without supervision.Our code is available at https://github.com/NUSTM/ISP-KGR.

## 28. GALA: Geometric Data Selection with Strategic Prospecting for Large Language Model Self-training

- Authors: Zhongwei Xie, Ruihao Liao, Zimo Wang, Chong Chen, Xian-Sheng Hua, Xiao Luo
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.312645439131577
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.500/
- PDF: https://aclanthology.org/2026.findings-acl.500.pdf
- Local PDF: pdf/2026-06-28_28_GALA_ Geometric Data Selection with Strategic Prospecting for Large Language Model Self-training.pdf

Self-training has emerged as a promising direction for autonomously improving large language models (LLMs). Existing approaches typically adopt a generate-and-filter paradigm based on rejection sampling, which could suffer from inefficiency and low-quality reasoning paths. Towards this end, this paper proposes a novel framework named ̲Geometric D ̲ata Se ̲lection with Str ̲ategic Prospecting (GALA) for LLM self-training. The core of our GALA is to identify diverse and informative samples from redundant data and exploit them more strategically. In particular, our proposed GALA first conducts clustering on latent sentence embeddings and then selects an anchor sample from each cluster based on the geometric distance to reduce data redundancy. To further exploit these samples, we conduct strategic brainstorming and reflection for high-quality reasoning trajectory prospecting. In addition, we introduce a lightweight dynamic validation module to validate the reliability of mini-batches to ensure the overall quality of the data. Extensive experiments on various benchmarks validate the effectiveness of the proposed GALA against several competing baselines.

## 29. CodeBind: Decoupled Representation Learning for Multimodal Alignment with Unified Compositional Codebook

- Authors: Zeyu Chen, Jie Li, Kai Han
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.3098241733046283
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.987/
- PDF: https://aclanthology.org/2026.findings-acl.987.pdf
- Local PDF: pdf/2026-06-28_29_CodeBind_ Decoupled Representation Learning for Multimodal Alignment with Unified Compositional Codebook.pdf

Multimodal representation alignment is pivotal for large language models and robotics. Traditional methods are often hindered by cross-modal information discrepancies and data scarcity, leading to suboptimal alignment spaces that overlook modality-unique features. We propose CodeBind, a framework that optimizes multimodal representation spaces through a modality-shared-specific codebook design. By incrementally aligning target and bridging modalities, CodeBind bypasses the need for fully paired data. Unlike traditional hard alignment, CodeBind decomposes features into shared components for semantic consistency and specific components for modality-unique details. This design utilizes a compositional vector quantization scheme, where a shared codebook bridges modality gaps and modality-specific codebooks mitigate representation bias by preventing dominant modalities from overshadowing others. Validated across nine modalities (text, image, video, audio, depth, thermal, tactile, 3D point cloud, EEG), CodeBind achieves state-of-the-art performance in multimodal classification and retrieval tasks. Project page: https://visual-ai.github.io/codebind

## 30. MotifAgent: Learning Molecular Assembly through Multi-Agent Collaboration for Chemical Language Understanding

- Authors: Jinjia Feng, Wenda Wang, Zhewei Wei
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.3048644981045863
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.2023/
- PDF: https://aclanthology.org/2026.findings-acl.2023.pdf
- Local PDF: pdf/2026-06-28_30_MotifAgent_ Learning Molecular Assembly through Multi-Agent Collaboration for Chemical Language Understanding.pdf

Large Language Models (LLMs) have shown great potential in molecular understanding by aligning molecular representations with text. However, existing approaches remain limited to static motif recognition without comprehending the generative principles—the connection rules governing how motifs assemble into valid topological structures. To address this challenge, we introduce **MotifAgent**, a multi-agent reinforcement learning framework inspired by emergent collective intelligence. We formulate molecular assembly as a collaborative problem where each motif is represented by an agent sharing a common LLM backbone, learning connection rules through explicit inter-motif negotiation rather than implicit sequence memorization. Key innovations include: (1) dynamic inter-agent negotiation for modeling motif connections; (2) Set-based Behavioral Cloning for learning multiple topologically equivalent assembly paths; (3) topology-aware reward shaping with MAPPO to maintain chemical validity while optimizing target properties. Extensive experiments demonstrate that MotifAgent achieves state-of-the-art performance across molecular property prediction, description generation, and reaction prediction tasks, with our generalist model surpassing specialized expert models.

## 31. MCLE-Mol: Empowering LLM with Molecular Comprehension and Low-Cost Continual Evolution for Interpretable Property Prediction

- Authors: Zhili Pu, Lantian Zhang, Hao Duan, Zhixing Zhang, Keyun Zhu, Yongqi Fan, Ruihui Hou, Tong Ruan, Yun Tang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.2991075058160724
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.262/
- PDF: https://aclanthology.org/2026.findings-acl.262.pdf
- Local PDF: pdf/2026-06-28_31_MCLE-Mol_ Empowering LLM with Molecular Comprehension and Low-Cost Continual Evolution for Interpretable Property Predic.pdf

Large language models (LLMs) offer a new paradigm for molecular property prediction (MPP), yet a semantic gap between natural language and molecular representations limits LLMs’ ability to capture structure–activity relationships (SAR). Recent approaches have explored injecting structure-level information into LLMs, primarily modeling associations based on statistical regularities. However, these methods are prone to misinterpreting coincidental associations as general principles, imposing a bottleneck on predictive performance. To tackle the challenges above, we propose MCLE-Mol, an ML–LLM–Rule collaborative framework for MPP. It bridges the semantic gap by injecting ML-derived substructure attribution values into LLMs, utilizing Context-Calibrated Substructure Attribution Rules (CCSAR) to calibrate these attributions under specific chemical contexts to mitigate such misinterpretation. In addition, MCLE-Mol introduces a low-cost continual evolution strategy that updates CCSAR with frozen model parameters to adapt to dynamic chemical spaces. Experiments on multiple benchmark datasets demonstrate that MCLE-Mol outperforms all baselines, successfully resolving the trade-off between predictive performance and interpretability.

## 32. TagRAG: Tag-guided Hierarchical Knowledge Graph Retrieval-Augmented Generation

- Authors: Wenbiao Tao, Xinyuan Li, Yunshi Lan, Weining Qian
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.2875892731239507
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.321/
- PDF: https://aclanthology.org/2026.findings-acl.321.pdf
- Local PDF: pdf/2026-06-28_32_TagRAG_ Tag-guided Hierarchical Knowledge Graph Retrieval-Augmented Generation.pdf

Retrieval-Augmented Generation enhances language models by retrieving external knowledge to support informed and grounded responses. However, traditional RAG methods rely on fragment-level retrieval, limiting their ability to address query-focused summarization queries. GraphRAG introduces a graph-based paradigm for global knowledge reasoning, yet suffers from inefficiencies in information extraction, costly resource consumption, and poor adaptability to incremental updates. To overcome these limitations, we propose TagRAG, a tag-guided hierarchical knowledge graph RAG framework designed for efficient global reasoning and scalable graph maintenance. TagRAG introduces two key components: (1) Tag Knowledge Graph Construction, which extracts object tags and their relationships from documents and organizes them into hierarchical domain tag chains for structured knowledge representation, and (2) Tag-Guided Retrieval-Augmented Generation, which retrieves domain-centric tag chains to localize and synthesize relevant knowledge during inference. This design significantly adapts to smaller language models, improves retrieval granularity, and supports efficient knowledge increment. Extensive experiments on UltraDomain datasets spanning Agriculture, Computer Science, Law, and cross-domain settings demonstrate that TagRAG achieves an average win rate of 78.36% against baselines while maintaining about 14.6x construction and 1.9x retrieval efficiency compared with GraphRAG.

## 33. Reasoning-Based Refinement of Unsupervised Text Clusters with LLMs

- Authors: Tunazzina Islam
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.270526571334006
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.482/
- PDF: https://aclanthology.org/2026.findings-acl.482.pdf
- Local PDF: pdf/2026-06-28_33_Reasoning-Based Refinement of Unsupervised Text Clusters with LLMs.pdf

Unsupervised methods are widely used to induce latent semantic structure from large text collections, yet their outputs often contain incoherent, redundant, or poorly grounded clusters that are difficult to validate without labeled data. We propose a **reasoning-based refinement framework** that leverages large language models (LLMs) not as embedding generators, but as semantic judges that validate and restructure the outputs of arbitrary unsupervised clustering algorithms. Our framework introduces three reasoning stages: (i) **coherence verification**, where LLMs assess whether cluster summaries are supported by their member texts; (ii) **redundancy adjudication**, where candidate clusters are merged or rejected based on semantic overlap; and (iii) **label grounding**, where clusters are assigned interpretable labels through a two-stage process that generates and consolidates semantically similar labels in a fully unsupervised manner. This design decouples representation learning from structural validation and mitigates the common failure modes of embedding-only approaches. We evaluate the framework in real-world social media corpora from two platforms with distinct interaction models, demonstrating consistent improvements in cluster coherence and human-aligned labeling quality over classical topic models and recent representation-based baselines. Human evaluation shows strong agreement with LLM-generated labels, despite the absence of gold-standard annotations. We further conduct robustness analysis under matched temporal and volume conditions to assess cross-platform stability. Beyond empirical gains, our results suggest that LLM-based reasoning can serve as a general mechanism for validating and refining unsupervised semantic structure, enabling more reliable and interpretable analysis of large text collections without supervision.

## 34. LANTERN in the Event Stream: Training-Free Temporal Knowledge Graph Forecasting by Balancing Inertia and Shifts

- Authors: Chengyuan Jin, Ao Chang, Daojian Zeng, Wenhao Teng, Xiangwen Liao, Kang Liu, Jun Zhao, Yubo Chen
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.2563358266860742
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.559/
- PDF: https://aclanthology.org/2026.findings-acl.559.pdf
- Local PDF: pdf/2026-06-28_34_LANTERN in the Event Stream_ Training-Free Temporal Knowledge Graph Forecasting by Balancing Inertia and Shifts.pdf

Temporal knowledge graph forecasting(TKGF) asks a model to rank the mostplausible future entity for a query such as(s, r, ?, t) from historical events. Recenttraining-free methods use large languagemodels (LLMs) for this task, but their accuracydepends heavily on which past events areshown in the prompt under a tight contextbudget. We present LANTERN, a training-freeprompting framework that addresses thisbottleneck by combining two complementaryviews of history: a long-window strengthscore for stable interaction patterns anda short-window novelty score for suddenchanges. LANTERN first filters unhelpfulevents, then selects a compact evidence setwith Pareto-greedy selection, and finally addsone structure-aware analogical demonstration.Across ICEWS14, ICEWS05-15, ICEWS18,and GDELT, LANTERN consistently outperforms the state-of-the-art training-free baselineAnRe under the same backbone and 2-hopcandidate protocol, improving Hits@1 by upto 2.5 points and MRR by up to 1.2 points.

## 35. CSMCIR: CoT-Enhanced Symmetric Alignment with Memory Bank for Composed Image Retrieval

- Authors: Zhipeng Qian, Zihan Liang, Yufei Ma, Ben Chen, Huangyu Dai, Yiwei Ma, Jiayi Ji, Chenyi Lei, Han Li, Xiaoshuai Sun
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.254506229788184
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.216/
- PDF: https://aclanthology.org/2026.findings-acl.216.pdf
- Local PDF: pdf/2026-06-28_35_CSMCIR_ CoT-Enhanced Symmetric Alignment with Memory Bank for Composed Image Retrieval.pdf

Composed Image Retrieval (CIR) enables users to search for target images using both a reference image and manipulation text, offering substantial advantages over single-modality retrieval systems. However, existing CIR methods suffer from representation space fragmentation: queries and targets comprise heterogeneous modalities and are processed by distinct encoders, forcing models to bridge misaligned representation spaces only through post-hoc alignment, which fundamentally limits retrieval performance. As evidenced by t-SNE visualization in Fig.(a), this architectural asymmetry manifests as three distinct, well-separated clusters in the feature space, directly demonstrating how heterogeneous modalities create fundamentally misaligned representation spaces from initialization. In this work, we propose CSMCIR, a unified representation framework that achieves efficient query-target alignment through three synergistic components. First, we introduce a Multi-level Chain-of-Thought (MCoT) prompting strategy that guides Multimodal Large Language Models to generate discriminative, semantically compatible captions for target images, establishing modal symmetry. Building upon this, we design a symmetric dual-tower architecture where both query and target sides utilize the identical shared-parameter Q-Former for cross-modal encoding, ensuring consistent feature representations and further reducing the alignment gap. Finally, this architectural symmetry enables an entropy-based, temporally dynamic Memory Bank strategy that provides high-quality negative samples while maintaining consistency with the evolving model state. Extensive experiments on four benchmark datasets demonstrate that our CSMCIR achieves state-of-the-art performance with superior training efficiency. Comprehensive ablation studies further validate the effectiveness of each proposed component.

## 36. CANDICE: Agentic Causal Disentanglement with Class Conditional Knowledge Integration for Long Tailed Domain Generalization

- Authors: Midhat Urooj, Ayan Banerjee, Sandeep Gupta
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.251145796140099
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.2018/
- PDF: https://aclanthology.org/2026.findings-acl.2018.pdf
- Local PDF: pdf/2026-06-28_36_CANDICE_ Agentic Causal Disentanglement with Class Conditional Knowledge Integration for Long Tailed Domain Generalizati.pdf

Deep learning models deployed in clinical settings face two major challenges: domain generalization (DG) and long-tailed (LT) recognition. DG requires learning domain-invariant features to ensure robustness across heterogeneous acquisition protocols and patient populations. However, we identify a fundamental trade-off: objectives that enforce domain invariance often suppress class-discriminative signals essential for long-tailed recognition.To address this, we propose the Agentic Causal Disentanglement (CANDICE) Framework , a modular architecture that integrates explicit clinical expertise from sonographers, radiologists, and specialists as a form of causal intervention. The framework combines clinical reasoning, causal representation learning, and automated pipeline construction to disentangle domain-invariant and class-discriminative features. By incorporating domain-specific causal knowledge, it effectively decouples the objectives of DG and LT learning. We evaluate CANDICE on 10 diverse medical imaging datasets spanning four modalities. The framework achieves an average performance improvement of 10.3% across both multi-domain and in-domain long-tailed tasks, demonstrating its effectiveness in handling distribution shifts while preserving minority class performance.

## 37. From Attenuation to Attention: Variational Information Flow Manipulation for Fine-Grained Visual Perception

- Authors: Jilong Zhu, Yang Feng
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.2423857936012226
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.927/
- PDF: https://aclanthology.org/2026.findings-acl.927.pdf
- Local PDF: pdf/2026-06-28_37_From Attenuation to Attention_ Variational Information Flow Manipulation for Fine-Grained Visual Perception.pdf

While Multimodal Large Language Models (MLLMs) have demonstrated impressive capabilities in general visual understanding, they frequently falter in fine-grained perception tasks that require identifying tiny objects or discerning subtle visual relationships. We attribute this limitation to Visual Attenuation: a phenomenon where sparse fine-grained visual signals are prematurely suppressed or diluted by dominant textual tokens during network propagation, resulting in a “loss of focus” during the deep-level decision-making process. Existing input-centric solutions fail to fundamentally reverse this intrinsic mechanism of information loss. To address this challenge, we propose the Variational Information Flow (VIF) framework. Adopting a probabilistic perspective, VIF leverages a Conditional Variational Autoencoder (CVAE) to model the visual saliency relevant to the question-answer pair as a latent distribution. As a plug-and-play module, VIF can be integrated into existing architectures. Extensive evaluations across diverse benchmarks—covering General VQA, fine-grained perception, and visual grounding—demonstrate that VIF yields competitive improvements over previous methods, validating its effectiveness in enhancing the fine-grained perception of MLLMs. Codes are available at https://github.com/ictnlp/VIF.

## 38. RouterHGC: Optimized Router for LLM-based Multi-Agent Systems via Heterogeneous Graph Contrastive Learning

- Authors: Yitao Xiao, Shaoyong Guo, Guoming Yang, Qingnan Wang, Yinlin Ren, Xuesong Qiu, Qi Feng
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.2356920213160367
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1589/
- PDF: https://aclanthology.org/2026.findings-acl.1589.pdf
- Local PDF: pdf/2026-06-28_38_RouterHGC_ Optimized Router for LLM-based Multi-Agent Systems via Heterogeneous Graph Contrastive Learning.pdf

Leveraging powerful planning and reasoning capabilities, Large Language Models (LLMs)-driven Multi-Agent Systems (MAS) have demonstrated remarkable scalability and generalizability across complex tasks. However, dynamically routing the optimal combination of agents and collaboration modes for a given query to balance performance and cost remains challenging. To address the limitation of prior work, which focuses on single-agent settings and overlooks collaborative structures and role assignment in MAS, we propose RouterHGC, the first heterogeneous graph contrastive learning framework for MAS routing. We formalize routing as node selection through edge-weight prediction on a heterogeneous graph whose node types include user queries, collaboration modes, agent roles, and LLMs, with message passing capturing their high-order dependencies. We further design a novel global–local contrastive loss function to jointly optimize graph-level representations and edge-level selections, pulling each query graph toward high-performing positives while pushing it away from underperforming or costly negatives. Experiments on five public datasets covering mathematical reasoning, code generation, and knowledge question answering show that RouterHGC outperforms the best single LLM and baselines, achieving 0.80%–6.17% accuracy gains on MATH and HotpotQA while reducing inference cost by 27.40%.

## 39. Breaking the Static Graph: Context-Aware Traversal for Graph-Based RAG

- Authors: Kwun Hang Lau, Fangyuan Zhang, Boyu Ruan, Yingli Zhou, Qintian Guo, Ruiyuan Zhang, Xiaofang Zhou
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.23465958438395
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.290/
- PDF: https://aclanthology.org/2026.findings-acl.290.pdf
- Local PDF: pdf/2026-06-28_39_Breaking the Static Graph_ Context-Aware Traversal for Graph-Based RAG.pdf

Recent advances in Retrieval-Augmented Generation (RAG) have shifted from simple vector similarity to structure-aware approaches like HippoRAG, which leverage Knowledge Graphs (KGs) and Personalized PageRank (PPR) to capture multi-hop dependencies. However, these methods suffer from a "Static Graph Fallacy": fixed transition probabilities set during indexing ignore query-dependent edgerelevance, causing semantic drift where random walks are diverted into high-degree "hub" nodes before reaching critical evidence. Models often achieve high partial recall but fail to retrieve the complete evidence chain for multi-hop queries. To address this, we propose CatRAG, Context-Aware Traversal for robust RAG, which builds on the HippoRAG 2 and transforms the static KG into a query-adaptive navigation structure. CatRAG steers the random walk via three mechanisms: (1) Symbolic Anchoring, injecting weak entity constraints to regularize the random walk; (2) QueryAware Dynamic Edge Weighting, dynamically modulating graph structure to prune irrelevant paths and amplify query-aligned ones; and (3) Key-Fact Passage Weight Enhancement, a cost-efficient bias anchoring the walk to key evidence. Experiments across multi-hop benchmarks show that CatRAG outperforms state-of-the-art baselines. While standard Recall gains are modest, CatRAG achieves substantial improvements in reasoning completeness—the capacity to recover entire evidence chains without gaps. These results reveal that CatRAG effectively bridges the gap between retrieving partial context and enabling fully grounded reasoning. Resources are available at https://github.com/kwunhang/CatRAG.

## 40. Omni-R1: Towards the Unified Generative Paradigm for Multimodal Reasoning

- Authors: Dongjie Cheng, Yongqi Li, Zhixin Ma, Hongru Cai, Yupeng Hu, Wenjie Wang, Liqiang Nie, Wenjie Li
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.233782440978853
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1937/
- PDF: https://aclanthology.org/2026.findings-acl.1937.pdf
- Local PDF: pdf/2026-06-28_40_Omni-R1_ Towards the Unified Generative Paradigm for Multimodal Reasoning.pdf

Multimodal Large Language Models (MLLMs) are making significant progress in multimodal reasoning. Early approaches focus on pure text-based reasoning. More recent studies have incorporated multimodal information into the reasoning steps; however, they often follow a single task-specific reasoning pattern, which limits their generalizability across various multimodal tasks. In fact, there are numerous multimodal tasks requiring diverse reasoning skills, such as zooming in on a specific region or marking an object within an image. To address this, we propose unified generative multimodal reasoning, which unifies diverse multimodal reasoning skills by generating intermediate images during the reasoning process. We instantiate this paradigm with Omni-R1, a two-stage SFT+RL framework featuring perception alignment loss and perception reward, thereby enabling functional image generation. Additionally, we introduce Omni-R1-Zero, which eliminates the need for multimodal annotations by bootstrapping step-wise visualizations from text-only reasoning data. Empirical results show that Omni-R1 achieves unified generative reasoning across a wide range of multimodal tasks, and Omni-R1-Zero can match or even surpass Omni-R1 on average, suggesting a promising direction for generative multimodal reasoning. The code and checkpoints are attached for reproducibility and subsequent open release.

## 41. E2E-GMNER: End-to-End Generative Grounded Multimodal Named Entity Recognition

- Authors: Meng Zhang, Jinzhong Ning, Xiaolong Wu, Hongfei Lin, Yijia Zhang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.2176114845777173
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1127/
- PDF: https://aclanthology.org/2026.findings-acl.1127.pdf
- Local PDF: pdf/2026-06-28_41_E2E-GMNER_ End-to-End Generative Grounded Multimodal Named Entity Recognition.pdf

Grounded Multimodal Named Entity Recognition (GMNER) aims to jointly identify named entity mentions in text, predict their semantic types, and ground each entity to a corresponding visual region in an associated image. Existing approaches predominantly adopt pipeline-based architectures that decouple textual entity recognition and visual grounding, leading to error accumulation and suboptimal joint optimization. In this paper, we propose E2E-GMNER, a fully end-to-end generative framework that unifies entity recognition, semantic typing, visual grounding, and implicit knowledge reasoning within a single multimodal large language model. We formulate GMNER as an instruction-tuned conditional generation task and incorporate chain-of-thought reasoning to enable the model to adaptively determine when visual evidence or background knowledge is informative, reducing reliance on noisy cues. To further address the instability of generative bounding box prediction, we introduce Gaussian Risk-Aware Box Perturbation (GRBP), which replaces hard box supervision with probabilistically perturbed soft targets to improve robustness against annotation noise and discretization errors. Extensive experiments on the Twitter-GMNER and Twitter-FMNERG benchmarks demonstrate that E2E-GMNER achieves highly competitive performance compared with state of the art methods, validating the effectiveness of unified end-to-end optimization and noise-aware grounding supervision.

## 42. MemORAI: Memory Organization and Retrieval via Adaptive Graph Intelligence for LLM Conversational Agents

- Authors: Hung Pham Van, Nguyen Manh Hieu, Khang Pham Tran Tuan, Nam Le Hai, Linh Ngo Van, Nguyen Thi Ngoc Diep, Trung Le
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.2152699786747863
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1408/
- PDF: https://aclanthology.org/2026.findings-acl.1408.pdf
- Local PDF: pdf/2026-06-28_42_MemORAI_ Memory Organization and Retrieval via Adaptive Graph Intelligence for LLM Conversational Agents.pdf

Large Language Models (LLMs) lack persistent memory for long-term personalized conversations. Existing graph-based memory systems suffer from information dilution, absent provenance tracking, and uniform retrieval that ignores query context. We introduce MemORAI (Memory Organization and Retrieval via Adaptive Graph Intelligence), a framework that integrates three innovations: selective memory filtering with dual-layer compression to retain user-persona-relevant content, a provenance-enriched multi-relational graph tracking factual origins at the turn level, and query-adaptive subgraph retrieval with Dynamic Weighted PageRank that applies query-conditioned edge weighting. Evaluated on LOCOMO and LongMemEval benchmarks, MemORAI achieves state-of-the-art performance in memory retrieval and personalized response generation, demonstrating that selective storage, enriched representation, and adaptive retrieval are essential for coherent, personalized LLM agents.

## 43. Generative Giants, Retrieval Weaklings: Why do Multimodal Large Language Models Fail at Multimodal Retrieval?

- Authors: Hengyi Feng, Zeang Sheng, Meiyi Qiang, Yang Li, Wentao Zhang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.2114314395460113
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.781/
- PDF: https://aclanthology.org/2026.findings-acl.781.pdf
- Local PDF: pdf/2026-06-28_43_Generative Giants, Retrieval Weaklings_ Why do Multimodal Large Language Models Fail at Multimodal Retrieval.pdf

Despite the remarkable success of multimodal large language models (MLLMs) in generative tasks, we observe that they exhibit a counterintuitive deficiency in the zero-shot multimodal retrieval task. In this work, we investigate the underlying mechanisms that hinder MLLMs from being effective retrievers. With the help of sparse autoencoders (SAEs), we decompose MLLM output representations into interpretable semantic concepts to probe their intrinsic behavior. Our analysis reveals that the representation space of MLLMs is overwhelmingly dominated by textual semantics; and the visual semantics essential for multimodal retrieval only constitute a small portion. We find that this imbalance is compounded by the heavy focus of MLLMs on bridging image-text modalities, which facilitates generation but homogenizes embeddings and finally diminishes the discriminative power required for multimodal retrieval. We further discover that the specific feature components that contribute most to the similarity computations of MLLMs are actually distractors that greatly reduce retrieval performance. Building on these insights, we propose , a test-time adaptation approach that applies a whitening transformation to adjust the geometry of MLLM representation spaces. Empirical results show that this simple intervention consistently improves zero-shot multimodal retrieval performance across diverse MLLMs without fine-tuning efforts.

## 44. G-HiRel: Enhancing the Adaption to Knowledge Updating for Large Language Model Reasoning

- Authors: Yudai Pan, Jiajie Hong, Tianzhe Zhao, Lingyun Song, Lingling Zhang, Yixin Chen, Xuequn Shang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.203604105828984
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1561/
- PDF: https://aclanthology.org/2026.findings-acl.1561.pdf
- Local PDF: pdf/2026-06-28_44_G-HiRel_ Enhancing the Adaption to Knowledge Updating for Large Language Model Reasoning.pdf

Large language models (LLMs) have achieved good performance in multiple reasoning tasks. However, they are limited to adapt the rapid knowledge updates in the real-world scenario without retraining the entire LLM or modifying the model weights. Excluding these consuming methods, knowledge graphs (KGs) are used as external memory under knowledge updating because of their structural knowledge and efficient updating ability, which is yet limited by the gap between structural KG and LLM, and the deficient entity-independent semantics. To this end, we propose an LLM reasoning framework with hierarchical relational retrieval for large-scale knowledge updating, named G-HiRel. To integrate the structural edited KG into continuous LLMs, G-HiRel generates hierarchical instructions based on natural language questions. In order to handle the knowledge inconsistency between the KG and LLM and obtain the entity independence, G-HiRel utilizes a designed hierarchical relational retrieval for relational path candidates, which are selected by a designed semantics-based strategy. Finally, top entity-independent relational paths are instantiated and integrated into LLMs to generate the answer, in order to verify the reasoning performance under knowledge edits. Extensive experiments of G-HiRel on three benchmarks show that G-HiRel achieves superiority in terms of accuracy and interpretability. The code of G-HiRel is available at the link: https://github.com/HJJ-designed/G-HiRel.

## 45. Beyond Chunks and Graphs: Retrieval-Augmented Generation through Triplet-Driven Thinking

- Authors: Shengbo Gong, Xianfeng Tang, Qi He, Carl Yang, Wei Jin
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.197347101946236
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1310/
- PDF: https://aclanthology.org/2026.findings-acl.1310.pdf
- Local PDF: pdf/2026-06-28_45_Beyond Chunks and Graphs_ Retrieval-Augmented Generation through Triplet-Driven Thinking.pdf

Retrieval-augmented generation (RAG) is critical for reducing hallucinations and incorporating external knowledge into Large Language Models (LLMs). However, advanced RAG systems face a trade-off between performance and efficiency. Multi-round RAG approaches achieve strong reasoning but incur excessive LLM calls and token costs, while Graph RAG methods suffer from computationally expensive, error-prone graph construction and retrieval redundancy. To address these challenges, we propose T 2 RAG, a novel framework that operates on a simple, graph-free knowledge base of atomic triplets. T 2 RAG leverages an LLM to decompose questions into searchable triplets with placeholders, which it then iteratively resolves by retrieving evidence from the triplet database. Empirical results show that T 2 RAG significantly outperforms state-of-the-art multi-round and Graph RAG methods, achieving an average performance gain of up to 11% across six datasets while reducing retrieval costs by up to 45%.

## 46. RouteRAG: Efficient Retrieval-Augmented Generation from Text and Graph via Reinforcement Learning

- Authors: Yucan Guo, Miao Su, Saiping Guan, Zihao Sun, Xiaolong Jin, Jiafeng Guo, Xueqi Cheng
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.1907678912101876
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1502/
- PDF: https://aclanthology.org/2026.findings-acl.1502.pdf
- Local PDF: pdf/2026-06-28_46_RouteRAG_ Efficient Retrieval-Augmented Generation from Text and Graph via Reinforcement Learning.pdf

Retrieval-Augmented Generation (RAG) integrates non-parametric knowledge into Large Language Models (LLMs), typically from unstructured texts and structured graphs. While recent progress has advanced text-based RAG to multi-turn reasoning through Reinforcement Learning (RL), extending these advances to hybrid retrieval introduces additional challenges. Existing graph-based or hybrid systems typically depend on fixed or handcrafted retrieval pipelines, lacking the ability to integrate supplementary evidence as reasoning unfolds. Besides, while graph evidence provides relational structures crucial for multi-hop reasoning, it is substantially more expensive to retrieve. To address these limitations, we introduce RouteRAG, an RL-based framework that enables LLMs to perform multi-turn and adaptive graph-text hybrid RAG. RouteRAG jointly optimizes the entire generation process via RL, allowing the model to learn when to reason, what to retrieve from either texts or graphs, and when to produce final answers, all within a unified generation policy. To guide this learning process, we design a two-stage training framework that accounts for both task outcome and retrieval efficiency, enabling the model to exploit hybrid evidence while avoiding unnecessary retrieval overhead. Experimental results across five question answering benchmarks demonstrate that RouteRAG significantly outperforms existing RAG baselines, highlighting the benefits of end-to-end RL in supporting adaptive and efficient retrieval for complex reasoning.

## 47. AdaptiveK: Complexity-Driven Sparse Autoencoders for Interpretable Language Model Representations

- Authors: Yifei Yao, Hanrong Zhang, Mengnan Du
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.1891091275938606
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1187/
- PDF: https://aclanthology.org/2026.findings-acl.1187.pdf
- Local PDF: pdf/2026-06-28_47_AdaptiveK_ Complexity-Driven Sparse Autoencoders for Interpretable Language Model Representations.pdf

Understanding the internal representations of large language models (LLMs) remains a central challenge for interpretability research. Sparse autoencoders (SAEs) offer a promising solution by decomposing activations into interpretable features, but existing approaches rely on fixed sparsity constraints that fail to account for input complexity. We propose AdaptiveK SAE (Adaptive Top K Sparse Autoencoders), a novel framework that dynamically adjusts sparsity levels based on the semantic complexity of each input. Leveraging linear probes, we demonstrate that context complexity is linearly encoded in LLM representations, and we use this signal to guide feature allocation during training. Experiments across ten language models demonstrate that this complexity-driven adaptation outperforms fixed-sparsity approaches on reconstruction fidelity, explained variance, cosine similarity and interpretability metrics while eliminating the burden of extensive hyperparameter tuning. Our code is available at: https://github.com/hiyukie/adaptiveK.

## 48. Spatial co-expression and cell-cell communication inference from spatially resolved transcriptomics with CONCISE

- Authors: Zhao, J., Shan, X., Wang, G., Chu, T., Lin, C., Chang, R., Zhao, H.
- Source: biorxiv
- Venue type: preprint
- Journal: biorxiv
- Publication status: preprint
- Publication date: 2026-06-28
- DOI: 10.64898/2026.06.22.733860
- Categories: bioinformatics
- Relevance: 3.1854056366972565
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://www.biorxiv.org/content/10.64898/2026.06.22.733860v1.full.pdf
- PDF: https://www.biorxiv.org/content/10.64898/2026.06.22.733860v1.full.pdf
- Local PDF: Not downloaded

Cell-cell communication is fundamental to tissue organization, homeostasis, and disease progression. Recent advances in spatial transcriptomics provide unprecedented opportunities to systematically characterize ligand-receptor interactions directly within intact tissues. However, robust inference of spatial ligand-receptor interactions remains challenging because intrinsic features of spatial transcriptomics data, including spatial autocorrelation, variation in total molecular counts, and measurement errors, can induce spurious spatial co-expression and lead to inflated false-positive results. Most existing methods do not adequately account for these confounding factors, limiting the reliability of inferred cellular communication. Here, we present CONCISE, a statistical method for spatially constrained co-expression and ligand-receptor interaction inference that jointly models spatial autocorrelation, variation in total molecular counts, measurement errors, and spatial proximity constraints. CONCISE combines efficient moment-based parameter estimation with analytical hypothesis testing, enabling fast and statistically rigorous inference without restrictive distributional assumptions. Through extensive simulations, real-data permutation experiments, and biologically motivated negative-control analyses across different spatial transcriptomics platforms, we show that most existing methods presented inflated false-positive rates, whereas CONCISE achieved well-calibrated inference, robust false-positive control, and improved detection power. Application of CONCISE to high-resolution MERFISH and CosMx datasets from intestinal inflammation and non-small cell lung cancer further highlights its biological utility in disease contexts. CONCISE uncovered inflammation-associated fibroblast-specific interactions during intestinal inflammation and delineated complex tumor-immune and tumor-stromal signaling networks within the tumor microenvironment.

## 49. A Herd of Language Models Makes a Better Zero-shot Annotator for Clinical Named Entity Recognition

- Authors: Seiji Shimizu, Shoko Wakamiya, Eiji Aramaki
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.1844652639178923
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.599/
- PDF: https://aclanthology.org/2026.findings-acl.599.pdf
- Local PDF: pdf/2026-06-28_49_A Herd of Language Models Makes a Better Zero-shot Annotator for Clinical Named Entity Recognition.pdf

Clinical named entity recognition (NER) remains difficult to scale due to the high cost of manual annotation. Although large language models (LLMs) enable zero-shot annotation, their performance on clinical NER is still limited. To this end, we improve the annotation quality by aggregating annotations from *a herd of diverse LLMs*, including general-purpose, medically adapted, and NER-specialized models. A key challenge in this multi-LLM setting is effectively leveraging entities extracted by only a minority of models: although they account for a substantial portion of true positives, they are heavily intermixed with noise. To address this, we introduce **MARY**, a label-modeling method for **M**ulti-LLM **A**nnotation using **R**epresentation learning to capture contextual similarit**Y**. During aggregation, MARY selectively incorporates minority-extracted entities whose contexts are similar to those of majority-extracted entities, yielding more reliable and comprehensive annotations. Experimental results show that MARY improves the average F1 score by 8.6% over vanilla zero-shot baselines while reducing annotation costs.

## 50. Risk-Controlled Event-Driven Cascading Updates for Knowledge Graph Consistency Restoration

- Authors: Bo Ni, Qinwen Ge, Haowei Fu, Ryan A. Rossi, Xiaorui Liu, Jiejun Xu, Tyler Derr
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.181164253680382
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.2111/
- PDF: https://aclanthology.org/2026.findings-acl.2111.pdf
- Local PDF: pdf/2026-06-28_50_Risk-Controlled Event-Driven Cascading Updates for Knowledge Graph Consistency Restoration.pdf

Knowledge Graphs (KGs) provide structured and interpretable representations of real-world entities and relations. While dynamic KGs attempt to capture real-time changes, they typically treat updates as independent facts. This overlooks a critical challenge: a factual, localized update can contradict and invalidate previously correct knowledge, requiring revisions beyond the localized update to maintain KG consistency. Many of these inconsistencies arise from events whose effects propagate through relational dependencies, necessitating coordinated multi-hop reasoning rather than isolated changes. To address this, we introduce a model-agnostic framework for cascading KG update identification that leverages conformal prediction to provide reliable uncertainty guarantees over the cascade as a whole, accounting for dependencies among multi-hop update candidates. Building on this foundation, we further develop a graph-based KG update scoring framework that integrates large language models (LLMs) to enrich event representations with world knowledge. Experiments on two newly constructed real-world datasets, designed to reflect scenarios where events necessitate coordinated multi-hop updates, demonstrate that our framework establishes a strong baseline while offering calibrated confidence estimates, providing an effective solution for event-driven KG consistency restoration.

## 51. ClimateCause: Complex and Implicit Causal Structures in Climate Reports

- Authors: Liesbeth Allein, Nataly Pineda-Castañeda, Andrea Rocci, Marie-Francine Moens
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.1811168988706466
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1272/
- PDF: https://aclanthology.org/2026.findings-acl.1272.pdf
- Local PDF: pdf/2026-06-28_51_ClimateCause_ Complex and Implicit Causal Structures in Climate Reports.pdf

Understanding climate change requires reasoning over complex causal networks. Yet, existing causal discovery datasets predominantly capture explicit, direct causal relations. We introduce ClimateCause, a manually expert-annotated dataset of higher-order causal structures from science-for-policy climate reports, including implicit and nested causality. Cause-effect expressions are normalized and disentangled into individual causal relations to facilitate graph construction, with unique annotations for cause-effect correlation, relation type, and spatiotemporal context. We further demonstrate ClimateCause’s value for quantifying readability based on the semantic complexity of causal graphs underlying a statement. Finally, large language model benchmarking on correlation inference and causal chain reasoning highlights the latter as a key challenge.

## 52. Structure-Aware Zero-Shot Relational Learning for Knowledge Graphs without External Knowledge

- Authors: Kuan Xu, Baoxin Zhang, Shuyue Fan, Ming Chen, Zhipeng Ke, Jian Yu, Xuezhong Zhou
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.1801151156989684
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.941/
- PDF: https://aclanthology.org/2026.findings-acl.941.pdf
- Local PDF: pdf/2026-06-28_52_Structure-Aware Zero-Shot Relational Learning for Knowledge Graphs without External Knowledge.pdf

Zero-shot Relational Learning (ZRL) aims to perform knowledge graph completion when dealing with newly emerging relations without instances of them. However, existing ZRL methods typically depend on external knowledge beyond Knowledge Graphs (KGs), resulting in increased annotation costs and limited practical applicability. To address this issue, we propose a new **S**tructure-**A**ware paradigm for **ZRL**, termed **SAZRL**, that performs ZRL without relying on external knowledge. SAZRL leverages intrinsic structural patterns in KGs to bridge semantic correlations for new relations with existing ones. It constructs structure-aware conditional query graphs based on shared entities and adaptive relation updating module to generate representations for new relations based on the query graphs. We conduct extensive experiments on three real-world benchmarks, **NELL-ZS**, **Wiki-ZS** and **FB15K-ZS**, demonstrating that SAZRL consistently surpasses state-of-the-art ZRL methods, achieving up to **10.66%** improvement in **MRR** while reducing annotation costs and enhancing practical applicability. **The code and data are provided in supplementary materials.**

## 53. Datasets for Scientific Literature Understanding: A Survey

- Authors: Yuanzhe Zhang, Xun Zhao, Maodi Hu, Xi Sun, Donghuan Song, Zhixiong Zhang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.1754565251265046
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1414/
- PDF: https://aclanthology.org/2026.findings-acl.1414.pdf
- Local PDF: pdf/2026-06-28_53_Datasets for Scientific Literature Understanding_ A Survey.pdf

Empowering machines to understand scientific literature is crucial for accelerating scientific discovery and advancing the AI for Science (AI4S) paradigm. In this paper, we present a comprehensive survey of datasets serving this domain. We propose a systematic taxonomy that organizes resources spanning structural understanding, text understanding, multimodal understanding and pre-training/instruction fine-tuning. Beyond a structured overview, we discuss the evolution of the field, elucidating how the emergence of Large Language Models (LLMs) has reshaped research priorities of dataset construction. By synthesizing existing datasets and identifying critical future directions, this work provides a roadmap for advancing intelligent scientific research systems.

## 54. GeoLAN: Geometric Learning of Latent Explanatory Directions in Large Language Models

- Authors: Tianyu Pan, Damon L. Woodard
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.1731368272995777
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.271/
- PDF: https://aclanthology.org/2026.findings-acl.271.pdf
- Local PDF: pdf/2026-06-28_54_GeoLAN_ Geometric Learning of Latent Explanatory Directions in Large Language Models.pdf

Large language models (LLMs) demonstrate strong performance, but they often lack transparency. We introduce GeoLAN, a training framework that treats token representations as geometric trajectories and applies stickiness conditions inspired by recent developments related to the Kakeya Conjecture. We have developed two differentiable regularizers, Katz-Tao Convex Wolff (KT-CW) and Katz-Tao Attention (KT-Attn), that promote isotropy and encourage diverse attention. Our experiments with Gemma-3 (1B, 4B, 12B) and Llama-3-8B show that GeoLAN frequently maintains task accuracy while improving geometric metrics and reducing certain fairness biases. These benefits are most significant in mid-sized models. Our findings reveal scale-dependent trade-offs between geometric precision and performance, suggesting that geometry-aware training is a promising approach to enhance mechanistic interpretability.

## 55. Conceptual Hierarchies within LLMs

- Authors: Tiago Almeida, Zining Zhu, Yue Ning
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.16924900235938
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.2041/
- PDF: https://aclanthology.org/2026.findings-acl.2041.pdf
- Local PDF: pdf/2026-06-28_55_Conceptual Hierarchies within LLMs.pdf

While it is widely agreed that large language models (LLMs) store concepts from multiple semantic hierarchies, much remains unknown regarding the structure of this storage. The correspondence between the functional roles of LLM components and the semantic hierarchies of knowledge remains underexplored in the current literature. For example, is information organized hierarchically within sections of an LLM? We take an initial step towards causally examining the correspondence between hierarchical concepts and the multi-granular structures (layers and attention heads) of various models. Specifically, we generate a dataset of semantic hierarchies and investigate their storage locations in six LLMs using activation patching, a causal intervention technique. At the layer level, our findings show a moderate indication that concepts at finer levels of granularity are stored around 61-78% of the time ( p < 0.01) before those at coarser granularity. There is evidence for this trend at the attention level; however, the high variability in attention level results suggests that concepts are stored across attention heads rather than within. Our results offer insight into semantic organization within LLMs.

## 56. Multimodal Unlearning Across Vision, Language, Video, and Audio: Survey of Methods, Datasets, and Benchmarks

- Authors: Nobin Sarwar, Shubhashis Roy Dipta, Zheyuan Liu, Vaidehi Patil
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.1672662384145225
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1379/
- PDF: https://aclanthology.org/2026.findings-acl.1379.pdf
- Local PDF: pdf/2026-06-28_56_Multimodal Unlearning Across Vision, Language, Video, and Audio_ Survey of Methods, Datasets, and Benchmarks.pdf

With the growing adoption of VLMs, DMs, LLMs, and AFMs, these multimodal foundation models can inadvertently encode sensitive, copyrighted, biased, or unsafe cross-modal associations that originate from their training data. Retraining after deletion requests or policy updates is often impractical, and targeted forgetting remains difficult because knowledge is distributed across shared representations. Multimodal unlearning addresses this challenge by enabling selective removal across modalities while retaining overall utility. This survey offers a unified, system-oriented view of multimodal unlearning across vision, language, audio, and video, grounded in recent advances, emerging applications, and open problems. Our taxonomy enables systematic comparison across model architectures and modalities, clarifying trade-offs among deletion strength, retention, efficiency, reversibility, and robustness. This survey highlights open problems and practical considerations to support future research and deployment of multimodal unlearning.

## 57. Graph Explorer: Training Faithful KG Agents with Visibility-Grounded Supervision

- Authors: Yifeng Chen, Sicheng Wan, Tianyi Zhang, Xuezhou Zhang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.1588817116623353
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.387/
- PDF: https://aclanthology.org/2026.findings-acl.387.pdf
- Local PDF: pdf/2026-06-28_57_Graph Explorer_ Training Faithful KG Agents with Visibility-Grounded Supervision.pdf

Large language models (LLMs) are strong reasoners but still hallucinate and make unreliable decisions on knowledge-intensive questions. Knowledge graphs (KGs) provide explicit, auditable facts, motivating KGQA agents that interact with KGs via tool calls to reduce hallucinations. However, LLM agents often struggle to reliably manipulate KG-specific symbols (entity IDs and relation names), leading to invalid or hallucinated tool-call arguments, and high-quality step-by-step supervision for such tool use is scarce. Meanwhile, large datasets of expert SPARQL programs exist for Freebase KGQA, but naively converting them into action supervision is brittle: SPARQL assumes a global view of the KG, while an agent acts from a truncated, local prompt, so expert steps can reference KG IDs (entity/relation/attribute symbols) that are not visible at decision time. We present Graph Explorer, a fully automatic data synthesis pipeline that turns expert SPARQL into executable, visibility-grounded (actions may use only IDs shown in the prompt) tool supervision without manual trace labeling. Graph Explorer compiles SPARQL into tool-call plans, executes them under the same context-control policy used at inference, and retains only tool-interaction traces whose tool-call arguments are visible at decision time, yielding clean (context, next-action) pairs for action-centric fine-tuning. We evaluate with a strict finish-or-fail protocol (success only if the agent issues a valid Finish within budget). Under this protocol, our fine-tuned Qwen3-8B reaches 74.0/80.2 Hit@1 on CWQ/WebQSP, improving over a reproduced prompting baseline by +22.5/+16.2 points, indicating more faithful multi-step graph exploration from visible evidence.

## 58. Tracing Relational Knowledge Recall in Large Language Models

- Authors: Nicholas Popovič, Michael Färber
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.1560464392371945
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.2160/
- PDF: https://aclanthology.org/2026.findings-acl.2160.pdf
- Local PDF: pdf/2026-06-28_58_Tracing Relational Knowledge Recall in Large Language Models.pdf

We study how large language models recall relational knowledge during text generation, with a focus on identifying latent representations suitable for relation classification via linear probes.Prior work shows how attention heads and MLPs interact to resolve subject, predicate, and object, but it remains unclear which representations support faithful linear relation classification and why some relation types are easier to capture linearly than others.We systematically evaluate different latent representations derived from attention head and MLP contributions, showing that per-head attention contributions to the residual stream are comparatively strong features for linear relation classification.Feature attribution analyses of the trained probes, as well as characteristics of the different relation types, reveal clear correlations between probe accuracy and relation specificity, entity connectedness, and how distributed the signal on which the probe relies is across attention heads.Finally, we show how token-level feature attribution of probe predictions can be used to reveal probe behavior in further detail.

## 59. Learning Continuous Temporal Dynamics on Symplectic Manifolds for Temporal Knowledge Graph Embedding

- Authors: Jiang Li, Zehua Duo, Tian Lan, Feilong Bao, Guanglai Gao, Xiangdong Su
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.1552348002377606
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.804/
- PDF: https://aclanthology.org/2026.findings-acl.804.pdf
- Local PDF: pdf/2026-06-28_59_Learning Continuous Temporal Dynamics on Symplectic Manifolds for Temporal Knowledge Graph Embedding.pdf

Temporal knowledge graph embedding (TKGE) aims to model the temporal evolution of relational facts. However, existing approaches predominantly rely on discrete timestamp lookup tables and high-dimensional embedding spaces, which lack explicit structural constraints for continuous-time dynamics. As a result, temporal patterns are often captured through capacity scaling rather than principled dynamic modeling, leading to limited parameter efficiency and scalability.To address these limitations, we propose , a physics-inspired framework that embeds temporal dynamics into a symplectic phase space. Our model introduces a structure-preserving Hamiltonian evolution mechanism based on a pairwise-decoupled Hamiltonian generator and its Cayley transform, ensuring that temporal transformations adhere to the symplectic group Sp (2d) and preserve phase-space volume with linear computational complexity. In addition, we design a Time-Aware Parameter Modulation mechanism that integrates continuous Rotary Time Embeddings via Feature-wise Linear Modulation, enabling smooth temporal evolution while capturing event-driven variations. Theoretical analysis establishes the geometric validity of the proposed framework. Extensive experiments on standard TKGE benchmarks demonstrate that achieves competitive performance with substantially lower embedding dimensions. Furthermore, empirical results show that the proposed continuous Hamiltonian evolution facilitates generalization to unseen timestamps by learning transferable temporal dynamics from the underlying geometric structure.

## 60. EvoHyper: Evolving Hypergraph Topologies for Unified Collaboration in Multi-Agent Communication

- Authors: Heng Zhang, Yihao Zhong, Lubin Gan, Zhihe Chen, Jiajun Wu, Yuling Shi, Xiaodong Gu, Hao Zhang, Haochen You, Jin Huang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.154863302814539
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1258/
- PDF: https://aclanthology.org/2026.findings-acl.1258.pdf
- Local PDF: pdf/2026-06-28_60_EvoHyper_ Evolving Hypergraph Topologies for Unified Collaboration in Multi-Agent Communication.pdf

Multi-agent systems powered by large language models have achieved strong performance on complex tasks, yet naive collaboration topologies often cause high communication costs and redundant context. Existing methods usually use a fixed communication graph and manage collaboration structure and shared memory in separate modules. Our log analysis of several representative systems shows that this separation leads to multiple copies of the same key facts in dialogue, memory and model inputs. We address this issue with EvoHyper, a framework based on an evolving hypergraph topology for multi-agent collaboration. In EvoHyper, a single hypergraph represents agents and shared memory, and each hyperedge serves as a collaboration unit that binds a group of agents to that shared memory. During execution a controller edits the hypergraph through a small set of predefined evolution operations, so collaboration units can spawn, update and merge as tasks unfold. Experiments on four benchmarks covering mathematical reasoning and code generation show that EvoHyper is (I) high-performing, achieving 3.2% to 7.8% accuracy gains over state-of-the-art methods, (II) efficient, reducing token consumption by up to 23.5%, and (III) adaptive, adjusting topology complexity according to task requirements.
