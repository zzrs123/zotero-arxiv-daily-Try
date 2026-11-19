# Paper Daily Reading - 2026-11-19

## 1. Every Measurement, Every Direction, All at Once: Multimodal Flow Matching for Molecules and Spectra

- Authors: Thorben Prein, Elton Pan, Rafael Gómez-Bombarelli, Santiago Miret
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-17
- DOI: Unavailable
- Categories: cs.LG, physics.chem-ph
- Relevance: 3.4470567370624305
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.22098v1
- PDF: https://arxiv.org/pdf/2611.22098v1
- Local PDF: pdf/2026-11-19_01_Every Measurement, Every Direction, All at Once_ Multimodal Flow Matching for Molecules and Spectra.pdf

Generative modeling in science is often data-limited, where experiments are expensive. However, each experiment may yield several coupled measurements of the same physical entity. Standard generative models often train only on a single direction, discarding supervision from the rest. We argue that each experiment contains more training signal than this asymmetry allows the model to exploit: random masking enables measurements to serve as either conditioning inputs or prediction targets, yielding multiple supervised denoising tasks from a single experiment. We investigate this premise with MOSAIC, a multimodal flow matching transformer over molecular 3D structure and UV, IR, and Raman spectra. MOSAIC is a single model that is capable of any-to-any generation: generating any subset of modalities from any disjoint subset of the others. On QM9S, MOSAIC achieves 88.8% molecular graph recovery, outperforming the strongest spectra-to-structure baseline by 23.2% in structure generation, while simultaneously outperforming a structure-to-spectra specialist model in spectral generation. Ablations show that the any-to-any objective improves structure generation over structure-only training across model sizes. Furthermore, MOSAIC supports arbitrary subsets of available measurements and enables molecular identification by matching generated spectra to experimental references.

## 2. OCCAM: Improved Single-Cell Representation Learning and Perturbation Effect Prediction

- Authors: Ihab Bendidi, Kian Kenyon-Dean, Alisandra K. Denton, Auguste Genovesio, Emmanuel Noutahi
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-16
- DOI: Unavailable
- Categories: q-bio.QM, cs.AI, cs.LG
- Relevance: 3.436788763699408
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.21959v1
- PDF: https://arxiv.org/pdf/2611.21959v1
- Local PDF: pdf/2026-11-19_02_OCCAM_ Improved Single-Cell Representation Learning and Perturbation Effect Prediction.pdf

Predicting the effects of genetic perturbations requires models that generalize beyond observed cell contexts and gene combinations. We introduce Occam, a multilayer perceptron (MLP) framework for representation learning and perturbation-effect prediction. Occam combines cell representations learned through denoising with gene interaction, text, and protein-sequence features. It achieves the highest aggregate representation scores for perturbation information and cell-type preservation with batch integration. In cross-context few-shot prediction, a perturbation and a cell context are each observed during training, but never together. Occam better captures the measured response patterns for these unobserved combinations than four retrained competitors or direct transfer of the same perturbation's measured effects from other training cell lines. Without fine-tuning, Occam best distinguishes perturbations among the evaluated models and simple baselines in cell lines held out from predictor training, across seen and unseen assays. Predicting expression levels accurately in these settings remains challenging. For double perturbations, which target two genes simultaneously, Occam composes learned single-gene responses to better capture the combined response and reduce expression error compared with competing models and summed single-gene effects. These gains extend to both strongly additive and weakly additive responses. Together, these results support simple MLPs for cell representation learning and perturbation-effect prediction across contexts and gene combinations.

## 3. When AUC Meets Generative Reconstruction: A Unified Principle for Balanced Visual Representation Learning

- Authors: Boyu Han, Qianqian Xu, Shilong Bao, Zhiyong Yang, Qingming Huang
- Source: arxiv
- Venue type: preprint
- Journal: IEEE Transactions on Pattern Analysis and Machine Intelligence
- Publication status: preprint
- Publication date: 2026-11-17
- DOI: https://doi.org/10.1109/tpami.2026.3754040
- Categories: Advanced Neural Network Applications, Domain Adaptation and Few-Shot Learning, Multimodal Machine Learning Applications, cs.AI, cs.CV, cs.LG
- Relevance: 3.352125604193297
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.22094v1
- PDF: https://arxiv.org/pdf/2611.22094v1
- Local PDF: pdf/2026-11-19_03_When AUC Meets Generative Reconstruction_ A Unified Principle for Balanced Visual Representation Learning.pdf

Multimodal large language models (MLLMs) require visual encoders that extract fine-grained visual features while constructing semantically disentangled and discriminative representations. Conventional methodologies encounter a fundamental trade-off: contrastive learning enhances inter-class discrimination by suppressing intra-class variability, whereas generative reconstruction emphasizes perceptual fidelity but lacks explicit comparative supervision. The naive aggregation of these objectives via composite loss functions often induces optimization conflicts and instability due to gradient interference within the shared latent space. To resolve this, we introduce a unified representation-learning paradigm that reformulates generative reconstruction as a discriminative ranking problem within the generative output manifold. Our approach maintains perceptual reconstruction as a supervisory signal and integrates a ranking-based discriminative constraint by systematically ordering matched and mismatched reconstruction outputs. This formulation embeds discriminative information seamlessly into the generative process, alleviating the risk of loss competition. Specifically, we propose AUC Generative Reconstruction (AUCGR), which optimizes the area under the ROC curve (AUC) by ensuring higher scores for matched pairs than for mismatched pairs, and Partial AUC Generative Reconstruction (pAUCGR), which addresses supervision bias by focusing on mismatched comparisons within reliable feature subspaces. The proposed objectives are designed to be plug-and-play, requiring no architectural modifications to existing generative reconstruction frameworks. Theoretical analysis establishes rigorous connections to AUC/pAUC optimization and provides generalization guarantees. Extensive experiments validate that our method advances both discriminative accuracy and fine-grained perceptual representation.

## 4. ST-FateFlow: Continuous Gene-Spatial Reconstruction with Differentiation-Potential Learning from Time-Resolved Spatial Transcriptomics

- Authors: Zhe Yu, Xiaobo Sun, Hao Wu
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-17
- DOI: Unavailable
- Categories: q-bio.GN
- Relevance: 3.2534432011853855
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.22256v1
- PDF: https://arxiv.org/pdf/2611.22256v1
- Local PDF: pdf/2026-11-19_04_ST-FateFlow_ Continuous Gene-Spatial Reconstruction with Differentiation-Potential Learning from Time-Resolved Spatial T.pdf

