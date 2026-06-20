# Paper Daily Reading - 2026-06-20

## 1. SPADE: A Deep Learning Framework for Spatial Mapping and Quantitative Cell–Cell Interaction Inference

- Authors: Xinyi Li, Ning Zhang, Zijie Jin
- Source: openalex
- Venue type: journal
- Journal: Advanced Science
- Publication status: published
- Publication date: 2026-06-18
- DOI: https://doi.org/10.1002/advs.76142
- Categories: Single-cell and spatial transcriptomics, Cell Image Analysis Techniques, Cancer Cells and Metastasis
- Relevance: 3.608546056859907
- Article: https://doi.org/10.1002/advs.76142
- PDF: Unavailable
- Local PDF: Not downloaded

ABSTRACT Spatial transcriptomics (ST) enables the study of tissue architecture by resolving gene expression in space, but current ST platforms are constrained by limited sequencing depth and indirect single‐cell identification. Existing deconvolution methods that integrate single‐cell RNA sequencing (scRNA‐seq) data with ST often overlook the biological principle that cells in communication with each other tend to be closer spatially. Here we introduce SPADE, a deep learning framework that aligns scRNA‐seq data to spatial locations by jointly modeling expression similarity between scRNA‐seq and ST data and concordance between the spot distance and cell–cell communication (CCC) patterns. SPADE also enables quantitative characterization of CCC across spots and regions. Evaluations on 55 simulated and real datasets show that SPADE achieves strong performance in recovering region‐specific cell‐type patterns and enhancing spatial gene expression profiles compared with existing methods. In the breast cancer datasets, SPADE demonstrates a unique advantage in identifying tumor‐infiltrating immune cells and tertiary lymphoid structures. In the colorectal cancer liver metastasis dataset, SPADE distinguishes tumor heterogeneity with region‐specific CCC events and describes the general CCC landscape in the tissue. Overall, SPADE highlights the key role of spatially constrained CCC in shaping tissue organization and enables biological interpretation of spatial transcriptomics data.

## 2. Detecting Hallucinations for Large Language Model-based Knowledge Graph Reasoning

- Authors: Xinyan Zhu, Yaoqi Liu, Yue Gao, Huadong Ma, Cheng Yang, Chuan Shi
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-04-27
- DOI: Unavailable
- Categories: cs.CL, cs.AI
- Relevance: 3.29883629986403
- Article: http://arxiv.org/abs/2606.19351v1
- PDF: https://arxiv.org/pdf/2606.19351v1
- Local PDF: pdf/2026-06-20_02_Detecting Hallucinations for Large Language Model-based Knowledge Graph Reasoning.pdf

Knowledge graph (KG) reasoning infers new knowledge from existing facts and is widely applied in question answering, recommendation, and decision support. With the rapid development of large language models (LLMs), LLM-based KG reasoning frameworks have become increasingly popular by leveraging retrieved KG information. However, hallucinations in LLMs remain a critical issue. Even when relevant KG knowledge is incorporated, models may still generate incorrect outputs, leading to misinformation and unreliable decisions. Existing hallucination detection methods either focus on LLM internal states or verify consistency with retrieved contexts, but both overlook the structural information in KGs, resulting in suboptimal performance. To address this gap, we propose LUCID, the first halLUcination deteCtIon method for LLM-based knowleDge graph reasoning frameworks. LUCID jointly leverages LLM attention scores, KG semantics, and structural information. Specifically, it extracts node and edge features from attention scores and semantic similarities, and integrates them with KG structure using a graph neural network. We also construct manually annotated benchmark datasets for evaluation. Experiments on nine datasets show that LUCID achieves state of the art performance compared to 15 baselines.

## 3. FineREX: Fine-Tuned NER-RE for Human Smuggling Knowledge Graphs

- Authors: Elijah Feldman, Dipak Meher, Carlotta Domeniconi
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-06-18
- DOI: Unavailable
- Categories: cs.CL, cs.AI
- Relevance: 3.235798328155947
- Article: http://arxiv.org/abs/2606.19710v1
- PDF: https://arxiv.org/pdf/2606.19710v1
- Local PDF: pdf/2026-06-20_03_FineREX_ Fine-Tuned NER-RE for Human Smuggling Knowledge Graphs.pdf

Court proceedings contain valuable evidence about human smuggling networks, but this information is often buried within unstructured, jargon-heavy legal documents. While large language models (LLMs) can support knowledge graph construction through automated information extraction, existing approaches rely on general-purpose models that are not tailored to the entity and relationship definitions required in this domain. We introduce FineREX, a streamlined knowledge graph construction pipeline built around a fine-tuned LLM for named entity recognition and relationship extraction (NER-RE). Using a manually annotated dataset of $512$ text chunks, FineREX achieves absolute improvements of 15.50% and 31.46% in entity and relationship F1-score, respectively, compared to a larger general-purpose baseline. These gains translate into higher-quality knowledge graphs, reducing legal noise by nearly half and lowering node duplication on long documents from 17.78% to 11.17%. By eliminating document rewriting and redundant extraction stages, FineREX also reduces end-to-end processing time by 50.0%. Our results demonstrate that domain-specific fine-tuning can substantially outperform larger general-purpose models while improving both the quality and efficiency of knowledge graph construction for illicit network analysis.

## 4. Visual Bridge: Universal Visual Perception Representations Generating

- Authors: Yilin Gao, Shuguang Dou, Junzhou Li, Zhiheng Yu, Yin Li, Dongsheng Jiang, Shugong Xu
- Source: openalex
- Venue type: conference
- Journal: Proceedings of the AAAI Conference on Artificial Intelligence
- Publication status: formally_published
- Publication date: 2026-03-14
- DOI: https://doi.org/10.1609/aaai.v40i25.39268
- Categories: Multimodal Machine Learning Applications, Generative Adversarial Networks and Image Synthesis, Domain Adaptation and Few-Shot Learning
- Relevance: 3.186882607403562
- Article: https://doi.org/10.1609/aaai.v40i25.39268
- PDF: Unavailable
- Local PDF: Not downloaded

Recent advances in diffusion models have achieved remarkable success in isolated computer vision tasks such as text-to-image generation, depth estimation, and optical flow. However, these models are often restricted by a ``single-task-single-model'' paradigm, severely limiting their generalizability and scalability in multi-task scenarios. Motivated by the cross-domain generalization ability of large language models, we propose a universal visual perception framework based on flow matching that can generate diverse visual representations across multiple tasks. Our approach formulates the process as a universal flow-matching problem from image patch tokens to task-specific representations rather than an independent generation or regression problem. By leveraging a strong self-supervised foundation model as the anchor and introducing a multi-scale, circular task embedding mechanism, our method learns a universal velocity field to bridge the gap between heterogeneous tasks, supporting efficient and flexible representation transfer. Extensive experiments on classification, detection, segmentation, depth estimation, and image-text retrieval demonstrate that our model achieves competitive performance in both zero-shot and fine-tuned settings, outperforming prior generalist and several specialist models. Ablation studies further validate the robustness, scalability, and generalization of our framework. Our work marks a significant step towards general-purpose visual perception, providing a solid foundation for future research in universal vision modeling.

