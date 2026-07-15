# Paper Daily Reading - 2026-07-15

## 1. UNIT: Unleash Large Language Models Potential for Graph Continual Learning

- Authors: Tairan Huang, Yili Wang, Beibei Hu, Yiting Shi, Qiutong Li, Changlong He, Jianliang Gao
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-11
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 3.7849100942952942
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.10159v1
- PDF: https://arxiv.org/pdf/2607.10159v1
- Local PDF: pdf/2026-07-15_01_UNIT_ Unleash Large Language Models Potential for Graph Continual Learning.pdf

In real-world multimodal web scenarios, graph-structured data often arrives in a streaming manner, making graph continual learning a crucial paradigm for continuously modeling such evolving structures. However, existing graph continual learning methods still face two fundamental challenges. 1) semantic-structural separation, where the graph-based methods excel at modeling topological relationships but neglect deep semantics. 2) imbalanced knowledge transfer, where existing models fail to effectively leverage general knowledge gained from early tasks to benefit subsequent new tasks. To address above issues, we propose a novel framework, \textbf{UN}leash Large Language Models PotentIal for Graph ConTinual Learning (UNIT). By fine-tuning large language model only on the first task, we bridge the distributional gap between the pre-trained LLM corpus and the target task dataset to enhance the adaptability of LLMs for graph-structured tasks. Meanwhile, we propose an uncertain-aware anchor generation mechanism to effectively preserve representative knowledge across tasks, avoiding the neglect of universal knowledge learned from previous tasks. Additionally, we introduce structural confluence modeling to explicitly integrates graph topology information into semantic information, enhancing the collaborative capabilities between semantic understanding and structural modeling. Extensive experiments demonstrate that our proposed method achieves state-of-the-art performance in the graph continual learning task.

## 2. Knowledge Graphs Meet Graph Neural Networks: A Comprehensive Survey

- Authors: Chengcheng Sun, Jiayun Tian, Cheng Zhai, Zhixiao Wang, Yajie Song, Xiaobin Rui, Jian Zhang, Philip S. Yu
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-05-12
- DOI: 10.1145/3814608
- Categories: cs.LG, cs.AI, cs.SI
- Relevance: 3.6979031166189102
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.09666v1
- PDF: https://arxiv.org/pdf/2607.09666v1
- Local PDF: pdf/2026-07-15_02_Knowledge Graphs Meet Graph Neural Networks_ A Comprehensive Survey.pdf

Graph Neural Networks (GNNs) have emerged as a powerful paradigm in Knowledge Graphs (KGs) due to their intrinsic ability to model graph-structured data. However, there remains a lack of a systematic review about GNN-based methodologies across the entire knowledge graph technologies pipeline. To address this gap, we first propose a novel two-level taxonomy framework for GNN-based knowledge graph technologies: the KG technologies pipeline and GNN-based perspective. Specifically, the knowledge graph technologies pipeline covers knowledge graph construction, knowledge graph embedding, knowledge reasoning and knowledge graph applications. Meanwhile, the GNN-based perspective provides a new categorization of knowledge graph technologies with GNN models, such as GCN, GAT, and HGNN. Then, we analyze the advantages of GNN technology based on the characteristics of different tasks in the knowledge graph lifecycle. Furthermore, we detailed review various GNN-based models for knowledge graph following the proposed taxonomy, and summarize strengths and limitations. Finally, we discuss unresolved challenges and outline promising directions for future research.

## 3. Surprisingly Simple and Effective Multi-Domain Graph Foundation Model through Graph-to-Table Alignment

- Authors: Chunyu Hu, Tianyin Liao, Ge Lan, Xingxuan Zhang, Jianxin Li, Peng Cui, Ziwei Zhang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-13
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.696376810066333
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.11374v1
- PDF: https://arxiv.org/pdf/2607.11374v1
- Local PDF: pdf/2026-07-15_03_Surprisingly Simple and Effective Multi-Domain Graph Foundation Model through Graph-to-Table Alignment.pdf

Graph Foundation Models (GFMs) have emerged as a promising paradigm for learning transferable representations across diverse graph domains. Recent advancements in GFMs have been largely dominated by two paradigms: Graph Neural Network and Large Language Model (LLM) based methods. However, these methods often face a fundamental dilemma between training with limited data and a heavy reliance on textual attributes. Tabular foundation models (TFMs) offer a potential alternative, as node features and representations can be naturally organized in a tabular form. However, how to enable TFMs to effectively capture structural information of graphs remains largely unexplored. The key challenge is to learn a graph-to-table alignment mechanism that enables graph structural understanding for TFMs. To address this, we propose GTAlign, a surprisingly simple yet effective Graph-to-Table Alignment framework for text-free Graph Foundation Model. Specifically, we first pretrain a graph encoder that maps diverse graphs into a unified latent space to capture domain-agnostic graph representations. To further bridge the gap between graph topology and the tabular representation space, we propose community-guided continual pre-training, where pseudo-labels derived from graph community are used to construct few-shot prediction episodes. Lastly, we adapt the graph encoder for an unseen target domain and perform in-context inference. Extensive experiments on five benchmark datasets demonstrate that GTAlign significantly outperforms state-of-the-art baselines on both node and graph classification, offering a simple, effective, and text-free GFM model. Code will be released upon acceptance.

## 4. Laguerre Geometry for Interpreting Large Language Models

- Authors: Chunwei Ma, Russell Wolfinger
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-12
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 3.448237280719762
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.10578v1
- PDF: https://arxiv.org/pdf/2607.10578v1
- Local PDF: pdf/2026-07-15_04_Laguerre Geometry for Interpreting Large Language Models.pdf

Existing hypotheses represent a concept in an LLM as a single point, a linear direction, or a Gaussian cluster, yet it remains unclear how and why such structures emerge. Here, we show that concept geometry can be precisely characterized via Laguerre Geometry, in which a concept is defined as a region--a Laguerre-Voronoi cell or a union of cells--allowing us to strictly define, measure, and separate concepts. Building on this formulation, we show that finer-grained concept structures, such as inclusion and hierarchy, are naturally revealed by the Laguerre weights. We then push this geometry inside the transformer. Decomposing each layer into piecewise-linear operators, we show that a token's hidden trajectory is governed by two coupled mechanisms: a static tree of self-contained piecewise-linear flow, and a dynamic transport that hops the trajectory across trees when cross-token attention fires. This decomposition yields Geometric Lens, a training-free, hyperparameter-free method for reading out the exact concept a hidden vector encodes at any layer. We also develop Laguerre Autoencoder, a 2D visualizer that renders both the decision geometry and a model's full reasoning trajectory in one view. Finally, we move beyond explanatory geometry toward actionable interpretability, showing that Geometric Lens recovers the correct factual token when a model is prompted with in-context interference. The code is available on GitHub.

