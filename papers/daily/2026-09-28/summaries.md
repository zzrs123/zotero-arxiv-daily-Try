# Paper Daily Reading - 2026-09-28

## 1. SCmapST enables single-cell spatial reconstruction by seeded matches-driven integration of single-cell and spatial transcriptomics

- Authors: Yi Liu, Pinglu Zhang, Ximei Luo, Quan Zou
- Source: openalex
- Venue type: journal
- Journal: Genome Medicine
- Publication status: published
- Publication date: 2026-09-23
- DOI: https://doi.org/10.1186/s13073-026-01778-9
- Categories: Single-cell and spatial transcriptomics, Extracellular vesicles in disease, Cancer Genomics and Diagnostics
- Relevance: 3.7749417428712007
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://doi.org/10.1186/s13073-026-01778-9
- PDF: Unavailable
- Local PDF: Not downloaded

Single cell (SC) RNA sequencing and spatial transcriptomics (ST) exhibit complementary limitations: they struggle to balance the cellular granularity inherent in SC data and the spatial coordinate unique to ST data. Here, we present SCmapST, a deep learning framework that leverages a novel seeded matches strategy to map single cells in SC data to spatial locations in ST data. SCmapST surpasses existing methods by consistently and robustly reconstructing global tissue topology while preserving local tissue heterogeneity. SCmapST successfully deciphers spatial co-localization patterns, resolves location-dependent neuronal heterogeneity, and delineates cell-type distributions within both discrete tumor domains and continuous liver zonation.

## 2. SpaCEy links spatial tissue patterns to clinical outcomes using explainable graph neural networks

- Authors: Ahmet Süreyya Rifaioğlu, Egle Helene Ervin, Ahmet Sarıgün, Deniz Germen, Bernd Bodenmiller, Jovan Tanevski, Julio Sáez-Rodríguez
- Source: openalex
- Venue type: journal
- Journal: Nature Communications
- Publication status: published
- Publication date: 2026-09-26
- DOI: https://doi.org/10.1038/s41467-026-77924-z
- Categories: Single-cell and spatial transcriptomics, Bioinformatics and Genomic Networks, Ferroptosis and cancer prognosis
- Relevance: 3.7198655900641873
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://doi.org/10.1038/s41467-026-77924-z
- PDF: Unavailable
- Local PDF: Not downloaded

Abstract Tissues are complex ecosystems organised in space, and alterations in this organisation underpin multiple diseases. Spatial omics enables molecular profiling of tissue organisation, but linking these patterns to clinical outcomes remains challenging. We present SpaCEy ( Spa tial C linical E xplainabilit y ), an explainable graph neural network that identifies tissue patterns predictive of clinical outcomes in spatial proteomics datasets. SpaCEy models tissues as spatial graphs from molecular marker expression, without using predefined cell-type labels or anatomical regions as model inputs. Its embeddings capture intercellular relationships and molecular dependencies for predicting overall survival and disease progression. An integrated explainer identifies recurring spatial patterns and coordinated marker expression relevant to model predictions. Applied to a spatial proteomic lung cancer cohort, SpaCEy identifies spatial and protein-expression patterns associated with disease progression. Across multiple breast cancer proteomic datasets, it stratifies patients by overall survival, both across and within established clinical subtypes, and highlights protein markers underlying this stratification.

## 3. DR-GEM enables self-supervised machine learning for single-cell embeddings and annotations

- Authors: Christine Y. Yeh, Min Sun, Livnat Jerby‐Arnon, Livnat Jerby
- Source: openalex
- Venue type: journal
- Journal: Nature Communications
- Publication status: published
- Publication date: 2026-09-24
- DOI: https://doi.org/10.1038/s41467-026-77908-z
- Categories: Single-cell and spatial transcriptomics, Cell Image Analysis Techniques, Domain Adaptation and Few-Shot Learning
- Relevance: 3.6510320415718334
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://doi.org/10.1038/s41467-026-77908-z
- PDF: Unavailable
- Local PDF: Not downloaded

Abstract Dimensionality reduction and clustering are instrumental to single-cell and spatial genomics data analysis. Here we show that existing methods tend to fit oversampled classes and miss more unique signals and patterns, such as rare cell types and states. We find that the problem in such cases is not primarily data scarcity per se, but the model equating abundance with importance. Addressing this, we present “Distributionally Robust and latent Group-AwarE consensus Machine learning” or DR-GEM, a self-supervised meta-algorithm that uses the reconstruction error to reorient the model attention to patterns it initially missed and applies balanced consensus learning to increase robustness and filter low-quality data. We apply DR-GEM to synthetic and real-world single-cell, spatial transcriptomics, and Perturb-seq datasets and demonstrate that it outperforms existing methods in obtaining reliable embeddings, recovering rare cell types, filtering noise, mitigating cell-level and patient-level underrepresentation, and uncovering held-out genetic and spatial features. We thus surface and address an underappreciated problem and present a self-supervised framework to help support AI-based and data-driven discoveries.

## 4. ResolVI: addressing noise and bias in spatial transcriptomics

- Authors: Can Ergen, Nir Yosef
- Source: openalex
- Venue type: journal
- Journal: Nature Methods
- Publication status: published
- Publication date: 2026-09-24
- DOI: https://doi.org/10.1038/s41592-026-03212-9
- Categories: Single-cell and spatial transcriptomics, Genomics and Chromatin Dynamics, RNA Research and Splicing
- Relevance: 3.443451915999046
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://doi.org/10.1038/s41592-026-03212-9
- PDF: Unavailable
- Local PDF: Not downloaded

Technologies for estimating RNA expression at high throughput, in intact tissue slices and with high spatial resolution (spatial transcriptomics) shed new light on how cells communicate and tissues function. A fundamental step in analyzing data generated by subcellular resolution spatial transcriptomics technologies is quantification, namely, segmenting the plane into regions, each approximating a cell, and then collating the molecules inside each region to estimate the cellular expression profile. Despite many advances in this area, a persistent problem is that of the incorrect assignment of molecules to cells, which limits many current applications to the level of a priori-defined cell subsets and complicates the discovery of novel cell states. Here we develop resolVI, a model that operates downstream of any segmentation algorithm to generate a probabilistic representation, correcting for the misassignment of molecules, as well as for batch effects and other nuisance factors. We demonstrate that resolVI improves our ability to distinguish between cell states, identify subtle expression changes in space and perform integrated analysis across datasets. ResolVI is available as open source software within scvi-tools.

