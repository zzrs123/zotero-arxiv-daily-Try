# Paper Daily Reading - 2026-10-03

## 1. Higher-Order Positional Encodings for Graph Representation Learning

- Authors: Caleb Stam, Aagrim Hoysal, Sanjukta Krishnagopal
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-01
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.67960334544452
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.01903v1
- PDF: https://arxiv.org/pdf/2610.01903v1
- Local PDF: pdf/2026-10-03_01_Higher-Order Positional Encodings for Graph Representation Learning.pdf

Many real-world systems exhibit higher-order interactions among groups of entities that cannot be captured by pairwise relationships alone. Graph Transformers and Graph Neural Networks increasingly rely on positional encodings to enrich graph representations, yet existing positional encodings are computed solely from the original graph and therefore cannot directly capture observed higher-order interactions. Topological Deep Learning addresses this limitation by lifting graphs to simplicial complexes, but typically requires performing message passing or attention on higher-order neural network representations. We introduce a representation learning paradigm that enriches graph representations with higher-order topology through positional encodings, enabling standard graph learning models to exploit lifted incidence structure without modifying the backbone. We derive a theoretical characterization of the expressivity of higher-order positional encodings, proving that node-level operators induced by higher-order lifts can mix graph Laplacian frequencies in ways that scalar graph spectral filters cannot. Guided by this theory, we instantiate higher-order positional encodings using Hodge Laplacians derived from clique complexes. Experiments with Graph Transformers on ZINC and controlled synthetic benchmarks demonstrate improvements in predictive performance, while a fixed-1-skeleton experiment shows that the pipeline can transmit higher-order information when cells are supplied independently of the graph. Together, our results establish higher-order positional encodings as a principled bridge between graph positional encodings and topological deep learning.

## 2. Coupling Perception and Reasoning in Federated Multimodal Graph Foundation Models

- Authors: Zekai Chen, Xun Wu, Hailin Zhang, Xunkai Li, Yu Liu, Kairui Yang, Muyan Huang, Xuaner Chen, Rong-Hua Li, Guoren Wang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-24
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.62343208925937
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.00277v1
- PDF: https://arxiv.org/pdf/2610.00277v1
- Local PDF: pdf/2026-10-03_02_Coupling Perception and Reasoning in Federated Multimodal Graph Foundation Models.pdf

Federated multimodal graph foundation models (GFMs) aim to adapt pretrained multimodal models to decentralized graph data, where each client owns a private multimodal graph and cannot share raw information. These models typically combine a multimodal Encoder that extracts semantic evidence from heterogeneous modalities and a graph neural network (GNN) that performs relational reasoning over graph structures. However, existing federated GFM adaptation methods mainly update graph-side modules while keeping the multimodal Encoder frozen, limiting adaptation to \emph{how information is propagated} while fixing \emph{what information is extracted}. Through empirical studies, we reveal that Encoder and GNN adaptations are not independent: Encoder adaptation is affected by graph relations, while cross-client module swapping reveals substantial pairing sensitivity between separately parameterized Encoder and GNN updates. Motivated by this observation, we propose \textbf{FedCORE}, a federated adaptation framework that represents Encoder and GNN updates through a shared low-dimensional latent state. FedCORE jointly optimizes this core from multimodal and structural signals and performs federated evolution directly in the shared state space, preserving compatibility between perception and reasoning adaptations. Extensive experiments demonstrate that FedCORE reduces the Encoder--GNN pairing gap from $30.6$ to $5.9$, corresponding to an $80.7\%$ reduction over independent joint adaptation.

## 3. Graph Representation via Elements of Discrete Morse and Cobordism Theories

- Authors: Jennifer Rozenblit, Chenguang Yang, Yuxin Liu, Yuzhou Chen, Yulia Gel
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-01
- DOI: Unavailable
- Categories: cs.LG, math.GN
- Relevance: 3.5353983471738144
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.01937v1
- PDF: https://arxiv.org/pdf/2610.01937v1
- Local PDF: pdf/2026-10-03_03_Graph Representation via Elements of Discrete Morse and Cobordism Theories.pdf

Topology is, by its nature and design, suited to structure that is nonlinear, multiscale, and nonstationary - however, within machine learning, its use remains largely confined to topological data analysis. We advocate that tools from low-dimensional topology which have remained almost exclusively contained within the domain of pure mathematics (such as Morse theory) offer a strong, complementary, and yet virtually unexplored perspective on the hidden structure of data-generating processes and learning tasks built upon them. Here we introduce concepts from cobordism theory and harness tools from discrete Morse theory to improve the performance of graph diffusion models through our pipeline MG-Diff. Further, we derive theoretical guarantees and sufficient conditions so that under a positive decision-gap, the Morse-theoretic tools and their application for induced diffusion guidance are stable under small perturbations. Finally, we illustrate the utility of discrete Morse theory in application to graph diffusion models for spatio-temporal graph forecasting and graph regeneration, and argue that these applications are only a small window into the part of what low-dimensional topology can offer to the field of machine learning.

## 4. Structure-agnostic Causal Representation Learning

- Authors: Arman Behnam, Binghui Wang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-01
- DOI: Unavailable
- Categories: cs.LG, cs.AI
- Relevance: 3.4741232470393992
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.00968v1
- PDF: https://arxiv.org/pdf/2610.00968v1
- Local PDF: pdf/2026-10-03_04_Structure-agnostic Causal Representation Learning.pdf

Causal representation learning aims to discover robust features by exploiting the causal structure underlying data generation. Existing methods require specifying the causal structure a priori, yet different structures demand fundamentally incompatible invariance constraints, and misspecification leads to representations that discard predictive information. We introduce SaCRL, a framework that jointly identifies the causal structure and learns the corresponding invariant representation without prior structural knowledge. Our approach formulates structure selection as a soft optimization over candidate invariances using HSIC-based violation metrics, with adaptive weights that automatically concentrate on the achievable structure. We provide theoretical guarantees for structure identification, including under random-feature approximation, invariance satisfaction, and out-of-distribution generalization. Empirically, SaCRL recovers the true structure on synthetic and semi-synthetic Bayesian-network benchmarks, outperforms fixed-invariance baselines on Colored MNIST, achieves state-of-the-art accuracy on three DomainBed benchmarks (PACS, VLCS, OfficeHome), and degrades gracefully under structural misspecification and limited environment diversity. Code is available at: https://github.com/ArmanBehnam/sacrl.