## 5. Virtual Multiplex Staining for Histological Images Using a Marker-Wise Conditioned Diffusion Model

- Authors: Hyun-Jic Oh, Junsik Kim, Zhiyi Shi, Yichen Wu, Yu-An Chen, Peter K. Sorger, Hanspeter Pfister, Won‐Ki Jeong
- Source: openalex
- Venue type: conference
- Journal: Proceedings of the AAAI Conference on Artificial Intelligence
- Publication status: formally_published
- Publication date: 2026-03-14
- DOI: https://doi.org/10.1609/aaai.v40i10.37764
- Categories: Cell Image Analysis Techniques, Advanced Neuroimaging Techniques and Applications, Medical Image Segmentation Techniques
- Relevance: 3.183006701595553
- Article: https://doi.org/10.1609/aaai.v40i10.37764
- PDF: Unavailable
- Local PDF: Not downloaded

Multiplex imaging is revolutionizing pathology by enabling the simultaneous visualization of multiple biomarkers within tissue samples, providing molecular-level insights that traditional hematoxylin and eosin (H&amp;E) staining cannot provide. However, the complexity and cost of multiplex data acquisition have hindered its widespread adoption. Additionally, most existing large repositories of H&amp;E images lack corresponding multiplex images, limiting opportunities for multi-modal analysis. To address these challenges, we leverage recent advances in latent diffusion models (LDMs), which excel at modeling complex data distributions by utilizing their powerful priors for fine-tuning to a target domain. In this paper, we introduce a novel framework for virtual multiplex staining that utilizes pretrained LDM parameters to generate multiplex images from H&amp;E images using a conditional diffusion model. Our approach enables marker-by-marker generation by conditioning the diffusion model on each marker, while sharing the same architecture across all markers. To tackle the challenge of varying pixel value distributions across different marker stains and to improve inference speed, we fine-tune the model for single-step sampling, enhancing both color contrast fidelity and inference efficiency through pixel-level loss functions. We validate our framework on two publicly available datasets, notably demonstrating its effectiveness in generating up to 18 different marker types with improved accuracy, a substantial increase over the 2-3 marker types achieved in previous approaches. This validation highlights the potential of our framework, pioneering virtual multiplex staining. Finally, this paper bridges the gap between H&amp;E and multiplex imaging, potentially enabling retrospective studies and large-scale analyses of existing H&amp;E image repositories.

## 6. Enrich-on-Graph: Query-Graph Alignment for Complex Reasoning with LLM Enriching

- Authors: Songze Li, Zhiqiang Liu, Zhengke Gui, Huajun Chen, Wen Zhang
- Source: acl_anthology
- Venue type: conference
- Journal: EMNLP
- Publication status: formally_published
- Publication date: 2025-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.1744628740178884
- Article: https://aclanthology.org/2025.emnlp-main.390/
- PDF: https://aclanthology.org/2025.emnlp-main.390.pdf
- Local PDF: pdf/2026-06-20_06_Enrich-on-Graph_ Query-Graph Alignment for Complex Reasoning with LLM Enriching.pdf

Large Language Models (LLMs) exhibit strong reasoning capabilities in complex tasks. However, they still struggle with hallucinations and factual errors in knowledge-intensive scenarios like knowledge graph question answering (KGQA). We attribute this to the semantic gap between structured knowledge graphs (KGs) and unstructured queries, caused by inherent differences in their focuses and structures. Existing methods usually employ resource-intensive, non-scalable workflows reasoning on vanilla KGs, but overlook this gap. To address this challenge, we propose a flexible framework, Enrich-on-Graph (EoG), which leverages LLMs’ prior knowledge to enrich KGs, bridge the semantic gap between graphs and queries. EoG enables efficient evidence extraction from KGs for precise and robust reasoning, while ensuring low computational costs, scalability, and adaptability across different methods. Furthermore, we propose three graph quality evaluation metrics to analyze query-graph alignment in KGQA task, supported by theoretical validation of our optimization objectives. Extensive experiments on two KGQA benchmark datasets indicate that EoG can effectively generate high-quality KGs and achieve the state-of-the-art performance.

## 7. Out-of-Distribution Detection via LLM-Guided Outlier Generation for Text-attributed Graph

- Authors: Xiangwei Lv, Mengze Li, Jingyuan Chen, Zhiang Dong, Sirui Han, Beishui Liao
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2025-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.1743495275125855
- Article: https://aclanthology.org/2025.findings-acl.1001/
- PDF: https://aclanthology.org/2025.findings-acl.1001.pdf
- Local PDF: pdf/2026-06-20_07_Out-of-Distribution Detection via LLM-Guided Outlier Generation for Text-attributed Graph.pdf

Text-Attributed Graphs (TAGs), which are characterized with text attributes, are widely used in the real world. When evaluating fully trained models designed for TAG predictions, they may perform significantly unsatisfactory on samples outside the In-Distribution (ID) data, which may raise serious security issues. To tackle it, Out-Of-Distribution (OOD) detection is introduced to the TAGs field, which aims to utilize a detector to classify OOD and ID samples. Recent studies attempt to introduce extra OOD datasets to regularize the detection model. However, due to the vastness of the OOD data space, high-quality OOD samples for training the detector are scarce and difficult to obtain in the real world. Thus, we utilize Large Language Models (LLMs) to generate the OOD training samples with high quality. There are two issues in this process: (1) LLMs tend to generate OOD-node samples significantly different from ID ones, with a limited learning value for OOD and ID relations. (2) Due to the inherent structure of TAGs, obtained OOD nodes need to be integrated with existing nodes by generating edges using LLMs. However, the large number of nodes makes reasoning over each node pair computationally unbearable. Toward these issues, we introduce LLMGuard with challenging OOD-node generation and lightweight edge predictors. Extensive experiments prove the effectiveness of LLMGuard. The source code is available.

## 8. MAKAR: a Multi-Agent framework based Knowledge-Augmented Reasoning for Grounded Multimodal Named Entity Recognition

- Authors: Xinkui Lin, Yuhui Zhang, Yongxiu Xu, Kun Huang, Hongzhang Mu, Yubin Wang, Gaopeng Gou, Li Qian, Li Peng, Wei Liu, Jian Luan, Hongbo Xu
- Source: acl_anthology
- Venue type: conference
- Journal: EMNLP
- Publication status: formally_published
- Publication date: 2025-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.1739863948001403
- Article: https://aclanthology.org/2025.emnlp-main.311/
- PDF: https://aclanthology.org/2025.emnlp-main.311.pdf
- Local PDF: pdf/2026-06-20_08_MAKAR_ a Multi-Agent framework based Knowledge-Augmented Reasoning for Grounded Multimodal Named Entity Recognition.pdf

