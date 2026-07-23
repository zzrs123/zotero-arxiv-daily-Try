# Paper Daily Reading - 2026-07-23

## 1. Scalable and Efficient Joint Spiking Embedding Predictive Architecture for Large-Scale Dynamic Graphs

- Authors: Huizhe Zhang, Yuchang Zhu, Huazhen Zhong, Liang Chen, Zibin Zheng
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-20
- DOI: Unavailable
- Categories: cs.LG, cs.NE
- Relevance: 3.811133576847644
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.18412v1
- PDF: https://arxiv.org/pdf/2607.18412v1
- Local PDF: pdf/2026-07-23_01_Scalable and Efficient Joint Spiking Embedding Predictive Architecture for Large-Scale Dynamic Graphs.pdf

Dynamic graph learning aims to capture evolving structural and semantic patterns in real-world systems, such as fraud detection and recommender systems. Due to the scarcity of labeled data in real-world dynamic graphs, recent studies have introduced generative or contrastive paradigms (e.g., masked graph autoencoders or graph contrastive learning) to generate task-agnostic graph embeddings. However, these methods typically rely on complex edge-level reconstruction objectives and tailored graph augmentation strategies. This incurs substantial computational overhead when scaling to large-scale dynamic graphs. In this paper, we propose SG-JEPA, a joint spiking embedding predictive architecture for large-scale dynamic graphs. In contrast to existing self-supervised methods, SG-JEPA partitions nodes into context and target sets along the temporal dimension to learn embeddings that are predictive of each other via additional spatial-temporal information. Furthermore, through encoding sequential inputs into coarse-to-fine spike count embeddings, spiking neurons enable SG-JEPA to adapt to the varying computational constraints of downstream tasks. Extensive experiments demonstrate that SG-JEPA achieves competitive or even superior performance over discriminative baselines on node classification, while effectively scaling to the dynamic graph with 13 million edges. SG-JEPA avoids the complex machinery (negative sampling, graph augmentations, edge-level reconstruction, etc.), resulting in superior training efficiency and memory scalability compared with prior self-supervised dynamic graph baselines.

## 2. GEqTrain: A Configuration-Driven Framework for Retargeting Equivariant Graph Neural Networks Across 3D Scientific Tasks

- Authors: Daniele Angioletti, Marco Nobile, Vittorio Limongelli
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-21
- DOI: Unavailable
- Categories: cs.LG, q-bio.BM
- Relevance: 3.7927017903357125
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.19083v1
- PDF: https://arxiv.org/pdf/2607.19083v1
- Local PDF: pdf/2026-07-23_02_GEqTrain_ A Configuration-Driven Framework for Retargeting Equivariant Graph Neural Networks Across 3D Scientific Tasks.pdf

Equivariant graph neural networks provide a powerful modeling language for three-dimensional scientific data, but their reuse is often limited by implementations tied to specific tasks, outputs, and training regimes. We present GEqTrain, a configuration-driven framework that separates dataset semantics, model composition, and training objectives. Raw data are mapped to typed node-, edge-, and graph-level fields, while model stacks, losses, and training workflows are assembled declaratively through Hydra configurations. A shared equivariant backbone and training infrastructure can therefore be retargeted to a new task primarily through configuration. We demonstrate this flexibility on three different problems handled within one software stack: coarse-grained-to-atomistic backmapping of biomolecular systems, prediction of NMR chemical shifts in molecular solids, and equivariant generative modeling. Our aim is not to surpass individually optimized task-specific systems, but to show that a shared representation and training infrastructure can achieve competitive accuracy across qualitatively different tasks at the cost of a configuration change. We further introduce GEqDiff, a generative extension based on equivariant flow matching. GEqDiff treats user-defined equivariant fields as first-class generation targets, jointly transporting Cartesian positions and non-scalar node fields spanning representations up to l=3 within a single equivariant flow. We validate this capability on a controlled synthetic benchmark inspired by protein secondary-structure motifs, showing that fields with heterogeneous transformation properties can be reconstructed jointly and with high fidelity. By reducing the software overhead of moving between predictive and generative, scalar and tensorial settings, GEqTrain aims to make equivariant modeling more reproducible, extensible, and reusable.

## 3. Parallel Noising in Neural Markov Logic Networks

- Authors: Peter Jung, Giuseppe Marra, Ondrej Kuzelka
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-21
- DOI: Unavailable
- Categories: cs.LG, cs.AI
- Relevance: 3.6815202314278563
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.19126v1
- PDF: https://arxiv.org/pdf/2607.19126v1
- Local PDF: pdf/2026-07-23_03_Parallel Noising in Neural Markov Logic Networks.pdf

Neural Markov Logic Networks (NMLNs) are a flexible neurosymbolic relational model. Previous work has shown that, although NMLNs achieve strong performance as generative models for small relational structures, they underperform diffusion-based generative graph models on larger structures. In this paper, we strengthen NMLNs along two main dimensions: (i) we increase the expressive capacity of their potential functions using graph neural networks, and (ii) we develop a new training and inference algorithm inspired by parallel-tempering Markov chain Monte Carlo methods, which we name parallel noising. Together, these enhancements enable NMLNs to attain strong performance in graph generation relative to general diffusion-based generative graph models. Furthermore, they allow NMLNs to match the performance of specialized text-based recurrent models when generating small molecular structures.

## 4. Attacking Graph Foundation Models Through Their Shared Representation

- Authors: Pankaj Kumar, Subhankar Mishra
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-20
- DOI: Unavailable
- Categories: cs.AI, cs.CR, cs.LG
- Relevance: 3.4725770045200144
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.18567v1
- PDF: https://arxiv.org/pdf/2607.18567v1
- Local PDF: pdf/2026-07-23_04_Attacking Graph Foundation Models Through Their Shared Representation.pdf

