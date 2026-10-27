# Paper Daily Reading - 2026-10-27

## 1. WL-SeqVAE: Sequence-Based Graph Generation Using Variational Autoencoders and Weisfeiler-Leman Colors

- Authors: Iakovos Evdaimon, Giannis Nikolentzos, Achilleas Tsimichodimos, Christos Xypolopoulos, Michalis Vazirgiannis
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-23
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.4780834215511103
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.32650v1
- PDF: https://arxiv.org/pdf/2610.32650v1
- Local PDF: pdf/2026-10-27_01_WL-SeqVAE_ Sequence-Based Graph Generation Using Variational Autoencoders and Weisfeiler-Leman Colors.pdf

In this paper, we introduce WL-SeqVAE, a sequence-based variational autoencoder for generating graphs. The key observation behind WL-SeqVAE is that node colors induced by the Weisfeiler-Leman (WL) algorithm provide compact discrete summaries of local graph structure and can therefore serve as structural tokens for generation. Rather than learning a distribution over adjacency matrices directly, our method maps each graph to a sequence of WL colors and employs a variational autoencoder that encodes this sequence into a Gaussian latent distribution, from which an autoregressive decoder reconstructs the graph. During generation, compatibility constraints derived from the WL colors guide node and edge predictions, combining global information from the latent representation with local structural consistency. This formulation turns graph generation into a sequence generation problem and avoids directly parameterizing a quadratic adjacency matrix. We evaluate WL-SeqVAE on molecular and general graph generation tasks. Across the evaluated datasets, WL-SeqVAE is competitive with established baselines on several local structural and molecular quality metrics. Code is available at https://github.com/iakovosevdaimon/WL-SeqVAE

## 2. Representation Learning via Composite Subspace Flow Matching

- Authors: José Afonso, Mário Figueiredo
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-23
- DOI: Unavailable
- Categories: cs.CV, cs.AI
- Relevance: 3.384802860626829
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.32256v1
- PDF: https://arxiv.org/pdf/2610.32256v1
- Local PDF: pdf/2026-10-27_02_Representation Learning via Composite Subspace Flow Matching.pdf

Distilling semantic meaning from raw image data remains a challenge in machine learning. Current self-supervised paradigms face a trade-off: joint-embedding architectures produce relevant features by aggressively discarding intra-class variance, irreversibly spatial and reconstruction. Conversely, generative models preserve spatial details but struggle to isolate semantics, as their optimization is dominated by pixel variations. To bridge this divide, we propose composite subspace flow matching (CSFM). Rather than corrupting data with unstructured isotropic noise, CSFM formulates representation learning as the variance-minimizing inversion of a deterministic degradation curriculum across spectral, color, and illumination subspaces. By bounding trajectory variance with hard temporal style truncation, a capacity-constrained encoder is driven to ignore transient style artifacts and encode persistent content. Empirical evaluations across CIFAR-10, CIFAR-100, and STL-10 show that CSFM yields competitive discriminative transferability while preserving generative synthesis across both convolutional and vision transformer architectures. By avoiding the collapse pathologies of non-generative methods, CSFM forms a smooth latent space that outperforms standard optimal transport flows on linear probing and few-shot classification, while enabling coherent synthesis and trajectory interpolation. These results confirm that steering the physical dynamics of generative flows offers a scalable paradigm for learning representations that are simultaneously linearly separable and generatively invertible.

## 3. ReLEAP: Upcycling Vision Datasets through Cross-Task Unification and Semi-Supervised Annotation

- Authors: Julia Simon, Daniel Steininger, Andreas Trondl
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-23
- DOI: Unavailable
- Categories: cs.CV, cs.LG
- Relevance: 3.2753418711291307
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.32289v1
- PDF: https://arxiv.org/pdf/2610.32289v1
- Local PDF: pdf/2026-10-27_03_ReLEAP_ Upcycling Vision Datasets through Cross-Task Unification and Semi-Supervised Annotation.pdf

Developing robust vision models requires large amounts of annotated data, especially for tasks involving fine-grained class distinctions under variable environmental conditions. Even in domains with numerous existing datasets, differences in annotation formats, label definitions and targeted learning tasks hinder data reuse and integration. To address this challenge, we introduce ReLEAP, a scalable Python framework for unifying heterogeneous image datasets through data-source abstraction, systematic reuse of annotations across learning tasks, and mapping of labels to a shared hierarchical taxonomy. We demonstrate its applicability in precision agriculture by integrating fifteen diverse datasets covering a broad range of plant species and annotation types. Beyond unification, ReLEAP enables systematic recycling of existing data and provides a robust foundation for learning-based annotation upcycling. Leveraging this foundation, we conduct extensive cross-dataset and fine-tuning experiments to investigate how domain-specific models trained on unified data and foundation models can be used to automatically generate higher-level annotations under unsupervised, weakly supervised and semi-supervised settings, and how dataset characteristics influence their effectiveness. Our results show that unified data access and annotation upcycling substantially expand the pool of reusable training data and annotations while improving data transparency, enabling more sustainable and resource-efficient use of existing datasets. We release the framework and trained models for academic use to support accessible and collaborative research, particularly in data-scarce and heterogeneous domains.

## 4. Ontology-Guided Knowledge Graph Construction from Structured Metadata and Climate Science Publications

- Authors: Aayush Acharya, Qi Zhang, Eduard Dragut, Longin Jan Latecki
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-23
- DOI: Unavailable
- Categories: cs.CL, cs.AI
- Relevance: 3.1451992235942927
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.32725v1
- PDF: https://arxiv.org/pdf/2610.32725v1
- Local PDF: pdf/2026-10-27_04_Ontology-Guided Knowledge Graph Construction from Structured Metadata and Climate Science Publications.pdf

The rapid expansion of scientific literature far outpaces the speed of manual curation, creating a fundamental bottleneck in extracting structured knowledge from scientific texts. To address this, we introduce an agentic, ontology-guided framework for knowledge graph (KG) construction. Our framework utilizes specialized agents for document understanding, information extraction, ontology conformance, and entity linking. First, an LLM extracts factual knowledge in the form of triples with explicit textual evidence from research papers. Then the triplets undergo a multistage verification process to ground the triplets in the ontology. By enforcing schema constraints and requiring evidence in the form of text fragments, we ensure the data is both semantically consistent and traceable. In an agreement study over 1,000 extracted triplets, Gemini-2.5-flash achieves Cohen's $κ$ scores of 0.640--0.700 against three human annotators, matching the human--human agreement range of 0.616--0.689. We applied this framework to 2,000 scientific publications and construct a novel, ontology-grounded KG for climate science with 133,990 nodes and 755,308 relations; of the 23,327 triplets that the publications contribute after validation, 98.96\% are judged correct. The pipeline code and KG is publicly available https://github.com/aayushacharya/climatekg.

