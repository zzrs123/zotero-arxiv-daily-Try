# Paper Daily Reading - 2026-08-02

## 1. Unify learns cellular evolution with universal multimodal embeddings

- Authors: Huawen Zhong, Wenkai Han, Guoxin Cui, David Gómez-Cabrero, Jesper Tegnér, Xin Gao, Manuel Aranda
- Source: openalex
- Venue type: journal
- Journal: Nature Communications
- Publication status: published
- Publication date: 2026-07-31
- DOI: https://doi.org/10.1038/s41467-026-76230-y
- Categories: Single-cell and spatial transcriptomics, Genomics and Phylogenetic Studies, Domain Adaptation and Few-Shot Learning
- Relevance: 3.5008584965604186
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://doi.org/10.1038/s41467-026-76230-y
- PDF: Unavailable
- Local PDF: Not downloaded

Abstract Integrating single-cell RNA-sequencing (scRNA-seq) data across species is hindered by evolutionary divergence, technical batch effects, and the reliance on one-to-one orthologs. Here, we present Unify, a transfer learning methodology that learns universal cell embeddings by defining functionally coherent, multi-modal macrogenes. This is achieved by combining RNA expression with embeddings from protein language models and general-purpose language models. Unify transcends species boundaries, enabling cross-species comparisons beyond strict gene-level homology. Unify corrects batch effects while preserving conserved biological signals across vast evolutionary distances and enables more accurate prediction of perturbation responses across species, such as from mouse to human. Applied to species separated by over 700 million years, Unify reconstructs more accurate multi-species cell-type evolutionary trees and uncovers convergent gene programs. Together, these results establish Unify as a powerful method for comparative single-cell genomics and evolutionary biology.

## 2. SpaMTP: integrative statistical analysis and visualization of spatial metabolomics and transcriptomics data

- Authors: Andrew Causer, Tianyao Lu, Jurgen Kriel, Joel J D Moffet, Christopher C. J. Fitzgerald, Andrew Newman, Hani Vu, Xiao Tan, Tuan Vo, Cedric S. Cui, Vinod K. Narayana, James R. Whittle, Sarah A. Best, Saskia Freytag, Quan Nguyen
- Source: openalex
- Venue type: journal
- Journal: Nature Methods
- Publication status: published
- Publication date: 2026-07-31
- DOI: https://doi.org/10.1038/s41592-026-03140-8
- Categories: Single-cell and spatial transcriptomics, Metabolomics and Mass Spectrometry Studies, Microbial Metabolic Engineering and Bioproduction
- Relevance: 3.4221456075101617
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://doi.org/10.1038/s41592-026-03140-8
- PDF: Unavailable
- Local PDF: Not downloaded

Spatially resolved multimodal data enable the exploration of transcriptional, proteomic and metabolic regulation, yet analytical tools to integrate these spatial omics modalities, particularly spatial metabolomics, remain limited. We developed SpaMTP, an end-to-end framework that implements functions within a common Seurat architecture. It introduces analyses for metabolite annotation, joint clustering, enrichment tests, spatial alignment, multimodal integration, visualization and seamless software interoperability. Its utility is demonstrated across different biological systems. SpaMTP enables comprehensive joint analysis of spatial metabolomics and transcriptomics data.

## 3. FADE: Probing the Limits of VLMs on fine-grained OCR

- Authors: Deep Shah, Nehal Kathrotia, Sanket Badhe
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.8459347376322346
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.alvr-main.23/
- PDF: https://aclanthology.org/2026.alvr-main.23.pdf
- Local PDF: pdf/2026-08-02_03_FADE_ Probing the Limits of VLMs on fine-grained OCR.pdf

Multimodal Large Language Models (MLLMs) have achieved remarkable success in semantic visual reasoning, yet their capacity for fine-grained, low-level perception remains critically under-evaluated. This perceptual fragility limits their reliability in noisy, real-world environments where visual signals are degraded. Furthermore, existing benchmarks often entangle visual perception with language priors, masking these underlying deficits. To address this, we introduce the FAint numeric Detection Evaluation (FADE) dataset, a novel evaluation suite designed to probe the limits of zero-shot Optical Character Recognition (OCR) in frontier MLLMs. By embedding synthetic, strictly numerical sequences over cluttered natural backgrounds at varying levels of transparency ( 𝛼 ), FADE explicitly disentangles pure visual perception from semantic predictability. We evaluate state-of-the-art models including Gemini 3.0, Claude 4.5 Sonnet, and Gemma 3 against a specialized UNet segmentation baseline. Our results reveal a striking limitation in frontier architectures: while they achieve near-perfect transcription at high visibility, their performance collapses under high transparency. Conversely, the UNet pipeline maintains robust spatial grounding, significantly outperforming generalist models at the lowest visibility thresholds. FADE provides a reproducible dataset to expose and diagnose the perceptual breakage points of modern multimodal systems.

## 4. ASTRA: Adaptive Semantic Tree Reasoning Architecture for Complex Table Question Answering

- Authors: Xiaoke Guo, Songze Li, Zhiqiang Liu, Zhaoyan Gong, Yuanxiang Liu, Huajun Chen, Wen Zhang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.8412628112530633
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1090/
- PDF: https://aclanthology.org/2026.acl-long.1090.pdf
- Local PDF: pdf/2026-08-02_04_ASTRA_ Adaptive Semantic Tree Reasoning Architecture for Complex Table Question Answering.pdf

