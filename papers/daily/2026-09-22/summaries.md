# Paper Daily Reading - 2026-09-22

## 1. M2G-LLM: Enhancing Clinical Prediction via Multimodal Graph Reasoning and LLM Context Injection

- Authors: Inyoung Choi, Sukwon Yun, Jiayi Xin, Jie Peng, Tianlong Chen, Qi Long
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-18
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.209674898652273
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.21164v1
- PDF: https://arxiv.org/pdf/2609.21164v1
- Local PDF: pdf/2026-09-22_01_M2G-LLM_ Enhancing Clinical Prediction via Multimodal Graph Reasoning and LLM Context Injection.pdf

Integrating diverse data modalities --- such as clinical notes, laboratory results, and medical imaging --- is essential for advancing clinical decision-making. While Large Language Models (LLMs) have shown remarkable performance in processing unstructured clinical text, their limited capacity to incorporate non-text modalities hinders their broader utility in healthcare applications. Here, we introduce M2G-LLM (Multimodal MedGraph-LLM), a novel framework that enhances LLMs with multimodal integration and alignment via Graph Neural Networks (GNNs). Our approach models temporal relationships between patient visits, propagates information across clinically similar patients, and aligns heterogeneous data sources to construct enriched multimodal context vectors. These vectors are injected into the intermediate layers of the LLM, enabling joint reasoning over textual and non-textual modalities. We evaluate M2G-LLM on the MIMIC-IV and MIMIC-CXR datasets, demonstrating improvements in clinical prediction tasks over strong baseline models. Our results highlight the promise of combining the language understanding of LLMs with the relational reasoning capabilities of GNNs for comprehensive, multimodal healthcare analysis.

## 2. OpenMAS-GCom. A Diagnostic Benchmark for Graph-enhanced Multi-Agent Systems

- Authors: Kairui Yang, Xunkai Li, Kaixiang Zhang, Minghao An, Zekai Chen, Yuxuan Ba, Rong-Hua Li
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-18
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.139791073625821
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.21527v1
- PDF: https://arxiv.org/pdf/2609.21527v1
- Local PDF: pdf/2026-09-22_02_OpenMAS-GCom. A Diagnostic Benchmark for Graph-enhanced Multi-Agent Systems.pdf

Graph-enhanced multi-agent systems (G-MAS) coordinate large language model agents through communication graphs and role assignments, which determine how agents exchange information and divide responsibilities. However, final-score comparisons across systems combine differences in models, communication patterns, roles, and computation costs, making performance differences difficult to attribute to specific communication structures, role assignments, and information flows. To address this evaluation attribution problem, we introduce OpenMAS-GCom, a benchmark for diagnosing how these components affect G-MAS performance through controlled interventions. We represent systems through collaboration units, communication links, shared intermediate information, and execution rules. OpenMAS-GCom compares original systems with versions modified by changing one component while keeping tasks, models, prompts, and budget limits fixed. We rewire communication edges, remove specialist or critic agents, replace intermediate messages with incorrect content, and disable workers during execution. The benchmark evaluates 17 single-agent, ordinary multi-agent, and graph-enhanced configurations on 29 datasets across six domains. We add 400 G-MAS-Complex tasks requiring agents to combine information from multiple documents, resolve conflicting records, and return specified values with source identifiers. Experiments show larger mean losses after specialist removal than after critic removal, different performance degradation under incorrect messages and worker failures despite similar original scores, and different configurations achieving the highest accuracy and accuracy per token on G-MAS-Complex.

## 3. HERMES: Contrast-Aware Knowledge Graph Reasoning from Clinical Notes for Patient Outcome Prediction

- Authors: Gia-Bach Nguyen, Hoang-Ha Nguyen, Tuan-Cuong Vuong, Trang Mai Xuan, Duy Quoc Ngo, Tien-Cuong Nguyen, Huan Vu, Thien Van Luong
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-22
- DOI: Unavailable
- Categories: cs.CL, cs.LG
- Relevance: 3.076619274611817
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.20825v1
- PDF: https://arxiv.org/pdf/2609.20825v1
- Local PDF: pdf/2026-09-22_03_HERMES_ Contrast-Aware Knowledge Graph Reasoning from Clinical Notes for Patient Outcome Prediction.pdf

Clinical predictive models often rely on structured Electronic Health Record data, such as time-series and procedure codes. While recent approaches have begun leveraging unstructured clinical notes, they typically encode them as flat sequences, which may lose explicit relational and temporal structure present in clinical narratives. In response, we propose HERMES, a graph-based framework that operates exclusively on clinical text while preserving clinical relationships. This approach builds on two key ideas. First, personalized Knowledge Graphs (KGs) are constructed through Large-Language-Model-guided extraction from clinical notes with Contrastive Logic Modeling that explicitly captures temporal dynamics and treatment failures and changes in outcomes. Second, a Graph Attention Network synthesizes patient representations through graph-based learning over the KGs. Experiments on MIMIC-III and MIMIC-IV for in-hospital mortality and 30-day readmission prediction show that HERMES consistently outperforms strong text-only baselines. Our findings demonstrate that explicit relational modeling with Contrastive Logic Modeling significantly advances predictive performance.

## 4. CaLR: Causal Latent Revision for Robust Diffusion Reasoning

- Authors: Wei Cai, Jian Zhao, Yuchen Yuan, Xuelong Li
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-17
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 3.0125508295722705
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.20981v1
- PDF: https://arxiv.org/pdf/2609.20981v1
- Local PDF: pdf/2026-09-22_04_CaLR_ Causal Latent Revision for Robust Diffusion Reasoning.pdf

