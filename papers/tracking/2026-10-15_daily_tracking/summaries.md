# Researcher Tracking - 2026-10-15 (daily)

Total new tracked papers: 9
Highlighted papers: 9

## 1. Share the Symbol, Not the Vector: Training-Free Fact Communication Across Language Models

- Authors: Xin Li, Mengbing Liu, Hao Jiang, Xin Gao, Annan Wang, Xingwei Qu, Yichi Zhang, Chau Yuen
- Source hits: arxiv
- Matched researchers: Xin Gao
- Matched groups: N/A
- Confidence: medium (author_alias)
- Topic keywords: multi-agent system
- Journal/source: arxiv
- Publication date: 2026-10-14
- Article: http://arxiv.org/abs/2610.19696v1

Multi-agent systems allow language models to solve tasks collaboratively by sharing complementary information. These systems typically communicate through text, while recent approaches also explore exchanging internal model states. However, sharing these states across architectures often requires learned translators or assumptions about model compatibility. We introduce SYNC (Symbol-Indexed Neural Communication), a word-indexed interface that connects heterogeneous models without fine-tuning or a learned translator. From descriptions only it can see, the sender selects words from a shared list and sends their indices for each object, without seeing the questions. The receiver writes the described facts into its hidden states using its own word directions, vectors fitted once from its activations. We test selective use by swapping one attribute between two objects and requiring correct answers about both changed and unchanged attributes before and after the swap, four answers in total. We choose an early write layer on four development receivers and then fix it. With three different senders and nine newer receivers from five families, four-answer success on new scenes reaches 72.0-98.3%, up to 96 percentage points above middle-layer writing, and the two largest receivers match plain text. A task-free probe predicted in advance which depths each new receiver can use (45 of 45 cases). Without retuning, messages listing every fact keep 89.6-100% success under new layouts, and sender messages reach 23.9-64.0% on a landmark task with multi-token symbols, below text but from 0% without a message. These results show that shared word indices and receiver-local directions can support selective fact use across model families without additional training.

## 2. Computational compressive imaging reconstruction with a simulated-annealing-based Ising solver

- Authors: Ze Zheng, Xiaoyan Wu, Hang Xu, Jingzheng Huang, Tailong Xiao, Guihua Zeng
- Source hits: arxiv
- Matched researchers: Hang Xu
- Matched groups: N/A
- Confidence: medium (author_alias)
- Topic keywords: N/A
- Journal/source: arxiv
- Publication date: 2026-10-14
- Article: http://arxiv.org/abs/2610.19778v1

Computational compressive imaging, such as single-pixel imaging and lensless imaging, is a promising imaging technique, enabling the reconstruction of objects from under-sampled measurements through compressed sensing algorithms or deep learning methods. However, the demand for electronic computational resources grows rapidly when recovering high-resolution and multi-dimensional images and training neural networks with numerous parameters, which has become a bottleneck for the widespread adoption of this technique. Here, we propose a physics-driven reconstruction framework that formulates imaging inverse problems as Ising models and directly recovers target objects through the self-evolution of non-von Neumann Ising machines toward the ground state of the Hamiltonian. We employ a simulated-annealing-based Ising solver to demonstrate this proof-of-concept by reconstructing objects in both single-pixel imaging and a lensless diffuser camera at sampling rates ranging from 1% to 25%. By further incorporating a foreground-sparsity constraint and a smoothness constraint, the reconstruction quality of our method is comparable to or even better than that of mainstream algorithms. This approach has the potential to substantially reduce the electronic computational burden of inverse reconstruction, paving the way for real-time, low-power computational imaging.

## 3. One Block Ahead: Promoting Sampler State in Diffusion Language Models

- Authors: Yangyi Shen, Pin-Jui Ku, Nicolai Oswald, Jean-Marie Lemercier, Yonggan Fu, Stefano Ermon, Jure Leskovec, Boris Ginsburg, Ante Jukić
- Source hits: arxiv
- Matched researchers: Jure Leskovec
- Matched groups: N/A
- Confidence: medium (author_alias)
- Topic keywords: diffusion
- Journal/source: arxiv
- Publication date: 2026-10-14
- Article: http://arxiv.org/abs/2610.19510v1

