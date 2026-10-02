# Paper Daily Reading - 2026-10-02

## 1. CellMSA: Context Modeling for Single-Cell Representation Learning

- Authors: Suyuan Zhao, Minghao Liu, Yizhen Luo, Zaiqing Nie
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-30
- DOI: Unavailable
- Categories: q-bio.GN, cs.AI, cs.LG
- Relevance: 3.7032592799937216
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.38908v1
- PDF: https://arxiv.org/pdf/2609.38908v1
- Local PDF: pdf/2026-10-02_01_CellMSA_ Context Modeling for Single-Cell Representation Learning.pdf

Single-cell transcriptomics enables profiling of cellular states at unprecedented resolution, but its high dimensionality, sparsity, and technical batch effects pose significant challenges for representation learning. Existing single-cell foundation models typically encode each cell independently or only model cells from the same batch for denoising, thereby underutilizing the rich relational information across batches and cell types to model gene expression patterns. We argue that single-cell models can benefit from more informative cell-context modeling. By comparing consistency and variation across cells, models can capture fine-grained gene-gene dependencies associated with cell states, which are essential for learning high-quality representations. Inspired by the use of multiple sequence alignment (MSA) context in protein modeling, we propose CellMSA, a single-cell representation learning framework that introduces an MSA-inspired inductive bias into transcriptomic modeling. For each target cell, CellMSA retrieves relevant cells from different batches and biologically related cell types as context, and summarizes cross-cell patterns into a context-dependent gene-pair representation. This representation is then injected into a pair-aware target-cell encoder for fine-grained representation learning. We pretrain CellMSA on a large-scale human single-cell corpus of approximately 109 million cell observations, including 65.6 million primary observations. Experiments show that our framework consistently outperforms existing methods across multiple benchmarks. Code is available at the following repository: https://github.com/PharMolix/CellMSA.

## 2. NodeGround: A Node Classification Benchmark in the Graph Foundation Model Era

- Authors: Jinmo Lee, Dooho Lee, Minho Jeong, Jaemin Yoo
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-30
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.609304781551078
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.39673v1
- PDF: https://arxiv.org/pdf/2609.39673v1
- Local PDF: pdf/2026-10-02_02_NodeGround_ A Node Classification Benchmark in the Graph Foundation Model Era.pdf

Can a pretrained graph model replace training and tuning a separate predictor for each dataset? Answering this requires evaluating prediction quality alongside computational cost. We present NodeGround, a node classification benchmark that puts graph foundation models (GFMs) and dataset-specific supervised learning under a common evaluation framework. The benchmark spans 51 datasets and evaluates six GFMs alongside 15 supervised methods under two label-availability regimes. Shared data partitions, validation-only model selection, controlled hyperparameter searches, and multiple predictive metrics make comparisons systematic, while workflow measurements account for adaptation, training, tuning, and inference. The results favor carefully tuned graph neural networks overall. GraphPFN reaches third place by Elo when more labels are available, yet its relative strengths vary substantially with dataset properties. Efficiency comparisons further qualify the benefits of pretrained reuse: GVT and GraphPFN appear on the Pareto frontiers when supervised methods are represented by their default and fully tuned configurations. Adding intermediate tuning budgets removes this advantage for GVT and leaves GraphPFN extending the estimated frontier in the label-rich setting alone. Thus, reusing pretrained parameters does not yet provide a broadly reliable route to either stronger predictions or cheaper workflows. We release the evaluation pipeline, run-level records, and an open leaderboard at https://github.com/nums-ai/nodeground.

## 3. scTrilemma: Balancing Identity, Invariance, and Fidelity in Single-Cell Representation Learning

- Authors: Yunhak Oh, Yoonho Lee, Junseok Lee, Namkyeong Lee, Sang-Yeon Hwang, Yinhua Piao, Hyomin Kim, Seonghwan Kim, Jaechang Lim, Woo Youn Kim, Sungsoo Ahn, Chanyoung Park
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-30
- DOI: Unavailable
- Categories: cs.LG, cs.AI
- Relevance: 3.5376942218879703
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.38840v2
- PDF: https://arxiv.org/pdf/2609.38840v2
- Local PDF: pdf/2026-10-02_03_scTrilemma_ Balancing Identity, Invariance, and Fidelity in Single-Cell Representation Learning.pdf

Single-cell RNA-seq representation learning is fundamentally label-free: cell identities, states, and contexts are not fixed training targets, so what constitutes signal or nuisance is analysis-dependent. A single representation must therefore preserve biological identity and state, remain robust to nuisance context, and retain the gene-level variation needed for expression analysis, three demands we call the representation trilemma. To tackle this problem, we introduce scTrilemma, a latent-bottleneck VAE that routes expression-derived variation to the embedding, the decoder, or the prior rather than forcing all of it through one embedding. It gates gene tokens by expression, routes the cell representation through the decoder, and conditions the prior on unlabeled pseudo-bulk context, under a single reconstruction objective and without target annotations or auxiliary representation losses. In release-based zero-shot evaluation on successive CZ CELLxGENE Census releases, scTrilemma leads all three demands at once and preserves biological-state, differential-expression, and pathway structure across multiple disease settings. Latent interventions further show that context can be removed at almost no cost to the other demands, leaving identity against fidelity as the remaining tension. Code is publicly available at https://github.com/yunhak0/scTrilemma.

## 4. DrugSAGE: a transcriptome aggregation approach using cell lines for drug response imputation

- Authors: Peilin Jia, Zhongming Zhao
- Source: openalex
- Venue type: journal
- Journal: Genome Medicine
- Publication status: published
- Publication date: 2026-09-30
- DOI: https://doi.org/10.1186/s13073-026-01781-0
- Categories: Single-cell and spatial transcriptomics, Bioinformatics and Genomic Networks, Ferroptosis and cancer prognosis
- Relevance: 3.463318794959079
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://doi.org/10.1186/s13073-026-01781-0
- PDF: Unavailable
- Local PDF: Not downloaded

Accurate drug response prediction is essential for optimizing cancer therapy, yet genomic heterogeneity drives variable responses even among tumors with identical driver mutations. We developed DrugSAGE, a Graph Neural Network framework that predicts drug response from transcriptomic data by aggregating features from each sample and its most similar counterparts. A customized linear layer incorporating gene-pathway annotations provides biological interpretability. Benchmarking across independent bulk and single-cell datasets showed significant associations with known drug targets and treatment-stratified patient groups. DrugSAGE effectively predicts single-cell drug responses and identifies key genes and pathways, offering a novel, interpretable approach with superior or comparable performance.

