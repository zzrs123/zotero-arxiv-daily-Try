# Paper Daily Reading - 2026-11-01

## 1. CellPatch: a flexible and efficient framework for single-cell foundation models empowered by heuristic gene patching

- Authors: Hanwen Zhu, Yushun Yuan, Jiyuan Yang, Kangwen Cai, Nana Wei, Senxin Zhang, Lu Wang, Wen-Jie Jiang, Sun Yuanchen, An Liu, Futing Lai, Yujuan Wang, Zeyu Ma, Xiaoqi Zheng, Hua-Jun Wu
- Source: openalex
- Venue type: journal
- Journal: Genome biology
- Publication status: published
- Publication date: 2026-10-30
- DOI: https://doi.org/10.1186/s13059-026-04329-y
- Categories: Single-cell and spatial transcriptomics, Gene expression and cancer classification, Bioinformatics and Genomic Networks
- Relevance: 3.757944758054037
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://doi.org/10.1186/s13059-026-04329-y
- PDF: Unavailable
- Local PDF: Not downloaded

Abstract Foundation models have advanced single-cell omics analysis but often remain too complex for practical use. We present CellPatch, a lightweight foundation model combining cross-attention with heuristic gene patching to reduce computational complexity during pretraining and fine-tuning while enabling inspection of gene-attention patterns. Across single-cell RNA-sequencing datasets spanning multiple organs and tissue states, CellPatch achieves state-of-the-art performance on diverse prediction tasks. Its modular design supports linear, adapter-based and task-specific architectures, enabling CellPatch to be adapted to diverse biological tasks.

## 2. SpaCut: Transcript‐Aware Morphology Fusion for Robust Cell Segmentation in Subcellular Spatial Transcriptomics

- Authors: Yongheng Li, Fangfang Zhu, Wenwen Min
- Source: openalex
- Venue type: journal
- Journal: Advanced Science
- Publication status: published
- Publication date: 2026-10-29
- DOI: https://doi.org/10.1002/advs.78423
- Categories: Single-cell and spatial transcriptomics, Cell Image Analysis Techniques, Medical Image Segmentation Techniques
- Relevance: 3.5211819993998565
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://doi.org/10.1002/advs.78423
- PDF: https://onlinelibrary.wiley.com/doi/pdfdirect/10.1002/advs.78423
- Local PDF: Not downloaded

Subcellular Spatial Transcriptomics (SST) offers unprecedented opportunities to decipher tissue architecture at subcellular resolution. Consequently, accurate cell segmentation is a fundamental prerequisite for analyzing SST data, as precise transcript assignment is essential for downstream single-cell interpretation. Existing methods often overlook the spatial organization of transcripts, rely on simplified geometric priors, or struggle to coordinate transcript-derived features with morphology-derived spatial guidance. This limitation restricts their adaptability to irregular cell shapes, often leading to transcript misassignment. To address this, we propose SpaCut, a unified deep learning framework designed to effectively integrate transcriptomic feature learning with dynamic morphological guidance. SpaCut comprises a Gene-Wise Attention (GWA) module and a Nuclei-Guided Attentive Fusion (NGAF) module. GWA encodes the high-dimensional transcript map and aggregates features across multiple depths. NGAF uses the encoded transcript features to modulate distance-based nuclear softmasks and refine nucleus-anchored cell boundaries through progressive training. Extensive evaluations across seven datasets from diverse platforms (including Xenium, CosMx, MERSCOPE, and Stereo-seq) demonstrate that SpaCut significantly outperforms state-of-the-art methods in both segmentation accuracy and consistency with single-cell reference data. The source code is available at https://github.com/wenwenmin/SpaCut.

## 3. IDPForge: deep learning of proteins with global and local regions of disorder

- Authors: Stefano De Castro, Oufan Zhang, Zi Hao Liu, Julie Deborah Forman-Kay, Teresa L. Head-Gordon
- Source: openalex
- Venue type: journal
- Journal: Nature Communications
- Publication status: published
- Publication date: 2026-10-30
- DOI: https://doi.org/10.1038/s41467-026-79191-4
- Categories: Protein Structure and Dynamics, Machine Learning in Bioinformatics, Enzyme Structure and Function
- Relevance: 2.839945159955206
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://doi.org/10.1038/s41467-026-79191-4
- PDF: Unavailable
- Local PDF: Not downloaded

Abstract Although machine learning has transformed protein structure prediction of folded protein ground states with remarkable accuracy, intrinsically disordered proteins and regions (IDPs/IDRs) are defined by diverse and dynamical structural ensembles that are predicted with low confidence by algorithms such as AlphaFold and RoseTTAFold. We present a machine learning method, IDPForge ( I ntrinsically D isordered P rotein, FO lded and disordered R egion GE nerator), that exploits a transformer protein language diffusion model to create all-atom IDP ensembles and IDR ensembles that maintains the folded domains. IDPForge does not require sequence-specific training, back transformations from coarse-grained representations, nor ensemble reweighting. The created IDP/IDR conformational ensembles show good agreement with both NMR and SAXS solution experimental data, and options for biasing with experimental restraints are available if desired. IDPForge with these diverse capabilities facilitates integrative and structural studies for proteins that contain intrinsic disorder, and is available as an open source resource for general use.

## 4. Foundation model for particle collision data analysis

- Authors: Ting-Hsiang Hsu, Bai-Hong Zhou, Qibin Liu, Yue Xu, Shu Li, George Wei-Shu Hou, Benjamin Nachman, Shih-Chieh Hsu, Vinicius Mikuni, Yuan-Tang Chou, Yulei Zhang
- Source: openalex
- Venue type: journal
- Journal: Nature Machine Intelligence
- Publication status: published
- Publication date: 2026-10-29
- DOI: https://doi.org/10.1038/s42256-026-01322-9
- Categories: Particle physics theoretical and experimental studies, High-Energy Particle Collisions Research, Particle Detector Development and Performance
- Relevance: 2.771189678774006
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://doi.org/10.1038/s42256-026-01322-9
- PDF: https://www.nature.com/articles/s42256-026-01322-9.pdf
- Local PDF: pdf/2026-11-01_04_Foundation model for particle collision data analysis.pdf

