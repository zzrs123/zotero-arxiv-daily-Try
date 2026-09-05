# Paper Daily Reading - 2026-09-05

## 1. When Vision Meets Graphs: A Survey on Graph Reasoning and Learning

- Authors: Xinjian Zhao, Wei Pang, Zhixuan Yu, Xiangru Jian, Xiaozhuang Song, Yaoyao Xu, Zhongkai Xue, Dingshuo Chen, Shu Wu, Philip Torr, Tianshu Yu
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-03
- DOI: Unavailable
- Categories: cs.SI, cs.CV, cs.LG
- Relevance: 3.8443599910405366
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.03816v1
- PDF: https://arxiv.org/pdf/2609.03816v1
- Local PDF: pdf/2026-09-05_01_When Vision Meets Graphs_ A Survey on Graph Reasoning and Learning.pdf

Graphs are a fundamental data structure underlying many problems in the natural and social sciences. Over the past decade, Graph Neural Networks (GNNs) have dominated graph machine learning, supported by solid theoretical foundations. Yet scientists often understand graph structure through vision: chemists read molecular diagrams and social scientists inspect network visualizations. Despite decades of work on graph visualization, most graph learning pipelines still treat graphs purely as symbolic structures, rarely leveraging the visual form of graphs. We argue that this gap deserves renewed attention in the era of powerful vision and vision-language models. This survey provides a first systematic overview of the emerging area we term vision meets graphs, which treats visual depictions of graphs as first-class inputs for reasoning and learning. We organize existing work into three threads. Vision for Graph Reasoning studies how models can use visual depictions of graphs to understand structure and carry out multi-step reasoning. Vision for Graph Learning explores how visual features can complement or augment graph encoders beyond known limitations of message passing. Scientific Graphs examines domains where standardized depiction conventions support both reasoning and learning. Our goal is to clarify what current methods can and cannot do, and to outline a path toward foundation models that perceive and reason about graphs as scientists do.

## 2. Language-encoded network topology enables large language models to reason about complex networks

- Authors: Ucchwas Talukder Utsha, Sakib Mostafa, James Zou, Md Tauhidul Islam
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-03
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.7609697056482205
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.03229v1
- PDF: https://arxiv.org/pdf/2609.03229v1
- Local PDF: pdf/2026-09-05_02_Language-encoded network topology enables large language models to reason about complex networks.pdf

Networks describe systems in biology and beyond, from protein interactions and social relationships to power grids and citation records. Reasoning about such systems requires understanding their structure: which elements are central, which connections bridge separate communities, and how it changes when elements are removed. Although large language models (LLMs) excel at natural language, they struggle with such questions when networks are given as edge lists, sentences or measurement tables, because their structural meaning must be inferred. Here we introduce BioGlyph, which compiles network topology into an interpretable and transferable language of structural roles. BioGlyph combines graph partitioning and structural measurements to identify roles such as hubs, community cores and cross-community connectors, and fixed rules to translate them into a universal vocabulary. The representation describes each element through its structural role, supporting evidence and semantic consequences, leaving both the network and the LLM unchanged. Across twenty networks spanning five domains, BioGlyph substantially improves open LLMs' ability to answer structural reasoning questions, outperforming edge-based, numerical and learned representations by up to 26 percentage points in system accuracy. Ablations show that the gain comes from explicitly encoding structural roles in semantically interpretable terms. The gain is more prominent in dense, community-structured networks and diminishes in sparse networks whose topology is more readily inferred from text. In a budding-yeast protein-interaction network, BioGlyph exposes biological organization: cross-community connectors are enriched for essential genes, whereas peripheral proteins are depleted. BioGlyph thus provides an interpretable representation for both language models and scientists to reason about network structure.

## 3. Microenvironment-aware transcriptome reconstruction in spatial transcriptomics

- Authors: Yang Shi-Tong, Pai Peng, Hui-Feng He, Meng-Guo Wang, Bo-Han Si, Xiao-Fei Zhang, Luonan Chen
- Source: openalex
- Venue type: journal
- Journal: Nature Communications
- Publication status: published
- Publication date: 2026-09-03
- DOI: https://doi.org/10.1038/s41467-026-77349-8
- Categories: Single-cell and spatial transcriptomics, Cell Image Analysis Techniques, Ferroptosis and cancer prognosis
- Relevance: 3.648539876071626
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://doi.org/10.1038/s41467-026-77349-8
- PDF: Unavailable
- Local PDF: Not downloaded

Abstract Imaging-based spatial transcriptomics offers single-cell resolution but measures limited panels dominated by identity-defining genes, leaving transcriptome-wide variation unobserved. Existing approaches for predicting unmeasured genes rely mainly on shared-gene alignment, which recovers identity-related expression but fails to capture subtle microenvironment-driven variation within a cell type. We introduce Emerge, a framework that reconstructs transcriptome-scale expression by jointly modeling intrinsic transcriptional manifolds from single-cell RNA sequencing and the extrinsic niche organization observed in spatial data within a type-constrained optimal transport formulation. Across fourteen MERFISH and Xenium datasets from neural and tumor tissues, Emerge improves prediction accuracy, spatial coherence and recovery of within-type heterogeneity. The reconstructed transcriptomes reveal microenvironment-stratified astrocyte, stromal and fibroblast states that are only partially captured by measured panels or existing prediction approaches, establishing Emerge as a generalizable foundation for context-aware reconstruction in spatial biology.

## 4. Pattern Over-Generalization of Knowledge Graph Embedding

- Authors: Junsik Kim, Kangil Kim
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-03
- DOI: Unavailable
- Categories: cs.CL, cs.AI
- Relevance: 3.4386950535733183
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.03487v1
- PDF: https://arxiv.org/pdf/2609.03487v1
- Local PDF: pdf/2026-09-05_04_Pattern Over-Generalization of Knowledge Graph Embedding.pdf

Knowledge graph embedding (KGE) demonstrates its effectiveness for predicting missing links in knowledge graphs (KGs) by projecting entities and relations into a low-dimensional vector space. It is crucial for KGE models to effectively capture inference patterns (patterns) inherent in KGs, such as symmetry/antisymmetry, inversion and composition. Although recent KGE models exhibit strong capabilities in modeling such diverse patterns, they suffer from inherent limitations stemming from pattern over-generalization, where embeddings learned from only a single pattern instance inevitably generalize that pattern to all related instances, i.e., generalize the pattern universally. To address this issue, we propose PogRE (Pattern Over-Generalization Robust Embedding), a simple but effective method that utilizes dense linear transformations and compound operations for relation representation. Our theoretical analysis demonstrates that a dense linear transformation allows a pattern to become progressively universal as more triples are observed in the pattern. Furthermore, after observing d+1 linearly independent entities (d+1 denotes the dimension of entity), the linear transformation guarantees universal generalization of the pattern across all related instances. Experimental results on three standard benchmark datasets show that PogRE outperforms existing state-of-the-art KGE models in link prediction. Moreover, our empirical results indicate that PogRE effectively addresses the negative impact of over-generalization.

## 5. GraFT: A Training-Free Framework for Spatial Reasoning in Multimodal Large Language Models via 3D Scene Graphs

- Authors: Junqing Du, Fernando Ropero, Erkin Turkoz, Yanfeng Zhang, Lu Liu
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-03
- DOI: Unavailable
- Categories: cs.CV, cs.AI, cs.RO
- Relevance: 3.4333389238411267
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.03892v1
- PDF: https://arxiv.org/pdf/2609.03892v1
- Local PDF: pdf/2026-09-05_05_GraFT_ A Training-Free Framework for Spatial Reasoning in Multimodal Large Language Models via 3D Scene Graphs.pdf

3D spatial reasoning underpins understanding and acting in the physical world, yet it remains unreliable in current multimodal large language models (MLLMs). These models falter at precise geometric measurement, at transforming between egocentric and allocentric viewpoints, and at grounding fine-grained appearance. The most common remedies fine-tune the model on large-scale curated spatial-reasoning datasets or attach dedicated encoders for 3D geometry, which typically couples the solution to costly supervision and a specific backbone. We instead introduce GraFT, a training-free framework that supplies the missing 3D structure through a compact, easily maintained 3D scene graph (3DSG). From this 3DSG, GraFT provides three spatial reasoning capabilities: (1) deterministic geometry through symbolic tools, (2) allocentric layout through a bird's-eye-view (BEV) rendering, and (3) visual-attribute grounding through task-relevant egocentric frames. On ScanQA, GraFT improves every metric over the same-backbone baseline, raising CIDEr by 27%. On VSI-Bench, GraFT improves frozen MLLMs by up to 65%, surpassing every proprietary and general-purpose open-source baseline, and several prominent fine-tuned spatial models.

## 6. NucleicBERT interprets RNA sequence space through self-supervised language modelling

- Authors: Utkarsh Upadhyay, Julian Herold, Markus Götz, Alexander Schug
- Source: openalex
- Venue type: journal
- Journal: Nature Machine Intelligence
- Publication status: published
- Publication date: 2026-09-03
- DOI: https://doi.org/10.1038/s42256-026-01295-9
- Categories: RNA and protein synthesis mechanisms, Machine Learning in Bioinformatics, Origins and Evolution of Life
- Relevance: 3.3646408025166874
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://doi.org/10.1038/s42256-026-01295-9
- PDF: Unavailable
- Local PDF: Not downloaded

Abstract Much of the human genome’s non-protein-coding fraction acts directly through RNA, yet the structural and functional roles encoded in these sequences remain poorly understood. Applying deep learning is hindered by scarce RNA structural data and it remains unclear what biological constraints such models can recover directly from the abundant RNA sequences alone. Here, to address these challenges, we developed NucleicBERT, a self-supervised masked-language model that learns contextual representations from single sequences without evolutionary information. Explainable artificial intelligence analyses show that the model organizes RNA sequences in latent space and encodes structural properties indicating that biologically meaningful constraints are learned from sequence correlations alone. When fine-tuned for downstream structural and functional tasks, NucleicBERT requires only single sequences while matching or exceeding current RNA prediction models. This alignment-free framework addresses the scarcity of annotated 3D RNA data while providing a rapid, computational complement to experimental techniques. By bridging abundant unlabelled sequence data with scarce structural annotations, NucleicBERT advances RNA structure prediction and informs how large language models encode biological information.

## 7. Geometry-Aware Graph Construction via Adaptive Spectral Bandwidth Control

- Authors: Ecem Bozkurt, Antonio Ortega
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-03
- DOI: Unavailable
- Categories: cs.LG, eess.SP
- Relevance: 3.2715014975218315
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.03306v1
- PDF: https://arxiv.org/pdf/2609.03306v1
- Local PDF: pdf/2026-09-05_07_Geometry-Aware Graph Construction via Adaptive Spectral Bandwidth Control.pdf

Kernelized graph methods - spectral clustering, diffusion maps, and sparse kernel -regression graphs - that use Gaussian kernels depend on the choice of Gaussian bandwidth sigma, which governs the spectral character of the local kernel operator. When sigma is too small, the kernel overestimates local complexity and treats each sample as an independent direction; when sigma is too large, the kernel collapses multiple directions together, the condition number diverges, and all geometric discrimination is lost. We propose a choice of scale to make the spectral complexity of the kernel consistent with the intrinsic complexity of the underlying manifold. We propose a per-node bandwidth criterion that operationalizes this principle by jointly matching the kernel's effective rank to the local intrinsic dimension estimated via minimum spanning tree, anchoring the search in the manifold-consistent log-log scaling regime. We evaluate SSL embeddings from six encoders on CIFAR-100, showing that adaptive bandwidth consistently improves leave-one-out (LOO) classification and label propagation (LP) accuracy over fixed-bandwidth methods and competing adaptive methods.

## 8. SENTINEL-RL: Offloading Topological Reasoning from LLM Agents in the Security Operations Center

- Authors: Uday Vallabhaneni, Cassie L. Cagwin, David J. Wild
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-03
- DOI: Unavailable
- Categories: cs.CR, cs.AI
- Relevance: 3.1513280412047093
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.04159v1
- PDF: https://arxiv.org/pdf/2609.04159v1
- Local PDF: pdf/2026-09-05_08_SENTINEL-RL_ Offloading Topological Reasoning from LLM Agents in the Security Operations Center.pdf

