# Paper Daily Reading - 2026-07-03

## 1. Geoparsing: Diagram Parsing for Plane and Solid Geometry with a Unified Formal Language

- Authors: Peijie Wang, Ming-Liang Zhang, Jun Cao, Chao Deng, Dekang Ran, Pi Bu, Hongda Sun, Xuan Zhang, Yingyao Wang, Jun Song, Bo Zheng, Fei Yin, Cheng-Lin Liu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.063605128306095
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1494/
- PDF: https://aclanthology.org/2026.findings-acl.1494.pdf
- Local PDF: pdf/2026-07-03_01_Geoparsing_ Diagram Parsing for Plane and Solid Geometry with a Unified Formal Language.pdf

Multimodal Large Language Models (MLLMs) have achieved remarkable progress but continue to struggle with geometric reasoning, primarily due to the perception bottleneck regarding fine-grained visual elements. While formal languages have aided plane geometry understanding, solid geometry which requires spatial understanding remains largely unexplored. In this paper, we address this challenge by designing a unified formal language that integrates plane and solid geometry, comprehensively covering geometric structures and semantic relations. We construct GDP-29K, a large-scale dataset comprising 20k plane and 9k solid geometry samples collected from diverse real-world sources, each paired with its ground-truth formal description. We propose a training paradigm combining Supervised Fine-Tuning with Reinforcement Learning via Verifiable Rewards, which effectively enforces syntactic correctness and geometric consistency. Experiments show that our approach achieves state-of-the-art parsing performance. Furthermore, we demonstrate that our parsed formal descriptions serve as a critical cognitive scaffold, significantly boosting MLLMs’ capabilities for downstream geometry reasoning tasks.

## 2. RAG-KT: Cross-platform Explainable Knowledge Tracing with Multi-view Fusion Retrieval Generation

- Authors: Zhiyi Duan, Hongyu Yuan, Rui Liu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.060936793668161
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.257/
- PDF: https://aclanthology.org/2026.findings-acl.257.pdf
- Local PDF: pdf/2026-07-03_02_RAG-KT_ Cross-platform Explainable Knowledge Tracing with Multi-view Fusion Retrieval Generation.pdf

Knowledge Tracing (KT) infers a student’s knowledge state from past interactions to predict future performance. Conventional Deep Learning (DL)-based KT models are typically tied to platform-specific identifiers and latent representations, making them hard to transfer and interpret. Large Language Model (LLM)-based methods can be either ungrounded under prompting or overly domain-dependent under fine-tuning. In addition, most existing KT methods are developed and evaluated under a same-distribution assumption. In real deployments, educational data often arise from heterogeneous platforms with substantial distribution shift, which often degrades generalization. To this end, we propose RAG-KT, a retrieval-augmented paradigm that frames cross-platform KT as reliable context constrained inference with LLMs. It builds a unified multi-source structured context with cross-source alignment via Question Group abstractions and retrieves complementary rich and reliable context for each prediction, enabling grounded prediction and interpretable diagnosis. Experiments on three public KT benchmarks demonstrate consistent gains in accuracy and robustness, including strong performance under cross-platform conditions.

## 3. What Makes AI Research Replicable? Executable Knowledge Graphs as Scientific Knowledge Representations

- Authors: Yujie Luo, Zhuoyun Yu, Xuehai Wang, Yuqi Zhu, Ningyu Zhang, Lanning Wei, Lun Du, Da Zheng, Huajun Chen
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.0600971891583963
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-short.70/
- PDF: https://aclanthology.org/2026.acl-short.70.pdf
- Local PDF: pdf/2026-07-03_03_What Makes AI Research Replicable_ Executable Knowledge Graphs as Scientific Knowledge Representations.pdf

Replicating AI research is a crucial yet challenging task for large language model (LLM) agents. Existing approaches often struggle to generate executable code, primarily due to insufficient background knowledge and the limitations of retrieval-augmented generation (RAG) methods, which fail to capture latent technical details hidden in referenced papers. Furthermore, previous approaches tend to overlook valuable implementation-level code signals and lack structured knowledge representations that support multi-granular retrieval and reuse. To overcome these challenges, we propose Executable Knowledge Graphs (xKG), a pluggable, paper-centric knowledge base that automatically integrates code snippets and technical insights extracted from scientific literature. When integrated into three agent frameworks with two different LLMs, xKG shows substantial performance gains (10.9% with o3-mini) on PaperBench, demonstrating its effectiveness as a general and extensible solution for automated AI research replication.

## 4. VideoStir: Understanding Long Videos via Spatio-Temporally Structured and Intent-Aware RAG

- Authors: Honghao Fu, Miao Xu, Yiwei Wang, Dailing Zhang, Jun Liu, Yujun Cai
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.0577384765193028
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1656/
- PDF: https://aclanthology.org/2026.acl-long.1656.pdf
- Local PDF: pdf/2026-07-03_04_VideoStir_ Understanding Long Videos via Spatio-Temporally Structured and Intent-Aware RAG.pdf

Scaling multimodal large language models (MLLMs) to long videos is constrained by limited context windows. While retrieval-augmented generation (RAG) is a promising remedy by organizing query-relevant visual evidence into a compact context, most existing methods (i) flatten videos into independent segments, breaking their inherent spatio-temporal structure, and (ii) depend on explicit semantic matching, which can miss cues that are implicitly relevant to the query’s intent. To overcome these limitations, we propose VideoStir, a structured and intent-aware long-video RAG framework. It firstly structures a video as a spatio-temporal graph at clip level, and then performs multi-hop retrieval to aggregate evidence across distant yet contextually related events. Furthermore, it introduces an MLLM-backed intent-relevance scorer that retrieves frames based on their alignment with the query’s reasoning intent. To support this capability, we curate IR-600K, a large-scale dataset tailored for learning frame–query intent alignment. Experiments show that VideoStir is competitive with state-of-the-art baselines without relying on auxiliary information, highlighting the promise of shifting long-video RAG from flattened semantic matching to structured, intent-aware reasoning. Codes and checkpoints are available at https://github.com/RomGai/VideoStir.

