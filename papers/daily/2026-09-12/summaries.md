# Paper Daily Reading - 2026-09-12

## 1. Reification as a Transferable Vocabulary: Zero-Shot Link Prediction with Vanilla GNNs

- Authors: Camille Pradel
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-10
- DOI: Unavailable
- Categories: cs.LG, cs.AI
- Relevance: 3.574069795448045
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.11347v1
- PDF: https://arxiv.org/pdf/2609.11347v1
- Local PDF: pdf/2026-09-12_01_Reification as a Transferable Vocabulary_ Zero-Shot Link Prediction with Vanilla GNNs.pdf

Knowledge graph foundation models such as ULTRA achieve zero-shot link prediction on unseen graphs through dedicated architectures that hard-code a transfer mechanism. In this work we move that mechanism out of the architecture and into the representation, by \emph{reifying} the input graph: every fact becomes a node, connected to its subject, object, and relation type through a fixed vocabulary of six meta-relations, with relation types as anonymous shared nodes rather than model parameters. On this representation, five textbook GNNs (GAT, GINE with sum and with mean+max aggregation, GraphSAGE, R-GCN), each trained on a single knowledge graph of 4,245 triples for 30 minutes on one NVIDIA A100, transfer zero-shot to 40 inductive link-prediction benchmarks. The best of them, an off-the-shelf GAT, matches ULTRA, a dedicated foundation model pretrained on three graphs, across ULTRA's own evaluation suite. The same fixed vocabulary extends to relational databases, a row becoming an entity and a foreign-key column a relation type; a preliminary probe on two unseen databases, with no cell values, schema text or in-context labels, shows a model of this family pretrained on three knowledge graphs ranking foreign-key targets far above random-initialization and degree controls. We release the code, the checkpoints, and the evaluation pipeline for all 40 benchmarks.

## 2. Geospatial AI, Dataverse Metadata, and the Study of Place-Based Government

- Authors: Danny EBanks, Devika Jain
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-10
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 3.33554568351059
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.11674v1
- PDF: https://arxiv.org/pdf/2609.11674v1
- Local PDF: pdf/2026-09-12_02_Geospatial AI, Dataverse Metadata, and the Study of Place-Based Government.pdf

Harvard Dataverse hosts over 150,000 research datasets, but the geographic information those datasets carry is entered as free text by depositors and has never been assembled into a searchable structure. We construct a knowledge graph from the repository's public data and metadata, organizing 102,650 datasets within a 215,985-node network of 528,003 edges linking datasets to keywords, publications, subjects, journals, and locations. Of those datasets, 43,991 (42.9 percent) carry at least one geospatial field, geographic coverage, geographic unit, or a bounding box and 96.9 percent of all nodes sit in a single connected component, so datasets remain reachable from one another even when their geospatial metadata share nothing in common. A conservative keyword search identifies 7,654 geospatially tagged datasets (17.4 percent) as directly policy-relevant, with elections and legislatures the largest cluster, followed by government administration, health policy, transportation, and education. Five datasets illustrate how this metadata behaves across policy domains and spatial scales, and an extended use case shows how community language models, stance detection with geographic aggregation, and partisan language bridging tools can attach discourse to place. The central obstacle is place resolution: the same location appears as many disconnected nodes. We argue that the graph provides a concrete setting for developing AI-driven metadata enrichment and entity resolution, and we document its coverage skew toward American, city-level data.

## 3. Enabling Knowledge Graph Understanding at Scale with the EXplore Your Graphs ENgine (EXYGEN)

- Authors: Harshdeep Singh, Yurui Zhu, Giovanni Colavizza, Matteo Romanello
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-10
- DOI: Unavailable
- Categories: cs.AI, cs.LG
- Relevance: 3.2937911873764056
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.11569v1
- PDF: https://arxiv.org/pdf/2609.11569v1
- Local PDF: pdf/2026-09-12_03_Enabling Knowledge Graph Understanding at Scale with the EXplore Your Graphs ENgine (EXYGEN).pdf

We present EXYGEN (EXplore Your Graphs ENgine), a framework for knowledge graph (KG) understanding that enables conversational access to KGs at scale. We address two questions in sequence. First, how effectively can LLMs perform text-to-SPARQL generation given only automatically derived structured metadata and small graph samples, rather than task-specific fine-tuning? We integrate VoID descriptions and ShEx schemas into a retrieval-augmented generation (RAG) pipeline and ablate KG-derived context on the SciQA benchmark. Our best configuration -- combining ShEx schemas, retrieved triples, and example question-query pairs -- reaches an exact match of 0.419 on execution results without any LLM fine-tuning. We further find that lexical metrics such as F1 poorly predict query correctness, and that larger general-purpose LLMs can outperform smaller code-specialized ones once given sufficient context. Second, we ask how to generate the structured metadata that this method relies on from very large KGs, where KG metadata generation becomes computationally intractable. We introduce a predicate-coverage-aware parallel graph sampling strategy that preserves structural diversity while remaining computationally tractable. On OpenCitations Meta and GESIS, it retains high predicate coverage with minimal triple loss and reduces runtime by over 80x; on ORKG, sampling is not just faster but the only tractable path to obtain complete metadata. Together, these results show that structured schema context and lightweight prompting can substantially reduce reliance on fine-tuning for scalable conversational access to KGs, though closing the remaining gap to fully fine-tuned approaches will likely require reducing dependence on curated question-query exemplars -- whether through synthetic generation or an execution-feedback-driven approach -- and validating these findings beyond a single benchmark.

## 4. CausalArena: Benchmarking Causal Discovery in the Foundation Model Era

- Authors: Zi-Rong Li, Si-Yang Liu, Tian-Zuo Wang, Han-Jia Ye
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-10
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.284599454770214
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.11897v1
- PDF: https://arxiv.org/pdf/2609.11897v1
- Local PDF: pdf/2026-09-12_04_CausalArena_ Benchmarking Causal Discovery in the Foundation Model Era.pdf