Autoregressive (AR) models suffer from local greediness, while diffusion language models (DLMs) often lack the strict causal structure required for reasoning. To combine the advantages and overcome the drawbacks of the dual, we propose Causal Latent Revision (CaLR), a framework that reformulates reasoning as constrained latent optimization. By adopting a causal topology matrix (CTM) from an expert model and implicit differentiation, CaLR performs gradient-guided ``thought revision" to enforce logical consistency, enabling dynamic self-correction of intermediate steps during parallel generation. Empirically, CaLR achieves SOTA DLM performance on complex benchmarks, surpassing strong AR baselines and demonstrating superior robustness in constrained tasks like Sudoku.

## 5. GraphSkillEvo: Evolutionary Optimization of Graph-Structured Agent Skills

- Authors: Rui Sun, Zhi Zheng, Zhenkun Wang, Zhichao Lu
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-18
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.0066702063823794
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.21749v1
- PDF: https://arxiv.org/pdf/2609.21749v1
- Local PDF: pdf/2026-09-22_05_GraphSkillEvo_ Evolutionary Optimization of Graph-Structured Agent Skills.pdf

Skills can improve the performance of Large Language Model (LLM) agents by providing task-specific procedural guidance, while skill optimization further improves their effectiveness through iterative refinement. However, existing skill optimization methods typically represent skills as unstructured natural-language instructions, creating two key challenges: 1) Unstructured skills often lack explicit workflow-level guidance and contain substantial redundancy, making them difficult for LLMs to execute; 2) the vast search space of unconstrained natural-language skills makes skill optimization ineffective. To address these challenges, we propose representing skills as graph-structured natural-language artifacts. In graph-structured skills, each node represents an execution step together with its operational guidance, while directed edges encode context-dependent transitions between steps. Compared to unstructured skills, graph-structured skills can provide clear workflow-level guidance. Moreover, the proposed graph-structured skill can also facilitate skill optimization. Building on this structured representation, we introduce GraphSkillEvo, a population-based evolutionary optimization framework with mutation and crossover operators for graph-structured skills. By maintaining multiple candidate skills and combining effective components, GraphSkillEvo enables broader and more comprehensive exploration of the structured skill space than purely LLM-based iterative self-refinement. Extensive experiments across five agent benchmarks demonstrate that GraphSkillEvo consistently outperforms the strong skill optimization baseline SkillOpt, improving average accuracy by 4.01% on GPT-5.4-nano and 1.76% on GPT-5.4. Our code is available at https://github.com/ruisun7/GraphSkillEvo.

## 6. AutoViewMem: Self-Configuring Orthogonal Views for Conversational Long-Term Memory

- Authors: Zijie Cao, Xijun Qu, Zhicheng Gu, Xiaoshu Chen, Duanyang Yuan, Yanning Hou, Sihang Zhou, Jianxing Gong, Jian Huang, Yang Mei
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-18
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 2.93780419478124
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.21940v1
- PDF: https://arxiv.org/pdf/2609.21940v1
- Local PDF: pdf/2026-09-22_06_AutoViewMem_ Self-Configuring Orthogonal Views for Conversational Long-Term Memory.pdf

Long-term memory is essential for large language model (LLM) agents to maintain consistency and personalization over extended interactions. Existing memory systems typically rely on fixed granularities or static schemas, but these designs struggle when heterogeneous information, such as preferences, events, constraints, and temporal updates, is embedded in a single mixed representation. The resulting semantic interference makes top-K retrieval sensitive to noise and often leaves relevant evidence poorly ranked. We present AutoViewMem, a data-driven framework that organizes long-term conversational memory into self-configuring, low-overlap semantic views before indexing. AutoViewMem discovers candidate views from interaction traces, selects a compact complementary view set, and uses these views to guide write-time structured extraction of provenance-grounded memories. This representation-first design moves semantic disentanglement from retrieval time to write time, allowing standard top-K similarity search to retrieve focused evidence without explicit routing or iterative retrieval. We further apply offline consolidation to improve memory compactness and consistency. Experiments on the LoCoMo and PersonaMem benchmarks, under both Qwen3-8B and Qwen3-14B backbones, show that AutoViewMem improves long-horizon question answering and personalization over strong memory baselines while preserving a simple inference pipeline.

## 7. VISPATH: Visual-Intent-Guided Path Reasoning for Multimodal Knowledge Graph Question Answering

- Authors: Jinke Wu, Zhengpin Li, Mengzhe Jia, Yang Li, Wentao Zhang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-04
- DOI: Unavailable
- Categories: cs.CL, cs.LG
- Relevance: 2.9254457684714286
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.20843v1
- PDF: https://arxiv.org/pdf/2609.20843v1
- Local PDF: pdf/2026-09-22_07_VISPATH_ Visual-Intent-Guided Path Reasoning for Multimodal Knowledge Graph Question Answering.pdf

Knowledge graph question answering (KGQA) enables models to answer natural-language questions through structured graph reasoning and has achieved substantial progress across many benchmarks and applications. Recently, multimodal KGQA (MM-KGQA) has attracted increasing attention because many questions require jointly using multimodal inputs and KG evidence. However, existing MM-KGQA methods typically use multimodal information only for starting entity grounding or evidence retrieval, after which multi-hop reasoning degenerates into text-only graph search. As a result, they cannot exploit multimodal cues that become important at intermediate hops. To address this limitation, we propose VISPATH, a visual-intent-guided path reasoning framework for MM-KGQA. VISPATH first identifies a reliable starting entity by combining multimodal grounding with graph-structural cues. It then performs intent-guided path discovery by recomputing hop-specific multimodal intent from the input, question, and current partial paths, so that each expansion is guided by the current reasoning state. The discovered paths are further refined through reasoning-chain pruning, which evaluates candidate paths as complete evidence chains based on their consistency with the question, reasoning sketch, and hop-specific intent. Finally, VISPATH checks whether the selected evidence is sufficient for answer generation. We further construct VISPATH-Bench, a benchmark for evaluating multimodal multi-hop reasoning over KGs, covering questions that require two to four hops over KG paths. Extensive experiments on VISPATH-Bench and three additional multimodal QA benchmarks show that VISPATH consistently outperforms strong baselines. Notably, with GPT-4o as the backbone, VISPATH surpasses GPT-5.4 on VISPATH-Bench, achieving a 10.6% relative improvement in average accuracy and a 13.1% improvement at 2-hop reasoning.

