# Paper Daily Reading - 2026-08-25

## 1. Graph Engineering in the Era of LLM Agents: From Individual Intelligence to System Intelligence

- Authors: Yuyuan Feng, Zhishang Xiang, Chaobin Yang, Qichao Ma, Zerui Chen, Yujing Zhang, Ke Huang, Chuanjie Wu, Zhaoxu Liu, Yili Wang, Xin He, Jiapu Wang, Zijin Hong, Hao Chen, Yuanchen Bei, Kun Wang, Shengyuan Chen, Ningyu Zhang, Enyan Dai, Linhao Luo, Qingyi Pan, Qi Wang, Wenqi Fan, Guangjing Wang, Na Zou, Yangqiu Song, Xin Wang, Zechao Li, Xia Hu, Qing Li, Xiao Huang, Zhihong Zhang, Jinsong Su, Qinggang Zhang, Yi Chang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-21
- DOI: Unavailable
- Categories: cs.IR, cs.AI, cs.ET
- Relevance: 3.3186430817813664
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.21156v1
- PDF: https://arxiv.org/pdf/2608.21156v1
- Local PDF: pdf/2026-08-25_01_Graph Engineering in the Era of LLM Agents_ From Individual Intelligence to System Intelligence.pdf

LLMs have evolved from language generators to autonomous agents capable of complex, long-horizon tasks. This evolution has produced paradigms including Prompt Engineering to elicit model capabilities, Context Engineering to manage information access, Harness Engineering to organize external tools and resources, and Loop Engineering to support continual reflection and self-improvement. Yet as tasks grow more complex, individual intelligence faces a fundamental limit: many tasks require heterogeneous expertise, interdependent subtasks, parallel execution, independent verification, and persistent state, exceeding any single agent's organizational capacity. Augmenting one agent's capabilities or context cannot resolve this architectural mismatch; intelligence must instead be distributed across specialized agents and organized at the system level. We call this System Intelligence: an agent system's ability to organize and coordinate multiple intelligent components into a coherent, adaptive whole pursuing a shared objective. Achieving it requires more than adding agents; it demands explicit structures to organize work, coordinate heterogeneous agents, and maintain evolving execution states. We introduce Graph Engineering, an emerging paradigm for next-generation agent systems. Unlike prior paradigms that mainly optimize individual interactions or agent-level behavior, Graph Engineering constructs explicit, dynamic, evolving graph structures representing tasks, agents, and system states. These abstractions provide a unified foundation for organizing complex objectives, orchestrating heterogeneous agents, modeling system dynamics, and enabling scalable agent evolution. We systematically review the principles, methodologies, and applications of Graph Engineering for LLM agents. Related papers, open-source data, and projects are collected at https://github.com/DEEP-JLU/Awesome-Graph-Engineering.

## 2. CellPath-Bench: A Multidimensional Benchmark for Whole-Slide Cellular Representations in Pathology Foundation Models

- Authors: Bokai Zhao, Yiyang Zhang, Hanqing Chao, Yawei Ma, Long Bai, Tai Ma, Minfeng Xu, Ming Song, Tianzi Jiang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-21
- DOI: Unavailable
- Categories: cs.AI, cs.CV
- Relevance: 3.247392724426043
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.21060v1
- PDF: https://arxiv.org/pdf/2608.21060v1
- Local PDF: pdf/2026-08-25_02_CellPath-Bench_ A Multidimensional Benchmark for Whole-Slide Cellular Representations in Pathology Foundation Models.pdf

Pathology foundation models (PFMs) are increasingly used as general-purpose backbones, yet existing benchmarks cannot systematically diagnose their whole-slide cellular representation capabilities, including the decodability of cell-type information and the transferability of such information across tissue sections, datasets, and anatomical organs. We introduce CellPath-Bench, a cellular-resolution benchmark that evaluates frozen PFMs themselves. Following quality control of 52 candidate Xenium datasets, we construct a panel of 25 spatially aligned H\&E--Xenium tissue sections spanning 11 organs and 7,079,283 cells, harmonized into fine- and coarse-grained taxonomies. CellPath-Bench samples frozen WSI feature maps at registered nuclear coordinates and evaluates them using standardized multiclass linear probes. Cell Representation Advantage (CRA) measures the within-section advantage of nucleus-anchored representations over patch-level mean pooling, while Cell Representation Transferability (CRT) characterizes the generalization of cell-type decodability across tissue sections, datasets, and organs. We benchmark 30 pathology-specific and general-purpose foundation models through 304,920 runs across spatial readouts, magnifications, taxonomic granularities, and evaluation protocols. The results reveal substantial model-dependent differences in cell-type decodability and its cross-domain generalization, yielding distinct multidimensional capability profiles. CellPath-Bench provides a standardized framework for auditing cellular information in frozen PFM representations.

## 3. Toward Auto-Research: Mining Falsifiable Research Ideas from Paper Knowledge Graphs with Categorical Structure

- Authors: Yuchen Wang, Zhongzhi Luan
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-06-17
- DOI: Unavailable
- Categories: cs.CL, cs.AI
- Relevance: 3.245985939628719
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.20361v1
- PDF: https://arxiv.org/pdf/2608.20361v1
- Local PDF: pdf/2026-08-25_03_Toward Auto-Research_ Mining Falsifiable Research Ideas from Paper Knowledge Graphs with Categorical Structure.pdf

Automated research-idea generation systems built on large language models (LLMs) share a structural weakness: they reduce ideation to free-text recombination, random paper pairing, or embedding-similarity retrieval. The three approaches fail in the same way: each treats a paper as a flat object, a string or a vector, and so quotients away the typed problem-method-metric-claim arrows a researcher actually uses when reasoning about a cross-domain analogy. We recover the missing structure with the minimal piece of category theory that a typed graph alone does not provide: composition, together with identity arrows, which makes it possible to ask whether a proposed analogy preserves relation chains. Concretely, each paper $p$ is modelled as a small category $C_p$ whose objects are extracted typed research entities and whose morphisms are the relations the paper asserts; a cross-paper bridge from $p$ to $q$ is then a partial functor candidate $F: C_p -> C_q$ that preserves object kinds and covered relation classes. We instantiate the model as a three-layer algorithm: categorical signature clustering, a functor-preservation gate, and a six-axis LLM plausibility judge. Evaluated on a corpus of tens of thousands of full-text-parsed papers under four ablation conditions, the categorical gate filters cross-domain candidates at roughly a 17:1 ratio while the quantitative-falsifier rate of accepted ideas stays above 83% throughout; every rejected candidate is retained with its per-axis rationale, so the gate doubles as a logging layer rather than a silent filter.

