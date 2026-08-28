# Paper Daily Reading - 2026-08-28

## 1. Learning Interpretable Tumor Microenvironment Representations by Fitting Pan-Cancer Cell State-Niche Correlation

- Authors: Xiao Xiao, Jiashu He, Shiyang Zhang, Meiyi Mao
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-26
- DOI: Unavailable
- Categories: q-bio.GN
- Relevance: 3.8456526926934886
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.26208v1
- PDF: https://arxiv.org/pdf/2608.26208v1
- Local PDF: pdf/2026-08-28_01_Learning Interpretable Tumor Microenvironment Representations by Fitting Pan-Cancer Cell State-Niche Correlation.pdf

In the tumor microenvironment, cell's state is influenced by cell-cell interactions (CCIs) with neighboring cells in its niches. Identifying dysregulated CCIs that are associated with pathogenic process pinpoints targets for drug discovery. Imaging-based spatial transcriptomics and single-cell RNA sequencing provide, respectively, single-cell spatial information and transcriptome-wide measurements needed to study CCIs, but neither modality provides both. Existing spatial transcriptomics foundation models also cannot effectively learn from spatially resolved single-cell data with full-transcriptome coverage, explicitly infer the CCI mechanisms driving cell state-niche associations, or interpretable enough to support direct biological interpretations. Here, we present GITIII-scale, a hierarchical, interpretable pan-cancer spatial transcriptomics foundation model for TME representation learning that investigates cell state-niche associations and their underlying ligand-receptor (LR) signaling pathways. GITIII-scale uses transformers to model interactions between pairs of cells at defined spatial distances, an interpretable single-layer graph transformer without a feed-forward network to decompose how each gene in a receiver cell is influenced by each neighboring sender cell, and a graph transformer to generate cellular-neighborhood embeddings. Trained on our assembled pan-cancer database of specimen-matched scRNA-seq and imaging-based spatial transcriptomics datasets, GITIII-scale generated TME embeddings that recovered niche-associated state changes more accurately than existing spatial transcriptomics foundation models in cancer types unseen during training. A case study of an unseen breast cancer dataset further demonstrated the model's interpretability by identifying potentially drug-targetable LR pathways associated with endothelial overgrowth and tumorigenesis.

## 2. GRAIN: Bridging Name and Narrative Shifts in Real-World Graph Reasoning through Invariance-Rewarded Agentic RL

- Authors: Zike Yuan, Han Zhang, Jianzhi Yan, Le Liu, Cai Ke, Huozhi Zhou, Jian Xie, Jiran Yin, Yukun Cao, Yue Yu, Hui Wang, Ming Liu, Bing Qin
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-27
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 3.636576040946018
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.27142v1
- PDF: https://arxiv.org/pdf/2608.27142v1
- Local PDF: pdf/2026-08-28_02_GRAIN_ Bridging Name and Narrative Shifts in Real-World Graph Reasoning through Invariance-Rewarded Agentic RL.pdf

Despite their potential in standardized graph tasks, Large Language Models (LLMs) remain brittle to real-world shifts in node identifiers and task formulation. While deterministic graph tools are invariant to such shifts, extracting topological structures from noisy text is highly fragile for LLMs, which often overfit to surface patterns. Moreover, mitigating these parsing failures via multi-agent systems incurs prohibitive latency. To address this, we propose GRAIN, a single-agent framework optimized via reinforcement learning. GRAIN models reasoning as a semantic parsing and tool-execution pipeline, guided by a Structure Invariance Reward. By validating extracted intermediate graphs against ground-truth topologies, this reward forces the LLM to learn robust text-to-structure mappings rather than memorizing linguistic artifacts. We also introduce GRIT, a benchmark evaluating sensitivity to such linguistic shifts. GRAIN outperforms multi-agent baselines by 16.45\% in accuracy with approximately 24\% lower latency. Furthermore, it demonstrates superior structural generalization, halving the out-of-distribution (OOD) gap of SFT models (from 15.77\% to 7.80\%) and maintaining robustness on large-scale graphs beyond the training distribution.

## 3. Decentralized Multitask Learning over Learned Task Graphs

- Authors: Zirui Wan, Stefan Vlaski
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-27
- DOI: Unavailable
- Categories: cs.LG, eess.SP, eess.SY
- Relevance: 3.520980258892259
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.26989v1
- PDF: https://arxiv.org/pdf/2608.26989v1
- Local PDF: pdf/2026-08-28_03_Decentralized Multitask Learning over Learned Task Graphs.pdf

This paper investigates decentralized multitask learning over networks when the underlying task relationships are unknown. While existing graph-regularized multitask frameworks typically assume a known structure, practical settings often require learning inter-task dependencies directly from distributed data. We propose a decentralized two-phase strategy that first estimates a generalized graph Laplacian from noisy non-cooperative stochastic gradient iterates, and subsequently exploits the learned graph to enable cooperative multitask diffusion learning. This framework is motivated by a Gaussian Markov random field prior, which gives rise to a decentralized maximum likelihood estimator for the graph Laplacian. The analysis quantifies the Laplacian estimation error and its propagation to the steady-state performance of the multitask diffusion recursion, and introduces a topology sensitivity index to capture the effect of network heterogeneity. Simulation results corroborate the theoretical findings and demonstrate that cooperation enabled by the learned task graph significantly improves performance over non-cooperative learning, while approaching the true-graph baseline when the estimation stepsize is sufficiently small.

## 4. Gromov-Monge Flow Matching for Equivariant Graph Generation

- Authors: Moritz Piening, Christian Wald
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-27
- DOI: Unavailable
- Categories: cs.LG, math.OC, stat.ML
- Relevance: 3.4821210942544063
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.26961v1
- PDF: https://arxiv.org/pdf/2608.26961v1
- Local PDF: pdf/2026-08-28_04_Gromov-Monge Flow Matching for Equivariant Graph Generation.pdf

Graphs are invariant under node permutations, motivating the use of permutation-equivariant architectures in generative models. In flow matching, however, symmetry may also enter the source--target coupling: once graph pairs are compared up to node relabeling, the natural Wasserstein geometry is that of the graph quotient space. The Euclidean quotient metric of this space coincides with the Gromov--Monge distance, obtained by optimally relabeling the nodes. We develop this perspective theoretically, showing that quotient couplings can be lifted to aligned representatives without additional cost and that symmetrization yields equivariant flow-matching minimizers, including for categorical endpoint prediction. In practice, exact Gromov--Monge alignment is intractable, so we construct minibatch couplings using efficient Gromov--Wasserstein-type relaxations and lower bounds for the inner node alignment, optionally combined with an outer assignment between graphs. The resulting procedure changes only the training coupling and is compatible with standard permutation-equivariant architectures. Across continuous graph and categorical molecular generation, these structure-aware couplings substantially improve sample quality at small integration budgets, while our scaled-up molecular models remain competitive under conventional many-step sampling.

