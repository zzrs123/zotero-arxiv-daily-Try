# Paper Daily Reading - 2026-08-23

## 1. CoxFormer enables spatial omics inference with multimodal generative modeling

- Authors: Yiyang Yang, Xu Liao, Haoyu Zhang, Yida Wu, Yuling Jiao, Xiaobo Sun, Yao Wang, Tianshu Yu, Jin Liu
- Source: openalex
- Venue type: journal
- Journal: Nature Communications
- Publication status: published
- Publication date: 2026-08-20
- DOI: https://doi.org/10.1038/s41467-026-76404-8
- Categories: Single-cell and spatial transcriptomics, Bioinformatics and Genomic Networks, Genomics and Chromatin Dynamics
- Relevance: 3.703720756967069
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://doi.org/10.1038/s41467-026-76404-8
- PDF: https://www.nature.com/articles/s41467-026-76404-8_reference.pdf
- Local PDF: pdf/2026-08-23_01_CoxFormer enables spatial omics inference with multimodal generative modeling.pdf

Gene co-expression maps transcriptome-wide gene-gene relationships, yet high-quality estimates cover less than half the genome. Meanwhile, spatial omics either profiles restricted in situ panels or lacks cellular resolution. Extending co-expression transcriptome-wide could overcome these limitations by inferring unassayed gene expression at subcellular resolution. Here we show that CoxFormer integrates literature-derived gene knowledge with co-expression networks from bulk tissues and large-scale single-cell atlases to learn 512-dimensional representations for 32,016 human genes. These embeddings capture functional gene relationships and serve as a generative prior for spatial inference across platforms and modalities. Without requiring a matched single-cell RNA-sequencing reference, CoxFormer supports four applications beyond measured genes: histology-based expression imputation, gene activity prediction from chromatin accessibility, subcellular super-resolution inference, and pathological region detection. Together, CoxFormer extends gene embedding from gene- and cell-level tasks to whole-transcriptome spatial inference, providing a unified framework for biological analysis beyond the limited gene coverage of current spatial omics technologies. Yang, Liao, Zhang and colleagues present CoxFormer, an approach that learns whole-transcriptome gene representations from biomedical knowledge and co-expression data, thereby enabling spatial omics to predict unmeasured genes, enhance resolution and identify disease-related tissue regions.

## 2. STADiffuser: high-fidelity simulation and full-view 3D modeling of spatial transcriptomics

- Authors: Chihao Zhang, Shihua Zhang
- Source: openalex
- Venue type: journal
- Journal: Nature Communications
- Publication status: published
- Publication date: 2026-08-19
- DOI: https://doi.org/10.1038/s41467-026-76829-1
- Categories: Single-cell and spatial transcriptomics, Gene expression and cancer classification, Gene Regulatory Network Analysis
- Relevance: 3.596056065491698
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://doi.org/10.1038/s41467-026-76829-1
- PDF: https://www.nature.com/articles/s41467-026-76829-1_reference.pdf
- Local PDF: Not downloaded

Abstract Spatial transcriptomics technologies have provided invaluable insights by profiling gene expression alongside precise spatial information. However, they encounter high costs, data sparsity, and limited resolution, hindering their broader adoption and utility. Moreover, the lack of flexible simulators capable of generating high-fidelity simulated data has impeded the development of computational tools for spatial transcriptomic data analysis. To this end, we introduce STADiffuser, a versatile deep generative model that leverages diffusion modeling for accurate simulation of spatial transcriptomic data. STADiffuser employs a two-stage architecture: an autoencoder with a graph attention mechanism for learning spot embeddings, followed by a latent diffusion model integrated with a spatial denoising network for data generation. STADiffuser is the first simulator designed for spatial transcriptomic data, capable of handling multiple samples and 3D coordinates while supporting user-defined conditions. STADiffuser facilitates various downstream analyses, including accurate imputation, super-resolution, and full-slice generation. Furthermore, its generative scheme enables in silico experiments, thereby enhancing the statistical power in detecting differentially expressed genes and identifying cell-type-specific genes while effectively controlling confounding factors. Notably, STADiffuser scales to millions of spots and supports the full-view 3D modeling of a marmoset cerebellum atlas with over 20 million spots, enabling detailed investigations from arbitrary viewing angles.

## 3. STWave: Fine‐Scale Spatial Structure Discovery in Microscopic‐Resolution Spatial Transcriptomics via Patchwise Wavelet Graphs

- Authors: Tao Jiang, Songming Zhang, Xiaofeng Chen, Xiongtao Xiao, Wenming Cao, Weikai Li, Tong Zhao, Bing Li, Xinyue Xu, Zhongshan Li
- Source: openalex
- Venue type: journal
- Journal: Advanced Science
- Publication status: published
- Publication date: 2026-08-19
- DOI: https://doi.org/10.1002/advs.77240
- Categories: Single-cell and spatial transcriptomics, Cell Image Analysis Techniques, Gene expression and cancer classification
- Relevance: 3.5343138240905203
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://doi.org/10.1002/advs.77240
- PDF: Unavailable
- Local PDF: Not downloaded

ABSTRACT The advent of microscopic‐resolution spatial transcriptomics () enables the mapping of tissue complexity at subcellular resolution. However, the massive increase in data volume introduces a critical “memory wall,” significantly limiting the applicability of existing computational methods on deployable hardware platforms. In addition, traditional single‐scale modeling approaches often struggle to disentangle weak biological signals from technical noise. To overcome these challenges, STWave is proposed as a scalable framework for spatial domain identification. Specifically, STWave first enables efficient computation during both training and inference by leveraging a decoupled patch‐based learning strategy, thereby mitigating hardware limitations without sacrificing global contextual information. Furthermore, STWave adopts a discrete wavelet transform to encode gene expression features across multiple scales, effectively capturing both global trends and fine‐grained details. Extensive experimental results show that STWave attains state‐of‐the‐art clustering performance while maintaining exceptional computational efficiency, enabling scalable analysis of ultra‐large spatial transcriptomics datasets under constrained computational resources. Across platforms including Visium HD, Xenium, and CosMx, the proposed STWave accurately resolves complex tissue structures, enabling the identification of distinct immune niches within the tumor microenvironment and revealing fine‐grained developmental substructures. These results support STWave as a robust and efficient tool for large‐scale analysis.