Table serialization remains a critical bottleneck for Large Language Models (LLMs) in complex table question answering, hindered by challenges such as structural neglect, representation gaps, and reasoning opacity. Existing serialization methods fail to capture explicit hierarchies and lack schema flexibility, while current tree-based approaches suffer from limited semantic adaptability. To address these limitations, we propose ASTRA ( A daptive S emantic T ree R easoning A rchitecture) including two main modules, AdaSTR and DuTR . First, we introduce AdaSTR , which leverages the global semantic awareness of LLMs to reconstruct tables into Logical Semantic Trees. This serialization explicitly models hierarchical dependencies and employs an adaptive mechanism to optimize construction strategies based on table scale. Second, building on this structure, we present DuTR , a dual-mode reasoning framework that integrates tree-search-based textual navigation for linguistic alignment and symbolic code execution for precise verification. Experiments on complex table benchmarks demonstrate that our method achieves state-of-the-art (SOTA) performance.

## 5. Calibrated Speculative Decoding: Frequency-Guided Candidate Selection for Efficient Inference

- Authors: Zhouxuwen, Fangxin Liu, Chao Wang, Xiao Zheng, Hao Zheng, Min He, Li Jiang, Haibing Guan
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.836720606018911
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1369/
- PDF: https://aclanthology.org/2026.acl-long.1369.pdf
- Local PDF: pdf/2026-08-02_05_Calibrated Speculative Decoding_ Frequency-Guided Candidate Selection for Efficient Inference.pdf

Speculative decoding accelerates autoregressive generation by letting draft tokens bypass full verification, but conventional frameworks suffer from frequent false rejections, particularly when draft models produce semantically correct but lexically divergent outputs. In this paper, we present Calibrated Speculative Decoding (CSD), a training-free framework that recovers valid tokens discarded by standard verification. Guided by the principle of “Frequency-Guided Candidate Selection and Probability-Guarded Acceptance,” CSD incorporates two lightweight modules: Online Correction Memory, which aggregates historical rejections to propose recurring divergence patterns as rescue candidates, and Semantic Consistency Gating, which verifies candidate admissibility using probability ratios instead of exact token matching. Our evaluation across diverse large language models demonstrates that CSD outperforms existing methods, achieving a peak throughput speedup of 2.33x. CSD preserves model accuracy across all tasks while further boosting performance on complex reasoning datasets. These results establish CSD as a highly effective, lightweight solution for practical LLM deployments.

## 6. MemRec: Collaborative Memory-Augmented Agentic Recommender System

- Authors: Weixin Chen, Yuhan Zhao, Jingyuan Huang, Zihe Ye, Mingxuan Ju, Tong Zhao, Neil Shah, Li Chen, Yongfeng Zhang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.836412758575663
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.2061/
- PDF: https://aclanthology.org/2026.acl-long.2061.pdf
- Local PDF: pdf/2026-08-02_06_MemRec_ Collaborative Memory-Augmented Agentic Recommender System.pdf

The evolution of recommender systems has shifted from traditional collaborative filtering to LLM-based agentic systems, which rely on semantic user and item memories to make predictions. However, existing agents maintain these memories in isolation. This overlooks crucial collaborative signals, such as user-item co-engagements and peer relationships across the community, which significantly limits their ability to uncover hidden preferences and accurately infer user needs, particularly for data-sparse users. To bridge this gap, we introduce collaborative memory, a paradigm that connects isolated semantics to enable the sharing of relational insights. Yet, naively utilizing collaborative memory causes severe context overload and introduces noise to downstream LLMs, alongside prohibitive computational costs. To resolve this, we propose MemRec, a framework that architecturally decouples memory management from reasoning. MemRec introduces a dedicated, lightweight language model LM_Mem to efficiently manage and synthesize a dynamic collaborative memory graph in the background. It provides only distilled, high-signal contexts to a downstream, heavyweight large language model (LLM_Rec) for the final recommendation. Extensive experiments on four benchmarks demonstrate that MemRec achieves state-of-the-art performance. Code: https://github.com/rutgerswiselab/memrecHomepage: https://memrec.weixinchen.com

## 7. STAR-Teaming: A Strategy-Response Multiplex Network Approach to Automated LLM Red Teaming

- Authors: Min Jae Jung, YongTaek Lim, Chaeyun Kim, Junghwan Kim, Kihyun Kim, Minwoo Kim
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.834357070942686
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1470/
- PDF: https://aclanthology.org/2026.findings-acl.1470.pdf
- Local PDF: pdf/2026-08-02_07_STAR-Teaming_ A Strategy-Response Multiplex Network Approach to Automated LLM Red Teaming.pdf

While Large Language Models (LLMs) are widely used, they remain susceptible to jailbreak prompts that can elicit harmful or inappropriate responses. This paper introduces STAR-Teaming, a novel black-box framework for automated red teaming that effectively generates such prompts. STAR-Teaming integrates a Multi-Agent System (MAS) with a Strategy-Response Multiplex Network and employs network-driven optimization to sample effective attack strategies. This network-based approach recasts the intractable high-dimensional embedding space into a tractable structure, yielding two key advantages: it enhances the interpretability of the LLM’s strategic vulnerabilities, and it streamlines the search for effective strategies by organizing the search space into semantic communities, thereby preventing redundant exploration. Empirical results demonstrate that STAR-Teaming significantly surpasses existing methods, achieving a higher attack success rate (ASR) at a lower computational cost. Extensive experiments validate the effectiveness and explainability of the Multiplex Network. The code is available at https://github.com/selectstar-ai/STAR-Teaming-paper .

## 8. Purging the Gray Zone: Latent-Geometric Denoising for Precise Knowledge Boundary Awareness

- Authors: Hao An, Yibin Lou, Jiayi Guo, Yang Xu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.833483309807497
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.122/
- PDF: https://aclanthology.org/2026.findings-acl.122.pdf
- Local PDF: pdf/2026-08-02_08_Purging the Gray Zone_ Latent-Geometric Denoising for Precise Knowledge Boundary Awareness.pdf

