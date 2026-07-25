# Paper Daily Reading - 2026-07-25

## 1. HierarchicalDAEW: Domain-Aware Edge-Weighted Graph Convolution with Evidential Uncertainty for Multi-Section Spatial Gene Expression Prediction from H&E Histology

- Authors: Kritanu Chattopadhyay, Soumya Chatterjee, Ondrej Krejcar, Debotosh Bhattacharjee
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-23
- DOI: Unavailable
- Categories: cs.LG, q-bio.GN
- Relevance: 3.953942762863223
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.20896v1
- PDF: https://arxiv.org/pdf/2607.20896v1
- Local PDF: pdf/2026-07-25_01_HierarchicalDAEW_ Domain-Aware Edge-Weighted Graph Convolution with Evidential Uncertainty for Multi-Section Spatial Gen.pdf

Spatial transcriptomics assays remain costly and technically demanding, restricting transcriptome-wide profiling to specialist settings and preventing routine clinical deployment. Predicting spatially resolved gene expression from H&E histology could close this gap, yet current methods largely ignore the underlying tissue architecture and rarely quantify how their predictions can be trusted. We introduce HierarchicalDAEW, a dual-graph architecture that addresses both gaps. On the spot graph, a Domain-Aware Edge-Weighted convolutional operator learns separate projections for inter-domain, intra-domain, and boundary edges derived from Leiden clustering, allowing the model to treat tissue heterogeneity as an explicit structural signal rather than an implicit one. A second gene-level graph then fuses protein-protein interaction priors from STRING-DB with tissue-specific co-expression through learned attention gating, propagating predictions from a landmark gene set to a broader gene panel. Reliability is handled through evidential uncertainty estimation, which produces far better calibrated confidence intervals than Monte Carlo dropout under identical conditions. Across six human Visium sections spanning breast, colorectal, prostate, and cerebellar tissue, and against thirteen published baselines, HierarchicalDAEW achieves the strongest correlation with ground-truth expression, with gains that hold up under multi-seed reproducibility checks and negative controls that rule out positional shortcuts. Ablations further confirm that both the domain-aware edge typing and the hierarchical depth are necessary to this improvement, and calibrated uncertainty estimates identify low-confidence predictions for pathologist review before clinical action.

## 2. Semi-Supervised Text-Attributed Graph Distillation

- Authors: Yurui Lai, Samir Moustafa, Renchi Yang, Tsz Nam Chan
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-05-27
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 3.660613031845727
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.20477v1
- PDF: https://arxiv.org/pdf/2607.20477v1
- Local PDF: pdf/2026-07-25_02_Semi-Supervised Text-Attributed Graph Distillation.pdf

{\em Text-Attributed Graphs} (TAGs) have emerged as an expressive data model for integrating graph topology with rich textual semantics. Existing representation learning methods over TAGs suffer from severe scalability bottlenecks, particularly together with {\em Large Language Models} (LLMs). While data distillation offers a promising data-centric solution, existing methods fail to capture the complex interplay between graph and text modalities, struggle with the label scarcity inherent in semi-supervised settings, and lack the ability to produce the human-readable textual attributes required for downstream LLM-based tasks.
  To address these challenges, we propose \algo{}, a unified semi-supervised framework guided by the {\em Wasserstein Distance} (WSD). Grounded in our empirical findings on real TAGs, \algo{} introduces a graph-text collaborative encoding module that utilizes dual-pathway encoders (graph-aware and -free) within a collaborative self-training scheme to harvest reliable pseudo-labels and fuse complementary graph-text features. Furthermore, we develop a theoretically grounded WSD-based graph sketching algorithm and a cost-effective LLM text synthesis module, which leverages cluster-based keyword extraction to generate coherent, human-readable summaries for condensed nodes. Extensive experiments on benchmark datasets demonstrate that \algo{} achieves a state-of-the-art performance-compression trade-off in terms of both GNN- and LLM-based downstream tasks, enabling effective and efficient TAG learning or analytics.

## 3. Beyond SBDD: Geometric Deep Learning in Polypharmacology and Multi-target Drug Design

- Authors: Tianming Han, Zhijie Pan, Wenchi Ge, Qi Zhao
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-14
- DOI: Unavailable
- Categories: cs.LG, cs.AI
- Relevance: 3.5837272905493
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.20550v1
- PDF: https://arxiv.org/pdf/2607.20550v1
- Local PDF: pdf/2026-07-25_03_Beyond SBDD_ Geometric Deep Learning in Polypharmacology and Multi-target Drug Design.pdf

The traditional "one drug, one target" paradigm of structure-based drug design (SBDD) frequently proves inadequate for treating multifactorial diseases such as cancer and neurodegenerative disorders, owing to compensatory signaling pathways and the emergence of drug resistance. While polypharmacology offers a synergistic therapeutic strategy, the rational design of ligands capable of simultaneously satisfying the geometric constraints imposed by multiple targets remains a major computational bottleneck. This review positions geometric deep learning (GDL) as a powerful integrative approach to overcome these limitations. We systematically survey GDL architectures ranging from invariant graph neural networks to SE(3)-equivariant diffusion models that harness non-Euclidean molecular data to capture intrinsic three-dimensional (3D) structural interdependencies. We critically analyze GDL applications across three core dimensions, including the characterization of shared binding pockets via geometric embeddings, multi-target bioactivity prediction through heterogeneous graph fusion, and de novo generation of dual-target ligands. Particular emphasis is placed on emerging structure-conditioned generative algorithms that integrate diffusion models with reinforcement learning to autonomously resolve complex geometric conflicts between competing binding sites. Furthermore, we evaluate the pivotal role of multimodal omics integration and specialized geometric benchmarking infrastructures in validating these models. By synthesizing these methodological advances, this review elucidates the paradigm shift in drug discovery from serendipitous exploration to rational, structure-driven polypharmacological molecular engineering, thereby providing a clear, structured guide for navigating the complexities of next-generation therapeutics.

## 4. Graph Learning on Ensembles of Cyclic Peptides: An Investigation of Molecular Ensemble Modeling

- Authors: Aaron Feller, Kris Deibler, Maxim Secor
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-23
- DOI: Unavailable
- Categories: cs.LG, q-bio.BM
- Relevance: 3.3609764179906367
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.21561v1
- PDF: https://arxiv.org/pdf/2607.21561v1
- Local PDF: pdf/2026-07-25_04_Graph Learning on Ensembles of Cyclic Peptides_ An Investigation of Molecular Ensemble Modeling.pdf