## 8. Kinks vs. Smoothness: Identifiability of Real Analytic nICA for Laplace-like Sources

- Authors: Isaac Manring, Kejun Huang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-18
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 2.915834769804354
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.21926v1
- PDF: https://arxiv.org/pdf/2609.21926v1
- Local PDF: pdf/2026-09-22_08_Kinks vs. Smoothness_ Identifiability of Real Analytic nICA for Laplace-like Sources.pdf

Many machine learning systems try to explain complex data - like images or financial time series - in terms of hidden, independent factors that generated them. Recovering the true underlying factors, rather than some scrambled version of them, is the central challenge of nonlinear Independent Component Analysis (nICA). We prove identifiability (exact recovery) up to trivial ambiguities for real analytic generating functions when source probability density functions have a finite number of discontinuities in the first derivative. The Laplace distribution is the most prominent example satisfying this assumption. Our proof relies on the contrast between kinks in the source distribution and the smoothness of real analytic functions. Real analytic functions comprise a broad class of generating mechanisms, and can be approximated with Normalizing Flows or Variational Autoencoders with standard activation functions (e.g., tanh, softplus, GELU), so our result applies with minimal changes to existing training pipelines. We perform experiments on real and synthetic data with both Normalizing Flows and Variational Auto-Encoders demonstrating their identifiability properties. In experiments on CelebA data we recover several interpretable latent factors controlling unique attributes across the dataset.

## 9. Decoupling Internal Representational Changes and Causal Importance in Fine-Tuned Large Language Models

- Authors: Lingfang Li, Procheta Sen, Shubham Das, Danushka Bollegala
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-17
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 2.8930425450638304
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.21113v1
- PDF: https://arxiv.org/pdf/2609.21113v1
- Local PDF: pdf/2026-09-22_09_Decoupling Internal Representational Changes and Causal Importance in Fine-Tuned Large Language Models.pdf

Fine-tuning has emerged as a widely adopted approach for adapting LLMs to a variety of downstream tasks. However, how it reshapes their internal mechanisms remains poorly understood. To address this, we investigate how fine-tuning alters internal representations in LLMs, including attention patterns and layer-wise activations, and examine whether these changes are linked to task-relevant components identified by EAP (e.g., attention heads and logit-level activations) that drive task performance. We find that EAP-identified components are concentrated within specific layers, indicating a degree of functional localisation in how models internalise task-specific behavior. Notably, the distribution of these components across layers is largely uncorrelated with the layers undergoing the most substantial representational changes during fine-tuning. Furthermore, we observe that overlap in EAP-identified components across tasks does not translate into cross-task performance transfer if the tasks are different in nature (e.g. classification vs. generative tasks). More specifically, fine-tuning on one task can lead to a degradation of performance on another when the two tasks exhibit a high degree of overlap in their EAP-identified components.

## 10. Hiding in Plain Sight: A Diffusion-based Mitigation of Geolocation Privacy Leakage in Vision-Language Models

- Authors: Yining Wang, Xi Li, Mi Zhang, Xiaohan Zhang, Xiaoyu You, Zhenxing Qian, Mi Wen
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-18
- DOI: Unavailable
- Categories: cs.CV, cs.LG
- Relevance: 2.8831708577361996
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.21363v1
- PDF: https://arxiv.org/pdf/2609.21363v1
- Local PDF: pdf/2026-09-22_10_Hiding in Plain Sight_ A Diffusion-based Mitigation of Geolocation Privacy Leakage in Vision-Language Models.pdf

Multimodal large reasoning models (MLRMs) have demonstrated remarkable capabilities in complex visual understanding. However, this very power introduces a critical yet underexplored privacy threat: adversaries can exploit MLRMs to precisely infer users' geographic locations from casually shared photographs, by performing structured reasoning over subtle visual cues such as architectural styles, vegetation, and lighting conditions. In this work, we present a systematic study of MLRM-driven geolocation privacy leakage. We first reveal that refusal-based safeguards are critically insufficient, as carefully crafted jailbreak prompts can raise model response rates to 100%. We further identify that existing defenses, which inject imperceptible perturbations into shared images, suffer from structural limitations intrinsic to their pixel-space optimization, resulting in degraded black-box transferability and pronounced visual artifacts. Motivated by these findings, we propose a diffusion-based framework that provides targeted, proactive defense against geolocation privacy leakage. By injecting perturbations into the latent space of a diffusion model during reverse sampling, our method operates directly on high-level semantic representations, thereby resolving the effectiveness-utility bottlenecks by construction. We further ground our optimization with GeoCLIP, a model explicitly aligned with GPS coordinates, as a surrogate to pinpoint and disrupt the geographic signals that MLRMs exploit for location inference. This targeted semantic disruption yields significantly stronger black-box transferability while preserving perceptual image quality, offering a seamless integration on social media platforms.

## 11. The Weight Is Over - Interactive Diffusion on Consumer GPUs

- Authors: Frieder Ganz, Maximilian Müller
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-18
- DOI: 10.1145/3829339.3847852
- Categories: cs.LG, cs.CV, cs.PF
- Relevance: 2.880783365291668
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.21849v1
- PDF: https://arxiv.org/pdf/2609.21849v1
- Local PDF: pdf/2026-09-22_11_The Weight Is Over - Interactive Diffusion on Consumer GPUs.pdf