## 5. Efficient differential expression analysis of large-scale single-cell transcriptomics data using Dreamlet

- Authors: Gabriel E. Hoffman, Donghoon Lee, Jaroslav M. Bendl, N. M. Prashant, Aram Hong, Clara Casey, Marcela Alvia, Zhiping Shao, Stathis Argyriou, Karen Therrien, Sanan Venkatesh, Georgios Voloudakis, Vahram H. Haroutunian, John F. Fullard, Panos Roussos
- Source: openalex
- Venue type: journal
- Journal: Nature Communications
- Publication status: published
- Publication date: 2026-09-23
- DOI: https://doi.org/10.1038/s41467-026-75680-8
- Categories: Single-cell and spatial transcriptomics, Gene expression and cancer classification, Health, Environment, Cognitive Aging
- Relevance: 3.0585279790141295
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://doi.org/10.1038/s41467-026-75680-8
- PDF: https://www.nature.com/articles/s41467-026-75680-8.pdf
- Local PDF: pdf/2026-09-28_05_Efficient differential expression analysis of large-scale single-cell transcriptomics data using Dreamlet.pdf

Advances in single-cell and -nucleus transcriptomics have enabled generation of increasingly large-scale datasets from hundreds of subjects and millions of cells. These studies promise to give unprecedented insight into the cell type specific biology of human disease. Yet performing differential expression analyses across subjects remains difficult due to challenges in statistical modeling of these complex studies and scaling analyses to large datasets. Our open-source R package dreamlet ( DiseaseNeurogenomics.github.io/dreamlet ) uses a pseudobulk approach based on precision-weighted linear mixed models to identify genes differentially expressed with traits across subjects for each cell cluster. Designed for data from large cohorts, dreamlet is substantially faster and uses less memory than existing workflows, while supporting complex statistical models and controlling the false positive rate. We demonstrate computational and statistical performance on published datasets, and a novel dataset of 1.4 M single nuclei from postmortem brains of 150 Alzheimer's disease cases and 149 controls.

## 6. Personalized single-cell transcriptomics reveals molecular diversity in Alzheimer’s disease

- Authors: Pramod Bharadwaj Chandrashekar, Sayali Anil Alatkar, Noah Cohen Kalafut, Ting Jin, Chirag Gupta, Ryan Conway Burczak, Huang Xiang, Shuang Liu, Athan Z. Li, Aram Hong, Biao Zeng, Chenfeng He, Christian Dillard, Christian Porras, Clara Casey, Colleen A. McClung, Collin Spencer, David Alan Bennett, David Burstein, Deepika Dayal Mathur, Fotios Tsetsos, Gennadi Ryan, Hui Yang, Jennifer Monteiro Fortes, Jerome J. Choi, Kalpana Hanthanan Arachchilage, Karen Therrien, Lars J. Jensen, Lisa L. Barnes, Logan C. Dumitrescu, Lyra Sheu, Madeline R. Scott, Marcela Alvia, Marios Anyfantakis, Maxim Signaevsky, Mikaela Koutrouli, Milos Pjanic, Monika Ahirwar, Nicolas Y. Masse, Pavan K. Auluck, Pavel Katsel, Pengfei Dong, Pramod B. Chandrashekar, N. M. Prashant, Rachel Bercovitch, Roman Kosoy, Sanan Venkatesh, Saniya Khullar, Sarah R. Murphy, Sayali Anil Alatkar, Seon Kinrot, Stathis Argyriou, Stefano Marenco, Steven M. Finkbeiner, Steven P. Kleopoulos, Tereza Clarence, Timothy J. Hohman, Vahram Haroutunian, Vivek G. Ramaswamy, Xinyi Wang, Zhenyi Wu, Zhiping Shao, Kiran Kumar Girdhar, Georgios Voloudakis, Gabriel E. Hoffman, Jaroslav M. Bendl, John F. Fullard, Donghoon Lee, Panos Roussos, Daifeng Wang
- Source: openalex
- Venue type: journal
- Journal: Nature Communications
- Publication status: published
- Publication date: 2026-09-23
- DOI: https://doi.org/10.1038/s41467-026-72310-1
- Categories: Single-cell and spatial transcriptomics, Ferroptosis and cancer prognosis, Bioinformatics and Genomic Networks
- Relevance: 3.0457860473376996
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://doi.org/10.1038/s41467-026-72310-1
- PDF: https://www.nature.com/articles/s41467-026-72310-1.pdf
- Local PDF: pdf/2026-09-28_06_Personalized single-cell transcriptomics reveals molecular diversity in Alzheimer’s disease.pdf

Alzheimer’s disease (AD) is highly heterogeneous and driven by diverse molecular and cellular mechanisms. Functional genomics investigates these mechanisms from genetic variants to gene expression and regulation. We performed personalized functional genomics analysis on population-scale single-nucleus RNA-seq data, with cross-cohort validation across multiple cohorts comprising over 1900 individual brains, capturing donor-level cell type interactions and gene regulatory networks. Using a knowledge-guided graph neural network, we learned latent representations of each donor’s functional genomics that accurately classified AD phenotypes, identified molecularly defined subpopulations, and traced disease progression trajectories. Our importance scores, derived from graph attentions, identified significant inter-donor differences and prioritized personalized cell type genes and regulatory networks. Finally, we identified gene regulatory QTLs (grQTLs) linking genetic variants to donor-level regulatory changes, providing insights into gene regulatory relationships beyond traditional eQTLs. All results are summarized into a personalized functional genomics atlas for AD, including an open-source framework, iBrainMap, for general use. Personalized functional genomics atlas for Alzheimer’s disease that uses knowledge-guided graph neural networks to analyze donor-level functional genomics, identify disease subpopulations and trajectories, and link genetic variants to gene regulation.

