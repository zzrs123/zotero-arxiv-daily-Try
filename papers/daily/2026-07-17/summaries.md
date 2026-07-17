# Paper Daily Reading - 2026-07-17

## 1. CoDiffGRN: Rethinking Gene Regulatory Network Inference via the BEELINE-KGC Benchmark and Co-evolutionary Discrete Diffusion

- Authors: Jiaze Song, Runhao Zhao, Minghao Xu, Bin Cui, Wentao Zhang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-14
- DOI: Unavailable
- Categories: cs.LG, cs.AI
- Relevance: 3.887912484355059
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.13120v1
- PDF: https://arxiv.org/pdf/2607.13120v1
- Local PDF: pdf/2026-07-17_01_CoDiffGRN_ Rethinking Gene Regulatory Network Inference via the BEELINE-KGC Benchmark and Co-evolutionary Discrete Diffu.pdf

Inferring gene regulatory networks (GRNs) from single-cell transcriptomic data is crucial for biological discovery, yet existing approaches suffer from a fundamental misalignment with real-world needs. Researchers typically seek a small set of high-confidence regulatory interactions for experimental validation, often involving previously unseen genes. However, current benchmarks rely on transductive splits with global classification metrics, while prevailing models struggle to generalize under inductive settings. To bridge this gap, we reformulate GRN inference as an inductive, ranking-centric graph completion problem and introduce \textbf{\benchmark}, a new benchmark that incorporates an inductive gene-holdout split together with knowledge graph completion metrics to better evaluate top-ranked predictions. Building on this, we propose \textbf{\method}, the first co-evolutionary discrete diffusion framework that jointly models biologically coherent discretized gene expression states and regulatory interactions for robust inductive generalization and improved top-ranked regulatory discovery. We further introduce TF-ALL Subgraph Sampling (TASS) for scalable training. Extensive experiments on {\benchmark} show that {\method} establishes new state-of-the-art performance, significantly outperforming existing methods in novel regulatory discovery, and ablation studies further verify the effectiveness of our design.

## 2. SHINE: Decoding transcriptional-metabolic microenvironments through higher-order spatial integration

- Authors: Du, B., Wong, J. W. H., Huang, Y.
- Source: biorxiv
- Venue type: preprint
- Journal: biorxiv
- Publication status: preprint
- Publication date: 2026-07-16
- DOI: 10.64898/2026.07.10.737648
- Categories: bioinformatics
- Relevance: 3.7527981473649454
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://www.biorxiv.org/content/10.64898/2026.07.10.737648v1.full.pdf
- PDF: https://www.biorxiv.org/content/10.64898/2026.07.10.737648v1.full.pdf
- Local PDF: pdf/2026-07-17_02_SHINE_ Decoding transcriptional-metabolic microenvironments through higher-order spatial integration.pdf

Spatial omics technologies are expanding to co-profile transcriptomics and metabolomics on the same tissue slide, providing complementary views of gene expression and biochemical activity to reveal molecular programs within native tissue microenvironments. However, integrating the transcriptome and metabolome remains technically challenging due to spatial misalignment, resolution disparity, and higher-order cross-modality interactions. Here, we present SHINE, a hypergraph-based computational framework for the joint analysis of spatial gene expression and metabolic networks derived from the co-profiling slide, focusing on representation learning and cross-modality interaction. Across multiple datasets, SHINE consistently outperformed existing methods for domain segmentation and biomarker co-localization and provided interpretable insights into metabolic-transcriptional microenvironments. Specifically, in Parkinson's disease mouse models, SHINE accurately delineates dopaminergic neuron-depleted regions and reconstructs coherent dopamine-associated axes. In human lung and breast cancers, SHINE resolves tumor-associated spatial regions and identifies spatially organized gene-metabolite programs associated with the tumor microenvironment. SHINE enables scalable spatial multi-omics integration across diverse biological systems.

## 3. CDS: Counterfactual Directionality Score for Structured Interventions in Spatial Graphs

- Authors: Humaira Anzum, Md Ishtyaq Mahmud, Jagan Mohan Reddy Dwarampudi, Tania Banerjee
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-15
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.4474800785726583
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.13508v1
- PDF: https://arxiv.org/pdf/2607.13508v1
- Local PDF: pdf/2026-07-17_03_CDS_ Counterfactual Directionality Score for Structured Interventions in Spatial Graphs.pdf

Quantifying directional influence between node populations is a fundamental problem in graph-based modeling, particularly in spatial biological systems where cell-cell interactions shape functional outcomes. Existing approaches based on attention, attribution, or correlation capture associations but do not provide a principled framework for evaluating directional effects under controlled perturbations. We introduce a framework for structured counterfactual interventions in graph-based models to estimate directional influence between node types. Our approach trains a Neighbor Influence Model (NIM) to predict node states from local neighborhoods and applies constrained interventions that modify neighborhood composition while preserving key spatial and structural properties. We define the Counterfactual Directionality Score (CDS), which measures the change in predicted node state induced by targeted perturbations, and provide a theoretical interpretation of CDS as a finite-difference measure of local intervention sensitivity. To obtain valid uncertainty estimates, we introduce a core-level bootstrap procedure that accounts for dependencies within spatial samples. Experiments on synthetic spatial graphs with known directional structure show that CDS recovers directional influence, remains well calibrated under null conditions, and is robust to confounding signals, while preliminary results on spatial transcriptomics data reveal biologically plausible and consistent interactions across tissue cores.

## 4. MxGPS: Multiplex Graph Transformers for a Power Grid Foundation Model

- Authors: Charilaos Papaioannou, Ioannis Tsantilas, Dimitris Giannakakos, Vasilis Michalakopoulos, Sotiris Pelekis, Vangelis Marinakis, Arsam Aryandoust, Antonello Monti, Ricardo J. Bessa, Perdo P. Vergara, Jochen Cremer, Elissaios Sarmas
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-15
- DOI: Unavailable
- Categories: cs.LG, cs.AI
- Relevance: 3.3503809434805176
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.13763v1
- PDF: https://arxiv.org/pdf/2607.13763v1
- Local PDF: pdf/2026-07-17_04_MxGPS_ Multiplex Graph Transformers for a Power Grid Foundation Model.pdf

