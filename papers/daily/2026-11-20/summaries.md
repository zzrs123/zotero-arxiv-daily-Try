# Paper Daily Reading - 2026-11-20

## 1. SCOPE: Single-Cell Omics Prediction from Histology via RNA-Protein Prior Enhancement

- Authors: Leyang Tao, Xuan Gong, Luyuan Xie, Arjun Beniwal, Yuqi Tan, Kun-Hsing Yu
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-18
- DOI: Unavailable
- Categories: cs.CV, q-bio.GN
- Relevance: 3.525091636526324
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.24104v1
- PDF: https://arxiv.org/pdf/2611.24104v1
- Local PDF: pdf/2026-11-20_01_SCOPE_ Single-Cell Omics Prediction from Histology via RNA-Protein Prior Enhancement.pdf

Predicting the RNA and protein content of cells from routine H&E images could extend spatial molecular profiling to existing slide archives. However, both H&E-spatial proteomics and H&E-spatial transcriptomics paired datasets are limited by the number of available markers and the insufficient availability of high-quality, cell-resolved data. We present SCOPE (Single-Cell Omics Prediction via RNA-protein prior Enhancement), a unified framework that leverages biologically complementary information between RNA and proteins to address the limited availability of single-omics supervision. Our key insight is that, although RNA and proteins represent distinct molecular modalities, their biological relationships provide valuable shared knowledge that can benefit single-omics prediction tasks. To this end, SCOPE introduces biologically informed biomarker priors to enhance shared gene-level representations, enabling knowledge transfer across RNA and protein modalities through gene-protein correspondence and molecular associations. By exploiting these complementary relationships, SCOPE enables both prediction tasks to benefit from a shared backbone enriched with cross-omics biological knowledge. Furthermore, its biomarker correlation design facilitates the prediction of unseen markers, extending spatially resolved molecular profiling beyond directly supervised targets. Across test datasets spanning 16 organs, SCOPE improves the average RNA Pearson correlation over the strongest baseline by 8.8%. On two external protein cohorts, it improves the average Pearson correlation over the strongest baseline by 9.7% for seen markers and 11.9% for unseen markers.

## 2. NaviGATE: Noise-Aware Dual-View Generation for Multimodal Knowledge Graph Reasoning

- Authors: Jie Peng, Yongxue Shan, Yongfu Zha, Cui Miao, Xiaodong Wang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-18
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 3.458172109519282
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.24552v1
- PDF: https://arxiv.org/pdf/2611.24552v1
- Local PDF: pdf/2026-11-20_02_NaviGATE_ Noise-Aware Dual-View Generation for Multimodal Knowledge Graph Reasoning.pdf

Multimodal knowledge graph reasoning (MKGR) aims to infer missing facts by jointly exploiting relational structures, textual descriptions, and visual evidence. Existing embedding-based methods effectively capture graph topology, but their fixed multimodal representations are less effective for query-specific fine-grained semantic reasoning, while generation-based methods are vulnerable to noisy retrieval and may produce invalid entities. To address these challenges, we propose NaviGATE, a noise-aware generative framework for MKGR. NaviGATE first aligns graph-derived structural representations with textual semantics, then performs structure-aware internal knowledge activation by fine-tuning the multimodal language model with multimodal entity summaries and injected structural tokens. In the noise-aware dual-view instruction tuning stage, NaviGATE jointly optimizes retrieval-free and retrieval-aware views: reliable retrieved candidates are reinforced through contrastive logit sharpening, while misleading candidates are suppressed through parametric consistency distillation. In inference, structure-constrained decoding restricts generation to valid entities in the target knowledge graph. Experiments on standard benchmarks show that NaviGATE consistently outperforms strong unimodal, multimodal, and generation-based baselines, and remains robust under noisy retrieval scenarios.

## 3. Horizontal Flow Matching for Single-Cell Spatiotemporal Dynamics

- Authors: Zihan Wang, Jianzhe Li, Zhenyi Zhang, Peijie Zhou
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-18
- DOI: Unavailable
- Categories: cs.LG, cs.AI, q-bio.QM
- Relevance: 3.3411002136761274
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.24764v1
- PDF: https://arxiv.org/pdf/2611.24764v1
- Local PDF: pdf/2026-11-20_03_Horizontal Flow Matching for Single-Cell Spatiotemporal Dynamics.pdf

Learning the spatiotemporal dynamics of cells from spatial transcriptomics requires connecting snapshots of different cells acquired in different coordinate frames. A rotation or translation of a section can appear as cell movement and distort the inferred correspondence. We introduce horizontal flow matching, which learns changes in tissue organization, molecular state, and cell abundance up to shared rigid motion. The dynamics follow a continuity--reaction equation whose action assigns no cost to shared rigid motion, and the resulting horizontal projector removes this component from spatial prediction errors during learning and from predicted velocities during generation. An equivalent endpoint problem jointly estimates correspondence and relative pose in Wasserstein--Fisher--Rao geometry and yields analytic paths whose velocity and growth serve as regression targets. Regressing these targets recovers the horizontal dynamics under ideal population conditions. Our model, HORIZON, uses an equivariant transformer to predict velocity and growth from the current tissue, so that a tissue can be generated continuously from a single initial snapshot. On a simulated tissue observed in perturbed coordinate frames, alignment improves reconstruction and projection reduces rigid drift. On four spatial transcriptomics time courses, HORIZON reconstructs tissue geometry, gene expression, and cell abundance more accurately than existing spatial and unbalanced trajectory methods, and interpolates held-out developmental stages.

## 4. MECI: Multi-Element Collaborative Interaction for Multimodal Entity Linking

- Authors: Jie Peng, Yongxue Shan, Yongfu Zha, Xiaodong Wang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-18
- DOI: Unavailable
- Categories: cs.CL, cs.AI
- Relevance: 3.282325057635422
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.24522v1
- PDF: https://arxiv.org/pdf/2611.24522v1
- Local PDF: pdf/2026-11-20_04_MECI_ Multi-Element Collaborative Interaction for Multimodal Entity Linking.pdf

