# Paper Daily Reading - 2026-09-30

## 1. Scalable GNN-based Knowledge Graph Representation Learning with Efficient Message Passing

- Authors: Huu Tan Mai, Cuong Xuan Chu, Heiko Paulheim, Daria Stepanova
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-28
- DOI: Unavailable
- Categories: cs.LG, cs.AI
- Relevance: 3.824428002554278
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.34499v1
- PDF: https://arxiv.org/pdf/2609.34499v1
- Local PDF: pdf/2026-09-30_01_Scalable GNN-based Knowledge Graph Representation Learning with Efficient Message Passing.pdf

Graph neural networks (GNNs) excel at representation learning on Knowledge Graphs (KGs), achieving stateof-the-art performance on tasks like link prediction or entity classification. However, their high computational complexity, inherent to their user-defined message passing (MP) algorithm, still prohibits their widespread adoption, especially for large KGs. Current efforts to mitigate the scalability bottlenecks of GNNs on KGs, such as subgraph sampling, are often task- and model-specific, and do not reliably guarantee lossless (if applicable) runtime/space reductions. To address this, we extend Relational Sparse Matrix Multiplication (RSPMM), originally designed to losslessly lower the space complexity of composition-based MP with pointwise composition functions, to support more expressive functions (e.g., 2x2 block-diagonal matrix multiplication, Givens rotation, circular correlation). Our method delivers significant task-independent reductions in runtime and space for current GNNs on KGs and facilitates efficient re-implementations of GNNs that maintain near state-of-the-art performance on challenging KG tasks, for a fraction of computational costs.

## 2. Graph Memory: Spectral Associative Memory via Dirichlet Energy

- Authors: Zhaoyang Shi
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-26
- DOI: Unavailable
- Categories: cs.LG, cs.IR
- Relevance: 3.8044586459092726
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.32365v1
- PDF: https://arxiv.org/pdf/2609.32365v1
- Local PDF: pdf/2026-09-30_02_Graph Memory_ Spectral Associative Memory via Dirichlet Energy.pdf

Dense associative memories have traditionally focused on storing and retrieving vector-valued patterns. Many modern machine learning problems, however, are naturally graph-structured, requiring memory mechanisms for relational patterns, graph diffusion geometries, community structures, and graph-based inductive biases. We propose a spectral dense associative memory for storage and retrieval of graph data, extending the classical vector-valued memories. Retrieval is performed through a log-sum-exp energy induced by Dirichlet energy with spectral norm distances, producing a softmax-weighted average of the stored Laplacians that remains a valid graph Laplacian. We prove exponential storage capacity and exponentially decaying retrieval error. Beyond graph retrieval, we establish theoretical guarantees for spectral quantities central to graph learning, including eigenvalues, eigenspaces, and diffusion operators. Experiments on synthetic graph data, real-world airline network, protein conformation data and wearable sensor data demonstrate robust graph retrieval while preserving the graph geometry of the data. Our framework provides a new associative memory paradigm for graph-structured data and bridges dense associative memory with modern graph learning and generative AI.

## 3. Is H&E Image-to-Spatial Transcriptomics Simpler Than It Looks?

- Authors: Duc T. Nguyen, Thanh Ha Do, Phuong M. Cao, Hieu Pham
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-26
- DOI: Unavailable
- Categories: cs.CV, cs.LG
- Relevance: 3.7736649669175137
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.32857v1
- PDF: https://arxiv.org/pdf/2609.32857v1
- Local PDF: pdf/2026-09-30_03_Is H&E Image-to-Spatial Transcriptomics Simpler Than It Looks.pdf

Predicting spatial gene expression from routine H&E histology offers a scalable route toward spatial molecular profiling. Recent work has pursued increasingly sophisticated architectures to capture spatial context and richer expression structure. At the same time, simple estimators have shown strong performance in several studies, but what they already solve and where additional complexity is needed remain unclear. We study this behavior through the structure of prediction error under the mean-squared error (MSE) objective. Differences in average expression across genes can account for a substantial part of aggregate prediction performance, while a key unresolved error lies in recovering variation within each slide. Decomposing MSE into slide-level and within-slide components, we find that the within-slide component has lower residual-normalized parameter sensitivity in controlled neural experiments. This motivates Component-Guided Loss (CGL), which increases supervision of the within-slide component. CGL-Linear is a closed-form affine instantiation that achieves overall state-of-the-art performance across HEST-1k cohorts and gene-panel sizes. The same within-slide supervision improves existing neural models. These results suggest that substantial gains can come from aligning the training objective with prediction-error structure rather than increasing model complexity.

## 4. Multi-Attractor GNNs: Set-Valued Expressivity Beyond Unique Equilibria

- Authors: Jialin Liu
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-28
- DOI: Unavailable
- Categories: cs.LG, cs.AI
- Relevance: 3.574200578989582
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.35274v1
- PDF: https://arxiv.org/pdf/2609.35274v1
- Local PDF: pdf/2026-09-30_04_Multi-Attractor GNNs_ Set-Valued Expressivity Beyond Unique Equilibria.pdf

Recurrent and equilibrium graph neural networks (GNNs) often enforce a unique fixed point or use one training target per graph. Yet many combinatorial and scientific problems admit multiple valid solutions, with no preferred one. A designated target can then impose an arbitrary selection rule. For tasks invariant to node relabeling, a symmetric graph may have a symmetric solution set but no symmetric solution.
  We show that multiple equilibria enable one weight-tied message-passing GNN to represent set-valued equivariant maps: different initializations approach different valid solutions. Under stated regularity assumptions, we first construct globally Lipschitz, permutation-equivariant dynamics that converge almost surely to valid solutions and reach every solution branch with positive probability. We then establish approximate realization by recurrent message passing with continuous component maps, with arbitrarily small update and limiting errors and arbitrarily high probability. This goes beyond standard universality arguments: although message passing alone cannot distinguish symmetric nodes, the evolving state keeps nodes distinguishable at every finite step without auxiliary node identifiers. Such dynamics can be learned without solution labels using problem-specific energies. On Ising ground states, structural module detection in protein graphs, and chemical reaction steady states, the learned updates produce multiple high-quality predictions with high numerical convergence rates. They achieve better average solution quality than the tested unique-equilibrium, single-target, and feedforward baselines, while remaining competitive with much larger diffusion-based solvers.