## 5. GATE-ST: Gene-Aware Text-image Encoder for Spatial Transcriptomics

- Authors: Lucas Ni, Jian Luo, Wentao Huang, Chao Chen
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-30
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 3.398815622163154
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.38690v1
- PDF: https://arxiv.org/pdf/2609.38690v1
- Local PDF: pdf/2026-10-02_05_GATE-ST_ Gene-Aware Text-image Encoder for Spatial Transcriptomics.pdf

Spatial transcriptomics enables spatially resolved gene expression analysis from slide-level images while preserving morphological features, providing valuable information for studying disease mechanisms and developing treatments. However, spatial gene expression profiling typically requires expensive and time-consuming tests. While existing image-based prediction optimizations mostly revolve around including positional embeddings and further image-based changes, text-based optimizations remain relatively unexplored. We present GATE-ST, which incorporates text-based inputs into image-based spatial gene expression predictions. With this approach, generated text descriptions of genes are utilized to better spatial transcriptomics prediction results. Gene summaries are put through a text encoder, generating embeddings that integrate with image embeddings through cross-attention layers to align with morphological features. We demonstrate the effectiveness of such text inputs by benchmarking performance against random gene embeddings and multiple other image-text fusion architectures, and show that GATE-ST outperforms these alternatives. Our results demonstrate the effectiveness of GATE-ST in pathology imaging, which may greatly reduce the time and cost of accurate spatial transcriptomic predictions, proving the potential of text-guided spatial gene expression prediction.

## 6. GraphMAS: A Systematic Benchmark of Multi-Agent Coordination for Graph Learning

- Authors: Jiayi Yang, Yifang Chen, Yuanfu Sun, Xinyan Ge, Qiaoyu Tan
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-30
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.3869729085828193
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.39777v1
- PDF: https://arxiv.org/pdf/2609.39777v1
- Local PDF: pdf/2026-10-02_06_GraphMAS_ A Systematic Benchmark of Multi-Agent Coordination for Graph Learning.pdf

LLM-based multi-agent systems coordinate specialized reasoning through aggregation, interaction, and adaptive control, yet their potential for graph learning remains unexplored. Graph learning is a natural setting for such systems because useful evidence may arise from heterogeneous local, long-range, global structural, and semantic perspectives whose relevance varies across instances. Existing LLM-based graph learning approaches primarily rely on single-agent reasoning, while multi-agent coordination has been studied mainly in general reasoning settings. Consequently, it remains unclear whether multiple specialized agents can improve graph learning and how coordination strategies should be designed and evaluated. To address this gap, we introduce GraphMAS, a systematic benchmark of multi-agent coordination for graph learning. GraphMAS builds a shared pool of graph reasoning specialists and organizes coordination along two dimensions, inter-agent interaction and runtime adaptivity, yielding four paradigms and seven representative coordination methods. Under a unified protocol, we evaluate these methods across seven text-attributed graphs, three domains, and two graph learning tasks. We find that heterogeneous graph perspectives are complementary, and that coordinating specialists improves over individual specialists and single-agent graph reasoning, with gains from decomposing reasoning across specialists rather than from broader evidence access alone. However, richer inter-agent interaction does not reliably help, whereas instance-adaptive specialist selection yields the strongest accuracy-efficiency trade-off. We further show that coordination can be learned over a fixed specialist pool and transfers to held-out graphs. GraphMAS therefore provides a controlled evaluation framework and empirical principles for understanding when and how multi-agent coordination benefits graph learning.

## 7. Synchronous Multi-view Neural Diffusion

- Authors: Yongquan Shi, Weijun Huang, Yueyang Pi, Wendi Zhao, Yiqing Shi, Shiping Wang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-30
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.3694247079966653
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.39019v1
- PDF: https://arxiv.org/pdf/2609.39019v1
- Local PDF: pdf/2026-10-02_07_Synchronous Multi-view Neural Diffusion.pdf

Multi-view learning seeks to learn more comprehensive representations by exploiting the complementarity and consistency across diverse modalities or views. However, existing multi-view fusion strategies treat intra- and inter-view fusion as independent stages, without simultaneously considering the evolution within views and the dependency across views. Such an asynchronous fusion paradigm inevitably constrains cross-view interactions due to conflicting view-specific structural inductive biases. As a result, information flow is prone to distortion and compression along intermediate pathways, confining the model to learn within a restricted solution space. To address this, we propose Synchronous Multi-view Neural Diffusion (SynMDiff), which conceptualizes the multi-view feature space as a unified dynamical system driven by a diffusion process. By modeling the diffusion flow across arbitrary dyadic feature interactions in a joint space, SynMDiff enables the concurrent and adaptive intra- and inter-view information fusion. While a direct implementation of this synchronized mechanism incurs prohibitive computational costs, we further introduce an energy-based topological sampling strategy and an Ego-Net style centralized training architecture, ensuring both efficiency and scalability during learning and inference. Due to its conceptual elegance and computational efficacy, evaluations on real-world datasets demonstrate that SynMDiff outperforms the baselines by a large margin.

## 8. Doc2LoRA Provides Decodable Representations of Scientific Ideas

- Authors: Chand Sahil Mansuri, Joel Zachariah, Sadamori Kojaku
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-29
- DOI: Unavailable
- Categories: cs.CL, cs.DL, cs.IR, cs.LG, physics.soc-ph
- Relevance: 3.3622855528402305
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.38374v1
- PDF: https://arxiv.org/pdf/2609.38374v1
- Local PDF: pdf/2026-10-02_08_Doc2LoRA Provides Decodable Representations of Scientific Ideas.pdf

