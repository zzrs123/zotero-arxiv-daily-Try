# Paper Daily Reading - 2026-06-15

## 1. Identifying Cellular Niches in Spatial Transcriptomics: An Investigation into the Capabilities of Large Language Models

- Authors: Huanhuan Wei, Xiao Luo, Hongyi Yu, Jinping Liang, Luning Yang, Lixing Lin, Alexandra Popa, Xiting Yan
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2025-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 4.010159865384515
- Article: https://aclanthology.org/2025.acl-long.455/
- PDF: https://aclanthology.org/2025.acl-long.455.pdf
- Local PDF: pdf/2026-06-15_01_Identifying Cellular Niches in Spatial Transcriptomics_ An Investigation into the Capabilities of Large Language Models.pdf

Spatial transcriptomic technologies enable measuring gene expression profile and spatial information of cells in tissues simultaneously. Clustering of captured cells/spots in the spatial transcriptomic data is crucial for understanding tissue niches and uncovering disease-related changes.Current methods to cluster spatial transcriptomic data encounter obstacles, including inefficiency in handling multi-replicate data, lack of prior knowledge incorporation, and producing uninterpretable cluster labels.We introduce a novel approach, LLMiniST, to identify spatial niche using a zero-shot large language models (LLMs) by transforming spatial transcriptomic data into spatial context prompts, leveraging gene expression of neighboring cells/spots, cell type composition, tissue information, and external knowledge. The model was further enhanced using a two-stage fine-tuning strategy for improved generalizability. We also develop a user-friendly annotation tool to accelerate the creation of well-annotated spatial dataset for fine-tuning.Comprehensive method performance evaluations showed that both zero-shot and fine-tunned LLMiniST had superior performance than current non-LLM methods in many circumstances. Notably, the two-stage fine-tuning strategy facilitated substantial cross-subject generalizability. The results demonstrate the feasibility of LLMs for tissue niche identification using spatial transcriptomic data and the potential of LLMs as a scalable solution to efficiently integrate minimal human guidance for improved performance in large-scale datasets.

## 2. Sheaf Graph Neural Networks via PAC-Bayes Spectral Optimization

- Authors: Yoonhyuk Choi, Jiho Choi, Taewook Ko, JongWook Kim, Chong-kwon Kim
- Source: openalex
- Venue type: conference
- Journal: Proceedings of the AAAI Conference on Artificial Intelligence
- Publication status: formally_published
- Publication date: 2026-03-14
- DOI: https://doi.org/10.1609/aaai.v40i25.39193
- Categories: Advanced Graph Neural Networks, Machine Learning and ELM, Advanced Technologies in Various Fields
- Relevance: 3.9896373806736585
- Article: https://doi.org/10.1609/aaai.v40i25.39193
- PDF: Unavailable
- Local PDF: Not downloaded

Over-smoothing in Graph Neural Networks (GNNs) causes collapse in distinct node features, particularly on heterophilic graphs where adjacent nodes often have dissimilar labels. Although sheaf neural networks partially mitigate this problem, they typically rely on static or heavily parameterized sheaf structures that hinder generalization and scalability. Existing sheaf-based models either predefine restriction maps or introduce excessive complexity, yet fail to provide rigorous stability guarantees. In this paper, we introduce a novel scheme called SGPC (Sheaf GNNs with PAC-Bayes Calibration), a unified architecture that combines cellular-sheaf message passing with several mechanisms, including optimal transport-based lifting, variance-reduced diffusion, and PAC-Bayes spectral regularization for robust semi-supervised node classification. We establish performance bounds theoretically and demonstrate that end-to-end training in linear computational complexity can achieve the resulting bound-aware objective. Experiments on nine homophilic and heterophilic benchmarks show that SGPC outperforms state-of-the-art spectral and sheaf-based GNNs while providing certified confidence intervals on unseen nodes.

## 3. Accurately Deciphering Tissue Heterogeneity From Spatial Multi‐Modal and Multi‐Omics With STransformer

- Authors: Xingyi Li, Jialuo Xu, Gaoming Du, Xiangting Jia, Dongmin Zhao, Chunyan Zhou, Kexin Xiao, Jia Gu, Junnan Zhu, Xuequn Shang
- Source: openalex
- Venue type: journal
- Journal: Advanced Science
- Publication status: published
- Publication date: 2026-06-09
- DOI: https://doi.org/10.1002/advs.75969
- Categories: Single-cell and spatial transcriptomics, Bioinformatics and Genomic Networks, Cell Image Analysis Techniques
- Relevance: 3.9836498282284802
- Article: https://doi.org/10.1002/advs.75969
- PDF: Unavailable
- Local PDF: Not downloaded

Advances in spatially resolved technologies enable the simultaneous acquisition of diverse data modalities within a tissue slice while preserving critical spatial context, which presents unprecedented opportunities to decipher intricate tissue heterogeneity. However, existing computational approaches lack the intrinsic flexibility to universally process both spatial multi-modal and multi-omics data. Here, we introduce STransformer, a unified deep learning framework designed to seamlessly accommodate a comprehensive landscape of spatial data. By simultaneously capturing short-range cellular interactions and tissue-wide semantic patterns, it extracts robust representations to accurately dissect complex tissue heterogeneity. Systematic evaluations across diverse species, tissue types, and data modalities highlight its profound versatility. For spatial multi-modal data, STransformer delineates intricate anatomical structures in the human cortex, uncovers pathological mechanisms in Alzheimer's disease, and characterizes dynamic spatiotemporal developmental trajectories during chicken cardiogenesis. Scaling to spatial multi-omics data, STransformer synergizes spatial transcriptomic and proteomic profiles to decipher intricate immune microenvironments within the human tonsil, and jointly analyzes spatial epigenomic and transcriptomic data to infer regulatory mechanisms in the mouse embryonic brain. Consequently, STransformer serves as a highly versatile and robust analytical framework for advancing our understanding of tissue heterogeneity and disease pathogenesis.

## 4. GRNFormer: A Biologically-Guided Framework for Integrating Gene Regulatory Networks into RNA Foundation Models

- Authors: Mufan Qiu, Xinyu Hu, Fengwei Zhan, Sukwon Yun, Jie Peng, Ruichen Zhang, Bhavya Kailkhura, Jiekun Yang, Tianlong Chen
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2025-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.934922565763669
- Article: https://aclanthology.org/2025.findings-acl.196/
- PDF: https://aclanthology.org/2025.findings-acl.196.pdf
- Local PDF: pdf/2026-06-15_04_GRNFormer_ A Biologically-Guided Framework for Integrating Gene Regulatory Networks into RNA Foundation Models.pdf

