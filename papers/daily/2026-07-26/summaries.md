# Paper Daily Reading - 2026-07-26

## 1. RETROFIT: Reference-free deconvolution of cell-type mixtures in spatial transcriptomics

- Authors: Roopali Singh, Xi He, Xinyue Wang, A Park, Ross C. Hardison, Xiang Zhu, Qunhua Li
- Source: openalex
- Venue type: journal
- Journal: Nature Communications
- Publication status: published
- Publication date: 2026-07-24
- DOI: https://doi.org/10.1038/s41467-026-74928-7
- Categories: Single-cell and spatial transcriptomics, Gene expression and cancer classification, Molecular Biology Techniques and Applications
- Relevance: 3.4951530343921604
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://doi.org/10.1038/s41467-026-74928-7
- PDF: Unavailable
- Local PDF: Not downloaded

Abstract Spatial transcriptomics (ST) enables genome-wide measurement of gene expression in intact tissues, but typically captures mixtures of multiple cell types at each spatial location. Deconvolving these mixtures is essential for resolving cell-type-specific spatial organization and transcriptional programs. Existing approaches often rely on matched single-cell references or curated marker genes, which may be unavailable, incomplete, or difficult to integrate across platforms. We present RETROFIT, a Bayesian framework for reference-free deconvolution of spatial transcriptomics data that operates directly on sequencing measurements and incorporates external information only at a post hoc annotation stage when available. Across extensive simulations and multiple real datasets, RETROFIT demonstrates robust performance, outperforming existing reference-free methods and matching or exceeding reference-based approaches when references are imperfect. Notably, RETROFIT remains effective at near–single-cell resolution, as demonstrated on Visium HD data, recovering fine-grained spatial patterns without requiring single-cell references or marker genes. These results establish RETROFIT as a broadly applicable approach for reference-free spatial transcriptomics analysis across platforms and resolutions. RETROFIT is available at https://bioconductor.org/packages/retrofit/ .

## 2. PopSVG enables scalable detection of spatially variable genes in population-level spatial transcriptomics

- Authors: Tao Deng, Zhe Yu, Xiaobo Sun, Tianwei Yu, Hao Wu
- Source: openalex
- Venue type: journal
- Journal: Communications Biology
- Publication status: published
- Publication date: 2026-07-22
- DOI: https://doi.org/10.1038/s42003-026-10648-4
- Categories: Single-cell and spatial transcriptomics, Genomic variations and chromosomal abnormalities, RNA regulation and disease
- Relevance: 3.381504939568373
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://doi.org/10.1038/s42003-026-10648-4
- PDF: https://www.nature.com/articles/s42003-026-10648-4_reference.pdf
- Local PDF: pdf/2026-07-26_02_PopSVG enables scalable detection of spatially variable genes in population-level spatial transcriptomics.pdf

Spatially variable gene (SVG) detection is one of the most important tasks in spatial transcriptomics (ST) data analysis. To identify SVGs from population-level ST data, current practices often call SVGs separately from individual slices and then combine, or select highly variable genes from the concatenated expression matrix of all subjects as a surrogate. These approaches fail to simultaneously account for the common and subject-specific spatial patterns, leading to low accuracy and power. To overcome this issue, we develop PopSVG, a statistical method for population-level SVG detection. PopSVG hierarchically models the spatial expression from a population of biological replicates, balancing inter-subject homogeneity and heterogeneity. After parameter estimation, PopSVG computes statistical significance of genes being population-level SVGs. Extensive experiments demonstrate PopSVG’s superiority over existing approaches in identifying biologically relevant SVGs and improving multi-slice tissue domain segmentation, while scaling efficiently to large datasets. A Python implementation of PopSVG is available at https://github.com/ToryDeng/PopSVG. A scalable statistical method that detects spatially variable genes at the population level in spatial transcriptomics and characterizes their prevalence and spatial pattern strength across subjects.

## 3. cellGeometry: ultra-fast single-cell deconvolution of bulk RNA-Seq using a geometric solution

- Authors: Rachel Lau, Cankut Çubuk, Athina Spiliopoulou, Pedro Martínez-Paz, Anna E. A. Surace, Liliane Fossati‐Jimack, Soumya Raychaudhuri, Costantino Pitzalis, Myles Lewis
- Source: openalex
- Venue type: journal
- Journal: Nature Communications
- Publication status: published
- Publication date: 2026-07-23
- DOI: https://doi.org/10.1038/s41467-026-75762-7
- Categories: Single-cell and spatial transcriptomics, Cell Image Analysis Techniques, Microfluidic and Bio-sensing Technologies
- Relevance: 3.3772788870139947
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://doi.org/10.1038/s41467-026-75762-7
- PDF: Unavailable
- Local PDF: Not downloaded

Abstract Single-cell analysis has rapidly expanded to produce cell atlases encompassing all human tissues. However, computational methods to deconvolute bulk samples using single-cell reference data have failed to keep pace with the increasing data size. Here we present cellGeometry, which uses non-negative geometric deconvolution (NGD), an intuitive vector projection method featuring non-negative matrix regularisation. Using matrix operations, cellGeometry scales to massive datasets and is ultrafast. Benchmarked using simulations from single-cell/nucleus RNA-Seq datasets with &gt;3 million cells, cellGeometry is more accurate than existing methods and more robust against noise simulating different sequencing chemistries. It identifies outlying residual genes which may unveil pathogenic changes in gene expression and the presence of cell types absent from the reference. cellGeometry’s flexible architecture allows merging of single-cell reference signatures to expand the range of cell types being deconvoluted. Validated against real bulk RNA blood and tissue samples, cellGeometry produces more accurate and realistic results.

## 4. A benchmark study of vision and pathology foundation models for computational pathology

- Authors: Rohan Bareja, Francisco Carrillo‐Pérez, Yuanning Zheng, Marija Pizurica, Tarak Nath Nandi, Lu Tian, Jeanne Shen, Ravi Madduri, Olivier Gevaert
- Source: openalex
- Venue type: journal
- Journal: Nature Communications
- Publication status: published
- Publication date: 2026-07-23
- DOI: https://doi.org/10.1038/s41467-026-76004-6
- Categories: AI in cancer detection, Medical Image Segmentation Techniques, Cell Image Analysis Techniques
- Relevance: 3.0180717977433034
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://doi.org/10.1038/s41467-026-76004-6
- PDF: https://www.nature.com/articles/s41467-026-76004-6_reference.pdf
- Local PDF: pdf/2026-07-26_04_A benchmark study of vision and pathology foundation models for computational pathology.pdf