## 5. Multimodal LLMs Outperform Pathology Foundation Models in Cross-Domain Histological Similarity

- Authors: Yishu Zhang, Yun Li, Daiwei Zhang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-26
- DOI: Unavailable
- Categories: cs.CV, cs.AI, cs.CL, cs.LG
- Relevance: 3.510218450899762
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.32876v2
- PDF: https://arxiv.org/pdf/2609.32876v2
- Local PDF: pdf/2026-09-30_05_Multimodal LLMs Outperform Pathology Foundation Models in Cross-Domain Histological Similarity.pdf

State-of-the-art pathology foundation models, trained on millions of histology tiles, can fail to preserve tissue similarity when comparisons cross slide or institution boundaries. We show that general-purpose multimodal LLMs, without being trained as pathology foundation models, consistently outperform these specialized models in cross-domain histological similarity judgments. Using a relative similarity framework that we release as the MOSAIC (Model Similarity Assessment across Institutions and Cohorts) benchmark, we evaluate 17 models across 6 datasets and find that pathology encoders often rank same-institution, different-disease tiles as more similar than same-disease, different-institution tiles, a clinically dangerous failure mode invisible to standard within-domain evaluations. LLMs appear less susceptible to this failure, likely because they perform semantic visual comparison of morphology and tissue architecture rather than relying on shortcut features tied to acquisition context. Scaling training data does not resolve the problem for pathology encoders, implicating the learning objective rather than data coverage. Our results expose a fundamental robustness gap in current pathology foundation models and establish multimodal LLMs as a viable alternative for cross-institutional retrieval, dataset harmonization, and multi-site quality control. Code and data will be released upon acceptance.

## 6. Extremely Fast and Compact Binary Graph Representations via Randomized Operator Sketching

- Authors: Srajan Agarwal, Megha P, Bikas C Das, Zakaria Laskar, Saptarshi Bej
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-26
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.4816669025787874
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.32641v1
- PDF: https://arxiv.org/pdf/2609.32641v1
- Local PDF: pdf/2026-09-30_06_Extremely Fast and Compact Binary Graph Representations via Randomized Operator Sketching.pdf

Graph neural networks typically rely on dense, floating-point node representations, which can impose substantial memory and computational costs. Binary graph hashing offers an alternative by encoding node information as compact bit strings. However, existing approaches either sacrifice global topological information for computational efficiency or incur substantial generation costs. We introduce an ultra-fast, entirely algebraic hashing method that constructs binary node representations directly from graph structure, without requiring node features or gradient-based training. Our method approximates a high-order structural transition matrix using randomized column sampling inspired by the Nyström method and combines it with an efficient label-safe semantic propagation mechanism. The resulting continuous representations are discretized through column-wise thresholding to obtain compact binary codes. Experiments on ten node classification datasets show that the proposed method consistently improves classification accuracy over existing feature-free binary baselines while requiring sub-second code generation on many datasets. The resulting binary representations are also naturally suited to event-driven computation, making them compatible with neuromorphic spiking neural networks and gradient-free learning rules. These results demonstrate that simple algebraic approximations can provide an efficient alternative to learned pipelines for discrete graph representation learning.

## 7. GenoMorph: Pathway-Grounded Genomic Disease Reasoning via Adaptive Latent Computation

- Authors: Tanmoy Kanti Halder, Akash Ghosh, Arijit Roy, Sriparna Saha
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-28
- DOI: Unavailable
- Categories: cs.AI, q-bio.GN
- Relevance: 3.4356351280499204
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.34079v1
- PDF: https://arxiv.org/pdf/2609.34079v1
- Local PDF: pdf/2026-09-30_07_GenoMorph_ Pathway-Grounded Genomic Disease Reasoning via Adaptive Latent Computation.pdf

Large language models (LLMs) have demonstrated strong capabilities in biological reasoning; however, genomic disease inference remains largely dependent on memorized gene-disease associations rather than understanding biological pathways. This shortcut learning undermines robustness and generalization, and breaks down when molecular identifiers are unavailable. We present GenoMorph, a multimodal genomic reasoning framework that shifts disease prediction from associative gene-disease mapping toward pathway-grounded reasoning. GenoMorph couples a frozen DNA foundation model with question-conditioned cross-attention fusion, self-adaptive latent reasoning (LatentSp), a residual reasoning gate for iterative genomic evidence reinjection, and rejection sampling fine-tuning regularized by hierarchical optimal transport (OT). Rather than learning direct gene-disease mappings, GenoMorph aligns genomic sequence representations with latent pathway dynamics, enabling reasoning trajectories that follow molecular interactions before producing disease predictions. LatentSp dynamically allocates computation according to reasoning confidence, reducing unnecessary reasoning steps and improving inference efficiency. We further construct an anonymized benchmark from the Kyoto Encyclopedia of Genes and Genomes (KEGG), replacing every gene and molecular identifier with anonymous symbols while preserving sequences and pathway topology, thereby removing memorization shortcuts. GenoMorph raises the weighted F1 from 0.7863 (BioReason) to 0.9412, and rejection sampling fine-tuning with self-adaptive latent reasoning pushes it to 0.9725 while cutting latency nearly 60%. On the anonymized benchmark it reaches 0.9465 F1, substantially outperforming prior systems and confirming that accurate disease prediction can arise from pathway reasoning rather than memorized gene-disease associations.

## 8. KoopCell: Koopman-Based Generative Model for Learning Single-Cell Dynamics from Distribution Snapshots

- Authors: Wanfeng Lu, Yutong Zhang, Keyi Zhou, Chenxin Ge, Wei Lin, Qunxi Zhu
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-27
- DOI: Unavailable
- Categories: cs.LG, cs.AI, q-bio.QM
- Relevance: 3.4133102859343314
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.33350v1
- PDF: https://arxiv.org/pdf/2609.33350v1
- Local PDF: pdf/2026-09-30_08_KoopCell_ Koopman-Based Generative Model for Learning Single-Cell Dynamics from Distribution Snapshots.pdf