## 7. Fast, flexible analysis of differences in cellular composition with crumblr

- Authors: Gabriel E. Hoffman, Panos Roussos
- Source: openalex
- Venue type: journal
- Journal: Nature Communications
- Publication status: published
- Publication date: 2026-09-23
- DOI: https://doi.org/10.1038/s41467-026-75681-7
- Categories: Single-cell and spatial transcriptomics, Cancer Genomics and Diagnostics, Cancer Immunotherapy and Biomarkers
- Relevance: 2.780447547189304
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://doi.org/10.1038/s41467-026-75681-7
- PDF: Unavailable
- Local PDF: Not downloaded

Changes in cell type composition play an important role in human health and disease. Recent advances in single-cell technology have enabled the measurement of cell type composition at increasing cell lineage resolution across large cohorts of individuals. Yet this raises new challenges for statistical analysis of these compositional data to identify changes in cell type frequency. We introduce crumblr ( DiseaseNeurogenomics.github.io/crumblr ), a scalable statistical method for analyzing count ratio data using precision-weighted linear mixed models incorporating random effects for complex study designs. Uniquely, crumblr performs statistical testing at multiple levels of the cell lineage hierarchy using a multivariate approach to increase power over tests of one cell type. In simulations, crumblr increases power compared to existing methods while controlling the false positive rate. We demonstrate the application of crumblr to published single-cell RNA-seq datasets for aging, tuberculosis infection in T cells, bone metastases from prostate cancer, and SARS-CoV-2 infection.

## 8. UpTCR: a unified progressive knowledge transfer foundation model for robust T-cell receptor-antigen binding recognition

- Authors: Tianxu Lv, Yang Xiao, Li Chen, Bing He, Maiyi Zhong, Zihan Feng, Zheyu Hu, Fei Ye, Jiashu Han, Shouzhi Chen, Zhenchao Tang, Jiale Zhou, Dawei Huang, Xiaoqing Lian, Jiansong Fan, Yixuan Huang, Chenyi Lei, Dandan Meng, Yuan Liu, Lihua Li, Pengjiang Qian, Jianhua Yao, Kai Miao, Xiao Liu, Xiang Pan
- Source: openalex
- Venue type: journal
- Journal: Nature Communications
- Publication status: published
- Publication date: 2026-09-24
- DOI: https://doi.org/10.1038/s41467-026-78075-x
- Categories: vaccines and immunoinformatics approaches, T-cell and B-cell Immunology, Cancer Immunotherapy and Biomarkers
- Relevance: 2.755592655039246
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://doi.org/10.1038/s41467-026-78075-x
- PDF: https://www.nature.com/articles/s41467-026-78075-x_reference.pdf
- Local PDF: pdf/2026-09-28_08_UpTCR_ a unified progressive knowledge transfer foundation model for robust T-cell receptor-antigen binding recognition.pdf

Abstract T-cell receptor (TCR) recognition of antigenic peptides presented by human leukocyte antigen (HLA) molecules underpins adaptive immunity and T cell-based immunotherapy. However, the scarcity of complete interaction data and TCR cross-reactivity challenge robust prediction. Here, we present UpTCR, a unified progressive knowledge-transfer foundation model that learns from incomplete data to predict TCR-antigen-HLA binding. UpTCR progressively transfers knowledge from dimeric and trimeric interactions to tetrameric complexes and uses soft contrastive learning to mitigate false negatives. It outperforms existing methods in predicting TCR binding specificity and antigen-HLA binding affinity, particularly for neoantigens, and reveals pairwise residue-level interactions across the tetramer. UpTCR also transfers effectively to breast cancer cohorts with limited data. Prospective validation against melanoma antigen variants identifies eight immunogenic peptides that elicit T cell responses and one variant associated with immune escape. These findings establish UpTCR as a generalizable and interpretable tool for studying antigen recognition and advancing TCR-based immunotherapies.

## 9. AEGIS: A Holistic Benchmark for Evaluating Forensic Analysis of AI-Generated Academic Images

- Authors: Bo Zhang, Tzu-Yen Ma, Zichen Tang, Junpeng Ding, Zirui Wang, Yizhuo Zhao, Peilin Gao, Zijie Xi, Zixin Ding, Haiyang Sun, Haocheng Gao, Yuan Liu, Liangjia Wang, Yiling Huang, Yujie Wang, Yuyue Zhang, Ronghui Xi, Yuanze Li, Jiacheng Liu, Zhongjun Yang, Haihong E
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.6709494233313253
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.976/
- PDF: https://aclanthology.org/2026.acl-long.976.pdf
- Local PDF: pdf/2026-09-28_09_AEGIS_ A Holistic Benchmark for Evaluating Forensic Analysis of AI-Generated Academic Images.pdf

We introduce AEGIS, A holistic benchmark for Evaluating forensic analysis of AI-Generated academic ImageS. Compared to existing benchmarks, AEGIS features three key advances: (1) Domain-Specific Complexity: covering seven academic categories with 39 fine-grained subtypes, exposing intrinsic forensic difficulty, where even GPT-5.1 reaches 48.80% overall performance and expert models achieve only limited localization accuracy (IoU 30.09%); (2) Diverse Forgery Simulations: modeling four prevalent academic forgery strategies across 25 generative models, with 11 yielding average forensic accuracy below 50%, showing that forensics lag behind generative advances; and (3) Multi-Dimensional Forensic Evaluation: jointly assessing detection, reasoning, and localization, revealing complementary strengths between model families, with multimodal large language models (MLLMs) at 84.74% accuracy in textual artifact recognition and expert detectors peaking at 79.54% accuracy in binary authenticity detection. By evaluating 25 leading MLLMs, nine expert models, and one unified multimodal understanding and generation model, AEGIS serves as a diagnostic testbed exposing fundamental limitations in academic image forensics.

## 10. Towards Explainable Diagnosis: A Self-learned Explanatory Knowledge Base Approach