## 5. SDAR-VL: Stable and Efficient Block-wise Diffusion for Vision-Language Understanding

- Authors: Shuang Cheng, Yuhua Jiang, Zineng Zhou, Dawei Liu, Tao Wang, Linfeng Zhang, Biqing Qi, Bowen Zhou
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.056346565563416
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1333/
- PDF: https://aclanthology.org/2026.acl-long.1333.pdf
- Local PDF: pdf/2026-07-03_05_SDAR-VL_ Stable and Efficient Block-wise Diffusion for Vision-Language Understanding.pdf

Block-wise discrete diffusion offers an attractive balance between parallel generation and causal dependency modeling, making it a promising backbone for vision-language modeling. However, its practical adoption has been limited by high training cost, slow convergence, and instability, which have so far kept it behind strong autoregressive (AR) baselines. We present SDAR-VL , the first systematic application of block-wise discrete diffusion to large-scale vision-language understanding (VLU), together with an integrated framework for efficient and stable training . This framework unifies three components: 1) Asynchronous Block-wise Noise Scheduling to diversify supervision within each batch; 2) Effective Mask Ratio Scaling for unbiased loss normalization under stochastic masking; and 3) a Progressive Beta Noise Curriculum that increases effective mask coverage while preserving corruption diversity. Experiments on 21 single-image, multi-image, and video benchmarks show that SDAR-VL consistently improves training efficiency , convergence stability , and task performance over conventional block diffusion. On this evaluation suite, SDAR-VL sets a new state of the art among diffusion-based vision-language models and, under matched settings, matches or surpasses strong AR baselines such as LLaVA-OneVision as well as the global diffusion baseline LLaDA-V, establishing block-wise diffusion as a practical backbone for VLU.

## 6. From Insight to Action: A Novel Framework for Interpretability-Guided Data Selection in Large Language Models

- Authors: Ling Shi, Xinwei Wu, Xiaohu Zhao, Hao Wang, Heng Liu, Yangyang Liu, Linlong Xu, Longyue Wang, Deyi Xiong, Weihua Luo
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.0556458264441093
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.283/
- PDF: https://aclanthology.org/2026.acl-long.283.pdf
- Local PDF: pdf/2026-07-03_06_From Insight to Action_ A Novel Framework for Interpretability-Guided Data Selection in Large Language Models.pdf

While mechanistic interpretability tools like Sparse Autoencoders (SAEs) can uncover meaningful features within Large Language Models (LLMs), a critical gap remains in transforming these insights into practical actions for model optimization. We bridge this gap with the hypothesis that data selection guided by a model’s internal task features is a effective training strategy. Inspired by this, we propose Interpretability-Guided Data Selection (IGDS), a framework that first identifies these causal task features through frequency recall and interventional filtering, then selects “Feature-Resonant Data” that maximally activates task features for fine-tuning. We validate IGDS on mathematical reasoning, summarization, and translation tasks within Gemma-2, LLaMA-3.1, and Qwen3 models. Our experiments demonstrate exceptional data efficiency: on the Math task, IGDS surpasses full-dataset fine-tuning by a remarkable **17.4%** on Gemma-2-2B while using only 50% of the data, and outperforms established baselines focused on data quality and diversity. Analysis confirms a strong positive correlation between feature amplification and task performance improvement. IGDS thus provides a direct and effective framework to enhance LLMs by leveraging their internal mechanisms, validating our core hypothesis.

## 7. Dual Activation-Weight Sparsity: A Training-Free Framework for Efficient Large Language Model Compression

- Authors: Luoyang Sun, Guangyan Li, Cheng Deng, Haifeng Zhang, Jian Zhao, Yongqiang Tang, Wensheng Zhang, Jun Wang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.0553859907313266
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.378/
- PDF: https://aclanthology.org/2026.acl-long.378.pdf
- Local PDF: pdf/2026-07-03_07_Dual Activation-Weight Sparsity_ A Training-Free Framework for Efficient Large Language Model Compression.pdf

Large language models (LLMs) excel at natural language tasks but face deployment challenges due to computational demands. We introduce Dual Activation-Weight Sparsity (DAWS) , a training-free framework that jointly exploits activation and weight sparsity through magnitude-based routing. Systematic analysis of pretrained transformers reveals two key observations: (1) the activation energy is concentrated in a few neurons, and (2) activation and weight sparsity patterns are complementary between attention and FFN layers. DAWS employs a three-tier routing strategy: high-magnitude activations pass through full-precision weights to preserve critical pathways, medium-magnitude activations use magnitude-pruned sparse weights for efficiency, and low-magnitude activations are directly discarded. Unlike prior work that uses activation-aware pruning methods like WANDA, our approach uses direct magnitude-based pruning, which we show is more robust to sample-level variations. Experiments on Llama and Mistral models demonstrate that DAWS maintains >98% of dense model performance at 50% sparsity, outperforming WANDA, TEAL, and R-Sparse.

## 8. Consolidation or Adaptation? PRISM: Disentangling SFT and RL Data via Gradient Concentration

- Authors: Yang Zhao, Yangou Ouyang, Xiao Ding, Hepeng Wang, Bibo Cai, Kai Xiong, Jinglong Gao, Zhouhao Sun, Li Du, Bing Qin, Ting Liu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.055342252046266
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1097/
- PDF: https://aclanthology.org/2026.acl-long.1097.pdf
- Local PDF: pdf/2026-07-03_08_Consolidation or Adaptation_ PRISM_ Disentangling SFT and RL Data via Gradient Concentration.pdf