Multimodal Entity Linking (MEL) aims to disambiguate mentions in multimodal contexts by grounding them to specific entities in a knowledge base. A pivotal challenge in MEL is capturing multi-level correspondences: the semantic consistency between mention-entity pairs and the complementary correlations across modalities. However, existing methods often suffer from element dominance due to their reliance on coupled interactions or coarse global aggregations. In response, we propose the Multi-Element Collaborative Interaction (MECI) framework. First, to capture multi-element mention-entity correspondences, we develop a Multi-view Experts Network that leverages a "divide-and-conquer" strategy for decoupled feature learning to mitigate element dominance, supported by a KL-guided routing mechanism that governs expert specialization and collaboration. Furthermore, to model cross-modal complementary correlations, we propose a Hierarchical Multimodal Interaction Module, where a dynamic modality-aware weighting network refines interactions across hierarchical semantic levels, thereby integrating multi-granular evidence to counteract element dominance. Finally, we incorporate a generative semantic refinement stage that utilizes large language models for zero-shot re-ranking. Extensive experiments on WikiDiverse, RichpediaMEL, and WikiMEL show that MECI consistently outperforms state-of-the-art baselines, improving Hits@1 by 1.95%, 7.30%, and 2.31%, respectively.

## 5. TabBioMed: A Large-Scale Benchmark for Biomedical Tabular Learning

- Authors: Pau Mateo-Bernadó, Saivenkata Nagavyjayanthi Polapragada, David Bonet, Pol Arbiol Rakuljic, Laia Mogas Pladevall, Marçal Comajoan Cara, Jesus Gonzalez-Ferrer, Jordi Abante, Daniel Mas Montserrat, David Haussler, Alexander G. Ioannidis
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-18
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.212945494966486
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.23779v1
- PDF: https://arxiv.org/pdf/2611.23779v1
- Local PDF: pdf/2026-11-20_05_TabBioMed_ A Large-Scale Benchmark for Biomedical Tabular Learning.pdf

Recent advances in machine learning have accelerated biomedical prediction, but evaluation on structured biomedical data remains fragmented, especially for datasets with high dimensionality, large sample size, missingness, and class imbalance. We introduce TabBioMed, a large-scale benchmark of 94 curated public biomedical tabular datasets spanning electronic health records, drug discovery, genomics, transcriptomics, proteomics, metabolomics, single-cell omics, and systems biology. TabBioMed unifies these datasets through a standardized, dataset-aware preprocessing and evaluation framework, enabling reproducible comparison across classification, regression, and multi-target tasks. We benchmark 23 models across classical baselines, gradient-boosted trees, neural tabular architectures, and tabular foundation models. Foundation models deliver the strongest family-level predictive performance. However, their gains are regime-dependent: tree-based models and tuned multilayer perceptrons remain highly competitive, often dominating under inference-time or training-cost constraints. Overall, TabBioMed shows that biomedical tabular learning is strongly context-dependent, with optimal model choice depending on data regime, task type, and computational budget. We release TabBioMed with curated datasets and splits, preprocessing code, baselines, and results, providing a reproducible benchmark for practical model selection and future methods development in biomedical machine learning, available at https://github.com/AI-sandbox/TabBioMed.

## 6. NOTREKS: Marginal Independence in Score-based Structure Learning

- Authors: Fabian Bleile, Sarah Lumpp, Mathias Drton
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-18
- DOI: Unavailable
- Categories: stat.ML, cs.LG, stat.ME
- Relevance: 3.2040498618411144
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.24015v1
- PDF: https://arxiv.org/pdf/2611.24015v1
- Local PDF: pdf/2026-11-20_06_NOTREKS_ Marginal Independence in Score-based Structure Learning.pdf

Score-based structure learning estimates causal graphs by optimizing a data-dependent objective over structural equation models. We study how prior knowledge that selected pairs of variables are marginally independent can be incorporated into such causal discovery methods. Under faithfulness, marginally independent pairs cannot be connected by a trek, so the knowledge becomes a graphical no-trek constraint, which we call NOTREKS information. We introduce a power-series trek (PSTrek) penalty for gradient-based optimization and a trek constraint for order-based search, and we analyze why such information helps in finite samples and how it restricts the search space. Our numerical experiments illustrate to what extent NOTREKS information helps in causal discovery. In particular, using synthetic benchmarks with oracle NOTREKS information, we show that these constraints can improve both structural recovery and adjustment-based effect identification.

## 7. The Elephant in the Question: Unified Models Picture the Concepts Behind Their Answers

- Authors: Tobias Braun, Marcus Rohrbach, Lorenzo Cavallaro
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-18
- DOI: Unavailable
- Categories: cs.CV, cs.CL, cs.LG
- Relevance: 3.1775741214546596
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.24793v1
- PDF: https://arxiv.org/pdf/2611.24793v1
- Local PDF: pdf/2026-11-20_07_The Elephant in the Question_ Unified Models Picture the Concepts Behind Their Answers.pdf

Visualizing intermediate representations could help us inspect the reasoning steps underlying a model output. Unified multimodal models offer this opportunity by combining understanding and generation in one architecture. Their image generators can access representations formed while processing text. We introduce the V-lens, which uses this connection to visualize a chosen token's hidden state without training a decoder. Across four diffusion-based and two purely autoregressive unified models, the resulting images reveal key intermediate concepts that connect a question to its answer even when the concepts are never named explicitly. Controlled tests show how this content changes with context, token position, and depth. We then introduce lens tuning, which supervises selected hidden states with pictures through the V-lens. Across BAGEL, SenseNova-U1, and HunyuanImage-3.0, the rate of correct visualizations of pronoun referents rises from 2-11% to 86-94%. Surprisingly, such visual supervision also improves text answers without supervising the answer tokens directly. Code is available at https://github.com/multimodal-ai-lab/V-lens.

## 8. Dual-Manifold Variational Autoencoders

- Authors: Hongxu Chen, Chun Wang, Yanghao Wang, Hongxiang Li, Zhen Wang, Zhixiang Zhang, Long Chen
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-18
- DOI: Unavailable
- Categories: cs.CV, cs.AI
- Relevance: 3.104103114064455
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.23964v1
- PDF: https://arxiv.org/pdf/2611.23964v1
- Local PDF: pdf/2026-11-20_08_Dual-Manifold Variational Autoencoders.pdf

