# Paper Daily Reading - 2026-11-12

## 1. Multimodal Graph Learning: A Survey of Models, Benchmarks, and Frontiers

- Authors: Rui Xue, Tianfu Wu
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-08
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.9238631351012296
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.12990v1
- PDF: https://arxiv.org/pdf/2611.12990v1
- Local PDF: pdf/2026-11-12_01_Multimodal Graph Learning_ A Survey of Models, Benchmarks, and Frontiers.pdf

Multimodal attributed graphs (MAGs), in which nodes carry text, images, and other modalities while edges encode relations among entities, underlie e-commerce, social media, content platforms, and creative applications. Learning on MAGs has developed along two complementary lines: graph-centric methods redesign how modalities are fused, propagated, and connected within message passing, while foundation-model-centric methods pretrain transferable multimodal graph encoders or bring graph context into multimodal large language models for prediction and generation. In parallel, several benchmarks have appeared with different datasets and evaluation protocols. This survey takes an algorithm-centric and evaluation-grounded view of the field and makes three contributions. Modeling: we introduce a unified message-passing formulation and organize methods into five integration levels (feature, propagation, topology, learning, and foundation model), covering discriminative and graph-conditioned generative models; within this formulation we derive representative methods as special cases, compare their assumptions, expressiveness, and cost, and identify cross-modal sensitivity as a property that separates otherwise similar architectures. Datasets and evaluation: we review recent benchmarks, summarize their datasets and metrics, define model-independent descriptors (label homophily, average degree, clustering, and edge provenance), and map each evaluation protocol to the baselines it uses. Frontiers: we connect multimodal graph learning to AI agents, covering the multimodal graphs that agents perceive and remember and graph engineering, the practice of organizing agent workflows as explicit graphs; we then discuss open problems, concrete efforts for the community, and research directions, including when graph structure helps in the presence of strong multimodal foundation models.

## 2. Bridging Graph and Pairwise Learning for Gene Regulatory Network Inference from scRNA-seq Data

- Authors: Hang Li, Jiaxin Qi, Yan Cui, Yuhua Zheng, Jianqiang Huang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-10
- DOI: Unavailable
- Categories: q-bio.GN, cs.AI
- Relevance: 3.883947063193899
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.13801v1
- PDF: https://arxiv.org/pdf/2611.13801v1
- Local PDF: pdf/2026-11-12_02_Bridging Graph and Pairwise Learning for Gene Regulatory Network Inference from scRNA-seq Data.pdf