Abstract Data-intensive collider experiments increasingly require models that transfer across high-dimensional, partially observed measurements, yet most analyses still optimize separate models for each task. Here, to address this bottleneck, we introduce EVENET, an event-level foundation model pretrained on 500 million simulated collision events using self-supervised learning and physics-informed supervision. The model constructs a shared particle-cloud representation from the variable-length set of physics objects in each event. Across searches for heavy resonances and exotic Higgs decays, EVENET outperforms both established and state-of-the-art baselines, particularly in low-statistics regimes. We validate transfer to experimental data by rediscovering the ϒ meson in CMS Open Data. The pretrained model also supports precise extraction of quantum-correlation observables that remain stable under the tested systematic variations. Together, these results establish a reusable backbone for diverse collider analyses, improving downstream adaptation after a substantial one-time pretraining investment.

## 5. Decoder-FFPE-seq enables sensitive, genome-wide spatial transcriptomics of archival tissues at single-cell resolution

- Authors: Jiao Cao, Jun Zeng, Yiwei Meng, Shanqing Huang, Jing Zhang, Xing Fang, Yang Guo, Weixiong Shi, Yutong Liu, Zhong Zheng, Jian Chen Fang, Xuepeng Xiong, Gang Chen, Lingling Wu, Chaoyong James Yang
- Source: openalex
- Venue type: journal
- Journal: Science Advances
- Publication status: published
- Publication date: 2026-10-30
- DOI: https://doi.org/10.1126/sciadv.ady5085
- Categories: Single-cell and spatial transcriptomics, Molecular Biology Techniques and Applications, Biotin and Related Studies
- Relevance: 2.722480405987591
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://doi.org/10.1126/sciadv.ady5085
- PDF: Unavailable
- Local PDF: Not downloaded

Formalin-fixed paraffin-embedded (FFPE) tissue–compatible spatial transcriptomics (ST) is transforming biology and histopathology, but achieving high sensitivity, genome-wide coverage, single-cell resolution, and researcher accessibility remains challenging. To address these challenges, we here present a dendrimeric DNA coordinate barcoding design for FFPE tissue–adapted spatial RNA sequencing (Decoder-FFPE-seq) by integrating RNA-to-DNA probe conversion with blotting-assisted barcoding. Decoder-FFPE-seq provides single-cell resolution with a >2.6-fold sensitivity increase in whole-transcriptome mouse brain and archived human sample profiling over existing platforms, resolving potential cellular identity of low-abundance genes, finer tissue architecture, and capturing an epithelial-mesenchymal transition–associated signature for prognostic value. With expanded probe libraries, Decoder-FFPE-seq captures long noncoding and viral RNAs, revealing their spatial coregulatory networks with messenger RNAs in oral squamous cell carcinomas (OSCCs). In an OSCC immunotherapy cohort, two CD8 + T cell subpopulations were respectively identified in pre- and postchemoimmunotherapy samples, potentially linked to treatment response. Decoder-FFPE-seq establishes a robust, high-resolution, and accessible framework for sensitive ST profiling of archival tissues in fundamental and translational studies.

## 6. ReLink: Reliable Deep Learning for Microscopic Motion Tracking

- Authors: Yuan Jiang, Xiaochen Feng, Hongda Wei, Hao Sha, Hongpeng Wang, Min Zhang, Sanyang Han, Yongbing Zhang
- Source: openalex
- Venue type: journal
- Journal: Advanced Science
- Publication status: published
- Publication date: 2026-10-28
- DOI: https://doi.org/10.1002/advs.78541
- Categories: Advanced Fluorescence Microscopy Techniques, Cell Image Analysis Techniques, Fractional Differential Equations Solutions
- Relevance: 2.719562246079026
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://doi.org/10.1002/advs.78541
- PDF: https://onlinelibrary.wiley.com/doi/pdfdirect/10.1002/advs.78541
- Local PDF: Not downloaded

Single-particle tracking (SPT) serves as a fundamental technique for deciphering complex microscopic dynamics in biological and physical systems by resolving trajectories of individual particles. However, linking localizations into trajectories remains challenging in realistic experiments, where crowding, blinking, and localization errors lead to linking ambiguity. Both statistical and deep-learning approaches have been explored in these conditions, yet reliable link selection that generalizes across varying data distributions remains elusive. Here, we propose ReLink, a general deep-learning framework for reliable trajectory linking in SPT. By integrating physical priors into geometric representations and leveraging confidence-based adaptive filtering at inference, ReLink enables automated selection of trustworthy linkages, thereby preserving the fidelity of downstream trajectory-based analyses. Across challenging simulated scenarios spanning broad experimental conditions and motion regimes, ReLink consistently outperforms representative statistical and deep learning-based trajectory linking methods in both edge-level and trajectory-level evaluation metrics, leading to markedly improved downstream inference on public benchmarks. We further validate ReLink on diverse real-world experiments, from free diffusion systems to crowded intracellular environments, demonstrating its practical significance for quantitative interpretation of microscopic dynamics and its promise for next-generation trustworthy and automated SPT.

## 7. Is this chart lying to me? Automating the detection of misleading visualizations

- Authors: Jonathan Tonglet, Jan Zimny, Tinne Tuytelaars, Iryna Gurevych
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.5979760802121463
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.398/
- PDF: https://aclanthology.org/2026.acl-long.398.pdf
- Local PDF: pdf/2026-11-01_07_Is this chart lying to me_ Automating the detection of misleading visualizations.pdf