While Hybrid Supervised Fine-Tuning (SFT) followed by Reinforcement Learning (RL) has become the standard paradigm for training LLM agents, effective mechanisms for data allocation between these stages remain largely underexplored. Current data arbitration strategies often rely on surface-level heuristics that fail to diagnose intrinsic learning needs. Since SFT targets pattern consolidation through imitation while RL drives structural adaptation via exploration, misaligning data with these functional roles causes severe optimization interference. We propose PRISM, a dynamics-aware framework grounded in Schema Theory that arbitrates data based on its degree of cognitive conflict with the model’s existing knowledge. By analyzing the spatial geometric structure of gradients, PRISM identifies data triggering high spatial concentration as high-conflict signals that require RL for structural restructuring. In contrast, data yielding diffuse updates is routed to SFT for efficient consolidation. Extensive experiments on WebShop and ALFWorld demonstrate that PRISM achieves a Pareto improvement, outperforming state-of-the-art hybrid methods while reducing computational costs by up to 3.22 × . Our findings suggest that disentangling data based on internal optimization regimes is crucial for scalable and robust agent alignment.

## 9. From Pixels to Policies: Reinforcing Spatial Reasoning in Language Models for Content-Aware Layout Design

- Authors: Sha Li, Stefano Petrangeli, Yu Shen, Xiang Chen
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.05521489061457
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-industry.104/
- PDF: https://aclanthology.org/2026.acl-industry.104.pdf
- Local PDF: pdf/2026-07-03_09_From Pixels to Policies_ Reinforcing Spatial Reasoning in Language Models for Content-Aware Layout Design.pdf

We introduce LaySPA, a reinforcement learning framework that equips large language models (LLMs) with explicit and interpretable spatial reasoning for content-aware graphic layout design. LaySPA addresses two key challenges: LLMs’ limited spatial reasoning and the lack of transparency in design decision making. Instead of operating at the pixel level, we reformulate layout design as a policy learning problem over a structured textual spatial environment that explicitly encodes canvas geometry, element attributes, and inter-element relationships. LaySPA produces dual-level outputs comprising interpretable reasoning traces and structured layout specifications, enabling transparent and controllable design decision making. Layout design policy is optimized via a multi-objective spatial critique that decomposes layout quality into geometric validity, relational coherence, and aesthetic consistency, and is trained using relative group optimization to stabilize learning in open-ended design spaces. Experiments demonstrate that LaySPA improves structural validity and visual quality, outperforming larger proprietary LLMs and achieving performance comparable to specialized state-of-the-art layout generators while requiring fewer annotated samples.

## 10. Choose Your Lens: Multi-Perspective Value Alignment of Chain-of-Thought Reasoning

- Authors: Gejian Zhao, Hanzhou Wu, Xinpeng Zhang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.0549689597774297
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.2075/
- PDF: https://aclanthology.org/2026.findings-acl.2075.pdf
- Local PDF: pdf/2026-07-03_10_Choose Your Lens_ Multi-Perspective Value Alignment of Chain-of-Thought Reasoning.pdf

Large language models (LLMs) are increasingly expected to support pluralistic alignment, representing diverse human perspectives. However, current methods often induce motivated reasoning: LLMs tend to hallucinate “convenient” facts to forcefully justify a requested stance. To address this, we propose Value-Graph-Consistent Chain-of-Thought (VGC-CoT), a neuro-symbolic framework that enables steerable pluralism without distorting objective reality. We enforce a strict distinction: facts should be shared, while value trade-offs may diverge. Our approach models reasoning as a directed traversal over a multi-perspective graph comprising a fixed factual layer and perspective-specific value layers. By projecting generated CoT paths onto this structure, we align the model with target values while constraining it to a shared factual backbone. Experiments show that our method reduces factual hallucinations by 3× and improves cross-perspective consistency by 25% compared to standard steerable baselines, paving the way for trustworthy pluralistic AI.

## 11. AED-RAG: Continuous Multi-Granular Context Fusion for Retrieval-Augmented Generation via Adaptive Ensemble Decoding

- Authors: Junzhe Zhou, Fulin Lin, Tairan Cheng, Shaowen Chen, Hongwei Wang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.0548351474621995
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1148/
- PDF: https://aclanthology.org/2026.findings-acl.1148.pdf
- Local PDF: pdf/2026-07-03_11_AED-RAG_ Continuous Multi-Granular Context Fusion for Retrieval-Augmented Generation via Adaptive Ensemble Decoding.pdf

Retrieval-Augmented Generation (RAG) enhances Large Language Models (LLMs) yet suffers from a mismatch between coarse retrieval granularity and fine-grained generation needs. Specifically, coarse-grained passages inherently conflate valid context with intra-passage noise that semantic retrieval often fails to filter. Existing alignment strategies, typically relying on discrete reranking, struggle to address this granularity mismatch or effectively balance external evidence with internal knowledge. To bridge this gap, we propose **AED-RAG**, a framework that synergizes discrete retrieval with continuous **A**daptive **E**nsemble **D**ecoding. Specifically, we fine-tune a utility predictor using contrastive perplexity to discern the information density differences between unstructured narrative passages and structured knowledge triplets. During inference, this predictor projects passages, triplets, and the model’s parametric memory into a unified probability space, enabling a soft, token-level fusion that dynamically optimizes information gain. Extensive experiments on four open-domain QA benchmarks demonstrate that AED-RAG significantly outperforms competitive baselines, underscoring the effectiveness of integrating multi-granular contexts.

## 12. The Paradox of Outcome Optimization: A Causal Information-Theoretic Bound on Reasoning Shortcuts in LLMs