Block-diffusion language models denoise a whole block of token positions in parallel so each forward pass can emit many tokens. However, blocks are still denoised in strict sequence, a cost that within-block acceleration leaves untouched. Here, we investigate decoding blocks concurrently and propose One Block Ahead (OBA), a training-free decoding algorithm that denoises the next block alongside the current one. We demonstrate that for uniform-state diffusion LMs, where a block's denoising progress is not visible in its intermediate tokens, concurrent decoding is advantageous if the next block's tokens are promoted together with the corresponding sampler state, including the self-conditioning signal and the denoising time. We also derive a break-even criterion that relates the benefit of OBA to the relative cost of a paired-block forward pass. On DiffusionGemma, a state-of-the-art diffusion LM, OBA increases the tokens per forward pass by 42.3% (from 15.64 to 22.25) and the single-request denoising throughput by 16.3%, averaged over ten benchmarks, with a small accuracy regression.

## 4. AesCode: Aesthetic Code Generation with Decoupled Cross-Modal Rewards

- Authors: Xin Gao, Yifan Yang, Xin Li, Pan Wang, Yan Li, Muzhao Tian, Mingxi Cheng, Bei Liu, Kai Qiu, Qi Dai, Dong Chen, Yue Dong, Leandros Tassiulas, Rex Ying, Ji Li, Chong Luo
- Source hits: arxiv
- Matched researchers: Xin Gao
- Matched groups: N/A
- Confidence: medium (author_alias)
- Topic keywords: N/A
- Journal/source: arxiv
- Publication date: 2026-10-13
- Article: http://arxiv.org/abs/2610.18860v1

Generating information-rich visual artifacts such as slides, posters, and dashboards as code is appealing because the outputs are structured, editable, and verifiable. Yet code models cannot see how their choices of layout and color come together on the canvas, often limiting spatial planning and aesthetic quality. Image generators excel at visual design but can misrender requested content, making their outputs unreliable targets for direct reproduction. We therefore introduce AesCode, which generates code grounded in the content prompt while using an image generated from the same prompt as an aesthetic guidance. To do so, AesCode represents the target as a design graph that describes the whole canvas and makes each property attributable. From this graph, we derive complementary cross-modal rewards: deterministic verifiers score properties parsable from code and rendering, while a VLM judge assesses the non-parsable ones with a sample-specific Visual Graph Rubric (VGR) tied to graph elements and relations. We optimize these decoupled rewards through reinforcement learning with per-channel normalization to jointly improve spatial planning, aesthetic quality, and verifiable correctness. To evaluate this setting, we build a benchmark that scores verifiable correctness and visual quality separately, with visual scores highly consistent with human judgments. We find that reference images substantially improve the visual quality of code generated by existing models, and ablations show that AesCode benefits from references both as model input and as a source of visual rewards. Relative to same-scale Qwen3-VL baselines given the same references, AesCode-8B and AesCode-32B improve visual quality by 31.1 and 22.4 percentage points, reaching scores comparable to those of closed-source frontier models such as GPT-5.5 and Claude Opus 4.8.

## 5. RT-J: Large-Scale Pretraining of Relational Transformers for Context-Efficient Predictions

- Authors: Rishabh Ranjan, Vignesh Kothapalli, Harshvardhan Agarwal, Charilaos Kanatsoulis, Roshan Upendra, Tom Palczewski, Carlos Guestrin, Jure Leskovec
- Source hits: arxiv
- Matched researchers: Jure Leskovec
- Matched groups: N/A
- Confidence: medium (author_alias)
- Topic keywords: foundation model
- Journal/source: arxiv
- Publication date: 2026-10-13
- Article: http://arxiv.org/abs/2610.17867v2

