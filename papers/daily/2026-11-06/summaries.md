# Paper Daily Reading - 2026-11-06

## 1. Graph-Mediated Large Language Model Systems in the Agentic Era: Reasoning, Knowledge, Retrieval, Execution, and Coordination

- Authors: Haihui Liu, Yang Chen, Zice Qiu, Yun Zhang, Jialun Zhong, Wenhua Wang, Yanzeng Li, Tian Wang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-04
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 3.475798394777876
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.05953v1
- PDF: https://arxiv.org/pdf/2611.05953v1
- Local PDF: pdf/2026-11-06_01_Graph-Mediated Large Language Model Systems in the Agentic Era_ Reasoning, Knowledge, Retrieval, Execution, and Coordina.pdf

Graphs play an increasingly important role in large language model (LLM) systems, supporting structural reasoning, knowledge grounding, retrieval, and memory. As these systems evolve toward the agentic era, graphs also organize execution dependencies and multi-agent communication, linking intermediate observations and retained information to subsequent decisions. However, understanding their contribution requires distinguishing the function of each graph operation, the component responsible for its computation, and the subsequent use of its output. This survey introduces an operation-level role--locus taxonomy for reasoning, knowledge and evidence, retrieval and memory, execution, and coordination. We compare how graph observations and external computations guide decisions, how memory representations and updates support later tasks, and how dependencies constrain execution and information delivery. These comparisons distinguish improvements in local metrics from downstream task performance while retaining the conditions under which results were reported. We then organize benchmarks, comparison designs, process diagnostics, and system costs into an evaluation framework. Finally, we identify open challenges in adaptive computation and stopping, memory maintenance, and dependency-aware recovery. The survey provides a basis for assessing when graph mechanisms are useful and for evaluating their effects across components and stages.

## 2. Learning Pseudo-Riemannian Manifolds for Heterophilic Graphs via Graph Signature

- Authors: Yun Young Choi, Asung Kil, Sun Woo Park, Minho Lee, Seokhwan Kim
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-04
- DOI: Unavailable
- Categories: cs.LG, cs.AI
- Relevance: 3.346416631266398
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.06265v1
- PDF: https://arxiv.org/pdf/2611.06265v1
- Local PDF: pdf/2026-11-06_02_Learning Pseudo-Riemannian Manifolds for Heterophilic Graphs via Graph Signature.pdf

Several widely used families of Graph Neural Networks carry a positive-definite geometric prior. Graph convolution read as heat diffusion needs a positive semi-definite operator, hyperbolic models place features on positive-definite Riemannian manifolds, and dot-product and GAT-style attention scores use positive-definite inner products. On heterophilic graphs, where edges often signify dissimilarity or structural repulsion, that prior is a mismatch: no positive-definite form can assign a negative squared distance to a direction the labels separate. To measure the mismatch, we introduce the Graph Signature Index ($s_{\mathcal{G}}$), the inertia of a class-compatibility matrix built from label topology alone, and we prove that no value of the edge or node homophily index in $(0,1)$ rules out a negative eigenvalue. We then propose the Pseudo-Riemannian Attention Network (PRAT), whose attention logit is a signed squared pseudo-distance under a learnable diagonal metric initialized from $s_{\mathcal{G}}$. The design is diagnose-then-learn: the signature supplies a sign structure that unconstrained training keeps outside near-zero directions, and the projection learns the rest of the metric around it. Across fifteen node-classification benchmarks PRAT outperforms or matches the strongest heterophily-adapted models. A controlled ablation ties that performance to the sign structure itself: with architecture and protocol fixed, forbidding the metric to be indefinite costs accuracy on the graphs $s_{\mathcal{G}}$ marks as indefinite and leaves the others unchanged.

## 3. Toward a Compositional Knowledge Architecture for a Shared Organizational Cortex

- Authors: Andrew Miracle, Phyl Georgiou, Christine Okoth, Ese Monday
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-03
- DOI: Unavailable
- Categories: cs.AI, cs.IR
- Relevance: 3.339750827499111
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.05753v1
- PDF: https://arxiv.org/pdf/2611.05753v1
- Local PDF: pdf/2026-11-06_03_Toward a Compositional Knowledge Architecture for a Shared Organizational Cortex.pdf

Organizations accumulate evidence in conversations, documents, decisions and relationships, but they act on interpretations: judgements assembled from several observations, resting on assumptions, and revised as circumstances change. Existing retrieval, knowledge graphs and agent memory keep the records and lose the interpretation. We propose a four-layer architecture, Signals, Domains, Claims and Dimensions, in which interpretations persist with their justifications and standing, a truth-maintenance network revises that standing as evidence changes, and validated, versioned Dimensions position interpretations on named axes. We call the result a shared organizational cortex. In a registered retrieval experiment, the Dimension term gains 0.028 nDCG@10 (p = 0.002). In system-level comparisons, the full retrieval configuration improves nDCG@10 by 0.081 over Signals-only and 0.053 over graph-augmented Signals-only retrieval (both reported p < 0.001). The architecture gives organizations a persistent, revisable basis for shared judgement.

## 4. CellCanon: An Agentic Cellular World Model for Prediction, Explanation, and Observation-Driven Updating

- Authors: Zhaokang Liang, Shuyang Zhuang, Xiaoran Jiao, Hao Chen
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-04
- DOI: Unavailable
- Categories: q-bio.QM, cs.AI
- Relevance: 3.3071030421486833
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.05890v1
- PDF: https://arxiv.org/pdf/2611.05890v1
- Local PDF: pdf/2026-11-06_04_CellCanon_ An Agentic Cellular World Model for Prediction, Explanation, and Observation-Driven Updating.pdf

Biological discovery requires using molecular knowledge and new measurements to infer responses beyond the conditions already observed. We introduce CellCanon, the first agentic cellular world model to unify single-cell expression prediction, evidence-grounded explanation, and observation-driven updating. Its predictive core reuses condition-level biological evidence across gene-specific numerical readouts to guide single-cell expression generation. A shared world state links predictions, acquired measurements, and source-linked claims, supporting explanation and revision. On 339 held-out SciPlex3 conditions across three cell lines, CellCanon improves differential-expression AUPRC and Macro-F1 over the best baseline for each metric by 63.3% and 17.3%, respectively, and direction Macro-F1 by 7.2%. Relative to gene-wise reasoning on matched drug-cell cohorts, measured language-model token use falls by 99.77% for Predict and 98.41% for Explain. On the source-grounded benchmark, Explain correctly answers all answerable questions with supporting proofs and identifies all insufficient-evidence cases. In simulated experimental feedback, Update uses one measured source context per drug to exceed the best fine-tuned baselines in differential-expression AUPRC and Macro-F1 without changing model weights. Together, these capabilities support a cumulative account of cellular responses, with predictions and biological judgments that can be revised as evidence accumulates.