Large language models (LLMs) often exhibit hallucinations due to their inability to accurately perceive their own knowledge boundaries. Existing abstention fine-tuning methods typically partition datasets directly based on response accuracy, causing models to suffer from severe label noise near the decision boundaries and consequently exhibit high rates of abstentions or hallucinations. This paper adopts a latent space representation perspective, revealing a “gray zone” near the decision hyperplane where internal belief ambiguity constitutes the core performance bottleneck. Based on this insight, we propose the GeoDe ( Geo metric De noising) framework for abstention fine-tuning. This method constructs a truth hyperplane using linear probes and performs “geometric denoising” by employing geometric distance as a confidence signal for abstention decisions. This approach filters out ambiguous boundary samples while retaining high-fidelity signals for fine-tuning. Experiments across multiple models (Llama3, Qwen3) and benchmark datasets (TriviaQA, NQ, SciQ, SimpleQA) demonstrate that GeoDe significantly enhances model truthfulness and demonstrates strong generalization in out-of-distribution (OOD) scenarios. Code is available at https://github.com/Notbesidemoon/GeoDe .

## 9. MetaMem: Evolving Meta-Memory for Knowledge Utilization through Self-Reflective Symbolic Optimization

- Authors: Haidong Xin, Xinze Li, Zhenghao Liu, Yukun Yan, Shuo Wang, Cheng Yang, Yu Gu, Ge Yu, Maosong Sun
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.8325749045923794
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.270/
- PDF: https://aclanthology.org/2026.findings-acl.270.pdf
- Local PDF: pdf/2026-08-02_09_MetaMem_ Evolving Meta-Memory for Knowledge Utilization through Self-Reflective Symbolic Optimization.pdf

Existing memory systems enable Large Language Models (LLMs) to support long-horizon human-LLM interactions by persisting historical interactions beyond limited context windows. However, while recent approaches have succeeded in constructing effective memories, they often disrupt the inherent logical and temporal relationships within interaction sessions, resulting in fragmented memory units and degraded reasoning performance. In this paper, we propose MetaMem, a novel framework that augments memory systems with a self-evolving meta-memory, aiming to teach LLMs how to effectively utilize memorized knowledge. During meta-memory optimization, MetaMem iteratively distills transferable knowledge utilization experiences across different tasks by self-reflecting on reasoning processes and performing actions to update the current meta-memory state. The accumulated meta-memory units serve as explicit knowledge utilization experiences, guiding the LLM to systematically identify and integrate critical evidence from scattered memory fragments. Extensive experiments demonstrate the effectiveness of MetaMem, which significantly outperforms strong baselines by over 3.6%. All codes and datasets are available at https://github.com/OpenBMB/MetaMem .

## 10. MARCH: Multi-Agent Reinforced Check for Hallucination

- Authors: Zhuo Li, Yupeng Zhang, Pengyu Cheng, Jiajun Song, Mengyu Zhou, Hao Li, Shujie Hu, Yu Qin, Erchao Zhao, Xiaoxi Jiang, Guanjun Jiang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.832017099197528
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1828/
- PDF: https://aclanthology.org/2026.acl-long.1828.pdf
- Local PDF: pdf/2026-08-02_10_MARCH_ Multi-Agent Reinforced Check for Hallucination.pdf

Hallucination remains a critical bottleneck for large language models (LLMs), undermining their reliability in real-world applications, especially in Retrieval-Augmented Generation (RAG) systems. While existing hallucination detection methods employ LLM-as-a-judge to verify LLM outputs against retrieved evidence, they suffer from inherent confirmation bias , where the verifier inadvertently reproduces the errors of the original generation. To address this, we introduce M ulti- A gent R einforced self- C heck for H allucination (MARCH), a framework that enforces rigorous factual alignment by leveraging deliberate information asymmetry . MARCH orchestrates a collaborative pipeline of three specialized agents: a Solver, a Proposer, and a Checker. The Solver generates an initial RAG response, which the Proposer decomposes into claim-level verifiable atomic propositions. Crucially, the Checker validates these propositions against retrieved evidence in isolation, deprived of the Solver’s original output. This well-crafted information asymmetry scheme breaks the cycle of self-confirmation bias. By training this pipeline with multi-agent reinforcement learning (MARL), we enable the agents to co-evolve and optimize factual adherence. Extensive experiments across hallucination benchmarks demonstrate that MARCH substantially reduces hallucination rates. Notably, an 8B-parameter LLM equipped with MARCH achieves performance competitive with powerful closed-source models. MARCH paves a scalable path for factual self-improvement of LLMs through co-evolution. The code is at https://github.com/Qwen-Applications/MARCH .

## 11. Generalizable Prompt Tuning for Audio-Language Models via Semantic Expansion

- Authors: Jaehyuk Jang, Wonjun Lee, Kangwook Ko, Changick Kim
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.830699000034731
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1583/
- PDF: https://aclanthology.org/2026.findings-acl.1583.pdf
- Local PDF: pdf/2026-08-02_11_Generalizable Prompt Tuning for Audio-Language Models via Semantic Expansion.pdf

Prompt tuning has achieved remarkable progress in vision–language models (VLMs) and is recently being adopted for audio–language models (ALMs). However, its generalization ability in ALMs remains largely underexplored. We observe that conventional prompt tuning for ALMs also suffers from the Base–New Tradeoff, and we identify that this issue stems from the disrupted semantic structure of the embedding space. To address this issue, we propose Semantically Expanded Prompt Tuning (SEPT)—a plug-and-play framework that explicitly regularizes the prompt embedding space by incorporating semantic neighbors generated by large language models. SEPT introduces a novel semantic expansion loss with margin constraints that promote intra-class compactness and inter-class separability, thereby enhancing the semantic structure of the prompt embedding space. For comprehensive evaluation, we establish the first benchmark setup for prompt generalization in ALMs, covering both base-to-new generalization and cross-dataset transferability. Extensive experiments demonstrate that SEPT consistently improves generalization performance across multiple prompt tuning baselines, while maintaining computational cost during inference.