- Authors: Zihan Chen, Yiming Zhang, Wenxiang Geng, Zenghui Ding, Yining Sun
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.053321928393115
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.925/
- PDF: https://aclanthology.org/2026.acl-long.925.pdf
- Local PDF: pdf/2026-07-03_12_The Paradox of Outcome Optimization_ A Causal Information-Theoretic Bound on Reasoning Shortcuts in LLMs.pdf

Large Language Models (LLMs) aligned via outcome-based Reinforcement Learning (RL) frequently exhibit a critical failure mode: they achieve high performance on in-distribution benchmarks while demonstrating brittle reasoning capabilities on out-of-distribution (OOD) tasks. We term this phenomenon Reward-Induced Manifold Collapse. We establish a theoretical framework bridging Structural Causal Models (SCM) and the Information Bottleneck (IB) principle to explain this paradox. We define reasoning as a high-complexity causal process and shortcut learning as the exploitation of low-complexity spurious correlations. Under the implicit inductive bias of Stochastic Gradient Descent (SGD), models optimized for outcome rewards are biased toward shortcut solutions whenever the training distribution allows for a “Markovian Screening” of the true causal mechanism. We derive a new generalization bound based on Semantic Coverage Measure ( 𝜂 ) rather than sample size, showing why data scaling on homogeneous distributions may fail to correct reasoning flaws. We also show that Process Reward Models (PRMs) function as Topological Filters, enforcing step-wise mutual information constraints that render the low-complexity shortcut manifold inadmissible. These results provide a mathematical grounding for the role of process supervision beyond simple credit assignment.

## 13. Why LLMs Hallucinate on Structured Knowledge: A Mechanistic Analysis of Reasoning over Linearized Representations

- Authors: Shanghao Li, Jinda Han, Yibo Wang, Yuanjie Zhu, Zihe Song, Langzhou He, Kenan Kamel A Alghythee, Philip S. Yu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.0527958561962643
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.914/
- PDF: https://aclanthology.org/2026.acl-long.914.pdf
- Local PDF: pdf/2026-07-03_13_Why LLMs Hallucinate on Structured Knowledge_ A Mechanistic Analysis of Reasoning over Linearized Representations.pdf

In many reasoning tasks, large language models (LLMs) rely on structured external knowledge, such as graphs and tables, which is typically linearized into sequential token representations. However, even when sufficient knowledge is available, LLMs can still produce hallucinated outputs, and the underlying mechanisms behind such failures remain poorly understood. We investigate these mechanisms and find that hallucinations arise from systematic internal dynamics rather than random noise. First, attention disproportionately concentrates toward shortcut-like structural cues rather than distributing across the full context. Second, feed-forward representations fail to ground the provided knowledge, causing the model to revert to parametric memory. Moreover, our results indicate that hallucination is consistently associated with failures in semantic grounding within feed-forward layers, while attention allocation exhibits greater task-dependent variability. Finally, we show that these mechanistic patterns generalize beyond single-hop graphs to multi-hop and tabular settings, enabling effective hallucination detection across structured knowledge formats.

## 14. Can LLMs Learn to Map the World from Local Descriptions?

- Authors: Sirui Xia, Aili Chen, Xintao Wang, Tinghui Zhu, Yikai Zhang, Jiangjie Chen, Yanghua Xiao
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.0526526211882254
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.128/
- PDF: https://aclanthology.org/2026.acl-long.128.pdf
- Local PDF: pdf/2026-07-03_14_Can LLMs Learn to Map the World from Local Descriptions.pdf

Recent advances in Large Language Models (LLMs) have demonstrated strong capabilities in tasks such as code generation and mathematical reasoning. However, their potential to internalize structured spatial knowledge remains underexplored. This study investigates whether LLMs, grounded in locally relative human observations, can construct coherent global spatial cognition by integrating fragmented relational descriptions. We focus on two core aspects of spatial cognition: spatial perception, where models infer consistent global layouts from local positional relationships, and spatial navigation, where models learn road connectivity from trajectory data and plan optimal paths between unconnected locations. Experiments conducted in a simulated urban environment demonstrate that LLMs not only generalize to unseen spatial relationships between points of interest (POIs) but also exhibit latent representations aligned with real-world spatial distributions. Furthermore, LLMs can learn road connectivity from trajectory descriptions, enabling accurate path planning and dynamic spatial awareness during navigation.

## 15. SPaCe: Unlocking Sample-Efficient Large Language Models Training With Self-Pace Curriculum Learning

- Authors: Van Dai Do, Manh Nguyen, Svetha Venkatesh, Hung Le
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.051925402148065
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.171/
- PDF: https://aclanthology.org/2026.findings-acl.171.pdf
- Local PDF: pdf/2026-07-03_15_SPaCe_ Unlocking Sample-Efficient Large Language Models Training With Self-Pace Curriculum Learning.pdf

Large language models (LLMs) have shown strong reasoning capabilities when fine-tuned with reinforcement learning (RL). However, such methods require extensive data and compute, making them impractical under many realistic training budgets. Many existing pipelines sample training examples uniformly across steps or epochs, ignoring differences in difficulty, redundancy, and learning value, which slows learning and wastes computation. We propose SPaCe, a self-paced learning framework that enables efficient learning based on the capability of the model being trained through optimizing which data to use and when. First, we apply cluster-based data reduction to partition training data by semantics and difficulty, extracting a compact yet diverse subset that reduces redundancy. Then, a multi-armed bandit treats data clusters as arms, allocating training samples based on the model’s solve rates and learning progress. Experiments across multiple reasoning benchmarks show that SPaCe achieves comparable or better accuracy than state-of-the-art baselines while using up to (100 times) fewer samples. Ablation studies and analyses further highlight the importance of both data clustering and adaptive selection. Our results demonstrate that carefully curated, performance-driven training curricula can unlock strong reasoning abilities in LLMs with minimal resources.

## 16. Beyond Query Memorization: Large Language Model Routing with Query Decomposition and Historical Matching