## 5. GraphMemix: Query-Aware Evidence Forests for Long-Term Multimodal Agent Memory

- Authors: Geng Li, Yuhao Wang, Dong Li, Jianye Hao, Yuxin Peng
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-27
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 3.442335354234041
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.26983v1
- PDF: https://arxiv.org/pdf/2608.26983v1
- Local PDF: pdf/2026-08-28_05_GraphMemix_ Query-Aware Evidence Forests for Long-Term Multimodal Agent Memory.pdf

Organizing long-term memory for multimodal agents remains challenging because existing methods either suffer from expensive question-agnostic offline summaries or naive embedding similarity matching that introduces incomplete and redundant context. To address these issues, we propose GraphMemix, a combinatorial-optimization graph memory framework that models memory organization as query-aware evidence-forest construction. Specifically, our method consists of three key components:(1) candidate graph construction, which expands multi-view seed memories through schema and semantic relations to acquire query-aware original context; (2) evidence utility and activation costs, which decouples direct memory support from anchor-conditioned relation verification to suppress redundant or conflicting information; and (3) forest optimization, which jointly selects a forest-format memory context under a maximum evidence budget and its reliable relational structure. By organizing memory into a query-relevant subgraph, the method avoids substantial lifecycle cost and recovers low-similarity complementary evidence. Experimental results across four long-term multimodal memory benchmarks demonstrate significant improvements with different foundation models and establish a new Pareto frontier between accuracy and lifecycle cost.

## 6. Neural Regression with Embeddings for Numerical Attribute Prediction in Knowledge Graphs

- Authors: Rupesh Sapkota, Louis Mozart Kamdem Teyou, Moshood Yekini, Caglar Demir, Axel-Cyrille Ngonga Ngomo
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-27
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.3836699062542497
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.26729v1
- PDF: https://arxiv.org/pdf/2608.26729v1
- Local PDF: pdf/2026-08-28_06_Neural Regression with Embeddings for Numerical Attribute Prediction in Knowledge Graphs.pdf

In recent years, transductive knowledge graph embedding models have been applied to tasks such as link prediction and query answering. Although knowledge graphs often contain rich numerical attributes, most embedding models neglect them, limiting their ability to represent real-world knowledge graphs with diverse information. In this work, we propose a neural regression model (LitEm) that enables transductive knowledge graph embedding models to predict numerical attributes within knowledge graphs. Experimental results demonstrate that LitEm achieves the best or second-best results on most attributes across FB15K-237, YAGO15K, DB15K, and Mutagenesis. Furthermore, we propose a co-training framework that jointly trains state-of-the-art transductive knowledge graph embedding models with LitEm, which improves link prediction performance mainly for bilinear models and simultaneously enables them to predict numerical attributes. In addition, the literal-awareness evaluation demonstrates that co-training helps models to encode and exploit attribute information in a "literal-aware'' manner, suggesting that the observed gains are not merely due to additional parameters. We publicly release our implementation at https://github.com/dice-group/dice-embeddings.

## 7. A knowledge-driven framework for predicting single-cell responses for unprofiled drugs

- Authors: Jinghao Feng, Ziheng Zhao, Xiaoman Zhang, Mingfei Liu, Jingyi Chen, Xingran Quan, Boyang Fu, Jian Zhang, Yanfeng Wang, Ya Zhang, Weidi Xie
- Source: openalex
- Venue type: journal
- Journal: Nature Machine Intelligence
- Publication status: published
- Publication date: 2026-08-26
- DOI: https://doi.org/10.1038/s42256-026-01286-w
- Categories: Cell Image Analysis Techniques, Computational Drug Discovery Methods, Bioinformatics and Genomic Networks
- Relevance: 3.3101773348740657
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://doi.org/10.1038/s42256-026-01286-w
- PDF: Unavailable
- Local PDF: Not downloaded

Predicting cellular response to chemical perturbations is critical to build virtual cells, yet experimentally profiled compounds cover only a small fraction of this space. Existing models struggle to generalize to unprofiled compounds, as they typically treat drugs as isolated identifiers without encoding their mechanistic relationships. Here, we present MAP, a framework that integrates structured biological knowledge into cellular perturbation modelling and supports zero-shot prediction for small molecules with scarce or absent profiles. (1) We construct MAP-KG, a knowledge graph that unifies 14 public resources, spanning 187,089 drugs, 22,924 genes and 694,246 mechanistic relationships. (2) We propose a knowledge-driven pretraining strategy that aligns molecular structures, protein sequences and textual mechanistic descriptions into a unified embedding space, producing mechanism-aware and transferable gene and compound embeddings. These representations are then coupled with a pretrained single-cell foundation model to condition perturbation response prediction. (3) We evaluate MAP under two zero-shot generalization regimes: unseen cell type–drug combinations and a stricter setting of unprofiled drugs, where it improves the top-50 differentially expressed gene Pearson delta correlation by up to +12.3% and +11.8%, respectively, over the strongest baselines across three benchmarks. We further perform pathway-level functional analysis via gene set enrichment analysis for in silico screening, where MAP predicts mechanism-consistent programmes on unprofiled candidate drugs, and prioritizes four out of five approved anti-cancer drugs in A-549 (non-small-cell lung cancer). Feng et al. introduce MAP, an artificial intelligence framework that integrates biological mechanism knowledge to predict how cells respond to chemical perturbation, improving generalization to untested drugs and prioritizing cancer drug candidates in virtual screening.

## 8. Chart2SVG: Editable SVG Generation from Raster Chart Images

- Authors: Jinning Cui, Lu Chen, Haoyan Shi, Yue He, Chenglong Wang, Mengyu Zhou, Weidong Huang, Yunhai Wang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-27
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.2532180537806674
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.26544v1
- PDF: https://arxiv.org/pdf/2608.26544v1
- Local PDF: pdf/2026-08-28_08_Chart2SVG_ Editable SVG Generation from Raster Chart Images.pdf