## 4. Trojaning the Alignment: Stealthy Backdoor Attacks against Graph Foundation Models

- Authors: Minhua Lin, Zhicheng Gao, Yilong Wang, Hanqing Lu, Xiang Zhang, Suhang Wang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-21
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.243230648543267
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.20991v1
- PDF: https://arxiv.org/pdf/2608.20991v1
- Local PDF: pdf/2026-08-25_04_Trojaning the Alignment_ Stealthy Backdoor Attacks against Graph Foundation Models.pdf

Graph Foundation Models (GFMs) on text-attributed graphs (TAGs) align graph representations with language semantics to support transferable graph learning. Despite these advantages, the backdoor vulnerability of GFMs on TAGs remains insufficiently understood, especially under graph-language alignment, where graph and text representations are trained to constrain each other in a shared semantic space. Existing backdoor attacks mainly target either the graph side or the text side, treating the two modalities independently. This makes direct adaptation ineffective: graph-only triggers can be constrained by clean text semantics, while text-only triggers alter the language view but do not directly shift the graph representation being aligned and scored. TAGs also impose a stealth challenge because triggers are exposed as both node text and local graph structure, making incoherent trigger attributes or anomalous subgraphs easy to inspect or filter. In this paper, we propose STAG, a stealthy trojan attack framework designed for the graph-language alignment interface of GFMs on TAGs. STAG coordinates a graph-trigger generator with a text-side soft prompt so that trigger-attached graph representations and triggered text representations move toward the same target-class text region. To address TAG-specific stealthiness, STAG realizes trigger nodes as readable text through candidate retrieval and regularizes the trigger-attached subgraph so that its local structure remains close to the original subgraph. Extensive experiments on multiple TAG datasets and representative GFMs demonstrate the effectiveness and stealthiness of STAG. Our code is available at https://github.com/ventr1c/STAG.

## 5. TH-GNN: Heterogeneous Temporal Graph Neural Networks for LLM-Agent Shilling Attack Detection

- Authors: Shivam Swarup, Divya Prakash Shrivastava, Rakesh Thakur
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-06-24
- DOI: Unavailable
- Categories: cs.CL, cs.LG
- Relevance: 3.1721771017294706
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.20376v1
- PDF: https://arxiv.org/pdf/2608.20376v1
- Local PDF: pdf/2026-08-25_05_TH-GNN_ Heterogeneous Temporal Graph Neural Networks for LLM-Agent Shilling Attack Detection.pdf

LLM agents can now generate realistic shilling profiles, fluent reviews, and coherent ratings at scale, systematically defeating recommender-system defenses. Text-only detectors that flag semantic drift in review embeddings are blind to graph structure and temporal coordination, while graph-only detectors that exploit neighborhood anomalies cannot reason over review semantics or the cross-modal inconsistencies produced by LLM-generated content. We propose TH-GNN, a heterogeneous temporal graph neural network with a two-layer Heterogeneous Graph Transformer backbone that applies per-type and per-relation attention augmented with learnable sinusoidal temporal encodings on every edge. Cross-modal attention fuses structural user embeddings with frozen RoBERTa representations of reviews and item descriptions, while a GRU operating over log inter-arrival times captures temporal burstiness. Evaluated across five attack families and four benchmark datasets, TH-GNN achieves a grand-mean F1 score of 0.870, outperforming the strongest text-only baseline on Agent4SR attacks by 10.9 percentage points and 11.5 percentage points at the lowest injection rate. These results demonstrate the effectiveness of jointly modeling temporal, structural, and semantic signals for detecting sophisticated LLM-driven shilling attacks.

## 6. Training, learning and inference: unified dynamics of neural systems

- Authors: Mian Wang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-21
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.1072293006730685
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.20965v1
- PDF: https://arxiv.org/pdf/2608.20965v1
- Local PDF: pdf/2026-08-25_06_Training, learning and inference_ unified dynamics of neural systems.pdf

We define an atomic generation fact f=(u,tau,omega,z;rho), recording the origin, realized transformation, concrete occurrence, generated result and relation role. Compiled into a Generation-Fact Graph (GFG), these facts provide an AI-native, compilable scientific fact substrate preserving generation histories. We establish a GFG-based recursive scientific process in which analysis, intervention, replay and validation form facts for later cycles. Using nanoGPT, we establish unified training-learning dynamics. Training is the evolution of a parameter-optimizer system with state and memory: each actual training action enters the receiving state and produces a finite-amplitude nonlinear functional response conditioned by that state and target-specific update geometry. Learning is the persistent reorganization of distributed functional support by these responses; capability formation, maintenance, decline or recovery becomes observable when target-specific states are evaluated against their readout boundaries. Three primary coordinates - target-boundary state, target-specific update geometry and parameter-Adam receiving state - yield a second-order predictor operating before post-update outputs are read. On held-out runs, it achieved 91.43% accuracy and 91.49% macro-averaged recall across four transitions. We further establish inference as a frozen projection of training-learning dynamics. Component gating and rollback show causal recruitment and non-additive combination of query-conditioned support formed during training, deriving organizational conditions realized by Attention. Controlled feedback indicates possible double-edged reinforcement effects. ResNet/CIFAR-100 and diffusion/CIFAR-10 experiments confirm receiving-state-conditioned responses, persistent support reorganization and frozen inference projection beyond nanoGPT.

## 7. Adapting Knowledge Graphs for Behavior Denoising in Sequential Recommendation

- Authors: Zichun Jin, Zihan Zhou, Yinan Liu, Bin Wang, Xiaochun Yang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-21
- DOI: Unavailable
- Categories: cs.IR, cs.AI
- Relevance: 3.082120138887852
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.21243v1
- PDF: https://arxiv.org/pdf/2608.21243v1
- Local PDF: pdf/2026-08-25_07_Adapting Knowledge Graphs for Behavior Denoising in Sequential Recommendation.pdf

Sequential recommendation predicts the next item from a user's interaction history, but not every interaction is equally informative. Real logs combine persistent preferences with temporary needs, exploration, and incidental behavior, so some interactions can distort history representations or provide unreliable supervision. Existing denoising methods judge such interactions mainly from co-occurrence, order, or model predictions, without explicit evidence from relations between items. Knowledge graphs (KGs) offer this evidence, but item popularity, graph degree, uneven coverage, and widely shared entities can inflate connectivity and bias reliability estimates. Here we present AdaptedKG, which derives calibrated KG evidence for each training example without adding graph representations to the recommendation model. It first compares the observed context with structurally matched alternatives to identify relational paths that are unusually prominent and uses them to build a local KG view. It then compares each interaction with structurally matched reference items to calibrate its support within that view. The resulting retention coefficients gate historical representations and reweight target losses. All sample-specific scores are computed offline using training interactions and a fixed KG, so the backbone remains unchanged and no KG access is required at inference. Experiments show gains with a standard sequential recommender and multiple behavior-denoising sequential recommenders.