Large language model (LLM) agents are increasingly proposed as autonomous SOC analysts, but two limitations make them unreliable at enterprise scale: a finite context window cannot hold a multi-thousand-host authentication graph, and free-form generation offers no guarantee that a recommended containment action is consistent with the topology it operates on. We present Sentinel-RL, an agentic-SOC architecture that decouples topological reasoning from semantic reasoning: a heterogeneous graph attention encoder summarizes the live authentication subgraph into a fixed-dimensional state, a Proximal Policy Optimization (PPO) policy maps this state to a constrained set of investigative actions, and an LLM agent loop is restricted to consuming the policy's recommendations and producing analyst-readable narratives gated by a critic. We instantiate the system on the LANL Comprehensive, Multi-Source Cyber-Security Events dataset and the Indiana University Quartz HPC cluster, reporting four results: (i) a two-phase CREATE ingestion pattern loads a 24M-edge authentication subgraph into Neo4j in 14.2 minutes on a single 32-core node, roughly 24x faster than the canonical MERGE-based pipeline; (ii) a sliding-window alert engine reliably trips a 25-event/10-second threshold in <=2.5 s across 50 trials; (iii) PPO training over 200 iterations converges to a mean episodic return of 8.74+/-0.31, with held-out precision of 0.91 and recall of 0.87 on labeled red-team events; and (iv) the integrated containment loop completes a full detect-investigate-recommend-human-approve cycle in a median of 6.3 s. We contribute a reusable engineering pattern (the hot-node deadlock workaround), a portable HPC deployment pattern (anchor-node co-location), and an enterprise-readiness analysis covering false-positive economics, reversibility guarantees, audit compliance, and the human-approval boundary.

## 9. Kernel Reboot: Breaking the Boundaries of Neural Tangent Kernels for Neural Fields

- Authors: Amir Mallak, Alaa Maalouf, Lior Wolf, Daniela Rus, Dan Rosenbaum
- Source: arxiv
- Venue type: preprint
- Journal: IEEE Transactions on Pattern Analysis and Machine Intelligence, vol. 48, no. 9, pp. 10940-10957, Sep. 2026
- Publication status: preprint
- Publication date: 2026-09-02
- DOI: 10.1109/TPAMI.2026.3692624
- Categories: cs.LG, cs.CV
- Relevance: 3.123801419407079
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.03117v1
- PDF: https://arxiv.org/pdf/2609.03117v1
- Local PDF: pdf/2026-09-05_09_Kernel Reboot_ Breaking the Boundaries of Neural Tangent Kernels for Neural Fields.pdf

Neural fields (NFs) map continuous coordinates to signals such as color or density, but fast high-quality reconstruction from sparse observations remains difficult. Classical Neural Tangent Kernel (NTK) regression gives closed-form fits, yet it is fundamentally linear and cannot accumulate reusable task priors. We develop three algorithms that address these gaps. NTK-KIP learns a distilled support set of coordinates (and optional labels) so that a finite NTK can inpaint large missing regions from little observed data, yielding a compact non-linear representation instead of a raw kernel solve. MetaQuill meta-learns a shared initialization for an INR so that new scenes can be adapted by updating only a small task-specific weight offset, which provides true feature learning and a reusable prior. Finally, MetaQuill-KIP fuses both ideas: it seeds the task with a KIP-style non-linear warm start, then refines only that small offset around the meta-learned initialization. MetaQuill-KIP achieves high-PSNR reconstructions and semantically plausible inpainting under very sparse observations, while requiring only lightweight per-instance adaptation, whereas diffusion-style baselines typically depend on large pretrained generative priors and costly per-image tuning. This shows that NTK-driven neural fields can be made both non-linear and meta-learnable, narrowing the gap between analytic kernels and practical few-shot reconstruction.

## 10. Causal Foundation Models

- Authors: Christopher Stith, Hossein Rahmani, Jesse C. Cresswell
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-02
- DOI: Unavailable
- Categories: cs.LG, stat.ML
- Relevance: 3.0904407727226872
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.03003v1
- PDF: https://arxiv.org/pdf/2609.03003v1
- Local PDF: pdf/2026-09-05_10_Causal Foundation Models.pdf

Causal inference is the practice of estimating the effect of a treatment or intervention from data. It traditionally requires a bespoke pipeline for every new problem: first proposing a causal mechanism, selecting a compatible estimator, and finally training it. Meanwhile, across diverse settings and modalities, much of machine learning has shifted to the paradigm of foundation models: networks pretrained once at scale and applied to new tasks without fine-tuning. Causal foundation models (CFMs) bring this paradigm to causal inference. CFMs are pretrained neural networks that estimate causal quantities, such as the average treatment effect, on entirely new datasets using in-context learning without requiring model updates. This work provides a practical introduction to this emerging area. We summarize the necessary background in causal inference and machine learning before discussing CFMs. Throughout, we include example code and Jupyter notebooks.

## 11. ENEAS: Embedding-guided Neural Ensemble for Adaptive Segmentation

- Authors: Javier del Pino, Salvador Rodríguez, Alejandro Garabito, Javier Álvarez, Chema Garabito
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-03
- DOI: Unavailable
- Categories: cs.CV, cs.AI
- Relevance: 3.060501863476819
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.03756v1
- PDF: https://arxiv.org/pdf/2609.03756v1
- Local PDF: pdf/2026-09-05_11_ENEAS_ Embedding-guided Neural Ensemble for Adaptive Segmentation.pdf

We present ENEAS, a unified, text-promptable method for instance tracking and semantic discovery. Text-promptable segmentation models, including the latest foundation models such as SAM 3, still suffer from temporal hallucinations, spatial fragmentation, and semantic misclassification: they fail to report target absence when an object leaves the field of view, segment local textures instead of the complete object during extreme close-ups, and prioritize visual features over ontological reality, so that visually similar artifacts such as statues, paintings, or reflections are segmented as target entities.
  ENEAS works two ways from a single method: precise tracking and high-quality segmentation of a unique instance, and open-concept discovery of every instance a text query names, resolved by a semantic verification layer. For tracking, we extend the geometrically robust SeC architecture, previously limited to point interactions, with a text-prompting adapter and leverage its temporal memory, so that the target is held through disappearance without drifting to distractors and kept whole even when it fills the entire view. For discovery, the verification layer combines high-speed visual embedding matching with conditional VLM refinement, invoking semantic reasoning only for ambiguous candidates, which filters out the ontological errors that visual-only models cannot distinguish while keeping latency low. Designed with 3D reconstruction in mind, where a single misclassified distractor corrupts the asset, ENEAS unlocks high-quality semantic tracking and segmentation of video, of broad libraries, and of collections of temporally or spatially unordered data, together with the discrimination to tell true instances from their doppelgangers: things that look alike but are not the same. The code and models are available at https://github.com/speridlabs/eneas

## 12. Modern Transformers Are Implicit Hybrids: From Functional Differentiation to Principled Hybrid Architecture Design

- Authors: Runlin Shi, Bojian Yin, Guoqi Li
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-02
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.0590257606233444
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.02986v1
- PDF: https://arxiv.org/pdf/2609.02986v1
- Local PDF: pdf/2026-09-05_12_Modern Transformers Are Implicit Hybrids_ From Functional Differentiation to Principled Hybrid Architecture Design.pdf

Hybrid architectures combining Full Attention (FA) and Linear Attention (LA) are increasingly prominent, yet their allocation remains heuristic. We seek an evidence-grounded basis in head-level functional organization learned by RoPE-based Transformers. Behavioral probes do not yield a complete taxonomy, so we propose two intervention metrics: RoPE Frequency Importance Score (RFIS), measuring how each frequency affects a head's attention distribution, and RoPE Positional Dependence (RPD), isolating dependence on rotary positional modulation. On Qwen3-series models and Llama3.1, RFIS suggests and RPD verifies a complete taxonomy of retrieval and positional heads separated by a salient mid-low-frequency band. Controlled Transformers show that this boundary follows the training-length positional scale; we term it the Global Positional Band (GPBand). The analysis suggests a potential cause of zero-shot length-extrapolation failure and yields two principles: positional modeling should operate only locally, with global access through position-independent retrieval; and both functions should be assigned at head granularity with layer-specific allocation. We instantiate them in Head-wise Hybrid Architecture (HwH), using NoPE FA for global retrieval and LA for local positional modeling. With an FA-to-LA ratio below 1:3, HwH retains strong language modeling and commonsense reasoning while improving retrieval and substantially strengthening zero-shot long-context extrapolation over Transformer, LA, and a layer-wise hybrid baseline. Ablations validate both principles and component roles, highlighting principled hybrid architecture design as a promising route toward future foundation models.

## 13. Privacy-Preserving Topology-Guided Safety for LLM-Based Multi-Agent Systems via Federated Graph Learning

- Authors: Jinxi Yu, Eric Hanchen Jiang, Levina Li, Dong Liu, Zhi Zhang, Wenxiao Zhao, Yanxuan Yu, Kai-Wei Chang, Ying Nian Wu
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-02
- DOI: Unavailable
- Categories: cs.CR, cs.AI, cs.LG, cs.MA
- Relevance: 3.0543405712446168
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.02967v1
- PDF: https://arxiv.org/pdf/2609.02967v1
- Local PDF: pdf/2026-09-05_13_Privacy-Preserving Topology-Guided Safety for LLM-Based Multi-Agent Systems via Federated Graph Learning.pdf

Topology-guided safeguards for LLM-based multi-agent systems (MAS) train a GNN over the inter-agent communication graph to localize risky agents and intervene on the topology---but they assume one operator can pool all labeled traces. Across organizations that assumption breaks: episodes contain private prompts, tool outputs, and proprietary workflows, and no silo alone sees the full attack distribution. We cast privacy-preserving MAS safeguarding as graph federated learning and instantiate FGLGuard: each operator fits an edge-featured graph attention detector on its own judge-labeled episode graphs and shares only model updates. The method couples a proximal local objective for non-IID clients, domain-balanced aggregation, over-refusal-constrained threshold calibration, corroborated upstream scoring, and a guarded rewrite for blocked answers. Federation is not optional: off-the-shelf transfer collapses under distribution shift (AUROC 0.51 to 0.70 only after in-domain retraining), so a deployable guard must adapt on each site's private traces. On Agent-SafetyBench, R-Judge, and AgentDojo, federated FGLGuard exceeds the in-domain centralized ceiling on all three benchmarks without pooling any data---where unsupervised anomaly guards and local-only training fail. One guard federated across four different-domain operators comes within 0.03 AUROC of multi-domain centralization, while any single-domain guard collapses on the others. Live FGLGuard cuts AgentDojo's ground-truth attack-success rate by 43% at near-unguarded utility, zero API cost, and negligible capability loss.

## 14. MemoryLACE: Memory Lifecycle-Aware Consolidation and Evidence Retrieval

- Authors: Meriem Yacoubi, Pia Schmidt, Nenad Petrovic, Ahmed Frikha, Martin Kirchhoff, Alois Knoll
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-02
- DOI: Unavailable
- Categories: cs.CL, cs.LG
- Relevance: 3.041658334889246
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.03201v1
- PDF: https://arxiv.org/pdf/2609.03201v1
- Local PDF: pdf/2026-09-05_14_MemoryLACE_ Memory Lifecycle-Aware Consolidation and Evidence Retrieval.pdf

Long-term LLM agents must preserve information across interactions while distinguishing repeated evidence, historical states, updates, and unresolved contradictions. Existing textual memory systems retrieve semantically relevant memories efficiently but often leave these relationships implicit, whereas richer structured approaches model them through global graphs, hierarchical abstractions, or reflection at greater complexity. We introduce MemoryLACE (MemLACE), a lightweight memory framework that explicitly models the lifecycle of textual evidence through sparse merge, supersession, and contradiction relations while preserving atomic natural-language memories and their provenance. Rather than retrieving memories independently, MemLACE reconstructs relation-aware evidence units that expose current, historical, supporting, and conflicting evidence for downstream reasoning. Across BEAM and StructMemEval, using open-weight and proprietary LLM backbones, MemLACE achieves the highest overall performance in same-backbone comparisons while reducing end-to-end runtime on BEAM by 66.6% relative to Hindsight, the strongest reported reflective-memory baseline. Ablation studies identify lifecycle expansion and temporal awareness as the principal contributors to these gains. Together, the results demonstrate that explicitly modeling the local lifecycle of textual evidence is sufficient to substantially improve long-term memory reasoning without requiring comprehensive knowledge graphs or global reflection.

## 15. DE-Venus: A Data-Efficient RLVR Framework for Large Language Models