## 4. CLEAR-ST: Physics-informed probabilistic decontamination of spatial transcriptomics by modeling mRNA lateral diffusion

- Authors: Ma, K., Huang, Y., Ho, J. W. K.
- Source: biorxiv
- Venue type: preprint
- Journal: biorxiv
- Publication status: preprint
- Publication date: 2026-08-22
- DOI: 10.64898/2026.08.13.744615
- Categories: bioinformatics
- Relevance: 3.3733406716967194
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://www.biorxiv.org/content/10.64898/2026.08.13.744615v1.full.pdf
- PDF: https://www.biorxiv.org/content/10.64898/2026.08.13.744615v1.full.pdf
- Local PDF: Not downloaded

Spatial transcriptomics is a rapidly evolving technology that allows for the measurement of gene expression in a spatially resolved manner. However, one technical problem that occurs for many sequencing-based spatial transcriptomics platforms is the presence of mRNA lateral diffusion, where mRNA from one spot can bind to probes in another spot, leading to contamination and inaccurate gene expression measurements. In Visium-like assays, this artifact is often visible as structured out-of-tissue signal and boundary-associated expression halos, yet its magnitude, spatial decay, and directional bias vary substantially across samples. Here, we present CLEAR-ST, a physics-informed probabilistic framework for correcting diffusion-like contamination in spatial transcriptomics data. CLEAR-ST infers a latent clean expression field using a denoising autoencoder and links it to the observed counts through a graph-Laplacian forward contamination model with learnable diffusion parameters, finally evaluated with a selectable count likelihood. We first conducted a comprehensive comparison between 10X official and independently generated Visium samples, demonstrating that out-of-tissue count profiles are highly related to nearby in-tissue expression, more concentrated near tissue boundaries, and diffusion directions across genes are likely coherent. Across real samples with varying contamination burden, CLEAR-ST improved spatial domain recovery, increased gene-level spatial autocorrelation, and enhanced the biological specificity of downstream analyses such as marker gene discovery, pathway identification and cell type deconvolution. Compared to benchmark methods, CLEAR-ST showed consistent gains in clustering quality and concordance with manual annotations. Together, CLEAR-ST provides an interpretable and practical approach for diffusion-aware correction of capture-based spatial transcriptomics data.

## 5. Pretraining Enhances Megabase-Scale Gene Expression Prediction with GeneUnet

- Authors: Sun, N., de Vazelhes, W., Li, P., Katz, T., Gong, J., Cheng, X., Song, L., Xing, E. P.
- Source: biorxiv
- Venue type: preprint
- Journal: biorxiv
- Publication status: preprint
- Publication date: 2026-08-22
- DOI: 10.64898/2026.08.13.744387
- Categories: genomics
- Relevance: 3.2544609320589313
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://www.biorxiv.org/content/10.64898/2026.08.13.744387v1.full.pdf
- PDF: https://www.biorxiv.org/content/10.64898/2026.08.13.744387v1.full.pdf
- Local PDF: Not downloaded

Predicting gene expression from DNA sequence across diverse genomic tracks is essential for understanding gene regulation and interpreting non-coding variants. Existing supervised methods are limited to few species and fail to exploit conserved regulatory mechanisms, while DNA foundation models capture cross-species information but remain constrained to kilobase-scale contexts insufficient for this task. Here we introduce GB.GeneUnet, an 837M-parameter transformer-based U-Net pretrained on 6 trillion tokens from multi-species genomes in OpenGenome2, extending genomic context to 1 Mb with up to 100x inference speedup over GeneMoE, a preliminary MoE transformer baseline of similar model size pretrained on the same data. Fine-tuned for gene expression prediction, GB.GeneUnet achieves state-of-the-art performance on the Borzoi benchmark at 524 kb context, and attains performance comparable to AlphaGenome at 1 Mb context while requiring a lighter fine-tuning procedure. Together, these results establish a scalable framework linking multi-species pretraining to ultra-long-context gene expression modeling.

## 6. PubMind: literature-based genetic variant extraction and functional annotation using large language models

- Authors: Peng Wang, Kai Wang
- Source: openalex
- Venue type: journal
- Journal: Nature Communications
- Publication status: published
- Publication date: 2026-08-20
- DOI: https://doi.org/10.1038/s41467-026-76834-4
- Categories: Biomedical Text Mining and Ontologies
- Relevance: 3.2524371755991193
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://doi.org/10.1038/s41467-026-76834-4
- PDF: https://www.nature.com/articles/s41467-026-76834-4_reference.pdf
- Local PDF: pdf/2026-08-23_06_PubMind_ literature-based genetic variant extraction and functional annotation using large language models.pdf

Abstract The rapid growth of biomedical literature has produced extensive functional knowledge on genetic variants, much of which remains buried in unstructured texts. Current databases such as ClinVar and the Human Gene Mutation Database (HGMD) attempt to catalog this knowledge but have significant limitations: ClinVar depends on voluntary submissions and covers only a fraction of published literature, while the academic version of HGMD is updated infrequently and provides limited functional annotation. To address these gaps, we developed PubMind, an AI-driven multi-layer framework that uses large language models (LLMs) to extract variant– function–disease associations and supporting evidence from text. PubMind integrates a fine-tuned BERT model for input triage with instruction-tuned GPT models for inferring disease associations and functional annotations. The system captures diverse variant types—including SNVs, CNVs, SVs, and gene fusions—and normalizes records to genome and transcriptome coordinates. Benchmarking demonstrates >90% accuracy in variant recognition and 99% precision in disease extraction. Application of PubMind on >41 million PubMed abstracts and >5 million open-access full-text articles produced PubMind-DB, a database containing ∼1.3 million unique variants with rich contextual annotations, accessible via a web interface and API. Only ∼10% of PubMind’s variants overlapped with ClinVar entries, yet >80% showed concordant pathogenicity labels, including full agreement with ClinVar’s expert-reviewed variants. Case studies demonstrate PubMind-DB’s ability to uncover supporting evidence for variant pathogenicity that might otherwise be missed by manual searches. Together, these findings establish PubMind as a scalable LLM-based framework that transforms unstructured biomedical text into structured genomic knowledge, advancing variant interpretation for precision medicine.