Causal discovery aims to uncover causal structures from data and is fundamental to scientific reasoning and intervention-based decision making. Its evaluation relies heavily on structural causal models (SCMs), which specify a causal graph together with the mechanisms that generate data, yet existing studies differ substantially in graph families, mechanisms, and evaluation protocols. The emergence of causal discovery foundation models (CDFMs) further complicates evaluation: performance may reflect not only causal discovery ability, but also overlap between pretraining environments and test SCMs, making results on fixed synthetic benchmarks difficult to interpret. We introduce CausalArena, a unified and evolvable benchmark for causal discovery under a common protocol. Synthetic SCMs supply controlled breadth over structures and mechanisms; semantic operational SCMs provide human-auditable, semantically grounded environments beyond standard synthetic generators; and formula-grounded SCMs test discovery under explicit scientific mechanisms. Public real-world datasets provide an additional external-validity check. Experiments across classical, neural, and pretrained methods reveal substantial ranking shifts across SCM families and protocols, showing that strong performance in one benchmark regime does not reliably transfer to others. These results highlight benchmark diversity and pretraining--evaluation overlap as central challenges for evaluating causal discovery in the foundation model era.

## 5. Exploring Diffusion Transformers for Cross-Modal Augmentation in Multimodal Brain State Decoding

- Authors: Ziwei Wang, Xingyi He, Hongbin Wang, Tianwang Jia, Bohan Fang, Dongrui Wu
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-10
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 3.0814385714554824
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.11341v1
- PDF: https://arxiv.org/pdf/2609.11341v1
- Local PDF: pdf/2026-09-12_05_Exploring Diffusion Transformers for Cross-Modal Augmentation in Multimodal Brain State Decoding.pdf

Multimodal brain state decoding has largely focused on fusing paired modalities for prediction, but has rarely explored how their correspondence can be further exploited to enrich training data and improve multimodal representation learning. To address this gap, we propose CoMA-DiT, a bidirectional cross-modal Diffusion Transformer for latent augmentation that treats paired modalities as sources of mutual generative supervision rather than merely as inputs to be fused. CoMA-DiT conditions velocity prediction on the paired modality through cross-modal attention and adaptively injects the resulting variation via a reliability-gated residual mechanism. Experiments on multimodal auditory attention decoding and emotion recognition showed that CoMA-DiT consistently outperformed 20 representative baselines, achieving absolute gains of 4.28% and 6.70% in accuracy and macro-F1 over the no-augmentation baseline, respectively. Extensive ablation, sensitivity, visualization, and interpretability analyses further demonstrated its robustness, generalizability, and ability to capture functionally relevant cross-modal interactions. These findings support a broader view of multimodal learning: Paired modalities can serve not only as inputs for fusion but also as supervision sources that augment one another.

## 6. scDEFT: A deep learning framework for drug-effect prediction and counterfactual reasoning

- Authors: Murthy Devarakonda
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-09
- DOI: Unavailable
- Categories: q-bio.QM, cs.LG
- Relevance: 2.9774405953291527
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.10831v1
- PDF: https://arxiv.org/pdf/2609.10831v1
- Local PDF: pdf/2026-09-12_06_scDEFT_ A deep learning framework for drug-effect prediction and counterfactual reasoning.pdf

Longitudinal single cell atlases now capture matched pre treatment and post treatment states from responders and non responders, presenting an opportunity to mechanistically explain why two patients on the same drug diverge. We introduce scDEFT (single cell Drug EFfect Transducer), which treats a drug as a conditioning operator on cell representations, enabling prediction and explanation. In scDEFT, feature wise linear modulation produces drug conditioned cell latents, learned under abundant per cell supervision and then frozen. Two independent heads aggregate those latents over shared transcriptional neighborhoods to predict drug induced state change and responder status. A backward stage ranks the latent dimensions by how strongly they separate responders from non responders and maps them to genes under a cell composition control. On a harmonized inflammatory bowel disease atlas of 1.16 million cells, three cohorts and two drug classes, scDEFT predicts state change at 45% of the baseline to reproducibility ceiling headroom and stratifies responders before treatment at AUROC 0.70, where standard predictors remain at chance. These predictions and the drivers behind them support target and co target nomination, patient stratification, and counterfactual prediction of unseen drug cohort effects.

## 7. The information geometry of large language models is shared, learned, and controllable

- Authors: Dario Picozzi
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-10
- DOI: Unavailable
- Categories: cs.LG, cs.CL
- Relevance: 2.964961241338134
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.11063v1
- PDF: https://arxiv.org/pdf/2609.11063v1
- Local PDF: pdf/2026-09-12_07_The information geometry of large language models is shared, learned, and controllable.pdf

Large language models learn similar behaviours, yet it remains unclear what structure they share or how to change one behaviour without disturbing others. The Fisher-Rao geometry of next-token probabilities connects these questions: behaviour determines this geometry up to output-preserving symmetries, whereas activation geometry depends on coordinates. Across transformer, state-space and recurrent models, output geometries agree more strongly than activation geometries, and shared geometry supports semantic-category transfer. Agreement with human word choices increases with predictive accuracy, scale and training, and improves further after model-only calibration. Token probabilities and read-out geometry jointly predict the spectrum and its effective dimension. Controlled language assignments show that geometry follows the language law across architectures. Pretraining corpus statistics predict held-out fact acquisition without recalibration, while randomised experiments show that deeper evidence substantially delays acquisition across every tested architecture and evidence construction. Finally, the geometry prescribes minimum-disturbance local interventions, predicts their relative cost, and supports reusable control: updates learned on donor prompts transfer to unseen prompts while better preserving behaviour on reference prompts than Euclidean control. The same geometric correction improves steering, editing, attribution, dictionary learning and fine-tuning.

## 8. Multimodal Taxonomic Conditioning for Generative Plankton Imagery

- Authors: Daniela Ivanova, Ozgu Goksu, Nicolas Pugeault
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-10
- DOI: Unavailable
- Categories: cs.CV, cs.LG
- Relevance: 2.956595091272391
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.11673v1
- PDF: https://arxiv.org/pdf/2609.11673v1
- Local PDF: pdf/2026-09-12_08_Multimodal Taxonomic Conditioning for Generative Plankton Imagery.pdf