GRNFormer 通过将多组学推断得到的分层基因调控网络以结构感知方式融入单细胞 RNA 基础模型，结合拓扑注意力适配器与生物学引导的边扰动策略，显著提升了药物反应预测、单细胞药物分类和基因扰动预测等下游任务表现。

## 5. Judge and Improve: Towards a Better Reasoning of Knowledge Graphs with Large Language Models

- Authors: Mo Zhiqiang, Yang Hua, Jiahui Li, Yuan Liu, Shawn Wong, Jianmin Huang
- Source: acl_anthology
- Venue type: conference
- Journal: EMNLP
- Publication status: formally_published
- Publication date: 2025-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.818777983054859
- Article: https://aclanthology.org/2025.emnlp-main.269/
- PDF: https://aclanthology.org/2025.emnlp-main.269.pdf
- Local PDF: pdf/2026-06-15_05_Judge and Improve_ Towards a Better Reasoning of Knowledge Graphs with Large Language Models.pdf

Graph Neural Networks (GNNs) have shown immense potential in improving the performance of large-scale models by effectively incorporating structured relational information. However, current approaches face two key challenges: (1) achieving robust semantic alignment between graph representations and large models, and (2) ensuring interpretability in the generated outputs. To address these challenges, we propose ExGLM (Explainable Graph Language Model), a novel training framework designed to seamlessly integrate graph and language modalities while enhancing transparency. Our framework introduces two core components: (1) a graph-language synergistic alignment module, which aligns graph structures with language model to ensure semantic consistency across modalities; and (2) a judge-and-improve paradigm, which allows the language model to iteratively evaluate, refine, and prioritize responses with higher interpretability, thereby improving both performance and transparency. Extensive experiments conducted on three benchmark datasets—ogbn-arxiv, Cora, and PubMed—demonstrate that ExGLM not only surpasses existing methods in efficiency but also generates outputs that are significantly more interpretable, effectively addressing the primary limitations of current approaches.

## 6. GraphInsight: Unlocking Insights in Large Language Models for Graph Structure Understanding

- Authors: Yukun Cao, Shuo Han, Zengyi Gao, Zezhong Ding, Xike Xie, S Kevin Zhou
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2025-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.7453949322546363
- Article: https://aclanthology.org/2025.acl-long.591/
- PDF: https://aclanthology.org/2025.acl-long.591.pdf
- Local PDF: pdf/2026-06-15_06_GraphInsight_ Unlocking Insights in Large Language Models for Graph Structure Understanding.pdf

Although Large Language Models (LLMs) have demonstrated potential in processing graphs, they struggle with comprehending graphical structure information through prompts of graph description sequences, especially as the graph size increases. We attribute this challenge to the uneven memory performance of LLMs across different positions in graph description sequences, known as ”Positional bias”. To address this, we propose GraphInsight, a novel framework aimed at improving LLMs’ comprehension of both macro- and micro-level graphical information. GraphInsight is grounded in two key strategies: 1) placing critical graphical information in positions where LLMs exhibit stronger memory performance, and 2) investigating a lightweight external knowledge base for regions with weaker memory performance, inspired by retrieval-augmented generation (RAG). Moreover, GraphInsight explores integrating these two strategies into LLM agent processes for composite graph tasks that require multi-step reasoning. Extensive empirical studies on benchmarks with a wide range of evaluation tasks show that GraphInsight significantly outperforms all other graph description methods (e.g., prompting techniques and reordering strategies) in understanding graph structures of varying sizes.

## 7. HiFusion: Hierarchical Intra-Spot Alignment and Regional Context Fusion for Spatial Gene Expression Prediction from Histopathology

- Authors: Ziqiao Weng, Yaoyu Fang, Jiahe Qian, Xinkun Wang, Lee Cooper, Weidong Cai, Bo Zhou
- Source: openalex
- Venue type: conference
- Journal: Proceedings of the AAAI Conference on Artificial Intelligence
- Publication status: formally_published
- Publication date: 2026-03-14
- DOI: https://doi.org/10.1609/aaai.v40i13.38036
- Categories: Single-cell and spatial transcriptomics, AI in cancer detection, Cell Image Analysis Techniques
- Relevance: 3.699755315501876
- Article: https://doi.org/10.1609/aaai.v40i13.38036
- PDF: Unavailable
- Local PDF: Not downloaded

Spatial transcriptomics (ST) bridges gene expression and tissue morphology but faces clinical adoption barriers due to technical complexity and prohibitive costs. While computational methods predict gene expression from H&amp;E-stained whole-slide images (WSIs), existing approaches often fail to capture the intricate biological heterogeneity within spots and are susceptible to morphological noise when integrating contextual information from surrounding tissue. To overcome these limitations, we propose HiFusion, a novel deep learning framework that integrates two complementary components. First, we introduce the Hierarchical Intra-Spot Modeling module that extracts fine-grained morphological representations through multi-resolution sub-patch decomposition, guided by a feature alignment loss to ensure semantic consistency across scales. Concurrently, we present the Context-aware Cross-scale Fusion module, which employs cross-attention to selectively incorporate biologically relevant regional context, thereby enhancing representational capacity. This architecture enables comprehensive modeling of both cellular-level features and tissue microenvironmental cues, which are essential for accurate gene expression prediction. Extensive experiments on two benchmark ST datasets demonstrate that HiFusion achieves state-of-the-art performance across both 2D slide-wise cross-validation and more challenging 3D sample-specific scenarios. These results underscore HiFusion’s potential as a robust, accurate, and scalable solution for ST inference from routine histopathology.

## 8. SpaDC enables sequence-based integrative analysis and regulatory inference of spatial chromatin accessibility data

- Authors: Shaolin Mao, Chenghui Yang, Caiwei Zhen, Zhentao He, Yi Luo, L Zhang
- Source: openalex
- Venue type: journal
- Journal: Communications Biology
- Publication status: published
- Publication date: 2026-06-06
- DOI: https://doi.org/10.1038/s42003-026-10462-y
- Categories: Genomics and Chromatin Dynamics, Single-cell and spatial transcriptomics, Epigenetics and DNA Methylation
- Relevance: 3.6973993997401355
- Article: https://doi.org/10.1038/s42003-026-10462-y
- PDF: Unavailable
- Local PDF: Not downloaded