- Authors: Bo Lv, Jingbo Sun, Jianwei Lv, Chen Tang, Shaojie Zhang, Nayu Liu, Guoxin Yu, Zihao Li, Qichao Zhang, Dongbin Zhao, Ping Luo, Yue Yu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.05124940171671
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1852/
- PDF: https://aclanthology.org/2026.acl-long.1852.pdf
- Local PDF: pdf/2026-07-03_16_Beyond Query Memorization_ Large Language Model Routing with Query Decomposition and Historical Matching.pdf

Optimizing the trade-off among predictive performance and computational cost is a central focus in the deployment of Large Language Models (LLMs). Current routing methods primarily rely on direct mapping from queries to models based on surface-level features, making them susceptible to the memorization trap and leading to poor generalizability on out-of-distribution (OOD) data. In this paper, we propose DecoR, a novel routing framework that recasts the routing task as a matching process of sifting similar queries from historical logs, effectively mitigating the memorization trap. To enhance matching accuracy, we introduce a query capability deconstruction method that decouples linguistic surface forms from task-intrinsic requirements, directing matching toward capability dimensions to ground decisions in essential task attributes. Furthermore, we develop CodaSet, a comprehensive benchmark for assessing routing generalization, where experimental results demonstrate that DecoR maintains superior accuracy while substantially lowering inference costs across both in-distribution and OOD settings.

## 17. Revealing Procedural Reasoning Structures in Chain-of-Thought Training via Span-Level Gradient Organization

- Authors: Jia Liu, Jiaxin Luo, Weiwen Xu, Jonathan M. Garibaldi, Xiao-Kun Wu, Yixue Hao, Min Chen
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.050562451925124
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1754/
- PDF: https://aclanthology.org/2026.acl-long.1754.pdf
- Local PDF: pdf/2026-07-03_17_Revealing Procedural Reasoning Structures in Chain-of-Thought Training via Span-Level Gradient Organization.pdf

Chain-of-Thought (CoT) prompting enables large language models to produce multi-step reasoning, yet how such reasoning-related structure is expressed during training remains poorly understood. We present Gradient-based Structural Developer (GSD), an unsupervised framework with a principled gradient aggregation view that tracks span-level gradient during fine-tuning on reasoning benchmarks to understand how models develop structured, step-by-step reasoning capabilities. Our analysis shows that while gradients at the level of individual tokens are often noisy, aggregating gradients over contiguous reasoning-related spans reveals stable and recurring directional alignment across samples. We refer to these directionally aligned patterns as aligned sequential stresses, reflecting consistent gradient organization associated with similar reasoning procedures. Beyond capturing semantically similar reasoning instances, such gradient alignment also reveals structurally similar but semantically diverse cases that share common procedural organization. These findings position GSD as a diagnostic framework for analyzing how procedural reasoning structures emerge during training, with downstream selection results serving as auxiliary evidence correlating gradient alignment with adaptation efficiency.

## 18. Emergence of Minimal Circuits for Indirect Object Identification in Attention-Only Transformers

- Authors: Rabin Adhikari
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.049972544516939
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-srw.4/
- PDF: https://aclanthology.org/2026.acl-srw.4.pdf
- Local PDF: pdf/2026-07-03_18_Emergence of Minimal Circuits for Indirect Object Identification in Attention-Only Transformers.pdf

Mechanistic interpretability aims to reverse-engineer large language models (LLMs) into human-understandable computational circuits. However, the complexity of pretrained models often obscures the minimal mechanisms required for specific reasoning tasks. In this work, we train small, attention-only transformers from scratch on a symbolic version of the Indirect Object Identification (IOI) task, a benchmark for studying coreference-like reasoning in transformers. Surprisingly, a single-layer model with only two attention heads achieves perfect IOI accuracy, despite lacking MLPs and normalization layers. Through residual stream decomposition, spectral analysis, and embedding interventions, we find that the two heads specialize into additive and contrastive subcircuits that jointly implement IOI resolution. Furthermore, we show that a two-layer, one-head model achieves performance comparable to that of a multi-head model by composing information across layers primarily through query-key interactions. These results demonstrate that task-specific training induces highly interpretable, minimal circuits, offering a controlled testbed for probing the computational foundations of transformer reasoning.

## 19. LUNE: Efficient LLM Unlearning via LoRA Fine-Tuning with Negative Examples

- Authors: Yezi Liu, Hanning Chen, Wenjun Huang, Yang Ni, Mohsen Imani
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.0498895152276524
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.816/
- PDF: https://aclanthology.org/2026.findings-acl.816.pdf
- Local PDF: pdf/2026-07-03_19_LUNE_ Efficient LLM Unlearning via LoRA Fine-Tuning with Negative Examples.pdf

Large Language Models (LLMs) encode vast factual knowledge, yet their inability to selectively forget specific information hinders privacy protection, bias mitigation, and post-deployment correction. We present LoRA-based Unlearning with Negative Examples (LUNE), a lightweight framework that performs negative-only unlearning by updating only low-rank adapters while freezing the backbone, thereby localizing edits and avoiding disruptive global changes. Leveraging Low-Rank Adaptation (LoRA), LUNE targets intermediate representations to suppress (or replace) requested knowledge with an order-of-magnitude lower compute and memory than full fine-tuning or direct weight editing. Extensive experiments on multiple factual unlearning tasks show that LUNE: (I) achieves effectiveness comparable to full fine-tuning and memory-editing methods; and (II) reduces computational cost by about an order of magnitude.

## 20. Look and Think: Efficient Multimodal Reasoning via Modality-Decoupled Compression