Automated plankton imaging produces severely long-tailed datasets, where the rare taxa of greatest ecological interest have too few images to train or evaluate classifiers reliably. We generate synthetic plankton imagery conditioned on taxonomy: a CLIP encoder is adapted on a large plankton corpus with a ranked contrastive objective extended to deep, ragged taxonomies, then frozen to condition a parameter-efficient diffusion transformer. We evaluate synthetic sample quality on distributional fidelity and downstream classifier utility.

## 9. From Document Silos to Process Intelligence: A Multi-Layer Knowledge Graph for CMC Process Development

- Authors: Reza Amirmoshiri, Faryad Sahneh, Yasser Jangjou
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-10
- DOI: Unavailable
- Categories: cs.AI, cs.MA
- Relevance: 2.9411181647856033
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.11493v1
- PDF: https://arxiv.org/pdf/2609.11493v1
- Local PDF: pdf/2026-09-12_09_From Document Silos to Process Intelligence_ A Multi-Layer Knowledge Graph for CMC Process Development.pdf

Chemistry, Manufacturing and Controls (CMC) process development generates an enormous body of technical information across a multi-stage, knowledge-intensive continuum from drug discovery to commercial manufacturing. This knowledge is traditionally fragmented across functions and heterogeneous formats, causing traceability gaps and significant knowledge-management costs during technology transfer and regulatory filing. We present a modular agentic-AI platform that converts a heterogeneous corpus of process-development documents into a queryable, dual-layer knowledge graph. A base knowledge layer builds a lexical graph with a Document-Section-Chunk hierarchy through lossless ingestion of digital, scanned, handwritten, and multilingual documents, while an intelligence layer extracts ontology-aligned entities and bridges cross-document concepts through a provenance-anchored domain graph. LLM agents operate across both layers, selecting the retrieval path best suited to each question. We evaluate the lexical layer with a novel three-tier protocol measuring the deployment-fidelity of a retrieval-augmented generation (RAG) system on proprietary data, demonstrated on 505 questions curated from 38 development reports of a Sanofi small-molecule program. Tier-1 multiple-choice accuracy of 95% signals strong platform reliability; the stricter Tier-2 LLM-judge pass rate of 85%, which degrades on comparative and corpus-wide questions, reveals a failure taxonomy that Tier-1 accuracy alone fails to capture. A router agent selects between layers according to question type. We anticipate this protocol will enable future designers of agentic platforms to assess their systems against nonpublic databases, and that graph-based architectures will see broader adoption in pharma as a means of transforming fragmented document repositories into structured process intelligence.

## 10. SWRouter: Similarity-Contractive Window Routing for Multi-Turn Large Language Model Conversations

- Authors: Yu Wang, Yuchen Li, Rui Kong, Xinran Chen, Jiamin Chen, Hengyi Cai, Shuaiqiang Wang, Jiashu Zhao, Yulun Zhang, Zhonghao Lyu, Haoyi Xiong, Linghe Kong, Jimmy Xiangji Huang, Dawei Yin
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-10
- DOI: Unavailable
- Categories: cs.CL, cs.AI, cs.IR
- Relevance: 2.906804985918491
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.11414v1
- PDF: https://arxiv.org/pdf/2609.11414v1
- Local PDF: pdf/2026-09-12_10_SWRouter_ Similarity-Contractive Window Routing for Multi-Turn Large Language Model Conversations.pdf

Large language models exhibit complementary strengths, motivating routing methods that dispatch each query to the most suitable model. Although existing routers are effective in single-turn settings, they do not directly transfer to multi-turn dialogue, where routing performance critically depends on how historical context is segmented, retained, and incorporated into the current prompt. This introduces two fundamental challenges: preventing information loss and information confusion during context construction, and evaluating routing quality without conflating model selection with prompt construction quality. In this paper, we propose SWRouter, a Similarity-Contractive Window Router for multi-turn large language model routing. SWRouter combines a similarity-based context segmentation mechanism for prompt construction with a dual-metric evaluation framework that decouples construction accuracy from router performance. Experiments on multi-turn dialogue benchmarks demonstrate that SWRouter consistently surpasses strong baselines, achieving a 16.26% improvement in evaluation accuracy over the best individual large language model and an additional 8.22% gain over the Conv-ID Context baseline. Our results highlight that multi-turn large language model routing requires a joint design of context construction and evaluation, rather than a direct extension of single-turn routing methods.

## 11. MindTopo: Can Foundation Models Reason in Topological Space?

- Authors: Yunfei Ge, Anbang Liu, Qineng Wang, Johnalbert Garnica, Jianwen Lyu, Zihan Wang, Reuben Tan, Jianfeng Gao, Ruohan Zhang, Yining Hong, Jiajun Wu, Manling Li
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-10
- DOI: Unavailable
- Categories: cs.AI, cs.CL, cs.CV
- Relevance: 2.8652958954265397
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.11900v1
- PDF: https://arxiv.org/pdf/2609.11900v1
- Local PDF: pdf/2026-09-12_11_MindTopo_ Can Foundation Models Reason in Topological Space.pdf

Spatial reasoning depends not only on metric properties such as distance, angle, and shape, but also on topological relations that remain invariant under continuous deformation. Cognitive science identifies these relations as foundational to spatial understanding, yet foundation-model evaluations largely focus on metric or viewpoint-dependent relations. We introduce MindTopo, a benchmark of topological intuition across five properties grounded in cognitive science and formal topology: continuity, separation, order, enclosure, and knots. MindTopo evaluates each property at two cognitive levels. Reasoning asks a model to identify topological relations or infer how they change. Planning instantiates a foundation model as a closed-loop agent whose policy selects environment actions. MindTopo contains 11,030 instances across 13 procedurally generated task types with controllable difficulty. We benchmark 14 MLLMs and study agent configurations augmented with image and video generation, including 3 video generative models in planning settings. Every MLLM performs better on reasoning than on planning, and the best-performing model remains far below observed human performance. On Qwen3-VL-2B-Instruct, supervised fine-tuning and reinforcement learning improve reasoning more than planning. Generated observations retain local cues and reach plausible endpoints, but audited rollouts do not reliably follow environment dynamics or preserve topology across transitions. Our website is at https://mind-topo.github.io/

## 12. From Queries to Narratives: Cultural Heritage Data Stories for Knowledge Graph Exploration and Quality Assessment