On-device inference is booming, but the momentum is almost all in language models. Diffusion pipelines are memory hungry, latency-sensitive, and require orchestrating an embedder, a transformer, a decoder, and often further postprocessing that is not as standardized as LLM inference loops are. We navigate the trade-off between performance, quality, and model footprint to reach as many client devices in the wild as possible. We make three contributions: an embedding translator that maps a small text encoder into a large encoder space to cut weight and latency; a reproducible sweep recipe for navigating the speed/quality/memory triangle in diffusion pipelines; and an interactive on-device image generation editor achieving sub-second TTFI on recent GPUs.

## 12. Detecting Pretraining Data in Large Language Models from a Free-Energy Perspective

- Authors: Chenye Ke, Zirui Liu, Qi Liu, Yan Zhuang, Jintao Zhang, Zhenya Huang, Shijin Wang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-18
- DOI: Unavailable
- Categories: cs.LG, cs.AI, cs.CL
- Relevance: 2.8635072616539334
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.21888v1
- PDF: https://arxiv.org/pdf/2609.21888v1
- Local PDF: pdf/2026-09-22_12_Detecting Pretraining Data in Large Language Models from a Free-Energy Perspective.pdf

Detecting pretraining data in large language models is challenging because high likelihood can reflect either training exposure or strong generalization. In the joint space of prediction loss and predictive entropy, a likelihood-only detector uses a horizontal boundary and can mistake predictable non-members for members. Motivated by this, we introduce an inclined boundary that evaluates prediction loss relative to predictive entropy. Our analysis shows that entropy correction can preserve the expected membership signal while reducing its variance, thereby improving standardized member--non-member separation. We further extend the mean--variance analysis to the more general setting with a nonzero mean entropy gap. Interestingly, this entropy-adjusted score admits a Helmholtz free-energy interpretation, leading to Energy Transfer Detection (ETD), which views pretraining data detection from a macroscopic residual free-energy transfer perspective. Extensive experiments show that ETD achieves the best average detection performance, improving average AUROC by up to 3.5\% and TPR@5\%FPR by up to 5.1\%, while remaining robust across diverse settings.

## 13. Accelerating Dense LLMs via L0-regularized Mixture-of-Experts

- Authors: Zhenyu Zhang, Jiudong Yang, Zhaowen Tao, Meng Chen
- Source: arxiv
- Venue type: preprint
- Journal: Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics, 2025
- Publication status: preprint
- Publication date: 2026-09-18
- DOI: Unavailable
- Categories: cs.AI, cs.CL
- Relevance: 2.8386742775125207
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.21672v1
- PDF: https://arxiv.org/pdf/2609.21672v1
- Local PDF: pdf/2026-09-22_13_Accelerating Dense LLMs via L0-regularized Mixture-of-Experts.pdf

Large language models (LLMs) achieve strong performance but suffer from slow and costly inference. Existing acceleration methods often lead to noticeable performance degradation, while Mixture-of-Experts (MoE) models require extensive computational resources. In this paper, we propose L0-MoE, a lightweight MoE approach using L0-regularization to accelerate dense LLMs nearly without performance loss. Our method introduces a cluster confusion matrix for domain-aware dataset curation and applies dynamic batching for efficient training. Experiments show that L0-MoE achieves up to 2.5x speedup over dense models while maintaining competitive performance, outperforming existing LLM acceleration baselines.

## 14. Generative inversion for early ranking of competing geologic interpretations

- Authors: Harun Ur Rashid, Daniel O'Malley
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-17
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 2.803719061465717
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.20978v1
- PDF: https://arxiv.org/pdf/2609.20978v1
- Local PDF: pdf/2026-09-22_14_Generative inversion for early ranking of competing geologic interpretations.pdf

High-consequence subsurface decisions are often made under severe data scarcity. Experts may arrive at competing interpretations of the same subsurface system, yet early in a project there is rarely a practical way to determine which one is most realistic. This uncertainty can persist until several wells are drilled, often costing millions of dollars. Existing approaches for evaluating geologic interpretations rely either on subjective judgment or on dense data that are rarely available in early-stage investigations. We present a workflow that addresses this challenge by translating competing geologic interpretations into alternative spatial priors and ranking them according to their consistency with hydraulic-head observations. For each interpretation, a text-to-image foundation model generates an ensemble of 1600 geologic images, and a separately trained variational autoencoder provides an interpretation-specific latent representation. A supervised inverse network maps the head observations into this latent space, and the frozen decoder produces an image that is mapped to a log-conductivity field. Steady-state flow simulation then provides predicted heads, and the resulting mismatch is converted into a Gaussian-form compatibility score. We evaluate the framework using a synthetic benchmark based on the Johansen Formation and three interpretations of decreasing consistency with the reference representation. Across 925 test cases, the mean head RMSE increases from 0.197 for the Precise \& Accurate interpretation to 0.227 for the Accurate interpretation and 0.280 for the Mismatched interpretation. We subsequently apply the workflow to two published conceptual models of the Culebra Dolomite Member at the Waste Isolation Pilot Plant. The revised model receives a compatibility weight of 0.991, compared with 0.009 for the original model, consistent with the independent evidence.

## 15. Watermarkable Multi-Draft Speculative Sampling via Poisson Processes

- Authors: Yanxiao Liu, Sicheng Wan, Zhan Gao, Deniz Gündüz
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-18
- DOI: Unavailable
- Categories: cs.CR, cs.LG
- Relevance: 2.78977923847063
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.21858v1
- PDF: https://arxiv.org/pdf/2609.21858v1
- Local PDF: pdf/2026-09-22_15_Watermarkable Multi-Draft Speculative Sampling via Poisson Processes.pdf

Large language models (LLMs) have achieved state-of-the-art performance across a wide range of tasks, motivating two important aspects of deployment: inference efficiency and output provenance, which can be tackled by speculative sampling and watermarking, respectively. However, recent works have shown that combining these two goals is highly nontrivial and can be potentially impossible. In this work, we develop a novel multi-draft speculative sampling algorithm based on Poisson processes that improves the frontier of this fundamental trade-off. The proposed algorithm has strong sampling efficiency on its own and, more interestingly, is naturally watermarkable: we can embed an unbiased watermark without degrading speculative acceptance. Moreover, our algorithm is based on an exact list-coupling-without-communication scheme, which yields a drafter invariance property that benefits both sampling and watermarking. It is the first multi-draft, drafter-invariant speculative sampling scheme that maintains both watermark strength and sampling efficiency, and we experimentally verify its strong performance in both aspects.