We present Chart2SVG, a multimodal large language model that converts static raster charts into structurally organized, semantically enriched SVGs that support programmatic editing. By incorporating chart-specific semantic tokens into a vision-language model, Chart2SVG captures both geometric primitives and their functional roles. To support robust structural recovery, we introduce Beagle+, a dataset of 33K canonicalized and structurally distilled chart samples. Our approach combines specialized training objectives with a rendering-aware post-training phase, producing SVGs that are both visually accurate and structurally consistent. To facilitate higher-level manipulations, we construct a Chart Structure Graph (CSG) that exposes visual dependencies, enabling tasks such as interactive exploration, chart repurposing, and layout reuse. Experiments show that Chart2SVG substantially outperforms baselines in reconstruction fidelity and downstream editing utility, advancing the development of intelligent and interactive visualization tools.

## 9. Syntax vs. Semantics: How Transformers Learn Deep Dependencies

- Authors: Jiangrui Zhao, Xiaoting Du
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-06-26
- DOI: Unavailable
- Categories: cs.CL, cs.AI
- Relevance: 3.2325931511083206
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.26139v1
- PDF: https://arxiv.org/pdf/2608.26139v1
- Local PDF: pdf/2026-08-28_09_Syntax vs. Semantics_ How Transformers Learn Deep Dependencies.pdf

Large Language Models demonstrate remarkable syntactic fluency, yet the optimization dynamics governing their acquisition of deep semantic dependencies remain poorly understood. We propose a mechanistic framework that models this learning process as a competition between Surface Statistics and Deep Semantics. Our theoretical analysis identifies a ``Gradient Starvation" phenomenon where the error signals for sparse semantic dependencies are actively suppressed during early optimization. This suppression impedes the learning of structural reasoning and causes its emergence to manifest as a sudden phase transition. Furthermore, this framework offers a mechanistic basis for the effectiveness of Chain-of-Thought (CoT) strategies. By externalizing intermediate reasoning steps into concrete tokens, CoT effectively bypasses the suppression regime inherent to implicit reasoning. We validate these findings across scales ranging from toy transformers to production models (Llama-3.1-8B, Qwen2.5-Coder-7B). Finally, guided by this theory, we propose a topology-aligned contrastive objective that explicitly rectifies the gradient geometry. Experiments on variable binding tasks demonstrate that our method achieves an improvement that is over 2x larger than that obtained via standard cross-entropy fine-tuning.

## 10. C-Unseen: Weak Signal Detection in Dynamic Temporal Knowledge Graphs via LLM Reasoning

- Authors: Yassir Lairgi, Ludovic Moncla, Khalid Benabdeslem, Rémy Cazabet, Pierre Cléau
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-27
- DOI: Unavailable
- Categories: cs.AI, cs.CL, cs.SI
- Relevance: 3.151130229346728
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.26870v1
- PDF: https://arxiv.org/pdf/2608.26870v1
- Local PDF: pdf/2026-08-28_10_C-Unseen_ Weak Signal Detection in Dynamic Temporal Knowledge Graphs via LLM Reasoning.pdf

Weak signals are early, low-visibility indicators that precede significant changes before those changes become established. Existing detection methods, based on keyword frequency, topic modeling, or untyped graph topology, fail to capture the semantic and relational structure through which such signals manifest. In this paper, we propose C-Unseen, a self-interpretable framework for weak signal detection in Dynamic Temporal Knowledge Graphs (DTKGs). We define a weak signal as a rare, semantically coherent subgraph that proliferates across consecutive TKG snapshots. The framework operates through two modules: a Rare Subgraphs Extractor, in which an LLM identifies subgraphs whose content is in tension with the dominant snapshot narrative via chain-of-thought reasoning, and a Weak Signal Alerter, in which the persistence of these rare subgraphs is tracked across time steps to isolate true weak signals. Experimental results demonstrate that C-Unseen outperforms keyword-, topic-, and graph-based baselines.

## 11. GRAS: Guided Reduced-Variance Proposals and Adaptive Selection for Training-Free Reward Alignment in Discrete Diffusion

- Authors: Kwanyoung Kim
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-27
- DOI: Unavailable
- Categories: cs.LG, cs.CE, q-bio.QM, stat.ML
- Relevance: 3.0832016087622094
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.26585v1
- PDF: https://arxiv.org/pdf/2608.26585v1
- Local PDF: pdf/2026-08-28_11_GRAS_ Guided Reduced-Variance Proposals and Adaptive Selection for Training-Free Reward Alignment in Discrete Diffusion.pdf

Discrete diffusion models have become a strong, widely adopted class of generators for sequence data, and steering them toward a downstream reward at inference time, without any retraining, is increasingly important. Such training-free steering is done by gradient guidance, by search, or by combining the two. We study the combined regime and identify two weaknesses in how it is usually run: the guided proposal estimates its gradient from a single noisy sample, and the search then resamples particles at a fixed temperature that ignores how rewards spread across each denoising step. We address both with a small set of changes that add no denoiser cost. For the proposal, we lower the estimator variance with a Rao-Blackwellized reveal for differentiable rewards and a leave-one-out baseline for non-differentiable ones; for the search, we standardize the per-step values into a group-relative advantage and prove it collapses to a single active ingredient, an adaptive resampling temperature. We call the resulting method Guided Reduced-variance proposals and Adaptive Selection (GRAS). GRAS is simple yet effective: across regulatory DNA and protein design it attains the best training-free reward, outperforming prior training-free methods and matching or surpassing a reward-fine-tuned model, and it remains effective even for non-differentiable rewards.

## 12. Unifying Detection and Adaptation in Task-Free Continual Learning

- Authors: Dezheng Han, Anbang Zhang, Zhihao Zhu, Shuaishuai Guo
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-27
- DOI: Unavailable
- Categories: cs.LG, cs.CL
- Relevance: 3.0463157357146606
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.27070v1
- PDF: https://arxiv.org/pdf/2608.27070v1
- Local PDF: pdf/2026-08-28_12_Unifying Detection and Adaptation in Task-Free Continual Learning.pdf