Learning population dynamics from temporally sparse, unpaired distribution snapshots is a fundamental challenge in developmental biology. Recent approaches based on neural differential equations and flow matching can interpolate between observed population snapshots, but may struggle to extrapolate beyond the training horizon and often lack an explicit mechanism for modeling developmental branching. We propose KoopCell, a unified generative framework based on Koopman-Mori-Zwanzig theory that jointly learns representations and predictive linear latent dynamics. Theoretically, using the weak continuity equation, we derive a closed-form least-squares estimator for the Koopman generator from distribution snapshots and establish convergence guarantees under suitable assumptions. To model branching dynamics, we further develop KoopCell-M, which incorporates non-Markovian memory into the latent Koopman dynamics through a Markovian embedding. Experiments on synthetic systems and three scRNA-seq datasets demonstrate the ability of our framework to recover Koopman spectra, model branching through memory, and scale to predicting high-dimensional gene expression distributions, achieving state-of-the-art performance among the evaluated methods.

## 9. Compute Time Scaling with Recursive Models for Combinatorial Optimization

- Authors: Zhengxi Zhang, Paul Swoboda
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-28
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.4065856765186986
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.34585v1
- PDF: https://arxiv.org/pdf/2609.34585v1
- Local PDF: pdf/2026-09-30_09_Compute Time Scaling with Recursive Models for Combinatorial Optimization.pdf

We propose Tiny Recursive Models for Combinatorial Optimization (\ours{}), a general neural method for combinatorial optimization that scales both depth (how often we recursively invoke our network) and width (how much we sample in parallel). Both are fundamental for combinatorial optimization: hard instances demand a large amount of compute, while a small network is essential to avoid overfitting and capture the algorithmic essence of optimization. In particular, our method consists of a graph-aware tiny recursive model that iterates on a latent state with adaptive halting and needs only a lightweight problem-specific decoder. Compared with previous heatmap-based general neural solvers, it achieves a better balance between solution quality and inference speed on both the Traveling Salesman Problem~(TSP) and the Maximum Independent Set~(MIS) problem, and remains competitive with hybrid methods that combine neural components with heuristics specific to each problem. With the same backbone architecture for both tasks, \ours{} outperforms every diffusion-based solver on TSP from 500 to 10,000 cities at a lower inference cost, and on the standard Erdős--Rényi-[700-800] MIS benchmark it surpasses all neural solvers except those that only work well on MIS. We then explore self-relabeling for self-supervised training. We periodically replace the current set of training labels with the model's own better solutions, as an alternative training signal. Self-relabeling can, while forgoing supervision from near-optimal solutions, still result in on-par quality.

## 10. CORTEX: Learning to Share and Specialize in Dense Language Models

- Authors: Chuiyang Meng, Ming Tang, Vincent W. S. Wong
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-28
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 3.3990222674559845
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.34449v1
- PDF: https://arxiv.org/pdf/2609.34449v1
- Local PDF: pdf/2026-09-30_10_CORTEX_ Learning to Share and Specialize in Dense Language Models.pdf

Large language models are trained on heterogeneous data mixtures, where different knowledge domains require both shared knowledge and specialization. Existing modular approaches typically impose explicit components or discover modules through interpretability analysis after training. In this work, we propose CORTEX, a learning dynamics-inspired framework that learns internal modularization within dense language models. CORTEX partitions trainable matrices into parameter groups and learns module assignments from domain-conditioned gradient and cross-domain gradient similarity. We introduce the selective lesion score and module-domain mutual information to characterize the target-domain lesion effects and alignment, and analyze how module assignment affects the trade-off between assignment bias and update magnitude. Experiments with 160M, Qwen3-8B, and Qwen3-32B backbone models show that CORTEX achieves the highest synthetic-domain exact match and largest average perplexity reduction, while remaining competitive on real-domain evaluations and forming identifiable modules.

## 11. Modeling Whole-Slide Images as Dynamic Tumor Microenvironment Fields

- Authors: Lei Wu, Jiashuai Liu, Di Zhang, Zhangpeng Gong, Yingkang Zhan, Yi Niu, Jiusong Ge, Chunze Yang, Kai Yi, Mireia Crispin-Ortuzar, Chen Li, Zeyu Gao
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-28
- DOI: Unavailable
- Categories: cs.CV, cs.AI
- Relevance: 3.3985692049800336
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.34451v1
- PDF: https://arxiv.org/pdf/2609.34451v1
- Local PDF: pdf/2026-09-30_11_Modeling Whole-Slide Images as Dynamic Tumor Microenvironment Fields.pdf

Due to the gigapixel-scale nature of whole-slide images (WSIs), weakly supervised WSI analysis is commonly formulated as a multiple instance learning (MIL) problem, where patch-level features are aggregated into slide-level representations. However, diagnostic and prognostic evidence often arises from spatially coherent tumor microenvironment regions and their interactions, rather than isolated patches alone. Existing patch-level or static region-based methods usually overlook how tissue regions should be adaptively formed and subsequently evolved through microenvironment interactions across heterogeneous boundaries. In this paper, we propose Concept-Guided Tumor Microenvironment Evolution (TMEvolve), a reaction-diffusion-inspired framework that models WSIs as latent tumor microenvironment fields over discrete patch graphs. TMEvolve instantiates this view as a learnable graph-discretized evolution process over patch neighborhoods. It first forms adaptive soft tissue regions as coherent microenvironment units, then performs pseudo-time evolution through two complementary local dynamics: intra-region diffusion, which stabilizes latent states within coherent tissue compartments, and concept-guided boundary flux, which propagates visual feature signals and language-derived concept signals across heterogeneous region interfaces. The evolved microenvironment regions are finally aggregated for slide-level prediction. We evaluate TMEvolve on six datasets across three weakly supervised WSI tasks: survival prediction, gene expression prediction, and histological subtype classification. TMEvolve consistently improves over representative MIL methods, pathology foundation models, and concept-guided baselines. Ablation studies and visualizations further support the effectiveness and interpretability of TMEvolve, highlighting the value of dynamic region modeling and boundary interaction.

## 12. HyperReCo: Retrieving and Connecting Evidence with Hypergraph Neural Networks for LLM Multi-hop Reasoning

- Authors: Zicheng Zhao, Linhao Luo, Junnan Dong, Haoran Luo, Xiaoli Li, Shirui Pan, Chen Gong
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-26
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 3.376148093908413
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.32327v1
- PDF: https://arxiv.org/pdf/2609.32327v1
- Local PDF: pdf/2026-09-30_12_HyperReCo_ Retrieving and Connecting Evidence with Hypergraph Neural Networks for LLM Multi-hop Reasoning.pdf

