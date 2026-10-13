# Paper Daily Reading - 2026-10-13

## 1. When Edge Independence Fails: Joint Graph Diffusion with Latent Sociability Priors

- Authors: Adarsh Jamadandi, Nicolas Keriven, Aline Roumy
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-09
- DOI: Unavailable
- Categories: cs.LG, cs.AI
- Relevance: 3.6746023890251553
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.13765v1
- PDF: https://arxiv.org/pdf/2610.13765v1
- Local PDF: pdf/2026-10-13_01_When Edge Independence Fails_ Joint Graph Diffusion with Latent Sociability Priors.pdf

Discrete graph diffusion models corrupt graph structure through independent edge updates with a Markovian noise model. Combined with the exchangeability requirement on the output distribution, the terminal prior is necessarily an Erdős--Rényi (E-R) random graph. This has a fundamental consequence for unconditional graph generation without node features: in the large graph limit, any GNN denoiser applied to an E-R graph approximately outputs an E-R graph, making effective denoising difficult. In practice, generated graphs fail to recover meaningful node heterogeneity and higher-order structure. Previous models introduced specialized node features to compensate, framing this as an expressivity problem, while the role of the prior remained unexamined. We instead address the root cause by introducing the Latent Sociability Prior (LSP) and a join} diffusion process that co-evolves latent node sociability variables and graph structure, removing edge independence while preserving exchangeability. Unlike existing latent graph diffusion methods, the sociability mechanism requires no complex encoder: its sole role is to guide edge updates and preserve node heterogeneity throughout the trajectory. We validate our approach on multiple graph generation datasets and show that the proposed framework more accurately captures graph distributions than baseline methods without node features.

## 2. Your Discrete Graph Diffusion Model is Secretly Memorizing

- Authors: Adarsh Jamadandi, Nicolas Keriven
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-09
- DOI: Unavailable
- Categories: cs.LG, cs.AI
- Relevance: 3.4164489020071405
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.13786v1
- PDF: https://arxiv.org/pdf/2610.13786v1
- Local PDF: pdf/2026-10-13_02_Your Discrete Graph Diffusion Model is Secretly Memorizing.pdf

Discrete graph diffusion models (GDMs) corrupt the graph structure by adding noise independently to nodes and edges under a Markovian noise model. In the unconditional setting without node features, an equivariant denoiser trained on a single graph is able to generate novel graphs and sample-level metrics such as edge overlap and WL kernel similarity find no evidence of memorization. In this work, we challenge this view and show for the first time that graph diffusion models indeed exhibit memorization. Analyzing the reverse diffusion trajectories of GDMs trained on two-block stochastic block models (SBMs), we find a strong train-data bias: the model recovers a corrupted training graph almost perfectly compared to a held-out test graph. We term this conditional memorization, as it surfaces only when the reverse trajectory is conditioned on a corrupted training graph and is not apparent during inference. It coincides with a growing generalization gap, where the training loss improves as the loss on held-out graphs degrades, and it cannot be mitigated by early stopping. The onset of memorization always precedes the emergence of community structure in the generated graphs, thus every checkpoint earlier produces structureless graphs. This behavior holds across all node sizes we test.

## 3. Mesh-Native Tokenisation: Retrofitting Foundation Models to Unstructured Data

- Authors: Georg Maierhofer, Miles Cranmer, Payel Mukhopadhyay
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-08
- DOI: Unavailable
- Categories: cs.CE, cs.AI, math.NA
- Relevance: 3.2801187301492165
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.12618v1
- PDF: https://arxiv.org/pdf/2610.12618v1
- Local PDF: pdf/2026-10-13_03_Mesh-Native Tokenisation_ Retrofitting Foundation Models to Unstructured Data.pdf

Physics foundation models are an increasingly popular approach for building versatile emulators for spatiotemporal systems. They require tokenisation layers that lift physical field data into a latent representation suitable for dynamic processing. A typical choice for this layer is a convolutional encoder, which lifts field information in a locality-aware way and can be trained very efficiently. However, this choice cannot be applied to a large class of scientific computing problems where data are represented on unstructured meshes, for example simulations on domains with curved boundaries. Such data typically require graph neural network architectures, which are more expensive to train and, in the form currently used, encode information differently from their CNN counterparts, thus limiting the portability of physics emulators between these data regimes. In this work we introduce Mesh-Native Convolution (MNC), a locality-aware tokenisation layer that encodes unstructured mesh-based data in a way that is analogous to CNNs. This approach leads to models that can be trained once on mesh data and then deployed to arbitrary unstructured meshes, even if these are irregular, with minimal retraining. We show that this tokenisation approach can be used to retrofit grid-pretrained foundation models efficiently on unstructured meshes and provide theoretical results to confirm the consistency of this approach with classical CNN encoders. We demonstrate the favourable performance of this retrofitting approach, which in many cases reaches acceptable accuracy even in zero-shot deployment, and outperforms existing baselines after only a few epochs of fine-tuning, thus providing an efficient bridge between the two data regimes.

## 4. PhySeqNet: physics-informed fluorescent foci detection for BARseq spatial transcriptomics

- Authors: Neha Goswami, John Hover, Renae Galluccio, Yichen Wu, Huiqing Zhan, Xiaoyin Chen, Anthony M. Zador
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-09
- DOI: Unavailable
- Categories: physics.optics, q-bio.QM
- Relevance: 3.2654908861152783
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.13779v1
- PDF: https://arxiv.org/pdf/2610.13779v1
- Local PDF: pdf/2026-10-13_04_PhySeqNet_ physics-informed fluorescent foci detection for BARseq spatial transcriptomics.pdf

BARseq enables spatially resolved gene-expression profiling across intact tissue, but its sensitivity depends on accurate detection and decoding of dense fluorescent rolonies. Existing spot-calling approaches can be conservative where signals overlap, while supervised deep learning is limited by the lack of reliable manual ground truth in real tissue images. Here we present PhySeqNet, a physics-informed deep learning framework for annotation-free fluorescent foci detection in BARseq. PhySeqNet trains U-Net detectors entirely on semi-synthetic images generated from an instrument-matched optical model combined with real sample-free experimental noise, and is integrated into pyBARseq, a modular Python pipeline for BARseq analysis. PhySeqNet achieved high detection performance on held-out simulated data across wavelength bands. On real tissue images, where ground truth is unavailable, we evaluated detections by forward-model reconstruction: PhySeqNet with conservative barcode-aware non-maxima suppression (NMSB) achieved higher reconstruction fidelity (NCC and MS-SSIM) than the BarDensr single-shot estimator, tuned classical spot detectors, and a pretrained deep-learning detector. In the analyzed brain section, PhySeqNet with NMSB yielded a median of 51 counts per cell versus 47 for BarDensr, with a similar number of genes detected per cell. The recovered transcripts produced spatial expression patterns qualitatively consistent with Allen MERFISH reference data and preserved cell-type composition after scANVI label transfer. These results show that physics-informed simulation can train practical, annotation-free detectors that improve BARseq sensitivity without disrupting downstream biological interpretation.