- Authors: Shenzhi Yang, Guangcheng Zhu, Kai Tang, Zhengqing Zang, Xing Zheng, Haobo Wang, Yingfan Ma, Bowen Song, Bo Han, Bo An, Lei Feng, Weiqiang Wang, Junbo Zhao, Gang Chen
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-03
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.0396366426011125
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.03324v1
- PDF: https://arxiv.org/pdf/2609.03324v1
- Local PDF: pdf/2026-09-05_15_DE-Venus_ A Data-Efficient RLVR Framework for Large Language Models.pdf

Reinforcement learning with verifiable rewards (RLVR) improves large language model reasoning, but its practical scaling is constrained by expensive on-policy rollouts and the cost of obtaining reliable targets at scale. Existing methods address sample selection, incomplete supervision, or noisy labels separately, often entangling supervision logic with distributed training and hindering controlled comparison and reuse. We present DE-Venus, a unified framework for data-efficient RLVR that treats supervision as evolving state across data preparation and policy optimization. It organizes this lifecycle into three modules: Active Data Selection allocates training and annotation budgets; Weak Supervision Construction derives learning signals from unlabeled examples; and Training-Time Supervision Refinement filters or corrects unreliable supervision. DE-Venus supports seven representative methods and a data-selection pipeline by expressing method-specific decisions as offline dataset transitions or online transformations of targets, rewards, batches, and advantages while preserving verl's distributed execution contracts. Across public benchmarks and three business scenarios, separate configurations preserve or improve model quality with only 10% of labels or as little as 13% of relevant data; selected business configurations also reduce observed convergence steps by 63%--75%. DE-Venus thus reduces annotation and training costs without sacrificing scalable RL execution.

## 16. Semantic Bayesian World Models

- Authors: Tommaso Soru
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-03
- DOI: Unavailable
- Categories: cs.AI, cs.DB, cs.LG
- Relevance: 3.0334397840408442
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.03834v1
- PDF: https://arxiv.org/pdf/2609.03834v1
- Local PDF: pdf/2026-09-05_16_Semantic Bayesian World Models.pdf

Knowledge graphs describe reality in crisp assertions, while the systems now consuming them, foundation models and autonomous agents, reason natively in probabilities. We argue that this mismatch is why the integration of language models and knowledge graphs remains a data-feeding pipeline rather than a unified reasoning architecture. We envision Semantic Bayesian World Models (SBWMs): a Web that describes the world not as a database of facts but as a shared, evolving fabric of beliefs over knowledge graphs, where ontological axioms constrain priors, observations update beliefs by Bayesian conditioning, and actions intervene upon the world. We work through what an agent gains from such a model: a home-security agent deciding whether the figure at the gate is a courier or a burglar, an actuarial estimate aggregated by entailment rather than by string frequency, a planning task that language models reliably fail, and the estimation of quantities that no document has ever stated. We then set out what the community must build to make them possible: belief annotation over RDF~1.2, probabilistic entailment regimes, semantic calibration layers, and protocols by which agents that have never met can exchange, and disagree over, calibrated beliefs.

## 17. Weighted sliced inverse regression for scalable supervised dimensionality reduction of spatial transcriptomics data

- Authors: Maximilian Woollard, Pratibha Panwar, Luke Harland, Jeremy Mo, Hanyun Zhang, Alexander Swarbrick, Berthold Göttgens, Shila Ghazanfar, Linh Nghiem
- Source: openalex
- Venue type: journal
- Journal: Nature Communications
- Publication status: published
- Publication date: 2026-09-03
- DOI: https://doi.org/10.1038/s41467-026-76871-z
- Categories: Single-cell and spatial transcriptomics, Gene expression and cancer classification
- Relevance: 3.0304182161864155
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://doi.org/10.1038/s41467-026-76871-z
- PDF: Unavailable
- Local PDF: Not downloaded

Abstract With the dramatic take-up of spatially resolved transcriptomics biotechnologies, performing spatially-aware analysis of the resulting data is crucial to maximise advances in biological understanding. Dimensionality reduction is a first step in almost any analysis of spatial transcriptomics data, regardless of whether the data is collected at the single-cell or spot level. While common approaches, such as principal component analysis, aim to identify low-dimensional scores that preserve total variances of gene expression features, such variances do not usually correspond to biologically relevant spatial variation. To this end, we have developed weighted sliced inverse regression (wSIR), a sufficient dimension reduction technique that performs dimensionality reduction and retains as much predictive power of the spatial coordinates as possible. As a linear dimensionality reduction approach, wSIR is applicable to multiple distinct spatial transcriptomic datasets, and is extremely scalable due to the algorithm and our Rcpp implementation, with over 100, 000 cells processed in under 2 minutes on a standard laptop. The feature loadings are interpretable, and new non-spatial data can be projected into the wSIR low-dimensional space for further downstream analyses. We examine wSIR’s performance through benchmarking and demonstrate its capability of biological discovery through two case studies in breast cancer and early embryonic development.

## 18. Federated Causal Discovery via Regression-Directed Cumulants

- Authors: Pablo Torrijos, Fabio Stella, José A. Gámez, José M. Puerta
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-03
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.011244604792531
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.03705v1
- PDF: https://arxiv.org/pdf/2609.03705v1
- Local PDF: pdf/2026-09-05_18_Federated Causal Discovery via Regression-Directed Cumulants.pdf

In this paper we study linear non-Gaussian acyclic models (LiNGAM) when used in federated environments. These causal models allow one to go beyond Markov equivalence. However, in many domains data are scarce, and increasing the sample size by centralising data from different clients is not advisable due to regulations such as the GDPR. The federated environment offers an attractive option to balance privacy and causal discovery accuracy. Unfortunately, the standard centralised estimator in the LiNGAM setting, i.e., DirectLiNGAM, cannot be straightforwardly federated. Higher-order cumulant tensors offer a way around this obstacle: they depend only on the joint distribution of the variables involved and add exactly across independent sample groups, so a single communication round suffices in horizontal, vertical, and hybrid partitions.
  However, FedISHC, i.e., the current federated method along these lines, breaks down under near-symmetric noise. To overcome the above limitation, we introduce the FedRCD family of causal discovery algorithms, and investigate three variants that trade off communication rounds against algebraic noise; two of them are exact federated counterparts of the centralised high-order cumulant (HC) and HC-LiNGAM algorithms, and the single-round variants further effectively support exact unlearning at any granularity, from a single observation to a whole client. Numerical experiments show that at sample sizes typical of real deployments, the entire cumulant-based federated family does not actually rank variables by the population asymmetry that the scores encode at zero. It ranks them by a variance ladder induced by the DAG along its directed paths, the cumulant counterpart of varsortability. Marginal standardisation collapses every cumulant method to near-random ordering, while scale-invariant DirectLiNGAM, not federable under this protocol, is unaffected.

## 19. TAP-Path: Task-Adaptive Structural and Token Pruning for Efficient and Trustworthy Pathology Foundation Models

- Authors: Mehedi Hasan, Ashfak Yeafi, Md Khairul Islam
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-03
- DOI: Unavailable
- Categories: cs.CV, cs.AI
- Relevance: 2.989631155869369
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.04071v1
- PDF: https://arxiv.org/pdf/2609.04071v1
- Local PDF: pdf/2026-09-05_19_TAP-Path_ Task-Adaptive Structural and Token Pruning for Efficient and Trustworthy Pathology Foundation Models.pdf

Pathology foundation models improve transferable representation learning for histopathology, but recent gains often rely on encoders with hundreds of millions of parameters and high inference cost. We propose TAP-Path, a task-adaptive compression framework that directly restructures a pretrained Virchow2 encoder rather than distilling it into a separate student. TAP-Path combines validation-driven transformer-block selection, physical removal of redundant blocks, input-adaptive patch-token pruning, multi-depth feature recovery, and a lightweight gated task head. The final model retains 24 of 32 transformer blocks and 70% of patch tokens after pruning, reducing encoder parameters by 24.96% (631.24M to 473.70M) and analytical encoder compute by 35.20% (340.13G to 220.40G FLOPs). Across three task-head optimization seeds, TAP-Path achieved $87.98 \pm 0.067%$ test accuracy, $81.26 \pm 0.49%$ balanced accuracy, and $82.38 \pm 0.48%$ macro-F1 on a 32-class histopathology benchmark, compared with 86.89% for full Virchow2 and 87.67% for UNI2-h. TAP-Path achieved a Brier score of $0.1800 \pm 0.0005$ and failure-detection AUROC of $0.9047 \pm 0.0060$. A validation-only rare-aware objective improved rare-class balanced accuracy in a secondary operating analysis. Frozen external evaluation on 433 CPTAC samples yielded $91.22 \pm 0.83%$ accuracy and $91.10 \pm 0.81%$ balanced accuracy. These results show that task-adaptive structural and token sparsification can improve the accuracy-efficiency trade-off of large pathology foundation models while preserving reliability under internal and external evaluation.

## 20. Knowledge Acquisition During Pre-training? Large Language Models Learn Better With Auxiliary Views

- Authors: Joseph Lee, Yidi Huang, Dokyoon Kim, Shu Yang, Li Shen
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-03
- DOI: Unavailable
- Categories: cs.CL, cs.AI
- Relevance: 2.9329203333561127
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.04180v1
- PDF: https://arxiv.org/pdf/2609.04180v1
- Local PDF: pdf/2026-09-05_20_Knowledge Acquisition During Pre-training_ Large Language Models Learn Better With Auxiliary Views.pdf

Gaps remain in our understanding of how large language models (LLMs) acquire knowledge during pre-training. We posit that auxiliary views, reformulations of knowledge, are causally helpful for learning. We design controlled experiments to isolate this. First, we confirm that repetition is necessary for acquisition and clarify that paraphrasing helps only at smaller batch sizes. Second, holding the token budget fixed, allocating tokens from document repetition to auxiliary views improves learning, counterintuitively, even for factual recall. Third, the effectiveness of auxiliary views is not contingent on the strength of the teacher model that generates them. Fourth, we identify forms of knowledge, contextual and foundational, that aid learning in the presence of prior knowledge gaps. Finally, we examine how these effects manifest mechanistically via layer-wise biases and compression. Together, our findings suggest that auxiliary representations of knowledge, which arise naturally in large pre-training corpora, are a key factor in the success of pre-training and offer a plausible explanation for why data diversity matters.

## 21. EraseSAE: Surgical Concept Erasure in Text-to-Video Diffusion Models via Sparse Autoencoders

- Authors: Xinghao Wang, Dong Li, Wei Yu, Yingwei Pan, Tao Gong, Qi Chu, Nenghai Yu, Ting Yao
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-03
- DOI: Unavailable
- Categories: cs.CV, cs.AI
- Relevance: 2.9126525091320548
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.03629v1
- PDF: https://arxiv.org/pdf/2609.03629v1
- Local PDF: pdf/2026-09-05_21_EraseSAE_ Surgical Concept Erasure in Text-to-Video Diffusion Models via Sparse Autoencoders.pdf

Recent advances in text-to-video (T2V) diffusion models have demonstrated remarkable generative capabilities, yet their reliance on loosely curated training data raises pressing safety and copyright concerns. Concept erasure offers a principled remedy by removing unwanted semantics from pretrained models while preserving remaining concepts. However, existing approaches typically operate at a coarse granularity misaligned with the fine-grained, distributed nature of concept representations, leading to incomplete removal or degraded generation quality. We argue that surgical erasure fundamentally requires intervention at the level of monosemantic features, where each unit encodes a single interpretable concept. To this end, we propose EraseSAE, a novel framework that leverages sparse autoencoders to achieve surgical concept erasure in DiT-based T2V diffusion models via a principled decompose-attribute-erase pipeline. We first introduce the Partitioned Convolutional Sparse Autoencoder, which decomposes dense spatiotemporal activations into disentangled, interpretable sparse features while preserving spatiotemporal coherence. A contrastive attribution mechanism then contrasts activations from paired prompts to isolate concept-specific feature kernels. At inference, timestep-resolved spatiotemporal masks derived from the identified kernels confine erasure to regions where the target concept is active, leaving unrelated content intact. Extensive experiments across diverse diffusion models and concept erasure tasks demonstrate that EraseSAE achieves precise and robust concept removal with minimal quality degradation, substantially outperforming state-of-the-art methods. The code is available at https://github.com/HiDream-ai/EraseSAE.

## 22. Bioinfoysis Technical Report