Large language models (LLMs) have shown strong capabilities, with retrieval-augmented generation (RAG) supporting complex multi-hop reasoning by retrieving evidence distributed across documents. Graph-based approaches exploit connections among evidence, and hypergraph-based retrieval further preserves higher-order entity associations within documents and connects documents through shared entities. However, existing hypergraph retrievers often rely on predefined structural expansion or diffusion, which may miss query-dependent interactions needed to identify relevant evidence. They also leave connections among retrieved evidence implicit, requiring LLMs to reconstruct these connections before reasoning. Therefore, we propose HyperReCo, a framework for retrieving and connecting evidence with a hypergraph neural network (HyperGNN). We represent each document as a hyperedge over its extracted entities, with shared entities connecting the hyperedges. Through hypergraph message passing with joint supervision over documents and entities, the HyperGNN learns query-dependent interactions to retrieve complementary evidence. We further introduce Gradient-Guided Hyper-Path Decoding (GGHD), which uses gradient attribution to interpret the learned interactions and translate them into explicit hyper-paths that help LLMs combine complementary facts for multi-hop reasoning. Experiments on six benchmarks show that HyperReCo achieves the best retrieval performance among the compared methods on all three multi-hop QA datasets, together with strong downstream QA performance. Case studies and further analyses demonstrate the utility of decoded hyper-paths for connecting retrieved evidence.

## 13. TemporalGraphLLM: Temporal Graph Neural Networks with Large Language Models for Dynamic Text-Attributed Graphs

- Authors: Moran Beladev, Or Eitan, Gilad Katz, Lior Rokach
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-25
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.352579858644674
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.31881v1
- PDF: https://arxiv.org/pdf/2609.31881v1
- Local PDF: pdf/2026-09-30_13_TemporalGraphLLM_ Temporal Graph Neural Networks with Large Language Models for Dynamic Text-Attributed Graphs.pdf

Dynamic text-attributed graphs (DTAGs), where nodes, edges, and textual attributes evolve over time, are crucial in applications such as social networks, citation graphs, and knowledge graphs. However, existing approaches struggle to jointly model the temporal evolution of graph structures and the semantic richness of textual attributes. While Temporal Graph Neural Networks (TGNNs) capture evolving node relationships, they often lack contextual text reasoning. Conversely, Large Language Models (LLMs) excel in textual understanding but struggle with structured graph reasoning in temporal settings. To bridge this gap, we propose TemporalGraphLLM, a novel framework that can integrate any temporal GNN with an LLM for enhanced reasoning in DTAGs. Our approach fine-tunes LLMs using graph-time-aware instruction tuning and novel temporal GNNs injection to replace dedicated added tokens with graph embeddings. TemporalGraphLLM effectively leverages pretrained TGNNs within an LLM framework to achieve state-of-the-art performance on edge classification, link prediction, and edge-based text generation tasks. Extensive evaluation on real-world dynamic graph datasets demonstrates state-of-the-art performance. Our findings highlight the synergistic potential of LLMs and TGNNs, opening new directions for learning on evolving graphs.

## 14. Not All Thinking is Created Equal: Latent Reasoning Discovers a Recurrent Search Algorithm for Depth Generalization

- Authors: Huzi Cheng, Zhewei Zhang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-28
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 3.332521557606536
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.35643v1
- PDF: https://arxiv.org/pdf/2609.35643v1
- Local PDF: pdf/2026-09-30_14_Not All Thinking is Created Equal_ Latent Reasoning Discovers a Recurrent Search Algorithm for Depth Generalization.pdf

Large Language Models can perform multi-step reasoning and improve task performance through different forms of intermediate computation, from token-based traces to computation carried out in latent space. However, a question remains open: do these different forms of thinking rely on the same underlying mechanism? To address this, we train and compare five variants of the same GPTNeoX backbone from scratch on an extended multi-hop reasoning task (ProsQA-Ext): a vanilla model, a Chain-of-Thought (CoT) model, a Pause Token model, and two latent-reasoning models that are optimized end-to-end without intermediate reasoning traces. We find that, strong in-distribution (ID) performance does not guarantee depth generalization. Vanilla, CoT, and Pause Token models solve ID problems well, but rely largely on local graph features and generalize poorly to out-of-distribution (OOD) problems with longer hops. In contrast, latent variants generalize better and show internal dynamics consistent with forward reachability propagation on the graph. Causal interventions and circuit analysis localize this computation to a sparse recurrent search circuit in the bottleneck latent model: an attention head retrieves graph relations, an MLP and the residual stream update the reachability state across recurrent steps, while multiple attention heads together then do the candidate matching. Together, these results show that different thinking mechanisms can learn distinct computational solutions, even at similar ID performance. In this setting, latent recurrence supports a reusable forward-search algorithm that generalizes beyond the training depth.

## 15. Panoptic Scene Program Diffusion Transformer

- Authors: Chika Maduabuchi
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-24
- DOI: Unavailable
- Categories: cs.CV, cs.LG
- Relevance: 3.3197407985896685
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.31780v1
- PDF: https://arxiv.org/pdf/2609.31780v1
- Local PDF: pdf/2026-09-30_15_Panoptic Scene Program Diffusion Transformer.pdf

Modern text-to-image models produce high-fidelity images but still struggle with compositional prompts that require instance identity, attribute ownership, counting, spatial ordering, and role-sensitive relations. We introduce Panoptic Scene Program Diffusion Transformer (PSP-DiT), a diffusion-transformer architecture that treats a panoptic scene program as a first-class latent variable rather than an external control signal or post-hoc parse. PSP-DiT jointly denoises image latents and scene-program latents through coupled transformer streams, while panoptic grounding and cycle-consistency objectives tie object instances, attributes, relations, and counts to visual support in the generated image. Under matched training and inference settings, PSP-DiT improves over a strong flat-text baseline across GenEval 2, SANEval-Simple, PSG-Score, and DetailMaster, with the largest gains on counting, attribute binding, role-sensitive relations, and long structured prompts. The method preserves image quality, adds modest inference overhead, and remains robust to imperfect scene programs.

## 16. Structured Latent Modeling for Supervised Multimodal Information Decomposition