A graph foundation model generalizes across graph domains by mapping every input into one shared representation before any task reasoning. We call this map the alignment layer, the component that separates a graph foundation model from a graph neural network, and we show it is a distinct attack surface that prior work has not studied. We attack it at inference time, with no access to training, on six public models spanning spectral tokenizers, text embedding spaces, and a discrete codebook. A directed representation-space perturbation collapses every model, but at a budget comparable to the representation norm a plain graph network also needs, with one exception: OpenGraph, whose spectral tokenizer collapses at a fifth of that budget, an alignment-specific fragility a plain network does not share and which a same-representation control traces to the tokenizer rather than the decoder. A realizable input-space attack that edits edges, features, or text removes at least half the correct predictions on three of the six models at peak. How much of this fragility an input-access attacker realizes tracks how directly the decoder reads the representation, and not the clean accuracy a task leaves; we measure this carrier gain structurally from the decoder's local Lipschitz sensitivity, and report clean-accuracy headroom as a within-model ordering heuristic that does not survive on realizable attacks.

## 5. Sequential Learner Modeling Using Multi-Relational Graph Convolutional Networks

- Authors: Rawaa Alatrash, Mohamed Amine Chatti, Hong Yang, Yumeng Wang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-21
- DOI: Unavailable
- Categories: cs.AI, cs.CY, cs.IR
- Relevance: 3.432675213965306
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.19253v1
- PDF: https://arxiv.org/pdf/2607.19253v1
- Local PDF: pdf/2026-07-23_05_Sequential Learner Modeling Using Multi-Relational Graph Convolutional Networks.pdf

User modeling is a critical task in a variety of personalized systems. Recognizing their effectiveness in learning from graph-structured data, Graph Neural Networks (GNNs), particularly Graph Convolutional Networks (GCNs), are increasingly employed for user modeling. However, existing approaches typically treat different relation types in a graph as homogeneous, limiting their ability to capture richer semantics and construct more informative user models. While multi-relational GNNs (MR-GNNs) have been adopted for representation learning and recommendation, their application for user modeling remains unexplored. Moreover, existing GNN-based user modeling approaches ignore the user interaction sequence. To address these research gaps, in this work we propose MR-ConceptGCN, a novel fully unsupervised approach focused on concept-based sequential learner modeling using multi-relational GCNs (MR-GCNs). MR-ConceptGCN effecively combines Personal Knowledge Graphs (PKGs), MR-GCNs, and the pre-trained language model SBERT to obtain enhanced relation- and semantic-aware representations of the PKG items. The enriched embeddings of the knowledge concepts that a learner did not understand when interacting with learning materials in CourseMapper are then used to construct a sequential learner model that combines long-term and short-term learner interactions. We report the results of an online user study (n = 31), demonstrating the benefits of MR-ConceptGCN in terms of several important user-centric aspects including accuracy, usefulness, diversity, and satisfaction with an educational recommender system.

## 6. On the Effectiveness of Pretraining for Graph Combinatorial Optimization

- Authors: David Aguado, Daniel Fuertes, Carlos R. del-Blanco, Fernando Jaureguizar
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-21
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 3.3239979864506717
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.19072v1
- PDF: https://arxiv.org/pdf/2607.19072v1
- Local PDF: pdf/2026-07-23_06_On the Effectiveness of Pretraining for Graph Combinatorial Optimization.pdf

This paper introduces a self-supervised pretraining framework for graph combinatorial optimization specifically designed to address the nature of routing problems like the Traveling Salesman Problem. By utilizing graph contrastive learning with geometric augmentations (specifically, rotations and axial reflections) the model is forced to learn invariant structural representations and global relative distance distributions. Results demonstrate that this pretraining strategy outperforms non-pretrained models across various problem scales. Notably, the hybrid strategy (combining rotation and reflection) achieved a 6.57% improvement in tour length for TSP1000, proving that geometric pretraining is an important inductive bias for effectively scaling neural solvers to high-dimensional instances.

## 7. Tangerine: A Python framework for dynamic gene regulation analysis from transcriptomic time series

- Authors: Narendra, T., Schweikert, G.
- Source: biorxiv
- Venue type: preprint
- Journal: biorxiv
- Publication status: preprint
- Publication date: 2026-07-22
- DOI: 10.64898/2026.07.17.739167
- Categories: bioinformatics
- Relevance: 3.3222743344169645
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://www.biorxiv.org/content/10.64898/2026.07.17.739167v1.full.pdf
- PDF: https://www.biorxiv.org/content/10.64898/2026.07.17.739167v1.full.pdf
- Local PDF: pdf/2026-07-23_07_Tangerine_ A Python framework for dynamic gene regulation analysis from transcriptomic time series.pdf

Motivation: Time-series single-cell transcriptomics enables the study of dynamic gene regulation. However, standard computational tools frequently aggregate temporal data into static, dense topologies, obscuring the precise regulatory rewiring that drives developmental transitions. Further, navigating the inherent noise of statistical inference without losing biological interpretability remains an important bottleneck. Results: We present Tangerine, a Python framework for the dynamic reconstruction and interactive exploration of time-varying gene regulatory networks. Tangerine integrates time-constrained metacell aggregation with regularized linear modelling and non-parametric correlation to infer dynamic topologies. To solve the interpretability gap, it features a browser-based visual analytics engine. Tangerine empowers researchers to track macroscopic gene module evolution, interactively filter effect sizes, and link topological rewiring directly to raw transcriptomic evidence. Availability and implementation: Tangerine is implemented in Python and Plotly Dash. The code is available on Github at https://github.com/ntanmayee/tangerine.

## 8. scLEMBAS: Context-Aware Modeling of Signaling Pathway Activity at Single-Cell Resolution

- Authors: Baghdassarian, H. M., Meimetis, N., Nordenstorm, O., Joughin, B., Nilsson, A., Lauffenburger, D.
- Source: biorxiv
- Venue type: preprint
- Journal: biorxiv
- Publication status: preprint
- Publication date: 2026-07-22
- DOI: 10.64898/2026.07.20.739670
- Categories: bioinformatics
- Relevance: 3.277407791965088
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://www.biorxiv.org/content/10.64898/2026.07.20.739670v1.full.pdf
- PDF: https://www.biorxiv.org/content/10.64898/2026.07.20.739670v1.full.pdf
- Local PDF: pdf/2026-07-23_08_scLEMBAS_ Context-Aware Modeling of Signaling Pathway Activity at Single-Cell Resolution.pdf