## 5. ActionRAG: Evidence-Refining Graph Diffusion for Long-Term Memory in LLM Agents

- Authors: Navyansh Mahla, Sashank Vandrangi
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-23
- DOI: Unavailable
- Categories: cs.AI, cs.CL
- Relevance: 3.0949891364258555
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.32752v1
- PDF: https://arxiv.org/pdf/2610.32752v1
- Local PDF: pdf/2026-10-27_05_ActionRAG_ Evidence-Refining Graph Diffusion for Long-Term Memory in LLM Agents.pdf

LLM agents need long-term memory that can recover precise and mutually consistent evidence from growing interaction histories, particularly when answers depend on relations among facts rather than isolated semantic matches. Current memory pipelines remain vulnerable at two stages: indexing errors can fragment repeated entities or merge distinct ones, and online retrieval often treats initial similarity scores as final even when the surrounding graph provides evidence for revising them. We introduce ActionRAG, a graph memory architecture that couples cautious indexing with query-time graph retroevaluation. Its indexing pipeline reconciles type labels and applies tiered entity resolution. Given a query, dual-channel entity and triple retrieval forms an initial evidence set and induces a bounded local graph. Query-conditioned receiver-normalized diffusion refines triple scores using local path structure. Seed protection, hub-penalized flux, and triple materialization preserve direct evidence while recovering missed connections. We evaluate ActionRAG on MemoryAgentBench (MAB), which tests accurate retrieval, conflict resolution, long-range understanding, and test-time learning. Across its eight deterministic-scoring columns, ActionRAG achieves 55.1 average accuracy, improving over the strongest retrieval-based memory baseline by 5.4 points. Under MAB's query-time cost accounting, mean synthesis cost stays below \$0.001 per query on the four reported cost columns, and the sum of separately measured retrieval-side p99 components is 440.7 ms on our consumer Apple Silicon setup.

## 6. Emergence of diffusion models from associative memory through memorization and generalization

- Authors: Bao Pham, Gabriel Raya, Matteo Negri, Mohammed Javeed Zaki, Luca Ambrogioni, Dmitry Krotov
- Source: openalex
- Venue type: journal
- Journal: Nature Communications
- Publication status: published
- Publication date: 2026-10-25
- DOI: https://doi.org/10.1038/s41467-026-78727-y
- Categories: Neural Networks and Applications, Generative Adversarial Networks and Image Synthesis, Adversarial Robustness in Machine Learning
- Relevance: 3.076059475813775
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://doi.org/10.1038/s41467-026-78727-y
- PDF: https://www.nature.com/articles/s41467-026-78727-y_reference.pdf
- Local PDF: pdf/2026-10-27_06_Emergence of diffusion models from associative memory through memorization and generalization.pdf

Abstract Dense Associative Memories (DenseAMs) are generalizations of Hopfield networks that store training data at local minima of the energy landscape. When the amount of training data exceeds the critical memory storage capacity, new local minima (different from the training data) emerge. These emergent local minima, known as spurious states, can hinder memory retrieval. We examine diffusion models (DMs) through the DenseAM lens, viewing their generative process as an attempt of a memory retrieval. In the small data regime, DMs create distinct attractors for each training sample, akin to DenseAMs below the critical capacity. As the training set size increases, DMs transition to generalization. We identify a critical intermediate phase, predicted by DenseAM theory, characterized by the emergence of spurious states. In generative modeling, these previously overlooked states are no longer negative artifacts but rather are the first signs of generative capabilities. Their existence is demonstrated across a wide range of architectures and datasets.

## 7. Concept Acupuncturist: An Efficient and Precise Concept Erasure Method for Diffusion Models via Sparse Autoencoders

- Authors: Yiran Xiahou, Siliang Qin, Kai Chen, Shengzhi Zhang, Renyang Liu
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-23
- DOI: Unavailable
- Categories: cs.CV, cs.AI, cs.CR, cs.LG
- Relevance: 3.068500119398123
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.32059v1
- PDF: https://arxiv.org/pdf/2610.32059v1
- Local PDF: pdf/2026-10-27_07_Concept Acupuncturist_ An Efficient and Precise Concept Erasure Method for Diffusion Models via Sparse Autoencoders.pdf

Diffusion-based image generation models produce high-quality images but may generate harmful or policy-violating content, motivating machine unlearning (MU) to selectively remove target concepts while preserving general capabilities. However, existing MU approaches often struggle with the distributed and entangled nature of concept representations, leading to inefficient optimization and imprecise edits when applied through large-scale fine-tuning over full diffusion trajectories. To bridge this gap, we propose Concept Acupuncturist (ConceptACP), a novel MU framework that integrates interpretability-guided analysis with inference-free fine-tuning for efficient and precise concept removal. By establishing mappings between semantic concepts and cross-attention blocks in the U-Net denoiser and localizing the most concept-relevant block for targeted optimization, ConceptACP avoids full diffusion trajectory optimization, thereby improving fine-tuning efficiency. To mitigate concept entanglement, we propose a feature-level correction mechanism based on Sparse Autoencoders (SAEs), where SAE-derived sparse, semantically meaningful feature activations are manipulated to construct targeted correction signals, which are then projected back to the output space of the corresponding block and used as supervision for precise concept removal. Consequently, ConceptACP eliminates the need for external inference-time modules while achieving efficient and fine-grained unlearning. Instantiated on SDXL-Turbo, ConceptACP improves the forgetting success rate by 36.34 percentage points in the standard one-step generation setting on average over the best-performing baseline, while preserving image quality and prompt fidelity, and generalizes effectively across other Stable Diffusion backbones. Our code is available at https://github.com/Eran-Xia/ConceptACP.

## 8. PRISM: Promoting Sampling Diversity of Large Language Models with Implicit Stochastic Modulation

- Authors: Qixin Xu, Zihan Zhu, Xiaojiang Liu, Bohan Lyu
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-23
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.0416772480030496
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.32101v1
- PDF: https://arxiv.org/pdf/2610.32101v1
- Local PDF: pdf/2026-10-27_08_PRISM_ Promoting Sampling Diversity of Large Language Models with Implicit Stochastic Modulation.pdf