Time-resolved spatial transcriptomics provides a powerful view of dynamic biological processes by measuring cellular states together with their spatial organization across time. However, destructive profiling and experimental cost restrict observations to a few discrete time points collected from independent samples, with no known cell pairing across time. This makes it difficult to reconstruct gene expression and tissue organization at unobserved stages and to characterize differentiation-associated dynamics. Here, we introduce ST-FateFlow, a flow-matching framework for continuous gene-spatial dynamics and differentiation-potential learning. ST-FateFlow jointly learns gene-expression and spatial-coordinate velocity fields, enabling interpolation of missing time points and continuous modeling of transcriptional evolution and tissue remodeling. In parallel, it independently learns a time-conditioned differentiation potential, whose values organize cell states along inferred differentiation progressions and support the analysis of differentiation-associated transcriptional changes. Across multiple time-resolved spatial transcriptomics datasets, ST-FateFlow effectively captures coordinated gene-expression and spatial dynamics. Case studies further show that the learned potential landscapes are consistent with known developmental and regenerative trajectories and help identify candidate genes associated with differentiation progression.

## 5. Do Diffusion Models Learn to Generalize Basic Visual Skills?

- Authors: Amish Sethi, Boya Zeng, Wenhao Chai, Zhuang Liu
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-17
- DOI: Unavailable
- Categories: cs.CV, cs.LG
- Relevance: 3.1490016418455777
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.22427v1
- PDF: https://arxiv.org/pdf/2611.22427v1
- Local PDF: pdf/2026-11-19_05_Do Diffusion Models Learn to Generalize Basic Visual Skills.pdf

Diffusion models generate high-quality images, but how well they generalize is hard to measure. Current evaluations rely on human preference and prompt-following benchmarks for text-to-image models and on distribution-level metrics such as Fréchet Inception Distance (FID) and Inception Score (IS) for class-conditional models, but these cannot tell whether models learn basic visual skills or largely match training patterns. To address this gap, we introduce the Visual Generative Lab (VGL), a controlled experimental framework for studying how diffusion models learn and generalize basic visual skills, including size, position, rotation, count, color, shape, and their compositions. By generating synthetic training data for each skill from explicit rules, VGL allows precise measurement of generalization with task-specific, rule-based metrics. Training models from scratch on these data reveals three patterns in this controlled setting: (1) with our default design, extrapolation is limited: size and position degrade within a few pixels of the training range, count reaches only about 50% accuracy on out-of-range counts, and rotation extrapolation accuracy varies widely across seeds; (2) for compositional generalization, the number of distinct basic visual skill combinations matters more than dataset size; (3) skills mostly fail independently, except position. Code and data-generation scripts: https://github.com/AmishSethi/visual-generative-lab.

## 6. DNeo: Your Parallel Draft Model Needs Better Target Feature Encoding

- Authors: Jameson Sandler, Shane Bergsma, Mostafa Elhoushi, Bin Claire Zhang, Gavia Gray, Joel Hestness, Nolan Dey, Ferdinando Fioretto
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-16
- DOI: Unavailable
- Categories: cs.AI, cs.CL
- Relevance: 3.1380071886935146
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.21925v1
- PDF: https://arxiv.org/pdf/2611.21925v1
- Local PDF: pdf/2026-11-19_06_DNeo_ Your Parallel Draft Model Needs Better Target Feature Encoding.pdf

Speculative-diffusion decoding uses a small parallel drafter model to generate b draft tokens in one forward pass, which then undergo parallel verification via a larger target model. Faster inference can be achieved when multiple draft tokens pass verification simultaneously. Recent parallel draft architectures (DFlash, DSpark) improve draft quality by conditioning on rich features computed by the target, through a mechanism known as feature encoding. However, standard feature encoding mechanisms have three limitations: (1) they are lossy, applying encoding projections that are destructive to the underlying target feature-space via a discovered effect known as residual mixing, (2) they are memory-less, with no record of previously processed proposals, and (3) they utilize features sampled uniformly from across the target layers, omitting important hidden states. To address these issues, we propose Mixture-of-Features Attention (MoFA), a lightweight feature-encoding approach equipped with a working memory that encodes previously rejected proposals. Leveraging MoFA, rejection memory, and a set of further enhancements, including 2-tap causal convolutions, prefix-only cross-attention, and non-uniform target layer selection, the final architecture, DNeo, achieves 1.3x faster generation speed than SoTA (DFlash-2) without impacting drafter footprint or generation quality. DNeo marks a new state of the art in high quality, fast LLM inference.

## 7. LMLineage: Content Lineage and Context Governance for LLM Agents

- Authors: Wei Hou, Jingxin Geng, Xin Chen, Zheqing Jiang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-17
- DOI: Unavailable
- Categories: cs.AI, cs.CL
- Relevance: 3.115785896500035
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.22511v1
- PDF: https://arxiv.org/pdf/2611.22511v1
- Local PDF: pdf/2026-11-19_07_LMLineage_ Content Lineage and Context Governance for LLM Agents.pdf

Interpretability for AI agents should not be confined to understanding the model's internal weights. It must also cover the agent's reasoning and decision-making process over multi-source context. We present LMLineage, an out-of-band system that attributes every output sentence of an agent session to its supporting input spans with calibrated confidences, without requiring white-box access to the model or any additional inference passes. On top of the lineage metadata, we build concept-drift micro compaction: instead of waiting for the context-length limit and summarizing everything, the system detects when previously used input documents have stopped being referenced ("drifted") and surgically compacts only those, preserving user instructions verbatim. We evaluate on a multi-tier corpus: 71 gold annotated sentences from 10 Chinese web-QA cases, plus 90 turns of independently collected multi-turn sessions across three generator models (gpt-4o-mini, qwen3.8-27b, deepseek-v4-flash). Results show that (i) window-level embedding similarity is far better aligned with LLM paraphrasing than whole document or lexical matching; (ii) the greedy-window fast path is both faster and more accurate on average than exhaustive line-matching (a multiple-comparisons bias in the latter inflates web recall at the cost of overall accuracy); (iii) per-turn attribution completes in 1s on a single GPU, remaining stable as context accumulates to 40 turns; and (iv) concept-drift detection is conservative (0% false compaction) with recall bounded by attribution accuracy. We further describe the concept-drift micro compaction design and an interactive incident-tracing/memory-cleaning case study. A companion patent application covers the lineage construction method.

## 8. Hierarchical Diffusion Transformer for End-to-End Image Generation

- Authors: Xiaoyu Wu, Yifei Wang, Weihang Guo, Chen Wei, Lydia E Kavraki, Niloofar Mireshghallah, Steven Wu
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-17
- DOI: Unavailable
- Categories: cs.CV, cs.AI, cs.LG
- Relevance: 3.1126779650879777
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.22962v1
- PDF: https://arxiv.org/pdf/2611.22962v1
- Local PDF: pdf/2026-11-19_08_Hierarchical Diffusion Transformer for End-to-End Image Generation.pdf

