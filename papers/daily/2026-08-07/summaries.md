# Paper Daily Reading - 2026-08-07

## 1. Multi-modal foundation model with whole-slide attention enables transferrable digital pathology at single-cell resolution

- Authors: Wu, Q., Gong, Q., Yuan, L., Li, Z., Ashenberg, O., Chen, F., Xavier, R., Uhler, C.
- Source: biorxiv
- Venue type: preprint
- Journal: biorxiv
- Publication status: preprint
- Publication date: 2026-08-06
- DOI: 10.64898/2026.07.31.741265
- Categories: bioinformatics
- Relevance: 3.7577788280630897
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://www.biorxiv.org/content/10.64898/2026.07.31.741265v1.full.pdf
- PDF: https://www.biorxiv.org/content/10.64898/2026.07.31.741265v1.full.pdf
- Local PDF: Not downloaded

Paired histopathology and spatial transcriptomics data are advancing our understanding of tissue biology and disease, but modeling both modalities at single-cell resolution while mapping local and distal cell-cell interdependencies remains computationally prohibitive. Here we introduce TissueFormer, a framework for pretraining foundation models with linear rather than quadratic computational complexity, overcoming a long-standing barrier to modeling long-range dependencies at scale. Trained on over 17 million image-expression pairs from 1.2K tissue slides, TissueFormer excels at predicting spatial gene expression from histology images at cellular resolution and scales to diagnostic tasks at the cell, region, and slide levels. Additionally, by identifying both long and short-range cell-cell interdependencies, our model enables the generation of testable hypotheses about disease mechanisms and staging, as demonstrated in lung fibrosis and breast cancer.

## 2. NodeJEPA: Structure-Conditioned Latent Prediction for Node-Level Graph Self-Supervised Learning

- Authors: Tinghe Zhang, Jian Xu, Jiaheng Chen, Jiaxing Li, Yucheng Xiao, Qiang Wang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-05
- DOI: Unavailable
- Categories: cs.LG, cs.AI
- Relevance: 3.699306332789617
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.04381v1
- PDF: https://arxiv.org/pdf/2608.04381v1
- Local PDF: pdf/2026-08-07_02_NodeJEPA_ Structure-Conditioned Latent Prediction for Node-Level Graph Self-Supervised Learning.pdf

Self-supervised learning on graphs is largely shaped by contrastive methods that depend on carefully designed augmentations, and by generative methods that reconstruct node attributes in the input space. Both paradigms can entangle representations with low-level input statistics rather than with relational structure. Joint-embedding predictive architectures (JEPA) instead learn by predicting latent targets rather than reconstructing inputs. Recent work has explored this idea for graph-level representation learning, but how to design JEPA-style objectives for node-level tasks, and which structural signals the predictor should condition on, remains less clear. We present NodeJEPA, a joint-embedding predictive architecture for node-level graph self-supervised learning. NodeJEPA masks structure-aware k-hop ego-subgraphs and trains a context encoder to predict the latent representations of the masked nodes. These targets come from an EMA-updated target encoder with stop-gradient. A structure-conditioned predictor integrates spectral and centrality descriptors through cross-attention. Variance, covariance, and Laplacian spectral regularizers help stabilize the embedding geometry, and an optional curriculum gradually increases masking difficulty during training. Because prediction occurs in latent space, NodeJEPA does not rely on input reconstruction or hand-crafted graph augmentations. We evaluate NodeJEPA on standard node classification benchmarks under linear probing and fine-tuning protocols, and conduct ablations on masking, prediction, and regularization design choices. Our study offers a practical recipe for node-level JEPA-style latent prediction on graphs, and clarifies when structural conditioning helps representation learning. Code, configurations, and evaluation scripts are publicly available at https://github.com/OliverZ-dot/Node-Jepa.

## 3. Hierarchical Graph Memory for LLM Agents with Path-level Localization and Rewrite

- Authors: Xiawei Yue, Boran Wang, Xiaoqing Zhang, Shuxin Zheng, Ziwei Zhang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-05
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 3.2289979835217766
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.05095v1
- PDF: https://arxiv.org/pdf/2608.05095v1
- Local PDF: pdf/2026-08-07_03_Hierarchical Graph Memory for LLM Agents with Path-level Localization and Rewrite.pdf

Agents for long term reasoning require a memory that can be efficiently and effectively updated over time, as new facts and external feedback continue to arrive. Recently, graph memory has been adopted to offer structural organization for multi-hop retrieval and reasoning. However, existing methods store all memories in a flat graph, and accumulated historical memories can introduce irrelevant contexts and increase the cost of evidence selection during retrieval. Moreover, they typically update memory units independently, requiring repeated unit-wise rewrite to cover related changes. To address these issues, we propose HiGram, an evolving hierarchical graph memory framework with path-level localization and rewriting. Specifically, we first propose a hierarchical graph memory, which organizes the memory into coarse-to-fine architecture composed of upper-level nodes and MemoryUnits, thereby reducing the amount of irrelevant information during retrieval. We further propose MicroGraph-based path-level localization, which leverages query and update conditioned MicroGraphs to identify support subgraph and evidence path before rewrite. Finally, we propose a coordinated rewriting method that jointly revises intra-unit memory and inter-unit dependencies, enable valid dependency structures updating in the localized evidence path. Experiments on benchmarks for long-term conversational question answering and conflict-aware memory evaluation demonstrate that our method demonstrate substantial improvements over baselines in answer quality and token efficiency. Besides, our method improves answer accuracy and query-valid evidence selection under dynamic, static, and conditional conflicts.

## 4. CSGen: A Multi-Domain Curvilinear Structure Generation Model via Hierarchical Multimodal Diffusion

- Authors: Zhe Shan, Ziming Yang, Lei Zhou, Wenwen Zhang, Cong Lin, Xia Xie
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-05
- DOI: Unavailable
- Categories: cs.CV, cs.AI
- Relevance: 3.200340772860727
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.04655v1
- PDF: https://arxiv.org/pdf/2608.04655v1
- Local PDF: pdf/2026-08-07_04_CSGen_ A Multi-Domain Curvilinear Structure Generation Model via Hierarchical Multimodal Diffusion.pdf