- Authors: Qingyang Shao, Xin Zhang, Zhouyang Yuan, Xianying Chen, Yujia Xiang, Zihao Yang, Tong Ye, Yangqi Zhang, Jiakang Xu, Xiaoqing Yan, Xuan Luo, Keyi Li, Enci Fan, Kai Kang, Zhuohan Liu, Xingyu Jin, Chunran Teng, Tao Li, Xinyu Lv, Minghui Wang, Wenfeng Li, Yidan Gao, Siyu Liu, Mingrui Luo, Zhu Liang, Guanren Qiao, Zhiping Xu
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-03
- DOI: Unavailable
- Categories: cs.AI, cs.MA
- Relevance: 2.9002499416174263
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.03871v1
- PDF: https://arxiv.org/pdf/2609.03871v1
- Local PDF: pdf/2026-09-05_22_Bioinfoysis Technical Report.pdf

Large language model agents have shown promise in bioinformatics, but most existing systems focus primarily on producing final answers, treating planning, tool use, and code execution as transient interactions. This design is poorly suited to long-horizon bioinformatics tasks, where conclusions must remain connected to the data, computations, and intermediate evidence that support them. We introduce \textbf{Bioinfoysis}, a multi-agent harness that represents each request as a persistent, artifact-grounded analysis run. Bioinfoysis combines global planning with step-wise, evidence-driven replanning: the planner maintains an executable checklist and revises pending steps using structured handoffs returned after each worker execution. These handoffs bind intermediate results to their responsible agent, checklist step, and plan generation, preventing stale evidence from being silently reused after replanning. A controlled runtime validates generated scripts, tables, and figures before they are used in downstream analysis or reporting, while role-specific context, persistent memory, and governed bioinformatics skills support reliable execution over long analysis trajectories. We evaluate Bioinfoysis on BixBench and two question-answering tracks of LAB-Bench 2. On BixBench, Bioinfoysis achieves state-of-the-art accuracy of 82.4\%. Across four underlying language models, Bioinfoysis increases average accuracy from 27.81\% to 64.13\% on SeqQA2 and from 3.13\% to 31.25\% on DbQA2. These results demonstrate that reliable bioinformatics automation depends not only on model capability, but also on the harness that governs planning, execution, memory, and evidence flow. We hope that the emergence of Bioinfoysis will play a driving and leading role in the development of the bioinformatics community. Our demo website can be seen in https://report.bioinfoysis.com/.

## 23. LLaDA-Image: Building Strong Image Generators with Fully Open Training Recipes

- Authors: Chuyan Chen, Haoxing Chen, Kun Chen, Zhenglin Cheng, Long Cui, Ruishan Fang, Zhangxuan Gu, Zhicheng Huang, Zhenzhong Lan, Yuanting Lei, Haoquan Li, Jianguo Li, Rongchuan Li, Sidu Li, Tao Lin, Deyuan Liu, Jiacheng Liu, Lin Liu, Yuxuan Lou, Zhisheng Lu, Yuxin Ma, Shuheng Shen, Peng Sun, Chaoyang Wang, Hongjun Wang, Xiaomei Wang, Yongxin Wang, Chengzhang Wu, Hongru Wu, Jun Xie
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-03
- DOI: Unavailable
- Categories: cs.CV, cs.AI
- Relevance: 2.8987154462312836
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.03796v1
- PDF: https://arxiv.org/pdf/2609.03796v1
- Local PDF: pdf/2026-09-05_23_LLaDA-Image_ Building Strong Image Generators with Fully Open Training Recipes.pdf

We introduce LLaDA-Image, a unified framework that pairs a 6B Diffusion Transformer (DiT) trained from scratch with a frozen vision-language understanding module built on the LLaDA2.0-Mini diffusion language model backbone. Instead of relying heavily on paired image-text data from the beginning, we first build a strong visual generative prior through image-only pre-training and mid-training. The generation pipeline comprises 220M samples, 98 of which are real images. For efficient and scalable optimization, we use parameter-free RMSNorm throughout the DiT together with the Muon optimizer. The resulting unified model produces highly photorealistic images while accurately following fine-grained editing instructions. We further distill LLaDA-Image into LLaDA-Image-Turbo, enabling fast inference in 2-4 sampling steps. On Qwen-Image-Bench, LLaDA-Image achieves overall scores of 53.53 and 53.38 on the English and Chinese tracks, respectively, setting a new state-of-the-art among open-source models on both tracks. To support further research on capable and efficient generative models, we release our model weights, training code, and detailed recipes.

## 24. TIGPO: Temporal Instance-Graph Policy Optimization for Long-Horizon LLM Agents

- Authors: Jinwei Gan
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-03
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 2.8585018744354733
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.03383v1
- PDF: https://arxiv.org/pdf/2609.03383v1
- Local PDF: pdf/2026-09-05_24_TIGPO_ Temporal Instance-Graph Policy Optimization for Long-Horizon LLM Agents.pdf

Graph-based policy optimization improves credit assignment for long-horizon LLM agents by organizing rollout trajectories into state-transition graphs. However, existing methods construct graphs independently within each policy update, discarding transitions discovered by earlier policies and limiting advantage estimation to small, batch-local rollout groups. We propose \emph{Temporal Instance-Graph Policy Optimization} (TIGPO), which extends graph-based credit assignment across policy updates. TIGPO maintains a persistent transition graph for each task, allowing valid transitions discovered by different policy versions to jointly determine credit for current rollouts. To actively reconnect current exploration with historical experience, TIGPO allocates a fixed rollout budget between Exploration slots for ordinary task sampling and Revisit slots for delayed reattempts of previously explored tasks. For each revisit, TIGPO pairs the current rollout group with its corresponding earlier Exploration group to construct a cross-temporal reference. The enlarged reference is designed to stabilize relative advantage estimation under small rollout groups, while comparison on the same task directly captures policy improvement across training stages. Historical transitions and scores serve only as structural and detached statistical references and are never replayed in the policy loss. Experiments on ALFWorld and WebShop demonstrate that TIGPO consistently outperforms prior group-based and graph-based policy optimization methods.

## 25. STAIR (STructure Aware Information Retriever): A novel dataset and LLM based retriever for document structure augmentation

- Authors: Vineet Kumar, Meghanadh Pulivarthi, vishwajeet kumar, Jaydeep Sen, Riyaz Ahmad Bhat, Sachindra Joshi
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-03
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 2.8354565065746296
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.03874v1
- PDF: https://arxiv.org/pdf/2609.03874v1
- Local PDF: pdf/2026-09-05_25_STAIR (STructure Aware Information Retriever)_ A novel dataset and LLM based retriever for document structure augmentati.pdf

Retrieval Augmented Generation (RAG) is a key component for generating accurate and hallucination free answers using Large Language Models (LLMs). LLMs are improving at handling long context, but still suffer from "lost in the middle" problem. Thus, precise and accurate retrieval is important. Current retrievers chunk long context into length-based manageable chunks - in the process throwing away rich and informative semantic global structure in the corpus. We introduce a novel retrieval system STAIR that empowers an LLM to exploit global structure in a corpus such as a Table of Contents (ToC) to efficiently store and retrieve information from its model parameters. Our thorough and careful ablation studies with a finetuned Differentiable Search Index (DSI) system show that ToC helps build a low hallucination (less than 0.05%) generative Information Retrieval (IR) system and can generalize to examples where very few training samples are available. To further research in this novel direction of ToC based retrieval we release SearchTome - a diverse benchmark created from 18 books across 6 diverse domains to further research in this novel direction. STAIR achieves a high Recall@1 score of 82.6% on SearchTome as compared to DSI (76.9%), where the difference is found to be statistically significant. STAIR easily beats other strong baselines such as BM25 (59.5%), DPR (68.7%) and out-of-the-box Mistral (13.8%).

## 26. Beyond Straightness: Non-Crossing Flow Matching via Quantile AlignTree Coupling

- Authors: Junyi Lin, Mengyu Li, Jingxuan Hu, Kejun He, Cheng Meng
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-03
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 2.8259050260101226
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.03443v1
- PDF: https://arxiv.org/pdf/2609.03443v1
- Local PDF: pdf/2026-09-05_26_Beyond Straightness_ Non-Crossing Flow Matching via Quantile AlignTree Coupling.pdf

The performance of Flow Matching largely depends on the quality of the coupling between the source and target distributions. However, independent coupling often leads to path crossings and local velocity ambiguity, while OT-based couplings typically incur high construction costs. To address this challenge, we propose Quantile AlignTree Flow Matching (QAT-FM), an efficient structured coupling strategy that constructs a hierarchical coupling between a Gaussian prior and the target data distribution via a quantile-aligned tree structure. QAT-FM constructs the coupling in $\mathcal{O}(Nd\log N)$ time and supports per-pair source sampling with $\mathcal{O}(d)$ complexity, enabling scalable training for large-scale high-dimensional generative tasks. Theoretically, we prove that the QAT coupling satisfies marginal consistency, induces non-crossing linear interpolation paths, and consistently improves path separation at intermediate times compared with independent coupling, thereby alleviating local velocity ambiguity. QAT-FM further extends naturally to conditional generation, enabling structured conditional coupling while preserving global Gaussian alignment. Experiments across diverse benchmark datasets demonstrate that QAT-FM achieves competitive generative performance while substantially reducing coupling construction cost.

## 27. Gradients Know What Outcomes Don't: Unlocking Reinforcement Learning for LLM Reasoning with Gradient-Aligned Rewards

- Authors: Leqi Zheng, Jinbo Su, Fang Niu, Chaokun Wang, Weiping Wang, Jiajun Zhang, Shannan Yan, Jie Wu, Zhaolu Kang, Rong Fu, Hang Zhang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-03
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 2.823730572986542
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.03342v1
- PDF: https://arxiv.org/pdf/2609.03342v1
- Local PDF: pdf/2026-09-05_27_Gradients Know What Outcomes Don't_ Unlocking Reinforcement Learning for LLM Reasoning with Gradient-Aligned Rewards.pdf

Reinforcement learning from verifiable rewards (RLVR) drives chain-of-thought reasoning in large language models, yet its binary outcome reward cannot distinguish among correct trajectories. Existing dense reward alternatives, from surface heuristics to process reward models, either ignore the expert solutions already present in training corpora or require expensive offline annotation. We propose Gradient-Aligned Reward (GAR), which operates in the policy's own gradient space: truncated backpropagation through the output projection layer extracts a compact gradient vector for each rollout, and cosine similarity with an expert-anchor gradient yields a dense, reasoning-aware reward with less than 9% wall-clock overhead. We prove that this cosine admits a multiplicative decomposition into prediction-error and activation-pattern factors, providing a concrete characterization of what the alignment signal measures. On Qwen3-4B and Qwen3-8B, GAR consistently improves over GRPO and other baselines on competition-level math benchmarks and transfers to GPQA Diamond and MMLU-Pro without domain-specific data. Code and data are available at https://github.com/LQgdwind/GAR.

## 28. Unlocking Lossless Speedups in LLMs via Discrete Diffusion

- Authors: Subham Sekhar Sahoo, Lingjie Chen, Khiem Pham, Jonathan Geuter, Chaitanya Dwivedi, Varad Pimpalkhute, Yash Akhauri, Alexander Moreno, Mikhail Yurochkin, Zhenting Wang, Mostafa Elhoushi, Nolan Dey, Shane Bergsma, Joel Hestness, John Thickstun, Eric Xing, Zhengzhong Liu
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-03
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 2.808613961617088
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.04010v1
- PDF: https://arxiv.org/pdf/2609.04010v1
- Local PDF: pdf/2026-09-05_28_Unlocking Lossless Speedups in LLMs via Discrete Diffusion.pdf

Large Language Models (LLMs) owe much of their success to next-token prediction (NTP), but their autoregressive (AR) structure requires slow, sequential token generation. To overcome this bottleneck, we introduce diffusion-augmented LLMs, a new class of models that defines an AR model distribution while using diffusion to draw multiple tokens in parallel from that distribution. We decouple the parameters of these models into two sets: AR weights, trained using the standard NTP objective, and lightweight diffusion weights, trained to generate multiple tokens simultaneously. The diffusion weights are learned through a simple Diffusion Distillation phase that adds negligible overhead to existing LLM training pipelines. We also introduce $Ψ$-Spec, a family of samplers that enables lossless acceleration and inference-time scaling at a fixed context length. Unlike speculative decoding, our method requires no separate draft model. Unlike diffusion LLMs (d-LLMs), it accelerates generation without sacrificing the quality of the underlying AR model. The resulting models, called Uno, can be trained from scratch or built by augmenting existing open-weight AR LLMs. Uno achieves higher throughput than leading speculative-decoding methods at every evaluated batch size and delivers up to $3\times$ speedups over the base AR model, including at the largest batch size supported by the device. Notably, our 8B Uno model outperforms the leading open d-LLM, the 26B DiffusionGemma, and the proprietary Mercury 2 across all evaluated benchmarks in agentic tool use, coding, and long-context reasoning. We release code and checkpoints at: https://s-sahoo.github.io/uno/