Foundation models for tables and relational databases are increasingly used for predictive tasks across various scientific and industrial domains. However, adapting existing models to unseen datasets requires tens of thousands of examples. Here we introduce RT-J, an 85M-parameter relational foundation model (RFM) that makes accurate predictions even with hundreds of in-context examples or fewer. To achieve this, we first assemble the Join, a large collection of 639 web-crawled databases with 6,023 LLM-generated forecasting tasks. We pretrain with long contexts of up to 8,192 database cells, using in-context examples from a novel lightweight random-walk retriever. Finally, we leverage context tuning and ensembling to scale up test-time compute. On in-context regression tasks from RelBench, RT-J requires 10x fewer examples on average to match strong feature engineering pipelines with LLM-agent or RDBLearn featurizers and TabICLv2 or LightGBM predictors. Overall, our work pushes the frontier for context-efficient predictions on relational data and highlights the importance of real-world semantics, context engineering and large-scale pretraining for RFMs.

## 6. Query Complexity of Densest Sub(hyper)graph Problems

- Authors: Sinan G. Aksoy, Eli Friedman, Nate Veldt, Stephen J. Young
- Source hits: arxiv
- Matched researchers: Nate Veldt
- Matched groups: N/A
- Confidence: medium (author_alias)
- Topic keywords: N/A
- Journal/source: arxiv
- Publication date: 2026-10-13
- Article: http://arxiv.org/abs/2610.17581v1

Rubinstein et al. introduce the study of connectivity and minimum cut problems in the cut query model, where an algorithm can only access the edges of a graph through CUT queries. In this work, we examine the query complexity of densest subgraph problems. Our first contribution is to generalize the uniform sparsification approach for Densest Subgraph and other heavy subgraph problems to weighted graphs, achieving the following results.
  >A $(1+\varepsilon)$-approximation for weighted Densest Subgraph in $O(n\log^2 n/\varepsilon^2)$ queries, roughly matching the $Ω(n/\log n)$ lower bound we prove for randomized algorithms.
  >A $(1+\varepsilon)$-approximation for weighted Max Cut in $O(n\log^2 n/\varepsilon^2)$ queries. This improves upon the bound of $O(n\log^3 n(\log n+1/\varepsilon^2))$ queries achieved by Plevrakis et al., making significant progress towards their lower bound of $Ω(n/\log n)$ queries.
  In contrast, we rule out approximation schemes with truly subquadratic query complexity for Densest $k$-Subgraph and settle its exact query complexity in both the unweighted and deterministic settings.
  For hypergraphs, we show CUT queries alone cannot achieve $o(\sqrt{n})$-approximation for Densest Subhypergraph or $o(n)$-approximation for Densest $k$-Subhypergraph, regardless of the number of queries. Augmenting CUT queries with the EDGE oracle of Chen et al., we overcome this barrier for Densest Subhypergraph and obtain a $(1+\varepsilon)$-approximation on rank-$r$ hypergraphs using $O(nr\log n/\varepsilon^2)$ queries. We also extend our Densest $k$-Subgraph hardness results to hypergraphs and prove exponential query lower bounds for exact Densest $k$-Subhypergraph. Lastly, confirming a conjecture of Chakrabarty and Liao, we show that simulating an ADD query using CUT and IS-EDGE$^?$ queries requires exponentially-many queries.

## 7. TRACESTEER: Trace Driven Activation Steering for Hallucination Mitigation in Diffusion Language Models

- Authors: Xin Zhang, Yili Wang, Yue Tan, Xin He, Rui Miao, Yixin Liu, Yi Chang, Xin Wang
- Source hits: arxiv
- Matched researchers: Yixin Liu
- Matched groups: N/A
- Confidence: medium (author_alias)
- Topic keywords: diffusion, large language model
- Journal/source: arxiv
- Publication date: 2026-10-13
- Article: http://arxiv.org/abs/2610.18173v1