- Authors: Tabea Tietz, Torsten Schrade, Etienne Posthumus, Linnaea Söhn, Jonatan Jalle Steller, Jörg Waitelonis, Harald Sack
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-10
- DOI: Unavailable
- Categories: cs.AI, cs.DL
- Relevance: 2.8559624733275046
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.11403v1
- PDF: https://arxiv.org/pdf/2609.11403v1
- Local PDF: pdf/2026-09-12_12_From Queries to Narratives_ Cultural Heritage Data Stories for Knowledge Graph Exploration and Quality Assessment.pdf

Cultural-heritage KGs such as the NFDI4Culture-KG contain millions of triples about artworks, music, inscriptions, historical events, and the people and places connected to them. For many users, however, discovering this knowledge can be difficult. While SPARQL can be learned, writing meaningful queries first requires an in-depth understanding of the graph's data model, an investment many domain researchers and practitioners are unwilling to make. Even with existing user interfaces, a starting point and some guidance are usually needed, because the data contained in the graph is highly specialized, heterogeneous, and constantly growing, making it challenging to know what it contains or which questions it can answer. In this paper, we present data stories as a way not only to lower this barrier, but also to turn exploration into data-quality assessment, and thus combine accessible querying with the discovery of issues that remain hidden in aggregate statistics. In this contribution, a data story is understood as a narrative document that integrates explanatory text and images with executable SPARQL queries and their visualized results. It is described how they are authored against the graph and how they serve several purposes: guiding users through an unfamiliar graph, creating reproducible narratives, and surfacing data-quality issues previously hidden in aggregate statistics. The authoring platform LODEON including its Sparnatural and AI-supported authoring assistants is introduced as a proof-of-concept. Within the authoring environment, every claim made about the data can be backed by an explicit query, making these narratives transparent and reproducible. This paper also reflects on lessons learned from hands-on seminars and workshops. Early experience suggests that such data stories make cultural-heritage knowledge graphs more accessible for both exploration and quality assessment.

## 13. A Dynamic Fusion Large Language Model for Traffic Flow Prediction

- Authors: Xue Qiu, Jianli Xiao
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-10
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 2.85277053994629
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.11314v1
- PDF: https://arxiv.org/pdf/2609.11314v1
- Local PDF: pdf/2026-09-12_13_A Dynamic Fusion Large Language Model for Traffic Flow Prediction.pdf

Traffic flow prediction is a core supporting technology for intelligent transportation systems. It uses historical data to infer future traffic dynamics in specific areas, thereby helping to alleviate congestion and improve resource allocation efficiency. Traditional neural networks struggle to break through accuracy limits due to their reliance on singular feature modeling, while large language models (LLMs) suffer from insufficient capture of spatial topological information and mining spatiotemporal correlation. This study proposes a Dynamic Fusion Large Language Model (DF-LLM) for traffic flow prediction. The model incorporates three core components: spatiotemporal embedding module, spatiotemporal fusion module, and LLM backbone. The spatiotemporal embedding module enables synergistic representation of multi-scale spatiotemporal features. The spatiotemporal fusion module integrates spatial topology and dynamic dependencies via graph convolution. The LLM backbone adopts a differentiated parameter adaptation strategy to balance training efficiency and traffic data adaptability. Additionally, it introduces a context aggregation attention module to strengthens global dependencies. More importantly, the LLM backbone takes the residual connections to mitigate the gradient vanishing in deep networks. Experiments show that DF-LLM has achieved better performance by comparing the metrics on all the four datasets.

## 14. LILA: Calibration-Free Structured Pruning of Large Language Models via Latent Spectral Geometry

- Authors: Sankar Behera, Dhruv Singh, Anshika Agnihotri, Raj Kumar Choudhary, Satyadev Ahlawat, Yamuna Prasad
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-10
- DOI: Unavailable
- Categories: cs.LG, cs.CL
- Relevance: 2.836460430613075
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.11163v1
- PDF: https://arxiv.org/pdf/2609.11163v1
- Local PDF: pdf/2026-09-12_14_LILA_ Calibration-Free Structured Pruning of Large Language Models via Latent Spectral Geometry.pdf

Structured pruning of large language models (LLMs) offers hardware-efficient compression, yet existing methods require calibration data, gradient computation, or large auxiliary policy networks at pruning time. LILA (\emph{Latent-Informed Layer Analysis}) scores neuron importance via the Kolmogorov--Smirnov (KS) distance between empirical singular value distributions of the full and neuron-ablated feed-forward network (FFN) weight matrix, providing a closed-form spectral rule requiring no training, calibration data, or auxiliary network. Without any fine-tuning, LILA surpasses PruneNet (45M-parameter RL policy) by 1.57~pp in zero-shot accuracy on LLaMA-2-7B at 25\% sparsity, and outperforms WikiText-2-calibrated SliceGPT by up to 6.0~pp across all sparsity levels, while preserving the original architecture. After one epoch of LoRA recovery fine-tuning, LILA achieves highly competitive performance, matching the heavily calibrated SliceGPT baseline to within a 0.48~pp margin across LLaMA-2-7B and Phi-2, despite using zero calibration data. A Neural Tangent Kernel analysis confirms a 22$\times$ reduction in functional distortion versus random pruning, providing theoretical grounding for the spectral importance criterion. Finally, extending LILA to dynamically allocate sparsity budgets via KS-scores yields state-of-the-art generative preservation at moderate compression, while uncovering fundamental single-layer architectural bottlenecks at higher compression regimes.

## 15. Ecdysis: Efficient and Effective Training of Runtime Harnesses for LLM Agents

- Authors: Ruiqing Yue, Yu Cui, Zhuoyu Sun, Sicheng Pan, Xianhong Xue, Tingyu Li, Ting Li, Wenzhuo Zhu, Yi Chen, Yifei Liu, Baohan Huang, Zhe Cui, Haibin Zhang, Cong Zuo
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-10
- DOI: Unavailable
- Categories: cs.SE, cs.AI
- Relevance: 2.796368926199259
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.11677v1
- PDF: https://arxiv.org/pdf/2609.11677v1
- Local PDF: pdf/2026-09-12_15_Ecdysis_ Efficient and Effective Training of Runtime Harnesses for LLM Agents.pdf