## 29. Guide, Not Bind: Why Defeasible Priors Fail in Augmented Lagrangian Causal Discovery

- Authors: Sairam Sundararaman, Sara Girdhar, Manit Narasimha Murthy, Samrudh N, Bhaskarjyoti Das
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-03
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 2.791693742322906
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.03442v1
- PDF: https://arxiv.org/pdf/2609.03442v1
- Local PDF: pdf/2026-09-05_29_Guide, Not Bind_ Why Defeasible Priors Fail in Augmented Lagrangian Causal Discovery.pdf

Differentiable causal discovery methods increasingly encode expert priors as forbidden-edge constraints enforced by an Augmented Lagrangian (ALM) penalty, on the assumption that a data-adaptive relaxation mechanism will discount and eventually override a rule the data consistently contradicts. We show this design, which we call \emph{guide, not bind}, fails for two independent, precisely characterized reasons, and that directly repairing both restores it only partially. First, sequential penalty-ramping ALM suppresses a wrongly-forbidden true edge before any counterfactual check can detect it: we give three necessary conditions any adaptive relaxation must satisfy to avoid this (Proposition~\ref{prop:conditions}), prove that DADU---the natural relaxation rule this paper introduces as the object of study---violates all three (Corollary~\ref{cor:dadu_failure}), and confirm the failure across 3{,}072 training runs spanning graphs from 4 to 32 nodes, where a single wrong prior suppresses a true edge in 87--97\% of trials under DADU. Second, and independent of any fix to the mechanism, we prove in closed form that the standard correlation-matching objective ties a true edge and its reverse to an identical cost of exactly $2r^2$ (Lemma~\ref{lem:tie}), not because the underlying equal-variance model is unidentifiable, but because normalizing to correlation discards exactly the variance information that would make it identifiable; covariance matching instead separates the two directions by a provable margin of at least $w_0^4$ (Lemma~\ref{lem:separation}).

## 30. High-Dimensional Learning Dynamics of Attention-Indexed Models

- Authors: Yizhou Xu, Margarita Sagitova, Lenka Zdeborová, Florent Krzakala
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-03
- DOI: Unavailable
- Categories: cs.LG, stat.ML
- Relevance: 2.7795037119458925
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.03858v1
- PDF: https://arxiv.org/pdf/2609.03858v1
- Local PDF: pdf/2026-09-05_30_High-Dimensional Learning Dynamics of Attention-Indexed Models.pdf

Attention mechanisms are central to modern foundation models, yet their training dynamics remain poorly understood, especially when the attention matrices have extensive rank. In this work, we study attention-indexed models, a broad framework that can represent multi-layer and multi-head attention architectures. First, we show that, in a suitable high-dimensional limit, the population-loss landscape is characterized by a finite set of trace order parameters. In contrast, online stochastic gradient descent (SGD) is governed by an infinite hierarchy of matrix moments, which we show can be exponentially well-approximated by a finite truncated system. Second, this framework reveals that attention parameterization itself can act as an architectural implicit bias. Direct optimization of an attention matrix $S\in\mathbb{R}^{d\times d}$ can remain trapped in an uninformative state. Tied attention ($S=WW^\top$) induces an automatic symmetry-breaking mechanism and yields weak recovery in $Θ(d^2\log d)$ samples. For untied attention, $S=UV^\top$, we uncover a fast-slow mechanism: the pre-activation mean first evolves on a fast timescale, while the overlaps evolve on a slower one. Weak recovery on the $Θ(d^2\log d)$ scale occurs when the state selected by the fast dynamics breaks the initial symmetry.

## 31. Spatial isoform sequencing at single-cell resolution reveals cell-type-specific spatial isoform variability in multiple brain cell types

- Authors: Lieke Michielsen, Andrey D. Prjibelski, Careen Foord, Yelizaveta Spiegelman, Taewoo Kim, Wen Hu, Julien Jarroux, Justine Hsu, Rebecca Pfeil, Xinyi Zhang, Li Gan, Alexandru I. Tomescu, Iman Hajirasouliha, Hagen Tilgner
- Source: openalex
- Venue type: journal
- Journal: Nature Methods
- Publication status: published
- Publication date: 2026-09-01
- DOI: https://doi.org/10.1038/s41592-026-03211-w
- Categories: Single-cell and spatial transcriptomics, Neurogenesis and neuroplasticity mechanisms, Neuroinflammation and Neurodegeneration Mechanisms
- Relevance: 3.013372478203224
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://doi.org/10.1038/s41592-026-03211-w
- PDF: Unavailable
- Local PDF: Not downloaded

Abstract Spatial long-read technologies are increasingly common but usually lack single-cell resolution. This leaves unanswered whether spatially variable isoforms reflect variability within one cell type or differences in region-specific cell-type composition. Here, we developed Spl-ISO-Seq2 (500-nm resolution) and accompanying software, Spl-IsoQuant-2 and Spl-IsoFind, enabling long-read sequencing of >450 million barcodes versus 80,000 previously. Applying this to the adult mouse brain, we compared differential isoform abundance between known regions and spatial isoform patterns independent of predefined regions. Both identified overlapping hits, for example, Rps24 in oligodendrocytes. For known Snap25 spatial isoform variation, we show that it occurs in excitatory neurons. The region-agnostic approach also uncovered patterns missed by region-based comparisons, for example, for Ighm . Notably, many spatial isoform signals are not driven by cell-type composition alone. Finally, our software is applicable to many spatial and single-cell protocols, demonstrating reproducibility between platforms (for example, Visium HD/Stereo-seq). Overall, our experimental/analytical methods enable a submicron-resolution-isoform view and open avenues for spatial isoform disease research.

## 32. An in silico transcription factor perturbation simulator uncovers diverse genetic architectures of brain disorders

- Authors: Haiyang Wang, Qingyu Li, Ying Zhu
- Source: openalex
- Venue type: journal
- Journal: Genome Medicine
- Publication status: published
- Publication date: 2026-09-04
- DOI: https://doi.org/10.1186/s13073-026-01752-5
- Categories: Single-cell and spatial transcriptomics, Genomics and Chromatin Dynamics, Genetic Associations and Epidemiology
- Relevance: 2.7422608821302297
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://doi.org/10.1186/s13073-026-01752-5
- PDF: Unavailable
- Local PDF: Not downloaded

Determining mechanisms and developing treatments for brain disorders with complex genetic architectures remains a challenge. We developed TFdisc, an in silico transcription factor (TF) perturbation simulator that uses wild-type single-cell RNA sequencing data to emulate corresponding post-TF perturbations. TFdisc’s accuracy in reconstructing gene regulatory networks, identifying differentially expressed genes, and predicting alterations in cell identity and lineage differentiation post-TF perturbations was validated across multiple perturbation datasets.Applying TFdisc to brain disorder risk factors revealed distinct molecular and cellular mechanisms. Further simulation of multiple TF simultaneous perturbations uncovered a “jigsaw mechanism” for schizophrenia and a “monolithic mechanism” for autism spectrum disorder.

## 33. Language Models Struggle to Use Representations Learned In-Context

- Authors: Michael A. Lepori, Tal Linzen, Ann Yuan, Katja Filippova
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.742187345559194
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.676/
- PDF: https://aclanthology.org/2026.acl-long.676.pdf
- Local PDF: pdf/2026-09-05_33_Language Models Struggle to Use Representations Learned In-Context.pdf

Though large language models (LLMs) have enabled great success across a wide variety of tasks, they still appear to fall short of one of the loftier goals of artificial intelligence research: creating an artificial system that can adapt its behavior to radically new contexts upon deployment. One important step towards this goal is to create systems that can induce rich representations of data that are seen in-context, and then flexibly deploy these representations to accomplish goals. Recently, Park et al. 2024 demonstrated that current LLMs are indeed capable of inducing such representation from context (i.e., in-context representation learning). The present study investigates whether LLMs can use these representations to complete simple downstream tasks.We first assess whether open-weights LLMs can use in-context representations for next-token prediction, and then probe models using a novel task, adaptive world modeling. In both tasks, we find evidence that open-weights LLMs struggle to deploy representations of novel semantics that are defined in-context, even if they encode these semantics in their latent representations. Furthermore, we assess closed-source, state-of-the-art reasoning models on the adaptive world modeling task, demonstrating that even the most performant LLMs cannot reliably leverage novel patterns presented in-context. Overall, this work seeks to inspire novel methods for encouraging models to not only encode information presented in-context, but to do so in a manner that supports flexible deployment of this information.

## 34. I²B-LPO: Latent Policy Optimization via Iterative Information Bottleneck

- Authors: Huilin Deng, Hongchen Luo, Yue Zhu, Long Li, Zhuoyue Chen, Xinghao Zhao, Ming LI, Chuyang Zhao, Jihai Zhang, MengChang Wang, Yang Cao, Yu Kang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.739040755778566
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1084/
- PDF: https://aclanthology.org/2026.acl-long.1084.pdf
- Local PDF: pdf/2026-09-05_34_I²B-LPO_ Latent Policy Optimization via Iterative Information Bottleneck.pdf

Despite recent advances in Reinforcement learning with verifiable rewards (RLVR) for large language model (LLM) reasoning, most methods suffer from exploration collapse, as the semantic homogeneity of random rollouts traps models in narrow, over-optimized behaviors. Existing methods leverage policy entropy to encourage exploration, but face inherent limitations: global entropy regularization is susceptible to reward hacking, inducing meaningless verbosity, whereas local token-selective updates struggle with the strong inductive bias of pre-trained models. To this end, we propose Latent Policy Optimization via Iterative Information Bottleneck ( I²B-LPO), which shifts from statistical perturbation of token distributions to topological branching of reasoning trajectories. I²BLPO triggers latent branching at high-entropy states to diversify reasoning trajectories and applies the Information Bottleneck as a trajectory filter and self-reward to ensure concise and informative exploration. Empirical results on four mathematical benchmarks demonstrate that I²B-LPO achieves state-of-the-art performance, with margins of up to 5.3% in accuracy and 7.4% in diversity metrics. Code is available at https://github.com/denghuilin-cyber/IIB-LPO .

## 35. Beyond Transcription: Unified Audio Schema for Perception-Aware AudioLLMs

- Authors: Linhao Zhang, Yuhan Song, Aiwei Liu, Chuhan Wu, Sijun Zhang, Wei Jia, Yuan Liu, Houfeng Wang, Zhou Xiao
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.73864352729774
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.967/
- PDF: https://aclanthology.org/2026.findings-acl.967.pdf
- Local PDF: pdf/2026-09-05_35_Beyond Transcription_ Unified Audio Schema for Perception-Aware AudioLLMs.pdf

Recent Audio Large Language Models (AudioLLMs) exhibit a striking performance inversion: while excelling at complex reasoning tasks, they consistently underperform on fine-grained acoustic perception. We attribute this gap to a fundamental limitation of ASR-centric training, which provides precise linguistic targets but implicitly teaches models to suppress paralinguistic cues and acoustic events as noise. To address this, we propose Unified Audio Schema (UAS), a holistic and structured supervision framework that organizes audio information into three explicit components—Transcription, Paralinguistics, and Non-linguistic Events—within a unified JSON format. This design achieves comprehensive acoustic coverage without sacrificing the tight audio-text alignment that enables reasoning. We validate the effectiveness of this supervision strategy by applying it to both discrete and continuous AudioLLM architectures. Extensive experiments on MMSU, MMAR, and MMAU demonstrate that UAS-Audio yields consistent improvements, boosting fine-grained perception by 10.9% on MMSU over the same-size state-of-the-art models while preserving robust reasoning capabilities. Our code and model are publicly available at https://github.com/Tencent/Unified_Audio_Schema .

## 36. BubbleRAG: Interactive Cognitive Offloading with Thought Bubble in Retrieval-Augmented Generation