In latent diffusion models, expanding the latent dimension of variational autoencoders (VAEs) is essential to push the upper bound of reconstruction quality. However, without explicit structural constraints, such unregularized expansion easily yields a rugged and ill-conditioned latent manifold, causing generated latents to drift off the manifold during generation (i.e., off-manifold problem). Recent works smooth this manifold by using external foundation models (e.g., DINOv2) as a topological regularizer. However, we argue that tying the latent space to frozen external priors inherently restricts generalization: bound by their pre-training distributions and semantic biases, they may fail to capture faithful visual details on out-of-distribution domains. Observing that low-dimensional latents naturally form a smoother, generation-friendly manifold, we propose dual-manifold VAE (DM-VAE) to leverage internal representations as a topological regularizer. Specifically, DM-VAE pairs a high-dimensional reconstructive branch with a low-dimensional branch that extracts a clean topological skeleton, anchoring the high-dimensional manifold to this smooth subspace. Building upon this framework, we further introduce topological representation alignment (TRA) to supervise intermediate generator features during training, and internal guidance with topological skeleton (IG_TS) to guide structural components while preserving high-frequency details at inference. On ImageNet-1K (256x256), our foundation-model-free DM-VAE achieves a state-of-the-art rFID of 0.12 and a generation FID50K of 1.28 (w/o CFG) and 1.20 (w/CFG), and further reaches 1.11 when orthogonally combined with DINOv2.

## 9. GenNA: Conditional generation of nucleotide sequences guided by natural language annotations

- Authors: Yi Shen, Guangshuo Cao, Jianghong Wu, Dijun Chen, Cong Feng, Miaona Chen
- Source: openalex
- Venue type: journal
- Journal: Science Advances
- Publication status: published
- Publication date: 2026-11-18
- DOI: https://doi.org/10.1126/sciadv.aej1481
- Categories: Genomics and Phylogenetic Studies, Machine Learning in Bioinformatics, RNA and protein synthesis mechanisms
- Relevance: 3.0847609149287485
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://doi.org/10.1126/sciadv.aej1481
- PDF: Unavailable
- Local PDF: Not downloaded

Deciphering the mapping between biomolecular sequences and complex biological functions is a central challenge in genomics. While existing generative nucleotide models capture sequence distributions, they lack explicit access to gene-associated biological semantics, limiting semantics-guided design. Here, we present GenNA, a generative nucleotide foundation model guided by natural language annotations. Pretrained on a multimodal nucleotide-text corpus spanning 2221 eukaryotic species (∼416 billion characters), GenNA internalizes relationships between sequence syntax and functional semantics within a unified autoregressive framework. Without explicit rule-based supervision, GenNA yields distinguishable perplexity responses to sequence-annotation mismatches, mutational variants, and species-label perturbations. Furthermore, across diverse generation tasks, GenNA produces statistically plausible nucleotide sequences consistent with target semantics, structural constraints, and species contexts. Overall, GenNA provides a versatile framework for controllable nucleotide generation, establishing a practical route to integrate functional descriptions with sequence design.

## 10. KnowledgeClaw: Towards Agentic Knowledge Engineering via Omnimodal Hypergraphs

- Authors: Haoran Luo, Jiapu Wang, Linhao Luo, Luu Anh Tuan
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-18
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 3.0660794404649105
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.24294v1
- PDF: https://arxiv.org/pdf/2611.24294v1
- Local PDF: pdf/2026-11-20_10_KnowledgeClaw_ Towards Agentic Knowledge Engineering via Omnimodal Hypergraphs.pdf

Knowledge engineering (KE) turns raw files into a reasoning-ready knowledge base, a task now within reach of LLM agents. KE has progressed from chunk and graph retrieval-augmented generation (RAG) to memory agents, agentic KE and multimodal KE. However, a live knowledge base needs omnimodality, a closed-loop lifecycle and multi-granular application at once, yet existing systems meet at most two and no benchmark measures all three. We formalize Omnimodal Knowledge Engineering (OmniKE) and release OmniKE-Bench, six tasks with 1,829 model-free items over 3,960 real files in five modalities. We further propose KnowledgeClaw, an agentic system that builds an omnimodal typed hypergraph, keeps it current with a closed-loop lifecycle agent and routes each query to the granularity it needs. Against 30 baselines, it ranks first on all six tasks with an overall OKE of 55.9, +14.6 over the strongest baseline. Our software and data are publicly available at https://github.com/LHRLAB/KnowledgeClaw.

## 11. Training-Free Domain Generation for One-Shot Federated Learning with Server-Side Pre-trained Diffusion Models

- Authors: Yixuan Tong, Yuanguo Bi, Mingjian Zhi, Wenchao Xu, Yuan Wu
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-18
- DOI: Unavailable
- Categories: cs.AI, cs.CV, cs.DC
- Relevance: 3.0018767189168925
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.23908v1
- PDF: https://arxiv.org/pdf/2611.23908v1
- Local PDF: pdf/2026-11-20_11_Training-Free Domain Generation for One-Shot Federated Learning with Server-Side Pre-trained Diffusion Models.pdf

One-shot federated learning (OSFL) has attracted increasing attention for its ability to substantially reduce communication overhead by limiting client-server interaction to a single communication round. Nevertheless, this limited interaction makes learning from heterogeneous client distributions challenging. Diffusion-based OSFL approaches seek to address this challenge by synthesizing data that approximate client distributions. However, existing diffusion-based approaches often impose substantial computational costs on clients and lack effective visual guidance to generate data aligned with client distributions. To address these limitations, we propose FedDoG, a training-free Domain Generation framework that leverages server-side pre-trained diffusion models to synthesize data aligned with client domains. FedDoG extracts compact domain representations using a frozen image encoder, substantially reducing client-side computational and communication costs. These representations are incorporated into the diffusion model through a pre-trained image-conditioning adapter, thereby providing explicit visual guidance for domain generation. To further improve the quality of synthetic data, FedDoG adapts the strength of visual conditioning according to domain concentration and filters generated samples based on class consistency and predictive entropy. Experiments on three benchmarks demonstrate that FedDoG generates higher-quality synthetic images and outperforms existing OSFL baselines in classification accuracy. Meanwhile, FedDoG reduces client upload and computation time by 99.9% and 91.5%, respectively. The code is available at https://github.com/YXTong17/FedDoG.