- Authors: Dongqi Huang, Tong Zhou, Zhuoran Jin, Shenghui Shi, Maoyujiao, Kang Liu, Jun Zhao, Yubo Chen
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.670582505887758
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1700/
- PDF: https://aclanthology.org/2026.acl-long.1700.pdf
- Local PDF: pdf/2026-09-28_10_Towards Explainable Diagnosis_ A Self-learned Explanatory Knowledge Base Approach.pdf

Explainable diagnosis requires that authoritative medical knowledge provide the rationales linking a patient’s clinical manifestations to the diagnostic conclusion. Although large language models (LLMs) hold great potential to facilitate explainable diagnosis, their effectiveness is often constrained by insufficient diagnostic expertise. To address this limitation, we propose Self-learned Explainable Knowledge Augmented Diagnosis (SEKAD), a unified LLM-based framework for faithful and explainable diagnosis. Our approach builds a high-quality diagnostic knowledge base through a record-driven explanation learning paradigm, as well as applies this knowledge via an explanation-based diagnostic process that ensures faithful inference. Experiments on the DiReCT and JAMA benchmarks show that SEKAD consistently outperforms strong baselines across the metrics. In particular, on the DiReCT benchmark, SEKAD improves the explanation completeness metric from 64.5% to 76.9% over the best existing methods, highlighting its effectiveness in enhancing diagnostic explainability and showing that our text mining approach produces knowledge that is both reliable in quality and large in quantity.

## 11. HAD: HAllucination Detection Language Models Based on a Comprehensive Hallucination Taxonomy

- Authors: Fan Xu, Xinyu Hu, Zhenghan Yu, Li Lin, Xu Zhang, Yang Zhang, Wei Zhou, Jinjie Gu, Xiaojun Wan
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.6702396620522464
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-industry.11/
- PDF: https://aclanthology.org/2026.acl-industry.11.pdf
- Local PDF: pdf/2026-09-28_11_HAD_ HAllucination Detection Language Models Based on a Comprehensive Hallucination Taxonomy.pdf

The increasing reliance on natural language generation (NLG) models, particularly large language models, has raised concerns about the reliability and accuracy of their outputs. A key challenge is hallucination, where models produce plausible but incorrect information. As a result, hallucination detection has become a critical task. In this work, we introduce a comprehensive hallucination taxonomy with 11 categories across various NLG tasks and propose the HAllucination Detection (HAD) models, which integrate hallucination detection, span-level identification, and correction into a single inference process. Trained on an elaborate synthetic dataset of about 90K samples, our HAD models are versatile and can be applied to various NLG tasks. We also carefully annotate a test set for hallucination detection, called HADTest, which contains 2,248 samples. Evaluations on in-domain and out-of-domain test sets show that our HAD models generally outperform the existing baselines, achieving state-of-the-art results on HaluEval, FactCHD, and FaithBench, confirming their robustness and versatility.

## 12. SpecExtend: A Drop-in Enhancement for Speculative Decoding of Long Sequences

- Authors: Jungyoub Cha, Hyunjong Kim, Sungzoon Cho
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.670186417036333
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.2153/
- PDF: https://aclanthology.org/2026.findings-acl.2153.pdf
- Local PDF: pdf/2026-09-28_12_SpecExtend_ A Drop-in Enhancement for Speculative Decoding of Long Sequences.pdf

Speculative decoding is a widely used technique for accelerating inference in large language models (LLMs), but its performance degrades as input length grows, with significant drops even at moderate lengths. Yet, this early degradation has remained largely underexplored. We introduce SpecExtend, a drop-in enhancement that improves speculative decoding on long sequences without additional training. SpecExtend integrates efficient attention mechanisms such as FlashAttention and Hybrid Tree Attention to accelerate prefill and verification steps. To improve both draft accuracy and speed on long inputs without retraining, we propose Cross-model Retrieval, a novel KV cache eviction strategy that leverages the target model’s attention scores to dynamically select relevant context for the smaller draft model. Extensive evaluations show that SpecExtend accelerates speculative decoding by up to 2.84× on 16K-token long document summarization and up to 3.86× on long-form reasoning, while preserving the short-input performance of state-of-the-art frameworks.

## 13. Data-Efficient Adaptation to Contextual Shifts in LLM-based Conversational Recommendation

- Authors: Hyeongjun Yang, Donghyun Kim, Seokju Hwang, Midan Shim, KyuHwan Yeom, KaeHyun Um, Kyong-Ho Lee
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.669621377909147
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1114/
- PDF: https://aclanthology.org/2026.findings-acl.1114.pdf
- Local PDF: pdf/2026-09-28_13_Data-Efficient Adaptation to Contextual Shifts in LLM-based Conversational Recommendation.pdf

Large language model (LLM)-based conversational recommender systems (CRSs) have demonstrated strong capabilities in capturing user preferences and generating contextually relevant recommendations. Nevertheless, the recommendation quality of the models frozen after training inevitably degrades under contextual shifts, such as changes in language and social trends. While periodic model updates are essential to maintain alignment with real-world preferences, training on large-scale data incurs substantial costs. This motivates data-efficient adaptation. However, existing data selection methods struggle to distinguish learnable samples under contextual shifts. To address this, we propose Contextual Shift-Adaptive Data Pruning and Training (CAPT), a framework agnostic to underlying LLM-based CRSs. Specifically, we conceptualize a three-class data taxonomy comprising familiar, valuable, and outlier samples to formalize data behavior under contextual shifts. Based on this taxonomy, we design an importance score estimation scheme that quantifies a sample’s relative learnability for shift adaptation. Leveraging these importance scores, CAPT prioritizes highly learnable samples and further guides shift-adaptive training to actively steer the model toward evolving preferences. Experiments on three CRS benchmarks with real-world temporal splits demonstrate that CAPT outperforms baselines, matching or surpassing full-data fine-tuning performance using only 10-50% of the training data.

## 14. AdaptEvolve: Improving Efficiency of Evolutionary AI Agents through Adaptive Model Selection