Molecular property prediction from structure often uses a single representative conformation, even though many molecules exist as conformational ensembles in solution. We introduce EnsembleEGNN, a molecular ensemble foundation model that encodes an ensemble by first encoding each conformer with shared Equivariant Graph Neural Network (EGNN) layers, then pooling the resulting conformer representations with a Set Attention Block. We pretrain the model on CREMP, a cyclic peptide ensemble dataset, using a multi-task self-supervised objective combining masked token recovery, noisy-coordinate reconstruction, and pairwise distance reconstruction. On the CREMP-CycPeptMPDB dataset, training EnsembleEGNN from scratch fails entirely ($R^2=0.005$). However, the pretrained model reaches $R^2=0.477$ and Pearson $r=0.699$, outperforming the sequence-only BERT baseline ($R^2=0.439$, Pearson $r=0.667$). When EnsembleEGNN is co-trained end-to-end with the BERT sequence encoder, the hybrid model improves further to $R^2=0.538$ and Pearson $r=0.737$. These results demonstrate that encoding conformational ensembles into a single thermodynamically informed embedding improves cyclic-peptide property prediction.

## 5. Monkey King Bang: A Unified Scientific Multimodal Foundation Model

- Authors: Hesen Chen, Xinyu Su, Xiaomeng Yang, Yuetan Lin, Zixiong Yang, Junyi An, Fenglei Cao, Yifeng Jiao, Yunqi Zhang, Yuan Cheng, Zhiyu Tan, Hao Li, Libo Wu, Yuan Qi
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-17
- DOI: Unavailable
- Categories: cs.LG, cs.AI
- Relevance: 3.246111359297293
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.20557v1
- PDF: https://arxiv.org/pdf/2607.20557v1
- Local PDF: pdf/2026-07-25_05_Monkey King Bang_ A Unified Scientific Multimodal Foundation Model.pdf

Scientific discovery is increasingly shifting from isolated disciplines to multi-domain reasoning, and AI for science faces a similar transition. Existing systems are either specialised for individual domains or unify scientific data mainly through text tokenisation and prompt-based interfaces, limiting their ability to handle diverse scientific inputs, produce modality-native outputs, and support joint understanding, reasoning, and generation across scientific domains. We introduce MKB, a unified scientific multimodal model for both understanding and generation, built around a shared Transformer backbone and modality-tailored encoders, adapters, and decoders. MKB covers six scientific branches, including DNA, RNA, proteins, small molecules, earth science, and medical images, and supports native outputs such as biological sequences, molecular strings, meteorological fields, and segmentation masks. Training follows a two-stage modality-then-language curriculum: Stage 1 aligns modality-specific components with the frozen backbone, and Stage 2 consolidates them with the language backbone using mixed scientific and general corpora. Experiments show that MKB achieves competitive scientific understanding across biological and molecular benchmarks, produces high-fidelity native outputs for weather forecasting, biological generation, and medical-image segmentation, and largely retains the general capabilities of its Qwen3-VL backbone. These results demonstrate the feasibility of the proposed paradigm, suggesting that shared-backbone models with modality-tailored components can provide a promising foundation for future cross-domain scientific multimodal exploration. The model and code are publicly available at https://github.com/Shanghai-Academy-of-AI-For-Science/MKB and https://huggingface.co/sais-org/MKB.

## 6. From Static Bibliometrics to Dynamic Knowledge Graphs: An LLM-Powered Framework for Modernizing Science, Technology, and Innovation (STI) Analytics

- Authors: Muhsen Hammoud
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-23
- DOI: Unavailable
- Categories: cs.DL, cs.AI
- Relevance: 3.147104535949082
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.21327v1
- PDF: https://arxiv.org/pdf/2607.21327v1
- Local PDF: pdf/2026-07-25_06_From Static Bibliometrics to Dynamic Knowledge Graphs_ An LLM-Powered Framework for Modernizing Science, Technology, and.pdf

Bibliometric indicators - citation counts, h-indexes, co-authorship networks - have long anchored science, technology, and innovation (STI) analytics, yet suffer from temporal lag, semantic shallowness, and an inability to capture the non-linear dynamics of contemporary knowledge ecosystems. Dynamic knowledge graphs and large language models (LLMs) have each been proposed as remedies, but neither is sufficient alone: existing scholarly knowledge graphs remain largely static, while LLM-driven pipelines are prone to hallucination, opacity, and corpus bias without structured grounding. This paper proposes a hybrid, symbolic-first framework integrating all three traditions under explicit methodological constraint. Organized across five layers - an open scholarly data backbone, a dynamic versioned knowledge graph, a constrained LLM-assisted semantic augmentation layer, a multi-layer validation pipeline, and an analytics layer - the framework positions LLMs strictly as generators of provisional candidate enrichments. Candidates become analytically admissible only after passing structural, evidentiary, comparative, and selective expert validation, with full provenance recorded at every stage. The analytics layer supports both established bibliometric indicators and extended graph-based analyses, including trend emergence detection, science-to-technology pathway mapping, and policy-oriented gap analysis. The framework's central theoretical contribution is treating validation as the mediating principle between semantic flexibility and epistemic discipline, enabling STI analytics that is semantically richer and temporally more responsive than static bibliometrics while remaining aligned with the evidentiary standards of science-of-science research. Governance considerations addressing reproducibility, bias, and auditability are also discussed.

## 7. The Devil is in the Spectrum: Mitigating Representation Collapse in LLMs via Topologically Regularized Side-Path

- Authors: Yiheng Tao, Kaiwen Cheng, Yao Lu, Chang Liu, Jie Chen
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-06-02
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 3.088546876054151
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.20484v1
- PDF: https://arxiv.org/pdf/2607.20484v1
- Local PDF: pdf/2026-07-25_07_The Devil is in the Spectrum_ Mitigating Representation Collapse in LLMs via Topologically Regularized Side-Path.pdf

Large Language Models (LLMs) are fundamentally limited by representation collapse, a bottleneck that severely degrades long-context performance. We identify that existing approaches risk drifting into one of two pathological extremes: homogenization collapse (e.g., attention sinks causing rank deficiency) and isolation collapse (e.g., local attention causing context disconnection). Through spectral analysis of attention dynamics, we derive an intrinsic trade-off between mixing efficiency (spectral gap) and information capacity (effective rank) that standard mechanisms struggle to balance. To resolve this dilemma, we propose the Topologically Regularized Side-Path (TRSP), a non-invasive architectural intervention that achieves spectral balance. TRSP employs a parameter-free Triangular Box mechanism, scaled by a lightweight, length-aware gate, to regularize the token interaction topology. By integrating proximal coupling to preserve effective rank and distal propagation to support non-degenerate mixing, TRSP promotes a geometrically healthier transition operator without altering core attention. Experiments show significant improvements across general capabilities and long-context benchmarks. Notably, on NoLiMa at $8\times$ the training length, TRSP retains $83\%$ accuracy and surpasses the Differential Transformer and Gated Attention by approximately 30 and 50 percentage points, respectively. Code available at: https://github.com/Eziotao-tyd/TRSP.

