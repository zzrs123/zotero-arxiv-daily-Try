# Paper Daily Reading - 2026-06-21

## 1. Post Hoc Regression Refinement via Pairwise Rankings

- Authors: Wijaya, Kevin Tirta, Sun, Michael, Guo, Minghao, Seidel, Hans-peter, Matusik, Wojciech, Babaei, Vahid
- Source: neurips
- Venue type: conference
- Journal: NeurIPS 2025
- Publication status: formally_published
- Publication date: 2026-04-23
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.1543285480332974
- Article: https://proceedings.neurips.cc/paper_files/paper/2025/hash/00e49fcb98ab1bbf0cdf6cb1cdb84712-Abstract-Conference.html
- PDF: https://proceedings.neurips.cc/paper_files/paper/2025/file/00e49fcb98ab1bbf0cdf6cb1cdb84712-Paper-Conference.pdf
- Local PDF: pdf/2026-06-21_01_Post Hoc Regression Refinement via Pairwise Rankings.pdf

Accurate prediction of continuous properties is essential to many scientific and engineering tasks. Although deep-learning regressors excel with abundant labels, their accuracy deteriorates in data-scarce regimes. We introduce RankRefine, a model-agnostic, plug-and-play post-hoc refinement technique that injects expert knowledge through pairwise rankings. Given a query item and a small reference set with known properties, RankRefine combines the base regressor’s output with a rank-based estimate via inverse-variance weighting, requiring no retraining. In molecular property prediction task, RankRefine achieves up to 10\% relative reduction in mean absolute error using only 20 pairwise comparisons obtained through a general-purpose large language model (LLM) with no finetuning. As rankings provided by human experts or general-purpose LLMs are sufficient for improving regression across diverse domains, RankRefine offers practicality and broad applicability, especially in low-data settings.

## 2. Text is All You Need: LLM-enhanced Incremental Social Event Detection

- Authors: Zitai Qiu, Congbo Ma, Jia Wu, Jian Yang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2025-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.146811700031983
- Article: https://aclanthology.org/2025.acl-long.233/
- PDF: https://aclanthology.org/2025.acl-long.233.pdf
- Local PDF: pdf/2026-06-21_02_Text is All You Need_ LLM-enhanced Incremental Social Event Detection.pdf

Social event detection (SED) is the task of identifying, categorizing, and tracking events from social data sources such as social media posts, news articles, and online discussions. Existing state-of-the-art (SOTA) SED models predominantly rely on graph neural networks (GNNs), which involve complex graph construction and time-consuming training processes, limiting their practicality in real-world scenarios. In this paper, we rethink the key challenge in SED: the informal and noisy nature of short texts on social media platforms, which impacts clustering accuracy. We propose a novel framework, LLM-enhanced Social Event Detection (LSED), which leverages the rich background knowledge of large language models (LLMs) to address this challenge. Specifically, LSED utilizes LLMs to formalize and disambiguate short texts by completing abbreviations and summarizing informal expressions. Furthermore, we introduce hyperbolic space embeddings, which are more suitable for natural language sentence representations, to enhance clustering performance. Extensive experiments on two challenging real-world datasets demonstrate that LSED outperforms existing SOTA models, achieving improvements in effectiveness, efficiency, and stability. Our work highlights the potential of LLMs in SED and provides a practical solution for real-world applications.

## 3. PropRAG: Guiding Retrieval with Beam Search over Proposition Paths

- Authors: Jingjin Wang, Jiawei Han
- Source: acl_anthology
- Venue type: conference
- Journal: EMNLP
- Publication status: formally_published
- Publication date: 2025-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.144444753034472
- Article: https://aclanthology.org/2025.emnlp-main.317/
- PDF: https://aclanthology.org/2025.emnlp-main.317.pdf
- Local PDF: pdf/2026-06-21_03_PropRAG_ Guiding Retrieval with Beam Search over Proposition Paths.pdf

Retrieval Augmented Generation (RAG) has become the standard approach for equipping Large Language Models (LLMs) with up-to-date knowledge. However, standard RAG, relying on independent passage retrieval, often fails to capture the interconnected nature of information required for complex, multi-hop reasoning. While structured RAG methods attempt to address this using knowledge graphs built from triples, we argue that the inherent context loss of triples (context collapse) limits the fidelity of the knowledge representation. We introduce PropRAG, a novel RAG framework that shifts from triples to context-rich propositions and introduces an efficient, LLM-free online beam search over proposition paths to discover multi-step reasoning chains. By coupling a higher-fidelity knowledge representation with explicit path discovery, PropRAG achieves state-of-the-art zero-shot Recall@5 and F1 scores on 2Wiki, HotpotQA, and MuSiQue, advancing non-parametric knowledge integration by improving evidence retrieval through richer representation and efficient reasoning path discovery.

## 4. CADiff: Context-Aware Diffusion for Controllable Anomaly Generation in Anomaly Detection

- Authors: Xuan Tong, Yuxuan Lin, Junxiong Lin, Xinji Mai, Haoran Wang, Zeng Tao, Yang Yao, Ruofan Wang, Wenqiang Zhang
- Source: openalex
- Venue type: conference
- Journal: Proceedings of the AAAI Conference on Artificial Intelligence
- Publication status: formally_published
- Publication date: 2026-03-14
- DOI: https://doi.org/10.1609/aaai.v40i12.37917
- Categories: Anomaly Detection Techniques and Applications, Advanced Malware Detection Techniques, Machine Learning and Data Classification
- Relevance: 3.14130835974551
- Article: https://doi.org/10.1609/aaai.v40i12.37917
- PDF: Unavailable
- Local PDF: Not downloaded

Generating anomalies is a crucial method to enhance detection and classification performance by expanding anomalous data repository. However, existing anomaly generation methods overlook the intrinsic entanglement between diverse anomaly types and product structures, leading to semantic ambiguity. We propose CADiff, a context-aware generation framework that reframes anomalies as compositional perturbations. Firstly, we propose Context-aware Text Prompt (CTP), a mechanism which contains multiple tokens that characterize anomalies and products separately to enhance the contextual consistency of generated images and refine the local variability of anomalies. Secondly, we develop Self-adaptive Spatial Control (SSC), a self-adaptive interaction design that mitigates anomaly leakage or missing phenomena. Thirdly, we introduce Intensity-controllable Attention Re-weighting (IAR), an inference scheduling scheme with the ability to amplify or attenuate abnormal semantic effects to improve generation diversity. Extensive experiments on MVTec AD and VisA datasets demonstrate the superiority of our proposed method over state-of-the-art methods in both realism and diversity of the generated results, and significantly improve the performance of downstream tasks, including anomaly detection, anomaly localization, and anomaly classification tasks.