- Authors: Xidi Cai, Junhao Zheng, Jingye Li, Boyuan Li, Shaowei Zhang, Qianli Ma
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.0496416039079497
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1241/
- PDF: https://aclanthology.org/2026.findings-acl.1241.pdf
- Local PDF: pdf/2026-07-03_20_Look and Think_ Efficient Multimodal Reasoning via Modality-Decoupled Compression.pdf

Multimodal large language models (MLLMs) have achieved strong performance on challenging visual question answering benchmarks, yet their inference efficiency is severely constrained by the rapidly growing context. This growth stems from two primary sources: the large number of visual tokens required to encode images, and the accumulation of intermediate reasoning traces during autoregressive generation. To address these challenges, we propose LaT (**L**ook **a**nd **T**hink), the first modality-decoupled compression method that enables efficient multimodal inference. LaT structures reasoning into alternating looking and thinking steps, thereby explicitly signaling when visual grounding is required. Building on this design, LaT (1) evicts visual tokens whenever visual grounding is unnecessary, and (2) applies co-learning-guided compression after each completed step, mitigating the two sources of context growth respectively. Experimental results demonstrate that LaT reduces the average context length by up to 57%, while maintaining performance comparable to the standard MLLM baseline. The code will be publicly released.

## 21. Topology-Enhanced Alignment for Large Language Models: Trajectory Topology Loss and Topological Preference Optimization

- Authors: Yurui Pan, Ke Xu, Bo Peng
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.048655776846786
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1242/
- PDF: https://aclanthology.org/2026.findings-acl.1242.pdf
- Local PDF: pdf/2026-07-03_21_Topology-Enhanced Alignment for Large Language Models_ Trajectory Topology Loss and Topological Preference Optimization.pdf

Alignment of large language models (LLMs) typically relies on supervised fine-tuning (SFT) and reinforcement learning from human feedback (RLHF), or more recently direct preference optimization (DPO). However, existing objectives largely ignore the global geometry and topology of the representation space: they operate on local token-level likelihoods or scalar preference scores, and do not explicitly constrain how hidden states move from a user prompt to an answer.We view generation as tracing a semantic trajectory in hidden space, and propose a topology-enhanced alignment framework that regularizes these trajectories using 0-dimensional persistent homology. First, at the SFT stage, we introduce a Trajectory Topology Loss (TTL). For each batch, we treat mean-pooled embeddings of prompts and gold answers as a mixed point cloud, run a Union-Find-based 0D persistent homology algorithm, and extract ”prompt–answer bridge” edges that connect previously disconnected components. TTL encourages the model’s actual update direction from prompt to answer to align with these topologically derived bridges, rather than with arbitrary or per-example directions.Second, at the RLHF/DPO stage, we propose Topological Preference Optimization (TPO). TPO constructs topic-specific semantic preference vectors from an offline pipeline and aligns the semantic improvement direction between rejected and chosen responses with these vectors in an intermediate hidden layer. We further introduce an exponential-moving-average-based dynamic weighting scheme to balance DPO and TPO losses, and also explore a fully topological variant that applies persistent homology on the chosen/rejected embedding cloud.We instantiate our methods on Qwen2.5-7B-Instruct and evaluate on UltraChat and Anthropic HH-RLHF. Across both SFT and DPO training, topology-enhanced objectives consistently outperform strong non-topological baselines (including per-example, nearest-neighbor, and random direction regularizers) on automatic preference metrics and LLM-judge evaluations, while maintaining or slightly improving toxicity. These results suggest that incorporating persistent homology and trajectory geometry is a promising and practical direction for more controllable LLM alignment.

## 22. From Words to Pixels: A Comprehensive Survey on Large Language Models in Visual Segmentation

- Authors: Yizhou Wang, Mang Tik Chiu, Lingzhi Zhang, Xuan Shen, Sohrab Amirghodsi, Yun Fu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.0455055085573877
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.2155/
- PDF: https://aclanthology.org/2026.acl-long.2155.pdf
- Local PDF: pdf/2026-07-03_22_From Words to Pixels_ A Comprehensive Survey on Large Language Models in Visual Segmentation.pdf

Visual segmentation, the task of segmenting an image into semantically meaningful regions, is a cornerstone in machine learning and has widespread applications in industry. Nevertheless, visual segmentation with instruction has been a challenging task for many years. This largely stems from the cross-modal discrepancy between language and image domains, resulting in difficulty in relating the instruction semantics and the pixel-level predictions. In recent years, the remarkable reasoning capabilities of Large Language Models (LLMs) and Large Multimodal Models (LMMs) have spurred a new wave of research aiming to bridge the disparity between natural language instructions and pixel-level understanding. This survey offers the first comprehensive overview of the rapidly evolving field of LLM-driven visual segmentation. We categorize existing approaches based on their core objectives and methodologies, including reasoning-based segmentation, open-vocabulary segmentation, grounding techniques connecting language to pixels, and extensions to video domains. We review recent seminal works in LLM-based visual segmentation, analyzing their architectural innovations, training strategies, and benchmark performance. Furthermore, we discuss the common datasets, evaluation metrics, and identify key challenges and promising future directions at the intersection of language and visual segmentation. We hope this survey serves as a valuable resource for researchers and practitioners seeking to understand the current landscape and future directions of leveraging LLMs for sophisticated visual segmentation tasks and applications. The resource summary is available at https://github.com/wyzjack/Awesome-LLM-Visual-Segmentation.

## 23. Truth as a Trajectory: What Internal Representations Reveal About Large Language Model Reasoning

- Authors: Hamed Damirchi, Imezadelajara, Ehsan Abbasnejad, Afshar Shamsi, Zhen Zhang, Javen Qinfeng Shi
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.0454051429216378
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.2073/
- PDF: https://aclanthology.org/2026.acl-long.2073.pdf
- Local PDF: pdf/2026-07-03_23_Truth as a Trajectory_ What Internal Representations Reveal About Large Language Model Reasoning.pdf