Curvilinear structure analysis is an important and fundamental task in multimedia. However, the controllable generation of images with precise curvilinear structure objects remains an open challenge. To address this, we propose CSGen, a hierarchical multimodal diffusion model that synthesizes high-fidelity images precisely aligned with multiple control conditions. The CSGen is built upon three key innovations: 1) We construct a multi-domain and multimodal dataset, including over 24K samples from 5 domains and 7 different types of annotations, to train the unified generation model. 2) We propose a novel hierarchical progressive control strategy that decouples topology clues from visual context by a phased signal injection, mitigating semantic drift while ensuring the topological integrity of sparse structures. 3) We design a sparsity-aware loss re-weighting mechanism to address the extreme sparsity of curvilinear structures, significantly enhancing the attention on thin and fragile structures during optimization. Extensive experiments demonstrate that CSGen generates images with superior structure accuracy and visual realism, significantly improving downstream segmentation performance while maintaining robustness across diverse prompts. Our results confirm CSGen as a scalable, data-centric paradigm for the analysis of complex curvilinear structures in diverse multimedia applications. Code and dataset are available at https://github.com/ShanZard/CSGen.

## 5. Attention, Anomalies! Handling Attention Layers in Unsupervised Federated Outlier Detection

- Authors: Mihailo Ilić, Miloš Savić, Vladimir Kurbalija, Mirjana Ivanović, Giancarlo Fortino, Dušan Jakovetić
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-05
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.184251229468311
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.04753v1
- PDF: https://arxiv.org/pdf/2608.04753v1
- Local PDF: pdf/2026-08-07_05_Attention, Anomalies! Handling Attention Layers in Unsupervised Federated Outlier Detection.pdf

Attention layers are the backbone of today's most powerful and impactful models. Models with multi-million and billion parameters rely on contextual knowledge provided by attention layers. However, their use goes well beyond just being the core component of large language models. One particularly interesting application is in Memory Augmented Autoencoders (MemAE), specifically for unsupervised representation learning in outlier detection tasks. It was shown that attention helps these models be more effective in centralized learning scenarios. Our work aims to address the lack of specialized aggregation techniques in Federated Learning (FL) when it comes to MemAE models. In this paper we analyze the intricacies of the architecture behind Memory Augmented Autoencoders, and propose novel, guided approaches to effectively aggregate these models in federated scenarios. We demonstrate our approach on non-IID datasets and show that these novel aggregation schemes are more robust when dealing with numerous edge nodes in environments with unbalanced datasets, specifically for unsupervised anomaly detection scenarios. This approach improves the performance of even very shallow autoencoders, allowing them to be used in resource constrained environments.

## 6. SVI-DAG: A Structured Variational Inference Approach to Bayesian Causal Discovery

- Authors: Shrenik Zinage
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-05
- DOI: Unavailable
- Categories: cs.LG, cs.AI
- Relevance: 3.178683898924459
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.04930v1
- PDF: https://arxiv.org/pdf/2608.04930v1
- Local PDF: pdf/2026-08-07_06_SVI-DAG_ A Structured Variational Inference Approach to Bayesian Causal Discovery.pdf

Bayesian causal discovery seeks to determine the posterior distribution of causal theories, which are interpreted as directed acyclic graphs (DAGs) that explain the observed data. The resulting posterior allows systematic reasoning regarding epistemic uncertainty within these theories. Nonetheless, finding such graphs is difficult due to identifiability problems and limited observational data. Furthermore, precisely approximating posterior over graphs is challenging given vast range of potential DAGs. Recent Bayesian approaches have addressed some of these challenges, yet they remain limited as they fail to encode dependencies between edges, and lack principled ways to incorporate domain knowledge as inductive biases during the search process. To overcome these limitations, we propose SVI-DAG, a structured variational inference approach to Bayesian causal discovery using observational data and prior beliefs that uses normalizing flows to model dependencies between edges, supporting expressive and multimodal posterior learning over DAGs. To mitigate mode seeking behaviour in evidence lower bound optimization and promote mode coverage, we use stein variational gradient descent to update the node potentials using a kernel in acyclicity space. We evaluate SVI-DAG against 5 state-of-the-art Bayesian DAG learning methods and demonstrate superior performance in uncertainty quantification while remaining competitive in terms of structural accuracy.

## 7. Intrinsic-Hybrid Latent Diffusion Models for Generative Modeling on Unknown Manifolds

- Authors: Yizhu Wang, Mu Niu, Xiaochen Yang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-05
- DOI: Unavailable
- Categories: stat.ML, cs.LG
- Relevance: 3.159423904813644
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.04827v1
- PDF: https://arxiv.org/pdf/2608.04827v1
- Local PDF: pdf/2026-08-07_07_Intrinsic-Hybrid Latent Diffusion Models for Generative Modeling on Unknown Manifolds.pdf

We introduce the Intrinsic Hybrid Latent Diffusion Model (ILDM), a generative framework that integrates probabilistic dimensionality reduction with geometry-aware diffusion on unknown manifolds. While diffusion models (DMs) have achieved state-of-the-art results in high-dimensional data synthesis, they rely on large training datasets and ignore intrinsic geometric structure. Latent diffusion models (LDMs) address the high dimensionality by learning a latent space, but they typically impose a Euclidean structure, failing to capture the underlying manifold geometry, especially problematic in data-sparse regimes. ILDM addresses these limitations by interpreting the latent space as a chart of an unknown Riemannian manifold, with geometry and uncertainty quantified through a probabilistic decoder. The forward process is a hybrid diffusion that switches between Riemannian and Euclidean dynamics based on local uncertainty, where the Riemannian component is governed by a probabilistic metric tensor derived from the decoder. To learn the generative dynamics, we introduce an approximate denoising score matching method tailored to the hybrid diffusion setting, enabling a backward process defined by hybrid Langevin dynamics. Experiments on COIL-100, MNIST, and cardiac MRI datasets demonstrate that ILDM significantly improves generation quality, achieving lower FID and LPIPS scores compared to standard diffusion and latent diffusion models.