Self-evolving runtime harnesses can substantially improve the capabilities of large language model (LLM) agents and provide a promising paradigm for optimizing agent execution. Existing harness evolution methods typically rely on iterative search, repeatedly evaluating and revising candidate harnesses based on execution feedback from task instances. While this paradigm enables continuous harness optimization, it incurs substantial time overhead due to repeated agent executions and code modifications, and may overfit to observed tasks and specific failure patterns, resulting in degraded generalization to unseen tasks. We identify the lack of principled failure diagnosis as a key bottleneck in harness evolution: an observed failure can reflect either model-specific deficiencies or systematic harness deficiencies, and directly optimizing against individual failures can lead to unnecessary model-specific accommodation. We therefore propose Ecdysis, an efficient and effective framework that distinguishes model-specific accommodation from harness-level repair and biases adaptation toward systematic harness deficiencies by identifying recurring cross-task failure patterns. Ecdysis adopts a batch-level cross-instance failure aggregation paradigm to jointly analyze failure evidence from multiple task instances and further introduces Failure-Driven Collaborative Refinement to diagnose failure causes and iteratively refine harness modification specifications. By combining cross-instance failure analysis with multi-role diagnosis, Ecdysis enables more effective harness evolution with lower training time. Experiments show that Ecdysis achieves up to a 1.84x speedup in harness training compared with existing harness evolution methods, while improving the reasoning accuracy of the resulting harnesses by 18.56%.

## 16. AcFlow: Controlling Text-to-Image Diffusion Transformers via Learned Conditional Activation Flow

- Authors: Junran Wang, Zehao Jin, Tianyu Luan, Xinjie Shen
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-09
- DOI: Unavailable
- Categories: cs.CV, cs.AI
- Relevance: 2.789154728051573
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.10723v1
- PDF: https://arxiv.org/pdf/2609.10723v1
- Local PDF: pdf/2026-09-12_16_AcFlow_ Controlling Text-to-Image Diffusion Transformers via Learned Conditional Activation Flow.pdf

Text-to-image diffusion transformers (DiTs) are powerful generators, yet direct prompting provides limited control interface for style intensity and can fail to suppress unwanted concepts. To enable these controls, we introduce AcFlow, an inference-time controller that transports intermediate layer image-token activations through a learned concept-conditioned velocity field while keeping the base DiT frozen. A textual concept description specifies the desired intervention, while the integration horizon provides a continuous control parameter. The field produces token-varying, activation-dependent updates. With parameters shared across concepts within each task family, the field supports fine-grained descriptions and generalizes to concepts unseen during training without per-concept fitting. On style control, AcFlow achieves the best style--content trade-off among the evaluated baselines in the high-style-alignment regime. At a fixed operating point, AcFlow attains style--content alignment of 0.5365/0.2860, compared with 0.4397/0.2684 for the baseline with the highest style alignment. Qualitative results demonstrate suppression of diverse concepts, including cases where direct prompting fails. Our analyses support the learned velocity field as an adaptive control mechanism, with update directions varying across tokens and depend on their activation states. Our code is available at https://github.com/Nove1yst/AcFlow.

## 17. REVA: Reusable Evidence View Aggregation for Context-Efficient RAG Serving

- Authors: Tuan Nguyen, Qiran Hu, Banruo Liu, Khoa D. Doan, Kok-Seng Wong, Fan Lai
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-10
- DOI: Unavailable
- Categories: cs.LG, cs.CL, cs.IR
- Relevance: 2.775287502005987
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.11209v1
- PDF: https://arxiv.org/pdf/2609.11209v1
- Local PDF: pdf/2026-09-12_17_REVA_ Reusable Evidence View Aggregation for Context-Efficient RAG Serving.pdf

Retrieval-augmented generation (RAG) improves knowledge-intensive large language model (LLM) applications by conditioning generation on retrieved documents, but longer contexts increase latency, key-value (KV) cache memory, and token cost. Post-retrieval compression can reduce this cost, yet existing compressors often operate independently for each query, rely on auxiliary models or rewriting, and introduce online overhead that can offset the benefit of shorter prompts. We revisit RAG compression from a data-mining perspective by aggregating historical query--document--model interactions into reusable evidence views. We first show that modern compressors have unstable gains over simple truncation and can add substantial inference-time latency. We then propose Reusable Evidence View Aggregation (REVA), a framework that mines the target generator's historical attention traces into a document-keyed, budget-agnostic score store. REVA maps token-level attention to readable word units, aggregates importance across repeated document accesses, and renders budget-specific plain-text views that preserve document order and the standard RAG interface. Across four representative benchmarks and modern LLMs, REVA improves generation quality by 1.0--5.8 points over existing advances, while reducing compression overhead by a factor of 5.3 to 15.6, adding less than 40 ms of latency.

## 18. When Synthetic Data Hurts: On Catastrophic Forgetting in Skill Retrieval for LLM Agents

- Authors: Syed Shariyar Murtaza, Yifan Nie, Utkarsh Soni, Eugene Wen, Arvid Frydenlund
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-09
- DOI: Unavailable
- Categories: cs.IR, cs.AI, cs.LG
- Relevance: 2.765536058886484
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.10750v1
- PDF: https://arxiv.org/pdf/2609.10750v1
- Local PDF: pdf/2026-09-12_18_When Synthetic Data Hurts_ On Catastrophic Forgetting in Skill Retrieval for LLM Agents.pdf

LLM agents increasingly rely on external skills retrieved at runtime, making skill selection from large repositories a critical challenge. We present a production skill router over 34,396 skills and a large-scale study of skill retrieval using limited real supervision and synthetic data. We found that the synthetic-data fine-tuning improves in-distribution retrieval but it causes catastrophic forgetting on real and out-of-distribution (OOD) data. We evaluate several forgetting mitigation fine-tuning approaches inspired by continual learning, including embedding-anchor regularization, Learning without Forgetting (LwF), Elastic Weight Consolidation (EWC), and L2-initialization. The results show that these approaches not only retain the performance on OOD skills retrieval but also improve the retrieval on synthetic in-distribution skills by 13.98\% for 0.6B Qwen retriever and reranker. Our results provide a practical benchmark and a robust fine-tuning recipe for scarce, multi-positive supervision.