## 5. MolRAG: Unlocking the Power of Large Language Models for Molecular Property Prediction

- Authors: Ziting Xian, Jiawei Gu, Lingbo Li, Shangsong Liang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2025-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.1406339601894007
- Article: https://aclanthology.org/2025.acl-long.755/
- PDF: https://aclanthology.org/2025.acl-long.755.pdf
- Local PDF: pdf/2026-06-21_05_MolRAG_ Unlocking the Power of Large Language Models for Molecular Property Prediction.pdf

Recent LLMs exhibit limited effectiveness on molecular property prediction task due to the semantic gap between molecular representations and natural language, as well as the lack of domain-specific knowledge. To address these challenges, we propose MolRAG, a Retrieval-Augmented Generation framework integrating Chain-of-Thought reasoning for molecular property prediction. MolRAG operates by retrieving structurally analogous molecules as contextual references to guide stepwise knowledge reasoning through chemical structure-property relationships. This dual mechanism synergizes molecular similarity analysis with structured inference, while generating human-interpretable rationales grounded in domain knowledge. Experimental results show MolRAG outperforms pre-trained LLMs on four datasets, and even matches supervised methods, achieving performance gains of 1.1%–45.7% over direct prediction approaches, demonstrating versatile effectiveness. Our code is available at https://github.com/AcaciaSin/MolRAG.

## 6. CypherBench: Towards Precise Retrieval over Full-scale Modern Knowledge Graphs in the LLM Era

- Authors: Yanlin Feng, Simone Papicchio, Sajjadur Rahman
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2025-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.1384720429938797
- Article: https://aclanthology.org/2025.acl-long.438/
- PDF: https://aclanthology.org/2025.acl-long.438.pdf
- Local PDF: pdf/2026-06-21_06_CypherBench_ Towards Precise Retrieval over Full-scale Modern Knowledge Graphs in the LLM Era.pdf

Retrieval from graph data is crucial for augmenting large language models (LLM) with both open-domain knowledge and private enterprise data, and it is also a key component in the recent GraphRAG system (CITATION). Despite decades of research on knowledge graphs and knowledge base question answering, leading LLM frameworks (Langchain and LlamaIndex) have only minimal support for retrieval from modern encyclopedic knowledge graphs like Wikidata. In this paper, we analyze the root cause and suggest that modern RDF knowledge graphs (Wikidata, Freebase) are less efficient for LLMs due to overly large schemas that far exceed the typical LLM context window, use of resource identifiers, overlapping and ambiguous relation types and lack of normalization. As a solution, we propose property graph views on top of the underlying RDF graph that can be efficiently queried by LLMs using Cypher . We instantiated this idea on Wikidata and introduced CypherBench, the first benchmark with 11 large-scale, multi-domain property graphs with 7.8 million entities and over 10,000 questions. To achieve this, we tackled several key challenges, including developing an RDF-to-property graph conversion engine, creating a systematic pipeline for text-to-Cypher task generation, and designing new evaluation metrics.

## 7. IRIS: An Iterative and Integrated Framework for Verifiable Causal Discovery in the Absence of Tabular Data

- Authors: Tao Feng, Lizhen Qu, Niket Tandon, Gholamreza Haffari
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2025-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.138315178879849
- Article: https://aclanthology.org/2025.acl-long.463/
- PDF: https://aclanthology.org/2025.acl-long.463.pdf
- Local PDF: pdf/2026-06-21_07_IRIS_ An Iterative and Integrated Framework for Verifiable Causal Discovery in the Absence of Tabular Data.pdf

Causal discovery is fundamental to scientific research, yet traditional statistical algorithms face significant challenges, including expensive data collection, redundant computation for known relations, and unrealistic assumptions. While recent LLM-based methods excel at identifying commonly known causal relations, they fail to uncover novel relations. We introduce IRIS (Iterative Retrieval and Integrated System for Real-Time Causal Discovery), a novel framework that addresses these limitations. Starting with a set of initial variables, IRIS automatically collects relevant documents, extracts variables, and uncovers causal relations. Our hybrid causal discovery method combines statistical algorithms and LLM-based methods to discover known and novel causal relations. In addition to causal discovery on initial variables, the missing variable proposal component of IRIS identifies and incorporates missing variables to expand the causal graphs. Our approach enables real-time causal discovery from only a set of initial variables without requiring pre-existing datasets.

## 8. FreeControl: Efficient, Training-Free Structural Control via One-Step Attention Extraction

- Authors: Lin, Jiang, Chen, Xinyu, Wu, Song, Zhang, Zhiqiu, Zhang, Jizhi, Wang, Ye, Tang, Qiang, Wang, Qian, Yang, Jian, Yi, Zili
- Source: neurips
- Venue type: conference
- Journal: NeurIPS 2025
- Publication status: formally_published
- Publication date: 2026-04-23
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.1367604448878788
- Article: https://proceedings.neurips.cc/paper_files/paper/2025/hash/00ed9ab006311be67879ecef8f80d7c5-Abstract-Conference.html
- PDF: https://proceedings.neurips.cc/paper_files/paper/2025/file/00ed9ab006311be67879ecef8f80d7c5-Paper-Conference.pdf
- Local PDF: pdf/2026-06-21_08_FreeControl_ Efficient, Training-Free Structural Control via One-Step Attention Extraction.pdf