## 7. FourCorners: A Production Knowledge Graph Unifying Thailand’s Legal System

- Authors: Pawitsapak Akarajaradwong, Sarana Nutanong, Chompakorn Chaksangchaichot
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.7677263601637394
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-industry.124/
- PDF: https://aclanthology.org/2026.acl-industry.124.pdf
- Local PDF: pdf/2026-08-23_07_FourCorners_ A Production Knowledge Graph Unifying Thailand’s Legal System.pdf

Jurisdictionally bound domains, such as law, often lack standardized, machine-readable data formats, requiring foundational infrastructure before downstream applications can succeed. We present ThLexGraph, the first unified temporal knowledge graph for Thai legal data, integrating 3,840 laws (6,273 versions) with 87,394 Supreme Court decisions, updated daily. The graph encodes hierarchy, temporal versioning, cross-references, and sequential order, all extracted from unstructured official sources where no structured representation previously existed. A five-setting comparison on NitiBench-Tax isolates data infrastructure as the sole variable: graph-structured retrieval achieves Citation F1 of 0.812 versus 0.666 for practitioner-standard web search and 0.685 for flat vector retrieval, while searching a corpus 53x larger. Trace analysis of 820 agent-issued queries reveals that hierarchy traversal and cross-reference following, capabilities absent from generic retrieval, are exercised in 50% and 16% of questions, respectively. Our system demonstrates that structured modeling of hierarchy, temporal versioning, cross-references, and sequential order can overcome structural limitations of legal data published without standardized formats.

## 8. A11y-Compressor: A Framework for Enhancing the Efficiency of GUI Agent Observations through Visual Context Reconstruction and Redundancy Reduction

- Authors: Michito Takeshita, Takuro Kawada, Takumi Ohashi, Shunsuke Kitada, Hitoshi Iyatomi
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.767468450306991
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-srw.50/
- PDF: https://aclanthology.org/2026.acl-srw.50.pdf
- Local PDF: pdf/2026-08-23_08_A11y-Compressor_ A Framework for Enhancing the Efficiency of GUI Agent Observations through Visual Context Reconstructio.pdf

AI agents that interact with graphical user interfaces (GUIs) require effective observation representations for reliable grounding.The accessibility tree is a commonly used text-based format that encodes UI element attributes, but it suffers from redundancy and lacks structural information such as spatial relationships among elements.We propose A11y-Compressor, a framework that transforms linearized accessibility trees into compact and structured representations.Our implementation, Compressed-a11y, applies a lightweight and structured transformation pipeline with modal detection, redundancy reduction, and semantic structuring.Experiments on the OSWorld benchmark show that Compressed-a11y reduces input tokens to 22% of the original while improving task success rates by 5.1 percentage points on average.

## 9. From Passive Metric to Active Signal: The Evolving Role of Uncertainty Quantification in Large Language Models

- Authors: Jiaxin Zhang, Wendi Cui, Zhuohang Li, Lifu Huang, Bradley A. Malin, Caiming Xiong, Chien-Sheng Wu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.7673056890179244
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.2064/
- PDF: https://aclanthology.org/2026.findings-acl.2064.pdf
- Local PDF: pdf/2026-08-23_09_From Passive Metric to Active Signal_ The Evolving Role of Uncertainty Quantification in Large Language Models.pdf

While Large Language Models (LLMs) show remarkable capabilities, their unreliability remains a critical barrier to deployment in high-stakes domains. This survey charts a functional evolution in addressing this challenge: the evolution of uncertainty from a passive diagnostic metric to an active control signal guiding real-time model behavior. We demonstrate how uncertainty is leveraged as an active control signal across three frontiers: in advanced reasoning to optimize computation and trigger self-correction; in autonomous agents to govern metacognitive decisions about tool use and information seeking; and in reinforcement learning to mitigate reward hacking and enable self-improvement via intrinsic rewards. By grounding these advancements in emerging theoretical frameworks like Bayesian methods and Conformal Prediction, we provide a unified perspective on this transformative trend. This survey provides a comprehensive overview, critical analysis, and practical design patterns, arguing that mastering the new trend of uncertainty is essential for building the next generation of scalable, reliable, and trustworthy AI.

## 10. CogToM: A Comprehensive Theory of Mind Benchmark inspired by Human Cognition for Large Language Models

- Authors: Haibo Tong, Zeyang Yue, Feifei Zhao, Erliang Lin, Lu Jia, Ruolin Chen, Yinqian Sun, Qian Zhang, Yi Zeng
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.766594534823565
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1448/
- PDF: https://aclanthology.org/2026.acl-long.1448.pdf
- Local PDF: pdf/2026-08-23_10_CogToM_ A Comprehensive Theory of Mind Benchmark inspired by Human Cognition for Large Language Models.pdf

Whether Large Language Models (LLMs) truly possess human-like Theory of Mind (ToM) capabilities has garnered increasing attention. However, existing benchmarks remain largely restricted to narrow paradigms like false belief tasks, failing to capture the full spectrum of human cognitive mechanisms. We introduce CogToM , a comprehensive, theoretically grounded benchmark comprising over 8000 bilingual instances across 46 paradigms, validated by 49 human annotators. A systematic evaluation of 22 representative models, including frontier models like GPT-5.1 and Qwen3-Max, reveals significant performance heterogeneities and highlights persistent bottlenecks in specific dimensions. Further analysis based on human cognitive patterns suggests potential divergences between LLM and human cognitive structures. CogToM offers a robust instrument and perspective for investigating the evolving cognitive boundaries of LLMs. We release our code and data at https://github.com/Beijing-AISI/CogToM .

## 11. Chimera: Compositional Jailbreak Attacks on LLMs via Judgment-Driven Search over Heterogeneous Strategies

- Authors: Leo Hyun Park, Juwon Cho, Gyuhwan Kim, YoonDong Yeo, Taekyoung Kwon
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.7641887165402816
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1667/
- PDF: https://aclanthology.org/2026.findings-acl.1667.pdf
- Local PDF: pdf/2026-08-23_11_Chimera_ Compositional Jailbreak Attacks on LLMs via Judgment-Driven Search over Heterogeneous Strategies.pdf