To advance precision medicine in pathology, artificial intelligence (AI)-driven foundation models must generalize across diverse datasets, tissues, and clinical tasks. However, their comparative performance and generalizability in computational pathology remain incompletely characterized. Here, we benchmark 32 AI foundation models across four categories, including general vision models (VM), general vision-language models (VLM), pathology-specific vision models (Path-VM), and pathology-specific vision-language models (Path-VLM), using slide- and patch-level tasks from The Cancer Genome Atlas (TCGA), Clinical Proteomic Tumor Analysis Consortium (CPTAC), external benchmarking datasets, and out-of-domain datasets. Across TCGA tasks, Path-VMs consistently rank among the strongest performers. Evaluation across CPTAC and out-of-domain datasets reveals more nuanced generalization behavior, with model rankings showing modest but consistent shifts across datasets and task categories. Pairwise statistical comparisons indicate that differences among top-performing models are often small and task dependent. Path-VMs outperform Path-VLMs and remain competitive with VMs. Model size and pretraining dataset scale do not consistently predict downstream performance. Finally, late decision-level ensembling improves aggregate performance across external datasets and tissue types, highlighting complementary strengths across foundation models. PathBench: https://pathbench.stanford.edu/ The comparative performance and generalisability of pathology foundation models remain largely unexamined. Here, the authors benchmark 32 AI pathology foundation models across large cancer datasets, showing that generalisation in computational pathology is heterogeneous and task-dependent regardless of dataset scale, but ensemble-based approaches can combine the strengths of different models.

## 5. HiC2Self: Self-supervised denoising for bulk and single-cell Hi-C contact maps

- Authors: Rui Yang, Alireza Karbalayghareh, Christina S. Leslie
- Source: openalex
- Venue type: journal
- Journal: Science Advances
- Publication status: published
- Publication date: 2026-07-23
- DOI: https://doi.org/10.1126/sciadv.adu8060
- Categories: Cell Image Analysis Techniques
- Relevance: 3.001449541571663
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://doi.org/10.1126/sciadv.adu8060
- PDF: Unavailable
- Local PDF: Not downloaded

Hi-C is a chromosome conformation capture assay used to study three-dimensional (3D) genome organization. Single-cell Hi-C technologies now enable the examination of 3D chromatin organization in individual cells, although these approaches often suffer from low-coverage libraries and data sparsity. Here, we introduce HiC2Self, a self-supervised framework for denoising Hi-C contact maps that requires only low-coverage data as input. HiC2Self reconstructs key structures such as topologically associating domains (TADs) and significant loops from bulk libraries, including cell-type-specific Hi-C structures, without the generalization challenges faced by supervised models. HiC2Self can also accurately reconstruct significant loops from Micro-C data at 1-kilobase resolution. When applied to single-nucleus methyl-3C data, HiC2Self successfully reconstructs local TAD structures around specific genes at 10-kilobase resolution with as few as 50 cells. Last, HiC2Self enables the examination of single-cell structures at 50-kilobase resolution in individual cells of the same cell type. HiC2Self thus provides a general tool for denoising bulk, pseudobulk, and single-cell 3D contact maps to enable downstream analyses.

## 6. FlashMem: Distilling Intrinsic Latent Memory via Computation Reuse

- Authors: Yubo Hou, Zhisheng Chen, Tao Wan, Zengchang Qin
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.8563941163184303
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.230/
- PDF: https://aclanthology.org/2026.findings-acl.230.pdf
- Local PDF: pdf/2026-07-26_06_FlashMem_ Distilling Intrinsic Latent Memory via Computation Reuse.pdf

The stateless architecture of Large Language Models inherently lacks the mechanism to preserve dynamic context, compelling agents to redundantly reprocess history to maintain long-horizon autonomy. While latent memory offers a solution, current approaches are hindered by architectural segregation, relying on auxiliary encoders that decouple memory from the reasoning backbone. We propose FlashMem , a framework that distills intrinsic memory directly from transient reasoning states via computation reuse. Leveraging the property that internal representations uniquely encode input trajectories, FlashMem identifies the last hidden state as a sufficient statistic for the interaction history. This enables a Shared-KV Consolidator to synthesize memory by attending directly to the backbone’s frozen cache, eliminating redundant re-parameterization. Furthermore, a parameter-free Cognitive Monitor leverages attention entropy to adaptively trigger consolidation only when high epistemic uncertainty is detected. Experiments demonstrate that FlashMem matches the performance of heavy baselines while reducing inference latency by 5 times , effectively bridging the gap between efficiency and persistent cognition.

## 7. Thesis Proposal: Targeted and Unified Cross-Lingual Unlearning from Multilingual Language Models

- Authors: Jan Bronec, Jindřich Helcl
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.8555917329390694
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-srw.49/
- PDF: https://aclanthology.org/2026.acl-srw.49.pdf
- Local PDF: pdf/2026-07-26_07_Thesis Proposal_ Targeted and Unified Cross-Lingual Unlearning from Multilingual Language Models.pdf

As large language models (LLM) trained on massive corpora scraped from the web exhibit the capability to reproduce sensitive and copyright-protected data, the field of machine unlearning has emerged to address the arising ethical and legal concerns.While previous research has provided a unified evaluation of LLM unlearning methods, this unification remains constrained to English-only models and datasets.We aim to address the prevailing fragmentation in recent cross-lingual unlearning research by extending existing unified benchmarks with multilingual data.To that end, we plan to compile a dataset of parallel translations of question-answer pairs consisting of real-world facts and synthetic personally identifiable information.Moreover, we will focus on mitigating model degradation during unlearning by selectively editing only those layers that contain the given knowledge.

## 8. Perplexity-Aware Data Scaling Law: Perplexity Landscapes Predict Performance for Continual Pre-training

- Authors: Lei Liu, Hao Zhu, Xiaoyan Yang, Yue Shen, Zhixuan Chu, Jian Wang, Jinjie Gu, Kui Ren
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.854936492587694
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.999/
- PDF: https://aclanthology.org/2026.acl-long.999.pdf
- Local PDF: pdf/2026-07-26_08_Perplexity-Aware Data Scaling Law_ Perplexity Landscapes Predict Performance for Continual Pre-training.pdf