Single-task fine-tuning of graph neural networks (GNNs) for power grid problems exhibits a systematic failure mode: models that achieve the lowest in-distribution error degrade the most under topology shift. We term this topology overfitting: the tendency of task-specific gradient signals to encode relational structure particular to the training topologies rather than the underlying physics, causing models to fail on unseen grids despite strong in-distribution performance. To expose and address this failure mode, we introduce MxGPS (Multiplex GPS), a multiplex graph transformer that runs K task-specialised GPS branches over a shared node encoder, jointly trained on Static State Estimation (SSE) and AC Power Flow (PF) via a self-supervised pre-training and multi-task fine-tuning protocol, with a cross-branch attention module evaluated in ablation. The joint SSE+PF objective forces the shared encoder to simultaneously satisfy complementary gradient signals, preventing it from overfitting to topology-specific relational structure. Under a 3-fold sliding-window cross-validation spanning four unseen topologies (14-, 24-, 162-, and 300-bus), MxGPS attains 0% boundary violation rate (BVR) on all four zero-shot Power Flow topologies. Critically, models with substantially lower in-distribution PF error degrade by 190% to 1400% under topology shift, whereas MxGPS degrades by only 39%, an inversion that directly implicates topology overfitting as the failure mechanism rather than insufficient model capacity. With only 1.6M parameters (12x fewer than the GridFM reference baseline), MxGPS demonstrates that multi-task joint training is a principled and parameter-efficient mechanism for topology-agnostic generalisation in power grid foundation models.

## 5. GeoAnchor: Collaborative Reasoning via Latent Decomposition for 3D Spatial Understanding

- Authors: Hao Li, Han Fang, Zixin Pan, Xin Wei, Hongbo Sun, Jinglin Xu, Zhiyu Lin, Ye Yuan, Zhongjiang He, Yu Yu, Hao Sun
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-15
- DOI: Unavailable
- Categories: cs.CV, cs.AI
- Relevance: 3.2963042487608982
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.13454v1
- PDF: https://arxiv.org/pdf/2607.13454v1
- Local PDF: pdf/2026-07-17_05_GeoAnchor_ Collaborative Reasoning via Latent Decomposition for 3D Spatial Understanding.pdf

Although multimodal large language models (MLLMs) have achieved remarkable progress, understanding 3D spatial relationships from 2D images remains a critical challenge. Existing methods primarily rely on symbolic text tokens, which inherently lack the fidelity to represent continuous geometric information. While recent methods use latent representations to enhance reasoning, relying on a single latent type cannot adapt to the diversity of spatial tasks, leading to misalignment in complex geometric scenarios. To address these limitations, we propose GeoAnchor, an interleaved text-latent reasoning framework. GeoAnchor decomposes 3D spatial information into three complementary components: position latents for object grounding, direction latents for relational orientation, and geometry latents for scene structure. These components are recombined in a structured space to construct local evidence while capturing global context, enabling dynamic and interpretable reasoning. Furthermore, we introduce a collaborative training strategy that guides the model from local spatial perception to comprehensive 3D understanding. Extensive experiments on diverse and complex 3D reasoning tasks demonstrate that GeoAnchor outperforms the state of the art, validating its effectiveness and generalization capabilities.

## 6. Reference Regulatory Element-Guided Gene Expression Analysis for Mechanistic Inference of Gene Regulatory Networks

- Authors: Ren, L., Debnath, I., Duren, Z.
- Source: biorxiv
- Venue type: preprint
- Journal: biorxiv
- Publication status: preprint
- Publication date: 2026-07-16
- DOI: 10.64898/2026.07.10.737848
- Categories: bioinformatics
- Relevance: 3.2494828115306174
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://www.biorxiv.org/content/10.64898/2026.07.10.737848v1.full.pdf
- PDF: https://www.biorxiv.org/content/10.64898/2026.07.10.737848v1.full.pdf
- Local PDF: pdf/2026-07-17_06_Reference Regulatory Element-Guided Gene Expression Analysis for Mechanistic Inference of Gene Regulatory Networks.pdf

Regulatory genomics faces a depth-breadth gap: deep multi-omics provides regulatory detail but is difficult to scale, whereas broad expression datasets often lack the regulatory structure needed for mechanistic Gene Regulatory Network (GRN) analysis. We developed Regulatory Elements Guided Analysis (REGA), an interpretable framework that uses reference Regulatory Element (RE) catalogs to infer transcription factor (TF)-RE-gene programs from gene expression data. Across ChIP-seq, knockdown, Hi-C, cis- and trans-eQTL benchmarks, REGA prioritized functional REs, improved RE-gene and TF-gene inference over existing baselines, including methods using more data, and recovered coherent regulatory modules. In PsychENCODE snRNA-seq, REGA identified disease-associated modules and TF activities, linked regulatory dysregulation to genetic risk, and detected cross-cell-type neuronal-glial programs. In spatial transcriptomics, REGA linked cell-intrinsic regulatory programs with intercellular ligand-receptor communication; in Perturb-seq, it mapped perturbation responses to trait-associated regulatory architectures. REGA enables scalable, interpretable GRN analysis across expression datasets.

## 7. Context-aware sequence-to-function model of human gene regulation

- Authors: Ekin Deniz Aksu, Martin Vingron
- Source: openalex
- Venue type: journal
- Journal: Nature Communications
- Publication status: published
- Publication date: 2026-07-14
- DOI: https://doi.org/10.1038/s41467-026-75527-2
- Categories: Genetics, Bioinformatics, and Biomedical Research, Gene Regulatory Network Analysis, Gene expression and cancer classification
- Relevance: 3.130173129280205
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://doi.org/10.1038/s41467-026-75527-2
- PDF: Unavailable
- Local PDF: Not downloaded

Abstract Sequence-to-function models have been very successful in predicting gene expression, chromatin accessibility, and epigenetic marks from DNA sequences alone. However, current state-of-the-art models have a fundamental limitation: they cannot extrapolate beyond the cell types and conditions included in their training dataset. Here, we introduce a new approach that is designed to overcome this limitation: Corgi, a new context-aware sequence-to-function model that accurately predicts genome-wide gene expression and epigenetic signals, even in previously unseen cell types. We designed an architecture that strives to emulate the cell: Corgi integrates DNA sequence and trans -regulator expression to predict the coverage of multiple assays including chromatin accessibility, histone modifications, and gene expression. We define trans- regulators as transcription factors, histone modifiers, transcriptional coactivators, and RNA binding proteins, which directly modulate chromatin states, gene expression, and mRNA decay. Trained on a diverse set of bulk and single cell human datasets, Corgi has robust predictive performance, approaching experimental-level accuracy in gene expression predictions in previously unseen cell types, while also setting a new state-of-the-art level for joint cross-sequence and cross-cell type epigenetic track prediction. Corgi can be used in practice to impute context-specific assays such as DNA accessibility and histone ChIP-seq, using only RNA-seq data.