Representing scientific papers as points in a space lets us search for similar papers and inquire about how fields relate to one another and drive innovation. Beyond search, the vector space of papers invites generation: mixing papers through simple vector operations creates new points, mirroring combinatorial novelty, the recombination of existing ideas into new ones. However, a mixed point often represents an idea no paper has yet realized, with no papers nearby to identify the idea. We propose representing each paper by a LoRA adapter generated by the Doc-to-LoRA hypernetwork. Every point in the space, including mixtures, thus represents a large language model (LLM) open to questions and instructions in natural language. On papers from the American Physical Society (APS), we instruct the LLM at the average of each subfield to name the field in a few words and obtain labels closer to the official names than the labels of five baselines, as judged by word overlap and a panel of five LLM judges. We also ask the LLMs at points between two APS papers to write an abstract and obtain descriptions shifting from one paper to the other in step with the mixing weight. While Doc-to-LoRA is trained for generation, a small invertible transform makes the embeddings competitive for search, on par with SPECTER2 and EmbeddingGemma and close to SBERT. Because the transform is invertible, every point in the transformed space still maps back to an LLM. The embeddings thus serve both search and generation, enabling researchers to question the idea at any point in the space as a starting point for generating new ideas.

## 9. D-Scope: Decomposing and Steering Diffusion Transformers with Sparse Autoencoders

- Authors: Xinyue Xu, Jiahao Zhang, Lijie Hu, Peter Hase, Hao Wang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-30
- DOI: Unavailable
- Categories: cs.CV, cs.AI
- Relevance: 3.349492258234939
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.39625v1
- PDF: https://arxiv.org/pdf/2609.39625v1
- Local PDF: pdf/2026-10-02_09_D-Scope_ Decomposing and Steering Diffusion Transformers with Sparse Autoencoders.pdf

Sparse autoencoders (SAEs) reveal visual structure in diffusion transformers (DiTs), but interpreting a feature does not establish whether it can be used to control generation. We introduce D-Scope (Diffusion Scope), a framework that connects feature interpretation to generation control through shared visual evidence. D-Scope aggregates SigLIP~2 embeddings of highly activating image patches into visual centroids. Matching target text descriptions against these visual centroids in the shared image-text embedding space then enables retrieval of individual features without per-feature text annotations. The underlying patches provide evidence for inspecting each selection, while spatially masked interventions test the corresponding decoder direction at varying strengths under fixed generation conditions. We characterize 150 SAEs across two model families and five layers, and introduce a benchmark of 100 target concepts with ten contexts each spanning under-specified and explicit-conflict conditions. Our empirical results show that high reconstruction fidelity can coexist with low dictionary utilization and limited visual-evidence coverage. Under per-case best-of-sweep strength selection, contrastive retrieval yields larger mean regional SigLIP~2 gains than direct retrieval across the tested steering configurations, without consistently improving outside-region preservation. D-Scope provides an inspectable framework for evaluating sparse DiT features through their visual evidence and the effects of their decoder directions on generation. The demo is available at https://jiahaozhang-public.github.io/d-scope/.

## 10. MIND: Marginal-Invariant Neural Dependency Diffusion for Mixed-Type Tabular Generation

- Authors: Pengfei Li, Mohammad Khalil
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-30
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.285754260237887
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.39628v1
- PDF: https://arxiv.org/pdf/2609.39628v1
- Local PDF: pdf/2026-10-02_10_MIND_ Marginal-Invariant Neural Dependency Diffusion for Mixed-Type Tabular Generation.pdf

This paper proposes MIND, a marginal-invariant neural dependency diffusion model for mixed-type tabular data. MIND does not directly learn the joint distribution in the original heterogeneous feature space. Instead, it first maps different variable types into a unified latent dependency space via column-wise marginal transport. A conditional diffusion model then learns cross-column relationships. Copula-tangent denoising separates known marginal components from learnable dependency residuals. Rank projection during the sampling phase further mitigates marginal shift in reverse diffusion. Experiments across nine diverse tabular benchmarks show that MIND consistently improves marginal fidelity and dependency preservation over existing unified approaches. By explicitly isolating marginal modelling from dependency learning, MIND achieves a strong and stable balance among marginal fidelity, joint dependency preservation, and downstream prediction utility. This work supports separating marginal and dependency modelling as a principled and highly effective paradigm for complex mixed-type tabular generation.

## 11. Stable Transformers for Graph Generation

- Authors: Luca Miglior, Alessio Gravina, Davide Bacciu
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-30
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.233052465281183
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.39739v1
- PDF: https://arxiv.org/pdf/2609.39739v1
- Local PDF: pdf/2026-10-02_11_Stable Transformers for Graph Generation.pdf

Graph generative models increasingly rely on Graph Transformers (GT) to capture complex dependencies among nodes and edges. While deeper architectures should provide greater expressive capacity and a broader receptive field, their effectiveness can decline with depth: repeated self-attention progressively contracts node representations, impeding information flow and gradient propagation. We analyse this phenomenon from a dynamical systems perspective, focusing on how the denoiser's spectral dynamics affect graph generation. We show that standard GT denoisers become increasingly dissipative as depth grows, leading to vanishing gradients and representation collapse. To isolate the effect of these dynamics, we construct a permutation-equivariant GT with inherently stable, non-dissipative transport. We also introduce a damping mechanism that continuously interpolates between non-dissipative and increasingly contractive regimes, enabling a direct assessment of how dissipation influences generation. Experiments on synthetic and molecular graph generation benchmarks show that the gap between these regimes widens with depth: non-dissipative dynamics preserve representation diversity and gradient flow, sustaining strong generative performance, whereas greater contraction progressively impairs it. These findings identify the denoiser's dynamical regime as a key design factor for deep graph generative models.

## 12. Gestalt: a meta-foundation model for astronomy

- Authors: Michael J. Smith, Shashwat Sourav
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-29
- DOI: Unavailable
- Categories: astro-ph.IM, cs.LG
- Relevance: 3.2294212833309595
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.38312v1
- PDF: https://arxiv.org/pdf/2609.38312v1
- Local PDF: pdf/2026-10-02_12_Gestalt_ a meta-foundation model for astronomy.pdf

The Platonic Representation Hypothesis predicts that sufficiently scaled foundation models converge on a shared representation of the world. As each non-converged model gives a noisy view of a common structure when passed the same input, we ask whether we can combine models into a representation that outperforms its individual components. We test this on galaxies: we embed images via a basket of 22 frozen foundation models from eight families, whiten each view, and take a randomised SVD of the embedding concatenation. The resulting 1024-dimensional embedding outperforms every basket member on 19/21 of our tested metrics for physical property and galaxy morphology estimation for HSC, JWST, and DESI Legacy Survey imagery. We find that performance rises with basket size and basket architectural diversity, and that the meta-foundation model's performance transfers across astronomical surveys. We conclude that a useful astronomical foundation model can be assembled from existing generalist models with no training required beyond a single unsupervised projection. By leveraging the community's already-spent work, we save a lot of compute: a fresh pre-train of a comparable single-domain model would cost $\mathcal{O}(10^{4}$--$10^{5})$ A100 GPU hours (emitting several tonnes of CO$_2$eq.), whereas assembling Gestalt requires minutes on a single machine.

