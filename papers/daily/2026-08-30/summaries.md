# Paper Daily Reading - 2026-08-30

## 1. scProtoTransformer: Scalable reference mapping across molecules, cells, and donors

- Authors: Zhenchao Tang, Haohuai He, Shouzhi Chen, Jun Zhu, Tianxu Lv, Zhou Jiale, Jiehui Huang, Yaokun Li, Guanxing Chen, Linlin You, Calvin Yu‐Chian Chen
- Source: openalex
- Venue type: journal
- Journal: Science Advances
- Publication status: published
- Publication date: 2026-08-28
- DOI: https://doi.org/10.1126/sciadv.aef0286
- Categories: Single-cell and spatial transcriptomics, Cell Image Analysis Techniques, Bioinformatics and Genomic Networks
- Relevance: 3.6550764013606827
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://doi.org/10.1126/sciadv.aef0286
- PDF: Unavailable
- Local PDF: Not downloaded

Abstract The rapid accumulation of single-cell data has made it possible to comprehensively characterize biological systems at molecular, cellular, and donor levels. However, scalable reference mapping across different resolutions remains a major challenge in current research. Here, we propose scProtoTransformer , a prototype-based Transformer architecture designed to achieve scalable reference mapping across molecular, cell, and donor levels. scProtoTransformer introduces a knowledge-guided prototype tokenizer that projects gene expression into biologically interpretable pathway prototypes, effectively reducing numerical batch effects while preserving biological semantic patterns. Furthermore, by leveraging knowledge distilled from the foundation model and a dynamic supervised fine-tuning strategy, scProtoTransformer achieves robust biological representations with reduced pre-training requirements. Benchmark experiments across molecular, cell, and donor-level reference mapping demonstrate that scProtoTransformer delivers competitive or even superior performance compared with state-of-the-art approaches, while providing interpretability through biologically prototypes. Together, these results establish scProtoTransformer as a unified framework for scalable reference mapping, laying the foundation for systematic understanding from genes to individuals.

## 2. Hi-Cformer enables multiscale chromatin contact map modeling for single-cell Hi-C data analysis

- Authors: Xiaoqing Wu, Zian Wang, Rui Jiang, Xiaoyang Chen
- Source: openalex
- Venue type: journal
- Journal: Science Advances
- Publication status: published
- Publication date: 2026-08-28
- DOI: https://doi.org/10.1126/sciadv.aeg0134
- Categories: Genomics and Chromatin Dynamics, Single-cell and spatial transcriptomics, RNA Research and Splicing
- Relevance: 3.5483179483547405
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://doi.org/10.1126/sciadv.aeg0134
- PDF: Unavailable
- Local PDF: Not downloaded

Abstract Single-cell Hi-C captures the three-dimensional organization of chromatin in individual cells and provides insights into fundamental genomic processes such as gene regulation and transcription. While analyses of bulk Hi-C data have revealed multi-scale chromatin structures like A/B compartments and topologically associating domains, single-cell Hi-C data remain challenging to analyze due to sparsity and uneven distribution of chromatin contacts across genomic distances. These characteristics lead to strong signals near the diagonal and complex multi-scale local patterns in single-cell contact maps. Here, we propose Hi-Cformer, a transformer-based method that simultaneously models multi-scale blocks of chromatin contact maps and incorporates a specially designed attention mechanism to capture the dependencies between chromatin interactions across genomic regions and scales, enabling the integration of both global and fine-grained chromatin interaction features. Building on this architecture, Hi-Cformer robustly derives low-dimensional representations of cells from single-cell Hi-C data, achieving clearer separation of cell types compared to existing methods. Hi-Cformer can also accurately impute chromatin interaction signals associated with cellular heterogeneity, including 3D genome features such as topologically associating domain-like boundaries and A/B compartments. Furthermore, by leveraging its learned embeddings, Hi-Cformer can be extended to cell type annotation, achieving high accuracy and robustness across both intra- and inter-dataset scenarios.

## 3. ChromSkills enables interpretable and domain-guided agentic chromatin data analysis

- Authors: Yuxuan Zhang, Yiman Wang, Yang Tan, Yong Zhang
- Source: openalex
- Venue type: journal
- Journal: Genome biology
- Publication status: published
- Publication date: 2026-08-29
- DOI: https://doi.org/10.1186/s13059-026-04263-z
- Categories: Genomics and Chromatin Dynamics, Genomics and Rare Diseases, Chromatin Remodeling and Cancer
- Relevance: 2.7952878367421374
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://doi.org/10.1186/s13059-026-04263-z
- PDF: Unavailable
- Local PDF: Not downloaded

Abstract High-throughput chromatin assays require flexible workflows and context-aware parameter choices. However, unconstrained large language model-based analysis can suffer from inconsistent tool selection, parameterization, and execution. We present ChromSkills, a curated library of domain-specific analytical Skills for agentic chromatin data analysis on coding-agent platforms that support Skills. ChromSkills encodes expert decision logic and parameter-selection rules as modular, human-readable Skills linked to structured tool interfaces, enabling interpretable workflow composition and consistent execution from natural-language tasks. Across representative analyses, ChromSkills improved tool and parameter consistency, execution stability, and token efficiency, providing a transparent and domain-guided framework for AI-assisted chromatin data analysis.

## 4. ReTRE: Benchmarking LLM Transfer Robustness with Structure-Preserving Variants

- Authors: ZhongDong Li, Weijie Shi, Yue Cui, Haolun MA, Yuanjun Liu, Jiawei Li, An Liu, Jia Zhu, Jiajie Xu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.752435538906566
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.2048/
- PDF: https://aclanthology.org/2026.acl-long.2048.pdf
- Local PDF: pdf/2026-08-30_04_ReTRE_ Benchmarking LLM Transfer Robustness with Structure-Preserving Variants.pdf