Spatial ATAC-seq enables simultaneous profiling of cellular locations and chromatin accessibility in intact tissues but faces challenges from high dimensionality, noise, and sparsity. Moreover, existing methods often overlook DNA sequence information, which contains critical regulatory motifs. To address these limitations, we introduce SpaDC, a graph-regularized convolutional neural network that integrates spatial location, chromatin accessibility, and DNA sequence. SpaDC employs a triplet loss function to integrate multiple spatial ATAC-seq datasets and remove batch effects. Benchmark analyses on real datasets demonstrate state-of-the-art performance in spatial domain identification, data denoising, and gene regulatory network (GRN) inference. Applied to mouse embryonic brain spatial ATAC-seq data, SpaDC accurately identified known brain structures and recovered chromatin accessibility signals. On P22 mouse brain spatial multi-omics data, SpaDC revealed spatial domain-specific cis-regulatory elements and GRNs. Collectively, SpaDC provides a powerful, sequence-based solution for spatial ATAC-seq analysis, enabling more accurate and robust investigation of tissue architecture and chromatin organization.

## 9. Structure-Aware Cooperative Ensemble Evolutionary Optimization on Combinatorial Problems with Multimodal Large Language Models

- Authors: Zhao, Jie, Cheong, Kang
- Source: neurips
- Venue type: conference
- Journal: NeurIPS 2025
- Publication status: formally_published
- Publication date: 2026-04-23
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.6820913298349875
- Article: https://proceedings.neurips.cc/paper_files/paper/2025/hash/0cda0892c74edef6bc73e46a4480511f-Abstract-Conference.html
- PDF: https://proceedings.neurips.cc/paper_files/paper/2025/file/0cda0892c74edef6bc73e46a4480511f-Paper-Conference.pdf
- Local PDF: pdf/2026-06-15_09_Structure-Aware Cooperative Ensemble Evolutionary Optimization on Combinatorial Problems with Multimodal Large Language.pdf

Evolutionary algorithms (EAs) have proven effective in exploring the vast solution spaces typical of graph-structured combinatorial problems. However, traditional encoding schemes, such as binary or numerical representations, often fail to straightforwardly capture the intricate structural properties of networks. Through employing the image-based encoding to preserve topological context, this study utilizes multimodal large language models (MLLMs) as evolutionary operators to facilitate structure-aware optimization over graph data. To address the visual clutter inherent in large-scale network visualizations, we leverage graph sparsification techniques to simplify structures while maintaining essential structural features. To further improve robustness and mitigate bias from different sparsification views, we propose a cooperative evolutionary optimization framework that facilitates cross-domain knowledge transfer and unifies multiple sparsified variants of diverse structures. Additionally, recognizing the sensitivity of MLLMs to network layout, we introduce an ensemble strategy that aggregates outputs from various layout configurations through consensus voting. Finally, experiments on real-world networks through various tasks demonstrate that our approach improves both the quality and reliability of solutions in MLLM-driven evolutionary optimization.

## 10. Taming Language Models for Text-attributed Graph Learning with Decoupled Aggregation

- Authors: Chuang Zhou, Zhu Wang, Shengyuan Chen, Jiahe Du, Qiyuan Zheng, Zhaozhuo Xu, Xiao Huang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2025-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.6764296987147853
- Article: https://aclanthology.org/2025.acl-long.173/
- PDF: https://aclanthology.org/2025.acl-long.173.pdf
- Local PDF: pdf/2026-06-15_10_Taming Language Models for Text-attributed Graph Learning with Decoupled Aggregation.pdf

Text-attributed graphs (TAGs) are prevalent in various real-world applications, including academic networks, e-commerce platforms, and social networks. Effective learning on TAGs requires leveraging both textual node features and structural graph information. While language models (LMs) excel at processing text and graph neural networks (GNNs) effectively capture relational structures, their direct integration is computationally prohibitive due to the high cost of text and graph representation learning. Existing approaches address this challenge by adopting a two-step pipeline where LMs generate fixed node embeddings, which are then used for GNN training. However, this method neglects the interaction between textual and structural information, leading to suboptimal learning outcomes. To overcome these limitations, we propose SKETCH (Semantic Knowledge and Structure Enrichment), a novel framework that decouples node aggregation from graph convolution and integrates it into the text representation learning process. SKETCH enhances TAG learning by incorporating two key aggregation mechanisms: (1) Semantic aggregation, which retrieves semantically relevant node texts for contextual enrichment, and (2) Structural aggregation, which propagates textual features beyond immediate neighbors to capture broader graph relationships. Extensive experiments demonstrate that SKETCH outperforms state-of-the-art TAG learning methods while requiring fewer computational resources. By enabling a more efficient and effective fusion of textual and structural information, SKETCH provides new insights into TAG problems and offers a practical solution for real applications.

## 11. Graph Counselor: Adaptive Graph Exploration via Multi-Agent Synergy to Enhance LLM Reasoning

- Authors: Junqi Gao, Xiang Zou, Ying Ai, Dong Li, Yichen Niu, Biqing Qi, Jianxing Liu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2025-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.6158161751986935
- Article: https://aclanthology.org/2025.acl-long.1202/
- PDF: https://aclanthology.org/2025.acl-long.1202.pdf
- Local PDF: pdf/2026-06-15_11_Graph Counselor_ Adaptive Graph Exploration via Multi-Agent Synergy to Enhance LLM Reasoning.pdf

Graph Retrieval Augmented Generation (GraphRAG) effectively enhances external knowledge integration capabilities by explicitly modeling knowledge relationships, thereby improving the factual accuracy and generation quality of Large Language Models (LLMs) in specialized domains. However, existing methods suffer from two inherent limitations: 1) Inefficient Information Aggregation: They rely on a single agent and fixed iterative patterns, making it difficult to adaptively capture multi-level textual, structural, and degree information within graph data. 2) Rigid Reasoning Mechanism: They employ preset reasoning schemes, which cannot dynamically adjust reasoning depth nor achieve precise semantic correction. To overcome these limitations, we propose Graph Counselor, an GraphRAG method based on multi-agent collaboration. This method uses the Adaptive Graph Information Extraction Module (AGIEM), where Planning, Thought, and Execution Agents work together to precisely model complex graph structures and dynamically adjust information extraction strategies, addressing the challenges of multi-level dependency modeling and adaptive reasoning depth. Additionally, the Self-Reflection with Multiple Perspectives (SR) module improves the accuracy and semantic consistency of reasoning results through self-reflection and backward reasoning mechanisms. Experiments demonstrate that Graph Counselor outperforms existing methods in multiple graph reasoning tasks, exhibiting higher reasoning accuracy and generalization ability.Our code is available at https://github.com/gjq100/Graph-Counselor.git.