Grounded Multimodal Named Entity Recognition (GMNER), which aims to extract textual entities, their types, and corresponding visual regions from image-text data, has become a critical task in multimodal information extraction. However, existing methods face two major challenges. First, they fail to address the semantic ambiguity caused by polysemy and the long-tail distribution of datasets. Second, unlike visual grounding which provides descriptive phrases, entity grounding only offers brief entity names which carry less semantic information. Current methods lack sufficient semantic interaction between text and image, hindering accurate entity-visual region matching. To tackle these issues, we propose MAKAR, a Multi-Agent framework based Knowledge-Augmented Reasoning, comprising three agents: Knowledge Enhancement, Entity Correction, and Entity Reasoning Grounding. Specifically, in the named entity recognition phase, the Knowledge Enhancement Agent leverages a Multimodal Large Language Model (MLLM) as an implicit knowledge base to enhance ambiguous image-text content with its internal knowledge. For samples with low-confidence entity boundaries and types, the Entity Correction Agent uses web search tools to retrieve and summarize relevant web content, thereby correcting entities using both internal and external knowledge. In the entity grounding phase, the Entity Reasoning Grounding Agent utilizes multi-step Chain-of-Thought reasoning to perform grounding for each entity. Extensive experiments show that MAKAR achieves state-of-the-art performance on two benchmark datasets. Code is available at: https://github.com/Nikol-coder/MAKAR.

## 9. ESCA: Contextualizing Embodied Agents via Scene-Graph Generation

- Authors: Huang, Jiani, Sethi, Amish, Kuo, Matthew, Keoliya, Mayank, Velingker, Neelay, Jung, JungHo, Lim, Ser Nam, Li, Ziyang, Naik, Mayur
- Source: neurips
- Venue type: conference
- Journal: NeurIPS 2025
- Publication status: formally_published
- Publication date: 2026-04-23
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.173631932197491
- Article: https://proceedings.neurips.cc/paper_files/paper/2025/hash/0418973e545b932939302cb605d06f43-Abstract-Conference.html
- PDF: https://proceedings.neurips.cc/paper_files/paper/2025/file/0418973e545b932939302cb605d06f43-Paper-Conference.pdf
- Local PDF: pdf/2026-06-20_09_ESCA_ Contextualizing Embodied Agents via Scene-Graph Generation.pdf

Multi-modal large language models (MLLMs) are making rapid progress toward general-purpose embodied agents. However, existing MLLMs do not reliably capture fine-grained links between low-level visual features and high-level textual semantics, leading to weak grounding and inaccurate perception. To overcome this challenge, we propose ESCA, a framework that contextualizes embodied agents by grounding their perception in spatial-temporal scene graphs. At its core is SGCLIP, a novel, open-domain, promptable foundation model for generating scene graphs that is based on CLIP. SGCLIP is trained on 87K+ open-domain videos using a neurosymbolic pipeline that aligns automatically generated captions with scene graphs produced by the model itself, eliminating the need for human-labeled annotations. We demonstrate that SGCLIP excels in both prompt-based inference and task-specific fine-tuning, achieving state-of-the-art results on scene graph generation and action localization benchmarks. ESCA with SGCLIP improves perception for embodied agents based on both open-source and commercial MLLMs, achieving state of-the-art performance across two embodied environments. Notably, ESCA significantly reduces agent perception errors and enables open-source models to surpass proprietary baselines. We release the source code for SGCLIP model training at https://github.com/video-fm/LASER and for the embodied agent at https://github.com/video-fm/ESCA.

## 10. GraphCheck: Breaking Long-Term Text Barriers with Extracted Knowledge Graph-Powered Fact-Checking

- Authors: Yingjian Chen, Haoran Liu, Yinhong Liu, Jinxiang Xie, Rui Yang, Han Yuan, Yanran Fu, Peng Yuan Zhou, Qingyu Chen, James Caverlee, Irene Li
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2025-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.1674215004032167
- Article: https://aclanthology.org/2025.acl-long.729/
- PDF: https://aclanthology.org/2025.acl-long.729.pdf
- Local PDF: pdf/2026-06-20_10_GraphCheck_ Breaking Long-Term Text Barriers with Extracted Knowledge Graph-Powered Fact-Checking.pdf

Large language models (LLMs) are widely used, but they often generate subtle factual errors, especially in long-form text. These errors are fatal in some specialized domains such as medicine. Existing fact-checking with grounding documents methods face two main challenges: (1) they struggle to understand complex multihop relations in long documents, often overlooking subtle factual errors; (2) most specialized methods rely on pairwise comparisons, requiring multiple model calls, leading to high resource and computational costs. To address these challenges, we propose GraphCheck, a fact-checking framework that uses extracted knowledge graphs to enhance text representation. Graph Neural Networks further process these graphs as a soft prompt, enabling LLMs to incorporate structured knowledge more effectively. Enhanced with graph-based reasoning, GraphCheck captures multihop reasoning chains that are often overlooked by existing methods, enabling precise and efficient fact-checking in a single inference call. Experimental results on seven benchmarks spanning both general and medical domains demonstrate up to a 7.1% overall improvement over baseline models. Notably, GraphCheck outperforms existing specialized fact-checkers and achieves comparable performance with state-of-the-art LLMs, such as DeepSeek-V3 and OpenAI-o1, with significantly fewer parameters.

## 11. TagRouter: Learning Route to LLMs through Tags for Open-Domain Text Generation Tasks

- Authors: Zhou Chen, Zhiqiang Wei, Yuqi Bai, Xue Xiong, Jianmin Wu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2025-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.1669431791141456
- Article: https://aclanthology.org/2025.findings-acl.1110/
- PDF: https://aclanthology.org/2025.findings-acl.1110.pdf
- Local PDF: pdf/2026-06-20_11_TagRouter_ Learning Route to LLMs through Tags for Open-Domain Text Generation Tasks.pdf

Model routing allocates queries to the suitable model, improving system performance while reducing costs. However, existing routing methods face practical limitations that hinder scalability in large-scale applications and struggle to keep up with the rapid growth of the large language model (LLM) ecosystem. To tackle these challenges, we propose TagRouter, a training-free model routing method designed to optimize the synergy among multiple LLMs for open-domain text generation tasks. Experimental results demonstrate that TagRouter outperforms 13 baseline methods, increasing the accept rate of system by 6.15% and reducing costs by 17.20%, achieving optimal cost-efficiency. Our findings provides the LLM community with an efficient and scalable solution for model ensembling, offering users an evolvable “super model.”

## 12. Human Cognition Inspired RAG with Knowledge Graph for Complex Problem Solving

- Authors: Yao Cheng, Yibo Zhao, Jiapeng Zhu, Yao Liu, Xing Sun, Xiang Li
- Source: openalex
- Venue type: conference
- Journal: Proceedings of the AAAI Conference on Artificial Intelligence
- Publication status: formally_published
- Publication date: 2026-03-14
- DOI: https://doi.org/10.1609/aaai.v40i36.40291
- Categories: Advanced Graph Neural Networks, Multimodal Machine Learning Applications, Topic Modeling
- Relevance: 3.166374549184602
- Article: https://doi.org/10.1609/aaai.v40i36.40291
- PDF: Unavailable
- Local PDF: Not downloaded