Cells sense and integrate extracellular cues through intracellular signaling networks that reshape transcription factor activity to dictate cellular responses. Signaling activity is difficult to decipher: it is non-linear, and it contains extensive feedback and crosstalk. Furthermore, the same perturbation can elicit markedly different responses depending on context (e.g., cell type, disease state, and tissue microenvironment) such that identical stimuli produce diverse responses in multicellular populations. Consequently, there is a vast combinatorial space of complex interactions and context-dependent responses that necessitate computational models. Computational models of single-cell perturbation responses are demonstrated to predict cellular responses, but are often limited in mechanistic insight. Prior knowledge networks offer a route to bridge predictive capability and interpretability. Here we present scLEMBAS, a context-aware, gray-box neural network that models signaling pathway activity at single-cell resolution while preserving mechanistic grounding. scLEMBAS encodes a prior-knowledge network of protein-protein interactions as a recurrent neural network whose learnable edge weights correspond to signaling interaction strengths. It also captures context and individual cell variance through compositional bias terms. An adversarial approach allows the model to answer a single-cell counterfactual - what a given cell's TF activity would be under a different perturbation or context - while involving mechanistic rather than simply relational information. Across two scRNA-seq datasets spanning single- and multi-perturbation settings, scLEMBAS accurately predicts out-of-distribution combinations of perturbation and context. Capturing population variance across individual cells enables the model to predict cell subtype specific perturbation responses, despite being agnostic to such labels. Beyond prediction, scLEMBAS learned parameters are biologically interpretable: learned edge weights carry information beyond network topology and "self-prune" spurious interactions, while the categorical bias nominates proteins associated with cell-type-specific perturbation states. Overall, scLEMBAS enables quantitative dissection of how signaling pathway activity is reshaped by perturbation within specific cellular contexts.

## 9. BatchDAG: LLM-Planned Execution Graphs for Scalable Ad-Hoc Analysis Over Enterprise Data

- Authors: Anupreet Walia
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-04-17
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 3.1631658260276945
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.18241v1
- PDF: https://arxiv.org/pdf/2607.18241v1
- Local PDF: pdf/2026-07-23_09_BatchDAG_ LLM-Planned Execution Graphs for Scalable Ad-Hoc Analysis Over Enterprise Data.pdf

Large language models (LLMs) excel at analyzing individual documents but break down on exhaustive, cross-entity analytical questions over enterprise-scale datasets due to context overflow, loss of per-entity attribution, and linear latency from sequential tool calls. We present BatchDAG, a system in which an LLM generates a typed directed acyclic graph (DAG) of operations -- SQL queries, semantic searches, in-memory transforms, parallel fan-outs, and single-shot analyses -- which a deterministic engine evaluates with topological-wave parallelism and structured JSON data flow. A key optimization, entity-aware batching, groups rows by logical entity before fan-out, reducing LLM calls by up to 47x. BatchDAG is not primarily an accuracy improvement over hand-optimized pipelines; rather, it is a general-purpose orchestration layer that replaces multiple hand-engineered workflows with a single system that generates the appropriate execution strategy from natural language. In controlled experiments on 12 transcript-heavy queries, BatchDAG (3.74/5) achieves quality comparable to an expert-designed pipeline (3.25/5) and significantly outperforms a ReAct agent (3.09/5, p<0.01), with superior provenance (77% transcript evidence rate vs. 46-60% for baselines). A controlled ablation shows structured JSON intermediates reduce hallucinations by 27% versus prose summaries (paired t-test, p=0.107, n=12). The planner achieves 98.8% valid-DAG rate across 300 planning calls. In production at Brevian.ai, BatchDAG processes queries over 50,000+ meetings in under 60 seconds, with measured per-query costs of $0.02-$0.24 at published GPT-5.1 pricing.

## 10. Appearance Pointers -- Multimodal Region Control of Diffusion Transformers

- Authors: Rahul Sajnani, Yulia Gryaditskaya, Radomír Měch, Srinath Sridhar, Matheus Gadelha
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-21
- DOI: Unavailable
- Categories: cs.CV, cs.AI, cs.GR
- Relevance: 3.1309975873278004
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.19344v1
- PDF: https://arxiv.org/pdf/2607.19344v1
- Local PDF: pdf/2026-07-23_10_Appearance Pointers -- Multimodal Region Control of Diffusion Transformers.pdf

Controllable image generation remains challenging for creative professionals, who often require precise regional control over materials, object identities, and spatial arrangements that cannot be reliably achieved through text prompting alone. Diffusion Transformers (DiTs) can natively ingest heterogeneous tokens stemming from texts and images, but they lack mechanisms for determining where and how these tokens should influence the output. We introduce appearance pointers, compact tokens that guide DiTs toward the correct appearance cues at the correct spatial locations by aligning text or image inputs with user-specified masks. Appearance pointers are produced by a region correspondence network and refined through a spatial aggregation mechanism, enabling the model to handle multiple regional descriptions without significantly increasing token load. Our approach introduces the first modality-agnostic interface for localized multimodal control in a DiT without retraining the base model from scratch. Across a range of metrics, our single model reaches or surpasses the performance of modality-specific state of the art methods, offering a simple and extensible path toward precise, region-aware, multimodal guidance in generative image synthesis.

## 11. ROMS-IMLE: A Minimalist Approach to Competitive Single-Step Generative Modelling

- Authors: Chirag Vashist, Ke Li
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-21
- DOI: Unavailable
- Categories: cs.LG, cs.CV
- Relevance: 3.017680765728748
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.19332v1
- PDF: https://arxiv.org/pdf/2607.19332v1
- Local PDF: pdf/2026-07-23_11_ROMS-IMLE_ A Minimalist Approach to Competitive Single-Step Generative Modelling.pdf

Generative models have undergone many generations of evolution, from VAEs/GANs to diffusion/flow matching. Along the way, the underlying techniques have become more complicated and various beliefs about what drives strong empirical performance have taken hold. Due to the success of diffusion models and flow matching, one of the more common beliefs is the importance of transforming the noise distribution to the data distribution gradually through many small transformations. We ask whether this is truly necessary, and take a minimalist approach to designing a competitive generative model. We start with the bare-bones essentials, namely just a training objective and a model. We purposefully make both simple. For the training objective, we choose Implicit Maximum Likelihood Estimation (IMLE), and eschew more complicated alternatives such as variational inference, adversarial training and numerical integration. For the model, we eschew transformers and instead choose a moderately sized convolutional network. Then we judiciously added elements that are truly essential, which surprisingly do not include iterative denoising. The result is a single-step parameter-efficient generative model that produces high quality samples at fast speed: it achieves an FID of 2.56 on ImageNet 256 and simultaneously attains good precision and recall.