Large language models (LLMs) have achieved strong performance on standard benchmarks, yet their performance is not robust across different task manifestations. It remains unclear how performance changes under controlled task rewrites that preserve the original solution structure, while varying the rewrite type and level. To address this question, we introduce ReTRE (Rewrite-based Transfer Robustness Evaluation), an evaluation benchmark inspired by learning transfer theory that probes transfer robustness along two rewrite levels: Near Transfer and Far Transfer. ReTRE employs a multi-agent system to construct textual and visual variants while preserving the structure of the original solution. Evaluations on mathematical and science tasks across state-of-the-art multimodal LLMs reveal a consistent transfer gap: performance exhibits a general declining trend as transfer similarity drops and strong text performance can face performance decline under cross-modal transfer. Crucially, we identify a divergence between post-training paradigms: reinforcement learning preserves transfer robustness, whereas supervised fine-tuning tends to overfit the training distribution, leading to severe degradation in far-transfer performance despite strong in-distribution accuracy.

## 5. How Large Language Models Balance Internal Knowledge with User and Document Assertions

- Authors: Shuowei Li, Haoxin Li, Wenda Chu, Yi Fang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.7490725547803403
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1267/
- PDF: https://aclanthology.org/2026.findings-acl.1267.pdf
- Local PDF: pdf/2026-08-30_05_How Large Language Models Balance Internal Knowledge with User and Document Assertions.pdf

Large language models (LLMs) often need to balance their internal parametric knowledge with external information, such as user beliefs and content from retrieved documents, in real-world scenarios like RAG or chat-based systems. A model’s ability to reliably process these sources is key to system safety. Previous studies on knowledge conflict and sycophancy are limited to a binary conflict paradigm, primarily exploring conflicts between parametric knowledge and either a document or a user, but ignoring the interactive environment where all three sources exist simultaneously. To fill this gap, we propose a three-source interaction framework and systematically evaluate 27 LLMs from 3 families on 2 datasets. Our findings reveal general patterns: most models rely more on document assertions than user assertions, and this preference is reinforced by post-training. Furthermore, our behavioral analysis shows that most models are impressionable, unable to effectively discriminate between helpful and harmful external information. To address this, we demonstrate that fine-tuning on diverse source interaction data can significantly increase a model’s discrimination abilities. In short, our work paves the way for developing trustworthy LLMs that can effectively and reliably integrate multiple sources of information. Code is available at https://github.com/shuowl/llm-source-balancing .

## 6. Federated LoRA Fine-Tuning with Pipelined Error-Mitigated Aggregation and Matrix-Wise Freezing

- Authors: Haoran Wang, Xiong Wang, Yuqing Li, Jing Chen, Junyi Zhang, Nan Yan, Kun He, Wei Wang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.7469942647823498
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.284/
- PDF: https://aclanthology.org/2026.findings-acl.284.pdf
- Local PDF: pdf/2026-08-30_06_Federated LoRA Fine-Tuning with Pipelined Error-Mitigated Aggregation and Matrix-Wise Freezing.pdf

Federated low-rank adaptation (LoRA) enables multiple clients to collaboratively fine-tune large language models (LLMs) without disclosing their raw data. However, existing works often experience performance degradation due to biased model aggregation and are hindered by significant communication and computation burden, both limiting training efficiency. In this paper, we propose iFLoRA, an improved Federated LoRA fine-tuning system for LLMs featuring pipelined error-mitigated model aggregation and adaptive matrix-wise parameter freezing. Specifically, iFLoRA mitigates aggregation error by first reconstructing local update matrices from clients’ low-rank matrices. These are then aggregated into a global update, which is decomposed via singular value decomposition (SVD) to form low-rank matrices for the next round. To mitigate the overhead from SVD, iFLoRA employs a pipeline to overlap global aggregation, local computation, and communication. Additionally, iFLoRA implements an adaptive matrix-wise freezing scheme that assesses their stability and selectively freezes them for adaptively adjusted periods, alleviating client training overheads without compromising model performance. Extensive experiments on real-world datasets show that iFLoRA can improve time-to-target by 2.17-8.48× than state-of-the-art methods. Our code is available at: https://github.com/whr819987540/iflora .

## 7. Fast-MIA: Efficient and Scalable Membership Inference for LLMs

- Authors: Hiromu Takahashi, Shotaro Ishihara
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.746948190587565
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-demo.9/
- PDF: https://aclanthology.org/2026.acl-demo.9.pdf
- Local PDF: pdf/2026-08-30_07_Fast-MIA_ Efficient and Scalable Membership Inference for LLMs.pdf