Misleading visualizations are a potent driver of misinformation on social media and the web. By violating chart design principles, they distort data and lead readers to draw inaccurate conclusions. Prior work has shown that both humans and multimodal large language models (MLLMs) are frequently deceived by such visualizations. Automatically detecting misleading visualizations and identifying the specific design rules they violate could help protect readers and reduce the spread of misinformation. However, the training and evaluation of AI models has been limited by the absence of large, diverse, and openly available datasets. In this work, we introduce Misviz, a benchmark of 2,604 real-world visualizations annotated with 12 types of misleaders. To support model training, we also release Misviz-synth, a synthetic dataset of 81,814 visualizations generated using Matplotlib and based on real-world data tables. We perform a comprehensive evaluation on both datasets using state-of-the-art MLLMs, rule-based systems, and fine-tuned classifiers. Our results reveal that the task remains highly challenging. We release Misviz, Misviz-synth, and the accompanying code.

## 8. Synthetic Eggs in Many Baskets: The Impact of Synthetic Data Diversity on LLM Fine-Tuning

- Authors: Max Schaffelder, Albert Gatt
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.5962581966865885
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.360/
- PDF: https://aclanthology.org/2026.findings-acl.360.pdf
- Local PDF: pdf/2026-11-01_08_Synthetic Eggs in Many Baskets_ The Impact of Synthetic Data Diversity on LLM Fine-Tuning.pdf

As synthetic data becomes widely used in language model development, understanding its impact on model behavior is crucial. This paper investigates the impact of the diversity of sources of synthetic data on fine-tuned large language models. We focus on three key dimensions: distribution collapse, adversarial robustness, and self-preference bias. Our findings reveal that fine-tuning models on synthetic data from diverse sources can mitigate distribution collapse, preserving the breadth of the output distribution and the diversity of the output text. Furthermore, while both human and synthetic fine-tuning data can remove safeguards, we observe a tendency for higher output quality in the latter case, thus making outputs potentially more usable and dangerous. Finally, we also find evidence that fine-tuning reduces self-preference bias, with human data being the most effective, followed by multi-source synthetic data. All code is available at https://github.com/maxschaffelder/synthetic_data_diversity .

## 9. Agentic Context Strategies for Multi-Format Document Understanding: When Should Language Models Use Tools?

- Authors: Mansi Uniyal, Mukul Singh, Ryan Nadel
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.594626242993374
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-industry.133/
- PDF: https://aclanthology.org/2026.acl-industry.133.pdf
- Local PDF: pdf/2026-11-01_09_Agentic Context Strategies for Multi-Format Document Understanding_ When Should Language Models Use Tools.pdf

Large language models face fundamental trade-offs when processing long documents: full context is expensive and may exceed limits, while RAG risks missing relevant information. We evaluate four context strategies across six frontier models on three document formats (Word, Excel, and PowerPoint). Our key finding: agentic tool-augmented approaches dramatically outperform passive strategies, with RAG+Tools achieving 46% accuracy vs 6% for RAG-only. Tool benefits are consistent across formats (+28-40 points) and models. We further show that (1) intelligent routing matters more than iteration count, (2) tools provide unique capability beyond reasoning loops, and (3) forcing active exploration matches providing context proactively. These results suggest tool augmentation is crucial for complex document QA.

## 10. POWSM: A Phonetic Open Whisper-Style Speech Foundation Model

- Authors: Chin-Jou Li, Kalvin Chang, Shikhar Bharadwaj, Eunjung Yeo, Kwanghee Choi, Jian Zhu, David R. Mortensen, Shinji Watanabe
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.5935804379311653
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.813/
- PDF: https://aclanthology.org/2026.acl-long.813.pdf
- Local PDF: pdf/2026-11-01_10_POWSM_ A Phonetic Open Whisper-Style Speech Foundation Model.pdf

Recent advances in spoken language processing have led to substantial progress in phonetic tasks such as automatic speech recognition (ASR), phone recognition (PR), grapheme-to-phoneme conversion (G2P), and phoneme-to-grapheme conversion (P2G). Despite their conceptual similarity, these tasks have largely been studied in isolation, each relying on task-specific architectures and datasets. In this paper, we introduce POWSM (Phonetic Open Whisper-style Speech Model), the first unified framework capable of jointly performing multiple phone-related tasks. POWSM enables seamless conversion between audio, text (graphemes), and phones, opening up new possibilities for universal and low-resource speech processing. Our model outperforms or matches specialized PR models of similar size (Wav2Vec2Phoneme and ZIPA) while jointly supporting G2P, P2G, and ASR. Our training data, models, and code are released to foster open science.

## 11. TLPO: Token-Level Policy Optimization for Mitigating Language Confusion in Large Language Models

- Authors: Jinho Choo, JunSeung Lee, Jimyeong Kim, Yeeho Song, S. K. Hong, Yeong-Dae Kwon
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.5932405728519874
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1976/
- PDF: https://aclanthology.org/2026.acl-long.1976.pdf
- Local PDF: pdf/2026-11-01_11_TLPO_ Token-Level Policy Optimization for Mitigating Language Confusion in Large Language Models.pdf

Large language models (LLMs) demonstrate strong multilingual capabilities, yet often fail to consistently generate responses in the intended language, exhibiting a phenomenon known as language confusion .Prior mitigation approaches based on sequence-level fine-tuning, such as DPO, ORPO, and GRPO, operate at the level of entire responses and can lead to unintended degradation of general model capabilities, motivating the need for more fine-grained alternatives.To address this, we introduce Token-Level Policy Optimization (TLPO) , a fine-tuning framework designed to mitigate language confusion through localized, token-level updates. TLPO identifies error-prone positions, explores alternative candidate tokens, and updates the policy using a tailored objective to suppress error-inducing outputs at a granular level.This selective intervention enables effective mitigation of language confusion without compromising the model’s general abilities.Experiments on multiple multilingual LLMs across diverse languages demonstrate that TLPO significantly outperforms baselines in improving language consistency while preserving downstream task accuracy.

## 12. CoTextor: Training-Free Modular Multilingual Text Editing via Layered Disentanglement and Depth-Aware Fusion