## 12. From Static to Active: Knowledge-Aware Node State Selection in Multi-view Graph Learning

- Authors: Weiran Liao, Jielong Lu, Yuhong Chen, Shide Du, Hongrong Chen, Shiping Wang
- Source: openalex
- Venue type: conference
- Journal: Proceedings of the AAAI Conference on Artificial Intelligence
- Publication status: formally_published
- Publication date: 2026-03-14
- DOI: https://doi.org/10.1609/aaai.v40i28.39518
- Categories: Advanced Graph Neural Networks, Domain Adaptation and Few-Shot Learning, Human Pose and Action Recognition
- Relevance: 3.6153483934099806
- Article: https://doi.org/10.1609/aaai.v40i28.39518
- PDF: Unavailable
- Local PDF: Not downloaded

Multimedia technologies leverage multi-source to alleviate real-world data incompleteness, providing a versatile platform for multi-view learning. Among existing research, graph-based multi-view learning has achieved notable success. However, prior studies always immerse in comprehensive collaboration across all views and nodes to pursue consistency and complementary, which ignore the negative contribution of nodes from low-quality views. To overcome the above limitation, we explore node behavior selection in multi-view dynamic modeling and propose a knowledge-aware multi-view state space model. Specifically, nodes autonomously select either activation sequences or static sequences according to their current knowledge. In the former, we design the mask-based attention mechanism to capture the dynamics of node behaviors. In the latter, we construct a history pool and simulate synaptic signals to regulate the behavioral distribution of nodes. Moreover, the proposed model provides a directional inter-view diffusion equation that selectively propagates information to alleviate interference from low-quality nodes across views. Extensive experiments demonstrate that the proposed model outperforms baselines on multiple benchmarks and achieves significant performance improvement.

## 13. Inductive Learning on Heterogeneous Graphs Enhanced by LLMs for Software Mention Detection

- Authors: Gabriel Silva, Mário Rodriges, António Teixeira, Marlene Amorim
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2025-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.614514029463792
- Article: https://aclanthology.org/2025.sdp-1.16/
- PDF: https://aclanthology.org/2025.sdp-1.16.pdf
- Local PDF: pdf/2026-06-15_13_Inductive Learning on Heterogeneous Graphs Enhanced by LLMs for Software Mention Detection.pdf

This paper explores the synergy between Knowledge Graphs (KGs), Graph Machine Learning (Graph ML), and Large Language Models (LLMs) for multilingual Named Entity Recognition (NER) and Relation Extraction (RE), specifically targeting software mentions within the SOMD 2025 challenge. We propose a methodology where documents are first transformed into heterogeneous KGs enriched with linguistic features (Universal Dependencies) and external knowledge (entity linking). An inductive GraphSAGE model, operating on PyTorch Geometric’s ‘HeteroData‘ structure with dynamically generated multilingual embeddings, performs node classification tasks. For NER, Graph ML identifies candidate entities and types, with an LLM (DeepSeek v3) acting as a validation layer. For RE, Graph ML predicts dependency path convergence points indicative of relations, while the LLM classifies the relation type and direction based on entity context. Our results demonstrate the potential of this hybrid approach, showing significant performance gains post-competition (NER Phase 2 Macro F1 improved to 0.4364 from 0.2953, RE Phase 1 0.3355 Macro F1), which are already described in this paper, and highlighting the benefits of integrating structured graph learning with LLM reasoning for information extraction.

## 14. RAG4GFM: Bridging Knowledge Gaps in Graph Foundation Models through Graph Retrieval Augmented Generation

- Authors: Wang, Xingliang, Liu, Zemin, Han, Junxiao, Deng, Shuiguang
- Source: neurips
- Venue type: conference
- Journal: NeurIPS 2025
- Publication status: formally_published
- Publication date: 2026-04-23
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.6062779788151005
- Article: https://proceedings.neurips.cc/paper_files/paper/2025/hash/0c3ce12ad831324fff8144c8025eb17b-Abstract-Conference.html
- PDF: https://proceedings.neurips.cc/paper_files/paper/2025/file/0c3ce12ad831324fff8144c8025eb17b-Paper-Conference.pdf
- Local PDF: pdf/2026-06-15_14_RAG4GFM_ Bridging Knowledge Gaps in Graph Foundation Models through Graph Retrieval Augmented Generation.pdf