Existing explainability methods for Large Language Models (LLMs) typically treat hidden states as static points in activation space, assuming that correct and incorrect inferences can be separated using representations from an individual layer. However, these activations are saturated with polysemantic features, leading to linear probes learning surface-level lexical patterns rather than underlying reasoning structures. We introduce Truth as a Trajectory (TaT), which models the transformer inference as an unfolded trajectory of iterative refinements, shifting analysis from static activations to layer-wise geometric displacement. By analyzing displacement of representations across layers, TaT captures structural patterns in the evolution of inference that distinguish valid reasoning from spurious behavior. We evaluate TaT across dense and Mixture-of-Experts (MoE) architectures on benchmarks spanning commonsense reasoning, question answering, and toxicity detection. Without access to the activations themselves and using only changes in activations across layers, we show that TaT effectively mitigates reliance on static lexical confounds, outperforming conventional probing, and establishes trajectory analysis as a complementary perspective on LLM explainability.

## 24. CLAG: Adaptive Memory Organization via Agent-Driven Clustering for Small Language Model Agents

- Authors: Taeyun Roh, WonJune Jang, Junha Jung, Jaewoo Kang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.042938308603892
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.824/
- PDF: https://aclanthology.org/2026.findings-acl.824.pdf
- Local PDF: pdf/2026-07-03_24_CLAG_ Adaptive Memory Organization via Agent-Driven Clustering for Small Language Model Agents.pdf

Large language model agents heavily rely on external memory to support knowledge reuse and complex reasoning tasks. Yet most memory systems store experiences in a single global retrieval pool which can gradually dilute or corrupt stored knowledge. This problem is especially pronounced for small language models (SLMs), which are highly vulnerable to irrelevant context. We introduce CLAG, a CLustering-based AGentic memory framework where an agent actively organizes memory. CLAG employs an SLM-agent driven router to assign each new memory to a semantically coherent cluster. By performing continual evolution within the cluster, it effectively reduces cross-topic interference. During the retrieval phase, CLAG targets a small set of relevant clusters for retrieval, thereby excluding distractors and reducing the search space. Experiments on multiple QA datasets with three SLM backbones show that CLAG consistently improves answer quality and robustness over prior memory systems for agents, remaining lightweight and efficient.

## 25. Task-Aware LLM Routing with Multi-Level Task-Profile-Guided Data Synthesis for Cold-Start Scenarios

- Authors: Hui Liu, Bin Zou, Kecheng Chen, Jie Liu, Wenya Wang, Haoliang Li
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.041016612375702
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1007/
- PDF: https://aclanthology.org/2026.acl-long.1007.pdf
- Local PDF: pdf/2026-07-03_25_Task-Aware LLM Routing with Multi-Level Task-Profile-Guided Data Synthesis for Cold-Start Scenarios.pdf

Large language models (LLMs) exhibit substantial variability in performance and computational cost across tasks and queries, motivating routing systems that select models to meet user-specific cost–performance trade-offs. However, existing routers generalize poorly in cold-start scenarios where in-domain training data is unavailable. We address this limitation with a multi-level task-profile–guided data synthesis framework that constructs a hierarchical task taxonomy and produces diverse question–answer pairs to approximate the test-time query distribution. Building on this, we introduce TRouter, a task-type–aware router approach that models query-conditioned cost and performance via latent task-type variables, with prior regularization derived from the synthesized task taxonomy. This design enhances TRouter’s routing utility under both cold-start and in-domain settings. Across multiple benchmarks, we show that our synthesis framework alleviates cold-start issues and that TRouter delivers effective LLM routing.

## 26. Balancing Knowledge Breadth and Task Depth for Effective Domain Adaptation Fine-Tuning

- Authors: Mu Zhang, Yuxiang Chu, Guangya Yu, Yongqi Fan, Weiyan Zhang, Hang Hu, Tong Ruan, Jingping Liu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.0405146928009263
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.405/
- PDF: https://aclanthology.org/2026.findings-acl.405.pdf
- Local PDF: pdf/2026-07-03_26_Balancing Knowledge Breadth and Task Depth for Effective Domain Adaptation Fine-Tuning.pdf

Training large language models for domain adaptation poses a significant challenge in balancing the acquisition of domain knowledge with the retention of general abilities, often leading to catastrophic forgetting. While curriculum learning offers a promising direction, conventional methods typically rely on a single dimension of knowledge or task, which is insufficient to navigate the trade-off between knowledge breadth and task depth. In this paper, we propose a two-dimensional curriculum learning framework that coordinates model training along two orthogonal axes: the knowledge dimension and the task dimension. We first reconstruct the dataset by clustering instances according to their semantic similarity to general-domain data, and subsequently annotate them with a task hierarchy. Then, we design an integrated curriculum that develops from general to domain-specific knowledge clusters, and within each cluster, from lower- to higher-order cognitive tasks. Compared with the second-best method, our method improves accuracy on medical evaluations by 2.49% and on financial evaluations by 1.2%. Ablation and cross-domain experiments further demonstrate our method as a scalable and effective framework for structured domain adaptation in large language model fine-tuning. We have released the code in an anonymous repository at https://github.com/Melo-1017/Balancing-Knowledge-Breadth-and-Task-Depth.

## 27. ATLAS: Orchestrating Heterogeneous Models and Tools for Multi-Domain Complex Reasoning

- Authors: Jinyang Wu, Guocheng Zhai, Ruihan Jin, Jiahao Yuan, Yuhao Shen, Shuai Zhang, Zhengqi Wen, Jianhua Tao
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.0399567857684913
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.867/
- PDF: https://aclanthology.org/2026.findings-acl.867.pdf
- Local PDF: pdf/2026-07-03_27_ATLAS_ Orchestrating Heterogeneous Models and Tools for Multi-Domain Complex Reasoning.pdf