Controlling the spatial and semantic structure of diffusion-generated images remains a challenge. Existing methods like ControlNet rely on handcrafted condition maps and retraining, limiting flexibility and generalization. Inversion-based approaches offer stronger alignment but incur high inference cost due to dual-path denoising. We present \textbf{FreeControl}, a training-free framework for semantic structural control in diffusion models. Unlike prior methods that extract attention across multiple timesteps, FreeControl performs \textit{one-step attention extraction} from a single, optimally chosen timestep and reuses it throughout denoising. This enables efficient structural guidance without inversion or retraining. To further improve quality and stability, we introduce \textit{Latent-Condition Decoupling (LCD)}: a principled separation of the timestep condition and the noised latent used in attention extraction. LCD provides finer control over attention quality and eliminates structural artifacts. FreeControl also supports compositional control via reference images assembled from multiple sources, enabling intuitive scene layout design and stronger prompt alignment. FreeControl introduces a new paradigm for test-time control—enabling structurally and semantically aligned, visually coherent generation directly from raw images, with the flexibility for intuitive compositional design and compatibility with modern diffusion models at ~5\% additional cost.

## 9. A Multi-Expert Structural-Semantic Hybrid Framework for Unveiling Historical Patterns in Temporal Knowledge Graphs

- Authors: Yimin Deng, Yuxia Wu, Yejing Wang, Guoshuai Zhao, Li Zhu, Qidong Liu, Derong Xu, Zichuan Fu, Xian Wu, Yefeng Zheng, Xiangyu Zhao, Xueming Qian
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2025-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.133808304575063
- Article: https://aclanthology.org/2025.findings-acl.1056/
- PDF: https://aclanthology.org/2025.findings-acl.1056.pdf
- Local PDF: pdf/2026-06-21_09_A Multi-Expert Structural-Semantic Hybrid Framework for Unveiling Historical Patterns in Temporal Knowledge Graphs.pdf

Temporal knowledge graph reasoning aims to predict future events with knowledge of existing facts and plays a key role in various downstream tasks. Previous methods focused on either graph structure learning or semantic reasoning, failing to integrate dual reasoning perspectives to handle different prediction scenarios. Moreover, they lack the capability to capture the inherent differences between historical and non-historical events, which limits their generalization across different temporal contexts. To this end, we propose a **M**ulti-**E**xpert **S**tructural-**S**emantic **H**ybrid (MESH) framework that employs three kinds of expert modules to integrate both structural and semantic information, guiding the reasoning process for different events. Extensive experiments on three datasets demonstrate the effectiveness of our approach.

## 10. LESA: Learnable LLM Layer Scaling-Up

- Authors: Yifei Yang, Zouying Cao, Xinbei Ma, Yao Yao, Zhi Chen, Libo Qin, Hai Zhao
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2025-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.132663043730001
- Article: https://aclanthology.org/2025.acl-long.1095/
- PDF: https://aclanthology.org/2025.acl-long.1095.pdf
- Local PDF: pdf/2026-06-21_10_LESA_ Learnable LLM Layer Scaling-Up.pdf

Training Large Language Models (LLMs) from scratch requires immense computational resources, making it prohibitively expensive. Model scaling-up offers a promising solution by leveraging the parameters of smaller models to create larger ones. However, existing depth scaling-up methods rely on empirical heuristic rules for layer duplication, which result in poorer initialization and slower convergence during continual pre-training. We propose LESA , a novel learnable method for depth scaling-up. By concatenating parameters from each layer and applying Singular Value Decomposition, we uncover latent patterns between layers, suggesting that inter-layer parameters can be learned. LESA uses a neural network to predict the parameters inserted between adjacent layers, enabling better initialization and faster training. Experiments show that LESA outperforms existing baselines, achieving superior performance with less than half the computational cost during continual pre-training. Extensive analyses demonstrate its effectiveness across different model sizes and tasks.

## 11. Flexible Concept Bottleneck Model

- Authors: Xingbo Du, Qiantong Dou, Lei Fan, Rui Zhang
- Source: openalex
- Venue type: conference
- Journal: Proceedings of the AAAI Conference on Artificial Intelligence
- Publication status: formally_published
- Publication date: 2026-03-14
- DOI: https://doi.org/10.1609/aaai.v40i25.39234
- Categories: Explainable Artificial Intelligence (XAI), Domain Adaptation and Few-Shot Learning, Multimodal Machine Learning Applications
- Relevance: 3.131145093571672
- Article: https://doi.org/10.1609/aaai.v40i25.39234
- PDF: Unavailable
- Local PDF: Not downloaded

Concept bottleneck models (CBMs) improve neural network interpretability by introducing an intermediate layer that maps human-understandable concepts to predictions. Recent work has explored the use of vision-language models (VLMs) to automate concept selection and annotation. However, existing VLM-based CBMs typically require full model retraining when new concepts are involved, which limits their adaptability and flexibility in real-world scenarios, especially considering the rapid evolution of vision-language foundation models. To address these issues, we propose Flexible Concept Bottleneck Model (FCBM), which supports dynamic concept adaptation, including complete replacement of the original concept set. Specifically, we design a hypernetwork that generates prediction weights based on concept embeddings, allowing seamless integration of new concepts without retraining the entire model. In addition, we introduce a modified sparsemax module with a learnable temperature parameter that dynamically selects the most relevant concepts, enabling the model to focus on the most informative features. Extensive experiments on five public benchmarks demonstrate that our method achieves accuracy comparable to state-of-the-art baselines with a similar number of effective concepts. Moreover, the model generalizes well to unseen concepts with just a single epoch of fine-tuning, demonstrating its strong adaptability and flexibility.

## 12. Knowledge Image Matters: Improving Knowledge-Based Visual Reasoning with Multi-Image Large Language Models

- Authors: Guanghui Ye, Huan Zhao, Zhixue Zhao, Xupeng Zha, Yang Liu, Zhihua Jiang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2025-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.1303960188342983
- Article: https://aclanthology.org/2025.acl-long.1063/
- PDF: https://aclanthology.org/2025.acl-long.1063.pdf
- Local PDF: pdf/2026-06-21_12_Knowledge Image Matters_ Improving Knowledge-Based Visual Reasoning with Multi-Image Large Language Models.pdf