Graph Foundation Models (GFMs) have demonstrated remarkable potential across graph learning tasks but face significant challenges in knowledge updating and reasoning faithfulness. To address these issues, we introduce the Retrieval-Augmented Generation (RAG) paradigm for GFMs, which leverages graph knowledge retrieval. We propose RAG4GFM, an end-to-end framework that seamlessly integrates multi-level graph indexing, task-aware retrieval, and graph fusion enhancement. RAG4GFM implements a hierarchical graph indexing architecture, enabling multi-granular graph indexing while achieving efficient logarithmic-time retrieval. The task-aware retriever implements adaptive retrieval strategies for node, edge, and graph-level tasks to surface structurally and semantically relevant evidence. The graph fusion enhancement module fuses retrieved graph features with query features and augments the topology with sparse adjacency links that preserve structural and semantic proximity, yielding a fused graph for GFM inference. Extensive experiments conducted across diverse GFM applications demonstrate that RAG4GFM significantly enhances both the efficiency of knowledge updating and reasoning faithfulness\footnote{Code: \url{https://github.com/Matrixmax/RAG4GFM}.}.

## 15. GraphChain: Large Language Models for Large-scale Graph Analysis via Tool Chaining

- Authors: Wei, Chunyu, Hu, Wenji, Hao, Xingjia, Wang, Xin, Yang, Yifan, Wang, Yunhai, Tian, Yang, Chen, Yueguo
- Source: neurips
- Venue type: conference
- Journal: NeurIPS 2025
- Publication status: formally_published
- Publication date: 2026-04-23
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.6038234736349795
- Article: https://proceedings.neurips.cc/paper_files/paper/2025/hash/0afacd536648265c03a0bd86dabb0e1a-Abstract-Conference.html
- PDF: https://proceedings.neurips.cc/paper_files/paper/2025/file/0afacd536648265c03a0bd86dabb0e1a-Paper-Conference.pdf
- Local PDF: pdf/2026-06-15_15_GraphChain_ Large Language Models for Large-scale Graph Analysis via Tool Chaining.pdf

Large Language Models (LLMs) face significant limitations when applied to large-scale graphs, struggling with context constraints and inflexible reasoning. We introduce GraphChain, a novel framework enabling LLMs to analyze large graphs by orchestrating dynamic sequences of specialized tools, mimicking human exploratory processes. GraphChain incorporates two core technical contributions: (1) Progressive Graph Distillation, a reinforcement learning approach that learns to generate tool sequences balancing task relevance and intermediate state compression, thereby overcoming LLM context limitations. (2) Structure-aware Test-Time Adaptation (STTA), a mechanism using a lightweight, self-supervised adapter conditioned on graph spectral properties to efficiently adapt a frozen LLM policy to diverse graph structures via soft prompts without retraining. Experiments show GraphChain significantly outperforms prior methods, enabling scalable and adaptive LLM-driven graph analysis.

## 16. scRAG: Hybrid Retrieval-Augmented Generation for LLM-based Cross-Tissue Single-Cell Annotation

- Authors: Zhiyin Yu, Chao Zheng, Chong Chen, Xian-Sheng Hua, Xiao Luo
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2025-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.600107226830833
- Article: https://aclanthology.org/2025.findings-acl.53/
- PDF: https://aclanthology.org/2025.findings-acl.53.pdf
- Local PDF: pdf/2026-06-15_16_scRAG_ Hybrid Retrieval-Augmented Generation for LLM-based Cross-Tissue Single-Cell Annotation.pdf

In recent years, large language models (LLMs) such as GPT-4 have demonstrated impressive potential in a wide range of fields, including biology, genomics and healthcare. Numerous studies have attempted to apply pre-trained LLMs to single-cell data analysis within one tissue. However, when it comes to cross-tissue cell annotation, LLMs often suffer from unsatisfactory performance due to the lack of specialized biological knowledge regarding genes and tissues. In this paper, we introduce scRAG, a novel framework that incorporates advanced LLM-based RAG techniques into cross-tissue single-cell annotation. scRAG utilizes LLMs to retrieve structured triples from knowledge graphs and unstructured similar cell information from the reference cell database, and it generates candidate cell types. The framework further optimizes predictions by retrieving marker genes from both candidate cells and similar cells to refine its results. Extensive experiments on a cross-tissue dataset demonstrate that our scRAG framework outperforms various baselines, including generalist models, domain-specific methods, and trained classifiers. The source code is available at https://github.com/YuZhiyin/scRAG.

## 17. MoToRec: Sparse-Regularized Multimodal Tokenization for Cold-Start Recommender

- Authors: Jialin Liu, Zhaorui Zhang, Ray C.C. CHEUNG
- Source: openalex
- Venue type: conference
- Journal: Proceedings of the AAAI Conference on Artificial Intelligence
- Publication status: formally_published
- Publication date: 2026-03-14
- DOI: https://doi.org/10.1609/aaai.v40i18.38558
- Categories: Recommender Systems and Techniques, Advanced Graph Neural Networks, Machine Learning in Healthcare
- Relevance: 3.584409072204301
- Article: https://doi.org/10.1609/aaai.v40i18.38558
- PDF: Unavailable
- Local PDF: Not downloaded

Graph neural networks (GNNs) have revolutionized recommender systems by effectively modeling complex user-item interactions, yet data sparsity and the item cold-start problem significantly impair performance, particularly for new items with limited or no interaction history. While multimodal content offers a promising solution, existing methods result in suboptimal representations for new items due to noise and entanglement in sparse data. To address this, we transform multimodal recommendation into discrete semantic tokenization. We present Sparse-Regularized Multimodal Tokenization for Cold-Start Recommender Systems (MoToRec), a framework centered on a sparsely-regularized Residual Quantized Variational Autoencoder (RQ-VAE) that generates a compositional semantic code of discrete, interpretable tokens, promoting disentangled representations. MoToRec’s architecture is enhanced by three synergistic components: (1) a sparsely regularized RQ-VAE that promotes disentangled representations, (2) a novel adaptive rarity amplification that promotes prioritized learning for cold-start items, and (3) a hierarchical multi-source graph encoder for robust signal fusion with collaborative signals. Extensive experiments on three large-scale datasets demonstrate MoToRec’s superiority over state-of-the-art methods in both overall and cold-start scenarios. Our work validates that discrete tokenization provides an effective and scalable alternative for mitigating the long-standing cold-start challenge.

## 18. Injecting Structured Knowledge into LLMs via Graph Neural Networks

- Authors: Zichao Li, Zong Ke, Puning Zhao
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2025-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.566988077998994
- Article: https://aclanthology.org/2025.xllm-1.3/
- PDF: https://aclanthology.org/2025.xllm-1.3.pdf
- Local PDF: pdf/2026-06-15_18_Injecting Structured Knowledge into LLMs via Graph Neural Networks.pdf

Large language models (LLMs) have achieved remarkable success in natural language processing (NLP), but they often struggle to capture explicit linguistic structures and world knowledge. To address this limitation, we propose a hybrid model that integrates LLMs with graph neural networks (GNNs) to inject structured knowledge into NLP tasks. Our approach leverages the strengths of both components: LLMs provide rich contextual representations, while GNNs encode explicit structural priors from sources such as dependency trees, Abstract Meaning Representations (AMRs), and knowledge graphs. We evaluate the hybrid model on a diverse set of tasks, including semantic parsing, multi-hop question answering, text summarization, commonsense reasoning, and dependency parsing. Experimental results demonstrate consistent improvements over both standalone baselines and state-of-the-art methods, with relative gains of up to 2.3% in Exact Match scores for multi-hop QA and 1.7% in accuracy for commonsense reasoning. Ablation studies and sensitivity analyses further highlight the importance of balancing contextual and structural information. By bridging the gap between unstructured textual data and structured knowledge, our work advances the state of the art in NLP and paves the way for more interpretable and robust language models.

## 19. Digest the Knowledge: Large Language Models empowered Message Passing for Knowledge Graph Question Answering

- Authors: Junhong Wan, Tao Yu, Kunyu Jiang, Yao Fu, Weihao Jiang, Jiang Zhu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2025-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.564559787368508
- Article: https://aclanthology.org/2025.acl-long.750/
- PDF: https://aclanthology.org/2025.acl-long.750.pdf
- Local PDF: pdf/2026-06-15_19_Digest the Knowledge_ Large Language Models empowered Message Passing for Knowledge Graph Question Answering.pdf

Despite their success, large language models (LLMs) suffer from notorious hallucination issue. By introducing external knowledge stored in knowledge graphs (KGs), existing methods use paths as the medium to represent the graph information that send into LLMs. However, paths only contain limited graph structure information and are unorganized with redundant sequentially appeared keywords, which are difficult for LLMs to digest. We aim to find a suitable medium that captures the essence of structure knowledge in KGs. Inspired by the Neural Message Passing in Graph Neural Networks, we propose Language Message Passing (LMP) that first learns a concise facts graph by iteratively aggregates neighbor entities and transforms them into semantic facts, and then we performs Topological Readout that encodes the graph structure information into multi-level lists of texts to augment LLMs. Our method serves as a brand-new innovative framework that brings a new perspective into KG-enhanced LLMs, and also offers human-level semantic explainability with significant performance improvements over existing methods on all 5 knowledge graph question answering datasets. Code is available at https://github.com/wanjunhong0/LMP.

## 20. Synergizing Multimodal Temporal Knowledge Graphs and Large Language Models for Social Relation Recognition

- Authors: Haorui Wang, Zheng Wang, Yuxuan Zhang, Bo Wang, Bin Wu
- Source: acl_anthology
- Venue type: conference
- Journal: EMNLP
- Publication status: formally_published
- Publication date: 2025-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.5451635775119748
- Article: https://aclanthology.org/2025.emnlp-main.224/
- PDF: https://aclanthology.org/2025.emnlp-main.224.pdf
- Local PDF: pdf/2026-06-15_20_Synergizing Multimodal Temporal Knowledge Graphs and Large Language Models for Social Relation Recognition.pdf

Recent years have witnessed remarkable advances in Large Language Models (LLMs). However, in the task of social relation recognition, Large Language Models (LLMs) encounter significant challenges due to their reliance on sequential training data, which inherently restricts their capacity to effectively model complex graph-structured relationships. To address this limitation, we propose a novel low-coupling method synergizing multimodal temporal Knowledge Graphs and Large Language Models (mtKG-LLM) for social relation reasoning. Specifically, we extract multimodal information from the videos and model the social networks as spatial Knowledge Graphs (KGs) for each scene. Temporal KGs are constructed based on spatial KGs and updated along the timeline for long-term reasoning. Subsequently, we retrieve multi-scale information from the graph-structured knowledge for LLMs to recognize the underlying social relation. Extensive experiments demonstrate that our method has achieved state-of-the-art performance in social relation recognition. Furthermore, our framework exhibits effectiveness in bridging the gap between KGs and LLMs. Our code will be released after acceptance.

## 21. Robust integration of weakly anchored spatial multi-omics

- Authors: Wang, C., Liu, Y., Wang, Z., Sun, P., Li, Z., Li, J., Wang, X., Chen, K., Zou, Q., Daoliang, Z., Hu, Z., Du, Y., Qian, B., Feng, X., Yuan, Z., Guan, R.
- Source: biorxiv
- Venue type: preprint
- Journal: biorxiv
- Publication status: preprint
- Publication date: 2026-06-14
- DOI: 10.64898/2026.06.10.731246
- Categories: bioinformatics
- Relevance: 3.527402325449554
- Article: https://www.biorxiv.org/content/10.64898/2026.06.10.731246v1.full.pdf
- PDF: https://www.biorxiv.org/content/10.64898/2026.06.10.731246v1.full.pdf
- Local PDF: Not downloaded

Spatial multi-omics holds great promise for dissecting complex biological processes, though inherent technical constraints continue to limit its widespread adoption. Currently, most studies therefore measure distinct omics features on separate tissue sections, necessitating spatial diagonal integration. An emerging practical solution is to leverage hematoxylin and eosin (H&E) images as an integration anchor, given their ubiquity, low cost, and compatibility across tissue preparations. However, this anchor is frequently compromised in real-world settings by variations in H&E staining style, absence of reliable histological landmarks, and mismatches in spatial resolutions across omics modalities. To address this, we introduce SpaWeaver, a computational framework that couples a pathology foundation model with a graph Transformer and a latent feature aligner module, providing a highly robust solution for weakly anchored spatial omics data diagonal integration. Extensive experiments demonstrate that SpaWeaver exhibits superior robustness against isolated or synergistic weak-anchoring factors. The spatial multi-omics profiles generated by SpaWeaver link molecular features originally separated on two sections, unlocking diverse downstream analyses once exclusive to co-assayed spatial multi-omics data, including niche-aware cell-cell communication inference and multi-omics resolved cell state. In this study, it unveils tumor-distance-dependent fibroblast-CD4+ T-cell signaling in human colon adenocarcinoma and identifies a hypoxic glycolytic tumor state with pyknotic nuclei in human ovarian cancer. Overall, our approach bridges readily accessible single-omics measurements across weakly anchored tissue sections, enabling unified spatial multi-omics characterization and system-level tissue analysis.

## 22. MARK: Multi-agent Collaboration with Ranking Guidance for Text-attributed Graph Clustering

- Authors: Yiwei Fu, Yuxing Zhang, Chunchun Chen, Jianwen Ma, Quan Yuan, Rong-Cheng Tu, Xinli Huang, Wei Ye, Xiao Luo, Minghua Deng
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2025-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.527191471187539
- Article: https://aclanthology.org/2025.findings-acl.314/
- PDF: https://aclanthology.org/2025.findings-acl.314.pdf
- Local PDF: pdf/2026-06-15_22_MARK_ Multi-agent Collaboration with Ranking Guidance for Text-attributed Graph Clustering.pdf

This paper studies the problem of text-attributed graph clustering, which aims to cluster each node into different groups using both textual attributes and structural information. Although graph neural networks (GNNs) have been proposed to solve this problem, their performance is usually limited when uncertain nodes are near the cluster boundaries due to label scarcity. In this paper, we introduce a new perspective of leveraging large language models (LLMs) to enhance text-attributed graph clustering and develop a novel approach named Multi-agent Collaboration with Ranking Guidance (MARK). The core of our MARK is to generate reliable guidance using the collaboration of three LLM-based agents as ranking-based supervision signals. In particular, we first conduct the coarse graph clustering, and utilize a concept agent to induce the semantics of each cluster. Then, we infer the robustness under perturbations to identify uncertain nodes and use a generation agent to produce synthetic text that closely aligns with their topology. An inference agent is adopted to provide the ranking semantics for each uncertain node in comparison to its synthetic counterpart. The consistent feedback between uncertain and synthetic texts is identified as reliable guidance for fine-tuning the clustering model within a ranking-based supervision objective. Experimental results on various benchmark datasets validate the effectiveness of the proposed MARK compared with competing baselines.

## 23. Spatial Coordinates as a Cell Language: A Multi-Sentence Framework for Imaging Mass Cytometry Analysis

- Authors: Chi-Jane Chen, Yuhang Chen, Sukwon Yun, Natalie Stanley, Tianlong Chen
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2025-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.5196320863749477
- Article: https://aclanthology.org/2025.findings-acl.685/
- PDF: https://aclanthology.org/2025.findings-acl.685.pdf
- Local PDF: pdf/2026-06-15_23_Spatial Coordinates as a Cell Language_ A Multi-Sentence Framework for Imaging Mass Cytometry Analysis.pdf

Image mass cytometry (IMC) enables high-dimensional spatial profiling by combining mass cytometry’s analytical power with spatial distributions of cell phenotypes. Recent studies leverage large language models (LLMs) to extract cell states by translating gene or protein expression into biological context. However, existing single-cell LLMs face two major challenges: (1) Integration of spatial information—they struggle to generalize spatial coordinates and effectively encode spatial context as text, and (2) Treating each cell independently—they overlook cell-cell interactions, limiting their ability to capture biological relationships. To address these limitations, we propose Spatial2Sentence, a novel framework that integrates both single-cell expression and spatial information into natural language using a multi-sentence approach. Given an expression matrix and spatial coordinates, Spatial2Sentence constructs expression similarity and distance matrices, pairing spatially adjacent and expressionally similar cells as positive pairs while using distant and dissimilar cells as negatives. These multi-sentence representations are processed by LLMs, enabling them to learn cellular interactions in both expression and spatial contexts. Equipped with multi-task learning, Spatial2Sentence outperforms existing single-cell LLMs on preprocessed IMC datasets for diabetes and brain tumors, improving cell-type classification by 5.98% and clinical status prediction by 4.18% on the diabetes dataset while enhancing interpretability. The source code can be found here: https://github.com/UNITES-Lab/Spatial2Sentence .

## 24. Can Graph Neural Networks Learn Language with Extremely Weak Text Supervision?

- Authors: Zihao Li, Lecheng Zheng, Bowen Jin, Dongqi Fu, Baoyu Jing, Yikun Ban, Jingrui He, Jiawei Han
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2025-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.5089154041895543
- Article: https://aclanthology.org/2025.acl-long.545/
- PDF: https://aclanthology.org/2025.acl-long.545.pdf
- Local PDF: pdf/2026-06-15_24_Can Graph Neural Networks Learn Language with Extremely Weak Text Supervision.pdf

While great success has been achieved in building vision models with Contrastive Language-Image Pre-training (CLIP) over Internet-scale image-text pairs, building transferable Graph Neural Networks (GNNs) with CLIP pipeline is challenging because of the scarcity of labeled data and text supervision, different levels of downstream tasks, and the conceptual gaps between domains. In this work, to address these issues, we propose a multi-modal prompt learning paradigm to effectively adapt pre-trained GNN to downstream tasks and data, given only a few semantically labeled samples, each with extremely weak text supervision. Our new paradigm embeds the graphs directly in the same space as the Large Language Models (LLMs) by learning both graph prompts and text prompts simultaneously. We demonstrate the superior performance of our paradigm in few-shot, multi-task-level, and cross-domain settings. Moreover, we build the first CLIP-style zero-shot classification prototype that can generalize GNNs to unseen classes with extremely weak text supervision.

## 25. LLM-Based Multi-Agent Systems are Scalable Graph Generative Models

- Authors: Jiarui Ji, Runlin Lei, Jialing Bi, Zhewei Wei, Xu Chen, Yankai Lin, Xuchen Pan, Yaliang Li, Bolin Ding
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2025-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.503347919341179
- Article: https://aclanthology.org/2025.findings-acl.78/
- PDF: https://aclanthology.org/2025.findings-acl.78.pdf
- Local PDF: pdf/2026-06-15_25_LLM-Based Multi-Agent Systems are Scalable Graph Generative Models.pdf

The structural properties of naturally arising social graphs are extensively studied to understand their evolution. Prior approaches for modeling network dynamics typically rely on rule-based models, which lack realism and generalizability, or deep learning-based models, which require large-scale training datasets. As abstract graph representations of entity-wise interactions, social graphs present an opportunity to explore network evolution mechanisms through realistic simulations of human-item interactions. Leveraging the pre-trained social consensus knowledge embedded in large language models (LLMs), we present GraphAgent-Generator (GAG), a novel simulation-based framework for dynamic, text-attributed social graph generation. GAG simulates the temporal node and edge generation processes for zero-shot social graph generation. The resulting graphs adhere to seven key macroscopic network properties, achieving an 11% improvement in microscopic graph structure metrics. Through the node classification benchmarking task, we validate that GAG effectively captures the intricate text-structure correlations in graph generation. Furthermore, GAG supports generating graphs with up to nearly 100,000 nodes or 10 million edges through large-scale LLM-based agent simulation with parallel acceleration, achieving a minimum speed-up of 90.4%. The source code is available at https://github.com/Ji-Cather/GraphAgent.

## 26. MuCoS: Efficient Drug–Target Discovery via Multi-Context-Aware Sampling in Knowledge Graphs

- Authors: Haji Gul, Abdul Ghani Naim, Ajaz Ahmad Bhat
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2025-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.501882408819302
- Article: https://aclanthology.org/2025.bionlp-1.27/
- PDF: https://aclanthology.org/2025.bionlp-1.27.pdf
- Local PDF: pdf/2026-06-15_26_MuCoS_ Efficient Drug–Target Discovery via Multi-Context-Aware Sampling in Knowledge Graphs.pdf

Accurate prediction of drug–target interactions is critical for accelerating drug discovery. In this work, we frame drug–target prediction as a link prediction task on heterogeneous biomedical knowledge graphs (KG) that integrate drugs, proteins, diseases, pathways, and other relevant entities. Conventional KG embedding methods such as TransE and ComplEx-SE are hindered by their reliance on computationally intensive negative sampling and their limited generalization to unseen drug–target pairs. To address these challenges, we propose Multi-Context-Aware Sampling (MuCoS), a novel framework that prioritizes high-density neighbours to capture salient structural patterns and integrates these with contextual embeddings derived from BERT. By unifying structural and textual modalities and selectively sampling highly informative patterns, MuCoS circumvents the need for negative sampling, significantly reducing computational overhead while enhancing predictive accuracy for novel drug–target associations and drug targets. Extensive experiments on the KEGG50k and PharmKG-8k datasets demonstrate that MuCoS outperforms baselines, achieving up to a 13% improvement in MRR for general relation prediction on KEGG50k, a 22% improvement on PharmKG-8k, and a 6% gain in dedicated drug–target relation prediction on KEGG50k.

## 27. Each graph is a new language: Graph Learning with LLMs

- Authors: Huachi Zhou, Jiahe Du, Chuang Zhou, Chang Yang, Yilin Xiao, Yuxuan Xie, Xiao Huang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2025-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.5018797706005667
- Article: https://aclanthology.org/2025.findings-acl.902/
- PDF: https://aclanthology.org/2025.findings-acl.902.pdf
- Local PDF: pdf/2026-06-15_27_Each graph is a new language_ Graph Learning with LLMs.pdf

GDL4LLM 将图结构视为一种“新语言”，通过把子图翻译成紧凑的图语言语料并对 LLM 进行预训练，使模型能比传统自然语言描述或属性嵌入方法更简洁且更充分地理解高阶邻居关系，并在五个数据集上取得更优表现。

## 28. scPilot: Large Language Model Reasoning Toward Automated Single-Cell Analysis and Discovery

- Authors: Gao, Yiming, Wang, Zhen, Chen, Jefferson, Antkowiak, Mark, Hu, Mengzhou, Kong, JungHo, Pratt, Dexter, Liu, Jieyuan, Ma, Enze, Hu, Zhiting, Xing, Eric
- Source: neurips
- Venue type: conference
- Journal: NeurIPS 2025
- Publication status: formally_published
- Publication date: 2026-04-23
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.4916532806080407
- Article: https://proceedings.neurips.cc/paper_files/paper/2025/hash/01dde7941bce255c2a061eef4fbb7fad-Abstract-Conference.html
- PDF: https://proceedings.neurips.cc/paper_files/paper/2025/file/01dde7941bce255c2a061eef4fbb7fad-Paper-Conference.pdf
- Local PDF: pdf/2026-06-15_28_scPilot_ Large Language Model Reasoning Toward Automated Single-Cell Analysis and Discovery.pdf

scPilot 提出了一种让大语言模型直接结合单细胞 RNA 测序数据与生物信息工具进行“组学原生推理”的系统框架，可通过迭代、可解释的步骤式分析提升细胞类型注释、发育轨迹重建和转录因子靶向预测的准确性与可审计性。

## 29. Are LLMs Truly Graph-Savvy? A Comprehensive Evaluation of Graph Generation

- Authors: Ege Demirci, Rithwik Kerur, Ambuj Singh
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2025-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.482873290952689
- Article: https://aclanthology.org/2025.acl-srw.64/
- PDF: https://aclanthology.org/2025.acl-srw.64.pdf
- Local PDF: pdf/2026-06-15_29_Are LLMs Truly Graph-Savvy_ A Comprehensive Evaluation of Graph Generation.pdf

While large language models (LLMs) have demonstrated impressive capabilities across diverse tasks, their ability to generate valid graph structures remains underexplored. We evaluate fifteen state-of-the-art LLMs on five specialized graph generation tasks spanning delivery networks, social networks, quantum circuits, gene-disease networks, and transportation systems. We also test the LLMs using 3 different prompt types: direct, iterative feedback, and program-augmented. Models supported with explicit reasoning modules (o3-mini-high, o1, Claude 3.7 Sonnet, DeepSeek-R1) solve more than twice as many tasks as their general-purpose peers, independent of parameter count. Error forensics reveals two recurring failure modes: smaller parameter size Llama models often violate basic structural constraints, whereas Claude models respect topology but mismanage higher-order logical rules. Allowing models to refine their answers iteratively yields uneven gains, underscoring fundamental differences in error-correction capacity. This work demonstrates that graph competence stems from specialized training methodologies rather than scale, establishing a framework for developing truly graph-savvy language models. Results and verification scripts available at https://github.com/egedemirci/Are-LLMs-Truly-Graph-Savvy-A-Comprehensive-Evaluation-of-Graph-Generation.

## 30. SPOT: Zero-Shot Semantic Parsing Over Property Graphs

- Authors: Francesco Cazzaro, Justin Kleindienst, Sofia Márquez Gomez, Ariadna Quattoni
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2025-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.4676466599875386
- Article: https://aclanthology.org/2025.findings-acl.524/
- PDF: https://aclanthology.org/2025.findings-acl.524.pdf
- Local PDF: pdf/2026-06-15_30_SPOT_ Zero-Shot Semantic Parsing Over Property Graphs.pdf

Knowledge Graphs (KGs) have gained popularity as a means of storing structured data, with property graphs, in particular, gaining traction in recent years. Consequently, the task of semantic parsing remains crucial in enabling access to the information in these graphs via natural language queries. However, annotated data is scarce, requires significant effort to create, and is not easily transferable between different graphs. To address these challenges we introduce SPOT, a method to generate training data for semantic parsing over Property Graphs without human annotations. We generate tree patterns, match them to the KG to obtain a query program, and use a finite-state transducer to produce a proto-natural language realization of the query. Finally, we paraphrase the proto-NL with an LLM to generate samples for training a semantic parser. We demonstrate the effectiveness of SPOT on two property graph benchmarks utilizing the Cypher query language. In addition, we show that our approach can also be applied effectively to RDF graphs.