To mitigate catastrophic forgetting in downstream continual learning (CL) for large language models (LLMs), existing methods typically constrain parameter updates or introduce task-specific adaptation modules. However, these methods often rely on explicit task boundaries during training, limiting their applicability to realistic task-free scenarios. In this paper, we propose a \textbf{Fi}sher-guided \textbf{uni}fied (\textbf{FiUni}) framework for batch-level task detection and parameter-efficient continual adaptation. FiUni is motivated by a key observation about the Fisher information matrix (FIM) of pre-trained models: the orthogonality among the principal subspaces of its Kronecker-Factored Approximate Curvature (K-FAC) approximation, estimated from a small number of downstream task samples, can reflect the similarity between different tasks. Based on this observation, FiUni constructs FIM-derived frozen subspaces to guide low-rank adaptation (LoRA), while matching the Fisher principal subspace of each incoming batch window with historical subspaces. This enables FiUni to adaptively determine whether to reuse existing knowledge, expand a related subspace, or create a new subspace, dynamically balancing knowledge sharing and task isolation. Experiments show that FiUni can effectively infer latent batch-level task affiliations and achieve competitive performance against advanced task-aware CL methods with fewer trainable parameters.

## 13. SymbolLKG: Towards Verifiable Logical Reasoning via Logical Knowledge Graph and Symbolic Solvers

- Authors: Haizhao Fan, Yuchi Xiong, Jize Wang, Xinping Guan, Xinyi Le
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-27
- DOI: Unavailable
- Categories: cs.AI, cs.CL
- Relevance: 3.024067415986008
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.26836v1
- PDF: https://arxiv.org/pdf/2608.26836v1
- Local PDF: pdf/2026-08-28_13_SymbolLKG_ Towards Verifiable Logical Reasoning via Logical Knowledge Graph and Symbolic Solvers.pdf

Large Language Models (LLMs) have demonstrated remarkable proficiency in natural language understanding, yet they struggle with strict multi-step reasoning, frequently suffering from hallucinations and inconsistency. Existing solutions like Chain-of-Thought (CoT) lack rigorous verification mechanisms, while standard Retrieval-Augmented Generation (RAG) often misses the complex, structural dependencies inherent in logical tasks. To bridge this gap, we propose a Neuro-Symbolic architecture that integrates a Logical Knowledge Graph (LKG) with dynamic solver routing. Specifically, we introduce an ontology-based LKG that treats logical rules and constraints as first-class topological nodes, enabling explicit modeling of dependencies extracted from text. We further design a Logic Router to dynamically dispatch tasks to the optimal symbolic engine, which is supported by a topology-aware hybrid retrieval mechanism. Experimental results on logical reasoning benchmarks demonstrate that our framework significantly outperforms state-of-the-art prompting and RAG baselines, delivering higher accuracy and verifiable reasoning paths.

## 14. pro-team at LLMs4OL 2026 Tasks Flagship and Reuse: Retrieval-Augmented Generation and Vocabulary-Constrained Filtering for Ontology Learning

- Authors: Shivam Mishra, Dhannu Ram Meena, Muneendra Ojha, Krishna Pratap Singh, Kuldeep Singh
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-27
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 2.985740365024565
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.27101v1
- PDF: https://arxiv.org/pdf/2608.27101v1
- Local PDF: pdf/2026-08-28_14_pro-team at LLMs4OL 2026 Tasks Flagship and Reuse_ Retrieval-Augmented Generation and Vocabulary-Constrained Filtering f.pdf

Ontology learning from text remains challenging despite significant progress in Large Language Models (LLMs), which can hallucinate domain terms, produce inconsistent formats, and favor hierarchical over associative relations. In the LLMs4OL 2026 Challenge, we address both the End-to-End Flagship Task (Task A) and Ontology Extension Reuse Task (Task B) using an offline retrieval-augmented few-shot prompting pipeline. Our system employs Qwen2.5-14B-Instruct with all-MiniLM-L6-v2 for demonstration retrieval, selecting the top-5 examples for Task A and top-2 for Task B. A left-truncated context-windowing strategy preserves task instructions within long prompts. For Task B, generated triples undergo deterministic vocabulary-constrained filtering, retaining triples when at least one endpoint belongs to the sample's closed term/type vocabulary and removing duplicates of the initial ontology. The approach achieves Semantic Graph Similarity of 0.8692, Term-Typing F1 of 0.9200, and Taxonomy Discovery F1 of 0.8540 on Task B, while Task A achieves 0.7416 Semantic Graph Similarity. However, no non-taxonomic relations are extracted, highlighting limitations of closed, taxonomy-oriented relation vocabularies.

## 15. From Reasoning to Pixels: Grounded Medical Multimodal LLMs for VQA and Segmentation

- Authors: Haowen Gu, Gensheng Pei, Junzhu Mao, Qiong Wang, Mingwu Ren, Yazhou Yao
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-27
- DOI: Unavailable
- Categories: cs.CV, cs.AI
- Relevance: 2.968477466801856
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.26856v1
- PDF: https://arxiv.org/pdf/2608.26856v1
- Local PDF: pdf/2026-08-28_15_From Reasoning to Pixels_ Grounded Medical Multimodal LLMs for VQA and Segmentation.pdf

Although Multimodal Large Language Models (MLLMs) have demonstrated impressive performance in Medical Visual Question Answering (Med-VQA), their reliance on global image features often lacks precise pixel-level grounding, thereby limiting clinical trustworthiness. To bridge the semantic gap between high-level clinical reasoning and spatial localization, we propose \textsc{\textsc{MedREAL}} (\textbf{Med}ical \textbf{RE}asoning-driven \textbf{A}nswering and \textbf{L}ocalization), a unified framework that seamlessly aligns linguistic reasoning with spatial grounding. Specifically, \textsc{MedREAL} introduces \textbf{S}eg \textbf{A}nchored \textbf{R}easoning \textbf{P}ooling (SARP) to distill task-relevant semantic evidence directly from \texttt{[SEG]} tokens within the MLLM's hidden states. Furthermore, a \textbf{R}easoning-to-\textbf{V}isual (R2V) fusion mechanism is proposed to effectively inject these reasoning-aware features into a segmentation pipeline for accurate mask decoding. To facilitate this paradigm, we construct MedRAVS-13K, a comprehensive dataset comprising 13,824 expertly validated samples across four diverse imaging modalities. Extensive experiments demonstrate that \textsc{MedREAL} significantly outperforms state-of-the-arts, achieving 68.49\% gIoU and 70.47\% cIoU on benchmark evaluations. By generating evidence masks that are strictly consistent with textual diagnoses, \textsc{MedREAL} provides a robust, interpretable framework for reasoning-driven medical image analysis.

## 16. Hierarchical Channel Stacking: A Structured Decision Framework for AI-Generated Image Detection