## 12. OntoBook: Ontology-Grounded Synthetic Textbooks for Medical Encoder Pretraining

- Authors: Rian Touchent, Éric de la Clergerie
- Source: arxiv
- Venue type: preprint
- Journal: Proceedings of Knowledge Graphs and Large Language Models Workshop, May 2026, Palma de Mallorca, Spain
- Publication status: preprint
- Publication date: 2026-07-21
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 3.0110746926923415
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.18927v1
- PDF: https://arxiv.org/pdf/2607.18927v1
- Local PDF: pdf/2026-07-23_12_OntoBook_ Ontology-Grounded Synthetic Textbooks for Medical Encoder Pretraining.pdf

We present OntoBook, a method that converts medical ontology structure into pretraining signal for encoder language models. Our approach has three stages: random walks through ontology graphs capture hierarchical and causal relations between medical codes, a large language model reformulates these walks into fluent textbook-style prose, and the resulting text is used to train ModernCamemBERT, a 149M-parameter French encoder, with two objectives on the same data: masked language modeling and relation prediction between code pairs. On three French medical coding benchmarks (FRACCO, Cantemist-FR, Distemist-FR), OntoBook achieves significant improvements over MLM-only pretraining, with +2.5 micro-F1 on FRACCO and +8.0 micro-F1 on Distemist. We find that alignment between objectives is necessary: misaligned training, where each task uses different data, causes a 30-point degradation. We release 1.3 million LLM-reformulated medical textbooks across three French ontologies (CIM-10, CCAM, ATC) and pretrained model checkpoints.

## 13. Fishing Out Free Riders: Shapley-Based Reward Attribution for Parallel Reasoning via Reinforcement Learning

- Authors: Wentao Zhang, Haoyu Zhang, Xinke Jiang, Yuxuan Cheng, Yuhan Pan, Miao Li, Zhipeng Qiao, Tao Feng, Zhen Tao, Dengji Zhao
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-21
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 2.9998037925804164
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.18979v1
- PDF: https://arxiv.org/pdf/2607.18979v1
- Local PDF: pdf/2026-07-23_13_Fishing Out Free Riders_ Shapley-Based Reward Attribution for Parallel Reasoning via Reinforcement Learning.pdf

Large Language Models (LLMs) excel at multi-step reasoning, yet current parallel reasoning approaches often fail to distinguish the contributions of individual reasoning paths. Many paths may be redundant, misleading, or even detrimental, but outcome-level rewards assign uniform reward, leading to ambiguous learning signals and unstable training. We propose Parallel Shapley, a reinforcement learning framework that attributes fine-grained, path-level contributions in multi-path reasoning. Treating each path as a player in a cooperative game, we leverage Shapley values to quantify marginal contributions, using a generative reward model to evaluate path utilities and Monte Carlo sampling for efficient approximation. Experiments on mathematical reasoning benchmarks show that Parallel Shapley outperforms existing baselines while providing more stable and interpretable training. Our framework effectively "fishes out the free riders," assigning reward proportionally and improving multi-path reasoning in LLMs.

## 14. BioPhasor: Decoding Cellular State Tensors from Multi-Omics Phasor Dynamics for Quantum Ready Systems Biology

- Authors: Sigdel, D., Panday, N.
- Source: biorxiv
- Venue type: preprint
- Journal: biorxiv
- Publication status: preprint
- Publication date: 2026-07-22
- DOI: 10.64898/2026.07.17.739210
- Categories: bioinformatics
- Relevance: 2.9775587078917893
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://www.biorxiv.org/content/10.64898/2026.07.17.739210v1.full.pdf
- PDF: https://www.biorxiv.org/content/10.64898/2026.07.17.739210v1.full.pdf
- Local PDF: pdf/2026-07-23_14_BioPhasor_ Decoding Cellular State Tensors from Multi-Omics Phasor Dynamics for Quantum Ready Systems Biology.pdf

Integrating multi-omics data - transcriptomics, proteomics, metabolomics, single-cell - remains a fundamental challenge in systems biology. We present BioPhasor, a framework that encodes each measurement as a complex phasor z = e^(i{varphi}) on the compact N-torus T^N, modelling the cell as phase-coupled oscillatory programs whose dissipative dynamics generate limit cycles and an attractor landscape. From this geometry we derive the Cell State Tensor (CST), a rank-3 tensor whose axes we root in measured multi-omics quantities: a pathway/module atlas on the regulatory axis and a directional central-dogma modality axis. Across nine scenarios on open public data (GEO, CPTAC), loaded through one unmodified data layer, we report verdicts honestly: four reproduce, three are partial, two do not. A data-driven cell-cycle axis lifts agreement with a reference method from 0.34 to 0.69; an explicit circadian origin cuts peak-time error from 10.6 to 1.4 h; and central-dogma coupling mRNA phase organising protein amplitude clears a surrogate null and is tumour-specific. Grounding the quantum-ready claim, the CST maps to a density-matrix formalism whose coherence and entropy match quantum-information counterparts, and the phasor circuit transpiles gate-for-gate to a variational quantum circuit, though no empirical advantage emerges. One loader regenerates every reported number, and the code is released.

## 15. Now We Know? A Systematic Comparison of TerraMind and THOR

- Authors: Frederick Schindlegger, Kenzo Bounegta, Eva Gmelich Meijling, Johannes Jakubik, Arnt-Børre Salberg, Theodor Forgaard, Nicolas Longepe, Valerio Marsocci
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-20
- DOI: Unavailable
- Categories: cs.LG, cs.AI, cs.CV
- Relevance: 2.9553025148328893
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.18504v1
- PDF: https://arxiv.org/pdf/2607.18504v1
- Local PDF: pdf/2026-07-23_15_Now We Know_ A Systematic Comparison of TerraMind and THOR.pdf