Large Language Models (LLMs) have demonstrated significant potential across various domains. However, they often struggle with integrating external knowledge and performing complex reasoning, leading to hallucinations and unreliable outputs. Retrieval Augmented Generation (RAG) has emerged as a promising paradigm to mitigate these issues by incorporating external knowledge. Yet, conventional RAG approaches, especially those based on vector similarity, fail to effectively capture relational dependencies and support multi-step reasoning. In this work, we propose CogGRAG, a human cognition-inspired, graph-based RAG framework designed for Knowledge Graph Question Answering (KGQA). CogGRAG models the reasoning process as a tree-structured mind map that decomposes the original problem into interrelated subproblems and explicitly encodes their semantic relationships. This structure not only provides a global view to guide subsequent retrieval and reasoning but also enables self-consistent verification across reasoning paths. The framework operates in three stages: (1) top-down problem decomposition via mind map construction, (2) structured retrieval of both local and global knowledge from external Knowledge Graphs (KGs), and (3) bottom-up reasoning with dual-process self-verification. Unlike previous tree-based decomposition methods such as MindMap or Graph-CoT, CogGRAG unifies problem decomposition, knowledge retrieval, and reasoning under a single graph-structured cognitive framework, allowing early integration of relational knowledge and adaptive verification. Extensive experiments demonstrate that CogGRAG achieves superior accuracy and reliability compared to existing methods.

## 13. Relink: Constructing Query-Driven Evidence Graph On-the-Fly for GraphRAG

- Authors: Manzong Huang, Chenyang Bu, Yi He, Xingrui Zhuo, Xindong Wu
- Source: openalex
- Venue type: conference
- Journal: Proceedings of the AAAI Conference on Artificial Intelligence
- Publication status: formally_published
- Publication date: 2026-03-14
- DOI: https://doi.org/10.1609/aaai.v40i37.40382
- Categories: Topic Modeling, Advanced Graph Neural Networks, Multimodal Machine Learning Applications
- Relevance: 3.166130777318043
- Article: https://doi.org/10.1609/aaai.v40i37.40382
- PDF: https://ojs.aaai.org/index.php/AAAI/article/download/40382/44343
- Local PDF: Not downloaded

Graph-based Retrieval-Augmented Generation (GraphRAG) mitigates hallucinations in Large Language Models (LLMs) by grounding them in structured knowledge. However, current GraphRAG methods are constrained by a prevailing build-then-reason paradigm, which relies on a static, pre-constructed Knowledge Graph (KG). This paradigm faces two critical challenges. First, the KG's inherent incompleteness often breaks reasoning paths. Second, the graph’s low signal-to-noise ratio introduces distractor facts, presenting query-relevant but misleading knowledge that disrupts the reasoning process. To address these challenges, we argue for a reason-and-construct paradigm and propose Relink, a framework that dynamically builds a query-specific evidence graph. To tackle incompleteness, Relink instantiates required facts from a latent relation pool derived from the original text corpus, repairing broken paths on the fly. To handle misleading or distractor facts, Relink employs a unified, query-aware evaluation strategy that jointly considers candidates from both the KG and latent relations, selecting those most useful for answering the query rather than relying on their pre-existence. This empowers Relink to actively discard distractor facts and construct the most faithful and precise evidence path for each query. Extensive experiments on five Open-Domain Question Answering benchmarks show that Relink achieves significant average improvements of 5.4% in EM and 5.2% in F1 over leading GraphRAG baselines, demonstrating the superiority of our proposed framework.

## 14. RSCF: Relation-Semantics Consistent Filter for Entity Embedding of Knowledge Graph

- Authors: Junsik Kim, Jinwook Park, Kangil Kim
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2025-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.165246112851973
- Article: https://aclanthology.org/2025.acl-long.602/
- PDF: https://aclanthology.org/2025.acl-long.602.pdf
- Local PDF: pdf/2026-06-20_14_RSCF_ Relation-Semantics Consistent Filter for Entity Embedding of Knowledge Graph.pdf

In knowledge graph embedding, leveraging relation specific entity transformation has markedly enhanced performance. However, the consistency of embedding differences before and after transformation remains unaddressed, risking the loss of valuable inductive bias inherent in the embeddings. This inconsistency stems from two problems. First, transformation representations are specified for relations in a disconnected manner, allowing dissimilar transformations and corresponding entity embeddings for similar relations. Second, a generalized plug-in approach as a SFBR (Semantic Filter Based on Relations) disrupts this consistency through excessive concentration of entity embeddings under entity-based regularization, generating indistinguishable score distributions among relations. In this paper, we introduce a plug-in KGE method, Relation-Semantics Consistent Filter (RSCF). Its entity transformation has three features for enhancing semantic consistency: 1) shared affine transformation of relation embeddings across all relations, 2) rooted entity transformation that adds an entity embedding to its change represented by the transformed vector, and 3) normalization of the change to prevent scale reduction. To amplify the advantages of consistency that preserve semantics on embeddings, RSCF adds relation transformation and prediction modules for enhancing the semantics. In knowledge graph completion tasks with distance-based and tensor decomposition models, RSCF significantly outperforms state-of-the-art KGE methods, showing robustness across all relations and their frequencies.

## 15. Unsupervised Causal Abstractions Discovery

- Authors: Théo Saulus, Simon Lacoste-Julien, Dhanya Sridhar
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-06-17
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.1639960120612654
- Article: http://arxiv.org/abs/2606.19594v1
- PDF: https://arxiv.org/pdf/2606.19594v1
- Local PDF: pdf/2026-06-20_15_Unsupervised Causal Abstractions Discovery.pdf

Causal abstractions formalize when a high-level structural causal model (SCM) captures the interventional behavior of a lower-level SCM. Existing applications of this notion largely follow a hypothesis-testing paradigm: an expert proposes a candidate high-level model and then evaluates if the low-level system implements it. We study the complementary problem of learning a high-level model directly from low-level measurements. Our contributions leverage hypotheses from low-rank causal discovery, and can be summarized as follows: (1) we show that observations generated by a low-rank graph induce latents that form a causal abstraction, (2) we provide identifiability results about these latents, and (3) we propose a practical objective to learn this high-level SCM.

## 16. Mixture of Length and Pruning Experts for Knowledge Graphs Reasoning

- Authors: Enjun Du, Siyi Liu, Yongqi Zhang
- Source: acl_anthology
- Venue type: conference
- Journal: EMNLP
- Publication status: formally_published
- Publication date: 2025-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.1627017592266027
- Article: https://aclanthology.org/2025.emnlp-main.23/
- PDF: https://aclanthology.org/2025.emnlp-main.23.pdf
- Local PDF: pdf/2026-06-20_16_Mixture of Length and Pruning Experts for Knowledge Graphs Reasoning.pdf