Diffusion large language models (dLLMs) have emerged as a promising alternative to autoregressive LLMs, yet remain susceptible to hallucination. Activation steering offers a promising mitigation approach by guiding parallel token predictions through internal representations. However, existing steering methods largely overlook two characteristics of dLLMs: dynamic denoising states and temporal hallucination risks, which challenge predefined steering vectors and uniform intervention strengths. We propose TRACESTEER, a trace-driven activation steering framework that uses preceding denoising predictions as feedback to jointly adapt steering direction and strength. Specifically, Denoising Feedback Steering (DF-Steering) constructs step-specific steering vectors from preceding predictions and current hidden states. Trajectory-Guided Steering Gate (TS-Gate) regulates their strength using prediction uncertainty and the denoising timestep. With the backbone frozen, factual supervision and magnitude regularization jointly guide the learning of adaptive steering interventions, promoting factual reliability and stability throughout denoising. Experiments on two dLLMs show improved factual reliability on TruthfulQA and generalization across five downstream benchmarks.

## 8. CoSMO: Conformal Semantic Mapping for Open-World Safe Robot Navigation

- Authors: Shuqi Wang, Yiwei Zheng, Pingrui Zhang, Yue Gao, Xiang Yin
- Source hits: arxiv
- Matched researchers: Yue Gao
- Matched groups: N/A
- Confidence: medium (author_alias)
- Topic keywords: N/A
- Journal/source: arxiv
- Publication date: 2026-10-13
- Article: http://arxiv.org/abs/2610.18321v1

Safe autonomous navigation requires not only geometric obstacle avoidance but also semantic awareness. Different object categories demand different safety clearances, and the set of relevant categories may expand as the robot explores novel environments. Vision-language models (VLMs) offer rich semantic representations for building maps of unknown scenes, yet their confidence scores are poorly calibrated, making raw predictions unreliable for safety-critical planning. Conformal prediction (CP) can provide coverage guarantees, but existing methods assume a fixed label set and stationary data, limiting their use in open-world settings. We propose Conformal Semantic Mapping for Open-World Safe Robot Navigation (CoSMO), a semantic safety mapping framework that transforms VLM embeddings into calibrated coverage sets and safety-aware obstacle dilations over a dynamically expanding hazard vocabulary, even under distribution shift. Experiments on the Matterport3D (MP3D) dataset show that CoSMO reduces semantic collisions by 61.6% relative to a geometry-only baseline, while maintaining formal coverage guarantees even under delayed expert feedback. Real-world experiments on a quadruped robot further demonstrate generalization by achieving long-run empirical coverage of 90.73% against the 90% target. Project website: https://yangming911.github.io/cosmo-page/.

## 9. Color Lorentz force on a transversely polarized quark in the nucleon

- Authors: Ziqi Zhang, Chandan Mondal, Siqi Xu, Xingbo Zhao, James P. Vary
- Source hits: arxiv
- Matched researchers: Ziqi Zhang
- Matched groups: N/A
- Confidence: medium (author_alias)
- Topic keywords: N/A
- Journal/source: arxiv
- Publication date: 2026-10-13
- Article: http://arxiv.org/abs/2610.18063v1

The $x^2$ moment of the genuine twist-3 component of the unpolarized scalar parton distribution function $e(x)$ is related to the average transverse color Lorentz force experienced by a transversely polarized quark in an unpolarized nucleon. This higher-twist quantity probes quark--gluon correlations and provides unique insight into the nonperturbative dynamics of quantum chromodynamics. For the first time, we study the corresponding off-forward matrix element and derive its Lorentz-covariant decomposition in terms of generalized form factors. We calculate these form factors from light-front wave functions obtained by solving the light-front Hamiltonian eigenvalue problem within the Basis Light-Front Quantization framework. Their Fourier transforms provide a spatial picture of the transverse color forces in impact-parameter space. In particular, $\mathscr{F}_2$, whose forward limit is directly related to the twist-3 matrix element $e_2$, can be interpreted as the impact-parameter-space representation of the Boer--Mulders force, providing an intuitive spatial picture of the final-state interaction mechanism underlying the Boer--Mulders effect.
