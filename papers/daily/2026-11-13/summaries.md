# Paper Daily Reading - 2026-11-13

## 1. Efficient and accurate mixed model association tool for single-cell eQTL analysis

- Authors: Wei Zhou, Anna S. E. Cuomo, Linfeng Hu, Angli Xue, Masahiro Kanai, Yijia Christiana Liu, Taeyeop Kang, Youngdae Kim, Alex Rodriguez, Ravi Madduri, Bram L. Gorissen, Grant Chau, Anne Senabouth, M. Grace Gordon, Richard Perez, Pooja Kathail, Min Cheol Kim, Chun Jimmie Ye, Chirag Krishna, Ramnik J. Xavier, Daniel G. MacArthur, Joseph E. Powell, Mark J. Daly, Benjamin M. Neale
- Source: openalex
- Venue type: journal
- Journal: Nature Genetics
- Publication status: published
- Publication date: 2026-11-06
- DOI: https://doi.org/10.1038/s41588-026-02798-2
- Categories: Genetic Associations and Epidemiology, Single-cell and spatial transcriptomics, Genetic Mapping and Diversity in Plants and Animals
- Relevance: 2.701542207244267
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://doi.org/10.1038/s41588-026-02798-2
- PDF: https://www.nature.com/articles/s41588-026-02798-2.pdf
- Local PDF: pdf/2026-11-13_01_Efficient and accurate mixed model association tool for single-cell eQTL analysis.pdf

Genetic effects on gene expression often vary across cell types, motivating expression quantitative trait loci (eQTL) mapping in single-cell RNA sequencing data. Existing approaches generally aggregate expression across cells, use Gaussian models poorly suited to read counts or do not scale. Here we show that SAIGE-QTL, a Poisson mixed model that directly models single-cell read counts, enables calibrated and computationally scalable eQTL mapping while accounting for donor-level and cell-level covariates and unequal numbers of cells per donor. In simulations and three single-cell datasets, SAIGE-QTL improved statistical efficiency and discovery of genes with significant eQTLs (eGenes) relative to pseudobulk methods and produced results consistent with existing single-cell models at substantially lower computational cost. In 1.2 million immune cells, SAIGE-QTL identified 48.8% more eGenes than pseudobulk analysis. SAIGE-QTL further enabled genome-wide trans-eQTL mapping and rare variant set-based testing, identifying rare variant associations independent of common eQTL signals. SAIGE-QTL therefore expands single-cell eQTL discovery across common, rare and trans-acting genetic variation.

## 2. MMC-seq enables efficient long-read eccDNA profiling from low-input samples

- Authors: Yaoxin Zhang, Muyuan You, Congcong Zhou, Yajuan Guo, Yaohua Huang, Suyue Wu, Xiaoqian Chen, Haobo Sun, Xinqi Leo Yu, Qi Feng, Wenqin Wang, Tao Huang, Yan Zhao, Hui Yang, Qiang Zhao, Wei Hua, Bin Han, Tingting Lu, Ying Qing Mao
- Source: openalex
- Venue type: journal
- Journal: Nature Communications
- Publication status: published
- Publication date: 2026-11-04
- DOI: https://doi.org/10.1038/s41467-026-79221-1
- Categories: Genomic variations and chromosomal abnormalities, Cancer Genomics and Diagnostics, Chromosomal and Genetic Variations
- Relevance: 2.5648802415895395
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://doi.org/10.1038/s41467-026-79221-1
- PDF: Unavailable
- Local PDF: Not downloaded

Extrachromosomal circular DNA (eccDNA) comprises diverse DNA circles outside chromosomes, yet limited material constrains their analysis. Here, we present Multi-Modal Circle-seq (MMC-seq), integrating optimised enrichment with PacBio HiFi sequencing, and CircleSeeker for reconstructing and classifying unique-locus, multi-locus and chimeric circles. Workflow optimisation increases detection 38.7-fold in matched 300,000-cell preparations; CircleSeeker achieves F1 scores above 96% in platform-matched human unique-locus simulations. MMC-seq profiles single-cell preparations and frozen tumour tissue, and supports a size-based readout from 100 μL of plasma. One gliosarcoma yields over a million eccDNAs, including nested circles within an EGFR amplification region. In cell lines, ≤5-kb unique-locus circles show largely replicate-specific junctions but reproducible density landscapes and cell-line-specific hotspots. Multi-locus circles reflect host repeat architecture; intra-chromosomal chimeric circles have median genomic spans of 8.0 Mb in human but 31–94 kb in three plant species. This framework makes eccDNA diversity accessible from limited material and biologically interpretable through structural classification. Comprehensive eccDNA profiling remains constrained by differences in protocol, input requirement and sensitivity. Here, the authors present Multi-Modal Circle-seq (MMC-seq), an efficient long-read approach for profiling and classifying eccDNA from low-input samples.

## 3. Grouped Adaptive Weight Sharing (GAWS): An Inference-Efficient Adaptation Method for Large Language Models

- Authors: Eman Alsuradi, Junhyun Lee, Kyenghun Lee, Hyeonmok Ko, Fahed Jubair
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.562493206980698
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1590/
- PDF: https://aclanthology.org/2026.findings-acl.1590.pdf
- Local PDF: pdf/2026-11-13_03_Grouped Adaptive Weight Sharing (GAWS)_ An Inference-Efficient Adaptation Method for Large Language Models.pdf

Although Low-Rank Adaptation (LoRA) revolutionized parameter-efficient fine-tuning, it often incurs an inference overhead due to the extra computation required by adapter layers. While most literature focuses on maximizing accuracy or minimizing parameter counts, this paper prioritizes single-request inference performance in the unmerged adapter setting, where adapters must remain decoupled from the base model at runtime. By analyzing LoRA adapters on GPUs, we identify segmented function calls as the primary source of this latency. To address this, we propose G rouped A daptive W eight S haring (GAWS), a novel adapter design based on structured Kronecker product decomposition . Experiments on T5-3B, GPT-2 Large, LLaMA3.2-3B, and RoBERTa-Large show that GAWS reduces latency to about 40% of the gap between the unmerged LoRA and the base model, while maintaining parameter efficiency and comparable accuracy. This positions GAWS as a Pareto-efficient solution for deploying adapted LLMs in latency-sensitive settings, balancing the high latency of compressed adapters with the accuracy of LoRA. The source code is available at: https://github.com/SamsungLabs/GAWS .