## 8. A Model Merging Approach for Continual MLLM Unlearning

- Authors: Yuhang Wang, Linlin Zhang, Haoxuan Ji, Xianmin Ye, Zhenxing Niu, Haichang Gao
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-05
- DOI: Unavailable
- Categories: cs.LG, cs.AI
- Relevance: 3.0846898304219668
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.04548v1
- PDF: https://arxiv.org/pdf/2608.04548v1
- Local PDF: pdf/2026-08-07_08_A Model Merging Approach for Continual MLLM Unlearning.pdf

Multimodal large language model (MLLM) unlearning methods have been proposed to remove private, sensitive, or proprietary information from well-trained models. However, most existing MLLM unlearning methods are designed for one-shot requests and fail to adequately address continual scenarios, as repeatedly applying one-shot operations leads to cumulative utility degradation, unlearning rebound, and retention drift. We introduce Merging for Continual Unlearning (MCU), an approach that dynamically merges multiple one-shot unlearning adapters into a unified adapter upon receiving each new unlearning request.Through a leave-one-out merging analysis, we reveal that these unlearning adapters exhibit strong cross-task dependencies. Such dependencies have two contrasting effects: they can facilitate cross-task unlearning transferability, but they can also introduce severe interference that degrades unlearning effectiveness and compromises retained knowledge. To address this challenge, MCU projects the adapters into a shared representation space, preserves their dominant directions, suppresses over-concentrated coordinates, and reconfigures cross-task dependencies to mitigate interference while enhancing transferability. Experiments on ICU-Bench and MLLMU-Bench demonstrate that MCU achieves superior unlearning effectiveness while preserving both retained knowledge and general multimodal utility.

## 9. Protoreasoning in Tiny Transformers

- Authors: Eduardo Valle, Fergal Reid
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-05
- DOI: Unavailable
- Categories: cs.CL, cs.AI, cs.LG
- Relevance: 3.0295514683290965
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.04980v1
- PDF: https://arxiv.org/pdf/2608.04980v1
- Local PDF: pdf/2026-08-07_09_Protoreasoning in Tiny Transformers.pdf

We show that tiny transformers can profitably employ a simple form of Chain of Thought, which we call protoreasoning, allowing us to study step-by-step reasoning on ~1M-parameter models and opening up opportunities for much more detailed experimentation and analysis than is feasible for larger models. Current Large Language Models exhibit impressive step-by-step reasoning, but we have yet to understand its generality, i.e., when and how LLMs learn genuinely general algorithms rather than "bags of heuristics." Such questions are hard to settle on compute-intensive frontier models trained on opaque data. To work at model scales far below the threshold for natural-language competence, we define reasoning-friendly tasks on Dyck languages (sentences of correctly nested brackets). We find that protoreasoning traces substantially close the out-of-distribution generalization gap, and ablations confirm that the trace's content, not merely its extra tokens, drives the gain.

## 10. EndoVLM: An Endoscopy Vision-Language Pre-training Model via Anatomy-Guided Sparsity and Progressive Alignment

- Authors: Zhenyu Yi, Jianwei Xu, Yue Hu, Zhongwei Qiu, Sijing Li, Liang Huang, Bin Lv, Ling Zhang, Yingda Xia
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-05
- DOI: Unavailable
- Categories: cs.CV, cs.AI, cs.CL
- Relevance: 3.0232749385796147
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.04472v1
- PDF: https://arxiv.org/pdf/2608.04472v1
- Local PDF: pdf/2026-08-07_10_EndoVLM_ An Endoscopy Vision-Language Pre-training Model via Anatomy-Guided Sparsity and Progressive Alignment.pdf

The development of foundation models (FMs) is crucial for advancing endoscopic image analysis. However, existing endoscopy FMs mainly rely on self-supervised learning from uni-modal images or videos, overlooking the rich semantic knowledge contained in clinical reports. Furthermore, effectively leveraging these records is hindered by a fundamental modality gap: structured anatomical descriptions are not naturally mapped to specific frames within the high-redundancy, uncurated visual streams. In this paper, we present EndoVLM, a novel vision-language FM pre-trained on over 348K endoscopic examinations, each pairing a clinical report with its corresponding image collection. An Anatomy-Guided Sparse Pooling mechanism utilizes textual descriptions as queries to drive sparse attention, efficiently aggregating semantically salient frames into anatomy-specific visual representations across redundant image-sets. Next, a Progressive Semantic-Aware Alignment strategy models clinical taxonomy (anatomy and pathological status) via structured soft targets, bridging the gap from global patient-level matching to fine-grained localized alignment. Finally, a Semantic-Concentrated Masked Autoencoder is applied exclusively to these semantic-rich frames, integrating low-level visual precision with robust high-level semantic representation. Extensive experiments across various downstream tasks demonstrate that EndoVLM outperforms existing foundation models and remains competitive with task-specific methods. Remarkably, EndoVLM also exhibits robust zero-shot generalization capabilities, highlighting its potential for broader clinical application.

## 11. EvolveNet: Collaborative Harness Evolution for Agent Self-Improvement

- Authors: Jun Nie, Yonggang Zhang, Qianshu Cai, Yiu-ming Cheung, Xinmei Tian, Bo Han
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-05
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 2.9988741522448246
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.04968v1
- PDF: https://arxiv.org/pdf/2608.04968v1
- Local PDF: pdf/2026-08-07_11_EvolveNet_ Collaborative Harness Evolution for Agent Self-Improvement.pdf