## 12. Every Query Routes Itself: Accelerating Video Diffusion Transformers with Per-Query Routed Sparse Attention

- Authors: Zhen Huang, Shuwei Li, Ruizhe Yao, Xinrui Chen, Danyi Liu, Haoyuan Liang, Zhiyu Ye, Qiuyan Sun, Bingwei Chen, Yiyuan Li, Xu Zhou, Haohuan Fu
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-18
- DOI: Unavailable
- Categories: cs.CV, cs.LG
- Relevance: 2.918905936221541
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.24479v1
- PDF: https://arxiv.org/pdf/2611.24479v1
- Local PDF: pdf/2026-11-20_12_Every Query Routes Itself_ Accelerating Video Diffusion Transformers with Per-Query Routed Sparse Attention.pdf

Self-attention over long token sequences dominates the inference cost of video diffusion transformers. Clustering-based sparse attention clusters both queries and keys and lets all queries in a cluster share one selection of key clusters. We show that this sharing limits accuracy: with key clusters and density fixed, attention grows more accurate as the query clusters are refined, and is most accurate when each query selects on its own, which needs no query clustering at all. We therefore propose Per-Query Routed Sparse Attention (PQRS), a training-free method that clusters only keys, lets each query select its own key clusters, and compensates for the unselected ones with their centroids. Per-query selections leave no query tile with a shared key list, so PQRS traverses key clusters instead of queries, buckets queries with identical selections into dense tasks, and merges their partial results in one pass under a fixed softmax offset carried from the previous denoising step. On four text-to-video and image-to-video models from the Wan and HunyuanVideo families, PQRS is the fastest of all the sparse attention methods we evaluate and the closest to the dense output, reaching $28.9$ dB PSNR on Wan2.1-T2V and $35.4$ dB on HunyuanVideo at $1.66$--$2.10\times$ end-to-end speedup.

## 13. Clover-35B-A3B-Preview Technical Report

- Authors: DiffuSpace Technical Team
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-18
- DOI: Unavailable
- Categories: cs.CL, cs.AI, cs.LG
- Relevance: 2.9132401837866677
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.24636v1
- PDF: https://arxiv.org/pdf/2611.24636v1
- Local PDF: pdf/2026-11-20_13_Clover-35B-A3B-Preview Technical Report.pdf

We introduce Clover-35B-A3B-Preview (Clover), a mixture-of-experts diffusion language model with 35 billion total parameters and 3 billion activated parameters, supporting thinking-mode generation. Clover adapts Gated Delta Networks to block diffusion by combining recurrent memory of previously generated context with bidirectional softmax attention inside the current block. Historical memory readout competes with current-block tokens in a shared softmax, with learnable block-size calibration and a separate, zero-initialized right-context convolution branch. Clover leads the seven evaluated agent metrics, including 73.6 on SWE-bench Verified and 51.7 on Terminal-Bench 2.1. On internal agent workloads, it reaches a reported generation speed of 680 tokens/s using one NVIDIA GB300 GPU at BF16 precision and batch size one. We organize the evaluation around model quality, drafting and verification costs, and deployment under constrained memory. We also describe a decision-model variant that generates answers to related questions in one denoising pass. On an internal set of 500 groups, joint prediction raises question accuracy from 90.37% to 93.88% and all-correct group accuracy from 65.4% to 77.0%.

## 14. Variable Length Diffuse Everything: Arbitrary Length Generative Modeling on Arbitrary State Spaces

- Authors: Kevin Rojas, Felix X. -F. Ye, Molei Tao
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-18
- DOI: Unavailable
- Categories: cs.LG, stat.ML
- Relevance: 2.908145272603675
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.23684v1
- PDF: https://arxiv.org/pdf/2611.23684v1
- Local PDF: pdf/2026-11-20_14_Variable Length Diffuse Everything_ Arbitrary Length Generative Modeling on Arbitrary State Spaces.pdf

Diffusion and flow-based generative models have achieved remarkable results across diverse applications, but most assume data of fixed-dimension/length. Meanwhile, real-world problems such as layout generation often involve variable-length, multimodal data, such as continuous bounding box coordinates paired with discrete types. Existing methods typically address variable length by padding data to a fixed size or by introducing specialized objectives to model lengths explicitly, adding complexity and limiting generality. We propose Variable Length Diffuse Everything (VL-DE), a simple and general framework for variable-length multimodal generation on arbitrary state spaces. Instead of padding, VL-DE handles variable length through an insertion-based mechanism grounded in a principled theoretical framework, yielding a tractable training objective. In addition, by utilizing the fact that VL-DE is based on a generator with an additive form, we develop a higher-order sampler by appropriately handling the time dependence. Extensive experiments on layout and molecule generation demonstrate the effectiveness of our approach.

## 15. Searching the Pareto Front: Multi-Objective Retrieval for Heterogeneous Scientific Modalities

- Authors: Song Young Oh, Nesar Ramachandra, Bin Xia, Ian Foster, Kyle Chard
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-18
- DOI: Unavailable
- Categories: cs.AI, astro-ph.IM
- Relevance: 2.8681146035549254
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.23639v1
- PDF: https://arxiv.org/pdf/2611.23639v1
- Local PDF: pdf/2026-11-20_15_Searching the Pareto Front_ Multi-Objective Retrieval for Heterogeneous Scientific Modalities.pdf

In cosmology, surveys span different sky regions and wavelength ranges, resulting in uneven modality coverage across observational datasets. Such heterogeneity can be addressed through either multimodal foundation models (FMs), which learn shared embedding spaces, or independently learned modality embeddings combined via late fusion. We investigate whether the latter provides an adaptive alternative to FM-based scientific retrieval. We evaluate this approach on a galaxy retrieval task spanning diverse modalities--history of star formation, spectra of light emitted, and multi-wavelength observations from two telescopes--comparing an FM baseline with separately trained embeddings fused through multi-objective optimization based on Pareto optimality. We find that the FM baseline achieves strong embedding-space proximity, but our method preserves modality-specific distance structure that allows scientists to inspect which physical signals drive similarity. Our method also achieves improved fidelity in raw-data space: across six measured properties, its nearest neighbor is 8% closer to the query on average than that retrieved by kNN in the FM embedding space (spread 0.128 vs. 0.139). These results suggest that multi-objective retrieval can surface astrophysically coherent candidates that single-objective search alone may overlook.

