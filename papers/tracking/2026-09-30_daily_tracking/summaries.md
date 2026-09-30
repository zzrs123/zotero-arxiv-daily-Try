# Researcher Tracking - 2026-09-30 (daily)

Total new tracked papers: 9
Highlighted papers: 9

## 1. Cyclostationary Phase Conditioning for Medical Time Series Diffusion

- Authors: Samuel Ruiperez-Campillo, Michele Copetti, Jorge da Silva Goncalves, Sonia Laguna, Thomas Hofmann, Julia E. Vogt
- Source hits: arxiv
- Matched researchers: Jorge Goncalves
- Matched groups: N/A
- Confidence: medium (author_alias)
- Topic keywords: diffusion
- Journal/source: arxiv
- Publication date: 2026-09-28
- Article: http://arxiv.org/abs/2609.34965v2

Many physiological time series, such as cardiac and brain recordings, exhibit cyclostationarity: their statistics vary periodically with an underlying cycle phase. Corruption from motion, poor contact, and physiological interference obscures morphology needed for diagnosis, making signal restoration essential. Existing diffusion approaches condition on corrupted observations alone and must learn cyclic structure implicitly. We instead propose two inductive biases which encode cyclostationarity: a shift-covariant wavelet representation and dense per-sample phase conditioning inferred from the corrupted input. We further introduce a training-free cyclostationarity index that quantifies phase structure and predicts when phase conditioning will help. Finally, we propose antithetic coupling of reverse trajectories to reduce sampling variance while achieving comparable performance with fivefold fewer network evaluations. Across modalities, our results show that explicitly encoding measurable cyclic structure improves physiological time-series restoration.

## 2. "Black Mirror?": Public Sensemaking of AI-Powered Lifelogging

- Authors: Ying Ma, Jarod Govers, Le Fang, Shuning Zhang, Yongquan 'Owen' Hu, Xin Yi, Jorge Goncalves
- Source hits: arxiv
- Matched researchers: Jorge Goncalves
- Matched groups: N/A
- Confidence: medium (author_alias)
- Topic keywords: N/A
- Journal/source: arxiv
- Publication date: 2026-09-28
- Article: http://arxiv.org/abs/2609.34950v1

AI-powered lifelogging wearables are emerging as a new class of consumer devices that transform everyday experience into searchable, AI-curated memory archives. We study early public sensemaking around these systems at the moment of their market entry, using the Looki L1 as an empirical lens. Analysing large-scale Chinese-language and English-language social media discourse (N = 5,053 comments), we combine topic clustering with inductive thematic analysis to examine how users interpret the social, moral, and political implications of AI-mediated memory. Across contexts, users reference dystopian surveillance imaginaries, express privacy resignation and bystander concerns, and debate assistive value alongside consumer logics. English-language comments more often framed these devices through interpersonal power, evidentiary use, and hacking anxieties, while Chinese-language comments more often foregrounded labour exploitation, governance surveillance, and technological inevitability.

## 3. Beyond Teacher Assignment: Domain-Normalized Multi-Teacher On-Policy Distillation

- Authors: Xin Li, Hao Jiang, Xin Gao, Annan Wang, Yuchen Xie, Jinghao Guo, Xingwei Qu, Yichi Zhang, Chau Yuen
- Source hits: arxiv
- Matched researchers: Xin Gao
- Matched groups: N/A
- Confidence: medium (author_alias)
- Topic keywords: N/A
- Journal/source: arxiv
- Publication date: 2026-09-28
- Article: http://arxiv.org/abs/2609.35347v1

Reinforcement learning can turn one language model into several specialists, each excellent at a single skill such as mathematics, coding or following instructions, but users need one model with all of these skills. Multi-teacher on-policy distillation (MOPD) merges them by letting the specialists teach one student: the student answers each prompt, and the specialist for that prompt's domain gives feedback on every token. This routing decides which specialist teaches, but not how strongly its feedback moves the shared student. In Qwen3.5 models at three sizes, we find that MOPD's student does not beat one taught by the best single specialist and gains little of the mathematics specialist's advantage. The feedback is unbalanced: instruction-following feedback is several times more spread out than mathematics feedback and dominates the student's updates. We propose Domain-Normalized MOPD (DN-MOPD), which keeps the routing and rescales each domain's feedback by its measured spread. On six public benchmarks, DN-MOPD improves the average score over MOPD at every size, across three random seeds and under two answer-length limits, and recovers most of the lost mathematics gain. Controls with fixed domain weights show that the gain comes mainly from turning down instruction-following feedback rather than turning up mathematics alone, and that fixed weights close to those DN-MOPD measures perform comparably. Combining specialists therefore requires deciding not only which one teaches, but also how strongly its feedback counts.

## 4. The Universal Classifier for Graph Learning