The capabilities of an LLM agent depend not only on its model but on the harness: the executable program that constructs context, invokes tools, verifies results, and recovers from failure. Recent work shows that evolving the harness yields persistent improvements without updating model weights. Existing approaches, however, assume that all execution experience can be routed to a single optimizer, which evolves one harness along a sequential trajectory. Real agent ecosystems violate that assumption: users, organizations, and environments generate isolated streams of experience that cannot be pooled, so the experience most worth learning from is exactly the experience that cannot be directly centralized. We introduce EvolveNet, a paradigm of collaborative harness evolution that moves experience extraction to the data. A shared harness is broadcast to data-local agent deployments, each of which evolves it on its own workload. Only the resulting program adaptations are composed into an updated shared harness and redistributed, so that every participating agent inherits operational experience discovered by the others. By shifting the aggregation boundary from raw workloads to learned adaptations, EvolveNet keeps workloads local and allows multiple evolutionary searches to proceed concurrently with reduced serial depth. Because independently modified programs cannot be averaged like model parameters and may conflict when composed, EvolveNet introduces scope-typed, evidence-guided program aggregation. Across five settings spanning text-to-SQL, data-science coding, competitive programming, software engineering, and agentic workflows, EvolveNet improves the shared harness in all five, with the largest gains under heterogeneous workloads, and ablations attribute the improvement to composition of adaptations from different agents rather than to selecting among them.

## 12. Canonical Joint Energy-Based Model on CIFAR-10: failure modes and practical indistinguishability of Predictor-Corrector and SGLD samplers

- Authors: Dmytro Knopov
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-05
- DOI: Unavailable
- Categories: cs.LG, stat.ML
- Relevance: 2.988549862052462
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.05025v1
- PDF: https://arxiv.org/pdf/2608.05025v1
- Local PDF: pdf/2026-08-07_12_Canonical Joint Energy-Based Model on CIFAR-10_ failure modes and practical indistinguishability of Predictor-Corrector.pdf

Joint Energy-Based Models (JEM) unify classification and generation within a single network and support out-of-distribution (OOD) detection. Canonical JEM training relies on stochastic gradient Langevin dynamics (SGLD); a theoretically motivated alternative, the Predictor-Corrector (PC) sampler, has not previously undergone a systematic replication test on the canonical model. We reproduce canonical JEM on WideResNet-28-10 without normalisation layers on two independent runs and test whether PC retains its theoretical advantage without an annealed noise schedule, across three protocols: PC replacing SGLD throughout the roughly 130 training epochs; cold-start generation (FID); and refinement-style multi-OOD detection (AUROC). The reconstruction reaches 92.88% test accuracy and buffer-FID 44.46 (canonical: 92.9% and 38.40). We document two failure modes: catastrophic late-training divergence via the canonical outlier-buffer mechanism (both SGLD runs and, with the same signature, both PC runs), and run-dependent SVHN OOD-discrimination dynamics. No method-level advantage of PC over SGLD is observed on any protocol: at inference the absolute AUROC difference stays below 0.007 across all ten checkpoint-OOD pairs and the FID difference below 0.5; on the training protocol a hierarchical seed-by-image bootstrap gives a 95% confidence interval on the macro-averaged AUROC difference that contains zero, while a seed-level equivalence test with two runs per method cannot establish formal equivalence. The data are consistent both with equivalence and with a small directional effect. This practical indistinguishability is theoretically expected: under fixed noise the PC predictor step degenerates by construction, so its guarantees do not transfer to canonical JEM.

## 13. Q-CueGraph: Query-Conditioned Visual Evidence Graphs for Multimodal Reasoning

- Authors: Pengcheng Pan, Xinfang Zhang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-05
- DOI: Unavailable
- Categories: cs.CV, cs.AI, cs.CL
- Relevance: 2.927571060782786
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.04452v1
- PDF: https://arxiv.org/pdf/2608.04452v1
- Local PDF: pdf/2026-08-07_13_Q-CueGraph_ Query-Conditioned Visual Evidence Graphs for Multimodal Reasoning.pdf

High-resolution pixels and crop or zoom tools give multimodal large language models the ability to inspect an image, but they do not provide a reliable task-conditioned policy for deciding where to inspect. Q-CueGraph makes this decision explicit. It maps a question and an image representation to budgeted, coordinate-level observations for a frozen reader. Text-rich images use a reusable OCR/layout graph; natural-image search instantiates query-conditioned visual nodes behind the same selection, composition, and budgeting interface. Optional utility refinement learns which candidate crops the frozen reader can use from training-answer correctness, without region-box supervision. With a frozen Qwen2.5-VL-7B reader, Q-CueGraph reaches 0.833 accuracy on V*Bench versus 0.696 for full-image inference from a 19% image-area budget, and reaches 92% of full-image ANLS on InfographicVQA from about half the image area. Across six benchmarks, explicit observation is most valuable when evidence is localizable, the question discriminates its location, and resolution limits full-image reading.

## 14. D$^2$F-ReAG: Dynamic Decomposition and Filtering for Multi-Hop Reasoning-Augmented Generation

- Authors: Jiaoyang Li, Junhao Ruan, Shengwei Tang, Kaiyan Chang, Zhengtao Yu, Tong Xiao, Jingbo Zhu
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-05
- DOI: Unavailable
- Categories: cs.CL, cs.AI
- Relevance: 2.9273399471347714
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.04444v1
- PDF: https://arxiv.org/pdf/2608.04444v1
- Local PDF: pdf/2026-08-07_14_D$^2$F-ReAG_ Dynamic Decomposition and Filtering for Multi-Hop Reasoning-Augmented Generation.pdf

Large language models (LLMs) often generate inaccurate answers due to their reliance on static internal knowledge. Retrieval-augmented generation (RAG) addresses this limitation by integrating external knowledge and excelling at single-hop queries. However, it struggles with multi-hop questions that require cross-document reasoning. Existing methods, such as graph structured RAG or question decomposition, often lack dynamic decomposition and effective filtering, which leads to lower efficiency and accuracy. To overcome these limitations, we propose Dynamic Decomposition and Filtering for Multi-Hop Reasoning-Augmented Generation (D2F-ReAG), a novel paradigm that adaptively controls reasoning depth by judging the reliability of the root-level reasoning. If the root reasoning is reliable, the model directly generates the answer. Otherwise, the question is logically decomposed into sub-questions, and the verified reasoning derived from these sub-questions is used to refine the root reasoning. Experiments on three multi-hop benchmarks demonstrate the effectiveness of our method in handling complex multi-hop questions.

## 15. When does training on downscaled images yield the same gradients?