The integration of large language models (LLMs) with external tools has significantly expanded the capabilities of AI agents. However, as the diversity of both LLMs and tools increases, selecting the optimal model-tool combination becomes a high-dimensional optimization challenge. Existing approaches often rely on a single model or fixed tool-calling logic, failing to exploit the performance variations across heterogeneous model-tool pairs. In this paper, we present **ATLAS** (**A**daptive **T**ool-**L**LM **A**lignment and **S**ynergistic Invocation), a dual-path framework for dynamic tool usage in cross-domain complex reasoning. **ATLAS** operates via a dual-path approach: (1) **training-free cluster-based routing** that exploits empirical priors for domain-specific alignment, and (2) **RL-based multi-step routing** that explores autonomous trajectories for out-of-distribution generalization. Extensive experiments across 15 benchmarks demonstrate that our method outperforms closed-source models like GPT-4o as well as existing routing methods on both in-distribution (+10.1%) and out-of-distribution (+13.1%) tasks. Furthermore, our framework shows significant gains in visual reasoning by orchestrating specialized multi-modal tools.

## 28. Cross-Modal Masked Compositional Concept Modeling for Enhancing Visio-Linguistic Compositionality

- Authors: Wei Li, Zhen Huang, Xinmei Tian
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.0393781768733676
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1490/
- PDF: https://aclanthology.org/2026.acl-long.1490.pdf
- Local PDF: pdf/2026-07-03_28_Cross-Modal Masked Compositional Concept Modeling for Enhancing Visio-Linguistic Compositionality.pdf

Contrastively trained vision-language models like CLIP, have made remarkable progress in learning joint image-text representations, but still face challenges in compositional understanding. They often exhibit a “bag-of-words” behavior—struggling to capture the object relations, attribute-object bindings, and word order dependencies. This limitation arises not only from the reliance on global, single-vector representations for optimization, but also from the insufficient exploitation and modeling of the rich compositional information inherently present in paired image text data. In this work, we propose **MACCO** (**MA**sked **C**ompositional **C**oncept M**O**deling), a framework that masks compositional concepts in one modality and reconstructs them conditioned on the full contextual information from the other, enabling the model to capture and align cross-modal compositional structures more effectively. To facilitate this process, we introduce two auxiliary objectives that jointly align and regularize masked features both inter-modally and intra-modally. Extensive experiments on five compositional benchmarks, along with in-depth analyses, demonstrate that our approach not only significantly enhances compositionality in VLMs but also improves their ability to capture syntactic structure and linguistic information. Additionally, the improved compositionality also benefits text-to-image generation and multimodal large language model.

## 29. MAGMA: A Multi-Graph based Agentic Memory Architecture for AI Agents

- Authors: Dongming Jiang, Yi Li, Guanpeng Li, Bingzhe Li
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.0381303671726028
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1709/
- PDF: https://aclanthology.org/2026.acl-long.1709.pdf
- Local PDF: pdf/2026-07-03_29_MAGMA_ A Multi-Graph based Agentic Memory Architecture for AI Agents.pdf

Memory-Augmented Generation (MAG) extends large language models with external memory to support long-context reasoning, but existing approaches largely rely on semantic similarity over monolithic memory stores, entangling temporal, causal, and entity information. This design limits interpretability and alignment between query intent and retrieved evidence, leading to suboptimal reasoning accuracy. In this paper, we propose MAGMA, a multi-graph agentic memory architecture that represents each memory item across orthogonal semantic, temporal, causal, and entity graphs. MAGMA formulates retrieval as policy-guided traversal over these relational views, enabling query-adaptive selection and structured context construction. By decoupling memory representation from retrieval logic, MAGMA provides transparent reasoning paths and fine-grained control over retrieval. Experiments on LoCoMo and LongMemEval demonstrate that MAGMA consistently outperforms state-of-the-art agentic memory systems in long-horizon reasoning task.

## 30. LegalGraphRAG: Multi-Agent Graph Retrieval-Augmented Generation for Reliable Legal Reasoning

- Authors: Zerui Chen, Qinggang Zhang, Zhishang Xiang, Zhimin Wei, Linfeng Gao, Xiao Huang, Zhihong Zhang, Jinsong Su
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.0345151037070406
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1738/
- PDF: https://aclanthology.org/2026.acl-long.1738.pdf
- Local PDF: pdf/2026-07-03_30_LegalGraphRAG_ Multi-Agent Graph Retrieval-Augmented Generation for Reliable Legal Reasoning.pdf

Graph-based Retrieval-Augmented Generation (GraphRAG) advances flat document retrieval by structuring knowledge as relational graphs, enabling more coherent and effective reasoning. However, applying it to specific domains like legal reasoning faces critical challenges. (i) Legal corpora are heterogeneous, containing multi-granular knowledge from cases, articles and interpretations. A flat knowledge graph cannot adequately differentiate between factual details, applied rules, and abstract principles, limiting accurate retrieval. (ii) Reliable legal judgment demands transparent, evidence-based reasoning. Traditional RAG passes retrieved context directly to an LLM without verification, resulting in opaque, error-prone reasoning. To this end, we propose LegalGraphRAG, a framework designed for reliable legal reasoning. Our approach introduces two core components: a hierarchical legal graph that hierarchically organizes legal sources to enable retrieval at appropriate abstraction levels, and a multi-agent system for reliable legal reasoning, where a Researcher retrieves candidate evidence, an Auditor rigorously verifies its validity against source documents, and an Adjudicator synthesizes the set of verified evidence to render a final judgment. Extensive experiments show that LegalGraphRAG achieves the state-of-the-art performance, outperforming existing GraphRAG baselines in accurate and trustworthy legal analysis. Our code, datasets and implementation details are available at https://github.com/XMUDeepLIT/LegalGraphRAG.