## 4. XToM: Exploring the Multilingual Theory of Mind for Large Language Models

- Authors: Chunkit Chan, Yauwai Yim, Hongchuan Zeng, Zhiying Zou, Xinyuan Cheng, Zhifan Sun, Zheye Deng, Kawai Chung, Yuzhuo Ao, Fan Yixiang, Cheng Jiayang, Ercong Nie, Ginny Wong, Helmut Schmid, Hinrich Schuetze, Simon See, Yangqiu Song
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.5594055321714313
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.805/
- PDF: https://aclanthology.org/2026.acl-long.805.pdf
- Local PDF: pdf/2026-11-13_04_XToM_ Exploring the Multilingual Theory of Mind for Large Language Models.pdf

Theory of Mind (ToM)—the ability to infer mental states in others—is pivotal for human social cognition. Existing evaluations of ToM in LLMs are largely limited to English, neglecting the linguistic diversity that shapes human cognition. This limitation raises a critical question: can LLMs exhibit Multilingual Theory of Mind—the capacity to reason about mental states across diverse linguistic contexts? To address this gap, we present XToM, a rigorously validated multilingual benchmark that evaluates ToM across five languages and incorporates diverse, contextually rich task scenarios. Using XToM, we systematically evaluate LLMs (e.g., DeepSeek R1), revealing a pronounced dissonance: while models excel in multilingual language understanding, their ToM performance varies across languages. Our findings expose limitations in LLMs’ ability to replicate human-like mentalizing across linguistic contexts.

## 5. Lending Eyesight to Language Models: Modeling and Probing Human scanpath through Transformer Decoder

- Authors: Junlin Li, David Robert Reich, Yu-Yin Hsu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.5590833280857215
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1591/
- PDF: https://aclanthology.org/2026.findings-acl.1591.pdf
- Local PDF: pdf/2026-11-13_05_Lending Eyesight to Language Models_ Modeling and Probing Human scanpath through Transformer Decoder.pdf

Human scanpaths offer rich and reliable clues about the cognitive mechanisms underlying language comprehension. Decoder-only language models, typically large language models (LLMs), have proven to exhibit striking parallels with human cognitive processes. In this study, we investigate to what extent language models can be endowed with human-like gaze shifts. Besides, by probing scanpath through eye model, analogous to probing language through language models, we ask whether such modeling can yield novel knowledge of the cognitive machinery of sense making.This study presents a novel plug-and-play module, EyeLM, to transform an autoregressive language model into an autoregressive eye model, thus facilitating a probabilistic spatial modeling of human explicit attention. Our EyeLM module, powered by LLMs, achieves competitive performance with novel cognitive probing capabilities. By probing EyeLM, we can reach the predictability and uncertainty of the scanpath. Exhibiting aligned patterns with prior knowledge about human reading comprehension, these probabilistic measures of scanpath act as promising predictors of human comprehension skills.

## 6. The Role of Mixed-Language Documents for Multilingual Large Language Model Pretraining

- Authors: Jiandong Shao, Raphael Tang, Crystina Zhang, Karin Sevegnani, Pontus Stenetorp, Jianfei Yang, Yao Lu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.558042296165901
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1706/
- PDF: https://aclanthology.org/2026.acl-long.1706.pdf
- Local PDF: pdf/2026-11-13_06_The Role of Mixed-Language Documents for Multilingual Large Language Model Pretraining.pdf

Multilingual large language models achieve impressive cross-lingual performance despite largely monolingual pretraining. While bilingual data in pretraining corpora is widely believed to enable these abilities, details of its contributions remain unclear. We investigate this question by pretraining models from scratch under controlled conditions, comparing the standard web corpus with a monolingual-only version that removes all multilingual documents. Despite constituting only 2% of the corpus, removing bilingual data causes translation performance to drop 56% in BLEU, while behaviour on cross-lingual QA and general reasoning tasks remains stable, with training curves largely overlapping the baseline. To understand this asymmetry, we categorize bilingual data into parallel (14%), code-switching (72%), and miscellaneous documents (14%) based on the semantic relevance of content in different languages. We then conduct granular ablations by reintroducing parallel or code-switching data into the monolingual-only corpus. Our experiments reveal that parallel data almost fully restores translation performance (91% of the unfiltered baseline), whereas code-switching contributes minimally. Other cross-lingual tasks remain largely unaffected by either type. These findings reveal that translation critically depends on systematic token-level alignments from parallel data, whereas cross-lingual understanding and reasoning appear to be achievable even without bilingual data.

## 7. Automated Knowledge Component Generation and Interpretable Knowledge Tracing in Coding Problems

- Authors: Zhangqi Duan, Nigel Fernandez, Arun Balajiee Lekshmi Narayanan, Mohammad Hassany, Rafaella Sampaio de Alencar, Peter Brusilovsky, Bita Akram, Andrew Lan
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.5579427585182386
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1670/
- PDF: https://aclanthology.org/2026.findings-acl.1670.pdf
- Local PDF: pdf/2026-11-13_07_Automated Knowledge Component Generation and Interpretable Knowledge Tracing in Coding Problems.pdf

Knowledge components (KCs) are key to assessing student knowledge levels on fine-grained skills and driving personalization and feedback. However, crafting KCs and tagging them for problems, traditionally performed by human domain experts, is highly labor-intensive. Prior work has studied automated KC generation only for multiple-choice questions but not open-ended ones. We bridge this gap and present an automated, large language model (LLM)-based pipeline for KC generation and tagging for open-ended programming problems. We also develop an LLM-based knowledge tracing (KT) framework to leverage these LLM-generated KCs. We conduct extensive quantitative and qualitative evaluations on two real-world student code submission datasets. Results show that our KT method outperforms existing ones and LLM-generated KCs outperform human-written KCs on future student response prediction. We also investigate how these KCs enable us to analyze student learning curves and conduct human evaluation with course instructors to further verify the quality of KC-problem tagging.