## 5. Let the Heads Talk: Beyond Diagonal Graph Attention

- Authors: Riccardo Ali, Alessio Borgi, Mario Severino, Alessio Gravina, Davide Bacciu, Pietro Liò, Christopher Irwin
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-01
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.340672435134322
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.01494v1
- PDF: https://arxiv.org/pdf/2610.01494v1
- Local PDF: pdf/2026-10-03_05_Let the Heads Talk_ Beyond Diagonal Graph Attention.pdf

Sheaf Neural Networks generalize scalar-weighted message passing by replacing scalar edge weights with linear transport maps between local feature spaces. Yet the role of this matrix-valued transport is entangled with the broader sheaf-diffusion construction. We isolate the transport primitive through quiver representations and establish a direct connection with multi-head attention. Treating attention heads as coordinates of a local transport space reveals that standard multi-head attention implements diagonal edge maps: along each directed interaction, a source head can contribute only to the corresponding receiver head. Allowing off-diagonal entries instead enables edge-conditioned communication across heads before neighborhood aggregation. We show that this operation cannot, in general, be absorbed into a single shared linear map applied after aggregation. Building on this characterization, we introduce Topological Attention (Top-A), a multi-head attention that learns edge-dependent off-diagonal routes while preserving the original same-head paths and exactly recovering vanilla attention when the additional routing vanishes. We evaluate Top-A on relational reasoning, heterogeneous graph learning, and algorithmic reasoning, including out-of-distribution generalization, with heterophilic node classification as a contrast setting. The results show that cross-head transport is most useful when the task benefits from interaction-dependent transformations, while heterophily alone provides no systematic advantage. These findings identify edge-conditioned cross-head communication as a distinct computational primitive of matrix-valued transport.

## 6. VANDAM: Viewing a nucleotide sequence with DNA molecular priors

- Authors: Jeremy Levy, Ariel Larey, Yury Nahshan, Raizy Kellerman, Elay Dahan, Amit Bleiweiss, Guy Leib, Omri Nayshool, Dan Ofer, Tal Zinger, Dan Dominissini, Gideon Rechavi, Marissa Wirth, Simon Lee, Dung Hoang, Noam D. Beckmann, Shane O'Connell, Nicole Bussola, Alexander W. Charney, Yoli Shavit, Nati Daniel
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-30
- DOI: Unavailable
- Categories: cs.LG, stat.ML
- Relevance: 3.3381567917041783
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.00411v1
- PDF: https://arxiv.org/pdf/2610.00411v1
- Local PDF: pdf/2026-10-03_06_VANDAM_ Viewing a nucleotide sequence with DNA molecular priors.pdf

Contemporary Genomic Foundation Models (GFMs) rely on a DNA-as-a-string paradigm that employs masked token prediction objectives for pretraining. However, this abstraction does not explicitly model the biochemical, structural, and physical properties essential to biological function. Many molecular properties can be estimated from sequence using established biophysical models, so their utility lies not in providing an independent modality, but in introducing priors that training objectives can explicitly exploit. We introduce VANDAM, a framework that extends the training of GFMs with DNA molecular priors. In self-supervised training, VANDAM predicts regional molecular properties from pooled representations. When functional labels are available and can reward retaining molecular priors, local features are additionally injected at the input. VANDAM consistently improves downstream performance across four architecture families and nine held-out genomic tasks by complementing token-based objectives. Probing experiments further demonstrate that the use of molecular priors generalizes to other unseen molecular properties.

## 7. CPathOGen: Spatially and Morphologically Controlled H&E Counterfactuals for Probing Pathology Models

- Authors: Samarth Singhal, Varang Rai
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-30
- DOI: Unavailable
- Categories: eess.IV, q-bio.QM
- Relevance: 3.3091711200862415
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.00602v1
- PDF: https://arxiv.org/pdf/2610.00602v1
- Local PDF: pdf/2026-10-03_07_CPathOGen_ Spatially and Morphologically Controlled H&E Counterfactuals for Probing Pathology Models.pdf