Continual Pre-training (CPT) serves as a fundamental approach for adapting foundation models to domain-specific applications. Scaling laws for pre-training define a power-law relationship between dataset size and the test loss of an LLM. However, the marginal gains from simply increasing data for CPT diminish rapidly, yielding suboptimal data utilization and inefficient training. To address this challenge, we propose a novel perplexity-aware data scaling law to establish a predictive relationship between the perplexity landscape of domain-specific data and the test loss. Our approach leverages the pre-trained model’s own perplexity on domain data as a proxy for estimating the knowledge gap, effectively quantifying the informational perplexity landscape of candidate training samples. By fitting this scaling law across diverse perplexity regimes, we enable adaptive selection of high-utility data subsets, prioritizing content that maximizes knowledge absorption while minimizing redundancy and noise. Extensive experiments on both medical and general-domain benchmarks demonstrate that our method consistently identifies near-optimal training subsets, achieving superior performance with significantly reduced data consumption.

## 9. SR-RAG: Verifiable Multi-Hop Reasoning via On-the-fly Symbolic Graph Construction

- Authors: Zehua Wang, Zhaojin Zhang, Boyu Qiu, Xiaolong Weng, Ying Xiong, Buzhou Tang, Min Zhang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.854929124515847
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1922/
- PDF: https://aclanthology.org/2026.findings-acl.1922.pdf
- Local PDF: pdf/2026-07-26_09_SR-RAG_ Verifiable Multi-Hop Reasoning via On-the-fly Symbolic Graph Construction.pdf

Retrieval-Augmented Generation (RAG) has been widely adopted to enhance large language models (LLMs) by incorporating external knowledge. However, the two main existing paradigms struggle with multi-hop reasoning: aggregate-first approaches suffer from high construction costs and limited adaptability to dynamic knowledge, while dynamic-first approaches rely heavily on LLM reasoning and are prone to error propagation across reasoning steps. To address these limitations, we propose SR-RAG, a symbolic reasoning framework for multi-hop question answering. SR-RAG integrates the advantages of both paradigms by dynamically generating sub-questions, performing information retrieval and symbolic encoding based on an on-the-fly graph, and using a symbolic verifier to formally validate intermediate reasoning steps to ensure the correctness of intermediate answers and the completeness of the reasoning chain . We evaluate SR-RAG on multiple multi-hop benchmarks and a medical dataset. Experimental results demonstrate that it significantly improves both accuracy and robustness.

## 10. LDEDE: LRP-Driven Efficient Detection and Editing Framework for LLM Privacy Neurons

- Authors: Zhao Zhengyuan, Cao Lifeng, Sunhaodong, Shi Haotian, Du Xuehui, Liu Aodi, Niu Lanjie, Yang Xiaocheng
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.853519132847753
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1666/
- PDF: https://aclanthology.org/2026.findings-acl.1666.pdf
- Local PDF: pdf/2026-07-26_10_LDEDE_ LRP-Driven Efficient Detection and Editing Framework for LLM Privacy Neurons.pdf

The rapid advancement of large language models (LLMs) has significantly propelled downstream innovation, yet pervasive sensitive information in training data and the models’ memory characteristics pose severe privacy leakage risks. This contravenes core requirements of the General Data Protection Regulation (GDPR) and the right to be forgotten, becoming a critical bottleneck for secure and compliant deployment. Existing privacy protection methods have notable limitations: data preprocessing fails to cover context-dependent sensitive information; differential privacy (DP) and homomorphic encryption (HE) degrade model performance and increase computational overhead; traditional machine unlearning may cause catastrophic collapse; and neuron editing methods struggle with the accuracy-efficiency trade-off in privacy neuron localization, alongside privacy seesaw phenomena and general performance degradation. To address these challenges, this paper proposes LDEDE, a Layer-wise Relevance Propagation (LRP)-driven framework for efficient privacy neuron detection and editing. It offers three core advantages: 1) Precise multi-scale privacy localization via LRP-based relevance backpropagation and multi-token attention aggregation, achieving over 80% higher efficiency than gradient attribution methods; 2) First reveals the existence of "coupled privacy neurons" in LLMs, which are the key cause of the privacy seesaw phenomenon—mitigated by Polarity-Aware Neuron Editing (PANE) with differentiated logic; 3) Enhanced robustness and generalization for batch processing via privacy neuron aggregation. Experiments on Enron and MIMIC datasets demonstrate that compared to baselines, LDEDE maintains comparable general performance while reducing leakage risks of Phone, Email, and medical privacy by 42.7%–73.5% on average and cutting computational time by 60%–90%. It also exhibits stable performance across GPT-2, BERT-base, and LLAMA-7B, providing an efficient, lightweight solution for post-deployment dynamic LLM privacy protection.

## 11. Learning Flexible Large Multimodal Models with Arbitrary Modality Combinations

- Authors: Xinyu Zhao, Kangqi Ni, Jie Peng, Ang Li, Tianlong Chen
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.8530439788229933
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.517/
- PDF: https://aclanthology.org/2026.findings-acl.517.pdf
- Local PDF: pdf/2026-07-26_11_Learning Flexible Large Multimodal Models with Arbitrary Modality Combinations.pdf

Multimodal Large Language Models (MLLMs) show strong potential for cross-modal understanding by integrating powerful language models with multimodal encoders. However, extending MLLMs to handle a diverse range of modalities introduces two critical and intertwined challenges: (1) the reliance on fully paired multimodal data, often scarce or costly to acquire across all modalities, and (2) the computational inefficiency from processing numerous modality tokens and requiring substantial model updates for each new modality. To address these challenges, we enable MLLMs to handle missing modalities by generating representations for absent inputs. Furthermore, recognizing that an increasing number of modalities leads to linearly scaling token counts and that lengthy generated sequences can hinder performance, we employ a dual-stage compression mechanism. It first reduces the number of tokens per modality and then condenses information from multiple modalities into a single, compact token sequence. This culminates in Flex-M 3 , a novel MLLM framework designed for flexible and efficient learning across arbitrary combinations of modalities. Experiments across diverse multimodal benchmarks and backbones demonstrate that Flex-M 3 robustly handles varied modality inputs and scales efficiently. Notably, Flex-M outperforms its counterpart trained on only full-modality data, with consistent improvements of 2.29%, 3.15%, 11.01% on multimodal reasoning tasks NExT-QA, MUSIC-AVQA, SQA3D. Moreover, Flex-M 3 demonstrates superior robustness during inference, even when a high proportion of modalities are missing from the input samples, showcasing its capacity for complex, data-scarce multimodal applications.

## 12. Partial Information Decomposition via Normalizing Flows in Latent Gaussian Distributions