- Authors: Pretam Ray, Pratik Prabhanjan Brahma, Zicheng Liu, Emad Barsoum
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.669261032555406
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.2019/
- PDF: https://aclanthology.org/2026.findings-acl.2019.pdf
- Local PDF: pdf/2026-09-28_14_AdaptEvolve_ Improving Efficiency of Evolutionary AI Agents through Adaptive Model Selection.pdf

Evolutionary agentic systems intensify the trade-off between computational efficiency and reasoning capability by repeatedly invoking large language models (LLMs) during inference. This setting raises a central question: how can an agent dynamically select an LLM that is sufficiently capable for the current generation step while remaining computationally efficient? While model cascades offer a practical mechanism for balancing this trade-off, existing routing strategies typically rely on static heuristics or external controllers and do not explicitly account for model uncertainty. We introduce AdaptEvolve: Adaptive LLM Selection for Multi-LLM Evolutionary Refinement within an evolutionary sequential refinement framework that leverages intrinsic generation confidence to estimate real-time solvability. Empirical results show that confidence-driven selection yields a favorable Pareto frontier, reducing total inference cost by an average of 37.9% across benchmarks while retaining 97.5% of the upper-bound accuracy of static large-model baselines.

## 15. MM-JudgeBias: A Benchmark for Evaluating Compositional Biases in MLLM-as-a-Judge

- Authors: Sua Lee, Sanghee Park, Jinbae Im
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.668942355440321
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1162/
- PDF: https://aclanthology.org/2026.acl-long.1162.pdf
- Local PDF: pdf/2026-09-28_15_MM-JudgeBias_ A Benchmark for Evaluating Compositional Biases in MLLM-as-a-Judge.pdf

Multimodal Large Language Models (MLLMs) have been increasingly used as automatic evaluators—a paradigm known as MLLM-as-a-Judge . However, their reliability and vulnerabilities to biases remain underexplored. We find that many MLLM judges fail to reliably integrate key visual or textual cues, yielding unreliable evaluations when evidence is missing or mismatched, and exhibiting instability under semantically irrelevant perturbations. To address this, we systematically define Compositional Bias in MLLM-as-a-Judge systems and introduce MM-JudgeBias , a benchmark for evaluating it. MM-JudgeBias introduces controlled perturbations across Query, Image, and Response, and evaluates model behavior via two complementary metrics: Bias-Deviation (BD) for sensitivity and Bias-Conformity (BC) for stability. Our dataset of over 1,800 curated and refined multimodal samples, drawn from 29 source benchmarks, enables a fine-grained diagnosis of nine bias types across diverse tasks and domains. Experiments on 26 state-of-the-art MLLMs reveal systematic modality neglect and asymmetric evaluation tendencies, underscoring the need for more reliable judges.

## 16. Do LLMs Encode Functional Importance of Reasoning Tokens ?

- Authors: Janvijay Singh, Dilek Hakkani-Tür
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.6682251418450176
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1419/
- PDF: https://aclanthology.org/2026.acl-long.1419.pdf
- Local PDF: pdf/2026-09-28_16_Do LLMs Encode Functional Importance of Reasoning Tokens.pdf

Large language models solve complex tasks by generating long reasoning chains, achieving higher accuracy at the cost of increased computational cost and reduced ability to isolate functionally relevant reasoning. Prior work on compact reasoning shortens such chains through probabilistic sampling, heuristics, or supervision from frontier models, but offers limited insight into whether models internally encode token-level functional importance for answer generation. We address this gap diagnostically and propose greedy pruning, a likelihood-preserving deletion procedure that iteratively removes reasoning tokens whose removal minimally degrades model likelihood under a specified objective, yielding length-controlled reasoning chains. We evaluate pruned reasoning in a distillation framework and show that students trained on pruned chains outperform a frontier-model–supervised compression baseline at matched reasoning lengths. Finally, our analysis reveals systematic pruning patterns and shows that attention scores can predict greedy pruning ranks, further suggesting that models encode a nontrivial functional importance structure over reasoning tokens.

## 17. Revisiting the Uniform Information Density Hypothesis in LLM Reasoning

- Authors: Minju Gwak, Guijin Son, Jaehyung Kim
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.6681680494850384
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1565/
- PDF: https://aclanthology.org/2026.findings-acl.1565.pdf
- Local PDF: pdf/2026-09-28_17_Revisiting the Uniform Information Density Hypothesis in LLM Reasoning.pdf

The Uniform Information Density (UID) hypothesis proposes that effective communication is achieved by maintaining a stable flow of information. In this work, we revisit this principle in the context of Large Language Model (LLM) reasoning, asking whether step-level uniformity reflects reasoning quality. To this end, we introduce a novel framework to quantify uniformity of information flow at both local and global levels, using an entropy-based stepwise density metric. Across experiments on seven reasoning benchmarks, we see a counter-intuitive pattern: while high-quality reasoning exhibit smooth step-by-step transitions (local uniformity) and structured, non-uniform information flow at the trajectory level (global non-uniformity). The results demonstrate that these uniformities outperform alternative internal signals as predictors of reasoning quality, and such divergence with human communication is not a model deficiency, but a byproduct of distinct objectives between human communication and LLM reasoning.

## 18. Selective Steering: Norm-Preserving Control Through Discriminative Layer Selection

- Authors: Quy-Anh Dang, Chris Ngo
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.6680192588943963
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.529/
- PDF: https://aclanthology.org/2026.findings-acl.529.pdf
- Local PDF: pdf/2026-09-28_18_Selective Steering_ Norm-Preserving Control Through Discriminative Layer Selection.pdf