## 16. A Hybrid Computational Intelligence Framework for scRNA-seq Imputation: Integrating scRecover and Random Forests

- Authors: Ali Anaissi, Deshao Liu, Yuanzhe Jia, Weidong Huang, Widad Alyassine, Junaid Akram
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2025-11-21
- DOI: Unavailable
- Categories: cs.LG, cs.AI, q-bio.GN
- Relevance: 2.7850019599772646
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2511.16923v1
- PDF: https://arxiv.org/pdf/2511.16923v1
- Local PDF: pdf/2026-09-22_16_A Hybrid Computational Intelligence Framework for scRNA-seq Imputation_ Integrating scRecover and Random Forests.pdf

Single-cell RNA sequencing (scRNA-seq) enables transcriptomic profiling at cellular resolution but suffers from pervasive dropout events that obscure biological signals. We present SCR-MF, a modular two-stage workflow that combines principled dropout detection using scRecover with robust non-parametric imputation via missForest. Across public and simulated datasets, SCR-MF achieves robust and interpretable performance comparable to or exceeding existing imputation methods in most cases, while preserving biological fidelity and transparency. Runtime analysis demonstrates that SCR-MF provides a competitive balance between accuracy and computational efficiency, making it suitable for mid-scale single-cell datasets.

## 17. SpecQuant: Speculative Decoding with Multi-Parent Quantization for Adaptive LLM Inference

- Authors: Harish KB, Jagadeeswaran M, Pradheep P, Yuvanesh S, Sivakumar T
- Source: arxiv
- Venue type: preprint
- Journal: 2026 Fifth International Conference on Power, Control and Computing Technologies (ICPC2T), Raipur, India, 11-13 March 2026, pp. 371-375, IEEE, 2026
- Publication status: preprint
- Publication date: 2026-09-18
- DOI: 10.1109/ICPC2T68221.2026.11646348
- Categories: cs.LG
- Relevance: 2.763726165248508
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.21704v1
- PDF: https://arxiv.org/pdf/2609.21704v1
- Local PDF: pdf/2026-09-22_17_SpecQuant_ Speculative Decoding with Multi-Parent Quantization for Adaptive LLM Inference.pdf

Running large language models (LLMs) locally continues to be limited by restrictions of compute and memory on consumer hardware. The popular acceleration technologies, such as quantization, speculative decoding, and adaptive inferencing, offer substantial speed boosts but usually necessitate retraining, per architecture tuning, or draft models. SpecQuant is a trainingfree framework, that combines speculative decoding with multiparent quantization to perform adaptive, efficient inference of LLMs. SpecQuant derives multiple quantized variants (INT4, FP8, FP16) from a shared base model, and dynamically routes queries based on predicted complexity; lightweight variants are used for simple or factual tasks, and full-precision models are used for complex reasoning tasks or long-context inputs. The shared-weight design of SpecQuant ensures sufficient token acceptance for speculative decoding without compatibility issues using separate draft parent models. We evaluate SpecQuant on Qwen2.5 based models on the MMLU, AlpacaEval, and GSM8K datasets, or benchmarks, demonstrating 35-43% speedups without degrading accuracy greater than 2%, substantial within the LLM community. SpecQuant enables practical on-device LLM deployment across diverse hardware without special infrastructure or expertise.

## 18. Physically Based Rendering in the Latent Space

- Authors: Vuk Radovanovic, Vishesh Gupta, Adrien Gruson, Binh-Son Hua
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-17
- DOI: 10.1111/cgf.70633
- Categories: cs.GR, cs.AI, cs.LG
- Relevance: 2.751669734593473
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.21054v1
- PDF: https://arxiv.org/pdf/2609.21054v1
- Local PDF: pdf/2026-09-22_18_Physically Based Rendering in the Latent Space.pdf

Image diffusion models have shown impressive image generation capabilities but are often hard to control, in contrast to classical computer graphics pipelines such as physically based rendering. However, we observe that there is a bridge between light transport phenomena and the distribution of latent space values produced by such models. Thus, we introduce physically based rendering in the feature space learned by the variational autoencoders in generative models, enabling light transport simulation in the latent space. This allows us to leverage physically based rendering techniques to output latent maps for physically guided content generation. We propose modifications to the rendering equation, which, when paired with a differentiable renderer, can yield an optimal set of scene parameters that require only minimal refinement to accurately render into the pretrained latent space. We train our method on a single rendered image, and then demonstrate the generalization of the method to scene geometry changes, lighting changes, and camera view changes.

## 19. RBS-Attention: Radius-Bounded Sparse Prefill for Long-Context Large Language Models

- Authors: Chuxu Song, Jiuqi Wei, Zhencan Peng
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-17
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 2.7481378011491864
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.20971v1
- PDF: https://arxiv.org/pdf/2609.20971v1
- Local PDF: pdf/2026-09-22_19_RBS-Attention_ Radius-Bounded Sparse Prefill for Long-Context Large Language Models.pdf