Benchmarks for Geospatial Foundation Models (GFMs) increasingly rank models by aggregate score, but such rankings obscure why models differ: how much of the gap is architecture, how much is decoder capacity, and how much is a use-case-specific artefact? This study addresses that gap through a controlled comparison of two GFMs developed under European Space Agency's $Φ$-lab with contrasting design philosophies: THOR, which introduces a compute-adaptive architecture supporting variable patch sizes and unifies Sentinel-1, -2, and -3 data at their native resolutions; and TerraMind, a multimodal generative GFM pretrained with a dual-scale token/pixel objective that enables any-to-any cross-modal generation (Thinking-in-Modalities) to infer missing sensors at inference time. Rather than reporting a single leaderboard, we investigate the axes along which the two architectures actually differ - patch size, decoder complexity, finetuning regime, input modality, and model scale - across ten use cases spanning segmentation and regression in diverse domains, including climate disaster response, methane leak detection, snow monitoring, or sea ice mapping. We find that architectural design choices - patch size and decoder type in particular - explain more performance variance than model identity itself, that the two models embody complementary investment strategies (pretraining-time scale for TerraMind versus inference-time tokenisation for THOR), and that correctly interpreting results requires dataset-level characterisation. The resulting picture is not a single winner but a set of hypotheses and a diagnostic ablation methodology that we expect to generalise to future GFMs beyond THOR and TerraMind.

## 16. PertReason: A Knowledge-Grounded Benchmark and Framework for Cell-State-Conditioned Mechanistic Reasoning of Perturbation Effects

- Authors: Dongkwan Kim, Yiming Gao, Yining Yang, Yang Shen
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-21
- DOI: Unavailable
- Categories: cs.LG, q-bio.MN
- Relevance: 2.942924134569182
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.18777v1
- PDF: https://arxiv.org/pdf/2607.18777v1
- Local PDF: pdf/2026-07-23_16_PertReason_ A Knowledge-Grounded Benchmark and Framework for Cell-State-Conditioned Mechanistic Reasoning of Perturbatio.pdf

Evaluating machine learning in scientific domains requires separating correct predictions from correct reasons under realistic distribution shifts. We introduce PertReason, a knowledge-grounded benchmark and framework suite for cell-state--conditioned reasoning about perturbation effects. At its core, PertReasonQA is a benchmark that tests whether models can generate mechanistically faithful explanations while remaining robust to complex shifts, such as new cells and unseen perturbations. PertReasonQA combines single-cell genetic and chemical perturbation data across multiple cellular contexts with knowledge graphs, and dynamically conditions pathways on cell-specific basal states to avoid generic memorization. Evaluations on state-of-the-art models reveal systematic gaps between predictive accuracy and mechanistic reasoning. Specifically, these models exhibit failure modes largely invisible to standard benchmarks, such as deriving correct answers through flawed logic, ignoring cellular context, and generating directionally inconsistent mechanisms. As a reference probe of the benchmark, we present PertReasonLM, a large language model trained to align outcome predictions with context-specific mechanistic reasoning. Our model targets the identified failure modes by grounding rationales in context-specific pathways and tightening agreement between outcomes and mechanisms. Together, we provide a diagnostic framework for exposing and mitigating failures in faithful reasoning in data-rich scientific systems.

## 17. Attributes Should Come from Images, Not Class Names: Distribution-Conditioned Attribute Selection for Vision-Language Models

- Authors: Gautam Rajendrakumar Gare, Jia Shi, Zhiqiu Lin, Deepak Pathak, John Galeotti, Deva Ramanan
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-21
- DOI: Unavailable
- Categories: cs.CV, cs.AI, cs.LG, eess.IV
- Relevance: 2.89073934526793
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.18695v1
- PDF: https://arxiv.org/pdf/2607.18695v1
- Local PDF: pdf/2026-07-23_17_Attributes Should Come from Images, Not Class Names_ Distribution-Conditioned Attribute Selection for Vision-Language Mo.pdf

A popular route to interpretable zero-shot classification asks a large language model (LLM) to describe each class name and prompts CLIP with the resulting descriptors. We show that these descriptors carry little visual evidence of their own: removing the class name from the prompt collapses ImageNet accuracy from 59.5% to 15.5%. The diagnosis is that the descriptors are conditioned on the label rather than on the images, so they describe the concept in general and mislead exactly when the data shifts; an LLM insists that strawberries are red, but every strawberry in ImageNet-Sketch is a colorless line drawing. We therefore select attributes from the target image collection instead: we score a large attribute pool against the images in CLIP's joint embedding space and keep the top-scoring attributes per class. Selected this way, class-name-free attribute prompts reach 23.8% on ImageNet (against 15.5% for LLM descriptors), the gain holds on four shifted ImageNet variants, and reselecting from the LLM's own pool isolates the selection mechanism as the cause. With one image per class, the selected attributes outperform the prompt-tuning method CoOp by 3 points while fitting in under a minute instead of 14 hours, with no learned soft prompt to obscure the decision. Because the attribute set is chosen by the data, it doubles as a readable summary of a dataset, which we use to describe distribution shift in words.

## 18. Neural sampling from cognitive maps enables goal-directed imagination and planning

- Authors: Hui Lin, Yukun Yang, Rong Zhao, Giovanni Pezzulo, Wolfgang Maass
- Source: openalex
- Venue type: journal
- Journal: Nature Machine Intelligence
- Publication status: published
- Publication date: 2026-07-21
- DOI: https://doi.org/10.1038/s42256-026-01254-4
- Categories: Ferroelectric and Negative Capacitance Devices, Advanced Memory and Neural Computing, Neural Networks and Reservoir Computing
- Relevance: 2.8812548884659823
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://doi.org/10.1038/s42256-026-01254-4
- PDF: Unavailable
- Local PDF: Not downloaded

Abstract Artificial intelligence systems are becoming more intelligent, but at a very high cost in terms of energy consumption and training requirements. By contrast, our brains only require 20 W of energy, they learn online and they can instantly adjust to changing contingencies. This begs the question what data structures, algorithms and learning methods enable brains to achieve that, and whether these can be ported into artificial devices. We are addressing this question for a core feature of intelligence: the capacity to plan and solve problems, including new problems that involve states that were never encountered before. Here we examine three tools that brains are likely to use for achieving that: cognitive maps, stochastic computing and compositional coding. We integrate these tools into a transparent neural network model, and demonstrate its power for flexible planning and problem-solving. Importantly, this approach is suitable for implementation by in-memory computing and other energy-efficient neuromorphic hardware. In particular, it only requires self-supervised local synaptic plasticity that is suited for on-chip learning. Hence, a core feature of brain intelligence—the capacity to generate solutions to problems that were never encountered before—does not require deep neural networks or large language models, and can be implemented in energy-efficient edge devices.