## 8. Leveraging unlabelled data for generalizable neural population decoding

- Authors: Ximeng Mao, Nanda H. Krishna, Avery Hee-Woon Ryoo, Matthew G. Perich, Guillaume Lajoie
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-15
- DOI: Unavailable
- Categories: cs.LG, q-bio.NC
- Relevance: 3.020538037754008
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.14086v1
- PDF: https://arxiv.org/pdf/2607.14086v1
- Local PDF: pdf/2026-07-17_08_Leveraging unlabelled data for generalizable neural population decoding.pdf

Robust and accurate neural decoders are integral to neurotechnologies such as brain-computer interfaces and closed-loop experiments. Recent work has shown that tokenizing neural data at the spike level facilitates multi-session pretraining and delivers state-of-the-art decoding performance. However, current spike-based models are restricted to supervised learning (SL), limiting training to datasets with paired behavioural labels. To address this limitation, we introduce MOJO (Masked autOencoder-based JOint training), a training framework for spike-tokenizing models that jointly leverages self-supervised learning (SSL) via masked autoencoding and SL objectives. We evaluate MOJO on three spiking datasets spanning monkey motor cortex during reaching tasks and multi-regional mouse recordings during vision and decision making tasks, demonstrating superior performance over purely SL-trained models. This improvement is especially pronounced when training with limited labelled data, particularly in few-shot finetuning, where only a small amount of labelled data from a new session is available. Incorporating SSL also yields more interpretable neuronal representations, improving performance on brain region classification and spike-statistics prediction without explicit optimization for these tasks. We further show that MOJO generalizes beyond spiking data to human electrocorticography during speech, where it continues to outperform purely SL-trained models and achieves performance comparable to neuro-foundation models (NFMs) designed specifically for continuous signals. Overall, augmenting spike-tokenizing models with SSL improves performance in label-impoverished settings and enables the use of unlabelled data across various tasks and species, while generalizing to other neural modalities. These results suggest a path towards more flexible and scalable data usage when training NFMs.

## 9. Causal Discovery of Radiation Response Mechanisms in Human Cells