## 13. Why Do Conventional World Models Fail to Learn Cellular Automata?

- Authors: Shaoyang Guo, Ziming Liu
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-30
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 3.1710370566032426
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.39604v1
- PDF: https://arxiv.org/pdf/2609.39604v1
- Local PDF: pdf/2026-10-02_13_Why Do Conventional World Models Fail to Learn Cellular Automata.pdf

Although conventional world models - auto-regressive or diffusion models based on transformers or convolutional networks - may learn surface statistics of world dynamics, can they learn the exact world dynamics from its observed history? Leveraging cellular automata as a simple testbed, we find the answer to be no in many cases. Conventional architectures predict most pixels correctly yet rarely complete a rollout: a CNN predicts 96.3% of cells but completes 18.9% of rollouts; a joint diffusion model completes none. We trace the gap to three failure modes of these world models - namely, they fail to exactly capture spatial locality, temporal locality or temporal stability. Simple changes repair each: (1) for spatial locality, two-dimensional rotary positions lift a transformer from 39.1% to 100% on the Game of Life; (2) for temporal locality, handing each token its cell's previous-frame neighbourhood lifts the same transformer from 25.8% to 99.9% on unseen rules; (3) for temporal stability, causal freezing lifts the same diffusion weights from 42.2% to 99.9%. None of the three changes touches the architectural backbone; each only modifies the information flow within it. We also compare joint and ordered sampling on billiards and, in an exploratory study, on a simulated Burgers equation.

## 14. GroundAnything: Reconciling Parallel Decoding with Precise Visual Grounding at Flash Speed

- Authors: Qize Yu, Lianrui Fan, Bowen Ping, Xini Ding, Zetian Song, Junbo Niu, Kaixuan Wang, Tianxing Chen, Yue Chen, Minghua He, Yuran Wang, Jie Huang, Haojun Zhang, Min Chen, Hao Li, Wenxuan Song, Ruihai Wu, Xianming Liu, Shilong Liu, Shuchang Zhou, Ping Luo, Shiyu Huang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-30
- DOI: Unavailable
- Categories: cs.CV, cs.AI, cs.LG, cs.RO
- Relevance: 3.1551311147503225
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.39600v1
- PDF: https://arxiv.org/pdf/2609.39600v1
- Local PDF: pdf/2026-10-02_14_GroundAnything_ Reconciling Parallel Decoding with Precise Visual Grounding at Flash Speed.pdf

Autoregressive (AR) grounding models serialize spatial predictions, introducing sequential latency and imposing a causal order on output tokens. We view grounding as visual evidence extraction: objects, locations, and spatial relations are jointly constrained by the image and query, yet their dependencies do not imply an intrinsic left-to-right generation order. This distinction makes bidirectional diffusion a natural fit, allowing spatial hypotheses to emerge in parallel and be jointly refined through iterative denoising. We introduce GroundAnything, a 4B-parameter grounding foundation model that reconciles fast parallel decoding with precise localization through blockwise denoising. Training combines grounding pretraining from public datasets and dedicated data engines, direct AR-to-diffusion conversion with joint AR and diffusion objectives, supervised fine-tuning, and GRPO-based reinforcement post-training. Across 30 grounding benchmarks, our autoregressive variant, GroundAnything-VLM, establishes a new overall state of the art among similarly sized models at 72.42%, remaining competitive with GPT-6 Astra (71.35%). With entropy-guided decoding, GroundAnything also surpasses the prior state of the art at this scale, averaging 61.75% versus 53.32% for the fast MTP-based LocateAnything model. We further explore decoding strategies, showing that an optional self-speculative mode achieves a $4.51\times$ speedup over the AR counterpart with a 0.74 percentage-point drop in COCO F1mIoU. Infrastructure experiments show that progressive inference optimizations translate parallel decoding into practical speedups. These support efficient visual grounding in latency-sensitive real-world systems.

## 15. GraphCert: Bootstrap Agentic Graph Reasoning with Certified Evidence Rubrics

- Authors: Weiqi Jiang, Yuchen Ying, Rui Wang, Kaixuan Chen, Bingde Hu, Shunyu Liu, Yu Wang, Tongya Zheng
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-30
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 3.149777081453377
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.38798v1
- PDF: https://arxiv.org/pdf/2609.38798v1
- Local PDF: pdf/2026-10-02_15_GraphCert_ Bootstrap Agentic Graph Reasoning with Certified Evidence Rubrics.pdf

Graph agents extend large language models (LLMs) with the ability to actively explore and reason over knowledge graphs through multi-step interactions with graph tools. However, training capable graph agents typically requires large collections of question-answer pairs and reasoning trajectories, whose manual construction is costly and difficult to scale. Moreover, employing proprietary LLMs to generate such supervision further risks exposing sensitive graph data to external services. Therefore, we propose GraphCert to bootstrap agentic graph reasoning with certified evidence rubrics during post-training. Specifically, the Bootstrapped Graph Quizzer guided by generation controls produces graph-grounded QA pairs and marks supporting evidence, which undergo execution certification and semantic curation. The accepted evidence is then canonicalized into certified evidence rubrics that later reward Graph Solver evidence alignment alongside answer correctness during GRPO training. Experiments on five graph reasoning domains in GRBENCH demonstrate that GraphCert consistently outperforms substantially larger LLM agents and post-training method. Furthermore, our analysis demonstrates that the learned policy transfers robustly across heterogeneous graph domains, suggesting that GraphCert acquires reusable graph-reasoning capabilities rather than domain-specific patterns. These results establish executable self-certification as an effective approach to self-training compact graph reasoning agents. Our code will be made publicly available.

## 16. RW-Flow: One-Step Generation on Compact Manifolds via Wasserstein Gradient Flows

- Authors: Ualibyek Nurgulan, Seungwoo Yoo, Prin Phunyaphibarn, Minhyuk Sung
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-30
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.1357462405038508
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.39271v2
- PDF: https://arxiv.org/pdf/2609.39271v2
- Local PDF: pdf/2026-10-02_16_RW-Flow_ One-Step Generation on Compact Manifolds via Wasserstein Gradient Flows.pdf