We revisit knowledge-based visual reasoning (KB-VR) in light of modern advances in multimodal large language models (MLLMs), and make the following contributions: (i) We propose Visual Knowledge Card (VKC) – a novel image that incorporates not only internal visual knowledge (e.g., scene-aware information) detected from the raw image, but also external world knowledge (e.g., attribute or object knowledge) produced by a knowledge generator; (ii) We present VKC-based Multi-Image Reasoning (VKC-MIR) – a four-stage pipeline which harnesses a state-of-the-art scene perception engine to construct an initial VKC (Stage-1), a powerful LLM to generate relevant domain knowledge (Stage-2), an excellent image editing toolkit to introduce generated knowledge into the updated VKC (Stage-3), and finally, an emerging multi-image MLLM to solve the VKC-enhanced task (Stage-4). By performing experiments on three popular KB-VR benchmarks, our approach achieves new state-of-the-art results compared to previous top-performing models.

## 13. Multimodal Language Models See Better When They Look Shallower

- Authors: Haoran Chen, Junyan Lin, Xinghao Chen, Yue Fan, Jianfeng Dong, Xin Jin, Hui Su, Jinlan Fu, Xiaoyu Shen
- Source: acl_anthology
- Venue type: conference
- Journal: EMNLP
- Publication status: formally_published
- Publication date: 2025-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.1276236928733114
- Article: https://aclanthology.org/2025.emnlp-main.339/
- PDF: https://aclanthology.org/2025.emnlp-main.339.pdf
- Local PDF: pdf/2026-06-21_13_Multimodal Language Models See Better When They Look Shallower.pdf

Multimodal large language models (MLLMs) typically extract visual features from the final layers of a pretrained Vision Transformer (ViT). This widespread deep-layer bias, however, is largely driven by empirical convention rather than principled analysis. While prior studies suggest that different ViT layers capture different types of information—shallower layers focusing on fine visual details and deeper layers aligning more closely with textual semantics, the impact of this variation on MLLM performance remains underexplored. We present the first comprehensive study of visual layer selection for MLLMs, analyzing representation similarity across ViT layers to establish shallow, middle, and deep layer groupings. Through extensive evaluation of MLLMs (1.4B–7B parameters) across 10 benchmarks encompassing 60+ tasks, we find that while deep layers excel in semantic-rich tasks like OCR, shallow and middle layers significantly outperform them on fine-grained visual tasks including counting, positioning, and object localization. Building on these insights, we propose a lightweight feature fusion method that strategically incorporates shallower layers, achieving consistent improvements over both single-layer and specialized fusion baselines. Our work offers the first principled study of visual layer selection in MLLMs, showing that MLLMs can often see better when they look shallower.

## 14. Generating Domain-Specific Knowledge Graphs from Large Language Models

- Authors: Marinela Parović, Ze Li, Jinhua Du
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2025-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.1250279786963016
- Article: https://aclanthology.org/2025.findings-acl.602/
- PDF: https://aclanthology.org/2025.findings-acl.602.pdf
- Local PDF: pdf/2026-06-21_14_Generating Domain-Specific Knowledge Graphs from Large Language Models.pdf

Knowledge graphs (KGs) have been a cornerstone of search and recommendation due to their ability to store factual knowledge about any domain in a structured form enabling easy search and retrieval. Large language models (LLMs) have shown impressive world knowledge across different benchmarks and domains but their knowledge is inconveniently scattered across their billions of parameters. In this paper, we propose a prompt-based method to construct domain-specific KGs by extracting knowledge solely from LLMs’ parameters. First, we use an LLM to create a schema for a specific domain, which contains a set of domain-representative entities and relations. After that, we use the schema to guide the LLM through an iterative data generation process equipped with Chain-of-Verification (CoVe) for increased data quality. Using this method, we construct KGs for two domains: books and landmarks, which we then evaluate against Wikidata, an open-source human-created KG. Our results show that LLMs can generate large domain-specific KGs containing tens of thousands of entities and relations. However, due to the increased hallucination rates as the procedure evolves, the utility of large-scale LLM-generated KGs in practical applications could remain limited.

## 15. Cross-model Transferability among Large Language Models on the Platonic Representations of Concepts

- Authors: Youcheng Huang, Chen Huang, Duanyu Feng, Wenqiang Lei, Jiancheng Lv
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2025-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.1237166961155505
- Article: https://aclanthology.org/2025.acl-long.185/
- PDF: https://aclanthology.org/2025.acl-long.185.pdf
- Local PDF: pdf/2026-06-21_15_Cross-model Transferability among Large Language Models on the Platonic Representations of Concepts.pdf

Understanding the inner workings of Large Language Models (LLMs) is a critical research frontier. Prior research has shown that a single LLM’s concept representations can be captured as steering vectors (SVs), enabling the control of LLM behavior (e.g., towards generating harmful content). Our work takes a novel approach by exploring the intricate relationships between concept representations across different LLMs, drawing an intriguing parallel to Plato’s Allegory of the Cave. In particular, we introduce a linear transformation method to bridge these representations and present three key findings: 1) Concept representations across different LLMs can be effectively aligned using simple linear transformations, enabling efficient cross-model transfer and behavioral control via SVs. 2) This linear transformation generalizes across concepts, facilitating alignment and control of SVs representing different concepts across LLMs. 3) A weak-to-strong transferability exists between LLM concept representations, whereby SVs extracted from smaller LLMs can effectively control the behavior of larger LLMs. Our code is provided in the supplementary file and will be openly released.

## 16. Diffusion Federated Dataset

- Authors: HAHN, SEOKJU, Lee, Junghye
- Source: neurips
- Venue type: conference
- Journal: NeurIPS 2025
- Publication status: formally_published
- Publication date: 2026-04-23
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.11867479989522
- Article: https://proceedings.neurips.cc/paper_files/paper/2025/hash/0408ce33f8491d7248ff732330dacc52-Abstract-Conference.html
- PDF: https://proceedings.neurips.cc/paper_files/paper/2025/file/0408ce33f8491d7248ff732330dacc52-Paper-Conference.pdf
- Local PDF: pdf/2026-06-21_16_Diffusion Federated Dataset.pdf