- Authors: Saifullah Shoaib, Akash Borigi, Rupendra Lekkala, Amaury Lendasse, Edward Ratner, Sai Sowjanya Bhamidipati, Alexander Schlager, Peggy Lindner
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-27
- DOI: Unavailable
- Categories: cs.CV, cs.LG
- Relevance: 2.958330339649918
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.26648v1
- PDF: https://arxiv.org/pdf/2608.26648v1
- Local PDF: pdf/2026-08-28_16_Hierarchical Channel Stacking_ A Structured Decision Framework for AI-Generated Image Detection.pdf

Many synthetic-image detectors produce accurate predictions but offer limited insight into how those decisions are formed. This paper introduces Hierarchical Channel Stacking (HCS), a compact framework for AI-generated image detection that converts intermediate CNN activations into a structured 60-dimensional representation organized across three progressively deeper backbone stages. HCS uses per-channel Level-1 classifiers and a Level-2 aggregator to produce image-level predictions while preserving explicit hierarchical structure for analysis. On a benchmark spanning GAN and diffusion generators, HCS achieves 86.7% accuracy and 86.7% macro-F1 on the held-out test set. Stage ablation shows that the full three-stage system outperforms reduced single-stage and two-stage variants, indicating that the hierarchy carries complementary predictive information. Stage-level contribution analysis further shows that, in the analyzed detector setting, fake GAN and fake diffusion images exhibit distinct stage-level contribution profiles. These results position HCS not simply as a compact detector, but as a structured framework for studying how synthetic-image detectors assemble evidence across representation levels.

## 17. Performance Foundations of Parallel & Distributed Reasoning Language Models

- Authors: Maciej Besta, Leonard Schmidt, Lara Nonino, Robert Gerstenberger, Pierre Pang, Patrik Okanovic, Ales Kubicek, Tiancheng Chen, Baraq Lipshitz, Torsten Hoefler
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-27
- DOI: Unavailable
- Categories: cs.LG, cs.AI, cs.DC, cs.PF
- Relevance: 2.935440339143895
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.27046v1
- PDF: https://arxiv.org/pdf/2608.27046v1
- Local PDF: pdf/2026-08-28_17_Performance Foundations of Parallel & Distributed Reasoning Language Models.pdf

Reinforcement Learning with Verifiable Rewards (RLVR) and other RL-style post-training paradigms have been used for aligning large language models (LLMs) with reasoning standards. The resulting recent Reasoning Language Models (RLMs) such as DeepSeek-R1, o3, and Kimi k1.5 show that such RL-style post-training ("RL-for-LLMs") can substantially improve chain-of-thought reasoning, long-horizon planning, and self-correction. However, the computational footprint of these systems is massive: state-of-the-art RLM training requires millions of GPU-hours and tightly coupled multi-model pipelines that stress modern hardware far beyond classical supervised LLM training. This makes RLM training as much a parallel and distributed systems problem as an algorithmic one. In this work, to facilitate developing RLMs that are simultaneously high-performance, scalable, and cost-effective, we first systematize the RL-for-LLM paradigm and provide a compute-centric analysis of prominent post-training algorithmic frameworks: Proximal Policy Optimization (PPO), Group Relative Policy Optimization (GRPO), as well as their variants. Second, we develop a taxonomy of intra- and inter-model parallelism strategies for RL-for-LLMs, covering both traditional techniques (data, tensor, pipeline, sequence, context, and expert parallelism) as well as novel forms of parallelism and optimization techniques for multi-model RLM training, for example disaggregated placement, stage fusion, hybrid parallelism, and asynchronous execution. We harness the work-depth model of parallel computing to make our taxonomy and its insights rigorous and portable. Finally, we analyze existing RLM frameworks and we distill practical guidelines and outline open research directions for building scalable, fast, and cost-effective RLMs.

## 18. Position Is All You Need: A Free Lunch Token Compression Strategy for MLLM-based Referring Expression Segmentation

- Authors: Yuhan Liu, Yixiong Zou, Yuhua Li, Ruixuan Li
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-06-26
- DOI: Unavailable
- Categories: cs.CL, cs.AI
- Relevance: 2.9278692598628813
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.26142v1
- PDF: https://arxiv.org/pdf/2608.26142v1
- Local PDF: pdf/2026-08-28_18_Position Is All You Need_ A Free Lunch Token Compression Strategy for MLLM-based Referring Expression Segmentation.pdf

Referring Expression Segmentation (RES) aims to generate pixel-wise segmentation masks from complex and implicit textual queries. While recent advances in Multimodal Large Language Models (MLLMs) have substantially boosted RES performance, their prohibitive computational overhead remains a critical bottleneck, which, however, is rarely explored. To fill this gap, we first evaluate typical token compression methods on this task and observe a surprising performance degradation. In this paper, we aim to understand this phenomenon for a solution. By extensive experiments, we find that token compression for RES requires preserving the original position embeddings and local neighboring spatial structures, indicating that visual token position information is far more critical than in other tasks. Building on this insight, we ask: Can we design the token compression method purely based on the position information? Therefore, we propose PAYN, a plug-and-play, training-free token compression method that relies solely on position information. PAYN retains tokens that are adequately distributed in every local neighboring region while strictly preserving original positional indices, thereby maintaining spatial relational consistency. Experiments on multiple RES benchmarks demonstrate that our method outperforms existing token compression methods, verifying that position is indeed all you need for token compression in the MLLM-based RES task. Codes are avaliable at https://github.com/YuhanLiu231/PAYN.

## 19. Omni-Interactive Universal Embedder

- Authors: Wei-Yao Wang, Kazuya Tateishi, Shuyang Cui, Christian Simon, Takashi Shibuya, Shusuke Takahashi, Yuki Mitsufuji
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-27
- DOI: Unavailable
- Categories: cs.AI, cs.CV
- Relevance: 2.923838108734728
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.27044v1
- PDF: https://arxiv.org/pdf/2608.27044v1
- Local PDF: pdf/2026-08-28_19_Omni-Interactive Universal Embedder.pdf