## 8. MIRROR: Learning from the Other View for Multi-Modal Reasoning

- Authors: Wen Ye, Yuxiao Qu, Aviral Kumar, Xuezhe Ma
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-23
- DOI: Unavailable
- Categories: cs.AI, cs.LG
- Relevance: 3.051322865494055
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.21552v1
- PDF: https://arxiv.org/pdf/2607.21552v1
- Local PDF: pdf/2026-07-25_08_MIRROR_ Learning from the Other View for Multi-Modal Reasoning.pdf

Unlike large language models (LLMs) that exhibit strong reasoning capabilities, vision-language models (VLMs) struggle with visual reasoning, even on geometry problems that admit equivalent text, diagram, and combined diagram+text views. We show that these views often elicit different behaviors: a model may solve a problem from text but fail on the corresponding diagram, or succeed visually while failing textually. This inconsistency suggests that different views expose complementary reasoning paths and failure modes that standard multimodal post-training does not fully exploit. To study and exploit this phenomenon, we construct ODA-Data, a high-quality paired multimodal geometry dataset with text-dominant, image-dominant, and combined image+text views of the same problems, together with splits for training and evaluating modality-dependent reasoning behaviors. We then develop Modality-Informed Reciprocal Reasoning Optimization (MIRROR), a reinforcement learning approach for improving multimodal reasoning via self supervision. For each problem, MIRROR evaluates the model under all views, selects the best-performing view as a teacher, and trains other views with a reverse-KL objective towards the teacher. Across reasoning benchmarks that evaluate on geometry problems, MIRROR improves over standard RL and yields more accurate and consistent behavior across modalities

## 9. Adaptive Depth Sparse Framework: Similarity-Driven Resource Allocation for Pre-Trained LLMs

- Authors: Yidu Wu, Xiang Wang, Kejie Zhao, Zhangchi Wang, Qinghai Guo, Xiaoying Tang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-23
- DOI: 10.1007/978-981-92-3447-9_43
- Categories: cs.CL, cs.LG
- Relevance: 3.0488775059868396
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.21291v1
- PDF: https://arxiv.org/pdf/2607.21291v1
- Local PDF: pdf/2026-07-25_09_Adaptive Depth Sparse Framework_ Similarity-Driven Resource Allocation for Pre-Trained LLMs.pdf

Large language models (LLMs) achieve strong generation and reasoning performance, but the Transformer architecture incurs high inference cost. Existing acceleration methods often rely on task-specific fine-tuning or training from scratch, increasing adaptation cost and limiting cross-task usability. We present an Adaptive Depth Sparse Framework (AdaDSF) that converts off-the-shelf pre-trained LLMs into depth-sparse models without full retraining. Our key insight is that layers contribute unequally to representation transformation, characterized by the cosine similarity between layer input and output hidden states. Based on this, AdaDSF assigns layer-wise token retention ratios from similarity statistics, uses a lightweight router to select informative tokens at each layer, and introduces a feature-preserving alignment objective to match intermediate and final representations between sparse and dense models. On GPT-NeoX and Qwen2.5 over language modeling and commonsense reasoning, AdaDSF substantially reduces inference FLOPs while preserving performance close to dense counterparts. Under comparable sparsity, AdaDSF consistently yields smaller accuracy degradation than strong baselines including MoD, D-LLM, and DLO.

## 10. Beyond Independent Optimization: Compression, MoE Routing, and Quantization Interactions in Multimodal Edge Intelligence

- Authors: Jay Gor, Karm Dave, Akshita Abrol, Rajesh Gupta, Sudeep Tanwar, Zhengkui Wang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-23
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 3.0151481547542307
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.20981v1
- PDF: https://arxiv.org/pdf/2607.20981v1
- Local PDF: pdf/2026-07-25_10_Beyond Independent Optimization_ Compression, MoE Routing, and Quantization Interactions in Multimodal Edge Intelligence.pdf

Efficient multimodal inference is increasingly constrained not only by model quality or FLOP count, but also by the cost of preserving, moving, routing, caching, and quantizing multimodal representations under latency, memory, and energy constraints. This paper reviews recent advances in efficient vision-language and multimodal large language models, covering visual token compression, video token management, KV-cache optimization, Mixture-of-Experts (MoE) routing, low-bit quantization, edge deployment, and hardware-aware benchmarking. We argue that these techniques cannot be treated as independent optimizations. Visual token compression alters downstream feature distributions and MoE routing decisions, routing behavior affects expert utilization and quantization sensitivity, quantized router logits influence expert assignment, KV-cache policies determine retained multimodal evidence, and hardware constraints often transform computational savings into memory and communication bottlenecks. We organize the literature around these interactions and identify key design trade-offs, including accuracy versus token budget, static versus adaptive compression, sparse routing efficiency versus expert collapse, and low-bit inference versus modality-specific degradation. Finally, we introduce Temporal Routing Consistency as a diagnostic for video MoE models and highlight open research directions in routing-aware compression, cross-modal cache management, hardware-aware co-design, and unified benchmarking for multimodal edge intelligence.

## 11. Are Single-Token Sparse Autoencoder Features Causally Necessary? Layer-Depth and SAE-Family Effects

- Authors: Seonglae Cho, Zekun Wu, Kleyton Da Costa, Rishi Kalra, Ilham Wicaksono, Adriano Koshiyama
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-22
- DOI: Unavailable
- Categories: cs.LG, cs.CL
- Relevance: 3.007468915433039
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.20596v1
- PDF: https://arxiv.org/pdf/2607.20596v1
- Local PDF: pdf/2026-07-25_11_Are Single-Token Sparse Autoencoder Features Causally Necessary_ Layer-Depth and SAE-Family Effects.pdf