## 12. FusionFlow: Enabling Deep Structural Exploration for Automated Agentic Workflow Generation

- Authors: Xiang Wang, Zongtao Yang, Zhuojian Hong, Shuhao Zhang, Wei Wei
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.8306626823558476
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1278/
- PDF: https://aclanthology.org/2026.acl-long.1278.pdf
- Local PDF: pdf/2026-08-02_12_FusionFlow_ Enabling Deep Structural Exploration for Automated Agentic Workflow Generation.pdf

Agentic workflows are commonly used to guide large language models in solving complex reasoning tasks. However, existing automated workflow generation methods primarily rely on stepwise local refinement or tree-based search over a single evolving workflow. Under limited optimization budgets, this paradigm constrains structural depth, hindering the discovery of workflows that require deep compositional structure. To address this limitation, we propose FusionFlow, a framework centered on workflow fusion. Unlike incremental refinement, fusion enables structural leaps by synthesizing multiple independently evolved workflows, allowing exploration of deeper regions of the workflow space within a finite budget. To make fusion effective, FusionFlow integrates local optimization, task-specific differentiation, and a dynamic scheduling mechanism. Experiments on six reasoning benchmarks demonstrate that FusionFlow consistently outperforms existing automated workflow generation methods. Further ablation and analysis confirm that fusion is the key driver of deep structural exploration, highlighting fusion-driven exploration as an effective approach for overcoming depth limitations in automated workflow generation.

## 13. Efficient Low-Resource Language Adaptation via Multi-Source Dynamic Logit Fusion

- Authors: Chen Zhang, Jiuheng Lin, Zhiyuan Liao, Yansong Feng
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.8301849400650756
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.207/
- PDF: https://aclanthology.org/2026.acl-long.207.pdf
- Local PDF: pdf/2026-08-02_13_Efficient Low-Resource Language Adaptation via Multi-Source Dynamic Logit Fusion.pdf

Adapting large language models (LLMs) to low-resource languages (LRLs) is constrained by the scarcity of task data and computational resources. Although Proxy Tuning offers a logit-level strategy for introducing scaling effects, it often fails in LRL settings because the large model’s weak LRL competence might overwhelm the knowledge of specialized smaller models. We thus propose TriMix, a test-time logit fusion framework that dynamically balances capabilities from three different sources: LRL competence from a continually pretrained small model, task competence from high-resource language instruction tuning, and the scaling benefits of large models. It is data- and compute-efficient, requiring no LRL task annotations, and only continual pretraining on a small model. Experiments across four model families and eight LRLs show that TriMix consistently outperforms single-model baselines and Proxy Tuning. Our analysis reveals that prioritizing the small LRL-specialized model’s logits is crucial for success, challenging the prevalent large-model-dominant assumption.

## 14. Can Large Language Models Adequately Perform Symbolic Reasoning Over Time Series?

- Authors: Zewen Liu, Juntong Ni, Xianfeng Tang, Max SY Lau, Qi He, Wenpeng Yin, Wei Jin
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.829847228485598
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1756/
- PDF: https://aclanthology.org/2026.findings-acl.1756.pdf
- Local PDF: pdf/2026-08-02_14_Can Large Language Models Adequately Perform Symbolic Reasoning Over Time Series.pdf

Uncovering hidden symbolic laws from time series data, as an aspiration dating back to Kepler’s discovery of planetary motion, remains a core challenge in scientific discovery and artificial intelligence. While Large Language Models show promise in structured reasoning tasks, their ability to infer interpretable, context-aligned symbolic structures from time series data is still underexplored. To systematically evaluate this capability, we introduce SymbolBench, a comprehensive benchmark designed to assess symbolic reasoning over real-world time series across three tasks: multivariate symbolic regression, Boolean network inference, and causal discovery. Unlike prior efforts limited to simple algebraic equations, SymbolBench spans a diverse set of symbolic forms with varying complexity. We further propose a unified framework that integrates LLMs with genetic programming to form a closed-loop symbolic reasoning system. Our empirical results reveal key strengths and limitations of current models, highlighting the importance of combining domain knowledge, context alignment, and reasoning structure to improve LLMs in automated scientific discovery.

## 15. Scaling Unverifiable Rewards: A Case Study on Visual Insights

- Authors: Shuyu Gan, James Mooney, Pan Hao, Renxiang Wang, Mingyi Hong, Qianwen Wang, Dongyeop Kang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.8296653509963003
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1724/
- PDF: https://aclanthology.org/2026.findings-acl.1724.pdf
- Local PDF: pdf/2026-08-02_15_Scaling Unverifiable Rewards_ A Case Study on Visual Insights.pdf

Large Language Model (LLM) agents can increasingly automate complex reasoning through Test-Time Scaling (TTS), an iterative refinement process guided by reward signals.However, many real-world tasks involve multi-stage pipelines whose final outcomes lack verifiable rewards or sufficient data to train robust reward models, making judge-based refinement prone to error accumulation across stages.We propose Selective TTS , a process-based refinement framework that scales inference across stages of a multi-agent pipeline, instead of repeatedly refining a single output over time as in prior work.By distributing compute across stages and pruning low-quality branches early using process-specific judgers, Selective TTS mitigates the judge drift and stabilizes refinement.Grounded in a data science workflow, we build an end-to-end multi-agent pipeline for generating visually insightful reports from a given dataset, and design a reliable LLM-based judge model that aligns with human experts (Kendall’s 𝜏 =0.55) to evaluate them.Our proposed selective TTS then improves insight quality under a fixed compute budget, increasing mean scores from 61.64 (baseline) to 65.86 while reducing variance.We hope our findings serve as the first step toward scaling complex, open-ended tasks with unverifiable rewards like scientific discovery. Our code and generated reports are publicly available at https://minnesotanlp.github.io/insight-scaling-webpage .