Large Language Models (LLMs) remain vulnerable to jailbreak attacks despite extensive safety alignment. While automated red-teaming has emerged as a critical evaluation protocol, existing methods face two primary limitations: they largely explore homogeneous transformations in isolation, and they rely on brittle judgment metrics that frequently misclassify non-refusal hallucinations as successful attacks. In this paper, we reformulate jailbreak attacks as a compositional search problem guided by context-aware evaluation. We propose Chimera, a framework that generates compositional jailbreak attacks via judgment-driven search over heterogeneous strategies. Chimera systematically explores the combinatorial space of disjoint primitives, such as integrating technical obfuscation with semantic persuasion, under strict ordering constraints. Crucially, to drive the search process effectively, we introduce StrongREJECT++, a relevance-aware metric that eliminates false positive rewards by penalizing irrelevant responses. Experiments on multiple open-source and commercial LLMs show that Chimera uncovers qualitatively different vulnerability regions and consistently improves attack success rates and transferability compared to state-of-the-art baselines.

## 12. Look Light, Think Heavy: What Multimodal Chain-of-Thought Reasoning Can and Cannot Do

- Authors: Zhuoran Jin, Kejian Zhu, Hongbang Yuan, Yupu Hao, Pengfei Cao, Yubo Chen, Kang Liu, Jun Zhao
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.763902627305182
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.387/
- PDF: https://aclanthology.org/2026.acl-long.387.pdf
- Local PDF: pdf/2026-08-23_12_Look Light, Think Heavy_ What Multimodal Chain-of-Thought Reasoning Can and Cannot Do.pdf

Chain-of-Thought (CoT) has become a standard method for improving reasoning capabilities in large language models (LLMs) by eliciting step-by-step thinking, but its effectiveness in multimodal tasks remains unclear. In this paper, we aim to systematically investigate the key question: What can multimodal Chain-of-Thought reasoning do, and where and why does it fall short? To this end, we evaluate 12 multimodal tasks across perception and reasoning categories using both 14 non-reasoning models and 8 reasoning models. Our analysis reveals several important findings: (1) CoT is not a free lunch and should be used selectively depending on the specific requirements of each task. For perception tasks, CoT can lead to undesirable side effects, such as reduced performance in visual grounding and object counting. In contrast, it proves effective for reasoning tasks involving mathematical, scientific, and multi-image reasoning; (2) Compared to original models, existing open-source multimodal reasoning models often yield only marginal overall improvements, possibly due to an overemphasis on mathematical reasoning at the expense of broader capabilities; (3) Visual reasoning remains a key bottleneck for current multimodal CoT, as models exhibit a Look Light, Think Heavy” pattern where verbal reflection rises and falls during reasoning, whereas visual reflection consistently diminishes. These findings suggest that while multimodal CoT handles verbal reflection relatively well, it lacks the ability to maintain deep visual introspection throughout the reasoning process.

## 13. Pru-CoT: Towards Efficient Reasoning Distillation via Pruning Chain-of-Thought

- Authors: Han Liu, Shuotian Ma, Hui Li, Xiaotong Zhang, Fenglong Ma, Hong Yu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.763052939058126
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1684/
- PDF: https://aclanthology.org/2026.findings-acl.1684.pdf
- Local PDF: pdf/2026-08-23_13_Pru-CoT_ Towards Efficient Reasoning Distillation via Pruning Chain-of-Thought.pdf

Knowledge distillation has emerged as a pivotal paradigm for transferring the superior reasoning capabilities of Large Reasoning Models (LRMs) to efficient student models. However, the raw Chain-of-Thought (CoT) trajectories are often verbose and redundant, which dilutes the underlying logic and hinders effective knowledge distillation for student models. Although recent work has focused on pruning CoT to streamline these reasoning paths, existing local heuristic methods often fail to capture global causal logic due to rigid rules and limited search spaces, while global heuristic approaches incur substantial computational costs. To address these issues, we propose Pru-CoT (Pruning Chain-of-Thought), a framework that aims to extract the essential logical structure from reasoning chains. Pru-CoT implements a step-level importance assessment via global optimization on a frozen student large language model (LLM), quantifying the gradient-based causal contribution of each component. Guided by these important signals, the framework performs fidelity-constrained pruning, utilizing an LLM-driven process to synthesize concise, logically coherent narratives. Extensive experiments on mathematical reasoning benchmarks demonstrate that models trained with Pru-CoT not only achieve superior accuracy but also generate significantly more compact reasoning paths compared to those trained on raw verbose data.

## 14. SMARTER: A Data-efficient Framework to Improve Toxicity Detection with Explanation via Self-augmenting Large Language Models

- Authors: Huy Nghiem, Advik Sachdeva, Hal Daumé Iii
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.76211570753996
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1584/
- PDF: https://aclanthology.org/2026.acl-long.1584.pdf
- Local PDF: pdf/2026-08-23_14_SMARTER_ A Data-efficient Framework to Improve Toxicity Detection with Explanation via Self-augmenting Large Language Mo.pdf

To address toxic content on social media, we introduce SMARTER, a data-efficient 2-stage framework for explainable content moderation using Large Language Models (LLMs). In Stage 1, we leverage LLMs’ own outputs to generate synthetic explanations for correct and incorrect labels, enabling preference optimization with minimal supervision. In Stage 2, we refine explanation quality through cross-model training, allowing weaker models to align with stronger ones. Experiments on 3 benchmarks (HateXplain, Latent Hate, Implicit Hate) show SMARTER achieves up to 13% macro-F1 improvement over few-shot baselines using only 6-57% of training data. Our framework offers a scalable strategy for low-data settings by harnessing LLMs’ self-improvement for explainable moderation.

## 15. EnsemW2S: Enhancing Weak-to-Strong Generalization with Large Language Model Ensembles

- Authors: Aakriti Agrawal, Mucong Ding, Chenghao Deng, Zora Che, Arjun Rajaram, Anirudh Satheesh, Bang An, C. Bayan Bruss, John Langford, Furong Huang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.7620511555881206
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.2093/
- PDF: https://aclanthology.org/2026.findings-acl.2093.pdf
- Local PDF: pdf/2026-08-23_15_EnsemW2S_ Enhancing Weak-to-Strong Generalization with Large Language Model Ensembles.pdf

