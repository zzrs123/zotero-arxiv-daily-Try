# Paper Daily Reading - 2026-08-10

## 1. Unlocking biological insight from single-cell data with an interpretable dual-stream foundation model

- Authors: Honglie Guo, Qinghang Cui, Xiang Zhang, Chao‐Wei Chen, Weihua Zheng, Changfeng Cai, Xinyi Wang, Shunfang Wang
- Source: openalex
- Venue type: journal
- Journal: Genome biology
- Publication status: published
- Publication date: 2026-08-08
- DOI: https://doi.org/10.1186/s13059-026-04193-w
- Categories: Mathematical Biology Tumor Growth, Cell Image Analysis Techniques, Single-cell and spatial transcriptomics
- Relevance: 3.7834187546740363
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://doi.org/10.1186/s13059-026-04193-w
- PDF: Unavailable
- Local PDF: Not downloaded

Abstract Deep learning foundation models are revolutionizing single-cell biology, yet learning holistic and discriminative representations from complex, high-dimensional data remains a central challenge. Although Transformer-based single-cell language models have shown significant progress, they typically rely on a single input-encoding scheme, a practice that results in the loss of critical gene expression information and hinders the effective learning of global cellular representations. To address these challenges, we introduce scDMC, an innovative single-cell Dual-stream Masked Contrastive pre-training framework designed to synergistically optimize information fidelity at both the gene and cellular levels. Pre-trained on only 2 million cells far fewer than the datasets used by mainstream models, scDMC sets a new state-of-the-art in multiple benchmark tasks, including cell annotation, clustering, and data integration. More importantly, we demonstrate that scDMC can uncover functional gene modules, infer cell-type-specific regulatory networks in a data-driven manner, and exhibits a high degree of biological interpretability.

## 2. Move BeTween modAlities (MBTA) employs flow matching to predict single cell data modalities

- Authors: Xu, B., Zhang, Y., Michor, F.
- Source: biorxiv
- Venue type: preprint
- Journal: biorxiv
- Publication status: preprint
- Publication date: 2026-08-09
- DOI: 10.64898/2026.08.05.743110
- Categories: bioinformatics
- Relevance: 3.5855303995013745
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://www.biorxiv.org/content/10.64898/2026.08.05.743110v1.full.pdf
- PDF: https://www.biorxiv.org/content/10.64898/2026.08.05.743110v1.full.pdf
- Local PDF: Not downloaded

Integrating diverse molecular modalities to obtain a comprehensive view of cellular identity remains a major challenge in single-cell biology. A fundamental but underappreciated obstacle is structural mismatch-the phenomenon in which the neighborhood structure of a cell differs depending on which molecular modality is used to define it. Existing approaches typically embed modalities into a shared latent space, which actively erases the structural differences between modalities that make multimodal measurements scientifically valuable. Here we introduce Move BeTween modAlities (MBTA), the first framework explicitly designed to address structural mismatch. Rather than forcing modalities into a shared representation, MBTA maintains modality-specific latent spaces and connects them via flow matching, preserving the structural integrity of each modality while enabling accurate cross-modal translation. Across extensive benchmarks on multi-modal single-cell datasets, MBTA consistently outperformed existing methods, with the largest gains observed in datasets with pronounced structural mismatch. Applied to joint genomic and transcriptomic profiles of breast cancer patients, MBTA identified transcriptomic lineage relationships corroborated by genomic variation and outperformed state-of-the-art transcriptomics-based copy number inference methods. Extending this framework to mouse embryonic development, we reconstructed temporal trajectories jointly defined by gene expression and seven complementary epigenetic modalities. MBTA can connect any number of molecular readouts without erasing their individual character, serving as the computational foundation for assembling multi-layered portraits of cells.

## 3. Virtual spatial transcriptomics from histopathology enables prognostic and therapeutic response prediction in cancer

- Authors: Jiao, S., Yuan, Z., Lu, D., Xu, Y., Dong, Y., Peng, J.
- Source: biorxiv
- Venue type: preprint
- Journal: biorxiv
- Publication status: preprint
- Publication date: 2026-08-09
- DOI: 10.64898/2026.08.04.742671
- Categories: genomics
- Relevance: 3.3836630725368124
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://www.biorxiv.org/content/10.64898/2026.08.04.742671v1.full.pdf
- PDF: https://www.biorxiv.org/content/10.64898/2026.08.04.742671v1.full.pdf
- Local PDF: Not downloaded

Spatial transcriptomics reveals cellular heterogeneity, intercellular communication, and tissue organization, but its cost and limited accessibility restrict clinical use. Here, we present VISTA, a model that integrates multi-scale histological features and spatial context to infer spatial gene expression from H&E stained tissue images. Across leave one section out cross validation and independent validation, VISTA robustly predicted thousands of genes and outperformed state-of-the-art methods. Beyond expression reconstruction, VISTA enabled clinically relevant downstream analyses. In TCGA breast cancer samples, it identified survival-associated genes, stratified prognostic risk groups, and revealed adverse tumor-associated spatial subtypes. In our inhouse intrahepatic cholangiocarcinoma cohort, it preserved tumor normal organization and identified CLDN4 and CYP3A4 as complementary spatial biomarkers. In HER2+ breast cancer, it predicted pathological response to neoadjuvant trastuzumab-based therapy and linked response-associated regions to immune and cytokine related programs. These results support virtual spatial transcriptomics from routine histopathology for oncology applications.

## 4. Activation Steering for Chain-of-Thought Compression

- Authors: Seyedarmin Azizi, Erfan Baghaei Potraghloo, Souvik Kundu, Massoud Pedram
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.8001043267249157
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1828/
- PDF: https://aclanthology.org/2026.findings-acl.1828.pdf
- Local PDF: pdf/2026-08-10_04_Activation Steering for Chain-of-Thought Compression.pdf