## 16. DVI-DTM: Dual-View Representation Learning for Interpretable Short Text Dynamic Topic Modeling

- Authors: Di Liu, Zheng Fang, Bin Wu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.829584212443162
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1318/
- PDF: https://aclanthology.org/2026.acl-long.1318.pdf
- Local PDF: pdf/2026-08-02_16_DVI-DTM_ Dual-View Representation Learning for Interpretable Short Text Dynamic Topic Modeling.pdf

Dynamic topic modeling aims to capture topic evolution from temporal text corpora. However, existing methods face two major challenges when applied to short texts: semantic ambiguity and interpretation ambiguity. Semantic ambiguity arises from the sparsity of short texts and the neglect of temporal semantic shifts. Interpretation ambiguity refers to the latent topics that lack human-understandable descriptions. In this work, we propose a novel Dual-View representation learning-based Interpretable short text Dynamic Topic Model (DVI-DTM). To address semantic ambiguity, the Dual-View Representation Learning module is presented to learn robust document-topic distributions by aligning temporal-aware term view and sentence view representations of short texts. To tackle interpretation ambiguity, we introduce a GEA Topic Refiner that leverages LLM agents to generate topic descriptions and refine document-topic distributions through collaborative semantic reasoning. Furthermore, a Dual-Factor Ranking module is designed to capture the topic evolution through semantic relevance and temporal uniqueness. Comprehensive experiments demonstrate that DVI-DTM outperforms the state-of-the-art baselines in topic alignment and dynamic topic quality metrics while producing highly interpretable topic descriptions.

## 17. Training LLMs for Divide-and-Conquer Reasoning Elevates Test-Time Scalability

- Authors: Xiao Liang, Zhong-Zhi Li, Zhenghao Lin, Eric Hanchen Jiang, Hengyuan Zhang, Yelong Shen, Kai-Wei Chang, Ying Nian Wu, Yeyun Gong, Weizhu Chen
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.829285218154945
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1588/
- PDF: https://aclanthology.org/2026.acl-long.1588.pdf
- Local PDF: pdf/2026-08-02_17_Training LLMs for Divide-and-Conquer Reasoning Elevates Test-Time Scalability.pdf

Large language models (LLMs) have demonstrated strong reasoning capabilities through step-by-step chain-of-thought (CoT) reasoning. Nevertheless, at the limits of model capability, CoT often proves insufficient, and its strictly sequential nature constrains test-time scalability. A potential alternative is divide-and-conquer (DAC) reasoning, which decomposes a complex problem into subproblems to facilitate more effective exploration of the solution space. Although promising, our analysis reveals a fundamental misalignment between general-purpose post-training and DAC-style inference, which limits the model’s capacity to fully leverage this potential. To bridge this gap and fully unlock LLMs’ reasoning capabilities on the most challenging tasks, we propose an end-to-end reinforcement learning (RL) framework to enhance their DAC-style reasoning capacity. At each step, the policy decomposes a problem into a group of subproblems, solves them sequentially, and addresses the original problem conditioned on the subproblem solutions, with both decomposition and solution integrated into RL training. Under comparable training settings, our DAC-style framework endows the model with a higher performance ceiling and stronger test-time scalability, surpassing CoT by 8.6% in Pass@1 and 6.3% in Pass@32 on competition-level benchmarks. The code is available at the provided link .

## 18. Context-Fidelity Boosting: Enhancing Faithful Generation through Watermark-Inspired Decoding

- Authors: Weixu Zhang, Fanghua Ye, Qiang Gao, Jian Li, Haolun Wu, Yuxing Tian, Sijing Duan, Nan Du, Xiaolong Li
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.8290161460099346
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.2121/
- PDF: https://aclanthology.org/2026.findings-acl.2121.pdf
- Local PDF: pdf/2026-08-02_18_Context-Fidelity Boosting_ Enhancing Faithful Generation through Watermark-Inspired Decoding.pdf

Large language models (LLMs) often produce content that contradicts or overlooks information provided in the input context, a phenomenon known as faithfulness hallucination. In this paper, we propose Context-Fidelity Boosting (CFB), a lightweight and general decoding-time framework that effectively reduces such hallucinations by boosting the generation probability of context-relevant tokens. Motivated by logit-shaping principles in watermarking techniques, CFB leverages token-level logit adjustments based on their presence or salience in the input context. Specifically, we develop three boosting strategies, static, context-aware, and token-aware that progressively incorporate distributional divergence, attention scores, and semantic similarity. Notably, CFB requires no retraining or architectural changes, making it compatible with a wide range of LLMs. Experiments on summarization and question answering tasks across multiple open-source LLMs show that CFB consistently improves faithfulness metrics, with minimal generation overhead. Our implementation is fully open-sourced.

## 19. Path Gradients after Flow Matching

- Authors: Vaitl, Lorenz, Klein, Leon
- Source: neurips
- Venue type: conference
- Journal: NeurIPS 2025
- Publication status: formally_published
- Publication date: 2026-04-23
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.8283731599337516
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://proceedings.neurips.cc/paper_files/paper/2025/hash/08f9de0232c0b485110237f6e6cf88f1-Abstract-Conference.html
- PDF: https://proceedings.neurips.cc/paper_files/paper/2025/file/08f9de0232c0b485110237f6e6cf88f1-Paper-Conference.pdf
- Local PDF: pdf/2026-08-02_19_Path Gradients after Flow Matching.pdf