Manifold-valued data, and consequently the distributions they induce, are prevalent across many domains, ranging from the locations of geospatial events, such as earthquakes, to biomolecular torsion angles that encode information about three-dimensional structure. While diffusion and flow-based generative models have been successfully extended to compact manifolds, sampling typically requires tens or hundreds of sequential network evaluations. We introduce RW-Flow, a theoretically grounded framework for learning one-step generative models on compact manifolds via Wasserstein gradient flows. The main challenge is identifiability: driving the velocity field to zero should guarantee that the model distribution matches the target distribution. We establish a necessary and sufficient condition for identifiability on compact, connected Riemannian manifolds. We specifically show that, for a symmetric, Lipschitz-continuous cost function, the velocity field induced by the Sinkhorn divergence is identifiable if and only if the associated Gibbs kernel is nondegenerate. This characterization provides a general principle for designing identifiable costs on compact manifolds. It also reveals that the squared geodesic distance, the natural manifold analogue of the squared Euclidean distance, does not always guarantee identifiability. Across benchmarks involving geospatial events, protein side chain torsion angles, RNA backbone torsion angles, and general manifolds discretized as triangular meshes, RW-Flow outperforms existing one-step methods in nearly all settings under fair comparison conditions.

## 17. ArchMap is a web-based platform for reference-based analysis of single-cell datasets

- Authors: Mohammad Lotfollahi, Chelsea A. Bright, Ronald Skorobogat, Mohammad Moghareh Dehkordi, Xavier George, Simon Richter, Vladimir A. Shitov, Aleksandra Topalova, Helena Melcher, Noah Nussbaumer, Annika Fomm, Malte D. Luecken, Fabian Joachim Theis
- Source: openalex
- Venue type: journal
- Journal: Nature Genetics
- Publication status: published
- Publication date: 2026-09-30
- DOI: https://doi.org/10.1038/s41588-026-02756-y
- Categories: Single-cell and spatial transcriptomics, Cell Image Analysis Techniques, Ferroptosis and cancer prognosis
- Relevance: 3.1266165257743292
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://doi.org/10.1038/s41588-026-02756-y
- PDF: Unavailable
- Local PDF: Not downloaded

Abstract Leveraging single-cell reference atlases to analyze new data has brought about a paradigm shift in single-cell data science akin to the first reference genome in genomics. However, methods for performing this mapping require computational expertise and, oftentimes, considerable compute power, limiting access for researchers who may benefit the most. Here ArchMap, a no-code query-to-reference mapping tool, removes this barrier by providing all-in-one automated mapping, cell-type annotation and collaborative features to analyze single-cell datasets from a wide range of integrated, often published, reference atlases and allows the extension of atlases with the growing Human Cell Atlas and related efforts. This paves the way for a democratization of reference mapping capabilities.

## 18. Molecular Property Prediction under Structural Shift with Tabular Foundation Models

- Authors: Jinmo Lee, Dooho Lee, Minho Jeong, Jaemin Yoo
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-30
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.0687012155964624
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.38744v1
- PDF: https://arxiv.org/pdf/2609.38744v1
- Local PDF: pdf/2026-10-02_18_Molecular Property Prediction under Structural Shift with Tabular Foundation Models.pdf

Predicting molecular properties for compounds that differ structurally from labeled training molecules is important for drug discovery and materials design. Tabular foundation models (TFMs) offer a promising approach through in-context learning, but their performance under structural shifts and the value of molecular comparisons in this setting remain underexplored. We study structural generalization in molecular property prediction and introduce MolPAIR (Molecular Pair-Augmented In-context Refinement), a framework that combines molecule-level and molecular-pair contexts without task-specific parameter updates. A global tabular foundation model (TFM) first predicts a query's property from labeled molecular examples. A second frozen TFM predicts differences in prediction errors between the query and labeled reference molecules, using these comparisons to refine the initial prediction. Across 58 MoleculeACE and Polaris tasks, CheMeleon representations combined with TabPFN-3 already outperform each evaluated baseline on a majority of tasks. MOLPAIR further improves this predictor on 46 of 58 tasks, with gains across four molecular representations and three TFM backbones. These results show that explicit molecular comparisons can strengthen tabular in-context learning for structural generalization while keeping the molecular encoder and pretrained model weights fixed. The code and datasets are available at https://github.com/nums-ai/MolPAIR.

## 19. Network-based Spatial Context Retrieval for Open-weight LLMs: A Faithfulness Benchmark for Grounded Geographic Reasoning

- Authors: Joan Perez
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-30
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.0642815309925373
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.39437v1
- PDF: https://arxiv.org/pdf/2609.39437v1
- Local PDF: pdf/2026-10-02_19_Network-based Spatial Context Retrieval for Open-weight LLMs_ A Faithfulness Benchmark for Grounded Geographic Reasoning.pdf

Large language models (LLMs) encode substantial latent geographic knowledge, yet they reason poorly over space and are unreliable when queried from coordinates alone. Useful behaviour emerges only when structured spatial context is supplied in the prompt. This raises a question geographic evaluation has left unexamined: once the right context is supplied, does the model reason from it, or override it with its own parametric recall? We take up this question with an open pipeline for network-based spatial context retriev-al. In it, the surroundings of a selected point are defined by the pedestrian street network, the area actually reachable on foot. Using only open data and open-weight models, the pipeline retrieves features from OpenStreetMap and the GHS-POP population grid, computes indicators over the network catchment in code, and injects them as a compact spatial brief. On this basis we build a faithfulness benchmark. It labels every claim a model makes by its source (grounded in the brief, or drawn from training knowledge) and its correctness, and it probes each case with a planted false premise that the brief refutes. We evaluate sixteen open-weight model configurations across three families (Qwen, Gemma and Llama, with Gemma in two generations), four size classes and, where available, both thinking and non-thinking modes, on three con-trasting cities, resampling every case over ten seeds. The results show that resistance to the planted premise varies more strongly by model family and generation than by scale, while brief-reading competence forms a partly separate dimension. These behaviours are not captured by conventional world-correctness scores or single-shot evaluation. We release the implementation, spatial briefs, model outputs, and claim-level labels as a reproducible workflow at github.com/perezjoan/NSCR-LLM.