## 8. Text2Mem: A Unified Memory Operation Language for Memory Operating System

- Authors: Leo Wang, Lihai Yang, Boyu Chen, Kerun Xu, Gongyi Zou, Bo Tang, Feiyu Xiong, Siheng Chen, Zhiyu li
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.557183408595862
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.100/
- PDF: https://aclanthology.org/2026.findings-acl.100.pdf
- Local PDF: pdf/2026-11-13_08_Text2Mem_ A Unified Memory Operation Language for Memory Operating System.pdf

Large language model agents increasingly rely on memory to support long-horizon interaction, yet existing frameworks expose only a small set of low-level primitives and lack a formal, executable specification for memory control. As a result, higher-order operations such as promotion, consolidation, or lifecycle governance are missing or inconsistently implemented, leading to unpredictable behavior across systems. We introduce Text2Mem, a unified memory operation language that standardizes the translation of natural-language instructions into reliable execution. Text2Mem defines a compact and expressive operation set spanning encoding, storage, and retrieval, and represents each instruction as a schema-based contract with explicit fields and semantic invariants. Validated schemas are parsed into typed operation objects and executed through a unified pipeline that supports both a SQL reference backend and real memory frameworks, enabling safe, deterministic, and portable behavior across heterogeneous systems. We further outline the Text2Mem Benchmark, which decouples schema generation from backend execution to systematically evaluate planning accuracy and execution fidelity. Together, Text2Mem and its benchmark establish a standardized foundation for controllable and reproducible memory management in LLM-based agents.

## 9. Visual Self-Fulfilling Alignment: Shaping Safety-Oriented Personas via Threat-Related Images

- Authors: Qishun Yang, Shu Yang, Lijie Hu, Di Wang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.5567867995768294
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.490/
- PDF: https://aclanthology.org/2026.acl-long.490.pdf
- Local PDF: pdf/2026-11-13_09_Visual Self-Fulfilling Alignment_ Shaping Safety-Oriented Personas via Threat-Related Images.pdf

Multimodal large language models (MLLMs) face safety misalignment where visual inputs enable harmful outputs. Existing methods require explicit safety labels or contrastive data, yet threat-related concepts are concrete and visually depictable, while safety concepts like helpfulness are abstract and lack visual referents. Inspired by self-fulfilling mechanism underlying emergent misalignment, we propose Visual Self-Fulfilling Alignment (VSFA). VSFA fine-tunes vision-language models (VLMs) on neutral VQA tasks constructed around threat-related images, without any safety labels. Through repeated exposure to threat-related visual content, models internalize implicit semantics of vigilance and caution, shaping safety-oriented personas. Experiments across multiple VLMs and safety benchmarks demonstrate that VSFA reduces attack success rate, improves response quality, and mitigates over-refusal while preserving general capabilities. Our work extends self-fulfilling mechanism from text to visual modalities, offering a label-free approach to VLMs alignment.

## 10. LEASH: Adaptive Length Penalty and Reward Shaping for Efficient Large Reasoning Model

- Authors: Yanhao Li, Lu Ma, Jiaran Zhang, Lexiang Tang, Wentao Zhang, Guibo Luo
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.5564485744522196
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.129/
- PDF: https://aclanthology.org/2026.acl-long.129.pdf
- Local PDF: pdf/2026-11-13_10_LEASH_ Adaptive Length Penalty and Reward Shaping for Efficient Large Reasoning Model.pdf

Large Language Models (LLMs) often produce unnecessarily lengthy reasoning traces, which significantly increase computational cost and latency. Existing approaches typically rely on fixed length penalties, but such penalties are hard to tune and fail to adapt to the evolving reasoning abilities of LLMs, leading to suboptimal trade-offs between accuracy and conciseness. To address this challenge, we propose LEASH ( adaptive LEngth penAlty and reward SHaping ), a reinforcement learning framework for efficient reasoning in LLMs. We formulate length control as a constrained optimization problem and employ a Lagrangian primal–dual method to dynamically adjust the penalty coefficient. When generations exceed the target length, the penalty is intensified; when they are shorter, it is relaxed. This adaptive mechanism guides models toward producing concise reasoning without sacrificing task performance. Experiments on Deepseek-R1-Distill-Qwen-1.5B and Qwen3-4B-Thinking-2507 show that LEASH reduces the average reasoning length by 60% across diverse tasks—including in-distribution mathematical reasoning and out-of-distribution domains such as coding and instruction following—while maintaining competitive performance. Our work thus presents a practical and effective paradigm for developing controllable and efficient LLMs that balance reasoning capabilities with computational budgets.

## 11. Visual Inception: Compromising Long-term Planning in Agentic Recommenders via Multimodal Memory Poisoning

- Authors: Jiachen Qian
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.5550114036980682
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.954/
- PDF: https://aclanthology.org/2026.acl-long.954.pdf
- Local PDF: pdf/2026-11-13_11_Visual Inception_ Compromising Long-term Planning in Agentic Recommenders via Multimodal Memory Poisoning.pdf

The evolution from static ranking models to Agentic Recommender Systems (Agentic RecSys) empowers AI agents to maintain long-term user profiles and autonomously plan service tasks. While this paradigm shift enhances personalization, it introduces a vulnerability: reliance on Long-term Memory (LTM). In this paper, we uncover a threat termed “Visual Inception.” Unlike traditional adversarial attacks that seek immediate misclassification, Visual Inception injects triggers into user-uploaded images (e.g., lifestyle photos) that act as “sleeper agents” within the system’s memory. When retrieved during future planning, these poisoned memories hijack the agent’s reasoning chain, steering it toward adversary-defined goals (e.g., promoting high-margin products) without prompt injection. To mitigate this, we propose CognitiveGuard, a dual-process defense framework inspired by human cognition. It consists of a System 1 Perceptual Sanitizer (diffusion-based purification) to cleanse sensory inputs and a System 2 Reasoning Verifier (counterfactual consistency checks) to detect anomalies in memory-driven planning. Extensive experiments on a mock e-commerce agent environment demonstrate that Visual Inception achieves about 85% Goal-Hit Rate (GHR), while CognitiveGuard reduces this risk to around 10% with configurable latency trade-offs (about 1.5s in lite mode to about 6.5s for full sequential verification), without quality degradation under our setup.Latency reporting uses separate accounting: query-time overhead excludes one-time upload-time preprocessing.