Long-context large language model inference is increasingly limited by prefill, where dense self-attention processes the entire prompt before generation begins. Sparse block selection can reduce this cost, but a block centroid may hide a highly relevant token among many irrelevant ones. We call this failure mode mean dilution and propose RBS-Attention, a training-free sparse-prefill method with two complementary selection branches. A centroid base branch captures average relevance, while a rescue branch uses the maximum key-block radius and its prompt-, layer-, and head-dependent distribution to identify blocks at risk of underestimation. Independently thresholding the two branches and combining their masks controls the contribution of rescue blocks while preserving regular block-sparse FlashAttention execution. On H100 GPUs, RBS-Attention achieves 20.65$\times$ standalone prefill-attention speedup, 11.92$\times$ vLLM prefill-attention speedup, and 5.97$\times$ end-to-end time-to-first-token speedup at 128K on Qwen3-30B-A3B-Instruct-2507-FP8. On the dense Qwen3-32B model, it obtains 88.65 overall RULER accuracy versus 89.52 for dense attention; LongBench-v2, InfiniteBench, and Video-MME provide additional quality evaluation. Supporting experiments measure actual retention, compare selectors at matched density, and characterize block-size, threshold, and memory behavior. Together, these results support radius-adaptive dual-branch selection as an effective approach to long-context prefill.

## 20. MACE: Memory-Agent Co-Evolution with Adaptive Memory Graphs for Multi-Agent Systems

- Authors: Kairui Yang, Minghao An, Xunkai Li, Ziheng Yi, Zekai Chen, Guangyuan He, Rong-Hua Li
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-18
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 2.7074708938442003
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.21533v1
- PDF: https://arxiv.org/pdf/2609.21533v1
- Local PDF: pdf/2026-09-22_20_MACE_ Memory-Agent Co-Evolution with Adaptive Memory Graphs for Multi-Agent Systems.pdf

LLM-based multi-agent systems generate collaboration traces that record how agents plan tasks, verify intermediate results, and repair failures. Reusing these procedures requires preserving an action's prerequisites and the outputs needed by subsequent agents. Our empirical studies show that grouping these dependencies into functional memory units improves their retention, while connecting units increases retrieval of the units and links jointly required by a task. The preferred combination of units also changes between instructions and checklists, even when each combination's content is fixed across formats. Updating choices from the outcomes of each combination and format pairing outperforms scoring combinations and formats separately. These findings motivate MACE, a memory-agent co-evolution framework that adapts memory organization and agent memory use through execution feedback. Its MemGoG structure represents functional units as subgraphs of related conditions, actions, and outputs, connecting them through support, conflict, and repair relations. MACE Loop selects task-relevant units and relations within a memory budget and provides each agent with instructions or checklists for its current operation. It records the selected units, presentation formats, agent outputs, and task outcomes to update unit scores and relations for retrieval and inform subsequent presentation choices. Across eight benchmarks, MACE outperforms ten baselines with an average score of 81.11%, compared with 78.97% for the strongest baseline, SAGE.

## 21. Micro-Collaborative Poisoning: A Distributed Attack on RAG Systems

- Authors: Pedro Pereira, Eva Maia, Isabel Praça
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-18
- DOI: Unavailable
- Categories: cs.CR, cs.AI
- Relevance: 2.7007085628604455
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.21573v1
- PDF: https://arxiv.org/pdf/2609.21573v1
- Local PDF: pdf/2026-09-22_21_Micro-Collaborative Poisoning_ A Distributed Attack on RAG Systems.pdf

Retrieval-Augmented Generation (RAG) improves large language models by grounding outputs in external knowledge sources, but this dependency also creates a surface for poisoning attacks. This paper introduces Micro-Collaborative Poisoning, a distributed attack in which a false target claim is divided across multiple locally plausible documents instead of being concentrated in a single malicious passage. We evaluate the attack across 108 RAG configurations by varying dataset, retriever architecture, retrieval depth, database composition, number of poisoned databases, and generator model. The results indicate that Micro-Collaborative Poisoning is not driven by a single dominant poisoned passage, but by the accumulation of weak adversarial signals across retrieved sources. Increasing top-$k$ and poisoning multiple databases make it more likely that these signals will appear together in the retrieved context, while clean database diversity and stronger retrievers can reduce their influence. The document-level poisoning visibility analysis further shows that this threat is difficult to expose through isolated document inspection, since Micro-Collaborative Poisoning achieves downstream influence while leaving a weaker explicit poisoning signature than direct poisoning.

## 22. Riemannian Neural Hamiltonian Flows: Geodesic Symplectic Transport and Interpretability

- Authors: Vincent Souveton
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-18
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 2.691232835544539
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.21647v1
- PDF: https://arxiv.org/pdf/2609.21647v1
- Local PDF: pdf/2026-09-22_22_Riemannian Neural Hamiltonian Flows_ Geodesic Symplectic Transport and Interpretability.pdf

Hamiltonian normalizing flows are attractive generative models because their phase-space maps are invertible and volume preserving, but most neural constructions are formulated in Euclidean space. We introduce Riemannian Neural Hamiltonian Flows, which combine the fixed kinetic energy of a Riemannian manifold, a learned scalar potential, and an explicit geodesic leapfrog integrator. Our analysis explains how the learned Hamiltonian can be made interpretable. Every normalizable potential defines an implicit profile, and the position marginal initially accelerates along the relative score between that profile and the base. The matched potential is the interpretable specialization for which the implicit profile is the target. In the isotropic Gaussian case, the mechanism corresponds to a phase-space rotation. A local harmonic analysis extends this result around each mode of a general target on a manifold. The gap between the learned and the matched potential is the sum of a residual memory of the base and a bias of the model, and the two potentials agree when the position base has been transferred to the momentum. This can be achieved when the former is broader than the target. Numerical experiments on Euclidean, hyperbolic, and spherical spaces show competitive sample quality and numerical cost against a Riemannian continuous normalizing flow, and confirm the interpretability of the learned potential.

## 23. A Survey of Deep Learning for Geometry Problem Solving

- Authors: Jianzhe Ma, Wenxuan Wang, Qin Jin
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.6726824794626265
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1829/
- PDF: https://aclanthology.org/2026.acl-long.1829.pdf
- Local PDF: pdf/2026-09-22_23_A Survey of Deep Learning for Geometry Problem Solving.pdf