With Large Language Models (LLMs) rapidly approaching and potentially surpassing human-level performance, it has become imperative to develop approaches capable of effectively supervising and enhancing these powerful models using smaller, human-level models exposed to only human-level data. We address this critical weak-to-strong (W2S) generalization challenge by proposing a novel method aimed at improving weak experts, by training on the same limited human-level data, enabling them to generalize to complex, super-human-level tasks. Our approach, called EnsemW2S, employs a token-level ensemble strategy that iteratively combines multiple weak experts, systematically addressing the shortcomings identified in preceding iterations. By continuously refining these weak models, we significantly enhance their collective ability to supervise stronger student models. We extensively evaluate the generalization performance of both the ensemble of weak experts and the subsequent strong student model across in-distribution (ID) and out-of-distribution (OOD) datasets. For OOD, we specifically introduce question difficulty as an additional dimension for defining distributional shifts. Our empirical results demonstrate notable improvements, achieving 4%, and 3.2% improvements on ID datasets and, upto 6% and 2.28% on OOD datasets for experts and student models respectively, underscoring the effectiveness of our proposed method in advancing W2S generalization.

## 16. CoVerRL: Breaking the Consensus Trap in Label-Free Reasoning via Generator-Verifier Co-Evolution

- Authors: Teng Pan, Yuchen Yan, Zixuan Wang, Ruiqing Zhang, Guiyang Hou, Wenqi Zhang, Weiming Lu, Jun Xiao, Yongliang Shen
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.76131696814713
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1376/
- PDF: https://aclanthology.org/2026.acl-long.1376.pdf
- Local PDF: pdf/2026-08-23_16_CoVerRL_ Breaking the Consensus Trap in Label-Free Reasoning via Generator-Verifier Co-Evolution.pdf

Label-free reinforcement learning enables large language models to improve reasoning capabilities without ground-truth supervision, typically by treating majority-voted answers as pseudo-labels. However, we identify a critical failure mode: as training maximizes self-consistency, output diversity collapses, causing the model to confidently reinforce systematic errors that evade detection. We term this the consensus trap. To escape it, we propose CoVerRL, a framework where a single model alternates between generator and verifier roles, with each capability bootstrapping the other. Majority voting provides noisy but informative supervision for training the verifier, while the improving verifier progressively filters self-consistent errors from pseudo-labels. This co-evolution creates a virtuous cycle that maintains high reward accuracy throughout training. Experiments across Qwen and Llama model families demonstrate that CoVerRL outperforms label-free baselines by 4.7-5.9% on mathematical reasoning benchmarks. Moreover, self-verification accuracy improves from around 55% to over 85%, confirming that both capabilities genuinely co-evolve.

## 17. PASs-MoE: Mitigating Misaligned Co-drift among Router and Experts via Pathway Activation Subspaces for Continual Learning

- Authors: ZhiYan Hou, Haiyun Guo, Haokai Ma, Yandu Sun, Yonghui Yang, Jinqiao Wang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.761045782946759
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1474/
- PDF: https://aclanthology.org/2026.acl-long.1474.pdf
- Local PDF: pdf/2026-08-23_17_PASs-MoE_ Mitigating Misaligned Co-drift among Router and Experts via Pathway Activation Subspaces for Continual Learnin.pdf

Continual instruction tuning (CIT) requires multimodal large language models (MLLMs) to adapt to a stream of tasks without forgetting prior capabilities. A common strategy is to isolate updates by routing inputs to different LoRA experts. However, existing LoRA-based Mixture-of-Experts (MoE) methods often jointly update the router and experts in an indiscriminate way, causing the router’s preferences to co-drift with experts’ adaptation pathways and gradually deviate from early-stage input–expert specialization. We term this as Misaligned Co-drift , which blurs expert responsibilities and exacerbates forgetting. To address this, we introduce the pathway activation subspace (PASs) , a LoRA-induced subspace that reflects which low-rank pathway directions an input activates in each expert, providing a capability-aligned coordinate system for routing and preservation. Based on PASs, we propose a fixed-capacity PASs-based MoE–LoRA method with two components: PAS-guided Reweighting, which calibrates routing using each expert’s pathway activation signals, and PAS-aware Rank Stabilization, which selectively stabilizes rank directions important to previous tasks. Experiments on a CIT benchmark show that our approach consistently outperforms a range of conventional continual learning baselines and MoE–LoRA variants in both accuracy and resistance to forgetting, without increasing model parameters. Our code is publicly available at https://github.com/yueluoshuangtian/PASs-MoE .

## 18. GCoT-Decoding: Unlocking Deep Reasoning Paths for Universal Question Answering

- Authors: Guanran Luo, Wentao Qiu, Zhongquan Jian, Meihong Wang, Qingqiang Wu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.760959139628514
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.319/
- PDF: https://aclanthology.org/2026.findings-acl.319.pdf
- Local PDF: pdf/2026-08-23_18_GCoT-Decoding_ Unlocking Deep Reasoning Paths for Universal Question Answering.pdf

Chain-of-Thought (CoT) reasoning can enhance large language models (LLMs), but it requires manually designed prompts to guide the model. Recently proposed CoT-decoding enables the model to generate CoT-style reasoning paths without prompts, but it is only applicable to problems with fixed answer sets. To address this limitation, we propose a general decoding strategy—GCoT-decoding—that extends applicability to a broader range of question-answering tasks. GCoT-decoding employs a two-stage branching method combining Fibonacci sampling and heuristic error backtracking to generate candidate decoding paths. It then splits each path into a reasoning span and an answer span to accurately compute path confidence, and finally aggregates semantically similar paths to identify a consensus answer, replacing traditional majority voting. We conduct extensive experiments on six datasets covering both fixed and free QA tasks. Our method not only maintains strong performance on fixed QA but also achieves significant improvements on free QA, demonstrating its generality.

## 19. Resonant Context Anchoring: Decoupling Attention Routing and Signal Gain at Inference Time