## 12. Towards Robust Real-World Spreadsheet Understanding with Multi-Agent Multi-Format Reasoning

- Authors: Houxing Ren, Mingjie Zhan, Zimu Lu, Ke Wang, Yunqiao Yang, Haotian Hou, Hongsheng Li
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.554992148189501
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.86/
- PDF: https://aclanthology.org/2026.acl-long.86.pdf
- Local PDF: pdf/2026-11-13_12_Towards Robust Real-World Spreadsheet Understanding with Multi-Agent Multi-Format Reasoning.pdf

Spreadsheets are central to real-world applications such as enterprise reporting, auditing, and scientific data management. Despite their ubiquity, existing large language model based approaches typically treat tables as plain text, overlooking critical layout cues and visual semantics. Moreover, real-world spreadsheets are often massive in scale, exceeding the input length that LLMs can efficiently process. To address these challenges, we propose SpreadsheetAgent, a two-stage multi-agent framework for spreadsheet understanding that adopts a step-by-step reading and reasoning paradigm. Instead of loading the entire spreadsheet at once, SpreadsheetAgent incrementally interprets localized regions through multiple modalities, including code execution results, images, and LaTeX tables. The method first constructs a structural sketch and row/column summaries, and then performs task-driven reasoning over this intermediate representation in the Solving Stage. To further enhance reliability, we design a verification module that validates extracted structures via targeted inspections, reducing error propagation and ensuring trustworthy inputs for downstream reasoning. Extensive experiments on two spreadsheet datasets demonstrate the effectiveness of our approach. With GPT-OSS-120B, SpreadsheetAgent achieves 38.16% on Spreadsheet Bench, outperforming the ChatGPT Agent baseline (35.27%) by 2.89 absolute points. These results highlight the potential of SpreadsheetAgent to advance robust and scalable spreadsheet understanding in real-world applications. Code is available at https://github.com/renhouxing/SpreadsheetAgent .

## 13. MuBench: Assessment of Multilingual Capabilities of Large Language Models Across 61 Languages

- Authors: Wenhan Han, Yifan Zhang, Zhixun Chen, Binbinliu, Mykola Pechenizkiy, Meng Fang, Yin Zheng
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.5548350062515657
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.794/
- PDF: https://aclanthology.org/2026.findings-acl.794.pdf
- Local PDF: pdf/2026-11-13_13_MuBench_ Assessment of Multilingual Capabilities of Large Language Models Across 61 Languages.pdf

Multilingual large language models (LLMs) are advancing rapidly, with new models frequently claiming support for an increasing number of languages. However, existing evaluation datasets are limited and lack cross-lingual alignment, leaving assessments of multilingual capabilities fragmented in both language and skill coverage. To address this, we introduce MuBench, a benchmark covering 61 languages with 3.9M samples and evaluating a broad range of capabilities. We evaluate several state-of-the-art multilingual LLMs and find notable gaps between claimed and actual language coverage, particularly a persistent performance disparity between English and low-resource languages. Leveraging MuBench’s alignment, we propose Multilingual Consistency (MLC) as a complementary metric to accuracy for analyzing performance bottlenecks and guiding model improvement. MuBench provides flexible evaluation formats, including mixed-language testing. Experimental results show that increasing model size does not improve its ability to handle mixed-language contexts. We recruited human experts to evaluate translation quality and cultural sensitivity for 34k samples across 17 languages, and combined these assessments with an LLM-as-a-Judge approach to ensure overall data quality in low resource languages.

## 14. Remember Me, Refine Me: A Dynamic Procedural Memory Framework for Experience-Driven Agent Evolution

- Authors: Zouying Cao, Jiaji Deng, Li Yu, Weikang Zhou, Zhaoyang Liu, Bolin Ding, Hai Zhao
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.554057446007083
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.829/
- PDF: https://aclanthology.org/2026.findings-acl.829.pdf
- Local PDF: pdf/2026-11-13_14_Remember Me, Refine Me_ A Dynamic Procedural Memory Framework for Experience-Driven Agent Evolution.pdf

Procedural memory enables large language model (LLM) agents to internalize ”how-to” knowledge and thus reduce redundant trial-and-error. However, existing frameworks predominantly suffer from a ”passive accumulation” paradigm, treating memory as a static append-only archive. To bridge the gap between static storage and dynamic reasoning, we propose ReMe (Remember Me, Refine Me), a comprehensive framework for experience-driven agent evolution. ReMe manages the memory lifecycle via three mechanisms: 1) multi-faceted distillation, which extracts fine-grained experiences by recognizing success patterns, analyzing failure triggers and generating comparative insights; 2) context-adaptive reuse, which tailors historical insights to new contexts through scenario-aware indexing; and 3) utility-based refinement, which automatically adds validated memories and prunes outdated ones to maintain a compact, high-quality experience pool. Experiments on BFCL-V3 and AppWorld demonstrate that ReMe establishes a new state-of-the-art in agent memory system. Crucially, we observe a significant memory-scaling effect: Qwen3-8B equipped with ReMe outperforms larger, memoryless Qwen3-14B, indicating that self-evolving memory provides a computation-efficient path for lifelong learning.

## 15. Do Personality Traits Interfere? Geometric Limitations of Steering in Large Language Models

- Authors: Pranav Bhandari, Usman Naseem, Mehwish Nasim
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.5540179256523854
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1463/
- PDF: https://aclanthology.org/2026.findings-acl.1463.pdf
- Local PDF: pdf/2026-11-13_15_Do Personality Traits Interfere_ Geometric Limitations of Steering in Large Language Models.pdf