Multimodal representation learning has been shifting from traditional two-tower architectures to large language model (LLM)-based embedders due to their strong instruction-following capabilities. Despite this progress, existing approaches primarily focus on language and image modalities, which also remain the dominant modalities for user-conditioned interactions in current embedders. In this paper, we propose the first Omni-Interactive Universal Embedder (OmniUE), which not only learns a unified embedding space across text, video, and audio by leveraging intermediate-layer representations from dedicated learnable tokens, but also supports omni-interactive querying, enabling users to provide inputs in the form of text, visual regions of interest, and audio spans. Within OmniUE, visual and audio segmenters process diverse user interactions and integrate them with an omni-LLM to produce user-conditioned any-to-any embeddings via context aggregation. To evaluate OmniUE's omni-interactive capabilities, we introduce OmniCHOIR, benchmarking models for omni-interactive compositional audio retrieval based on the given text, video, and audio as well as unimodal or multimodal interaction prompts. OmniUE consistently surpasses state-of-the-art baselines across diverse modalities, with average improvements of 10.5% on textual-interactive video benchmarks (MMEB-v2-video), 1.1% on audio tasks (MAEB), 83.7% on visual-interactive benchmarks (SCaR), and 24.1% on our omni-interactive OmniCHOIR benchmark. We believe that jointly advancing omni-modal representation learning and omni-interactive querying paves the way toward universal embedders.

## 20. Affix Cache for Diffusion Large Language Models

- Authors: Kaihua Liang, An Zhong, Xin Tan, Zafar Ayyub Qazi, Hong Xu, Jian Weng, Marco Canini
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-06-26
- DOI: Unavailable
- Categories: cs.CL, cs.LG
- Relevance: 2.9028637911774293
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.26140v1
- PDF: https://arxiv.org/pdf/2608.26140v1
- Local PDF: pdf/2026-08-28_20_Affix Cache for Diffusion Large Language Models.pdf

Diffusion Large Language Models (DLLMs) enable non-autoregressive decoding and bidirectional context modeling, but efficient inference remains challenging. Unlike autoregressive systems, whose key-value (KV) cache can be reused for shared prefixes, DLLMs couple the KV states of shared context tokens with evolving generated tokens through bidirectional attention, making naive cache reuse stale while full recomputation is expensive. We present ACache, an affix-oriented cache reuse mechanism for shared text spans in DLLMs beyond prefixes. ACache identifies a small request-specific subset of critical affix tokens, called Anchor Tokens, by measuring their influence on masked generation tokens, and selectively recomputes the KV states of only these tokens while reusing the remaining affix cache. Built on Fast-dLLM, ACache recovers the accuracy loss caused by direct affix-cache reuse across different settings when recomputing around 20% of affix tokens. We also build a shared-prefix prototype on top of the Nano-vLLM engine, showing that ACache reduces recompute latency by up to 55.7% and improves end-to-end throughput by up to 1.68$\times$.

## 21. What Makes Good Agentic Data? An ACE Lens on Data Generation for LLM Agents

- Authors: Xingshan Zeng, Zishan Xu, Boju Zhang, Yuzhou Wu, Lingzhi Wang, Jianghao Lin, Liangyou Li, Yasheng Wang, Lifeng Shang, Xin Jiang, Weinan Zhang, Yong Yu, Qun Liu, Weiwen Liu
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-27
- DOI: Unavailable
- Categories: cs.AI, cs.CL
- Relevance: 2.9026369977375923
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.27260v1
- PDF: https://arxiv.org/pdf/2608.27260v1
- Local PDF: pdf/2026-08-28_21_What Makes Good Agentic Data_ An ACE Lens on Data Generation for LLM Agents.pdf

LLM agents increasingly rely on generated interaction data to learn how to interact with external environments. Agentic data generation must maintain consistency among environments, tasks, interactions, and success signals while producing experience that is useful rather than merely abundant. Existing work spans many agent domains, but domain-centered organization and heterogeneous evaluation often obscure common generation mechanisms and conflate candidate construction with verification and selection. This work develops a two-level framework for the field. First, we represent agentic data as a common factorized object $(E,q,τ,v)$, comprising an environment specification, task signal, interaction realization, and optional verifier. We organize generation paradigms by their primary anchor and dependency structure. Second, we formulate generation as constrained distribution design through the Accuracy-Complexity-divErsity (ACE) lens. Accuracy establishes the feasible support of grounded and internally consistent data. Within this support, Complexity places learning mass relative to the capability of a declared learner and execution configuration, while divErsity controls coverage and redundancy of data. Using this framework, we explore how prior work verifies generated experience, constructs and calibrates difficulty, and expands behavioral coverage. The literature reveals a shift toward execution-grounded accuracy, learner-relative complexity, and diversity beyond surface variation or dataset size. We further discuss broader directions and emerging trends in agentic data generation through the ACE lens, including their implications for scaling, data sources, training regimes and adaptive learning. Overall, the central challenge is not simply to generate more data, but to continually allocate valid, informative, and non-redundant experience as agents and environments evolve.

## 22. AgentFold: Closed-Loop Agentic Search for Protein Folding Model Design

- Authors: Mingquan Liu, Jiangyu Chen, Hanqun Cao, Xujun Zhang, Pengsen Ma, Xiangru Tang, Shuting Jin, Zhuo Yang, Tianfan Fu, Fang Wu, Xiangxiang Zeng
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-27
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 2.9020258458422896
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.26747v1
- PDF: https://arxiv.org/pdf/2608.26747v1
- Local PDF: pdf/2026-08-28_22_AgentFold_ Closed-Loop Agentic Search for Protein Folding Model Design.pdf

Scientific LLM agents have shown promise in literature reasoning, tool use, and experiment planning, but it remains unclear whether they can autonomously improve large, tightly coupled scientific machine-learning systems through executable code changes and computationally expensive validation. We study this question in protein folding, where progress requires coordinated architectural modifications, multi-objective evaluation, and domain-aware interpretation. We present AgentFold, a multi-agent framework that formulates folding-model development as a closed-loop search over executable code variants. Starting from ESMFold, AgentFold proposes hypotheses, implements and debugs code-level modifications, evaluates model variants, analyzes experimental outcomes, and stores both successful and failed interventions in structured memory. An MCTS-style policy allocates computational resources across high-scoring search branches. On an engineering-scale protein-folding codebase comprising more than 2,000 lines of code, AgentFold explores approximately 80 model variants using approximately 5,000 GPU-hours and 170 million LLM tokens. Under a matched computational budget, AgentFold improves the best lDDT by 7.5% over independent Codex proposals and outperforms a random-search control. Beyond model improvement, the resulting intervention traces reveal recurring empirical design patterns: stable gains tend to arise from early, soft, learnable priors and gated refinement, whereas direct geometric perturbations and geometry-conditioned feedback often destabilize training. The code and experimental resources are publicly available at https://github.com/lmqfly/AgentFold.