Boltzmann Generators have emerged as a promising machine learning tool for generating samples from equilibrium distributions of molecular systems using Normalizing Flows and importance weighting. Recently, Flow Matching has helped speed up Continuous Normalizing Flows (CNFs), scale them to more complex molecular systems, and minimize the length of the flow integration trajectories. We investigate the benefits of using path gradients to fine-tune CNFs initially trained by Flow Matching, in the setting where a target energy is known. Our experiments show that this hybrid approach yields up to a threefold increase in sampling efficiency for molecular systems, all while using the same model, a similar computational budget and without the need for additional sampling. Furthermore, by measuring the length of the flow trajectories during fine-tuning, we show that path gradients largely preserve the learned structure of the flow.

## 20. Supplement Generation Training for Enhancing Agentic Task Performance

- Authors: Young Min Cho, Daniele Bonadiman, Divya Bhargavi, Tamer Alkhouli, Salvatore Romeo, Dongwei Jiang, Khushbu Pahwa, Yubin Ge, Etsuko Ishii, Monica Sunkara, Yi Zhang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.827640415488904
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.2021/
- PDF: https://aclanthology.org/2026.findings-acl.2021.pdf
- Local PDF: pdf/2026-08-02_20_Supplement Generation Training for Enhancing Agentic Task Performance.pdf

Training large foundation models for agentic tasks is increasingly impractical due to the high computational costs, long iteration cycles, and rapid obsolescence as new models are continuously released. Instead of post-training massive models for every new task or domain, we propose Supplement Generation Training (SGT), a more efficient and sustainable strategy. SGT trains a smaller LLM to generate useful supplemental text that, when appended to the original input, helps the larger LLM solve the task more effectively. These lightweight models can dynamically adapt supplements to task requirements, improving performance without modifying the underlying large models. This approach decouples task-specific optimization from large foundation models and enables more flexible, cost-effective deployment of LLM-powered agents in real-world applications.

## 21. Anatomy of Unlearning: The Dual Impact of Fact Salience and Model Fine-Tuning

- Authors: Anna Borisiuk, Andrey Savchenko, Alexander Panchenko, Elena Tutubalina
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.8274344013036568
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1287/
- PDF: https://aclanthology.org/2026.findings-acl.1287.pdf
- Local PDF: pdf/2026-08-02_21_Anatomy of Unlearning_ The Dual Impact of Fact Salience and Model Fine-Tuning.pdf

Machine Unlearning (MU) enables Large Language Models (LLMs) to remove unsafe or outdated information. However, existing work assumes that all facts are equally forgettable and largely ignores whether the forgotten knowledge originates from pretraining or supervised fine-tuning (SFT). In this paper, we introduce DUAL (Dual Unlearning Evaluation across Training Stages), a benchmark of 28.6k Wikidata-derived triplets annotated with fact popularity using Wikipedia link counts and LLM-based salience scores. Our experiments show that pretrained and SFT models respond differently to unlearning. An SFT step on the forget data yields smoother forgetting, more stable tuning, and 10–50% higher retention, while direct unlearning on pretrained models remains unstable and prone to relearning or catastrophic forgetting.

## 22. Mitigating Coordinate Prediction Bias from Positional Encoding Failures

- Authors: Xingjian Tao, Yiwei Wang, Yujun Cai, Yihong Luo, Kai Han, Jing Tang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.8264751606467264
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1034/
- PDF: https://aclanthology.org/2026.findings-acl.1034.pdf
- Local PDF: pdf/2026-08-02_22_Mitigating Coordinate Prediction Bias from Positional Encoding Failures.pdf

While Multimodal Large Language Models (MLLMs) excel at general vision-language tasks, precise coordinate prediction remains a significant challenge, particularly as high-resolution inputs cause visual positional encodings (VPEs) to degrade. We demonstrate that these encoding failures do not result in random noise but instead trigger predictable, directional biases, suggesting that models default to internal spatial priors when grounding signals are weak. To counteract this, we introduce Vision-PE Shuffle Guidance (VPSG), a training-free, inference-time correction method. VPSG isolates position-unconditioned tendencies by shuffling VPEs and utilizes this negative evidence to steer digit decoding through a lightweight finite-state machine. Evaluation on the ScreenSpot-Pro benchmark confirms that VPSG effectively rectifies coordinate drift, yielding consistent improvements in localization accuracy across various model scales without any retraining.

## 23. Let Retrievers Think Before Action: Thought-Augmented Embedding for Dense Retrieval

- Authors: Ruiran Yan, Wen Xiong, Ze Liu, Chaozhuo Li, Hao Liao, Defu Lian, Zheng Liu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.825673368599537
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1603/
- PDF: https://aclanthology.org/2026.findings-acl.1603.pdf
- Local PDF: pdf/2026-08-02_23_Let Retrievers Think Before Action_ Thought-Augmented Embedding for Dense Retrieval.pdf

Large language models (LLMs) have demonstrated that explicitly performing step-by-step thinking before producing final outputs can substantially improve performance on complex tasks, as exemplified by recent reasoning-oriented models such as OpenAI O1 and DeepSeek R1. Inspired by these advancements, we propose the O1 Embedder, a novel approach aiming to endow retrieval models with similar capabilities to address challenges like multi-task retrieval, zero-shot retrieval, and tasks requiring intensive reasoning of complex relationships. The O1 Embedder generates preliminary thoughts for input queries before document retrieval. To realize this objective, we address two fundamental challenges in integrating thinking mechanisms into dense retrieval. First, retrieval tasks lack explicit supervision for intermediate thinking processes, making it difficult to define thoughts that are truly useful for retrieval. We address this challenge with a data synthesis framework following an “Exploration-Refinement” process, ensuring alignment with retrieval utility. Second, effectively integrating thought generation with representation learning requires a unified modeling framework that can jointly support generation and embedding within a single model. O1 Embedder addresses this challenge by jointly optimizing thought generation and dense retrieval in an end-to-end manner, enhancing retrieval accuracy while reducing complexity through a single deployable model. Extensive evaluations across diverse datasets demonstrate significant performance improvements, highlighting the effectiveness and generalization capability of O1 Embedder.