Pixel-space diffusion learns visual representations and image generation jointly in a single end-to-end training stage, without a separately pretrained visual encoder. However, plain pixel-space Transformers still trail leading two-stage latent diffusion models in generation quality and training efficiency. We hypothesize that part of this gap arises from retaining one token per patch throughout the backbone, which does not explicitly encourage a visual hierarchy that summarizes related content at progressively coarser levels. To address this, we introduce Hierarchical Diffusion Transformers (HiT), which progressively group related tokens and represent each group with a single token. The main Transformer bottleneck processes these compact group tokens, and ungrouping restores features to their original image positions. A compression budget regulates the average compression ratio across the batch, allowing group memberships and counts to vary across images and diffusion timesteps during both training and generation. The model exhibits emergent semantic structure, learning to group coherent objects and object parts without segmentation labels. In text-to-image generation, HiT further learns to group caption words with image patches depicting the same concepts, without region annotations. HiT achieves 1.48 FID on ImageNet $256\times256$ and reaches comparable generation quality to JiT using approximately 40\% of its cumulative training FLOPs. For text-to-image generation, HiT exceeds UniLiP's average score across five benchmarks with roughly $6\times$ fewer denoiser parameters and $3\times$ fewer forward FLOPs. These results suggest that learning a visual hierarchy within the generator breaks down the barrier to stronger image generation without external visual pretraining.

## 9. From Perception to Simulation: Unveiling and Empowering Mental Spatial Dynamics in MLLMs

- Authors: Jiachun Li, Zhuoran Jin, Kang Liu, Jun Zhao
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-17
- DOI: Unavailable
- Categories: cs.CV, cs.AI, cs.CL
- Relevance: 3.0627219600831825
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.22541v1
- PDF: https://arxiv.org/pdf/2611.22541v1
- Local PDF: pdf/2026-11-19_09_From Perception to Simulation_ Unveiling and Empowering Mental Spatial Dynamics in MLLMs.pdf

Spatial reasoning is a fundamental component of world understanding for Multimodal Large Language Models (MLLMs). While existing research has advanced the perception of spatial relations in static scenes, the domain of dynamic spatial simulation remains relatively unexplored. To bridge this gap, we introduce MentalGrid, a benchmark focused on spatial reasoning tasks that require models to simulate evolving spatial states without intermediate visual feedback. Extensive evaluation on our benchmark reveals a significant deficiency in the spatial simulation capabilities of existing models. Specifically, we find that performance is constrained by perceptual limitations in simple simulation scenarios and hindered by inadequate multi-step reasoning as complexity increases. To address these challenges, we propose a three-stage curriculum learning framework utilizing 16k specialized spatial reasoning samples. This approach yields SpatialWalker, which achieves a 33.8% average improvement over its base model, surpassing proprietary models like Gemini-3-Flash in spatial simulation. Furthermore, SpatialWalker demonstrates robust generalization, maintaining a 4.9% average gain on out-of-domain benchmarks, demonstrating the pivotal role of spatial simulation as a fundamental building block for broader spatial intelligence.

## 10. EpiPack: A computational framework for reference mapping and out-of-reference detection for single-cell ATAC-seq data with heterogeneous peak features

- Authors: Yuqi Cheng, Xiuwei Zhang
- Source: openalex
- Venue type: journal
- Journal: Nature Communications
- Publication status: published
- Publication date: 2026-11-17
- DOI: https://doi.org/10.1038/s41467-026-78924-9
- Categories: Single-cell and spatial transcriptomics, Genomics and Chromatin Dynamics, Epigenetics and DNA Methylation
- Relevance: 3.059913895472406
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://doi.org/10.1038/s41467-026-78924-9
- PDF: https://www.nature.com/articles/s41467-026-78924-9_reference.pdf
- Local PDF: pdf/2026-11-19_10_EpiPack_ A computational framework for reference mapping and out-of-reference detection for single-cell ATAC-seq data wi.pdf

Despite substantial recent advances in query mapping and cell type or cell state discovery tools, their application to single-cell assay for transposase-accessible chromatin using sequencing (scATAC-seq) data remains challenging. The heterogeneous nature of peak feature spaces across samples hinders the effectiveness of existing methods, while the absence of dedicated tools for detecting perturbed cell types and states in scATAC-seq data further limits the depth of downstream analyses. To address these limitations, we present EpiPack, an integrative computational toolkit that leverages heterogeneous transfer learning and graph-based modeling strategies to advance scATAC-seq analysis. At its core, the Peak Embedding Informed Variational Inference (PEIVI) framework within EpiPack enhances mappable reference construction, query mapping, and label transfer, demonstrating that leveraging heterogeneous features in scATAC-seq data outperforms methods relying solely on conventional homogeneous features. In addition, EpiPack’s global-local out-of-reference (OOR) detection framework achieves robust and efficient detection of perturbed cell types and states, extending the utility of scATAC-seq to disease and perturbation contexts. With its modular design and transferable pre-trained references, EpiPack can be readily applied to diverse analytical tasks and is available as a Python package at https://github.com/ZhangLabGT/EpiPack. EpiPack maps single-cell chromatin accessibility data across heterogeneous datasets and identifies cell types and states absent from reference atlases, enabling analysis of disease-associated cellular changes.

## 11. TeleChat to Xing4: Advancing Frontier Agentic Models on Domestic Chips and Frameworks

- Authors: Xingchen AGI Lab, :, Baotian Hu, Bingkai Yang, Boyang Wang, Changzai Pan, Chao Lyu, Chao Wang, Chen Li, Chenshuo Pan, Chenyu Lin, Chenyuan Zhang, Chongming Liu, Dawei Fan, Di Wu, Dong Guo, Dong Li, Dongfang Li, Enlin Liu, Fanye Xiao, Fengkai Li, Fubei Yao, Gang Lin, Han Gao, Hanming Wu, Haowei He, Huapeng Liu, Hua Wang, Huinan Xu, Jiahong Xiong, Jiaxin Peng, Jianxiang Ma, Jianxing Zhuge, Jie Zhang, Ji Xiong, Jinglin Chen, Jingqi Li, Jingxuan Li, Jiwang Ye, Junchen Li, Junbiao Li, Junyang Wu, Kaidong Yu, Kaipeng Jia, Kehai Chen, Kuai Li, Laobin Liu, Lei Li, Libo Qin, Lingling Shi, Luwen Pu, Menghao Xu, Mengjiao Bao, Mengqi Chen, Min Zhang, Mingrui Wang, Naying Wang, Peicong Han, Peiming Guo, Pengfei Li, Qiang Feng, Qi Wang, Qingjun Zhu, Qingli Li, Qitai Ding, Qiyi Xie, Quanchao Zhao, Rongbao Han, Rui Xue, Ruiyu Fang, Ruiting Song, Shijie Li, Shiquan Wang, Shuangyong Song, Sishi Xiong, Teng Su, Wankang Bao, Weijie Zhang, Wei Mao, Weiwei Fu, Weiyang Huang, Wenmin Deng, Wenqing Hu, Wujie Zhong, Xi Yu, Xiaohui Hu, Xiaomin Fang, Xiaomeng Huang, Xiaoqiong Shi, Xiaotong Shang, Xiaoyu Li, Xinglei Xu, Xin Jiang, Xin Wang, Xin Zhang, Xinzhang Liu, Xue Liu, Xuefeng Bai, Xuewei He, Yahan Li, Yanhan Zhang, Yanlei Xue, Yanzhang Wu, Yang Yu, Yi Liu, Yin Zhang, Yingyan Li, Yitong Yao, Yixuan Li, Yongqiang Xia, Yongxiang Li, Yinzhou Zhu, Yu Zhao, Yuhao Jiang, Yunpeng Zhang, Yuting Lin, Yuxuan Wu, Yuyao Huang, Yuyi Wang, Zebo Peng, Zhenwu Pei, Zhenxiong Li, Zhao Wang, Zhaoxi Zhang, Zhihao Yang, Zhiqiang Dong, Zhiwei Yan, Zhilong Lu, Zhonghao Guo, Zhongheng Wu, Zhongjiang He, Zhongqiu Li, Zhu Yuan, Zhuoru Jiang, Zhuoyi Wei, Zijia Guo, Zilu Huang, Zhipeng Guo, Zirui Li, Zihan Wang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-17
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 2.983622172136342
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.22115v1
- PDF: https://arxiv.org/pdf/2611.22115v1
- Local PDF: pdf/2026-11-19_11_TeleChat to Xing4_ Advancing Frontier Agentic Models on Domestic Chips and Frameworks.pdf