## 19. Flow Duality and Source Geometry for Categorical Generation

- Authors: Etrit Haxholli
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-09
- DOI: Unavailable
- Categories: cs.LG, stat.ML
- Relevance: 2.7462352456526613
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.10863v1
- PDF: https://arxiv.org/pdf/2609.10863v1
- Local PDF: pdf/2026-09-12_19_Flow Duality and Source Geometry for Categorical Generation.pdf

Continuous and discrete flow matching are usually treated as separate constructions. This paper identifies a duality between them: projecting continuous convex-interpolant paths with one-hot targets through a position-wise argmax yields discrete convex-interpolant paths. The result requires source laws with appropriate coordinate symmetry and boundary regularity, and it makes the continuous source distribution an explicit design choice for categorical generation. We derive the induced discrete interpolation behavior for Gaussian, bounded-uniform, and centered negative-exponential sources, showing that different source geometries lead to qualitatively different transition timing and vocabulary-size dependence. Small visual diagnostics and a short language-modeling pilot suggest that these source-design effects can also appear in learned transports and early generative quality.

## 20. Model-Aware Schedules Improve Generation via Fiberwise Optimal Transport

- Authors: Luyi Jia, Boyan Zhang, Yilun Liu, Steffen Rulands
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-10
- DOI: Unavailable
- Categories: cs.LG, cs.AI
- Relevance: 2.721970915070044
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.11842v1
- PDF: https://arxiv.org/pdf/2609.11842v1
- Local PDF: pdf/2026-09-12_20_Model-Aware Schedules Improve Generation via Fiberwise Optimal Transport.pdf

Diffusion and flow-matching schedules control the signal and noise coefficients that mix data and noise along affine probability paths. Minimizing a kinetic action defined on coefficient paths, motivated by optimal transport, helps explain strong baselines but remains model-agnostic and ignores prediction error. Here we introduce a model-aware schedule construction based on fiberwise optimal transport. At a fixed time and state on the probability path, compatible signal/noise decompositions form an affine fiber. We define a fiberwise prediction risk by averaging optimal-transport costs between the true and predictor-induced decompositions within these fibers. On a fixed coefficient curve, combining this risk with coefficient-path kinetic action yields a closed-form optimal time allocation. This construction extends to general linear prediction targets, and the risk profile can be estimated from an early baseline checkpoint. We evaluate DDPMs and flow matching across prediction targets, training configurations, risk-estimation checkpoints, datasets, and architectures. Our model-aware schedules consistently outperform strong baselines, including a 38.6% relative FID reduction for flow matching on CIFAR-10 at 16 function evaluations. Each model-agnostic kinetic baseline determines its own kinetic reference coordinate. In these coordinates, fiberwise-risk profiles from independently trained models in different settings align closely after normalization to unit area. The resulting schedule deformations used in training also align, suggesting empirical universality across the evaluated models and settings. Pretrained-checkpoint diagnostics extend this normalized-risk agreement to larger conditional latent diffusion and 2-RF models. A frozen analytic allocation template retains most of the model-aware improvement without further risk estimation or model-specific fitting.

## 21. GEOSTEER: Geodesic Optimization for Activation Steering in Large Language Models

- Authors: Xuan Cuong Ngo, Hao Vo, Ngan Le
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-09
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 2.7197806344068898
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.10658v1
- PDF: https://arxiv.org/pdf/2609.10658v1
- Local PDF: pdf/2026-09-12_21_GEOSTEER_ Geodesic Optimization for Activation Steering in Large Language Models.pdf

Activation steering provides a lightweight way to control large language models (LLMs) by modifying their hidden activations at inference time. Among these approaches, norm-preserving steering aims to change model behavior without altering the activation norm, reducing the risk of representation collapse and degradation. However, existing norm-preserving methods are limited by predefined steering trajectories and by their reliance on one-step updates, which may fail to capture the complex structure of activation distributions. We propose GeoSteer, an optimization-based method for norm-preserving activation steering. GeoSteer formulates steering as a Riemannian optimization problem and updates activations through a sequence of small geodesic steps on the representation manifold. To avoid fixed steering directions, GeoSteer learns a nonlinear activation-space objective that distinguishes desired from undesired activations, and uses this function to adaptively guide each steering step. This multistep formulation yields smoother, more stable, and more consistent steering behavior while preserving the activation norm. Across TruthfulQA, RealToxicityPrompts, and UltraFeedback benchmarks, GeoSteer consistently improves over state-of-the-art activation steering baselines. These results suggest that norm-preserving steering can be made more effective by replacing predefined one-step edits with adaptive, geometry-aware optimization.

## 22. Structural Divergence Between the Moltbook AI‐Agent Network and Human Social Networks

- Authors: Wenpin Hou, Zhicheng Ji
- Source: openalex
- Venue type: journal
- Journal: Advanced Science
- Publication status: published
- Publication date: 2026-09-09
- DOI: https://doi.org/10.1002/advs.77665
- Categories: Complex Network Analysis Techniques, Opinion Dynamics and Social Influence, Language and cultural evolution
- Relevance: 2.7115569521562275
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://doi.org/10.1002/advs.77665
- PDF: Unavailable
- Local PDF: Not downloaded

Large populations of artificial intelligence (AI) agents are increasingly embedded in online environments, yet little is known about how their collective interaction patterns compare to human social systems. Here, we analyze the full interaction network of Moltbook, an agent-native platform in which AI agents interact through posts and comments, and systematically compare its structure to well-characterized human communication networks. Although Moltbook follows the same node-edge scaling relationship observed in human systems, indicating comparable global growth constraints, its internal organization diverges markedly. The network exhibits extreme attention inequality, heavy-tailed, and asymmetric degree distributions, suppressed reciprocity, and a global under-representation of connected triadic structures. Community analysis reveals a structured modular architecture with elevated modularity and comparatively lower community size inequality relative to degree-preserving null models. Together, these findings show that the Moltbook agent-platform system reproduces global structural regularities of human networks while exhibiting a distinct internal organization, highlighting that key features of social network structure can vary substantially across interaction environments.