## 5. Rethinking One Gene, One Token: Transcriptome-Aware Tokenization for Single-Cell Foundation Models

- Authors: Jiaqi Xiong, Jiaying Li, Yu Zheng, Xiang Zhou, Ziteng Wang, Xinting Hu, Jiaxin Qi
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-21
- DOI: Unavailable
- Categories: q-bio.GN
- Relevance: 3.2184811706589045
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.05410v1
- PDF: https://arxiv.org/pdf/2611.05410v1
- Local PDF: pdf/2026-11-06_05_Rethinking One Gene, One Token_ Transcriptome-Aware Tokenization for Single-Cell Foundation Models.pdf

Single-cell foundation models typically treat each gene as a token, which is both costly and wasteful. A cell can express thousands of genes, so one token per gene makes self-attention expensive, yet many of these genes are detected at low levels and carry too little signal to deserve a token of their own. Genes that are expressed together could instead share a token, leaving separate tokens for genes that stand out. We introduce scTAT (Transcriptome-Aware Tokenization), which pairs a gene-set vocabulary with a per-cell tokenizer. The vocabulary holds overlapping gene sets that recur with stable relative expression across the pretraining corpus. Using these sets raises two difficulties. First, which genes should share a token depends on the cell, whereas existing multi-gene tokens fix the grouping in advance. Second, gene sets of different sizes must be compared with single genes on a common scale. The tokenizer therefore decides per cell, letting gene sets and single genes compete for token positions under an expression score normalized by the square root of set size. Training still reconstructs individual genes, so predictions stay at gene resolution. In frozen-embedding cell-type annotation, scTAT matches the strongest one-gene-per-token model with half the token budget. Its advantage over one-gene-per-token models at the same budget grows as the budget shrinks and the tokenizer assigns more positions to gene sets. Encoding the same genes with gene-set tokens also nearly halves the Transformer's matrix-multiplication cost. These results show that a token need not hold exactly one gene: when the tokenizer decides per cell which genes share a token, a fixed budget covers more of each transcriptome at no cost in annotation accuracy.

## 6. ModalSearcher: Weaving Visual Evidence into Autonomous Cross-Modal Deep Search

- Authors: Zhihan Yin, Ruyi Li, Chengyu Fang, Yifeng Yao, Nonghai Zhang, Pengfei Xiong, Terry Zhang, Huishuai Zhang, Dongyan Zhao
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-04
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 3.0992565484873777
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.06131v1
- PDF: https://arxiv.org/pdf/2611.06131v1
- Local PDF: pdf/2026-11-06_06_ModalSearcher_ Weaving Visual Evidence into Autonomous Cross-Modal Deep Search.pdf

Static and incomplete parametric knowledge limits the performance of multimodal large language models on novel-knowledge and knowledge-intensive tasks, especially those requiring multi-hop evidence acquisition. Existing multimodal agentic search methods often fix visual evidence at the input or a predefined trajectory position, making it difficult for agents to select search modalities as their information needs evolve and to handle complex real-world queries. We define this capability as autonomous cross-modal search: an agent chooses among direct reasoning, text-to-text search, text-to-image search, and reverse-image search, actively introduces visual evidence when appropriate, and switches between and integrates modalities across multiple hops. We propose ModalSearch-Pipeline, a scalable procedure for constructing an interleaved multimodal knowledge graph. It samples paths with diverse depths and modality compositions and uses backward question construction to obscure entity names and image targets that would expose reasoning shortcuts while retaining necessary disambiguating clues, yielding text-only, image-initialized, and arbitrarily interleaved multi-hop problems. We train the ModalSearcher Agent with supervised fine-tuning and reinforcement learning in a live Web environment, and construct ModalSearch-Bench. Experiments show that ModalSearcher-8B improves average accuracy by 16.2 points over Qwen3-VL-8B under the same agentic workflow across five multimodal knowledge-intensive QA benchmarks, with consistent gains on independently constructed active visual-search benchmarks.

## 7. ArcRAG: Agentic Compositional Retrieval over Knowledge Graphs

- Authors: Jyotin Goel, Abhinav Arun, Tejas Prakash Agarwal, Bhaskarjit Sarmah, Stefano Pasquali
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-04
- DOI: Unavailable
- Categories: cs.CL, cs.AI, cs.IR
- Relevance: 3.0972632247422585
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.06481v1
- PDF: https://arxiv.org/pdf/2611.06481v1
- Local PDF: pdf/2026-11-06_07_ArcRAG_ Agentic Compositional Retrieval over Knowledge Graphs.pdf

Graph-based retrieval-augmented generation (GraphRAG) answers questions by retrieving over a knowledge graph built from a corpus. Yet retrieval strategies are designed around the structure their own construction pipeline produces, and whether they survive a change of construction is rarely tested. We study this cross-construction portability: whether one retrieval procedure, with no construction-specific schema, relation names, or retuning, stays effective when the graph is built differently. We introduce ArcRAG, which induces a query-local graph interface at inference time (the node labels, relation descriptors, and property keys reachable from the entities a question names), plans multi-hop traversals against it, and executes and repairs them as Cypher. We build each of the MuSiQue, HotpotQA, and TriviaQA corpora as a schema-guided graph (typed nodes, a closed relation set, source provenance) and as an open-information-extraction graph (untyped nodes, free-text relations), with the retriever's configuration fixed across them. We compare against a construction-agnostic Direct-Cypher agent, ablate each stage across retry and pass budgets on both graph families, and compare with results reported for prior GraphRAG systems, most of which design retrieval together with their own graph construction. Across the two constructions, we find that retrieval need not be co-designed with the graph: query-time interface induction keeps a construction-agnostic retriever effective when the construction changes, although construction still shapes absolute accuracy.

## 8. Split-KV: Efficient Context Parallelism for Training Diffusion Drafters