Despite significant progress in alignment, large language models (LLMs) remain vulnerable to adversarial attacks that elicit harmful behaviors. Activation steering techniques offer a promising inference-time intervention approach, but existing methods suffer from critical limitations: activation addition requires careful coefficient tuning and is sensitive to layer-specific norm variations, while directional ablation provides only binary control. Recent work on Angular Steering introduces continuous control via rotation in a 2D subspace, but its practical implementation violates norm preservation, causing distribution shift and generation collapse, particularly in models below 7B parameters. We propose Selective Steering , which addresses these limitations through two key innovations: (1) a mathematically rigorous norm-preserving rotation formulation that maintains activation distribution integrity, and (2) discriminative layer selection that applies steering only where feature representations exhibit opposite-signed class alignment. Experiments across nine models demonstrate that Selective Steering achieves 5.5 higher attack success rates than prior methods while maintaining zero perplexity violations and approximately 100% capability retention on standard benchmarks. Our approach provides a principled, efficient framework for controllable and stable LLM behavior modification.

## 19. Evaluating Visual Narrative Coherence in Story Visualization via Diversified Storylines

- Authors: Minha Jhang, Kyeongman Park, Hyukhun Koh, Kyomin Jung
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.667985731475299
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1578/
- PDF: https://aclanthology.org/2026.acl-long.1578.pdf
- Local PDF: pdf/2026-09-28_19_Evaluating Visual Narrative Coherence in Story Visualization via Diversified Storylines.pdf

Story visualization requires generating a coherent sequence of images that collectively form a narrative, yet existing evaluation metrics and datasets often overlook visual continuity and narrative diversity. In this paper, we introduce the Visual Context-Aware Metric for Story Visualization, which uses large vision-language models to jointly assess caption fidelity and inter-image consistency, achieving Spearman’s correlation comparable to human agreement on two benchmarks. Also, to address the shortcomings of narrowly defined datasets with low diversity, we propose a diffusion-augmented evaluation pipeline that blends diverse and controlled narrative elements at adjustable ratios, producing challenging evaluation sets. By combining VCMS with this pipeline, we provide a scalable, human-aligned framework for evaluating story visualization models.

## 20. ProRank: Prompt Warmup via Reinforcement Learning for Small Language Models Reranking

- Authors: Xianming LI, Aamir Shakir, Rui Huang, Julius Lipp, Benjamin Clavié, Jing Li
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.667349368908536
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.51/
- PDF: https://aclanthology.org/2026.findings-acl.51.pdf
- Local PDF: pdf/2026-09-28_20_ProRank_ Prompt Warmup via Reinforcement Learning for Small Language Models Reranking.pdf

Reranking is fundamental to information retrieval and retrieval-augmented generation, with recent Large Language Models (LLMs) significantly advancing reranking quality. Most current works rely on large-scale LLMs (>7B parameters), presenting high computational costs. Small Language Models (SLMs) offer a promising alternative because of computational efficiency. However, our preliminary quantitative analysis reveals key limitations of SLMs: their representation space is narrow, leading to reduced expressiveness, and they struggle with understanding task prompts without fine-tuning. To address these issues, we introduce a novel two-stage training approach, ProRank , for SLM-based document reranking. We propose using reinforcement learning to improve the understanding of task prompts. Additionally, we introduce fine-grained score learning to enhance representation expressiveness and further improve document reranking quality. Extensive experiments suggest that ProRank consistently outperforms both the most advanced open-source and proprietary reranking models. Notably, our ProRank even surpasses powerful LLM reranking models on the BEIR benchmark, establishing that properly trained SLMs can achieve superior document reranking performance while maintaining computational efficiency.

## 21. Thermometer of Thoughts: Enhancing LLM’s Exploration via Attention Temperature Modulation

- Authors: Zhiyuan Yu, Shijian Xiao, Cam-Tu Nguyen, Zhangyue Yin, Lekai Xing, Wenzhong Li, Sanglu Lu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.66684873337913
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.200/
- PDF: https://aclanthology.org/2026.acl-long.200.pdf
- Local PDF: pdf/2026-09-28_21_Thermometer of Thoughts_ Enhancing LLM’s Exploration via Attention Temperature Modulation.pdf

Improving the exploration of reasoning is essential for advancing Large Language Models’ (LLMs) problem-solving performance. Current methods primarily rely on output-level stochasticity, which decode within fixed reasoning patterns of LLM and suffer from insufficient exploration. In this paper, we introduce adjusting attention temperature to directly modulate the model’s internal focus during reasoning, which enables a dynamic shift between exploratory and focused processing. We reveal that moderate adjustments preserve LLM’s reasoning capability while producing problem hardness-dependent benefits: higher temperatures facilitate solving complex tasks by encouraging wider exploration, whereas lower temperatures mitigate overthinking on simpler problems. Leveraging this insight, we propose a two-stage inference strategy: first, attention temperature scaling modulates the LLM’s reasoning patterns to diversify the reasoning traces; then, a difficulty-aware aggregation scheme is introduced to effectively identify the most reliable solution from the generated candidates. Extensive evaluations show that our method improves Pass@10 by 6.78–14.20% and aggregation accuracy by 9.74% across 7 reasoning benchmarks.

## 22. Augur: Modeling Covariate Causal Associations in Time Series via Large Language Models

- Authors: Zhiqing Cui, Binwu Wang, Qingxiang Liu, Yeqiang Wang, Zhengyang Zhou, Yuxuan Liang, Yang Wang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.6667973160511007
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.32/
- PDF: https://aclanthology.org/2026.acl-long.32.pdf
- Local PDF: pdf/2026-09-28_22_Augur_ Modeling Covariate Causal Associations in Time Series via Large Language Models.pdf

Large language models (LLM) have emerged as a promising avenue for time series forecasting, offering the potential to integrate multimodal data. However, existing LLM-based approaches face notable limitations—such as marginalized role in model architectures, reliance on coarse statistical text prompts, and lack of interpretability. In this work, we introduce Augur, a fully LLM driven time series forecasting framework that exploits LLM causal reasoning to discover and use directed causal associations among covariates. Augur uses a two stage teacher student architecture where a powerful teacher LLM infers a directed causal graph from time series using heuristic search together with pairwise causality testing. A lightweight student agent then refines the graph and fine tune on high confidence causal associations that are encoded as rich textual prompts to perform forecasting. This design improves predictive accuracy while yielding transparent, traceable reasoning about variable interactions. Extensive experiments on real-world datasets with 25 baselines demonstrate that Augur achieves competitive performance and robust zero-shot generalization.