Knowledge Graph (KG) reasoning, which aims to infer new facts from structured knowledge repositories, plays a vital role in Natural Language Processing (NLP) systems. Its effectiveness critically depends on constructing informative and contextually relevant reasoning paths. However, existing graph neural networks (GNNs) often adopt rigid, query-agnostic path-exploration strategies, limiting their ability to adapt to diverse linguistic contexts and semantic nuances. To address these limitations, we propose MoKGR , a mixture-of-experts framework that personalizes path exploration through two complementary components: (1) a mixture of length experts that adaptively selects and weights candidate path lengths according to query complexity, providing query-specific reasoning depth; and (2) a mixture of pruning experts that evaluates candidate paths from a complementary perspective, retaining the most informative paths for each query. Through comprehensive experiments on diverse benchmark, MoKGR demonstrates superior performance in both transductive and inductive settings, validating the effectiveness of personalized path exploration in KGs reasoning.

## 17. Structure-aware Domain Knowledge Injection for Large Language Models

- Authors: Kai Liu, Ze Chen, Zhihang Fu, Wei Zhang, Rongxin Jiang, Fan Zhou, Yaowu Chen, Yue Wu, Jieping Ye
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2025-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.162559295803886
- Article: https://aclanthology.org/2025.acl-long.1425/
- PDF: https://aclanthology.org/2025.acl-long.1425.pdf
- Local PDF: pdf/2026-06-20_17_Structure-aware Domain Knowledge Injection for Large Language Models.pdf

This paper introduces a pioneering methodology, termed StructTuning, to efficiently transform foundation Large Language Models (LLMs) into domain specialists. It significantly reduces the training corpus needs to a mere 5% while achieving an impressive 100% of traditional knowledge injection performance. Motivated by structured human education, we propose a novel two-stage strategy for knowledge injection and alignment: Structure-aware Continual Pre-Training (SCPT) and Structure-aware Supervised Fine-Tuning (SSFT). In the SCPT phase, we automatically extract the domain knowledge taxonomy and reorganize the training corpora, enabling LLMs to effectively link textual segments to targeted knowledge points within the taxonomy. In the SSFT phase, we explicitly prompt models to elucidate the underlying knowledge structure in their outputs, leveraging the structured domain insight to address practical problems. Our ultimate method was extensively evaluated across model architectures and scales on LongBench and MMedBench datasets, demonstrating superior performance against other knowledge injection methods. We also explored our method’s scalability across different training corpus sizes, laying the foundation to enhance domain-specific LLMs with better data utilization.

## 18. From Selection to Generation: A Survey of LLM-based Active Learning

- Authors: Yu Xia, Subhojyoti Mukherjee, Zhouhang Xie, Junda Wu, Xintong Li, Ryan Aponte, Hanjia Lyu, Joe Barrow, Hongjie Chen, Franck Dernoncourt, Branislav Kveton, Tong Yu, Ruiyi Zhang, Jiuxiang Gu, Nesreen K. Ahmed, Yu Wang, Xiang Chen, Hanieh Deilamsalehy, Sungchul Kim, Zhengmian Hu, Yue Zhao, Nedim Lipka, Seunghyun Yoon, Ting-Hao Kenneth Huang, Zichao Wang, Puneet Mathur, Soumyabrata Pal, Koyel Mukherjee, Zhehao Zhang, Namyong Park, Thien Huu Nguyen, Jiebo Luo, Ryan A. Rossi, Julian McAuley
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2025-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.161302023980132
- Article: https://aclanthology.org/2025.acl-long.708/
- PDF: https://aclanthology.org/2025.acl-long.708.pdf
- Local PDF: pdf/2026-06-20_18_From Selection to Generation_ A Survey of LLM-based Active Learning.pdf

Active Learning (AL) has been a powerful paradigm for improving model efficiency and performance by selecting the most informative data points for labeling and training. In recent active learning frameworks, Large Language Models (LLMs) have been employed not only for selection but also for generating entirely new data instances and providing more cost-effective annotations. Motivated by the increasing importance of high-quality data and efficient model training in the era of LLMs, we present a comprehensive survey on LLM-based Active Learning. We introduce an intuitive taxonomy that categorizes these techniques and discuss the transformative roles LLMs can play in the active learning loop. We further examine the impact of AL on LLM learning paradigms and its applications across various domains. Finally, we identify open challenges and propose future research directions. This survey aims to serve as an up-to-date resource for researchers and practitioners seeking to gain an intuitive understanding of LLM-based AL techniques and deploy them to new applications.

## 19. LLMSR@XLLM25: A Language Model-Based Pipeline for Structured Reasoning Data Construction

- Authors: Hongrui Xing, Xinzhang Liu, Zhuo Jiang, Zhihao Yang, Yitong Yao, Zihan Wang, Wenmin Deng, Chao Wang, Shuangyong Song, Wang Yang, Zhongjiang He, Yongxiang Li
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2025-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.1575615409841036
- Article: https://aclanthology.org/2025.xllm-1.31/
- PDF: https://aclanthology.org/2025.xllm-1.31.pdf
- Local PDF: pdf/2026-06-20_19_LLMSR@XLLM25_ A Language Model-Based Pipeline for Structured Reasoning Data Construction.pdf

In this paper, we present a novel pipeline for the XLLM Shared Task-III: Large Language Model for Structural Reasoning (LLM-SR). Our pipeline addresses key challenges in automatic process-reward training data construction, such as high manual annotation costs, limited accuracy of large models in structured data processing, and dependency on auxiliary information for validation. To overcome these limitations, we first decompose the construction process into extraction and validation phases. Leveraging model-generated annotations, we produce pseudo-labeled data and iteratively refine model performance. Second, by analyzing structured data patterns, we encode structural constraints into a rule-based module and fine-tune the model with Gradient Reward Policy Optimization (GRPO), significantly improving structured data extraction success rates. Finally, we train the model to generate critical responses that assess evidence-conclusion relationships, thus enhancing validation reliability. Experimental results demonstrate that our pipeline outperforms models with an order of magnitude more parameters and achieves the first position on the task.

## 20. Improving Region Representation Learning from Urban Imagery with Noisy Long-Caption Supervision

- Authors: Yimei Zhang, Guojiang Shen, Kaili Ning, Tongwei Ren, Xuebo Qiu, Mengmeng Wang, Xiangjie Kong
- Source: openalex
- Venue type: conference
- Journal: Proceedings of the AAAI Conference on Artificial Intelligence
- Publication status: formally_published
- Publication date: 2026-03-14
- DOI: https://doi.org/10.1609/aaai.v40i19.38678
- Categories: Multimodal Machine Learning Applications, Human Mobility and Location-Based Analysis, Generative Adversarial Networks and Image Synthesis
- Relevance: 3.1574867340276356
- Article: https://doi.org/10.1609/aaai.v40i19.38678
- PDF: https://ojs.aaai.org/index.php/AAAI/article/download/38678/42640
- Local PDF: Not downloaded