- Authors: Geng Zhang, Fangzhao Zhang, Cong Xie, Tiantian Fan, Yang You
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-04
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 3.056144187884784
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.05926v1
- PDF: https://arxiv.org/pdf/2611.05926v1
- Local PDF: pdf/2026-11-06_08_Split-KV_ Efficient Context Parallelism for Training Diffusion Drafters.pdf

Diffusion drafters accelerate speculative decoding by denoising multiple draft tokens in parallel. Their training uses anchor sampling to construct compact draft queries and performs cross-attention with a block-sparse mask over a much longer context. We empirically show that acceptance length remains stable as context scales with a fixed query budget, while increasing the query budget yields diminishing quality gains, jointly establishing a practical regime with queries far shorter than the context. No existing context parallelism (CP) method jointly exploits this query--context asymmetry and meets the nonlinear, sample-dependent load-balancing requirement created by anchor sampling. We present Split-KV, an exact CP method that keeps key/value shards local and limits per-layer attention communication to query-sized tensors, making this communication independent of context length. Its global query view further enables a cost-aware longest-processing-time-first (LPT) strategy that balances context key/value chunks by their realized attention cost. At a CP size of 64, Split-KV retains 85--91\% weak-scaling efficiency and achieves up to $3.67\times$ speedup over the fastest available CP baseline. LPT achieves $<$1\% imbalance and plans three orders of magnitude faster than the best load-balancing baseline. Code is available at https://github.com/zxgx/verl.

## 9. Data-Efficient Scaling-Law Discovery for Recommendation Systems via Coupled Hyperparameter Scaling

- Authors: John Martabano Landy, Louis C. Tiao, Yao Xuan, Luc Kien Hang, Rupinder P. Khandpur, Arvind M. Vepa, Srinidhi Raghavendran, Anirudh Agrawal, Xiaoyi Leo Liu, Jiang Liu, Peggy Yao, Alireza Vahdatpour, Djordje Gligorijevic
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-03
- DOI: Unavailable
- Categories: cs.LG, cs.IR
- Relevance: 3.052004168997382
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.05643v1
- PDF: https://arxiv.org/pdf/2611.05643v1
- Local PDF: pdf/2026-11-06_09_Data-Efficient Scaling-Law Discovery for Recommendation Systems via Coupled Hyperparameter Scaling.pdf

Large-scale ranking and recommendation models of Web platforms benefit from increased compute much as large language models do, and their scaling behavior is broadly power-law in form. Yet ranking models have heterogeneous architectures which makes their scaling law less straightforward than that of LLMs. We address how to discover the scaling law of an arbitrary ranking model efficiently. We introduce a scaling layer, which groups primitive architecture parameters into semantically coherent groups and defines how they co-vary, inducing a mapping from a low-dimensional space of hyper-hyperparameters into the full architecture space. On top of it, Axia fits scaling-informed surrogates, selects configurations by a posterior-based acquisition criterion, and returns a Pareto frontier from which per-model operating points are validated -- replacing exhaustive sweeps with a small number of informative runs. A fleet-level evaluation protocol, computed on a fixed representative model set under matched trial budgets, makes refinements to either component measurable. Our contribution is an automated system that learns model-specific complexity-quality relationships and gives uncertainty-aware guidance for allocating compute across a heterogeneous model ecosystem. Across 34 model iterations in two development cycles on Meta's ads ranking and retrieval system, the workflow yielded a mean 0.66% offline normalized-entropy improvement and 0.36% cumulative online lift.

## 10. Intra-Architecture Source Attribution for Stable Diffusion: A New Task with Benchmark Dataset and Baseline

- Authors: Ashutosh Dayal, Mallika Garg, Debashis Sen
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-04
- DOI: Unavailable
- Categories: cs.CV, cs.AI
- Relevance: 3.051829797174544
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.06000v1
- PDF: https://arxiv.org/pdf/2611.06000v1
- Local PDF: pdf/2026-11-06_10_Intra-Architecture Source Attribution for Stable Diffusion_ A New Task with Benchmark Dataset and Baseline.pdf

Designing systems that attribute a generated image to its source model has lately become a major area of AI research. Most existing datasets and systems related to image source attribution are targeted towards the detection of architectural signatures of the source models. Distinct from this, focusing on stable diffusion, we introduce a novel task, IntrAA-SD, Intra-Architecture source Attribution for Stable Diffusion, where the source models to be differentiated share the same architectural backbone and differ only due to fine-tuning. The proposed task aligns with the emergence of fine-tuned generators having the same architecture, like Juggernaut XL and RealVis XL, which are fine-tuned versions of Stable Diffusion XL (SDXL). We provide a first-of-its-kind $140$K-image benchmark dataset containing images generated from different fine-tunes of SDXL, along with in-domain and out-of-distribution prompts. We also provide a baseline framework for IntrAA-SD, which leverages a style-conditioned Mixture-of-Experts network. It uses a frozen CLIP backbone to capture the image style and gate the MoE, which processes fine-tuned trace features from a high-resolution LoRA-adapted DINOv2 network. The fine-tuned models used, the prompting strategies considered, and the formation details employed in the novel dataset are elaborated. Our baseline intra-architecture source attribution method is evaluated in terms of attribution accuracy on our dataset, and ablation studies are also performed. Code and dataset is available at https://github.com/mallikagarg/IntrAA-SD.

## 11. Multimodal Fusion Methods for Whole-Slide Images and Clinical Data in Inflammatory Bowel Disease

- Authors: Ankana Banerjee, Mark van der Giezen, Ole Gunnar Aasprong, Emiel A. M. Janssen, Øyvind Steinsbø, Tore Grimstad, Kjersti Engan
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-03
- DOI: Unavailable
- Categories: cs.CV, cs.AI, cs.LG
- Relevance: 3.038292841731378
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.05579v1
- PDF: https://arxiv.org/pdf/2611.05579v1
- Local PDF: pdf/2026-11-06_11_Multimodal Fusion Methods for Whole-Slide Images and Clinical Data in Inflammatory Bowel Disease.pdf