Diffusion models have demonstrated decent generation quality, yet their deployment in federated learning scenarios remains challenging. Due to data heterogeneity and a large number of parameters, conventional parameter averaging schemes often fail to achieve stable collaborative training of diffusion models. We reframe collaborative synthetic data generation as a cooperative sampling procedure from a mixture of decentralized distributions, each encoded by a pre-trained local diffusion model. This leverages the connection between diffusion and energy-based models, which readily supports compositional generation thereof. Consequently, we can directly obtain refined synthetic dataset, optionally with differential privacy guarantee, even without exchanging diffusion model parameters. Our framework reduces communication overhead while maintaining the generation quality, realized through an unadjusted Langevin algorithm with a convergence guarantee.

## 17. A Comprehensive Graph Framework for Question Answering with Mode-Seeking Preference Alignment

- Authors: Quanwei Tang, Sophia Yat Mei Lee, Junshuang Wu, Dong Zhang, Shoushan Li, Erik Cambria, Guodong Zhou
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2025-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.1171733719993266
- Article: https://aclanthology.org/2025.findings-acl.1108/
- PDF: https://aclanthology.org/2025.findings-acl.1108.pdf
- Local PDF: pdf/2026-06-21_17_A Comprehensive Graph Framework for Question Answering with Mode-Seeking Preference Alignment.pdf

Recent advancements in retrieval-augmented generation (RAG) have enhanced large language models in question answering by integrating external knowledge. However, challenges persist in achieving global understanding and aligning responses with human ethical and quality preferences. To address these issues, we propose GraphMPA, a comprehensive graph-based framework with mode-seeking preference alignment. Our approach constructs a hierarchical document graph using a general similarity measurement, mimicking human cognitive processes for information understanding and synthesis. Additionally, we introduce mode-seeking preference optimization to better align model outputs with human preferences through probability-matching constraints. Extensive experiments on six datasets demonstrate the effectiveness of our GraphMPA.

## 18. mRAKL: Multilingual Retrieval-Augmented Knowledge Graph Construction for Low-Resourced Languages

- Authors: Hellina Hailu Nigatu, Min Li, Maartje Ter Hoeve, Saloni Potdar, Sarah Chasins
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2025-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.1160872112051976
- Article: https://aclanthology.org/2025.findings-acl.678/
- PDF: https://aclanthology.org/2025.findings-acl.678.pdf
- Local PDF: pdf/2026-06-21_18_mRAKL_ Multilingual Retrieval-Augmented Knowledge Graph Construction for Low-Resourced Languages.pdf

Knowledge Graphs represent real-world entities and the relationships between them. Multilingual Knowledge Graph Construction (mKGC) refers to the task of automatically constructing or predicting missing entities and links for knowledge graphs in a multilingual setting. In this work, we reformulate the mKGC task as a Question Answering (QA) task and introduce mRAKL: a Retrieval-Augmented Generation (RAG) based system to perform mKGC. We achieve this by using the head entity and linking relation in a question, and having our model predict the tail entity as an answer. Our experiments focus primarily on two low-resourced languages: Tigrinya and Amharic. We experiment with using higher-resourced languages, Arabic and English, to utilize cross-lingual transfer for mKGC. With a BM25 retriever, we find that the RAG-based approach improves performance over a no-context setting. Further, our ablation studies show that with an idealized retrieval system, mRAKL improves accuracy by up to 4.92 and 8.79 percentage points for Tigrinya and Amharic, respectively.

## 19. HG-InsightLog: Context Prioritization and Reduction for Question Answering with Non-Natural Language Construct Log Data

- Authors: Supriya Bajpai, Athira Gopal, Chandrakant Harjpal, Niraj Kumar
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2025-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.1160004351240254
- Article: https://aclanthology.org/2025.findings-acl.1214/
- PDF: https://aclanthology.org/2025.findings-acl.1214.pdf
- Local PDF: pdf/2026-06-21_19_HG-InsightLog_ Context Prioritization and Reduction for Question Answering with Non-Natural Language Construct Log Data.pdf

Modern IT systems generate vast amounts of log data, which pose challenges for Large Language Models (LLMs) due to their large size, irrelevant entries, and non-Natural Language (non-NL) construct (e.g., domain-specific jargon, error codes, file paths, and abbreviations). Traditional methods like Retrieval-Augmented Generation (RAG) and GraphRAG fail to preserve temporal sequences, handle non-NL for context and entities extraction, and dynamically prioritize query-relevant context. To address these limitations, we propose HG-InsightLog, a novel framework that constructs a multi-entity temporal hypergraph representing log attribute-value pair as nodes and connecting them with hyperedges, capturing critical connections in the data. HG-InsightLog introduces a multi-step query personalization mechanism enhancing the Personalized PageRank algorithm to rank hyperedges based on query relevance and contextual centrality to priortize critical connections. Top ranked hyperedges are extracted and converted back into log formats preserving temporal order and reducing context. Experimental results across multiple datasets demonstrate its superiority over existing methods, enhancing factual, causal, and analytical reasoning. Our approach enables smaller LLMs like LLaMA-8B to perform effective log-based QA. Being model-agnostic and training-free, it scales with evolving open-source LLMs without relying on proprietary systems.

## 20. RSVP: Reasoning Segmentation via Visual Prompting and Multi-modal Chain-of-Thought

- Authors: Yi Lu, Jiawang Cao, Yongliang Wu, Bozheng Li, Licheng Tang, Yangguang Ji, Chong Wu, Jay Wu, Wenbo Zhu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2025-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.1150651981199173
- Article: https://aclanthology.org/2025.acl-long.715/
- PDF: https://aclanthology.org/2025.acl-long.715.pdf
- Local PDF: pdf/2026-06-21_20_RSVP_ Reasoning Segmentation via Visual Prompting and Multi-modal Chain-of-Thought.pdf