- Authors: Seunghyun Ji
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-05
- DOI: Unavailable
- Categories: cs.CV, cs.AI
- Relevance: 2.9094552267057154
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.04448v1
- PDF: https://arxiv.org/pdf/2608.04448v1
- Local PDF: pdf/2026-08-07_15_When does training on downscaled images yield the same gradients.pdf

Diffusion transformers deliver strong image generation, but their training cost grows superlinearly with resolution. Recent work justifies training or sampling at reduced resolution on a spectral premise: at high noise, a downscaled latent preserves almost the full surviving signal. Whether a downscaled step also preserves the native training gradient signal, however, has remained unresolved. We reduce how that signal changes under downscaling to two terms: a noise-dependent term governed by the downscale ratio, which decays at high noise as the spectral premise predicts, and a σ-independent floor governed by the target grid's absolute token count, carried by the compute graph itself and removed by no noise level. The measured (route, σ) map corroborates the account and uncovers structure the spectral picture cannot express: on the 1024->768 route, a window (0.65 < σ< 0.95), predicted by no spectral criterion at any tolerance, where the downscaled gradient stays within a small margin of the native one. Training LoRA adapters with downscaled steps restricted to the routes and noise windows the map validates reduces training time by 14.6% at a fixed step budget while remaining near-native in weight space. Code is available at https://github.com/sorryhyun/anima_lora.

## 16. Leak-Resistant Unlearning: A New Benchmark for Evaluating Multi-Hop Reasoning Consistency and Recovery Robustness

- Authors: Haoting Qian, Qingjie Zhang, Zhicong Huang, Cheng Hong, Han Qiu
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-05
- DOI: Unavailable
- Categories: cs.AI, cs.CL
- Relevance: 2.874914797728005
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.04519v1
- PDF: https://arxiv.org/pdf/2608.04519v1
- Local PDF: pdf/2026-08-07_16_Leak-Resistant Unlearning_ A New Benchmark for Evaluating Multi-Hop Reasoning Consistency and Recovery Robustness.pdf

Benchmarking machine unlearning methods is critical to understand whether sensitive knowledge is removed from large language models (LLMs) or not. Current unlearning benchmarks include mainly single-hop questions and a narrow set of multi-hop questions. Although effective, they still face two challenges. (1) Knowledge is not isolated, whereby diverse multi-hop reasoning paths can potentially induce knowledge leakage than normal queries. (2) Unlearning may be fragile: unlearned knowledge can be partially recovered through recovery attacks such as lightweight post-unlearning adaptation, making static evaluation insufficient. Therefore, in this paper, we introduce \unlearning as a novel benchmark to understand robust LLM knowledge removal across diverse reasoning paths and recovery attacks. We experiment with this benchmark on 3 models, 6 unlearning methods, and 2 carefully curated datasets. Results show that existing methods are vulnerable to multi-hop reasoning paths and recovery attacks. We further explore the trade-off among forget quality, robustness, and model utility for LLM unlearning.

## 17. The Neural Echo: A Signal Processing Perspective for Understanding Neural Networks

- Authors: Chongbiao Wang, Daniel Gaa, Joachim Weickert, Karl Schrader
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-05
- DOI: Unavailable
- Categories: eess.SP, cs.LG
- Relevance: 2.851172169078972
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.04864v1
- PDF: https://arxiv.org/pdf/2608.04864v1
- Local PDF: pdf/2026-08-07_17_The Neural Echo_ A Signal Processing Perspective for Understanding Neural Networks.pdf

We introduce the neural echo as a tool for understanding the behavior of neural networks. It generalizes the model-based concepts of impulse responses, diffusion echoes, and filter echoes to learning-based methods. It provides local, space-adaptive impulse responses and filter kernels for a neural network, its so-called echoes. These echoes depend on the input image and can be visualized to understand the learned dynamics of the network via an affine mapping. Neural echoes build a bridge from classical signal processing to modern explainable AI. They are very general and can be applied to both image-to-image and classification networks, with convolutional or fully connected structure, of feedforward or recurrent type, including modern transformer networks. Network differentiability is not required. In the differentiable case, neural echoes comprise concepts based on the network Jacobian, such as saliency maps and the analysis of adversarial perturbations, as special instances. As a simple blueprint to explain our framework, we derive neural echoes for the denoising convolutional neural network (DnCNN). Our experiments suggest that this network weights pixels based on their spatial and gray value distances. This not only clarifies its behavior, but also shows that it can reproduce key concepts of classical model-based denoisers such as bilateral filtering.

## 18. Training-Free Hashing-Based Attention via Binary Principal Components

- Authors: Daohai Yu, Zhanpeng Zeng, Keyu Chen, Wenhao Li, Zhifeng Shen, Luxi Lin, Ruizhi Qiao, Xing Sun, Rongrong Ji
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-05
- DOI: Unavailable
- Categories: cs.LG, cs.AI, cs.CL
- Relevance: 2.8472740358730473
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.04405v1
- PDF: https://arxiv.org/pdf/2608.04405v1
- Local PDF: pdf/2026-08-07_18_Training-Free Hashing-Based Attention via Binary Principal Components.pdf

Long-context large language models (LLMs) are increasingly deployed in real-world applications, yet self-attention remains a major efficiency bottleneck -- especially during decoding -- due to the necessity of repeatedly processing ever-growing key-value (KV) caches. Existing sparse attention reduce computation by attending to fewer KV pairs, but often suffer from substantial accuracy degradation, require additional training, or rely on expensive hashing. In this work, we present BinaryPC, a training-free, data-aware hashing-based sparse attention for long-context LLMs. BinaryPC constructs compact binary hash codes and corresponding hash function by computing binary principal components of data. Unlike Locality-Sensitive Hashing (LSH) with data-independent random projections or learned non-linear hashing methods, BinaryPC constructs binary codes that explicitly preserve the structural information of data without requiring gradient-based training. Comprehensive experiments across multiple model families and long-context benchmarks show that BinaryPC preserves accuracy relative to full attention while achieving superior performance among sparse and hashing-based baselines. On modern GPUs, BinaryPC improves end-to-end decoding throughput by 3.56$\times$ over the FlashAttention kernel. Our code is available at https://github.com/yudaohai666/BPC.