## 5. DAG-FM: A Foundation Model for Causal Discovery under Heterogeneous Causal Mechanisms

- Authors: Yikang Chen, Zhengkang Guan, Haoyuan Qian, Peng Cui, Yi Yang, Kun Kuang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-13
- DOI: Unavailable
- Categories: cs.LG, stat.ML
- Relevance: 3.3766475125444066
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.11510v1
- PDF: https://arxiv.org/pdf/2607.11510v1
- Local PDF: pdf/2026-07-15_05_DAG-FM_ A Foundation Model for Causal Discovery under Heterogeneous Causal Mechanisms.pdf

Causal discovery from observational tabular data remains fundamentally challenging, primarily due to the heterogeneity of underlying causal mechanisms and the high-dimensional combinatorial search space of Directed Acyclic Graphs (DAGs). In this paper, we propose \textbf{DAG-FM}, a novel foundation model architecture that amortizes causal discovery. Unlike direct matrix prediction, DAG-FM decomposes the causal discovery process into two auto-regressive stages using two specialized Transformer-based sub-modules: a leaf-node predictor and a parent-node predictor. To effectively model complex row-column interactions, we adopt a robust tabular interaction block to output feature-wise representations. Crucially, to handle diverse and unknown Functional Causal Model (FCM) assumptions in real-world scenarios, we introduce Mixture-of-Leaf-Experts (MoLE), allowing the model to dynamically route and adapt to identifiable mechanism families. Through an iterative inference algorithm, DAG-FM seamlessly extracts causal orderings and constructs valid DAGs. Extensive experiments demonstrate that DAG-FM achieves state-of-the-art performance on both synthetic benchmarks and complex real-world datasets, significantly outperforming traditional classical algorithms and recent foundation models in both accuracy and scalability.

## 6. CDFM: Towards a General-Purpose Causal Discovery Foundation Model

- Authors: Jie Qiao, Ruichu Cai, Zijian Li, Weilin Chen, Pengfei Hua, Boyan Xu, Zhengming Chen, Zhifeng Hao, Peng Cui
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-13
- DOI: Unavailable
- Categories: cs.LG, cs.AI, stat.ML
- Relevance: 3.355923082112218
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.11508v1
- PDF: https://arxiv.org/pdf/2607.11508v1
- Local PDF: pdf/2026-07-15_06_CDFM_ Towards a General-Purpose Causal Discovery Foundation Model.pdf

Causal discovery, the process of recovering underlying causal structures from observational data, is a fundamental pursuit across scientific disciplines. Over the past decades, numerous algorithms have been developed to tackle this challenge through workflows tailored to the specific causal mechanisms underlying each type of dataset, demonstrating effectiveness across a wide range of applications. However, as the volume and heterogeneity of real-world data continue to grow, this dataset-specific approach inevitably leads to a fragmented, test-driven paradigm that struggles to scale to the demands of modern scientific discovery. To address this, we formulate the Causal Discovery Foundation Model (CDFM) as a unified, general-purpose framework for zero-shot structural inference. To ensure reliable generalization across unknown domains, we first investigate the theoretical boundaries of causal identifiability, revealing the indispensable role of causal prior mechanisms in this process. Building on these insights, we formulate a principled variational framework that treats unknown causal mechanisms as latent variables and mathematically decomposes the intractable marginal likelihood into distinct, tractable learning modules. The variational decomposition provides a conceptual design principle for the architecture design of CDFM, while comprehensive causal knowledge guides the large-scale synthesis of our pretraining data. By pretraining on a massive, highly diverse space of synthetic structural causal models, CDFM successfully internalizes complex statistical asymmetries. Extensive experiments demonstrate that CDFM consistently outperforms traditional algorithms, driving a paradigm shift toward a general-purpose causal discovery foundation model.

## 7. RAGU: A Multi-Step GraphRAG Engine with a Compact Domain-Adapted LLM

- Authors: Mikhail Komarov, Ivan Bondarenko, Stanislav Shtuka, Oleg Sedukhin, Roman Shuvalov, Yana Dementyeva, Matvey Solovyov, Nikolay O. Nikitin
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-13
- DOI: Unavailable
- Categories: cs.CL, cs.AI
- Relevance: 3.339398101788878
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.11683v1
- PDF: https://arxiv.org/pdf/2607.11683v1
- Local PDF: pdf/2026-07-15_07_RAGU_ A Multi-Step GraphRAG Engine with a Compact Domain-Adapted LLM.pdf

Graph retrieval-augmented generation (GraphRAG) enhances large language models with structured knowledge, yet existing systems construct knowledge graphs in a single extraction pass, producing noisy entities and brittle retrieval. RAGU, an open-source modular GraphRAG engine, addresses this by separating extraction from consolidation: entities and relations pass through two-stage typed extraction, DBSCAN-backed deduplication, LLM summarization, and Leiden community detection. A key insight motivates a compact extractor: the skills an in-pipeline LLM needs - comprehension, extraction, reasoning over context - are language skills that grow only weakly with model size, unlike factual world knowledge. Accordingly, we train Meno-Lite-0.1, a 7B model optimized for language skills, which outperforms Qwen2.5-32B on knowledge-graph construction (+12.5% relative harmonic mean) and matches it on English GraphRAG tasks. On GraphRAG-Bench (Medical), RAGU retrieves the most complete context at every factoid level (evidence recall up to 0.84 vs. $\leq$0.76) and overtakes HippoRAG2 on synthesis tasks; on multi-hop factoid QA, the apparent HippoRAG2 advantage is shown to be largely an answer-format artifact. RAGU is installable via $\texttt{pip install graph_ragu}$, runs on a single GPU, and is released under MIT. The source code is publicly available at https://github.com/RaguTeam/RAGU, and the Meno-Lite-0.1 model can be obtained from https://huggingface.co/bond005/meno-lite-0.1.