- Authors: Wanting Huang, Sanvesh Srivastava, Weiran Wang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-28
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.3086471567571762
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.35502v1
- PDF: https://arxiv.org/pdf/2609.35502v1
- Local PDF: pdf/2026-09-30_16_Structured Latent Modeling for Supervised Multimodal Information Decomposition.pdf

Multimodal prediction relies on diverse forms of evidence: information repeated across modalities, cues specific to a single source, and complex cross-modal dependencies that emerge only when inputs are considered together. While recent methods promote richer interactions, they lack a principled way to isolate these target-relative contributions within learned continuous representations. We introduce a framework that applies contrastive or masked objectives at intermediate layers, coupled with source-wise invertible normalizing flows and a supervised, low-rank latent variable model. This architecture explicitly factorizes the joint distribution into shared task-relevant variation, modality-specific predictive variation, and task-irrelevant dependence. Drawing connections to prior multimodal learning assumptions, our approach evaluates how modalities independently and jointly contribute to the target. Ultimately, this framework unites intermediate representation learning with structured likelihood-based guidance, offering a practical latent-variable lens for characterizing continuous multimodal interactions. Empirically, we demonstrate the effectiveness of our approach across diverse multimodal benchmarks, showing robust improvements in predictive performance.

## 17. You Can't Have It Both Ways: Concept Entanglement Limits Diffusion Model Unlearning

- Authors: Yian Wang, Ali Ebrahimpour-Boroojeny, Hari Sundaram, Varun Chandrasekaran
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-28
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 3.2960348481113746
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.34137v1
- PDF: https://arxiv.org/pdf/2609.34137v1
- Local PDF: pdf/2026-09-30_17_You Can't Have It Both Ways_ Concept Entanglement Limits Diffusion Model Unlearning.pdf

Concept unlearning in text-to-image diffusion models aims to suppress a target concept (e.g., \texttt{horse}) while preserving related but distinct content (e.g., \texttt{donkey}), yet existing methods either leak under indirect prompts or visibly degrade other concepts. We show that these failure modes stem from the geometry of concept representations rather than from any particular algorithm. Formalizing concepts as activation-space regions, we prove that the overlap between a target and other concepts lower-bounds the damage any robust erasure must inflict on them, with the trade-off scaling linearly in the degree of overlap. Across thirteen unlearning methods, including methods designed to preserve non-target concepts, no method achieves both strong erasure and strong neighbor preservation: STEREO nearly eliminates indirect leakage but cuts neighbor generation by more than 75\%, while sparse inference-time methods preserve neighbors but leak. Damage increases with our overlap measure, monotonically so for STEREO; the $κ$-scaling reproduces on SDXL, and neighbor-selective damage recurs on FLUX. Perfect unlearning is the wrong target for entangled concepts; methods should be evaluated on the Pareto frontier our theorem establishes.

## 18. Do World Models Learn Global Understanding?

- Authors: Alexander Detkov, Matt Thomson
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-28
- DOI: Unavailable
- Categories: cs.LG, cs.AI
- Relevance: 3.280349801058983
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.34058v1
- PDF: https://arxiv.org/pdf/2609.34058v1
- Local PDF: pdf/2026-09-30_18_Do World Models Learn Global Understanding.pdf

AI systems often feel brittle and fragmented. A large language model (LLM) may correctly explain a concept but fail to apply it, or follow safety instructions in one context but not another. This behavior suggests a general failure to lift local information to a global understanding. To gain fundamental insight, we frame "understanding" as learning constraints and propagating their consequences. We construct learning tasks on monoid worlds, sets of states connected by action transitions, where observed training transitions and an unseen constraint jointly determine held-out transitions. Measuring generalization tests whether models can learn global constraints from local transitions and propagate their consequences. We consider inverse, commutativity, composition, and periodicity constraints relevant to spatial and semantic structure. Across attention, recurrent, and state-space architectures, next-state training fits the data but fails to propagate non-trivial constraints. Compositional training, which uses identical paths but hides intermediate states from the input, achieves 96% accuracy on inverse, commutativity, and composition constraints across architectures, yields corresponding improvements in geometric generalization of world models trained on embodied environments and relational generalization in Wikidata-finetuned LLMs. How far do models propagate constraints when inferring an unseen fact may depend on first inferring others? We define proof depth d of a held-out transition, measuring the minimum number of inference rounds to infer the transition, and find that model generalization decreases sharply with proof depth. Increasing compositional path length T improves generalization. These results provide a formal way to investigate global understanding in language and world models and demonstrate that compositional training promotes information propagation and integration.

## 19. Permutation-Equivariant Flow Matching for Alignment-Free Neural Weight Generation

- Authors: Arkadi Piven, Yam Eitan, Guy Bar-Shalom, Fabrizio Frasca, Daniel Cremers, Thomas Dagès, Ron Kimmel, Haggai Maron
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-26
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.2764704447321624
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.32833v1
- PDF: https://arxiv.org/pdf/2609.32833v1
- Local PDF: pdf/2026-09-30_19_Permutation-Equivariant Flow Matching for Alignment-Free Neural Weight Generation.pdf

A trained neural network can be represented by a parameter vector in high dimensions. Learning distributions over these vectors enables the generation of new models across various tasks and architectures. A central challenge is permutation symmetry: permuting hidden neurons can produce distant parameter vectors representing the same function. This introduces variations that a generative model must account for when learning from trained networks. Existing methods typically address this using networks derived from a common base model or costly approximate neuron alignment. We instead parameterize a flow-matching velocity field with a permutation-equivariant Graph Meta Network, enabling direct learning from independently trained networks without alignment. Extensive experiments show that our method closely reproduces the joint statistics of accuracy, functional similarity, and weight similarity of independently trained collections, providing evidence of generation beyond checkpoint memorization. A single conditional model also generates task-specific networks on heterogeneous architectures and generalizes to unseen hidden-width configurations. On a tabular domain-shift task, intermediate conditioning produces individual networks with performance comparable to logit ensembles across both domains. Taken together, our results show how permutation equivariance enables learning from diverse collections of independently trained networks without permutation alignment.

## 20. Bison: Cross-Dataset Learning for Unseen-Compound Perturbation Prediction