Large language models (LLMs) demonstrate strong performance on multi-step reasoning tasks by producing intermediate explanations, commonly referred to as chains of thought (CoTs). However, the generated rationales are typically verbose, consuming many additional tokens, and thus degrading throughput and increasing inference energy consumption. Interestingly, we find that verbose and concise CoTs correspond to distinct regions in the model’s intermediate activation space, suggesting that verbosity is a steerable latent attribute. Building on this observation, we develop an inference-time method to automatically steer the model response towards concise reasoning traces without updating model parameters. Our method, dubbed ASC (Activation-Steered Compression), generates concise CoTs by directly adjusting internal representations via activation steering. A key component of ASC is Contrastive Energy-Based Steering (CES) , a principled procedure to learn a single steering vector from a small set of verbose–concise CoT pairs by optimizing a length-normalized contrastive energy objective. To further ensure reliable steering and preserve general utility, CES enforces a differentiable KL trust region during steering vector optimization, explicitly constraining the distribution shift within a specified budget. With only 100 pairs of verbose–concise examples, ASC reduces the generated token length by as much as 69.4% across five reasoning benchmarks (MATH500, GSM8K, LiveCodeBench, GSM8K-Hard, and AQuA-RAT) while maintaining accuracy across models with 1.5B, 7B, 8B, and 32B parameters. On MATH500, ASC achieves an end-to-end inference speed-up of 2.7× on an 8B model.

## 5. Mem-Gallery: Benchmarking Multimodal Long-Term Conversational Memory for MLLM Agents

- Authors: Yuanchen Bei, Tianxin Wei, Xuying Ning, Yanjun Zhao, Zhining Liu, Xiao Lin, Yada Zhu, Hendrik Hamann, Jingrui He, Hanghang Tong
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.79996961605824
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1892/
- PDF: https://aclanthology.org/2026.acl-long.1892.pdf
- Local PDF: pdf/2026-08-10_05_Mem-Gallery_ Benchmarking Multimodal Long-Term Conversational Memory for MLLM Agents.pdf

Long-term memory is a critical capability for multimodal large language model (MLLM) agents, particularly in conversational settings where information accumulates and evolves over time. However, existing benchmarks either evaluate multi-session memory in text-only conversations or assess multimodal understanding within localized contexts, failing to evaluate how multimodal memory is preserved, organized, and evolved across long-term conversational trajectories. Thus, we introduce Mem-Gallery, a new benchmark for evaluating multimodal long-term conversational memory in MLLM agents. Mem-Gallery features high-quality multi-session conversations grounded in both visual and textual information, with long interaction horizons and rich multimodal dependencies. Building on this dataset, we propose a systematic evaluation framework that assesses key memory capabilities along three functional dimensions: memory extraction and test-time adaptation, memory reasoning, and memory knowledge management. Extensive benchmarking across twelve memory systems reveals several key findings, highlighting the necessity of explicit multimodal information retention and memory organization, the persistent limitations in memory reasoning and knowledge management, as well as the efficiency bottleneck of current models. Our benchmark and dataset are available at https://github.com/YuanchenBei/Mem-Gallery .

## 6. Soft Head Selection for Injecting ICL-Derived Task Embeddings

- Authors: Jungwon Park, Jimyeong Kim, Changin Choi, Wonjong Rhee
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.7982605924845325
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1355/
- PDF: https://aclanthology.org/2026.findings-acl.1355.pdf
- Local PDF: pdf/2026-08-10_06_Soft Head Selection for Injecting ICL-Derived Task Embeddings.pdf

Large language models (LLMs) are commonly adapted to downstream tasks using parameter-efficient fine-tuning (PEFT) or in-context learning (ICL). Recently, ICL-driven embedding-based adaptation has been proposed as a distinct task adaptation paradigm. It derives task-specific embeddings from intermediate activations using few-shot prompts and injects them during inference. Despite its conceptual appeal, this approach has not demonstrated consistent performance gains over PEFT or ICL, and its empirical advantages have been limited in practice. We propose Soft head-selection for ICL-derived Task Embeddings (SITE), a gradient-based method that identifies task-relevant attention heads to enable effective task embedding injection. Across various types of open-ended generation, reasoning, and natural language understanding tasks, SITE significantly outperforms prior embedding-based adaptation methods and few-shot ICL, while using substantially fewer trainable parameters than PEFT. Experiments on 12 LLMs ranging from 4B to 70B parameters demonstrate the generality of our approach, and intra-task and inter-task activation patching analyses further provide new mechanistic insights by revealing strong task dependence in attention head functionality.

## 7. From 2:4 to 8:16 sparsity patterns in LLMs for Outliers and Weights with Variance Correction

- Authors: Egor Maximov, Yulia Kuzkina, Egor Shvetsov, Azamat Kanametov, Aleksandr Prutko, Maxim Zhelnin, Aleksei Goncharov
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.7977085147723213
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-industry.66/
- PDF: https://aclanthology.org/2026.acl-industry.66.pdf
- Local PDF: pdf/2026-08-10_07_From 2_4 to 8_16 sparsity patterns in LLMs for Outliers and Weights with Variance Correction.pdf

As large language models (LLMs) grow in size, efficient compression techniques like quantization and sparsification are critical. While quantization maintains performance with reduced precision, structured sparsity methods, such as N:M sparsification, often fall short due to limited flexibility and sensitivity to outlier weights. We explore 8:16 semi-structured sparsity, demonstrating its ability to surpass the Performance Threshold—where a compressed model matches the accuracy of its uncompressed or smaller counterpart under equivalent memory constraints. Compared to 2:4 sparsity, 8:16 offers greater flexibility with minimal storage overhead (0.875 vs. 0.75 bits/element). We also apply sparse structured patterns for salient weights, showing that structured sparsity for outliers is competitive with unstructured approaches, leading to equivalent or better results. Finally, we demonstrate that simple techniques such as variance correction and SmoothQuant-like weight equalization improve sparse models performance.

## 8. Enabling Stroke-Level Structural Analysis of Hieroglyphic Scripts without Language-Specific Priors