- Authors: Yu, Zhenyu, IDRIS, MOHD, Wang, Pei, Qureshi, Rizwan
- Source: neurips
- Venue type: conference
- Journal: NeurIPS 2025
- Publication status: formally_published
- Publication date: 2026-08-14
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.592644247360435
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://proceedings.neurips.cc/paper_files/paper/2025/hash/3ff6d26192f2c4cb6c61f51c9ceaa18f-Abstract-Creative_AI_Track.html
- PDF: https://proceedings.neurips.cc/paper_files/paper/2025/file/3ff6d26192f2c4cb6c61f51c9ceaa18f-Paper-Creative_AI_Track.pdf
- Local PDF: pdf/2026-11-01_12_CoTextor_ Training-Free Modular Multilingual Text Editing via Layered Disentanglement and Depth-Aware Fusion.pdf

We introduce \textit{CoTextor}, a modular and training-free framework for multilingual text editing in images, designed to support human-AI co-creation through a user-controllable and reversible workflow. Unlike diffusion-based systems that operate as black boxes, \textit{CoTextor} separates the editing process into transparent layers—foreground extraction, background inpainting, semantic rewriting, and depth-aware reintegration—allowing precise user-guided operations such as rotation, translation, scaling, and warping. To ensure realism, we introduce a perceptually guided integration module that enhances photometric and geometric coherence during text reinsertion. Built entirely from publicly available pretrained components, \textit{CoTextor} is accessible to non-technical, multilingual users, requiring no retraining or annotation. Through real-world scenarios in poster localization, street art remixing, and educational content creation, we demonstrate how \textit{CoTextor} enables inclusive and expressive visual storytelling across cultural and linguistic contexts.

## 13. Dynamic Tool Dependency Retrieval for Lightweight Function Calling

- Authors: Bhrij Patel, Davide Belli, Amir Jalalirad, Maximilian Arnold, Aleksandr Ermolov, Bence Major
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.592496687347295
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1680/
- PDF: https://aclanthology.org/2026.findings-acl.1680.pdf
- Local PDF: pdf/2026-11-01_13_Dynamic Tool Dependency Retrieval for Lightweight Function Calling.pdf

Function calling agents powered by Large Language Models (LLMs) select external tools to automate complex tasks. On-device agents typically use a retrieval module to select relevant tools, improving performance and reducing context length. However, existing retrieval methods rely on static and limited inputs, failing to capture multi-step tool dependencies and evolving task context. This limitation often introduces irrelevant tools that mislead the agent, degrading efficiency and accuracy. We propose Dynamic Tool Dependency Retrieval (DTDR), a lightweight retrieval method that conditions on both the initial query and the evolving tool calling plan. DTDR models tool dependencies from function calling demonstrations, enabling adaptive retrieval as plans unfold. We benchmark DTDR against state-of-the-art retrieval methods across multiple datasets and LLM backbones, evaluating retrieval precision, downstream task accuracy, and computational efficiency. Additionally, we explore strategies to integrate retrieved tools into prompts. Our results show that DTDR improves function calling success rates between 23% and 104% compared to state-of-the-art static retrievers.

## 14. GlossaGen: Making Academic Translation Smarter with Glossing

- Authors: Zixiao Wang, Duzhen Zhang, Juntian Zhang, Yuhan Liu, Guoming Li, Haolun Wu, Le Song, Xiuying Chen
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.5921730726044396
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.952/
- PDF: https://aclanthology.org/2026.findings-acl.952.pdf
- Local PDF: pdf/2026-11-01_14_GlossaGen_ Making Academic Translation Smarter with Glossing.pdf

When reading foreign-language literature, non-native users often face significant challenges. Existing traditional machine translation systems tend to obscure or mistranslate key terminology, while paraphrasing aimed at lay readers often oversimplifies it, thereby hindering their ability to master domain-specific technical vocabulary. To bridge this gap, we first define a novel task, Glossing-Oriented Academic Translation (GOAT), which aims to produce translations dynamically adapted to a reader’s academic proficiency, or level. We then propose GlossaGen, a comprehensive framework to address this task. GlossaGen features two key innovations: a multi-agent data synthesis pipeline that leverages academic personas to automatically generate a large-scale, structured dataset with level-specific explanations; and a novel training strategy based on dynamic adapter merging, which balances task generalization with user-level specialization by combining a ”generalist” adapter with a fine-grained ”expert” one. We evaluate GlossaGen on our synthesized benchmark, where results from automatic metrics, large language model (LLM)-based assessments, and human evaluations consistently demonstrate that our approach achieves higher scores than strong baselines across most metrics. Our framework provides a scalable pathway to enhance the comprehensibility of scientific literature for non-native readers, delivering more accurate translations accompanied by pedagogically sound, level-specific term explanations, and we release our code and data to facilitate further research.

## 15. LBLLM: Lightweight Binarization of Large Language Models via Three-Stage Distillation

- Authors: Siqing Song, Chuang Wang, Yong Lang, Yi Yang, Xu-Yao Zhang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.5918218286008066
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1640/
- PDF: https://aclanthology.org/2026.acl-long.1640.pdf
- Local PDF: pdf/2026-11-01_15_LBLLM_ Lightweight Binarization of Large Language Models via Three-Stage Distillation.pdf

Deploying large language models (LLMs) in resource-constrained environments is hindered by heavy computational and memory requirements. We present LBLLM, a lightweight binarization framework that achieves effective W(1+1)A4 quantization through a novel three-stage quantization strategy. The framework proceeds as follows: (1) initialize a high-quality quantized model via PTQ; (2) quantize binarized weights, group-wise bitmaps, and quantization parameters through layer-wise distillation while keeping activations in full precision; and (3) training learnable activation quantization factors to dynamically quantize activations to 4 bits. This decoupled design mitigates interference between weight and activation quantization, yielding greater training stability and better inference accuracy. LBLLM, trained only using 0.016B tokens with a single GPU, surpasses existing state-of-the-art binarization methods on W2A4 quantization settings across tasks of language modeling, commonsense QA, and language understanding. These results demonstrate that extreme low-bit quantization of LLMs can be both practical and highly effective without introducing any extra high-precision channels or rotational matrices commonly used in recent PTQ-based works, offering a promising path toward efficient LLM deployment in resource-limited situations.