## 23. Beyond Examples: Towards Automated Thought-level In-Context Reasoning for Large Language Models

- Authors: Jinyang Wu, Mingkuan Feng, Shuai Zhang, Feihu Che, Zhengqi Wen, Chonghua Liao, Ling Yang, Haoran Luo, Zheng Lian, Jianhua Tao
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.666218626769159
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.135/
- PDF: https://aclanthology.org/2026.acl-long.135.pdf
- Local PDF: pdf/2026-09-28_23_Beyond Examples_ Towards Automated Thought-level In-Context Reasoning for Large Language Models.pdf

In-context learning (ICL) leverages demonstrations to enhance the performance of large language models (LLMs). However, traditional ICL struggles with complex reasoning mainly due to superficial, example-level implicit imitation. To address these limitations, we introduce ThoughtICR , an automated Thought -level I n- C ontext R easoning paradigm that shifts from surface-level examples to more guidance-oriented thought patterns. Specifically, we first define atomic reasoning actions and construct thought patterns on small-scale seed data using Monte Carlo Tree Search (MCTS). During inference, we dynamically select appropriate thought patterns based on target problem attributes, providing explicit guidance for model reasoning. Thanks to its automated and strategic design, our method enables seamless plug-and-play integration with various post-training techniques. Experimental results demonstrate that our method improves performance across different model sizes and generalizes effectively across reasoning domains. Using only small-scale seed data, we achieve 80.6% accuracy on MATH and 62.5% on AMC, surpassing GPT-4o’s 77.2% and 57.5%, respectively. Moreover, compared to test-time scaling methods, our approach reduces computational costs by over 10. Our code is available at https://github.com/jinyangwu/ThoughtICR .

## 24. Seek-and-Solve: Benchmarking MLLMs for Visual Clue-Driven Reasoning in Daily Scenarios

- Authors: Xiaomin Li, Tala Wang, Zichen Zhong, Ying Zhang, Zirui Zheng, Takashi Isobe, Dezhuang Li, Huchuan Lu, You He, Xu Jia
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.6657994193447463
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.760/
- PDF: https://aclanthology.org/2026.findings-acl.760.pdf
- Local PDF: pdf/2026-09-28_24_Seek-and-Solve_ Benchmarking MLLMs for Visual Clue-Driven Reasoning in Daily Scenarios.pdf

Daily scenarios are characterized by visual richness, requiring Multimodal Large Language Models (MLLMs) to filter noise and identify decisive visual clues for accurate reasoning. Yet, current benchmarks predominantly aim at evaluating MLLMs’ pre-existing knowledge or perceptual understanding, often neglecting the critical capability of reasoning. To bridge this gap, we introduce DailyClue, a benchmark designed for visual clue-driven reasoning in daily scenarios. Our construction is guided by two core principles: (1) strict grounding in authentic daily activities, and (2) challenging query design that necessitates more than surface-level perception. Instead of simple recognition, our questions compel MLLMs to actively explore suitable visual clues and leverage them for subsequent reasoning. To this end, we curate a comprehensive dataset spanning four major daily domains and 16 distinct subtasks. Comprehensive evaluation across MLLMs and agentic models underscores the formidable challenge posed by our benchmark. Our analysis reveals several critical insights, emphasizing that the accurate identification of visual clues is essential for robust reasoning.

## 25. How Context Shapes Truth: Geometric Transformations of Statement-level Truth Representations in LLMs

- Authors: Shivam Adarsh, Maria Maistro, Christina Lioma
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.6651807929857
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1695/
- PDF: https://aclanthology.org/2026.acl-long.1695.pdf
- Local PDF: pdf/2026-09-28_25_How Context Shapes Truth_ Geometric Transformations of Statement-level Truth Representations in LLMs.pdf

Large Language Models (LLMs) often encode whether a statement is true as a vector in their residual stream activations. These vectors, also known as truth vectors, have been studied in prior work, however how they change when context is introduced remains unexplored. We study this question by measuring (1) the directional change ( 𝜃 ) between the truth vectors with and without context and (2) the relative magnitude of the truth vectors upon adding context. Across four LLMs and four datasets, we find that (1) truth vectors are roughly orthogonal in early layers, converge in middle layers, and may stabilize or continue increasing in later layers; (2) adding context generally increases the truth vector magnitude, i.e., the separation between true and false representations in the activation space is amplified; (3) larger models distinguish relevant from irrelevant context mainly through directional change ( 𝜃 ), while smaller models show this distinction through magnitude differences. We also find that context conflicting with parametric knowledge produces larger geometric changes than parametrically aligned context. Collectively, these findings provide a geometric characterization of how context transforms the truth vector in the activation space of LLMs.

## 26. RShield: A User-level Traceable Backdoor Watermark for LLMs in Embedding-as-a-Service

- Authors: Lingyun Xiang, Yufan Zhong, Chengfu Ou, Zhihua Xia, Chunfang Yang, Daojian Zeng, Zhangjie Fu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.6648143845034373
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1347/
- PDF: https://aclanthology.org/2026.findings-acl.1347.pdf
- Local PDF: pdf/2026-09-28_26_RShield_ A User-level Traceable Backdoor Watermark for LLMs in Embedding-as-a-Service.pdf

Embedding-as-a-Service (EaaS) has emerged as a critical paradigm for commercializing large language models (LLMs). However, existing backdoor watermarking techniques are fundamentally limited to “zero-bit” detection, which prevents user-level traceability in multi-user EaaS scenarios. To address these limitations, we propose RShield, a multi-bit backdoor watermarking that enables reliable user-level attribution of LLMs for EaaS under model extraction attacks. RShield integrates Reed-Solomon error-correcting codes with orthogonal feature mapping to introduce highly-structured redundancy, constructing fault-tolerant symbol sequences for multi-bit watermark space, thereby staying recoverable even after aggressive extraction noise condition.To mitigate semantic distortion under the interference of noise channel, RShield employs a lightweight Adapter to adaptively inject multi-bit watermarks in the feature space, preserving the quality of EaaS while achieving a user-level traceability.Extensive experiments on four NLP benchmarks demonstrate that RShield efficiently achieves 100% multi-bit watermark recovery and high semantic fidelity under model extraction attacks compared to existing methods, while significantly reducing the degradation of watermarking on downstream task performance.