- Authors: Fuwen Luo, Zihao Wan, Ziyue Wang, Yaluo Liu, Pau Tong Lin Xu, Xuanjia Qiao, Xiaolong Wang, Peng Li, Yang Liu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.7968512424557987
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1383/
- PDF: https://aclanthology.org/2026.findings-acl.1383.pdf
- Local PDF: pdf/2026-08-10_08_Enabling Stroke-Level Structural Analysis of Hieroglyphic Scripts without Language-Specific Priors.pdf

Hieroglyphs, as logographic writing systems, encode rich semantic and cultural information within their internal structural composition. Yet, current advanced Large Language Models (LLMs) and Multimodal LLMs (MLLMs) usually remain structurally blind to this information. LLMs process characters as textual tokens, while MLLMs additionally view them as raw pixel grids. Both fall short to model the underlying logic of character strokes. Furthermore, existing structural analysis methods are often script-specific and labor-intensive. In this paper, we propose Hieroglyphic Stroke Analyzer (HieroSA), a novel and generalizable framework that enables MLLMs to automatically derive stroke-level structures from character bitmaps without handcrafted data. It transforms modern logographic and ancient hieroglyphs character images into explicit, interpretable line-segment representations in a normalized coordinate space, allowing for cross-lingual generalization. Extensive experiments demonstrate that HieroSA effectively captures character-internal structures and semantics, bypassing the need for language-specific priors. Experimental results highlight the potential of our work as a graphematics analysis tool for a deeper understanding of hieroglyphic scripts.

## 9. ContrastKV: Robust KV Cache Eviction via Contrastive Signal Fusion for Multi-Query Generalization

- Authors: Xingchi Chen, Peiyuan Zong, Ziqiang Gao, Qing Li, Yong Jiang, Fa Zhu, Hui Li
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.7943787862531346
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.417/
- PDF: https://aclanthology.org/2026.acl-long.417.pdf
- Local PDF: pdf/2026-08-10_09_ContrastKV_ Robust KV Cache Eviction via Contrastive Signal Fusion for Multi-Query Generalization.pdf

Large Language Models (LLMs) face significant memory and latency overheads during long-context inference due to the growing KV cache, especially in Knowledge Base Question Answering (KBQA) settings that require support for multiple downstream queries. Query-aware eviction methods do not generalize across queries, while existing query-agnostic approaches rely on a single proxy query, leading to fragile eviction decisions under high eviction ratios. We propose ContrastKV, a robust query-agnostic KV cache eviction algorithm for multi-query generalization. ContrastKV introduces a contrastive signal fusion mechanism that jointly exploits complementary semantic and non-semantic signals. By contrasting semantic consistency with structural robustness, the method constructs a more reliable eviction criterion that alleviates the blind spots of single-query proxies. The framework integrates efficient signal generation, parallel importance scoring, and multi-level fusion across heads and layers. Experiments show that ContrastKV outperforms state-of-the-art methods, retaining up to 92% accuracy with only 20% of the KV cache budget, while reducing decoding latency by approximately 50% and significantly lowering GPU memory usage.

## 10. MemSearch-o1: Empowering Large Language Models with Reasoning-Aligned Memory Growth in Agentic Search

- Authors: Sheng Zhang, Junyi Li, Yingyi Zhang, Pengyue Jia, Yichao Wang, Xiaowei Qian, Wenlin Zhang, Maolin Wang, Yong Liu, Xiangyu Zhao
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.7935593393978886
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.41/
- PDF: https://aclanthology.org/2026.acl-long.41.pdf
- Local PDF: pdf/2026-08-10_10_MemSearch-o1_ Empowering Large Language Models with Reasoning-Aligned Memory Growth in Agentic Search.pdf

Recent advances in large language models (LLMs) have scaled the potential for reasoning and agentic search, wherein models autonomously plan, retrieve, and reason over external knowledge to answer complex queries. However, the iterative think–search loop accumulates long system memories, leading to memory dilution problem. In addition, existing memory management methods struggle to capture fine-grained semantic relations between queries and documents and often lose substantial information. Therefore, we propose MemSearch-o1, an agentic search framework built on reasoning-aligned memory growth and retracing. MemSearch-o1 dynamically grows fine-grained memory fragments from memory seed tokens from the queries, then retraces and deeply refines the memory via a contribution function, and finally reorganizes a globally connected memory path. This shifts memory management from stream-like concatenation to structured, token-level growth with path-based reasoning. Experiments on eight benchmark datasets show that MemSearch-o1 substantially mitigates memory dilution, and more effectively activates the reasoning potential of diverse LLMs, establishing a solid foundation for memory-aware agentic intelligence.

## 11. Hidden States as Early Signals: Step-level Trace Evaluation and Pruning for Efficient Test-Time Scaling

- Authors: Zhixiang Liang, Beichen Huang, Zheng Wang, Minjia Zhang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.7928390634299487
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1336/
- PDF: https://aclanthology.org/2026.findings-acl.1336.pdf
- Local PDF: pdf/2026-08-10_11_Hidden States as Early Signals_ Step-level Trace Evaluation and Pruning for Efficient Test-Time Scaling.pdf

Large Language Models (LLMs) can enhance reasoning capabilities through test-time scaling by generating multiple traces. However, the combination of lengthy reasoning traces with multiple sampling introduces substantial computation and high end-to-end latency. Prior work on accelerating this process has relied on similarity-based or confidence-based pruning, but these signals do not reliably indicate trace quality. To address these limitations, we propose STEP : S tep-level T race E valuation and P runing, a novel pruning framework that evaluates reasoning steps using hidden states and dynamically prunes unpromising traces during generation. We train a lightweight step scorer to estimate trace quality, and design a GPU memory-aware pruning strategy that triggers pruning as the GPU memory is saturated by KV cache to reduce end-to-end latency. Experiments across challenging reasoning benchmarks demonstrate that STEP reduces end-to-end inference latency by 45%–70% on average compared to self-consistency while also improving reasoning accuracy.