Computational pathology models infer biologically and clinically meaningful outcomes from histology, but their predictions are shaped by complex, intertwined tissue signals whose roles are important to understand. Common pixel- and feature-space perturbations can produce implausible tissue, making model responses difficult to interpret. We introduce CPathOGen, a conditional latent-diffusion framework for generating paired H\&E counterfactuals with explicit controls over cellular spatial organization, nuclear morphology, and stain appearance. Cellular maps condition spatial structure through a spatial encoder, while a morphology/appearance vector modulates denoising through blockwise feature-wise linear modulation (FiLM). On held-out H\&E tiles, CPathOGen generates visually plausible tissue with improved distributional agreement after spatially guided selection, as reflected by lower Fréchet Inception Distance (FID) and Kernel Inception Distance (KID); generated cells track requested abundance and position, and measured morphology and color vary monotonically with their controls. We use these verified interventions to probe pathology encoders with endpoint heads, task-specific classifiers, and survival models. Responses are quantified using total variation distance and prediction-flip rate. We further introduce the Biology-Nuisance Sensitivity Ratio, a metric that contrasts model sensitivity to biologically motivated morphology and spatial factors with sensitivity to non-biological, stain-related nuisance variation. CPathOGen provides a practical, fidelity-audited framework for evaluating robustness and controlled feature sensitivity in computational pathology model. \href{https://github.com/a12dongithub/PathOGen}{GitHub} and \href{https://huggingface.co/a12donhf/CPathOGen}{Hugging~Face}.

## 8. Sample complexity bounds for categorical Markov random fields via Discrete Diffusions

- Authors: Shivam Kumar, Nabarun Deb
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-01
- DOI: Unavailable
- Categories: math.ST, cs.LG, stat.ML
- Relevance: 3.298237176564297
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.02128v1
- PDF: https://arxiv.org/pdf/2610.02128v1
- Local PDF: pdf/2026-10-03_08_Sample complexity bounds for categorical Markov random fields via Discrete Diffusions.pdf

Many applications in statistics, economics, and physics require sampling from high-dimensional categorical distributions with local dependence structures. Examples include finite memory language models, Ising and Potts systems in statistical physics and protein folding, etc. In modern machine learning, discrete diffusions have emerged as a flexible approach for sampling such data, with strong empirical performance. Motivated by this, we develop learning methods with end-to-end sample complexity bounds for discrete diffusion with uniform noising under local dependence, which we model through low order Markov random fields (MRFs). Our main technical insight is a new \emph{pinning decomposition} of the discrete score. It shows that unlike in continuous diffusions, the score decomposes into components where the dependence on time separates multiplicatively from the dependence on the target. Building on this decomposition, we propose a \emph{weight-sharing neural score learner} and combine it with $τ$-leaping to obtain an end-to-end sampling procedure. Rather than treating score-learning error as a black-box input, as is common in existing sampling analyses, we study the score learning error from finite data and derive optimal sampling guarantees with explicit dependence on the vocabulary size, the interaction order of the MRF, and the sample size. Moreover, our strategy trains a single score network across uniform noise levels while leaving the sampling discretization to be chosen at inference-time. This allows the same trained model to trade accuracy for computational cost as inference-time budgets vary. Numerical experiments on Potts, Ising, and tree-structured models show that weight-sharing score networks outperform fully connected ones for sampling long sequences.

## 9. Geometric Similarity in VLM Low-Level Vision Representations

- Authors: Shao-Jun Xia, Huixin Zhang, Zhen Lei, Anlan Sun, Yuner Zhang, Xiaoyang Chen
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-01
- DOI: Unavailable
- Categories: cs.CV, cs.AI
- Relevance: 3.2824409819518
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.00848v1
- PDF: https://arxiv.org/pdf/2610.00848v1
- Local PDF: pdf/2026-10-03_09_Geometric Similarity in VLM Low-Level Vision Representations.pdf

Vision-language models (VLMs) have emerged as powerful candidates for universal vision backbones, with representative architectures including autoregressive (AR) models and diffusion transformers (DiTs). Yet, adapting them efficiently for all-in-one low-level image restoration remains a challenge. Crucially, the field lacks an understanding of how VLMs organize hidden-layer representations and whether these structurally distinct paradigms share a common geometric organization for pixel-level perception. Such shared organization is a prerequisite for building highly transferable, unified restoration VLMs and adapters. In this paper, we systematically investigate representational similarity across 24 low-level tasks spanning 5 categories. We propose GeoSim, a unified four-level framework that analyzes task-conditioned representations from global similarity, local geometry, sparse feature decomposition, and topological verification perspectives. Our formulation applies to the analysis of hidden states in AR models and feature maps in DiTs across same- and cross-task/model settings. Our results reveal the organizing principles of low-level visual representations while exposing their limits in cross-task and cross-model agreement. Ultimately, GeoSim provides an interpretability lens for probing latent transferability in low-level vision and diagnosing model limitations in task- or model-specific scenarios.

## 10. Beyond Linear Concepts: Discovering and Aligning Non-Linear Concept Manifolds in Large Language Models

- Authors: Tido Specht, Elias Benedict Krey, Nils Neukirch, Nils Strodthoff
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-01
- DOI: Unavailable
- Categories: cs.LG, cs.CL
- Relevance: 3.2640024832736527
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.01821v1
- PDF: https://arxiv.org/pdf/2610.01821v1
- Local PDF: pdf/2026-10-03_10_Beyond Linear Concepts_ Discovering and Aligning Non-Linear Concept Manifolds in Large Language Models.pdf

Understanding information processing in large language models (LLMs) requires dissecting the geometric organization of their internal token representations. While existing mechanistic interpretability (MI) methods seek to extract concepts, they are constrained by a strong linearity assumption challenged by evidence of non-linear feature manifolds. We move beyond linear concepts by adapting Non-Linear Multi-Dimensional Concept Discovery (NLMCD) from computer vision to token-level LLM activations, modeling concepts as low-dimensional manifolds. To compare concept manifolds across layers and models, we introduce a concept-based alignment (CBA) score, a generalized Rand index that measures geometric proximity without explicit feature matching. Our analysis yields six key findings: (i) a neighboring-layer sanity check shows CBA is more sensitive than PCA- or CKA-based linear baselines; (ii) layer-by-layer alignment matrices reveal two block structures in intermediate and late layers, consistent across models and obscured by linear metrics; (iii) concept composition remains syntax-dominated through most of the network before giving way to increasingly mixed syntactic-semantic concepts in later layers, with increasing output-orientation toward the final layers; (iv) multilingual concept sharing between English and Mandarin is training-dependent rather than universal, strongest in Qwen, weaker in Llama, and absent in GPT-2; (v) inter-model alignment mirrors this structure, with strong correspondence between same-family Qwen models of different scale but weak alignment across model families; and (vi) across Tulu-3 training stages, alignment is highest between adjacent stages, with the largest shift between the base model and SFT, while subsequent preference-alignment stages (DPO, RLVR) leave early layers largely unchanged and RLVR mostly preserves DPO's concepts in late layers.

## 11. RelICL: Training-free Relational Learning with Tabular Foundation Models

- Authors: Simon Forbat, Rainer Gemulla
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-01
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.251671735750228
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.01725v1
- PDF: https://arxiv.org/pdf/2610.01725v1
- Local PDF: pdf/2026-10-03_11_RelICL_ Training-free Relational Learning with Tabular Foundation Models.pdf

Tabular foundation models achieve state-of-the-art performance on single-table tasks without any training. Recent work suggests that they are also well-suited for relational learning via deep feature synthesis (DFS), which flattens a relational schema into a single table by adding aggregates of the other tables' columns as features. This approach is appealing because it directly benefits from improvements to or customization of the underlying tabular foundation model. In this paper, we identify two key problems with DFS: feature explosion and interaction blindness. The first problem arises because the number of DFS features grows quickly as the schema becomes more complex, limiting scalability and performance. The second problem arises because column-wise aggregates do not account for feature interactions, limiting performance. We propose and explore an alternative method termed RelICL, which keeps the benefits of DFS but alleviates these two problems. At its heart, RelICL propagates and fuses information step by step through the schema graph, using the same tabular foundation model that is eventually used for prediction to do so. In our experimental study using RelBench tasks, RelICL was on par with the strongest approach based on deep feature synthesis.

## 12. RelationVGGT: Visual Geometry Transformers for 3D Spatial Relation Segmentation

- Authors: Minsu Kim, Jaesung Choe, Jiwoo Lee, Yu-Chiang Frank Wang, Seon Joo Kim
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-01
- DOI: Unavailable
- Categories: cs.CV, cs.AI
- Relevance: 3.2328851110505816
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.00970v1
- PDF: https://arxiv.org/pdf/2610.00970v1
- Local PDF: pdf/2026-10-03_12_RelationVGGT_ Visual Geometry Transformers for 3D Spatial Relation Segmentation.pdf

Recent advances in 3D reconstruction have progressed from per-scene optimization to feed-forward inference, and semantic scene understanding has followed suit -- yet existing methods remain confined to object-centric perception, neglecting spatial relations between objects. We formulate 3D spatial relation segmentation in a feed-forward, pose-free multi-view setting: given a visually specified subject and a relational text query, the model segments the target across views without receiving its category name. To this end, we propose RelationVGGT, a novel feed-forward framework that integrates semantic features from a visual foundation model with geometry-aware representations from a 3D geometry foundation model and leverages a relation transformer for subject-conditioned, cross-view relation prediction -- requiring neither per-scene optimization nor known camera poses. We additionally provide a fully automated annotation pipeline built on ScanNet++ with VLMs and LLMs, enabling scalable training data generation for this new task.

## 13. Mapping the RAG Landscape: A Four Axis Taxonomy of Efficiency, Defense, Interactivity, and Reasoning

- Authors: Meghana Sunil, Shravya V, Shravan Venkatraman, Joe Dhanith PR
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-01
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 3.1912034924513004
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.01936v1
- PDF: https://arxiv.org/pdf/2610.01936v1
- Local PDF: pdf/2026-10-03_13_Mapping the RAG Landscape_ A Four Axis Taxonomy of Efficiency, Defense, Interactivity, and Reasoning.pdf

Large Language Models (LLMs) have demonstrated remarkable fluency across many tasks but remain limited by their static, parameter bound knowledge and their susceptibility to hallucinating information. Retrieval Augmented Generation (RAG) addresses these issues by incorporating external retrieval into the generation process, grounding model outputs in verifiable and up to date sources. While prior surveys primarily focus on core RAG architectures and standard pipelines, recent research explores broader challenges and capabilities that extend beyond these foundational designs. This survey provides a consolidated and structured examination of contemporary RAG developments, organizing the field into a four axis taxonomy: improving retrieval efficiency, strengthening robustness and security, supporting user driven and interactive workflows, and enabling multi step or complex reasoning. We formalize key components of the RAG framework and review methods spanning dense and sparse retrieval, fusion strategies, embedding optimizations, and reinforcement learning based retrieval policies, highlighting how these advances influence practical deployment and system design. We also synthesize evaluation practices, domain specific applications, and architectural variants such as Naive, Advanced, and Modular RAG. Finally, we outline persistent challenges related to retrieval quality, reliability, domain adaptation, scalability, and explainability, and identify opportunities for building RAG systems that are more reliable, adaptable, and transparent.

## 14. Higher-Order Molecular Grammars for Generative and Foundation Models in Chemistry

- Authors: Yiming Huang, Yujie Zeng, Vijay Prakash Dwivedi, Simone Foti, Jianmin Wang, Jure Leskovec, Tolga Birdal
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-01
- DOI: Unavailable
- Categories: cs.LG, cs.AI
- Relevance: 3.160869927292853
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.02186v1
- PDF: https://arxiv.org/pdf/2610.02186v1
- Local PDF: pdf/2026-10-03_14_Higher-Order Molecular Grammars for Generative and Foundation Models in Chemistry.pdf

Molecular learning models are strongly shaped by their underlying representations. Yet standard sequential and graph formalisms struggle to explicitly encode higher-order topology, such as ring systems and recurring motifs. Existing higher-order representations can capture these structures directly, but they are often computationally demanding and difficult to decode into valid molecules. Here, we introduce Higher-order Grammar Representation (HGR), a principled, topology-aware framework that lifts molecules to combinatorial complexes and parses each complex into a compact sequence of production rules under a context-free higher-order grammar. By serialising higher-order topology into rule sequences, HGR makes these structures directly compatible with standard sequence models, avoiding the computational overhead of explicit higher-order encodings while preserving topological expressiveness. To reduce benchmark bias towards simple ring systems, we construct RingDiv, a ring-enriched benchmark containing 1.18 million molecules, including the curated RingDiv300k subset, and introduce the ring diversity index (RDI) to quantify ring-system coverage. In molecular generation, HGR-based models uniquely combine 100% validity by construction with leading distributional alignment, ranking first in FCD on all five generation benchmarks. In representation learning, HGR-FM achieves the highest mean AUC across seven MoleculeNet benchmarks under both transfer protocols, improving on the strongest baseline by 8.3 and 3.3 AUC points under probing and full fine-tuning, respectively. Collectively, these results establish HGR as an efficient higher-order representation for molecular generation and transferable representation learning.

## 15. Temporally-Resolved Token Attribution Reveals the Generation Dynamics of Diffusion Language Models

- Authors: Darpan Aswal, Céline Hudelot
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-01
- DOI: Unavailable
- Categories: cs.CL, cs.AI, cs.LG
- Relevance: 3.106565804890077
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.01177v1
- PDF: https://arxiv.org/pdf/2610.01177v1
- Local PDF: pdf/2026-10-03_15_Temporally-Resolved Token Attribution Reveals the Generation Dynamics of Diffusion Language Models.pdf

This work presents Diffusion Layer Integrated Gradients (DLIG), a token attribution method for diffusion language models (DLMs) that extends Integrated Gradients (IG~\cite{sundararajan2017axiomatic}) to arbitrary layers and denoising steps. DLIG attributes a DLM's progressive commitment to a self-generated or fixed completion for an input prompt. We establish direct correspondences between DLIG and the IG axioms of completeness, implementation invariance, linearity, and symmetry preservation. As a lightweight complement to interventional analysis, DLIG provides an inexpensive first check of mechanistic hypotheses across the denoising trajectory. We demonstrate this on word-sense disambiguation, multi-hop graph reasoning, and sentence infilling, revealing how DLMs draw on inputs across positions, layers, and denoising steps.

## 16. From Task Mixtures to Specialized Experts

- Authors: Hojat Allah Salehi, Mehrdad Mahdavi, Andrew Arash Mahyari, M. Hadi Amini
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-30
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.0930845520636363
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.00580v1
- PDF: https://arxiv.org/pdf/2610.00580v1
- Local PDF: pdf/2026-10-03_16_From Task Mixtures to Specialized Experts.pdf

In collaborative foundation model fine-tuning, client data is rarely homogeneous. Instead, clients typically possess unknown mixtures of distinct data distributions, or tasks. Conventional federated learning primarily addresses heterogeneity across clients without explicitly resolving latent task mixtures within each client. We study this setting as compound heterogeneity, where data is heterogeneous both across and within clients. We study adaptation over a common frozen representation and show that, when tasks share the same feature geometry, the optimal model for a client's task mixture under squared loss is a convex combination of the optimal models for its underlying tasks. Thus, a single locally trained model represents the client's overall task mixture, while individual inputs may be drawn from different underlying task distributions. This motivates routing inputs to specialized experts, and we show that, when the task optima form a simplex, task-aligned routing achieves lower risk than any single adapted model for genuinely mixed clients. With access to a small set of task-labeled public samples, we derive a convex program to recover task experts and match them to their corresponding tasks. Our routing analysis shows that effective specialization requires input-dependent expert selection aligned with each client's task mixture. Motivated by this analysis, we propose FedSEE. Across our experiments, FedSEE avoids the negative transfer observed in the evaluated baselines and improves performance by 2.9 points overall and 3.7 points for the worst-served quartile.

## 17. Initialization Improves LLM-Driven Discovery

- Authors: Mansi Sakarvadia, Marco Ciccone, Colin Raffel
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-30
- DOI: Unavailable
- Categories: cs.LG, cs.AI, cs.CL
- Relevance: 3.090806616670597
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.00707v1
- PDF: https://arxiv.org/pdf/2610.00707v1
- Local PDF: pdf/2026-10-03_17_Initialization Improves LLM-Driven Discovery.pdf

Large Language Models (LLMs) have been used for novel discovery of algorithms, theorems, drugs, and other tasks through the use of harnesses that prompt an LLM to iteratively optimize an objective. In this work, we study the relationship between the population of previous iterates and eventual discovery success. We generalize past work on harness design to develop a suite of 12 harnesses called 'Modular' and characterize their performance across 5 diverse discovery tasks, finding that discovery success is brittle and sensitive to harness design. We uncover mode collapse, characterized by a dramatic drop in the diversity of iterates, as a common failure mode. We find that popular state-of-the-art harnesses and diversity-inducing harness interventions, which aim to prolong this collapse, yield inconsistent gains. Our results instead uncover that the performance of early discoveries is predictive of eventual success. We therefore propose a universally applicable intervention that performs an initial stage of parallel exploration in order to initialize subsequent iterative optimization. Our method provides consistent gains across many harnesses and target applications, confirming the importance of initialization in LLM-driven discovery.

## 18. Fixed-point neural samplers on discrete spaces

- Authors: Jiajun He, Denis Blessing, Mouyang Cheng, Yuanqi Du, Carles Domingo-Enrich
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-01
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.076270037872595
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.01739v1
- PDF: https://arxiv.org/pdf/2610.01739v1
- Local PDF: pdf/2026-10-03_18_Fixed-point neural samplers on discrete spaces.pdf

Sampling from discrete, unnormalized distributions without access to data is a challenging problem. Neural samplers offer a promising approach by training generative models from density evaluations directly. Despite recent progress, existing discrete neural samplers are prone to mode collapse, come without convergence guarantees when trained via fixed-point iterations, and are often tied to a specific reference process such as masked or uniform diffusion. In this work, we introduce Discrete Gibbs Iterative Neural Sampler, a fixed-point neural sampler that addresses these limitations, enabling efficient, scalable learning, substantially reducing mode collapse in practice. Our framework builds on masked diffusion and also extends to transport between pairs of distributions. We demonstrate that the resulting method scales effectively to high-dimensional systems, supports amortized sampling across different conditions, and enables accurate estimation of alloy phase diagrams.

## 19. Where-OPD: Spatially Guided On-Policy Self-Distillation of MLLMs with Synthetic Scenes

- Authors: Sophia Sirko-Galouchenko, Monika Wysoczanska, Andrei Bursuc, Nicolas Thome, Spyros Gidaris
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-01
- DOI: Unavailable
- Categories: cs.CV, cs.AI, cs.CL, cs.LG
- Relevance: 3.049481959542913
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.02117v1
- PDF: https://arxiv.org/pdf/2610.02117v1
- Local PDF: pdf/2026-10-03_19_Where-OPD_ Spatially Guided On-Policy Self-Distillation of MLLMs with Synthetic Scenes.pdf

On-policy self-distillation has recently emerged as an effective approach for improving language-model reasoning by supervising students with a frozen or EMA version of themselves that receives privileged information. Its application to multimodal large language models (MLLMs), however, remains largely unexplored. Recent approaches use privileged visual information, such as image crops corresponding to a question, to improve fine-grained perception, but their gains are confined to tasks that benefit from such visual zooming and require either human-annotated grounding data or external teacher models. We introduce a different form of on-policy self-distillation for MLLMs that provides the teacher with textual, spatially grounded guidance identifying the visual elements relevant to a query. We use procedurally generated scenes with automatically available object identities and spatial coordinates, enabling scalable and annotation-free post-training. The teacher uses this spatial guidance to locate and integrate evidence from multiple relevant image regions, while the student learns to reproduce the resulting behavior from the image and question alone. Our approach consistently improves performance on counting, document and chart understanding benchmarks across multiple models. Importantly, although post-training uses only synthetic scenes, the resulting improvements transfer to real-world perception benchmarks, yielding a 3.23-point gain in average performance across CVBench, V*, ZoomBench, BLINK, HR-Bench, and MME-RealWorld. These results show that spatially grounded privileged information can induce broader perceptual capabilities through on-policy self-distillation, enabling substantial synthetic-to-real transfer beyond the task and data distribution used for post-training. Project page: https://github.com/sirkosophia/Where-OPD

## 20. From Knowledge Access to Source Learning: Developing Source-Specific Competence

- Authors: Lucheng Fu, Kejing Xia, Yiyang Wang, Yiqiao Jin, Jinjin He, Xiyuan Yang, Haoxin Liu, Ye Yu, Haibo Jin, Yijia Xiao, Wenke Lee, B. Aditya Prakash, Haohan Wang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-01
- DOI: Unavailable
- Categories: cs.CL, cs.AI, cs.LG
- Relevance: 3.045001168714032
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.02150v1
- PDF: https://arxiv.org/pdf/2610.02150v1
- Local PDF: pdf/2026-10-03_20_From Knowledge Access to Source Learning_ Developing Source-Specific Competence.pdf

Large language model (LLM) agents increasingly rely on persistent external sources to solve sequences of knowledge-intensive tasks. Existing methods improve how source content is accessed and organized, while agent-memory systems preserve reusable knowledge from prior interactions, but repeated use of the same source is still largely treated as repeated access rather than an opportunity to progressively improve understanding of that source. We study source learning: developing reusable source-specific competence over a persistent authoritative source. We represent this competence with a persistent source model that captures reusable understanding of the source, including how its knowledge is structured, interpreted, and applied. To construct and progressively refine such models, we propose SourceLearn, which combines two complementary learning mechanisms. Self-Directed Source Learning identifies what remains incompletely understood and adaptively revisits the source, while Task-Guided Source Learning uses downstream experience to reveal local representational gaps and recurring needs in how source knowledge should be organized. In both cases, learning signals determine what should be reconsidered, while persistent updates are reconstructed from the authoritative source. Across five benchmarks and three LLM backends, SourceLearn achieves the best performance in 13 of 15 settings, with gains of up to 22.6 points over Hybrid RAG and substantial overall improvements over static source representations and experience-based memory baselines.

## 21. STEER: Reducing Inference Cost in Relational Foundation Models through Semantically Informed Sampling

- Authors: Abdalla Mohamed, Ashraf Aboulnaga
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-01
- DOI: Unavailable
- Categories: cs.DB, cs.LG
- Relevance: 3.044562417301609
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.00907v1
- PDF: https://arxiv.org/pdf/2610.00907v1
- Local PDF: pdf/2026-10-03_21_STEER_ Reducing Inference Cost in Relational Foundation Models through Semantically Informed Sampling.pdf

Relational foundation models (RFMs) are pretrained once on a collection of relational databases and prediction tasks, and then applied zero-shot to previously unseen databases and tasks. To make a prediction for a target row, an RFM samples a neighborhood of rows linked to that row through foreign keys and uses this neighborhood as its inference context. Lowering inference cost is an important goal for any foundation model, and for RFMs this cost grows with the size of the context. The simplest ways to shrink the context is to drop some of the sampled rows, but this ignores the semantics of the database schema, so it is as likely to discard informative rows as uninformative ones. We propose STEER, a sampling approach that shrinks the inference context by concentrating it on the tables most relevant to the prediction task at hand. STEER obtains relevance information by prompting a large language model to rank the foreign-key edges of the database schema into relevance tiers for the given task, and then maps each tier to a probability of following that edge during traversal. Because the ranking uses only the schema, it is computed once per task and reused across all subsequent predictions, amortizing its cost. We evaluate STEER on three state-of-the-art RFMs (RT, RT-J, and Griffin) and show that it reduces inference context size by about 40% on average while maintaining, and in some cases improving, prediction accuracy.

## 22. Towards Fast and Disentangled Counterfactuals for Visual Foundation Models

- Authors: Sidney Bender, Benedikt Kunz, Ahmed Zeid, Shinichi Nakajima, Klaus-Robert Müller, Marco Morik
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-01
- DOI: Unavailable
- Categories: cs.LG, cs.CV
- Relevance: 3.037468262790037
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.00895v1
- PDF: https://arxiv.org/pdf/2610.00895v1
- Local PDF: pdf/2026-10-03_22_Towards Fast and Disentangled Counterfactuals for Visual Foundation Models.pdf

Foundation models remain vulnerable to spurious correlations and ``Clever Hans'' strategies. Explainable machine learning can find and remove such strategies for classifiers without metadata. For foundation models, no such option exists yet. We propose Disentangled Diffusion Autoencoders (DiDAE). DiDAE wraps a frozen foundation model in a conditional diffusion decoder. A counterfactual is one closed-form edit along a direction of a disentangled dictionary, followed by decoding. The dictionary can be supervised (Procrustes) or unsupervised (Singular Value Decomposition, Sparse Autoencoders). No gradients are needed, so DiDAE is up to 2000 times faster than the state of the art. We evaluate on six datasets, two synthetic and four real-world. In a desiderata-driven benchmark on three of them, its counterfactuals are on par with or better than the state of the art, and they repair downstream classifiers through Counterfactual Knowledge Distillation (CFKD), where they beat metadata-based correction. The same machinery can rank a pretrained dictionary against a trained classifier. It returns the few directions the classifier actually reads, each causally verified by a counterfactual that flips the decision, and repairs the classifier along those a teacher marks spurious. The workflow is plug-and-play in our open-source Peal library we publish alongside the paper. With a public dictionary and a pretrained decoder, all that remains is a cheap linear distillation of the classifier and its own fine-tuning.

## 23. Hierarchical Continuous Diffusion Language Models

- Authors: Hui Ren, Zihan Li, Chang Liu, Huidong Liu, Alexander Schwing
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-01
- DOI: Unavailable
- Categories: cs.CL, cs.AI, cs.LG
- Relevance: 3.034412836569743
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.02193v1
- PDF: https://arxiv.org/pdf/2610.02193v1
- Local PDF: pdf/2026-10-03_23_Hierarchical Continuous Diffusion Language Models.pdf

Discrete diffusion language models offer a compelling alternative to autoregressive generation for tasks demanding bidirectional reasoning and global constraint satisfaction. Yet they share a structural bottleneck: when decoding in parallel, each token is sampled independently from its marginal, severing the statistical dependencies among the tokens decoded together. Continuous diffusion language models avoid this by denoising a shared continuous state, but their denoiser sees only that state, so nothing ties it to a valid token configuration until it is finally decoded. To address this, we propose Hierarchical Continuous Diffusion Language Models (HC-DLM), which couple discrete token generation with a continuous latent trajectory in a single, principled denoising process, whose training objective is derived from a variational bound on the token likelihood. In contrast to recent methods that attach continuous context to a self-contained discrete chain, HC-DLM makes the latent the only persistent generative state: tokens are read out from it at every step and feed back as a scaffold for the next latent update. On structured reasoning (Sudoku), mathematical planning (Countdown) and language modeling (LM1B), HC-DLM improves over discrete and continuous diffusion baselines at matched model size, in puzzle accuracy on Sudoku and Countdown and in generative perplexity on LM1B. Project page: https://hc-dlm.github.io/.

## 24. Spatial Strategies, Not Actions: Vector-Quantized Geodesics as Tools for LLM-Driven Agents

- Authors: Gabriel Turinici
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-30
- DOI: Unavailable
- Categories: cs.AI, cs.RO, eess.SY
- Relevance: 3.020313416310436
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.00613v1
- PDF: https://arxiv.org/pdf/2610.00613v1
- Local PDF: pdf/2026-10-03_24_Spatial Strategies, Not Actions_ Vector-Quantized Geodesics as Tools for LLM-Driven Agents.pdf

Large language model (LLM) based agents are often criticized for lacking spatial understanding and mainly exploiting statistical text patterns. We investigate their spatial comprehension through an architecture combining geometrical tools with a LLM serving as a high-level orchestrator in grid-world environments. The agent first collects geodesic trajectories, which are then vector-quantized to extract a representative subset. Offline, the LLM associates a natural language description of the underlying behavioral patterns to each selected trajectory, making it a tool. Online, the LLM chooses the appropriate tool conditioned on the current state and goal. Low-level control is handled by primitive actions that execute the trajectory associated with the tool. From an agentic AI perspective, this approach separates learning into two levels: tool discovery is handled through unsupervised quantization of trajectories, while reasoning and decision-making are handled by the LLM. We test the approach in a partially observable dynamic 2D grid environment with an open vision-language model (Qwen3.6-35B-A3B). Pairing the geometry-derived tool library with an agent-centered zoom tool and a collision detection tool lets a fast, non-reasoning configuration match the goal-reaching rate of a much more costly chain-of-thought version, while cutting the cost of a decision from minutes to seconds.

## 25. Debias Anything: Fairness with Diversity without Supervision in Diffusion Models

- Authors: Théau d'Audiffret, Mariia Vladimirova, Jean-Yves Franceschi
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-01
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 2.99708716646582
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.01815v1
- PDF: https://arxiv.org/pdf/2610.01815v1
- Local PDF: pdf/2026-10-03_25_Debias Anything_ Fairness with Diversity without Supervision in Diffusion Models.pdf

Although diffusion models produce high-quality images, they also reproduce and amplify demographic imbalances in their training data. Debiasing their generation process post-training w.r.t. some sensitive attribute usually relies on classifier guidance or explicit text extra-conditioning, but this reduces methods' applicability and output diversity. Conversely, methods promoting diversity alone do not ensure fair attribute representation. In this paper, we propose a method tackling fairness and diversity jointly that is generally applicable to any diffusion model and any sensitive attribute. To this end, an adapter connects the frozen diffusion model to a pretrained vision-language embedding space, enabling fairness and diversity guidance without sensitive-attribute annotations. For fairness, pairs of text prompts define attribute directions which guide batch composition towards specific proportions. For diversity, we introduce a score measuring disagreement between the semantic estimates derived from this representation. The formulation supports unconditional and text-conditional diffusion models, while requiring no prior knowledge or data of sensitive attribute. Experiments confirm that our method improves quality and diversity scores at comparable fairness levels.

## 26. Scalable, Transferable Meta-network for Data Selection Requires a Different Loss (and Why the Obvious Choice is Problematic)

- Authors: Zilin Du, Bowen Yang, Boyang Albert Li
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-01
- DOI: Unavailable
- Categories: cs.CL, cs.AI, cs.LG
- Relevance: 2.9847125393570986
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.02092v1
- PDF: https://arxiv.org/pdf/2610.02092v1
- Local PDF: pdf/2026-10-03_26_Scalable, Transferable Meta-network for Data Selection Requires a Different Loss (and Why the Obvious Choice is Problema.pdf

Data selection is critical for training large language models on massive and heterogeneous corpora. Meta-learning for Training-data Selection offers a principled alternative to heuristic scoring by learning data weights from a target validation objective, but existing methods face a trade-off between fine-grained valuation and transferability to unseen data. A natural solution is to replace per-sample weights with a selection network. However, we find that directly incorporating such a network into existing MTS objectives leads to unstable optimization and poor generalization, caused by weight suppression and persistent reliance on easy-to-learn features. To address these issues, we propose Transferable Example Scoring and Selection (TESS), a scalable data-selection framework built on a Pointwise Value Matching objective (PVM). Experiments on LLM safety and targeted instruction tuning demonstrate strong transfer across datasets, from subsets to full corpora, and from smaller to larger models.

## 27. A foundation for systematic analysis of transformers and RNNs for tractography

- Authors: Emmanuelle Renauld, Philippe Poulin, Hugo Larochelle, Antoine Théberge, Maxime Descoteaux
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-01
- DOI: Unavailable
- Categories: cs.LG, eess.IV, q-bio.NC
- Relevance: 2.982522773880288
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.01894v1
- PDF: https://arxiv.org/pdf/2610.01894v1
- Local PDF: pdf/2026-10-03_27_A foundation for systematic analysis of transformers and RNNs for tractography.pdf

Machine learning (ML) has emerged as a promising approach for improving diffusion MRI (dMRI) tractography, a task that remains limited by the intrinsic tension between local diffusion information and global anatomical plausibility. In this work, we systematically evaluate recurrent neural networks (RNNs) and Transformer models for iterative tractography, with particular attention to training strategies, input representations (including convolutional neural network (CNN)-based embeddings and end-of-sequence (EOS) tokens), and hyperparameter selection. We introduce a generation-validation phase enabling supervision at the streamline level during training, allowing supervision despite the mismatch between local loss functions and global streamline quality. Using the ISMRM2015 tractography challenge dataset, our models achieve the highest reported performance to date. Through controlled experiments, we quantify the impact of missing bundles, noisy or imperfect training streamlines, and invalid fibers in the training set. Finally, we demonstrate the applicability of our best-performing models for in vivo data from the Tractoinferno database. Overall, our results highlight both the potential and the limits of sequence-based deep learning models such as Transformers and RNNs for tractography, and emphasize the need for improved phantoms and evaluation methods for in vivo validation. We provide takeaways and recommendations for future researchers training and validating sequence-based supervised methods for tractography.

## 28. Pragmatic DML with AI-Learned Representations

- Authors: Andres Aradillas Fernandez, Victor Chernozhukov, Carlos Cinelli, Sven Klaassen, Whitney Newey, Martin Spindler, Jan Teichert-Kluge, Suhas Vijaykumar
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-01
- DOI: Unavailable
- Categories: econ.EM, stat.ML
- Relevance: 2.9628342978239974
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.01935v1
- PDF: https://arxiv.org/pdf/2610.01935v1
- Local PDF: pdf/2026-10-03_28_Pragmatic DML with AI-Learned Representations.pdf

Text, images, and other rich covariates are increasingly compressed into AI-learned representations and then used as controls in causal analysis. We study when this approach is valid and develop a practical framework for causal inference with learned representations. For a broad class of estimands, an imperfect representation distorts the target causal parameter by the product of two representation errors: one in the outcome regression and one in the balancing weight (or Riesz representer). This yields three constructive results. First, cross-fitted double machine learning (DML) provides valid Wald inference for the representation-dependent target. When representation errors are small, the same interval covers the causal parameter, and it can even attain the semiparametric efficiency bound. Second, fold-wise representation learning (or fine-tuning) is compatible with DML inference for the causal parameter. To this end, we develop convex- and star-aggregation pipelines for learning and combining representations. Third, when representation errors are substantial, we can provide interpretable sensitivity regions and root-$n$ inference for their endpoints. In a multi-modal demand application, seven representation-specific estimates and their star aggregate all imply a negative near-unit elasticity for rank-based price response, and the result remains robust over the reported sensitivity grid.

## 29. SkillSpec: Consensus-Gated Agent Skill Evolution via Representation Specialization

- Authors: Huancheng Chen, Xiaodi Sun, Zhaoqiong Huang, Shenyang Huang Shreya Singhal, Jingwen Lu
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-30
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 2.9489727139803734
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.00704v1
- PDF: https://arxiv.org/pdf/2610.00704v1
- Local PDF: pdf/2026-10-03_29_SkillSpec_ Consensus-Gated Agent Skill Evolution via Representation Specialization.pdf

Natural-language skills are textual procedural memories through which large language model (LLM) agents retain reusable task knowledge without updating model weights. Existing methods typically treat skills as either static artifacts or monolithic documents optimized using aggregate validation scores as feedback. However, representing a skill as a monolithic document restricts optimization to its textual content, without explicitly modeling the structure through which procedural knowledge is retrieved and executed. We identify a key distinction between learning what knowledge to retain and determining how to organize it: textual updates should first be validated through execution evidence, after which the retained knowledge should be structured according to its procedural dependencies and retrieval requirements. To this end, we introduce SkillSpec, a two-phase framework comprising consensus-gated evolution and representation specialization. In the consensus-gated phase, complementary editing intents generate complete candidate skills. An update is committed only when paired evaluations reach consensus, requiring sufficient overall improvement and non-negative aggregate paired gain in every repeated evaluation. In the specialization phase, signals of process and redundancy sensitivity derived from the full optimization trajectory, including accepted and rejected candidates, guide the selection of a flat, graph, or hybrid representation.Across six benchmarks and three target language models, SkillSpec improves average success rate over SkillOpt by 6.89%, averaged across the three models. These results demonstrate that reliable skill evolution and representation specialization address complementary objectives: deciding what knowledge to retain and how to structure it for inference.

## 30. ChainLoRA: Geometry-Preserving Task Vector Merging for Continual Learning in LLMs

- Authors: Hang Yin, Haozhe Wang, Yuhua Luo, Zhangqi Pan, Xiaoxing Wang, Junchi Yan
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-30
- DOI: Unavailable
- Categories: stat.ML, cs.LG
- Relevance: 2.937409883138833
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.00431v1
- PDF: https://arxiv.org/pdf/2610.00431v1
- Local PDF: pdf/2026-10-03_30_ChainLoRA_ Geometry-Preserving Task Vector Merging for Continual Learning in LLMs.pdf

Continual parameter-efficient fine-tuning for large language models (LLMs) must balance retention of previously acquired knowledge, adaptation to new tasks, and strict parameter budgets. We present \textbf{ChainLoRA}, a replay-free continual merging framework built on chain-updated task-vector geometry. From a parameter-merging perspective, we formulate a geometric view of forgetting through a measurable interaction between task updates, separating directional overlap from coefficient coupling. Building on this view, ChainLoRA combines chain-updated training with post-stream adaptive SVD merging. During training, initialization and a one-sided orthogonality proxy use only the last carrier, keeping their historical-state footprint and regularization overhead constant as the task stream grows. At merging time, Adaptive SVD extracts a shared carrier and aligns it to the latest task through Procrustes adaptation. Our theoretical analysis shows that Procrustes adaptation facilitates geometric approximate separation of shared and task-specific components. The one-sided proxy further bounds inter-task interference. An effective-rank penalty additionally promotes efficient utilization of the task subspace during continual learning. Experiments show that ChainLoRA achieves state-of-the-art performance among the evaluated replay-free methods on the Large and SuperNI benchmarks, while remaining competitive on Standard CL and attaining almost the closest average scores to the evaluated replay-based method across all three benchmarks.