Region representation learning plays a pivotal role in urban computing by extracting meaningful features from unlabeled urban data. Analogous to how perceived facial age reflects an individual's health, the visual appearance of a city serves as its "portrait", encapsulating latent socio-economic and environmental characteristics. Recent studies have explored leveraging Large Language Models (LLMs) to incorporate textual knowledge into imagery-based urban region representation learning. However, two major challenges remain: i) difficulty in aligning fine-grained visual features with long captions, and ii) suboptimal knowledge incorporation due to noise in LLM-generated captions. To address these issues, we propose a novel pre-training framework called UrbanLN that improves Urban region representation learning through Long-text awareness and Noise suppression. Specifically, we introduce an information-preserved stretching interpolation strategy that aligns long captions with fine-grained visual semantics in complex urban scenes. To effectively mine knowledge from LLM-generated captions and filter out noise, we propose a dual-level optimization strategy. At the data level, a multi-model collaboration pipeline automatically generates diverse and reliable captions without human intervention. At the model level, we employ a momentum-based self-distillation mechanism to generate stable pseudo-targets, facilitating robust cross-modal learning under noisy conditions. Extensive experiments across four real-world cities and various downstream tasks demonstrate the superior performance of our UrbanLN.

## 21. Learning with Structure: Computing Consistent Subsets on Structurally-Regular Graphs

- Authors: Aritra Banik, Mano Prakash Parthasarathi, Venkatesh Raman, Diya Roy, Abhishek Sahu
- Source: openalex
- Venue type: conference
- Journal: Proceedings of the AAAI Conference on Artificial Intelligence
- Publication status: formally_published
- Publication date: 2026-03-14
- DOI: https://doi.org/10.1609/aaai.v40i17.38427
- Categories: Advanced Clustering Algorithms Research, Face and Expression Recognition, Machine Learning and Data Classification
- Relevance: 3.1563547225879534
- Article: https://doi.org/10.1609/aaai.v40i17.38427
- PDF: Unavailable
- Local PDF: Not downloaded

The Minimum Consistent Subset (MCS) problem arises naturally in the context of supervised clustering and instance selection. In supervised clustering, one aims to infer a meaningful partitioning of data using a small labeled subset. However, the sheer volume of training data in modern applications poses a significant computational challenge. The MCS problem formalizes this goal: given a labeled dataset X in a metric space, the task is to compute a smallest subset S of X such that every point in X shares its label with at least one of its nearest neighbors in S. Recently, the MCS problem has been extended to graph metrics, where distances are defined by shortest paths. Prior work has shown that MCS remains NP-hard even on simple graph classes like trees, and presented an fixed-parameter tractable (FPT) algorithm parameterized by the number of colors for MCS on trees. This raises the challenge of identifying graph classes that admit algorithms efficient in both input size (n) and the number of colors (c). In this work, we study the Minimum Consistent Subset problem on graphs, focusing on two well-established measures: the vertex cover number (vc) and the neighborhood diversity (nd). Specifically, we design efficient algorithms for graphs exhibiting small vc or small nd, which frequently arise in real-world domains characterized by local sparsity or repetitive structure. These parameters are particularly relevant because they capture structural properties that often correlate with the tractability of otherwise hard problems. Graphs with small vertex cover sizes are "almost independent sets", representing sparse interactions, while graphs with small neighborhood diversity exhibit a high degree of symmetry and regularity. Importantly, small neighborhood diversity can occur even in dense graphs, a property frequently observed in domains such as social networks with modular communities or knowledge graphs with repeated relational patterns. Thus, algorithms designed to work efficiently for graphs with small neighborhood diversity are capable of efficiently solving MCS in complex settings where small vertex covers may not exist. We show that MCS is FPT when parameterized by the vertex cover number and by neighborhood diversity. In each case, we present an algorithm whose running time is polynomial in n and c, and the non-polynomial part depends solely on the chosen parameter. Notably, our algorithms remain efficient for arbitrarily many colors, as their complexity is polynomially dependent on the number of colors.

## 22. Ask in Any Modality: A Comprehensive Survey on Multimodal Retrieval-Augmented Generation

- Authors: Mohammad Mahdi Abootorabi, Amirhosein Zobeiri, Mahdi Dehghani, Mohammadali Mohammadkhani, Bardia Mohammadi, Omid Ghahroodi, Mahdieh Soleymani Baghshah, Ehsaneddin Asgari
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2025-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.15477360497625
- Article: https://aclanthology.org/2025.findings-acl.861/
- PDF: https://aclanthology.org/2025.findings-acl.861.pdf
- Local PDF: pdf/2026-06-20_22_Ask in Any Modality_ A Comprehensive Survey on Multimodal Retrieval-Augmented Generation.pdf

Large Language Models (LLMs) suffer from hallucinations and outdated knowledge due to their reliance on static training data. Retrieval-Augmented Generation (RAG) mitigates these issues by integrating external dynamic information for improved factual grounding. With advances in multimodal learning, Multimodal RAG extends this approach by incorporating multiple modalities such as text, images, audio, and video to enhance the generated outputs. However, cross-modal alignment and reasoning introduce unique challenges beyond those in unimodal RAG. This survey offers a structured and comprehensive analysis of Multimodal RAG systems, covering datasets, benchmarks, metrics, evaluation, methodologies, and innovations in retrieval, fusion, augmentation, and generation. We review training strategies, robustness enhancements, loss functions, and agent-based approaches, while also exploring the diverse Multimodal RAG scenarios. In addition, we outline open challenges and future directions to guide research in this evolving field. This survey lays the foundation for developing more capable and reliable AI systems that effectively leverage multimodal dynamic external knowledge bases. All resources are publicly available at https://github.com/llm-lab-org/Multimodal-RAG-Survey.

## 23. RAG-Enhanced Collaborative LLM Agents for Drug Discovery

- Authors: Namkyeong Lee, Edward De Brouwer, Ehsan Hajiramezanali, Tommaso Biancalani, Chanyoung Park, Gabriele Scalia
- Source: openalex
- Venue type: conference
- Journal: Proceedings of the AAAI Conference on Artificial Intelligence
- Publication status: formally_published
- Publication date: 2026-03-14
- DOI: https://doi.org/10.1609/aaai.v40i1.37020
- Categories: Biomedical Text Mining and Ontologies, Machine Learning in Materials Science, Computational Drug Discovery Methods
- Relevance: 3.153434580255714
- Article: https://doi.org/10.1609/aaai.v40i1.37020
- PDF: https://ojs.aaai.org/index.php/AAAI/article/download/37020/40982
- Local PDF: Not downloaded