Multimodal AI fusion of histology and clinical data is an active research area in computational pathology, but fusion methods are rarely compared under identical conditions and across different clinical endpoints. We present a modular framework in which slide-level embeddings, obtained by training an attention-based aggregator over patch embeddings from a frozen foundation model, and per-visit clinical embeddings are fed into 15 interchangeable fusion methods with a shared output dimension and prediction head (except decision-level methods). Using a prospective cohort of newly diagnosed inflammatory bowel disease patients, we predicted STRIDE-II-aligned remission outcomes from baseline or follow-up visits. The best fusion method reached macro-F1 of 0.57-0.75, outperforming both single-modality models in four of six scenarios, and differed by outcome and input. Image reliance, the drop in balanced accuracy when the slide embedding is removed, tended to follow the remission type - highest for histological and lowest for endoscopic remission; methods with similar accuracy relied on the slide to very different degrees.

## 12. Graph Foundation Models Can Become Effective Multivariate Time Series Anomaly Detectors

- Authors: Zhuangyan Hu, Zhuoxuan Liang, Wei Li, Xiaohua Jia, Moustafa Youssef, Sumi Helal
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-04
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.012289890160771
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.06441v1
- PDF: https://arxiv.org/pdf/2611.06441v1
- Local PDF: pdf/2026-11-06_12_Graph Foundation Models Can Become Effective Multivariate Time Series Anomaly Detectors.pdf

Multivariate time series anomaly detection (MTSAD) relies on modeling both temporal dynamics and inter-sensor dependencies to identify complex system faults. Although graph-based detectors explicitly model sensor topologies, they train task-specific networks from scratch on limited target-domain data, remaining vulnerable to spurious correlations and unable to reuse transferable priors. While pretrained Graph Foundation Models (GFMs) offer transferable topological priors and anomaly discriminability, directly adapting them to MTSAD is hindered by cross-modal feature-topology mismatch, unreliable pseudo-anomaly supervision, and decision distortion during node-to-window aggregation. To fill these gaps, we propose a novel adaptation framework, Gfm4Mtsad, which unleashes pretrained GFMs for MTSAD. We introduce the Structure-and-Information Contract Alignment (SICA) module to bridge continuous time series and the pretrained GFM space. This module harmonizes principal subspace token projection, normal-prior-guided graph construction, and residual recovery to suppress spurious edges while retaining fine-grained temporal details. We propose a Mechanism-Aligned Pseudo-Anomaly Screening strategy (MAPS) to steer unsupervised learning. It applies localized dependency breaks while preserving empirical residuals, selecting hard negatives near the normal boundary for targeted supervision. We develop a Tail-Gated Evidence Calibration mechanism (TGEC) to eliminate node-to-window aggregation distortion. It calibrates multi-granular graph responses against normal operational references, strictly preserving benign score rankings while selectively refining extreme anomaly candidates in the tail distribution for reliable window detection and interpretable sensor evidence. Extensive evaluations with two GFM backbones demonstrate that Gfm4Mtsad achieves superior detection performance over existing baselines.

## 13. Recasting Visual Language Models as EEG Foundation Models for Clinical Neurodiagnostics

- Authors: Xin Zhou, Elena Sergeeva, Nan Bi, Wenyu Song, Lijun Yin, Hao Deng
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-03
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.0048502731694215
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.05538v1
- PDF: https://arxiv.org/pdf/2611.05538v1
- Local PDF: pdf/2026-11-06_13_Recasting Visual Language Models as EEG Foundation Models for Clinical Neurodiagnostics.pdf

Historically automated electroencephalography (EEG) systems was done using task-specific supervised models trained on purposely annotated data. A more recent modeling paradigm relies on creating a unified representation, or a 'foundation model', for multiple modality-specific tasks through large-scale domain-specific pretraining on the unannotated EEG signal. The quality of this unified representation directly depends on the availability of the modality-specific datasets. At the same time, generalist Vision Language Models (VLMs) exhibit broad few-shot learning capacities as well as good fine-tuning adaptability to different visual and language tasks. Can VLMs learn how to read and interpret EEG visually, emulating to a degree the way human clinicians inspect the EEG patterns? In this work we make a case that they can: we show that generalist VLMs without large-scale EEG pretraining perform competitively across a collection of clinical neuro-diagnostic tasks, can adapt to different tasks in a few-shot learning setting better than specialist foundation models, and exhibit better performance with model scaling when modality-specific models fail to exhibit.

## 14. On the Design of Hyper-Connections: Simplification, Stability, and Scalability

- Authors: Xiangdong Zhang, Xiaohan Qin, Sunan Zou, Tuo Dai, Bizhao Shi, Zhuo Xia, Yebin Yang, Yizhou Chen, Yuliang Liu, Yu Cheng, Junchi Yan
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-04
- DOI: Unavailable
- Categories: cs.LG, cs.CL
- Relevance: 3.004713328595141
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.05984v1
- PDF: https://arxiv.org/pdf/2611.05984v1
- Local PDF: pdf/2026-11-06_14_On the Design of Hyper-Connections_ Simplification, Stability, and Scalability.pdf

Hyper-Connections (HC) architectures are increasingly adopted in frontier language models, yet their components remain insufficiently understood and introduce non-negligible training overhead. In this work, we systematically study the HC architecture to understand its components and identify simpler, more efficient designs. We find that learned read/write gating without mixing and unconstrained mixing with fixed gates form two effective interaction groups: either alone achieves performance comparable to mHC. We also identify repeated access to the expanded residual state as a major source of training overhead, even without mixing. These findings lead to SimpleHC, which simplifies the architecture by removing residual mixing and simplifies execution through shared memory access, using the resulting additive structure and shared gate inputs. Layer-specific gates share a group-entry state, enabling batched reads and deferred writes; scalar corrections exactly preserve preceding sublayer output contributions. Our analyses support both the retained residual structure and the design of shared memory access. SimpleHC incurs only 2.4% extra end-to-end training time over a vanilla residual baseline at the largest tested scale. It maintains performance comparable to mHC when scaling from 15B to 30B MoE models, exhibits smoother gradient dynamics during standard training, and remains stable under stress. We hope SimpleHC will encourage a broader pursuit of simplicity in foundation model design, making performance gains more accessible and practical at scale.

## 15. Editing Large Language Models with Geometry-Aware Regularization

- Authors: Bingqing Liu, Wei Liu, Jun Wang, Xiaobo Sun, Yuhua Li, Ruixuan Li
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-04
- DOI: Unavailable
- Categories: cs.CL, cs.AI
- Relevance: 2.985285960165982
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.06185v1
- PDF: https://arxiv.org/pdf/2611.06185v1
- Local PDF: pdf/2026-11-06_15_Editing Large Language Models with Geometry-Aware Regularization.pdf