## 19. Chained Recursive Language Models for Multi-Iteration Reasoning

- Authors: Purbesh Mitra, Sennur Ulukus
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-05
- DOI: Unavailable
- Categories: cs.CL, cs.AI, cs.IT, cs.LG, eess.SP
- Relevance: 2.841218056624626
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.05124v1
- PDF: https://arxiv.org/pdf/2608.05124v1
- Local PDF: pdf/2026-08-07_19_Chained Recursive Language Models for Multi-Iteration Reasoning.pdf

Long context reasoning in large language models (LLMs) is usually constrained by the fact that a single inference trajectory has to simultaneously explore the context, store intermediate state, verify evidence, and produce the final answer. This becomes particularly difficult in tasks that require extraction, counting, ordering, or multi-hop reasoning, where an early mistake can propagate until the final response. In this work, we propose Chained Recursive Language Models (Chained RLM), an inference-time architecture, in which the same underlying model is called repeatedly as a sequence of fresh reasoning roots. Each root receives the original problem and context, but does not inherit the full conversational history. Instead, it receives a compact plain-text summary, a plain-text blackboard, and some durable task-specific artifacts written by predecessor roots. The motivation is to manage the context by chopping into partial tasks rather than one large inference response; in each staged computation, intermediate artifacts can be inspected, corrected, and extended by a later fresh inference by the same model. We describe the system model, handoff mechanism, artifact workspace, and evaluation protocol for this system. We study when fresh-context artifact continuation gives a measurable gain in accuracy over direct LLM answering even with recursive tool-calling.

## 20. AutoProteinEngine: A Large Language Model Driven Agent Framework for Multimodal AutoML in Protein Engineering

- Authors: Yungeng Liu, Zan Chen, Yu Guang Wang, Yiqing Shen
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2024-11-07
- DOI: Unavailable
- Categories: q-bio.QM, cs.AI
- Relevance: 2.8404862523970618
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2411.04440v1
- PDF: https://arxiv.org/pdf/2411.04440v1
- Local PDF: pdf/2026-08-07_20_AutoProteinEngine_ A Large Language Model Driven Agent Framework for Multimodal AutoML in Protein Engineering.pdf

Protein engineering is important for biomedical applications, but conventional approaches are often inefficient and resource-intensive. While deep learning (DL) models have shown promise, their training or implementation into protein engineering remains challenging for biologists without specialized computational expertise. To address this gap, we propose AutoProteinEngine (AutoPE), an agent framework that leverages large language models (LLMs) for multimodal automated machine learning (AutoML) for protein engineering. AutoPE innovatively allows biologists without DL backgrounds to interact with DL models using natural language, lowering the entry barrier for protein engineering tasks. Our AutoPE uniquely integrates LLMs with AutoML to handle model selection for both protein sequence and graph modalities, automatic hyperparameter optimization, and automated data retrieval from protein databases. We evaluated AutoPE through two real-world protein engineering tasks, demonstrating substantial performance improvements compared to traditional zero-shot and manual fine-tuning approaches. By bridging the gap between DL and biologists' domain expertise, AutoPE empowers researchers to leverage DL without extensive programming knowledge. Our code is available at https://github.com/tsynbio/AutoPE.

## 21. RAG-Stack: Co-Optimizing RAG Serving Performance and Quality

- Authors: Haiqiang Zhang, Yuanqing Lei, Wanting Li, Tao Zhang, Wenqi Jiang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-04
- DOI: Unavailable
- Categories: cs.DB, cs.AI, cs.IR
- Relevance: 2.8155392954916185
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.03487v1
- PDF: https://arxiv.org/pdf/2608.03487v1
- Local PDF: pdf/2026-08-07_21_RAG-Stack_ Co-Optimizing RAG Serving Performance and Quality.pdf

Retrieval-augmented generation (RAG), which augments large language model (LLM) generation with information retrieved from databases, has become a widely used approach for knowledge-intensive applications. Modern RAG systems, however, expose many configuration choices, such as retrieval indexes, model selections, and how models invoke retrieval. Each configuration yields a different trade-off between answer quality and serving performance, making it challenging to choose the optimal setting for a specific application deployment. We present RAG-Stack, a framework for efficiently discovering quality-performance Pareto frontiers across diverse RAG applications and serving systems. RAG-Stack consists of RAG-PE, an iterative design-space exploration algorithm that selects the next RAG configuration to evaluate; RAG-IR, a workload abstraction for diverse RAG algorithms; and RAG-CM, a performance model that predicts the optimal deployment and serving performance on the given hardware. Together, these components allow RAG-Stack to search the joint algorithm-system configuration space without deploying every candidate and to transfer an existing Pareto frontier to a new serving system. Given the same number of optimization iterations across diverse datasets, the Pareto frontiers found by RAG-Stack cover 52.5% to 153.2% more of the normalized quality-performance space than those found by state-of-the-art configuration-search methods evaluated over the same RAG design space.

## 22. Why Does Reinforcement Learning Generalize? A Feature-Level Mechanistic Study of Post-Training in Large Language Models

- Authors: Dan Shi, Zhuowen Han, Simon Ostermann, Renren Jin, Josef van Genabith, Deyi Xiong
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.8114614598120613
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1808/
- PDF: https://aclanthology.org/2026.acl-long.1808.pdf
- Local PDF: pdf/2026-08-07_22_Why Does Reinforcement Learning Generalize_ A Feature-Level Mechanistic Study of Post-Training in Large Language Models.pdf

Reinforcement learning (RL)-based post-training often improves the reasoning performance of large language models (LLMs) beyond the training domain, while supervised fine-tuning (SFT) frequently leads to general capabilities forgetting. However, the mechanisms underlying this contrast remain unclear.To bridge this gap, we present a feature-level mechanistic analysis methodology to probe RL generalization using a controlled experimental setup, where RL- and SFT-tuned models are trained from the same base model on identical data. Leveraging our interpretability framework, we align internal activations across models within a shared feature space and analyze how features evolve during post-training.We find that SFT rapidly introduces many highly specialized features that stabilize early in training, whereas RL induces more restrained and continually evolving feature changes that largely preserve base models’ representations. Focusing on samples where RL succeeds but the base model fails, we identify a compact, task-agnostic set of features that directly mediate generalization across diverse tasks. Feature-level interventions confirm their causal role: disabling these features significantly degrades RL models’ generalization performance, while amplifying them improves base models’ performance. The code is available at https://github.com/danshi777/RL-generalization .