- Authors: Zhao, Wenyuan, Balachandran, Adithya, Tian, Chao, Liang, Paul
- Source: neurips
- Venue type: conference
- Journal: NeurIPS 2025
- Publication status: formally_published
- Publication date: 2026-04-23
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.852849690885067
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://proceedings.neurips.cc/paper_files/paper/2025/hash/06f484b5e9ce4e4b0e88ac0f29239201-Abstract-Conference.html
- PDF: https://proceedings.neurips.cc/paper_files/paper/2025/file/06f484b5e9ce4e4b0e88ac0f29239201-Paper-Conference.pdf
- Local PDF: pdf/2026-07-26_12_Partial Information Decomposition via Normalizing Flows in Latent Gaussian Distributions.pdf

The study of multimodality has garnered significant interest in fields where analyzing interactions among multiple information sources can enhance predictive modeling, data fusion, and interpretability. Partial information decomposition (PID) has emerged as a useful information-theoretic framework to quantify the degree to which individual modalities independently, redundantly, or synergistically convey information about a target variable. However, existing PID methods depend on optimizing over a joint distribution constrained by estimated pairwise probability distributions, which are costly and inaccurate for continuous and high-dimensional modalities. Our first key insight is that the problem can be solved efficiently when the pairwise distributions are multivariate Gaussians, and we refer to this problem as Gaussian PID (GPID). We propose a new gradient-based algorithm that substantially enhances computational efficiency for GPID based on an alternative formulation of the underlying optimization problem. To generalize the applicability to non-Gaussian data, we learn information-preserving encoders to transform random variables of arbitrary input distributions into pairwise Gaussian random variables. Along the way, we resolved an open problem regarding the optimality of joint Gaussian solutions for GPID. Empirical validation on diverse synthetic examples demonstrates that our proposed method provides more accurate and efficient PID estimates than existing baselines. We further evaluate on a series of large-scale multimodal benchmarks to show its utility in real-world applications of quantifying PID in multimodal datasets and selecting high-performing models.

## 13. Analyze Like a Venture Capitalist: Information-Gain and Knowledge Enhanced Graph Reasoning for Startup Success Prediction

- Authors: Haoyu Pei, Zhongyang Liu, Xiangyi Xiao, Xiaocong Du, Suting Hong, Kunpeng Zhang, Haipeng Zhang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.8527399303965644
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1555/
- PDF: https://aclanthology.org/2026.findings-acl.1555.pdf
- Local PDF: pdf/2026-07-26_13_Analyze Like a Venture Capitalist_ Information-Gain and Knowledge Enhanced Graph Reasoning for Startup Success Predictio.pdf

Most venture capital (VC) investments fail, while a few deliver outsized returns. Predicting startup success requires synthesizing relational evidence across company fundamentals, investor track records, and investment networks through explicit reasoning, which traditional machine learning and graph neural networks lack. Large language models excel at reasoning, but applying them to VC prediction must address: selecting compact evidence subgraphs from large investment networks, one-sided label noise where failures may be latent successes, and grounding decisions in structured VC domain knowledge. We present MIRAGE-VC, an evidence-grounded reasoning framework with three innovations. First, an information-gain-driven retriever distills networks into compact evidence subgraphs. Second, a dual-layer knowledge base grounds reasoning in VC principles. Third, a noise-aware mechanism down-weights mislabeled negatives via improved Positive-Unlabeled (PU) estimation. MIRAGE-VC achieves +5.9% F1 and +22.1% Precision@5 over state-of-the-art baselines. Expert evaluation confirms professional-quality rationales. We further validate our approach on public data with consistent improvements. Code and reasoning results are available at: https://github.com/ZhangDataLab/MIRAGE-VC.git

## 14. Eliminating Out-of-Domain Recommendations in LLM-based Recommender Systems: A Unified View

- Authors: Hao Liao, Jiwei Zhang, Jianxun Lian, Wensheng Lu, Mingqi Wu, Shuowangg, Yong Zhang, Yitian Huang, Mingyang Zhou, Rui Mao
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.852422874541758
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.310/
- PDF: https://aclanthology.org/2026.findings-acl.310.pdf
- Local PDF: pdf/2026-07-26_14_Eliminating Out-of-Domain Recommendations in LLM-based Recommender Systems_ A Unified View.pdf

Recommender systems based on Large Language Models (LLMs) are often plagued by hallucinations of out-of-domain (OOD) items. To address this, we propose RecLM, a unified framework that bridges the gap between retrieval and generation by instantiating three grounding paradigms under a single architecture: embedding-based retrieval, constrained generation over rewritten item titles, and discrete item-tokenizer generation. Using the same backbone LLM and prompts, we systematically compare these three views on public benchmarks. RecLM strictly eradicates OOD recommendations (OOD@10 = 0) across all variants, and the constrained generation variants RecLM-cgen and RecLM-token achieve overall state-of-the-art accuracy compared to both strong ID-based and LLM-based baselines. Our unified view provides a systematic basis for comparing three distinct paradigms to reduce item hallucinations, offering a practical framework to facilitate the application of LLMs to recommendation tasks. Source code is at https://github.com/microsoft/RecAI.

## 15. RRAtention: Dynamic Block Sparse Attention via Per-Head Round-Robin Shifts for Long-Context Inference

- Authors: Siran Liu, Guoxia Wang, Sa Wang, Jinle Zeng, Haoyang Xie, Siyu Lou, Jiabin Yang, Dianhai Yu, Haifeng Wang, Chao Yang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.852148258750351
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1199/
- PDF: https://aclanthology.org/2026.acl-long.1199.pdf
- Local PDF: pdf/2026-07-26_15_RRAtention_ Dynamic Block Sparse Attention via Per-Head Round-Robin Shifts for Long-Context Inference.pdf