Personality steering in large language models (LLMs) commonly relies on injecting trait-specific steering vectors, implicitly assuming that personality traits can be controlled independently. In this work, we examine whether this assumption holds by analysing the geometric relationships between Big Five personality steering directions. We study steering vectors extracted from two model families (LLaMA-3-8B and Mistral-8B) and apply a range of geometric conditioning schemes, from unconstrained directions to soft and hard orthonormalisation. Our results show that personality steering directions exhibit substantial geometric dependence: steering one trait consistently induces changes in others, even when linear overlap is explicitly removed. While hard orthonormalisation enforces geometric independence, it does not eliminate cross-trait behavioural effects and can reduce steering strength. These findings suggest that personality traits in LLMs occupy a slightly coupled subspace, limiting fully independent trait control.

## 16. CE-GPPO: Coordinating Entropy via Gradient-Preserving Clipping Policy Optimization in Reinforcement Learning

- Authors: Zhenpeng Su, Leiyu Pan, Minxuan Lv, Yuntao Li, Wenping Hu, Fuzheng Zhang, Kun Gai, Guorui Zhou
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.553846616158995
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1752/
- PDF: https://aclanthology.org/2026.acl-long.1752.pdf
- Local PDF: pdf/2026-11-13_16_CE-GPPO_ Coordinating Entropy via Gradient-Preserving Clipping Policy Optimization in Reinforcement Learning.pdf

Reinforcement learning (RL) has become a powerful paradigm for optimizing large language models (LLMs) to handle complex reasoning tasks. A core challenge in this process lies in managing policy entropy, which reflects the balance between exploration and exploitation during training. Existing methods, such as proximal policy optimization (PPO) and its variants, discard valuable gradient signals from low-probability tokens due to the clipping mechanism. We systematically analyze the entropy dynamics and reveal that these clipped tokens play a critical yet overlooked role in regulating entropy evolution. We propose Coordinating Entropy via Gradient-Preserving Policy Optimization (CE-GPPO), a novel algorithm that reintroduces gradients from clipped tokens in native PPO in a gentle and bounded manner. By controlling the magnitude of gradients from tokens outside the clipping interval, CE-GPPO is able to achieve an exploration-exploitation trade-off. We provide theoretical justification and empirical evidence showing that CE-GPPO effectively mitigates entropy instability. Extensive experiments on mathematical reasoning benchmarks show that CE-GPPO consistently outperforms strong baselines across different model scales.

## 17. ♪ Something Just Like TRuST ♪ *: Toxicity Recognition of Span and Target

- Authors: Berk Atıl, Namrata Sureddy, Rebecca J. Passonneau
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.5537396784328434
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1854/
- PDF: https://aclanthology.org/2026.findings-acl.1854.pdf
- Local PDF: pdf/2026-11-13_17_♪ Something Just Like TRuST ♪ __ Toxicity Recognition of Span and Target.pdf

Toxic language includes content that is offensive, abusive, or that promotes harm. Progress in preventing toxic output from large language models (LLMs) is hampered by inconsistent definitions of toxicity. We introduce TRuST, a large-scale dataset that unifies and expands prior resources through a carefully synthesized definition of toxicity, and corresponding annotation scheme. It consists of ∼300k annotations, with high-quality human annotation on ∼11k. To ensure high-quality, we designed a rigorous, multi-stage human annotation process, and evaluated the diversity of the annotators. Then we benchmarked state-of-the-art LLMs and pre-trained models on three tasks: toxicity detection, identification of the target group, and of toxic words. Our results indicate that fine-tuned PLMs outperform LLMs on the three tasks, and that current reasoning models do not reliably improve performance. TRuST constitutes one of the most comprehensive resources for evaluating and mitigating LLM toxicity, and other research in socially-aware and safer language technologies.

## 18. Failure makes the agent stronger: Enhancing Accuracy through Structured Reflection for Reliable Tool Interactions

- Authors: Junhao Su, Yuanliang Wan, Junwei Yang, Hengyu Shi, Tianyang Han, Yurui Qiu, Junfeng Luo
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.5533299090317496
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.618/
- PDF: https://aclanthology.org/2026.findings-acl.618.pdf
- Local PDF: pdf/2026-11-13_18_Failure makes the agent stronger_ Enhancing Accuracy through Structured Reflection for Reliable Tool Interactions.pdf

Tool-augmented large language models (LLMs) are typically trained via supervised imitation learning or coarse-grained reinforcement learning, approaches that primarily optimize one-shot tool calls. Existing practices of self-reflection largely rely on heuristic prompting or unidirectional reasoning traces: the model is encouraged to “think more,” rather than to treat error diagnosis and correction as a learnable capability. This makes them fragile in multi-turn interaction settings—once a call fails, the model tends to repeat the same mistake instead of recovering. To address this issue, we propose structured reflection, which transforms the “from error to repair” process into a first-class, controllable, and trainable action. The agent produces a concise yet precise reflection process: specifically, the model diagnoses the error based on evidence from the previous step and then proposes a correct and executable follow-up call. During training, we combine DAPO and GSPO’s objective functions and design a more principled reward mechanism tailored to tool calling, optimizing the stepwise strategy Reflect → Call → Final. To evaluate this capability, we introduce Tool-Reflection-Bench, a lightweight benchmark dataset that programmatically verifies structural validity, executability, parameter correctness, and result consistency. Tasks in the benchmark are constructed as miniature trajectories of Erroneous Call → Reflection → Corrected Call and are split into disjoint training and testing sets. Experiments on BFCL v3 and Tool-Reflection-Bench show that our method achieves significant improvements in multi-turn tool-call success rates and error recovery, while also reducing redundant calls. These results demonstrate that making reflection explicit and treating it as an optimization objective can substantially enhance the reliability of tool interaction, providing a reproducible pathway for agents to grow stronger by learning from failure. We will release all the code and datasets as open source once the paper is accepted by the community.

## 19. Confidence over Time: Confidence Calibration with Temporal Logic for Large Language Model Reasoning

- Authors: Zhenjiang Mao, Anirudhh Venkat, Artem Bisliouk, Sindhura Kumbakonam Subramanian, Akshat Kothiyal, Saithej Singhu, Ivan Ruchkin
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.5531384694131303
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.484/
- PDF: https://aclanthology.org/2026.findings-acl.484.pdf
- Local PDF: pdf/2026-11-13_19_Confidence over Time_ Confidence Calibration with Temporal Logic for Large Language Model Reasoning.pdf