## 23. Debiasing Reward Models via Causally Motivated Inference-Time Intervention

- Authors: Kazutoshi Shinoda, Kosuke Nishida, Kyosuke Nishida
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.811000320478605
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1029/
- PDF: https://aclanthology.org/2026.acl-long.1029.pdf
- Local PDF: pdf/2026-08-07_23_Debiasing Reward Models via Causally Motivated Inference-Time Intervention.pdf

Reward models (RMs) play a central role in aligning large language models (LLMs) with human preferences. However, RMs are often sensitive to spurious features such as response length. Existing inference-time approaches for mitigating these biases typically focus exclusively on response length, resulting in performance trade-offs. In this paper, we propose causally motivated intervention for mitigating multiple types of biases in RMs at inference time. Our method first identifies neurons whose activations are strongly correlated with predefined bias attributes, and applies neuron-level intervention that suppresses these signals. We evaluate our method on RM benchmarks and observe reductions in sensitivity to spurious features across diverse bias types, without inducing performance trade-offs. Moreover, when used for preference annotation, small RMs (2B and 7B) with our method, which edits less than 2% of all the neurons in RMs, enable LLMs to improve alignment, achieving performance comparable to that of a state-of-the-art 70B RM on AlpacaEval and MT-Bench. Further analysis reveals that bias signals are primarily encoded by neurons in early layers, shedding light on the internal mechanisms of bias exploitation in RMs.

## 24. A Survey of Inductive Reasoning for Large Language Models

- Authors: Kedi Chen, Dezhao Ruan, Yuhao Dan, Yaoting Wang, Siyu Yan, Xuecheng Wu, Yinqi Zhang, Qin Chen, Jie Zhou, Liang He, Biqing Qi, Linyang Li, Qipeng Guo, Xiaoming Shi, Wei Zhang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.810050607815339
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1447/
- PDF: https://aclanthology.org/2026.acl-long.1447.pdf
- Local PDF: pdf/2026-08-07_24_A Survey of Inductive Reasoning for Large Language Models.pdf

Reasoning is an important task for large language models (LLMs). Among all the reasoning paradigms, inductive reasoning is one of the basic types, which is characterized by its particular-to-general thinking process and the non-uniqueness of its answers. The inductive mode is crucial for knowledge generalization and aligns better with human cognition, so it is a fundamental mode of learning, hence attracting increasing interest. Despite the importance of inductive reasoning, there is no systematic summary of it. Therefore, this paper presents the first comprehensive survey of inductive reasoning for LLMs. First, methods for improving inductive reasoning are categorized into three main areas: post-training enhancement, test-time exploration, and data augmentation. Then, current benchmarks of inductive reasoning are summarized, and a unified sandbox-based evaluation approach with the observation coverage metric is derived. Finally, we offer some analyses regarding the source of inductive ability and how simple model architectures and data help with inductive tasks, providing a solid foundation for future research.

## 25. SciImpact: A Multi-Dimensional, Multi-Field Benchmark for Scientific Impact Prediction

- Authors: Hangxiao Zhu, Yuyu Zhang, Ping Nie, Yu Zhang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.80999519831022
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1445/
- PDF: https://aclanthology.org/2026.findings-acl.1445.pdf
- Local PDF: pdf/2026-08-07_25_SciImpact_ A Multi-Dimensional, Multi-Field Benchmark for Scientific Impact Prediction.pdf

The rapid growth of scientific literature calls for automated methods to assess and predict research impact.Prior work has largely focused on citation-based metrics, leaving limited evaluation of models’ capability to reason about other impact dimensions.To this end, we introduce SciImpact, a large-scale, multi-dimensional benchmark for scientific impact prediction spanning 19 fields.SciImpact captures various forms of scientific influence, ranging from citation counts to award recognition, media attention, patent reference, and artifact adoption, by integrating heterogeneous data sources and targeted web crawling.It comprises 215,928 contrastive paper pairs reflecting meaningful impact differences in both short- (e.g., Best Paper Award) and long-term settings (e.g., Nobel Prize).We evaluate 11 widely used large language models (LLMs) on SciImpact.Results show that off-the-shelf models show substantial variability across dimensions and fields, while multi-task supervised fine-tuning consistently enables smaller LLMs (e.g., 4B) to markedly outperform much larger models (e.g., 30B) and surpass powerful closed-source LLMs (e.g., o4-mini).These results establish SciImpact as a challenging benchmark and demonstrate its value for multi-dimensional, multi-field scientific impact prediction.Our project homepage is https://flypig23.github.io/sciimpact-homepage/ .

## 26. Your Reasoning Model is Secretly a Reward Model - Optimization-Free Verification from Experience

- Authors: Zhenwen Liang, Ruosen Li, Yujun Zhou, Linfeng Song, Dian Yu, Xinya Du, Haitao Mi, Dong Yu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.808873914549782
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.788/
- PDF: https://aclanthology.org/2026.acl-long.788.pdf
- Local PDF: pdf/2026-08-07_26_Your Reasoning Model is Secretly a Reward Model - Optimization-Free Verification from Experience.pdf