## 24. Disentangling Continued Pre-Training: Attention-Driven Routing and Semantic Hub Preservation in Language Adaptation

- Authors: Khanh-Tung Tran, Vinh-Khanh Tran, Barry O’Sullivan, Hoang D. Nguyen
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.825508569074087
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1218/
- PDF: https://aclanthology.org/2026.findings-acl.1218.pdf
- Local PDF: pdf/2026-08-02_24_Disentangling Continued Pre-Training_ Attention-Driven Routing and Semantic Hub Preservation in Language Adaptation.pdf

Continued Pre-Training (CPT) enables Large Language Models (LLMs) to acquire second-language capabilities, yet the underlying mechanisms remain poorly understood. In this work, we investigate how CPT adapts model representations across diverse language families and scripts, model sizes, and architectures. We find that second-language abilities emerge through a selective adaptation mechanism: task-solving capabilities are preserved in “semantic hub”, while interface layers retarget to shifted token distributions. Layer-swapping experiments demonstrate that semantic understanding can be surgically transferred between base and CPT models with minimal loss (e.g., swapping 50% of model parameters reduces performance by only 0.3%). Furthermore, we establish that attention components route language adaptation: larger parameter changes than feedforward networks, correlate more strongly with language-specific neurons, and their surgical replacement substantially degrades performance. Overall, our work provides a mechanistic understanding of CPT, guiding future work on efficient strategies for language adaptation.

## 25. From Competition to Synergy: Unlocking Reinforcement Learning for Subject-Driven Image Generation

- Authors: Ziwei Huang, Ying Shu, Fanghao, Quanyu Long, Wenya Wang, Qiushi Guo, Tiezheng Ge, Leilei Gan
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.825449735334122
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1908/
- PDF: https://aclanthology.org/2026.acl-long.1908.pdf
- Local PDF: pdf/2026-08-02_25_From Competition to Synergy_ Unlocking Reinforcement Learning for Subject-Driven Image Generation.pdf

Subject-driven image generation models face a fundamental trade-off between identity preservation (fidelity) and prompt adherence (editability). While online reinforcement learning (RL), specifically GPRO, offers a promising solution, we find that a naive application of GRPO leads to competitive degradation, as the simple linear aggregation of rewards with static weights causes conflicting gradient signals and a misalignment with the temporal dynamics of the diffusion process. To overcome these limitations, we propose Customized-GRPO, a novel framework featuring two key innovations: (i) Synergy-Aware Reward Shaping (SARS), a non-linear mechanism that explicitly penalizes conflicted reward signals and amplifies synergistic ones, providing a sharper and more decisive gradient. (ii) Time-Aware Dynamic Weighting (TDW), which aligns the optimization pressure with the model’s temporal dynamics by prioritizing prompt-following in the early, identity preservation in the later. Extensive experiments demonstrate that our method significantly outperforms naive GRPO baselines, successfully mitigating competitive degradation. Our model achieves a superior balance, generating images that both preserve key identity features and accurately adhere to complex textual prompts.

## 26. CoSToM: Causal-oriented Steering for Intrinsic Theory-of-Mind Alignment in Large Language Models

- Authors: Mengfan Li, Xuanhua Shi, Yang Deng
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.8253187431490634
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.421/
- PDF: https://aclanthology.org/2026.acl-long.421.pdf
- Local PDF: pdf/2026-08-02_26_CoSToM_ Causal-oriented Steering for Intrinsic Theory-of-Mind Alignment in Large Language Models.pdf

Theory of Mind (ToM), the ability to attribute mental states to others, is a hallmark of social intelligence. While large language models (LLMs) demonstrate promising performance on standard ToM benchmarks, we observe that they often fail to generalize to complex task-specific scenarios, relying heavily on prompt scaffolding to mimic reasoning. The critical misalignment between the internal knowledge and external behavior raises a fundamental question: Do LLMs truly possess intrinsic cognition, and can they externalize this internal knowledge into stable, high-quality behaviors? To answer this, we introduce CoSToM (Causal-oriented Steering for ToM alignment), a framework that transitions from mechanistic interpretation to active intervention. First, we employ causal tracing to map the internal distribution of ToM features, empirically uncovering the internal layers’ characteristics in encoding fundamental ToM semantics. Building on this insight, we implement a lightweight alignment framework via targeted activation steering within these ToM-critical layers. Experiments demonstrate that CoSToM significantly enhances human-like social reasoning capabilities and downstream dialogue quality.

## 27. Shuttle Between Symbolic Instructions and Neural Parameters of Large Language Models

- Authors: Wangtao Sun, Haotian Xu, Huanxuan Liao, Xuanqing Yu, Zhongtao Jiang, Shizhu He, Jun Zhao, Kang Liu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.824378773398859
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1269/
- PDF: https://aclanthology.org/2026.acl-long.1269.pdf
- Local PDF: pdf/2026-08-02_27_Shuttle Between Symbolic Instructions and Neural Parameters of Large Language Models.pdf

This paper notices that while symbolic instruction and neural parameters play different roles on steering LLMs’ behavior, both instructions and parameters are the compression of task data, they are supposed be strongly correlated and can be learned to predict one from the other. Therefore, This paper proposes a novel neural network framework, SHIP ( Sh uttle between the I nstructions and the P arameters), to model and learn the bi-directional mappings between the instructions and the parameters of LLMs. We verify that SHIP can effectively map one of the instructions/parameters to the other by evaluating it on the tasks of instruction deduction and induction. The results show that SHIP performs better than existing baseline methods in terms of deductive capabilities while significantly surpassing them in inductive capabilities. Moreover, SHIP can effectively combine the two mapping processes to perform excellent inductive reasoning. We further discuss how the latent fusing methods and latent dimensions affect SHIP’s performance, and show SHIP can effectively generalize with pre-training. The code and data for this paper are released at https://anonymous.4open.science/r/Shuttle-Between-Instructions-Parameters