## 8. KGCQual: An Interpretable Framework for Evaluating the Knowledge Graph Construction Quality from Text

- Authors: Nipun Misra, Vikranth Udandarao, Aanchal Gupta, Yogender Kumar, Manuj Mukherjee, Raghava Mutharaju
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-11
- DOI: Unavailable
- Categories: cs.AI, cs.CL
- Relevance: 3.2711400479281005
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.10212v1
- PDF: https://arxiv.org/pdf/2607.10212v1
- Local PDF: pdf/2026-07-15_08_KGCQual_ An Interpretable Framework for Evaluating the Knowledge Graph Construction Quality from Text.pdf

Knowledge Graphs (KGs) are increasingly constructed through automated extraction pipelines; however, such systems often introduce spurious or incomplete triples, which degrade downstream performance. Existing evaluation practices rely heavily on task-specific metrics or small-scale manual verification, offering limited insight into the structural and semantic fidelity of extracted graphs. We propose a novel, interpretable metric for intrinsic KG quality assessment that measures how closely an automatically extracted graph approximates an "ideal" graph capturing the key noun phrases, predicate relations, and basic linguistic phenomena such as negation expressed in the source text. Our framework integrates two complementary components: (1) an entity-level assessment that evaluates completeness, resolution quality, and connectivity, and (2) a relation-level assessment that judges predicate preservation and multiplicity using lexical similarity, dependency-parse alignment, and light-weight negation handling to ensure semantic faithfulness. We evaluate our metric across multiple state-of-the-art triple extraction systems and datasets, including WebNLG, TinyButMighty, and BenchIE, demonstrating that it reliably identifies omissions, redundancy, and structural deviations that existing metrics overlook. Our work offers a scalable, model-agnostic, and interpretable framework for comparing automated KG construction methods and provides a foundation for standardised evaluation. We further validate the metric through an ablation study isolating noun and verb components, and a downstream evaluation showing that KGCQual scores correlate significantly with link prediction performance on the same extracted KGs. The code repository is available at https://github.com/kracr/kg-quality-metric.

## 9. Integrating Background Knowledge for Scalable Causal Discovery

- Authors: Mátyás Schubert, Theofanis Aslanidis, Tom Claassen, Sara Magliacane
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-11
- DOI: Unavailable
- Categories: stat.ML, cs.LG
- Relevance: 3.270614638521561
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.10456v1
- PDF: https://arxiv.org/pdf/2607.10456v1
- Local PDF: pdf/2026-07-15_09_Integrating Background Knowledge for Scalable Causal Discovery.pdf

Expert background knowledge is often available in practical applications of causal discovery. Such constraints on the true causal graph can help causal discovery in terms of identifiability of causal effects and accuracy of the learned structure, but also in reducing the space of candidate causal graphs. As causal discovery can become computationally expensive for large number of variables, it is crucial to utilize background knowledge effectively during the causal discovery process. However, most current methods only use background knowledge in a postprocessing step after causal discovery to refine the learned graph. In this work, we develop a framework for utilizing background knowledge during the causal discovery process, focusing especially on scalable causal discovery methods that recover only a subset of the whole graph. We implement our framework for multiple algorithms and empirically show that utilizing background knowledge can both reduce computational requirements and increase the quality of the learned structures.

## 10. GAE: Graph-Augmented Evolution for Scientific Discovery via Reinforcement Optimization

- Authors: Xuanzhou Chen, Taoli Cheng
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-11
- DOI: Unavailable
- Categories: cs.LG, cs.AI
- Relevance: 3.2540132711021377
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.10127v1
- PDF: https://arxiv.org/pdf/2607.10127v1
- Local PDF: pdf/2026-07-15_10_GAE_ Graph-Augmented Evolution for Scientific Discovery via Reinforcement Optimization.pdf

Evolutionary program search guided by Large Language Models (LLMs) has emerged as a powerful paradigm for automated scientific discovery. However, current approaches are fundamentally constrained by three bottlenecks: structurally blind parent selection, sparse whole-program evaluation rewards, and static mutation operators that fail to adapt during search. We present GAE (Graph-Augmented Evolution), a framework that resolves these limitations through a tightly coupled, three-pillar architecture. First, a relational graph neural network (GNN) parses programs into typed computation graphs, producing structure-aware embeddings. Second, an RL-optimized meta-controller leverages these embeddings to replace blind evolutionary sampling with a directed policy, dynamically selecting optimal parents and mutation directions based on reward history. Third, an online GRPO fine-tuning loop continuously updates the LLM mutation operator at test-time using group-normalized evaluation rewards, directly aligning the model's generation distribution with high-fitness structural edits. We evaluate GAE on a challenging scientific discovery task: symbolic regression for complex nonlinear oscillator systems. By transforming stochastic search into a directed, self-improving trajectory, GAE efficiently discovers closed-form physical equations, consistently matching or outperforming static LLM-driven baselines and achieving state-of-the-art out-of-distribution performance.

## 11. SciMKG: A Multimodal Knowledge Graph for Science Education with Text, Image, Video and Audio

- Authors: Tong Lu, Zhichun Wang, Y. Zhou, Yiming Guan, Zhiyong Bai, Junsheng Du
- Source: openalex
- Venue type: conference
- Journal: Proceedings of the AAAI Conference on Artificial Intelligence
- Publication status: formally_published
- Publication date: 2026-03-14
- DOI: https://doi.org/10.1609/aaai.v40i18.38574
- Categories: Advanced Graph Neural Networks, Multimodal Machine Learning Applications, Topic Modeling
- Relevance: 3.239881037203806
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://doi.org/10.1609/aaai.v40i18.38574
- PDF: https://ojs.aaai.org/index.php/AAAI/article/download/38574/42536
- Local PDF: Not downloaded