Large language models (LLMs) exhibit mode collapse, where their output distribution concentrates on familiar semantic modes. When diversity disappears, repeated sampling becomes semantic repetition rather than discovery, making rare but stronger solutions unlikely to surface and leaving self-evolution and continual learning difficult to sustain. Most remedies intervene only at inference time, shaping sam- ples without making diversity a model capability. We propose PRISM, a training-time framework that internalizes diversity within the model. PRISM combines (i) submodular curation that pairs each prompt with diverse-yet-correct multi-teacher solutions, and (ii) stochastic embedding modulation, which turns special-token perturbations into implicit signals for sampling distinct outputs. A theoretical analysis establishes the stability of this mechanism. On WritingPrompts and BookMIA, PRISM moves the quality-diversity frontier outward, achieving the best generation quality in all model-benchmark settings while maintaining the strongest or near-strongest semantic diversity across two open-weight model families. It also improves sampling efficiency on math and code benchmarks. Beyond inference, PRISM yields a stronger foundation for reinforcement learning, sustaining diverse rollouts and mitigating the diversity collapse commonly observed during RL training.

## 9. Beyond Post-Hoc Rewards: Privileged Reasoning Exploration for Multimodal Embeddings

- Authors: Tianyu Yang, Yijun Tian, Lars Benedikt Kaesberg, Jan Philip Wahle, Bela Gipp, Terry Ruas, Daniel Kurzawe
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-23
- DOI: Unavailable
- Categories: cs.AI, cs.CL
- Relevance: 2.9848958573770723
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.32474v1
- PDF: https://arxiv.org/pdf/2610.32474v1
- Local PDF: pdf/2026-10-27_09_Beyond Post-Hoc Rewards_ Privileged Reasoning Exploration for Multimodal Embeddings.pdf

Advances in Multimodal Large Language Models (MLLMs) have driven substantial progress in multimodal embeddings. Recent methods exploit generative capabilities by augmenting embedded inputs with self-generated reasoning to produce more informative embeddings. However, conventional retrieval supervision for training embedding models specifies pairwise relevance relations without explicitly guiding the reasoning used for input augmentation. Such reasoning is neither directly observed nor uniquely determined by the input, allowing multiple plausible traces to introduce semantic cues of varying retrieval utility. Existing approaches largely optimize reasoning conditioned on the input alone, limiting the exploration of retrieval-relevant traces. We introduce PILOT, a framework that models reasoning as a latent variable and instantiates its prior and posterior distributions as distinct reasoning modes of a shared MLLM. The prior conditions only on the input, whereas the posterior uses additional training-time relational evidence to guide reasoning exploration. To translate the posterior's broader exploration into inference-time improvements, we derive an importance-weighted variational objective and instantiate it as a prior-posterior co-evolution framework that improves both modes under a shared inference-compatible reward while selectively transferring posterior trajectories to the prior according to their utility and prior reachability. On the 78-task MMEB-V2 benchmark, PILOT outperforms the primary baseline across all 12 task groups at both 2B and 7B parameters, improving overall scores by 3.2 and 3.3 points, respectively, with the largest gains in visual-document retrieval (+6.1 and +6.4 points). Our results show that relational supervision is most valuable not as a post-hoc reward but as a signal for shaping how reasoning is explored in training reasoning-enhanced embedding models.

## 10. On the Identifiability of Hybrid Deep Generative Models: Meta-Learning as a Solution

- Authors: Yubo Ye, Maryam Toloubidokhti, Sumeet Vadhavkar, Xiajun Jiang, Huafeng Liu, Linwei Wang
- Source: arxiv
- Venue type: preprint
- Journal: Advances in Neural Information Processing Systems 37 (NeurIPS 2024), 7714-7735
- Publication status: preprint
- Publication date: 2026-10-23
- DOI: 10.52202/079017-0247
- Categories: cs.LG
- Relevance: 2.966243105944498
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.32748v1
- PDF: https://arxiv.org/pdf/2610.32748v1
- Local PDF: pdf/2026-10-27_10_On the Identifiability of Hybrid Deep Generative Models_ Meta-Learning as a Solution.pdf

The interest in leveraging physics-based inductive bias in deep learning has resulted in recent development of hybrid deep generative models (hybrid-DGMs) that integrate known physics-based mathematical expressions in neural generative models. To identify these hybrid-DGMs requires inferring parameters of the physics-based component along with their neural component. The identifiability of these hybrid-DGMs, however, has not yet been theoretically probed or established. How does the existing theory of the un-identifiability of general DGMs apply to hybrid-DGMs? What may be an effective approach to construct a hybrid-DGM with theoretically-proven identifiability? This paper provides the first theoretical probe into the identifiability of hybrid-DGMs, and presents meta-learning as a novel solution to construct identifiable hybrid-DGMs. On synthetic and real-data benchmarks, we provide strong empirical evidence for the un-identifiability of existing hybrid-DGMs using unconditional priors, and strong identifiability results of the presented meta-formulations of hybrid-DGMs. Code is available at https://github.com/GoForIt-YYB/Meta-Hybrid-VAE.

## 11. Every Weight Is a Path of Shared Discrete Decisions

- Authors: Ammar Ali, Stamatis Lefkimmiatis
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-22
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 2.9443945996531395
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.31931v1
- PDF: https://arxiv.org/pdf/2610.31931v1
- Local PDF: pdf/2026-10-27_11_Every Weight Is a Path of Shared Discrete Decisions.pdf

We introduce TWIG (Tree-structured Weights with Inherited Gates), a representation in which every weight of a neural network is the end of a path of small discrete decisions: a sign, a shift by a power of two, a zero gate, an index into a shared table. Weights that belong together share the upper part of their paths, and each decision is inherited by every weight below it, so it is stored once and applied once. This simple change has three consequences. Any trained network can be written as a TWIG, and when the decisions are powers of two its weight layers become circuits made almost entirely of wires and adders, suited to chips whose weights are fixed at fabrication. Pruning, quantization, low-rank factorization, codebooks and weight sharing become edits of one object, so a single optimizer can choose among all of them for a whole network. And choosing the decisions is the ground-state problem of a higher-order Boltzmann machine whose interactions follow the paths of the tree, the problem class that annealers and quantum optimizers are built to solve. Today these questions are handled apart: each compression method brings its own format and solver, a circuit with fixed weights needs a dedicated constant multiplier for every weight, and discrete solvers reach only narrow subproblems such as rounding. Weight formats have long been moving toward shared decisions, through group scales, shared exponents, microexponents and sparse weights; TWIG takes this trend to its end, and every common format is a shallow TWIG at no extra cost. On five weight matrices of a large language model, a flat tree whose signed power-of-two terms are chosen per weight for circuit cost, with no group scales, needs 9--15\% fewer additions than GPTQ at equal layer error at 3- and 4-bit accuracy on typical matrices, and 20--55\% fewer on matrices with strong outliers.

## 12. Topological Equivalence of Spectral and Density Cluster Hierarchies