## 19. Beyond Static Personas: Situational Personality Steering for Large Language Models

- Authors: Zesheng Wei, Mengxiang Li, Zilei Wang, Yang Deng
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.8668479901374697
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.958/
- PDF: https://aclanthology.org/2026.findings-acl.958.pdf
- Local PDF: pdf/2026-07-23_19_Beyond Static Personas_ Situational Personality Steering for Large Language Models.pdf

Personalized Large Language Models (LLMs) facilitate more natural, human-like interactions in human-centric applications. However, existing personalization methods are constrained by limited controllability and high resource demands. Furthermore, their reliance on static personality modeling restricts adaptability across varying situations. To address these limitations, we first demonstrate the existence of situation-dependency and consistent situation-behavior patterns within LLM personalities through a multi-perspective analysis of persona neurons. Building on these insights, we propose IRIS, a training-free, neuron-based Identify–Retrieve–Steer framework for advanced situational personality steering. Our approach comprises situational persona neuron identification, situation-aware neuron retrieval, and similarity-weighted steering. We empirically validate our framework on PersonalityBench and our newly introduced SPBench, a comprehensive situational personality benchmark. Experimental results show that our method surpasses best-performing baselines, demonstrating IRIS’s generalization and robustness to complex, unseen situations and different models architecture.

## 20. Rewarding the Rare: Uniqueness-Aware RL for Creative Problem Solving in LLMs

- Authors: Zhiyuan Hu, Yucheng Wang, Yufei He, Jiaying Wu, Yilun Zhao, See-Kiong Ng, Cynthia Breazeal, Anh Tuan Luu, Hae Won Park, Bryan Hooi
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.865537130553606
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1982/
- PDF: https://aclanthology.org/2026.findings-acl.1982.pdf
- Local PDF: pdf/2026-07-23_20_Rewarding the Rare_ Uniqueness-Aware RL for Creative Problem Solving in LLMs.pdf

Reinforcement learning (RL) has become a central paradigm for post-training large language models (LLMs), particularly for complex reasoning tasks, yet it often suffers from exploration collapse: policies prematurely concentrate on a small set of dominant reasoning patterns, improving pass@1 while limiting rollout-level diversity and gains in pass@k. We argue that this failure stems from regularizing local token behavior rather than diversity over sets of solutions. To address this, we propose Uniqueness-Aware Reinforcement Learning, a rollout-level objective that explicitly rewards correct solutions that exhibit rare high-level strategies. Our method uses an LLM-based judge to cluster rollouts for the same problem according to their high-level solution strategies, ignoring superficial variations, and reweights policy advantages inversely with cluster size. As a result, correct but novel strategies receive higher rewards than redundant ones. Across mathematics, physics, and medical reasoning benchmarks, our approach consistently improves pass@k across large sampling budgets and increases the area under the pass@k curve (AUC@K) without sacrificing pass@1, while sustaining exploration and uncovering more diverse solution strategies at scale. Code is in Software part under submission page.

## 21. DeepGuard: Secure Code Generation via Multi-Layer Semantic Aggregation

- Authors: Li Huang, Zhongxin Liu, Yifan Wu, Tao Yin, Dong li, Jichao Bi, Nankun Mu, Hongyu Zhang, Meng Yan
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.8654018289922316
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.907/
- PDF: https://aclanthology.org/2026.acl-long.907.pdf
- Local PDF: pdf/2026-07-23_21_DeepGuard_ Secure Code Generation via Multi-Layer Semantic Aggregation.pdf

Large Language Models (LLMs) for code generation can replicate insecure patterns from their training data. To mitigate this, a common strategy for security hardening is to fine-tune models using supervision derived from the final transformer layer. However, this design may suffer from a final-layer bottleneck: vulnerability-discriminative cues can be distributed across layers and become less detectable near the output representations optimized for next-token prediction. To diagnose this issue, we perform layer-wise linear probing. We observe that vulnerability-related signals are most detectable in a band of intermediate-to-upper layers yet attenuate toward the final layers. Motivated by this observation, we introduce DeepGuard, a framework that leverages distributed security-relevant cues by aggregating representations from multiple upper layers via an attention-based module. The aggregated signal powers a dedicated security analyzer within a multi-objective training objective that balances security enhancement and functional correctness, and further supports a lightweight inference-time steering strategy. Extensive experiments across five code LLMs demonstrate that DeepGuard improves the secure-and-correct generation rate by an average of 11.9% over strong baselines such as SVEN. It also preserves functional correctness while exhibiting generalization to held-out vulnerability types.

## 22. mllm-shap: A Shapley Value Explainability Platform for Text-Audio Multimodal Large Language Models

- Authors: Jakub Muszyński, Paweł Pozorski, Maria Ganzha
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.8645872613830403
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-demo.38/
- PDF: https://aclanthology.org/2026.acl-demo.38.pdf
- Local PDF: pdf/2026-07-23_22_mllm-shap_ A Shapley Value Explainability Platform for Text-Audio Multimodal Large Language Models.pdf

We present mllm-shap, an open-sourcePython platform for researchers and ML practitioners that extends Shapley value (SV)explainability from text-only large languagemodels to multimodal LLMs (MLLMs) thatjointly process text and audio. Buildingon the token-level SV framework introducedby TokenSHAP, mllm-shap addresses threechallenges absent in the text-only setting:(1) modality-aware coalition masking thathandles the coexistence of text tokens anddense audio encoder frames within a single input, (2) multi-turn conversation tracking withper-token role and modality metadata, and(3) audio token grouping via phonetic alignment that reduces the coalition space by 10–50 times. The platform ships as a pip-installablepackage implementing five SV estimation strategies – including a Complementary Contributions estimator with Neyman-optimal allocation that outperforms Monte Carlo baselines – together with an interactive web GUIfor real-time attribution visualization. Toour knowledge, mllm-shap is the first publicly available framework for complete, reproducible SV-based explainability of text-audioMLLMs. The package is MIT-licensed withfull source code on GitHub and a demonstration video included as supplementary material.

## 23. Making Large Language Models Efficient Dense Retrievers