Geometry problem solving, a crucial aspect of mathematical reasoning, is vital across various domains, including education, the assessment of AI’s mathematical abilities, and multimodal capability evaluation. The recent surge in deep learning technologies, particularly the emergence of multimodal large language models, has significantly accelerated research in this area. This paper presents a survey of the applications of deep learning in geometry problem solving, including (i) a comprehensive summary of the relevant tasks in geometry problem solving; (ii) a thorough review of related deep learning methods; (iii) a detailed analysis of evaluation metrics and methods; and (iv) a critical discussion of state-of-the-art performance, existing challenges, and promising future directions. Our objective is to offer a comprehensive and practical reference of deep learning for geometry problem solving, thereby fostering further advancements in this field. We maintain a list of relevant papers: https://github.com/majianz/dl4gps .

## 24. Experience-Driven Reflective Co-Evolution of Prompts and Heuristics for Autonomous Algorithm Design

- Authors: Yihong Liu, Junyi Li, Hongyu Lu, Xin Zhao, Ji-Rong Wen
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.672218330765732
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.245/
- PDF: https://aclanthology.org/2026.findings-acl.245.pdf
- Local PDF: pdf/2026-09-22_24_Experience-Driven Reflective Co-Evolution of Prompts and Heuristics for Autonomous Algorithm Design.pdf

Combinatorial optimization has long been dominated by manually engineered heuristics, a paradigm requiring substantial expert intuition and implementation overhead. The advent of Large Language Models has disrupted this landscape, enabling the autonomous synthesis and optimization of algorithms. Recent approaches typically iterate on heuristic populations using LLMs as mutators; however, these strategies often suffer from limited exploration, leading to stagnation in local optima. To overcome this, we present the Experience-Driven Reflective Co- Evo lution of P rompt and H euristics ( EvoPH ) for autonomous algorithm design, a novel framework that couples an island migration model with elite selection to maintain population diversity. Uniquely, EvoPH co-evolves both the guiding prompts and the heuristics themselves, using a feedback loop driven by past experience to refine the search process. We demonstrate EvoPH’s efficacy on the Traveling Salesman and Bin Packing Problems. Our results show that EvoPH achieves superior accuracy compared to baselines, marking a significant step forward in LLM-aided algorithm design.

## 25. CascadeDebate: Multi-Agent Deliberation for Cost-Aware LLM Cascades

- Authors: Raeyoung Chang, Dongwook Kwon, Jisoo Lee, Nikhil Verma
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.671698310864286
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-industry.93/
- PDF: https://aclanthology.org/2026.acl-industry.93.pdf
- Local PDF: pdf/2026-09-22_25_CascadeDebate_ Multi-Agent Deliberation for Cost-Aware LLM Cascades.pdf

Cascaded LLM systems coordinate models of varying sizes with human experts to balance accuracy, cost, and abstention under uncertainty. However, single-model tiers at each stage falter on ambiguous queries, triggering premature escalations to costlier models or experts due to under-confidence and inefficient compute scaling. CascadeDebate addresses this critical gap by inserting multi-agent deliberation directly at each tier’s escalation boundary. Confidence-based routers activate lightweight agent ensembles only for uncertain cases, enabling consensus-driven resolution of ambiguities internally, without invoking higher-cost upgrades. Our unified architecture alternates single-model inference with selective multi-agent deliberation across model scales, culminating in human experts as final fallback. This design scales test-time compute dynamically to query difficulty. Across five benchmarks spanning science, medicine, and general knowledge, CascadeDebate outperforms strong single-model cascades and standalone multi-agent systems by up to 26.75%.An online threshold optimizer proves essential, boosting accuracy 20.98–52.33% relative improvement over fixed policies and enabling elastic adaptation to real-world distributions.

## 26. Dictionary Guided Sparse Logit Editing for Reliable Jailbreak Attacks

- Authors: Shuaibiao Han, Ruiyang Ni, Zhiyu Yi, Changlong Li, Perley Xu, Wenjie Ruan
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.6716850124721034
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.2137/
- PDF: https://aclanthology.org/2026.findings-acl.2137.pdf
- Local PDF: pdf/2026-09-22_26_Dictionary Guided Sparse Logit Editing for Reliable Jailbreak Attacks.pdf

Although Large Language Models undergo rigorous safety alignment, they remain vulnerable to adversarial attacks. Existing methods, particularly gradient-based prompt optimization, suffer from high computational costs and produce uninterpretable, high-perplexity inputs. While recent logit-space attacks improve efficiency, they often rely on cumbersome auxiliary models or complex pipelines. In this work, we propose Sparse Index-Based Intervention (SIBI), a white-box, inference-time jailbreak that bypasses guardrails via lightweight, sparse logit editing. SIBI operates without gradients or auxiliary models, modifying pre-softmax logits using a compact, tokenizer-aligned dictionary of penalty and reward tokens. By incorporating temperature-consistent scaling and a mixed-norm trust region, the method ensures attack effectiveness while preserving generation fluency. On standard benchmarks, SIBI achieves high attack success rates while reducing computational overhead and space overhead compared to optimization baselines.

## 27. Decentralized Arena: Towards Democratic and Scalable Automatic Evaluation of Language Models

- Authors: Yanbin Yin, Kun Zhou, Zhen Wang, Xiangdong Zhang, Yifei Shao, Shibo Hao, Yi Gu, Jieyuan Liu, Somanshu Singla, Tianyang Liu, Eric P. Xing, Zhengzhong Liu, Haojian Jin, Zhiting Hu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.671235906728601
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1639/
- PDF: https://aclanthology.org/2026.acl-long.1639.pdf
- Local PDF: pdf/2026-09-22_27_Decentralized Arena_ Towards Democratic and Scalable Automatic Evaluation of Language Models.pdf