- Authors: Sajjad Hashemian
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-22
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 2.9267046114236224
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.31909v1
- PDF: https://arxiv.org/pdf/2610.31909v1
- Local PDF: pdf/2026-10-27_12_Topological Equivalence of Spectral and Density Cluster Hierarchies.pdf

We compare two canonical ways to recover hierarchical clustering from an underlying density $f$: the \emph{density cluster tree} given by connected components of superlevel sets $\{f\geλ\}$, and a \emph{spectral hierarchy} obtained by applying single linkage to diffusion distances induced by a Laplacian operator. We give conditions under which, at an appropriate diffusion time, the diffusion hierarchy is \emph{topologically equivalent} to the density cluster tree up to a monotone rescaling of heights. It further shows that a $k$-NN graph implementation inherits this equivalence from uniform approximation of diffusion distances, yielding a finite-sample reduction from spectral graph constructions to density-level-set topology.

## 13. TGR-EvoDAG: A DAG-based Multi-Agent Code Evolution Framework for Generative Recommendation on Tencent

- Authors: Junlin He, Junzhang Zhu, Yudong Li, Yihong Tang, Xuefeng Jiang, Wei Ma, Chengxiang Zhuo, Zang Li
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-23
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 2.911054363942367
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.32326v1
- PDF: https://arxiv.org/pdf/2610.32326v1
- Local PDF: pdf/2026-10-27_13_TGR-EvoDAG_ A DAG-based Multi-Agent Code Evolution Framework for Generative Recommendation on Tencent.pdf

Large Language Model (LLM) agents have enabled automated code evolution for algorithm discovery. However, current recursive self-improvement (RSI) research for sequential recommendation faces a dilemma: general-purpose frameworks lack domain-specific feedback, while recommender-specific frameworks rely on linear evolution. Crucially, naively integrating them fails when applied to Generative Recommendation (GR). Unlike end-to-end models, GR relies on a module-cascaded pipeline (tokenization, pre-training, and alignment). In this paradigm, existing evolution methods suffer from: i) cost blindness, squandering budgets by ignoring stage-asymmetric retraining overheads; and ii) short-sighted evaluation, discarding promising upstream innovations that temporarily regress metrics before downstream adaptation. To bridge these gaps, we propose TGR-EvoDAG, a multi-agent code evolution framework tailored for GR. TGR-EvoDAG models code evolution as a Directed Acyclic Graph (DAG) to maintain multiple evolution branches and merge complementary innovations, unifying advanced search with rich GR diagnostic feedback. We further introduce stage-aware cost planning to optimize GPU-hour budgets, and active downstream co-adaptation to navigate temporary regressions and unlock cross-stage gains. On public Amazon datasets, TGR-EvoDAG enables the first autonomous evolution of a complete GR pipeline, improving offline metrics by up to 37.4% and Agent4Rec simulated user satisfaction by 19.7% over the strongest baseline. Furthermore, in industrial deployment on Tencent's large-scale commercial media platform, the evolved GR achieves a 12.16% relative improvement in offline Hit@1 and a statistically significant 0.40% increase in online click-through rate (CTR).

## 14. Trajectory Matching: Discrete Flow Matching with Structured Actions

- Authors: Niklas Kemper, Marten Lienen, David Lüdke, Stephan Günnemann
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-23
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 2.882723692724399
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.32602v1
- PDF: https://arxiv.org/pdf/2610.32602v1
- Local PDF: pdf/2026-10-27_14_Trajectory Matching_ Discrete Flow Matching with Structured Actions.pdf

The natural units of structured discrete generation are often not independent single-component edits but richer actions: attaching a fragment to a molecule, inserting a node together with an incident edge, or growing a hierarchy by adding a child. Yet most existing discrete flow matching methods (DFM) are restricted to independent component-wise edits over fixed-size states. This restriction stems from endpoint conditioning: endpoints fix the source and target during training but not the action sequence between them, making tractable conditional rates hard to define for complex actions that cannot be factorized component-wise. We propose trajectory matching, which conditions the flow on a full sequence of actions connecting the endpoints. This yields principled, simulation-free training targets for user-defined action spaces, including actions that change state size, modify multiple components, or depend on earlier actions. We prove that the resulting objective recovers the marginal flow and that trajectory matching strictly subsumes factorized DFM, while additionally capturing actions with prerequisite structure such as hierarchy growth or fragment-based molecule generation. Empirically, on tree and molecular graph generation, trajectory matching with domain-aligned actions matches or surpasses factorized DFM baselines (lifting MOSES validity from 92.8% to 99.2%) and transfers without retraining to substructure extension and linking. Trajectory matching enlarges the design space of discrete flow matching by turning the action vocabulary into a modeling choice. An interactive explanation of trajectory matching is available at https://niklaskemper.com/blog/trajectory-matching/.

## 15. Democratizing LLM Training with the Edge: Challenges, Systems, and the Road Ahead

- Authors: Ziyue Luo, Jiaxuan Cai, Cedric LeDenmat, Srijith Nair, Fatemeh Nourzad, Rohith Krishnan, Qinhang Wu, Jifan Zhang, Sungjae Lee, Zhe Li, Peiwen Qiu, Siddharth Shah, Rishabh Sharma, Sundararajan Srinivasan, Yinglun Xia, Xue Zheng, Zidong Liu, Bicheng Ying, Kaushik Chowdhury, Gauri Joshi, Yingbin Liang, Robert Nowak, Srinivasan Parthasarathy, Saurav Prakash, Balaraman Ravindran, Sanjay Shakkottai, Ness B. Shroff, Haibo Yang, Aylin Yener, Jia Liu
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-23
- DOI: Unavailable
- Categories: cs.DC, cs.LG
- Relevance: 2.8720439615918423
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.32215v1
- PDF: https://arxiv.org/pdf/2610.32215v1
- Local PDF: pdf/2026-10-27_15_Democratizing LLM Training with the Edge_ Challenges, Systems, and the Road Ahead.pdf

The growing computational power of modern GPU data centers has let a few industrial giants train and deploy large language models (LLMs) on massive amounts of data. Yet the sheer scale of these models and their training data makes centralized development increasingly hard to sustain, and at the same time shuts out smaller institutions that hold relevant private data but lack comparable infrastructure. In this paper, we organize our positions on distributed LLM training around the pretraining and fine-tuning paradigms, covering federated learning, split learning, and decentralized approaches, and we assess their readiness for geo-distributed settings with heterogeneous hardware and unreliable connectivity. We then present a {\em unified} system architecture built around a cloud-hosted parameter server that coordinates heterogeneous clients over outbound gRPC connections, reusing one communication, compression, and fault-tolerance stack for both pretraining and a family of fine-tuning methods. We validate the design with real geo-distributed experiments on GPT-2 Medium and Llama3-1B pretraining across multiple university sites, showing stable convergence under realistic conditions. Finally, we chart the road ahead, identifying open problems that span frontier model support, elastic fault tolerance, adaptive compression, federated alignment, privacy and trust, incentive design, and system--algorithm co-design, all of which must be addressed to make democratized LLM training a reality.