Recent advances in large language models (LLMs) have shown great potential to accelerate drug discovery. However, the specialized nature of biochemical data often necessitates costly domain-specific fine-tuning, posing critical challenges. First, it hinders the application of more flexible general-purpose LLMs in cutting-edge drug discovery tasks. More importantly, it limits the rapid integration of the vast amounts of scientific data continuously generated through experiments and research. Compounding these challenges is the fact that real-world scientific questions are typically complex and open-ended, requiring reasoning beyond pattern matching or static knowledge retrieval. To address these challenges, we propose CLADD, a retrieval-augmented generation (RAG)-empowered agentic system tailored to drug discovery tasks. Through the collaboration of multiple LLM agents, CLADD dynamically retrieves information from biomedical knowledge bases, contextualizes query molecules, and integrates relevant evidence to generate responses - all without the need for domain-specific fine-tuning. Crucially, we tackle key obstacles in applying RAG workflows to biochemical data, including data heterogeneity, ambiguity, and multi-source integration. We demonstrate the flexibility and effectiveness of this framework across a variety of drug discovery tasks, showing that it outperforms general-purpose and domain-specific LLMs as well as traditional deep learning approaches.

## 24. LocDiff: Identifying Locations on Earth by Diffusing in the Hilbert Space

- Authors: Wang, Zhangyu, Liu, Zeping, Zhang, Jielu, Zhou, Zhongliang, Cao, Qian, Wu, Nemin, Mu, Lan, Song, Yang, Xie, Yiqun, Lao, Ni, Mai, Gengchen
- Source: neurips
- Venue type: conference
- Journal: NeurIPS 2025
- Publication status: formally_published
- Publication date: 2026-04-23
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.153423089793419
- Article: https://proceedings.neurips.cc/paper_files/paper/2025/hash/011864a6ed5c1e1c8f580f2578985109-Abstract-Conference.html
- PDF: https://proceedings.neurips.cc/paper_files/paper/2025/file/011864a6ed5c1e1c8f580f2578985109-Paper-Conference.pdf
- Local PDF: pdf/2026-06-20_24_LocDiff_ Identifying Locations on Earth by Diffusing in the Hilbert Space.pdf

Image geolocalization is a fundamental yet challenging task, aiming at inferring the geolocation on Earth where an image is taken. State-of-the-art methods employ either grid-based classification or gallery-based image-location retrieval, whose spatial generalizability significantly suffers if the spatial distribution of test images does not align with the choices of grids and galleries. Recently emerging generative approaches, while getting rid of grids and galleries, use raw geographical coordinates and suffer quality losses due to their lack of multi-scale information. To address these limitations, we propose a multi-scale latent diffusion model called LocDiff for image geolocalization. We developed a novel positional encoding-decoding framework called Spherical Harmonics Dirac Delta (SHDD) Representations, which encodes points on a spherical surface (e.g., geolocations on Earth) into a Hilbert space of Spherical Harmonics coefficients and decodes points (geolocations) by mode-seeking on spherical probability distributions. We also propose a novel SirenNet-based architecture (CS-UNet) to learn an image-based conditional backward process in the latent SHDD space by minimizing a latent KL-divergence loss. To the best of our knowledge, LocDiff is the first image geolocalization model that performs latent diffusion in a multi-scale location encoding space and generates geolocations under the guidance of images. Experimental results show that LocDiff can outperform all state-of-the-art grid-based, retrieval-based, and diffusion-based baselines across 5 challenging global-scale image geolocalization datasets, and demonstrates significantly stronger generalizability to unseen geolocations.

## 25. How Do LLMs Acquire New Knowledge? A Knowledge Circuits Perspective on Continual Pre-Training

- Authors: Yixin Ou, Yunzhi Yao, Ningyu Zhang, Hui Jin, Jiacheng Sun, Shumin Deng, Zhenguo Li, Huajun Chen
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2025-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.1530772371200695
- Article: https://aclanthology.org/2025.findings-acl.1021/
- PDF: https://aclanthology.org/2025.findings-acl.1021.pdf
- Local PDF: pdf/2026-06-20_25_How Do LLMs Acquire New Knowledge_ A Knowledge Circuits Perspective on Continual Pre-Training.pdf

Despite exceptional capabilities in knowledge-intensive tasks, Large Language Models (LLMs) face a critical gap in understanding how they internalize new knowledge, particularly how acquired knowledge becomes structurally embedded in their neural computations. We address this issue through the lens of knowledge circuit evolution, identifying computational subgraphs that facilitate knowledge storage and processing. Our systematic analysis of circuit evolution throughout continual pre-training reveals several key findings: (1) the acquisition of new knowledge is influenced by its relevance to pre-existing knowledge; (2) the evolution of knowledge circuits exhibits a distinct phase shift from formation to optimization; (3) the evolution of knowledge circuits follows a deep-to-shallow pattern. These insights not only advance our theoretical understanding of the mechanisms of new knowledge acquisition in LLMs, but also provide potential implications for improving continual pre-training strategies to enhance model performance.

## 26. Zooming from Context to Cue: Hierarchical Preference Optimization for Multi-Image MLLMs

- Authors: Li, Xudong, Zhang, Mengdan, Chen, Peixian, Zheng, Xiawu, Zhang, Yan, Zheng, Jingyuan, Shen, Yunhang, Li, Ke, Fu, Chaoyou, Sun, Xing, Ji, Rongrong
- Source: neurips
- Venue type: conference
- Journal: NeurIPS 2025
- Publication status: formally_published
- Publication date: 2026-04-23
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.1513288024542696
- Article: https://proceedings.neurips.cc/paper_files/paper/2025/hash/007ec2ca7a2079de8e7e45102d9f0feb-Abstract-Conference.html
- PDF: https://proceedings.neurips.cc/paper_files/paper/2025/file/007ec2ca7a2079de8e7e45102d9f0feb-Paper-Conference.pdf
- Local PDF: pdf/2026-06-20_26_Zooming from Context to Cue_ Hierarchical Preference Optimization for Multi-Image MLLMs.pdf

Multi-modal Large Language Models (MLLMs) excel at single-image tasks but struggle with multi-image understanding due to cross-modal misalignment, leading to hallucinations (context omission, conflation, and misinterpretation). Existing methods using Direct Preference Optimization (DPO) constrain optimization to a solitary image reference within the input sequence, neglecting holistic context modeling. To address this, we propose Context-to-Cue Direct Preference Optimization (CcDPO), a multi-level preference optimization framework that enhances per-image perception in multi-image settings by zooming into visual clues—from sequential context to local details. Our approach features two sequentially dependent components: (i) Context-Level Optimization: By introducing low-cost sequence preference pairs, we optimize the model to distinguish between complete and disrupted multi-image contexts, thereby correcting cognitive biases in MLLMs’ multi-image understanding. (ii) Needle-Level Optimization: By integrating region-specific visual prompts with multimodal preference supervision, we direct the model’s attention to critical visual details, effectively suppressing perceptual biases toward fine-grained visual information. To support scalable optimization, we also construct MultiScope-42k, an automatically generated multi-image dataset with hierarchical preference pairs. Experiments show that CcDPO significantly reduces hallucinations and yields consistent performance gains across general single- and multi-image tasks. Codes are available at https://github.com/LXDxmu/CcDPO.