## 16. OpenGNS: An Open Dataset of the Gradient Noise Scale across Vision, Language, and Diffusion Models

- Authors: Marcel Aach, Jiangtao Wang, Stefan Kesselheim, Andreas Lintermann
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-18
- DOI: Unavailable
- Categories: cs.LG, cs.DC
- Relevance: 2.863498875816223
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.24331v1
- PDF: https://arxiv.org/pdf/2611.24331v1
- Local PDF: pdf/2026-11-20_16_OpenGNS_ An Open Dataset of the Gradient Noise Scale across Vision, Language, and Diffusion Models.pdf

The Gradient Noise Scale (GNS) metric measures the signal-to-noise ratio of gradients in stochastic gradient descent and, as shown by McCandlish et al. (2018), can be used to approximate the Critical Batch Size (CBS) during neural network training. Despite its appearance in technical reports of frontier models, no open dataset of GNS measurements across modern architectures exists, limiting systematic study of the metric. We close this gap by releasing OpenGNS, a dataset of more than 400 GNS measurement trajectories spanning three domains: image classification with ResNets, autoregressive language modeling with Generative Pre-trained Transformers (GPTs), and image synthesis with Diffusion Transformers (DiTs), covering models from 11M to 1B parameters trained under Maximal Update Parameterization (muP) with dense batch-size and learning-rate sweeps. Building on this dataset, we study how the GNS depends on hyperparameters, scale, and training progress, and how it relates to the CBS. We find that the GNS behaves as a consistent "temperature of training", remaining stable across model sizes under muP at equivalent loss, and our results suggest task-dependent biases in its relation to the CBS: a tendency to overestimate the CBS for classification and to underestimate it for generative tasks, consistent in direction across common CBS definitions. The dataset is available at https://huggingface.co/datasets/olympique-marcel/OpenGNS

## 17. Fill-Distance-Guided Active Learning for Causal Function Recovery under Network Interference

- Authors: Peiyao Liu, Hongtao Zhu, Sizhe Zhang, Yang Su, Zhenyu Zhao, Nan Chen
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-18
- DOI: Unavailable
- Categories: stat.ME, cs.LG
- Relevance: 2.8536412090938468
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.24143v1
- PDF: https://arxiv.org/pdf/2611.24143v1
- Local PDF: pdf/2026-11-20_17_Fill-Distance-Guided Active Learning for Causal Function Recovery under Network Interference.pdf

Causal inference seeks to learn how outcomes change under alternative interventions, but network interactions complicate this task. Under network interference, outcomes depend on both own treatment and neighbors' treatments, making causal effects functions of neighborhood exposure rather than single treatment contrasts. Existing methods primarily target prespecified causal contrasts or their estimation precision, leaving global response-function recovery largely unexplored. We study sequential experimentation under a limited experimental budget, with the goal of recovering the full exposure-dependent population-average response function. To this end, we propose FANCI (Fill-Distance-Guided Active Learning for Network-Interference Causal Inference). For function learning, treatment-specific Gaussian processes flexibly model nonlinear conditional response surfaces. For experimental design, we formulate global response-function recovery as a coverage problem and propose a fill-distance criterion that guides new experiments toward poorly covered regions. To account for network constraints on attainable exposure patterns, we develop full-network and target-screened strategies for selecting feasible network--assignment pairs. Theoretically, we derive uniform error bounds linking fill distance to response-function estimation and characterize the approximation loss from target screening. Simulations and an online-game experiment show that FANCI improves recovery of nonlinear exposure-dependent effects and reveals treatment patterns obscured when network interference is ignored.

## 18. Incremental Roseland: Batch-wise Landmark Diffusion via Kernelized Sequential Karhunen--Loève Update

- Authors: Jeanie Schreiber
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-17
- DOI: Unavailable
- Categories: cs.LG, math.FA, math.NA
- Relevance: 2.844095678387486
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.23414v1
- PDF: https://arxiv.org/pdf/2611.23414v1
- Local PDF: pdf/2026-11-20_18_Incremental Roseland_ Batch-wise Landmark Diffusion via Kernelized Sequential Karhunen--Loève Update.pdf

Landmark diffusion (Roseland) computes a diffusion-map-style spectral embedding from the singular value decomposition of a degree-normalized data-to-landmark kernel matrix, at a cost far below that of full diffusion maps. It assumes, however, that all data are available at once. We introduce incremental Roseland (iRoseland), which casts the landmark affinity as a row-growing matrix whose SVD can be updated with a kernelized Sequential Karhunen--Loève (SKL) scheme. Degre correction is handled by a first order expansion about a reference mean kernel row and so that the landmark-side eigenbasis may be recovered from a single landmark-by-landmark eigendecomposition at each step. The presented method requires only a single pass over the data and runs in bounded-memory with state independent of the number of points processed. A forgetting factor lets the method track drifting distributions, and a sample-size-invariant embedding keeps outputs comparable across time. Experiments show agreement with Roseland to round-off on stationary data, and accuracy that exceeds equal-memory Roseland by an order of magnitude on long streams. On drifting data, we observe large gains from forgetting with a window matched to the drift.

## 19. Same Rank, Different Needs: Rethinking LoRA Redistribution in Federated Learning

- Authors: Jinqian Chen, Jihua Zhu, Chang Liu
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-18
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 2.842926007374778
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.23742v1
- PDF: https://arxiv.org/pdf/2611.23742v1
- Local PDF: pdf/2026-11-20_19_Same Rank, Different Needs_ Rethinking LoRA Redistribution in Federated Learning.pdf