Knowledge editing has become a key technique for updating knowledge in large language models. However, existing methods neglect the geometric structure of the knowledge representation space, leading to two key limitations: they cannot distinguish which pre-trained knowledge should be preferentially preserved (core vs. non-core) nor which new edits are inherently difficult (hard vs. easy). To address this, we propose GEdit, a geometry-aware framework built on a Low-Rank Plus Diagonal (LR+D) factor model that captures the intrinsic low-rank structure of Transformer FFN hidden representations. GEdit features two complementary mechanisms. First, the low-rank regularization applies targeted protection on a low-rank core knowledge subspace. Second, the adaptive regularization dynamically adjusts the regularization strength based on each edit request's editability: relaxing constraints for hard edits to ensure success, and tightening them for easy edits to better preserve pretrained knowledge. Extensive experiments on GPT2-XL, GPT-J, and LLaMA-3-8B under large-scale editing scenarios, including both mini-batch and fully sequential editing settings with up to 10,000 continuous updates, show that GEdit consistently and significantly outperforms state-of-the-art baselines in both editing success and knowledge preservation.

## 16. Constraint-Preserving Flow Matching for Spectral Graph Generation

- Authors: Anita Yang, Ken-ichi Kawarabayashi, Yohan Jung
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-03
- DOI: Unavailable
- Categories: cs.LG, cs.AI
- Relevance: 2.960419673184536
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.05436v1
- PDF: https://arxiv.org/pdf/2611.05436v1
- Local PDF: pdf/2026-11-06_16_Constraint-Preserving Flow Matching for Spectral Graph Generation.pdf

Spectral graph generation models graphs through the eigenvalues and eigenvectors of their Laplacians, providing a compact and continuous alternative to direct graph construction. However, these eigensystems must retain the structural properties of graph Laplacians. Existing approaches preserve eigenvector orthonormality but do not enforce the Laplacian nullspace constraint, potentially producing eigensystems inconsistent with Laplacian structure. To address this, we introduce Laplacian-Constrained Stiefel Flow Matching (LaSFM), which preserves the nullspace condition alongside eigenvector orthonormality and positive eigenvalues during generation. We characterize the underlying constrained Stiefel manifold and formulate flow matching on it. We further extend LaSFM to property-guided generation, steering samples toward desired graph properties while maintaining these constraints. Experiments demonstrate improved performance on both spectral and graph-level metrics, along with better alignment with target properties.

## 17. Objective-Conditioned Active Preference Learning for Multi-Objective Alignment

- Authors: Duc Anh Vu, Thong Nguyen, Hoang Pham, Ponhvoan Srey, Luu Anh Tuan
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-03
- DOI: Unavailable
- Categories: cs.LG, cs.AI
- Relevance: 2.9055573484160515
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.05506v1
- PDF: https://arxiv.org/pdf/2611.05506v1
- Local PDF: pdf/2026-11-06_17_Objective-Conditioned Active Preference Learning for Multi-Objective Alignment.pdf

Aligning large language models (LLMs) with several objectives, such as helpfulness, harmlessness, and honesty, typically relies on preference judgment for each objective, growing the annotation cost linearly with the number of objectives. Active preference learning can reduce this cost by selecting the comparisons whose labels are expected to change the policy most. Existing remedies either lack an objective-aware query selection mechanism for the multi-objective setting or regard conflicting preferences as harmful, therefore excluding them from the training data. We introduce OGC-DPO (Objective-conditioned Gradient Coverage DPO), an active learning framework that treats each (response pair, objective) combination as a separate query and measures its informativeness through the policy's own implicit gradient, without relying on an external reward model. OGC-DPO then selects the queries that most expand each objective's gradient coverage. Empirical experiments across varying numbers of objectives demonstrate the effectiveness of OGC-DPO over existing active preference learning methods under the same annotation cost. Further analysis demonstrates that informative conflicts, rather than being uniformly harmful, provide a useful policy training signal.

## 18. FlyHash for LLM Agent Memory: An Empirical Validation and a New Application

- Authors: Mohan Bheemadolu, Chrisogonas O. Odhiambo
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-04
- DOI: Unavailable
- Categories: cs.AI, cs.LG
- Relevance: 2.897855682515763
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.05791v1
- PDF: https://arxiv.org/pdf/2611.05791v1
- Local PDF: pdf/2026-11-06_18_FlyHash for LLM Agent Memory_ An Empirical Validation and a New Application.pdf

Large language model (LLM) agents increasingly rely on external memory stores to retain information across conversations, typically via dense vector embeddings searched with approximate nearest-neighbor methods. The fruit fly's olfactory circuit computes a locality-sensitive hash of sensory input using a strikingly different mechanism - sparse random projection followed by winner-take-all competition - and prior work (Dasgupta et al., 2017) showed this scheme, dubbed FlyHash, preserves neighbor structure better per bit than conventional random-hyperplane hashing (SimHash) on several benchmarks. We apply FlyHash, to our knowledge for the first time, to LLM agent memory retrieval, and ask three questions a practitioner actually needs answered: does the quality advantage hold under a correctly matched-bit protocol (it does, robustly, across 10 seeds and four datasets spanning two modalities, with one specific, previously undocumented comparison pitfall identified and corrected along the way); does that advantage translate into real memory and latency savings, including against the dense-vector indexing (HNSW) practitioners default to today (no: at equal bits FlyHash's codes are larger and slower to compare than SimHash's, and HNSW dominates both hash methods at ordinary scale; a sparse-set comparison we introduce recovers most but not all of a naive latency gap, leaving hashing's practical case narrower and more specific than the quality result alone implies); and does the advantage survive genuine, non-circular agent-memory relevance labels rather than the nearest-neighbor-by-embedding proxy this literature otherwise relies on (it does). We report all three answers precisely, including the two that narrow rather than flatter the headline result, and release our implementation, a working agent-memory demo, and a full account of the methodological pitfalls we found and corrected.

## 19. Learning Noise Optimization for Reward Alignment in Few-Step Generative Models