Multi-modal Large Language Models (MLLMs) have demonstrated remarkable reasoning capability while lack explicit mechanisms for visual grounding and segmentation, creating a gap between cognitive reasoning and visual perception. To bridge this gap, we introduce Reasoning Segmentation via Visual Prompting (RSVP), a novel framework that unifies multi-step multimodal reasoning with grounded visual understanding. RSVP is a two-stage structuralized framework that integrates reasoning-driven localization with segmentation refinement. In the reasoning stage, RSVP employs multimodal chain-of-thought visual prompts to help MLLMs understand queries and infer targets, generating interpretable region proposals that enhance visual grounding. In segmentation stage, RSVP refines these proposals with a Vision-Language Segmentation Module (VLSM), seamlessly integrates textual and visual cues to produce precise segmentation masks. By explicitly modelling the interaction between multimodal reasoning and segmentation, RSVP introduces a new paradigm for interpretable reasoning segmentation. It exploits MLLMs’ inherent localization capabilities, enabling the models to not only reason about objects but also generate structured visual representations. Our extensive experiments demonstrate that RSVP achieves state-of-the-art performance, surpasses state-of-the-art methods by up to +6.5 gIoU and +9.2 cIoU on ReasonSeg, and achieves 49.7 mAP on SegInW under zero-shot settings. These results validate RSVP as an effective and scalable framework for integrating cognitive reasoning with structured visual understanding.

## 21. Structural Reasoning Improves Molecular Understanding of LLM

- Authors: Yunhui Jang, Jaehyung Kim, Sungsoo Ahn
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2025-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.1039346198334643
- Article: https://aclanthology.org/2025.acl-long.1023/
- PDF: https://aclanthology.org/2025.acl-long.1023.pdf
- Local PDF: pdf/2026-06-21_21_Structural Reasoning Improves Molecular Understanding of LLM.pdf

Recently, large language models (LLMs) have shown significant progress, approaching human perception levels. In this work, we demonstrate that despite these advances, LLMs still struggle to reason using molecular structural information. This gap is critical because many molecular properties, including functional groups, depend heavily on such structural details. To address this limitation, we propose an approach that sketches molecular structures for reasoning. Specifically, we introduce Molecular Structural Reasoning (MSR) framework to enhance the understanding of LLMs by explicitly incorporating the key structural features. We present two frameworks for scenarios where the target molecule is known or unknown. We verify that our MSR improves molecular understanding through extensive experiments.

## 22. Migician: Revealing the Magic of Free-Form Multi-Image Grounding in Multimodal Large Language Models

- Authors: You Li, Heyu Huang, Chi Chen, Kaiyu Huang, Chao Huang, Zonghao Guo, Zhiyuan Liu, Jinan Xu, Yuhua Li, Ruixuan Li, Maosong Sun
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2025-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.1036498100002463
- Article: https://aclanthology.org/2025.findings-acl.512/
- PDF: https://aclanthology.org/2025.findings-acl.512.pdf
- Local PDF: pdf/2026-06-21_22_Migician_ Revealing the Magic of Free-Form Multi-Image Grounding in Multimodal Large Language Models.pdf

The recent advancement of Multimodal Large Language Models (MLLMs) has significantly improved their fine-grained perception of single images and general comprehension across multiple images. However, existing MLLMs still face challenges in achieving precise grounding in complex multi-image scenarios. To address this, we first explore a Chain-of-Thought (CoT) framework that integrates single-image grounding with multi-image comprehension. While partially effective, it remains unstable and struggles to capture abstract visual information due to its non-end-to-end nature. Therefore, we introduce Migician, the first multi-image grounding model capable of performing free-form and accurate grounding across multiple images. To support this, we present the MGrounding-630k dataset, which comprises data for several multi-image grounding tasks derived from existing datasets, along with newly generated free-form grounding instruction-following data. Furthermore, we propose MIG-Bench, a comprehensive benchmark specifically designed for evaluating multi-image grounding capabilities. Experimental results demonstrate that our model achieves significantly superior multi-image grounding capabilities, outperforming the best existing MLLMs by 24.94% and even surpassing much larger 70B models. Our code, model, dataset, and benchmark are fully open-sourced at https://migician-vg.github.io/.

## 23. ToolExpNet: Optimizing Multi-Tool Selection in LLMs with Similarity and Dependency-Aware Experience Networks

- Authors: Zijing Zhang, Zhanpeng Chen, He Zhu, Ziyang Chen, Nan Du, Xiaolong Li
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2025-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.103150139119386
- Article: https://aclanthology.org/2025.findings-acl.811/
- PDF: https://aclanthology.org/2025.findings-acl.811.pdf
- Local PDF: pdf/2026-06-21_23_ToolExpNet_ Optimizing Multi-Tool Selection in LLMs with Similarity and Dependency-Aware Experience Networks.pdf

Tool learning enhances Large Language Models’ (LLMs) dynamic interaction with external tools, improving their ability to solve complex problems. However, current empirical methods, which primarily focus on isolated tools learning, still struggle with accurate multi-tool selection due to issues like confusing similar tools and neglecting dependencies. To address these challenges, we propose the Tool Experience Network (ToolExpNet), which integrates tools and trial-and-error experiences into a network characterized by semantic similarity and dependency relationships. ToolExpNet iteratively conducts simulated experiments using adaptive sampling to explore subtle differences and connections between tools, and summarizes these experiences to provide insightful guidance for LLM tool selection. Our experiments demonstrate that learning the relationships between tools helps achieve more comprehensive tool learning. Evaluations on multiple real-world API datasets show that ToolExpNet effectively addresses common challenges in multi-tool selection, significantly outperforming existing baselines across different foundation LLMs.

## 24. CLIP-MoE: Towards Building Mixture of Experts for CLIP with Diversified Multiplet Upcycling

- Authors: Jihai Zhang, Xiaoye Qu, Tong Zhu, Yu Cheng
- Source: acl_anthology
- Venue type: conference
- Journal: EMNLP
- Publication status: formally_published
- Publication date: 2025-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.1019345918238272
- Article: https://aclanthology.org/2025.emnlp-main.275/
- PDF: https://aclanthology.org/2025.emnlp-main.275.pdf
- Local PDF: pdf/2026-06-21_24_CLIP-MoE_ Towards Building Mixture of Experts for CLIP with Diversified Multiplet Upcycling.pdf