- Authors: Yunfan Liu, Kasra Ghorbani, Yufei Huang, Zicheng Liu, Jiangbin Zheng, Jingbo Zhou, Shaorong Chen, Chang Yu, Stan Z. Li
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-26
- DOI: Unavailable
- Categories: cs.LG, cs.AI
- Relevance: 3.2668251343768855
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.32467v1
- PDF: https://arxiv.org/pdf/2609.32467v1
- Local PDF: pdf/2026-09-30_20_Bison_ Cross-Dataset Learning for Unseen-Compound Perturbation Prediction.pdf

Predicting transcriptional responses to unseen compounds is limited by fragmented chemical coverage and heterogeneous experimental platforms and gene panels. To assess molecular generalization across these settings, we build on Chem-PerturBridge to benchmark eight datasets with 16,771 compounds, withholding test compounds from every training dataset. This comparison reveals that high overall response agreement can coexist with weak prediction of drug-specific differences, despite reproducible signals across repeated measurements. To exploit complementary chemical supervision while targeting these differences, we introduce Bison: a shared gene representation connects native panels, while two discrete diffusion models compose context-dependent responses with molecular deviations learned through matched drug-contrast supervision. A single Bison model jointly trained across all eight datasets achieves the highest mean overall-response and drug-contrast Pearson correlations on the full benchmark in comparison with 11 methods trained independently per dataset. Compared with dataset-specific training of the same architecture, joint training increases mean drug-contrast correlation by 27.4\%, with gains across all eight datasets and improvements in overall response prediction. These results demonstrate how matched drug contrasts turn complementary screens into shared molecular supervision for unseen-drug response prediction while preserving native gene measurements.

## 21. First Learn, Then Memorize: The Spectral Bias of Diffusion Models

- Authors: Raphaël Urfin, Tony Bonnaire, Giulio Biroli, Marc Mézard
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-28
- DOI: Unavailable
- Categories: cs.LG, cond-mat.dis-nn
- Relevance: 3.2637250860400306
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.35377v1
- PDF: https://arxiv.org/pdf/2609.35377v1
- Local PDF: pdf/2026-09-30_21_First Learn, Then Memorize_ The Spectral Bias of Diffusion Models.pdf

Diffusion models trained on a finite dataset first learn to generate novel, high-quality samples and only much later collapse onto their training set. We identify the mechanism behind this separation of timescales and the object that probes it. The training dynamics of the score function are governed---exactly, and at any width---by the Gram matrix of the Neural Tangent Kernel (NTK) evaluated on the noisy training data, so the timescales of generalization and of memorization must be encoded in its spectrum. We show that they are, and that the structure responsible has no analogue in standard kernel settings. The use of multiple noise realizations per sample ($m$ noised copies at a fixed noise level) in the score-matching loss is what restructures the Gram matrix spectrum into two distinct parts. The first, of large eigenvalues, carries the global features of the target distribution and is present already for $m=1$. The second, which the repeated noising creates, consists of the smallest eigenvalues and is supported on eigenvectors aligned with the sample-specific noise directions; it sets a memorization timescale parametrically larger in the training set size $n$. We establish this picture on two fronts. Analytically, we solve the spectrum in the lazy high-dimensional limit for both linear ($n \asymp d$) and polynomial ($n \asymp d^k$) sample complexities, and prove through a bias--variance decomposition that the first bulk minimizes the approximation error while the second drives the error associated with memorization. Empirically, we show the same two-bulk structure in Convolutional NTKs on CelebA and in finite-width U-Nets trained well beyond the lazy regime, and we make the link causal: truncating the Gram matrix at rank $r$ tunes the generalization--memorization transition, and an $L_2$ penalty targeting the second bulk suppresses memorization in feature-learning U-Nets.

## 22. InterTab: Interleaved Visual-Structure Alignment for Multi-Modal Table Reasoning

- Authors: Hanqian Li, Sirui Huang, Chen Ling, Jungang Li, Yu Huang, Kening Zheng, Yonghua Hei, Xiangrong He, Shiyi Wang, Pengcheng Zhu, Dongnan Liu, Wei Zhou, Linjian Mo, Nai Ding, Xuming Hu
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-26
- DOI: Unavailable
- Categories: cs.CV, cs.AI
- Relevance: 3.2357703910215463
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.32660v1
- PDF: https://arxiv.org/pdf/2609.32660v1
- Local PDF: pdf/2026-09-30_22_InterTab_ Interleaved Visual-Structure Alignment for Multi-Modal Table Reasoning.pdf

Table images preserve structural information that are often lost in text serialization, and reasoning over them requires locating relevant rows, columns, and cells step by step. Current multimodal large language models (MLLMs) encode the whole image once before reasoning, so they cannot pick up row-, column-, and cell-level evidence as the question unfolds. Encoder-side table structure and generic interleaved visual chain-of-thought still do not bind each reasoning step to that structure. We propose \textbf{InterTab}, an \textbf{Inter}leaved structure-aware framework for CoT reasoning over \textbf{Tab}le images, interleaves chain-of-thought with tool calls that crop structure-aligned table regions. First, we build InterTab-22K, includes reasoning trajectories in which each step is tied to both a structural location and a bounding box. InterTab is trained in two stages: supervised structure-aware alignment (SSA) on InterTab-22K teaches the model to interleave reasoning with structure-aligned crops, and active localization optimization (ALO) further optimizes answer correctness, localization IoU, and output format, while penalizing missing or excessive tool calls. Experiments on nine table benchmarks show that InterTab improves the average accuracy of its backbone from 68.28% to 73.17% and achieves the best average performance among all compared methods. Code and data will be released soon.

## 23. Feasible Flow Matching for Graph Reconstruction via Within-Sampling Primal-Dual Guidance

- Authors: Haoming Chen, Nicolas Zilberstein, Santiago Paternain, Santiago Segarra
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-26
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.2090257876125556
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.32980v1
- PDF: https://arxiv.org/pdf/2609.32980v1
- Local PDF: pdf/2026-09-30_23_Feasible Flow Matching for Graph Reconstruction via Within-Sampling Primal-Dual Guidance.pdf