Federated low-rank adaptation (LoRA) enables clients with different resource budgets to collaboratively fine-tune foundation models. To distribute an aggregated update within each client's rank budget, existing methods commonly retain its leading singular directions. However, directions that best reconstruct the update matrix need not best preserve its responses on a particular client's inputs: a lower-energy direction may matter more to that recipient. We formalize this mismatch and show that matrix-optimal truncation can incur arbitrarily larger response error than another readout of the same rank. Motivated by this result, we propose Receiver-Aware Subspace Adaptation (RASA), a plug-in framework for receiver-aware knowledge transfer. RASA uses compact diagonal input second moments to perform uncentered PCA of receiver-weighted update responses. The resulting readout is globally optimal for the rank-constrained receiver objective and preserves at least as much response energy as spectral truncation under the diagonal metric. RASA also introduces spectral-reference aggregation, which removes the personalized initialization offset while retaining the locally learned increment. Experiments on DomainNet-100, NICO++, GLUE, and SuperNI demonstrate RASA's effectiveness across methods under resource, task, and data heterogeneity. In particular, RASA improves DomainNet-100 accuracy by 3.23 percentage points with FlexLoRA and achieves gains of up to 8.33 ROUGE-L points on seen SuperNI tasks and 4.37 on unseen tasks with modest overhead.

## 20. Error Analysis of Deep Learning

- Authors: Yuling Jiao, Peiying Wu, Jerry Zhijian Yang, Pingwen Zhang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-15
- DOI: Unavailable
- Categories: math.NA, cs.LG
- Relevance: 2.838281312245038
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.23321v1
- PDF: https://arxiv.org/pdf/2611.23321v1
- Local PDF: pdf/2026-11-20_20_Error Analysis of Deep Learning.pdf

This review examines deep learning theory through the lens of error decomposition, systematically addressing approximation, statistical, and optimization errors. We trace the development of error analyses from bounds on individual error components to frameworks that account for all three. Using nonparametric regression and the Deep Ritz Method as dual running examples, we demonstrate how these analyses apply across fundamentally different loss structures. We then review representative analyses in scientific machine learning, generative learning, reinforcement learning, representation learning, and large language models, showing how learning errors affect solutions, distributions, and predictions through problem-specific arguments. Throughout, we clarify which error components are controlled, how they are combined, and what assumptions are needed to obtain guarantees for trained networks.

## 21. ReliFlow: Reliability-Calibrated Residual Transport for Combinatorial Single-Cell Perturbation Prediction

- Authors: Jinrui David, Yun Peng
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-18
- DOI: Unavailable
- Categories: stat.ML, cs.AI, cs.LG
- Relevance: 2.81555458174239
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.23999v1
- PDF: https://arxiv.org/pdf/2611.23999v1
- Local PDF: pdf/2026-11-20_21_ReliFlow_ Reliability-Calibrated Residual Transport for Combinatorial Single-Cell Perturbation Prediction.pdf

Predicting the transcriptional response to combined perturbations requires distinguishing interactions between interventions from errors in their individual effect estimates. The latter become more pronounced when single-perturbation evidence is sparse or withheld. We introduce a conditional flow-matching model that estimates the reliability of single-gene effects from training-only cross-fitting and uses those estimates to calibrate the additive source distribution. The velocity is decomposed into a known correction of the additive reference and a learned residual transport field. On Norman genetic perturbations, reduces mean absolute error (MAE) from 0.142 to 0.131 for unseen combinations of observed singles and from 0.198 to 0.178 when constituent singles are withheld. On held-out ComboSciPlex drug combinations, MAE decreases from 0.191 to 0.176. Non-additive residual correlation improves from 0.574 to 0.638, and component ablations identify the contribution of reliability weighting. The results indicate that accounting for uncertain constituent effects improves generalization to unseen genetic and chemical combinations, with a moderate increase in training cost.

## 22. Elysium: Simulation-Free Unbalanced Schrödinger Bridges

- Authors: Zihan Wang, Jianzhe Li, Zhenyi Zhang, Peijie Zhou
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-18
- DOI: Unavailable
- Categories: cs.LG, cs.AI, q-bio.QM
- Relevance: 2.8065122592307237
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.24763v1
- PDF: https://arxiv.org/pdf/2611.24763v1
- Local PDF: pdf/2026-11-20_22_Elysium_ Simulation-Free Unbalanced Schrödinger Bridges.pdf

Reconstructing cellular dynamics from snapshots is challenging because the destructive nature of single-cell measurements makes tracking the same cells over time impossible. Cellular dynamics are inherently stochastic and involve changes in population size through proliferation and apoptosis. Growth-based methods represent population change as a rate on the density, which does not assign exits and entries to individual cells. Unbalanced Schrödinger bridges model individual events, but neural solvers for killed diffusion bridges simulate trajectories during training. We introduce Elysium, a simulation-free solver that jointly learns state transition and mass change. Using a killed Brownian reference and its time reversal, Elysium constructs direct regression objectives from an optimal endpoint coupling and conditional bridge distributions, without simulating trajectories during training. We show that the minimizers of the expected training objectives recover the optimal unbalanced Schrödinger bridge. Empirically, Elysium reconstructs state transitions, population size, and event distributions on simulated benchmarks with known killed-diffusion ground truth, outperforming existing deterministic and bridge-based solvers. On single-cell time courses, it interpolates cell state distributions at unobserved time points, tracks population expansion and contraction, and captures biphasic drug-response dynamics.

## 23. ViLFlow: Parallel Vision-Language Generation with Continuous Latent Flows

- Authors: Kevin Zhai, Bian Sun, Zhenyi Wang, Song Wang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-18
- DOI: Unavailable
- Categories: cs.CV, cs.LG
- Relevance: 2.7780820673799784
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.24240v1
- PDF: https://arxiv.org/pdf/2611.24240v1
- Local PDF: pdf/2026-11-20_23_ViLFlow_ Parallel Vision-Language Generation with Continuous Latent Flows.pdf