Contrastive Language-Image Pre-training (CLIP) has become a cornerstone in multimodal intelligence. However, recent studies discovered that CLIP can only encode one aspect of the feature space, leading to substantial information loss and indistinctive features. To mitigate this issue, this paper introduces a novel strategy that fine-tunes a series of complementary CLIP models and transforms them into a CLIP-MoE. Specifically, we propose a model-agnostic Diversified Multiplet Upcycling (DMU) framework for CLIP. Instead of training multiple CLIP models from scratch, DMU leverages a pre-trained CLIP and fine-tunes it into a diverse set with highly cost-effective multistage contrastive learning, thus capturing distinct feature subspaces efficiently. To fully exploit these fine-tuned models while minimizing computational overhead, we transform them into a CLIP-MoE, which dynamically activates a subset of CLIP experts, achieving an effective balance between model capacity and computational cost. Comprehensive experiments demonstrate the superior performance of CLIP-MoE across various zero-shot retrieval, zero-shot image classification tasks, and downstream Multimodal Large Language Model (MLLM) benchmarks when used as a vision encoder. Code is available at https://github.com/OpenSparseLLMs/CLIP-MoE.

## 25. LADDER: Language-Driven Slice Discovery and Error Rectification in Vision Classifiers

- Authors: Shantanu Ghosh, Rayan Syed, Chenyu Wang, Vaibhav Choudhary, Binxu Li, Clare B Poynton, Shyam Visweswaran, Kayhan Batmanghelich
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2025-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.1002827928963677
- Article: https://aclanthology.org/2025.findings-acl.1177/
- PDF: https://aclanthology.org/2025.findings-acl.1177.pdf
- Local PDF: pdf/2026-06-21_25_LADDER_ Language-Driven Slice Discovery and Error Rectification in Vision Classifiers.pdf

Slice discovery refers to identifying systematic biases in the mistakes of pre-trained vision models. Current slice discovery methods in computer vision rely on converting input images into sets of attributes and then testing hypotheses about configurations of these pre-computed attributes associated with elevated error patterns. However, such methods face several limitations: 1) they are restricted by the predefined attribute bank; 2) they lack the common sense reasoning and domain-specific knowledge often required for specialized fields radiology; 3) at best, they can only identify biases in image attributes while overlooking those introduced during preprocessing or data preparation. We hypothesize that bias-inducing variables leave traces in the form of language (logs), which can be captured as unstructured text. Thus, we introduce ladder, which leverages the reasoning capabilities and latent domain knowledge of Large Language Models (LLMs) to generate hypotheses about these mistakes. Specifically, we project the internal activations of a pre-trained model into text using a retrieval approach and prompt the LLM to propose potential bias hypotheses. To detect biases from preprocessing pipelines, we convert the preprocessing data into text and prompt the LLM. Finally, ladder generates pseudo-labels for each identified bias, thereby mitigating all biases without requiring expensive attribute annotations.Rigorous evaluations on 3 natural and 3 medical imaging datasets, 200+ classifiers, and 4 LLMs with varied architectures and pretraining strategies – demonstrate that ladder consistently outperforms current methods. Code is available: https://github.com/batmanlab/Ladder .

## 26. FRAG: A Flexible Modular Framework for Retrieval-Augmented Generation based on Knowledge Graphs

- Authors: Zengyi Gao, Yukun Cao, Hairu Wang, Ao Ke, Yuan Feng, S Kevin Zhou, Xike Xie
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2025-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.0994753013629204
- Article: https://aclanthology.org/2025.findings-acl.321/
- PDF: https://aclanthology.org/2025.findings-acl.321.pdf
- Local PDF: pdf/2026-06-21_26_FRAG_ A Flexible Modular Framework for Retrieval-Augmented Generation based on Knowledge Graphs.pdf

To mitigate the hallucination and knowledge deficiency in large language models (LLMs), Knowledge Graph (KG)-based Retrieval-Augmented Generation (RAG) has shown promising potential by utilizing KGs as an external resource to enhance LLM reasoning.However, existing KG-RAG approaches struggle with a trade-off between flexibility and retrieval quality. Modular methods prioritize flexibility by avoiding the use of KG-fine-tuned models during retrieval, leading to fixed retrieval strategies and suboptimal retrieval quality. Conversely, coupled methods embed KG information within models to improve retrieval quality but at the expense of flexibility.In this paper, we propose a novel flexible modular KG-RAG framework, termed FRAG, which synergizes the advantages of both approaches. FRAG estimates the hop range of reasoning paths based solely on the query and classifies it as either simple or complex.To match the complexity of the query, tailored pipelines are applied to ensure efficient and accurate reasoning path retrieval, thus fostering the final reasoning process. By using the query text instead of the KG to infer the structural information of reasoning paths and employing adaptable retrieval strategies, FRAG improves retrieval quality while maintaining flexibility. Moreover, FRAG does not require extra LLM fine-tuning or calls, significantly boosting efficiency and conserving resources. Extensive experiments show that FRAG achieves state-of-the-art performance with high efficiency and low resource consumption. The code for our method is publicly available at https://github.com/gzy02/FRAG.

## 27. GraphIF: Enhancing Multi-Turn Instruction Following for Large Language Models with Relation Graph Prompt

- Authors: Zhenhe Li, Can Lin, Ling Zheng, Wen-Da Wei, Junli Liang, Qi Song
- Source: openalex
- Venue type: conference
- Journal: Proceedings of the AAAI Conference on Artificial Intelligence
- Publication status: formally_published
- Publication date: 2026-03-14
- DOI: https://doi.org/10.1609/aaai.v40i38.40457
- Categories: Topic Modeling, Speech and dialogue systems, Multimodal Machine Learning Applications
- Relevance: 3.098386571172101
- Article: https://doi.org/10.1609/aaai.v40i38.40457
- PDF: https://ojs.aaai.org/index.php/AAAI/article/download/40457/44418
- Local PDF: Not downloaded