## 20. Does Learning Protein Folding Generalize to Broader Reasoning?

- Authors: Yong Liu, Zhanpeng Shi, Yizhou Dang, Zhongyue Zhang, Xiaoliang Shi, Zhijian Wei, Shuangjia Zheng
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-30
- DOI: Unavailable
- Categories: cs.LG, cs.AI
- Relevance: 3.0634457121921783
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.38879v1
- PDF: https://arxiv.org/pdf/2609.38879v1
- Local PDF: pdf/2026-10-02_20_Does Learning Protein Folding Generalize to Broader Reasoning.pdf

Large language models rely heavily on human text, which often conveys surface answers rather than the spatial and structural logic behind them. Protein folding is a natural testbed, because one solved structure yields thousands of exactly checkable spatial and topological statements. We ask: can learning to fold proteins teach general models reusable reasoning capabilities? To answer this, we build FoldingCorpus, a protein-derived question-answer dataset, and Fold2Reason, a recipe that post-trains on it through two complementary signals: discrete structural answers predicted via the model's native language head, and continuous 3D geometry decoded from the same shared representations. On FoldBench, Fold2Reason achieves structure prediction scores 2.7 to 3.5 times those of Qwen3.5-9B. Beyond protein structure prediction, it improves performance on all 10 benchmarks spanning spatial, graph, scientific, and general reasoning, raising macro-average accuracy from 45.09% to 48.33% (+3.23 pp), with positive gains on all 10 benchmarks, while matched controls built from random, synthetic, and shuffled structure yield substantially smaller or negative gains. Our work shows that non-linguistic, structure-dense scientific data can systematically improve broad reasoning in language models, making a solved scientific problem a practical source of post-training supervision.

## 21. SparseEngine: Sparse-First Inference Engine

- Authors: Jitai Hao, Quansheng Gu, Qiang Huang, Jun Yu
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-30
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.059237688340228
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.39068v1
- PDF: https://arxiv.org/pdf/2609.39068v1
- Local PDF: pdf/2026-10-02_21_SparseEngine_ Sparse-First Inference Engine.pdf

Long-context LLM agents accumulate interaction histories that strain KV-cache memory and attention computation. Although sparse attention reduces these costs, heterogeneous cache representations and workflows hinder integration with existing inference engines, while prior sparse-serving abstractions support only specific layouts or workflows. We present SparseEngine, a ground-up, sparse-first inference engine whose shared lifecycle contract lets each method control its KV representation and computation while coordinating state transitions with common serving infrastructure. SparseEngine supports 15 methods across four categories and enables cross-request state management through Chain Cache, which resumes KV-eviction methods from retained history, and controllable Prefix-Cache Pruning, which removes KV from selected history regions while preserving logical-prefix matching. While maintaining method quality, SparseEngine delivers over 10x higher throughput with KV eviction, over 2.5x faster decoding at matched concurrency than vLLM, and over 2x end-to-end speedup on agent benchmarks. The code is available at https://github.com/CURRENTF/SparseEngine.

## 22. Distilling Diffusion Score Discrepancy for Efficient Training Data Attribution

- Authors: Shixuan Liu, Joan Serrà, Kin Wai Cheuk, Jinju Kim, Woosung Choi, Yukara Ikemiya, Wei-Hsiang Liao, Jiaqi W. Ma, Yuki Mitsufuji
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-30
- DOI: Unavailable
- Categories: cs.LG, cs.AI
- Relevance: 3.056217471676916
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.38776v1
- PDF: https://arxiv.org/pdf/2609.38776v1
- Local PDF: pdf/2026-10-02_22_Distilling Diffusion Score Discrepancy for Efficient Training Data Attribution.pdf

Training data attribution for diffusion models aims to identify the training samples that influence a generated instance, but existing methods either require costly per-sample gradient computation or query-specific model optimization. Moreover, most methods attribute changes in a proxy loss rather than changes in the actual model's generative behavior. We address these limitations by formulating attribution directly with a local score discrepancy measure, which applies to any diffusion variant (including DDPM, EDM, and flow matching), and by showing that such measure can be estimated without retraining, as a preconditioned gradient similarity. We instantiate this estimator as Training-data Influence via score Discrepancy (TID), which uses Kronecker-factored curvature to avoid random projections and per-sample gradient storage. We then distill TID into TIDE, a forward-only student trained online to reproduce the teacher's rankings from the diffusion model's internal activations. Under counterfactual evaluation on CIFAR-10, ArtBench-10, and MS-COCO, TID matches or outperforms state-of-the-art approaches, while TIDE retains most of TID's accuracy at four to five orders of magnitude lower per-query cost, attributing generated samples in milliseconds and faster than the generation itself.

## 23. FlashDiffusion: Fused Tiled Kernel Spectral Decomposition

- Authors: Julio Candanedo
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-18
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.042244962847247
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.38198v1
- PDF: https://arxiv.org/pdf/2609.38198v1
- Local PDF: pdf/2026-10-02_23_FlashDiffusion_ Fused Tiled Kernel Spectral Decomposition.pdf

Diffusion maps, and kernel methods more generally, provide an interpretable nonlinear spectral representation basis for geometric learning. In the geometric limit, small bandwidth, these matrices tend to be high rank and thus require materializing dense Gaussian kernels requires $O(N^2)$ memory. We introduce FlashDiffusion, a matrix-free method that evaluates dense Gaussian kernel blocks in fused GPU tiles and couples the eigensolver to an empirical $β$-flow that selects the finite-sample resolution scale. A continuation over sample size and bandwidth warm-starts increasingly expensive spectral solves from coarser resolutions.

## 24. Graph Residual Conjugate Diffusion: SNR-Equalized Heat Flow for Graph Signals

- Authors: Jinwei Li, Daniel Tenbrinck
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-30
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.0372190862719632
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.39658v1
- PDF: https://arxiv.org/pdf/2609.39658v1
- Local PDF: pdf/2026-10-02_24_Graph Residual Conjugate Diffusion_ SNR-Equalized Heat Flow for Graph Signals.pdf