Knowledge graphs (KGs) play a vital role in intelligent education by offering structured representations of educational content. However, constructing multimodal educational knowledge graphs (EKGs) from diverse open educational resources remains a challenge due to the reliance on costly manual annotations and the lack of multimodal integration. In this work, we propose an automated framework that harnesses the reasoning capabilities of large language models (LLMs) to construct multimodal EKGs from open courses efficiently. In our framework, an Extraction-Verification-Integration-Augmentation pipeline is designed to incrementally extract and refine disciplinary concepts from learning resources. Texts, images, videos and audios are aligned with their corresponding concepts. To ensure semantic consistency across modalities, we propose a cross-modal alignment method based on shared structural and semantic features. Using our framework, we build SciMKG, a large-scale multimodal EKG for Chinese K12 education in sciences (biology, physics, and chemistry), encompassing 1,356 knowledge points, 34,630 multimodal concepts, and 403,400 relational triples. Experimental results show that our method improves concept extraction F1 score by 9 % over state-of-the-art baselines; both automatic and human evaluations confirm the robustness of our multimodal alignment method. SciMKG and our construction toolkit will be publicly released to support further research and applications in AI-driven education.

## 12. From Global to Factor-Wise Expert Composition in Discrete Diffusion Models

- Authors: Haozhe Huang, Yudong Xu, Abhijoy Mandal, Alán Aspuru-Guzik
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-13
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.1976453593671286
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.11758v1
- PDF: https://arxiv.org/pdf/2607.11758v1
- Local PDF: pdf/2026-07-15_12_From Global to Factor-Wise Expert Composition in Discrete Diffusion Models.pdf

Discrete diffusion models offer a powerful framework for solving complex reasoning tasks, particularly through compositional generation, which combines multiple pre-trained experts to generalize beyond their individual training data. Recent theoretical corrections introduce time-dependent mixing weights to better align composed diffusion dynamics with the intended target. However, these methods are fundamentally limited by working on a per-sample basis, treating each generated state monolithically and ignoring the potential spatial or functional specializations of different experts. In this work, we address this limitation by proposing FactorDiff - a factor-wise composition framework for diffusion models. We posit that samples can be further decomposed into smaller factors, and propose a sampling process that dynamically routes each factor to the most relevant expert. We instantiate this framework with spatial/pixel-level compositions and validate it on the ARC-AGI benchmark, demonstrating that simple factor-specific routing consistently outperforms complex global scalar weighting schemes on tasks that require logical consistency and spatial disentanglement.

## 13. PromptGraph: Graph-Guided Prompt Sanitization for Balancing Privacy and Utility in LLM Inference

- Authors: Chen Gu, Hui Wan, Donghui Hu, Hui Wang, Zhuoer Gu
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-12
- DOI: Unavailable
- Categories: cs.CR, cs.AI
- Relevance: 3.15773697355223
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.10709v1
- PDF: https://arxiv.org/pdf/2607.10709v1
- Local PDF: pdf/2026-07-15_13_PromptGraph_ Graph-Guided Prompt Sanitization for Balancing Privacy and Utility in LLM Inference.pdf

Large Language Model (LLM) services introduce a fundamental privacy challenge. Sensitive information may be inferred not only from explicit identifiers, such as names or phone numbers, but also from contextual associations among otherwise innocuous spans. Existing sanitizers typically assign privacy or utility signals to individual spans without explicitly modeling pairwise relationships among them. In this paper, we propose PromptGraph, a graph-guided prompt-sanitization approach for privacy-preserving LLM inference. PromptGraph estimates privacy leakage at the span level and utility-relevant contextual dependencies between pairs of spans. It represents each prompt as an attributed graph, in which nodes carry span-level privacy scores and edges encode contextual dependencies needed to preserve utility. The sanitization objective selects a protected span set that maximizes privacy gain while penalizing the loss of contextual dependencies. This formulation explicitly balances privacy and utility when contextual evidence is hidden. Protected spans are sanitized locally, and returned placeholders are restored only after passing local consistency checks. We conduct extensive experiments showing that PromptGraph achieves a more favorable balance between privacy and utility than prompt-privacy baselines.

## 14. GRATE: Temporal Extensions for Inductive KG Foundation Models via Gated Rotary Attention

- Authors: Jiaxin Pan, Osama Mohammed, Daniel Hernández, Steffen Staab
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-11
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 3.1415520124605556
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.10197v1
- PDF: https://arxiv.org/pdf/2607.10197v1
- Local PDF: pdf/2026-07-15_14_GRATE_ Temporal Extensions for Inductive KG Foundation Models via Gated Rotary Attention.pdf

Knowledge graph foundation models such as Ultra and Trix achieve strong inductive transfer by learning relation-graph representations that generalise to unseen entities and relations. Extending this transferability to temporal knowledge graphs (TKGs) remains challenging: existing temporal models tie their parameters to dataset-specific entities, relations, or timestamps and are not designed to transfer to TKGs with disjoint vocabularies. We propose GRATE (Gated Rotary Attention for Temporal Encoding), an entity-side message function that adds no learnable parameters and encodes time through relative time differences by rotating each edge message according to its time gap to the query and applying a query-conditioned gate to select temporally relevant signals. GRATE integrates into NBFNet-style KG foundation models while preserving structural transferability. Existing TKG benchmarks evaluate within shared train/test vocabularies and cannot directly test cross-dataset temporal transfer; we therefore construct GDELTIndT and WIKIIndT, inductive transfer benchmark suites with disjoint entities, relations, and timestamps spanning both interpolation and extrapolation. Across these benchmarks and held-out forecasting datasets, a single jointly pretrained GRATE checkpoint improves over the static base model in most settings.

## 15. LaGuadia: Language-Guided Adaptive Distillation from Pathology Foundation Models

- Authors: Gangsu Kim, Won-Ki Jeong
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-13
- DOI: Unavailable
- Categories: cs.CV, cs.LG
- Relevance: 3.125612496750044
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.11257v1
- PDF: https://arxiv.org/pdf/2607.11257v1
- Local PDF: pdf/2026-07-15_15_LaGuadia_ Language-Guided Adaptive Distillation from Pathology Foundation Models.pdf

Pathology Foundation Models (PFMs) offer powerful Whole Slide Image (WSI) representations but suffer from massive computational costs. While Knowledge Distillation (KD) can create efficient student models, existing multi-teacher methods often use suboptimal uniform weighting that ignores tissue heterogeneity. We propose LaGuadia (Language-Guided Adaptive DistillAtion), a framework that develops a compact pathology image encoder by dynamically integrating expertise from multiple PFMs under clinical linguistic guidance. Our approach utilizes a multi-stage pipeline: first, extracting visually observable clinical keywords from pathology reports; second, aligning visual features with these keywords via a Vision-Language meta-teacher (MedSigLIP) to provide dense semantic guidance; and finally, performing adaptive KD where teacher contributions are weighted based on their semantic alignment with the clinical narrative. Experiments on WSI captioning, visual question answering, and slide-level classification tasks demonstrate that an 87M parameter LaGuadia student model matches or exceeds foundation-scale models such as GigaPath and UNI, achieving strong factual consistency and robust generalization. These results highlight clinical language as an effective semantic anchor for building efficient and reliable digital pathology systems. Code is available at https://github.com/hvcl/LaGuadia.