Vision-language generation has predominantly relied on autoregressive and discrete diffusion models. Autoregressive models generate tokens sequentially, while discrete diffusion models typically predict tokens independently within each denoising step. We propose ViLFlow (Vision-Language Flow), a continuous-flow vision-language model that combines joint modeling of output embeddings with parallel token decoding. ViLFlow adapts pretrained continuous language generation to visual question answering and image captioning through learned image guidance and prediction-aware token decoding. A visually adapted teacher provides image-guided predictions as additional denoising supervision. The denoiser learns to reproduce these predictions directly, retaining one image-conditioned prediction per generation step. We train the token decoder on denoiser predictions and paired reference text to improve the conversion of continuous outputs into words. The decoder can be adapted independently, improving answering and captioning without further denoiser training. For captioning, it also supplies text feedback during late denoising, allowing decoded words to inform subsequent refinement. ViLFlow outperforms autoregressive and masked-diffusion baselines by up to 8.46 percentage points on VQAv2 and 4.50 points on GQA without GQA training. On COCO Karpathy test, it improves CIDEr by 16.25 over masked diffusion and 17.81 over sampled autoregression.

## 24. NullTok: empirical-null token selection for training-free long video understanding

- Authors: Zhang Ziyue, Juwei Jian, Baiyang Song, Yunshan Zhong, Jun Peng, Yiyi Zhou, Rongrong Ji
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-18
- DOI: Unavailable
- Categories: cs.CV, cs.AI
- Relevance: 2.7779202546586483
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.23881v1
- PDF: https://arxiv.org/pdf/2611.23881v1
- Local PDF: pdf/2026-11-20_24_NullTok_ empirical-null token selection for training-free long video understanding.pdf

Long video understanding remains a daunting challenge for existing multimodal large language models (MLLMs), mainly due to the large number of visual tokens accumulated in long videos. Currently, frame selection and token selection are two main paradigms for addressing this issue, both aiming to select relevant visual information to form a compact input for MLLMs. A natural approach combines these two paradigms by selecting frames before pruning tokens, but noisy frame-level relevance estimates can cause irreversible evidence loss. In this paper, we study this problem from the perspective of assessing the spatiotemporal distribution of query-specific evidence and propose a novel and training-free approach termed NULLTOK. For every patch across all frames, we construct an empirical-null distribution from 64 group-matched irrelevant control queries, capturing the scores expected in the absence of target-specific evidence. Target affinities are calibrated against these same-position references into right-tail Monte Carlo p-values, which are discrete super-uniform under a conditional exchangeability assumption. Calibrated screening and a high-recall semantic guard produce candidate tokens for deterministic visual deduplication and joint spatiotemporal budget allocation. To validate NullTok, we apply it to two representative MLLMs and conduct extensive experiments on a set of video benchmarks. The experimental results demonstrate its effectiveness under a bounded visual token budget. For example, it achieves 65.81% and 68.85% on Video-MME using frozen LLaVA-Video-7B and Qwen3-VL-8B backbones, respectively, at a cap of 64 full-frame equivalents (FFE), without subtitles or audio. These results outperform all evaluated baselines on Video-MME under the same budget for both backbones. Code is available at https://github.com/potato-kitty/NullTok.

## 25. Can LLMs Understand What They Predict? Evaluating Latent Causal Structure Inference in Financial Markets

- Authors: Yixiang Zheng, Yuechen Jiang, Zhiwei Liu, Jimin Huang, Yuyan Wang, Sophia Ananiadou
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-17
- DOI: Unavailable
- Categories: cs.CL, cs.LG
- Relevance: 2.776489330940639
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.23533v1
- PDF: https://arxiv.org/pdf/2611.23533v1
- Local PDF: pdf/2026-11-20_25_Can LLMs Understand What They Predict_ Evaluating Latent Causal Structure Inference in Financial Markets.pdf

Large language models (LLMs) are increasingly evaluated through their ability to predict future outcomes, implicitly assuming that predictive success reflects an understanding of the underlying system. However, accurate predictions can often be achieved without recovering the latent mechanisms that generate observable outcomes. To examine this assumption, we introduce LUCID, a benchmark that evaluates whether models can infer latent market structures from event descriptions and historical financial observations. Models generate event-induced causal graphs representing inferred market structure and are evaluated through a reconstruction-based framework. Our evaluation of 6 open-weight and proprietary LLMs shows that adding their generated graphs generally reduces reconstruction quality compared with using historical observations alone, although a few metrics improve. These findings suggest that inferring informative, event-specific market structures from observable evidence remains challenging for the evaluated LLMs.

## 26. SpecLook: Speculating Where to Look for Fast and Reliable Agentic MLLMs

- Authors: Xi Ding, Jiawei Zhang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-17
- DOI: Unavailable
- Categories: cs.AI, cs.CL, cs.CV, cs.LG
- Relevance: 2.77014440400126
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.23483v1
- PDF: https://arxiv.org/pdf/2611.23483v1
- Local PDF: pdf/2026-11-20_26_SpecLook_ Speculating Where to Look for Fast and Reliable Agentic MLLMs.pdf

Agentic multimodal large language models (MLLMs) that think with images interleave reasoning with zoom-in tool calls. However, this sequential loop is slow, and its answers carry no reliability score. Prior speculation of tokens, reasoning steps, or answers keeps the loop, and answer speculation also accepts confident errors. We find that the loop mostly adds one zoom-in step, with which a small model is ahead of the agent on most splits. Our key insight is to speculate the agent's next observation, which, unlike a drafted answer, can be verified, corrected, and used to test the answer. We propose SpecLook, a training-free speculate-and-verify framework with three levels. A small model drafts a glimpse and re-answers from it, and the question ends if the answer is unchanged and confident. Otherwise, the agent's large model verifies and corrects the glimpse without tools, and their answers are fused. Only questions that still lack evidence reach the agent, in one forward pass that SpecLook-Fast skips, so no question runs the loop. The trace scores every answer's reliability without labels. Extensive experiments on V*, HR-Bench, and POPE show that both are more accurate than every baseline on every split. SpecLook reaches 87.2% and 86.2% mean accuracy with 7.7x and 4.7x speedups over the DeepEyes-7B and Thyme-RL agents, and SpecLook-Fast reaches 9.9x and 6.3x.

## 27. Thinking Fast, Anywhere: One System-1 for the Decision Points of Any Agent Workflow

- Authors: Rui Li, Liyang He, Zheng Zhang, Zhenya Huang, Qi Liu
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-18
- DOI: Unavailable
- Categories: cs.AI, cs.CL, cs.LG
- Relevance: 2.7514522748831878
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.23751v1
- PDF: https://arxiv.org/pdf/2611.23751v1
- Local PDF: pdf/2026-11-20_27_Thinking Fast, Anywhere_ One System-1 for the Decision Points of Any Agent Workflow.pdf