The quadratic complexity of attention mechanisms poses a critical bottleneck for large language models processing long contexts. While dynamic sparse attention methods offer input-adaptive efficiency, they face fundamental trade-offs: requiring preprocessing, lacking global evaluation, violating query independence, or incurring high computational overhead. We present RRAttention, a novel dynamic sparse attention method that simultaneously achieves all desirable properties through a head **r**ound-**r**obin (RR) sampling strategy. By rotating query sampling positions across attention heads within each stride, RRAttention maintains query independence while enabling efficient global pattern discovery with stride-level aggregation. Our method reduces complexity from O(L 2 ) to O(L 2 /S 2 ) and employs adaptive Top- 𝜏 selection for optimal sparsity. Extensive experiments on natural language understanding (HELMET) and multimodal video comprehension (Video-MME) demonstrate that RRAttention recovers over 99% of full attention performance while computing only half of the attention blocks, achieving 2.4 × speedup at 128K context length and outperforming existing dynamic sparse attention methods. The code is available at [https://github.com/PaddlePaddle/PaddleFleet](https://github.com/PaddlePaddle/PaddleFleet) (see ‘Research/RRAttention‘).

## 16. Hindsight: Structured Agent Memory that Retains, Recalls, and Reflects

- Authors: Christopher Latimer, Nicolò Boschi, Andrew Neeser, Chris Bartholomew, Gaurav Srivastava, Xuan Wang, Naren Ramakrishnan
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.8515832674037975
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-demo.27/
- PDF: https://aclanthology.org/2026.acl-demo.27.pdf
- Local PDF: pdf/2026-07-26_16_Hindsight_ Structured Agent Memory that Retains, Recalls, and Reflects.pdf

We demonstrate Hindsight, a working memory system for AI agents that organizes long-term memory into four logical networks and exposes three core operations. The world, experience, observation, and opinion networks separate objective facts from subjective beliefs, giving developers visibility into what an agent knows versus what it believes. The retain, recall, and reflect operations handle ingestion, retrieval, and reasoning respectively, with a parallel pipeline that combines vector search, keyword matching, graph traversal, and temporal filtering, backed by PostgreSQL with pgvector. Unlike existing systems such as MemGPT, Zep, and Mem0, Hindsight is the only one that jointly provides fact-belief separation, temporal entity graphs, evolving opinions with confidence scores, and configurable behavioral profiles. On LongMemEval and LoCoMo, Hindsight with a 20B open-source model reaches 83.6% and 83.2% accuracy, outperforming full-context GPT-4o and all prior memory systems; with Gemini-3 Pro, LongMemEval accuracy reaches 91.4%. Our interactive demo lets users build memory graphs through multi-session conversations, inspect how memories are classified, and watch opinions form and change. The system is **open-source under the MIT license**, available as a Python package (pip install hindsight-all) and Docker image, with **13.3K GitHub stars** and 763 forks to date, and in production use at Fortune 500 enterprises. Video demo: https://youtu.be/4M2wS-yEmVA.

## 17. DDSurfer: A Weakly‐Supervised Dual‐Stream Deep Learning Framework for Cortical Surface Reconstruction From Diffusion MRI

- Authors: C L Li, Wei Zhang, Xi Zhu, Yuehua Chen, Nir A. Sochen, Jarrett Rushmore, Westin Cf, Yogesh Rathi, Lauren J. O'Donnell, Ofer Pasternak, Fan Zhang
- Source: openalex
- Venue type: journal
- Journal: Advanced Science
- Publication status: published
- Publication date: 2026-07-23
- DOI: https://doi.org/10.1002/advs.76596
- Categories: Advanced Neuroimaging Techniques and Applications, Functional Brain Connectivity Studies, Morphological variations and asymmetry
- Relevance: 2.8513082283611615
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://doi.org/10.1002/advs.76596
- PDF: Unavailable
- Local PDF: Not downloaded

Cortical surface reconstruction of white matter and pial surfaces from diffusion MRI (dMRI) is critical for neuroimaging analyses, including tractography, connectomics, and multimodal data integration. However, obtaining these surfaces from dMRI data is inherently challenged by its low spatial resolution and poor tissue contrast. Currently, this relies on T1-weighted images, from which the surfaces are reconstructed and then registered to the dMRI space-a process affected by inaccurate inter-modality registration. This study introduces DDSurfer, an end-to-end deep learning framework that directly generates high-fidelity cortical surfaces from dMRI data. DDSurfer leverages a novel dual-stream architecture that processes and synergistically fuses complementary microstructural features from dMRI, learning a diffeomorphic transformation for subject-specific surface reconstruction. The model is trained using a robust weakly-supervised strategy with automatically generated pseudo-ground-truth surfaces. Extensive evaluations on diverse datasets demonstrate that DDSurfer surpasses traditional methods in geometric accuracy, morphological consistency, and generalization. By providing a computationally efficient and robust T1-weighted-independent solution, DDSurfer overcomes a major bottleneck in dMRI, delivering a practical tool to advance accurate dMRI-centric connectomics and surface-based investigations. Source code and implementation as an interactive 3D Slicer module are publicly available at: https://github.com/ChengjinLii/DDSurfer.

## 18. Taming "Zombie" Agents: A Markov State-Aware Framework for Resilient Multi-Agent Evolution

- Authors: Taolin Zhang, Pukun Zhao, Qizhou Chen, Jiuheng Wan, Chen Chen, Xiaofeng He, Chengyu Wang, Richang Hong
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.851059658444046
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.373/
- PDF: https://aclanthology.org/2026.acl-long.373.pdf
- Local PDF: pdf/2026-07-26_18_Taming _Zombie_ Agents_ A Markov State-Aware Framework for Resilient Multi-Agent Evolution.pdf

Recent advancements in LLM-based multi-agent systems have demonstrated remarkable collaborative capabilities across complex tasks. To enhance the overall efficiency, existing methods often rely on aggressive graph topology evolution for agents (e.g., node or edge pruning), which risks prematurely discarding valuable agents due to transient issues such as hallucinations or temporary knowledge gaps. However, such hard pruning overlooks the potential for "zombie" agents to recover and contribute in subsequent discussion rounds. In this paper, we propose AgentRevive, a Markov state-aware framework for resilient multi-agent evolution. Our approach dynamically manages agent collaboration through soft state transitions, implemented via two key components: (1) State-Aware Policy Learning: Agent states are divided into "Active", "Standby", and "Terminated", selectively propagating messages based on agent memory. The policy employs a risk estimator to optimize agent state transitions by assessing hallucination risk, minimizing the influence of unreliable nodes while safeguarding valuable ones. (2) State-Aware Edge Optimization: Subgraph edges are pruned according to states learned from the policy, permanently removing "Terminated" nodes and retaining "Standby" nodes for subsequent rounds to observe potential future contributions. Extensive experiments on general reasoning, domain-specific, and hallucination challenge tasks show that our method consistently outperforms strong baselines and significantly reduces token consumption through state-aware agent scheduling.

## 19. SciVQR: A Multidisciplinary Multimodal Benchmark for Advanced Scientific Reasoning Evaluation

- Authors: Longteng Guo, Xuanxu Lin, Dongze Hao, Tongtian Yue, Pengkang Huo, Jiatong Ma, Yuchen Liu, Jing Liu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.850892863555496
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.28/
- PDF: https://aclanthology.org/2026.findings-acl.28.pdf
- Local PDF: pdf/2026-07-26_19_SciVQR_ A Multidisciplinary Multimodal Benchmark for Advanced Scientific Reasoning Evaluation.pdf

Scientific reasoning is a key aspect of human intelligence, requiring the integration of multimodal inputs, domain expertise, and multi-step inference across various subjects. Existing benchmarks for multimodal large language models (MLLMs) often fail to capture the complexity and traceability of reasoning processes necessary for rigorous evaluation. To fill this gap, we introduce SciVQR, a multimodal benchmark covering 54 subfields in mathematics, physics, chemistry, geography, astronomy, and biology. SciVQR includes domain-specific visuals, such as equations, charts, and diagrams, and challenges models to combine visual comprehension with reasoning. The tasks range from basic factual recall to complex, multi-step inferences, with 46% including expert-authored solutions. SciVQR not only evaluates final answers but also examines the reasoning process, providing insights into how models reach their conclusions. Our evaluation of leading MLLMs, including both proprietary and open-source models, reveals significant limitations in handling complex multimodal reasoning tasks, underscoring the need for improved multi-step reasoning and better integration of interdisciplinary knowledge in advancing MLLMs toward true scientific intelligence. The dataset and evaluation code are publicly available at https://github.com/CASIA-IVA-Lab/SciVQR.

## 20. REVEALER: Reinforcement-Guided Visual Reasoning for Element-Level Text-Image Alignment Evaluation

- Authors: FuLin Shi, Wenyi Xiao, Leilei Gan, Liang Ding, Binchen
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.8502836988709785
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.2200/
- PDF: https://aclanthology.org/2026.acl-long.2200.pdf
- Local PDF: pdf/2026-07-26_20_REVEALER_ Reinforcement-Guided Visual Reasoning for Element-Level Text-Image Alignment Evaluation.pdf

Evaluating the alignment between textual prompts and generated images is critical for ensuring the reliability and usability of text-to-image (T2I) models. However, most existing evaluation methods rely on coarse-grained metrics or static Question Answering (QA) pipelines, which lack fine-grained interpretability and struggle to reflect human preferences. To address this, we propose REVEALER , a reinforcement-guided visual reasoning framework for element-level text-to-image alignment evaluation. Adopting a structured ''grounding–reasoning–conclusion'' paradigm, our method enables Multimodal Large Language Models (MLLMs) to explicitly localize semantic elements and derive interpretable alignment judgments. We optimize the model via Group Relative Policy Optimization (GRPO) using a multi-dimensional reward function that targets format compliance, localization precision, and alignment accuracy.Extensive experiments confirm that REVEALER achieves state-of-the-art results across four benchmarks. Notably, on EvalMuse-40K, it surpasses the strong proprietary Gemini 3 Pro and Training-based baselines with absolute accuracy gains of +4.2% and +13.3% , respectively. Ablation studies further demonstrate the efficacy of our method, contributing a cumulative 19.6% improvement over the base model.

## 21. MTA:A Merge-then-Adapt Framework for Personalized Large Language Models

- Authors: Xiaopeng Li, Yuanjin Zheng, Wanyu Wang, Wenlin Zhang, Pengyue Jia, Yingyi Zhang, Haiying He, Mengyang Ma, Yiqi Wang, Maolin Wang, Xuetao Wei, Xiangyu Zhao
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.849990140218577
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.2040/
- PDF: https://aclanthology.org/2026.acl-long.2040.pdf
- Local PDF: pdf/2026-07-26_21_MTA_A Merge-then-Adapt Framework for Personalized Large Language Models.pdf

Personalized Large Language Models (PLLMs) aim to align model outputs with individual user preferences, a crucial capability for user-centric applications. However, the prevalent approach of fine-tuning a separate module for each user faces two major limitations: (1) storage costs scale linearly with the number of users, rendering the method unscalable; and (2) fine-tuning a static model from scratch often yields suboptimal performance for users with sparse data. To address these challenges, we propose MTA, a Merge-then-Adapt framework for PLLMs. MTA comprises three key stages. First, we construct a shared Meta-LoRA Bank by selecting anchor users and pre-training meta-personalization traits within meta-LoRA modules. Second, to ensure scalability and enable dynamic personalization combination beyond static models, we introduce an Adaptive LoRA Fusion stage. This stage retrieves and dynamically merges the most relevant anchor meta-LoRAs to synthesize a user-specific one, thereby eliminating the need for user-specific storage and supporting more flexible personalization. Third, we propose a LoRA Stacking for Few-Shot Personalization stage, which applies an additional ultra-low-rank, lightweight LoRA module on top of the merged LoRA. Fine-tuning this module enables effective personalization under few-shot settings. Extensive experiments on the LaMP benchmark demonstrate that our approach outperforms existing SOTA methods across multiple tasks. Our code is also available.

## 22. Training-Free Adaptive Speculative Decoding via Linguistic Priors

- Authors: Jingyi Wang, Jiaqi Huang, Zunnan Xu, Jun Zhou, Kehong Yuan, Xiang Qian
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.8496071827998137
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1065/
- PDF: https://aclanthology.org/2026.findings-acl.1065.pdf
- Local PDF: pdf/2026-07-26_22_Training-Free Adaptive Speculative Decoding via Linguistic Priors.pdf

Speculative decoding (SPD) has emerged as a promising technique to accelerate Large Language Model (LLM) inference. However, current approaches typically enforce a uniform verification standard, neglecting the inherent heterogeneity of natural language and failing to distinguish between semantically-rich content and structurally-predictable syntax. In this paper, we propose LinguaSpec, a training-free framework that leverages linguistic priors to enable adaptive drafting and verification. Specifically, we introduce: (1) a Static Linguistic Probe (SLP) to categorize tokens with zero latency; (2) Syntactic Normalized Surprisal (SNS) to calibrate uncertainty against category-specific entropy; and (3) a dual strategy of Syntactically-Guided Elastic Expansion and POS-Adaptive Deferred Verification to dynamically adjust drafting depth and verification rigor. By balancing semantic integrity with structural efficiency, LinguaSpec significantly accelerates inference without requiring additional training. Experimental results demonstrate its superior performance across diverse benchmarks.

## 23. Structured Confidence–Guided Online Adaptation for LLM-based Multi-Label Classification

- Authors: Pengyu Xu, JingRen Hou, Liping Jing, Jian Yu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.8480957772377358
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.822/
- PDF: https://aclanthology.org/2026.findings-acl.822.pdf
- Local PDF: pdf/2026-07-26_23_Structured Confidence–Guided Online Adaptation for LLM-based Multi-Label Classification.pdf

Large language models (LLMs) enable zero-shot and few-shot multi-label text classification via in-context learning, yet most approaches perform static inference and degrade under streaming test data due to distribution shift and long-tail labels. We study online test-time adaptation for LLM-based multi-label generation without any parameter updates, and identify two bottlenecks: (1) standard generation probabilities provide unreliable confidence because they ignore label competition at key decoding branches; (2) naive confidence-based caching overfits to frequent and easy examples, reducing label coverage and diversity. We propose SCOTTA, a structured confidence-guided online adaptation framework. SCOTTA introduces Label-set Local Likelihood Ratio (L3R), a label-level confidence measure that compares a target label against its valid competitors at critical decision positions. Using L3R as a unified signal, SCOTTA maintains an in-context exemplar cache via streaming submodular maximization, balancing label coverage, semantic diversity, and sample quality under a fixed context budget. Across four benchmarks, SCOTTA consistently improves Micro-F1 and Macro-F1 over strong LLM and non-LLM baselines, with the largest gains on long-tail labels.

## 24. Representation Interventions Enable Lifelong Knowledge Memory Control in LLMs

- Authors: Xuyuan Liu, Shengyu Chen, Xinshuai Dong, Yanchi Liu, Xujiang Zhao, Haoyu Wang, Yujun Yan, Haifeng Chen, Zhengzhang Chen
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.84800284644823
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.246/
- PDF: https://aclanthology.org/2026.acl-long.246.pdf
- Local PDF: pdf/2026-07-26_24_Representation Interventions Enable Lifelong Knowledge Memory Control in LLMs.pdf

Large language models (LLMs) often produce incorrect or outdated content. Updating their knowledge efficiently and accurately without costly retraining is a major challenge. This problem is particularly challenging for complex, unstructured knowledge in lifelong settings, where many edits must coexist without interference. We introduce **RILKE** (**R**epresentation **I**ntervention for **L**ifelong **K**nowledg**E** Control), a robust and scalable method that treats knowledge control as interventions within the model’s representation space. Leveraging representation-space expressiveness, we identify two key properties enabling RILKE to achieve fine-grained control over complex, unstructured knowledge while maintaining general utility with frozen base weights. During training, RILKE learns paraphrase-robust and edit-localized modules that limit each update to a low-dimensional subspace to minimize cross-edit interference. In inference, a query-adaptive router selects the appropriate module to guide the model’s generation. Across LLaMA and Qwen models, RILKE scales effectively to large-scale benchmarks, demonstrating high edit success and strong paraphrase generalization while preserving general utility with modest memory overhead. These results show RILKE is an effective and scalable solution for lifelong knowledge control in LLMs.

## 25. DPN-LE: Dual Personality Neuron Localization and Editing for Large Language Models

- Authors: Lifan Zheng, Xue Yang, Jiawei Chen, Chenyan WU, Jingyuan Zhang, Fanheng Kong, Xinyi Zeng, Xiang Chen, Yu Tian
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.8479338514673094
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1528/
- PDF: https://aclanthology.org/2026.findings-acl.1528.pdf
- Local PDF: pdf/2026-07-26_25_DPN-LE_ Dual Personality Neuron Localization and Editing for Large Language Models.pdf

With the widespread adoption of large language models (LLMs), understanding their personality representation mechanisms has become critical. As a novel paradigm in Personality Editing, most existing methods employ neuron-editing to locate and modify LLM neurons, requiring changes to numerous neurons and leading to significant performance degradation. This raises a fundamental question: Are all modified neurons directly related to personality representation? In this work, we investigate and quantify this specificity through assessments of general capability impact and representation-level patterns. We find that: 1) Current methods can change personalities but reduce overall performance. 2) Neurons are multifunctional, connecting personality traits and general knowledge. 3) Opposing personality traits demonstrate distinctly mutually exclusive representation patterns. Motivated by these findings, we propose DPN-LE (Dual Personality Neuron Localization and Editing), which identifies personality-specific neurons by contrasting MLP activations between high-trait and low-trait samples. DPN-LE constructs layer-wise steering vectors and applies dual-criterion filtering based on Cohen’s d effect size and activation magnitude to isolate mutually exclusive neuron subsets. Sparse linear intervention on these neurons enables precise personality control at inference time. Using only 1,000 contrastive sample pairs per trait, DPN-LE intervenes on ∼ 0.5% of neurons while achieving competitive personality control and substantially better capability preservation across reasoning tasks. Experiments on LLaMA-3-8B-Instruct and Qwen2.5-7B-Instruct demonstrate the effectiveness and generalizability of our approach.