## 12. Guided by Gut: Efficient Test-Time Scaling with Reinforced Intrinsic Confidence

- Authors: Amirhosein Ghasemabadi, Keith G. Mills, Baochun Li, Di Niu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.792646881219374
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.739/
- PDF: https://aclanthology.org/2026.acl-long.739.pdf
- Local PDF: pdf/2026-08-10_12_Guided by Gut_ Efficient Test-Time Scaling with Reinforced Intrinsic Confidence.pdf

Test-Time Scaling (TTS) methods for enhancing Large Language Model (LLM) reasoning often incur substantial inference costs, due to reliance on long chain-of-thought (CoT) generation, self-consistency sampling methods, or searching under Process Reward Models (PRMs). This paper introduces Guided by Gut (GG), an efficient self-guided TTS framework that enables LLMs to perform step-by-step reasoning at a low cost, without any reward models or verifiers. GG performs a lightweight tree search guided solely by intrinsic confidence signals of the LLM at each reasoning step and improves the reliability of such internal confidence signals by reinforcement learning. Empirical evaluations on challenging mathematical reasoning benchmarks demonstrate that GG enables smaller models (e.g., 1.5B-7B parameters) to achieve accuracy matching or surpassing significantly larger models (e.g., 32B–70B parameters), while reducing GPU memory usage by up to 10×. Compared to TTS with PRMs, GG achieves comparable accuracy with 8× faster inference speeds and 4–5× lower memory usage. Additionally, GG reduces KV cache memory usage by approximately 50% compared to Best-of-N sampling, facilitating more efficient and practical deployment of TTS techniques.

## 13. CAST: Achieving Stable LLM-based Text Analysis for Data Analytics

- Authors: Jinxiang Xie, Zihao Li, Wei He, Rui Ding, Shi Han, Dongmei Zhang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.7920103832234755
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.113/
- PDF: https://aclanthology.org/2026.findings-acl.113.pdf
- Local PDF: pdf/2026-08-10_13_CAST_ Achieving Stable LLM-based Text Analysis for Data Analytics.pdf

Text analysis of tabular data relies on two core operations: summarization for corpus-level theme extraction and tagging for row-level labeling. A critical limitation of employing large language models (LLMs) for these tasks is their inability to meet the high standards of output stability demanded by data analytics. To address this challenge, we introduce CAST ( C onsistency via A lgorithmic Prompting and S table T hinking), a framework that enhances output stability by constraining the model’s latent reasoning trajectory. CAST combines (i) Algorithmic Prompting to impose a procedural scaffold over valid reasoning transitions and (ii) Thinking-before-Speaking to enforce explicit intermediate commitments before final generation. To measure progress, we introduce CAST-S and CAST-T , stability metrics for bulleted summarization and tagging, and validate their alignment with human judgments. Experiments across publicly available benchmarks on multiple LLM backbones show that CAST consistently achieves the best stability among all baselines, improving Stability Score by up to 16.2%, while maintaining or improving output quality.

## 14. Vista-LLM: Decoupled Query-Guided Visual Token Pruning for Efficient Long-Video Large Language Models

- Authors: Zhenyu Li, Zuchao Li, Ping Wang, Lefei Zhang, Haojun Ai
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.7919545772607357
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.601/
- PDF: https://aclanthology.org/2026.acl-long.601.pdf
- Local PDF: pdf/2026-08-10_14_Vista-LLM_ Decoupled Query-Guided Visual Token Pruning for Efficient Long-Video Large Language Models.pdf

Long-video understanding is bottlenecked by the high cost of processing massive visual tokens. Current reduction strategies often rely on static allocation or inefficient in-network selection that disrupts optimized attention kernels. In this paper, we introduce Vista-LLM, a decoupled framework for query-guided visual token pruning. By filtering redundancy prior to inference with minimal overhead, Vista-LLM ensures full compatibility with Flash Attention. Our method employs a coarse-to-fine pipeline: (1) Query-Guided Dynamic Budgeting for adaptive temporal allocation; (2) a lightweight Semantic Scout for fine-grained, query-specific selection; and (3) Structure-Aware Compensation to preserve global context. Extensive experiments on benchmarks like Video-MME and MLVU demonstrate a significantly improved Pareto frontier. Notably, on LLaVA-OneVision, Vista-LLM reduces visual tokens by 90% and accelerates inference while retaining over 98% of baseline performance on average, effectively filtering visual noise.

## 15. SepSeq: A Training-Free Framework for Long Numerical Sequence Processing in LLMs

- Authors: Jie Sun, Yu Liu, Lu Han, Qiwen Deng, Xiang Shu, Yang Xiao, Lintao Ma, Xingyu Lu, Jun Zhou, Pengfei Liu, Jiancan Wu, Xiang Wang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.791536041974609
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.272/
- PDF: https://aclanthology.org/2026.findings-acl.272.pdf
- Local PDF: pdf/2026-08-10_15_SepSeq_ A Training-Free Framework for Long Numerical Sequence Processing in LLMs.pdf

While transformer-based Large Language Models (LLMs) theoretically support massive context windows, they suffer from severe performance degradation when processing long numerical sequences. We attribute this failure to the attention dispersion in the Softmax mechanism, which prevents the model from concentrating attention. To overcome this, we propose Sep arate Seq uence ( SepSeq ), a training-free, plug-and-play framework to mitigate dispersion by strategically inserting separator tokens. Mechanistically, we demonstrate that separator tokens act as an attention anchor, recalibrating attention to focus on local segments while preserving global context. Extensive evaluations on 9 widely-adopted LLMs confirm the effectiveness of our approach: SepSeq yields an average relative accuracy improvement of 35.6% across diverse domains while reducing 16.4% inference token consumption.

## 16. CAMO: An Agentic Framework for Automated Causal Discovery from Micro Behaviors to Macro Emergence in LLM Agent Simulations