- Authors: Yibin Lei, Shwai He, Ang Li, Andrew Yates
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.863966719564793
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.587/
- PDF: https://aclanthology.org/2026.acl-long.587.pdf
- Local PDF: pdf/2026-07-23_23_Making Large Language Models Efficient Dense Retrievers.pdf

Recent work has shown that directly fine-tuning large language models (LLMs) for dense retrieval yields strong performance, but their substantial parameter counts make them computationally inefficient. While prior studies have revealed significant layer redundancy in LLMs for generative tasks, it remains unclear whether similar redundancy exists when these models are adapted for retrieval tasks, which require encoding entire sequences into fixed representations rather than generating tokens iteratively. To this end, we conduct a comprehensive analysis of layer redundancy in LLM-based dense retrievers. We find that, in contrast to generative settings, MLP layers are substantially more prunable, while attention layers remain critical for semantic aggregation. Building on this insight, we propose EffiR, a framework for developing efficient retrievers that performs large-scale MLP compression through a coarse-to-fine strategy (coarse-grained depth reduction followed by fine-grained width reduction), combined with retrieval-specific fine-tuning. Across diverse BEIR datasets and LLM backbones, EffiR achieves substantial reductions in model size and inference cost while preserving the performance of full-size models.

## 24. DVMap: Fine-Grained Pluralistic Value Alignment via High-Consensus Demographic-Value Mapping

- Authors: Pengyun Zhu, Yuqi Ren, Zhen Wang, Lei Yang, Deyi Xiong
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.8636111110229923
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.909/
- PDF: https://aclanthology.org/2026.acl-long.909.pdf
- Local PDF: pdf/2026-07-23_24_DVMap_ Fine-Grained Pluralistic Value Alignment via High-Consensus Demographic-Value Mapping.pdf

Current Large Language Models (LLMs) typically rely on coarse-grained national labels for pluralistic value alignment. However, such macro-level supervision often obscures intra-country value heterogeneity, yielding a loose alignment.We argue that resolving this limitation requires shifting from national labels to multi-dimensional demographic constraints, which can identify groups with predictable, high-consensus value preference. To this end, we propose DVMap (High-Consensus Demographic-Value Mapping), a framework for fine-grained pluralistic value alignment. In this framework, we first present a demographic archetype extraction strategy to construct a high-quality value alignment corpus of 56,152 samples from the World Values Survey (WVS) by strictly retaining respondents with consistent value preferences under identical demographics. Over this corpus, we introduce a Structured Chain-of-Thought (CoT) mechanism that explicitly guides LLMs to reason about demographic-value correlations. Subsequently, we employ Group Relative Policy Optimization (GRPO) to achieve adaptive anchoring of value distributions. To rigorously evaluate generalization, we further establish a triple-generalization benchmark (spanning cross-demographic, cross-country, and cross-value) comprising 21,553 samples. Experimental results demonstrate that DVMap effectively learns the manifold mapping from demographics to values, exhibiting strong generalization and robustness. On cross-demographic tests, Qwen3-8B-DVMap achieves 48.6% accuracy, surpassing the advanced open-source LLM DeepSeek-v3.2 (45.1%). The source code and dataset are available at https://github.com/EnlightenedAI/DVMap.

## 25. VFA: Empowering Multilingual MLLMs via Vision-Free Adaptation

- Authors: Yixia Li, Yaqing Shi, Zhiwen Ruan, Dongdong Zhang, Lingjie Jiang, Shaohan Huang, Yun Chen, Guanhua Chen, Furu Wei
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.86360102600458
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.407/
- PDF: https://aclanthology.org/2026.acl-long.407.pdf
- Local PDF: pdf/2026-07-23_25_VFA_ Empowering Multilingual MLLMs via Vision-Free Adaptation.pdf

Multimodal large language models have advanced rapidly, yet most remain English-centric, as scaling multilingual multimodal instruction tuning is limited by the scarcity and high cost of high-quality non-English image–text supervision. Although multilingual text data is abundant, naive textual fine-tuning can disrupt vision–language alignment and induce catastrophic forgetting. We propose Vision-Free Adaptation (VFA), a framework that decouples multilingual language enhancement from visual alignment by composing complementary task vectors over a shared LLM backbone. Specifically, we fine-tune a base LLM on multilingual text data to derive a multilingual task vector, which is then merged with the vision-aligned task vector of an MLLM. Experiments on five MLLMs across six multilingual multimodal benchmarks show consistent improvements while preserving both general multimodal and text-only capabilities. Moreover, VFA attains competitive performance with a fully multimodally trained model using less than 2% of the text data, demonstrating its efficiency and effectiveness.

## 26. Accelerating Prefilling via Decoding-time Contribution Sparsity

- Authors: Zhiyuan He, Yike Zhang, Chengruidong Zhang, Huiqiang Jiang, Yuqing Yang, Lili Qiu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.8633851891221216
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.801/
- PDF: https://aclanthology.org/2026.findings-acl.801.pdf
- Local PDF: pdf/2026-07-23_26_Accelerating Prefilling via Decoding-time Contribution Sparsity.pdf

Large Language Models (LLMs) incur quadratic attention complexity with input length, creating a major time bottleneck in the prefilling stage. Existing acceleration methods largely exploit attention score sparsity by estimating blocks with high attention scores and applying dynamic sparse attention. In this work, we identify another untapped form of sparsity in the prefilling stage, namely decoding-time contribution sparsity, where many attention blocks exhibit nontrivial attention scores during prefilling yet contribute negligibly to subsequent decoding. Building on this observation, we propose TriangleMix, which replaces dense attention with Triangle attention in a subset of layers. Extensive experiments demonstrate that TriangleMix achieves near-lossless performance on both long-context and long-context reasoning benchmarks, while significantly improving efficiency. For 128K inputs, Triangle attention in the subset of layers achieves a 15.3 × speedup in attention kernel computation, significantly exceeding the acceleration of typical dynamic sparse methods ( 1.9 × to 3.4 × ). Furthermore, TriangleMix can be seamlessly combined with dynamic sparsity approaches, delivering an additional 6%–19% reduction in TTFT over using dynamic sparsity alone.

## 27. Towards Efficient and Effective Diffusion Language Model Inference via Semantic-Aware Adaptive Denoising