## 16. KnitTrans: Coordinated Trajectory Transfer for Effective and Efficient LLM Reinforcement Learning

- Authors: Bangjun Xiao, Chiheng Lou, Xiaodong Ji, Xiangwei Deng, Yikai Zhao, Gang Huang, Hailin Zhang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-23
- DOI: Unavailable
- Categories: cs.DC, cs.LG
- Relevance: 2.8633184818586077
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.32389v1
- PDF: https://arxiv.org/pdf/2610.32389v1
- Local PDF: pdf/2026-10-27_16_KnitTrans_ Coordinated Trajectory Transfer for Effective and Efficient LLM Reinforcement Learning.pdf

Trajectory transfer from rollout to training affects both learning quality and system efficiency in large language model reinforcement learning (RL). Enforcing batch-wide training requirements can delay the admission of completed trajectories, resulting in higher architectural staleness: the additional parameter-version gap from disaggregated pipelining relative to colocated execution. Beyond admission, misalignment between data access and training consumption causes redundant movement and unnecessary waiting when transferring large trajectory payloads. We present KnitTrans, a system that coordinates the rollout-to-training path through three designs. First, constraint-preserving mini-batch admission allows flexibility in early mini-batch composition, while checking that enough capacity remains to satisfy the remaining quotas. Second, on-demand trajectory data access matches storage units to consumer assignments and overlaps micro-batch data preparation with computation. Third, multimodal encoding deduplication supports reuse across a mini-batch while preserving gradient contributions from all backbone micro-batches. Experiments show up to 93% lower architectural staleness than with train-batch admission, narrowing the learning-quality gap between disaggregated execution and colocated execution. On multimodal workloads, KnitTrans reduces transfer latency by two orders of magnitude and achieves a speedup of up to 5.8 times in transfer plus training over the baseline.

## 17. Generalization properties of the token perceptron: the role of embedding and vocabulary

- Authors: Dario Bocchi, Matteo Negri, Flavio Nicoletti, Francesco D'Amico
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-23
- DOI: Unavailable
- Categories: cond-mat.dis-nn, cond-mat.stat-mech, cs.LG, stat.ML
- Relevance: 2.860883189251271
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.32788v1
- PDF: https://arxiv.org/pdf/2610.32788v1
- Local PDF: pdf/2026-10-27_17_Generalization properties of the token perceptron_ the role of embedding and vocabulary.pdf

Large language models are trained to predict tokens from a finite vocabulary, each represented by a vector in a $d$-dimensional embedding space. Therefore, token prediction is a classification problem whose classes have a geometry determined by the embedding. We study how this geometry affects learning in a minimal solvable model: a linear predictor that maps a sequence of $N$ embedded tokens to a $d$-dimensional output through one $d\times d$ matrix per position, trained in the teacher--student setting. We call this the \textit{token perceptron}. We compute its generalization error with the replica method, taking $N\to\infty$ at fixed number of examples per position $α=P/N$ and keeping $d$ and the vocabulary size $D$ finite. As a first reference case, we consider continuous embeddings on the sphere, which isolate the role of the embedding dimension. The natural load is then $α/d$, and for $d>1$ a normalized label fixes the direction of the teacher output, so the problem becomes a noiseless regression: the teacher is recovered exactly above $α_{\rm rec}=d^2/(d-1)$, and spherical cross-entropy reaches this threshold at large inverse temperature. In the same setting the storage capacity of random associations scales as $d^2$ for margins $O(1/\sqrt{d})$. We then turn to vocabulary embeddings, where a label only identifies the Voronoi cell of the teacher output, so that each example imposes inequalities rather than equations, as in the classical perceptron. We compute the Bayes-optimal error for a given embedding matrix through an approximate spectral closure and show that the optimal learner first resolves the directions in which the vocabulary has the largest variance, even when the teacher is isotropic.

## 18. PathJev: Decision-Native Vision-Language Modelling for Histopathology

- Authors: Cristian Tommasino, Antonio M. Rinaldi
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-23
- DOI: Unavailable
- Categories: cs.CV, cs.LG
- Relevance: 2.8509608986969575
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.32478v1
- PDF: https://arxiv.org/pdf/2610.32478v1
- Local PDF: pdf/2026-10-27_18_PathJev_ Decision-Native Vision-Language Modelling for Histopathology.pdf

Vision-language models used for decisions in histopathology rarely return calibrated probabilities over the candidates a user cares about. Decision-native models write a question and a candidate set chosen at run time into the input and return a normalised distribution from a small decision head in one forward pass. We build PathJev-P, a decision-native model for histopathology: MedGemma-1.5-4B with LoRA adapters and a decision head, trained on 40,000 patch states from three public collections whose expert labels are turned into typed questions with organ-specific candidate sets and a "none of these" option. In a comparison over 3 seeds with an analysis plan fixed before testing, on test sets without documented overlap with the training data of the backbone, PathJev-P is more accurate than a generative model trained with the same backbone, data and selection rule, the zero-shot pathology model CONCH and a general medical decision model (balanced accuracy 0.541 against 0.492, 0.345 and 0.213); its advantage over the generative model comes from two organs absent from training. The calibration advantage depends on how the generative model's probabilities are read out. With the summed candidate log-likelihood used in previous work, PathJev-P has the lower calibration error (ECE 0.204 against 0.279); with a length-normalised read-out of the same generative model, examined post hoc, the two have similar mean calibration error (0.201) and the generative model is better calibrated on the unseen organs, where PathJev-P remains over-confident. A supervised linear probe on a pathology foundation model is better calibrated in every setting. In a qualitative whole-slide demonstration, PathJev-P labels unsupervised tissue clusters with abstention and separates carcinoma from other tissue while running the model on a fraction of the tiles.

## 19. 4DMemory: Benchmarking Long-Horizon Spatiotemporal Memory with Harness-Augmented Agents

- Authors: Yanhao Jia, Yi Zhu, Yiran Zhong, Weigao Sun, Feida Zhu, Pengkun Jiao, Sihan Yang, Ming Ma, Steven Hoi, Erik Cambria
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-23
- DOI: Unavailable
- Categories: cs.CV, cs.AI, cs.CL, cs.MM
- Relevance: 2.8474779488769233
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.32332v1
- PDF: https://arxiv.org/pdf/2610.32332v1
- Local PDF: pdf/2026-10-27_19_4DMemory_ Benchmarking Long-Horizon Spatiotemporal Memory with Harness-Augmented Agents.pdf