- Authors: Ben Finkelshtein, André Linhares, Petar Veličković, Bryan Perozzi, Mikhail Galkin
- Source hits: arxiv
- Matched researchers: Bryan Perozzi
- Matched groups: N/A
- Confidence: medium (author_alias)
- Topic keywords: foundation model
- Journal/source: arxiv
- Publication date: 2026-09-28
- Article: http://arxiv.org/abs/2609.36302v1

While foundation models have revolutionized natural language processing and computer vision by leveraging universal vocabularies, Graph Machine Learning (GML) remains fractured due to the absence of a unified feature and structural representation across diverse domains. Existing works claiming to be Graph Foundation Models (GFMs) are typically restricted to node-level predictions or require fixed feature dimensions, failing to provide a truly task-agnostic backbone for the full spectrum of graph learning applications. In this paper, we introduce the Universal Classifier (UC), which supports arbitrary feature and class cardinalities, unifying node-, edge-, and graph-level objectives under a single similarity-based classification objective. The UC reformulates all node-, edge-, and graph-level prediction tasks as maximizing similarity in the latent space: by lifting heterogeneous features and labels into 3D latent tensors, the model learns transferable features independent of specific input schemas. This architecture allows a single pre-trained model to generalize to node classification, node regression, and link prediction across unseen graphs with varying feature semantics. Experiments show strong zero-shot transfer performance across node-, link-, and graph-level tasks.

## 5. Explainable and Generalisable LLM-based Cognitive Decline Detection with Spontaneous Speech

- Authors: Ziyun Cui, Wen Wu, Chuan Shi, Shuguang Yang, Xueying Gui, Yan Zheng, Qiong Yang, Haiyan Zhao, Wei-Qiang Zhang, Ji Wu, Yelei Li, Nan Li, Chao Zhang
- Source hits: arxiv
- Matched researchers: Chuan Shi
- Matched groups: N/A
- Confidence: medium (author_alias)
- Topic keywords: large language model
- Journal/source: arxiv
- Publication date: 2026-09-28
- Article: http://arxiv.org/abs/2609.34217v1

Alzheimer's disease (AD) and mild cognitive impairment (MCI), which may precede AD, manifest early through subtle linguistic and acoustic alterations. Traditional diagnostics, however, are often resource-intensive and lack scalability for mass screening. To address these challenges, we introduce a novel bilingual speech large language model framework for automated, explainable cognitive screening. Unlike conventional pipelines that rely on error-prone automatic speech recognition, our system directly processes raw speech to learn joint acoustic-semantic representations, preserving critical prosodic cues often lost in transcription. Utilising our newly collected PUTH-AD dataset alongside multiple open-source corpora, we implemented a multi-task learning objective that simultaneously performs cognitive status classification and generates clinician-understandable natural language explanations. Our system achieved the highest average accuracy and AUROC across six dataset/task conditions, comparing three representative baselines. The system demonstrated cross-task transfer to held-out PUTH-AD task subsets, maintaining classification accuracy on an entirely unseen cognitive task without task-specific fine-tuning. Furthermore, clinician evaluation confirms that the generated explanations are both clinically relevant and largely consistent with the underlying speech evidence, supporting their potential utility in clinical interpretation. This study provides a scalable, objective, and explainable framework for speech-based cognitive screening, combining cognitive status classification with natural language explanations that clinicians can assess and verify, bridging the gap between advanced AI and clinical utility.

## 6. Hardware-Aware Features for CUTLASS Kernel Selection

- Authors: Shriram Chandran, Dominic Rinderer, Yakup Budanaz, Alexandru Calotoiu, Marcin Copik, Torsten Hoefler
- Source hits: arxiv
- Matched researchers: Torsten Hoefler
- Matched groups: N/A
- Confidence: medium (author_alias)
- Topic keywords: N/A
- Journal/source: arxiv
- Publication date: 2026-09-28
- Article: http://arxiv.org/abs/2609.35587v1

GPU libraries such as CUTLASS expose tens of thousands of semantically equivalent kernels for a single operation, making exhaustive autotuning expensive and execution-free selection difficult. Existing analytical selectors require hand-designed performance rules, while learned selectors operate on raw configuration parameters and must infer hardware consequences from data. We introduce a hardware-aware representation for CUTLASS kernel selection that augments candidate configurations with statically computable estimates of induced hardware behavior. We construct a dataset of 4.9 million CUTLASS kernels and train gradient-boosted and neural learning-to-rank models to rank candidates within each problem. On held-out exhaustive evaluation problems, hardware-aware representations reduce selection regret by up to 40\% relative to structural baselines and 64.2\% relative to NVIDIA's matrix-multiply heuristics. We further evaluate data-efficient cross-precision and epilogue-fusion transfer within CUTLASS GEMM, showing that explicitly representing candidate-induced hardware behavior provides a useful inductive bias for learned kernel selection.

## 7. Learning Propagation Geometry from Message-Passing Feedback