- Authors: Xiangning Yu, Yuwei Guo, Yuqi Hou, Xiao Xue, Qun Ma
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.791485468139132
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1224/
- PDF: https://aclanthology.org/2026.findings-acl.1224.pdf
- Local PDF: pdf/2026-08-10_16_CAMO_ An Agentic Framework for Automated Causal Discovery from Micro Behaviors to Macro Emergence in LLM Agent Simulatio.pdf

LLM-empowered agent simulations are increasingly used to study social emergence, yet the micro-to-macro causal mechanisms behind macro outcomes often remain unclear. This is challenging because emergence arises from intertwined agent interactions and meso-level feedback and nonlinearity, making generative mechanisms hard to disentangle. To this end, we introduce CAMO , an automated Ca usal discovery framework from M icr o behaviors to M acr o Emergence in LLM agent simulations. CAMO converts mechanistic hypotheses into computable factors grounded in simulation records and learns a compact causal representation centered on an emergent target . CAMO outputs a computable Markov boundary and a minimal upstream explanatory subgraph, yielding interpretable causal chains and actionable intervention levers. It also uses simulator-internal counterfactual probing to orient ambiguous edges and revise hypotheses when evidence contradicts the current view. Experiments across four emergent settings demonstrate the promise of CAMO.[The code is available at an anonymous link: https://anonymous.4open.science/r/CAMO-0E6C/ .]

## 17. AgentSlimming: Towards Efficient and Cost-Aware Multi-Agent Systems

- Authors: Yulang Chen, Haoxuan Peng, Jinyan Liu, Zichen Wen, Dongrui Liu, Linfeng Zhang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.7912100411709133
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1387/
- PDF: https://aclanthology.org/2026.acl-long.1387.pdf
- Local PDF: pdf/2026-08-10_17_AgentSlimming_ Towards Efficient and Cost-Aware Multi-Agent Systems.pdf

Large Language Model-based Multi-Agent Systems (MAS) have demonstrated remarkable capabilities in complex tasks. However, manually designing optimal communication topologies is labor-intensive, while automated expansion methods often result in bloated structures with redundant agents, leading to excessive token consumption. To address this problem, we introduce AgentSlimming, a plug-and-play compression framework for graph-structured multi-agent workflows. Motivated by the AgentPruner and AgentQuant in neural networks, AgentSlimming compresses workflows by firstly estimate the importance score of each agent with a hybrid mechanism, and then removing redundant agents or replacing them with low-cost ones, where each operation is then validated with a baseline-anchored acceptance rule to prevent performance collapse. Experiments show that AgentSlimming reduces average token cost by up to 78.9% with negligible performance degradation, and even sometimes improves accuracy, achieving a strong Pareto-optimal trade-off between cost and quality.

## 18. DataArc-SynData-Toolkit: A Unified Closed-Loop Framework for Multi-Path, Multimodal, and Multilingual Data Synthesis

- Authors: Zhichao Shi, Cehao Yang, Hao Zhou, Xiaojun Wu, Huajie Li, Xuhui Jiang, Chengjin Xu, Yuanzhuo Wang, Jian Guo
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.791194759570061
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-demo.31/
- PDF: https://aclanthology.org/2026.acl-demo.31.pdf
- Local PDF: pdf/2026-08-10_18_DataArc-SynData-Toolkit_ A Unified Closed-Loop Framework for Multi-Path, Multimodal, and Multilingual Data Synthesis.pdf

Synthetic data has emerged as a crucial solution to the data scarcity bottleneck in large language models (LLMs), particularly for specialized domains and low-resource languages. However, the broader adoption of existing synthetic data tools is severely hindered by convoluted workflows, fragmented data standards, and limited scalability across modalities.To address these limitations, we develop DataArc-SynData-Toolkit, an open-source framework featuring: (1) a configuration-driven, end-to-end pipeline equipped with an intuitive visual interface and simplified CLI for exceptional usability; (2) a unified, quality-controllable synthesis paradigm that standardizes multi-source data generation to ensure high reusability; and (3) a highly modular architecture designed for seamless multimodal, multilingual, and multi-task adaptation.We apply the toolkit in multiple application scenarios. Experimental results demonstrate that our toolkit achieves an optimal balance between generation efficiency and data quality. By offering an end-to-end and visually interactive pipeline, DataArc-SynData-Toolkit significantly lowers the technical barrier to synthetic data generation and subsequent model training, accelerating its practical deployment in real-world applications.

## 19. SCURank: Ranking Multiple Candidate Summaries with Summary Content Units for Enhanced Summarization

- Authors: Bo-Jyun Wang, Ying-Jia Lin, Hung-Yu Kao
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.791144900903263
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1941/
- PDF: https://aclanthology.org/2026.findings-acl.1941.pdf
- Local PDF: pdf/2026-08-10_19_SCURank_ Ranking Multiple Candidate Summaries with Summary Content Units for Enhanced Summarization.pdf

Small language models (SLMs), such as BART, can achieve summarization performance comparable to large language models (LLMs) via distillation. However, existing LLM-based ranking strategies for summary candidates suffer from instability, while classical metrics (e.g., ROUGE) are insufficient to rank high-quality summaries. To address these issues, we introduce SCURank, a framework that enhances summarization by leveraging Summary Content Units (SCUs). Instead of relying on unstable comparisons or surface-level overlap, SCURank evaluates summaries based on the richness and semantic importance of information content. We investigate the effectiveness of SCURank in distilling summaries from multiple diverse LLMs. Experimental results demonstrate that SCURank outperforms traditional metrics and LLM-based ranking methods across evaluation measures and datasets. Furthermore, our findings show that incorporating diverse LLM summaries enhances model abstractiveness and overall distilled model performance, validating the benefits of information-centric ranking in multi-LLM distillation.

## 20. scXpand: Pan-cancer detection of T cell clonal expansion from single-cell RNA sequencing without paired single-cell TCR sequencing

- Authors: Ofir Shorer, Ron Amit, Keren Yizhak
- Source: openalex
- Venue type: journal
- Journal: Cell Genomics
- Publication status: published
- Publication date: 2026-08-01
- DOI: https://doi.org/10.1016/j.xgen.2026.101328
- Categories: Cancer Genomics and Diagnostics, Single-cell and spatial transcriptomics, CAR-T cell therapy research
- Relevance: 2.791024754894824
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://doi.org/10.1016/j.xgen.2026.101328
- PDF: Unavailable
- Local PDF: Not downloaded

Advances in single-cell sequencing have enabled detailed characterization of T cell clonal dynamics in cancer. However, analyses aiming to link the transcriptional landscape to T cell clonality remain limited by confounding factors unequally controlled in different studies. To address this challenge, we developed scXpand, a machine-learning framework for pan-cancer detection of T cell clonal expansion directly from single-cell RNA sequencing (scRNA-seq), without paired T cell receptor (TCR) sequencing. Trained and tested using our in-house-constructed human pan-cancer database of paired scRNA/TCR-seq profiles from 2.6 million T cells, scXpand demonstrates robust and accurate detection of clonal expansion across tissues and T cell subtypes. Applied to datasets lacking TCR sequencing, scXpand predictions correspond with known characteristics of the tumor microenvironment. Overall, scXpand provides a framework for detecting T cell clonal expansion across cancers directly from scRNA-seq, enabling broad use on datasets lacking scTCR-seq, while supporting scalable, memory-efficient processing, including pre-trained models with user-friendly documentation for flexible applications.

## 21. MulDimIF: A Multi-Dimensional Constraint Framework for Evaluating and Improving Instruction Following in Large Language Models

- Authors: Junjie Ye, Caishuang Huang, Zhuohan Chen, Wenjie Fu, Chenyuan Yang, Leyi Yang, Yilong Wu, Peng Wang, Meng Zhou, Xiaolong Yang, Tao Gui, Qi Zhang, Zhongchao Shi, Jianping Fan, Xuanjing Huang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.7908767325274484
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.99/
- PDF: https://aclanthology.org/2026.findings-acl.99.pdf
- Local PDF: pdf/2026-08-10_21_MulDimIF_ A Multi-Dimensional Constraint Framework for Evaluating and Improving Instruction Following in Large Language.pdf

Instruction following refers to the ability of large language models (LLMs) to generate outputs that satisfy all specified constraints. Existing research has primarily focused on constraint categories, offering limited evaluation dimensions and little guidance for improving instruction-following abilities. To address this gap, we introduce MulDimIF, a multi-dimensional constraint framework encompassing three constraint patterns, four constraint categories, and four difficulty levels. Based on this framework, we design a controllable instruction generation pipeline. Through constraint expansion, conflict detection, and instruction rewriting, we construct 9,106 code-verifiable samples. We evaluate 18 LLMs from six model families and find marked performance differences across constraint settings. For instance, average accuracy decreases from 80.82% at Level I to 36.76% at Level IV. Moreover, training with data generated by our framework significantly improves instruction following without compromising general performance. In-depth analysis indicates that these gains stem largely from parameter updates in attention modules, which strengthen constraint recognition and adherence. Code and data are available in https://github.com/Junjie-Ye/MulDimIF .

## 22. ReasonRank: Empowering Passage Ranking with Strong Reasoning Ability

- Authors: Wenhan Liu, Xinyu Ma, Weiwei Sun, Yutao Zhu, Yuchen Li, Dawei Yin, Zhicheng Dou
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.790758310677191
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1005/
- PDF: https://aclanthology.org/2026.acl-long.1005.pdf
- Local PDF: pdf/2026-08-10_22_ReasonRank_ Empowering Passage Ranking with Strong Reasoning Ability.pdf

Large Language Model (LLM) based listwise ranking has shown superior performance in many passage ranking tasks. With the development of Large Reasoning Models (LRMs), many studies have demonstrated that step-by-step reasoning during test-time helps improve listwise ranking performance. However, due to the scarcity of reasoning-intensive training data, existing rerankers perform poorly in many complex ranking scenarios, and the ranking ability of reasoning-intensive rerankers remains largely underdeveloped. In this paper, we first propose an automated reasoning-intensive training data synthesis framework, which sources training queries and passages from diverse domains and applies DeepSeek-R1 to generate high-quality training labels. To empower the listwise reranker with strong reasoning ability, we further propose a two-stage training approach, which includes a cold-start supervised fine-tuning (SFT) stage and a reinforcement learning (RL) stage. During the RL stage, we design a novel multi-view ranking reward tailored to the multi-turn nature of listwise ranking. Extensive experiments demonstrate that our trained reasoning-intensive reranker ReasonRank outperforms existing baselines significantly and also achieves much lower latency than the pointwise reranker.

## 23. StructBreak: Structural Cognitive Overload-Induced Safety Failures in MLLMs

- Authors: Yang Luo, Liu Xinran, TianTian Ji, Zhiyi Yin, Lingyun Peng, Shuyu Li
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.7905162414105478
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.293/
- PDF: https://aclanthology.org/2026.findings-acl.293.pdf
- Local PDF: pdf/2026-08-10_23_StructBreak_ Structural Cognitive Overload-Induced Safety Failures in MLLMs.pdf

Multimodal Large Language Models (MLLMs) excel at structural reasoning yet suffer from a sharp logical brittleness in structural consistency. We term this phenomenon Structural Cognitive Overload (SCO), a byproduct of the contention between deep reasoning and safety alignment. However, prior work has predominantly targeted typographic and pixel-level perturbations, leaving the study of SCO largely unexplored. To this end, we propose StructBreak, an automated end-to-end framework designed to quantify SCO. By leveraging StructBreak, we uncover a novel higher-order cognitive overload attack paradigm; notably, this attack operates under a practical black-box setting, requiring no internal model access. Consequently, we utilize this framework to establish a comprehensive benchmark spanning ten diverse threat scenarios. Empirical evaluations on six leading MLLMs reveal that SCO readily triggers toxic generation, yielding a 92% average ASR (up to 97% on Gemini 2.5). To elucidate the mechanism of SCO, we further conduct model-level interpretations spanning attention dynamics, latent space topology, and geometric analysis. Our findings reveal that StructBreak acts as a novel structural channel to circumvent safety filters. Furthermore, the limited efficacy of inherent safety mechanisms underscores that current alignment paradigms are insufficient for the era of complex multimodal reasoning.

## 24. Heterogeneity in Formal Linguistic Competence of Language Models: Is Data the Real Bottleneck?

- Authors: H S V N S Kowndinya Renduchintala, Sumit Bhatia
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.7903606379874075
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.224/
- PDF: https://aclanthology.org/2026.findings-acl.224.pdf
- Local PDF: pdf/2026-08-10_24_Heterogeneity in Formal Linguistic Competence of Language Models_ Is Data the Real Bottleneck.pdf

Large Language Models (LLMs) exhibit a puzzling disparity in their formal linguistic competence: while they learn some linguistic phenomena with near-perfect mastery, they often perform below chance on others, even after training on trillions of tokens. In this work, we investigate whether these failures stem from inherent architectural limitations or simply the scarcity of these specific grammatical constructions in web-scale corpora. We pre-train simple GPT-2 Small (124M) models on a 100M-token random sample of the FineWeb corpus and intervene by injecting a minimal amount (1%) of synthetic data targeting specific linguistic phenomena. We find that this targeted intervention substantially improves model performance in 8 out of the 9 worst-performing BLiMP paradigms – notably the accuracy on a specific paradigm, only_npi_scope, surges from 20.9% to 69.4%. Furthermore, we observe that these interventions generally preserve or slightly improve aggregate performance. However, while we also identify a resistant phenomenon, principle_A_c_command, whose performance remains below chance even after our data augmentation, our findings do serve as an optimistic existence proof that even small language models can substantially improve on those linguistic phenomena on which models typically perform poorly, provided the pre-training data contains sufficient exposure to them. This suggests that efforts towards human-scale language modeling may benefit greatly by focusing on data composition. The code to reproduce our results is open-sourced at https://github.com/kowndinya-renduchintala/heterogeneity-in-formal-linguistic-competence .

## 25. Minimal Free Resolution Guided Adaptive Tree Reasoning

- Authors: Dezhao Tang, Meihan Liu, Yulai Tong, Guan Yuan, Qiuyan Yan
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.7902041820529173
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.2158/
- PDF: https://aclanthology.org/2026.acl-long.2158.pdf
- Local PDF: pdf/2026-08-10_25_Minimal Free Resolution Guided Adaptive Tree Reasoning.pdf

Dynamic reasoning trees can help large language models solve complex tasks by explicitly structuring intermediate decisions.However, existing approaches often rely on manually specified subproblems or predefined decomposition patterns, which limits the effectiveness of reasoning and generalization.To solve this problem, we propose SyRA, a hierarchical reasoning framework based on MFR theory that supports the construction of adaptive reasoning trees and reliable error correction within a single LLM. Specifically, SyRA focuses on reasoning-tree construction, dynamically controlling branching and expansion using MFR principles to enable informative, non-redundant subproblem decomposition. In addition, it introduces a residual backtracking mechanism for adaptive cross-layer error correction, allowing the model to revise earlier reasoning decisions based on downstream feedback.Across eight reasoning benchmarks, SyRA significantly reduces logical errors and improves reasoning accuracy, while achieving a better balance between accuracy and reasoning time than the Chain-of-Thought, Decompose–Analyze–Rethink and Tree-of-Thought. Our code and dataset are available at https://github.com/Tim798-art/SyRA/tree/main/SyRA .

## 26. CreditDecoding: Accelerating Parallel Decoding in Diffusion Large Language Models with Trace Credit

- Authors: Kangyu Wang, Zhiyun Jiang, Haibo Feng, Weijia Zhao, Lin Liu, Jianguo Li, Zhenzhong Lan, Weiyao Lin
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.790101056605703
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.509/
- PDF: https://aclanthology.org/2026.acl-long.509.pdf
- Local PDF: pdf/2026-08-10_26_CreditDecoding_ Accelerating Parallel Decoding in Diffusion Large Language Models with Trace Credit.pdf

Diffusion large language models (dLLMs) generate text through iterative denoising. In commonly adopted parallel decoding schemes, each step confirms only high-confidence positions while remasking the others. By analyzing dLLM denoising traces, we uncover a key inefficiency: models often predict the correct target token several steps before its confidence becomes high enough to be decoded. This gap between early prediction and late decoding forces repeated remasking of already-correct tokens, causing redundant iterations and limiting acceleration. To exploit this temporal redundancy, we introduce Trace Credit to quantify a token’s decoding potential by accumulating historical evidence. Building on this, we propose CreditDecoding, a training-free parallel decoding method that fuses Trace Credit with current logits to boost the confidence of correct but underconfident tokens, thereby accelerating denoising and improving robustness. On eight benchmarks, CreditDecoding achieves up to 5.48 times speedup with +0.48 accuracy on LLaDA-8B and consistently improves performance across diverse dLLM architectures and parameter scales. It further scales to long contexts and remains orthogonal to mainstream inference optimizations, making it a practical and widely applicable solution.

## 27. Don’t Adapt Small Language Models for Tools; Adapt Tool Schemas to the Models

- Authors: Jonggeun Lee, Woojung Song, Jongwook Han, Haesung Pyun, Yohan Jo
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.788786792388467
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.948/
- PDF: https://aclanthology.org/2026.acl-long.948.pdf
- Local PDF: pdf/2026-08-10_27_Don’t Adapt Small Language Models for Tools; Adapt Tool Schemas to the Models.pdf

Small language models (SLMs) enable scalable tool-augmented multi-agent systems where multiple SLMs handle subtasks orchestrated by a powerful coordinator. However, they struggle with tool-use tasks, particularly in selecting appropriate tools and identifying correct parameters. A common failure mode is schema misalignment : models hallucinate plausible tool names that are absent from the provided tool schema, due to different naming conventions internalized during pretraining. Rather than training models to adapt to unfamiliar schemas, we propose adapting schemas to align with models’ pretrained knowledge. We introduce PA-Tool (Pretraining-Aligned Tool Schema Generation), a training-free method that leverages peakedness, a signal used in contamination detection that indicates pretraining familiarity, to rename tool components. By generating multiple candidates and selecting the candidate with the highest peakedness, PA-Tool identifies pretraining-aligned naming patterns. Experiments on MetaTool and RoTBench show improvements of up to 17%, with schema misalignment errors reduced by 80%. PA-Tool enables small models to substantially improve tool-use accuracy without retraining, showing that schema-level interventions can unlock the tool-use potential of resource-efficient models. Our code is available at https://github.com/holi-lab/PA-Tool .

## 28. UrbanGeoEval: A City-Scale Benchmark for Evaluating Large Language Models in Geospatial Reasoning

- Authors: Mutian Bao, Qiuyi Qi, Tian Liang, Jinjian Zhang, Wei Zhou, Ming Kong, Linjian Mo, Qiang Zhu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.788620647980171
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1867/
- PDF: https://aclanthology.org/2026.acl-long.1867.pdf
- Local PDF: pdf/2026-08-10_28_UrbanGeoEval_ A City-Scale Benchmark for Evaluating Large Language Models in Geospatial Reasoning.pdf

Current evaluations of geospatial reasoning in LLMs are frequently impeded by the entanglement of factual recall and spatial logic, which often obscures the models’ true capabilities in complex city-scale environments. To address this, we introduce UrbanGeoEval, a comprehensive benchmark featuring a dual-module framework designed to disentangle these competencies. The Knowledge Module assesses urban memory via scalable map-based queries, while the Reasoning Module isolates pure logical inference across 3,148 realistic tasks by providing necessary geospatial context. Unlike prior benchmarks that hand the model pre-computed spatial text, UrbanGeoEval provides raw geometry and forces the model to act as a spatial computing engine. Our evaluation methodology introduces a reliable hybrid pipeline that merges deterministic programmatic checks with an LLM-as-a-Judge, achieving expert-level evaluation accuracy. Extensive experiments on 18 widely used LLMs uncover critical insights: (1) models exhibit severe geographic biases and resolution gaps; (2) failures in complex multi-hop tasks often stem from brittle foundational spatial skills rather than high-level logic deficits. UrbanGeoEval provides a precise diagnostic tool for advancing urban geospatial intelligence in LLMs.

## 29. Coarse-to-Fine Multimodal Information Selection for Video Speaking Style Recognition with Large Language Models

- Authors: Beibei Zhang, Yanan Lu, Lin Fen, Tongwei Ren
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.7884780259510826
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1466/
- PDF: https://aclanthology.org/2026.findings-acl.1466.pdf
- Local PDF: pdf/2026-08-10_29_Coarse-to-Fine Multimodal Information Selection for Video Speaking Style Recognition with Large Language Models.pdf

Video Speaking Style Recognition (VSSR) aims to classify conversation videos into different types, significantly facilitating human interaction understanding. Recent approaches explore the potential of large language models (LLM) in VSSR with a training-free process. However, directly integrating all multimodal data yields suboptimal results, since the great redundancy in visual data can overshadow other valuable multimodal information, such as valuable textual dialogues and critical visual clues. To address this, we propose CFMiS (Coarse-to-Fine Multimodal Information Selection), a novel framework for VSSR that dynamically obtain valuable multimodal data via coarse-to-fine selection, enhancing LLM reasoning for VSSR. Specifically, the core of CFMiS are two cascaded modules: 1) a text-dominant modality selection module firstly selects VSSR-required modalities originating from text-based prediction; and 2) if vision is included in the selected modalities, a visual refinement module iteratively collects VSSR-relevant critical visual clues. The former resolves which modality to utilize, while the latter determines which information to adopt from selected modalities, efficiently alleviating information redundancy. Extensive experiments on multiple datasets prove that CFMiS is highly effective for VSSR, outperforming all existing training-free approaches and most training-based methods.