## 28. LongInsightBench: A Comprehensive Benchmark for Evaluating Omni-Modal Models on Human-Centric Long-Video Understanding.

- Authors: ZhaoYang Han, Qihan Lin, Hao Liang, Bowen Chen, Zhou Liu, Wentao Zhang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.823989303321983
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.965/
- PDF: https://aclanthology.org/2026.findings-acl.965.pdf
- Local PDF: pdf/2026-08-02_28_LongInsightBench_ A Comprehensive Benchmark for Evaluating Omni-Modal Models on Human-Centric Long-Video Understanding.pdf

We introduce LongInsightBench , the first benchmark designed to assess models’ ability to understand long videos, with a focus on human language, viewpoints, actions, and other contextual elements, while integrating visual, audio, and text modalities. Our benchmark excels in three key areas: a) Long-Duration, Human-Centric Videos: We carefully selected approximately 1,000 videos from open-source datasets FineVideo based on duration limit and multi-modal information density, focusing on content like lectures, interviews, and vlogs, which contain rich human-centric semantic and contextual attributes. b) Diverse and Challenging Task Scenarios: We have designed six challenging task scenarios, including both Intra-Event and Inter-Event Tasks. c) Rigorous and Comprehensive Quality Assurance Pipelines: We have developed a three-step, semi-automated data quality assurance pipeline to ensure the difficulty and validity of the synthesized questions and answer options. Based on LongInsightBench, we designed a series of experiments. which shows that Omni-modal models(OLMs) still face challenge in tasks requiring precise temporal localization (T-Loc) and long-range causal inference (CE-Caus). Surprisingly, extended experiments reveal the information loss in modal fusion of OLMs, which we called the Fusion Deficit Paradox .

## 29. Autonomous bioisosteric replacement for multi-property optimization in drug design

- Authors: Hyeongwoo Kim, Seokhyun Moon, Wonho Zhung, Shin‐Woo Kim, Jaechang Lim, Woo Youn Kim
- Source: openalex
- Venue type: journal
- Journal: Nature Communications
- Publication status: published
- Publication date: 2026-07-27
- DOI: https://doi.org/10.1038/s41467-026-75512-9
- Categories: Computational Drug Discovery Methods, Machine Learning in Materials Science, Cholinesterase and Neurodegenerative Diseases
- Relevance: 2.823228687351156
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://doi.org/10.1038/s41467-026-75512-9
- PDF: https://www.nature.com/articles/s41467-026-75512-9_reference.pdf
- Local PDF: pdf/2026-08-02_29_Autonomous bioisosteric replacement for multi-property optimization in drug design.pdf

Abstract Optimizing molecular properties while preserving biological activity is a central challenge in drug design. Bioisosteric replacement, which substitutes a molecular fragment with a chemically or biologically analogous moiety, offers a powerful strategy for fine-tuning properties without disrupting target binding. However, existing in silico approaches often rely on expert-defined modification sites or struggle to modulate multiple molecular properties simultaneously. Here, we present DeepBioisostere, a deep generative model that performs end-to-end bioisosteric replacement by autonomously selecting and substituting molecular fragments to satisfy multiple target properties. The model captures complex relationships across the molecular graph, enabling the optimization of sophisticated properties such as drug-likeness and synthetic accessibility. By learning from experimental bioassay data, DeepBioisostere proposes replacements that maintain biological activities, even generating potential bioisosteres beyond the training data. We demonstrate the effectiveness of the model in computational hit-to-lead optimization scenarios, highlighting its potential to accelerate rational molecular design without relying on expert heuristics or pre-established substitution rules.

## 30. C2PO: Diagnosing and Disentangling Bias Shortcuts in LLMs

- Authors: Xuan Feng, Bo An, Tianlong Gu, Liang Chang, Fengrui Hao, Peipeng Yu, Shuai Zhao
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.8230891786107497
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1226/
- PDF: https://aclanthology.org/2026.findings-acl.1226.pdf
- Local PDF: pdf/2026-08-02_30_C2PO_ Diagnosing and Disentangling Bias Shortcuts in LLMs.pdf

Bias in Large Language Models (LLMs) poses significant risks to trustworthiness, manifesting primarily as stereotypical biases (e.g., gender or racial stereotypes) and structural biases (e.g., lexical overlap or position preferences). However, prior paradigms typically address these in isolation, often mitigating one at the expense of exacerbating the other. To address this, we conduct a systematic exploration of these reasoning failures and identify a primary inducement: the latent spurious feature correlations within the input that drive these erroneous reasoning shortcuts. Driven by these findings, we introduce Causal-Contrastive Preference Optimization (C2PO), a unified alignment framework designed to tackle these specific failures by simultaneously discovering and suppressing these correlations directly within the optimization process. Specifically, C2PO leverages causal counterfactual signals to isolate bias-inducing features from valid reasoning paths, and employs a fairness-sensitive preference update mechanism to dynamically evaluate logit-level contributions and suppress shortcut features. Extensive experiments across multiple benchmarks covering stereotypical bias (BBQ, Unqover), structural bias (MNLI, HANS, Chatbot, MT-Bench), out-of-domain fairness (StereoSet, WinoBias), and general utility (MMLU, GSM8K) demonstrate that C2PO effectively mitigates stereotypical and structural biases while preserving robust general reasoning capabilities.