- Authors: Ashka Shah, Rick Stevens
- Source: arxiv
- Venue type: preprint
- Journal: Proceedings of Machine Learning Research [VOLUME # 340] 2026
- Publication status: preprint
- Publication date: 2026-07-15
- DOI: Unavailable
- Categories: q-bio.GN
- Relevance: 3.0065530620935803
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.13994v1
- PDF: https://arxiv.org/pdf/2607.13994v1
- Local PDF: pdf/2026-07-17_09_Causal Discovery of Radiation Response Mechanisms in Human Cells.pdf

Next-generation sequencing technologies, including RNA-sequencing, provide genome-wide measurements of gene expression and enable broad explorations of biomarkers and mechanisms underlying disease and treatment response. Bioinformatics tools for processing this data, such as differential expression analysis, are largely univariate, linear, and rely on predefined pathway knowledge annotations, which limits their ability to capture nonlinear and multivariate gene interactions. This paper explores the application of causal discovery to characterizing transcriptional responses to radiation as a function of dose rate in human cells. By jointly modeling radiation perturbations and gene expression, we learn directed gene networks that capture important regulatory relationships beyond correlation and exhibit significant enrichment of known radiation response pathways compared to baseline approaches. We find that inferred causal graphs reveal structured network features such as high in-degree housekeeping genes and high out-degree transcription factors. Further analysis suggests a hierarchical organization of stress response pathways and triggered cell death pathways. This work highlights the potential of causal discovery in healthcare settings with applications to understanding response mechanisms, identifying regulatory targets, and improving interpretation of complex genomic data.

## 10. Concurrent Image Understanding and Generation: Self-Correcting Coupled Markov Jump Processes

- Authors: Minh-Quan Le, Armand Comas, Alexandros Lattas, Stylianos Moschoglou, Pedro Vélez, Amit Raj, Aaron Germuth, Thabo Beeler, Dimitris Samaras, Di Qiu
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-14
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 2.998645491143479
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.13188v1
- PDF: https://arxiv.org/pdf/2607.13188v1
- Local PDF: pdf/2026-07-17_10_Concurrent Image Understanding and Generation_ Self-Correcting Coupled Markov Jump Processes.pdf

Human cognition does not separate understanding and generation. A teacher at a whiteboard speaks and draws $\textit{together}$, each modality reshapes the other. In this paper, we bring this coupled loop to artificial systems. Masked Diffusion Models (MDMs) are ideally suited to this task, yet existing samplers either decode text and image interleavedly or independently update them in parallel branches that share only previous-step history, but not the other modality's latest decisions $\textit{within}$ the same step; combined with MDMs' inability to remask, cross-modal contradictions are neither detected nor repaired. We introduce $\textbf{Self-Correcting Coupled Markov Jump Processes (SC-CMJP)}$, a framework in which one modality's transition rates are functionals of the other modality's confidence score, as weighted by cross-modal attention. Furthermore, a remasking jump retracts commitments the moment cross-modal evidence turns against them. In conjunction with SC-CMJP, we introduce $\texttt{CO}_\texttt{2}\texttt{Jump}$ (Self-$\underline{\text{CO}}$rrecting $\underline{\text{CO}}$upled $\underline{\text{Jump}}$), a novel training-free single-pass sampler for joint multimodal geneneration. For training and evaluation purposes, we have created and will release three large-scale joint multimodal generation corpora: $\text{JEdit-1M}$, $\text{JMaze-200K}$, $\text{JNono-200K}$, with matching in- and out-of-distribution benchmarks. $\texttt{CO}_\texttt{2}\texttt{Jump}$ achieves best joint performance for image understanding and editing as well as visual reasoning (maze and nonogram solving). The performance of the sampler scales monotonically with the number of denoising steps, evidence that the benefits of cross-modal coupling $\textit{compound}$ across the trajectory. Project page: https://coupled-jump.github.io

## 11. Consensus as Privileged Context for Label-Free Self-Distillation

- Authors: John Gkountouras, Josip Jukić, Ivan Titov
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-15
- DOI: Unavailable
- Categories: cs.LG, cs.AI, cs.CL
- Relevance: 2.977264001385475
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.13643v1
- PDF: https://arxiv.org/pdf/2607.13643v1
- Local PDF: pdf/2026-07-17_11_Consensus as Privileged Context for Label-Free Self-Distillation.pdf

Sampling multiple solutions and returning the majority answer is among the most reliable ways to improve the reasoning accuracy of large language models without labels, and a growing family of methods converts this consensus signal into training supervision. However, existing approaches use consensus only in restricted forms: as a filter that selects solutions for fine-tuning, as a preference between answers, or as a scalar reward for reinforcement learning, discarding most of the information that the agreeing solutions contain. We present CANON (Consensus-ANchored self-distillatiON), a label-free training method that turns consensus into dense, token-level supervision. For each unlabeled prompt, CANON samples multiple solutions, extracts the majority answer, and conditions a frozen snapshot of the model on a solution that reaches it; this consensus-anchored teacher then supervises the model on its own rollouts at every token. Experiments on mathematical and scientific reasoning benchmarks show that CANON improves pass@1 by up to 12 points, outperforming label-free reinforcement learning by 6 points at a seventh of its compute and approaching a teacher conditioned on gold solutions; trained on pooled unlabeled data, it transfers to held-out benchmarks, matching training methods that use gold labels. Analysis suggests that the improvements are not pure distribution sharpening: after training, the model solves problems it previously never solved in 32 attempts, and its majority vote itself becomes more accurate.

## 12. Biological Continued Pretraining Reshapes the Capability Profile of a Foundation Model Without Catastrophic Forgetting

- Authors: Wang, L.
- Source: biorxiv
- Venue type: preprint
- Journal: biorxiv
- Publication status: preprint
- Publication date: 2026-07-16
- DOI: 10.64898/2026.07.06.736700
- Categories: bioinformatics
- Relevance: 2.9439324629232075
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://www.biorxiv.org/content/10.64898/2026.07.06.736700v1.full.pdf
- PDF: https://www.biorxiv.org/content/10.64898/2026.07.06.736700v1.full.pdf
- Local PDF: pdf/2026-07-17_12_Biological Continued Pretraining Reshapes the Capability Profile of a Foundation Model Without Catastrophic Forgetting.pdf

It is widely assumed that continued pretraining (CPT) on a narrow, out-of-distribution corpus such as raw biological sequence must trade away a general-purpose model's broad competence --- the "alignment tax" or catastrophic-forgetting intuition. We test this directly, without any new training, by re-analyzing three checkpoints from a single lineage of a 26B-parameter Mixture-of-Experts model (Gemma-4-26B-A4B): the instruction-tuned base, the same model after biological CPT (8.7B tokens of DNA, protein, and biomedical text), and after subsequent supervised fine-tuning (SFT). Across three independent capability axes --- general knowledge/reasoning (MMLU, ARC, HellaSwag), code generation (MBPP), and biomedical knowledge (BixBench) --- we find that biological CPT does not degrade the model; it lifts it: MMLU +13 points, MBPP pass@1 nearly doubles (0.33 to 0.63), and BixBench discrimination rises sharply (MCC 0.23 to 0.92). The single measured regression is truthfulness (TruthfulQA -8.8 points), a small and interpretable domain drift. A clean vocabulary-expansion ablation (<0.4 pt on every general metric) confirms the gains are attributable to CPT, not tokenizer changes. Crucially, subsequent SFT narrows the model back: all three axes fall to near-base levels, revealing a consistent division of labor --- CPT re-organizes and lifts the shared capability substrate; SFT cashes it out onto target tasks. We argue this reframes biological sequence not as a competitor for a foundation model's capacity but as a form of structured scientific data that reshapes its capability profile, and that CPT and SFT should be budgeted as complementary rather than substitutable stages. All checkpoints, evaluation code, and per-example outputs are public.

## 13. Self-Improving is Often Sudden: Enlightenment-style Finetuning for Large-Scale Models

- Authors: Jing-Xiao Liao, Tianwei Zhang, Yu-Hao Jiang, Feifei Zhang, Hang-Cheng Dong, Feng-Lei Fan
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-15
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 2.9319867411795784
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.13395v1
- PDF: https://arxiv.org/pdf/2607.13395v1
- Local PDF: pdf/2026-07-17_13_Self-Improving is Often Sudden_ Enlightenment-style Finetuning for Large-Scale Models.pdf

The pursuit of autonomously self-improving models has attracted growing interest in the era of large-scale foundation models. Drawing inspiration from the concept of "enlightenment" or "aha moment" in human brain, we hypothesize that large models exhibit an analogous enlightenment phenomenon-a latent capacity for sudden capability boost. Then, we propose Enlightenment, a novel training-free post-tuning paradigm for large-scale models. Our approach modifies shortcuts for key modules/layers without weight updates, while existing training-free ones predominantly manipulate attention weights. We introduce two architecture-specific instantiations: i) For large language models, we propose attention head-mixing shortcuts that recalibrate attention weights by linking the initial attention head's output to all other target heads, modulated by an adaptive scaling factor initialization strategy. ii) For vision-language models, we apply a lightweight scalar-modulated factor to residual connections in the decoder layers, regulating information flow. Extensive experiments show that Enlightenment efficiently unlocks the latent potential of pre-trained networks, yielding remarkable performance improvements across diverse benchmarks and models.

## 14. LOKA: Conflict-Aware LLM Knowledge Update with Adaptive Knowledge Memory

- Authors: Binchi Zhang, Zhengzhang Chen, Zaiyi Zheng, Jundong Li, Haifeng Chen
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.892430825117775
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.760/
- PDF: https://aclanthology.org/2026.acl-long.760.pdf
- Local PDF: pdf/2026-07-17_14_LOKA_ Conflict-Aware LLM Knowledge Update with Adaptive Knowledge Memory.pdf