We present Xing 4, a series of large language models that extends the TeleChat lineage through coordinated advances in model architecture and training infrastructure on Ascend. This report describes the design principles and systems engineering behind the series, spanning architecture selection, large-scale pretraining, and reasoning and agentic post-training. We study how sparse activation, attention design, model depth and width, and speculative decoding balance model capacity with computation, memory access, and execution overhead. Our pretraining infrastructure builds on MindSpore HyperParallel, combining topology-aware hybrid sharding, efficient distributed optimizer execution, and coordinated management of long-sequence workloads and activation memory. CPU affinity and core isolation further reduce host scheduling interference. Together, these mechanisms support the pretraining of a 285B-parameter model on 8,192 Ascend 910C cards, providing a concrete setting for the architectural and systems studies. For post-training, we introduce TeleGym, a unified agent execution platform that connects execution, evaluation, and trajectory construction to policy optimization. Disaggregated asynchronous execution, bounded oversampling, and partial rollout accommodate heterogeneous task durations while preserving trajectory continuity across policy updates. Together, these advances establish an Ascend-oriented training foundation for the continued development of Xing 4 across model scales and increasingly demanding reasoning and agent workloads.

## 12. LoopPrune: Recurrent Pruning for Looped Diffusion Transformers

- Authors: Weizhong Huang, Huaijia Kou, Yan Zhang, Fei Chao, Xiawu Zheng, Liujuan Cao
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-17
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 2.973141475693961
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.22757v1
- PDF: https://arxiv.org/pdf/2611.22757v1
- Local PDF: pdf/2026-11-19_12_LoopPrune_ Recurrent Pruning for Looped Diffusion Transformers.pdf

Looped diffusion Transformers reuse shared blocks to deepen computation and match larger models with fewer parameters, reducing storage and deployment burdens. Yet repeated attention and MLP computations remain costly. Pruning reduces storage and computation by removing redundant parameters or units. Training-free methods struggle to resolve recurrent contributions, while training-based methods lack explicit constraints on position-specific errors affecting later inputs and final outputs. We propose LoopPrune, a pruning and recovery framework addressing these requirements. Recurrent importance estimation combines shared-removal effects and position variation to select a shared structure; shared reconstruction pools recurrent input statistics to compensate weights. Loop-position recovery compares complete denoising predictions at identical student states and matches text guidance, updating all student parameters against a fixed dense teacher. Extensive experiments across four open-source models, six benchmarks, and three pruning paradigms demonstrate effectiveness. At 30% structured parameter pruning, Looped-DiT B/16 retains 93.14% of dense six-benchmark average accuracy, exceeding the best baseline by 9.49%. Across PyTorch, vLLM-Omni, and SGLang Diffusion, pruned SDXSv3 reduces peak allocated GPU memory by 34.36-44.64% and accelerates denoising 1.46-1.74x over dense models.

## 13. NVIDIA Kumo Tabular: Pushing the Accuracy-Efficiency Frontier for Tabular Prediction

- Authors: Jingang Qu, Valter Hudovernik, Martin Jurkovič, Cedric Lorenz, David Holzmüller, Federico Lopez, Dmitry Gordeev, Akihiro Nitta, Ramona Bendias, Ardrian Wong, Vedaant Jain, Vignesh Kothapalli, Gilberto Titericz Junior, Jure Leskovec, Matthias Fey
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-17
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 2.9226626126126733
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.23001v1
- PDF: https://arxiv.org/pdf/2611.23001v1
- Local PDF: pdf/2026-11-19_13_NVIDIA Kumo Tabular_ Pushing the Accuracy-Efficiency Frontier for Tabular Prediction.pdf

We introduce Kumo Tabular, a family of open tabular foundation models for classification and regression, in three sizes: Kumo Tabular-S (27M parameters), Kumo Tabular-M (61M), and Kumo Tabular-L (214M). Pretrained only on artificial tables from the Kumo prior, they can make predictions on new tables without any training. In our approach, a table encoder compresses each row into an embedding, and an in-context learning transformer predicts the unlabeled rows from the labeled ones. Kumo Tabular introduces architectural innovations that improve both training stability and predictive performance, enabling the model to scale up to 150M cells on modern GPUs. Kumo Tabular-L ranks first on eight benchmarks: TabArena, TALENT, BeyondArena, ScoringBench, STRABLE, MulTaBench, RamanBench, and TabBench-Bio. These cover probabilistic regression, tables with over 1M rows or 100K columns, and tables with strings, text, or images. Accuracy improves with model size in all tested comparisons. All three sizes lie on the accuracy-speed frontiers of TabArena and BeyondArena. Kumo Tabular-L predicts faster than the runners-up, LimiX-2 on TabArena (36 times) and TabPFN-3.5 on BeyondArena (1.7 times). Weights and pretraining code are released under OpenMDW-1.1 and Apache 2.0, respectively.

## 14. Inventa: Decentralized Self-Improving Agents for Autonomous Scientific Discovery

- Authors: Prithwish Jana, Nikos Kanakaris, Purak Jain, Anoop Deoras, Sahika Genc
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-16
- DOI: Unavailable
- Categories: cs.LG, cs.AI
- Relevance: 2.895945205878609
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.21847v1
- PDF: https://arxiv.org/pdf/2611.21847v1
- Local PDF: pdf/2026-11-19_14_Inventa_ Decentralized Self-Improving Agents for Autonomous Scientific Discovery.pdf