## 16. modelDNA: Calibrated Lineage Verification and Merge Decomposition from Sampled Weight Fingerprints

- Authors: Muhammad Awais Bin Adil, Saad Aamir
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-12
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.1094537440093695
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.10617v1
- PDF: https://arxiv.org/pdf/2607.10617v1
- Local PDF: pdf/2026-07-15_16_modelDNA_ Calibrated Lineage Verification and Merge Decomposition from Sampled Weight Fingerprints.pdf

The lineage graph of open-weight language models is self-reported: Hugging Face's base_model metadata field is optional and unverified, and over 60% of Hub models document no parentage at all. Methods for detecting lineage from weights exist in the research literature, but each ships as paper code tied to one signal and one experiment; when a provenance dispute breaks, the analysis is redone by hand. This report describes modelDNA, a tool that fingerprints a model from roughly 100-300 MB of ranged HTTP reads (instead of a full 15 GB download for a 7B model), compares the fingerprint against a reference database of foundation models across four published signal families, and returns one of eight verdict classes with a calibrated probability, preferring honest abstention to confident error. On a benchmark of 15 real Hub models with org-documented parentage, judged against 8 candidate bases (13 positives, 107 hard negatives), the system achieves AUROC 1.0, zero false positives at its reporting threshold, and 13/13 correct top-1 parent attribution. The report's second contribution is merge decomposition. Every mainstream weight-merging method is (near-)linear per tensor, and fingerprint sample positions are deterministic functions of tensor identity, so a merged model's fingerprint is the same linear combination of its parents' fingerprints. Mixture weights can therefore be recovered from fingerprints alone by sum-to-one constrained least squares. Against merges with published mergekit configurations as ground truth, the method recovers a slerp merge's layer-interpolation curves at r = 0.999 and a dare_ties merge's mixture weights to within 0.011 of the published values, without downloading any weights beyond the fingerprints. All fingerprints, benchmarks, and the inferred lineage graph of 55 models are public and reproducible offline.

## 17. Generative Augmentation of Raman Spectra for Glioma Classification

- Authors: Andrei Iuşan, Iulian Vasile, Daria Voiculescu, Ion Petre, Andrei Păun, Bogdan Oancea, Mihaela Păun
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-11
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.0080017129845387
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.10196v1
- PDF: https://arxiv.org/pdf/2607.10196v1
- Local PDF: pdf/2026-07-15_17_Generative Augmentation of Raman Spectra for Glioma Classification.pdf

Access to sufficiently large biomedical datasets remains a major obstacle for machine learning in Raman spectroscopy-based diagnostics. In particular, for glioma analysis, datasets are typically small and heterogeneous, affected by acquisition-specific variability. This work investigates the utility of deep generative augmentation in such a small-cohort setting. We analyze glioma biopsy spectra acquired from 58 tumor samples and consider both binary IDH-status classification and 6-class methylation subtype classification problems. To address the limited size and imbalance of the dataset, we develop a conditional variational autoencoder ($β$-CVAE) capable of generating class-conditioned synthetic Raman spectra. The generated data are evaluated in Train-on-Synthetic, Test-on-Real (TS/TR) and Train-on-Synthetic+Real, Test-on-Real (TSR/TR) settings under a strict patient-isolated cross-validation protocol. Models trained exclusively on synthetic data underperform models trained on real spectra, indicating a substantial domain gap between synthetic and real distributions. However, augmenting the real training data with synthetic spectra consistently improves classification performance across multiple models. These findings indicate that, even with a limited number of independent patient samples, generative models can capture sufficient structure to provide useful regularization for downstream classifiers. We also investigate a reconstruction-based inference strategy, termed Classification by Reconstruction (CbR), in which class prediction is based on reconstruction error under different class conditions. Overall, the results support the use of deep generative augmentation as a practical strategy for improving machine learning robustness in Raman spectroscopy applications characterized by limited biomedical datasets.

## 18. From Expressivity to Sample Complexity: Narrow Teachers for Transformers via C-RASP

- Authors: Michael Rizvi-Martel, Satwik Bhattamishra, Guillaume Rabusseau, Michael Hahn
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-13
- DOI: Unavailable
- Categories: cs.LG, cs.CL
- Relevance: 2.995933438627871
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.11760v1
- PDF: https://arxiv.org/pdf/2607.11760v1
- Local PDF: pdf/2026-07-15_18_From Expressivity to Sample Complexity_ Narrow Teachers for Transformers via C-RASP.pdf

A theoretical understanding of Transformers is crucial to better understand the capacities and limitations of large language models (LLMs). There is much work analyzing the expressivity of attention-based models. By proposing handcrafted weights or using computational complexity arguments, a large amount of past theoretical works have sought to characterize which tasks are and which are not in the hypothesis class of Transformer models. However, little work investigates the learnability of such solutions. In this work, we make progress towards this goal. Inspired by recent loss landscape analysis work, we propose preliminary sample complexity bounds for learning C-RASP constructions with Transformers.

## 19. Unified Backbone Refinement for Diffusion Models via Internal-Latent Analysis

- Authors: Haksoo Lim, Myeongjin Lee, Wonjoon Chang, Jaesik Choi
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-04
- DOI: Unavailable
- Categories: cs.CV, cs.AI, cs.LG
- Relevance: 2.9829296684128552
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.09753v1
- PDF: https://arxiv.org/pdf/2607.09753v1
- Local PDF: pdf/2026-07-15_19_Unified Backbone Refinement for Diffusion Models via Internal-Latent Analysis.pdf