Humans efficiently process multimodal streams spanning hours to years, building persistent, fine-grained spatiotemporal memories that support reasoning about and predicting long-horizon events. In contrast, existing benchmarks focus on short- and medium-context tasks, and most foundation models struggle to preserve fine-grained information over long horizons. To evaluate and improve long-horizon spatiotemporal reasoning, we introduce the LongVideo dataset and the 4DMemoryBench. LongVideo comprises about 900 hours of video and over 5,000 manually reviewed questions covering visual, textual, and spatiotemporal reasoning across diverse context lengths. We further develop the 4DMemory Harness, which integrates four complementary skills, 22+ specialized tool models, and a model-specific retrieval-augmented generation system. Evaluating 13 leading models, we find that standalone foundation models struggle with long-horizon tasks, while the 4DMemory Harness improves all of them by over 50\%. Compared to previous benchmark, the same models exhibit a performance drop of more than 10\% on 4DMemoryBench. We hope 4DMemory will facilitate the development of spatiotemporal agents capable of addressing complex, long-horizon tasks.

## 20. Distributional Alignment of LLMs and Its Generalization Properties

- Authors: Nelson Jo
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-05
- DOI: Unavailable
- Categories: cs.CL, cs.AI
- Relevance: 2.829742128612711
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.31687v1
- PDF: https://arxiv.org/pdf/2610.31687v1
- Local PDF: pdf/2026-10-27_20_Distributional Alignment of LLMs and Its Generalization Properties.pdf

Large language models are increasingly used to simulate and probe human behavior, e.g., for surveys. For these applications, a key property is that outputs satisfy distributional alignment: to match its output distribution with some reference (in this case, human) distribution. An obstacle in achieving distributional alignment is generalizing from small training data. In this work, we study (1) how to distributionally align LLMs; and (2) how aligned LLMs might generalize to unseen samples and unrelated topics and tasks. Using two large-scale benchmarks, we find that LLMs can indeed achieve distributional alignment and generalize to unseen questions of the same domain. Cross-topic generalization depends on the relationship between topics (e.g., questions about politics are related to trust in institutions). However, aligned LLMs can degrade in surprising ways (e.g., lose their creative ability), suggesting that its generalization properties are inherently unpredictable and unstable.

## 21. LLaCO: Continuous Diffusion for Large Language Models with Competition-Aware Semantic Scheduling

- Authors: Zijian Jia, Peixuan Zhang, Genying Li, Di Wu, Yujie Fu, Si Li, Boxin Shi, Shuchen Weng
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-23
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 2.821949089015387
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.32604v1
- PDF: https://arxiv.org/pdf/2610.32604v1
- Local PDF: pdf/2026-10-27_21_LLaCO_ Continuous Diffusion for Large Language Models with Competition-Aware Semantic Scheduling.pdf

Continuous diffusion models have emerged as a promising non-autoregressive paradigm for text generation over continuous embedding spaces. Along the continuous trajectory, the residual token identity directly shapes the denoising objective. However, the geometric trajectory misaligns with temporal progression, triggering severe temporal compression. In this paper, we show that embedding norm decay causes Euclidean distance to yield spurious overtaking, indicating that token competition must be evaluated directionally. In this space, a candidate overtakes the source token only when the effective noise magnitude surpasses their semantic separation. We formalize these pairwise dynamics as the Competition Threshold Theory (CTT). Crucially, high-dimensional overtaking requires extreme noise levels, causing standard trajectories to concentrate identity decay into a narrow window near the noisy endpoint. To resolve this, we propose Semantic Retention Scheduling (SRS) to align time allocation with the progression of identity decay, and demonstrate that existing token identity metrics are fundamentally statistical aggregations of these pairwise crossings. Building on these theoretical insights, we introduce LLaCO, a generative framework powered by competition-aware semantic scheduling. LLaCO adapts a pretrained backbone to continuous representations via an embedding directional adapter and timestep-conditioned modulation. To operate within the directional space, LLaCO employs a spherical noising process formulated as a geodesic interpolation toward a mask-biased endpoint, eliminating norm decay while preserving accurate token competition. Guided by SRS, LLaCO reallocates the denoising trajectory proportionally to the logarithmic rank decay. Instantiated as an 8B model, LLaCO outperforms previous continuous diffusion baselines and rivals discrete diffusion models of comparable scale.

## 22. MG-REPA: Multi-Granularity Representation Alignment for Generative Target Speaker Extraction

- Authors: Dohwan Kim, Jung-Woo Choi
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-23
- DOI: Unavailable
- Categories: eess.AS, cs.AI
- Relevance: 2.8199638605196604
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.32161v1
- PDF: https://arxiv.org/pdf/2610.32161v1
- Local PDF: pdf/2026-10-27_22_MG-REPA_ Multi-Granularity Representation Alignment for Generative Target Speaker Extraction.pdf

Generative target speaker extraction (TSE) models achieve high-quality extraction, but suffer from considerably slow training convergence. Representation Alignment (REPA) accelerates diffusion transformer training by aligning hidden states with a pre-trained Self-Supervised Learning (SSL) teacher. However, existing alignment in the speech and audio domain operates at a single granularity. For TSE, frame-level alignment leaves the global, time-invariant characteristics of the target speech implicit, whereas utterance-level alignment leaves the time-varying content implicit, even though extracting the target requires both. We propose Multi-Granularity Representation Alignment (MG-REPA), aligning the hidden states with an SSL model at the frame level and a speaker verification model at the utterance level. We further apply temporal normalization to the frame-level target, removing its utterance-level statistics so that each branch concentrates on its granularity. On Libri2Mix, MG-REPA reaches the OVRL and PESQ of a MeanFlow-TSE baseline with $3.0\times$ and $2.1\times$ fewer epochs, respectively. Trained for 750 epochs, it is competitive with the published 2,000-epoch baseline on intrusive metrics while improving non-intrusive metrics. An ablation demonstrates that MG-REPA outperforms alignment at a single granularity.

## 23. Solvent: Long-Horizon Reasoning for Multi-Step Retrosynthesis

- Authors: Yifei Wang, Botian Wang, YiFei Wang, Jiangtao Feng, Xinbo Zhang, Yawen Ouyang, Yixin Wu, Lihao Wang, Xiaoqing Zheng, Xuanjing Huang, Hao Zhou
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-23
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 2.795772410388651
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.32308v1
- PDF: https://arxiv.org/pdf/2610.32308v1
- Local PDF: pdf/2026-10-27_23_Solvent_ Long-Horizon Reasoning for Multi-Step Retrosynthesis.pdf