## 8. Is Multimodal Speculative Decoding Ready for Diffusion-Based Parallel Drafting? A Survey and Empirical Diagnosis

- Authors: Yantao Li, Huanlin Gao, Fang Zhao, Chao Tan, Qiang Hui, Shuting Liu, Fuyuan Shi, Ting Lu, Shaoan Zhao, Xueqiang Guo, Xinpei Su, Jianbing Zhang, Xinyu Dai, Kai Wang, Shiguo Lian
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-21
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 3.039986792002715
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.20743v1
- PDF: https://arxiv.org/pdf/2608.20743v1
- Local PDF: pdf/2026-08-25_08_Is Multimodal Speculative Decoding Ready for Diffusion-Based Parallel Drafting_ A Survey and Empirical Diagnosis.pdf

Speculative decoding accelerates autoregressive generation by allowing a lightweight drafter to propose future tokens while a target model verifies them in parallel. Its lossless guarantee has motivated a line of work that pushes the drafter itself toward parallel generation. The most recent paradigm is block-parallel generative drafting, including diffusion-based methods such as DFlash and DSpark, achieving up to 3.6x speedup on common daily chatting tasks. While this transition is well studied in text-only LLMs, its applicability to multimodal models remains an open question. Existing multimodal speculative decoding efforts focus on input compression, adapter alignment, candidate coverage, or modality-specific verification; however, block-parallel generative drafting remains largely unexplored. To bridge this gap, this paper combines a modality-centered survey with a cross-architecture empirical study to ask: Is multimodal speculative decoding ready for diffusion-based parallel drafting? In this survey, we systematically analyze a wide spectrum of multimodal models, spanning Vision-Language, Video-Language, Audio, and Vision-Language-Action (VLA) architectures, from the dual perspectives of drafting parallelism and cross-modal information interaction. We introduce a unified taxonomy that isolates drafter-side parallelism from orthogonal design choices such as tree construction and verification strategies. Furthermore, we provide a comprehensive empirical comparison of existing methods under varying degrees of parallelism across standardized multimodal benchmarks, including OCR, VQA, visual reasoning, and image captioning. Finally, we summarize the limitations of current approaches, discuss open challenges, and outline promising future directions for this rapidly evolving field.

## 9. LingShu: A Large-Scale Symptom-Centric Contextualized Knowledge Graph Bridging Traditional Chinese Medicine and Modern Biomedicine

- Authors: Rui Hua, Zixin Shu, Kai Chang, Dengying Yan, Jianan Xia, Hui Zhu, Shujie Song, Shurui Yang, Tongxin Wang, Yue Yin, Yu Wei, Lijuan Pei, Yunhui Hu, Hao Xu, Mingzhong Xiao, Xiaodong Li, Haibin Yu, Runshun Zhang, Wenjia Wang, Baoyan Liu, Xuezhong Zhou
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-29
- DOI: Unavailable
- Categories: cs.CL, cs.AI
- Relevance: 3.012090818631445
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.20402v1
- PDF: https://arxiv.org/pdf/2608.20402v1
- Local PDF: pdf/2026-08-25_09_LingShu_ A Large-Scale Symptom-Centric Contextualized Knowledge Graph Bridging Traditional Chinese Medicine and Modern B.pdf