Large language model (LLM) agents can generate research ideas and improve scientific discovery through iterative experimentation. However, increasing the number of agents or iterations does not automatically translate to producing more diverse or feasible ideas. Agents may converge on similar candidates, propagate unsupported claims through shared memory components and repeatedly apply search strategies that no longer yield any improvements.
  We introduce Inventa, a framework for automated scientific discovery that employs autonomous research units and verified shared knowledge. Each unit creates a lineage of candidate ideas using a mutator agent. A local orchestrator agent periodically adapts the mutator's harness. When progress stalls, the orchestrator agent replaces its model or restarts the idea evolution process. Verifiers evaluate each candidate idea and record verified improvements, useful components and constraint violations in a shared knowledge, the only channel between units. We evaluate Inventa on five benchmarks spanning the research cycle, covering retrieval (ScholarCatalyst), ideation (IdeaBench), proposal writing (IdeaScientist), and scientific law discovery (EurekaBench, SciLaws-Bench). It leads all five, achieving 73.6% on EurekaBench versus 56.2% for CORAL. On IdeaBench, it discovers 26.0 novel ideas per paper, compared with 18.6 for ResearchAgent, with 82% fewer model calls.

## 15. Weight-Space Programming Doesn't Need Transformers

- Authors: Hyunjong Ok, Jaeho Lee
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-17
- DOI: Unavailable
- Categories: cs.LG, cs.AI, cs.CL
- Relevance: 2.8865948093732663
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.22055v1
- PDF: https://arxiv.org/pdf/2611.22055v1
- Local PDF: pdf/2026-11-19_15_Weight-Space Programming Doesn't Need Transformers.pdf

Standard neural architectures such as the Transformer were chosen because they train well with gradient descent and run fast on GPUs. In weight-space programming, a large language model (LLM) writes target weights by hand without gradient-based training, so those reasons no longer apply. Should we keep the Transformer? Given minimal guidance, ten labeled examples, and a sandbox, mainly on multiple-choice questions, we task three frontier LLMs with either generating the weights of a fixed architecture or designing the architecture themselves. When free to design, all three compile plain-text facts into a sparse table queried by a fixed procedure, reaching up to 54.4% test accuracy. An LLM-designed model achieves higher test accuracy than the most accurate released Transformer that the same LLM wrote while using about 1,800x fewer parameters. Without gradients, they choose a table, in which the LLM can state what each weight means and can find and rewrite a wrong one. Each wrong answer points to one row, and removing a row changes about one other answer. From this, we propose an associative-memory-based model up to 17x faster on GPUs than a same-sized Transformer. We also test pretrained weights, other benchmarks, and tasks where models generate answers. Pretrained LLMs remain more accurate; the claim concerns which structure to build when writing weights.

## 16. Scaling Laws for Vision-Language Fusion

- Authors: Seng Pei Liew, Teppei Suzuki, Seiya Tokui
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-17
- DOI: Unavailable
- Categories: cs.LG, cs.CV
- Relevance: 2.8850735422656184
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.22351v1
- PDF: https://arxiv.org/pdf/2611.22351v1
- Local PDF: pdf/2026-11-19_16_Scaling Laws for Vision-Language Fusion.pdf

Vision-language models (VLMs) have emerged as central foundation models combining multimodal perception with text comprehension. While VLMs are traditionally built via late fusion by continued pre-training an off-the-shelf language model on multimodal (image-text) data, mixing modalities from the start of pre-training (early fusion) has recently gained traction. However, the fundamental trade-offs between these paradigms remain poorly understood, resulting in expensive and heuristic-driven training recipes. In this paper, we systematically analyze the learning dynamics of these multimodal pre-training processes, showing that validation losses during vision-language fusion can be modeled by separating the base learning trajectory, where different data types contribute at distinct rates, from a distribution shift driven by the competition between modalities. We derive a scaling law that unifiedly describes these dynamics, enabling accurate loss predictions across mixture ratios, training steps, and model sizes. Crucially, our law characterizes the trade-off between early and late fusion: under a fixed data budget, early fusion preserves text performance while late fusion favors vision performance, yielding a trade-off that increasingly tilts toward early fusion as model size scales. Extensive experiments confirm that our scaling law reliably captures multimodal learning dynamics and governs fusion decisions.

## 17. Echidna: a Bayesian framework for integrative inference of copy number alterations impacting phenotypic plasticity

- Authors: Joy Linyue Fan, Mingxuan Zhang, William O'Brien, Joshua D. Myers, Sharanya Chatterjee, Kevin Hoffer-Hawlik, Nicolas Beltran-Velez, Alexander Preau, Isha Arora, Johannes C. Melms, Jana Biermann, Edridge K. D’Souza, Somnath Tagore, Timothy R. Olsen, Siran Li, Peter A. Sims, Benjamin Izar, Elham Azizi
- Source: openalex
- Venue type: journal
- Journal: Nature Methods
- Publication status: published
- Publication date: 2026-11-16
- DOI: https://doi.org/10.1038/s41592-026-03279-4
- Categories: Cancer Genomics and Diagnostics, Genomic variations and chromosomal abnormalities, Single-cell and spatial transcriptomics
- Relevance: 2.8770731731102748
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://doi.org/10.1038/s41592-026-03279-4
- PDF: https://www.nature.com/articles/s41592-026-03279-4.pdf
- Local PDF: pdf/2026-11-19_17_Echidna_ a Bayesian framework for integrative inference of copy number alterations impacting phenotypic plasticity.pdf

The ability of cells to adapt their behavior in response to genetic or environmental changes is a fundamental biological process that drives cellular diversity in both normal and pathological contexts, including in tumor evolution. Copy number alterations (CNAs), which can include large-scale changes in genomic ploidy, play a key role in creating adaptive advantages in evolving cell populations. However, tracing these populations across experiments and disentangling the role of CNAs from other sources of transcriptional variability remains challenging and expensive. Here we present Echidna, a Bayesian hierarchical model that integrates single-cell RNA sequencing and bulk whole-genome sequencing data to enable robust integrative inference of CNAs, jointly across samples and treatment time points, to better understand the impact of genomic events on cellular phenotype. Applying Echidna to patient tumor specimens, we demonstrate its superior performance in clonal reconstruction and derive insights into therapy resistance mechanisms.

## 18. DARWIN: a Geospatial Foundation Model for Marine Intelligence

- Authors: Coen van den Elsen, Laurens Geffert
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-17
- DOI: Unavailable
- Categories: cs.AI, physics.ao-ph
- Relevance: 2.8729811140867403
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.22496v1
- PDF: https://arxiv.org/pdf/2611.22496v1
- Local PDF: pdf/2026-11-19_18_DARWIN_ a Geospatial Foundation Model for Marine Intelligence.pdf