## 23. From Tokens to Steps: Verification-Aware Speculative Decoding for Efficient Multi-Step Reasoning

- Authors: Kiran Purohit, Ramasuri Narayanam, Soumyabrata Pal
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.711293316163992
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.864/
- PDF: https://aclanthology.org/2026.findings-acl.864.pdf
- Local PDF: pdf/2026-09-12_23_From Tokens to Steps_ Verification-Aware Speculative Decoding for Efficient Multi-Step Reasoning.pdf

Speculative decoding (SD) accelerates large language model inference by allowing a lightweight draft model to propose outputs that a stronger target model verifies. However, its token-centric nature allows erroneous steps to propagate. Prior approaches mitigate this using external reward models, but incur additional latency, computational overhead, and limit generalizability. We propose SpecGuard, a verification-aware speculative decoding framework that performs step-level verification using only model-internal signals. At each step, SpecGuard samples multiple draft candidates and selects the most consistent step, which is then validated using an ensemble of two lightweight model-internal signals: (i) an attention-based grounding score that measures attribution to the input and previously accepted steps, and (ii) a log-probability-based score that captures token-level confidence. These signals jointly determine whether a step is accepted or recomputed using the target, allocating compute selectively. Experiments across a range of reasoning benchmarks show that SpecGuard improves accuracy by 3.6% while reducing latency by ~11%, outperforming both SD and reward-guided SD.

## 24. Do We Always Need Query-Level Workflows? Rethinking Agentic Workflow Generation for Multi-Agent Systems

- Authors: Zixu Wang, Bingbing Xu, Yige Yuan, Huawei Shen, Xueqi Cheng
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.709840069130642
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.254/
- PDF: https://aclanthology.org/2026.findings-acl.254.pdf
- Local PDF: pdf/2026-09-12_24_Do We Always Need Query-Level Workflows_ Rethinking Agentic Workflow Generation for Multi-Agent Systems.pdf

Multi-Agent Systems (MAS) built on large language models typically solve complex tasks by coordinating multiple agents through workflows. Existing approaches generates workflows either at task level or query level, but their relative costs and benefits remain unclear. After rethinking and empirical analyses, we show that query-level workflow generation is not always necessary, since a small set of top-K best task-level workflows together already covers equivalent or even more queries. We further find that exhaustive execution-based task-level evaluation is both extremely token-costly and frequently unreliable. Inspired by the idea of self-evolution and generative reward modeling, we propose a low-cost task-level generation framework SCALE , which means S elf prediction of the optimizer with few shot CAL ibration for E valuation instead of full validation execution. Extensive experiments demonstrate that SCALE maintains competitive performance, with an average degradation of just 0.61% compared to existing approach across multiple datasets, while cutting overall token usage by up to 83%.

## 25. Self-SoftCoT: A Self-Consistent Framework via Position-Aware Latent Space Reinforcement Learning

- Authors: Liangliang Dong, Lianlei Shan, Shuaimin Li
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.709553008319259
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1496/
- PDF: https://aclanthology.org/2026.acl-long.1496.pdf
- Local PDF: pdf/2026-09-12_25_Self-SoftCoT_ A Self-Consistent Framework via Position-Aware Latent Space Reinforcement Learning.pdf

While Chain-of-Thought (CoT) reasoning empowers Large Language Models (LLMs) to tackle complex tasks, its reliance on discrete token decoding imposes an inherent Discreteness Bottleneck, limiting expressiveness within a restricted vocabulary space. Existing continuous reasoning approaches, such as SoftCoT, mitigate this but typically rely on external auxiliary models, resulting in complex deployment and fractured inference pipelines. To address these challenges, we propose Self-SoftCoT, a self-contained framework that enables a frozen LLM to internally generate and consume latent thoughts without external assistants. By establishing a single-stream “Thinking → Speaking” closed-loop, we decouple latent planning from explicit generation. Furthermore, we adopt Group Sequence Policy Optimization (GSPO) to stabilize learning and employ Position-Aware Independent Projection to mitigate representation homogenization. Experimental results on five reasoning benchmarks demonstrate that our method significantly improves the reasoning performance of frozen LLMs. Specifically, our Qwen2.5-based model uses only N=2 soft tokens to outperform the SoftCoT baseline (N=4), improving the average accuracy from 75.06% to 78.42%. Similarly, LLaMA-3.1 performance increases from 70.52% to 74.55%.

## 26. PILOT: Planning via Internalized Latent Optimization Trajectories for Large Language Models

- Authors: Haoyu Zheng, Yun Zhu, Yuqian Yuan, Bo Yuan, Wenqiao Zhang, Siliang Tang, Jun Xiao
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.709200807560685
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.236/
- PDF: https://aclanthology.org/2026.acl-long.236.pdf
- Local PDF: pdf/2026-09-12_26_PILOT_ Planning via Internalized Latent Optimization Trajectories for Large Language Models.pdf

Strategic planning is critical for multi-step reasoning, yet compact Language Language Models (LLMs) often lack the capacity to formulate global strategies, leading to error propagation in long-horizon tasks. Our analysis reveals that LLMs possess latent reasoning capabilities that can be unlocked when conditioned on explicit plans from a teacher model; however, runtime reliance on external guidance is often impractical due to latency and availability constraints. To bridge this gap, we propose PILOT ( P lanning via I nternalized L atent O ptimization T rajectories), a non-invasive framework designed to internalize the strategic oversight of large models into intrinsic Latent Guidance . Instead of altering backbone weights, PILOT employs a lightweight Hyper-Network to synthesize a query-conditioned Latent Guidance . This vector acts as an internal steering mechanism, guiding the model’s representations toward optimal reasoning paths. Extensive experiments on mathematical and coding benchmarks demonstrate that PILOT effectively stabilizes reasoning trajectories, consistently outperforming strong baselines (e.g., +8.9% on MATH500) with negligible inference latency. Our code is available at: https://anonymous.4open.science/r/PILOT-B266

## 27. Task Assignment meets Annotator Modeling: Human-LLM Collaborative Annotation with Constraints