Autonomous LLM agents incur substantial cost and latency by invoking a large model (System-2) at every step, even when many intermediate actions choose among a small set of known candidates. Existing dual-system agents offload such decisions to a lightweight System-1 model, but rely on workflow-specific hooks authored per environment. We present AnyS1, a framework that turns human-authored procedural skills, whose instructions naturally specify where choices arise and which options apply, into a shared, domain-general source of decision points. Offline, AnyS1 mines grounded enumerable decisions across over 1,000 public skills, gathers execution-grounded trajectory states inside isolated containers to construct Any-DP, and trains a single calibrated 4B pointer System-1 with label smoothing. At run time, compiled workflows resolve routine decisions in one forward pass and fall back to System-2 when confidence falls below a calibrated threshold. Across three unseen benchmarks and distinct System-2 model families, AnyS1 preserves task reliability while cutting episode cost by 75-91% and model-call time by 63-92% relative to an uncompiled System-2 agent, and maintains performance under zero-shot threshold transfer.

## 28. KnowMe Paper Radar: Lightweight Discovery of Promising Papers in the Age of Autoresearch

- Authors: Zhuo Chen, Jian Wang, Jinjie Gu, Lijun Wu
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-18
- DOI: Unavailable
- Categories: cs.AI, cs.IR
- Relevance: 2.745679493466135
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.23702v1
- PDF: https://arxiv.org/pdf/2611.23702v1
- Local PDF: pdf/2026-11-20_28_KnowMe Paper Radar_ Lightweight Discovery of Promising Papers in the Age of Autoresearch.pdf

The growing volume of topically similar papers makes it difficult to identify new work that can offer useful research insights or methodological guidance. We present KnowMe Paper Radar, a lightweight discovery tool that combines multiple sources of evidence into personalized reading priorities. Users specify topics, priorities, exclusions and dates; the system brings together topical relevance, recency, author research histories, collaboration paths and direction-specific institutional context. By exposing each score component and its supporting sources, KnowMe helps readers select promising papers for their current questions and discover relevant work beyond familiar authors. Automatic acquisition, version merging and graph-cache reuse keep this workflow convenient without large language model (LLM) inference during ordinary use. Experiments on 174,640 acquired records show more than threefold faster repeated context preparation, while cached abstracts improve normalized discounted cumulative gain at rank 10 (NDCG@10) from 0.412 to 0.598 on expert-judged retrieval tasks. Complementary analyses examine how the same accumulated records support semantic retrieval, research-history modeling and literature-grounded planning. A browser interface and a structured command-line interface (CLI) make these capabilities available to both researchers and research agents, positioning KnowMe as a practical upstream tool for literature-informed recursive self-improvement (RSI) workflows.

## 29. ARISE: Practical Self-Evolving Memory for Accurate and Cost-Efficient Enterprise Agents

- Authors: Jiangyun Zhang, Zhou Tang, Kristen Surrao, Zhiyu Chen, Albert Guan, Tor Nitayanont, Yupei Zhang, Roopali Singh, Yunkai Xiao, Shreya Pandit, Julia Huang, Shayan Ali Akbar, Erwin Cornejo, Yuan Li, Yi Zhang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-17
- DOI: Unavailable
- Categories: cs.AI, cs.MA
- Relevance: 2.7240679249570716
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.23588v1
- PDF: https://arxiv.org/pdf/2611.23588v1
- Local PDF: pdf/2026-11-20_29_ARISE_ Practical Self-Evolving Memory for Accurate and Cost-Efficient Enterprise Agents.pdf

Enterprise LLM agents operate in dynamic environments where foundation models evolve rapidly, workflows update frequently, and deployments need to satisfy accuracy and cost requirements. We propose ARISE (Agent Refinement through Iterative Self-Evaluation), a practical memory architecture in which the agent's memory evolves from its own failures without updating model weights, tools, or workflow logic. ARISE uses the model itself or a teacher model to attribute the failures and propose corrections. Then, ARISE keeps the corrections as retrievable micro memory, consolidates them into macro rules, and accepts a rule update only if held-out accuracy rises. Across 14 enterprise-workflow domains from SOP-Bench and $τ^2$-bench using 5 models, ARISE-Teacher, which uses Claude Opus 4.6 for attribution and consolidation, gains 10.9 pp over the baseline on SOP-Bench and 5.8 pp on $τ^2$-bench. ARISE-Teacher also outperforms GEPA by 4.5 pp on $τ^2$-bench and 1.4 pp on SOP-Bench. With the deployment model as its own attributor, ARISE-Self still gains 10.0 pp on SOP-Bench. ARISE-Teacher uses 4.0% fewer model calls and 5.2% fewer output tokens at comparable per-task cost (-1.0%).

## 30. Tracking Representations in LLM Reasoning Traces for Iterated Games

- Authors: Chaipat Tirapongprasert, Rajarshi Das, Parijat Dube
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-17
- DOI: Unavailable
- Categories: cs.CL, cs.AI, cs.GT
- Relevance: 2.7165386623390866
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.23403v1
- PDF: https://arxiv.org/pdf/2611.23403v1
- Local PDF: pdf/2026-11-20_30_Tracking Representations in LLM Reasoning Traces for Iterated Games.pdf

Large language model (LLM) agents achieve state-of-the-art performance across domains through chain-of-thought (CoT) reasoning. Despite their ubiquitous use, little is understood about the relationship between the externalized trace and the model's actual computation. We address this by investigating how LLM agents make decisions in iterative games with incomplete information. Using a series of mechanistic interpretability techniques, we find that the model forms and iteratively revises an internal representation of the game throughout the CoT. Once the model prematurely commits to an incorrect belief, it rarely recovers. This failure is manifested in both the literal trace and the layer activations. Ultimately, as multi-agent systems are more prevalent, our work opens the door to a more focused diagnosis of their strategic reasoning errors. For illustrative purposes, we offer an interactive visualizer of our methodology on selected sample traces at https://interp-self.github.io/gametrace/