## 26. Learning Uncertainty from Sequential Internal Dispersion in Large Language Models

- Authors: Ponhvoan Srey, Xiaobao Wu, Cong-Duy T Nguyen, Anh Tuan Luu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.847789188287923
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1862/
- PDF: https://aclanthology.org/2026.acl-long.1862.pdf
- Local PDF: pdf/2026-07-26_26_Learning Uncertainty from Sequential Internal Dispersion in Large Language Models.pdf

Uncertainty estimation is a promising approach to detect hallucinations in large language models (LLMs). Recent approaches commonly depend on model internal states to estimate uncertainty. However, they suffer from strict assumptions on how hidden states should evolve across layers, and from information loss by solely focusing on last or mean tokens. To address these issues, we present Sequential Internal Variance Representation (SIVR), a supervised hallucination detection framework that leverages token-wise, layer-wise features derived from hidden states. SIVR adopts a more basic assumption that uncertainty manifests in the degree of dispersion or variance of internal representations across layers, rather than relying on specific assumptions, which makes the method model and task agnostic. It additionally aggregates the full sequence of per-token variance features, learning temporal patterns indicative of factual errors and thereby preventing information loss. Experimental results demonstrate SIVR consistently outperforms strong baselines. Most importantly, SIVR enjoys stronger generalisation and avoids relying on large training sets, highlighting the potential for practical deployment.