## 16. CoEvolve: Training LLM Agents via Agent-Data Mutual Evolution

- Authors: Shidong Yang, Ziyu Ma, Tongwen Huang, Yiming Hu, Yong Wang, Xiangxiang Chu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.5914313875775297
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1055/
- PDF: https://aclanthology.org/2026.acl-long.1055.pdf
- Local PDF: pdf/2026-11-01_16_CoEvolve_ Training LLM Agents via Agent-Data Mutual Evolution.pdf

Reinforcement learning for LLM agents is typically conducted on a static data distribution, which fails to adapt to the agent’s evolving behavior and leads to poor coverage of complex environment interactions. To address these challenges, we propose CoEvolve, an agent-data mutual evolution framework that enables LLM agents to improve through closed-loop, interaction-driven training. Specifically, CoEvolve extracts feedback signals such as forgetting and uncertainty from rollout trajectories to identify failure-prone interaction patterns, and utilizes them to guide LLM-based task synthesis. The synthesized tasks are validated through environment interaction and utilized to update the data distribution, enabling joint adaptation of the agent and its data. Extensive experiments on AppWorld and BFCL across Qwen2.5-7B, Qwen3-4B, and Qwen3-30B-A3B demonstrate consistent and significant improvements over strong base models, yielding absolute gains of 19.43%, 15.58%, and 18.14%, respectively.

## 17. STAPO: Selective Trajectory-Aware Policy Optimization for LLM Agent Training

- Authors: Qiuyi Qi, Tian Liang, Mutian Bao, Jinjian Zhang, Dongnan Liu, Wei Zhou, Linjian Mo, Ming Kong, Jie Liu, Feng Zhang, Qiang Zhu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.5912279294456786
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1308/
- PDF: https://aclanthology.org/2026.acl-long.1308.pdf
- Local PDF: pdf/2026-11-01_17_STAPO_ Selective Trajectory-Aware Policy Optimization for LLM Agent Training.pdf

Reinforcement Learning (RL) is the dominant paradigm for training Large Language Model (LLM) agents on long-horizon tasks. However, sparse and delayed rewards often lead to trajectory neglect, in which agents lose focus on the task goal and interaction history at intermediate steps. Prior work has explored step-level supervision using Shannon-entropy–based uncertainty signals, which conflate inherent state complexity with agent confidence and therefore provide unreliable estimates of decision reliability. To address this issue, we propose normalized entropy, which measures confidence deviations relative to an agent’s average behavior under a given state, thereby strengthening the association between low-quality actions and trajectory neglect. Building on this insight, we introduce Selective Trajectory-Aware Policy Optimization (STAPO), a hierarchical group-based RL framework. STAPO leverages normalized entropy to locate outlier steps associated with trajectory neglect and optimizes them via a joint mechanism of trajectory-aware reward and trajectory-independent penalty, enhancing trajectory awareness while preserving training stability. Extensive experiments on ALFWorld, WebShop, and Search-Augmented QA demonstrate that STAPO achieves state-of-the-art performance while substantially alleviating trajectory neglect, validating its effectiveness and robustness for agentic tasks.

## 18. PVPO: Pre-Estimated Value-Based Policy Optimization for Agentic Reasoning

- Authors: Wenfeng Feng, Penghong Zhao, Guochao Jiang, Chuzhan Hao, Guohua Liu, Yuewei Zhang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.5911711419674366
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.182/
- PDF: https://aclanthology.org/2026.findings-acl.182.pdf
- Local PDF: pdf/2026-11-01_18_PVPO_ Pre-Estimated Value-Based Policy Optimization for Agentic Reasoning.pdf

Grouping-based methods have emerged as a significant frontier in Reinforcement Learning (RL), yet agentic reasoning poses a fundamental challenge for grouping-based methods: frequent environmental interactions and multi-step tool invocation generate highly variable trajectories, rendering intra-group advantage estimation unstable. In response, practitioners resort to excessive rollouts to stabilize training, which in turn incurs prohibitive computational costs. This negative feedback loop between advantage estimation instability and sampling inefficiency severely limits learning performance. We present PVPO, a stable and efficient critic-free RL framework that breaks this cycle through a pre-estimated value baseline and pre-sampled data filtering. Specifically, before training begins, PVPO performs a single round of rollouts to compute two signals: (1) Static V, a Monte Carlo estimate of the expected return that serves as a fixed baseline to stabilize advantage estimation; and (2) sample-level accuracy, as a difficulty metric to filter out trivial samples and inject ground-truth trajectories into hard ones, thereby enhancing training efficiency. As shown in Figure 1, experiments demonstrate that PVPO outperforms other grouping-based methods in both multi-step retrieval tasks and advanced mathematical reasoning benchmarks. Notably, our 7B model trained with PVPO matches or exceeds the performance of large language models (LLMs). Moreover, PVPO achieves a 2.5x speedup in training time compared to prior methods while maintaining comparable final performance.

## 19. One Panel Does Not Fit All: Case-Adaptive Multi-Agent Deliberation for Clinical Prediction

- Authors: Yuxing Lu, Yushuhong Lin, Jason Zhang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.5902519259009016
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-srw.75/
- PDF: https://aclanthology.org/2026.acl-srw.75.pdf
- Local PDF: pdf/2026-11-01_19_One Panel Does Not Fit All_ Case-Adaptive Multi-Agent Deliberation for Clinical Prediction.pdf