- Authors: Kei Moriyama, Kouta Nakayama, Yukino Baba
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.7090534931637684
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-srw.79/
- PDF: https://aclanthology.org/2026.acl-srw.79.pdf
- Local PDF: pdf/2026-09-12_27_Task Assignment meets Annotator Modeling_ Human-LLM Collaborative Annotation with Constraints.pdf

Crowdsourced annotators and Large Language Models (LLMs) offer complementary, cost-effective ways to obtain labeled data, yet ensuring high label quality remains challenging.We observe that task features influence the accuracy of humans and LLMs, while real-world constraints, such as per-annotator assignment limits, further complicate allocation.Prior work typically addresses either task features or constraints, but not both.We present an integrated framework that (i) estimates per-task accuracy from task features using a learning from crowds model and (ii) incorporates these estimations into a linear programming formulation that assigns tasks under practical constraints. Experimental results demonstrate that the proposed method achieves accuracy comparable to that of baseline methods while satisfying given constraints.

## 28. PRA-RAG: Provably Robust Aggregation in Retrieval-Augmented Generation against Retrieval Corruption

- Authors: Xue Tan, Yi Zheng, Chang Huo, Yunruo Zhang, Yu Liu, Hao Luan, Zhuyang Yu, Jun Dai, Xiaoyan Sun, Ping Chen
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.708662194453504
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1794/
- PDF: https://aclanthology.org/2026.findings-acl.1794.pdf
- Local PDF: pdf/2026-09-12_28_PRA-RAG_ Provably Robust Aggregation in Retrieval-Augmented Generation against Retrieval Corruption.pdf

Retrieval-Augmented Generation (RAG) enhances Large Language Models (LLMs) by incorporating external knowledge, effectively mitigating their inherent knowledge limitations. However, RAG remains vulnerable to poisoning attacks that manipulate retrieved texts to mislead model outputs. Existing defense mechanisms often lack theoretical robustness guarantees and perform unreliably when the LLM has limited knowledge of the retrieved content. In this work, we propose PRA-RAG, a provably robust retrieval aggregation algorithm designed to defend against poisoning attacks on retrieved texts. PRA-RAG samples multiple combinations of retrieved texts and utilizes geometric structures in the embedding space to identify a robust subset, from which a stable aggregated representation is derived. We provide theoretical bounds on the maximum impact of poisoned retrieved content and establish a quantitative measure of RAG’s robustness. Experiments across multiple benchmarks and RAG architectures demonstrate that PRA-RAG reduces the attack success rate to as low as 1% while maintaining an accuracy of 71%, significantly outperforming representative state-of-the-art (SOTA) methods.

## 29. MAESTRO: Meta-learning Adaptive Estimation of Scalarization Trade-offs for Reward Optimization

- Authors: Yang Zhao, Hepeng Wang, Xiao Ding, Yangou Ouyang, Bibo Cai, Kai Xiong, Jinglong Gao, Zhouhao Sun, Li Du, Bing Qin, Ting Liu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.7081367223695634
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1019/
- PDF: https://aclanthology.org/2026.acl-long.1019.pdf
- Local PDF: pdf/2026-09-12_29_MAESTRO_ Meta-learning Adaptive Estimation of Scalarization Trade-offs for Reward Optimization.pdf

Group-Relative Policy Optimization (GRPO) has emerged as an efficient paradigm for aligning Large Language Models (LLMs), yet its efficacy is primarily confined to domains with verifiable ground truths. Extending GRPO to open-domain settings remains a critical challenge, as unconstrained generation entails multi-faceted and often conflicting objectives—such as creativity versus factuality—where rigid, static reward scalarization is inherently suboptimal. To address this, we propose MAESTRO ( M eta-learning A daptive E stimation of S calarization T rade-offs for R eward O ptimization), which introduces a meta-cognitive orchestration layer that treats reward scalarization as a dynamic latent policy, leveraging the model’s terminal hidden states as a semantic bottleneck to perceive task-specific priorities. We formulate this as a contextual bandit problem within a bi-level optimization framework, where a lightweight Conductor network co-evolves with the policy by utilizing group-relative advantages as a meta-reward signal. Across seven benchmarks, MAESTRO consistently outperforms single-reward and static multi-objective baselines, while preserving the efficiency advantages of GRPO, and in some settings even reducing redundant generation.

## 30. Towards Scalable Lightweight GUI Agents via Multi-role Orchestration

- Authors: Ziwei Wang, Junjie Zheng, Leyang Yang, Sheng Zhou, Xiaoxuan Tang, Fang Zhouhua, Zhiwei Liu, Dajun Chen, Yong Li, Jiajun Bu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.707484987951018
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1122/
- PDF: https://aclanthology.org/2026.findings-acl.1122.pdf
- Local PDF: pdf/2026-09-12_30_Towards Scalable Lightweight GUI Agents via Multi-role Orchestration.pdf

Autonomous Graphical User Interface (GUI) agents powered by Multimodal Large Language Models (MLLMs) enable digital automation on end-user devices. While scaling both parameters and data has yielded substantial gains, advanced methods still suffer from prohibitive deployment costs on resource-constrained devices. When facing complex in-the-wild scenarios, lightweight GUI agents are bottlenecked by limited capacity and poor task scalability under end-to-end episodic learning, impeding multi-agent systems (MAS) adaptation, while training multiple skill-specific experts remains costly. Can we strike an effective trade-off in this cost–scalability dilemma, enabling lightweight MLLMs to participate in realistic GUI workflows? To address these challenges, we propose LAMO framework, which endows a lightweight MLLM with GUI-specific knowledge and task scalability, allowing multi-role orchestration to expand their capability boundary for GUI automation. LAMO combines role-oriented data synthesis with a two-stage training recipe: (i) supervised fine-tuning with Perplexity-Weighted Cross-Entropy optimization for knowledge distillation and visual perception enhancement, and (ii) reinforcement learning for role-oriented cooperative exploration. Via LAMO, we develop a task-scalable native GUI agent LAMO-3B supporting monolithic execution and MAS-style orchestration. When paired with advanced planners, as a plug-and-play policy executor, LAMO-3B can continuously benefit from planner advances, enabling a higher performance ceiling. Extensive static and online evaluations validate the effectiveness of our designs.