Diffusion models have achieved remarkable success across diverse domains, with performance closely related to the denoising backbones that parameterize the score function. In this paper, we present a systematic, phase-aware analysis of diffusion components and show that abrupt, early-stage fluctuations in deep latents are strongly associated with artifacts. Guided by these findings, we introduce DUNE (Diffusion Unified Network refiNEr), a training-free refinement framework that detects abrupt deviations in deep low-noise internal latents using a shared EMA-based criterion, and applies backbone-specific suppression to the detector-selected entries. Although derived from U-Net, the same detect-suppress principle extends naturally to Transformer-based diffusion models by acting on the latents of deep self-attention blocks. Extensive experiments across multiple backbones indicate that DUNE improves fidelity while reducing hallucinations, offering new insight into where and when diffusion backbones should be controlled.

## 20. Multi-Agent LLMs Fail to Explore Each Other

- Authors: Hyeong Kyu Choi, Jiatong Li, Wendi Li, Xin Eric Wang, Sharon Li
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-13
- DOI: Unavailable
- Categories: cs.MA, cs.AI
- Relevance: 2.9414784759997845
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.11250v1
- PDF: https://arxiv.org/pdf/2607.11250v1
- Local PDF: pdf/2026-07-15_20_Multi-Agent LLMs Fail to Explore Each Other.pdf

Exploration is essential for reliable autonomy in multi-agent systems, yet it remains unclear whether large language model (LLM) agents can explore effectively when interacting with one another. We show that modern LLM agents fail to do so, often exhibiting myopic and polarized interaction patterns that lead to suboptimal coordination and increased regret. We formalize this challenge as the Multi-Agent Exploration problem, modeling it as a partially observable stochastic game (POSG) problem in which agents must probe peers to infer their capabilities and identify effective interaction strategies. To address this, we introduce Multi- Agent Contextual Exploration (MACE), a lightweight framework that explicitly promotes exploration through structured peer selection. Across both contextual and parametric diversity settings, MACE substantially improves exploration behavior and downstream task performance. We further show theoretically that the value of exploration increases with agent diversity. Overall, our results highlight a fundamental limitation of current LLM agents and underscore the importance of explicitly guided exploration for reliable multi-agent autonomy. Code will be released in https://github.com/deeplearning-wisc/mace

## 21. Route, Communicate, and Reason: Gated Routing and Adaptive Depth for Efficient Multi-Agent Reasoning

- Authors: Sudipto Ghosh, Tanmoy Chakraborty
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-12
- DOI: Unavailable
- Categories: cs.AI, cs.CL, cs.LG
- Relevance: 2.932714130117478
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.10836v1
- PDF: https://arxiv.org/pdf/2607.10836v1
- Local PDF: pdf/2026-07-15_21_Route, Communicate, and Reason_ Gated Routing and Adaptive Depth for Efficient Multi-Agent Reasoning.pdf

Multi-agent ensembling multiplies active parameters and inference cost without answering three basic questions: which agents to consult, how deeply a query should traverse a hierarchy of agents, and when inter-agent communication is worth its cost. We present GRADE (Gated Routing and Adaptive Depth for Efficient Reasoning), a hierarchical multi-agent system in which four lightweight learned gates jointly govern agent selection, hierarchy depth, inter-agent communication, and branch pruning. Training uses CoGRPO (Collaborative Group-Relative Policy Optimization), a novel critic-free recipe that adapts GRPO to multi-agent hierarchies and assigns a shared advantage signal to every gate and agent that participated in a rollout. Agent models are drawn from a hot-swappable Expert Registry; per-agent calibration maps allow experts to be replaced at inference time without retraining. At $\sim$17B average active parameters, GRADE outperforms all baselines on GSM8K, MMLUPro, and GPQA, surpassing the strongest baseline by 4.8 points on MMLUPro at half the active compute. On AIME-2025, where model depth dominates, GRADE remains competitive to existing frameworks. Ablations isolate the hierarchy and masked cross-attention as the largest contributors to accuracy, and show that per-agent calibration is necessary for safe hot-swapping.

## 22. Agentic Routing: The Harness-Native Data Flywheel

- Authors: Xinchen Liu, Hang Zhou, Yingjie Zong, Yuchuan Tian, Liuyang Song, Shuo Zhang, Yulong Li, Wei He, Mengyu Zheng, Runke Liu, Siyang Cheng, Xiang Kuang, Hailin Hu, Kai Han, Yunhe Wang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-13
- DOI: Unavailable
- Categories: cs.CL, cs.AI
- Relevance: 2.9275062149586573
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.11399v1
- PDF: https://arxiv.org/pdf/2607.11399v1
- Local PDF: pdf/2026-07-15_22_Agentic Routing_ The Harness-Native Data Flywheel.pdf

Large language model agents are increasingly executed not by a single model call, but by an execution harness that manages observation, context, control, action, state, and verification. At the same time, frontier and open models are becoming structurally specialized: a model that is strong at code editing, long-context recovery, tool use, mathematical reasoning, or low-latency response may not dominate on the other axes. This makes model selection inside an agent a core systems problem rather than a per-query serving trick. Existing routing methods mostly optimize single-turn cost-quality trade-offs and therefore miss the execution state, intermediate failures, and feedback loops that make agents different from chat completion. We propose Harness-Native agentic routing, a step-level routing paradigm that selects either a single best-fit model for cost-effective execution or multiple complementary models for ensemble-style accuracy improvement, conditioned on the full harness state. The key insight is that every routing decision naturally produces a structured data record -- consisting of the query, harness state, model choice or model set, execution trace, outcome, and cost -- whose labels are supplied by the environment rather than by the router itself. These records form a harness-native data flywheel: execution traces train better routers and harness-native models, which improve cost-quality trade-offs and generate more traces under the same budget. We instantiate this idea in OpenSquilla with a four-layer routing stack, an open LightGBM cold-start ranker, and a staged router-model path that turns logged arena records into progressively stronger routing policies. The report studies singleton and multi-model routing on agentic benchmarks including DRACO and PinchBench, and argues that agentic routing is not merely cost control, but a data engine for agent-native training.

## 23. Structured Thoughts For Improved Reasoning And Context Pruning

- Authors: Zain Sarwar, Supriyo Chakraborty, Berkcan Kapusuzoglu, Chia-Hsuan Lee, Anirban Das, Stephen Rawls, Kartik Balasubramaniam, Sambit Sahu
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-11
- DOI: Unavailable
- Categories: cs.CL, cs.AI
- Relevance: 2.9222977834945634
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.10386v1
- PDF: https://arxiv.org/pdf/2607.10386v1
- Local PDF: pdf/2026-07-15_23_Structured Thoughts For Improved Reasoning And Context Pruning.pdf