- Authors: Hongeun Kim, Jeongsol Kim, Jong Chul Ye
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-04
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 2.880190534620714
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.06255v1
- PDF: https://arxiv.org/pdf/2611.06255v1
- Local PDF: pdf/2026-11-06_19_Learning Noise Optimization for Reward Alignment in Few-Step Generative Models.pdf

Reward alignment for diffusion- and flow-based generative models is often formulated over stochastic trajectories, making it less suitable for few-step deterministic generators. Initial noise optimization provides a trajectory-free alternative, but existing gradient-free methods require costly per-sample search at inference. We introduce LeNO (Learning Noise Optimization), which amortizes reward-guided initial noise optimization into a learned residual transport while keeping the pretrained generator frozen. LeNO learns an anchor-conditioned distribution over noise corrections using Local GRPO and scalar rewards, eliminating iterative test-time optimization. For Gaussian initial noise with norm-preserving projection, we derive a tractable upper bound on the KL divergence between the corrected noise distribution and the original prior, providing a principled regularization objective. We evaluate LeNO on few-step text-to-image and protein structure generation, including expensive black-box designability rewards. Across both domains, LeNO improves target rewards with a single noise correction at inference while largely preserving generation quality and diversity.

## 20. A Training-Free Socket for DNA in Frozen Language Models

- Authors: Arash Fatehi
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-16
- DOI: Unavailable
- Categories: q-bio.GN, cs.AI
- Relevance: 2.8746305779191763
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.05401v1
- PDF: https://arxiv.org/pdf/2611.05401v1
- Local PDF: pdf/2026-11-06_20_A Training-Free Socket for DNA in Frozen Language Models.pdf

Connecting a DNA foundation model to a large language model (LLM) usually requires training a connector, and often the LLM too. We show that a closed-form map is enough for gene-level questions. Our method, the socket, fits one ridge regression (the plug) from frozen Evo 2 features to the host LLM's own representation of the gene's symbol, name, and description at an early layer. The plug's output replaces the hidden state at placeholder positions, and no gradient passes through the host.
  We test it on GeneHop, a five-way multiple-choice benchmark split by homology. In a single run on the held-out test set, under a frozen analysis plan, real DNA beats shuffled DNA on all four hosts: by +22.2 points [19.8, 25.0] on Qwen3.5-4B, +26.1 [24.3, 27.9] on Qwen3.6-27B, +16.7 [14.2, 19.7] on Mistral-7B, and +18.4 [16.2, 21.0] on OLMo-2-7B. All four survive Holm correction, every null control stays within two points of the sham level, and the development results agree within 2.3 points.
  A layer rule that uses no task items was selected on three hosts; it predicted the working layer of the fourth before any DNA-plug scoring on it. A text-only linear map lets one plug feed any other host, at a cost of at most 0.9 points on test. The socket conveys gene identity: nearest-neighbour retrieval recovers 72-84% of the effect, but the plug beats it on every host by 3.0-5.2 points and keeps most of its effect without training homologs.

## 21. LIBRA: Programmatic Induction of Executable Tool Libraries

- Authors: Zekai Li, Zhenke Liu, Yonghao Li, Junhan Liu, Xulong Xiao, Jiapeng Zhang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-03
- DOI: Unavailable
- Categories: cs.SE, cs.AI, cs.IR
- Relevance: 2.8720449184737418
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.05445v1
- PDF: https://arxiv.org/pdf/2611.05445v1
- Local PDF: pdf/2026-11-06_21_LIBRA_ Programmatic Induction of Executable Tool Libraries.pdf

Large language model agents increasingly retrieve tools from large catalogs, yet most retrievers rank each tool independently by request similarity. For multi tool tasks, this recovers the goal matching tool while omitting prerequisite tools required by the workflow.We introduce LIBRA, a framework for Library Induction by Runtime Assembly that turns a flat tool catalog into an executable tool library. An LLM proposes per tool contracts of candidate invocations, reusable outputs and state changes, and success conditions; LIBRA then tests these compositions in a sandbox and retains the relations supported at runtime. Constructed before user queries, the library requires no dependency annotations, tool use trajectories, or task specific training, and supports both one-shot and agentic retrieval. On AppWorld, BFCL, and SciToolEval, LIBRA improves one-shot Recall and NDCG over the same dense retriever by 7.9 and 3.7 percentage points on average. Within ToolReAGt, it yields corresponding gains of 4.5 and 2.9 points after ten retrieval iterations.

## 22. Morpheus.AI: agents autonomously generate, execute and refine virtual tissue models

- Authors: Prerana Chandratre, Anjali Sharma, Justin Bürger Michaelis, Diego Jahn, Jörn Starruß, Lutz Brusch, Simon Syga
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-29
- DOI: Unavailable
- Categories: q-bio.QM, q-bio.CB, q-bio.TO
- Relevance: 2.8566665611041397
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.05413v1
- PDF: https://arxiv.org/pdf/2611.05413v1
- Local PDF: pdf/2026-11-06_22_Morpheus.AI_ agents autonomously generate, execute and refine virtual tissue models.pdf

Virtual tissue models link observations to mechanistic hypotheses, but building them demands expertise in biology, mathematics and programming. Here, large language model (LLM) agents paired with the simulator Morpheus (Morpheus.AI) autonomously built such models from fifteen benchmark studies, five without a published model. With a frontier LLM, agents that ran their simulations met 83-86% of study-specific criteria in under two hours and for under US\$4 per model. Such agents could make in silico modeling routine.

## 23. Neural Stochastic Forecasting for Lateral Molecular Diffusion Simulations

- Authors: Jacob Ede Levine, Mario Hidalgo-Soria, Chen Yun Wen, Yun Lyna Luo, Sai Chandra Kosaraju
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-04
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 2.845408346893529
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.06157v1
- PDF: https://arxiv.org/pdf/2611.06157v1
- Local PDF: pdf/2026-11-06_23_Neural Stochastic Forecasting for Lateral Molecular Diffusion Simulations.pdf