Large Language Models (LLMs) have achieved remarkable success in natural language processing by encoding extensive knowledge, but their utility relies on timely updates as human knowledge keeps evolving. In this paper, we investigate the problem of LLM knowledge updates, which requires simultaneously unlearning unwanted information and learning new knowledge. Existing approaches that tackle unlearning and learning separately encounter *task conflicts* and *knowledge management issues* when applied to comprehensive knowledge updates.In this paper, we validate our findings with theoretical analysis and empirical evidence, and propose LOKA, a conflict-aware framework for Large language mOdel Knowledge updAtes. During training, LOKA introduces an adaptive knowledge memory approach in which updated knowledge is allocated across multiple memory units. During inference, LOKA retrieves the most relevant memory unit from the knowledge memory and integrates it with the original LLM to apply updated knowledge, while a learning-based router controls the activation of the knowledge memory to improve knowledge utilization. Extensive experiments demonstrate the efficacy of LOKA in achieving accurate, flexible, and conflict-aware knowledge updates.

## 15. Routing with Generated Data: Annotation-Free LLM Skill Estimation and Expert Selection

- Authors: Tianyi Niu, Justin Chen, Genta Indra Winata, Shi-Xiong Zhang, Supriyo Chakraborty, Sambit Sahu, Yue Zhang, Elias Stengel-Eskin, Mohit Bansal
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.888564032692443
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1498/
- PDF: https://aclanthology.org/2026.acl-long.1498.pdf
- Local PDF: pdf/2026-07-17_15_Routing with Generated Data_ Annotation-Free LLM Skill Estimation and Expert Selection.pdf

Large Language Model (LLM) routers dynamically select optimal models for given inputs. Existing approaches typically assume access to ground-truth labeled data, which is often unavailable in practice, especially when user request distributions are heterogeneous and unknown. We introduce Routing with Generated Data (RGD), a challenging setting in which routers are trained exclusively on generated queries and answers produced from high-level task descriptions by generator LLMs. We evaluate query-answer routers (using both queries and labels) and query-only routers across four diverse benchmarks and 12 models, finding that query-answer routers degrade faster than query-only routers as generator quality decreases. Our analysis reveals two crucial characteristics of effective generators: they must accurately respond to their own questions, and their questions must produce sufficient performance differentiation among the model pool. We then show how filtering for these characteristics can improve the quality of generated data. We further propose CASCAL, a novel query-only router that estimates model correctness through consensus voting and identifies model-specific skill niches via hierarchical clustering. CASCAL is substantially more robust to generator quality, outperforming the best query-answer router by 4.6% absolute accuracy when trained on weak generator data.

## 16. From Isolated Scoring to Collaborative Ranking: A Comparison-Native Framework for LLM-Based Paper Evaluation

- Authors: Pujun Zheng, Jiacheng Yao, Jinquan Zheng, Chenyang Gu, Guoxiu He, Jiawei Liu, Yong Huang, Tianrui Guo, Wei Lu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.8879881629492887
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1195/
- PDF: https://aclanthology.org/2026.findings-acl.1195.pdf
- Local PDF: pdf/2026-07-17_16_From Isolated Scoring to Collaborative Ranking_ A Comparison-Native Framework for LLM-Based Paper Evaluation.pdf

Large language models (LLMs) are currently applied to scientific paper evaluation by assigning an absolute score to each paper independently. However, since score scales vary across conferences, time periods, and evaluation criteria, models trained on absolute scores are prone to fitting narrow, context-specific rules rather than developing robust scholarly judgment. To overcome this limitation, we propose shifting paper evaluation from isolated scoring to collaborative ranking. In particular, we design a C omparison- N ative framework for P aper E valuation ( CNPE ), integrating comparison into both data construction and model learning. We first propose a graph-based similarity ranking algorithm to facilitate the sampling of more informative and discriminative paper pairs from a collection. We then enhance relative quality judgment through supervised fine-tuning and reinforcement learning with comparison-based rewards. At inference, the model performs pairwise comparisons over sampled paper pairs and aggregates these preference signals into a global relative quality ranking. Experimental results demonstrate that our framework achieves an average relative improvement of 21.8 % over the strong baseline DeepReview-14B, while exhibiting robust generalization to five previously unseen datasets. Our code is available at https://github.com/ECNU-Text-Computing/ComparisonReview.

## 17. UR 2 : Unify RAG and Reasoning through Reinforcement Learning

- Authors: Weitao Li, Boran Xiang, Xiaolong Wang, Jingyi Ren, Ante Wang, Zhinan Gou, Weizhi Ma, Yang Liu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.887531257729865
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.580/
- PDF: https://aclanthology.org/2026.acl-long.580.pdf
- Local PDF: pdf/2026-07-17_17_UR 2 _ Unify RAG and Reasoning through Reinforcement Learning.pdf

Large Language Models (LLMs) have shown strong capabilities through two complementary paradigms: Retrieval-Augmented Generation (RAG) for knowledge grounding and Reinforcement Learning from Verifiable Rewards (RLVR) for complex reasoning. However, existing attempts to unify these paradigms remain narrow in scope, typically limited to open-domain QA with fixed retrieval settings, which constrains generalization to broader domains. To address this limitation, we propose **UR 2 ** (**U**nified **R**AG and **R**easoning), a general reinforcement learning framework that dynamically coordinates retrieval and reasoning. UR 2 introduces two key designs: a difficulty-aware curriculum that selectively invokes retrieval only for challenging instances, and a hybrid knowledge access strategy that combines domain-specific offline corpora with on-the-fly LLM-generated summaries. Together, these components mitigate the imbalance between retrieval and reasoning and improve robustness to noisy information. Experiments on open-domain QA, MMLU-Pro, medical, and mathematical reasoning tasks show that UR 2 , built on Qwen-2.5-3/7B and LLaMA-3.1-8B, consistently outperforms existing RAG and RL baselines, and achieves performance comparable to GPT-4o-mini and GPT-4.1-mini on several benchmarks. We will release all code, models, and data.

## 18. SciFlow-Bench: Evaluating Structure-Aware Scientific Diagram Generation via Inverse Parsing

- Authors: Tong Zhang, Honglin Lin, Zhou Liu, Chong Chen, Wentao Zhang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.886207455595398
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.807/
- PDF: https://aclanthology.org/2026.acl-long.807.pdf
- Local PDF: pdf/2026-07-17_18_SciFlow-Bench_ Evaluating Structure-Aware Scientific Diagram Generation via Inverse Parsing.pdf