Motivation: Gene regulatory networks (GRNs) capture the underlying interactions through which transcription factors (TFs) regulate genes. Based on gene expression data, existing GRN inference approaches generally fall into two categories: graph-based methods, which model the GRN as a whole graph, and pairwise-based methods, which decompose the GRN into individual TF-target gene pairs for modeling. However, each approach exhibits limitations that are precisely the strengths of its counterpart. Graph-based methods tend to overfit due to their reliance on a single training graph, whereas pairwise-based methods benefit from abundant TF-target training pairs. In contrast, pairwise-based methods overlook the global topological structure, which is essential for comprehensively capturing regulatory mechanisms. Results: To address these limitations, we propose scGPL, an end-to-end unified framework that jointly models global regulatory topology and local interactions. scGPL extracts macro-level features from the global regulatory graph and introduces a dynamic, importance-guided subgraph sampling mechanism to capture fine-grained local dependencies. By fusing global representations with subgraph-enhanced local features, our framework bridges the gap between the two paradigms, incorporating essential whole-graph topological dependencies while retaining the data abundance advantage of pairwise methods. Extensive experiments on seven benchmark datasets demonstrate that scGPL consistently achieves state-of-the-art performance, with up to 13.7% improvement over the strongest baseline, validating the effectiveness of our integrative design. Availability and implementation: The source code is maintained on GitHub (https://github.com/talent-hang/scGPL), and the datasets and versioned releases are archived at https://doi.org/10.5281/zenodo.21608485 for reproducibility.

## 3. Hierarchical Graph Representation Learning with Pooling-Induced Substructures

- Authors: Luca Sbicego, Xiaowen Dong, Dorina Thanou
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-10
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.76960456997541
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.14126v1
- PDF: https://arxiv.org/pdf/2611.14126v1
- Local PDF: pdf/2026-11-12_03_Hierarchical Graph Representation Learning with Pooling-Induced Substructures.pdf

Hierarchical graph-level tasks that require reasoning over substructures that extend beyond local neighborhoods are posing challenges for standard Graph Neural Networks (GNNs). While graph pooling aims to address this by coarsening graphs into hierarchical representations, existing methods often fail to explicitly preserve the substructures they induce, leading to inconsistent empirical performance. Moreover, evaluating such approaches remains challenging due to the lack of benchmarks with explicit hierarchical structure. We propose Pooled-Substructure-Aware GNNs, an approach to graph pooling that explicitly preserves and processes substructures uncovered by structure-based pooling schemes. We show that this design enhances the expressive power of pooling-based GNNs in the sense of the Weisfeiler-Lehman (WL) test. To enable principled evaluation, we introduce two new synthetic datasets with controllable hierarchical structure and propose a metric to characterize the prevalence of hierarchical patterns in real-world graph-level benchmarks. On tasks with relevant hierarchical structure, our approach outperforms matched pooling baselines, while remaining competitive on structurally simpler benchmarks. Code and datasets are publicly available at https://github.com/lsbicego/PSA-GNN/.

## 4. Continuous 3D Spatial Transcriptomics Reconstruction via Histology-Informed Implicit Neural Representations

- Authors: Kaito Shiku, Ryoma Bise, Ahtisham Fazeel Abbasi, Yuichiro Iwashita, Shumpei Takezaki, Andreas Dengel, Muhammad Nabeel Asim
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-10
- DOI: Unavailable
- Categories: cs.CV, cs.LG
- Relevance: 3.537882851410592
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.14129v1
- PDF: https://arxiv.org/pdf/2611.14129v1
- Local PDF: pdf/2026-11-12_04_Continuous 3D Spatial Transcriptomics Reconstruction via Histology-Informed Implicit Neural Representations.pdf

Three-dimensional spatial transcriptomics (3D ST) enables the analysis of gene-expression patterns across tissue depths. However, 3D ST measurements are acquired from discrete 2D tissue sections, which are often sparsely sampled due to high acquisition costs. To address this limitation, we propose a histology-informed multi-task implicit neural representation (HIM-INR) for continuous 3D gene-expression reconstruction from sparse ST observations. HIM-INR jointly reconstructs gene-expression profiles and histological representations using an INR with a shared backbone, leveraging densely sampled histological images as auxiliary spatial supervision. Once trained, HIM-INR predicts gene expression at arbitrary 3D coordinates without requiring histological images. Experiments on two 3D ST datasets demonstrate improved reconstruction over existing methods, particularly as the number of missing ST sections increases.

## 5. Emergent Biological Capabilities in a Foundation Model for Molecular Interactions

- Authors: Adi Mashiach
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-10
- DOI: Unavailable
- Categories: cs.LG, q-bio.BM
- Relevance: 3.3468843165302333
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.14504v1
- PDF: https://arxiv.org/pdf/2611.14504v1
- Local PDF: pdf/2026-11-12_05_Emergent Biological Capabilities in a Foundation Model for Molecular Interactions.pdf

Foundation models trained on large unlabeled corpora develop emergent capabilities, tasks that go beyond the training objective. We extend this paradigm to multimodal biology with Bonbon, a foundation model for molecular interactions trained on approximately 3.2 trillion tokens of paired protein-ligand sequences. From a single representation space, Bonbon exhibits three zero-shot emergent capabilities at hierarchical levels of resolution: functional (mechanism of action), residue (binding site localization, including orthosteric/allosteric discrimination), and bond (covalent versus non-covalent engagement). All three capabilities generalize to out-of-distribution complexes. Bonbon was trained on protein-ligand sequences alone, without any task-specific supervision and without structural coordinates. We conducted controlled scaling experiments across six model scales from 42M to 1.6B parameters; every capability evaluated shows a sharp jump at the largest scale on continuous metrics, even as pretraining loss decreases smoothly. This demonstrates that loss-based scaling laws alone are insufficient to predict when zero-shot emergent capabilities become available. The capabilities reported here emerge after training at a 1:2,000 parameter-to-token ratio to accommodate the sparsity of paired biological interaction data. The same frozen representations achieve state-of-the-art binding and affinity prediction at five orders of magnitude greater speed than co-folding methods. In prospective wet-lab validation across nine disease targets spanning seven protein families, Bonbon achieves a 61.5% dose-response hit rate on de novo compounds, yielding structurally novel molecules not previously reported to inhibit these proteins, including for out-of-distribution targets.

## 6. Controlled Knowledge Engineering for Taxonomy Induction with Tool-Grounded LLM Agents and Runtime-Adaptive Policies

- Authors: Jonas Limniatis, Bennet Schaarmann, Georg Reuber, Robert Stahlbock
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-10
- DOI: Unavailable
- Categories: cs.IR, cs.AI
- Relevance: 3.287606157656885
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.13966v1
- PDF: https://arxiv.org/pdf/2611.13966v1
- Local PDF: pdf/2026-11-12_06_Controlled Knowledge Engineering for Taxonomy Induction with Tool-Grounded LLM Agents and Runtime-Adaptive Policies.pdf

Taxonomies are structured knowledge representations that support semantic search, recommendation, product catalog organization, and retrieval-augmented generation. Their automated construction from a fixed set of candidate entities requires more than plausible text generation: the resulting hierarchy must be complete, structurally valid, and semantically coherent. Large Language Models (LLMs) are promising for this task, but iterative free-form generation remains vulnerable to omitted or hallucinated entities, invalid hierarchical relations, and inconsistent organizational principles. We introduce TIGA (Taxonomy Induction with Tool-Grounded Agents), a knowledge-engineering architecture that formulates taxonomy induction as an iterative decision process over an explicit state and constrained action space. TIGA combines executable taxonomy-editing tools, an memory that records tool calls, rationales, and outcomes, and a runtime-adaptive organizational policy that the agent revises during inference. An optional global reviewer evaluates the constructed taxonomy against the candidate set and the active policy. We evaluate TIGA on four benchmark taxonomies using two LLM backbones and compare it with single-shot and iterative prompting-based baselines. TIGA achieves the strongest structural-quality results in most evaluated configurations, but does not dominate on every precision measure. The gains are accompanied by substantially higher token consumption, API-call volume, and inference time. Ablation results show consistent benefits from the policy and interaction-memory components, whereas the effect of global review depends on the dataset and the available revision budget. These findings characterize tool grounding and runtime policy adaptation as promising but costly mechanisms for improving the controlled construction of structured knowledge representations.

## 7. Transformers Provably Learn Graph Search: Training Dynamics and the Exponential Power of Depth

- Authors: Xutao Ma, Somayeh Sojoudi
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-10
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 3.230470813134242
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.13594v1
- PDF: https://arxiv.org/pdf/2611.13594v1
- Local PDF: pdf/2026-11-12_07_Transformers Provably Learn Graph Search_ Training Dynamics and the Exponential Power of Depth.pdf

Large Language Models (LLMs) have achieved remarkable progress on complex reasoning tasks, yet the mechanisms by which they acquire reasoning capabilities and the efficiency of their reasoning remain poorly understood. In this paper, we investigate the path-finding problem over directed graphs, a symbolic abstraction of multi-step reasoning. We first characterize the architectural requirements for this task, proving that one-layer transformers require $Ω(N^2)$ size on dense graphs to implement the key DFS child-selection primitive. While a two-layer transformer implements full DFS with $O(N\log(N))$ size. Thus, a second layer is necessary and sufficient for near-linear DFS reasoning. We then extend this expressivity analysis to deeper models: for every $k\geq3$, a $k$-layer transformer implements a bounded-reachability DFS policy with look-ahead horizon $1+2^{k-3}$, establishing an exponential increase in reachability horizon with depth. Finally, going beyond expressivity, given appropriately curated training data, we show that two-layer transformers can provably learn to execute DFS via gradient flow and generalize to unseen graphs. Together, our results provide a mechanistic account of how transformers implement graph search, how depth expands bounded look-ahead, and how such reasoning algorithms can emerge through training.

## 8. Mechanistic Interpretability of Deep Neural Networks: Methods, Frameworks, and Perspectives

- Authors: Lorenzo Cirillo, Irene Amerini, Andrea Cavallaro
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-10
- DOI: Unavailable
- Categories: cs.LG, cs.AI, cs.CV
- Relevance: 3.1828180180816146
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.13868v1
- PDF: https://arxiv.org/pdf/2611.13868v1
- Local PDF: pdf/2026-11-12_08_Mechanistic Interpretability of Deep Neural Networks_ Methods, Frameworks, and Perspectives.pdf

Deep neural networks underpin fundamental tasks in a wide range of signal domains, such as image, audio, and language processing. However, their internal mechanisms are notably difficult to interpret. Internal activations are structured signals transformed across layers that may encode a multitude of interdependent relationships, as individual neurons frequently represent multiple underlying concepts. Mechanistic interpretability aims to uncover the internal mechanisms of neural networks by identifying components whose activations are causally responsible for specific behaviors. In such a context, this article provides an overview of advances in mechanistic interpretability for the analysis of causal inference in deep neural networks.

## 9. LUMIR: Decoupled Multimodal Representation Learning from Heterogeneous Data for Next-POI Recommendation

- Authors: Zehui Wang, Wolfram Höpken, Dietmar Jannach
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-10
- DOI: Unavailable
- Categories: cs.IR, cs.LG, cs.MM
- Relevance: 3.1375413588647723
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.14004v1
- PDF: https://arxiv.org/pdf/2611.14004v1
- Local PDF: pdf/2026-11-12_09_LUMIR_ Decoupled Multimodal Representation Learning from Heterogeneous Data for Next-POI Recommendation.pdf

As multimodal tourism-related information collected from heterogeneous data sources has become increasingly available, learning effective representations has attracted attention for improving recommendation performance. Existing approaches often tightly couple multimodal fusion with the architecture and optimization objective of a specific downstream model, which limits the generality and reusability of the learned representations. To address these limitations, we propose LUMIR, a decoupled multimodal representation learning framework based on contrastive learning. Multimodal information collected from heterogeneous data sources is first semantically unified into a shared textual representation space using large language models (LLMs). An interaction-aware fusion mechanism is then designed to model cross-modal interactions, while sequential signals are incorporated as a structural constraint to guide representation learning. To evaluate the learned representations, experiments are conducted on a multimodal point-of-interest (POI) dataset under the next-POI recommendation setting across multiple sequential recommendation backbones. The results show that LUMIR consistently outperforms existing multimodal fusion baselines in both accuracy-oriented and beyond-accuracy metrics, demonstrating that decoupling representation learning from downstream optimization provides an effective paradigm for learning reusable multimodal representations. The code is publicly available at https://github.com/wzehui/LUMIR.

## 10. Toward Foundation Detection Models via Example-Based Grounding in EM-DETR

- Authors: Sheethal Bhat, Bogdan Georgescu, Awais Mansoor, Florin C. Ghesu, Sasa Grbic, Andreas Maier
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-10
- DOI: Unavailable
- Categories: cs.CV, cs.AI
- Relevance: 3.072879749235151
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.14518v1
- PDF: https://arxiv.org/pdf/2611.14518v1
- Local PDF: pdf/2026-11-12_10_Toward Foundation Detection Models via Example-Based Grounding in EM-DETR.pdf

DeepLearning (DL)-based Computer-Aided Diagnostic (CAD) systems have shown great promise in supporting clinicians, but their performance heavily depends on the availability of large, well-annotated datasets. In medical lesion detection, the scarcity of comprehensive, stan dardized annotations and the heterogeneity of existing datasets limit the development of robust foundation models. In this work, we introduce a novel approach to building a multi-domain foundation model for le sion detection by integrating diverse medical image datasets annotated for both anatomical structures and abnormalities. We first propose a student-teacher training strategy to effectively combine datasets with heterogeneous label spaces, mitigating catastrophic forgetting, and im proving feature learning. In addition, building on our previously pro posed example-based EM-DETR framework, we adapt it to jointly learn from multiple domain-specific datasets, enabling fine-grained, example driven detection across modalities. Our model achieves state-of-the-art (SOTA) results, with image-level AUC scores exceeding previous SOTA by 1% point on four key findings in CXRs. We achieve a leading mAP50 in CXRs and mammography, surpassing EM-DETR trained on a single dataset by 2-3% points. This approach paves the way for scalable foundation models in medical imaging that leverage heterogeneous data while maintaining robust and generalizable performance.

## 11. An Analytical Model of Compute-limited Multistage Training Pipelines

- Authors: Nishil Patel, Jin Hwa Lee, Basile Confavreux, Andrew Saxe
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-09
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.0172224274921557
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.13276v1
- PDF: https://arxiv.org/pdf/2611.13276v1
- Local PDF: pdf/2026-11-12_11_An Analytical Model of Compute-limited Multistage Training Pipelines.pdf

Modern foundation models are trained through multiple stages, yet how these stages interact and how compute should be allocated across them remain poorly understood. We introduce an analytically tractable high-dimensional model combining unsupervised pretraining with a linear autoencoder, supervised fine-tuning (SFT) with noisy stepwise labels, and reinforcement learning (RL) with sparse episodic rewards. Using random matrix theory and an operator-projection closure, we derive approximate low-dimensional learning dynamics that closely match simulations. We show that finite pretraining data imposes a representation-dependent performance limit, with Bayes classification error scaling as the inverse square root of the pretraining sample ratio, and observe the same exponent in asymptotic SFT and RL errors. Better pretraining also reduces sensitivity to noisy supervision. SFT initialization shortens the initial RL plateau induced by sparse rewards, an effect we also observe in OLMo-2 1B on GSM8K. Longer SFT warm starts additionally improve asymptotic RL performance. Optimizing compute across all three stages reveals that the optimal allocation depends on supervision quality and total budget, with a non-monotonic dependence of the RL compute share on budget. Finally, a complementary compositional model shows how RL selectively strengthens task-relevant pretrained skills while largely preserving unused skills. Together, these results identify mechanisms linking representation quality, feedback structure, and compute allocation in multistage training.

## 12. When Covariance Is Not Enough: Kernel-Based Regularization for Single-Cell Counterfactuals

- Authors: Korbinian Traeuble, Edward de Brouwer, Archit Verma, Doron Haviv, Kipper Fletez-Brant
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-10
- DOI: Unavailable
- Categories: cs.LG, q-bio.GN
- Relevance: 3.0137179512147476
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.13748v1
- PDF: https://arxiv.org/pdf/2611.13748v1
- Local PDF: pdf/2026-11-12_12_When Covariance Is Not Enough_ Kernel-Based Regularization for Single-Cell Counterfactuals.pdf

Counterfactual editing of single cells, predicting how an observed cell would look had one factor been different, enables in-silico screening where experiments are infeasible, but is useful only if the edit is faithful to the individual and not merely to the condition. Concept bottleneck generative models make the effects of interventions interpretable by decomposing a cell's representation into known and unknown factors. Previous work uses a linear cross-covariance penalty to disentangle known and unknown dimensions. We demonstrate that this first-order criterion does not fully separate information when non-linear interactions are present. We first demonstrate the inadequacy of linear cross-factor penalization with simulation experiments with controlled edits and known non-linear covariate effects. We then demonstrate that adding a nonlinear kernel criterion, the normalized Hilbert-Schmidt Independence Criterion, is able to recover the true intervention effects on simulation data. Finally, we apply the non-linear concept bottleneck model to a complex single-cell RNA-seq dataset and find that it improves the ability to generate counterfactual expression profiles of cells under different tissue environments.

## 13. Geometry and Stochastic Analysis of Flow and Diffusion Models: A Survey

- Authors: Ehsan Mirafzali, Razvan Marinescu
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-09
- DOI: Unavailable
- Categories: math.PR, stat.ML
- Relevance: 3.0107286746906707
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.12107v1
- PDF: https://arxiv.org/pdf/2611.12107v1
- Local PDF: pdf/2026-11-12_13_Geometry and Stochastic Analysis of Flow and Diffusion Models_ A Survey.pdf

Flow-based and diffusion-based models have become the principal means of learning and sampling high-dimensional probability distributions, from images and video to proteins, molecules and physical fields, and increasingly language. Each carries a simple law to the law of the data along a curve of probability measures, and behind the variety of their names lie three geometries, those of the state space on which the data live, of the space of probability measures through which the curve passes, and of the space of paths traced by the generating process. A single analytic idea runs through the subject. Every score identity used to train a diffusion model is an integration by parts, on the noise, on the data or on Wiener space, and Malliavin calculus extends this to nonlinear and infinite-dimensional diffusions. We develop these foundations with full definitions and follow them through normalising flows, flow matching and few-step maps, diffusion models and their convergence theory, conditioning, Schrödinger bridges and stochastic control, and their extension to manifolds, Lie groups, discrete and function spaces and jump processes. We close with statistical physics, renormalisation and, more speculatively, holography, in which the radial direction of anti-de Sitter space can play the role of flow time. A table of the main methods and a collection of open problems complete the survey.

## 14. Graph Visualizations in Prompts for Knowledge Graph Question Answering

- Authors: Luiz do Valle Miranda, Andreas L. Opdahl, Grzegorz J. Nalepa
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-06
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 3.0064179021429043
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.12938v1
- PDF: https://arxiv.org/pdf/2611.12938v1
- Local PDF: pdf/2026-11-12_14_Graph Visualizations in Prompts for Knowledge Graph Question Answering.pdf

We study when and how multimodal input improves knowledge graph question answering (KGQA) in large vision--language models. Using a controlled evaluation over 1,500 WebQSP and CWQ questions and six VLMs within a fixed KGQA pipeline, we compare text-only prompting against text-plus-graph visualization at the per-question level and analyze performance changes as a function of reasoning complexity, model size, and image layout. Adding a graph image yields an average gain of 1.85 F1 points, driven by strong precision improvements on low-complexity questions (+4.65 F1). Mixed-effects and regression analyses show that these multimodal gains do not depend strongly on model scale, but are highly sensitive to graph layout: image-only settings sharply degrade performance, hierarchical Graphviz layouts outperform less organized renderings, and decomposing large subgraphs into separated paths yields the largest improvements. Taken together, the results indicate that visual prompting primarily aids KGQA by enhancing prediction precision in low-complexity contexts, provided that visual design respects cognitive and perceptual constraints. To optimize both accuracy and inference efficiency, we argue for adaptive visual prompting policies that selectively append diagrams to small, visually sparse subgraphs with well-structured layouts, avoiding unnecessary visual clutter and token overhead on complex queries. We conclude by relating these findings to a visual notation design theory, outlining how principled diagram encoding can guide future multimodal VLM prompting.

## 15. VIGOR: Benchmarking Visual Rationale Correctness in Multimodal Large Language Models

- Authors: Yanlin Chen, Tang Li, Xi Peng
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-09
- DOI: Unavailable
- Categories: cs.CV, cs.LG
- Relevance: 2.9969651024861843
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.13150v1
- PDF: https://arxiv.org/pdf/2611.13150v1
- Local PDF: pdf/2026-11-12_15_VIGOR_ Benchmarking Visual Rationale Correctness in Multimodal Large Language Models.pdf

Multimodal large language models (MLLMs) are typically evaluated by whether they produce correct answers, but correctness alone does not reveal whether their outputs are supported by the right visual evidence. We introduce VIGOR, a benchmark for evaluating VIsually GrOunded Rationales in MLLMs. VIGOR represents visual rationales as explicit concepts paired with pixel-level groundings, covering multiple abstraction levels including low-level visual properties, intermediate structures, objects, parts and high-level motion, relations. To construct VIGOR at scale, we develop an automatic annotation framework that reuses existing dense supervision when available and generates missing concept groundings through proposal-based annotation followed by conservative multimodal verification. Using VIGOR, we evaluate whether MLLMs "look at what they say" by comparing model-derived visual evidence for each expressed concept against annotated ground-truth rationales. Our results show that current MLLMs exhibit limited visual rationale correctness and reveal distinct grounding failures across concept levels. VIGOR provides a benchmark and scalable data construction pipeline for studying whether MLLM outputs are supported by appropriate visual evidence. Code is available at https://github.com/deep-real/VIGOR

## 16. Discovering Structurally Plausible and Interpretable Cognitive Models with Large Language Models

- Authors: Boyoung Kwon, Jiyoon Seo, Sang Ho Lee
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-10
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 2.981849994602759
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.13561v1
- PDF: https://arxiv.org/pdf/2611.13561v1
- Local PDF: pdf/2026-11-12_16_Discovering Structurally Plausible and Interpretable Cognitive Models with Large Language Models.pdf

Computational cognitive modeling has traditionally relied on manual model construction, which is a time-intensive process that requires substantial domain expertise. Although recent LLM-based approaches have begun to automate model generation, they often prioritize predictive accuracy at the expense of structural plausibility and parameter identifiability. We introduce DisCo, an LLM-guided framework that discovers interpretable symbolic cognitive models through evolutionary search with two structural components: a Validator that filters structurally invalid models, and a Cleaner that promotes parameter identifiability by removing redundant parameters. Across three behavioral tasks, DisCo consistently discovers models that achieve performance competitive with task-specific baselines. Ablation analyses show that the Validator is important for recovering psychologically meaningful structure. Without this component, models tend to violate behavioral constraints and show less consistent associations with external cognitive measures. These results suggest that LLM-driven model discovery, when coupled with appropriate structural constraints, can yield cognitively plausible models that go beyond predictive fit.

## 17. TreeAgent: Structure-Aware Memory Agent for Processing Long Hierarchical Data

- Authors: Wei Gu, Weiwei Qi, Jiajun Tang, Tianhang Zheng, Bo Chen, Zhibo Zhang, Jinfei Liu, Kui Ren
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-10
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 2.9757190400049978
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.13946v1
- PDF: https://arxiv.org/pdf/2611.13946v1
- Local PDF: pdf/2026-11-12_17_TreeAgent_ Structure-Aware Memory Agent for Processing Long Hierarchical Data.pdf

Practical Web applications increasingly require agents to interpret long conversations or documents. For inputs exceeding the context windows of large language models (LLMs), memory agents process segments sequentially and retain past information in bounded memory. However, they typically divide inputs into flat token segments without preserving structure or hierarchy, causing three limitations for structured data such as API responses or HTML documents. First, fixed-length segmentation can split fields of the same record, breaking their relationships. Second, segments lack hierarchical information, obscuring their structural context and positions. Third, successive memory updates may discard details of earlier sibling records needed for reasoning on later segments. To address these limitations, we propose TreeAgent, a structure-aware agent that uses the input hierarchy to guide both segment-wise context processing and access to past information. Specifically, TreeAgent constructs segments from complete subtrees and groups of adjacent sibling subtrees to preserve local structural relationships. We provide theoretical guarantees on segment counts to guide token budget selection toward matching the segment count of fixed-length segmentation. We further attach structural paths to the segments for the agent to identify their ancestors and hierarchical positions. We also introduce residual memory links from the segments of low-level children to the segments of high-level parents, enabling direct information flows beyond successive memory updates. We evaluate TreeAgent with four representative memory agents on eight retrieval and aggregation tasks. The inputs are derived from real-world application data in JSON, HTML, YAML, and JavaScript and range from 8K to 1M tokens. TreeAgent improves the average score across the four datasets for all four agents, with 3.61% performance gain on average.

## 18. Mixed Signals: Weight-Space Programming for EEG and ECG

- Authors: Dara Varam, Taraneh Aminosharieh Najafi, David Atienza
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-10
- DOI: Unavailable
- Categories: cs.LG, cs.AI, eess.SP
- Relevance: 2.965635956738803
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.13758v1
- PDF: https://arxiv.org/pdf/2611.13758v1
- Local PDF: pdf/2026-11-12_18_Mixed Signals_ Weight-Space Programming for EEG and ECG.pdf

Weight-space programming allows language models to read a trained neural network's weights and edit them. This opens the door to ``training'' by reasoning rather than through gradient descent. Prior work has demonstrated its functionality and promise for game-playing networks and fixing specific failures in language models, even extending to diffusion models. In this work, we present its applicability to models trained on biosignal data, specifically EEG and ECG data. We show that frontier models are not only able to debug specific faults planted in biosignal-based models without being told what these faults are, but are even capable of writing all the weights of a network from scratch, given only the architecture, the task, and a minimal set of training subjects. In particular, in one set of experiments, a language model was able to match standard gradient-descent training using $6\times$ fewer training subjects, through reasoning alone and without any gradient descent step. Networks written by Claude Opus 5.5 also scored higher than classic hand-crafted EEG pipelines (alpha band power, and common spatial patterns with linear discriminant analysis) when built from the same 5 subjects. We also highlight some of the limitations, which include the inability of language models to improve already well-trained classification models, and their incapacity to reliably recognize, from the weights alone, the task a network was trained on. Overall, our results indicate that weight-space programming can be useful for small networks, such as those deployed on edge devices and wearables, but the concept still requires further investigation before it can be used in practice.

## 19. The WoW: A Large-Scale World Knowledge Corpus for Full-Lifecycle LLM Training

- Authors: Tianze Sun, Yongyao Duan, Sam Chen
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-10
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 2.946038439599703
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.13487v1
- PDF: https://arxiv.org/pdf/2611.13487v1
- Local PDF: pdf/2026-11-12_19_The WoW_ A Large-Scale World Knowledge Corpus for Full-Lifecycle LLM Training.pdf

Existing Chinese educational corpora often suffer from fragmented coverage and a lack of systematic organization. In this paper, we propose WoW (\textbf{Wo}rld Kno\textbf{w}ledge), a large-scale dataset designed for the full-cycle training of foundation models. The construction of this dataset is driven by an Educational Knowledge Graph, which serves as a taxonomic backbone for the systematic collection and completion of missing educational modules across all levels. Compared to previous versions, this iteration provides enhanced systematicity, superior quality, and a larger scale, while incorporating multimodal signals and supporting every stage of model development. Experiments demonstrate that WoW significantly improves model performance across diverse benchmarks. To facilitate community research, we further provide an interactive platform for graph-based data selection and retrieval.

## 20. An ensemble of graph generative models for assisted history matching of the Brugge field case

- Authors: Gleb Shishaev, Anton Shirokov, Shadfar Davoodi, Mohammed Al-Shargabi, Vasily Demyanov, Daniel Arnold
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-03
- DOI: Unavailable
- Categories: cs.LG, cs.NE
- Relevance: 2.945689656211527
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.12927v1
- PDF: https://arxiv.org/pdf/2611.12927v1
- Local PDF: pdf/2026-11-12_20_An ensemble of graph generative models for assisted history matching of the Brugge field case.pdf

Assisted history matching remains non-unique because many geological realisations can reproduce equivalent production responses with substantial differences between individual well matches. This ambiguity increases when a field comprises several depositional settings and modelling strategies. The paper applied a graph autoencoder approach to history matching of a benchmark Brugge field that comprises different depositional zones. Each stratigraphic zone is modelled with its dedicated generative model that comprises a joint latent space for optimisation history matching loops. Graph-based generators operate directly on the active cells of the corner-point grid, so its irregular geometry is handled without conversion to a regular lattice. The optimisation search in the 160-dimensional joint latent space is done with the Covariance Matrix Adaptation Evolution Strategy. The multi-component objective function includes static well data mismatch, dynamic production mismatch, and a geological realism penalty based on the Decoder induced latent metric. Latent space diagnostics with topological data analysis are applied prior to history matching to test whether one generator is sufficient or whether a multiple generator formulation is required. The results show that the zone-based formulation gives coherent latent spaces, preserves the main porosity and permeability relations that vary from one zone to another, and supports history matching while keeping the solutions within the learned geological manifold. The matched models reproduce field oil and water production within the prior uncertainty range and provide a comparable well-level match to previously published Brugge studies based on Ensemble Kalman Filter, Particle Swarm Optimisation with principal component analysis of parameterisation, and Multiple Kernel Learning with Particle Swarm Optimisation.

## 21. An Energy-Based Perspective on Machine Learning

- Authors: Bo Dai, Yilun Du
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-10
- DOI: Unavailable
- Categories: cs.AI, cs.LG
- Relevance: 2.9440424904165297
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.14383v1
- PDF: https://arxiv.org/pdf/2611.14383v1
- Local PDF: pdf/2026-11-12_21_An Energy-Based Perspective on Machine Learning.pdf

Energy-based models (EBMs) define a distribution through a scalar energy, $p_θ(x)\propto\exp(-E_θ(x))$, and are usually presented as one model family among many. This tutorial has a broader goal: beyond introducing EBMs, it uses them as a single lens that connects the different aspects of machine learning. Any EBM is specified by three choices, the energy, which determines what the model represents; the inference procedure, which samples from or optimizes the energy; and the learning method, which fits the energy to data. We first develop these components, including sampling, variational inference, and learning by maximum likelihood, noise contrastive estimation, pseudolikelihood, score matching, and adversarial training, and show that the learning methods share one contrastive structure. We then show that discriminative models, generative models such as GANs, normalizing flows, diffusion and autoregressive models, representation learning methods such as contrastive learning, word2vec, BERT, denoising auto-encoders, and diffusion representations, reinforcement learning with EBM policies and world models, inverse reinforcement learning, and planning, as well as inference-time computation with verifiers, are all EBMs that differ in these three choices, mostly in how they handle the partition function and sampling. This view explains existing methods, organizes them into a common framework, and suggests new algorithms by replacing one component while keeping the others, with composition of energies as a principled way to combine learned models at inference time.

## 22. Single-cell machine learning uncovers genetically anchored, cell-type specific programs of Alzheimer’s disease

- Authors: Adithya V. Madduri, Randall J. Ellis, Chirag M. Lakhani, David A. Bennett, Chirag J. Patel
- Source: openalex
- Venue type: journal
- Journal: Nature Communications
- Publication status: published
- Publication date: 2026-11-09
- DOI: https://doi.org/10.1038/s41467-026-77651-5
- Categories: Single-cell and spatial transcriptomics, Alzheimer's disease research and treatments, Dementia and Cognitive Impairment Research
- Relevance: 2.944026037424724
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://doi.org/10.1038/s41467-026-77651-5
- PDF: https://www.nature.com/articles/s41467-026-77651-5.pdf
- Local PDF: pdf/2026-11-12_22_Single-cell machine learning uncovers genetically anchored, cell-type specific programs of Alzheimer’s disease.pdf

Univariate differential expression analysis dominates single-cell transcriptomic studies of Alzheimer's disease, yet marginal testing alone cannot resolve multivariate disease-associated structure or distinguish clinical from neuropathological signatures. Here we introduce TriSCOPE, a framework integrating multivariate predictive modeling, donor-aware differential expression, and pseudotime inference, applied to six Alzheimer's disease snRNA-seq datasets comprising ~4.2 million nuclei from 627 donors. Across six major brain cell types and 41 subclusters, we identify cell-type-specific predictively expressed genes that are largely non-overlapping with differentially expressed genes, revealing disease-relevant signals invisible to univariate approaches. Conditional GWAS-eQTL colocalization anchors a subset of these predictively expressed genes to inherited Alzheimer's disease risk loci, including 27 genetically supported gene-cell type pairs (among them ARL17B, JAZF1) with no significant differential expression. Integration across all three analytical branches nominates high-confidence convergent programs including astrocytic stress markers (such as GFAP, MT2A), neuronal signaling genes (like RASGEF1B, LINGO1, NRG1), and microglial and oligodendrocyte regulators (including SYTL3, SPP1, APOD). Comparison of clinical and neuropathological models reveals cell-type-specific divergence between cognitive and pathological Alzheimer's disease signatures. Key predictively expressed genes including ARL17B, LINGO1, and APOE replicate across independent cohorts, with cross-cohort generalizability confirmed across all three analytical branches of TriSCOPE.

## 23. BioXArena-Pro: a research-grade benchmark for autonomous biomedical machine learning agents

- Authors: Loka Li, Duzhen Zhang, Xingbo Du, Leonard Song, Kun Zhang, Le Song
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-10
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 2.938938545856809
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.13994v1
- PDF: https://arxiv.org/pdf/2611.13994v1
- Local PDF: pdf/2026-11-12_23_BioXArena-Pro_ a research-grade benchmark for autonomous biomedical machine learning agents.pdf

Coding agents are increasingly proposed as autonomous builders of biomedical models, but existing benchmarks are small, near saturation or open to leaked information. We present BioXArena-Pro, 64 research-level modelling tasks from eight biomedical domains, each rebuilt from a published study; most hold out whole biological units such as species or cohorts. Across 22 agent configurations, the best scores 55.1 of 100, and the scaffold matters almost as much as the model. We re-ran a published method for every task: where the published recipe applies unchanged, the best agent and the methods tie; on rebuilt tasks the methods trail by 8.2 points, suggesting that agents gain by adapting to new data. Pretrained models (including biological foundation models) matter where the strongest agent uses them: forbidding them decreases its score on those tasks by 9 points. Every task was audited in several AI-assisted rounds and a final human review.

## 24. ScaleBrain: A Scale-Consistent Framework for EEG Foundation Models

- Authors: Minyu Zhou, Yajing Wu, Yongqiang Tang, Wang Jia, Wensheng Zhang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-10
- DOI: Unavailable
- Categories: cs.LG, eess.SP, q-bio.NC
- Relevance: 2.8889255148203654
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.14035v1
- PDF: https://arxiv.org/pdf/2611.14035v1
- Local PDF: pdf/2026-11-12_24_ScaleBrain_ A Scale-Consistent Framework for EEG Foundation Models.pdf

Foundation models pre-trained on large unlabeled electroencephalography (EEG) corpora have emerged as a transformative paradigm for Brain-Computer Interface (BCI) applications. Recent EEG foundation models have shown that multi-scale representations derived from fixed-length patches can improve EEG representation learning. Existing frameworks commonly construct temporal scales through feature-level operations. However, these operations leave the correspondence between learned features and scale-specific characteristics of the original EEG signals implicit. Moreover, when the self-supervised objective is not aligned with the multi-scale input representations, information at some temporal scales may receive insufficient supervision during pre-training. In light of this, we propose ScaleBrain, a scale-consistent pre-training framework that explicitly coordinates multi-scale representations of EEG from both the model input and optimization objective sides. Specifically, ScaleBrain introduces multi-scale EEG tokenization to represent the same EEG segment through analysis windows with different temporal spans and shared temporal anchors, and pairs these representations with scale-specific reconstruction to align with the multi-scale input structure and provide supervision across temporal resolutions during self-supervised learning. We further develop an axial spatio-temporal attention mechanism to contextualize the fused multi-scale representation along spatial and temporal dimensions. Extensive evaluations on six public BCI benchmarks against 12 representative baselines show that ScaleBrain achieves the highest mean Balanced Accuracy on five datasets and ranks third on the remaining one, with only 5.0M parameters, demonstrating strong performance and favorable parameter efficiency.

## 25. Exploring Post-Hoc Disentanglement of Audio Foundation Models for Music Similarity

- Authors: Lucas de Souza Brandão, Gabriel da Costa Merlin, Diego Furtado Silva
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-10
- DOI: Unavailable
- Categories: cs.SD, cs.LG
- Relevance: 2.861418496509431
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.14415v1
- PDF: https://arxiv.org/pdf/2611.14415v1
- Local PDF: pdf/2026-11-12_25_Exploring Post-Hoc Disentanglement of Audio Foundation Models for Music Similarity.pdf

Audio foundation models like CLAP, MuQ, and MERT excel at capturing general musical similarity. On the other hand, their entangled latent spaces limit interpretability and fine-grained attribute control. Conditional Similarity Networks (CSN) address this by pairing a backbone representation model with learned masks that gate the embedding space into attribute-specific subspaces. However, existing methods train the backbone from scratch, rather than leveraging pretrained foundation models. We instead present a systematic study of post-hoc disentanglement, adapting CSN to gate frozen pretrained embeddings. We evaluate adding trainable parameters to adapt the embedding under different masking and pooling regimes across two datasets. Our findings show that minimal adaptation capacity is sufficient for post-hoc gating to improve both attribute-specific disentanglement and overall retrieval performance, while pooling, masking, and depth choices yield limited additional gains.

## 26. Tree-Ising: Repairing Language Models with Bit-Level Ising Edits

- Authors: Hadi Salloum, Ammar Ali
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-10
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 2.840604701199526
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.14210v1
- PDF: https://arxiv.org/pdf/2611.14210v1
- Local PDF: pdf/2026-11-12_26_Tree-Ising_ Repairing Language Models with Bit-Level Ising Edits.pdf

Weight-space programming, introduced in recent MIT work by Takehi et al., enables a frontier LLM agent to read a network's weights and write a repair. Their GPT-6 Astra agent corrected the reasoning loops of Qwen3.5-0.8B without gradients, using 158 agent turns, 89.7 million tokens, and 50 forward-pass requests. Our method, Tree-Ising, casts this repair as a sparse discrete optimization problem over the model's own BF16 weights. Forward statistics define an objective that weakens a loop direction, strengthens a concluding direction, and preserves the layer's output on productive tokens. Within a state-tree representation, where lossless BF16 storage acts as a special case, the admissible edits are sign flips and exponent shifts that preserve all shared group exponents and mantissas. We decompose this objective exactly into independent QUBO (Ising) problems, one per output row, which we solve on a GPU using simulated annealing or quantum-inspired simulated bifurcation. On the agent's two layers, Tree-Ising achieves 54.6% on MATH-500, outperforming the agent's edit (51.7%) under the same evaluation protocol, while the base model scores 7.9% as reported. The simulated bifurcation solver yields a statistically indistinguishable repair at 55.1%. Both solvers outperform the agent edit across all five math benchmarks, with statistically significant improvements on MATH-500 and GSM8K after correcting for multiple comparisons. Our approach modifies 13% to 17% fewer weights and reduces BF16 bit flips by a factor of 2.2 to 2.3. It requires only four forward-pass requests and zero LLM tokens, with the annealing recipe costing about $0.90 in GPU time. On Qwen3.5-2B, with layers and dose selected using only the base model, the same recipe increases greedy GSM8K accuracy from 21.6% to 69.4%. As a proof of concept, we execute an eight-variable repair subproblem using QAOA on an IBM Heron processor.

## 27. Rethinking in Spikes: Mitigating Hallucinations in MDLMs with Step-Aware Decoding

- Authors: Zhongxing Xu, Zhonghua Wang, Zhe Qian, Shiyan Su, Ming Hu, Xiaocheng Zou, Wei Feng, Mingquan Lin, Yuyin Zhou, Yifan Peng, Hamid Rezatofighi, Zongyuan Ge
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-14
- DOI: Unavailable
- Categories: cs.CL, cs.AI
- Relevance: 2.8376799893966003
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.12901v1
- PDF: https://arxiv.org/pdf/2611.12901v1
- Local PDF: pdf/2026-11-12_27_Rethinking in Spikes_ Mitigating Hallucinations in MDLMs with Step-Aware Decoding.pdf

Recent advancements in multimodal diffusion language models (MDLMs) have exhibited strong global modeling capabilities through iterative refinement. We observe that mask uncertainty follows an overall downward trend during iterative denoising, while a few denoising steps exhibit localized entropy spikes closely associated with hallucinations. We argue that anomalous steps can be identified by measuring the entropy deviation of each denoising step from its neighboring temporal window. We hypothesize that discrete token commitment discards the distributional information at masked positions, limiting the continued interaction between candidate semantics and the context during entropy spikes. With this goal, we present StepRefine, a plug-and-play decoding strategy that leverages semantic context to achieve reliable denoising. The core of our method lies in a step-aware switch between discrete denoising and latent refinement. The model employs probability-weighted embeddings at entropy spike steps to preserve diverse reasoning hypotheses and performs multiple rounds of continuous refinement. Meanwhile, a refinement controller monitors distributional stability to reduce unnecessary loops and switch the model back to standard discrete denoising. Through extensive experiments, StepRefine demonstrates significant hallucination mitigation across different MDLMs on multimodal benchmarks.

## 28. MouldIt: Data Efficiency of Multi-Task Temporal Representation Learning in Injection Moulding

- Authors: Abdullah Ayad
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-10
- DOI: Unavailable
- Categories: cs.LG, cs.RO, eess.SP
- Relevance: 2.8217800438145564
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.13646v1
- PDF: https://arxiv.org/pdf/2611.13646v1
- Local PDF: pdf/2026-11-12_28_MouldIt_ Data Efficiency of Multi-Task Temporal Representation Learning in Injection Moulding.pdf

Smart industrial solutions that can address multiple tasks require models that understand the underlying processes. We examine representation learning for modeling the injection moulding process as an example of such solutions. We consider its data efficiency and multi-modal benefit compared to classical machine learning alternatives. To this end, we synthesize a process-informed dataset based on a real reference cycle of an Erlanger Träger part. We then introduce MouldIt, a temporal convolution and attention based variational autoencoder that reconstructs in-mould signals, while classifying parts as acceptable or as one of our synthetic failure modes. We evaluate MouldIt on two tasks, known-class classification and unknown-class detection, across nine dataset sizes in single-modal and multi-modal settings. We compare it with an accept-all baseline and the classical methods k-nearest neighbors, logistic regression, random forests, and principal component analysis, which we adapt to support both tasks. MouldIt outperforms classical methods across both tasks from 4000 cycles in the single-modal setting and from 2000 cycles in the multi-modal setting. It achieves part sorting losses of 6.0 $\pm$ 0.7% and 1.0 $\pm$ 0.3% in the single-modal and multi-modal settings respectively, ranking first across all baselines and a combination of principal component analysis and random forests.

## 29. Community benchmarking of generative models for privacy-preserving synthetic bulk RNA-seq data generation

- Authors: Hakime Öztürk, Tejumade Afonja, Joonas Jälkö, Rūta Binkytė, Pablo Rodríguez-Mier, Sebastian Lobentanzer, A B Wicks, Jules Kreuer, Sofiane Ouaari, Nico Pfeifer, Shane Menzies, Sikha Pentyala, Daniil Filienko, Steven Golob, P.S. McKeever, Jineta Banerjee, Luca Foschini, Martine De Cock, Julio Sáez-Rodríguez, Mario Fritz, Oliver Stegle, Antti Honkela
- Source: openalex
- Venue type: journal
- Journal: Genome biology
- Publication status: published
- Publication date: 2026-11-09
- DOI: https://doi.org/10.1186/s13059-026-04326-1
- Categories: Privacy-Preserving Technologies in Data, Single-cell and spatial transcriptomics, Gene expression and cancer classification
- Relevance: 2.8136886661740124
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://doi.org/10.1186/s13059-026-04326-1
- PDF: Unavailable
- Local PDF: Not downloaded

Abstract Background The synthesis of anonymized data derived from real-world cohorts offers a promising strategy for regulatory-compliant and privacy-preserving biological data sharing, potentially facilitating model development that can improve predictive performance. However, the extent to which generative models can preserve biological signals while remaining resilient to adversarial privacy attacks in high-dimensional omics contexts remains underexplored. To address this gap, the CAMDA 2025 Health Privacy Challenge launched a community-driven effort to evaluate synthetic and privacy-preserving data generation for bulk RNA-seq cohorts. Results Building on this initiative, we systematically benchmark 11 generative methods across two cancer cohorts (~ 1,000 and ~ 5,000 patients) over 978 landmark genes. Methods are evaluated across distributional fidelity, downstream utility, biological plausibility and empirical privacy risk, with emphasis on trade-offs between vulnerability to membership inference attacks and other evaluation dimensions. Expressive deep generative models achieve strong predictive utility and differential expression recovery, but are often more vulnerable to membership inference risk under the evaluated threat model. Differentially private methods improve resistance to attacks at the cost of reduced utility, while simpler statistical approaches offer competitive utility with moderate privacy risk and fast training. Conclusions Synthetic bulk RNA-seq quality is inherently multi-dimensional and shaped by trade-offs between utility, biological preservation and privacy. Our results indicate that model architecture drives distinct trade-offs across these axes, suggesting that model choice should align with dataset characteristics, intended downstream use and privacy requirements. Privacy risk should also be assessed using multiple complementary attack methods and, where possible, mitigated through formal differential privacy protection.

## 30. Decode Token Parallelism: Memory-Efficient Distributed Attention Parallelism for Scalable LLM Decoding

- Authors: Susav Shrestha, Brad Settlemyer, Narasimha Reddy
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-09
- DOI: Unavailable
- Categories: cs.DC, cs.CL, cs.LG
- Relevance: 2.807613822261551
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.13293v1
- PDF: https://arxiv.org/pdf/2611.13293v1
- Local PDF: pdf/2026-11-12_30_Decode Token Parallelism_ Memory-Efficient Distributed Attention Parallelism for Scalable LLM Decoding.pdf

Serving large language models at high concurrency with long contexts requires KV-cache capacity and attention bandwidth that grow with the decode pool. Existing parallelization strategies trade one against the other: data parallelism replicates model weights, limiting KV capacity; tensor parallelism stops scaling attention at the model's KV-head count and pushes dense collectives across nodes; and decode context parallelism (DCP) recovers capacity by sharding the sequence but adds cross-node aggregation of partial attention results. We observe that during decode, dense layers and attention scale differently: dense layers amortize weight reads across the batch and run efficiently within a single NVLink domain, whereas attention cost grows with every active request's KV cache. We present Decode Token Parallelism (TKNP), a decode-pool architecture that decouples weight placement from attention ownership. TKNP distributes a single model copy across nodes in balanced layer blocks. The active node holding a block executes its projections and MLP for the full batch using intra-node tensor parallelism, while every node computes attention for its own requests against locally resident KV cache. This extends request-local attention across nodes without replicating weights: only current-token activations cross the network, dense all-reduces remain within NVLink, and attention requires no cross-node merging of partial results. Implemented in vLLM and evaluated on Llama 3.1 405B and Nemotron-4 340B on up to 64 H100 GPUs, TKNP improves completion throughput for long-context, high-concurrency workloads by up to 1.7$\times$ over DCP and by up to 2.06$\times$ over data parallelism at matched GPU count.