## 27. D-VST: Diffusion Transformer for Pathology-Correct Tone-Controllable Cross-Dye Virtual Staining of Whole Slide Images

- Authors: yang, shurong, Wei, Dong, Hu, Yihuang, Peng, Qiong, Liu, Hong, Huang, Yawen, Wu, Xian, Zheng, Yefeng, Wang, Liansheng
- Source: neurips
- Venue type: conference
- Journal: NeurIPS 2025
- Publication status: formally_published
- Publication date: 2026-04-23
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.8459938778688687
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://proceedings.neurips.cc/paper_files/paper/2025/hash/048445f5e3321dc9721930b15ba9387b-Abstract-Conference.html
- PDF: https://proceedings.neurips.cc/paper_files/paper/2025/file/048445f5e3321dc9721930b15ba9387b-Paper-Conference.pdf
- Local PDF: pdf/2026-07-26_27_D-VST_ Diffusion Transformer for Pathology-Correct Tone-Controllable Cross-Dye Virtual Staining of Whole Slide Images.pdf

Diffusion-based virtual staining methods of histopathology images have demonstrated outstanding potential for stain normalization and cross-dye staining (e.g., hematoxylin-eosin to immunohistochemistry). However, achieving pathology-correct cross-dye virtual staining with versatile tone controls poses significant challenges due to the difficulty of decoupling the given pathology and tone conditions. This issue would cause non-pathologic regions to be mistakenly stained like pathologic ones, and vice versa, which we term “pathology leakage.” To address this issue, we propose diffusion virtual staining Transformer (D-VST), a new framework with versatile tone control for cross-dye virtual staining. Specifically, we introduce a pathology encoder in conjunction with a tone encoder, combined with a two-stage curriculum learning scheme that decouples pathology and tone conditions, to enable tone control while eliminating pathology leakage. Further, to extend our method for billion-pixel whole slide image (WSI) staining, we introduce a novel frequency-aware adaptive patch sampling strategy for high-quality yet efficient inference of ultra-high resolution images in a zero-shot manner. Integrating these two innovative components facilitates a pathology-correct, tone-controllable, cross-dye WSI virtual staining process. Extensive experiments on three virtual staining tasks that involve translating between four different dyes demonstrate the superiority of our approach in generating high-quality and pathologically accurate images compared to existing methods based on generative adversarial networks and diffusion models. Our code and trained models will be released.