- Authors: Fan Li, Yu Gu, Zhigang Wang, Fangling Leng, Zhenghao Liu, Ge Yu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.863105193006585
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.819/
- PDF: https://aclanthology.org/2026.acl-long.819.pdf
- Local PDF: pdf/2026-07-23_27_Towards Efficient and Effective Diffusion Language Model Inference via Semantic-Aware Adaptive Denoising.pdf

Diffusion language models (DLMs) have emerged as a powerful non-autoregressive alternative to GPT-style sequential generation, but suffer from substantial computational overhead due to their iterative parallel denoising. Existing acceleration works cannot accurately detect semantically stabilized tokens and then skip computation, leading to sub-optimal speedup in practice. This paper presents the first systematic study of convergence dynamics in DLMs. Innovative observations include the misalignment between traditionally used scalar detection criterion and the semantic convergence, and the post-peak confidence score, that wastes denoising computation and degrades inference quality. To address these limitations, we propose Ada-DLM, a semantic-aware adaptive denoising framework that encodes the trajectory of scalar confidence scores into an evolution-aware feature vector and then clusters vectors proactively and adaptively identify semantically converged tokens. Furthermore, we incorporate system-level optimizations to maximize runtime efficiency. Experiments show that Ada-DLM consistently outperforms the SOTA competitor, achieving up to 2x speedup and 19% quality improvement. That offers a practical path toward efficient high-quality DLM deployment.

## 28. Explainable and Fine-Grained Safeguarding of LLM Multi-Agent Systems via Bi-Level Graph Anomaly Detection

- Authors: Junjun Pan, Yixin Liu, Rui Miao, Kaize Ding, Yu Zheng, Quoc Viet Hung Nguyen, Alan Wee-Chung Liew, Shirui Pan
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.861645154988697
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1407/
- PDF: https://aclanthology.org/2026.acl-long.1407.pdf
- Local PDF: pdf/2026-07-23_28_Explainable and Fine-Grained Safeguarding of LLM Multi-Agent Systems via Bi-Level Graph Anomaly Detection.pdf

Large language model (LLM)-based multi-agent systems (MAS) have shown strong capabilities in solving complex tasks. As MAS become increasingly autonomous in various safety-critical tasks, detecting malicious agents has become a critical security concern. Although existing graph anomaly detection (GAD)-based defenses can identify anomalous agents, they mainly rely on coarse sentence-level information and overlook fine-grained lexical cues, leading to suboptimal performance. Moreover, the lack of interpretability in these methods limits their reliability and real-world applicability. To address these limitations, we propose , an explainable and fine-grained safeguarding framework for detecting malicious agents in MAS. To incorporate both coarse and fine-grained textual information for anomalous agent identification, we utilize a bi-level agent encoder to jointly model the sentence- and token-level representations of each agent. A theme-based anomaly detector further captures the evolving discussion focus in MAS dialogues, while a bi-level score fusion mechanism quantifies token-level contributions for explanation. Extensive experiments across diverse MAS topologies and attack scenarios demonstrate robust detection performance and strong interpretability of XG-Guard.

## 29. Safety-Utility Conflicts Are Not Global: Surgical Alignment via Head-Level Diagnosis

- Authors: Wang Cai, Yilin Wen, Jinchang Hou, Du Su, Guoqiu Wang, Zhonghou Lv, Chenfu Bao, Yunfang Wu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.8616231702491532
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.340/
- PDF: https://aclanthology.org/2026.acl-long.340.pdf
- Local PDF: pdf/2026-07-23_29_Safety-Utility Conflicts Are Not Global_ Surgical Alignment via Head-Level Diagnosis.pdf

Safety alignment in Large Language Models (LLMs) inherently presents a multi-objective optimization conflict, often accompanied by an unintended degradation of general capabilities. Existing mitigation strategies typically rely on global gradient geometry to resolve these conflicts, yet they overlook Modular Heterogeneity within Transformers, specifically that the functional sensitivity and degree of conflict vary substantially across different attention heads. Such global approaches impose uniform update rules across all parameters, often resulting in suboptimal trade-offs by indiscriminately updating utility sensitive heads that exhibit intense gradient conflicts. To address this limitation, we propose Conflict-Aware Sparse Tuning (CAST), a framework that integrates head-level diagnosis with sparse fine-tuning. CAST first constructs a pre-alignment conflict map by synthesizing Optimization Conflict and Functional Sensitivity, which then guides the selective update of parameters. Experiments reveal that alignment conflicts in LLMs are not uniformly distributed. We find that the drop in general capabilities mainly comes from updating a small group of “high-conflict” heads. By simply skipping these heads during training, we significantly reduce this loss without compromising safety, offering an interpretable and parameter-efficient approach to improving the safety-utility trade-off.

## 30. Unlocking Multilingual Reasoning Capability of LLMs and LVLMs through Representation Engineering

- Authors: Qiming Li, Xiaocheng Feng, Yixuan Ma, Ruihan Chen, Zihe Tong, Zekai Ye, Xiachong Feng, Libo Qin, Haoyu Ren, Kun Chen, Yunfei Lu, Dandan Tu, Bing Qin
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.8613229011670094
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1138/
- PDF: https://aclanthology.org/2026.acl-long.1138.pdf
- Local PDF: pdf/2026-07-23_30_Unlocking Multilingual Reasoning Capability of LLMs and LVLMs through Representation Engineering.pdf

Large Language Models (LLMs) and Large Vision-Language Models (LVLMs) demonstrate strong reasoning capabilities, yet their performance in English significantly outperforms that in low-resource languages, raising fairness concerns in multilingual applications. Existing approaches either rely on costly multilingual training or employ prompting with external translation tools, both of which are resource-intensive and sensitive to translation quality. To address these limitations, we propose a training-free inference-time method to enhance Multilingual Reasoning capabilities via Representation Engineering (MRRE) without using any additional training data or tools. MRRE sequentially injects two precomputed vectors at specific layers during inference processing: cross-lingual reasoning enhancement vectors, which steer non-English reasoning representations toward English space to unlock multilingual reasoning, and target-language output anchoring vectors, which restore the distribution of the target language to preserve input–output language consistency. Comprehensive experiments across six advanced LLMs and LVLMs on four reasoning benchmarks demonstrate that MRRE consistently enhances non-English reasoning by an average gain of 5.48% and up to 7.54% in low-resource languages (e.g., Thai and Swahili), while improving input-output language consistency by 3.78%.