Graph reconstruction from partial observations often comes with structural side information, such as degree bounds, triangle counts, or an edge-density band. Prior-Informed Flow Matching (PIFM) reconstructs graphs by transporting a local prior toward the graph distribution, but it provides no mechanism to incorporate this side information. We put forth Constrained Primal-Dual PIFM (CPD-PIFM), which augments the sampler with Lagrange multipliers that evolve along each trajectory. The multipliers respond to constraint violations at a predicted endpoint and guide subsequent sampling steps without retraining. We prove that the sampler inherits PIFM's permutation equivariance and bound its expected terminal slack by a term that decays as the inverse square root of the number of steps, plus two approximation terms. On three link-prediction benchmarks and nine combinations of datasets and constraints, CPD-PIFM raises feasibility by 11-26 percentage points and remains competitive with fixed guidance without selecting a separate multiplier for each constraint.

## 24. Collaborative Principle Evolution via Evidence Transfer for Scientific Discovery

- Authors: Yingming Pu, Hongyu Chen, Tao Lin
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-28
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.200289328722799
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.35315v1
- PDF: https://arxiv.org/pdf/2609.35315v1
- Local PDF: pdf/2026-09-30_24_Collaborative Principle Evolution via Evidence Transfer for Scientific Discovery.pdf

Large Language Model (LLM)-based agents promise to automate scientific discovery, yet exploring the vast hypothesis space remains costly. Existing principle-evolution methods accelerate this loop, but operate sequentially, which caps exploration breadth and wastes wall-clock time on challenging problems. To address this, we formulate collaborative scientific discovery as evidence transfer between parallel principle-evolution branches. We present COEVOLVE, which realizes this transfer through a coordination core over parallel branches. By integrating value-of-information-gated routing and context-discounted likelihood injection, COEVOLVE enables branches to collaborate through shared measurements while keeping their principle posteriors separate. Across six scientific-discovery tasks under a matched evaluation budget, COEVOLVE attains a mean solution quality of 66.5% versus 57.0% for single-branch principle evolution, with a 1.80x mean wall-clock speedup on the GPT-5.6-Terra backbone; on five auto-research tasks delegated to an autonomous research harness, it is the only arm whose mean stays above the published SOTA anchor on every task. These results establish when evidence sharing accelerates parallel discovery and when transfer safeguards are necessary to limit negative or inert transfers

## 25. EngramRAG: Dynamic Usage-Weighted Topology and Synaptic Consolidation for Multi-Hop Agentic Memory

- Authors: Bhavyateja Potineni, Lohit Giri, Anu Jain, Vadim Kutsyy, Rajasekhar Pentakota
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-25
- DOI: Unavailable
- Categories: cs.AI, cs.CL, cs.IR, cs.MA
- Relevance: 3.187059525862251
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.32049v1
- PDF: https://arxiv.org/pdf/2609.32049v1
- Local PDF: pdf/2026-09-30_25_EngramRAG_ Dynamic Usage-Weighted Topology and Synaptic Consolidation for Multi-Hop Agentic Memory.pdf

As autonomous LLM agents are deployed across multi-session environments, conventional memory architectures suffer from Associative Blindness (inability to traverse multi-hop relational dependencies), Scaffolding Amnesia (temporal decay evicting core persona invariants), and Static Topology Stagnation (immutable graphs ignoring usage dynamics). Grounded in Complementary Learning Systems (CLS) principles, we propose EngramRAG, an adaptive memory architecture coupling a low-latency Waking State reflex with an asynchronous background Dreaming State consolidation cycle. EngramRAG introduces: (1) Usage-Modulated Personalized PageRank (U-PPR), where transition probabilities adapt via Hebbian plasticity to promote persistent entities into high-centrality Epistemic Macro-Hubs; (2) Consolidation-Activated Topology Decay (CATD), which scales retention half-life by topological load-bearing weight rather than wall-clock recency, protected by a cold-start grace period (N_grace >= 4); (3) Directed SUPERSEDES DAG filtering to suppress obsolete state during fact mutations; and (4) Triple-source hybrid retrieval fusing dense vectors, BM25, and U-PPR via dynamic Reciprocal Rank Fusion (RRF). Evaluating on all 1,982 QA pairs across 10 long-term conversations in the LoCoMo benchmark, EngramRAG achieves +38.9% relative improvement in Recall@5 (53.21% vs. 38.29%, p < 0.001) and +43.1% in MRR (0.4203 vs. 0.2937) over dense vector RAG, significantly outperforming Okapi BM25 (48.66%) and isolated static graph retrieval (8.50%). On temporal reasoning, EngramRAG reaches 62.33% Recall@5 (+16.67 points over dense vectors). In controlled mutation tests, SUPERSEDES suppresses split-brain hallucinations from 70.0% to 0.0%, while 90-day simulations show 100.0% scaffolding retention under a 26.21ms interactive retrieval reflex.

## 26. Making LLMs Truly Forget: Deep Unlearning by Searching, Selecting, and Severing Knowledge Paths

- Authors: Jialu Wang, Peizhi Niu, Haoteng Yin, Hans Hao-Hsun Hsu, Pan Li, Rongzhe Wei
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-28
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.1844529019781875
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.34442v1
- PDF: https://arxiv.org/pdf/2609.34442v1
- Local PDF: pdf/2026-09-30_26_Making LLMs Truly Forget_ Deep Unlearning by Searching, Selecting, and Severing Knowledge Paths.pdf

While an unlearned language model may no longer recall a fact directly, the fact often remains recoverable through multi-hop reasoning over related knowledge. Most existing unlearning techniques overlook this vulnerability, targeting facts in isolation while leaving their supporting knowledge intact. To achieve true forgetting, we propose a general deep unlearning framework compatible with existing unlearning algorithms. Our approach adaptively explores both explicit responses and latent internal representations to discover valid reasoning paths, compiles them into a confidence-aware supporting subgraph, and we apply a graph minimum cut to sever all recovery paths while preserving unrelated knowledge. To rigorously evaluate deep unlearning, we introduce a model-specific pipeline that extracts and completes knowledge graphs from raw text, filtering them by calibrated model confidence to reflect what the model genuinely retains. Comprehensive experiments demonstrate that selectively unlearning supporting knowledge yields substantially deeper forgetting than superficial methods while preserving model utility, highlighting that genuine unlearning requires breaking the relational structures that enable factual reconstruction.

## 27. The Devil is in the Spectrum Bias: Spectrum-Balanced Feature Matching for Robust Representation Distillation