## 30. Exons-Detect: Identifying and Amplifying Exonic Tokens via Hidden-State Discrepancy for Robust AI-Generated Text Detection

- Authors: Xiaowei Zhu, Yubing Ren, Fang Fang, Shi Wang, Yanan Cao, Li Guo
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.788326000022243
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1211/
- PDF: https://aclanthology.org/2026.acl-long.1211.pdf
- Local PDF: pdf/2026-08-10_30_Exons-Detect_ Identifying and Amplifying Exonic Tokens via Hidden-State Discrepancy for Robust AI-Generated Text Detecti.pdf

The rapid advancement of large language models has increasingly blurred the boundary between human-written and AI-generated text, raising societal risks such as misinformation dissemination, authorship ambiguity, and threats to intellectual property rights. These concerns highlight the urgent need for effective and reliable detection methods. While existing training-free approaches often achieve strong performance by aggregating token-level signals into a global score, they typically assume uniform token contributions, making them less robust under short sequences or localized token modifications. To address these limitations, we propose Exons-Detect, a training-free method for AI-generated text detection based on an exon-aware token reweighting perspective. Exons-Detect identifies and amplifies informative exonic tokens by measuring hidden-state discrepancy under a dual-model setting, and computes an interpretable translation score from the resulting importance-weighted token sequence. Empirical evaluations demonstrate that Exons-Detect achieves state-of-the-art detection performance and exhibits strong robustness to adversarial attacks and varying input lengths. In particular, it attains a 2.2% relative improvement in average AUROC over the strongest prior baseline on DetectRL.