Large language models (LLMs) excel at generating long chains of thought, but long reasoning traces are often verbose and memory-inefficient. In this work, we introduce Structured Thoughts, a framework that organizes reasoning into alternating <try> and <outcome> blocks: <try> captures exploratory scratch work, while <outcome> contains the distilled conclusion of that step. We construct a dataset of structured thoughts by segmenting reasoning traces into <try> blocks and prompting an LLM to summarize each step into its corresponding <outcome>. Fine-tuning pretrained foundation models on this reformatted data produces models that adopt the structured reasoning style, leading to performance gains of up to 8.08\% on reasoning benchmarks compared to standard SFT. The explicit structure also enables context pruning: after each <try>/<outcome> pair, the <try> can be pruned, allowing the model to retain conclusions without keeping the full scratch work in the context. A proof-of-concept pruning implementation achieves an average of 85\% memory / context savings with an 8.67\% performance drop across mathematical tasks.

## 24. ToolAtlas: Learning Once, Reusing Everywhere with Tool-Side Memory

- Authors: Yue Fang, Zhibang Yang, Fangkai Yang, Xiaoting Qin, Liqun Li, Qingwei Lin, Saravan Rajmohan, Dongmei Zhang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-13
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 2.9213830333192043
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.11126v1
- PDF: https://arxiv.org/pdf/2607.11126v1
- Local PDF: pdf/2026-07-15_24_ToolAtlas_ Learning Once, Reusing Everywhere with Tool-Side Memory.pdf

Large language model (LLM) agents increasingly rely on external tools served by shared providers and accessed by heterogeneous downstream agents. Existing approaches improve tool use on the agent side through parameter updates, prompt refinement, or agent-side memory, making tool knowledge difficult to share and limited to behaviors observed in past tasks. We argue that reusable tool knowledge should instead be maintained by the tool provider. We introduce ToolAtlas, a graph-based framework that builds a persistent provider-side tool memory of tool capabilities, failure boundaries, and cross-tool compositions through execution-verified probing. At inference time, agents query the tool memory via adaptive graph traversal. Across two MCP-based benchmarks spanning eight services, ToolAtlas outperforms existing tool-side optimization and agent-side memory baselines by up to 21.61% in pass@1 and 18.61% in pass@4. The same tool memory also transfers across environment instances and agent frameworks without retraining or task-time exploration, yielding up to 24.16%/16.22% and 17.49%/14.27% relative gains in pass@1/pass@4, respectively. Ablation studies show that these gains arise from combining tool-centered memory organization with capability-guided execution probing. These results establish provider-side tool memory as an effective and reusable paradigm for tool servers. Our code is in: https://github.com/PuppyKnightUniversity/ToolAtlas.

## 25. The Universal Language of CSI:Unifying Wireless Sensing Across Devices and Environments

- Authors: Jiayi Chen, Weiting Ou, Guangxu Zhu
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-06-30
- DOI: Unavailable
- Categories: eess.SP, cs.AI
- Relevance: 2.92085289972311
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.09727v1
- PDF: https://arxiv.org/pdf/2607.09727v1
- Local PDF: pdf/2026-07-15_25_The Universal Language of CSI_Unifying Wireless Sensing Across Devices and Environments.pdf

WiFi sensing based on Channel State Information (CSI) promises ubiquitous, device-free perception, yet current research remains trapped in a Tower of Babel - fragmented into isolated silos where models are tailored to specific hardware dialects, fixed environments, and narrow tasks. The primary bottleneck is the Heterogeneity Gap: the disparity in signal dimensions, sampling rates, and semantic labels that prevents cross-system understanding. To bridge this gap, we propose a foundation-model framework that treats CSI not merely as raw signals but as a structured language with a learnable universal grammar. We first curate and standardize a large collection of heterogeneous real-world CSI datasets, establishing a unified infrastructure that allows incompatible signal formats to be treated as a single corpus. Second, we introduce a modular architecture that acts as a universal translator where lightweight dataset-specific adapters tokenize diverse signal inputs into a shared latent vocabulary, while a shared self-supervised Transformer backbone learns the temporal syntax of human motion and environmental dynamics. This design decouples sensing semantics from hardware syntax. Extensive evaluations show that by mastering this universal language, our approach consistently outperforms task-specific baselines and exhibits strong generalization capability in new environments, achieving superior efficiency in few-shot scenarios. By effectively absorbing heterogeneity, the framework offers a path toward robust, general-purpose wireless sensing, mirroring the linguistic generalization observed in Large Language Models. The code implementation is available at: https://github.com/cjychenjiayi/WiLLM.

## 26. GraphMind: LLMs as Dynamic Knowledge Builders for Sequential Decision-Making

- Authors: Sunguk Shin, Hayeong Lee, Jun Ho Seo, Jinho Lee, Myunsoo Kim, Minsuk Chang, Byung-Jun Lee
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.902020133721699
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1651/
- PDF: https://aclanthology.org/2026.findings-acl.1651.pdf
- Local PDF: pdf/2026-07-15_26_GraphMind_ LLMs as Dynamic Knowledge Builders for Sequential Decision-Making.pdf

While the reasoning capabilities of large language models (LLMs) have advanced considerably, efficiently internalizing and leveraging new information in dynamically interactive environments remains a significant challenge. This limitation is particularly pronounced in partially observable environments, which require agents to manage long-term memory and perform effective exploration under incomplete information. To address this, we propose an LLM agent architecture that integrates a knowledge graph as a graph-based memory module. The agent incrementally constructs the knowledge graph through environmental interactions and retrieves relevant information to generate efficient plans. We evaluate our approach in complex navigation tasks specifically designed to present long-horizon and partially observable challenges. Experimental results demonstrate that incorporating a self-extending memory module significantly enhances the performance and efficiency of the LLM’s planning capabilities.

## 27. FROST: Factual Reasoning via Optimized Stochastic Trajectories in Large Language Models during Inference