Scientific diagrams convey explicit structural information, yet modern text-to-image models often produce visually plausible but structurally incorrect results. Existing benchmarks either rely on image-centric or subjective metrics insensitive to structure, or evaluate intermediate symbolic representations rather than final rendered images, leaving pixel-based diagram generation underexplored. We introduce SciFlow-Bench, a structure-first benchmark for evaluating scientific diagram generation directly from pixel-level outputs. Built from real scientific PDFs, SciFlow-Bench pairs each source framework figure with a canonical ground-truth graph and evaluates models as black-box image generators under a closed-loop, round-trip protocol that inverse-parses generated diagram images back into structured graphs for comparison. This design enforces evaluation by structural recoverability rather than visual similarity alone, and is enabled by a hierarchical multi-agent system that coordinates planning, perception, and structural reasoning. Experiments show that preserving structural correctness remains a fundamental challenge, particularly for diagrams with complex topology, underscoring the need for structure-aware evaluation.

## 19. DeepSynth-Eval: Objectively Evaluating Information Consolidation in Deep Survey Writing

- Authors: Hongzhi Zhang, Yuanze Hu, Tinghai Zhang, Jia Fu, Tao Wang, Junwei Jing, Zhaoxin Fan, Wei Bi, Ruiming Tang, Han Li, Guorui Zhou, Kun Gai
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.884593781162134
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1688/
- PDF: https://aclanthology.org/2026.findings-acl.1688.pdf
- Local PDF: pdf/2026-07-17_19_DeepSynth-Eval_ Objectively Evaluating Information Consolidation in Deep Survey Writing.pdf

The evolution of Large Language Models (LLMs) towards autonomous agents has catalyzed progress in Deep Research. While retrieval capabilities are well-benchmarked, the post-retrieval synthesis stage—where agents must digest massive amounts of context and consolidate fragmented evidence into coherent, long-form reports—remains under-evaluated due to the subjectivity of open-ended writing.To bridge this gap, we introduce DeepSynth-Eval, a benchmark designed to objectively evaluate information consolidation capabilities. We leverage high-quality survey papers as gold standards, reverse-engineer research requests, and construct Oracle Contexts from their bibliographies to isolate synthesis from retrieval noise. We propose a fine-grained evaluation protocol using General Checklists (for factual coverage) and Constraint Checklists (for structural organization), transforming subjective judgment into verifiable metrics. Experiments across 96 tasks reveal that synthesizing information from hundreds of references remains a significant challenge. Our results demonstrate that agentic "plan-then-write" workflows significantly outperform single-turn generation, effectively reducing hallucinations and improving adherence to complex structural constraints.

## 20. SCAN: Structured Capability Assessment and Navigation for LLMs

- Authors: Zongqi Wang, Tianle Gu, Chen Gong, Xin Tian, Siqi Bao, Yujiu Yang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.884440802863163
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.126/
- PDF: https://aclanthology.org/2026.acl-long.126.pdf
- Local PDF: pdf/2026-07-17_20_SCAN_ Structured Capability Assessment and Navigation for LLMs.pdf

Evaluating Large Language Models (LLMs) has become increasingly important, with automatic evaluation benchmarks gaining prominence as alternatives to human evaluation. While existing research has focused on approximating model rankings, such benchmarks fail to provide users and developers with a comprehensive and fine-grained understanding of a specific model’s capabilities. To fill this gap, we propose SCAN (Structured Capability Assessment and Navigation), a practical framework that enables detailed characterization of LLM capabilities through comprehensive and fine-grained evaluation. SCAN incorporates four key components: (1) TaxBuilder, which extracts capability-indicating tags from extensive queries to construct a hierarchical taxonomy automatically; (2) RealMix, a query synthesis and filtering mechanism that ensures sufficient evaluation data for each capability tag; (3) a suite of visualization and analysis tools that facilitate efficient navigation and analysis of model capabilities; and (4) a PC 2 -based (Pre-Comparison-derived Criteria) LLM-as-a-Judge approach that achieves significantly higher accuracy compared to classic LLM-as-a-Judge method. Using SCAN, we conduct a comprehensive evaluation of 21 mainstream LLMs. Our detailed analysis of the GPT-OSS family reveals substantial performance variations, even within sub-capabilities belonging to the same category of capability. This finding highlights the importance of fine-grained evaluation in accurately understanding LLM behavior. Project homepage and resources are available at https://github.com/liudan193/SCAN.

## 21. Domain-Specific Data Generation Framework for RAG Adaptation

- Authors: Chris Xing Tian, Weihao Xie, Zhen Chen, Hui Liu, Zhengyuan Yi, Haoliang Li, Shiqi Wang, Siwei Ma
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.8839048651679744
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.960/
- PDF: https://aclanthology.org/2026.findings-acl.960.pdf
- Local PDF: pdf/2026-07-17_21_Domain-Specific Data Generation Framework for RAG Adaptation.pdf

Retrieval-Augmented Generation (RAG) combines the language understanding and reasoning capabilities of large language models (LLMs) with external retrieval to produce domain-grounded responses. Effectively adapting RAG systems to domain-specific settings requires specialized, context-rich training data beyond general-purpose question-answering datasets. Here, we propose RAGen, a scalable and modular data-centric framework for generating domain-grounded question–answer–context (QAC) triples tailored to diverse RAG adaptation strategies. These QAC triples serve as training signals for multiple RAG adaptation approaches; in this work, we demonstrate their use for contrastive fine-tuning of embedding models and supervised fine-tuning of LLMs under retrieved contexts. RAGen generates QAC triples by identifying key concepts within documents, producing diverse questions guided by Bloom’s Taxonomy–inspired principles, and pairing them with precise answers extracted from relevant contexts. Its modular pipeline incorporates semantic chunking, hierarchical concept extraction, multi-chunk retrieval, and curated distractor contexts to encourage robust reasoning. Designed for scalability, RAGen efficiently handles large and evolving document corpora without redundant processing, making it particularly suitable for dynamic domains like enterprise knowledge bases.

## 22. Beyond Memorization: Extending Reasoning Depth with Recurrence, Memory and Test-Time Compute Scaling