Diffusion models generate data by reversing a forward corruption process that typically approaches a simple Gaussian prior. Recent work has extended this framework to signals supported on fixed graphs, e.g., road-network traffic and sensor-network measurements. Many graph signals have nonuniform spectral energy, whereas isotropic corruption adds the same conditional noise variance to every graph-frequency mode. Driving all modes to near-zero terminal signal-to-noise ratio (SNR) requires strong corruption, which increases the noise range that must be covered under a fixed sampling budget. We introduce Graph Residual Conjugate Diffusion (GRCD), which replaces the shared clock of graph heat diffusion with a mode-dependent clock that gives every graph-Fourier mode the same conditional SNR. GRCD fits a zero-mean graph-spectral Gaussian reference on the training split and stops at a finite terminal SNR at which the propagated reference still carries the fitted spectral variances. The Gaussian component has an exact modewise propagator in the probability-flow ODE, so sampling advances it analytically and integrates only the learned residual score numerically. We evaluate GRCD on five settings (METR-LA traffic, Molene weather, and three stochastic block models) against seven comparators under a matched protocol: Graph-Aware Diffusion (GAD), EDM (graph backbone), two adaptations of Whitened Score Diffusion (WSD), and three preconditioning controls. At four function evaluations (NFEs), GRCD lowers averaged maximum mean discrepancy (aMMD) by 22 to 36 times over the best comparator on all five settings, reaching 0.054 on METR-LA, where it clears an aMMD 0.1 target with 87% less sampling wall-clock time than the cheapest comparator that reaches it. Fitting the terminal reference reduces aMMD by 2.7 to 7.3 times at finite terminal SNR, while the factors shrink to 1.00 to 1.01 near zero.

## 25. TAGGRAPH: Tag-Augmented Graphs for Graph Retrieval of Agent Persistent Histories

- Authors: Yu-Su Chen, Yu-Jung Liang, Pengtao Xie
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-29
- DOI: Unavailable
- Categories: cs.IR, cs.AI
- Relevance: 3.029445590391635
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.38353v1
- PDF: https://arxiv.org/pdf/2609.38353v1
- Local PDF: pdf/2026-10-02_25_TAGGRAPH_ Tag-Augmented Graphs for Graph Retrieval of Agent Persistent Histories.pdf

Long-term memory lets LLM agents recall past interactions and remain consistent across sessions, but memory systems are hard to compare because they often vary in representation, indexing, retrieval, and evaluation. We present a controlled evaluation framework based on shared 5W-style conversational memories. Localized graph configurations traverse a common base graph; AdaptiveGraph adds chronological edges and Personalized PageRank diffusion. We also evaluate BM25 over the same extracted notes and OpenClaw as a raw-input external reference. Retrieval rankings vary across memory settings. On LongMemEval-S, AdaptiveGraph is the strongest graph configuration at 0.844 MRR, but BM25 reaches 0.867 and OpenClaw 0.880. On ATANT Core, localized graph traversal outperforms diffusion and BM25, whereas BM25 leads the stress rounds. Reducing LongMemEval-S within the tested range does not reproduce the ATANT diffusion penalty, but the smallest tested store remains larger than ATANT Core, so store size cannot be ruled out. The penalty also persists under a permissive content-match criterion. Vocabulary normalization and extraction quality substantially affect graph retrieval, and missing extraction tags are common among top-five misses. Retrieval strategies should therefore be evaluated jointly with the memory setting and against strong lexical baselines.

## 26. Predicting Multi-View Rashomon Representation: Can We Learn Where Models Disagree?

- Authors: Mingyue Ma, Zongbo Han, Changqing Zhang, Guangyu Wang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-30
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.024673776304056
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.39848v1
- PDF: https://arxiv.org/pdf/2609.39848v1
- Local PDF: pdf/2026-10-02_26_Predicting Multi-View Rashomon Representation_ Can We Learn Where Models Disagree.pdf

Foundation models are increasingly adopted across a wide range of applications, often serving as core blocks within AI systems. Yet different foundation models may encode the same input from multiple different views, leading to substantial representation disagreement, which we term Rashomon Representation. Such disagreement often signals inputs that a given model encodes in a way inconsistent with other models, offering a valuable yet underexplored signal for input reliability estimation. While prior work has largely focused on measuring disagreement across multiple models with a representation set, we instead focus on predicting disagreement from a single representation. We hypothesize that this disagreement follows some consistent, input-dependent patterns rather than occurring at random. To test this, we quantify disagreement by comparing each sample's nearest neighbors across different models' representation spaces, then train a lightweight predictor that estimates disagreement from a single model's representation. At inference time, given a new input, the predictor uses that input's representation to tell whether it aligns with or diverges from those of other models. Extensive experiments across diverse foundation models and datasets show that representational disagreement is indeed input-dependent, predictable, and generalizable, enabling efficient reliability estimation of foundation models.

## 27. Learning to Route in Visual Space via Multi-Step Embedding Retrieval

- Authors: Tianyu Chen, Mingyuan Zhou, Jiaxing Wu
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-30
- DOI: Unavailable
- Categories: cs.AI, cs.IR
- Relevance: 3.0239925392828986
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.38743v1
- PDF: https://arxiv.org/pdf/2609.38743v1
- Local PDF: pdf/2026-10-02_27_Learning to Route in Visual Space via Multi-Step Embedding Retrieval.pdf

LLM agents rely on retrieval tools to access external knowledge, yet visual agentic search remains severely bottlenecked by standard single-step retrievers. In current pipelines, the agent must issue text queries for every intermediate step, struggling when visual clues are difficult to describe or when the retriever fails to surface necessary intermediate evidence within its top results. We hypothesize that offloading multi-step navigation across the entire embedding space directly to the retrieval tool resolves this performance bottleneck. To study this systematically, we introduce VHOP, a flexible data generation framework and benchmark with five core difficulty levels testing both visual matching and search planning. Using this framework, we develop VHOP-Router, an end-to-end training pipeline---combining supervised fine-tuning, online imitation learning, and reinforcement learning---that transforms a standard embedding model into an autoregressive multi-step retriever. Operating directly in the visual latent space, VHOP-Router retrieves linked image chains in a single tool call without requiring the agent to formulate intermediate text queries. Experiments show VHOP-Router boosts retrieval performance from under 5\% to 76.3\%. In agentic search, it improves task success rates by 52.7\% and reduces the average token length by 61\% from 1886 to 728, whereas upgrading the agent yields only a 3.7\% gain. Compared to a strong baseline where the agent retrieves the top 50 results per step, VHOP-Router maintains superior performance while reducing in-context images by $23\times$ and cutting the cumulative API payload by $35\times$. The models also generalize robustly to unseen difficulty levels and realistic test sets. Ultimately, VHOP and VHOP-Router provide an efficient and effective solution for visual agentic search that leaves native LLM capabilities entirely intact.