Large Language Models (LLMs) increasingly rely on long-form, multi-step reasoning to solve complex tasks such as mathematical problem solving and scientific question answering. Despite strong performance, existing confidence estimation methods typically reduce an entire reasoning process to a single scalar score, ignoring how confidence evolves throughout the generation. As a result, these methods are often sensitive to superficial factors such as response length or verbosity, and struggle to distinguish correct reasoning from confidently stated errors. We propose to characterize the stepwise confidence signal using Signal Temporal Logic (STL). Using a discriminative STL mining procedure, we discover temporal formulas that distinguish confidence signals of correct and incorrect responses. Our analysis found that the STL patterns generalize across tasks, and numeric parameters exhibit sensitivity to individual questions. Based on these insights, we develop a confidence estimation approach that informs STL blocks with parameter hypernetworks. Experiments on multiple reasoning tasks show our confidence scores are more calibrated than the baselines.

## 20. Stroke Patches: Customizable Artistic Image Styling Using Regression

- Authors: Jaffray, Ian, Bronskill, John
- Source: neurips
- Venue type: conference
- Journal: NeurIPS 2025
- Publication status: formally_published
- Publication date: 2026-08-14
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.5530691855736936
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://proceedings.neurips.cc/paper_files/paper/2025/hash/afcb54794b58913b166518f91b094305-Abstract-Creative_AI_Track.html
- PDF: https://proceedings.neurips.cc/paper_files/paper/2025/file/afcb54794b58913b166518f91b094305-Paper-Creative_AI_Track.pdf
- Local PDF: pdf/2026-11-13_20_Stroke Patches_ Customizable Artistic Image Styling Using Regression.pdf

We present a novel, regression-based method for artistically styling images. Unlike recent neural style transfer or diffusion-based approaches, our method allows for explicit control over the stroke composition and level of detail in the rendered image through the use of an extensible set of stroke patches. The stroke patch sets are procedurally generated by small programs that control the shape, size, orientation, density, color, and noise level of the strokes in the individual patches. Once trained on a set of stroke patches, a U-Net based regression model can render any input image in a variety of distinct, evocative and customizable styles.

## 21. LLaDA 1.5: Variance-Reduced Preference Optimization for Large Language Diffusion Models

- Authors: Fengqi Zhu, Rongzhen Wang, Shen Nie, Xiaolu Zhang, Chunwei Wu, Jun Zhou, Yankai Lin, Ji-Rong Wen, Chongxuan Li
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.5528842722297047
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.524/
- PDF: https://aclanthology.org/2026.acl-long.524.pdf
- Local PDF: pdf/2026-11-13_21_LLaDA 1.5_ Variance-Reduced Preference Optimization for Large Language Diffusion Models.pdf

Masked diffusion language models present a promising paradigm for language modeling, yet the systematic theoretical analysis and comprehensive empirical validation of their alignment on general tasks remain relatively underexplored. In this paper, we identify the primary challenge for this problem: the high variance in Evidence Lower Bound (ELBO)-based likelihood estimates required for preference optimization. To address this issue, we propose Variance-Reduced Preference Optimization (VRPO), a framework that formally analyzes the bias and variance of the preference optimization loss and gradient based on Direct Preference Optimization, showing both are governed by a score-estimator variance. Building on this foundation, we introduce multiple unbiased variance reduction strategies, including optimal budget allocation and antithetic sampling, to improve alignment performance. We demonstrate the effectiveness of VRPO by applying it to LLaDA, a large diffusion language model. The resulting model, LLaDA 1.5, consistently outperforms its SFT-only predecessor consistently across various general benchmarks, such as mathematics (GSM8K +4.7), coding (HumanEval +3.0, MBPP +1.8), and alignment (IFEval +4.0, Arena-Hard +4.3). Furthermore, LLaDA 1.5 demonstrates a highly competitive mathematical performance compared to other strong language MDMs and ARMs. Our model is available at https://huggingface.co/GSAI-ML/LLaDA-1.5 .

## 22. SQLAgent: Learning to Explore Before Generating as a Data Engineer

- Authors: Wenjia Jiang, Yiwei Wang, Boyan Han, Joey Tianyi Zhou, Chi Zhang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.5524018376977913
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1959/
- PDF: https://aclanthology.org/2026.findings-acl.1959.pdf
- Local PDF: pdf/2026-11-13_22_SQLAgent_ Learning to Explore Before Generating as a Data Engineer.pdf

Large Language Models have recently shown impressive capabilities in reasoning and code generation, making them promising tools for natural language interfaces to relational databases. However, existing approaches often fail to generalize in complex, real-world settings due to the highly database-specific nature of SQL reasoning, which requires deep familiarity with unique schemas, ambiguous semantics, and intricate join paths. To address this challenge, we introduce a novel two-stage LLM-based framework that decouples knowledge acquisition from query generation. In the Exploration Stage, the system autonomously constructs a database-specific knowledge base by navigating the schema with a Monte Carlo Tree Search–inspired strategy, generating triplets of schema fragments, executable queries, and natural language descriptions as usage examples. In the Deployment Stage, a dual-agent system leverages the collected knowledge as in-context examples to iteratively retrieve relevant information and generate accurate SQL queries in response to user questions. This design enables the agent to proactively familiarize itself with unseen databases and handle complex, multi-step reasoning. Extensive experiments on large-scale benchmarks demonstrate that our approach significantly improves accuracy over strong baselines, highlighting its effectiveness and generalizability.

## 23. Beyond Rejection Sampling: Trajectory Fusion for Scaling Mathematical Reasoning

- Authors: Jie Deng, Hanshuang Tong, Jun Li, Shining Liang, Ning Wu, Hongzhi Li, Yutao Xie
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.5523254002317852
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.390/
- PDF: https://aclanthology.org/2026.findings-acl.390.pdf
- Local PDF: pdf/2026-11-13_23_Beyond Rejection Sampling_ Trajectory Fusion for Scaling Mathematical Reasoning.pdf