Multi-step retrosynthesis requires recursively transforming a target molecule through successive reaction steps into purchasable building blocks, and recent work has begun to draw on large language model (LLM) reasoning to tackle the task. In its latest evolution, LLM reasoning has entered the long-horizon regime: models pursue objectives across interdependent steps, interact with environments, and adapt to feedback. This shift has markedly advanced LLM capabilities, as illustrated by breakthroughs in AI-driven mathematical research. At this frontier, we introduce Solvent, an 8B LLM that successfully extends long-horizon reasoning to multi-step retrosynthesis. Through a two-round post-training curriculum, Solvent learns to interleave iterative synthesis planning, external availability verification, and adaptive route revision. Experiments show that, following a $2.1\times$ performance boost from RL, Solvent scores 61.86% across four benchmarks, surpassing mid-scale language models and prior search-based retrosynthesis systems, and rivaling frontier trillion-parameter LLMs.

## 24. Beyond Data Schedule: Fast LLM Pretraining on Data Mixtures by Loss-Reweighting

- Authors: Jiazheng Li, Huaqing Zhang, Jing Xu, Tianle Cai, Jingzhao Zhang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-23
- DOI: Unavailable
- Categories: cs.LG, cs.AI
- Relevance: 2.7909508792779825
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.32141v1
- PDF: https://arxiv.org/pdf/2610.32141v1
- Local PDF: pdf/2026-10-27_24_Beyond Data Schedule_ Fast LLM Pretraining on Data Mixtures by Loss-Reweighting.pdf

Large language models often acquire specialized capabilities through successive pretraining stages, but these gains can come at the cost of forgetting earlier knowledge. In this work, we investigate whether such trade-offs can be improved by changing how strongly each domain contributes to learning while keeping its data exposure fixed. We find that, in controlled knowledge--mathematics experiments, loss reweighting produces a single checkpoint that surpasses the best knowledge and reasoning scores attained along either stage trajectory. This reveals an independent control that data-mixture ratios alone do not capture. Building on this finding, we propose LARE (Loss-Adaptive Reweighting under fixed Exposure), which automatically adjusts domain weights from running loss statistics. Motivated by a theoretical analysis of gradient noise, its normalized inverse-square-root rule balances relative loss scales without changing the sampled mixture or requiring additional runs to search for weights. Across knowledge, mathematics, and code, \Method{} improves all five evaluated benchmarks for a 1.5B model trained on 240B tokens, averaging +7.84 pp over a matched direct mixture, including gains of +17.06 pp on GSM8K and +9.00 pp on MATH. These findings demonstrate that adjusting domain loss scales can improve joint capabilities without additional domain exposure.

## 25. Reimagining Enterprise RAG for Multi-Agent Systems: A Knowledge Layer That Organizes Before It Retrieves

- Authors: Garima Agrawal, Prasun Das, Akshay Sarvade, Priyanka L, Minisha N, Sravani Joshna, Hemath Manivannan, Lavanya Korada, Sambhrit Pattanayak, Srashti Gupta, Siddu R, Prasad Kalyanasundaram
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-23
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 2.787547463048168
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.32851v1
- PDF: https://arxiv.org/pdf/2610.32851v1
- Local PDF: pdf/2026-10-27_25_Reimagining Enterprise RAG for Multi-Agent Systems_ A Knowledge Layer That Organizes Before It Retrieves.pdf

Enterprises are deploying agentic AI across the software development lifecycle, and they need the behavioral logic of the systems they act on, not stakeholder documentation. A seven-agent reverse-engineering pipeline recovered this logic, processing 241 repositories across 18 services into thousands of artifacts describing scope, journeys, rules and acceptance criteria. Recovery does not confer usability. Entities like offer, eligibility, and activation recur across services under a shared vocabulary, related in name but operationally distinct, so one end-to-end journey implicates over a thousand near-identical rules that must not be conflated. Flat vector retrieval fails, returning an identical rule from the wrong service at high similarity with no signal of error. Content-level ontology, the traditional remedy, did not exist, and relating every occurrence of recurring entities would have cost more than the engagement and not survived a release cycle. We place the ontology at the artifact level. In this machine-generated corpus, each artifact retains its producer, component, service, domain and type, provenance that disambiguates before content is read. We present a knowledge layer that organizes before retrieving: a self-describing catalog, a sparse metadata registry, and a navigation hypergraph defined over artifacts rather than extracted entities. Queries resolve to artifact identifiers that constrain vector search, so the competing rule from another service is absent rather than outranked, making disambiguation structural, not statistical. Built in under a week and admitting new services by convention, the layer serves SDLC agents, developers, quality engineers and analysts. It supported root-cause analysis and resolution of 100+ production defects with developer verification and attributed 35 release regression failures to specific rules and services.

## 26. SOPO: Socratic Guided Policy Optimization for Span-Level Hallucination Detection

- Authors: Jiawei Dong, Zilong Bai, Pengtian zhu, Peng Zhou
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-23
- DOI: Unavailable
- Categories: cs.CL, cs.AI
- Relevance: 2.781038364796244
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.32212v1
- PDF: https://arxiv.org/pdf/2610.32212v1
- Local PDF: pdf/2026-10-27_26_SOPO_ Socratic Guided Policy Optimization for Span-Level Hallucination Detection.pdf

Large Language Models (LLMs) have gained widespread adoption in various natural language processing tasks, but suffer from hallucination issues where they generate unfaithful or inconsistent content. While Reinforcement Learning with Verifiable Rewards (RLVR) has shown promising applications in reasoning tasks, its application to span-level hallucination detection is challenged by localization ambiguity, reward sparsity on hard examples, and uncontrolled length inflation. To address these issues, we introduce Socratic Guided Policy Optimization (SOPO), a multi-turn RL framework for robust hallucination detection. The key innovation of SOPO is a Socratic feedback mechanism, where a teacher model guides the reasoning trajectories during rollout by providing indirect hints inferred from the ground truth. This teacher-guided approach enables the model to generate more effective reasoning trajectories for hard examples, thus alleviating reward sparsity. Furthermore, we incorporate Turn-based Advantage Scaling to penalize verbosity bias, encouraging the model to develop efficient and autonomous reasoning capabilities. Empirical results on RAGTruth demonstrate that SOPO (4B) achieves state-of-the-art performance, surpassing leading proprietary models (e.g., GPT-5) and standard RL baselines, while obtaining higher reported mean scores than GRPO on four out-of-domain benchmarks, with mixed evidence against CAPO. We release our training and evaluation code alongside the 1.7B and 4B SOPO models at https://github.com/patsnap/SOPO.

## 27. On-Policy Self-Training: Data-Free Self-Improvement in Large Language Models