We propose Fast-MIA ( https://github.com/Nikkei/fast-mia ), a Python library for efficiently evaluating membership inference attacks (MIA) against large language models (LLMs). MIA has emerged as a crucial technique for auditing privacy risks and copyright infringement in LLMs. However, computational demands have grown substantially: recent methods rely on repeated inference, while practical auditing requires large-scale evaluation. Progress is further hindered by existing implementations that execute methods independently, redundantly computing shared intermediate results such as log-probabilities. To address these challenges, Fast-MIA combines two strategies: (1) high-throughput batch inference via vLLM, achieving approximately 5 × speedup, and (2) a cross-method caching architecture that computes intermediate results once and shares them across methods.The library includes representative MIA methods under a unified framework, integrates with established benchmarks, and supports flexible YAML configuration.We release Fast-MIA under the Apache License 2.0 to support scalable and reproducible MIA research.

## 8. Min- k Sampling: Decoupling Truncation from Temperature Scaling via Relative Logit Dynamics

- Authors: Yuanhao Ding, Meimingwei Li, Esteban Garces Arias, Matthias Aßenmacher, Christian Heumann, Chongsheng Zhang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.7467839911358616
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.681/
- PDF: https://aclanthology.org/2026.acl-long.681.pdf
- Local PDF: pdf/2026-08-30_08_Min- k Sampling_ Decoupling Truncation from Temperature Scaling via Relative Logit Dynamics.pdf

The quality of text generated by large language models depends critically on the decoding sampling strategy. While mainstream methods such as Top- k , Top- p , and Min- p achieve a balance between diversity and accuracy through probability-space truncation, they share an inherent limitation: extreme sensitivity to the temperature parameter. Recent logit-space approaches like Top- n𝜎 achieve temperature invariance but rely on global statistics that are susceptible to long-tail noise, failing to capture fine-grained confidence structures among top candidates. We propose Min- k Sampling , a novel dynamic truncation strategy that analyzes the local shape of the sorted logit distribution to identify “semantic cliffs”: sharp transitions from high-confidence core tokens to uncertain long-tail tokens. By computing a position-weighted relative decay rate, Min- k dynamically determines truncation boundaries at each generation step. We formally prove that Min- k achieves strict temperature invariance and empirically demonstrate its low sensitivity to hyperparameter choices. Experiments on multiple reasoning benchmarks, creative writing tasks, and human evaluation show that Min- k consistently improves text quality, maintaining robust performance even under extreme temperature settings where probability-based methods collapse. We make our code, models, and analysis tools publicly available.

## 9. MSEarth: A Multimodal Benchmark for Earth Science Phenomenon Discovery with MLLMs

- Authors: Xiangyu Zhao, Wanghan Xu, Bo Liu, Yuhao Zhou, Fenghua Ling, Ben Fei, Xiaoyu Yue, Lei Bai, Wenlong Zhang, Xiao-Ming Wu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.7464067392023273
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.239/
- PDF: https://aclanthology.org/2026.acl-long.239.pdf
- Local PDF: pdf/2026-08-30_09_MSEarth_ A Multimodal Benchmark for Earth Science Phenomenon Discovery with MLLMs.pdf

The rapid advancement of multimodal large language models (MLLMs) offers new opportunities for complex scientific challenges, yet their application in earth science—especially at the graduate level—remains underexplored due to a lack of benchmarks reflecting the depth and complexity of geoscientific reasoning. Existing datasets often rely on synthetic data or simple figure-caption pairs, failing to capture the nuanced reasoning required for real-world applications. To address this, we introduce MSEarth, a multimodal scientific dataset and benchmark curated from high-quality, open-access publications. Covering the five major spheres of Earth science—atmosphere, cryosphere, hydrosphere, lithosphere, and biosphere—MSEarth features over 289K figures with refined captions enriched by contextual discussions and reasoning from the original papers. The benchmark supports tasks such as scientific figure captioning, multiple choice questions, and open-ended reasoning, providing a scalable, high-fidelity resource for developing and evaluating MLLMs in scientific reasoning.

## 10. MEAV: Model Editing with Alignment Vectors for inference time LLM alignment in single and multidomain preference spectrum

- Authors: Sadat Shahriar, Zheng Qi, Nikolaos Pappas, Srikanth Doss, Kishaloy Halder, Monica Sunkara, Manuel Mager, Yassine Benajiba
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.7458698210742365
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.2035/
- PDF: https://aclanthology.org/2026.findings-acl.2035.pdf
- Local PDF: pdf/2026-08-30_10_MEAV_ Model Editing with Alignment Vectors for inference time LLM alignment in single and multidomain preference spectru.pdf

Aligning Large Language Models (LLM) to address subjectivity and nuanced preference levels requires adequate flexibility and control, which can be a resource-intensive and time-consuming procedure. Existing training-time alignment methods require full re-training when a change is needed and inference-time ones typically require access to the reward model at each inference step. We introduce MEAV , an inference-time model-editing-based LLM alignment method that learns encoded representations of preference dimensions, called Alignment Vectors (AV). These representations enable dynamic adjusting of the model behavior during inference through simple linear operations. Here, we focus on three gradual response levels across three specialized domains: medical, legal, and financial, exemplifying its practical potential. This new alignment paradigm introduces adjustable preference knobs during inference, allowing users to tailor their LLM outputs while reducing the inference cost by half compared to the prompt engineering approach. Additionally, we find that AVs are transferable across different fine-tuning stages of the same model, demonstrating their flexibility. AVs also facilitate multidomain, diverse preference alignment, making the process 12x faster than the retraining approach.

## 11. PAR 2 -RAG: Planned Active Retrieval and Reasoning for Multi-Hop Question Answering

- Authors: Xingyu Li, Rongguang Wang, Yuying Wang, Mengqing Guo, Chenyang Li, Tao Sheng, Sujith Ravi, Dan Roth
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.7454219623985865
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-industry.118/
- PDF: https://aclanthology.org/2026.acl-industry.118.pdf
- Local PDF: pdf/2026-08-30_11_PAR 2 -RAG_ Planned Active Retrieval and Reasoning for Multi-Hop Question Answering.pdf

Multi-hop question answering (MHQA) is a practical bottleneck in industry applications such as enterprise assistants, customer-support copilots, and compliance analysis, where systems must combine evidence across multiple documents before answering. Large language models (LLMs) remain brittle in this setting: iterative retrieval can commit too early to low-recall trajectories, while planning-only approaches can produce static query sets that fail to adapt when intermediate evidence changes. We propose Planned Active Retrieval and Reasoning RAG (PAR 2 -RAG) , a training-free two-stage framework that separates coverage from commitment . PAR 2 -RAG first performs breadth-first anchoring to build a high-recall evidence frontier, then applies depth-first refinement with evidence sufficiency control in an iterative loop. This design targets deployment constraints by avoiding retraining cycles, reducing maintenance overhead under changing corpora, and improving scalability across domains. Across four MHQA benchmarks, PAR 2 -RAG consistently outperforms strong baselines: compared with IRCoT, it achieves up to 23.5% higher answer accuracy and up to 10.5% NDCG gains in retrieval quality.

## 12. Gradient-Guided Multi-Judge Prompt Optimization

- Authors: ChenZhuo Zhao, Xinda Wang, Pu Zhao, Yue Huang, Junting Lu, Ziqian Liu, Qingwei Lin, Saravan Rajmohan, Dongmei Zhang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.74516432925366
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1089/
- PDF: https://aclanthology.org/2026.acl-long.1089.pdf
- Local PDF: pdf/2026-08-30_12_Gradient-Guided Multi-Judge Prompt Optimization.pdf

Automatic prompt optimization is a practical alternative to fine-tuning for adapting large language models (LLMs), yet existing approaches often trade off signal quality against computational cost. Methods that rely on generative feedback can be informative but expensive to scale, while sampling-based optimization typically requires many evaluations and exhibits high variance. Even loss-driven prompt optimization remains limited by costly segment attribution that scales with prompt length and by overfitting to a single evaluator, which weakens transfer across model families and domains. We propose Gradient-guided Multi-judge Prompt Optimization (GMPO), a scalable framework that improves both efficiency and robustness. GMPO uses a first-order gradient approximation to score segment importance in a continuous masking direction, requiring only one forward and one backward pass. GMPO further employs a generate multi-judge design in which candidate prompt edits are proposed by a generator and selected using cross-entropy losses aggregated from multiple lightweight judge models, reducing evaluator bias and improving generalization. Experiments across math, reasoning, instruction-following evaluation, and safety robustness benchmarks demonstrate consistent gains with substantially lower optimization overhead.

## 13. When Backdoors Go Beyond Triggers: Semantic Drift in Diffusion Models Under Encoder Attacks

- Authors: Shenyang Chen, Liuwan Zhu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.7449296112316777
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1421/
- PDF: https://aclanthology.org/2026.findings-acl.1421.pdf
- Local PDF: pdf/2026-08-30_13_When Backdoors Go Beyond Triggers_ Semantic Drift in Diffusion Models Under Encoder Attacks.pdf

Standard evaluations of backdoor attacks on text-to-image (T2I) models primarily measure trigger activation and visual fidelity. We challenge this paradigm, demonstrating that encoder-side poisoning induces persistent, trigger-free semantic corruption that fundamentally reshapes the representation manifold. We trace this vulnerability to a geometric mechanism: a Jacobian-based analysis reveals that backdoors act as low-rank, target-centered deformations that amplify local sensitivity, causing distortion to propagate coherently across semantic neighborhoods. To rigorously quantify this structural degradation, we introduce SEMAD (Semantic Alignment and Drift), a diagnostic framework that measures both internal embedding drift and downstream functional misalignment. Our findings, validated across diffusion and contrastive paradigms, expose the deep structural risks of encoder poisoning and highlight the necessity of geometric audits beyond simple attack success rates.

## 14. SELECting over Tokens: Curating Pre-training Data at Scale via Token Classification

- Authors: Xin Tong, Weidong Zhang, Jiaang Li, Haibin Chen, Shilei Liu, Langming Liu, Kangtao Lv, Yujin Yuan, Wenbo Su, Bo Zheng
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.7448941031758025
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.2219/
- PDF: https://aclanthology.org/2026.acl-long.2219.pdf
- Local PDF: pdf/2026-08-30_14_SELECting over Tokens_ Curating Pre-training Data at Scale via Token Classification.pdf

The quality of pre-training data critically impacts the capabilities of large language models. Existing pipelines rely on expert-crafted heuristic rules, which primarily operate at the sample level and are based on coarse statistical indicators, thus lacking content-aware, fine-grained noise detection. While recent generative approaches, e.g., ProX-C, enable token-level refinement, their reliance on synthesizing Python code incurs prohibitive computational cost at scale and can introduce hallucinations into the refined data. To overcome these limitations, we propose Selecting over Tokens (SelecT), a novel framework that reframes data refinement as a highly efficient token classification task. SelecT classifies each token as either informative or noisy and subsequently removes the latter. This design achieves fine-grained data optimization while avoiding the inefficiency of generation, ensuring scalability. When evaluated on diverse downstream benchmarks, the model trained on SelecT-refined corpora, on average, outperforms the one trained on raw data by over 2% and exceeds the best heuristic baselines by more than 1% while preserving 17% more tokens than the latter. Furthermore, SelecT achieves higher average performance than the generative ProX-C across all experimental settings, and is 2.5x faster at inference, even with twice the parameters. Our results establish SelecT as an effective, efficient, and scalable solution for pre-training data optimization.

## 15. GRASS: Gradient-based Adaptive Layer-wise Importance Sampling for Memory-efficient Large Language Model Fine-tuning

- Authors: Kaiyuan Tian, Linbo Qiao, Yu Tang, Gongqingjian Jiang, Baihui Liu, Yifu Gao, Xialin Su, Dongsheng Li
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.744885312928205
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.475/
- PDF: https://aclanthology.org/2026.findings-acl.475.pdf
- Local PDF: pdf/2026-08-30_15_GRASS_ Gradient-based Adaptive Layer-wise Importance Sampling for Memory-efficient Large Language Model Fine-tuning.pdf

Full-parameter fine-tuning of large language models is constrained by substantial GPU memory demands. Low-rank adaptation methods mitigate this challenge by updating only a subset of parameters. However, these approaches often limit model expressiveness and yield lower performance than full-parameter fine-tuning. Layer-wise fine-tuning methods have emerged as an alternative, enabling memory-efficient training through static layer importance sampling strategies. However, these methods overlook variations in layer importance across tasks and training stages, resulting in suboptimal performance on downstream tasks. To address these limitations, we propose GRASS, a gradient-based adaptive layer-wise importance sampling framework. GRASS utilizes mean gradient norms as a task-aware and training-stage-aware metric for estimating layer importance. Furthermore, GRASS adaptively adjusts layer sampling probabilities through an adaptive training strategy. We also introduce a layer-wise optimizer state offloading mechanism to further reduce memory usage while maintaining comparable training throughput. Extensive experiments across multiple models and benchmarks demonstrate that GRASS consistently outperforms state-of-the-art methods, achieving an average accuracy improvement of up to 4.38 points and reducing memory usage by up to 19.97%.

## 16. MEDSYN: Benchmarking Multi-EviDence SYNthesis in Complex Clinical Cases for Multimodal Large Language Models

- Authors: Boqi Chen, Xudong Liu, Jiachuan Peng, Marianne Frey-Marti, Kyle Lam, Bang Zheng, Lin Li, Jianing Qiu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.744522678984746
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1183/
- PDF: https://aclanthology.org/2026.findings-acl.1183.pdf
- Local PDF: pdf/2026-08-30_16_MEDSYN_ Benchmarking Multi-EviDence SYNthesis in Complex Clinical Cases for Multimodal Large Language Models.pdf

Multimodal large language models (MLLMs) have shown great potential in medical applications, yet existing benchmarks inadequately capture real-world clinical complexity. We introduce MEDSYN, a multilingual, multimodal benchmark of highly complex clinical cases with up to 7 distinct visual clinical evidence (CE) types per case. Mirroring clinical workflow, we evaluate 18 MLLMs on differential diagnosis (DDx) generation and final diagnosis (FDx) selection. While frontier models often match or even outperform human experts on DDx generation, all MLLMs exhibit a much larger DDx–FDx performance gap compared to expert clinicians, indicating a failure mode in synthesis of heterogeneous CE types. Ablations attribute this failure to (i) overreliance on less discriminative textual CE ( e.g. , medical history) and (ii) a cross-modal CE utilization gap. We introduce Evidence Sensitivity to quantify the latter and show that a smaller gap correlates with higher diagnostic accuracy. Finally, we demonstrate how it can be used to guide interventions to improve model performance. https://github.com/jianing-lab/MEDSYN .

## 17. Progressive Planning and Reinforced Reasoning: Large Language Model-Guided Multi-hop Question Answering over Knowledge Graph

- Authors: Xiang Li, Runhai Jiao, Ruifan Li, Dongnan Wu, Ruojiao Qiao, Lei Liu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.743349550735151
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1147/
- PDF: https://aclanthology.org/2026.findings-acl.1147.pdf
- Local PDF: pdf/2026-08-30_17_Progressive Planning and Reinforced Reasoning_ Large Language Model-Guided Multi-hop Question Answering over Knowledge G.pdf

Reinforcement learning, with its interpretable path reasoning, has emerged as a promising paradigm for multi-hop question answering over knowledge graphs. However, existing approaches suffer from two inherent limitations: (1) lacking effective intermediate guidance, agents often fall into aimless exploration when confronted with complex multi-hop questions; and (2) policy networks focus on local neighborhood information, making it difficult to anticipate the long-term consequences of decisions. To address these challenges, we propose a Progressive Planning and Reinforced Reasoning (PPRR) framework. Specifically, we introduce large language models as multi-hop reasoning planners, converting decomposed sub-question sequences into stepwise decision guidance and thereby granting the agent human-like, step-by-step problem-solving capabilities. In addition, we design a structure-aware lookahead policy network, which explicitly models inter-node dependencies along the multi-hop reasoning process and performs lookahead value evaluations for candidate actions, thereby enhancing the agent’s global state awareness and decision foresight in complex environments. Finally, we conducted extensive experiments on four public multi-hop question answering benchmarks and one domain-specific dataset. The results demonstrate that our framework surpasses state-of-the-art methods while demonstrating strong generalization.

## 18. Learning How and What to Memorize: Cognition-Inspired Two-Stage Optimization for Evolving Memory

- Authors: Derong Xu, Shuochen Liu, Pengfei Luo, Pengyue Jia, Yingyi Zhang, Yi Wen, Yimin Deng, Wenlin Zhang, Enhong Chen, Xiangyu Zhao, Tong Xu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.7432069322177584
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.2084/
- PDF: https://aclanthology.org/2026.acl-long.2084.pdf
- Local PDF: pdf/2026-08-30_18_Learning How and What to Memorize_ Cognition-Inspired Two-Stage Optimization for Evolving Memory.pdf

Large language model (LLM) agents require long-term user memory for consistent personalization, but limited context windows hinder tracking evolving preferences over long interactions. Existing memory systems mainly rely on static, hand-crafted update rules; although reinforcement learning (RL)-based agents learn memory updates, sparse outcome rewards provide weak supervision, resulting in unstable long-horizon optimization. Drawing on memory schema theory and the functional division between prefrontal regions and hippocampus regions, we introduce MemCoE, a cognition-inspired two-stage optimization framework that learns how memory should be organized and what information to update. In the first stage, we propose Memory Guideline Induction to optimize a global guideline via contrastive feedback interpreted as textual gradients; in the second stage, Guideline-Aligned Memory Policy Optimization uses the induced guideline to define structured process rewards and performs multi-turn RL to learn a guideline-following memory evolution policy. We evaluate on three personalization memory benchmarks, covering explicit and implicit preferences as well as different sizes and noise levels, and observe consistent improvements over strong baselines with favorable robustness, transferability, and efficiency[ https://github.com/Applied-Machine-Learning-Lab/ACL2026_MemCoE ].

## 19. Learning Diverse Responses with Prefix-Conditioned Supervised Fine-Tuning

- Authors: Zhiyuan Fan, Guanqiao Chen, Yanyi Huang, Mingkuan Zhao, Dadi Guo, Yi R. Fung
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.7430860809611266
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.9/
- PDF: https://aclanthology.org/2026.acl-long.9.pdf
- Local PDF: pdf/2026-08-30_19_Learning Diverse Responses with Prefix-Conditioned Supervised Fine-Tuning.pdf

Large language models (LLMs) have shown strong performance on hard reasoning and general instruction-following tasks. However, when sampling multiple outputs for the same prompt, they often produce highly homogeneous, repetitive responses, resulting in inefficient exploration. This limits the gains from test-time scaling and constrains the upper bound of RL training. We attribute this issue in part to supervised fine-tuning (SFT): when a single prompt is paired with multiple reference responses, the model is trained to generate diverse outputs under the same prior condition, which induces optimization interference and can lead to diversity collapse. To address this, we propose Prefix-Conditioned SFT (P-SFT), a simple yet effective method that constructs semantically consistent yet distributionally distinct prior contents to different responses, thereby projecting the instruction into distinct latent regions to establish diverse prior distributions and decouple the one-to-many mapping. Experiments on large reasoning language models show that our approach improves absolute performance by 5.3% and increases generation diversity by 198.3% on average, while substantially enhancing output diversity and test-time scaling. Notably, even without any additional training, our prefixing strategy can be applied at inference time alone and still yields significant gains in both diversity and reasoning performance for instruction-tuned LLMs and reasoning-enhanced models.

## 20. CausalityCheck: A Framework for Evaluating Causal Reasoning in Large Language Models

- Authors: Jiang Li, Zehua Duo, Guanglai Gao, Xiangdong Su
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.742996227260072
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.808/
- PDF: https://aclanthology.org/2026.findings-acl.808.pdf
- Local PDF: pdf/2026-08-30_20_CausalityCheck_ A Framework for Evaluating Causal Reasoning in Large Language Models.pdf

Causal reasoning is a crucial component of understanding complex phenomena and building intelligent systems. Recent advancements in large language models (LLMs) have demonstrated their strong capabilities in reasoning tasks; however, their true understanding of causal relationships remains limited, particularly in cases where causal chains are misidentified or reliance on empirical inference occurs. To mitigate the risk that models misclassify data as false positives due to these issues, we introduce CausalityCheck, an automated tool designed to efficiently generate causal reasoning checklists. This checklist enables the creation of multi-task causal reasoning datasets with task generalization and reasoning robustness from a single causal reasoning dataset. Using CausalityCheck, we developed CausalityCheck-CP to assess the causal reasoning abilities of 18 LLMs. This framework also measures the extent to which causal chains are misidentified or rely on empirical inferences. Our results indicate that the current large language models still face two critical issues when handling complex causal reasoning tasks: incorrect identification of causal chains and reliance on empirical inference. The code and data are available at https://github.com/dzh597/CausalityCheck .

## 21. Mechanistic Interpretability of Large-Scale Counting in LLMs through a System-2 Strategy

- Authors: Hosein Hasani, Mohammadali Banayeeanzade, Ali Nafisi, Sadegh Mohammadian, Fatemeh Askari, Mobin Bagherian, Amirmohammad Izadi, Mahdieh Soleymani Baghshah
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.7429024465906195
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.2031/
- PDF: https://aclanthology.org/2026.findings-acl.2031.pdf
- Local PDF: pdf/2026-08-30_21_Mechanistic Interpretability of Large-Scale Counting in LLMs through a System-2 Strategy.pdf

Large language models (LLMs), despite strong performance on complex mathematical problems, exhibit systematic limitations in counting tasks. This issue arises from the architectural limits of transformers, where counting is performed across layers, leading to degraded precision for larger counting problems due to depth constraints. To address this limitation, we propose a simple test-time strategy inspired by System-2 cognitive processes that decomposes large counting tasks into smaller, independent sub-problems that the model can reliably solve. We evaluate this approach using observational and causal mediation analyses to understand the underlying mechanism of this System-2-like strategy. Our mechanistic analysis identifies key components: latent counts are computed and stored in the final item representations of each part, transferred to intermediate steps via dedicated attention heads, and aggregated in the final stage to produce the total count. Experimental results demonstrate that this strategy enables LLMs to surpass architectural limitations and achieve higher accuracy on large-scale counting tasks. This work provides mechanistic insight into System-2 counting in LLMs and presents a generalizable approach for improving and understanding their reasoning behavior.

## 22. Efficient Training for Cross-lingual Speech Language Models

- Authors: Yan Zhou, Qingkai Fang, Yun Hong, Yang Feng
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.742863404987844
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.642/
- PDF: https://aclanthology.org/2026.findings-acl.642.pdf
- Local PDF: pdf/2026-08-30_22_Efficient Training for Cross-lingual Speech Language Models.pdf

Currently, large language models (LLMs) predominantly focus on the text modality. To enable more natural human-AI interaction, speech LLMs are emerging, but building effective end-to-end speech LLMs remains challenging due to limited data and the difficulty in expanding to more languages. In this paper, we introduce C ross-lingual S peech L anguage M odel ( CSLM ), an efficient training method for cross-lingual speech LLMs based on discrete speech tokens. We propose a novel alignment strategy that achieves cross-modal and cross-lingual alignment through continual pre-training. By conducting instruction fine-tuning following a speech-text interleaved chain-of-modality generation process, we enhance modal alignment at a finer granularity, thereby improving generation quality and reducing latency. CSLM aligns different modalities and languages simultaneously without the need for massive speech data, thus exhibiting good language scalability. Evaluations on cross-modal tasks, mono-lingual conversational tasks, and cross-lingual conversational tasks demonstrate CSLM’s strong cross-modal alignment capabilities and general task abilities.

## 23. Multilingual and Cross-Lingual Citation Needed Detection on Wikipedia for Lower-Resource Languages

- Authors: Gerrit Quaremba, Amy Rechkemmer, Elizabeth Black, Denny Vrandečić, Elena Simperl
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.7419573455532613
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1291/
- PDF: https://aclanthology.org/2026.acl-long.1291.pdf
- Local PDF: pdf/2026-08-30_23_Multilingual and Cross-Lingual Citation Needed Detection on Wikipedia for Lower-Resource Languages.pdf

In automated fact-checking (AFC), check-worthiness detection identifies claims requiring verification based on domain-specific criteria. On Wikipedia, this task instantiates as Citation Needed Detection (CND), which flags claims lacking supporting citations. However, existing research has largely overlooked lower-resource languages, and recent AFC pipelines rely on large language models (LLMs), which are inaccessible to low-resource organizations. We introduce MCN, a multilingual CND corpus spanning 18 languages across three resource levels, on which we conduct an extensive study of small decoder-based language models (SLMs). Our experiments show that SLMs fine-tuned with an encoder-style objective substantially outperform prompted LLMs across languages. We further present one of the first studies on cross-lingual CND, demonstrating that SLMs fine-tuned solely on English claims surpass LLMs, even with little to no target-language adaptation. Our findings have important implications for lower-resource Wikipedia communities and suggest that compact, task-specific models are preferable to LLMs for CND.

## 24. IPS: In-Prompt Process Supervision for Short Video Content Moderation

- Authors: Mingchao Liu, Yu Sun, Ruixiao Sun, Xin Dong, Xiang Shen, Hongwei Wang, Hongyu Xiong, Yang Song
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.7415283057801743
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-industry.89/
- PDF: https://aclanthology.org/2026.acl-industry.89.pdf
- Local PDF: pdf/2026-08-30_24_IPS_ In-Prompt Process Supervision for Short Video Content Moderation.pdf

Multimodal large language models (MLLMs) are effective at capturing the semantics of short video content; however, they often fail to attend to the policy-specific details required for reliable content moderation.To address this limitation, we introduce IPS, a novel framework that integrates In-prompt Process Supervision into MLLMs by introducing sequential reasoning over ancillary questions during fine-tuning. IPS consistently outperforms baseline MLLMs on public and proprietary benchmarks.Moreover, replacing human-annotated ancillary labels with MLLM-generated ones results in only marginal performance degradation, demonstrating robustness to noisy supervision and strong scalability with model-generated annotations.These findings establish IPS as a scalable and effective solution for complex multimodal classification in large-scale industrial settings.

## 25. Efficient and Effective Internal Memory Retrieval for LLM-Based Healthcare Prediction

- Authors: Mingchen Li, Jiatan Huang, Zonghai Yao, Hong yu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.741464949850889
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1788/
- PDF: https://aclanthology.org/2026.findings-acl.1788.pdf
- Local PDF: pdf/2026-08-30_25_Efficient and Effective Internal Memory Retrieval for LLM-Based Healthcare Prediction.pdf

Large language models (LLMs) hold significant promise for healthcare, yet their reliability in high-stakes clinical settings is often compromised by hallucinations and a lack of granular medical context. While Retrieval-Augmented Generation (RAG) can mitigate these issues, standard supervised pipelines require computationally intensive searches over massive external knowledge bases, leading to high latency that is impractical for time-sensitive care. To address this, we introduce Keys-to-Knowledge (K2K), a novel framework that replaces external retrieval with internal, key-based knowledge access. By encoding essential clinical information directly into the model’s parameter space, K2K enables rapid retrieval from internal key–value memory without inference-time overhead. We further enhance retrieval quality through activation-guided probe construction and cross-attention reranking. Experimental results demonstrate that K2K achieves state-of-the-art performance across four benchmark healthcare outcome prediction datasets.

## 26. GroupToM-Bench: Benchmarking Group Theory of Mind and Nonlinear Social Emergence in MLLMs

- Authors: Weidong Tang, Jierui Li, Yueling Hou, Zihan Mei, Can Zhang, Xinyan Wan, Zhiyuan Liang, Pengfei Zhou, Yang You, Wangbo Zhao
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.7409295857442926
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1859/
- PDF: https://aclanthology.org/2026.acl-long.1859.pdf
- Local PDF: pdf/2026-08-30_26_GroupToM-Bench_ Benchmarking Group Theory of Mind and Nonlinear Social Emergence in MLLMs.pdf

True general intelligence requires not only a model of the physical world but also a social world model: the capacity to infer how individual mental states interact and crystallize into group-level outcomes. Despite notable progress in individual-level Theory of Mind (ToM) reasoning, existing multimodal large language models systematically fail at this: collective behavior emerges non-linearly from social tensions, conformity dynamics, and structural constraints, and cannot be recovered by summing individual intentions. We present GroupToM-Bench , the first multimodal benchmark for group-level ToM, built around a causal chain spanning micro-level BDI states (belief, desire, intention), meso-level group tension and structural constraints, and macro-level outcome prediction and mechanistic attribution. To probe this full arc, we develop a seven-level cognitive audit framework. Experiments reveal that frontier models perform significantly below human levels, exposing fundamental blind spots in modeling social structures and nonlinear collective behavior.

## 27. ReContraster: Making Your Posters Stand Out with Regional Contrast

- Authors: Peixuan Zhang, Zijian Jia, Ziqi Cai, Shuchen Weng, Si Li, Boxin Shi
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.7408844353735127
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.98/
- PDF: https://aclanthology.org/2026.acl-long.98.pdf
- Local PDF: pdf/2026-08-30_27_ReContraster_ Making Your Posters Stand Out with Regional Contrast.pdf

Effective poster design requires rapidly capturing attention and clearly conveying messages. Inspired by the “contrast effects” principle, we propose ReContraster, the first training-free model to leverage regional contrast to make posters stand out. By emulating the cognitive behaviors of a poster designer, ReContraster introduces the compositional multi-agent system to identify elements, organize layout, and evaluate generated poster candidates. To further ensure harmonious transitions across region boundaries, ReContraster integrates the hybrid denoising strategy during the diffusion process. We additionally contribute a new benchmark dataset for comprehensive evaluation. Seven quantitative metrics and four user studies confirm its superiority over relevant state-of-the-art methods, producing visually striking and aesthetically appealing posters.

## 28. Faithful-First Reasoning, Planning, and Acting for Multimodal LLMs

- Authors: Junxian Li, Xinyue Xu, Sai Ma, Di Zhang, Sichao Li
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.7404377609463233
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.336/
- PDF: https://aclanthology.org/2026.findings-acl.336.pdf
- Local PDF: pdf/2026-08-30_28_Faithful-First Reasoning, Planning, and Acting for Multimodal LLMs.pdf

Multimodal Large Language Models (MLLMs) frequently suffer from unfaithfulness, generating reasoning chains that drift from visual evidence or contradict final predictions. We propose Faithful-First Reasoning, Planning, and Acting (RPA) framework in which FaithEvi provides step-wise and chain-level supervision by evaluating the faithfulness of intermediate reasoning, and FaithAct uses these signals to plan and execute faithfulness-aware actions during inference. Experiments across multiple multimodal reasoning benchmarks show that faithful-first RPA improves perceptual faithfulness by up to 24% over prompt-based and tool-augmented reasoning frameworks, without degrading task accuracy. Our analysis shows that treating faithfulness as a guiding principle perceptually faithful reasoning trajectories and mitigates hallucination behavior. This work thereby establishes a unified framework for both evaluating and enforcing faithfulness in multimodal reasoning. Code is at https://github.com/lijunxian111/Faithful-First-RPA .

## 29. From Natural Language to Certified Geometry Proofs: A Survey of LLM-Augmented Verification and Neuro-Symbolic Theorem Proving

- Authors: Ioannis Tzachristas, Georgios Tzachristas
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.7404075153397596
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.bigpicture-main.1/
- PDF: https://aclanthology.org/2026.bigpicture-main.1.pdf
- Local PDF: pdf/2026-08-30_29_From Natural Language to Certified Geometry Proofs_ A Survey of LLM-Augmented Verification and Neuro-Symbolic Theorem Pr.pdf

Large Language Models (LLMs) can produce convincing geometric arguments, yet their outputs are not reliable enough to be treated as proofs without independent verification. In parallel, symbolic geometry tools (e.g. automated theorem provers in dynamic geometry systems) offer strong rigor guarantees, but require formalized inputs and can struggle with problem formalization, auxiliary construction, and proof presentation. This survey synthesizes work at the intersection of these lines: hybrid LLM–symbolic systems for geometry that (i) translate natural language and diagrams into formal constraints, (ii) search for solution plans and proof steps using learned or heuristic methods, and (iii) verify the resulting steps using symbolic provers or proof assistants. We propose a taxonomy organized around (a) the role of the LLM in the pipeline (parser, strategist, prover, critic), (b) the target proof artifact (answer-only, informal proof, semi-formal step trace, or kernel-checked formal proof), and (c) the verification backend (numeric testing, algebraic provers, synthetic provers, and proof-assistant kernels). We review representative systems in NLP and AI (e.g. GeoS, Inter-GPS, FormalGeo, AlphaGeometry, AutoGPS, and recent heuristic-only deductive solvers), and connect them to broader neurosymbolic paradigms for faithful reasoning (e.g. SatLM, LINC, and autoformalization). Finally, we outline evaluation protocols emphasizing step-level soundness and robustness, and we discuss open problems in multimodal formalization, handling of non-degeneracy conditions, human-readable certified proofs, and reproducibility.

## 30. CLARO: Controlled Attribute-Driven Reasoning Optimization for Efficient Chain-of-Thought

- Authors: Oded Schlesinger, Young Kyung Kim, J. Matias Di Martino, Guillermo Sapiro
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.7403799805705087
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1335/
- PDF: https://aclanthology.org/2026.findings-acl.1335.pdf
- Local PDF: pdf/2026-08-30_30_CLARO_ Controlled Attribute-Driven Reasoning Optimization for Efficient Chain-of-Thought.pdf

Large language models exhibit strong reasoning capabilities but often require significant computational resources due to verbose, unstructured Chain-of-Thought outputs. Recent approaches guide reasoning length through token penalties or truncation, risking the omission of necessary steps. We posit that conciseness should be an emergent property of structured thought, rather than a result of artificially forced brevity. To this end, we first demonstrate that Attribute-Guided Prompting, a lightweight zero-shot strategy, improves reasoning performance while reducing inference cost. Building on this foundation, we introduce Controlled Attribute-Driven Reasoning Optimization (CLARO), a reinforcement learning framework designed to internalize these benefits. CLARO guides models to embed high-quality structural attributes, such as readability, math density, syntactic compression, and low redundancy, within a user-defined token budget. The proposed method outperforms state-of-the-art baselines across diverse benchmarks, yielding accuracy gains of up to 63.6%, demonstrating that guiding generated output language structure enhances reasoning. Overall, our findings establish that optimizing the thought process structure refines reasoning efficacy, with computational efficiency emerging as a derivative benefit of a clearer thought process. Code and models are available at https://github.com/odedsc/CLARO .