## 5. Transformer-based In-Context Score Operator Learning for Diffusion Models

- Authors: Wuzhe Xu, Zhaiming Shen, Yulong Lu, Wenjing Liao, Rongjie Lai
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-09
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.2521933768313427
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.13690v1
- PDF: https://arxiv.org/pdf/2610.13690v1
- Local PDF: pdf/2026-10-13_05_Transformer-based In-Context Score Operator Learning for Diffusion Models.pdf

Diffusion models typically learn the generative dynamics of a single target distribution or a family of distributions indexed by conditioning variables fixed during training. This limits their ability to adapt to a previously unseen distribution from only a small set of examples. We introduce an in-context solution operator learning framework for diffusion models, in which each target distribution is treated as a task drawn from a meta-distribution and is specified at inference time by an empirical context set. Our method learns an in-context score operator that maps the context samples, a noisy query point, and the diffusion time to the task-dependent score, enabling reverse-diffusion sampling on unseen tasks without retraining or parameter updates. A key observation is that the task-dependent score admits a Gaussian-kernel conditional-mean representation. Its empirical Nadaraya--Watson approximation can be represented exactly by a model in our constructed transformer class, providing a principled foundation for the proposed query-dependent attention architecture. The operator is trained through amortized denoising score matching across task distributions. We establish generalization-error bounds that quantify the effects of the context size, the numbers of training tasks and within-task samples, model complexity, and intrinsic and ambient dimensions. Numerically, we evaluate the method on a range of scientific and visual datasets, including Navier-Stokes, ERA5 climate data, QuickDraw sketches, and Food-101. The results show that the proposed method performs well on relatively simple task families, while its performance degrades as task complexity increases, thereby illustrating both the promise and the limitations of in-context learning for diffusion models.

## 6. Byzantine-Resilient Federated Large Language Model via Hypergraph Message Passing

- Authors: Kai Li, Hanlin Cai, Zihao Liu, Yichen Li, Jose Alcaraz Calero, Wei Ni, Falko Dressler, Özgür B. Akan
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-08
- DOI: Unavailable
- Categories: cs.LG, cs.CR
- Relevance: 3.2279297418712396
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.12711v1
- PDF: https://arxiv.org/pdf/2610.12711v1
- Local PDF: pdf/2026-10-13_06_Byzantine-Resilient Federated Large Language Model via Hypergraph Message Passing.pdf

Federated Large Language Models (FedLLMs) are promising to deliver privacy-preserving, collaborative intelligence. The decentralized training process is vulnerable to Byzantine attacks that corrupt semantic consistency and factual resilience through malicious model updates. This paper presents a new resilience strategy that prevents semantically corrupted knowledge from propagating during federated aggregation. A defense problem is formulated to jointly maximize global accuracy and suppress manipulated model updates, enabling trustworthy knowledge aggregation without accessing private local data. To strengthen the resilience of FedLLMs, we develop a novel Hypergraph Message Passing Graph Autoencoder (HMP-GAE) framework, where low-rank model updates are represented as nodes in a hypergraph and high-order semantic relationships among multiple agents are exploited through iterative message passing. By leveraging historical checkpoints and cross-agent relational reasoning, HMP-GAE identifies and suppresses semantically inconsistent updates while preserving knowledge alignment among agents throughout federated training. HMP-GAE is implemented using Qwen-2.5 and Llama-3.2 as pretrained FedLLM backbones and evaluated on AG News and Yahoo! Answers datasets. Compared to existing defenses, HMP-GAE improves global accuracy by $1.21$\%, reduces final-model classification semantic entropy by $44.08$\%, and lowers perplexity by $13.34$\%. HMP-GAE outperforms the GAE-based defense by improving the accuracy $1.39$\%, reducing the semantic entropy by $54.5$\%, and lowering perplexity by $35.5$\%.

## 7. A Multi-Agent LLM System for Automated Tuning of Specialized Neural Network Models

- Authors: Ivan Moloshnikov, Dmitry Kunitsyn, Alexander Sboev, Maksim Skorokhodov, Roman Rybka, Yuanchao Liu
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-09
- DOI: Unavailable
- Categories: cs.AI, cs.CL, cs.LG, cs.MA, cs.NE
- Relevance: 3.2072432088890883
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.13663v1
- PDF: https://arxiv.org/pdf/2610.13663v1
- Local PDF: pdf/2026-10-13_07_A Multi-Agent LLM System for Automated Tuning of Specialized Neural Network Models.pdf

Many machine learning approaches are two-level: an expert selects a class of methods, within this class the choice of key components is critical and usually manual. This paper addresses the automatic tuning of these components and proposes a framework transferable across models of different nature. The multi-agent large language model (LLM) framework has three roles---analyst, coder, and recorder~---with an experiment log and a sandboxed execution environment. Unlike systems that optimize the entire ML script or search architectures in a discrete space, the framework operates over an open but semantically narrow space: the agent generates code only for the specified components, leaving the overall network structure unchanged. The approach is validated in two directions: tuning a classification spiking neural network with correlation learning, and solving high-order differential equations with Physics-Informed Neural Networks (PINN). Across five tasks---spiking classification on MNIST and Digits, and boundary-value problems for the generalized nonlinear Schrödinger equation (GNLSE) and Kuramoto--Sivashinsky (KS) equations---the agent outperforms the baselines: classification accuracy is 13 percentage points (MNIST) and 6 percentage points (Digits) higher; the error against the analytical single-soliton solution is reduced approximately 2491-fold; the invariant-preservation error drops approximately 325-fold in the selected GNLSE run with a Gaussian perturbation and by more than 100-fold on average over repeated initializations; and the mass drift drops 14-fold for the KS problem with a Gaussian perturbation. The framework thus tunes key components on tasks of different nature without changing its internal structure.

## 8. TabMF: Learning Dataset Representations with Tabular Foundation Models

- Authors: Rafiq Kamel, Nicolas Atienza, Aziz Fouché, Nicola Cancedda, Josif Grabocka
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-09
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.206127131539032
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.13818v1
- PDF: https://arxiv.org/pdf/2610.13818v1
- Local PDF: pdf/2026-10-13_08_TabMF_ Learning Dataset Representations with Tabular Foundation Models.pdf