Sparse autoencoder (SAE) features are used to interpret and steer large language models, yet whether a feature's causal role is stable across SAE families remains untested. Single-token features that activate on one vocabulary item provide the diagnostic case where ground truth permits direct comparison. We analyze 3.9M features across six models and three SAE families using zero-ablation at full layer depth. Single-token features cluster 4.7x tighter in decoder space and concentrate in early layers (Layer 0 in GPT2-Small; L0-L4 in Gemma). Ablating them yields Benjamini-Hochberg-significant logit reductions in 178 of 208 full-layer conditions, with depth controlling whether damage cascades downstream or shapes the output directly. Cross-family causal differences exceed within-family scale effects: on the same base model, GemmaScope and BatchTopK features remain causally anchored, while LlamaScope features are locally redundant. The target token's rank recovers to within 2x baseline 96-98% of the time after the same ablation, and a controlled activation-function comparison reverses sign within the same model, leaving training recipe as the residual candidate. Cross-family interpretability claims are therefore sensitive to training methodology, not just activation function or scale.

## 12. SiGMA: Sign-Guided Merging and Adaptation for Multimodal Continual Instruction Tuning

- Authors: Keonhee Park, Gunhee Kim
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-05
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 3.0068670876560324
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.20511v1
- PDF: https://arxiv.org/pdf/2607.20511v1
- Local PDF: pdf/2026-07-25_12_SiGMA_ Sign-Guided Merging and Adaptation for Multimodal Continual Instruction Tuning.pdf

Multimodal Continual Instruction Tuning (MCIT) is crucial for adapting Multimodal Large Language Models (MLLMs) to evolving a sequence of downstream tasks. Prior methods mostly utilize Mixture of Experts or expansion merge approach, primarily focusing on catastrophic forgetting, yet they still suffer from negative interference during inference, where newly learned updates overwrite useful prior knowledge and degrade overall performance. To address this, we propose SiGMA (Sign Guided Merging and Adaptation), a simple yet effective framework that mitigates negative interference with two components: sign guided adaptive tuning during training and sign guided merging at inference. Sign guided adaptive tuning reduces collisions with past knowledge and learns the current task with minimal drift, mitigating severe forgetting. Sign guided merging further improves consolidation by selectively scaling salient parameters to preserve and amplify useful task specific knowledge. Experiments on UCIT and DCL benchmarks show that SiGMA significantly reduces negative interference and outperforms state of the art MCIT methods. Our code is available at SiGMA.

## 13. ExecuGraph: A Multi-Agent, Execution-Grounded Framework for Reliable Backend Code Synthesis with Large Language Models

- Authors: Sai Deekshith Lekkala, Jothi Prabha Appadurai, Rohith Reddy Bellibatlu, Manpreet Singh
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-06-18
- DOI: Unavailable
- Categories: cs.AI, cs.SE
- Relevance: 3.0036594942488657
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.20499v1
- PDF: https://arxiv.org/pdf/2607.20499v1
- Local PDF: pdf/2026-07-25_13_ExecuGraph_ A Multi-Agent, Execution-Grounded Framework for Reliable Backend Code Synthesis with Large Language Models.pdf

Large Language Models generate plausible backend code, but a single-pass paradigm provides no guarantee of correctness or runtime reliability. We present ExecuGraph, a multi-agent framework that places execution-based validation at the center of backend code synthesis. Six specialized agents (Planner, Code Generator, Logical Reviewer, Evaluator, Optimizer, and Explainer) are coordinated by a typed directed workflow with a bounded retry budget, implemented on LangGraph with locally hosted models (Ollama) and an optional retrieval layer for algorithmic technique recall. A subprocess-isolated sandbox with a wall-clock timeout guards every evaluation. We evaluate on a curated 30-problem DSA suite (internal-30), HumanEval (n=64), and an APPS-introductory subset, contrasting ExecuGraph against a single-agent one-shot baseline and a single-agent execution-retry baseline (a Reflexion-style ablation that isolates the contribution of multi-agent decomposition). On internal-30, the three conditions are statistically indistinguishable (n=30; paired Wilcoxon p=0.59 MF vs. SO, p=0.08 SR vs. SO); 95% bootstrap confidence intervals on all pairwise mean differences include zero. On HumanEval, multi-full edges ahead by +3.1 pp. The strongest signal is cross-model: with DeepSeekCoder V2 Lite, graph-category accuracy improves from 57.5% (oneshot) to 80.0% (multi-full), a +22.5 pp jump that supports a scaling hypothesis: the value of multi-agent decomposition grows with base-model capability. The framework's primary contribution is methodological: a single codebase that collapses by configuration into one-shot, execution-retry, and per-agent ablation conditions, enabling controlled measurement of each lever's marginal contribution. A per-agent ablation, retry-budget sweep, error-class taxonomy, and test-source audit are reported.

## 14. Agent-Guided Relational Concept Discovery: Toward Interpretable Surgical Margin Assessment

- Authors: Nooshin Maghsoodi, Amoon Jamzad, Robert Policelli, Mohammad Farahmand, Dilakshan Srikanthan, Martin Kaufmann, Kevin Y. M. Ren, Shaila Merchant, Sonal Varma, Ross Walker, Doug McKay, John Rudan, Gabor Fichtinger, Parvin Mousavi
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-23
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 2.97495653670051
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.21437v1
- PDF: https://arxiv.org/pdf/2607.21437v1
- Local PDF: pdf/2026-07-25_14_Agent-Guided Relational Concept Discovery_ Toward Interpretable Surgical Margin Assessment.pdf

Deep learning models can effectively use Rapid Evaporative Ionization Mass Spectrometry (REIMS) data for surgical margin assessment. However, their clinical adoption remains challenging due to limited generalization to operating room conditions. This difficulty arises because models are typically trained on labeled spectra collected from resected tissue samples, while they must operate on noisy, unlabeled data acquired directly during surgery. In addition, the black-box nature of deep learning models makes it difficult to understand and systematically improve their behavior. Concept-based learning offers a promising way to address these challenges by mapping raw measurements to human-understandable concepts. However, supervised concept-based approaches rely on concept annotations, which are difficult to obtain in complex mass spectrometry workflows. We propose Agent-Guided Concept Discovery, a framework that learns meaningful concepts directly from data without requiring predefined concept labels. During training, a reasoning agent refines semantic descriptions of the learned concepts and adaptively adjusts their weight based on diagnostic relevance. These concepts are further grounded using a biochemical knowledge graph to ensure consistency with known metabolic relationships. Across Skin and Breast Cancer datasets, our model improves balanced accuracy and sensitivity over the baseline. In a representative intraoperative case, it shows fewer false positives, indicating better generalization to surgical conditions.

## 15. GRADRAG: Cross-Component Prompt Adaptation for Coordinated Multi-Agent RAG

- Authors: Paolo Pedinotti, Enrico Santus
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-23
- DOI: Unavailable
- Categories: cs.CL, cs.AI
- Relevance: 2.9719535086414606
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.21324v1
- PDF: https://arxiv.org/pdf/2607.21324v1
- Local PDF: pdf/2026-07-25_15_GRADRAG_ Cross-Component Prompt Adaptation for Coordinated Multi-Agent RAG.pdf