- Authors: Kuniaki Saito, Yoshitaka Ushiku
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-28
- DOI: Unavailable
- Categories: cs.CV, cs.AI
- Relevance: 3.1780377760651533
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.34106v1
- PDF: https://arxiv.org/pdf/2609.34106v1
- Local PDF: pdf/2026-09-30_27_The Devil is in the Spectrum Bias_ Spectrum-Balanced Feature Matching for Robust Representation Distillation.pdf

Large visual foundation models have demonstrated remarkable transferability across a wide range of downstream tasks. To deploy such models efficiently, feature matching has become a popular knowledge distillation approach that transfers teacher representations to smaller student models without requiring labeled data. However, we show that the conventional feature matching objective with L2-distance is inherently biased toward reconstructing dominant spectral directions of the teacher representation, while under-optimizing low-variance directions that often contain task-relevant information. To address this, we propose Spectrum-Balanced Feature Matching, SpecMatch, a simple objective that adaptively emphasizes under-optimized spectral directions while preserving the relative importance of dominant directions. SpecMatch is easy to implement and introduces negligible computational overhead. Extensive experiments on image recognition demonstrate that SpecMatch consistently improves downstream adaptation across diverse tasks, including image classification, anomaly detection, medical image analysis, and domain generalization. In particular, SpecMatch outperforms conventional feature matching in 40 of 42 teacher--student and training-setting combinations, while consistently improving over the original student model in all settings. We further demonstrate that the proposed objective generalizes beyond vision, improving downstream performance across six protein understanding tasks.

## 28. Scaffold Then Internalize: Representation Injection for Diffusion Transformers

- Authors: Han Fu, Jiacheng Chen, Baoquan Zhao, Weidong Chen, Wei Liu, Qing Li, Xudong Mao
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-28
- DOI: Unavailable
- Categories: cs.CV, cs.LG
- Relevance: 3.1727665922389585
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.35292v1
- PDF: https://arxiv.org/pdf/2609.35292v1
- Local PDF: pdf/2026-09-30_28_Scaffold Then Internalize_ Representation Injection for Diffusion Transformers.pdf

Recent representation alignment (REPA) methods accelerate diffusion transformer training by aligning projections of the transformer's hidden states with representations from pretrained visual encoders. In this work, we explore a reverse and complementary direction to REPA: rather than projecting diffusion representations into the encoder's space, we inject encoder representations into the diffusion transformer, allowing them to actively participate in the denoising process. To this end, we introduce \textit{REPresentation Injection} (REPI), a training framework based on a scaffold-to-internalization strategy, in which projected encoder representations initially serve as a temporary scaffold and are then progressively internalized by the diffusion transformer. REPI outperforms REPA across a wide range of backbones and is highly complementary to it: combining the two yields substantial gains over either alone. Notably, with only 160K training steps, REPI + REPA matches vanilla SiT trained for 7M steps, a speedup of over $43.5\times$. Code will be available at https://jeneveuxpas.github.io/REPI

## 29. Graph Forward Distribution Matching for Molecular Inverse Design

- Authors: Yihan Zhu, Yuhan Liu, Brett Savoie, Tengfei Luo, Meng Jiang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-25
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.1624090850435884
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.32056v1
- PDF: https://arxiv.org/pdf/2609.32056v1
- Local PDF: pdf/2026-09-30_29_Graph Forward Distribution Matching for Molecular Inverse Design.pdf

Achieving precise control over multiple properties without sacrificing chemical validity remains a central challenge in molecular inverse design. Existing reinforcement learning (RL) methods fine-tune graph diffusion models by treating **reverse** sampling as a sequential policy, using a single terminal reward to optimize hundreds of coupled decisions. They often suffer from instability, validity collapse, and limited property gains. We introduce GraphFDM (Graph Forward Distribution Matching), a new online RL paradigm for graph diffusion that performs optimization through the **forward** process. GraphFDM uses valid generations to define a reward-tilted target distribution jointly optimized over graph size and molecular structure for each property condition, incorporating reinforcement signals into supervised learning without storing reverse trajectories. We derive the unique optimal target, prove a condition-wise improvement guarantee, and show that the fixed graph-size prior of standard graph diffusion leaves an irreducible matching gap. In multi-conditional polymer and small-molecule generation, GraphFDM achieves the lowest MAE on every target property, with reductions of up to 53.0\% relative to the strongest baselines and chemical validity above 0.99. It further generalizes to out-of-distribution property combinations.

## 30. Residual-Stream Burden Shapes Representation Learning in Diffusion Transformers

- Authors: Tongtong Liang, Siqi Kou, Ziqiao Xi, Esha Singh, Kun Zhou, Zhijie Deng, Alexander Cloninger, Yu-Xiang Wang, Rahul Parhi
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-27
- DOI: Unavailable
- Categories: cs.CV, cs.LG
- Relevance: 3.1567210455619343
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.33895v1
- PDF: https://arxiv.org/pdf/2609.33895v1
- Local PDF: pdf/2026-09-30_30_Residual-Stream Burden Shapes Representation Learning in Diffusion Transformers.pdf

In diffusion-based generation, a neural network can be trained to predict the clean data, the noise, or the velocity from a noisy input. These prediction targets are interconvertible and describe the same generative process, yet plain Diffusion Transformers operating on large pixel patches succeed with clean prediction and fail with noise or velocity prediction. We argue that this asymmetry arises because noisy targets require the residual stream to preserve noise-dependent input variation through depth for the final readout, forcing subsequent layers to compute on noisy representations. A spectrally concentrated clean target imposes a lighter demand, leaving greater freedom to organize hidden representations for subsequent computation. We call this preservation requirement *residual-stream burden* and show how it shapes representation learning in Diffusion Transformers. Controlled experiments indicate that the exploitable structure is spectral concentration in patch space and that the bandwidth of the persistent residual state is a key resource for noisy prediction. We further show that this account is consistent with recent decoupled pixel-space architectures, whose diverse designs all reduce the residual-stream burden on the main pathway. To examine this understanding from a complementary direction, we expand and reorganize the residual-stream bandwidth directly, introducing Spatially Indexed Hyper-Connections (SiHC) that reach FID 1.71 on ImageNet $256^2$. Together, these results identify residual-stream burden as a mechanism through which prediction targets and architecture jointly shape representation learning in Diffusion Transformers.