Large language models applied to clinical prediction exhibit case-level heterogeneity: simple cases yield consistent outputs, while complex cases produce divergent predictions under minor prompt changes. Existing single-agent strategies sample from one role-conditioned distribution, and multi-agent frameworks use fixed roles with flat majority voting, discarding the diagnostic signal in disagreement. We propose CAMP (Case-Adaptive Multi-agent Panel), where an attending-physician agent dynamically assembles a specialist panel tailored to each case’s diagnostic uncertainty. Each specialist evaluates candidates via three-valued voting (KEEP/REFUSE/NEUTRAL), enabling principled abstention outside one’s expertise. A hybrid router directs each diagnosis through strong consensus, fallback to the attending physician’s judgment, or evidence-based arbitration that weighs argument quality over vote counts. On diagnostic prediction and brief hospital course generation from MIMIC-IV across four LLM backbones, CAMP consistently outperforms strong baselines while consuming fewer tokens than most competing multi-agent methods, with voting records and arbitration traces offering transparent decision audits.

## 20. From Completion to Editing: Unlocking Context-Aware Code Infilling via Search-and-Replace Instruction Tuning

- Authors: Jiajun Zhang, Zeyu Cui, Jiaxi Yang, Lei Zhang, Yuheng Jing, Zeyao Ma, Tianyi Bai, Zilei Wang, Qiang Liu, Liang Wang, Binyuan Hui, Junyang Lin
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.590246677566219
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.361/
- PDF: https://aclanthology.org/2026.acl-long.361.pdf
- Local PDF: pdf/2026-11-01_20_From Completion to Editing_ Unlocking Context-Aware Code Infilling via Search-and-Replace Instruction Tuning.pdf

The dominant Fill-in-the-Middle (FIM) paradigm for code completion is constrained by its rigid inability to correct contextual errors and reliance on unaligned, insecure Base models. While Chat LLMs offer safety and Agentic workflows provide flexibility, they suffer from performance degradation and prohibitive latency, respectively. To resolve this dilemma, we propose Search-and-Replace Infilling ( SRI ), a framework that internalizes the agentic verification-and-editing mechanism into a unified, single-pass inference process. By structurally grounding edits via an explicit search phase, SRI harmonizes completion tasks with the instruction-following priors of Chat LLMs, extending the paradigm from static infilling to dynamic context-aware editing. We synthesize a high-quality dataset, SRI-200K , and fine-tune the SRI-Coder series. Extensive evaluations demonstrate that with minimal data (20k samples), SRI-Coder enables Chat models to surpass the completion performance of their Base counterparts. Crucially, unlike FIM-style tuning, SRI preserves general coding competencies and maintains inference latency comparable to standard FIM. We release our dataset and models, establishing SRI as a robust, secure, and efficient alignment recipe for next-generation interactive development.

## 21. EVOTOOL: Self-Evolving Tool-Use Policy Optimization in LLM Agents via Blame-Aware Mutation and Diversity-Aware Selection

- Authors: Shuo Yang, Caren Han, Xueqi Ma, Yan Li, Mohammad Reza Ghasemi Madani, Eduard Hovy
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.589670761923376
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.2016/
- PDF: https://aclanthology.org/2026.acl-long.2016.pdf
- Local PDF: pdf/2026-11-01_21_EVOTOOL_ Self-Evolving Tool-Use Policy Optimization in LLM Agents via Blame-Aware Mutation and Diversity-Aware Selection.pdf

LLM-based agents depend on effective tool-use policies to solve complex tasks, yet optimizing these policies remains challenging dueto delayed supervision and the difficulty ofcredit assignment in long-horizon trajectories.Existing optimization approaches tend to beeither monolithic, which are prone to entangling behaviors, or single-aspect, which ignorecross-module error propagation. To addressthese limitations, we propose EVOTOOL, a self-evolving framework that optimizes a modulartool-use policy via a gradient-free evolutionary paradigm. EVOTOOL decomposes agent’stool-use policy into four modules, includingPlanner, Selector, Caller, and Synthesizer, anditeratively improves them through three mechanisms. Trajectory-Grounded Blame Attribution uses diagnostic traces to localize failuresto a specific module. Feedback-Guided Targeted Mutation then edits only that modulevia natural-language critique. Diversity-AwarePopulation Selection preserves complementarycandidates to ensure solution diversity. Acrossfour diverse benchmarks, EVOTOOL outperforms strong baselines by over 5 points on bothGPT-4.1 and Qwen3-8B, while achieving superior efficiency and transferability.

## 22. Beyond Markovian Forgetfulness: Episodic Memory for Reasoning-Intensive Retrieval

- Authors: Dohyeon Lee, Yeonseok Jeong, Seung-won Hwang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.5895761112003237
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1728/
- PDF: https://aclanthology.org/2026.acl-long.1728.pdf
- Local PDF: pdf/2026-11-01_22_Beyond Markovian Forgetfulness_ Episodic Memory for Reasoning-Intensive Retrieval.pdf

Reasoning-intensive information retrieval uses large language models to solve complex queries via multi-step reasoning. However, existing methods have critical limitations. Chain-of-Thought (CoT) approaches suffer from inefficiency, while state-based methods, despite better token efficiency, often fall into reasoning cycles that trap the query refinement process. To address these issues, we propose Episodic Memory for Retrieval (EMR), which enhances the state-based framework with an episodic memory. This module stores the full history of prior states for a query, allowing the model to avoid repetition of such cycles. Experiments on the BRIGHT benchmark show that EMR consistently outperforms both CoT and state-based baselines. Moreover, it is highly token-efficient, reducing token usage by 72% on average. Our results show that episodic memory is an effective and token-efficient mechanism for reasoning-intensive retrieval. The gains also generalize across different base models and stay efficient in terms of end-to-end latency. The code is available in https://github.com/ldilab/EMR .

## 23. TableVista: Benchmarking Multimodal Table Reasoning under Visual and Structural Complexity

- Authors: Zheyuan Yang, Liqiang Shang, Junjie Chen, Xun Yang, Chenglong Xu, Bo Yuan, Chenyuan Jiao, Yaoru Sun, Yilun Zhao
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.5887396725920873
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1745/
- PDF: https://aclanthology.org/2026.findings-acl.1745.pdf
- Local PDF: pdf/2026-11-01_23_TableVista_ Benchmarking Multimodal Table Reasoning under Visual and Structural Complexity.pdf