Retrieval-Augmented Generation (RAG) systems increasingly employ multiple LLM agents. Yet, most prior work optimizes components in isolation rather than coordinating improvements across the pipeline. We introduce GRADRAG, a framework for cross-component prompt adaptation that models the RAG pipeline as a computational graph and propagates structured evaluation feedback to update upstream agents. An Evaluator critiques downstream answers and supporting evidence, producing actionable feedback that a Prompt Optimizer uses to iteratively update adaptive agents, such as retrievers, graph constructors, and answerers. The Evaluator also triggers early stopping when the output is deemed satisfactory. We evaluate GRADRAG on the SQUALITY and QMSUM benchmarks under two retrieval paradigms: flat chunk-based retrieval using IRCoT-style query refinement (Trivedi et al., 2023), and graph-based retrieval that constructs and iteratively enriches an entity-relation graph from the document. Across both settings, GRADRAG consistently outperforms one-step refinement baselines that update only the final generator, achieving a 12-15 percentage point net preference margin in LLM-judged pairwise comparisons, with most gains realized within two refinement iterations.

## 16. DecodeShare: Tracing the Shared Subspace of LLM Decode-Time Decisions

- Authors: Zishan Shao, Lixun Zhang, Kangning Cui, Yixiao Wang, Ting Jiang, Hancheng Ye, Qinsi Wang, Zhixu Du, Yuzhe Fu, Fan Yang, Danyang Zhuo, Yiran Chen, Hai Helen Li
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-05-21
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 2.957608109389935
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.20469v1
- PDF: https://arxiv.org/pdf/2607.20469v1
- Local PDF: pdf/2026-07-25_16_DecodeShare_ Tracing the Shared Subspace of LLM Decode-Time Decisions.pdf

Large language models (LLMs) handle many tasks with one set of parameters, but under KV-cached inference it is unclear what task-general structure, if any, is used at decode time rather than during prefill. We propose DecodeShare, a protocol that identifies a low-dimensional subspace consistently shared across tasks in decode-time hidden states, and then tests its causal role by removing that subspace only during decoding. In our experiments, disturbing the discovered shared subspace degrades decision performance far more than disturbing either a prefill-derived or random subspace under the same intervention budget. We further show this decode-shared subspace has practical consequences for activation steering: common steering directions can overlap the task-general decode channel. Projecting out this shared subspace directly separates the functional roles of the two components, while evaluating steering vectors at decode-time yields more reliable signal for downstream deployment than prefill-based proxies. Despite its compactness, the shared subspace can serve as a high-leverage causal channel at decode time. Code is available at: https://github.com/Zishan-Shao/decodeshare.git.

## 17. From Atoms to Entropy: Optimal Noise Allocation for Diffusion Training in the Convex Regime

- Authors: Luca Ambrogioni, Giulio Franzese, Alberto Foresti, Gabriel Raya, Bac Nguyen, Georgios Batzolis, Yuhta Takida, Naoki Murata, Chieh-Hsin Lai, Yuki Mitsufuji
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-10
- DOI: Unavailable
- Categories: cs.LG, cs.AI
- Relevance: 2.9553438343654292
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.20540v1
- PDF: https://arxiv.org/pdf/2607.20540v1
- Local PDF: pdf/2026-07-25_17_From Atoms to Entropy_ Optimal Noise Allocation for Diffusion Training in the Convex Regime.pdf

How should a diffusion model decide which noise levels to train on, and how much? Despite the importance of this choice, current noise schedules are based largely on heuristics or empirical tuning. Here, we develop a general statistical framework for studying asymptotically optimal noise-level allocation in diffusion training. Our first main result concerns the fully coupled regime, where information can spread between different time points. Under convexity or Polyak-Lojasiewicz-type assumptions, we show that the optimized training schedule admits an atomic minimizer, concentrated on finitely many noise levels. Our second main result specializes this framework to an idealized independent-learner regime, intended to model temporal specialization in neural networks. Under an additional feature-noise decoupling condition, a random-matrix analysis leads to an information-theoretic proxy: the decoupled sampling density is proportional to the square root of the generative entropy rate, the rate at which conditional entropy grows along the forward process. We test these predictions in controlled settings where the coupled objective can be optimized directly, including Dirac mixtures, low-dimensional manifolds, and MNIST. In these settings, the optimized schedules are consistently finite-support, while the smooth entropic proxy closely tracks the atomic optimum in neural-network models and breaks down mainly in the fully coupled parametric case, as the theory suggests. We then evaluate the entropic schedule in larger-scale experiments, where full schedule optimization is currently intractable. The results indicate that square-root entropy scheduling can substantially improve training efficiency on discrete domains and remains competitive with standard EDM-style heuristics on continuous images.

## 18. Auditing pretraining contamination in single-cell foundation model benchmarks

- Authors: Sarwan Ali
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-21
- DOI: Unavailable
- Categories: q-bio.GN
- Relevance: 2.9543494044744496
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.20572v1
- PDF: https://arxiv.org/pdf/2607.20572v1
- Local PDF: pdf/2026-07-25_18_Auditing pretraining contamination in single-cell foundation model benchmarks.pdf

Single-cell foundation models (scFMs) such as Geneformer, scGPT, and Universal Cell Embeddings (UCE) are pretrained on tens of millions of cells drawn from public repositories. The same repositories underlie widely used integration benchmarks, creating an unmeasured risk that zero-shot benchmark performance reflects pretraining exposure rather than genuine generalization. We introduce \textbf{scContam}, a per-cell audit framework that combines a MinHash-based gene-set fingerprint signal against the explicit pretraining corpus with a loss-based membership inference attack (MIA-scFM). Applied to four scIB benchmarks and three scFMs, we find that two of the most-cited benchmarks, PBMC 3k and the CELLxGENE human pancreatic islet atlas, contain extensive pretraining-overlap evidence ($80.4\%$ and $77.0\%$ of cells with fingerprint $p < 0.05$ against Genecorpus-30M), whereas the post-cutoff datasets AIDA v2 and Tahoe-100M show no overlap evidence ($0\%$). A controlled re-pretraining experiment establishes that MIA-scFM AUROC scales monotonically with the model's capacity-to-data ratio (AUROC $0.494 \to 0.690 \to 0.881$ across properly-regularized, mildly-overfit, and aggressively-overfit regimes), demonstrating that production scFMs resist instance-level memorization but distributional contamination must be detected separately. A donor-matched, within-cell-type analysis with three architectures shows that contaminated cells embed measurably more tightly than donor-matched clean cells (permutation $p = 0.030, 0.014, < 0.002$, respectively), with a perfectly null AIDA negative control. Pretraining audits are tractable and should accompany scFM benchmark reporting.