## 23. How Language Models Organize and Structure Moral Knowledge

- Authors: Orion Reblitz-Richardson
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-27
- DOI: Unavailable
- Categories: cs.CL, cs.AI, cs.LG
- Relevance: 2.8768505498028074
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.27402v1
- PDF: https://arxiv.org/pdf/2608.27402v1
- Local PDF: pdf/2026-08-28_23_How Language Models Organize and Structure Moral Knowledge.pdf

How do large language models (LLMs) organize moral knowledge? Models detect moral content broadly, but detection is a low bar. We ask whether they go further, distinguishing moral foundations from one another and organizing the relationships between them geometrically.
  We train six independent linear probes on open-weight language models, one per Moral Foundations Theory (MFT) category (care/harm, fair/cheat, lib/oppress, loy/betray, auth/subv, sanc/degrade), and examine how the resulting directions relate to each other in representation space. We find the directions neither collapse into a single moral detector nor isolate from one another. Rather, they span a near-maximal number of independent dimensions while sharing a positive common component. The shared component is the signature of integration, and it is moral-specific relative to a matched non-moral concept battery built identically (mean pairwise cosine 0.26 vs. 0.013).
  The geometry is consistent across architectures and scale and reaches its integration regime early in pre-training, well before probe accuracy saturates. The structure the model discovers shows no evidence of the individualizing/binding distinction predicted by Moral Foundations Theory (an underpowered test: only 20 candidate partitions exist) but rather reflects corpus statistics. Extending to moral dilemmas, each dilemma direction partially composes from its component foundations, at 2.7x a mismatched-pair baseline, while the majority of its variance encodes conflict-specific structure. The model represents moral tension itself, not a pre-resolved judgment.

## 24. Towards a universal meta-optics solver via large language models

- Authors: Huanshu Zhang, Lei Kang, Yuyan Chen, Luxiang Wang, Zhaolong Cao, Douglas H. Werner
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-26
- DOI: Unavailable
- Categories: physics.optics, cs.LG
- Relevance: 2.8220191067473954
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.26417v1
- PDF: https://arxiv.org/pdf/2608.26417v1
- Local PDF: pdf/2026-08-28_24_Towards a universal meta-optics solver via large language models.pdf

Metasurface design increasingly requires fast models that can operate across structurally distinct device families, rather than retraining a separate surrogate for every geometry class. Conventional neural network surrogates often depend on fixed-dimensional descriptors, family-specific output formats, and repeated architecture tuning, which limits their scalability across heterogeneous meta-atoms. Here, we present a unified large language model (LLM) workflow for multi-family metasurface modeling and inverse-design. Geometries, design parameters, and optical response channels were converted into a shared instruction-following text format and used to fine-tune Gemma-2-9B across 8 metasurface families. Compared with single-family baselines, the joint model simultaneously predicted the optical responses of all metasurface families while reducing the MSE for each family by an average of 56.5%. The same representation was also used for inverse design. These results show that a shared sequence-based LLM interface can provide a practical route to cross-family metasurface design while reducing the need for task-specific surrogate architectures.

## 25. Discovering Relationships in Data Lakes Using Large Language Models: An Industrial Case

- Authors: Ahlame Diouan, Eric Ferey, Sabine Loudcher, Jérôme Darmont
- Source: arxiv
- Venue type: preprint
- Journal: 28th International Conference on Big Data Analytics and Knowledge Discovery (DaWaK 2026), Aug 2026, Graz, Austria. pp.116-130
- Publication status: preprint
- Publication date: 2026-08-27
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 2.7918330117848367
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.26750v1
- PDF: https://arxiv.org/pdf/2608.26750v1
- Local PDF: pdf/2026-08-28_25_Discovering Relationships in Data Lakes Using Large Language Models_ An Industrial Case.pdf

Data lakes rely on metadata to remain usable, yet this meta data is often limited or weakly informative for column relationship discovery, especially in ERP-derived datasets with coded or abbreviated schema labels. We propose ColRel, a two-stage method that builds column embeddings from metadata and data available at ingestion time. In difficult cases, such as coded schemata, business dictionaries help better interpret column names and support the generation of short natural-language descriptions used in the second stage. Experiments on public benchmarks and an industrial ERP dataset show that ColRel is particularly effective in semantically related, weak-signal settings.

## 26. From SQL to Knowledge Graphs: An LLM-Driven Multi-Agent Approach with Data Schema Improvement

- Authors: Dinh-Khanh Pham, Quy-Anh Dang, Lam Mai Thanh, Khanh Bui, Truong-Son Hy
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-06-17
- DOI: Unavailable
- Categories: cs.DB, cs.AI
- Relevance: 2.7848785708734507
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.26117v1
- PDF: https://arxiv.org/pdf/2608.26117v1
- Local PDF: pdf/2026-08-28_26_From SQL to Knowledge Graphs_ An LLM-Driven Multi-Agent Approach with Data Schema Improvement.pdf

RDBMS (Relational Database Management System) databases face several limitations, including slow execution with multi-hop queries and a lack of explainability by graphical interpretations. In contrast, Graph database offers a more intuitive and efficient data schema that performs faster execution on large datasets. Most existing RDBMS conversion pipelines focus on running traditional loading commands and relying on Cypher queries. However, the efficiency of using an LLM to generate an effective graph data schema, significantly reducing the ambiguity of the graph database, remains underexplored in the current research literature. This paper presents a novel algorithm that bridges RDBMS and graph database by using a novel LLM-powered ETL agent to standardize table and column names before saving them to the Data Mart. A Multi-Agent System generates a looping discussion between ETL, Analyzer, and Graph agents to optimize the final design through an iterative process of suggesting and scoring the graph database schema. We ensure that the final graph database meets three criteria before being accepted for data conversion: Accuracy, Groundedness, and Faithfulness. This system demonstrates an effective pipeline to automatically convert a tabular database into a graph database through a comprehensive end-to-end process. Our study highlights notable efficiency in using the converted graph database, which is measured on 1,081 samples of the BFSI dataset across three levels of complexity (easy, medium, and hard). Specifically, CypherAgent achieves an 85.6% accuracy for Q&A tasks using a Graph database, which is 12.12% higher than the accuracy achieved by an SQLAgent on the RDBMS database type PostgreSQL, for all queries. Additionally, the Graph database demonstrates faster performance, reducing latency by approximately 3 times.