We present DARWIN, a geospatial foundation model for marine intelligence. Recent Earth-observation foundation models have concentrated on terrestrial domains. The marine realm poses distinct challenges: missingness, multi-modal physical and biogeochemical variables, sparse labels, and dynamics that are transient, multi-scale, and non stationary over time. DARWIN adapts a masked-autoencoder backbone to these properties through missingness-aware encoding, expanded spatial and temporal masking, and Fourier-style positional embeddings, and is pretrained on 26 years of global Copernicus reanalysis together with GEBCO bathymetry.
  On predicting chlorophyll-a, the pretrained backbone attains the lowest monthly relative error in every month of 2022, outperforming both no-encoder baselines and an identically architected random-init encoder. At 10% of the supervised training data, DARWIN already surpasses the random-init model trained on 100% of the data. Embedding analysis and qualitative reconstructions show that DARWIN captures coherent oceanographic structure rather than memorising input statistics, providing a scalable backbone for downstream marine applications such as anomaly detection, species distribution modelling, and environmental monitoring.

## 19. Communicate the Change: Efficient Expert Parallelism via Activation Compression

- Authors: Fengyuan Liu, Jay Gala, Siva Reddy, Dzmitry Bahdanau
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-17
- DOI: Unavailable
- Categories: cs.LG, cs.AI, cs.DC
- Relevance: 2.860354005563852
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.22215v1
- PDF: https://arxiv.org/pdf/2611.22215v1
- Local PDF: pdf/2026-11-19_19_Communicate the Change_ Efficient Expert Parallelism via Activation Compression.pdf

Scaling has driven the success of large language models (LLM), with sparse mixture-of-experts (MoE) architectures enabling greater parameter capacity without a proportional increase in computation. At large scales, MoE models rely on expert parallelism to distribute experts across devices. Each MoE layer requires two synchronous collective communication steps during inference: dispatching hidden states to the activated experts and combining the resulting expert outputs. As compute throughput has outpaced interconnect bandwidth, these synchronous collectives have become a major bottleneck to MoE scaling and efficiency. We address this challenge with EchoMoE, a lightweight architecture modification that retrofits existing MoE models, requiring approximately 8,500x fewer training tokens than full pretraining. Motivated by the observation that transformer blocks update the residual stream incrementally, we use a hidden state from an earlier layer as a reference and communicate only the compressed difference between it and the current state, rather than communicating each hidden state in full. EchoMoE periodically refreshes these reference states and transmits only the compressed differences synchronously, reducing the traffic on latency-critical paths without significant computational overhead. EchoMoE reduces inter-node communication volume by 58% and improves throughput by 22.6%, while preserving average performance within 3.8 percentage points across 18 benchmarks. EchoMoE further improves inference throughput by up to 2.38x over bandwidth-constrained Ethernet, paving the way for wide-area distributed inference. EchoMoE also tolerates quantization of the communicated representations without measurable quality loss. We release an efficient implementation for applying EchoMoE to pretrained MoE models, together with an inference integration for vLLM.

## 20. Amortizing Tempered Sampling with Corrected Self-Training

- Authors: Hoang-Viet Nguyen, Hai-Dang Dau, Alexandre H. Thiéry
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-17
- DOI: Unavailable
- Categories: stat.ML, cs.LG
- Relevance: 2.8545434584380684
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.23072v1
- PDF: https://arxiv.org/pdf/2611.23072v1
- Local PDF: pdf/2026-11-19_20_Amortizing Tempered Sampling with Corrected Self-Training.pdf

Learning a neural sampler can reduce the cost of repeated sampling from an un-normalized distribution, but obtaining good training data remains difficult. We develop a corrected self-training scheme across a sequence of tempered targets, making use of importance sampling and Markov chain Monte Carlo to correct the samples and replay buffers to store them. We introduce Sequential Score Sampler (SSS) as a particular case. In SSS, the proposal is a score-based diffusion trained by regression on energy gradients; and the samples are corrected by importance weights on the path space. After training, samples can be collected directly from the model, from its importance-corrected proposals, or from the final-temperature buffer. The method amortizes repeated sampling by encoding the global structure of the target in the model. SSS achieves competitive sampling accuracy across the benchmarks and, on several targets, uses shorter runtimes with fewer energy evaluations than competing samplers.

## 21. RISA: Recoverable Sparse Attention for Block-Diffusion Language Models

- Authors: Xinrui Zhong, Fanjiang Ye, Yuke Wang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-17
- DOI: Unavailable
- Categories: cs.CL, cs.LG
- Relevance: 2.8491588828560444
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.22191v1
- PDF: https://arxiv.org/pdf/2611.22191v1
- Local PDF: pdf/2026-11-19_21_RISA_ Recoverable Sparse Attention for Block-Diffusion Language Models.pdf

Block-wise diffusion language models (DLMs) refine multiple tokens in parallel, offering an alternative to token-by-token autoregressive decoding. Their long-context inference, however, remains bottlenecked by memory-bound attention: every denoising step repeatedly reads a growing historical key--value (KV) cache. Directly applying sparse attention does not fully solve this problem, because different queries can select different pages, inflating the block's collective read set, while repeated support construction adds overhead and permanent eviction can discard information needed later. We present RISA, a recoverable sparse-attention method with shared read plans for block-wise DLMs. RISA exploits the fact that historical KV remains fixed within a block while queries evolve across denoising steps. Newly generated history is organized into exact priority and recovery tiers; seed queries then build a protected, bounded read plan whose indices are reused across the block while attention is recomputed with fresh queries and current-block KV. This separates history preservation from repeated reading and amortizes sparse-support construction without changing the backbone or decoder. On DreamReasoner-8B, RISA retains comparable task performance. At 32K, the default configuration speeds up attention by $2.67\times$ and fixed-trajectory requests by $1.36\times$ over dense, and attention speedup reaches $5.53\times$ at 128K. Across eight settings on three models, RISA decodes faster than the tested MAGE, QUEST, and LoSA budgets at matched KL.

## 22. DSADiff: Data Structure-Aware Diffusion for Crystal Structure Prediction via Mitigating Complexity- and Imbalance-Induced Biases

- Authors: Jiang Xiaobo, Dinghong Lai
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-17
- DOI: Unavailable
- Categories: cs.LG, cond-mat.mtrl-sci
- Relevance: 2.8311080715154437
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.22050v1
- PDF: https://arxiv.org/pdf/2611.22050v1
- Local PDF: pdf/2026-11-19_22_DSADiff_ Data Structure-Aware Diffusion for Crystal Structure Prediction via Mitigating Complexity- and Imbalance-Induce.pdf