Representations of supervised datasets support higher-level machine-learning tasks such as dataset retrieval and distribution-shift monitoring. However, existing approaches typically rely either on hand-crafted meta-features or on dataset encoders trained specifically for representation learning. We introduce TabMF, a framework that repurposes pretrained tabular foundation models (TFMs) as encoders of supervised datasets. TabMF equips a predictive TFM with an architecture-aware dataset-level readout and adapts the model end-to-end using contrastive post-training on stochastic views of synthetic supervised datasets. We instantiate TabMF on TabICLv2 and TabPFN-2.5 and evaluate the resulting representations across six tasks on unseen real datasets. Simple frozen TFM readouts yield competitive representations, indicating that predictive pretraining already induces substantial dataset-level structure. The two TabMF encoders obtain the strongest aggregate performance among the evaluated learned and classical dataset representations, with particularly strong results in dataset retrieval, compact benchmark construction, and distribution-shift severity assessment.

## 9. Transformer-Based Masked Diffusion Models Provably Learn Distributions with Latent Structure

- Authors: Jingda Wu, Changxiao Cai
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-08
- DOI: Unavailable
- Categories: cs.LG, cs.IT, math.ST, stat.ML
- Relevance: 3.1666004997066857
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.12544v1
- PDF: https://arxiv.org/pdf/2610.12544v1
- Local PDF: pdf/2026-10-13_09_Transformer-Based Masked Diffusion Models Provably Learn Distributions with Latent Structure.pdf

Masked diffusion models (MDMs) generate discrete data by iteratively unmasking multiple tokens in parallel using a learned mask predictor. Their output carries two errors: parallelization error due to parallel sampling, and estimation error from the mask predictor learned with finite samples. Existing theory treats these errors separately, and the available statistical bounds typically scale with the number $V^L$ of length-$L$ sequences over a vocabulary of size $V$, suffering from the curse of dimensionality. In this work, we establish end-to-end statistical guarantees showing that transformer-based MDMs learn structured distributions with a sample complexity governed by their latent structure. Specifically, we model this structure through mixtures of hidden Markov trees, which capture latent dependencies within components and heterogeneity across components. When the data distribution is well approximated by such a mixture, a transformer-based MDM with parallel unmasking schedules achieves $\varepsilon$-accurate sampling in KL divergence with $\widetilde{O}(LK_{\mathrm{par}}/\varepsilon)$ training samples, where $K_{\mathrm{par}}$ is polynomial in $L$, $V$, the number of hidden states, and the number of mixture components. The transformer network and sampling procedure require no knowledge of the tree topologies or component parameters, thereby adapting to the unknown latent structure automatically. Overall, our results provide theoretical justification for the empirical effectiveness of MDMs on real-world data.

## 10. Benchmarking Embedding Geometries and Clustering Algorithms for Unsupervised Patent Claim Classification

- Authors: Sujith Subramanian, P N Bhargav Teja, Susen Sarkar, Rajasekhara Reddy Duvvuru Muni
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-09
- DOI: Unavailable
- Categories: cs.AI, cs.CL
- Relevance: 3.1183565827049353
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.12997v1
- PDF: https://arxiv.org/pdf/2610.12997v1
- Local PDF: pdf/2026-10-13_10_Benchmarking Embedding Geometries and Clustering Algorithms for Unsupervised Patent Claim Classification.pdf

Prior-art retrieval systems are structurally organized around classification codes, making cross-code discovery difficult. This paper asks if an unsupervised representation trained on patent text can recover relevant connections that code-restricted search cannot, and if hyperbolic space helps. We trained a hyperbolic and a matched Euclidean Variational Autoencoder (VAE) on 45,000 US patents (96 runs, 6 seeds). The hyperbolic model retrieves genuinely cross-category prior art 52% more often than the Euclidean model (18.76% vs. 12.34% of top-10 results, 3,000 queries). This represents a practical gain for the motivating search problem. The hyperbolic model agrees less with official classification (NMI 0.2392 vs. 0.3206), which we explain geometrically: the two measures capture different goals, and only one aligns with prior-art search needs. In a study of 10 technology domains (50,000 more patents), we find that a domain's classification breadth--the number of distinct CPC subgroups spanned--predicts approach performance (Pearson r=-0.642, p=0.045, N=10), and that patents per subgroup is an even stronger predictor (r=0.715, p=0.020). This provides a checkable signal for practitioners to determine where the method is most valuable. We report all findings with statistical transparency and release a complete, 91-test automated implementation.

## 11. GIST: Generator-state-Informed Supervision for Tabular Foundation Models

- Authors: Zhangyang Peng, Jingze Shi, Tongyi Zhang, Yuyu Luo
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-09
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.1179457573741445
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.12904v1
- PDF: https://arxiv.org/pdf/2610.12904v1
- Local PDF: pdf/2026-10-13_11_GIST_ Generator-state-Informed Supervision for Tabular Foundation Models.pdf

Tabular foundation models (TFMs) based on prior-data fitted networks typically use sampled hard query labels, leaving avoidable sampling variability in pretraining. A key observation is that intermediate generator states can reveal label uncertainty beyond a sampled outcome. We propose Generator-state-Informed Supervision for TFMs (GIST), which uses these states to average query losses over conditional label distributions. GIST jointly designs task generation and query supervision, using entropy-calibrated encodings to obtain tractable, input-consistent targets on supported label-dependent branches. We show that this averaging preserves the population objective and yields no larger gradient covariance at fixed parameters within each generating distribution. Under matched pretraining schedules, GIST improves mean rank across three architectures on both TabArena and TALENT without changing architecture or inference. Across these benchmarks and architectures, GIST wins 62.1% of paired dataset-level comparisons against the corresponding hard-label controls.

## 12. Surfing the Activation Wave: Analyzing the Information and Geometry of LLM Hidden States for Speculative Decoding

- Authors: Raghavv Goel, Sudhanshu Agrawal, Mukul Gagrani, Risheek Garrepalli, Mingu Lee
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-09
- DOI: Unavailable
- Categories: cs.CL, cs.AI
- Relevance: 3.0730271395478423
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.12939v1
- PDF: https://arxiv.org/pdf/2610.12939v1
- Local PDF: pdf/2026-10-13_12_Surfing the Activation Wave_ Analyzing the Information and Geometry of LLM Hidden States for Speculative Decoding.pdf