The recent explosion of large language models (LLMs), each with its own general or specialized strengths, makes scalable, reliable benchmarking more urgent than ever. Standard practices nowadays face fundamental trade-offs: closed-ended question-based benchmarks (MMLU) struggle with saturation as newer models emerge, while crowd-sourced leaderboards (Chatbot Arena) rely on costly and slow human judges. Recently, automated methods (LLM-as-a-judge) shed light on the scalability, but risk bias by relying on one or a few “authority” models. To tackle these issues, we propose Decentralized Arena (), a fully automated framework leveraging collective intelligence from all LLMs to evaluate each other. It mitigates single-model judge bias by democratic, pairwise evaluation, and remains efficient at scale through two key components: (1) a coarse-to-fine ranking algorithm for fast incremental insertion of new models with sub-quadratic complexity, and (2) an automatic question selection strategy for the construction of new evaluation dimensions. Across extensive experiments across 66 LLMs, attains up to 97% correlation with human judgements, while significantly reducing the cost.

## 28. Learning stochasticity via a nonparametric approach to state-dependent noise estimation

- Authors: Gianluigi Pillonetto, A. Giaretta, M. Bisiacco
- Source: openalex
- Venue type: journal
- Journal: Nature Communications
- Publication status: published
- Publication date: 2026-09-16
- DOI: https://doi.org/10.1038/s41467-026-75727-w
- Categories: Machine Learning and Algorithms, Gaussian Processes and Bayesian Inference, Reinforcement Learning in Robotics
- Relevance: 2.6709641002993485
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://doi.org/10.1038/s41467-026-75727-w
- PDF: https://www.nature.com/articles/s41467-026-75727-w_reference.pdf
- Local PDF: pdf/2026-09-22_28_Learning stochasticity via a nonparametric approach to state-dependent noise estimation.pdf

Modeling stochastic dynamical systems remains a central challenge across disciplines. Incomplete knowledge of nonlinear interactions and state-dependent fluctuations often renders bottom-up approaches ineffective, motivating methods that infer governing equations directly from data. However, parametric models struggle in the absence of strong prior assumptions, particularly when the intensity of the process noise depends on the system state. Here we introduce Trine (Three-phase Regression for INferred noisE), a nonparametric, kernel-based framework for inferring state-dependent noise from time-series data. The approach naturally extends to supervised learning settings with heteroskedastic noise. Trine employs a three-stage algorithm combining analytically solvable subproblems with a structured kernel architecture capable of capturing both abrupt stochastic fluctuations and smooth variations in variance. We validate Trine on biological and ecological systems, where it uncovers hidden dynamics without predefined parametric assumptions. Across benchmark systems, Trine achieves near-oracle performance, matching an idealized observer with direct access to the stochastic input realizations. On live-cell RNA transcription trajectories, Trine reveals localized regimes of elevated stochastic activity, demonstrating how effective state-dependent diffusion models can uncover biologically meaningful hidden variability directly from experimental observations. The Trine framework thus opens new avenues for quantifying how process noise shapes the behavior of complex dynamical systems. Trine is a nonparametric kernel-based framework for inferring state-dependent noise from time-series data. Using a three-stage regression approach, it uncovers hidden stochastic dynamics without requiring predefined functional forms.

## 29. Ready to Translate, Not to Represent? Bias and Performance Gaps in Multilingual LLMs Across Language Families and Domains

- Authors: Md. Faiyaz Abdullah Sayeedi, Subhey Sadi Rahman, Md. Mahbub Alam, Md. Adnanul Islam, Jannatul Ferdous Deepti, Tasnim Mohiuddin, Md Mofijul Islam, Swakkhar Shatabda
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.6709169250637954
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.68/
- PDF: https://aclanthology.org/2026.findings-acl.68.pdf
- Local PDF: pdf/2026-09-22_29_Ready to Translate, Not to Represent_ Bias and Performance Gaps in Multilingual LLMs Across Language Families and Domain.pdf

The rise of Large Language Models (LLMs) has redefined Machine Translation (MT), enabling context-aware and fluent translations across hundreds of languages and textual domains. Despite their remarkable capabilities, LLMs often exhibit uneven performance across language families and specialized domains. Moreover, recent evidence reveals that these models can encode and amplify different biases present in their training data, posing serious concerns for fairness, especially in low-resource languages. To address these gaps, we introduce Translation Tangles, a unified framework and dataset for evaluating the translation quality and fairness of open-source LLMs. Our approach benchmarks 24 bidirectional language pairs across multiple domains using different metrics. We further propose a hybrid bias detection pipeline that integrates rule-based heuristics, semantic similarity filtering, and LLM-based validation. We also introduce a high-quality, bias-annotated dataset based on human evaluations of 1,439 translation-reference pairs. The code and dataset are accessible on GitHub: https://github.com/faiyazabdullah/TranslationTangles

## 30. T ⋆ : Progressive Block Scaling for Masked Diffusion Language Models Through Trajectory Aware Reinforcement Learning

- Authors: Hanchen Xia, Baoyou Chen, Yutang Ge, Guojiang Zhao, Siyu Zhu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.670818282101235
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-short.67/
- PDF: https://aclanthology.org/2026.acl-short.67.pdf
- Local PDF: pdf/2026-09-22_30_T ⋆ _ Progressive Block Scaling for Masked Diffusion Language Models Through Trajectory Aware Reinforcement Learning.pdf

We present T ⋆ , a simple TraceRL-based curriculum for progressive block-size scaling in masked diffusion language models (MDMs).Starting from an AR-initialized small-block MDM, T ⋆ gradually increases the block size while re-optimizing the denoising policy at each stage, enabling higher-parallelism decoding with limited degradation on math reasoning benchmarks. Across two SDAR scales and three benchmarks, T ⋆ consistently outperforms direct large-block TraceRL and is substantially more stable during training. Our schedule analysis suggests that the learned policy does not simply revert to a strictly left-to-right order; instead, it retains block-size-specific non-monotone updates while improving accuracy.