- Authors: Fuda Ye, Jiachuan Wang, Yongqi Zhang, Lei Chen, Shuangyin Li
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.7376789740683116
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.2163/
- PDF: https://aclanthology.org/2026.findings-acl.2163.pdf
- Local PDF: pdf/2026-09-05_36_BubbleRAG_ Interactive Cognitive Offloading with Thought Bubble in Retrieval-Augmented Generation.pdf

Retrieval-augmented generation (RAG) extends the capabilities of large language models (LLMs) by providing access to external knowledge. However, traditional retrieval-augmented LLMs rely on a silent reading paradigm that processes all retrieved documents passively, forcing them to reason without any interaction with the documents. This paradigm contrasts sharply with human interactive reading behavior, where external tools, such as bookmarks and notes, are used to offload cognitive demands. This paper introduces BubbleRAG, an enhanced RAG framework that emulates human interactive reading through annotation and re-reading. Specifically, BubbleRAG utilizes a lightweight thought bubble module that offloads LLM’s internal cognition into external bookmark tokens, which are then annotated back into the context. These bookmarks serve as externalized memory, allowing the LLM to revisit these annotations in subsequent reading and answering. Notably, BubbleRAG is particularly suitable for low-resource scenarios, as the LLM parameters remain frozen. Extensive experiments confirm the effectiveness, robustness, and generalizability of BubbleRAG. Our findings demonstrate that BubbleRAG enables LLMs to achieve superior evidence identification abilities typically seen in retrievers, while establishing a cognitive link between external and internal information during answer generation. The source code is available at https://github.com/yefd/BubbleRAG .

## 37. TokenTiming: A Dynamic Alignment Method for Universal Speculative Decoding Model Pairs

- Authors: Sibo Xiao, Fu Jinyuan, Zhongle Xie, Lidan Shou
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.7368932405538575
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1983/
- PDF: https://aclanthology.org/2026.acl-long.1983.pdf
- Local PDF: pdf/2026-09-05_37_TokenTiming_ A Dynamic Alignment Method for Universal Speculative Decoding Model Pairs.pdf

Accelerating the inference of large language models (LLMs) has been a critical challenge in generative AI. Speculative decoding (SD) substantially improves LLM inference efficiency. However, its utility is limited by a fundamental constraint: the draft and target models must share the same vocabulary, thus limiting the herd of available draft models and often necessitating the training of a new model from scratch. Inspired by Dynamic Time Warping (DTW), a classic algorithm for aligning time series, we propose the algorithm TokenTiming for universal speculative decoding. It operates by re-encoding the draft token sequence to get a new target token sequence, and then uses DTW to build a mapping to transfer the probability distributions for speculative sampling. Benefiting from this, our method accommodates mismatched vocabularies and works with any off-the-shelf models without retraining and modification. We conduct comprehensive experiments on various tasks, demonstrating 1.57x speedup. This work enables a universal approach for draft model selection, making SD a more versatile and practical tool for LLM acceleration.

## 38. Temporal Evidence Chain for Temporal Knowledge Graph Question Answering with Large Language Models

- Authors: Shihao Liu, Xiaofei Zhou, Bo Wang, Geyuan Zhang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.7367159473798397
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1361/
- PDF: https://aclanthology.org/2026.acl-long.1361.pdf
- Local PDF: pdf/2026-09-05_38_Temporal Evidence Chain for Temporal Knowledge Graph Question Answering with Large Language Models.pdf

Temporal Knowledge Graph Question Answering (TKGQA) aims to answer temporal questions using knowledge from Temporal Knowledge Graphs (TKGs).Existing LLM-based TKGQA methods typically utilize RAG-based or Agent-based paradigms, yet both struggle to construct reliable temporal evidence chains. RAG-based approaches primarily rely on semantic retrieval to fetch question-relevant contexts but overlook the structural dependencies within TKGs, leading to broken evidence chains, whereas iterative agents are prone to error propagation during multi-step reasoning.To address these limitations, we propose TECQA, a framework designed to construct temporal evidence chains for LLM reasoning. Firstly, TECQA employs structure-guided subgraph retrieval to capture structural dependencies and intermediate reasoning paths. Subsequently, it utilizes a k-nearest temporal neighbor pruning strategy to filter irrelevant noise while strictly preserving the continuous local history surrounding critical events. Finally, the retained temporal neighbors are serialized by temporal proximity to explicitly reconstruct a coherent temporal evidence chain. Extensive experiments on MultiTQ and CronQuestions demonstrate that TECQA achieves state-of-the-art performance, outperforming strong baselines by 45.3% particularly on complex queries. Code is available at https://github.com/SimonsLiu/TECQA .

## 39. CARO: Chain-of-Analogy Reasoning Optimization for Robust Content Moderation

- Authors: Bingzhe Wu, Haotian Lu, Yuchen Mou
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.736492398796524
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1442/
- PDF: https://aclanthology.org/2026.findings-acl.1442.pdf
- Local PDF: pdf/2026-09-05_39_CARO_ Chain-of-Analogy Reasoning Optimization for Robust Content Moderation.pdf

Current large language models (LLMs), even those explicitly trained for reasoning, often struggle with ambiguous content moderation cases due to misleading “decision shortcuts” embedded in context. Inspired by cognitive psychology insights into expert moderation, we introduce CᴀʀO (Chain-of-Analogy Reasoning Optimization), a novel two-stage training framework to induce robust analogical reasoning in LLMs. First, CᴀʀO bootstraps analogical reasoning chains via retrieval-augmented generation (RAG) on moderation data and performs supervised fine-tuning (SFT). Second, we propose a customized direct preference optimization (DPO) approach to reinforce analogical reasoning behaviors explicitly. Unlike static retrieval methods, CᴀʀO dynamically generates tailored analogical references during inference, effectively mitigating harmful decision shortcuts. Extensive experiments demonstrate that CᴀʀO substantially outperforms state-of-the-art reasoning models (DeepSeek R1, QwQ), specialized moderation models (LLaMA Guard), and advanced fine-tuning and retrieval-augmented methods, achieving an average F1 score improvement of 24.9% on challenging ambiguous moderation benchmarks.

## 40. Mitigating Hallucinations in VLMs: Enhancing Visual Attention via Head-Wise Perturbation

- Authors: Zhenghua Wang, Yixin Wu, Feiran Zhang, Qi Qian, Changze Lv, Xuanjing Huang, Xiaoqing Zheng
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.736428988832333
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1016/
- PDF: https://aclanthology.org/2026.findings-acl.1016.pdf
- Local PDF: pdf/2026-09-05_40_Mitigating Hallucinations in VLMs_ Enhancing Visual Attention via Head-Wise Perturbation.pdf

Vision–Language Models (VLMs) have demonstrated strong capabilities in tasks that require joint understanding of text and images. However, as many VLMs are built upon pre-trained large language models, they often over-rely on linguistic priors at the expense of visual features, causing persistent hallucinations. We observe that these hallucinations stem not only from insufficient visual attention but also from imbalanced activation profiles across attention heads, while hallucinated samples tend to disproportionately activate heads that fail to capture visual cues. To promote a more balanced attention distribution, we propose HWP , a strategy that incorporates head-wise attention perturbation via continuous multiplicative noise, coupled with a visual-guided loss focused on vision-sensitive text tokens. Beyond simply strengthening visual grounding, this design encourages a broader set of attention heads to engage with visual signals, thereby alleviating information loss caused by activation concentration on a few dominant heads. Consistent gains across different architectures and scales on multiple benchmarks demonstrate the effectiveness and robustness of our approach in mitigating VLM hallucinations.

## 41. FIFA: Unified Faithfulness Evaluation Framework for Text-to-Video and Video-to-Text Generation

- Authors: Liqiang Jing, Viet Dac Lai, Seunghyun Yoon, Trung Bui, Xinya Du
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.7361061909229454
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.555/
- PDF: https://aclanthology.org/2026.findings-acl.555.pdf
- Local PDF: pdf/2026-09-05_41_FIFA_ Unified Faithfulness Evaluation Framework for Text-to-Video and Video-to-Text Generation.pdf

Video Multimodal Large Language Models (VideoMLLMs) have achieved remarkable progress in both Video-to-Text and Text-to-Video tasks. However, they often suffer from hallucinations, generating content that contradicts the visual input. Existing evaluation methods are limited to one task (V2T) and also fail to assess hallucinations in open-ended, free-form responses. To address this gap, we propose FIFA, a unified F a I th F ulness ev A luation framework that extracts comprehensive descriptive facts, models their semantic dependencies via a Spatio-Temporal Semantic Dependency Graph, and verifies them using VideoQA models. We further introduce , a tool-based correction framework that revises hallucinated content. Extensive experiments demonstrate that FIFA aligns more closely with human judgment than existing evaluation methods, and that effectively improves factual consistency in both text and video generation.

## 42. GRASPrune: Global Gating for Budgeted Structured Pruning of Large Language Models

- Authors: Ziyang Wang, Jiangfeng Xiao, Chuan Xiao, Ruoxiang LI, Rui Mao, Jianbin Qin
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.735492080321796
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.491/
- PDF: https://aclanthology.org/2026.acl-long.491.pdf
- Local PDF: pdf/2026-09-05_42_GRASPrune_ Global Gating for Budgeted Structured Pruning of Large Language Models.pdf

Large language models (LLMs) are expensive to serve because dense FFN blocks, multi-head attention, and KV caches dominate memory, making structured pruning a natural way to reduce serving costs under tight parameter and memory budgets. We present GRASPrune, a global budgeted structured pruning framework applied post-hoc to a pretrained model that jointly prunes FFN channels and attention KV head groups under a single global parameter budget. GRASPrune attaches lightweight learnable gates to prunable units and optimizes only these gates on a small unlabeled language-modeling calibration set, keeping all backbone weights frozen while enforcing the target sparsity at every step. A final budget-preserving scaling calibration reweights the surviving channels and heads to correct scale shifts introduced by pruning. On LLaMA-2-7B, GRASPrune removes 50% of parameters and achieves 12.18 perplexity on WikiText-2 while maintaining competitive average zero-shot accuracy on five downstream benchmarks, using a short calibration run of four epochs on 512 unlabeled sequences on a single NVIDIA A100 80GB GPU, all without any full-model fine-tuning.

## 43. Beyond Experience Retrieval: Learning to Generate Utility-Optimized Structured Experience for Frozen LLMs

- Authors: Xuancheng Li, Haitao Li, Yujia Zhou, Yiqun Liu, Qingyao Ai
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.7348834801572375
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1831/
- PDF: https://aclanthology.org/2026.acl-long.1831.pdf
- Local PDF: pdf/2026-09-05_43_Beyond Experience Retrieval_ Learning to Generate Utility-Optimized Structured Experience for Frozen LLMs.pdf

Large language models (LLMs) are largely static and often redo reasoning or repeat mistakes. Prior experience reuse typically relies on external retrieval, which is similarity-based, can introduce noise, and adds latency. We introduce SEAM ( S tructured E xperience A dapter M odule), a lightweight, executor-specific plug-in that stores experience in its parameters and generates a structured, instance-tailored experience entry in a single forward pass to guide a frozen LLM executor. SEAM is trained for utility via executor rollouts and GRPO while keeping the executor frozen, and can be further improved with logged-success SFT after deployment. Experiments on mathematical reasoning benchmarks show consistent accuracy gains across executors with low overhead. Extensive ablation and analysis further elucidate the mechanisms underlying SEAM’s effectiveness and robustness.

## 44. The Inner Monologue of Language Models: When Reasoning Traces Reveal More Than They Hide

- Authors: Pratham Singla, Shivank Garg, Ayush Singh, Ishan Garg, Ketan Suhaas Saichandran
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.734797605446877
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.2078/
- PDF: https://aclanthology.org/2026.findings-acl.2078.pdf
- Local PDF: pdf/2026-09-05_44_The Inner Monologue of Language Models_ When Reasoning Traces Reveal More Than They Hide.pdf

Recent advances in post-training techniques have endowed Large Language Models (LLMs) with enhanced capabilities for tackling complex, logic-intensive tasks through the generation of supplementary planning tokens. This development raises a fundamental question – Are these models aware of what they "learn” and "think”? To address this, we define three core competencies: (1) awareness of learned latent policies, (2) generalization of these policies across domains, and (3) alignment between internal reasoning traces and final outputs. We empirically evaluate these abilities on several tasks, each designed to require learning a distinct policy. Furthermore, we contrast the profiles of models post-trained via Supervised Fine-Tuning (SFT), Direct Policy Optimization (DPO), and Group Relative Policy Optimization (GRPO). Our findings indicate that RL-trained models not only demonstrate greater awareness of their learned behaviors and stronger generalizability to novel, structurally similar tasks than SFT models but also often exhibit weak alignment between their reasoning traces and final outputs, an effect most pronounced in GRPO-trained models.