- Authors: Yingxu Wang, Kunyu Zhang, Xinwang Liu, Mengzhu Wang, Siyang Gao, Chang Tang, Nan Yin
- Source hits: arxiv
- Matched researchers: Xinwang Liu
- Matched groups: N/A
- Confidence: medium (author_alias)
- Topic keywords: N/A
- Journal/source: arxiv
- Publication date: 2026-09-28
- Article: http://arxiv.org/abs/2609.34711v1

Learning local geometry enables graph neural networks (GNNs) to adapt how they compare and integrate neighborhood information. However, estimating geometry from aggregated representations can overlook variation among individual messages and dependencies across feature dimensions. We propose GeoF, a recurrent framework that jointly evolves node features and propagation geometry through message-passing feedback. Each node maintains a local symmetric positive-definite geometry, initialized from a structure-aware prototype atlas and parameterized in block log-triangular coordinates. At each step, the geometry determines neighborhood weights, while triangular frame transport maps transformed source messages into the target node's local coordinates before aggregation. Weighted second-order statistics of residuals between aligned messages and the transformed target state capture directional variation and within-block dependencies, yielding a geometric update target. A shared controller learns complementary corrections through task supervision. A bounded log-triangular update combines these corrections, the target, and the previous geometric state while preserving positive definiteness. The geometry governs subsequent propagation, closing the feedback loop. With parameters shared across recurrent steps, task-specific readouts support node classification, link prediction, and graph classification. Experiments on benchmark datasets show that GeoF consistently outperforms state-of-the-art GNN baselines.

## 8. mmHRI: Towards Privacy-Preserving Human-Robot Interaction with Millimeter-Wave Radar

- Authors: Junqiao Fan, Yuxuan Hu, Bofan Lyu, Yanshuo Lu, Pengfei Liu, Jiarui Zhang, Fangqiang Ding, Lihua Xie, Gen Li, Jianfei Yang
- Source hits: arxiv
- Matched researchers: Yuxuan Hu
- Matched groups: N/A
- Confidence: medium (author_alias)
- Topic keywords: N/A
- Journal/source: arxiv
- Publication date: 2026-09-28
- Article: http://arxiv.org/abs/2609.34220v1

Assistive robots increasingly operate in many human-centered environments and perform various human-robot interaction (HRI) tasks, such as object delivery. However, most existing HRI systems rely on RGB cameras that continuously observe humans to respond to non-verbal commands, such as hand gestures. This raises privacy concerns in privacy- critical environments, such as hospital wards or restaurants, where direct camera observation of humans is restricted. To develop privacy-preserving HRI, we leverage millimeter-wave (mmWave) radar, which can sense human motion through privacy barriers without identifiable imagery. We propose mmHRI, the first multi-modal robot manipulation framework that achieves mmWave radar-guided privacy-preserving HRI. mmHRI introduces two key designs to mitigate the sparsity and temporal inconsistency of radar data in cluttered robot manipulation environments. First, we propose a dual-stream architecture that jointly learns from unfiltered raw radar tensors and radar point clouds to estimate both human actions and 3D poses. To mitigate signal inconsistency, mmHRI further incorporates a memory-based state-space model (MSSM) that retains historical radar features to reduce abrupt changes in pose/action. These estimated human states are then converted into structured textual robot instructions, which control a vision-language-action (VLA) policy for closed-loop robot manipulation and human-aware reactions. Our evaluation covers human action recognition and closed-loop delivery and retrieval. In the privacy-preserving curtain setting, mmHRI achieves 85.09% action-recognition accuracy, outperforming existing radar-based alternatives. Robot trials further demonstrate successful delivery and retrieval under visual occlusion, with stable task performance across unseen subjects, clutter configurations, and environments.

## 9. Structured Interaction, Visual Localization, and Robust Execution for Complex Web Tasks: A Technical Report on the WebRetriever Challenge

- Authors: Ziqi Zhang, Shaohui Li, Bing Li
- Source hits: arxiv
- Matched researchers: Ziqi Zhang
- Matched groups: N/A
- Confidence: medium (author_alias)
- Topic keywords: N/A
- Journal/source: arxiv
- Publication date: 2026-09-28
- Article: http://arxiv.org/abs/2609.35904v1

This report presents the web agent system developed for the WebRetriever Challenge. The system follows a structuredinteraction- first strategy, using semantic webpage information for routine browser operations and invoking visual perception only when structured representations are insufficient. Three key designs are introduced: grid-assisted visual localization for difficult-to-access controls, hierarchical context management for reducing redundant page and interaction history, and fault-aware execution mechanisms for stable multi-browser task processing. The system achieved a pass rate of up to 79% in local evaluation on Protocol 1. In the official Protocol 3 competition, it achieved a 59% pass rate with eight concurrent browser workers and ranked first overall, winning the WebRetriever Challenge.