Crystal Structure Prediction (CSP) is an important step in accelerating the generation and discovery of new materials. In recent years, diffusion-based CSP methods have made significant progress. However, existing models still suffer from generation bias when facing diverse materials spaces, while systematic approaches for tracing the sources of such performance variations remain limited. To address this issue, we propose LAS (Layered Analysis Strategy), a mechanism analysis framework that identifies crystal complexity and elemental composition imbalance as two key factors affecting generation difficulty and further reveals their relationships with model generation performance. Building on these findings, we further propose DSADiff (Data Structure-Aware Diffusion), a data structure-aware diffusion model that transforms the key factors identified by LAS into a unified generation difficulty representation and uses it to jointly drive feature modeling and training strategy optimization. This enables the model to adapt its representation and generation capability to samples with different data structures and difficulty levels, thereby mitigating learning bias across samples. Experiments on three CSP benchmark datasets, including Carbon-24, demonstrate that DSADiff consistently improves both Match Rate and RMSE, with a maximum Match Rate improvement of 9%, surpassing existing state-of-the-art methods and achieving new state-of-the-art performance. This work deepens the understanding of diffusion-based CSP models from the perspective of generation bias and provides a new direction for designing less biased generative models for complex materials spaces.

## 23. STRUCT: a statistical approach to detect conserved RNA secondary structures from raw sequencing data without multiple sequence alignment

- Authors: Julie Fangran Wang, Arjun Rustagi, Julia Salzman
- Source: openalex
- Venue type: journal
- Journal: Genome biology
- Publication status: published
- Publication date: 2026-11-17
- DOI: https://doi.org/10.1186/s13059-026-04324-3
- Categories: RNA and protein synthesis mechanisms, Genomics and Phylogenetic Studies, RNA Research and Splicing
- Relevance: 2.8196532461571575
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://doi.org/10.1186/s13059-026-04324-3
- PDF: Unavailable
- Local PDF: Not downloaded

Abstract Covariation among orthologous sequences is an established evolutionary signal of conserved RNA secondary structures. We present STRUCT (Statistical Testing of RNA Units with Covariation Traits), a covariation-based statistical test that applies to raw sequencing data, bypassing assembly and multiple sequence alignment required by existing covariation methods. Simulations demonstrate false discovery rate control and high power under matched model assumptions. STRUCT rediscovers known HIV structural elements in provirus sequences, identifies conserved rRNA structures, and prioritizes putative viral RNA structures in metatranscriptomics samples. STRUCT offers a novel approach for high-throughput detection of conserved RNA structures and hypothesis generation for viral discovery.

## 24. StitchRAG: Constructing Compact and Evidence-Preserving Contexts for RAG with Diffusion-Based Stitching

- Authors: Minsang Kim, Junpyo Lim, Heeje Cho, Seungjun Baek
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-17
- DOI: Unavailable
- Categories: cs.CL, cs.AI
- Relevance: 2.8178985663246046
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.22766v1
- PDF: https://arxiv.org/pdf/2611.22766v1
- Local PDF: pdf/2026-11-19_24_StitchRAG_ Constructing Compact and Evidence-Preserving Contexts for RAG with Diffusion-Based Stitching.pdf

Retrieval-augmented generation (RAG) improves factuality by grounding large language models (LLMs) in external evidence. However, long retrieved contexts incur computational overhead and can even hurt performance due to noisy or irrelevant content. We propose \textsc{StitchRAG}, a framework for constructing compact context in RAG. \textsc{StitchRAG} builds a faithful, information-dense context while dynamically compressing the retrieved passages. We adapt the size reduction ratio to each passage by formulating a utility maximization trading-off the retained information and computation costs. We then extract answer candidates and query-related keywords from passages as anchors and collect passage sentences containing anchors under the derived size constraint. Finally, we connect or stitch the collected sentences together using text diffusion to form a coherent and natural context. Experiments on five open-domain QA benchmarks show that \textsc{StitchRAG} consistently outperforms diverse multi-step and compression baselines. Extensive ablations show the effectiveness of dynamic size allocation, anchor preservation, and diffusion-based stitching.

## 25. RSI-Prime: Training Models to Train Models

- Authors: Dewu Zheng, Yang Ye, Hongyu Zhang, Jun Yu, Yanlin Wang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-17
- DOI: Unavailable
- Categories: cs.AI, cs.LG
- Relevance: 2.805375175621762
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.23138v1
- PDF: https://arxiv.org/pdf/2611.23138v1
- Local PDF: pdf/2026-11-19_25_RSI-Prime_ Training Models to Train Models.pdf

Enabling large language models (LLMs) to autonomously conduct training and improve target models is an important foundation for recursive self-improvement (RSI). As LLMs expand their role from being trained to conducting training, their model-training capability warrants dedicated study and systematic development. To this end, we construct RSI-Prime, a dataset for improving model-training capability, comprising 350 complete experimental trajectories across seven task categories. To help LLMs learn to make high-quality experimental decisions from training practice, we perform fine-grained decision identification and quality annotation, then apply decision-level loss masking to exclude supervision on low-quality behavior. Experiments with GLM-5.3 on PostTrainBench, a benchmark for autonomous post-training, show that training on RSI-Prime yields a 31.95% relative improvement in overall performance over the original GLM-5.3, highlighting a path toward future RSI systems in which models autonomously sustain their own advancement.

## 26. Margin Dynamics for Large Language Model Alignment

- Authors: Xingzi Xu, Mehmet Saygin Seyfioglu, Karim Bouyarmane
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-16
- DOI: Unavailable
- Categories: cs.LG, cs.AI
- Relevance: 2.8019373650847705
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.21766v1
- PDF: https://arxiv.org/pdf/2611.21766v1
- Local PDF: pdf/2026-11-19_26_Margin Dynamics for Large Language Model Alignment.pdf

Practitioners choose among LLM alignment methods largely by trial and error. We provide a theoretical foundation: each pairwise method defines a vector field on the probability simplex that governs how the model redistributes mass between preferred and dispreferred completions. Projecting onto a single preferred/dispreferred pair reduces this to a one-dimensional margin ODE with a closed-form solution. These solutions reveal that DPO margins grow without bound (logarithmically as $O(\log t)$ in the gradient-flow limit) while IPO margins converge to a finite $1/(2τ)$; that label noise induces a qualitative phase transition in DPO (unbounded $\to$ bounded) but affects IPO only quantitatively; and that gradient concentration under asymmetric weighting governs trainability at scale. We confirm all three predictions across five model families spanning four benchmarks. The closed-form solutions also enable principled method design: we prove that adding any label smoothing $\varepsilon > 0$ to SimPO creates a finite margin attractor at $Δ^* = β^{-1}\log((1-\varepsilon)/\varepsilon)$, while $\varepsilon = 0$ (standard SimPO) has no attractor. We test this across three models (8B-9B) and confirm the prediction: the theory-derived configuration (TPO-S, $\varepsilon = 0.05$) is competitive with the strongest baselines, attaining the highest mean IFEval score among the compared methods on all three, validating that the predicted finite attractor is a usable operating point rather than proposing a new state-of-the-art loss.