Assessing the quality of Large Language Model (LLM) outputs becomes especially challenging in high-branching settings, where a single prompt yields many plausible candidates. Existing verifiers typically operate on the surface text (e.g., reward models, LLM judges, majority voting) or on confidence proxies derived from token probabilities, both of which can be brittle: the former can be influenced by stylistic artifacts, while the latter is often miscalibrated. In this paper, we study a third source of information—the model’s hidden states—for binary correctness verification in tasks with a reliable success/failure signal (e.g., deterministic checkers or reference-grounded answers). We find that correct and incorrect solutions exhibit measurable geometric differences in their hidden-state trajectories. To isolate this signal with minimal modeling assumptions, we introduce Clue (Clustering and Experience-based Verification) , a training-free, non-parametric verifier. Clue summarizes each reasoning trace by an activation delta —the difference between hidden states at the start and end of the explicit reasoning span—and predicts correctness by comparing this delta to two class centroids computed from labeled experience. Across math (AIME 24/25), scientific QA (GPQA), and a multi-domain benchmark (WebInstruct-verified), Clue improves selection and reranking, with particularly strong gains on smaller or less-calibrated models. For example, on AIME 24 with a 1.5B model, Clue raises accuracy from 56.7% (majority@64) to 70.0% (top-maj@16).

## 27. Causal2Vec: Improving Decoder-only LLMs as Embedding Models through a Contextual Token

- Authors: Ailiang Lin, Zhuoyun Li, Yusong Wang, Kotaro Funakoshi, Manabu Okumura
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.8088662398298365
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1042/
- PDF: https://aclanthology.org/2026.acl-long.1042.pdf
- Local PDF: pdf/2026-08-07_27_Causal2Vec_ Improving Decoder-only LLMs as Embedding Models through a Contextual Token.pdf

Decoder-only large language models (LLMs) have been increasingly adopted to build embedding models for diverse tasks. To overcome the inherent limitations of causal attention in representation learning, many existing methods modify the attention mechanism to be bidirectional, potentially undermining LLMs’ ability to extract semantic information acquired during pre-training. Meanwhile, leading unidirectional approaches often rely on extra input text to generate contextualized embeddings, inevitably increasing computational costs. In this work, we propose Causal2Vec, a general-purpose embedding model tailored to enhance the performance of decoder-only LLMs without altering their original architectures or introducing significant computational overhead. Specifically, we first employ a lightweight BERT-style model to pre-encode the input text into a single Contextual token, which is then prepended to the LLM’s input sequence, allowing each token to capture contextualized information even without attending to future tokens. Furthermore, to mitigate the recency bias introduced by last-token pooling, we concatenate the last hidden states of Contextual and EOS tokens as the final text embedding. In practice, Causal2Vec achieves a new state-of-the-art performance on the MTEB benchmark among models trained solely on publicly available retrieval datasets.

## 28. Diffusion with Truncated Blocks: Fast and High-Quality Text Generation using Truncated Block Generation

- Authors: Yuyan Zhou, Weiyu Chen, James Kwok
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.8079349250895818
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.212/
- PDF: https://aclanthology.org/2026.findings-acl.212.pdf
- Local PDF: pdf/2026-08-07_28_Diffusion with Truncated Blocks_ Fast and High-Quality Text Generation using Truncated Block Generation.pdf

Diffusion-based Large Language Models (dLLMs) are emerging as a powerful alternative to traditional autoregressive models. These models learn to generate text by iteratively denoising masked sequences. In this work, we identify a critical problem in dLLMs: the model’s attention is wastefully expended on uninformative mask tokens, diluting its focus on meaningful context. We term this phenomenon “attention dilution”. We further show that this artifact is amplified by token-level noising, whereas models employing sequence-level noise exhibit a reduced effect. To resolve this problem, we introduce Truncated Block Generation, a novel sampling algorithm that not only mitigates attention dilution but also enables faster inference and flexible-length sequence generation. Extensive experiments validate our analysis and demonstrate the marked effectiveness of our proposed method in enhancing both the performance and efficiency of dLLMs.

## 29. Gated Tree Cross-Attention for Checkpoint-Compatible Syntax Injection in Decoder-Only LLMs

- Authors: Xinyu Gao, Shaonan Wang, Nai Ding
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.80705301388229
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1629/
- PDF: https://aclanthology.org/2026.acl-long.1629.pdf
- Local PDF: pdf/2026-08-07_29_Gated Tree Cross-Attention for Checkpoint-Compatible Syntax Injection in Decoder-Only LLMs.pdf

Decoder-only large language models achieve strong broad performance but are brittle to minor grammatical perturbations, undermining reliability for downstream reasoning. However, directly injecting explicit syntactic structure into an existing checkpoint can interfere with its pretrained competence. We introduce a checkpoint-compatible gated tree cross-attention (GTCA) branch that reads precomputed constituency chunk memory while leaving backbone architecture unchanged. Our design uses a token update mask and staged training to control the scope and timing of structural updates. Across benchmarks and transformer backbones, GTCA strengthens syntactic robustness beyond continued-training baselines without compromising Multiple-Choice QA performance or commonsense reasoning, providing a practical checkpoint-compatible route to more syntax-robust decoder-only LLMs.

## 30. Spectral Characterization and Mitigation of Sequential Knowledge Editing Collapse

- Authors: Chi Zhang, Mengqi Zhang, Xiaotian Ye, Runxi Cheng, Zisheng Zhou, Ying Zhou, Pengjie Ren, Zhumin Chen
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.806706459151613
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1384/
- PDF: https://aclanthology.org/2026.acl-long.1384.pdf
- Local PDF: pdf/2026-08-07_30_Spectral Characterization and Mitigation of Sequential Knowledge Editing Collapse.pdf

Sequential knowledge editing in large language models often causes catastrophic collapse of the model’s general abilities, especially for parameter-modifying methods. Existing approaches mitigate this issue through heuristic constraints on parameter updates, the mechanisms underlying such degradation remain insufficiently understood. In this work, we present a systematic spectral analysis of sequential knowledge editing and show that a model’s general abilities are closely associated with dominant singular directions of pretrained weight matrices. These directions are highly sensitive to perturbations and are progressively disrupted by repeated edits, closely tracking the collapse in both editing efficacy and general performance. Building on this insight, we propose REVIVE, a plug-and-play framework that prevents model collapse by explicitly preserving this dominant subspace. REVIVE analyzes parameter updates in the spectral basis of the original weights and filters out components that would interfere with the dominant subspace. Extensive experiments across multiple models and benchmarks show that REVIVE consistently improves editing efficacy while substantially preserving general abilities under long-horizon sequential editing, including extreme settings with up to 20,000 edits.