We introduce TableVista, a comprehensive benchmark for evaluating foundation models in multimodal table reasoning under visual and structural complexity. TableVista consists of 3,000 high-quality table reasoning problems, where each instance is expanded into 10 distinct visual variants through our multi-style rendering and transformation pipeline. This process encompasses diverse scenario styles, robustness perturbations, and vision-only configurations, culminating in 30,000 multimodal samples for a multi-dimensional evaluation. We conduct an extensive evaluation of 29 state-of-the-art open-source and proprietary foundation models on TableVista. Through comprehensive quantitative and qualitative analysis, we find that while evaluated models remain largely stable across diverse rendering styles, they exhibit pronounced performance degradation on complex structural layouts and vision-only settings, revealing that current models struggle to maintain reasoning consistency when structural complexity combines with visually integrated presentations. These findings highlight critical gaps in current multimodal capabilities, providing insights for advancing more robust and reliable table understanding models.

## 24. AIPO: Adaptive Information Guided Token-Level Reinforcement Learning for Large Language Model Reasoning

- Authors: Bin Chen, Hongfei Ye, Huiyang Wang, Wenxi Liu, Yu Zhang, Furui Liu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.5883750985657143
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.2057/
- PDF: https://aclanthology.org/2026.acl-long.2057.pdf
- Local PDF: pdf/2026-11-01_24_AIPO_ Adaptive Information Guided Token-Level Reinforcement Learning for Large Language Model Reasoning.pdf

Reinforcement Learning with Verifiable Rewards (RLVR) improves the reasoning capability of Large Language Models (LLMs). Current RLVR trains LLMs on all generated tokens, rather than exploring which tokens actually contribute to reasoning. We propose AIPO(Adaptive–Information Policy Optimization), which focuses updates on those decisive tokens discovered on the fly. AIPO estimates each hidden state’s mutual information to score tokens. Policy gradients are then computed only on these critical tokens, using an advantage that blends information gain and verifiable correctness. To improve the efficiency of mutual-information estimation, AIPO adopts a Random–Fourier approximation of the Hilbert–Schmidt Independence Criterion. Across five math and science benchmarks, AIPO yields up to +20% accuracy over strong RLVR baselines while updating merely 10% of tokens, demonstrating superior efficiency and effectiveness. Our findings highlight the importance of information–driven token selection for efficient and effective reinforcement learning of LLM reasoning.

## 25. DPEPO: Diverse Parallel Exploration Policy Optimization for LLM-based Agents

- Authors: JunShuo Zhang, Chengrui Huang, Feng Guo, Zihan Li, Ke Shi, Menghua Jiang, Jiguo Yu, Shuo Shang, Shen Gao
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.5882593964348555
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.2151/
- PDF: https://aclanthology.org/2026.acl-long.2151.pdf
- Local PDF: pdf/2026-11-01_25_DPEPO_ Diverse Parallel Exploration Policy Optimization for LLM-based Agents.pdf

Large language model (LLM) agents that follow the sequential “reason-then-act” paradigm have achieved superior performance in many complex tasks. However, these methods suffer from limited exploration and incomplete environmental understanding, as they interact with only a single environment per step. In this paper, we first introduce a novel paradigm that enables an agent to interact with multiple environments simultaneously and share cross-trajectory experiences. Build upon this paradigm, we further propose Diverse Parallel Exploration Policy Optimization (DPEPO), a reinforcement learning (RL) algorithm that encourages the agent to perform diverse parallel exploration. There are two stages in DPEPO: initial supervised fine-tuning (SFT) imparts basic parallel reasoning and action generation, followed by reinforcement learning stage with a hierarchical reward scheme. We design a parallel trajectory-level success reward and two step-level rewards: Diverse Action Reward and Diverse State Transition Reward, which actively penalize behavioral redundancy and promote broad exploration. Extensive experiments on ALFWorld and ScienceWorld show that DPEPO achieves state-of-the-art (SOTA) success rates, while maintaining comparable efficiency to strong sequential baselines.

## 26. AgentAsk: Multi-Agent Systems Need to Ask

- Authors: Bohan Lin, Kuo Yang, Zelin Tan, Yingchuan Lai, Chen Zhang, Guibin Zhang, Xinlei Yu, Miao Yu, Xu Wang, Yudong Zhang, Yang Wang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.5881549948413083
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1294/
- PDF: https://aclanthology.org/2026.acl-long.1294.pdf
- Local PDF: pdf/2026-11-01_26_AgentAsk_ Multi-Agent Systems Need to Ask.pdf

Multi-agent systems (MAS) built on large language models promise improved problem-solving through collaboration, yet they often fail to consistently outperform strong single-agent baselines due to error propagation at inter-agent message handoffs. In this work, we conduct a systematic empirical analysis of such failures and introduce an edge-level error taxonomy that identifies four dominant error types: Data Gap, Signal Corruption, Referential Drift, and Capability Gap, as primary sources of failure in multi-agent interactions. Building on this taxonomy, we propose AgentAsk, a lightweight clarification module designed to intervene at the edge level in MAS to prevent cascading errors. The module operates by strategically applying minimal clarifications at critical points within the system, improving the accuracy and efficiency of the overall task. AgentAsk is trained to balance the trade-offs between clarification cost, latency, and accuracy, while it is also architecture-agnostic and can be easily integrated into existing systems. Evaluated across five benchmarks, AgentAsk consistently improves accuracy by up to 4.69%, while keeping latency and extra costs below 10% compared to baseline MAS, showcasing its high efficiency and minimal overhead. The code is available at https://anonymous.4open.science/r/AgentAsk-3432 .

## 27. Guaranteeing Knowledge Integration with Joint Decoding for Retrieval-Augmented Generation

- Authors: Zhengyi Zhao, Shubo Zhang, Zezhong Wang, Yuxi Zhang, Huimin Wang, Yutian Zhao, Yefeng Zheng, Binyang Li, Kam-Fai Wong, Xian Wu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.588062235708133
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.192/
- PDF: https://aclanthology.org/2026.acl-long.192.pdf
- Local PDF: pdf/2026-11-01_27_Guaranteeing Knowledge Integration with Joint Decoding for Retrieval-Augmented Generation.pdf