- Authors: Mingkuan Zhao, Yide Gao, Wentao Hu, Suquan Chen, Tianchen Huang, Zhenhua An, Zetao Chang, Xiayu Sun, Yuheng Min
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.7607496263954188
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1824/
- PDF: https://aclanthology.org/2026.findings-acl.1824.pdf
- Local PDF: pdf/2026-08-23_19_Resonant Context Anchoring_ Decoupling Attention Routing and Signal Gain at Inference Time.pdf

Large Language Models (LLMs) frequently exhibit “contextual disregard” when faced with input evidence that conflicts with their internal parametric memory, leading to persistent factual hallucinations. Existing mitigation strategies primarily rely on suppressing specific neuron activations or employing computationally expensive contrastive decoding mechanisms, which often result in increased perplexity or significantly elevated inference latency. To address these limitations, we propose Resonant Context Anchoring (RCA), a lightweight inference-time intervention method grounded in the perspective of residual stream signal dynamics. RCA aims to resolve the signal attenuation of external evidence during its propagation through deep networks. The core mechanism involves the orthogonal decoupling of routing logic and information magnitude within the self-attention module. By utilizing raw pre-softmax attention scores as an instantaneous metric of semantic alignment, we construct a dynamic gain field via non-linear rectification to selectively amplify the norms of value vectors corresponding to context tokens, without altering the attention probability distribution. This mechanism effectively elevates the signal-to-noise ratio (SNR) of input evidence within the residual stream mixture, thereby robustly anchoring the generation trajectory to the truthful context during inference. Extensive experiments on the Llama-3 model series demonstrate that RCA significantly improves contextual faithfulness across multiple factual consistency and strong knowledge-conflict tasks, effectively suppressing parametric hallucinations. Furthermore, results confirm that as a training-free and computationally negligible plug-and-play module, RCA achieves a Pareto improvement in faithfulness and fluency while maintaining the model’s general language understanding capabilities. Our code is available at https://anonymous.4open.science/r/RCA-Implementation-D8B5

## 20. Losing our Tail, Again: (Un)Natural Selection & Multilingual LLMs

- Authors: Eva Vanmassenhove
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.76046550589734
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.532/
- PDF: https://aclanthology.org/2026.acl-long.532.pdf
- Local PDF: pdf/2026-08-23_20_Losing our Tail, Again_ (Un)Natural Selection & Multilingual LLMs.pdf

Multilingual Large Language Models considerably changed how technologies influence language. While previous technologies could mediate or assist humans, there is now a tendency to offload the task of writing itself to these technologies, enabling models to change our languages more directly. While they provide us quick access to information and impressively fluent output, beneath their (apparent) sophistication lies a subtle, insidious threat: the gradual decline and loss of linguistic diversity. In this position paper, I explore how model collapse, with a particular focus on translation technology, can lead to the loss of linguistic forms, grammatical features, and cultural nuance. Model collapse refers to the consequences of self-consuming training loops, where automatically generated data (re-)enters the training data, leading to a gradual distortion of the data distribution and the underrepresentation of low-probability linguistic phenomena. Drawing on recent work in Computer Vision, Natural Language Processing and Machine Translation, I argue that the many tails of our linguistic distributions might be vanishing, and with them, the narratives and identities they carry. This paper is a call to resist linguistic flattening and to reimagine Natural Language Processing as a field that encourages, values and protects expressive multilingual diversity and creativity.

## 21. Frame-Semantic Knowledge Injection for Event-Level Inference in LLMs

- Authors: Shahid Iqbal Rai, Danilo Croce, Roberto Basili
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.7600545933784773
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-short.55/
- PDF: https://aclanthology.org/2026.acl-short.55.pdf
- Local PDF: pdf/2026-08-23_21_Frame-Semantic Knowledge Injection for Event-Level Inference in LLMs.pdf

Large language models (LLMs) are fluent but often brittle when interpretation depends on external information (e.g., events or participant roles), as next-token prediction does not explicitly encode situation-level semantic constraints. FrameNet provides a structured account of semantics through its inventory of frames, roles, and relations. We present a scalable framework that injects frame-semantic knowledge into LLMs via LoRA, moving from fact-oriented prompting to principle-oriented supervision over the full FrameNet inventory. The supervision encodes semantic constraints through semantic types, sense-aware definitions, frame relations, and role-annotated examples. To test whether this knowledge generalizes beyond surface cues, we use Natural Language Inference (NLI) as a diagnostic task for event-level reasoning. Experiments on CONFER and SNLI show consistent gains over Meta-Llama-3.1-8B-Instruct in zero-shot and few-shot settings, especially for entailment and contradiction. Complementary semantic role labeling analyses further indicate improved sensitivity to frame, role, and span structure.

## 22. Discovering the Gems in Early Layers: Accelerating Long-Context LLMs with 1000x Input Token Reduction

- Authors: Zhenmei Shi, Yifei Ming, Xuan-Phi Nguyen, Yingyu Liang, Shafiq Joty
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.759621566690922
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.677/
- PDF: https://aclanthology.org/2026.findings-acl.677.pdf
- Local PDF: pdf/2026-08-23_22_Discovering the Gems in Early Layers_ Accelerating Long-Context LLMs with 1000x Input Token Reduction.pdf

Large Language Models (LLMs) have demonstrated remarkable capabilities in handling long context inputs, but this comes at the cost of increased computational resources and latency. Our research introduces a novel approach for the long context bottleneck to accelerate LLM inference and reduce GPU memory consumption. We show that LLMs can identify relevant tokens in the early layers prior to generating query responses. Leveraging this insight, we propose an algorithm that uses early layers of an LLM as filters to select and compress input tokens, significantly reducing the context length for subsequent processing. Our method, GemFilter, demonstrates substantial improvements in both speed and memory efficiency compared to existing techniques, such as standard attention and SnapKV/H2O. Notably, it achieves a 2.4X speedup and 30% reduction in GPU memory usage compared to SOTA methods. When evaluated on the Needle in a Haystack task, GemFilter significantly outperforms standard attention and SnapKV, while demonstrating comparable performance on the LongBench challenge. GemFilter is simple, training-free, and broadly applicable across different LLMs. Moreover, it provides interpretability by allowing humans to inspect the selected input sequence. Our findings provide practical benefits for deploying LLMs and deepen our understanding of their internal mechanisms, paving the way for further optimizations in LLM design and inference. Our code is available at https://github.com/SalesforceAIResearch/GemFilter .