Predicting the long-time diffusion of membrane proteins is challenging because molecular dynamics (MD) simulations are computationally expensive, while experimental single-particle tracking is often limited by finite observation times. Here, we introduce a neural stochastic (NS) model for forecasting the collective diffusion of membrane proteins from coarse-grained MD trajectories. The model combines a transformer-based representation of protein configurations, recurrent networks operating at multiple temporal scales, and a stochastic latent process with learned memory. A cross-attention decoder then generates correlated protein displacements while accounting for the instantaneous system geometry and periodic boundary conditions. We evaluate the model in two membrane systems: seven interacting PIEZO channels and a mixed system containing seven PIEZO and ten TREK channels. For the seven PIEZO system, the NS model reproduces the anomalous diffusion exponent measured in MD simulations $α\sim 1$, substantially improving on a previously developed variational autoregressive model that exhibits superdiffusive behavior. The model also generates trajectories extending to 40,000 frames and captures the distinct diffusion characteristics of PIEZO and TREK populations in the mixed system. Comparisons of time-averaged mean-square displacements, Van Hove displacement distributions, and non-Gaussian parameters show that the model preserves key statistical features of the simulated dynamics. These results establish neural stochastic modeling as a promising approach for generating long trajectories of multi-protein membrane diffusion and extending the statistical analysis of molecular dynamics simulations.

## 24. Understanding the Out-of-Distribution Generalization of Chain-of-Thought Reasoning in LLMs

- Authors: Nuo-Jing Liang, Xiao-Tong Yuan, Pan Zhou
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-04
- DOI: Unavailable
- Categories: cs.LG, stat.ML
- Relevance: 2.7401454401661822
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.06438v1
- PDF: https://arxiv.org/pdf/2611.06438v1
- Local PDF: pdf/2026-11-06_24_Understanding the Out-of-Distribution Generalization of Chain-of-Thought Reasoning in LLMs.pdf

Chain-of-Thought (CoT) reasoning substantially improves Large Language Models (LLMs), yet its out-of-distribution (OOD) generalization mechanism remains theoretically underexplored. We study CoT as compositional OOD generalization: the target task lacks complete reasoning trajectories or direct input-output pairs, while training provides only in-distribution (ID) atomic step data. We show that CoT generalizes by repeatedly applying a shared single-step predictor to compose reusable ID transitions. Theoretically, let $T$ denote the number of reasoning steps in the target task, $n$ the number of training samples per sub-task, and $k$ the number of output tokens per step; then the OOD task risk is controlled by the sum of the ID sub-task risks, scaled by a coefficient of order $\mathcal{O}(k)$ that is independent of $T$, although the summed risk itself may still grow with $T$. A Rademacher-complexity analysis further shows that the estimation term is of order $\mathcal{O}(\sqrt{T/n})$, rather than linear in $T$, due to predictor sharing under a uniform capacity control on the shared class. For autoregressive Next-Token Prediction, the final-task risk is bounded by the best-in-class step-level risk scaled by the same coefficient of order $\mathcal{O}(k)$, plus an estimation term of order $\widetilde{\mathcal{O}}\big(k\sqrt{T/n}\big)$. A parity-coupled construction further shows that, for the sub-task empirical risk minimizer, the expected final-task risk is at least the best in-class risk plus $Ω(\sqrt{T/n})$ when $T\le n$. Experiments on Atom-Task and GSM8K support the theory: CoT enables short-to-long and compositional generalization, while explicit state tracking is crucial.
  Our code is available at https://github.com/maxliang114514/CoT-OOD.

## 25. Agentic intelligent data engine for scientific large language models

- Authors: Shufang Xie, Zequn Liu, Pan Deng, Renqian Luo, Yingce Xia, Tao Qin, Rui Yan
- Source: openalex
- Venue type: journal
- Journal: Nature Communications
- Publication status: published
- Publication date: 2026-11-04
- DOI: https://doi.org/10.1038/s41467-026-78887-x
- Categories: Machine Learning in Materials Science, Research Data Management Practices, Scientific Computing and Data Management
- Relevance: 2.7299411641048597
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://doi.org/10.1038/s41467-026-78887-x
- PDF: Unavailable
- Local PDF: Not downloaded

Artificial intelligence is reshaping scientific discovery across diverse fields. Yet scientific AI remains constrained by data curation, which demands substantial manual effort and deep domain expertise, creating major cost and scalability barriers. Here we present the Agentic Intelligent Data Engine (AIDE), a multi-agent framework that automates data curation for scientific AI. AIDE collects, selects, and organizes data in three stages, providing an end-to-end pipeline that turns a data request into training-ready datasets. We benchmarked AIDE on 14 tasks across biomedical and chemical domains. Scientific AI models built with AIDE-curated datasets matched or outperformed those built with manually curated data, and AIDE’s fully automated preparation delivered significant gains in efficiency and data utilization without compromising quality. These findings provide consistent evidence of AIDE’s applicability across scientific domains and usage paradigms and demonstrate its potential to accelerate scientific AI development and democratize access to scientific AI. Here, authors develop AIDE, a multiagent framework that automates scientific data curation, and demonstrate across biomedical and chemical tasks that its automatically curated datasets can match or outperform manually curated data while improving efficiency.

## 26. Exploring the Privacy--Size Tradeoff for Differentially Private Self-Attentive Variational Autoencoders

- Authors: Rohit Sadavarte, Dhruvi Kothari, Sparsh Gupta, Eric Van Oeveren
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-03
- DOI: Unavailable
- Categories: cs.LG, cs.CE, cs.CR
- Relevance: 2.7284066949121986
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.05582v1
- PDF: https://arxiv.org/pdf/2611.05582v1
- Local PDF: pdf/2026-11-06_26_Exploring the Privacy--Size Tradeoff for Differentially Private Self-Attentive Variational Autoencoders.pdf

Data tends to be most useful when it is shared, and the data most worth sharing is often the data that privacy obligations restrict. Synthetic data from a generator trained under differential privacy (DP) is one way to reconcile the two, but its utility depends on the privacy budget $\varepsilon$ and on how much data the generator sees - a parameter that most data sharing applications of synthetic data control. We present SAVANT, a self-attentive variational autoencoder for tabular data trained with DP-SGD that, to our knowledge, is the first to combine attention, a VAE, and DP in one tabular model. We evaluate it against two marginal mechanisms, PrivBayes and MST, jointly over the privacy budget and the dataset size on two public datasets, measuring the utility a downstream classifier loses by training on synthetic rather than real data. We find that, under the same DP guarantee, more data generally means more utility. For the marginal mechanisms it absorbs most of what a strict budget costs, and a noise-scaling argument suggests DP-SGD exchanges data fo budget at a worse rate. Two independent membership-inference attacks, judged against a measured null, found no aggregate membership signal.