## 27. Silencing the Guardrails: Inference-Time Jailbreaking via Dynamic Contextual Representation Ablation

- Authors: Wenpeng Xing, Moran Fang, Guangtai Wang, Changting Lin, Meng Han
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.6646027056845507
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.211/
- PDF: https://aclanthology.org/2026.findings-acl.211.pdf
- Local PDF: pdf/2026-09-28_27_Silencing the Guardrails_ Inference-Time Jailbreaking via Dynamic Contextual Representation Ablation.pdf

While Large Language Models (LLMs) have achieved remarkable performance, they remain vulnerable to jailbreak attacks that circumvent safety constraints. Existing strategies, ranging from heuristic prompt engineering to computationally intensive optimization, often face significant trade-offs between effectiveness and efficiency. In this work, we propose Contextual Representation Ablation (CRA), a novel inference-time intervention framework designed to dynamically silence model guardrails. Predicated on the geometric insight that refusal behaviors are mediated by specific low-rank subspaces within the model’s hidden states, CRA identifies and suppresses these refusal-inducing activation patterns during decoding without requiring expensive parameter updates or training. Empirical evaluation across multiple safety-aligned open-source LLMs demonstrates that CRA significantly outperforms baselines. By revealing that safety constraints can be surgically ablated from internal representations, our findings expose the intrinsic fragility of current alignment mechanisms and underscore the urgent need for more robust latent-space defenses.

## 28. TwiUSD: A Benchmark Dataset and Structure-Aware LLM Framework for User Stance Detection

- Authors: Fuqiang Niu, Zini Chen, Zhiyu Xie, Hu Huang, Qing Liao, Qianlong Wang, Genan Dai, Bowen Zhang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.6636071189896073
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.2095/
- PDF: https://aclanthology.org/2026.acl-long.2095.pdf
- Local PDF: pdf/2026-09-28_28_TwiUSD_ A Benchmark Dataset and Structure-Aware LLM Framework for User Stance Detection.pdf

Political user-level stance detection is vital for analyzing polarization, yet progress is hindered by the scarcity of high-quality benchmarks integrating linguistic and social signals. Existing datasets, largely relying on noisy heuristic or distant supervision, limit model robustness and generalizability. To address this, we introduce TwiUSD, a large-scale, expert-annotated benchmark for political user-level stance detection with explicit social network structure. TwiUSD comprises 16,211 users and 47,757 tweets, labeled by domain experts using a protocol that integrates both user content and followee signals, ensuring high-quality annotations (kappa > 0.9). Building upon TwiUSD, we propose MRFG, a Multi-scale Relevance Filtering and Graph-aware framework that leverages large language models to filter stance-relevant followee content and adaptively routes features based on structural informativeness. This design enables robust stance prediction by jointly modeling semantic and relational cues. Extensive experiments show that MRFG significantly outperforms strong baselines, highlighting the importance of relevance filtering and structure-aware modeling.

## 29. Rectified Sparse Attention for Efficient Long-Sequence Generation

- Authors: Yutao Sun, Tianzhu Ye, Li Dong, Yuqing Xia, Jian Chen, Yizhao Gao, Shijie Cao, Jianyong Wang, Furu Wei
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.6635381969793928
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.348/
- PDF: https://aclanthology.org/2026.findings-acl.348.pdf
- Local PDF: pdf/2026-09-28_29_Rectified Sparse Attention for Efficient Long-Sequence Generation.pdf

Efficient long-sequence generation is a critical challenge for Large Language Models. While recent sparse decoding methods improve efficiency, they suffer from KV cache misalignment, where approximation errors accumulate and degrade generation quality. In this work, we propose Rectified Sparse Attention (ReSA), a simple yet effective method that combines block-sparse attention with periodic dense rectification. By refreshing the KV cache at fixed intervals using a dense forward pass, ReSA bounds error accumulation and preserves alignment with the pretraining distribution. Experiments across math reasoning, language modeling, and retrieval tasks demonstrate that ReSA achieves near-lossless generation quality with significantly improved efficiency. Notably, ReSA delivers up to 3.77x end-to-end speedup under decoding at 256K sequence length, making it a practical solution for scalable long-context inference.

## 30. LitVISTA: A Benchmark for Narrative Orchestration in Literary Text

- Authors: Mingzhe Lu, Yiwen Wang, Yanbing Liu, Qi You, Chong Liu, Ruize Qin, Haoyu Dong, Wenyu Zhang, JiaRui Zhang, Yue Hu, Yunpeng Li
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.663476705115487
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1024/
- PDF: https://aclanthology.org/2026.acl-long.1024.pdf
- Local PDF: pdf/2026-09-28_30_LitVISTA_ A Benchmark for Narrative Orchestration in Literary Text.pdf

Computational narrative analysis aims to capture rhythm, tension, and emotional dynamics in literary texts. Existing large language models can generate long stories but overly focus on causal coherence, neglecting the complex story arcs and orchestration inherent in human narratives. This suggests a structural misalignment between model- and human-generated narratives.We therefore position narrative analysis as a diagnostic proxy for generation and propose VISTA Space, a high-dimensional framework for narrative orchestration that unifies human and model perspectives while jointly characterizing narrative function and structure in a common space.We further introduce LitVISTA, a structurally annotated benchmark grounded in literary texts, which operationalizes VISTA Space for systematic evaluation of models’ narrative orchestration capabilities. Under an oracle setting with gold event anchors, we evaluate frontier LLMs including GPT, Claude, Grok, and Gemini. Results reveal systematic deficiencies, as current models struggle to jointly capture narrative function and structure and fail to form an integrated global view of literary narrative orchestration. End-to-end analysis further shows that failures are dominated by anchor identification and localization errors. Even advanced thinking modes yield mixed and often limited gains for literary narrative understanding.