Large language models (LLMs) have made impressive strides in mathematical reasoning, often fine-tuned using rejection sampling, which retains only correct reasoning trajectories. While effective, this paradigm treats supervision as a binary filter that systematically excludes teacher-generated errors, leaving a gap in how reasoning failures are modeled during training. In this paper, we propose TrajFusion, a fine-tuning strategy that reframes rejection sampling as a structured supervision construction process. Specifically, TrajFusion forms fused trajectories that explicitly model trial-and-error reasoning by interleaving selected incorrect trajectories with reflection prompts and correct trajectories. The length of the fused sample is adaptively controlled based on the frequency and diversity of teacher errors, providing richer supervision for challenging problems while safely reducing to vanilla rejection sampling fine-tuning (RFT) when error signals are uninformative. TrajFusion requires no changes to the architecture or training objective. Extensive experiments across multiple math benchmarks demonstrate that TrajFusion consistently outperforms RFT, particularly on challenging and long-form reasoning problems.

## 24. Beyond the Context Window: Scaling Agentic RL via End-to-end Optimized Context Compression

- Authors: Miao Lu, Weiwei Sun, Weihua Du, Zhan Ling, Xuesong Yao, Kang Liu, Jiecao Chen
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.551819576438032
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.966/
- PDF: https://aclanthology.org/2026.acl-long.966.pdf
- Local PDF: pdf/2026-11-13_24_Beyond the Context Window_ Scaling Agentic RL via End-to-end Optimized Context Compression.pdf

We study reinforcement learning (RL) fine-tuning of large language model (LLM) agents for long-horizon multi-turn tool use, where context length quickly becomes a fundamental bottleneck. Existing multi-turn RL pipelines suffer from degraded instruction following, excessive rollout costs, and most importantly, strict context limits. In this work, to address these challenges, we introduce summarization-based context management to training . In specific, it periodically compresses the tool using history by LLM-generated summaries that retain task-relevant information to keep a compact context while enabling the agent to scale beyond the fixed context window. Building on this formulation, we derive a policy gradient representation that seamlessly enables standard LLM RL infrastructures to optimize both tool-use behaviors as well as summarization strategies in an end-to-end fashion. We instantiate this framework with SUmmarization augmented Policy Optimization (SUPO), an LLM RL algorithm that enables long-horizon training beyond a fixed context limit. Experiments on interactive function calling and searching tasks demonstrate that SUPO significantly improves the success rate while maintaining the same or even lower working context length compared to baselines. We also demonstrate that for complex searching tasks SUPO can further improve the evaluation performance when scaling test-time maximum round of summarization beyond that of training time.

## 25. Interpretability of LLM Classifiers via the Rational Inattention Theory with Application to Hate Speech Detection

- Authors: Yuan Zhao, Ali Abdi
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.5517920377517465
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-srw.23/
- PDF: https://aclanthology.org/2026.acl-srw.23.pdf
- Local PDF: pdf/2026-11-13_25_Interpretability of LLM Classifiers via the Rational Inattention Theory with Application to Hate Speech Detection.pdf

Hate speech detection is essential for maintaining healthy online communities. Large language models (LLMs) perform well on text classification, yet their decision strategies need to be better understood. While post-hoc rationales can justify individual decisions, they substantially increase inference cost and limit scalability in high-throughput settings. As another approach, we propose an extended rational inattention model that parameterizes linguistic noise and information processing cost, providing an interpretable behavioral framework for black-box LLM classifiers. Treating LLMs as rational decision-makers under information constraints allows us to estimate - from the observed classification behavior - the parameters that represent information processing cost and noise sensitivity. As a case study and using a hate-speech dataset spanning multiple noise environments, we evaluate four commercial LLMs and show that the introduced extended rational inattention model predictions closely match the observed performance across different noise levels. We further test the performance under various noise mechanisms and find that the inferred information cost parameters remain consistent while the noise parameters vary with the distortion mechanism. Overall, our introduced framework offers a cost-efficient and quantitative approach to derive interpretable indices of LLM moderation behavior and decisions, without additional rationale generation.

## 26. Knowledge is Not Enough: Injecting RL Skills for Continual Adaptation

- Authors: Pingzhi Tang, Yiding Wang, Muhan Zhang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.5514511964149915
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.550/
- PDF: https://aclanthology.org/2026.acl-long.550.pdf
- Local PDF: pdf/2026-11-13_26_Knowledge is Not Enough_ Injecting RL Skills for Continual Adaptation.pdf

Large Language Models (LLMs) face the “knowledge cutoff” challenge, where their frozen parametric memory prevents direct internalization of new information. While Supervised Fine-Tuning (SFT) is commonly used to update model knowledge, it often updates factual content without reliably improving the model’s ability to use the newly incorporated information for question answering or decision-making. Reinforcement Learning (RL) is essential for acquiring reasoning skills; however, its high computational cost makes it impractical for efficient online adaptation. We empirically observe that the parameter updates induced by SFT and RL are nearly orthogonal. Based on this observation, we propose Parametric Skill Transfer (PaST) , a framework that supports modular skill transfer for efficient and effective knowledge adaptation. By extracting a domain-agnostic Skill Vector from a source domain, we can linearly inject knowledge manipulation skills into a target model after it has undergone lightweight SFT on new data. Experiments on knowledge-incorporation QA (SQuAD, LooGLE) and agentic tool-use benchmarks (ToolBench) demonstrate the effectiveness of our method. On SQuAD, PaST outperforms the state-of-the-art self-editing SFT baseline by up to 9.9 points. PaST further scales to long-context QA on LooGLE with an 8.0-point absolute accuracy gain, and improves zero-shot ToolBench success rates by +10.3 points on average with consistent gains across tool categories, indicating strong scalability and cross-domain transferability of the Skill Vector.

## 27. Selective Knowledge Distillation: Fusing LLM Semantic Strengths with DNN Efficiency for Binary Code Similarity Detection