## 27. VRLLM: Turning LLMs into Powerful Tabular Classifiers

- Authors: Yingtong Dou, Shubham Jain, Junpeng Wang, Hadi Abdullah, Vineeth Rakesh Mohan, Yuzhong Chen, Liang Wang, Yiwei Cai
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-17
- DOI: Unavailable
- Categories: cs.LG, cs.CL
- Relevance: 2.801010259803922
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.22308v1
- PDF: https://arxiv.org/pdf/2611.22308v1
- Local PDF: pdf/2026-11-19_27_VRLLM_ Turning LLMs into Powerful Tabular Classifiers.pdf

Large Language Models (LLMs) have shown strong performance on text, but whether pretrained LLMs are effective for large-scale tabular classification remains unclear, as many previous works demonstrate that LLMs' tabular data classification performance falls behind tree-based models or neural architectures designed for tabular data. At Visa Research, we managed to fine-tune a pretrained Llama 3.2 1B LLM on billions of rows of labeled tabular data and make it outperform a wide array of tabular classifiers and even our competitive production deep learning model. For ease of reference, we refer to the model as the Visa Research LLM (VRLLM). In this paper, we share how we achieved this exciting result, covering data preparation, training recipe, ablation studies of design choices and deployment validation. We also benchmark frontier LLMs on the same task and analyze their prediction behavior across model families and generations. Our interpretability experiments suggest that VRLLM learns feature-specific predictive associations, while component ablations indicate that the earliest two FFN layers contribute to the emergence of linearly decodable task information. Our paper provides an engineering recipe and a focused empirical case study on adapting compact LLMs to industrial tabular prediction tasks.

## 28. What Does Weight-Space Programming Add to Diffusion Editing? Program Construction versus Score-Guided Refinement

- Authors: Zitian Gao, Jingyi Xu, Ziqi Han, Chengkai Lei, Ye Liu, Liangliang Shi
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-17
- DOI: Unavailable
- Categories: cs.LG, cs.CV
- Relevance: 2.788694446564657
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.22228v1
- PDF: https://arxiv.org/pdf/2611.22228v1
- Local PDF: pdf/2026-11-19_28_What Does Weight-Space Programming Add to Diffusion Editing_ Program Construction versus Score-Guided Refinement.pdf

Weight-space programming (WSP) lets a language model construct executable weight updates for another network. We study diffusion concept editing through an interface in which programs define training contexts, preservation constraints and update directions, while a shared numerical fitter selects their coefficients. We compare generated programs with published editors, a shared-panel hand-written baseline and budget-matched search over conventional edits on 24 TIMED test edits for Stable Diffusion 1.4. The preregistered rewrite pipeline shows no advantage over the strong baseline. In an exploratory comparison, one-shot Astra programs improve fresh-scene VLM joint success, which requires subject presence together with whole-image target matching, by +10.0 points over the shared-panel baseline, while CLIP relative match shows no detectable change. These programs organise adjustable directions around protected text-state subspaces. Probing and rewriting the Astra programs then raises CLIP by +6.2 points while joint success changes by -9.7. On a fixed 144-image sample, five additional evaluators give point estimates in the same directions under whole-image target matching; checks of subject-local change give less decisive differences. Together, these results identify useful behaviour in complete generated programs and show that score-guided revision need not preserve it: program construction and revision should be evaluated as distinct stages of a WSP pipeline.

## 29. Think Once, Act Fast: Cost-Effective Recursive Self-Improvement for Decision Model Harness

- Authors: Siqi Lai, Haitao Li, Hao Liu
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-17
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 2.7825096713286044
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.22432v2
- PDF: https://arxiv.org/pdf/2611.22432v2
- Local PDF: pdf/2026-11-19_29_Think Once, Act Fast_ Cost-Effective Recursive Self-Improvement for Decision Model Harness.pdf

Fast System-1 models enable responsive actions but struggle with complex or unfamiliar tasks. Large language model (LLM)-based System-2 provides strong reasoning capabilities, yet repeated invocation incurs substantial latency and computational costs. To bridge this gap, we propose JevRSI, a System-1/System-2 collaboration framework that transforms LLM reasoning into transferable decision support through recursive harness improvement. A Jev-style System-1 model enables low-latency action selection, while an asynchronous System-2 LLM develops a modular harness. The harness integrates procedures, state memory, and world models to provide decision contexts spanning the past, present, and future. Utility-driven retrieval selects modules based on both contextual relevance and their utility on previous tasks. Environmental feedback guides targeted revisions and enables recursive self-improvement. Experiments across three datasets show that JevRSI consistently improves decision quality, matching or surpassing LLM agents in several settings. It preserves low-latency execution with favorable performance-cost trade-offs. Moreover, System-2 development interventions decrease as the harness evolves, amortizing System-2 costs through continuous improvement. Our project is available at https://github.com/usail-hkust/JevRSI.

## 30. How Much of SAR Vehicle Recognition Is the Vehicle? Background Shortcuts, Angle Gaps and Partial Libraries on MSTAR and ATRNet-STAR

- Authors: Mousa Shaya
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-16
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 2.7758072548204247
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.21827v1
- PDF: https://arxiv.org/pdf/2611.21827v1
- Local PDF: pdf/2026-11-19_30_How Much of SAR Vehicle Recognition Is the Vehicle_ Background Shortcuts, Angle Gaps and Partial Libraries on MSTAR and.pdf

Deep networks score near 99% on the MSTAR vehicle benchmark, and the newer ATRNet-STAR benchmark was built to be harder. We ask how much of these scores comes from the vehicle itself. With a modern network (ConvNeXt-Small, 3 seeds) we first reproduce the known MSTAR result: with the central 96x96 pixels zeroed out, accuracy is still 73.3% (chance 10%). The same shortcut is present in ATRNet-STAR, which was collected across several scenes: with the vehicle removed, accuracy is 63.3% on the 40-class SOC split (chance 2.5%). Under the official scene-change split, the background stops helping and starts hurting. Accuracy is 22.8% on full chips and 30.8% when only the vehicle is shown. A SAR foundation model, SARATR-X, leans on the background more than ConvNeXt does (+4 to +6 points with the vehicle removed, in every seed) and does not solve the scene change. We then hold the amount of training data fixed and vary the depression angles used for training. Accuracy is set mainly by the gap to the nearest training angle: 57% at 15 degrees, 39% at 30 degrees and 26% at 45 degrees. Adding more training angles does not help. Finally, when most classes have training images at the test angle and a few do not, the missing classes do worse than when no class has them: 9.0% instead of 22.4% at a 45-degree gap. Most of their images are assigned to known classes. We recommend reporting background-only and target-only controls, and the angle gap, next to any accuracy figure. Code is public.