## 45. SPAGBias: Uncovering and Tracing Structured Spatial Gender Bias in Large Language Models

- Authors: Binxian Su, Haoye Lou, Shucheng Zhu, Weikang Wang, Ying Liu, Dong Yu, Pengyuan Liu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.734405956257074
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.55/
- PDF: https://aclanthology.org/2026.acl-long.55.pdf
- Local PDF: pdf/2026-09-05_45_SPAGBias_ Uncovering and Tracing Structured Spatial Gender Bias in Large Language Models.pdf

Large language models (LLMs) are being increasingly used in urban planning, but since gendered space theory highlights how gender hierarchies are embedded in spatial organization, there is concern that LLMs may reproduce or amplify such biases. We introduce SPAGBias — the first systematic framework to evaluate spatial gender bias in LLMs. It combines a taxonomy of 62 urban micro-spaces, a prompt library, and three diagnostic layers: explicit (forced-choice resampling), probabilistic (token-level asymmetry), and constructional (semantic and narrative role analysis). Testing six representative models, we identify structured gender-space associations that go beyond the public-private divide, forming nuanced micro-level mappings. Story generation reveals how emotion, wording, and social roles jointly shape “spatial gender narratives”. We also examine how prompt design, temperature, and model scale influence bias expression. Tracing experiments indicate that these patterns are embedded and reinforced across the model pipeline (pre-training, instruction tuning, and reward modeling), with model associations found to substantially exceed real-world distributions. Downstream experiments further reveal that such biases produce concrete failures in both normative and descriptive application settings. This work connects sociological theory with computational analysis, extending bias research into the spatial domain and uncovering how LLMs encode social gender cognition through language.

## 46. Potato 2.0: A Comprehensive Annotation Platform with AI-in-the-Loop Support

- Authors: David Jurgens, Michael Chen, Lina Iyer
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.7341605378497276
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-demo.37/
- PDF: https://aclanthology.org/2026.acl-demo.37.pdf
- Local PDF: pdf/2026-09-05_46_Potato 2.0_ A Comprehensive Annotation Platform with AI-in-the-Loop Support.pdf

Annotated data remains essential for training and evaluating NLP systems. Large language models have broadened the kinds of data researchers need, including multimodal and agentic system data. Here, we introduce Potato 2.0, a major update to our open source annotation platform designed for easy deployment, customization, and fully reproducible and shareable annotation designs. Potato offers broad support for many types of annotations in NLP, including 39 different types of annotation tasks, support for text, audio, image, and video modalities, or mixtures thereof. Potato 2.0 includes robust support for labeling agentic system outputs through reading common trace formats, or live interaction and annotation with agents in multiple settings, such as chatting, web-browsing, and coding. Potato also includes multiple AI-assistance features to help annotators more easily label data. Finally, Potato introduces a new agentic AI-in-the-loop workflow where a single human annotator collaborates with an LLM through iterative prompt refinement, uncertainty-driven instance selection, and progressive autonomy—enabling efficient dataset creation without a large annotation team.

## 47. AutoRubric: Rubric-Based Generative Rewards for Faithful Multimodal Reasoning

- Authors: Mengzhao Jia, Zhihan Zhang, Ignacio Cases, Zheyuan Liu, Meng Jiang, Peng Qi
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.7339000112594696
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1282/
- PDF: https://aclanthology.org/2026.findings-acl.1282.pdf
- Local PDF: pdf/2026-09-05_47_AutoRubric_ Rubric-Based Generative Rewards for Faithful Multimodal Reasoning.pdf

Multimodal large language models (MLLMs) have rapidly advanced from perception tasks to complex multi-step reasoning, yet reinforcement learning with verifiable rewards (RLVR) often leads to spurious reasoning since only the final-answer correctness is rewarded. To address this limitation, we propose AutoRubric, a framework that integrates RLVR with process-level supervision through automatically collected rubric-based generative rewards. Our key innovation lies in a scalable self-aggregation method that distills consistent reasoning checkpoints from successful trajectories, enabling problem-specific rubric construction without human annotation or stronger teacher models. By jointly leveraging rubric-based and outcome rewards, AutoRubric-R1V achieves state-of-the-art performance on six multimodal reasoning benchmarks and substantially improves reasoning faithfulness in dedicated evaluations.

## 48. Multi-Hop Knowledge Editing via Critic-Guided Multi-Agent Reasoning

- Authors: Xudong Li, Yuhang Tian, Dandan Song, Zhijing Wu, Shuhao Zhang, Jun Yang, Yongyu Huo, Changzhi Zhou, Xinyu Zhang, Chenhao Li, Huipeng Ma, Luan Zhang, Yan Xu, Qian Liu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.7337189939524427
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.853/
- PDF: https://aclanthology.org/2026.findings-acl.853.pdf
- Local PDF: pdf/2026-09-05_48_Multi-Hop Knowledge Editing via Critic-Guided Multi-Agent Reasoning.pdf

Knowledge within large language models (LLMs) inevitably lags behind an evolving world, motivating knowledge editing methods that update facts without expensive retraining. In multi-hop knowledge editing, models must not only recall updated facts but also correctly propagate them through multi-step reasoning chains. However, most existing approaches rely on unidirectional, feed-forward pipelines, decomposing questions and retrieving edited facts in a rigid hop-wise sequence. This design is brittle: a minor retrieval error or logical mismatch at an early hop can become a silent failure that cascades to the final answer without an explicit recovery mechanism. To address this limitation, we propose Critic-Guided Multi-Agent Reasoning for Knowledge Editing (CARE), a framework for closed-loop post-edit reasoning. A Critic agent performs chain-level verification by checking both global coherence and step-wise correctness, and triggers bounded backtracking for iterative self-correction, while a Selector agent supplies high-fidelity, low-noise candidate pools from the edit store to enable effective revision. Experiments on MQuAKE-2002 and MQuAKE-hard demonstrate that CARE effectively mitigates error propagation, achieving a new state-of-the-art.

## 49. RISER: Orchestrating Latent Reasoning Skills for Adaptive Activation Steering

- Authors: Wencheng Ye, Xiaoyang Yuan, Yi Bin, Hengyu Jin, Liang Peng, Pengpeng Zeng, Heng Tao Shen
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.732680105672658
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.226/
- PDF: https://aclanthology.org/2026.findings-acl.226.pdf
- Local PDF: pdf/2026-09-05_49_RISER_ Orchestrating Latent Reasoning Skills for Adaptive Activation Steering.pdf

Recent work on domain-specific reasoning with large language models (LLMs) has largely relied on training-intensive approaches that require updating model parameters. Although activation steering has emerged as a parameter-efficient alternative, existing methods typically rely on static and manually designed interventions, limiting their ability to adapt to the dynamic nature of complex reasoning. To address this limitation, we propose RISER (Router-based Intervention for Steerable Enhancement of Reasoning), a plug-and-play intervention framework that adaptively steers LLM reasoning in activation space. RISER builds a library of reusable reasoning vectors and employs a lightweight Router to dynamically compose these vectors for each input. The Router is optimized via reinforcement learning under task-level rewards, enabling the emergent and compositional activation of latent cognitive primitives. Across seven diverse benchmarks, RISER achieves average zero-shot accuracy improvements of 3.4–6.5% over the base model, while outperforming chain-of-thought-style reasoning with 2–3× higher token efficiency and robust accuracy gains. Further analysis demonstrates that RISER autonomously combines multiple vectors into interpretable and precise control strategies, pointing toward more controllable and efficient LLM reasoning.

## 50. What Resources Matter for Interlinear Glossing? Using LLMs and RAG for the Low-Resource Mapudungun Language

- Authors: Anaís Almendra, Arianna Bisazza, Claudio Gutierrez, Felipe Hasler
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.732472191264873
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.americasnlp-6.6/
- PDF: https://aclanthology.org/2026.americasnlp-6.6.pdf
- Local PDF: pdf/2026-09-05_50_What Resources Matter for Interlinear Glossing_ Using LLMs and RAG for the Low-Resource Mapudungun Language.pdf

Interlinear glossing is essential for the study and revitalization of endangered languages. However, it remains a time-consuming process that requires extensive linguistic expertise. Recent advances in Large Language Models (LLMs) offer a potential solution. In this research, we study the case of Mapudungun, an endangered language spoken in Chile and Argentina, to generate automatic interlinear glosses using the Gemini 2.5 Pro model. Our study investigates which information configuration through Retrieval-Augmented Generation (RAG) yields the best results. We compare the integration of a formal grammar, a dictionary, a small annotated corpus, and a combination of all these resources. Our evaluation shows that while dictionary integration causes a significant degradation in performance, grounding the model with a structured corpus maximizes accuracy relative to the resources employed. Notably, we find that a remarkably small dataset of 589 meaning units provides enough normative guidance to significantly improve the morphological tagging task. This work highlights the viability of utilizing minimally annotated corpora to assist in the documentation of morphologically complex languages.

## 51. RAG or Learning? Understanding the Limits of LLM Adaptation under Continuous Knowledge Drift in the Real World

- Authors: Hanbing Liu, Lang Cao, Yang Li
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.7322449439069665
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.546/
- PDF: https://aclanthology.org/2026.findings-acl.546.pdf
- Local PDF: pdf/2026-09-05_51_RAG or Learning_ Understanding the Limits of LLM Adaptation under Continuous Knowledge Drift in the Real World.pdf

Large language models (LLMs) acquire most of their knowledge during pretraining, which ties them to a fixed snapshot of the world and makes adaptation to continuously evolving knowledge challenging. As facts, entities, and events change over time, models may experience continuous knowledge drift, resulting not only in outdated predictions but also in temporally inconsistent reasoning. Although existing approaches, such as continual finetuning, knowledge editing, and retrieval-augmented generation (RAG), aim to update or supplement model knowledge, they are rarely evaluated in settings that reflect chronological, evolving, and real-world knowledge evolution. In this work, we introduce a new benchmark of real-world dynamic events, constructed from time-stamped evidence that captures how knowledge evolves over time, which enables systematic evaluation of model adaptation under continuous knowledge drift. The benchmark reveals that most existing methods, including vanilla RAG and several learning-based approaches, struggle under this setting, exposing critical limitations such as catastrophic forgetting and temporal inconsistency. To mitigate these limitations, we propose a time-aware retrieval baseline, Chronos, which progressively organizes retrieved evidence into an Event Evolution Graph to enable more temporally consistent understanding in LLMs without additional training. Overall, this work provides a foundation for analyzing and advancing LLM adaptation to continuous knowledge drift in realistic settings.

## 52. IDP Accelerator: Agentic Document Intelligence from Extraction to Compliance Validation

- Authors: Md Mofijul Islam, Md Sirajus Salekin, Joe King, Priyashree Roy, Vamsi Thilak Gudi, Spencer Romo, Akhil Nooney, Bob Strahan, Boyi Xie, Diego A. Socolinsky
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.7320152684422307
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-demo.11/
- PDF: https://aclanthology.org/2026.acl-demo.11.pdf
- Local PDF: pdf/2026-09-05_52_IDP Accelerator_ Agentic Document Intelligence from Extraction to Compliance Validation.pdf

Understanding and extracting structured insights from unstructured documents remains a foundational challenge in industrial NLP. While Large Language Models (LLMs) enable zero-shot extraction, traditional pipelines often fail to handle multi-document packets, complex reasoning, and strict compliance requirements. We present IDP (Intelligent Document Processing) Accelerator, a framework enabling agentic AI for end-to-end document intelligence with four key components: (1) DocSplit, a novel benchmark dataset and multimodal classifier using BIO tagging to segment complex document packets; (2) configurable Extraction Module leveraging multimodal LLMs to transform unstructured content into structured data; (3) Agentic Analytics Module, compliant with the Model Context Protocol (MCP) providing data access through secure, sandboxed code execution; and (4) Rule Validation Module replacing deterministic engines with LLM-driven logic for complex compliance checks. The interactive demonstration enables users to upload document packets, visualize classification results, and explore extracted data through an intuitive web interface. We demonstrate effectiveness across industries, highlighting a production deployment at a leading healthcare provider achieving 98% classification accuracy, 80% reduced processing latency, and 77% lower operational costs over legacy baselines. IDP Accelerator is open-sourced with a live demonstration available to the community.