## 27. TamEdit: Trajectory-Aware Meta-Learning for Specificity-Preserving Continual Knowledge Editing

- Authors: Shiqiang Tian, Cheng Ding, Qin Chen, Jie Zhou, Liang He
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.761385840267585
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.979/
- PDF: https://aclanthology.org/2026.acl-long.979.pdf
- Local PDF: pdf/2026-08-28_27_TamEdit_ Trajectory-Aware Meta-Learning for Specificity-Preserving Continual Knowledge Editing.pdf

Knowledge editing is a promising method for updating Large Language Models efficiently. However, previous studies often suffer from poor specificity in continual editing, as they typically focus on single edits or preventing knowledge forgetting. To address this, we propose TamEdit, a trajectory-aware meta-learning method that preserves specificity for continual knowledge editing. TamEdit unifies three levels: Inner Optimization performs multi-step fast fine-tuning on the single edit; Trajectory-based Editing unifies continual edits with a growing memory; and Outer Optimization leverages meta-learning to distill cross-task strategies for preserving specificity. By capturing the relationships between different single edits within the trajectory, our method learns how to effectively avoid specificity drift. Experiments across multiple LLMs show TamEdit significantly outperforms baselines in continual editing, improving specificity by 14.81% with fast speed (requiring only 8.84% of the time cost of most baselines), while preserving general capabilities.

## 28. Mechanistic Reaction Prediction via Discrete Flow Matching on Graph-Structured Electron Occupation

- Authors: Nguyen Xuan-Vu, Octavian Susanu, Daniel Armstrong, Philippe Schwaller
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-27
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 2.757699922130553
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.27429v1
- PDF: https://arxiv.org/pdf/2608.27429v1
- Local PDF: pdf/2026-08-28_28_Mechanistic Reaction Prediction via Discrete Flow Matching on Graph-Structured Electron Occupation.pdf

Chemical reactions are fundamentally transformations in electron space, yet most machine learning approaches model them either through \textit{de novo} generation of product molecules or through heuristic graph edits that operate directly on molecular topology.
  We introduce MAELLE (\textbf{M}ech\textbf{A}nistic \textbf{E}dit f\textbf{L}ow-matching on e\textbf{L}ectron r\textbf{E}arrangements), which instead models reactions as discrete flow matching over electron occupation vectors.
  Concretely, we formulate the reactant-to-product mapping as a Continuous-time Markov Chain (CTMC) over the graph-structured integer-valued electron occupation space defined on all bonding, non-bonding, and hydrogen sites.
  To construct the intermediate edit trajectories, we generalize the discrete flow matching mixture path to discrete electron rearrangements using Optimal Transport, yielding a sequence of mechanistically interpretable edit moves without requiring elementary step annotations.
  MAELLE achieves competitive performance on the USPTO-480K benchmark compared with leading reaction prediction models.
  Beyond in-distribution accuracy, we evaluate robustness across two out-of-distribution settings - structural complexity and reaction type - and find that MAELLE maintains strong performance where existing methods degrade.
  Finally, because the learned flow operates over the full electron redistribution, MAELLE naturally recovers mechanistic trajectories that align with known chemistry and can predict side products of a reaction.

## 29. Proximity-Based Multi-Turn Optimization: Practical Credit Assignment for LLM Agent Training

- Authors: Yangyi Fang, Jiaye Lin, Xiaoliang Fu, Cong Qin, Haolin Shi, Chang Liu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.7572404547668325
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-industry.19/
- PDF: https://aclanthology.org/2026.acl-industry.19.pdf
- Local PDF: pdf/2026-08-28_29_Proximity-Based Multi-Turn Optimization_ Practical Credit Assignment for LLM Agent Training.pdf

Multi-turn LLM agents are becoming pivotal to production systems, spanning customer service automation, e-commerce assistance, and interactive task management, where accurately distinguishing high-value informative signals from stochastic noise is critical for sample-efficient training. In real-world scenarios, a failure in a trivial task may reflect random instability, whereas success in a high-difficulty task signifies a genuine capability breakthrough. Yet, existing group-based policy optimization methods rigidly rely on statistical deviation within discrete batches, frequently misallocating credit when task difficulty fluctuates. To address this issue, we propose Proximity-based Multi-turn Optimization (ProxMO) , a practical and robust framework engineered specifically for the constraints of real-world deployment. ProxMO integrates global context via two lightweight mechanisms: success-rate-aware modulation dynamically adapts gradient intensity based on episode-level difficulty, while proximity-based soft aggregation derives baselines through continuous semantic weighting at the step level. Extensive evaluations on ALFWorld and WebShop benchmarks demonstrate that ProxMO yields substantial performance gains over existing baselines with negligible computational cost. Ablation studies further validate the independent and synergistic efficacy of both mechanisms. Crucially, ProxMO offers plug-and-play compatibility with standard GRPO frameworks, facilitating immediate, low-friction adoption in existing industrial training pipelines. Our implementation is available at: https://github.com/GithubX-F/ProxMO-RL .

## 30. Two-Stage Parameter Alignment for Multi-LoRA Merging in Large Language Models

- Authors: Zijian Li, Xiachong Feng, Weitao Ma, Yichong Huang, Xiaocheng Feng, Bing Qin
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.7569710146520783
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1504/
- PDF: https://aclanthology.org/2026.findings-acl.1504.pdf
- Local PDF: pdf/2026-08-28_30_Two-Stage Parameter Alignment for Multi-LoRA Merging in Large Language Models.pdf

Merging a large number of low-rank adaptations (LoRAs) is a key technology for enhancing the integration and deployment efficiency of large language models (LLMs). However, current general model merging methods are prone to “parameter interference” problem, and this issue is especially pronounced when merging high-rank LoRAs, where parameter conflicts tend to be more severe. While the classical rotation alignment approach can enhance robustness, it is difficult to apply due to incompatibility with the LoRA structure and its high computational complexity. To address these challenges, we propose a novel two-stage parameter alignment (TSPA) framework. TSPA is designed from the perspective of the LoRA architecture, overcoming the limitations of existing methods and reducing the computational complexity from quadratic to linear. We conduct experiments on Natural Language Processing (NLP) tasks using models such as Llama-3-8B. The results show that the two-stage design of TSPA achieves a balance between task capabilities and general knowledge. It exhibits greater robustness than other methods in high-rank and high-interference scenarios, while effectively preserving fine-grained functions.