Biomedical knowledge graphs (KGs) are pivotal for knowledge organization, yet traditional binary relations often struggle to represent the conditional nature of biomedical knowledge. Symptoms provide a shared phenotypic layer for linking Traditional Chinese Medicine (TCM), which relies on symptom patterns for syndrome differentiation and treatment selection, with modern biomedicine, which connects clinical manifestations to diseases and molecular mechanisms. We present LingShu, a large-scale symptom-centric contextualized knowledge graph designed to bridge TCM and modern biomedicine. The exported version of LingShu analyzed in this study comprises 17.33 million atom-level entity records and 39.47 million relation records, including 17.19 million semantic triples and 22.29 million contextualized quadruples. LingShu integrates multi-source data, including clinical electronic medical records, authoritative TCM texts, biomedical ontologies, and curated knowledge bases, through a pipeline combining natural language processing, terminology normalization, and human-in-the-loop verification. A key innovation of LingShu is its hybrid data model: it maintains 64 typed triple relation patterns to ensure broad connectivity, while incorporating 35 contextual quadruple relation patterns to capture conditional medical associations. This dual-structure approach explicitly encodes conditional knowledge, providing a granular representation of the contexts associated with medical relations. These contextualized relations cover syndrome-dependent herb efficacy, disease-contextualized drug effects, population-specific clinical associations, and mechanism-related therapeutic responses. Furthermore, we developed a web platform (http://www.tcmkg.com/) that integrates graph visualization, graph-based reasoning, and an evidence-grounded knowledge question-answering agent.

## 10. Tydra: An Efficient Hybrid Model for Tabular Data

- Authors: Mieszko Komisarczyk, Saurabh Mathur, Maurice Kraus, Sriraam Natarajan, Kristian Kersting
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-21
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 2.972784950569103
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.21199v1
- PDF: https://arxiv.org/pdf/2608.21199v1
- Local PDF: pdf/2026-08-25_10_Tydra_ An Efficient Hybrid Model for Tabular Data.pdf

Transformer-based tabular foundation models such as TabPFN achieve strong predictive performance but incur quadratic computational cost with context length. On the other hand, subquadratic SSM-based alternatives such as Hydra trade away accuracy for efficiency. To balance both, we introduce Tydra, a hybrid Transformer-State Space Model (SSM) architecture for tabular in-context learning that interleaves attention and SSM layers. Across 30 OpenML datasets, Tydra reduces inference time by 30% relative to TabPFN while retaining much of its predictive performance. Tydra also outperforms an approximately ten-times-larger Hydra model while providing faster inference. The results indicate that hybrid architectures are a promising direction for tabular foundation models.

## 11. A2DINOv3: Rethinking Multi-Modal Object Detection via Socialized Collaboration

- Authors: Jiekang Feng, Zhihe Fan, Yunqi Zhu, Xinjie Yao, Yueying Zhang, Yike Gao, Ranxin Li, Guanzuo Chen
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-21
- DOI: Unavailable
- Categories: cs.CV, cs.AI
- Relevance: 2.9482111990713253
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.21099v1
- PDF: https://arxiv.org/pdf/2608.21099v1
- Local PDF: pdf/2026-08-25_11_A2DINOv3_ Rethinking Multi-Modal Object Detection via Socialized Collaboration.pdf

Multi-modal object detection is essential for robust scene understanding in challenging conditions, including low-light and adverse environments. Recent vision foundation models (e.g., DINOv3) have exhibited strong representation capabilities, yet adapting them to multi-modal scenarios remains challenging. Existing dense cross-modal fusion strategies often force heterogeneous modalities to interact indiscriminately, which may introduce redundant information and disrupt the valuable pre-trained representations. To address this issue, we revisit multi-modal fusion from the perspective of socialized learning and propose adapter to DINOv3 (A2DINOv3), a multi-expert collaboration framework with a Socialized Collaboration Protocol (SCP). Specifically, RGB and infrared branches are modeled as heterogeneous experts that independently preserve their specialized knowledge while exchanging complementary information through selective and constrained interactions. This design mitigates harmful cross-modal interference and prevents degradation of pre-trained priors during adaptation. Furthermore, a zero-initialization strategy is introduced to gradually activate cross-modal collaboration, enabling a smooth transition from modality-specific learning to cooperative representation learning. Extensive experiments on four multi-modal benchmarks, including aerial detection (GAIIC), autonomous driving (FLIR), low-light surveillance (LLVIP), and diverse real-world scenarios (M3FD), demonstrate that A2DINOv3 consistently achieves state-of-the-art performance in multi-modal object detection.

## 12. Deep Learning Models Also Recall Features

- Authors: Pierre Beckmann
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-21
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 2.9381722184123444
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.20970v1
- PDF: https://arxiv.org/pdf/2608.20970v1
- Local PDF: pdf/2026-08-25_12_Deep Learning Models Also Recall Features.pdf

Recent work in mechanistic interpretability has studied how large language models recall facts stored in their weights. This paper argues that factual recall points to something broader: a general kind of operation in deep learning models, which I call feature recall. The core observation is that a linear projection can be read as retrieving stored information scaled by input activations. I define feature recall, show it applies across architectures, and contrast it with the established paradigm of feature combination. I also consider how cases of feature recall might be mechanistically identified. The account gives philosophers a new conceptual tool for understanding deep learning, and points to empirical directions for mechanistic interpretability research.

## 13. MGAL: A Multilingual Granularity-Aware Long-Context Benchmark

- Authors: Chunhan Li, Chenglin Xu, Zongyang Zhang, Jiale Liu, Zhuoxi Rao, Xudong Jia, Junxiu He, Menglin Yang, Wenjuan Gong, Zhengzhe Liu, Chengwei Qin
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-21
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 2.9332931580583055
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.20853v1
- PDF: https://arxiv.org/pdf/2608.20853v1
- Local PDF: pdf/2026-08-25_13_MGAL_ A Multilingual Granularity-Aware Long-Context Benchmark.pdf

Evaluation of long-context Large Language Models (LLMs) has advanced rapidly. However, most existing benchmarks are limited to the document level and focus mainly on high-resource languages, leaving many fine-grained challenges insufficiently evaluated. To address this gap, we present MGAL, the first multilingual, granularity- and position-aware long-context benchmark. MGAL is constructed from United Nations (UN) reports spanning 8K to 128K tokens across the six official UN languages. It covers four coherent levels of linguistic granularity (word, sentence, paragraph, and document) and further stratifies entries by their position within the document (begin, middle, and end), indexed at both the document and paragraph levels. This design enables systematic diagnosis of multilingual long-context comprehension across different granularities.
  Through extensive experiments and analyses, we find that: (1) LLMs perform well at word-level tasks but struggle with coarser-grained ones; and (2) Closed-source models retain a clear performance advantage in lower-resource languages. We further identify two new challenges: (1) Under local semantic crowding, where neighboring sentences share topics and entities, models tend to follow surface cues (e.g., connectives like ``however'' or repeated entities) rather than the discourse role of the sentence in surrounding context (e.g., background, outcome); and (2) A gap between fluency and consistency in generated outputs, where models produce text that reads smoothly but drifts from the source facts. In addition, we observe several patterns in line with prior studies, including reliance on nearby evidence and reuse of options under uncertainty.

## 14. PerturbRx: Learning Treatment-Conditioned Latent Transitions for Patient Drug Response Prediction

- Authors: Yoshitaka Inoue, Minoh Jeong, Alfred Hero, Rui Kuang, Augustin Luna
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-21
- DOI: Unavailable
- Categories: q-bio.QM, cs.LG
- Relevance: 2.9071918390417615
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.21349v1
- PDF: https://arxiv.org/pdf/2608.21349v1
- Local PDF: pdf/2026-08-25_14_PerturbRx_ Learning Treatment-Conditioned Latent Transitions for Patient Drug Response Prediction.pdf

Scarce data and tumor heterogeneity limit patient-level cancer treatment-response prediction. Existing approaches predict response from pretreatment molecular profiles and drug representations, without explicitly modeling the molecular changes expected under treatment. We propose PerturbRx, a treatment-conditioned representation learning framework that learns intervention-induced latent transitions and uses them as patient-drug response features. PerturbRx trains a drug- and dose-conditioned transition predictor from context-matched but cell-unpaired control and treated single-cell populations, then freezes and transfers the predictor to pretreatment patient profiles without requiring post-treatment measurements. The transition is combined with patient and drug representations to predict response. Across TCGA and patient-derived xenograft benchmarks, PerturbRx achieves the strongest aggregate predictive performance among the evaluated methods. These results support perturbation-pretrained latent transitions as useful representations for patient-level drug-response prediction.

## 15. TracingFlow: A Simulation-Free Trajectory Inference Framework Based on Second-Order Dynamics

- Authors: Yuhao Sun, Zekun Wu, Zixun Huang, Peijie Zhou
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-21
- DOI: Unavailable
- Categories: cs.LG, cs.AI, q-bio.GN
- Relevance: 2.9010201378681097
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.21070v1
- PDF: https://arxiv.org/pdf/2608.21070v1
- Local PDF: pdf/2026-08-25_15_TracingFlow_ A Simulation-Free Trajectory Inference Framework Based on Second-Order Dynamics.pdf

Inferring continuous system evolution from sparse temporal snapshots is a key challenge in generative modeling and single-cell omics. While Optimal Transport (OT) is popular, existing frameworks are largely restricted to first-order dynamics, assuming memoryless velocity fields. This limits expressiveness, as first-order systems fail to account for regulatory momentum and time-delayed responses inherent in processes like cell differentiation. Here, we introduce TracingFlow, a simulation-free Flow Matching framework generalizing to second-order dynamics. By using neural networks to regress the acceleration field, TracingFlow provides an exact, efficient solution to the Dynamical Optimal Acceleration Transport (DOAT) problem. Unlike first-order methods yielding over-smoothed trajectories, our second-order formulation captures high-curvature transitions and nonlinear evolutions by learning the underlying force fields. Evaluated on complex synthetic and large-scale scRNA-seq datasets, TracingFlow achieves superior accuracy in distributional reconstruction and trajectory faithfulness. Moreover, by integrating lineage tracing priors, it recovers dynamical structures that are both mathematically optimal and biologically plausible.

## 16. Nexus: Depth-Adaptive KV-Cache Splicing and Retrieval-Decoupled Tool Routing for Agentic LLMs on Unified Memory

- Authors: Mustafa Arslan
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-01
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 2.899017122685774
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.20397v1
- PDF: https://arxiv.org/pdf/2608.20397v1
- Local PDF: pdf/2026-08-25_16_Nexus_ Depth-Adaptive KV-Cache Splicing and Retrieval-Decoupled Tool Routing for Agentic LLMs on Unified Memory.pdf

Agentic large language models (LLMs) on the Model Context Protocol (MCP) re-encode verbose tool schemas every turn, so prefill - quadratic in sequence length - dominates time-to-first-token (TTFT) as the tool registry grows. Nexus's primary lever is to decouple routing from the schema-prefill cost: an INT8 semantic lookaside buffer (SLB) with a calibrated cross-encoder margin gate selects tools by retrieval, and arguments are generated over a compressed textual signature (median 19 tokens) rather than over spliced key/value (KV) cache. This path is depth-independent: routing accuracy stays near 89% as the registry scales to 250 tools - where a concatenate-all-schemas baseline overflows the context window entirely - and it reaches a first-argument token 1.66x sooner than a full-schema re-prefill at a ~80% main-context token saving. As a secondary, bounded lever we transplant a compiled schema KV block directly into the live context. This is fundamentally limited by rotary position embedding (RoPE) phase drift: an anchored splice is output-exact, but off-anchor placement corrupts attention, so beyond a threshold P=256 Nexus repairs the seam with a depth-adaptive suffix redecode that escalates to a full re-prefill. The resulting never-regress property is a guarantee on output fidelity (top-1 agreement, D_KL approx. 0) - not on latency, which can dip to 0.98x before converging to parity - alongside a 1.1-1.7x TTFT speedup at moderate depth that narrows to parity at deep context. Two negative results bound the design: the off-anchor RoPE fidelity boundary, and the failure of a reference-free drift gate to predict drift (Spearman rho = 0.193). All measurements are from one model tuple (Qwen2.5-14B-Instruct Q4_K_M) on Apple-silicon unified memory; the qualitative boundaries generalize, while the quantitative envelope is tuple-specific.

## 17. Volumetric Radiology AI in the Era of Multimodal Large Language Models

- Authors: Zanting Ye, Shengyuan Liu, Xin Liu, Chenhui Wang, Zhisong Wang, Jiashuai Liu, Zipei Wang, Cheng Wang, Wentao Pan, Mengjie Fang, Di Dong, Mohammad Salmanpour, Arman Rahmim, Yu Gu, Yong Xia, Hongming Shan, Yixuan Yuan, Yefeng Zheng, Lijun Lu
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-20
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 2.8946789459895106
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.20549v1
- PDF: https://arxiv.org/pdf/2608.20549v1
- Local PDF: pdf/2026-08-25_17_Volumetric Radiology AI in the Era of Multimodal Large Language Models.pdf

Advances in multimodal large language models (MLLMs) are extending radiological artificial intelligence (AI) beyond task-specific image analysis toward multimodal understanding and reasoning. Volumetric radiology, however, presents a fundamental representational mismatch: clinical interpretation often requires full-volume spatial context and acquisition-dependent quantitative information, whereas current MLLMs are commonly conditioned on selected two-dimensional (2D) images, compressed visual representations, or report-derived text. Reliable volumetric radiology AI therefore requires representations that preserve task-relevant three-dimensional (3D) information and systems that can access, verify, and integrate this information across clinical workflows. In this Review, we examine more than 200 publications through July 2026. We organize the literature around volumetric representation and multimodal understanding at the model level, agentic orchestration at the system level, and their links to clinical applications and evaluation. We review volumetric foundation models, language alignment and compression strategies, and agentic systems that extend MLLMs through planning, tools, memory, and workflow interaction. We distinguish settings in which selected 2D views or report-mediated reasoning may suffice from those that warrant native volumetric modeling. We also introduce a Claim-Design-Validation framework to assess whether technical, workflow, and clinical claims are matched by appropriate design and validation. Across the literature, native volumetric modeling and agentic capabilities depend on the spatial, quantitative, contextual, and workflow requirements of the intended task. Clinical credibility requires faithful volumetric representation, traceable system behavior, claim-aligned validation, and clearly defined human oversight in realistic workflows.

## 18. Causal Modeling of Adverse Pregnancy Outcomes via Adaptive LLM Proposals

- Authors: Kavimayil P. Komarasamy, Saurabh Mathur, Ameet Soni, David M. Haas, Kristian Kersting, Sriraam Natarajan
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-21
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 2.86058917305422
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.21079v1
- PDF: https://arxiv.org/pdf/2608.21079v1
- Local PDF: pdf/2026-08-25_18_Causal Modeling of Adverse Pregnancy Outcomes via Adaptive LLM Proposals.pdf

Adverse Pregnancy Outcomes (APOs) such as preterm birth and gestational diabetes can have long-term consequences for both the mother and child, yet an understanding of their causes remains elusive. Causal discovery in this domain is especially challenging due to a paucity of data and incomplete domain knowledge. As a result, pure data-driven methods fail, and Large Language Model (LLM) outputs remain inconsistent or contradictory. We introduce a neurosymbolic framework for generating plausible causal hypotheses that iteratively combines the broad prior knowledge of LLMs with empirical scoring on data. Our method treats the LLM as an adaptive proposal distribution, generating hypotheses that are scored against empirical data; the resulting high-scoring graphs are then used to update the LLM's context, steering subsequent generations toward more promising regions of the hypothesis space. We evaluate our approach on a real-world clinical dataset for modeling APOs and their risk factors, comparing our results against an expert-constructed causal graph. Our method recovers all expert-validated edges and identifies additional plausible causal relations not previously listed by experts, potentially providing new insights for targeted interventions.

## 19. Denoising the Future: Context-Aware Spectral Diffusion for Temporal Knowledge Graph Extrapolation

- Authors: Yanglei Gan, Peng He, Run Lin, Peiyuan Jiang, Yifan Wang, Qiao Liu
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-21
- DOI: Unavailable
- Categories: cs.CL, cs.AI
- Relevance: 2.8591760228648786
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.20804v1
- PDF: https://arxiv.org/pdf/2608.20804v1
- Local PDF: pdf/2026-08-25_19_Denoising the Future_ Context-Aware Spectral Diffusion for Temporal Knowledge Graph Extrapolation.pdf

Temporal Knowledge Graph (TKG) extrapolation seeks to infer future facts from time-varying relational histories. Recent diffusion-based approaches improve uncertainty modeling through generative denoising, but their aggregated conditioning on subject histories may insufficiently distinguish query-specific evidence from non-salient historical facts, thereby diluting target-discriminative signals. To bridge this gap, we propose FreqDiff, a Frequency-aware Diffusion framework for TKG extrapolation. Specifically, FreqDiff formulates future object prediction as query-slot denoising and develops a dual-stream denoiser that integrates temporal dependency modeling with context-aware spectral calibration. The spectral branch synthesizes history-conditioned filters from learnable bases to adaptively re-calibrate denoising representations, while a frequency-domain regularizer is proposed to align the denoised target with the gold object in spectral space. Experiments on four public TKG benchmarks demonstrate that FreqDiff achieves state-of-the-art performance.

## 20. An LLM agent for end-to-end computational materials discovery

- Authors: Chen Yuntong, Huang Ju, Liu Yu, Zhao Dan, Sun Mingqi, Ju Chentian, Liu Yanbing, Huang Lijiang, Zhao Guobin
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-20
- DOI: Unavailable
- Categories: cond-mat.mtrl-sci, cs.AI
- Relevance: 2.82680041756871
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.20434v1
- PDF: https://arxiv.org/pdf/2608.20434v1
- Local PDF: pdf/2026-08-25_20_An LLM agent for end-to-end computational materials discovery.pdf

The coordination of multi-scale tasks is an effective strategy for computational materials discovery, yet the repeated application of diverse algorithms and tools renders it challenging. We report MAESTRO, a large language model (LLM) agent system capable of executing the entire screening pipeline for metal-organic frameworks (MOFs). It processes a large body of MOF literature, links relevant publications to their crystal structures, and curates the results into a computation-ready database, which is then screened through a strategy of progressively increasing computational cost. The promising candidates identified for separation under wet flue gas conditions all originate from unrelated studies. By connecting the heterogeneous stages of computational materials discovery, the LLM-based agents of MAESTRO can operate across application domains and uncover high-performance materials that conventional screening approaches would be unlikely to consider.

## 21. Shared Physics Responses Recover Hidden Rankings in Neural Operator Libraries

- Authors: Hanbing Liang, Fujun Liu
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-20
- DOI: Unavailable
- Categories: cs.LG, math.NA, physics.comp-ph
- Relevance: 2.8137354246052206
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.20441v1
- PDF: https://arxiv.org/pdf/2608.20441v1
- Local PDF: pdf/2026-08-25_21_Shared Physics Responses Recover Hidden Rankings in Neural Operator Libraries.pdf

Selecting the optimal neural-operator prediction during deployment is challenging when high-fidelity reference solutions are unavailable. We demonstrate that under a squared Hilbert-space loss, ranking a finite model library depends strictly on the low-dimensional span of candidate differences, allowing us to score all models simultaneously using a single anchor-based linearized response of the governing equation. This shared physical diagnostic accurately recovered over 99.6\% of pairwise preferences and 99.0\% of optimal checkpoints across diverse Fourier and convolutional operator libraries for fluid, reaction-diffusion, and wave dynamics. Furthermore, the corrected physical proxy frequently outperformed the best individual candidates, and we establish computable sufficient conditions that rigorously certify exact decisions for strongly monotone discretizations. By exploiting the local dynamical response rather than raw defect magnitude, this framework enables the reliable and highly efficient deployment of scientific surrogates without requiring ground-truth data.

## 22. A Survey on Foundations and Frontiers of Multimodal Agentic Frameworks: Techniques and Applications

- Authors: Neel Mokaria, Rishie Raj, Dheeraj Baiju, Xiaoqian Shen, Shraman Pramanick, Kevin Qinghong Lin, Arda Senocak, Mike Zheng Shou, Philip Torr, Mohamed Elhoseiny, Yapeng Tian, Ruohan Gao, Salman Khan, Sayan Nag, Sanjoy Chowdhury, Dinesh Manocha
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-06-28
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 2.811381144858939
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.20379v1
- PDF: https://arxiv.org/pdf/2608.20379v1
- Local PDF: pdf/2026-08-25_22_A Survey on Foundations and Frontiers of Multimodal Agentic Frameworks_ Techniques and Applications.pdf

Advances in large language models (LLMs) have fueled a wave of research into agency: the ability to reason, plan, and act. This effort has produced agentic frameworks that orchestrate perception, memory, and decision-making around powerful LLM backbones. With the advent of large multimodal models (LMMs), these systems can process and integrate diverse modalities, including images, audio, and video, thereby improving their real-world applicability. Yet, while surveys of LLM-based agents exist, the role of multimodality in shaping agency has not been systematically examined in recent years. This survey fills the gap by analyzing the impact of multimodality across the core functional modules of the agentic framework: perception, reasoning, planning, memory, and action. Using this lens, we trace the evolution from text-centric agents to multimodal frameworks, examine how modalities are integrated through delegated, late-fusion, and early-fusion architectures, and assess the emergence of agentic behaviors enabled by grounded perception and multimodal reasoning. We organize existing work through a modality-centric taxonomy that links architectural design choices to agent capabilities. Moreover, we review multimodal agentic systems across various application domains, including Robotics, GUI & Web Navigation, Multimedia Content Generation & Editing, and Long-form Video Understanding & Retrieval. Beyond capabilities, we analyze performance across these settings and discuss efficiency-scalability trade-offs, including training and inference costs, latency, and deployment constraints. By focusing on the impact of multimodality in agentic design, we aim to identify key gaps and chart a roadmap toward robust and general-purpose intelligent systems.

## 23. FL-MAESTRO: Multi-Agent LLM Orchestration for Resource-Constrained Federated Learning

- Authors: Jiajun Wu, Zirui Wang, Jiayu Zhou, Qiang Ye, Steve Drew
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-20
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 2.7989264179675164
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.20518v1
- PDF: https://arxiv.org/pdf/2608.20518v1
- Local PDF: pdf/2026-08-25_23_FL-MAESTRO_ Multi-Agent LLM Orchestration for Resource-Constrained Federated Learning.pdf

In Federated Learning (FL), the communication topology is a runtime variable rather than a fixed design choice, since links and edge devices drop in and out during training. Each round, the server must commit three coupled decisions, namely the communication topology, per-client resource allocation, and the aggregation rule for combining local updates. Recent agentic systems have begun bringing large language models (LLM) into FL, but the existing line of work either operates at setup time or handles a single runtime dimension such as client selection. We propose FL-MAESTRO, a multi-agent orchestrator that makes the joint runtime FL decision directly through three specialist LLM agents, one per decision dimension. A coordinator combines their analyses into a single decision, and a non-LLM feasibility check confirms it before the round executes. Because the orchestrator consumes the server's predicted-failure list, it withholds clients whose updates would never be aggregated, which removes the dominant source of wasted round energy in classical FL on volatile edge networks. Because client state is read as natural-text profiles, the same orchestrator extends to heterogeneous device classes without per-class energy models. On a non-IID CIFAR-10 benchmark, FL-MAESTRO matches the accuracy of the strongest energy-aware baseline while cutting wasted round energy from over a third to near zero. Code is available at https://github.com/denoslab/FL-MAESTRO.

## 24. COEC: Calibrated Orthogonal-Equivalence Compensation for Structured Pruning of Large Language Models

- Authors: Peiqi Yu, Nam Ling, Wei Wang, Wei Jiang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-21
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 2.7966597822154093
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.21142v1
- PDF: https://arxiv.org/pdf/2608.21142v1
- Local PDF: pdf/2026-08-25_24_COEC_ Calibrated Orthogonal-Equivalence Compensation for Structured Pruning of Large Language Models.pdf

Structured pruning reduces the size and inference cost of large language models (LLMs) by removing weight columns, but the resulting output error can degrade accuracy. Existing training-free compensation methods use an additive bias or a single orthogonal rotation on the output side of the retained weight. These corrections leave its input singular frame unchanged and therefore limit how the retained weight can adapt after column removal. We propose COEC (Calibrated Orthogonal-Equivalence Compensation), a training-free compensation framework that applies alternating left and right orthogonal rotations to the retained weight. The right rotation is optimized on a reduced Stiefel manifold, while singular values are rescaled using generalized cross-validation to select the regularization strength for each layer. COEC further tempers the calibration Gram matrix to reduce the dominance of high-energy activation directions and introduces an alignment penalty that preserves the geometric relation between adjacent attention projections.All components use second-order statistics from a small calibration set and require neither backpropagation through the LLM nor retraining of the model parameters. COEC is independent of the column pruning criterion and can be applied to multiple structured pruning methods. Experiments on the Llama-3, Llama-3.1, and Qwen2.5 model families across multiple structured sparsity levels show that COEC improves perplexity on every model and zero-shot accuracy in most settings over existing compensation methods, with larger gains at higher sparsity. These results show that post-pruning compensation can recover part of the performance lost to column removal.

## 25. Knowledge-Graph-Gated Defactualization for Style-Controllable and Fact-Preserving Generation in Agentic Conversational AI

- Authors: Tanmay Kumar Shrivastava, Darsh Rohit Nandu, Rajesh Kumar Mundotiya
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-01
- DOI: Unavailable
- Categories: cs.CL, cs.AI
- Relevance: 2.780516927059855
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.20393v1
- PDF: https://arxiv.org/pdf/2608.20393v1
- Local PDF: pdf/2026-08-25_25_Knowledge-Graph-Gated Defactualization for Style-Controllable and Fact-Preserving Generation in Agentic Conversational A.pdf

Agentic large language models (LLMs) deployed in fact-sensitive applications such as customer support must simultaneously preserve factual correctness and generate responses in a controllable stylistic register. Activation steering enables fine-tuning-free style control by perturbing hidden representations, but it lacks an explicit mechanism for distinguishing verifiable facts from stylistic content, leading to semantic leakage. We address this challenge through \emph{Defactualize-Steer-Rehydrate} (DSR), a knowledge-engineering framework that integrates a typed, salience-weighted knowledge graph (KG) with activation steering. DSR extracts salient entities using a layered regex or NER or lexical-classifier pipeline, replaces them with typed placeholders prior to steering, and deterministically restores verified values through salience-guided rehydration after generation. DSR is evaluated across six LLaMA-family models (1B--13B parameters) on 600 A2A-generated customer-support cases (1,200 generations), with a dedicated KG ablation study. DSR significantly increases verified-entity recovery relative to a steering-only baseline (Cohen's $d=0.225$, $p_{\text{Bonf}}=1.0\times10^{-4}$), though the absolute recovery rate remains modest, while preserving effective style control across diverse model families. Layer-wise separability and steering-strength diagnostics further show previously unexplored interactions between representation-level steering and factual grounding. hese results demonstrate that explicit knowledge engineering can systematically enhance trustworthy, controllable, and reproducible generative AI without requiring model fine-tuning. Code, cached steering vectors, and evaluation scripts are publicly released to support reproducibility.\footnote{https://github.com/Tanmay-IITDSAI/KG-Gated-Defactualization}

## 26. FS-Researcher: Test-Time Scaling for Long-Horizon Research Tasks with File-System-Based Agents

- Authors: Chiwei Zhu, Benfeng Xu, Mingxuan Du, Shaohan Wang, Xiaorui Wang, Zhendong Mao, Yongdong Zhang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.759719305773193
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.288/
- PDF: https://aclanthology.org/2026.acl-long.288.pdf
- Local PDF: pdf/2026-08-25_26_FS-Researcher_ Test-Time Scaling for Long-Horizon Research Tasks with File-System-Based Agents.pdf

Deep research is emerging as a representative long-horizon task for large language model (LLM) agents. However, long trajectories in deep research often exceed model context limits, compressing token budgets for both evidence collection and report writing, and preventing effective test-time scaling. We introduce FS-Researcher, a file-system-based, dual-agent framework that scales deep research beyond the context window via a persistent workspace. Specifically, a Context Builder agent acts as a librarian which browses the internet, writes structured notes, and archives raw sources into a hierarchical knowledge base that can grow far beyond context length. A Report Writer agent then composes the final report section by section, treating the knowledge base as the source of facts. In this framework, the file system serves as a durable external memory and a shared coordination medium across agents and sessions, enabling iterative refinement beyond the context window. Experiments on two open-ended benchmarks (DeepResearch Bench and DeepConsult) show that FS-Researcher achieves state-of-the-art report quality across different backbone models. Further analyses demonstrate a positive correlation between final report quality and the computation allocated to the Context Builder, validating effective test-time scaling under the file-system paradigm. The code and data are open-sourced at https://github.com/Ignoramus0817/FS-Researcher .

## 27. Consistency Models for Fast MRI Reconstruction Using Regularization by Denoising

- Authors: Merve Gülle, Junno Yun, Yaşar Utku Alçalar, Mehmet Akçakaya
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-20
- DOI: Unavailable
- Categories: eess.IV, cs.AI, cs.CV, cs.LG, physics.med-ph
- Relevance: 2.7583337624652193
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.20561v1
- PDF: https://arxiv.org/pdf/2608.20561v1
- Local PDF: pdf/2026-08-25_27_Consistency Models for Fast MRI Reconstruction Using Regularization by Denoising.pdf

Diffusion models (DMs) have emerged as powerful generative priors for MRI reconstruction with promising results. Yet DM-based methods require extensive iterative refinement, limiting their practical deployment. Consistency models (CMs) provide a compelling alternative, aiming to map out the diffusion trajectory in a single pass, enabling faster generation. In this work, we propose CM-RED, a novel MRI reconstruction method that integrates a pretrained CM into the regularization by denoising (RED) scheme. Our method builds on accelerated proximal gradient RED (RED-APG), and further incorporates controlled noise injection during the update steps to enhance generative diversity and accelerate convergence. Extensive experiments on the fastMRI knee and brain datasets demonstrate that CM-RED achieves high-quality reconstructions across multiple anatomies, contrast weights, acceleration factors, and undersampling patterns, using only 4 network function evaluations (NFEs). The proposed method consistently outperforms existing DM- and CM-based approaches in both quantitative metrics and visual fidelity, and exhibits strong robustness to hyperparameter variations, highlighting CM-RED as an efficient and effective generative framework for accelerated MRI reconstruction. The source code and pretrained models are publicly available at https://github.com/MerveGulle/CM-RED.

## 28. MoRI: Learning Motivation-Grounded Reasoning for Scientific Ideation in Large Language Models

- Authors: Chenyang Gu, Jiahao Cheng, Meicong Zhang, Pujun Zheng, Jinquan Zheng, Guoxiu He
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.757859794124396
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1609/
- PDF: https://aclanthology.org/2026.acl-long.1609.pdf
- Local PDF: pdf/2026-08-25_28_MoRI_ Learning Motivation-Grounded Reasoning for Scientific Ideation in Large Language Models.pdf

Scientific ideation aims to propose novel solutions within a given scientific context. Existing LLM-based agentic approaches emulate human research workflows, yet inadequately model scientific reasoning, resulting in surface-level conceptual recombinations that lack technical depth and scientific grounding. To address this issue, we propose MoRI ( Mo tivation-grounded R easoning for Scientific I deation), a framework that enables LLMs to explicitly learn the reasoning process from research motivations to methodologies. The base LLM is initialized via supervised fine-tuning to generate a research motivation from a given context, and is subsequently trained under a composite reinforcement learning reward that approximates scientific rigor: (1) entropy-aware information gain encourages the model to uncover and elaborate high-complexity technical details grounded in ground-truth methodologies, and (2) contrastive semantic gain constrains the reasoning trajectory to remain conceptually aligned with scientifically valid solutions. Empirical results show that MoRI consistently outperforms strong commercial LLMs and complex agentic baselines across multiple dimensions, including novelty, technical rigor, and feasibility. The code is available on GitHub.

## 29. GroupRank: A Groupwise Paradigm for Effective and Efficient Passage Reranking with LLMs

- Authors: Meixiu Long, Duolin Sun, Dan Yang, Yihan Jiao, Lei Liu, Jiahai Wang, Binbin Hu, Yue Shen, Jie Feng, Zhehao Tan, Junjie Wang, Lianzhen Zhong, Jian Wang, Peng Wei, Jinjie Gu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.7571957028345033
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1260/
- PDF: https://aclanthology.org/2026.findings-acl.1260.pdf
- Local PDF: pdf/2026-08-25_29_GroupRank_ A Groupwise Paradigm for Effective and Efficient Passage Reranking with LLMs.pdf

Large Language Models (LLMs) have emerged as powerful tools for passage reranking in information retrieval, leveraging their superior reasoning capabilities to address the limitations of conventional models on complex queries. However, current LLM-based reranking paradigms are fundamentally constrained by an efficiency-accuracy trade-off: (1) pointwise methods are efficient but ignore inter-document comparison, yielding suboptimal accuracy; (2) listwise methods capture global context but suffer from context-window constraints and prohibitive inference latency. To address these issues, we propose GroupRank, a novel paradigm that balances flexibility and context awareness. To unlock the full potential of groupwise reranking, we propose an answer-free data synthesis pipeline that fuses local pointwise signals with global listwise rankings. These samples facilitate supervised fine-tuning and reinforcement learning, with the latter guided by a specialized group-ranking reward comprising ranking-utility and group-alignment. These complementary components synergistically optimize document ordering and score calibration to reflect intrinsic query-document relevance.Experimental results show GroupRank achieves a state-of-the-art 65.2 NDCG@10 on BRIGHT and surpasses baselines by 2.1 points on R2MED, while delivering a 6.4 × inference speedup. The code is available at https://github.com/AQ-MedAI/Diver/tree/main/Reranker/GroupRank .

## 30. Beyond Meta-Reasoning: Metacognitive Consolidation for Self-Improving LLM Reasoning

- Authors: Ziqing Zhuang, Linhai Zhang, Jiasheng Si, Deyu Zhou, Yulan He
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.757153603548069
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1095/
- PDF: https://aclanthology.org/2026.acl-long.1095.pdf
- Local PDF: pdf/2026-08-25_30_Beyond Meta-Reasoning_ Metacognitive Consolidation for Self-Improving LLM Reasoning.pdf

Large language models (LLMs) have demonstrated strong reasoning capabilities, and as existing approaches for enhancing LLM reasoning continue to mature, increasing attention has shifted toward meta-reasoning as a promising direction for further improvement. However, most existing meta-reasoning methods remain episodic: they focus on executing complex meta-reasoning routines within individual instances, but ignore the accumulation of reusable meta-reasoning skills across instances, leading to recurring failure modes and repeatedly high metacognitive effort. In this paper, we introduce Metacognitive Consolidation, a novel framework in which a model consolidates metacognitive experience from past reasoning episodes into reusable knowledge that improves future meta-reasoning. We instantiate this framework by structuring instance-level problem solving into distinct roles for reasoning, monitoring, and control to generate rich, attributable meta-level traces. These traces are then consolidated through a hierarchical, multi-timescale update mechanism that gradually forms evolving meta-knowledge. Experimental results demonstrate consistent performance gains across benchmarks and backbone models, and show that performance improves as metacognitive experience accumulates over time.