## 27. CHARM+: Cross-Hardware Attention with Re-Merge Multistream Mechanism

- Authors: Xinhang Zhang, Boning Zhang, Chengchun Liu, Chunpu Li, Lei Sun, Weifeng Zhang, Limin Xiao
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-04
- DOI: Unavailable
- Categories: cs.AI, cs.AR, cs.DC
- Relevance: 2.721097580806941
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.05906v1
- PDF: https://arxiv.org/pdf/2611.05906v1
- Local PDF: pdf/2026-11-06_27_CHARM+_ Cross-Hardware Attention with Re-Merge Multistream Mechanism.pdf

As sequence lengths continue to grow, distributed attention based on sequence parallel (e.g., Ring-Attention) has become a mainstream solution for large language models (LLMs). Nevertheless, inherent communication dependencies limit computation-communication overlap, reducing GPU utilization. Moreover, in cross-hardware (NUMA or node) architectures, due to imbalanced communication bandwidth, frequent communication synchronization will limit overall performance. Based on these insights, we propose CHARM+, Cross-Hardware Attention with Re-Merge Multistream Mechanism. We reorganize sequential communications into several levels and achieve intra-level parallelism and computation overlap. Furthermore, we decouple cross-hardware communication from intra-hardware communication, eliminating synchronization overhead caused by bandwidth imbalance. Forward and backward algorithms were evaluated on multiple hardware architectures and consistently outperformed state-of-the-art methods. Compared to Ring-Attention, our forward and backward algorithms achieve average speedups of 1.3x and 1.7x on a dual-NUMA PCIe architecture, and 2.8x and 2.9x on a dual-node NVLink architecture, respectively.

## 28. Give the Drafter a Second Chance to Guess: Parallel Reconsideration for Speculative Decoding

- Authors: Hoang Anh Duy Le, Huibing Dong, Alireza Khadem, Ziteng Sun, Xiang Song, Yizheng Huang, Soroush Radpour, Anshumali Shrivastava, Ye He
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-03
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 2.7172168465862656
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.05724v1
- PDF: https://arxiv.org/pdf/2611.05724v1
- Local PDF: pdf/2026-11-06_28_Give the Drafter a Second Chance to Guess_ Parallel Reconsideration for Speculative Decoding.pdf

Speculative decoding accelerates large language model inference with a small drafter, whose per-guess acceptance rate determines the achievable speedup. Feature-level drafters share a design choice: every token, easy or hard, is drafted under a single forward pass. Many of the tokens the target rejects are ones the drafter is itself unsure about yet the target answers decisively. To address this, we introduce Parallel Reconsideration: guided by its own uncertainty, the drafter reconsiders its hesitant guesses with extra passes that run in parallel with the one-pass draft, adding negligible latency. A co-designed training recipe and serving-time drafting algorithm append these reconsidered guesses to the original draft tree as refined candidates. Across models and benchmarks, on average, Parallel Reconsideration improves over the baselines by 5.3% to 10.2% on acceptance length and by 3.5% to 9.2% on speedup.

## 29. Analysis of Local Open-Weight LLM Agents on Vulnerability-Reproduction Tasks

- Authors: Jorge García-Carrasco, Javier Sanchis, Álvaro Navarro, Alejandro Maté, Juan Trujillo
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-04
- DOI: Unavailable
- Categories: cs.CR, cs.LG, cs.SE
- Relevance: 2.71630830354861
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.06257v1
- PDF: https://arxiv.org/pdf/2611.06257v1
- Local PDF: pdf/2026-11-06_29_Analysis of Local Open-Weight LLM Agents on Vulnerability-Reproduction Tasks.pdf

Open-weight language models that fit on a single consumer GPU are becoming capable on a growing range of tasks, and they matter because they can run locally without sending the code to a hosted service. Vulnerability reproduction, turning a vulnerability description into an input that crashes the vulnerable build, is a natural target for them, since it is an automated analysis task closer to test generation than to code comprehension and it runs against a build that must be executed rather than read. In order to assess whether current models can perform it, we evaluate twelve configurations of local models, spanning three generations, two architectures and three quantization levels, on ten CyberGym vulnerability-reproduction tasks, three runs each under one harness, and release the full artefact. We show that every configuration, down to the 4B model, solves most of the six easier tasks, and configurations separate only on the remaining four. For the harder tasks, the 27B model is required. Quantization did not change what the models solved in any matched pair, but it changed how fast they got there, and the mixture of experts reached the same scores in less wall clock. We also examine the agent trajectories. Almost every run we examined, including those that fail, names the vulnerable function and states the correct hypothesis, and what separates a solved task from an unsolved one is whether that hypothesis becomes a working input.

## 30. D3D: Decoupled Diffusion Drafting for Asynchronous Speculative Decoding

- Authors: Baoyou Chen, Ruiqiao Mei, Guancong Lin, Tao Song, Weihao Yuan, Qun Liu, Siyu Zhu
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-04
- DOI: Unavailable
- Categories: cs.AI, cs.LG
- Relevance: 2.6951224869053227
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.06425v1
- PDF: https://arxiv.org/pdf/2611.06425v1
- Local PDF: pdf/2026-11-06_30_D3D_ Decoupled Diffusion Drafting for Asynchronous Speculative Decoding.pdf

Target-conditioned diffusion drafters predict candidate tokens in parallel, yet each new block must wait for updated target-model hidden states. This forces drafting and verification to run sequentially, limiting speedup even though each block is generated in one pass. We introduce D3D, a standalone diffusion drafter that removes this inter-round dependency. D3D combines blockwise denoising with auxiliary autoregressive supervision to achieve long accepted prefixes without target hidden states. This independence lets D3D draft successor blocks during verification in one packed pass, enabling asynchronous speculative decoding. We progressively prune layers according to their effect on acceptance length to reduce the cost of packed drafting. Removing five of 36 layers retains over 99\% of mean acceptance length across three benchmarks with Qwen3-8B as the target. Across seven benchmarks, D3D averages 5.00$\times$ and 5.71$\times$ decoding speedup with Qwen3-8B and Qwen3-32B targets, compared with 4.03$\times$ and 3.67$\times$ for DFlash. On GSM8K with Qwen3-32B, speedup reaches 7.48$\times$. Code is publicly available at https://github.com/fudan-generative-vision/D3D.