## 28. ViLL-E: Video LLM Embeddings for Retrieval

- Authors: Rohit Gupta, Jayakrishnan Unnikrishnan, Fan Fei, Sheng Liu, Son Tran, Mubarak Shah
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.845409914410731
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.2003/
- PDF: https://aclanthology.org/2026.acl-long.2003.pdf
- Local PDF: pdf/2026-07-26_28_ViLL-E_ Video LLM Embeddings for Retrieval.pdf

Video Large Language Models (VideoLLMs) excel at video understanding tasks where outputs are textual, such as Video Question Answering and Video Captioning. However, they underperform specialized embedding-based models in Retrieval tasks, such as Text-toVideo Retrieval and Moment Retrieval. We introduce ViLL-E (Video-LLM-Embed), a unified VideoLLM architecture endowed with a novel embedding generation mechanism that allows the model to "think longer" for complex videos and stop early for easy ones. We train this model with a three-stage training methodology combining generative and contrastive learning: initial large-scale pre-training with video-caption pairs; followed by continual training on a smaller, detailed-caption dataset; and concluding with task-specific fine-tuning on a novel multi-task dataset covering Video QA, Temporal Localization, Video Retrieval, and Video-Text Matching. Our model significantly improves temporal localization (on avg. 7% over other VideoLLMs) and video retrieval (up to 4% over dual encoder models), achieving performance comparable to state-of-the-art specialized embedding models while remaining competitive on VideoQA tasks. Furthermore, our joint contrastive-generative training unlocks new zero-shot capabilities, significantly outperforming state-of-the-art methods in composed video retrieval (+5% over SotA) and retrieval from long text (+2% over SotA).

## 29. Diffuse Thinking: Exploring Diffusion Language Models as Efficient Thought Proposers for Reasoning

- Authors: Chenyang Shao, Sijian Ren, Fengli Xu, Yong Li
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.8453893237499415
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1231/
- PDF: https://aclanthology.org/2026.acl-long.1231.pdf
- Local PDF: pdf/2026-07-26_29_Diffuse Thinking_ Exploring Diffusion Language Models as Efficient Thought Proposers for Reasoning.pdf

Large language models (LLMs) have demonstrated strong capabilities in complex reasoning tasks, yet their autoregressive generation paradigm makes it computationally expensive to explore diverse reasoning paths. In contrast, diffusion language models (DLMs) adopt a parallel, non-autoregressive generation mechanism that enables the efficient production of diverse candidate outputs. Motivated by this complementarity, we explore a collaborative reasoning framework that combines diffusion-based generation with autoregressive evaluation. Specifically, we leverage DLMs to efficiently generate diverse intermediate reasoning thoughts, and employ LLMs as evaluators to assess and select candidates based on their plausibility and correctness. By decoupling proposal generation from evaluation, our framework exploits the strengths of both models: efficient exploration from diffusion models and causally grounded assessment from autoregressive models, which naturally aligns with the divergent-convergent thinking framework in cognitive psychology. Experiments across various mathematical and logical reasoning benchmarks demonstrate that our framework improves inference efficiency while maintaining competitive or superior reasoning accuracy, laying the groundwork for building efficient reasoning architectures. Our code is open-source at https://anonymous.4open.science/r/Diffuse-Thinking-EC60.

## 30. TopoDIM: One-shot Topology Generation of Diverse Interaction Modes for Multi-Agent Systems

- Authors: Rui Sun, Jie Ding, Chenghua Gong, Tianjun Gu, Yihang Jiang, Juyuan Zhang, Liming Pan, Linyuan Lü
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.8451043056176237
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.207/
- PDF: https://aclanthology.org/2026.findings-acl.207.pdf
- Local PDF: pdf/2026-07-26_30_TopoDIM_ One-shot Topology Generation of Diverse Interaction Modes for Multi-Agent Systems.pdf

Optimizing communication topology in LLM–based multi-agent system is critical for enabling collective intelligence. Existing methods mainly rely on spatio-temporal interaction paradigms, where the sequential execution of multi-round dialogues incurs high latency and computation. Motivated by the recent insights that evaluation and debate mechanisms can improve problem-solving in multi-agent systems, we propose TopoDIM, a framework for one-shot Topology generation with Diverse Interaction Modes. Designed for decentralized execution to enhance adaptability and privacy, TopoDIM enables agents to autonomously construct heterogeneous communication without iterative coordination, achieving token efficiency and improved task performance. Experiments demonstrate that TopoDIM reduces total token consumption by 46.41% while improving average performance by 1.50% over state-of-the-art methods. Moreover, the framework exhibits strong adaptability in organizing communication among heterogeneous agents. Code is available at: https://github.com/Sundiasy/TopoDIM.