Decoder hidden states from different layers of large language models (LLMs) often encode complementary information. However, existing speculative decoding methods typically rely on a small set of target-model layers chosen using fixed, position-based heuristics. Selecting an optimal subset of layers is inherently a combinatorial problem, making exhaustive evaluation infeasible even for moderately deep models. In this work, we present a principled framework for multi-layer hidden-state selection for speculative decoding based on two complementary criteria: informativeness, measured through matrix-entropy analysis, and diversity, quantified using centered kernel alignment (CKA). We investigate layer-wise Shannon entropy, aggregate entropy under hidden-state concatenation, and pairwise CKA dynamics across depth, revealing distinct geometric and informational compartments within decoder representations. Motivated by these findings, we propose entropy and CKA-based layer selection algorithms that favor hidden-state sets that are both highly informative and minimally redundant. As part of this framework, we introduce token-entropy filtering, which removes hidden states associated with low predictive-entropy tokens, thereby improving the quality of layer-selection statistics. In EAGLE3-style speculative decoding, our selected sets outperform fixed baseline choices, including the default $[2, N//2, N-3]$ rule, while providing a clearer explanation of why some defaults can remain competitive. Our results provide a practical recipe for multi-layer hidden-state selection for speculative decoding, insights into the geometry and information in LLM decoder states, and a foundation for extending similar analysis to related applications.

## 13. On the Design Space of Continuous Diffusion Language Models

- Authors: Oscar Davis, Daan Roos, Alice Bizeul, Amitis Shidani, Victor Turrisi, Louis Béthune, Pierre Ablin, Marco Cuturi
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-09
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.0728970071669726
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.13834v1
- PDF: https://arxiv.org/pdf/2610.13834v1
- Local PDF: pdf/2026-10-13_13_On the Design Space of Continuous Diffusion Language Models.pdf

Continuous diffusion language models (CDLMs) promise to bring the benefits of continuous flow modelling to language, including accelerated sampling and controllable generation. The field has grown rapidly, and the capabilities of CDLMs have begun to rival those of discrete diffusion. Yet, unlike for continuous modalities such as images or videos, our grasp of the levers that matter when training CDLMs remains limited. In this work, we focus on two of these levers, namely self-conditioning and embedding geometry, and shed light on some of the mechanisms behind them, which in turn suggest cheaper and more effective designs. We begin by showing that self-conditioning corrects a train/inference mismatch by exposing the model to inference-like states that are otherwise rare during training. These gains can be recovered without an extra forward pass by a two-level interpolant, coined $\mathrm{DoubleCat}$, which improves TinyGSM accuracy more than threefold. Self-conditioning also aids in recognising tokens dominated by large-norm Gaussians$\unicode{x2013}$an issue known as token identifiability. To address it directly, we introduce discrete reveals to $\mathrm{DoubleCat}$, yielding $\mathrm{SemiCat}$, which achieves discrete diffusion-level performance on TinyGSM, reaching $49.94\%$ with standard training hyperparameters and a tuned sampler. At the $1.7$B scale, $\mathrm{SemiCat}$ outperforms discrete diffusion on four of six likelihood-based evaluations, and surpasses one-hot flows on unconditional generation. On embedded spaces, we find that cross-entropy drives embeddings towards a geometry whose decoding error rate closely matches the one-hot one. We briefly explore a range of further options, such as hybrid corruption processes and noise schedules, including asynchronous ones. We believe this exploration can help the community better understand and advance the design space of CDLMs.

## 14. Sparse Dictionary Learning for Measure-Valued Data via Linearized Optimal Transport: Efficient Algorithms and Sample Complexity

- Authors: Brendan Mallery, Shuchin Aeron, James Murphy
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-09
- DOI: Unavailable
- Categories: stat.ML, cs.LG
- Relevance: 3.065639595412242
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.12924v1
- PDF: https://arxiv.org/pdf/2610.12924v1
- Local PDF: pdf/2026-10-13_14_Sparse Dictionary Learning for Measure-Valued Data via Linearized Optimal Transport_ Efficient Algorithms and Sample Com.pdf

We study dictionary learning for probability measure-valued data by embedding measures into Hilbert spaces using features derived from optimal transport geometry. We learn data-adapted dictionaries through sparse autoencoder parameterizations, producing fast, scalable representations of probability measures as sparse finite-dimensional codes. The resulting framework combines the rich, geometric structure of optimal transport with the interpretability and efficiency of sparse representation learning. We demonstrate its utility across diverse data modalities, including hyperspectral images, geometric point clouds, and document embeddings in large language model latent spaces. We also prove generalization bounds for sparse dictionary learning objectives on broad classes of $L^2$-valued measure embeddings, expressed in terms of the metric complexity of the atom class. For optimal transport and entropic transport map dictionaries, we derive new covering number bounds that yield explicit rates. Together, our computational and theoretical results support a new, scalable model for representation learning in the space of probability measures via embedding into Hilbert spaces.

## 15. Collaborative Learning and Reasoning over Model Slices

- Authors: Yuheng Wang, Runde Yang, Zhuohan Bao, Qiran Zhang, Huatao Li, Yiyang Zheng, Lin Wu, Jingru Fan, Shu Yao, Yihan Li, Zhi Li, Chen Qian
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-09
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 3.0574492738848242
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.12927v1
- PDF: https://arxiv.org/pdf/2610.12927v1
- Local PDF: pdf/2026-10-13_15_Collaborative Learning and Reasoning over Model Slices.pdf

Large language models (LLMs) excel across diverse tasks, benefiting from knowledge priors, in-context reasoning, and test-time computation. Despite these strengths, single-model reasoning remains vulnerable to error propagation, as later steps depend on the model's earlier outputs, leaving reasoning blind spots difficult to independently reassess. To address this limitation, we develop \textit{collaborative learning}, encompassing the construction of heterogeneous collaborators and the learning of effective cross-model collaboration. Specifically, \textit{model slicing} replaces a large model with smaller, heterogeneous models under a comparable parameter budget, enabling prior reasoning to be reassessed across distinct model parameterizations. \textit{Pyramid supervision} combines protocol distillation with step-level supervision to refine reasoning and interaction decisions throughout collaboration. We evaluate our approach across four task categories: multi-hop question answering, mathematical reasoning, code generation, and open-ended constrained generation. The trained heterogeneous models achieve comparable or better task performance than the original large model and established multi-agent baselines, including reinforcement-learning-based methods, while also achieving higher inference efficiency than the multi-agent baselines and exhibiting differentiated collaboration patterns across tasks. These findings show that learned collaboration turns model heterogeneity into complementary reasoning capabilities.

## 16. Mind the Spatial Gap: A Benchmark for Geospatial Reasoning and Constrained Spatial Editing

- Authors: Zheng Ren, Yanning Wang, Ziheng Huang, Fei Huang, Shiqi Wang, Ziqian Ye, Yang Yue
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-09
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 3.051271151399828
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.12881v1
- PDF: https://arxiv.org/pdf/2610.12881v1
- Local PDF: pdf/2026-10-13_16_Mind the Spatial Gap_ A Benchmark for Geospatial Reasoning and Constrained Spatial Editing.pdf

Understanding and manipulating spatial relations is fundamental to AI systems that reason about physical environments and construct grounded world models. However, existing evaluations of multimodal large language models (MLLMs) for spatial reasoning rely predominantly on static question-answering (QA) over small-scale or synthetic scenes, rarely probing whether models can modify spatial configurations while satisfying explicit geometric constraints. We introduce GeoSpatialBench, a benchmark designed to evaluate an escalating progression of spatial cognition, ranging from spatial relation understanding and geometric reasoning to constrained spatial editing. Grounded in real-world urban data across six geographically diverse cities, GeoSpatialBench evaluates a comprehensive taxonomy of 28 topological, directional, metric, and ordering relations across structured GeoJSON and map image modalities, with ground-truth references and constraints verified via GIS operations. Our empirical evaluation across frontier MLLMs uncovers a stark spatial gap: structured GeoJSON consistently outperforms map images, with multimodal combinations offering no reliable gain over GeoJSON alone, and while models show reasonable competence on qualitative topological and ordering, performance drops on quantitative metric relations. Crucially, editing performance on ordering relations declines relative to QA, and most failed edits violate at least one specified spatial constraint. These results highlight a gap between passively recognizing spatial relations and actively manipulating geometric configurations. GeoSpatialBench provides an open, rigorous diagnostic testbed to benchmark these spatial limitations, laying essential empirical groundwork for physically grounded world models and embodied spatial AI.

## 17. Scaling RNA Foundation Models through Iterative Refinement

- Authors: Pengan Chen, Liang Hong, Xinyuan Liu, Han Huang, Ziqian Lin, Jiayang Chen, Yimin Fan, Jiyue Jiang, Yu Li
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-09
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.049228812119748
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.13106v1
- PDF: https://arxiv.org/pdf/2610.13106v1
- Local PDF: pdf/2026-10-13_17_Scaling RNA Foundation Models through Iterative Refinement.pdf

Biological function in RNA is encoded across scales, from local sequence motifs to long-range structural dependencies. Conventional RNA foundation models couple parameter capacity and inference depth within a fixed architecture, prescribing a fixed computation graph for each inference. Here we present Eco-RNA, an 80M-parameter RNA foundation model that makes inference depth adjustable through learned iterative refinement. Its shared, input-conditioned Transformer core refines sequence representations through repeated application. The iteration count is selected after training and controls effective depth at fixed model parameters. We train across recurrent depths with masked reconstruction, state regularization, and a one-sided loss that anchors deeper reconstruction to a shallow reference. On the 70-assay RNAGym fitness benchmark, increasing refinement from one to four iterations raises aggregate absolute Spearman correlation from 0.242 to 0.286, with the gain retained through eight iterations. At four iterations, Eco-RNA surpasses the current SOTA Evo 2 40B on all three aggregate fitness metrics despite 500x fewer parameters. Its iteration configurations advance the compute-performance Pareto frontier among the evaluated models. It also outperforms the evaluated baselines in non-coding RNA family classification, RNA secondary-structure prediction, and chemical probing profile prediction. These results establish internal inference computation as an effective scaling dimension for RNA foundation models.

## 18. APEX: Asynchronous Prefix Denoising for Extreme Compression

- Authors: David Dinkevich, Nisan Chiprut, Yoav HaCohen, Dani Lischinski
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-09
- DOI: Unavailable
- Categories: cs.CV, cs.LG
- Relevance: 3.037552891639159
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.12843v1
- PDF: https://arxiv.org/pdf/2610.12843v1
- Local PDF: pdf/2026-10-13_18_APEX_ Asynchronous Prefix Denoising for Extreme Compression.pdf

Fewer latent tokens promise cheaper diffusion. Yet aggressive latent compression creates a reconstruction-generation dilemma: adding channels improves reconstruction but makes generation harder. We introduce APEX, short for Asynchronous Prefix denoising for EXtreme compression, which pairs a hierarchical latent space with asynchronous denoising over channel groups. Our autoencoder orders channel prefixes from structure to detail, while one shared denoiser generates them at staggered local times without adding tokens. On ImageNet-512, APEX outperforms existing methods at every evaluated channel count under 64x and 128x compression. At matched training and guided sampling compute, it also outperforms a 256-token model at every evaluated budget, with larger gains at lower compute. Code is available at https://daviddinkevich.github.io/APEX.

## 19. Mitigating Capability Degradation in LLM Self-Improvement via Representation Geometry Regularization

- Authors: Jiaqi Tian, Ting Long
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-09
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 3.031631066532439
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.12855v1
- PDF: https://arxiv.org/pdf/2610.12855v1
- Local PDF: pdf/2026-10-13_19_Mitigating Capability Degradation in LLM Self-Improvement via Representation Geometry Regularization.pdf

On-Policy Self-distillation is a self-improvement paradigm that enables large language models (LLMs) to improve their capabilities by leveraging the same model as both teacher and student under different conditioning contexts. However, we find that OPSD methods can progressively degrade previously acquired capabilities: queries that are correctly responded at earlier training stages may become incorrectly responded as optimization proceeds, even the overall performance continues to improve. Further analysis reveals that this degradation coincides with a deterioration of the geometry of hidden representations, characterized by reduced intra-cluster compactness and diminished inter-cluster separation. Motivated by this observation, we propose Representation Geometry Regularization (RGR), which preserves representation geometry during post-training by encouraging compactness within cluster and separation across cluster. RGR can be seamlessly integrated into existing OPSD methods without altering their core optimization procedures. Extensive experiments on multiple OPSD methods and benchmarks show that RGR generally alleviates capability degradation while retaining capability improvements. Our code is available in https://github.com/supermachinelearner/RGR.

## 20. Decoding Register Tokens Preserves Global Scene Details

- Authors: David Jacob Drexlin, Julius Hense, Jonas Dippel
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-09
- DOI: Unavailable
- Categories: cs.CV, cs.LG
- Relevance: 3.0134467549801913
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.13299v1
- PDF: https://arxiv.org/pdf/2610.13299v1
- Local PDF: pdf/2026-10-13_20_Decoding Register Tokens Preserves Global Scene Details.pdf

Pretrained vision transformers learn structured image representations spanning spatial patch tokens and non-spatial tokens. Recent analyses suggest that non-spatial register tokens encode global scene properties such as illumination, blur, and style. Yet patch-based image decoders discard these outputs, leaving the decoder to recover image appearance from patches alone. We investigate whether retaining register features improves decoding when the complete spatial patch representation is already available. We study this question using representation autoencoders (RAEs) with frozen register-equipped encoders. Our decoder processes four register tokens together with all patch tokens through joint self-attention. Appearance probes, paired reconstruction-error analysis, and fixed-decoder register substitutions examine which global image properties are accessible from registers and how their values affect reconstructed pixels. For generation, we train a multi-head attention pooling (MHAP) predictor to recover register features from sampled patches, keeping the pretrained diffusion model and its samples unchanged. On ImageNet-1K, our ViT-B decoders achieve mean reconstruction FIDs of 0.472 with DINOv2 and 0.442 with DINOv3, reductions of 9.5% and 5.2% relative to their respective patch-only baselines. The corresponding PSNRs are 19.73 and 20.54 dB. For generation, our DINOv2 models achieve a mean FID of 1.641, 9.8% below the patch-only baseline on identical sampled patches.

## 21. Task Context Shapes Component Roles in Language Models

- Authors: Sovesh Mohapatra, Dani S Bassett
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-09
- DOI: Unavailable
- Categories: cs.CL, cs.AI
- Relevance: 3.0112949747860274
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.13895v1
- PDF: https://arxiv.org/pdf/2610.13895v1
- Local PDF: pdf/2026-10-13_21_Task Context Shapes Component Roles in Language Models.pdf

Large language models reuse the same attention heads across tasks, but identifying these shared heads does not explain what they do differently in each task. A natural source of inspiration is task-dependent interactions among shared brain regions, which motivate a network view of language-model computation. Here, we compare fixed model components across tasks using identical graph facts, statements specifying which directed connections are present. We measure how interventions affect attention heads and the activation state in later layers (influence), as well as the answer (importance). Task changes redistribute the influence in five open-weight models spanning four families and 1.5-14 billion parameters. In Gemma-2-9B and Qwen3-14B, an activation edit changes an early internal activation vector and switches which fact the model reads while the written instruction stays fixed. The same heads then respond to different graph facts and influence later components differently. For each prompt, we construct two linear response maps, one before the edit and one after it. Each map predicts a later head's response from a measured change in an earlier head. For a separate factual intervention, the map for the corresponding condition reduces mean squared prediction error by 53.6% in Gemma and 5.0% in Qwen compared with the average of the two maps. These findings show that task context changes both which graph facts the shared components respond to and how their outputs affect later computation. A network account may help explain how models use shared parameters to perform different computations. Measurements of task-dependent influence could also guide interventions intended to alter one behavior while preserving others.

## 22. PlacePulse: Learning Transferable Place Representations from Structural Geographic Data

- Authors: Lucía García-Duarte, Miguel Álvarez, Diego Vicente, Javier Pérez Trufero, Javier de la Torre
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-09
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 2.992024648760463
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.13390v1
- PDF: https://arxiv.org/pdf/2610.13390v1
- Local PDF: pdf/2026-10-13_22_PlacePulse_ Learning Transferable Place Representations from Structural Geographic Data.pdf

Geospatial machine learning often depends on task-specific feature engineering over large collections of sociodemographic, business, and environmental variables. Geospatial foundation models offer reusable representations of place, but leading approaches typically encode dynamic signals, such as mobility and search activity, or visual signals from satellite imagery. Few models represent the static structural composition of places (who lives and works there, which businesses operate there, and which risks they face) as transferable embeddings at fine spatial resolution. We introduce PlacePulse, a structural geospatial foundation model that compresses 572 attributes, expanded to 2,288 inputs through H3 neighborhood aggregates, into 256-dimensional unit-norm embeddings for 1,055,537 H3 resolution-7 cells in the United States. We also introduce a reusable two-axis benchmark that separates intrinsic representation quality from downstream predictive utility across multiple targets and spatial supports. Intrinsically, the embeddings reconstruct standardized inputs with mean $R^2 = 0.853$, use 251 of 256 approximately decorrelated dimensions, and show strong spatial organization, with Moran's $I = 0.93$ on the leading principal component and autocorrelation persisting beyond the input radius. Extrinsically, across 74 held-out targets from 12 external sources and four spatial supports, PlacePulse outperforms a dimensionality-matched feature-selection baseline on targets unrelated to the training inputs and is competitive with Google's Population Dynamics Foundation Model, leading on health, economic, election, economic-mobility and social-vulnerability outcomes, with relative strengths that vary by domain. These findings position structural composition as a distinct and complementary modality for geospatial foundation models, not simply a fallback where behavioral or imagery data are unavailable.

## 23. Zebra3D: Efficient Hybrid Foundation Models For Scalable 3D Reconstruction

- Authors: Utkarsh Saxena, Ruijing Yang, Mehdi Rezagholizadeh, Akash Haridas, Vikram Appia, Emad Barsoum
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-08
- DOI: Unavailable
- Categories: cs.CV, cs.LG
- Relevance: 2.969486971704598
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.12727v1
- PDF: https://arxiv.org/pdf/2610.12727v1
- Local PDF: pdf/2026-10-13_23_Zebra3D_ Efficient Hybrid Foundation Models For Scalable 3D Reconstruction.pdf

Feed-forward 3D foundation models reconstruct scenes from unposed images, but the quadratic cost of global attention limits their scalability to large view sets. We present Zebra3D, a layerwise sparse-linear hybrid attention framework that improves the efficiency of pretrained 3D foundation models without training from scratch. Across VGGT, HunyuanWorld-Mirror, and $π^3$, we observe a broadly consistent depth-wise pattern: early stages are relatively tolerant to linear replacement, while sensitive middle-to-late stages tend to exhibit more concentrated attention. Zebra3D exploits this structure by assigning linear-centered attention to tolerant stages and tile-sparse attention to sensitive stages, using landmark summaries to preserve unselected context. Closed-form affine fitting enables training-free conversion, while optional post-conversion training combines task supervision with output and relational feature distillation. Across all three backbones, Zebra3D achieves strong reconstruction and camera-pose accuracy at high attention sparsity, with training-free variants remaining close to their dense counterparts. End-to-end speedups increase with input view count, reaching up to $7.1\times$ at 1,024 views. After post-conversion training, Zebra3D-VGGT reaches 80.5\% RealEstate10K AUC@30 at 94\% mean attention sparsity, within 1.1 percentage points of dense VGGT fine-tuned on the same data and schedule.

## 24. Kairos: Toward a Byte-Level Foundation Model for Every Modality

- Authors: Fabien Furfaro
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-26
- DOI: Unavailable
- Categories: cs.LG, cs.AI, cs.CL
- Relevance: 2.9012185503280885
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.12495v1
- PDF: https://arxiv.org/pdf/2610.12495v1
- Local PDF: pdf/2026-10-13_24_Kairos_ Toward a Byte-Level Foundation Model for Every Modality.pdf

Small language models trained on a single local machine leave little room for architectural trial and error. Kairos combines bidirectional gated-DeltaNet linear attention and sliding-window attention over shared projections (LiZAttention2), block-wise Attention-Residual aggregation, a sparse Mixture-of-Experts (MoE) feed-forward layer and a multi-scale byte-level codec, trained with a uniform-noise denoising objective over one byte space shared by text, image, audio, video, lidar and control streams; this report asks whether the combination optimizes at all before asking whether it is useful. We give code-derived algorithms for each component, including a cross-session recurrent-state memory gate, then run convergence sanity checks: overfittinga single 440-byte sentence at 1--15M parameters, text only, with three seeds for codec and attention choices and single-run sweeps for seven further factors. The two attention variants tested at 3\,000 steps (LiZAttention2 and window attention alone) reach a minimum loss near $10^{-3}$. After 600 steps, the mean minimum loss ranges from 0.018 (patch codec) to 0.354 (depthwise convolutional codec) with an identical ranking on three seeds. An apparent advantage of shared over separate attention projections closes with more steps or more diverse data and reverses when the projections are frozen: it is a convergence-speed effect, not a capacity effect. These checks suggest that the implementation optimizes; they say nothing about generalization, multimodal training or comparison with existing models, which a planned pretraining run is meant to address. The Discussion sizes a 200M-total/25M-active target analytically; none of its throughput figures is measured. Code is available at https://github.com/fabienfrfr/Kairos . Python package at https://pypi.org/project/kairos-fm/ .

## 25. ReSFlow: Rectifying Categorical Flows on Statistical Manifolds for One-Step Generation

- Authors: Xiaohuan Jia, Renzhe Xu, Xiao Wang, Jiayun Wu, Shaohua Fan
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-09
- DOI: Unavailable
- Categories: cs.LG, cs.AI
- Relevance: 2.880191382676214
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.13225v1
- PDF: https://arxiv.org/pdf/2610.13225v1
- Local PDF: pdf/2026-10-13_25_ReSFlow_ Rectifying Categorical Flows on Statistical Manifolds for One-Step Generation.pdf

Generative modeling for discrete data has been significantly advanced by learning continuous vector fields on the statistical manifolds to transport simple priors to target discrete distributions. However, because these continuous-time flows are not constrained to follow geodesics on the statistical manifold, thereby requiring multi-step numerical integration for simulation and leading to substantial computational costs during inference. In this work, drawing inspiration from the "straight and fast" properties of Rectified Flow in continuous Euclidean space, we propose the Rectified Statistical Flow (ReSFlow) model, which enables one-step categorical generation on statistical manifolds by explicitly learning geodesic trajectories that adhere to the intrinsic Riemannian geometry. By rectifying the flow on the statistical manifold, we theoretically guarantee that trajectories between prior and target distributions approximate geodesics. This rectification significantly reduces the transport cost by aligning the learned trajectories directly along geodesics on the statistical manifold, allowing the model to map pure noise to target discrete data in a single step. Through extensive experiments on diverse real-world generative tasks, ranging from image and text to biological domains, we demonstrate ReSFlow's superior one-step generation quality, which truly embodies geodesically optimal and rapid categorical generation. Our code is available at https://github.com/xiaohuanjia/ReSFlow.

## 26. Artificial Intelligence-Assisted Systems Biology Reconstruction of Diabetic Bone Marrow Dysfunction

- Authors: Paolo Madeddu
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-09
- DOI: Unavailable
- Categories: q-bio.MN
- Relevance: 2.8758006643005016
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.13721v1
- PDF: https://arxiv.org/pdf/2610.13721v1
- Local PDF: pdf/2026-10-13_26_Artificial Intelligence-Assisted Systems Biology Reconstruction of Diabetic Bone Marrow Dysfunction.pdf

This study aimed to reconstruct a regulatory network suitable for systems biology analysis of diabetic bone marrow.
  Three artificial intelligence large language models independently analysed 18 Discovery and 43 Validation publications. Investigator guided integration produced a frozen network of 62 biological entities and 79 directed interactions. Open source software Gephi created a visual representation before and after main node removal. The plausibility of the reconstructed interactions was tested against independent curated knowledge resources, including the Kyoto Encyclopedia of Genes and Genomes, connectomeDB2025, Reactome, and Gene Ontology. Further analysis examined physiological correspondence, missing edge sensitivity, and graph constrained interrogation.
  Functional modules encompassed endothelial perivascular support, stem cell retention and trafficking, neural circadian regulation, inflammatory myelopoiesis, metabolic stress, and epigenetic regulation. They intersected through shared effects on endothelial function and stem cell behaviour. The endothelium was the principal connecting node. Computational removal of the endothelial node increased network fragmentation and diameter, while average directed path length remained essentially unchanged. External resources supported 60/79 interactions (75.9%); 19 remained unresolved, with none classified as contradictory. Complementary assessments supported biological plausibility and faithful interrogation of the reconstructed network.
  This investigator led dialogue with artificial intelligence provides a foundation for a systems level understanding of diabetic bone marrow dysfunction. The approach may facilitate the generation of testable hypotheses and the identification of mechanistic targets for coordinated restoration of disrupted niche interactions.

## 27. NV-Tesseract-AD: Curriculum-Enhanced Conditional Diffusion for Multivariate Time-Series Anomaly Detection

- Authors: Aditi Gautam, Manikandan Ravikiran, Saira Qureshi, Sena Fatma Ekiz, Charan Jagwani, Mahmoud Elhadidy, Sanjeev Roka
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-08
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 2.8594970874556043
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.12754v1
- PDF: https://arxiv.org/pdf/2610.12754v1
- Local PDF: pdf/2026-10-13_27_NV-Tesseract-AD_ Curriculum-Enhanced Conditional Diffusion for Multivariate Time-Series Anomaly Detection.pdf

We propose NV-Tesseract-AD, a curriculum learning-enhanced conditional diffusion framework for multivariate time-series anomaly detection. Our central hypothesis is that reconstruction difficulty can be explicitly structured along two complementary axes, masking severity and diffusion noise level, and that training from easier to harder tasks along both axes simultaneously stabilizes optimization and improves residual discriminability. We integrate a Transformer-based diffusion backbone with a three-stage dual curriculum over masking ratios and diffusion timesteps, retaining anomalous samples throughout training and relying on structured corruption to drive self-supervised representation learning. We evaluate NV-Tesseract-AD under two regimes: in-distribution training on the TSB-UAD-M corpus and strict zero-shot transfer to ten EasyTSAD benchmark families without per-dataset tuning. The dual-axis curriculum produces masking-invariant reconstruction, confirmed by a near-zero loss gap between complementary masking strategies within the first training stage, and yields an approximately 3.7-fold improvement in F1 and a 56 percent reduction in MSE relative to a non-curriculum baseline. Zero-shot performance reaches F1 = 0.984 on NAB and F1 = 0.948 on NormA. Weaker results on heterogeneous families are traced to unsupervised threshold calibration rather than reconstruction quality, identifying calibration as the dominant remaining detection bottleneck. Accelerated inference via DPM-Solver++ reduces sampling cost by a factor of 3.5 to 5.7 at the dataset level but couples to thresholding behavior, establishing that the sampler and threshold must be validated jointly. Together, these findings demonstrate that aligning diffusion denoising difficulty with curriculum learning principles provides a principled and practical approach for robust anomaly detection in complex multivariate time series.

## 28. Spatial Prediction with Guided Diffusion

- Authors: Andrew Zammit-Mangion, Lachlan Astfalck, Raphaël Huser, Christopher Nemeth, Henry B. Moss
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-09
- DOI: Unavailable
- Categories: stat.ME, stat.CO, stat.ML
- Relevance: 2.8499476950384506
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.12967v1
- PDF: https://arxiv.org/pdf/2610.12967v1
- Local PDF: pdf/2026-10-13_28_Spatial Prediction with Guided Diffusion.pdf

Spatial prediction is a critically important task in data analyses that involve spatially or spatio-temporally-referenced data. It is commonly carried out using hierarchical models, which comprise a process model describing the latent process of interest, and a data model describing how the process is observed. The target quantity is the predictive distribution, which is the conditional distribution of the latent spatial process given the observed data. Unfortunately, the predictive distribution is rarely available in closed form and can be difficult to sample from. Here, we show how recent developments in guided diffusion modelling from machine learning can address a wide class of problems in spatial prediction when the likelihood function derived from the data model is known and differentiable, possibly after relaxation. To show the versatility of the approach, we apply it to both Gaussian and non-Gaussian process models and a variety of data models that describe direct partial observations, linear and areal aggregates, counts, right censoring, and area-exceedance functionals. Where possible, we validate the framework against exact and Markov-chain-Monte-Carlo (MCMC)-derived predictive distributions. We demonstrate our approach on several simulation studies and in a controlled experiment of methane-flux inversion over the UK and Ireland. We show that guided diffusion can sample from the correct predictive distribution in a variety of settings, that it can be applied to models where MCMC is intractable, and that it scales well with the dimensionality of the latent process.

## 29. Rethinking the Roles of Diffusion and Decoding: Predictive-State Flows for Parallel Language Generation

- Authors: Jinjin He, Xinsong Feng, Lucheng Fu, Sinan Wang, Bo Zhu, Jiayun Wang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-09
- DOI: Unavailable
- Categories: cs.CL, cs.LG
- Relevance: 2.848563135060468
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.12898v1
- PDF: https://arxiv.org/pdf/2610.12898v1
- Local PDF: pdf/2026-10-13_29_Rethinking the Roles of Diffusion and Decoding_ Predictive-State Flows for Parallel Language Generation.pdf

In continuous diffusion language models (DLMs), latents generated by the diffusion prior are mapped almost deterministically to tokens, either by a decoder or through a token embedding matrix. Unlike in image generation, where visual details can vary continuously, the diffusion prior must capture fine-grained discrete token choices in continuous space, which can make the joint latent distribution difficult to model. We argue that generative roles should instead be divided: the diffusion prior should generate high-level predictive information, while the decoder should resolve the remaining token-level choices. Based on this view, we introduce Predictive-State Flows (PSF), which partitions a sequence into blocks and associates each block with a predictive state computed solely from the preceding context. A rectified-flow prior generates the sequence of predictive states, after which a block-causal decoder generates all blocks in parallel, autoregressively only within each block. This design reduces diffusion from L token-level states to K << L predictive states and reduces token-level sequential depth to L/K. On unconditional OpenWebText generation, a 197M-parameter model with K=8 achieves a generative perplexity of 22.8 at entropy 5.16 using 0.31 TFLOPs per 1024-token document, versus 24.0 and 7.2 TFLOPs for ELF-B with 32 sampling steps. The corresponding measured operating points yield MAUVE@512 of 0.93 and 0.73, respectively. Controlled comparisons further show that content states, which additionally encode their own blocks, yield 8-16% higher generative perplexity than predictive states, and that replacing sampled predictive-state trajectories with a shared mean lowers MAUVE@512 by 0.11. These results suggest that latent design for continuous DLMs should consider not only how compactly text is represented, but also how generative roles are divided between the prior and the decoder.

## 30. MORAD: Reinforcement Learning with Multi-Objective Rewards for RNA Inverse Design

- Authors: Jixin Tang, Ji Guo, Jun Zhao
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-09
- DOI: Unavailable
- Categories: cs.LG, q-bio.BM
- Relevance: 2.8459217975958087
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.13305v1
- PDF: https://arxiv.org/pdf/2610.13305v1
- Local PDF: pdf/2026-10-13_30_MORAD_ Reinforcement Learning with Multi-Objective Rewards for RNA Inverse Design.pdf

We introduce MORAD, an online reinforcement learning framework for backbone-conditioned RNA diffusion models that trains a single shared policy across diverse target backbones. Structure-conditioned RNA inverse design seeks nucleotide sequences compatible with a target three-dimensional backbone, yet existing reinforcement learning approaches either optimize a separate policy for each target backbone or rely on offline preference optimization, leaving online post-training of a reusable backbone-conditioned model largely unexplored. MORAD combines backbone-conditioned group sampling, group-relative reward normalization, and a forward-process diffusion objective. Beyond existing RL rewards that primarily target tertiary structural quality, MORAD jointly optimizes six measurements spanning tertiary geometry, base pairing, ensemble behavior, and sequence composition. To aggregate these heterogeneous objectives despite differences in scale and optimization direction, MORAD maps each measurement to a bounded desirability score and combines them with a weighted geometric mean. Compared with a tertiary-structure-only reward, this multi-objective formulation improves 10 of the 11 evaluation metrics that have a preferred direction. Applied to pretrained RIDE, MORAD improves GDT-TS by 16.0% (from 0.3300 to 0.3827) and pairing MCC by 19.4% (from 0.6110 to 0.7295), while reducing normalized ensemble defect by 27.5% (from 0.3906 to 0.2830). On the test set, MORAD outperforms RiboDiffusion, gRNAde, and RDesign across tertiary structural accuracy, secondary-structure pairing, and thermodynamic quality, establishing a new state of the art in structure-conditioned RNA inverse design.