- Authors: Ivan Rodkin, Daniil Orel, Konstantin Smirnov, Arman Bolatov, Bilal Elbouardi, Besher Hassan, Yuri Kuratov, Aydar Bulatov, Preslav Nakov, Timothy Baldwin, Artem Shelmanov, Mikhail Burtsev
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.88382950137649
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.2103/
- PDF: https://aclanthology.org/2026.findings-acl.2103.pdf
- Local PDF: pdf/2026-07-17_22_Beyond Memorization_ Extending Reasoning Depth with Recurrence, Memory and Test-Time Compute Scaling.pdf

Reasoning is a core capability of large language models (LLMs), yet how multi-step reasoning is learned and executed remains unclear. We study this question in a controlled cellular-automata (1dCA) framework that excludes memorization by using disjoint training and test rules. Given a short state sequence, the model is required to infer the hidden local rule and then chain it to predict multiple future steps. Our evaluation shows that LLMs largely fail to reliably solve a natural-language proxy of the proposed task. We find that most neural architectures trained from scratch can learn rule inference and achieve high next-step accuracy, but performance drops sharply as the required number of intermediate reasoning steps increases. Experiments show that increasing model depth is crucial, and extending effective depth via recurrence, memory, or test-time compute improves results but remains bounded. Code is available on github: https://github.com/RodkinIvan/associative-recurrent-memory-transformer/tree/ACT.

## 23. Detecting Hallucinations in Large Language Models via Internal Attention Divergence Signals

- Authors: Gijs van Dijk
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.8837480390364956
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-srw.6/
- PDF: https://aclanthology.org/2026.acl-srw.6.pdf
- Local PDF: pdf/2026-07-17_23_Detecting Hallucinations in Large Language Models via Internal Attention Divergence Signals.pdf

We propose a lightweight and single-pass uncertainty quantification method for detecting hallucinations in Large Language Models. The method uses attention matrices to estimate uncertainty without requiring repeated sampling or external models. Specifically, we measure the Kullback–Leibler divergence between each attention head’s distribution and a uniform reference distribution, and use these features in a logistic regression probe. Across multiple datasets, task types, and model families, attention divergence is strongly predictive of answer correctness and performs competitively with existing uncertainty estimation methods. We find that this signal is concentrated in middle layers and on factual tokens such as named entities and numbers, suggesting that attention dynamics provides an efficient and interpretable white-box signal of model uncertainty.

## 24. BiCSRouter: Bi-Level Cross-System Routing for Utility-Aware LLM Inference

- Authors: Mao Keyu, Eiki Murata, Ukyo Honda
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.883645316304635
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.947/
- PDF: https://aclanthology.org/2026.findings-acl.947.pdf
- Local PDF: pdf/2026-07-17_24_BiCSRouter_ Bi-Level Cross-System Routing for Utility-Aware LLM Inference.pdf

Selecting an appropriate LLM configuration for a given query is critical, yet existing routing frameworks operate within a single computational paradigm. To address this gap, we formalize the Cross-System Routing Problem, a hierarchical decision-making task that decomposes routing into intra-regime configuration selection and inter-regime system selection. Building on this, we propose BiCSRouter, a bi-level cross-system routing framework that integrates two orthogonal regimes: intensive reasoning via single-agent systems and extensive collaboration via multi-agent systems. BiCSRouter performs policy learning within each system and employs a lightweight inter-regime router that selects the optimal regime based on predicted performance and cost. Experiments on the MBPP and MATH benchmarks demonstrate that BiCSRouter outperforms 15 representative baselines across three types. On MBPP, compared to the performance ceiling of GPT-5, BiCSRouter achieves a 46% reduction in cost with only a 2% drop in accuracy. Finally, we show that BiCSRouter can extend to additional regimes, highlighting its generality as a cross-system routing framework.

## 25. A Shared Geometry of Difficulty in Multilingual Language Models

- Authors: Stefano Civelli, Pietro Bernardelle, Nicolò Brunello, Gianluca Demartini
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.8833646980170053
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-short.66/
- PDF: https://aclanthology.org/2026.acl-short.66.pdf
- Local PDF: pdf/2026-07-17_25_A Shared Geometry of Difficulty in Multilingual Language Models.pdf

Large language models (LLMs) encode problem difficulty as an internal signal that can be linearly decoded from their residuals. Given their multilingual capabilities, we investigate whether this meta-cognitive signal is language-agnostic and how it is organized across the model’s layers by training linear probes on the AMC subset of the Easy2Hard benchmark, translated into 21 languages. We found that difficulty-related signals emerge at two distinct stages of the model internals, corresponding to shallow (early-layers) and deep (later-layers) internal representations, that exhibit functionally different behaviors. Probes trained on deep representations achieve high accuracy when evaluated on the same language but exhibit weaker cross-lingual transfer. In contrast, probes trained on shallow representations generalize better across languages, despite achieving lower within-language performance. This closely aligns with existing findings in LLM interpretability, showing that models tend to operate in an abstract conceptual space before producing language-specific outputs. Our results suggest that this two-stage organizational principle extends beyond simple semantic processing to meta-cognitive properties such as problem difficulty, highlighting an internal control signal that is not tied to surface meaning.

## 26. DiZiNER: Disagreement-guided Instruction Refinement via Simulating Pilot Annotation for Zero-shot Named Entity Recognition

- Authors: Siun Kim, Hyung-Jin Yoon
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.8832302338747215
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.795/
- PDF: https://aclanthology.org/2026.acl-long.795.pdf
- Local PDF: pdf/2026-07-17_26_DiZiNER_ Disagreement-guided Instruction Refinement via Simulating Pilot Annotation for Zero-shot Named Entity Recogniti.pdf

Large language models (LLMs) have advanced information extraction (IE) by enabling zero-shot and few-shot named entity recognition (NER), yet their generative outputs still show persistent and systematic errors. Despite progress through instruction fine-tuning, zero-shot NER still lags far behind supervised systems. These recurring errors mirror inconsistencies observed in early-stage human annotation processes that resolve disagreements through pilot annotation. Motivated by this analogy, we introduce DiZiNER (Disagreement-guided Instruction Refinement via Pilot Annotation Simulation for Zero-shot Named Entity Recognition), a framework that simulates the pilot annotation process, employing LLMs to act as both annotators and supervisors. Multiple heterogeneous LLMs annotate shared texts, and a supervisor model analyzes inter-model disagreements to refine task instructions. Across 18 benchmarks, DiZiNER achieves zero-shot SOTA results on 14 datasets, improving prior bests by +8.0 F1 and reducing the zero-shot to supervised gap by over +11 points. It also consistently outperforms its supervisor, GPT-5 mini, indicating that improvements stem from disagreement-guided instruction refinement rather than model capacity. Pairwise agreement between models shows a strong correlation with NER performance, further supporting this finding.