Retrieval-Augmented Generation (RAG) significantly enhances Large Language Models (LLMs) by providing access to external knowledge. However, current research primarily focuses on retrieval quality, often overlooking the critical ”integration bottleneck”: even when relevant documents are retrieved, LLMs frequently fail to utilize them effectively due to conflicts with their internal parametric knowledge. In this paper, we argue that implicitly resolving this conflict in a single generation pass is suboptimal. We introduce GuarantRAG, a framework that explicitly decouples reasoning from evidence integration. First, we generate an ”Inner-Answer” based solely on parametric knowledge to capture the model’s reasoning flow. Second, to guarantee faithful evidence extraction, we generate a ”Refer-Answer” using a novel Contrastive DPO objective. This objective treats the parametric Inner-Answer as a negative constraint and the retrieved documents as positive ground truth, forcing the model to suppress internal hallucinations in favor of external evidence during this phase. Finally, rather than naive concatenation or using the DPO trained model directly, we propose a joint decoding mechanism that dynamically fuses the logical coherence of the Inner-Answer with the factual precision of the Refer-Answer at the token level. Experiments on five QA benchmarks demonstrate that GuarantRAG improves accuracy by up to 12.1% and reduces hallucinations by 16.3% compared to standard and dynamic RAG baselines.

## 28. Teaching Language Models to Check Grounded Claim Factuality with Human Test-Taking Strategies

- Authors: Yuxuan Ye, Raul Santos-Rodriguez, Edwin Simpson
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.5878810886488264
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1468/
- PDF: https://aclanthology.org/2026.acl-long.1468.pdf
- Local PDF: pdf/2026-11-01_28_Teaching Language Models to Check Grounded Claim Factuality with Human Test-Taking Strategies.pdf

Grounded claim factuality checking is important for large language model (LLM) applications such as retrieval-augmented generation, as it helps users assess the correctness of generated outputs. Existing metrics using entailment classifiers require dataset-specific threshold tuning, while LLM-based approaches often use direct prompting, which underutilises the reasoning capabilities of LLMs. We address this by formulating grounded claim factuality checking as a true/false reading comprehension task and prompting LLMs with explicit test-taking strategies for efficient reasoning. Our method reduces token usage by over 80% compared to unguided open-ended reasoning, and achieves competitive performance to more expensive alternatives across two factuality benchmarks, setting a new state of the art on one. To further reduce inference cost, we train small language models (SLMs) to replace LLMs in the checking pipeline. Using supervised fine-tuning (SFT) and a self-revision mechanism, the SLMs learn to improve their factuality judgements. Experimental results show that the resulting SLMs perform on par with strong baselines, combining low inference costs with generating supporting rationales to support interpretability. Code and datasets will be released upon acceptance.

## 29. WildSci: Advancing Scientific Reasoning from In-the-Wild Literature

- Authors: Tengxiao Liu, Deepak Nathani, Zekun Li, Kevin Yang, William Yang Wang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.587446970401235
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.567/
- PDF: https://aclanthology.org/2026.findings-acl.567.pdf
- Local PDF: pdf/2026-11-01_29_WildSci_ Advancing Scientific Reasoning from In-the-Wild Literature.pdf

Recent progress in large language model (LLM) reasoning has focused on domains like mathematics and coding, where abundant high-quality data and objective evaluation metrics are readily available. In contrast, progress in scientific reasoning remains limited in domains such as medicine and materials science due to restricted dataset coverage and the inherent complexity of open-ended scientific questions. To address these challenges, we propose a general framework for sustainable scientific reasoning QA generation, and introduce WildSci, a new dataset of domain-specific science questions automatically synthesized from peer-reviewed literature, spanning 9 scientific disciplines and 26 subdomains. WildSci enables scalable training with well-defined reward signals in a multiple-choice format. We further apply reinforcement learning to finetune models on WildSci and analyze the resulting training dynamics, including domain-specific performance changes, response behaviors, and generalization trends. Experiments on a suite of scientific benchmarks demonstrate the effectiveness of our framework and dataset. We release WildSci to enable scalable and sustainable research in scientific reasoning.

## 30. LeLoRA: Learnable Low-Rank Adaptation of Large Language Models

- Authors: Xiaoling Zhou, Mingjie Zhang, Zhemg Lee, Wei Ye, Shikun Zhang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.5874228508626675
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1628/
- PDF: https://aclanthology.org/2026.acl-long.1628.pdf
- Local PDF: pdf/2026-11-01_30_LeLoRA_ Learnable Low-Rank Adaptation of Large Language Models.pdf

Fine-tuning large language models (LLMs) is an effective approach to enhancing their performance on specialized downstream tasks. Among the various techniques, low-rank adaptation has garnered significant attention due to its ability to maintain the full performance of fine-tuning while enhancing computational efficiency. However, existing approaches often rely on manually specified and fixed hyperparameters to identify the trainable components within weight matrices, resulting in suboptimal performance and low parameter efficiency. This paper presents a novel Learnable Low-Rank Adaptation (LeLoRA) framework that utilizes dynamically learned fine-tuning strategies to facilitate the effective adaptation of LLMs. Our framework integrates an LLM with a policy network that automatically and adaptively generates matrix-specific adaptation strategies to identify the trainable components of each weight matrix, taking into account their unique characteristics, such as singular values and matrix norms. A reinforcement learning-based optimization algorithm is then employed to iteratively update the LLM and the policy network, ensuring that the generated strategies adapt in real time to the evolving states of the LLM. Extensive experiments have been conducted across various natural language processing and multimodal tasks. The results across ten different LLMs, ranging from 125M to 70B parameters, provide compelling evidence that LeLoRA consistently outperforms existing baselines in adapting LLMs. Moreover, analytical experiments provide valuable insights into the effectiveness of the generated strategies.