- Authors: Leon Sick, Lukas Hoyer, Yannick Strümpler, Christian Reisswig, Timo Ropinski, Federico Tombari
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-23
- DOI: Unavailable
- Categories: cs.CL, cs.AI, cs.LG
- Relevance: 2.761154351152373
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.32770v1
- PDF: https://arxiv.org/pdf/2610.32770v1
- Local PDF: pdf/2026-10-27_27_On-Policy Self-Training_ Data-Free Self-Improvement in Large Language Models.pdf

On-policy self-distillation enables post-training foundation models without relying on stronger external teachers. However, existing approaches rely on ground-truth question-answer pairs, human-curated problem sets, or other supervised signals. In this work, we reformulate on-policy self-distillation as a self-training framework, driven by self-generated question-answer pairs and privileged reasoning demonstrations. We push supervision to the limit: guided solely by coarse, high-level topic descriptions, the model synthesizes its own curriculum of queries and privileged reasoning traces without access to any human-curated prompts or answers. We find that self-distillation on fully synthetic privileged information enables a model to improve across multiple domains while retaining its capabilities on domains it is not self-trained on. We demonstrate the generality of this framework across text and multimodal domains, achieving consistent self-improvement on standard language benchmarks and Visual Question Answering. Our findings demonstrate that foundation models possess rich latent capabilities that can be amplified without external task supervision or curated problem distributions.

## 28. PASTA: Prompt-Aware Annealed Diffusion Sampling

- Authors: Ren Ajiki, Ryugo Morita, Stanislav Frolov, Brian Bernhard Moser, Ko Watanabe, Riku Takahashi, Andreas Dengel, Jinjia Zhou
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-23
- DOI: Unavailable
- Categories: cs.CV, cs.AI, cs.LG
- Relevance: 2.7553156515551387
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.32390v1
- PDF: https://arxiv.org/pdf/2610.32390v1
- Local PDF: pdf/2026-10-27_28_PASTA_ Prompt-Aware Annealed Diffusion Sampling.pdf

While Diffusion models produce high-quality images, real-world visual design requires intentionally preserving clean regions for headlines, logos, or UI elements. Existing layout-aware text-to-image methods struggle to strictly preserve reserved regions, often introducing unwanted content that complicates downstream editing. Existing approaches either manipulate attention to displace content or suppress conditioning via noise-level interventions. However, these methods sacrifice visual coherence, producing flat regions or noticeable style inconsistencies between reserved and non-reserved areas. To address this limitation, we propose a Prompt-Aware Shared-Latent Training-Free Annealed Diffusion Sampling (PASTA), a training-free framework that enforces reserved-region constraints by selectively applying semantic guidance to object-allowed regions during sampling. PASTA operates on a shared latent trajectory, where full-prompt and context-prompt guidance are fused through mask-guided sampling. An annealed schedule suppresses semantic leakage during early denoising stages while gradually restoring visual consistency in later stages. Extensive experiments demonstrate that PASTA improves reserved-region fidelity while preserving overall image realism and perceptual consistency.

## 29. Autoregressive Multimodal Anomaly Detection with Large Language Models for Microservice Systems

- Authors: Yixiang Tang, Fagui Liu, Guoxiang Zhong, Xi Yao, C. L. Philip Chen
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-22
- DOI: Unavailable
- Categories: cs.LG, cs.AI, cs.SE
- Relevance: 2.753617144689292
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.31722v1
- PDF: https://arxiv.org/pdf/2610.31722v1
- Local PDF: pdf/2026-10-27_29_Autoregressive Multimodal Anomaly Detection with Large Language Models for Microservice Systems.pdf

Microservice systems have become a dominant architecture for large-scale cloud applications, enabling rapid deployment and elastic scaling. However, ensuring the reliability and availability of microservice systems critically relies on effective anomaly detection, as failures and performance anomalies can quickly propagate across services and severely impact end-to-end system behavior. Existing multimodal anomaly detection approaches for microservice systems often struggle with two fundamental limitations: (i) the neglect of modality-specific characteristics in favor of cross-modality fusion, and (ii) the "identity-shortcut" problem that affects the feature reconstruction process. To address these issues, we propose LLMMAD, an autoregressive multimodal anomaly detection framework for microservice systems based on Large Language Models (LLMs). Initially, to reconcile cross-modality fusion with modality-specific preservation, LLMMAD embeds and recombines multimodal data into a unified sequence for LLM processing to model inter-modality relationships, while employing modality-wise reconstruction heads to retain modality-specific information. Subsequently, to eliminate the identity-shortcut, we implement a prediction-driven autoregressive objective, under which the model predicts future states rather than copies current inputs. Finally, we conduct extensive experiments on three real-world datasets. The results demonstrate that LLMMAD consistently outperforms state-of-the-art methods, achieving F1-score improvements of 3.1%, 1.4%, and 0.9%, respectively, thereby providing a more reliable solution for microservice monitoring.

## 30. CASE: Confusion-Aware Skill Evolution for Frozen Multimodal Emotion Models

- Authors: Siyu Wu, Zeyu Liang, Linghao Wang, Qiyun Zheng, Yi Yao, Ling Lo, Hongxia Xie
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-23
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 2.7532804411026914
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.32481v1
- PDF: https://arxiv.org/pdf/2610.32481v1
- Local PDF: pdf/2026-10-27_30_CASE_ Confusion-Aware Skill Evolution for Frozen Multimodal Emotion Models.pdf

Multimodal large language models (MLLMs) have substantially advanced Multimodal Emotion Recognition (MER) by enabling fine-grained emotion understanding through reasoning over multimodal evidence. However, they still exhibit systematic confusion between semantically adjacent emotions with highly overlapping multimodal cues. Existing approaches typically address these errors through global parameter adaptation, making confusion correction costly and inflexible. We instead observe that emotion confusion is highly localized and therefore better addressed through reusable pair-specific expertise. Building on this insight, we propose Confusion-Aware Skill Evolution (CASE), the first agent-skill framework for MER. CASE maintains a sparse, self-evolving library of pair-specific EmotionSkills that externalize affective expertise from model parameters, enabling the learned expertise to be continuously refined and readily transferred across diverse frozen MLLM backbones. During inference, CASE dynamically retrieves the appropriate EmotionSkill to reinforce boundary-aware reasoning while keeping the MLLM backbone frozen. Extensive experiments on CA-MER, DFEW, and EMER demonstrate the effectiveness and transferability of CASE across both general-purpose and emotion-specialized MLLMs. Notably, CASE improves the average accuracy of Qwen3-VL-8B on the CA-MER benchmark from 46.80% to 59.13%, while achieving consistent gains across MLLMs.