## 27. Fisher-Driven Adaptive Locating for Knowledge Editing in Large Language Models

- Authors: Chenghao Xu, Jiexi Yan, Guangtao Lyu, Qi Liu, Muli Yang, Cheng Deng
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.8827715656896267
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.957/
- PDF: https://aclanthology.org/2026.acl-long.957.pdf
- Local PDF: pdf/2026-07-17_27_Fisher-Driven Adaptive Locating for Knowledge Editing in Large Language Models.pdf

Large language models (LLMs) store extensive factual knowledge acquired during pretraining, yet this knowledge is inherently static and may become inaccurate or outdated, leading to knowledge hallucinations. Knowledge editing offers an efficient alternative to full retraining by enabling targeted factual updates while preserving overall model behavior. Existing locate-then-edit methods, however, rely on fixed layer selection strategies, treating the locating stage as a static design choice and failing to account for the hierarchical and instance-dependent nature of knowledge representation in LLMs. In this paper, we propose FiDAL, a Fisher-driven adaptation-aware locating strategy that dynamically identifies which model components should be edited for a given knowledge update. FiDAL formulates localization as a weight-level decision problem and leverages Fisher Information to select layers that are both influential and sensitive to factual modifications. A lightweight probing stage with low-rank modulation enables efficient localization with minimal overhead. Experiments on standard benchmarks demonstrate that FiDAL consistently improves editing effectiveness and knowledge preservation across multiple editing methods.

## 28. VizoMem: A Visual-Textual Memory Framework for Efficient Long-Horizon Reasoning

- Authors: Weijie Liang, Yuanfeng Song, Xing Chen, Caleb Chen Cao, Sirui Han, Yike Guo
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.8827628748278897
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.365/
- PDF: https://aclanthology.org/2026.findings-acl.365.pdf
- Local PDF: pdf/2026-07-17_28_VizoMem_ A Visual-Textual Memory Framework for Efficient Long-Horizon Reasoning.pdf

Agentic systems built upon large language models (LLMs) increasingly depend on long-context modeling to support document understanding, long-term memory recall, and multi-step reasoning. However, extending context windows incurs substantial computational and memory overhead, significantly limiting the scalability and practicality of long-context LLM-based agents. Recent studies suggest that visual representations can serve as an effective medium for compressing and organizing long textual content. Motivated by this insight, we propose VizoMem, a novel visual memory framework for agentic systems. In this framework, textual memories are pre-rendered into structured images and stored as visual notes, enabling compact and persistent memory representations. Moving beyond standard vision-language models like Glyph, we pioneer a specialized retrieval system designed for large-scale visual memory. Our innovation lies in the construction of a dedicated dataset and the development of a highly efficient retrieval model that repurposes foundational vision-language encoders to navigate complex, text-heavy visual environments. Experiments on public datasets demonstrate that our approach significantly reduces token consumption while preserving effective long-term memory recall, highlighting its potential as a scalable alternative to conventional long-context modeling.

## 29. Disco-RAG: Discourse-Aware Retrieval-Augmented Generation

- Authors: Dongqi Liu, Hang Ding, Qiming Feng, Xurong Xie, Zhucun Xue, Chengjie Wang, Jian Li, Jiangning Zhang, Yabiao Wang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.882356741580403
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.189/
- PDF: https://aclanthology.org/2026.acl-long.189.pdf
- Local PDF: pdf/2026-07-17_29_Disco-RAG_ Discourse-Aware Retrieval-Augmented Generation.pdf

Retrieval-Augmented Generation (RAG) has emerged as an important means of enhancing the performance of large language models (LLMs) in knowledge-intensive tasks. However, most existing RAG strategies treat retrieved passages in a flat and unstructured way, which prevents the model from capturing structural cues and constrains its ability to synthesize knowledge from dispersed evidence across documents. To overcome these limitations, we propose Disco-RAG, a discourse-aware framework that explicitly injects discourse signals into the generation process. Our method constructs intra-chunk discourse trees to capture local hierarchies and builds inter-chunk rhetorical graphs to model cross-passage coherence. These structures are jointly integrated into a planning blueprint that conditions the generation. Experiments on question answering and long-document summarization benchmarks show the efficacy of our approach. Disco-RAG achieves state-of-the-art results on the benchmarks without fine-tuning. These findings underscore the important role of discourse structure in advancing RAG systems.

## 30. Leveraging Label Semantics and Entity Description Generation for LLM-based Fine-grained Entity Typing

- Authors: Yingying Ma, Hongliang Dai, Xia Zhang, Piji Li
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.882135514143504
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1584/
- PDF: https://aclanthology.org/2026.findings-acl.1584.pdf
- Local PDF: pdf/2026-07-17_30_Leveraging Label Semantics and Entity Description Generation for LLM-based Fine-grained Entity Typing.pdf

Fine-grained entity typing (FET) aims to assign semantically rich and contextually appropriate types to entity mentions. While recent studies have explored the use of large language models (LLMs) for this task, two key challenges persist. First, FET typically involves a large number of entity types, making it difficult for LLMs to perform accurate classification. Second, the presence of label noise in the training data introduced by automatic supervision methods hinders effective fine-tuning. To address these challenges, we propose DR-FET, a descriptor-based retrieval-augmented framework that reduces the effective label space and constructs high-precision training data under noisy supervision. Our method introduces natural language descriptors as an intermediate semantic representation for both entity mentions and types. During inference, entity descriptors are used to retrieve a small set of semantically relevant candidate types, enabling the LLM to perform fine-grained classification under explicit candidate constraints. During training, the same descriptor and retrieval mechanism is reused to identify high-confidence instances from distantly supervised data, prioritizing label precision for efficient fine-tuning. Experiments on two widely used benchmarks demonstrate that the proposed method consistently outperforms existing fine-grained entity typing approaches under noisy supervision.