## 28. CAST: Causal Advantage-Structured Training with Spatially Grounded Compositional Rewards for Diffusion Models

- Authors: Shu Yu, Chaochao Lu
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-30
- DOI: Unavailable
- Categories: cs.CV, cs.AI, cs.LG
- Relevance: 3.0152472169471256
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.39441v1
- PDF: https://arxiv.org/pdf/2609.39441v1
- Local PDF: pdf/2026-10-02_28_CAST_ Causal Advantage-Structured Training with Spatially Grounded Compositional Rewards for Diffusion Models.pdf

Online reinforcement learning has been extended to flow matching for diffusion model (DM) image generation. However, this paradigm faces three limitations: (1) Window selection. Existing methods manually set the stochastic differential equation (SDE) sampling window, i.e., the denoising steps where exploration noise is injected. We instead determine it from each model's denoising trajectory. (2) Reward saturation. Current methods rely on scoring models trained on human annotations; we find that such scores are extremely high and nearly indistinguishable on the latest SOTA open-source DMs, making advantage estimation largely ineffective. (3) Sample inefficiency. A single scalar reward collapses different failure modes into almost identical scores, leaving minimal gradient guidance for targeted improvement. To address these issues, we propose CAST (Causal Advantage-Structured Training), an RL fine-tuning method for pretrained DMs, which (1) identifies the denoising step at which each model fixes the objects and their spatial arrangement in the image and uses that timing to set the SDE window, (2) decomposes each prompt via Causal Scene Graphs (CSG) into verifiable-atoms, i.e., minimal semantic units such as an object, count, attribute, or spatial relation that can each be checked independently, and rewards each atom separately, and (3) projects the signed atom-level advantages into pixel space through teacher-forced attention and uses them to spatially weight the SDE policy objective. We fine-tune two of the strongest open-source DMs, FLUX.2-dev and Qwen-Image-2512, with CAST, and evaluate them on GenEval 2, a compositional benchmark, and on Qwen-Image-Bench for overall quality. Within almost the same training budget, CAST's improvement over the base model on the most challenging GenEval 2 prompts is up to 3.07x that of Flow-GRPO, while overall generation quality also improves.

## 29. DAGent: Evaluate-then-Grow Planning for Deep Research Agents

- Authors: Hanwen Liu, Yuanfu Sun, Qiaoyu Tan
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-30
- DOI: Unavailable
- Categories: cs.CL, cs.AI
- Relevance: 3.0099329324410764
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.39154v1
- PDF: https://arxiv.org/pdf/2609.39154v1
- Local PDF: pdf/2026-10-02_29_DAGent_ Evaluate-then-Grow Planning for Deep Research Agents.pdf

Deep research tasks require agents to navigate large knowledge spaces, synthesize evidence across many sources, and adapt their plans as findings emerge. Directed acyclic graph (DAG)-based multi-agent systems suit this setting because they support parallel execution and isolate each sub-task within a focused dependency context. Yet existing DAG-based agents instantiate a task-level plan before execution and repair the graph only after failures or missing evidence are observed. This Plan-then-Patch strategy is brittle for deep research: the system commits most strongly when its evidence is weakest, and later revisions waste computation on branches that should not have been planned. We propose DAGent, a DAG-based multi-agent framework with Evaluate-then-Grow incremental planning: an Orchestrator grows the task graph one batch at a time, conditioning each expansion on confidence and uncertainty signals from completed nodes. A hierarchical context layer propagates compact QueryDocs by default while preserving full execution traces for on-demand recall. The recorded DAG topology admits structural RL signals that outcome-only recipes cannot define; DAGRPO, a GRPO adaptation, injects topology-conditioned credit on Executor rollouts and a structural compliance regularization on Orchestrator plans. Across BrowseComp-Plus, GAIA, and xbench-DeepSearch, DAGent surpasses the strongest open-source baseline by 5.3 / 5.8 / 2.0 points at the Qwen3-235B-A22B scale, and the lead replicates across four open-source backbones and extends to GPT-5 at 327K context. At the Qwen3-8B scale, DAGRPO improves over a same-budget outcome-only GRPO baseline by 3.0 average Pass@1 points. A same-architecture comparison shows that evidence-conditioned planning reaches higher accuracy at lower per-task token, tool-call, and step footprints than its Plan-then-Patch counterpart. Code: https://github.com/hanwenliu6825/DAGent

## 30. Life-Bench: A Benchmark and Knowledge Graph Framework for Multimodal Personalization Beyond Concept Recognition

- Authors: Xia Hu, Honglei Zhuang, Brian Potetz, Alireza Fathi, Bo Hu, Babak Samari, Howard Zhou
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-02-22
- DOI: Unavailable
- Categories: cs.CV, cs.AI, cs.CL, cs.IR
- Relevance: 3.0022253898608344
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2602.19001v2
- PDF: https://arxiv.org/pdf/2602.19001v2
- Local PDF: pdf/2026-10-02_30_Life-Bench_ A Benchmark and Knowledge Graph Framework for Multimodal Personalization Beyond Concept Recognition.pdf

As large language models increasingly power personal assistants, users expect them to reason over multimodal life histories, from recognizing people to understanding events to aggregating patterns, yet existing benchmarks primarily target concept-level recognition. We introduce Life-Bench, a fully synthetic, human-verified multimodal benchmark of over 11,800 question-answer pairs across 10 tasks, organized by required evidence scope: concept identification, event understanding, and aggregated reasoning. The benchmark's photo-centric personal histories are distributionally aligned with real user accounts under embedding statistic. The interconnected structure of personal data invites graph-based solutions; we propose LifeGraph, a personal knowledge graph framework providing structured retrieval with on-demand access to source visual evidence, showing particular promise on event and aggregated tasks. Systematic evaluation of four retrieval paradigms on Life-Bench demonstrates that accuracy degrades sharply with evidence scope, falling below 0.40 on aggregated tasks, and that no single paradigm dominates across categories. Performance beyond concept recognition remains modest for all evaluated methods, establishing personalization over multimodal histories as an open challenge and Life-Bench as a testbed for future progress.