- Authors: Soumedhik Bharati, Ebad Shabbir, Jiechao Gao
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.9019983896322277
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-industry.77/
- PDF: https://aclanthology.org/2026.acl-industry.77.pdf
- Local PDF: pdf/2026-07-15_27_FROST_ Factual Reasoning via Optimized Stochastic Trajectories in Large Language Models during Inference.pdf

Large language models face a trade-off between factual consistency and reasoningdiversity: deterministic decoding prioritizes reliability but may miss alternativesolution paths, while high-temperature sampling increases exploration at the costof accuracy. We present FROST (Factual Reasoning via Optimized StochasticTrajectories), an inference-time framework that balances exploration andexploitation without additional training or context augmentation. FROST combinesdeterministic inference from a large model with targeted stochastic sampling froma smaller model, selecting outputs via multi-criteria validation over coherence,factual grounding, and semantic novelty. Across HotpotQA, CommonsenseQA, andMMLU, FROST achieves 2–5 percentage point improvements over standard chain-of-thoughtprompting and reduces unsupported outputs by 40% relative to Standard CoT. Comparedto Self-Consistency ensembles, FROST delivers comparable accuracy at 28% lowerinference cost through strategic delegation to smaller models. On an adversarialsubset with unanswerable queries, FROST abstains on 34% of cases versus 8% forstandard chain-of-thought, reducing false positives by 45%. Task-stratifiedevaluation shows that exploration benefits scale with problem ambiguity.Generalization to mathematical reasoning, code generation, and multimodal domainsremains future work.

## 28. Reinforcement Learning with Semantic Rewards Enables Low-Resource Language Expansion without Alignment Tax

- Authors: Zeli Su, Ziyin Zhang, Zhou Liu, Xuexian Song, Zhankai Xu, Longfei Zheng, Xiaolu Zhang, Rong Fu, Guixian Xu, Wentao Zhang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.9012311252844185
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.880/
- PDF: https://aclanthology.org/2026.findings-acl.880.pdf
- Local PDF: pdf/2026-07-15_28_Reinforcement Learning with Semantic Rewards Enables Low-Resource Language Expansion without Alignment Tax.pdf

Extending large language models (LLMs) to low-resource languages often incurs an “align- ment tax”: improvements in the target lan- guage come at the cost of catastrophic forget- ting in general capabilities. We argue that this trade-off arises from the rigidity of supervised fine-tuning (SFT), which enforces token-level surface imitation on narrow and biased data distributions. To address this limitation, we propose a semantic-space alignment paradigm powered by Group Relative Policy Optimiza- tion (GRPO), where the model is optimized us- ing embedding-level semantic rewards rather than likelihood maximization. This objective encourages meaning preservation through flex- ible realizations, enabling controlled updates that reduce destructive interference with pre- trained knowledge. We evaluate our approach on Tibetan–Chinese machine translation and Ti- betan headline generation. Experiments show that our method acquires low-resource capa- bilities while markedly mitigating alignment tax, preserving general competence more effec- tively than SFT. Despite producing less rigid surface overlap, semantic RL yields higher se- mantic quality and preference in open-ended generation, and few-shot transfer results indi- cate that it learns more transferable and ro- bust representations under limited supervision. Overall, our study demonstrates that reinforce- ment learning with semantic rewards provides a safer and more reliable pathway for inclusive low-resource language expansion.

## 29. MCP-Flow: Facilitating LLM Agents to Master Real-World, Diverse and Scaling MCP Tools

- Authors: WenHao Wang, Peizhi Niu, Zhao Xu, Zhaoyu Chen, Jian Du, Yaxin Du, Xianghe Pang, Keduan Huang, Yanfeng Wang, Qiang Yan, Siheng Chen
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.9004038671561325
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.231/
- PDF: https://aclanthology.org/2026.acl-long.231.pdf
- Local PDF: pdf/2026-07-15_29_MCP-Flow_ Facilitating LLM Agents to Master Real-World, Diverse and Scaling MCP Tools.pdf

Large Language Models (LLMs) increasingly rely on external tools to perform complex, realistic tasks, yet their ability to utilize the rapidly expanding Model Contextual Protocol (MCP) ecosystem remains limited. Existing MCP research covers few servers, depends on costly manual curation, and lacks training support, hindering progress toward real-world deployment. To overcome these limitations, we introduce MCP-Flow, an automated web-agent-driven pipeline for large-scale server discovery, data synthesis, and model training. MCP-Flow collects and filters data from 1166 servers and 11536 tools, producing 68733 high-quality instruction-function call pairs and 6439 trajectories, far exceeding prior work in scale and diversity. Extensive experiments demonstrate MCP-Flow’s effectiveness in driving superior MCP tool selection, function-call generation, and enhanced agentic task performance. MCP-Flow thus provides a scalable foundation for advancing LLM agents’ proficiency in real-world MCP environments.

## 30. Parallel Test-Time Scaling for Latent Reasoning Models

- Authors: Runyang You, Yongqi Li, Meng Liu, Wenjie Wang, Liqiang Nie, Wenjie Li
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.8996909330187117
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.2069/
- PDF: https://aclanthology.org/2026.acl-long.2069.pdf
- Local PDF: pdf/2026-07-15_30_Parallel Test-Time Scaling for Latent Reasoning Models.pdf

Parallel test-time scaling (TTS) is a pivotal approach for enhancing large language models (LLMs), typically by sampling multiple token-based chains-of-thought in parallel and aggregating outcomes through voting or search. Recent advances in latent reasoning, where intermediate reasoning unfolds in continuous vector spaces, offer a more efficient alternative to explicit Chain-of-Thought, yet whether such latent models can similarly benefit from parallel TTS remains open, mainly due to the absence of sampling mechanisms in continuous space, and the lack of probabilistic signals for advanced trajectory aggregation. This work enables parallel TTS for latent reasoning models by addressing the above issues. For sampling, we introduce two uncertainty-inspired stochastic strategies: Monte Carlo Dropout and Additive Gaussian Noise. For aggregation, we design a Latent Reward Model (LatentRM) trained with step-wise contrastive objective to score and guide latent reasoning. Extensive experiments and visualization analyses show that both sampling strategies scale effectively with compute and exhibit distinct exploration dynamics, while LatentRM enables effective trajectory selection. Together, our explorations open a new direction for scalable inference in continuous spaces. Code and checkpoint are included as supplementary materials.GitHub Project: https://github.com/ModalityDance/LatentTTS