## 19. Source-Prior-Driven Selective Adaptation for Efficient Diffusion Model Finetuning

- Authors: Yi Xiong, Yuan-Yuan Cheng, Xiao-Ming Fu
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-23
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 2.9409896671145686
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.20913v1
- PDF: https://arxiv.org/pdf/2607.20913v1
- Local PDF: pdf/2026-07-25_19_Source-Prior-Driven Selective Adaptation for Efficient Diffusion Model Finetuning.pdf

Fine-tuning large diffusion models for new domains or styles involves a trade-off: improving target-specific generation often degrades the pretrained model's broad generative capability. Existing full and parameter-efficient fine-tuning methods typically handle this trade-off only implicitly. In this work, we propose a novel source-prior-driven selective adaptation method to efficiently fine-tune diffusion models, achieving a favorable trade-off. Our method relies on two key observations: (1) the loss of general generative capability is highly inconsistent across pretrained parameters, and (2) parameters that have a relatively small impact on the model's general generative capability remain structurally inconsistent across layers and parameter types. Motivated by these observations, we first learn a static mask to explicitly identify parameters better suited for downstream adaptation, and then construct structured update strategies for the selected subset. Experiments show that our method achieves a better adaptation-retention trade-off than existing strong baselines.

## 20. Bridging the Gap Between Plausibility and Admissibility: Constraint-Aware Flow Maps for Dynamic Graph Systems

- Authors: Michael Romei de Socio, Gian Luca Pozzato, Alessio Merlo
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-23
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 2.9361779067824347
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.21421v1
- PDF: https://arxiv.org/pdf/2607.21421v1
- Local PDF: pdf/2026-07-25_20_Bridging the Gap Between Plausibility and Admissibility_ Constraint-Aware Flow Maps for Dynamic Graph Systems.pdf

Generative models can support decision-making under uncertainty by producing ensembles of plausible future system trajectories, but statistical plausibility does not ensure structural feasibility. This study investigates whether post-sampling symbolic constraints can improve the reliability of generative trajectory modeling in dynamic graph-structured systems. A conditional diffusion model generates future graph-state trajectories from partial observations, while an external symbolic layer applies hard filtering, soft weighting, or projection-based repair. The framework is evaluated on two controlled synthetic regimes: a compact graph and a medium-complexity dependency graph, using metrics for structural validity, sample efficiency, diversity, robustness, and calibration. In the compact regime, the model produces an invalid probability mass of 0.002996, indicating an almost entirely admissible trajectory manifold. Under the same architecture and training protocol, invalid mass increases to 0.155929 in the medium-complexity regime. Hard filtering removes all invalid retained trajectories while preserving 84.4% of generated samples, whereas soft weighting preserves effective sample size but yields only limited validity gains. Family-level analysis shows that dependency constraints account for nearly all observed inadmissibility. These results indicate that statistical plausibility and structural admissibility are distinct reliability properties and that symbolic constraint handling becomes more valuable as graph-structural complexity increases.

## 21. MSBraM: A Multi-scale Self-supervised Brain Foundation Model for Hierarchical EEG Dynamics Learning

- Authors: Tao Zhou, Jing Han, Lingyu Shu, Zixing Zhang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-23
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 2.9323731568105735
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.21402v1
- PDF: https://arxiv.org/pdf/2607.21402v1
- Local PDF: pdf/2026-07-25_21_MSBraM_ A Multi-scale Self-supervised Brain Foundation Model for Hierarchical EEG Dynamics Learning.pdf

Self-supervised foundation models have recently shown strong potential for electroencephalogram (EEG)-based analysis. However, existing approaches struggle to capture the inherently multi-scale temporal structure of EEG signals, where local neural patterns and long-range dependencies jointly encode task-relevant information. This limitation hampers cross-scale representation learning and generalization across diverse downstream tasks. To address this challenge, we propose MSBraM, a Multi-Scale self-supervised Brain foundation Model designed to learn hierarchical EEG representations. MSBraM follows a two-stage pretraining framework. First, a multi-scale neural tokenizer discretizes raw EEG signals into semantic codes at different temporal resolutions via vector-quantized reconstruction. Second, the model is pretrained to predict masked codes using a curriculum multi-scale masking strategy, progressively integrating fine-grained local patterns with global temporal context. We pretrain MSBraM on over 2,400 hours of EEG data and evaluate it across 10 downstream tasks on 12 public datasets. Extensive experiments show that MSBraM achieves superior performance on other state-of-the-art pretrained models, demonstrating strong generalization and transferability. These results indicate that explicitly modeling multi-scale temporal dynamics is critical for effective EEG foundation models.

## 22. FlowEdit: Information-Theoretic Control of LLM Reasoning Flows for Ill-posed Problems Involving Conflicts

- Authors: Sizhe Tang, Guangyu Jiang, Yu Li, Rongqian Chen, Ioannis G. Kevrekidis, Tian Lan
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-06-20
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 2.8891534791352336
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.20500v1
- PDF: https://arxiv.org/pdf/2607.20500v1
- Local PDF: pdf/2026-07-25_22_FlowEdit_ Information-Theoretic Control of LLM Reasoning Flows for Ill-posed Problems Involving Conflicts.pdf

Large Language Models (LLMs) perform strongly on well-specified reasoning tasks with a feasible answer. However, problems encountered in the open world can become ill-posed due to inconsistent conditions, conflicting statements, or mutually incompatible requirements, admitting no valid responses. We argue that reasoning of such ill-posed problems involving conflicts require novel LLM capabilities to make hidden conflicts explicit, maintain competing hypotheses via multiple reasoning branches, and generate alternative responses in a single pass, all of which are challenging due to the limitation of the next-token prediction mechanism in LLMs. To this end, we propose FlowEdit, a novel framework that leverages information-theoretic principles to quantify and regulate internal reasoning flows of LLMs, for generating a full set of alternative responses under valid hypotheses. FlowEdit can be viewed as enforcing a branch-aware reasoning process using two dual information-theoretic objectives on the model's internal reasoning representations: maximizing the information flow from each selected hypothesis to the branch outcome, while minimizing the overlap and conditional dependence across sibling branches, to provide a diverse, informative set of responses with broad coverage. We show that this is achieved through tractable variational bounds under boundary embeddings being ε-sufficient, optimizing the underlying conditional mutual information in LLM reasoning process. Extensive experiments demonstrate that FlowEdit outperforms leading proprietary models, improving exact-set-match accuracy by 68%, while boosting overall response informativeness by 24%. We further show that flow regulation surfaces in the token stream as a redistribution of next-token entropy that concentrates inside each branch, amplifies at flow boundaries, and scales with the number of flows the problem requires.