## 53. ERRV: Eliciting Efficient Reasoning through Reasoning Vectors for Policy Optimization in Large Language Models

- Authors: Zhuowen Han, Lei Yang, Renren Jin, Dan Shi, Chenxi Sun, Deyi Xiong
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.7318528242804248
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1425/
- PDF: https://aclanthology.org/2026.findings-acl.1425.pdf
- Local PDF: pdf/2026-09-05_53_ERRV_ Eliciting Efficient Reasoning through Reasoning Vectors for Policy Optimization in Large Language Models.pdf

Recently, large reasoning models have achieved impressive performance, but their lengthy reasoning processes incur substantial inference overhead. To mitigate this issue, we propose the concept of reasoning vectors, representations extracted from the model’s hidden states, which can guide the model towards generating more concise and accurate responses. Building upon this, we present ERRV, a training framework that elicits efficient reasoning through reasoning vectors, which enables the model to generate high-quality responses during reinforcement learning. By performing targeted policy optimization on both accuracy and length objectives, ERRV effectively activates the model’s latent capability for efficient reasoning. Our experiments demonstrate that after training with ERRV, the model achieves approximately 30% reduction in reasoning length while maintaining stable accuracy, without guidance from the reasoning vector during inference. This establishes a trade-off between efficiency and performance. Furthermore, we identify key properties of reasoning vectors: robustness, characterized by high similarity before and after training, and generalizability, demonstrating applicability across base models, distilled models, RL-trained models, parameter-merged models, and mixed-thought models. These properties collectively guarantee the reliability and broad applicability of our approach.

## 54. SemPA: Improving Sentence Embeddings of Large Language Models through Semantic Preference Alignment

- Authors: Ziyang Chen, Zhenxuan Huang, Yile Wang, Weiqin Wang, Lu Yin, Hui Huang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.731066412695638
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1858/
- PDF: https://aclanthology.org/2026.findings-acl.1858.pdf
- Local PDF: pdf/2026-09-05_54_SemPA_ Improving Sentence Embeddings of Large Language Models through Semantic Preference Alignment.pdf

Traditional sentence embedding methods employ token-level contrastive learning on non-generative pre-trained models. Recently, there have emerged embedding methods based on generative large language models (LLMs). These methods either rely on fixed prompt templates or involve modifications to the model architecture. The former lacks further optimization of the model and results in limited performance, while the latter alters the internal computational mechanisms of the model, thereby compromising its generative capabilities. We propose SemPA, a novel approach that boosts the sentence representations while preserving the generative ability of LLMs via semantic preference alignment. We leverage sentence-level Direct Preference Optimization (DPO) to efficiently optimize LLMs on a paraphrase generation task, where the model learns to discriminate semantically equivalent sentences while preserving inherent generative capacity. Theoretically, we establish a formal connection between DPO and contrastive learning under the Plackett-Luce model framework. Empirically, experimental results on both semantic textual similarity tasks and various benchmarks for LLMs show that SemPA achieves better semantic representations without sacrificing the inherent generation capability of LLMs.

## 55. Efficient Agent Evaluation via Diversity-Guided User Simulation

- Authors: Itay Nakash, George Kour, Ateret Anaby Tavor
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.730974244631984
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-industry.112/
- PDF: https://aclanthology.org/2026.acl-industry.112.pdf
- Local PDF: pdf/2026-09-05_55_Efficient Agent Evaluation via Diversity-Guided User Simulation.pdf

Large language models (LLMs) are increasingly deployed as customer-facing agents, yet evaluating their reliability remains challenging due to stochastic, multi-turn interactions. Current evaluation protocols rely on linear Monte Carlo rollouts of full agent-user conversations to estimate success. This approach is computationally inefficient - reprocessing identical conversation prefixes across runs, and often fails to uncover deep failure modes triggered by rare user behaviors.We introduce DIVERT (Diversity-Induced Evaluation via Branching of Trajectories), a snapshot-based, coverage-guided user simulation framework for efficient and systematic exploration of multi-turn agent behavior. DIVERT captures the full agent–environment state at critical junctions and resumes execution from these points, reusing shared prefixes to avoid redundant regeneration and reduce token cost. From each junction, it branches with targeted, diverse user responses, enabling directed exploration of alternative interaction paths while preserving task intent.By reallocating computation from redundant restarts to behaviorally salient mid-trajectory states, DIVERT steers evaluation toward under-explored semantic regions and rare interaction failures. Experiments on realistic multi-domain benchmarks show that our method consistently improves failure discovery efficiency and task-level coverage compared to standard linear rollout evaluation, without increasing overall cost.

## 56. Reducing Peak Memory Usage for Modern Multimodal Large Language Model Pipelines

- Authors: Junwan Kim, Hyunkyung Bae
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.730682689748265
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1422/
- PDF: https://aclanthology.org/2026.findings-acl.1422.pdf
- Local PDF: pdf/2026-09-05_56_Reducing Peak Memory Usage for Modern Multimodal Large Language Model Pipelines.pdf

Multimodal large language models (MLLMs) have recently demonstrated strong capabilities in understanding and generating responses from diverse visual inputs, including high-resolution images and long video sequences. As these models scale to richer visual representations, inference increasingly relies on storing large numbers of vision tokens in the key–value (KV) cache, making memory consumption a central bottleneck. Existing methods address this issue by identifying redundancy in vision tokens and compressing the cache, but such compression is typically applied only after all inputs are processed, resulting in high peak memory usage during the prefill stage. In this work, we show that MLLMs exhibit inherent structural regularities and representational redundancy that can be exploited to control memory growth throughout inference. Based on this insight, we propose a sequential input-compression mechanism that enforces a fixed memory budget by performing structure-aware key–value cache compression during the prefill process. This approach substantially reduces peak memory usage while maintaining generative performance with only minimal degradation, enabling more practical and memory-efficient multimodal inference.

## 57. MT 3 : A Synergistic Multi-Task RL Framework for Specializing MLLMs in Text Image Machine Translation

- Authors: Zhaopeng Feng, Yupu Liang, Shaosheng Cao, Jiayuan Su, Jiahan Ren, Zhijie Zhou, Wenxuan Huang, Jian Wu, Zuozhu Liu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.7304353216838297
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.460/
- PDF: https://aclanthology.org/2026.acl-long.460.pdf
- Local PDF: pdf/2026-09-05_57_MT 3 _ A Synergistic Multi-Task RL Framework for Specializing MLLMs in Text Image Machine Translation.pdf

Text Image Machine Translation (TIMT)—the task of translating textual content embedded in images—is critical for applications in accessibility, cross-lingual information access, and real-world document understanding. However, TIMT remains a complex challenge due to the need for accurate optical character recognition (OCR), robust visual-text reasoning, and high-quality translation, often requiring cascading multi-stage pipelines. Recent advances in large-scale Reinforcement Learning (RL) have improved reasoning in Large Language Models (LLMs) and Multimodal LLMs (MLLMs), but their application to end-to-end TIMT is still underexplored. To bridge this gap, we introduce MT 3 , a novel Multi-Task RL framework to specialize MLLMs into end-to-end expert TIMT models. MT 3 adopts a synergistic multi-task optimization paradigm targeting three key sub-skills: text recognition, context-aware reasoning, and translation. It is trained using a novel multi-mixed reward mechanism that provides fine-grained feedback, fostering a controllable and transparent optimization process. Furthermore, to facilitate the evaluation of TIMT in authentic cross-cultural and real-world social media contexts, we introduced XHSPost, the first social media TIMT benchmark. Our MT 3 -7B-Zero achieves state-of-the-art results on the latest in-domain MIT-10M benchmark, outperforming strong baselines such as Qwen2.5-VL-72B and InternVL2.5-78B by notable margins across multiple metrics. Additionally, the model shows strong generalization to out-of-distribution language pairs and datasets. In-depth analyses reveal how multi-task synergy, reinforcement learning initialization, curriculum design, and reward formulation contribute to advancing MLLM-driven TIMT.

## 58. NoisyCausal: A Benchmark for Evaluating Causal Reasoning Under Structured Noise

- Authors: Zhi Xu, Yun Fu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.730087982114501
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1833/
- PDF: https://aclanthology.org/2026.acl-long.1833.pdf
- Local PDF: pdf/2026-09-05_58_NoisyCausal_ A Benchmark for Evaluating Causal Reasoning Under Structured Noise.pdf

Causal reasoning in natural language requires identifying relevant variables, understanding their interactions, and reasoning about effects and interventions, often under noisy or ambiguous conditions. While large language models (LLMs) exhibit strong general reasoning abilities, they struggle to disentangle correlation from causation, particularly when observations are partially incorrect or irrelevant information is present. In this work, we introduce NoisyCausal, a new benchmark designed to evaluate causal reasoning under structured noise. Each instance is generated from a ground-truth causal graph and contextualized with a natural language scenario by injecting controllable forms of noise, such as irrelevant distractors, value perturbations, confounding, and partial observability. Moreover, we propose a modular reasoning framework that combines LLMs with explicit causal structure to address these challenges. Our method prompts the LLM to extract variables, construct a causal graph from context, and then reformulates the reasoning task as a structured prompt grounded in this graph. Rather than relying on statistical patterns alone, the LLM is guided by symbolic structure, enabling more interpretable and robust inference. Experimental results show that our method significantly outperforms standard prompting and reasoning baselines on NoisyCausal. Furthermore, it generalizes well to external benchmarks such as Cladder without task-specific tuning. Our findings highlight the importance of combining causal abstractions with language-driven reasoning to achieve faithful and robust causal understanding in LLMs.

## 59. Robust In-Context Selection via Online Learned Position-Corrected Attention

- Authors: Deeksha Koul, Gaurav Kumar, Yash Sabale, Sunita Sarawagi
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.7294034693819826
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1743/
- PDF: https://aclanthology.org/2026.findings-acl.1743.pdf
- Local PDF: pdf/2026-09-05_59_Robust In-Context Selection via Online Learned Position-Corrected Attention.pdf

Large Language Models (LLMs) are often deployed in tasks that require selecting an item from a long list provided in the model’s context. LLMs’ native selection behavior is brittle: predictions are sensitive to the surface form of the identifiers, their placement within the context, and the ordering of candidate items. We present OLR-Heads, a robust method for list selection that harnesses attention patterns available from a single forward call on the LLM. OLR-Heads learns the logic for item selection using a few in-context examples, and a simple online position-debiasing mechanism to correct attention distortion. Across multiple database and tool selection benchmarks, OLR-Heads consistently improves selection performance over direct generation and prior attention-based methods, while remaining robust to prompt variations and item ordering.The LLM’s KV cache states are unaffected, and can be reused for subsequent response generation. In contrast, existing approaches either entail additional LLM calls, or task-specific offline learning, or position debiasing methods that modify the attention or encoding rendering the KV states unusable for subsequent generation.

## 60. Tailored Primitive Initialization is the Secret Key to Reinforcement Learning

- Authors: Yihang Yao, Guangtao Zeng, Raina Wu, Yang Zhang, Ding Zhao, Zhang-Wei Hong, Chuang Gan
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.7293641709638883
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1537/
- PDF: https://aclanthology.org/2026.acl-long.1537.pdf
- Local PDF: pdf/2026-09-05_60_Tailored Primitive Initialization is the Secret Key to Reinforcement Learning.pdf

Reinforcement learning (RL) has emerged as a powerful paradigm for improving the reasoning capabilities of large language models (LLMs). Despite its success, RL faces fundamental challenges, including low sample efficiency and a strong dependence on the quality of the base model: while some models improve rapidly with limited RL updates, others require substantial training data to achieve meaningful gains. Recent studies suggest that the patterns of thinking tokens play a critical role in RL performance, and that supervised fine-tuning (SFT) on datasets exhibiting desirable reasoning patterns can reduce reliance on base models and better prepare LLMs for RL. However, how to automatically discover such patterns across tasks remains unclear. In this work, we describe thinking token patterns with reasoning primitives and argue that initializing LLMs with diverse, high-quality primitives is crucial for stable and efficient RL training. We propose Tailor, a pipeline that automatically discovers such reasoning primitives and curates SFT datasets to prepare LLMs for RL. Extensive experiments on mathematical and logical reasoning benchmarks demonstrate that Tailor consistently improves downstream RL performance, outperforming strong baselines, including methods with expert domain knowledge.