## 23. Beyond Facts- Benchmarking Distributional Reading Comprehension in Large Language Models

- Authors: Pei-Fu Guo, Ya An Tsai, Chun-Chia Hsu, Kai-Xin Chen, Yun-Da Tsai, Kai-Wei Chang, Nanyun Peng, Mi-Yen Yeh, Shou-De Lin
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.759535048339096
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.520/
- PDF: https://aclanthology.org/2026.findings-acl.520.pdf
- Local PDF: pdf/2026-08-23_23_Beyond Facts- Benchmarking Distributional Reading Comprehension in Large Language Models.pdf

While most reading comprehension benchmarks for LLMs focus on factual information that can be answered by localizing specific textual evidence, many real-world tasks require understanding distributional information, such as population-level trends and preferences expressed across collections of text. We introduce Text2DistBench, a reading comprehension benchmark for evaluating LLMs’ ability to infer distributional knowledge from natural language. Built from real-world YouTube comments about movie and music entities, the benchmark provides models with entity metadata and associated comments, and requires them to answer distributional questions, such as estimating the proportions of positive and negative comments, or identifying the most and second most frequent topics discussed among viewers. To support reliable and long-term evaluation, the construction pipeline of Text2DistBench is fully automated and continuously updated to incorporate newly emerging entities over time. Experiments across multiple LLMs show that while models substantially outperform random baselines, performance varies widely across different distribution types and characteristics. These findings highlight both the capabilities and limitations of current LLMs in distributional reading comprehension and demonstrate the value of Text2DistBench as a practical and scalable testbed for future research.

## 24. Token-Level Policy Optimization: Linking Group-Level Rewards to Token-Level Aggregation via sequence-level likelihood

- Authors: Xingyu Lin, Yilin Wen, Du Su, En Wang, Wenbin Liu, Zhonghou Lv, Jinchang Hou, Chenfu Bao
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.7594126547823707
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1488/
- PDF: https://aclanthology.org/2026.acl-long.1488.pdf
- Local PDF: pdf/2026-08-23_24_Token-Level Policy Optimization_ Linking Group-Level Rewards to Token-Level Aggregation via sequence-level likelihood.pdf

Group Relative Policy Optimization (GRPO) has significantly advanced the reasoning ability of large language models (LLMs), particularly in their mathemat- ical reasoning performance. However, GRPO and related entropy regularization methods still struggle with token-level sparse-rewards, which is an inherent challenge in chain-of-thought (CoT) reasoning. These approaches often rely on undifferentiated token-level entropy regu- larization, which easily leads to entropy collapse or model degradation under sparse token rewards. In this work, we propose TEPO, a novel token-level framework that (1) leverages sequence-level likelihood to link group-level rewards with individual tokens via token-level aggregation, and (2) introduces a token-level KL-Divergence mask constraint that targets tokens with positive advantages and decreasing entropy to mitigate abrupt policy updates. Experiments demonstrate that TEPO not only achieves state-of-the-art performance on mathematical reasoning benchmarks but also markedly enhances training stability, reducing convergence time by 50% compared with GRPO/DAPO.

## 25. Improving Long-Context Translation via Self-Supervised Dual Learning

- Authors: Shanbo Cheng, Shuaijie She, Yu Bao, Jianbing Zhang, Jiajun Chen, Shujian Huang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.759357572331923
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1257/
- PDF: https://aclanthology.org/2026.acl-long.1257.pdf
- Local PDF: pdf/2026-08-23_25_Improving Long-Context Translation via Self-Supervised Dual Learning.pdf

Large language models (LLMs) with long context windows offer the potential to translate entire documents in a single pass, yet they frequently suffer from catastrophic information distortion, undermining the strict faithfulness required for translation. This challenge is compounded by the scarcity of document-level parallel data, which makes both supervised fine-tuning and reliable evaluation prohibitively expensive. We propose LongDu, a self-supervised post-training framework that improves long-document translation reliability via round-trip consistency. Given monolingual documents, LongDu samples multiple candidate translations, back-translates each candidate, and optimizes the model to prefer translations that best reconstruct the source. To make this signal robust for long-form generation, we design a reward that filters trivial failure modes (e.g., copying and local language drift) before applying a reconstruction and fluency score, enabling stable reinforcement learning without human annotations. We additionally introduce Long-CIRT, an automatic evaluation protocol that quantifies information distortion by measuring how much a LLM’s performance degrades after a translation cycle. Across multiple base models, LongDu substantially improves information retention and translation quality, with gains that generalize beyond the training length range and to unseen target languages.

## 26. ASTRA: An Automated Framework for Strategy Discovery, Retrieval, and Evolution for Jailbreaking LLMs

- Authors: Xu Liu, Yan Chen, Kan Ling, Yichi Zhu, Hengrun Zhang, Guisheng Fan, Huiqun Yu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.7582019734254617
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1843/
- PDF: https://aclanthology.org/2026.acl-long.1843.pdf
- Local PDF: pdf/2026-08-23_26_ASTRA_ An Automated Framework for Strategy Discovery, Retrieval, and Evolution for Jailbreaking LLMs.pdf

Despite extensive safety alignment, Large Language Models (LLMs) remain vulnerable to jailbreak attacks. However, existing methods generally lack the capability for continuous learning and self-evolution from interactions, limiting the diversity and adaptability of attack strategies. To address this, we propose ASTRA, an automated framework capable of autonomously discovering, retrieving, and evolving attack strategies. ASTRA operates on a closed-loop "attack-evaluate-distill-reuse” mechanism, which not only generates attack prompts but also automatically distills reusable strategies from every interaction. To systematically manage these strategies, we introduce a dynamic three-tier strategy library (Effective, Promising, and Ineffective) that categorizes strategies based on performance. This hierarchical memory mechanism enables the framework to enhance efficiency by leveraging successful patterns while optimizing the exploration space by avoiding known failures. Extensive experiments in a black-box setting demonstrate that ASTRA significantly outperforms existing baselines.

## 27. ZoFia: Zero-Shot Fake News Detection with Entity-Guided Retrieval and Multi-LLM Interaction