## 27. Graph of Records: Boosting Retrieval Augmented Generation for Long-context Summarization with Graphs

- Authors: Haozhen Zhang, Tao Feng, Jiaxuan You
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2025-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.1487275358300564
- Article: https://aclanthology.org/2025.acl-long.1159/
- PDF: https://aclanthology.org/2025.acl-long.1159.pdf
- Local PDF: pdf/2026-06-20_27_Graph of Records_ Boosting Retrieval Augmented Generation for Long-context Summarization with Graphs.pdf

Retrieval-augmented generation (RAG) has revitalized Large Language Models (LLMs) by injecting non-parametric factual knowledge. Compared with long-context LLMs, RAG is considered an effective summarization tool in a more concise and lightweight manner, which can interact with LLMs multiple times using diverse queries to get comprehensive responses. However, the LLM-generated historical responses, which contain potentially insightful information, are largely neglected and discarded by existing approaches, leading to suboptimal results. In this paper, we propose graph of records ( GoR ), which leverages historical responses generated by LLMs to enhance RAG for long-context global summarization. Inspired by the retrieve-then-generate paradigm of RAG, we construct a graph by establishing an edge between the retrieved text chunks and the corresponding LLM-generated response. To further uncover the intricate correlations between them, GoR features a graph neural network and an elaborately designed BERTScore -based objective for self-supervised model training, enabling seamless supervision signal backpropagation between reference summaries and node embeddings. We comprehensively compare GoR with 12 baselines across four long-context summarization datasets, and the results indicate that our proposed method reaches the best performance ( e.g. , 15%, 8%, and 19% improvement over retrievers w.r.t. Rouge-L, Rouge-1, and Rouge-2 on the WCEP dataset). Extensive experiments further demonstrate the effectiveness of GoR.

## 28. BioHopR: A Benchmark for Multi-Hop, Multi-Answer Reasoning in Biomedical Domain

- Authors: Yunsoo Kim, Yusuf Abdulle, Honghan Wu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2025-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.14809068844625
- Article: https://aclanthology.org/2025.findings-acl.668/
- PDF: https://aclanthology.org/2025.findings-acl.668.pdf
- Local PDF: pdf/2026-06-20_28_BioHopR_ A Benchmark for Multi-Hop, Multi-Answer Reasoning in Biomedical Domain.pdf

Biomedical reasoning often requires traversing interconnected relationships across entities such as drugs, diseases, and proteins. Despite the increasing prominence of large language models (LLMs), existing benchmarks lack the ability to evaluate multi-hop reasoning in the biomedical domain, particularly for queries involving one-to-many and many-to-many relationships. This gap leaves the critical challenges of biomedical multi-hop reasoning underexplored. To address this, we introduce BioHopR, a novel benchmark designed to evaluate multi-hop, multi-answer reasoning in structured biomedical knowledge graphs. Built from the comprehensive PrimeKG, BioHopR includes 1-hop and 2-hop reasoning tasks that reflect real-world biomedical complexities.Evaluations of state-of-the-art models reveal that O3-mini, a proprietary reasoning-focused model, achieves 37.93% precision on 1-hop tasks and 14.57% on 2-hop tasks, outperforming proprietary models such as GPT4O and open-source biomedical models including HuatuoGPT-o1-70B and Llama-3.3-70B. However, all models exhibit significant declines in multi-hop performance, underscoring the challenges of resolving implicit reasoning steps in the biomedical domain. By addressing the lack of benchmarks for multi-hop reasoning in biomedical domain, BioHopR sets a new standard for evaluating reasoning capabilities and highlights critical gaps between proprietary and open-source models while paving the way for future advancements in biomedical LLMs. BioHopR is available at https://huggingface.co/datasets/knowlab-research/BioHopR.

## 29. From Phrases to Subgraphs: Fine-Grained Semantic Parsing for Knowledge Graph Question Answering

- Authors: Yurun Song, Xiangqing Shen, Rui Xia
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2025-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.1472706594020083
- Article: https://aclanthology.org/2025.findings-acl.272/
- PDF: https://aclanthology.org/2025.findings-acl.272.pdf
- Local PDF: pdf/2026-06-20_29_From Phrases to Subgraphs_ Fine-Grained Semantic Parsing for Knowledge Graph Question Answering.pdf

The recent emergence of large language models (LLMs) has brought new opportunities to knowledge graph question answering (KGQA), but also introduces challenges such as semantic misalignment and reasoning noise. Semantic parsing (SP), previously a mainstream approach for KGQA, enables precise graph pattern matching by mapping natural language queries to executable logical forms. However, it faces limitations in scalability and generalization, especially when dealing with complex, multi-hop reasoning tasks.In this work, we propose a Fine-Grained Semantic Parsing (FGSP) framework for KGQA. Our framework constructs a fine-grained mapping library via phrase-level segmentation of historical question-logical form pairs, and performs online retrieval and fusion of relevant subgraph fragments to answer complex queries. This fine-grained, compositional approach ensures tighter semantic alignment between questions and knowledge graph structures, enhancing both interpretability and adaptability to diverse query types. Experimental results on two KGQA benchmarks demonstrate the effectiveness of FGSP, with a notable 18.5% relative F1 performance improvement over the SOTA on the complex multi-hop CWQ dataset. Our code is available at https://github.com/NUSTM/From-Phrases-to-Subgraphs.

## 30. A General Framework to Enhance Fine-tuning-based LLM Unlearning

- Authors: Jie Ren, Zhenwei Dai, Xianfeng Tang, Hui Liu, Jingying Zeng, Zhen Li, Rahul Goutam, Suhang Wang, Yue Xing, Qi He, Hui Liu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2025-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.147193811951286
- Article: https://aclanthology.org/2025.findings-acl.949/
- PDF: https://aclanthology.org/2025.findings-acl.949.pdf
- Local PDF: pdf/2026-06-20_30_A General Framework to Enhance Fine-tuning-based LLM Unlearning.pdf

Unlearning has been proposed to remove copyrighted and privacy-sensitive data from Large Language Models (LLMs). Existing approaches primarily rely on fine-tuning-based methods, which can be categorized into gradient ascent-based (GA-based) and suppression-based methods. However, they often degrade model utility (the ability to respond to normal prompts). In this work, we aim to develop a general framework that enhances the utility of fine-tuning-based unlearning methods. To achieve this goal, we first investigate the common property between GA-based and suppression-based methods. We unveil that GA-based methods unlearn by distinguishing the target data (i.e., the data to be removed) and suppressing related generations—essentially the same strategy employed by suppression-based methods. Inspired by this finding, we introduce Gated Representation UNlearning (GRUN) which has two components: a soft gate function for distinguishing target data and a suppression module using Representation Fine-tuning (ReFT) to adjust representations rather than model parameters. Experiments show that GRUN significantly improves the unlearning and utility. Meanwhile, it is general for fine-tuning-based methods, efficient and promising for sequential unlearning.