- Authors: Shize Zhou, Peiyu Liu, Lirong Fu, Tong Ye, Wenhai Wang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.550698349283345
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1193/
- PDF: https://aclanthology.org/2026.acl-long.1193.pdf
- Local PDF: pdf/2026-11-13_27_Selective Knowledge Distillation_ Fusing LLM Semantic Strengths with DNN Efficiency for Binary Code Similarity Detection.pdf

Binary Code Similarity Detection (BCSD) plays a vital role in various security applications, including vulnerability identification, malware analysis, and code plagiarism detection. With the growing adoption of deep neural networks (DNNs), substantial progress has been made in recognizing and classifying similar code segments. However, DNN-based BCSD methods often exhibit low accuracy and robustness because they struggle to capture fine-grained and high-level program semantics. In contrast, such semantics are typically captured through natural language interpretations of source code by large language models (LLMs). Yet, LLM-based BCSD methods are constrained by their large model sizes and high inference latency. To alleviate these limitations, this paper proposes BinSKD. The key idea is to leverage an LLM-based BCSD method as the teacher model and transfer its knowledge of high-level program semantics to various DNN-based student models. Specifically, to avoid propagating errors from the teacher to the student, we introduce selective distillation, selecting targets with accurate semantics according to their detection retrieval. In addition, to mitigate the noise introduced by a number of negative samples during distillation, we further propose discrepancy-weighted sampling to focus on the sampleswhere the student’s prediction notably deviates from the teacher’s. Our experiments show that BinSKD yields Recall@1 improvements of 14.5%–91.2% for DNN-based BCSD methods and enables HermesSim to match the teacher’s performance with orders-of-magnitude efficiency.

## 28. Analyzing Prompt Design Choices in Biomedical Information Extraction for Low-Resource Languages

- Authors: Ayesha Khatun, Kadir Bulut Ozler, Steven Bethard, Egoitz Laparra
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.550531741437924
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.bionlp-1.4/
- PDF: https://aclanthology.org/2026.bionlp-1.4.pdf
- Local PDF: pdf/2026-11-13_28_Analyzing Prompt Design Choices in Biomedical Information Extraction for Low-Resource Languages.pdf

This paper studies how to improve biomedical named entity recognition (NER) using large language models (LLMs), especially for low-resource languages like Bangla and Basque. The main goal is to understand how different prompt styles and output formats affect model performance. The study finds that the way we design prompts is very important. Among all methods, question-style prompting works best across all languages. It helps the model understand the biomedical task more clearly and improves accuracy. In fact, improvements are much greater in Bangla and Basque compared to high-resource languages like English and Spanish. Another key finding is about the output format. Traditional BIO tagging (labeling each word) performs poorly with LLMs because it is strict and sensitive to small errors. Instead, span-based extraction (directly extracting text phrases) works much better and gives higher F1 scores. This is because LLMs naturally generate text spans rather than token-level labels. The paper also analyzes errors. Common problems include hallucination, missing entities, and boundary mistakes. Translation-based prompts can reduce hallucination, while question-style prompts reduce empty outputs in biomedical NER. Overall, the study shows that choosing the right prompt and output format is very important, especially for low-resource high-vocabulary languages. It provides useful guidance for building better multilingual medical information extraction systems.

## 29. ReproEvalCard: A Reporting Standard for Reproducible Evaluation of LLM Pipelines

- Authors: Priyaranjan Pattnayak, Apoorv Bhatia
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.5504420966503565
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-short.22/
- PDF: https://aclanthology.org/2026.acl-short.22.pdf
- Local PDF: pdf/2026-11-13_29_ReproEvalCard_ A Reporting Standard for Reproducible Evaluation of LLM Pipelines.pdf

Evaluation of modern large language model (LLM) systems increasingly relies on multi-stage pipelines such as retrieval-augmented generation, tool-using agents, and prompt chains. Reproducing reported evaluation results for these systems often requires evaluation-specific artifacts beyond model weights and datasets, including prompts, judge configurations, retrieval snapshots, and intermediate traces, yet their availability has not been systematically examined.We introduce ReproEvalCard , a lightweight reporting standard that specifies the minimal artifacts required to reproduce and validate evaluations of LLM pipelines. To motivate this standard, we audit 55 pipeline-based LLM papers published between 2022 and 2025 and quantify the availability of reproducibility-critical evaluation artifacts. We find that randomness controls are missing in 75% of papers and intermediate execution traces in 61%, substantially limiting evaluation reproducibility. We further demonstrate ReproEvalCard through a worked example and provide a concise checklist for authors and reviewers, aiming to improve reproducibility and comparability in LLM evaluation.

## 30. MedEinst: Benchmarking the Einstellung Effect in Medical LLMs through Counterfactual Differential Diagnosis

- Authors: Wenting Chen, Guolin Huang, Wenxuan Wang, Zhongrui Zhu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.550357884143918
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1847/
- PDF: https://aclanthology.org/2026.acl-long.1847.pdf
- Local PDF: pdf/2026-11-13_30_MedEinst_ Benchmarking the Einstellung Effect in Medical LLMs through Counterfactual Differential Diagnosis.pdf

Despite achieving high accuracy on medical benchmarks, LLMs exhibit the Einstellung Effect in clinical diagnosis—relying on statistical shortcuts rather than patient-specific evidence, causing misdiagnosis in atypical cases. Existing benchmarks fail to detect this critical failure mode. We introduce MedEinst, a counterfactual benchmark with 5,383 paired clinical cases across 49 diseases. Each pair contains a control case and a “trap” case with altered discriminative evidence that flips the diagnosis. We measure susceptibility via Bias Trap Rate—probability of misdiagnosing traps despite correctly diagnosing controls. Evaluation shows frontier models achieve high baseline accuracy but severe bias trap rates. Thus, we propose ECR-Agent, aligning LLM reasoning with Evidence-Based Medicine via two components: (1) Dynamic Causal Inference (DCI) performs structured reasoning through dual-pathway perception, dynamic causal graph reasoning across three levels (association, intervention, counterfactual), and evidence audit for final diagnosis; (2) Critic-Driven Graph Memory Evolution (CGME) iteratively refines the system by storing validated reasoning paths in an exemplar base and consolidating disease-specific knowledge into evolving illness graphs. Source code is to be released.