- Authors: Lvhua Wu, Xuefeng Jiang, Sheng Sun, Yan Lei, Tian Wen, Yuwei Wang, Min Liu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.7580102899401022
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1083/
- PDF: https://aclanthology.org/2026.findings-acl.1083.pdf
- Local PDF: pdf/2026-08-23_27_ZoFia_ Zero-Shot Fake News Detection with Entity-Guided Retrieval and Multi-LLM Interaction.pdf

The rapid spread of fake news threatens social stability and public trust, highlighting the urgent need for its effective detection.Although large language models (LLMs) show potential in fake news detection, they are limited by knowledge cutoff and easily generate factual hallucinations when handling time-sensitive news.Furthermore, the thinking of a single LLM easily falls into early stance locking and confirmation bias, making it hard to handle both content reasoning and fact checking simultaneously.To address these challenges, we propose ZoFia, a two-stage zero-shot fake news detection framework.In the first retrieval stage, we propose novel Hierarchical Salience and Salience-Calibrated Minimum Marginal Relevance (SC-MMR) algorithm to extract core entities accurately, which drive dual-source retrieval to overcome knowledge and evidence gaps.In the subsequent stage, a multi-agent system conducts multi-perspective reasoning and verification in parallel and achieves an explainable and robust result via adversarial debate.Comprehensive experiments on two public datasets show that ZoFia outperforms existing zero-shot baselines and even most few-shot methods.Our code has been open-sourced to facilitate the research community at https://github.com/SakiRinn/ZoFia .

## 28. VLCE: A Knowledge-Enhanced Framework for Image Description in Disaster Assessment

- Authors: Md. Mahfuzur Rahman, Marufa Kamal, Fahad Rahman, Sunzida Siddique, Ahmed Rafi Hasan, Mohd Ariful Haque, Kishor Datta Gupta, Roy George
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.7578829621906618
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.alvr-main.15/
- PDF: https://aclanthology.org/2026.alvr-main.15.pdf
- Local PDF: pdf/2026-08-23_28_VLCE_ A Knowledge-Enhanced Framework for Image Description in Disaster Assessment.pdf

General-purpose vision-language models (VLMs) such as LLaVA and QwenVL produce descriptions of disaster imagery that lack domain-specific vocabulary and actionable detail. We propose the Vision-Language Caption Enhancer (), a framework that integrates external semantic knowledge from ConceptNet and WordNet into the caption generation process for post-disaster satellite and UAV imagery. operates in two stages: first, a baseline VLM generates an initial caption conditioned on YOLOv8 object detections; second, a knowledge-enriched sequential model, a CNN-LSTM or a hierarchical cross-modal Transformer, refines the caption using a vocabulary augmented with 1,566 domain-relevant terms extracted from knowledge graphs. We evaluate on two disaster benchmarks: xBD (satellite, 6,369 images, 3 damage classes) and RescueNet (UAV, 4,494 images, 12 damage classes), using CLIPScore for semantic alignment and InfoMetIC for informativeness. On RescueNet with the Transformer decoder, with knowledge graph enrichment produces captions preferred over QwenVL baselines in 95.33% of image pairs on InfoMetIC and 73.64% on CLIPScore. Qualitative analysis shows that without knowledge graph integration, generated captions exhibit hallucinations, word repetition, and semantic incoherence, whereas knowledge-enriched captions maintain factual consistency and domain-appropriate vocabulary. intended as a continuous, extensible monitor of differential framing under changing real-world inputs.

## 29. A Survey of Toxicity Mitigation Strategies for Multilingual Language Models

- Authors: Soham Dan, Himanshu Beniwal, Thomas Hartvigsen
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.757351690012219
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1780/
- PDF: https://aclanthology.org/2026.findings-acl.1780.pdf
- Local PDF: pdf/2026-08-23_29_A Survey of Toxicity Mitigation Strategies for Multilingual Language Models.pdf

Large language models (LLMs) are transforming natural language processing across diverse linguistic communities. However, they can reproduce and amplify toxic content, including hate speech, harassment, and bias, posing significant risks to multilingual applications. We provide the first comprehensive survey of the many detoxification methods specifically tailored to multilingual LLMs. First, we define toxicity its measurement, then we provide a brief review of monolingual mitigation strategies, including data filtering, style transfer, expert-based logit steering, retrieval augmentation, and alignment with human feedback. We then present an in-depth taxonomy of multilingual approaches spanning (1) training methods, (2) post-hoc editing and decoding strategies, (3) alignment and reinforcement-learning techniques, and (4) data-centric innovations, such as parallel detox corpora and synthetic data generation. Finally, we discuss open challenges in multilingual detoxification, including data scarcity, evaluation inconsistencies, cultural nuances and biases. Overall, we produce a needed overview of the state of multi-lingual toxicity detection and mitigation on which the community can ground to build globally safe and equitable LLMs.

## 30. DART: Disambiguation-Aware Reasoning for Video-guided Machine Translation

- Authors: Boyu Guan, Chuang Han, Yang Zhao, Chengqing Zong
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.7573469576492866
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.352/
- PDF: https://aclanthology.org/2026.acl-long.352.pdf
- Local PDF: pdf/2026-08-23_30_DART_ Disambiguation-Aware Reasoning for Video-guided Machine Translation.pdf

Video-guided Machine Translation (VMT) seeks to enhance translation quality by incorporating contextual information derived from paired short video clips. However, many VMT samples are text-sufficient; even when visual information is needed, only minimal cues are required. Aiming to tackle these issues, we propose a novel framework DART ( D isambiguation- A ware R easoning for Video-guided Machine T ranslation). Reinforcement learning is used to incorporate multimodal large language models’ multimodal reasoning into VMT. The model dynamically switches between text-only processing and multimodal integration, contingent on the necessity of visual disambiguation. Furthermore, we present TVRF ( T ranslation-oriented V ideo R elevance F iltering), a systematic pipeline for constructing training data based on multimodal relevance to translation. This pipeline filters samples where video information is translation-relevant, mitigating training collapse caused by video-irrelevant data in conventional VMT. Experimental results show that our approach improves multimodal information utilization in VMT, yielding gains in both translation quality and computational efficiency.