## 23. AISE-Bench: A Full-Cycle Curated Benchmark for Information Seeking on Academic Knowledge Graphs

- Authors: Fanjin Zhang, Zhengyang Wang, Ruixuan Huang, Kefan Zhang, Amy Xin, Yuanchun Wang, Shu Zhao, Evgeny Kharlamov, Jie Tang, Juanzi Li
- Source: arxiv
- Venue type: preprint
- Journal: Proceedings of the 32nd ACM SIGKDD Conference on Knowledge Discovery and Data Mining (KDD '26), August 09-13, 2026, Jeju Island, Republic of Korea
- Publication status: preprint
- Publication date: 2026-06-16
- DOI: 10.1145/3770855.3817492
- Categories: cs.AI
- Relevance: 2.876383785077997
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.20498v1
- PDF: https://arxiv.org/pdf/2607.20498v1
- Local PDF: pdf/2026-07-25_23_AISE-Bench_ A Full-Cycle Curated Benchmark for Information Seeking on Academic Knowledge Graphs.pdf

Large language models (LLMs) augmented with tools are emerging as autonomous agents capable of using Web engine, APIs, and code to solve complex, long-horizon tasks. Current tool-using benchmarks for information seeking on academic graphs rely on synthetic templates, simplified solution spaces, or narrow tasks such as paper-centric tasks, leaving key challenges underexplored - realistic user intent, complex multi-step API planning, rich parameter filling for APIs, grounded answers with references, and comprehensive evaluation of both the process and the outcome. We introduce AISE-Bench, a real-world, full-cycle annotated benchmark for information seeking on academic knowledge graphs. AISE-Bench release contains 1,133 QA pairs, including query taxonomies, full API execution trajectories, validated parameters, and source-grounded answers with reference links. To support high-quality annotation, we design a customized agent workflow to enable annotators to plan, execute, and revise complex API workflows efficiently. We develop a comprehensive evaluation protocol measuring answer quality, reference grounding, API-planning correctness, and execution success. Among the 14 evaluated methods, even the strongest model (PLAY2PROMPT with Gemini-3-Pro) achieves only moderate performance and often struggles with API planning and execution. AISE-Bench establishes a challenging new testbed for quantitatively evaluating and improving the stepwise correctness, grounded summarization, and traceable reasoning of multi-step API-using LLM agents. Our code and data are available at https://aise-bench.github.io/.

## 24. Context-weighted Discrete Flow Matching

- Authors: Daniil Cherniavskii, Daniel Severo, Karen Ullrich
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-23
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 2.863924053027127
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.21427v1
- PDF: https://arxiv.org/pdf/2607.21427v1
- Local PDF: pdf/2026-07-25_24_Context-weighted Discrete Flow Matching.pdf

Discrete flow matching provides a flexible framework for generative modeling on discrete structures. However, the standard factorized training objective exposes the model to targets of varying difficulty, mixing well-conditioned, predictable tokens with ambiguous, high-entropy ones. We empirically demonstrate that the uncertainty over the value of each token is closely related to the density of available context in its neighborhood. Motivated by this observation, we propose a simple modification to the underlying continuous-time Markov chain (CTMC) that incorporates local context information. Our context-weighted sampler improves generation quality with negligible computational overhead, while our scaled cross-entropy loss function reweights the training signal from different tokens and reduces generative perplexity by up to 63% on OpenWebText. Moreover, our approach matches a strong semi-autoregressive block diffusion baseline in quality while retaining the ability to perform generation in any order. These results highlight the role of local context as an important factor in discrete generative modeling and show that simple context-aware modifications can significantly improve both sampling and training efficiency.

## 25. PlanE: Meta Planning of Data, Tuning, and Inference for Extractive-based LLMs

- Authors: Jiacheng Wang, Weiyan Zhang, Guangya Yu
- Source: arxiv
- Venue type: preprint
- Journal: ACL
- Publication status: preprint
- Publication date: 2026-05-22
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 2.859777806288851
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.20470v1
- PDF: https://arxiv.org/pdf/2607.20470v1
- Local PDF: pdf/2026-07-25_25_PlanE_ Meta Planning of Data, Tuning, and Inference for Extractive-based LLMs.pdf

Enhancing the task-specific capabilities of Large Language Models (LLMs) primarily requires substantial instruction-tuning datasets. However, the sheer volume of such data imposes a considerable annotation cost, and a lack of optimization methods for tailoring LLMs to specific tasks. To address the above issues, we propose a \textbf{Plan}ning framework for constructing \textbf{E}xtractive-based LLMs called \textbf{PlanE}, which includes data decomposition, instruction tuning, and prompt inference. Additionally, we introduce a Data-Tuning-Inference (DTI) planner, aimed at selecting the optimal base-LLM and its DTI combinations for specific datasets to improve construction efficiency. The experimental results demonstrate the effectiveness of our PlanE from two views: (1) across different datasets using the same base-LLM, and (2) on the same dataset using different base-LLMs. Furthermore, we validate the generalizability of the proposed DTI planner under different optimization objectives. The codes are publicly available at https://github.com/gugugu-469/PlanE.

## 26. Vocab Diet: Reshaping the Vocabulary of LLMs via Vector Arithmetic

- Authors: Yuval Reif, Guy Kaplan, Roy Schwartz
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.85957831396746
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1618/
- PDF: https://aclanthology.org/2026.findings-acl.1618.pdf
- Local PDF: pdf/2026-07-25_26_Vocab Diet_ Reshaping the Vocabulary of LLMs via Vector Arithmetic.pdf

Large language models (LLMs) often encode word-form variation (e.g., *walk* vs. *walk**ed***) as linear directions in the embedding space. However, standard tokenization algorithms treat such variants as distinct words with different vocabulary entries—quickly filling the size-capped token vocabulary with surface-form variation (e.g., *walk*, *walk**ing***, ***W**alk*), at the expense of diversity and multilingual coverage. We show that many of these variations can be captured by *transformation* vectors—additive offsets that yield the appropriate word representation when applied to a *base form* embedding, in both the input and output spaces. Building on this, we propose a compact reshaping of the vocabulary: instead of assigning unique tokens to each surface form, we compose them from shared *base form* and *transformation* vectors (e.g., *walked* is *walk*+*past tense*). Our approach is lightweight—keeping the pretrained backbone frozen and only training small adaptation modules. We apply it across five languages and multiple LLMs in both pretraining and post-hoc adaptation, freeing 10-40% of vocabulary slots to be reallocated where tokenization is inefficient. Importantly, we do so while also expanding vocabulary coverage to out-of-vocabulary words, and with minimal impact on downstream performance. Our findings motivate a rethinking of vocabulary design, towards a representation that better matches the underlying structure of language and the practical needs of multilingual coverage.

## 27. TENP: Trapezoidal Expert Neuron Pruning For Mixture-of-Experts

- Authors: Jiangyang He, Shaolin Zhu, Deyi Xiong
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.8588487556871667
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1049/
- PDF: https://aclanthology.org/2026.findings-acl.1049.pdf
- Local PDF: pdf/2026-07-25_27_TENP_ Trapezoidal Expert Neuron Pruning For Mixture-of-Experts.pdf

Mixture-of-Experts large language models (LLMs) scale efficiently through sparse activation, yet their deployment is fundamentally constrained by the large static parameter footprint of experts. Existing compression approaches either remove entire experts, disrupting routing topology and harming performance, or rely on unstructured weight pruning with limited practical efficiency. To address the limitations, we propose TENP, a structured **T**rapezoidal **E**xpert **N**euron **P**runing framework. Using a few samples, we identify and retain important experts, while applying expert neuron pruning (ENP) to less important experts, preserving model parameters in a trapezoidal pattern from shallow to deep layers. When evaluating expert importance, we jointly consider both the magnitude of the expert output and its ability to change the direction of the input vector. For ENP, we measure each neuron’s projected contribution to the expert output to identify and retain important neurons. We conduct extensive experiments on the Qwen and DeepSeek models. Under a routing expert sparsity of 40% and an average of 63.76% activated expert parameters, the DeepSeek model suffers only a 1-point drop in accuracy compared to the full-parameter model. Moreover, it outperforms the full-parameter model by 10% on code generation tasks.

## 28. WebSynthesis: World Model-Guided Monte Carlo Tree Search for Efficient WebAgent Trajectory Synthesis

- Authors: Yifei Gao, Junhong Ye, Yifan Yang, Jiaqi Wang, Yi Zhang, Zhang Ruichen, Jitao Sang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.8562261580037362
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1157/
- PDF: https://aclanthology.org/2026.acl-long.1157.pdf
- Local PDF: pdf/2026-07-25_28_WebSynthesis_ World Model-Guided Monte Carlo Tree Search for Efficient WebAgent Trajectory Synthesis.pdf

Recent advances in large language models (LLMs) have enabled increasingly capable web agents, yet training such agents still relies on high-quality interaction trajectories that are difficult to obtain at scale. We identify two key challenges: (1) Infrastructure Overhead, where network instability and website access restrictions limit data collection scalability; and (2) Constrained Exploration, where irreversible state transitions preclude tree-based search and thus limit trajectory diversity. To address these challenges, we introduce WebSynthesis, a framework for scalable trajectory synthesis. WebSynthesis employs an LLM-based World Model to simulate state transitions without network dependencies, and integrates Monte Carlo Tree Search to enable reversible exploration over the simulated state space. Experiments on WebArena, WebVoyager, and Mind2Web-Online demonstrate that agents trained exclusively on synthesized trajectories outperform those trained on real-world data, providing a viable alternative to costly real-world data collection.

## 29. SERE: Structural Example Retrieval for Enhancing LLMs in Event Causality Identification

- Authors: Zhifeng Hao, Zhongjie Chen, Junhao Lu, Shengyin Yu, Guimin Hu, Keli Zhang, Ruichu Cai, Boyan Xu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.856073270481297
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.2126/
- PDF: https://aclanthology.org/2026.findings-acl.2126.pdf
- Local PDF: pdf/2026-07-25_29_SERE_ Structural Example Retrieval for Enhancing LLMs in Event Causality Identification.pdf

Event Causality Identification (ECI) requires models to determine whether a given pair of events in a context exhibits a causal relationship. While Large Language Models (LLMs) have demonstrated strong performance across various NLP tasks, their effectiveness in ECI remains limited due to biases in causal reasoning, often leading to overprediction of causal relationships (causal hallucination). To mitigate these issues and enhance LLM performance in ECI, we propose SERE , a structural example retrieval framework that leverages LLMs’ few-shot learning capabilities. SERE introduces an innovative retrieval mechanism based on three structural concepts: (i) Conceptual Path Metric , which measures the conceptual relationship between events using edit distance in ConceptNet; (ii) Syntactic Metric , which quantifies structural similarity through tree edit distance on syntactic trees; and (iii) Causal Pattern Filtering , which filters examples based on predefined causal structures using LLMs. By integrating these structural retrieval strategies, SERE selects more relevant examples to guide LLMs in causal reasoning, mitigating bias and improving accuracy in ECI tasks. Extensive experiments on multiple ECI datasets validate the effectiveness of SERE .

## 30. Reinforcement Learning for Diffusion LLMs via Energy-Based Gibbs Alignment

- Authors: Yijia Fan, Jing Yang, Mingyu Liu, Kaitong Cai, Jian Wang, Keze Wang, Jusheng Zhang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.8557815577875454
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.2131/
- PDF: https://aclanthology.org/2026.acl-long.2131.pdf
- Local PDF: pdf/2026-07-25_30_Reinforcement Learning for Diffusion LLMs via Energy-Based Gibbs Alignment.pdf

Diffusion Large Language Models (dLLMs) have emerged as a promising non-autoregressive paradigm for text generation, offering parallel decoding and bidirectional context modeling. However, aligning dLLMs with reinforcement learning (RL) remains a significant challenge, as the marginal likelihood of sequences in masked diffusion is typically intractable, rendering standard policy gradient methods unstable or computationally prohibitive. In this work, we propose **Diffusion-Gibbs Alignment (DGA)**, a novel variational framework that reformulates RL for dLLMs as a distribution matching problem. DGA bypasses the explicit computation of log-probabilities by leveraging a learned energy function to model the relative quality of samples. The optimization is decoupled into two stable steps: (1) contrastive energy ranking to capture global reward structures, and (2) weighted diffusion alignment to update the policy via importance sampling. Empirically, DGA establishes a new state-of-the-art across logical reasoning (Sudoku, Countdown), mathematical reasoning (GSM8K, Math500), and code generation (HumanEval, MBPP) benchmarks. DGA offers a novel variational perspective for dLLM alignment, achieving better performance while simultaneously enhancing training speed and memory efficiency.