Multi-turn instruction following is essential for building intelligent conversational systems that can consistently adhere to instructions across dialogue turns. However, existing approaches to enhancing multi-turn instruction following primarily rely on collecting or generating large-scale multi-turn dialogue datasets to fine-tune large language models (LLMs), which treat each response generation as an isolated task and fail to explicitly incorporate multi-turn instruction following into the optimization objectives. As a result, instruction-tuned LLMs often struggle with complex long-distance constraints. In multi-turn dialogues, relational constraints across turns can be naturally modeled as labeled directed edges, making graph structures particularly suitable for modeling multi-turn instruction following. Despite this potential, leveraging graph structures to enhance the multi-turn instruction following capabilities of LLMs remains unexplored. To bridge this gap, we propose GraphIF, a plug-and-play framework that models multi-turn dialogues as directed relation graphs and leverages graph prompts to enhance the instruction following capabilities of LLMs. GraphIF comprises three key components: (1) an agent-based relation extraction module that captures inter-turn semantic relations via action-triggered mechanisms to construct structured graphs; (2) a relation graph prompt generation module that converts structured graph information into natural language prompts; and (3) a response rewriting module that refines initial LLM outputs using the generated graph prompts. Extensive experiments on two long multi-turn dialogue datasets demonstrate that GraphIF can be seamlessly integrated into instruction-tuned LLMs and leads to significant improvements across all four multi-turn instruction-following evaluation metrics.

## 28. COCO-Tree: Compositional Hierarchical Concept Trees for Enhanced Reasoning in Vision-Language Models

- Authors: Sanchit Sinha, Guangzhi Xiong, Aidong Zhang
- Source: acl_anthology
- Venue type: conference
- Journal: EMNLP
- Publication status: formally_published
- Publication date: 2025-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.0959895218725997
- Article: https://aclanthology.org/2025.emnlp-main.135/
- PDF: https://aclanthology.org/2025.emnlp-main.135.pdf
- Local PDF: pdf/2026-06-21_28_COCO-Tree_ Compositional Hierarchical Concept Trees for Enhanced Reasoning in Vision-Language Models.pdf

Compositional reasoning remains a persistent weakness of modern vision language models (VLMs): they often falter when a task hinges on understanding how multiple objects, attributes, and relations interact within an image. Multiple research works have attempted to improve compositionality performance by creative tricks such as improving prompt structure, chain of thought reasoning, etc. A more recent line of work attempts to impart additional reasoning in VLMs using well-trained Large Language Models (LLMs), which are far superior in linguistic understanding than VLMs to compensate for the limited linguistic prowess of VLMs. However, these approaches are either resource-intensive or do not provide an interpretable reasoning process. In this paper, we present “COCO-Tree” - a novel approach that augments VLM outputs with carefully designed neurosymbolic concept trees learned from LLMs to improve VLM’s linguistic reasoning. COCO-Tree’s beam search-inspired reasoning process boosts compositionality performance and provides a rationale behind VLM predictions. Empirical results on four compositionality benchmarks, Winoground, EqBench, ColorSwap, and SugarCrepe, in seven different open-source VLMs with varying sizes, demonstrate that COCO-Tree significantly improves compositional generalization by 5-10% over baselines.

## 29. CLM-Access: A Specialized Foundation Model for High-Dimensional Single-Cell ATAC-Seq Analysis

- Authors: Ziqiang Liu, Bowen Li, Zhenyu Xu, Yantao Li, Junwei Zhang, Chulin Sha, Xiaolin Li
- Source: openalex
- Venue type: conference
- Journal: Proceedings of the AAAI Conference on Artificial Intelligence
- Publication status: formally_published
- Publication date: 2026-03-14
- DOI: https://doi.org/10.1609/aaai.v40i1.37046
- Categories: Single-cell and spatial transcriptomics, Domain Adaptation and Few-Shot Learning, Machine Learning in Bioinformatics
- Relevance: 3.095383968652292
- Article: https://doi.org/10.1609/aaai.v40i1.37046
- PDF: https://ojs.aaai.org/index.php/AAAI/article/download/37046/41008
- Local PDF: Not downloaded

Inspired by the success of large language models (LLMs) in natural language processing, cell language models (CLMs) have emerged as a promising paradigm to learn cell representations from high-dimensional single-cell data—particularly transcriptomic profiles from scRNA-seq. These foundation models have shown remarkable potential across a variety of downstream applications. However, there remains a lack of foundation models for scATAC-seq data, which measures chromatin accessibility at single-cell level and is critical for decoding epigenetic regulation. Developing such model is considerably more challenging due to the unique characteristics of scATAC-seq data, including the vast number of chromatin regions, lack of standardized annotations, extreme sparsity, and near-binary distributions. To address these challenges, we systematically explore various strategies and propose CLM-Access, a specialized foundation model for scATAC-seq data. CLM-Access incorporates three main innovations: (1) an unified data processing pipeline that maps 2.8 million cells onto an unified reference of over 1 million chromatin regions; (2) a specialized patching and embedding strategy to effectively manage high-dimensional inputs; and (3) a tailored masking and loss function design that preserves fine-grained regional information while enhancing training efficiency and representation quality. With comprehensive benchmarks, we show that CLM-Access significantly outperforms existing methods in key downstream tasks, including batch effect correction, cell type annotation, RNA expression prediction, and multi-modal integration. This work establishes a scalable and interpretable foundation model for single-cell epigenomic analysis and expands the application of CLMs in single-cell research.

## 30. ImageSet2Text: Describing Sets of Images Through Text

- Authors: Piera Riccio, Francesco Galati, Kajetan Schweighofer, Noa Garcia, Nuria M Oliver
- Source: openalex
- Venue type: conference
- Journal: Proceedings of the AAAI Conference on Artificial Intelligence
- Publication status: formally_published
- Publication date: 2026-03-14
- DOI: https://doi.org/10.1609/aaai.v40i11.37826
- Categories: Multimodal Machine Learning Applications, Topic Modeling, Advanced Image and Video Retrieval Techniques
- Relevance: 3.094354698045288
- Article: https://doi.org/10.1609/aaai.v40i11.37826
- PDF: Unavailable
- Local PDF: Not downloaded

In the era of large-scale visual data, understanding collections of images is a challenging yet important task. To this end, we introduce ImageSet2Text, a novel method to automatically generate natural language descriptions of image sets. Based on large language models, visual-question answering chains, an external lexical graph, and CLIP-based verification, ImageSet2Text iteratively extracts key concepts from image subsets and organizes them into a structured concept graph. We conduct extensive experiments evaluating the quality of the generated descriptions in terms of accuracy, completeness, and user satisfaction. We also examine the method's behavior through ablation studies, scalability assessments, and failure analyses. Results demonstrate that ImageSet2Text combines data-driven AI and symbolic representations to reliably summarize large image collections for a wide range of applications.
