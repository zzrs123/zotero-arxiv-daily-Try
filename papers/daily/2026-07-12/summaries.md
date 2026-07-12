# Paper Daily Reading - 2026-07-12

## 1. Why Multimodal In-Context Learning Lags Behind? Unveiling the Inner Mechanisms and Bottlenecks

- Authors: Yu Wang, Sharon Li
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.944866459597737
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.622/
- PDF: https://aclanthology.org/2026.acl-long.622.pdf
- Local PDF: pdf/2026-07-12_01_Why Multimodal In-Context Learning Lags Behind_ Unveiling the Inner Mechanisms and Bottlenecks.pdf

In-context learning (ICL) enables models to adapt to new tasks via inference-time demonstrations. Despite its success in large language models, the extension of ICL to multimodal settings remains poorly understood in terms of its internal mechanisms and how it differs from text-only ICL. In this work, we conduct a systematic analysis of ICL in multimodal large language models. Using identical task formulations across modalities, we show that multimodal ICL performs comparably to text-only ICL in zero-shot settings but degrades significantly under few-shot demonstrations. To understand this gap, we decompose multimodal ICL into task mapping construction and task mapping transfer, and analyze how models establish cross-modal task mappings, and transfer them to query samples across layers. Our analysis reveals that current models lack reasoning-level alignment between visual and textual representations, and fail to reliably transfer learned task mappings to queries. Guided by these findings, we further propose a simple inference-stage enhancement method that reinforces task mapping transfer. Our results provide new insights into the mechanisms and limitations of multimodal ICL and suggest directions for more effective multimodal adaptation.

## 2. Spatial-Agent: Agentic Geo-spatial Reasoning with Scientific Core Concepts

- Authors: Riyang Bao, Cheng Yang, Dazhou Yu, Zhexiang Tang, Gengchen Mai, Liang Zhao
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.941542064446765
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.679/
- PDF: https://aclanthology.org/2026.acl-long.679.pdf
- Local PDF: pdf/2026-07-12_02_Spatial-Agent_ Agentic Geo-spatial Reasoning with Scientific Core Concepts.pdf

Geospatial reasoning is essential for real-world applications such as urban analytics, transportation planning, and disaster response. However, existing LLM-based agents often fail at genuine geospatial computation, relying instead on web search or pattern matching while hallucinating spatial relationships. We present Spatial-Agent, an AI agent grounded in foundational theories of spatial information science. Our approach formalizes geo-analytical question answering as a concept transformation problem, where natural-language questions are parsed into executable workflows represented as GeoFlow Graphs—directed acyclic graphs with nodes corresponding to spatial concepts and edges representing transformations. Drawing on spatial information theory, Spatial-Agent extracts spatial concepts, assigns functional roles with principled ordering constraints, and composes transformation sequences through template-based generation. Extensive experiments on MapEval-API and MapQA benchmarks demonstrate that Spatial-Agent significantly outperforms existing baselines including ReAct and Reflexion, while producing interpretable and executable geospatial workflows.

## 3. One Task Vector is not Enough: A Large-Scale Study for In-Context Learning

- Authors: Pavel Tikhonov, Ivan Oseledets, Elena Tutubalina
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.9415314036868105
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-srw.127/
- PDF: https://aclanthology.org/2026.acl-srw.127.pdf
- Local PDF: pdf/2026-07-12_03_One Task Vector is not Enough_ A Large-Scale Study for In-Context Learning.pdf

In-context learning (ICL) enables Large Language Models (LLMs) to adapt to new tasks using few examples, with task vectors, defined as specific hidden state activations hypothesized to encode task information. Existing studies are limited by small-scale benchmarks, restricting comprehensive analysis. We introduce QᴜɪᴛᴇAFᴇᴡ, a novel dataset of 3,096 diverse few-shot tasks, each with 30 input-output pairs derived from the Alpaca dataset. Experiments with Llama-3-8B on QᴜɪᴛᴇAFᴇᴡ reveal: (1) task vector performance peaks at an intermediate layer (e.g., 15th), (2) effectiveness varies significantly by task type, and (3) complex tasks rely on multiple, subtask-specific vectors rather than a single vector, suggesting distributed task knowledge representation.

## 4. Towards Intrinsic Interpretability of Large Language Models: A Survey of Design Principles and Architectures

- Authors: Yutong Gao, Qinglin Meng, Yuan Zhou, Liangming Pan
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.940859553900429
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1605/
- PDF: https://aclanthology.org/2026.acl-long.1605.pdf
- Local PDF: pdf/2026-07-12_04_Towards Intrinsic Interpretability of Large Language Models_ A Survey of Design Principles and Architectures.pdf

While Large Language Models (LLMs) have achieved strong performance across many NLP tasks, their opaque internal mechanisms hinder trustworthiness and safe deployment. Existing surveys in explainable AI largely focus on post-hoc explanation methods that interpret trained models through external approximations. In contrast, intrinsic interpretability, which builds transparency directly into model architectures and computations, has recently emerged as a promising alternative. This paper presents a systematic review of the recent advances in intrinsic interpretability for LLMs, categorizing existing approaches into five design paradigms: functional transparency, concept alignment, representational decomposability, explicit modularization, and latent sparsity induction. We further discuss open challenges and outline future research directions in this emerging field. The paper list is available at: Survey-Intrinsic-Interpretability-of-LLMs

## 5. Label Words as Local Task Vectors in In-Context Learning

- Authors: Bowen Zheng, Ming Ma, Zhongqiao Lin, Tianming Yang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.9405629814682754
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.314/
- PDF: https://aclanthology.org/2026.findings-acl.314.pdf
- Local PDF: pdf/2026-07-12_05_Label Words as Local Task Vectors in In-Context Learning.pdf

Large Language Models (LLMs) have demonstrated remarkable abilities, one of the most important being in-context learning (ICL). With ICL, LLMs can derive the underlying rule from a few demonstrations and provide answers that comply with the rule. Previous work hypothesized that the network creates a task vector in specific positions during ICL. The task vector can be computed by averaging across the dataset. It conveys the overall task information and can thus be considered global. Patching the global task vector allows LLMs to achieve zero-shot performance with dummy inputs comparable to few-shot learning. However, we find that such a global task vector does not exist in all tasks, especially in tasks that rely on rules that can only be inferred from multiple demonstrations, such as categorization tasks. Instead, the information provided by each demonstration is first transmitted to its answer position and forms a local task vector associated with the demonstration. In some tasks but not in categorization tasks, all demonstrations’ local task vectors converge in later layers, forming the global task vector. We further show that local task vectors encode a high-level abstraction of rules extracted from the demonstrations. Our study provides novel insights into the mechanism underlying ICL in LLMs, demonstrating how ICL may be achieved through an information aggregation mechanism.

## 6. Modal Dependency Parsing as Structured Prediction over Source-Cue Scope

- Authors: Jayeol Chun, Nianwen Xue
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.9405324875407315
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1362/
- PDF: https://aclanthology.org/2026.acl-long.1362.pdf
- Local PDF: pdf/2026-07-12_06_Modal Dependency Parsing as Structured Prediction over Source-Cue Scope.pdf

Modal dependency parsing-the task of identifying a semantic graph that represents who is responsible for an event-centered claim and with what degree of certainty-relies on recognizing source-introducing cues and correctly linking them to their associated content. However, prior work has largely focused on identifying sources only, treating cue expressions and their modal coverage as auxiliary signals. In this work, we propose a structured prediction framework that leverages large language models (LLMs) to explicitly identify source-cue pairs as well as their respective scope, which together define the modal contexts governing downstream source attribution for events. By concentrating learning at the source-cue level and constraining event-level decisions to a small, scope-defined candidate set, our top-down approach enables more efficient inference in long, event-rich documents. Experiments show this approach surpasses prior state-of-the-art results by 3 and 4% for English and Chinese datasets, respectively.

## 7. TopoSHIELD: Reshaping the Flow of Malice via Spatio-Temporal Risk-Aware Topological Evolution in Multi-Agent Systems

- Authors: Ruiyang Huang, Chenxi Wang, Tinghe Zhang, Fengrui Liu, Jiayan Sun, Haocheng Wang, Yifan Wu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.9399797302434028
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.426/
- PDF: https://aclanthology.org/2026.findings-acl.426.pdf
- Local PDF: pdf/2026-07-12_07_TopoSHIELD_ Reshaping the Flow of Malice via Spatio-Temporal Risk-Aware Topological Evolution in Multi-Agent Systems.pdf

While LLM-based Multi-Agent Systems (MAS) demonstrate remarkable problem-solving capabilities, their interconnectivity acts as a conduit for the rapid spread of malicious injections. Addressing the limitations of static defenses, we present TopoSHIELD, a framework that reshapes the flow of malice via risk-aware topological evolution. Our approach utilizes a spatio-temporal graph neural network to monitor interaction dynamics, calculating node risk entropy (NRE) and edge attack conductivity (EAC) to pinpoint vulnerabilities. Guided by these metrics, TopoSHIELD executes precise structural interventions, pruning high-risk edges and isolating compromised communities to block attack diffusion. Empirically, TopoSHIELD reduces toxicity by 58% on GPT-4o while preserving high utility (>90% success rate), outperforming existing baselines in both suppression efficiency and scalability.

## 8. LLM-induced Rationales for More Compact Explainable Style Classification Models

- Authors: Ahmad Aljanaideh, Saeb Ganideh
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.937797481307861
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1426/
- PDF: https://aclanthology.org/2026.findings-acl.1426.pdf
- Local PDF: pdf/2026-07-12_08_LLM-induced Rationales for More Compact Explainable Style Classification Models.pdf

The complexity of recent natural language classification models led to interest in developing methods for improving the performance of explainable models (e.g. Logistic Regression). Existing methods focus on clustering word embeddings to discover fine-grained contextual features that can be used to train a linear model. While those methods help reduce the gap in performance between black-box models and explainable models, they are based on discovering a large number of features, and this affects interpretability. In this work, we propose a model that leverages Large Language Models (LLMs) and clustering algorithms to discover a compact set of interpretable features. The proposed model first uses GPT-4o mini to extract rationales (i.e. phrases which explain an item’s label) from labeled text, and then clusters those rationales to obtain a compact, interpretable feature space. Across 3 Style Classification tasks, the resulting features achieve comparable performance to word-cluster baselines on most tasks, while reducing the number of features by 85–99%. These results highlight the potential of LLMs to improve the compactness of explainable AI models.

## 9. Harmonizing the Past, Present, and Future: A Null-Space Constrained Region-Specific Method for Continual Learning in LLMs

- Authors: Jinhui Chen, Shizhu He, Xingchang Yang, Huanxuan Liao, Yequan Wang, Xiangwen Liao, Wenhao Teng, Kang Liu, Jun Zhao
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.936741090745051
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1244/
- PDF: https://aclanthology.org/2026.acl-long.1244.pdf
- Local PDF: pdf/2026-07-12_09_Harmonizing the Past, Present, and Future_ A Null-Space Constrained Region-Specific Method for Continual Learning in LLM.pdf

Enabling Large Language Models (LLMs) to evolve sustainably requires simultaneously preserving previously acquired knowledge (Past), effectively acquiring new task-specific skills (Present), and reserving sufficient parameter capacity for subsequent adaptation (Future). However, existing continual learning (CL) paradigms often prioritize immediate performance through dense updates, leading to catastrophic forgetting and rapid exhaustion of model capacity. To harmonize these conflicting demands, we draw inspiration from the brain’s functional partitioning and propose the Null-Space Constrained Parameter Region Specificity Method (PaRSP). PaRSP establishes a dynamic "Task-Region Mapping" that distinguishes between specialized neurons and generalist neurons. By precisely localizing a sparse "functional core" for each task, PaRSP restricts updates to specific regions via null-space orthogonality, preserving the vast majority of the network as an immutable "long-term memory bank." This induced sparsity not only enhances plasticity via targeted adaptation and minimizes interference to ensure stability, but also strategically reserves substantial capacity, securing sustainability for future evolution. Extensive experiments validate PaRSP’s state-of-the-art performance, particularly on Standard CL and Long Sequence benchmarks, effectively harmonizing the stability-plasticity-sustainability trade-off. Code is available at https://github.com/JinhuiBot/PaRSP

## 10. SSSD: Simply-Scalable Speculative Decoding

- Authors: Michele Marzollo, Jiawei Zhuang, Niklas Roemer, Niklas Zwingenberger, Lorenz K Muller, Lukas Cavigelli
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.9355237482758834
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1530/
- PDF: https://aclanthology.org/2026.acl-long.1530.pdf
- Local PDF: pdf/2026-07-12_10_SSSD_ Simply-Scalable Speculative Decoding.pdf

Speculative Decoding has emerged as a popular technique for accelerating inference in Large Language Models. However, most existing approaches yield only modest improvements in production serving systems. Methods that achieve substantial speedups typically rely on an additional trained draft model or auxiliary model components, increasing deployment and maintenance complexity. This added complexity reduces flexibility, particularly when serving workloads shift to tasks, domains, or languages that are not well represented in the draft model’s training data.We introduce Simply-Scalable Speculative Decoding (SSSD), a training-free method that combines lightweight n-gram matching with hardware-aware speculation. Relative to standard autoregressive decoding, SSSD reduces latency by up to 2.9×. It achieves performance on par with leading training-based approaches across a broad range of benchmarks, while requiring substantially lower adoption effort—no data preparation, training or tuning are needed—and exhibiting superior robustness under language and domain shift, as well as in long-context settings.

## 11. Structure Guided Retrieval-Augmented Generation for Factual Queries

- Authors: Miao Xie, Xiao Zhang, Yi Li, Chunli Lv
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.935225923153983
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1873/
- PDF: https://aclanthology.org/2026.acl-long.1873.pdf
- Local PDF: pdf/2026-07-12_11_Structure Guided Retrieval-Augmented Generation for Factual Queries.pdf

Retrieval-Augmented Generation (RAG) has been proposed to mitigate hallucinations in large language models (LLMs), where generated outputs may be factually incorrect. However, existing RAG approaches predominantly rely on vector similarity for retrieval, which is prone to semantic noise and fails to ensure that generated responses fully satisfy the complex conditions specified by factual queries, often leading to incorrect answers. To address this challenge, we introduce a novel research problem, named Exact Retrieval Problem (ERP). To the best of our knowledge, this is the first problem formulation that explicitly incorporates structural information into RAG for factual questions to satisfy all query conditions. For this novel problem, we propose Structure Guided Retrieval-Augmented Generation (SG-RAG), which models the retrieval process as an embedding-based subgraph matching task, and uses the retrieved topological structures to guide the LLM to generate answers that meet all specified query conditions. To facilitate evaluation of ERP, we construct and publicly release Exact Retrieval Question Answering (ERQA), a large-scale dataset comprising 120,000 fact-oriented QA pairs, each involving complex conditions, spanning 20 diverse domains. The experimental results demonstrate that SG-RAG significantly outperforms strong baselines on ERQA, delivering absolute improvements from 20.68 to 50.88 points across all evaluation metrics, while maintaining reasonable computational overhead.

## 12. Capability Decomposition for Unified Information Extraction via Hierarchical Mixture-of-Experts

- Authors: Jing Zhou, Peng Wang, Wenjun Ke, Jiajun Liu, Yao He
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.9350566199651187
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.561/
- PDF: https://aclanthology.org/2026.acl-long.561.pdf
- Local PDF: pdf/2026-07-12_12_Capability Decomposition for Unified Information Extraction via Hierarchical Mixture-of-Experts.pdf

Unified Information Extraction (UIE) aims to handle heterogeneous IE tasks within a single framework, but existing methods often suffer from inconsistent schema representation, implicitly intermediate reasoning and full-parameter adaptation, which limit generalization, interpretability and parameter efficiency. To address these issues, we propose UC-UIE (Universal Capabilities-based Unified Information Extractor), a unified framework based on Large Language Model (LLM), which introduces a unified frame-and-slots schema for IE tasks and explicitly decomposes IE reasoning into three universal capabilities: judging, locating, and associating. Furthermore, UC-UIE adopts a Low-Rank Adaptation (LoRA) based hierarchical Mixture-of-Experts (MoE) adapter to fine-tune LLMs for IE tasks, which explicitly models these three capabilities in a task-driven way while ensuring parameter efficiency. With only 1.24% trainable parameters, UC-UIE outperforms full-parameter tuning methods, showing excellent parameter efficiency. Zero-shot evaluation reveals its strong generalization ability to unseen domains and schemas, benefiting from unified schema representation and explicit capability decomposition. Further experiments validate that the hierarchical MoE adapter learns capability specialization and composition, which enhances both UIE performance and interpretability.

## 13. Reasoning-Aware AIGC Detection via Alignment and Reinforcement

- Authors: Zhao Wang, Max Xiong, Jianxun Lian, Zhicheng Dou
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.934202308268393
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1043/
- PDF: https://aclanthology.org/2026.findings-acl.1043.pdf
- Local PDF: pdf/2026-07-12_13_Reasoning-Aware AIGC Detection via Alignment and Reinforcement.pdf

The rapid advancement and widespread adoption of Large Language Models (LLMs) have elevated the need for reliable AI-generated content (AIGC) detection, which remains challenging as models evolve. We introduce AIGC-text-bank, a comprehensive multi-domain dataset with diverse LLM sources and authorship scenarios, and propose REVEAL, a detection framework that generates interpretable reasoning chains before classification. Our approach uses a two-stage training strategy: supervised fine-tuning to establish reasoning capabilities, followed by reinforcement learning to improve accuracy, improve logical consistency, and reduce hallucinations. Extensive experiments show that REVEAL achieves state-of-the-art performance across multiple benchmarks, offering a robust and transparent solution for AIGC detection. The project is open-source at https://aka.ms/reveal

## 14. DiFRa: A Unified Framework for Harmonizing Semantic Diversity and Factual Consistency in Question-Answer Generation

- Authors: Zhenqin Li, ShengYong Ding, Shuangyin Li
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.933919615282764
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1493/
- PDF: https://aclanthology.org/2026.findings-acl.1493.pdf
- Local PDF: pdf/2026-07-12_14_DiFRa_ A Unified Framework for Harmonizing Semantic Diversity and Factual Consistency in Question-Answer Generation.pdf

Question-Answer Generation (QAG) is essential for alleviating the cold-start problem in domain-specific large language model (LLM) post-training, where high-quality data is severely scarce.Effective training samples include rich semantic diversity and rigorous factual consistency.Thus, it is necessary to consider the inherent tension between semantic breadth and factual fidelity.However, it is extremely challenging to trade off semantic diversity against factual consistency, in that generalization across the semantic space must be achieved effectively and reliably, and factual integrity must be ensured as well.To address this issue, we propose an effective framework, namely DiFRa, that integrates continuous concept diffusion with discrete knowledge graph constraints to balance semantic diversity and factual consistency.Specifically, the proposed DiFRa models discrete concepts as a continuous latent distribution to sample embeddings that capture rich semantic variations, and constructs a refined knowledge graph as explicit factual constraints.Then, a diversity and consistency aware mechanism is designed to dynamically integrate both embeddings and the knowledge graph for QA pairs generation.Furthermore, we introduce SeFa, which harmonizes semantic entropy and consistency scores to quantify the trade-off between diversity and correctness.Extensive experiments demonstrate that DiFRa consistently outperforms the baseline models, validating its efficacy in reconciling the tension to generate semantically diverse and factually consistent QA pairs. The source code is publicly available.

## 15. CogGen: A Cognitively Inspired Recursive Framework for Deep Research Report Generation

- Authors: Kuo Tian, Pengfei Sun, Zhen Wu, Junran Ding, Xinyu Dai
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.9333150086102924
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.296/
- PDF: https://aclanthology.org/2026.findings-acl.296.pdf
- Local PDF: pdf/2026-07-12_15_CogGen_ A Cognitively Inspired Recursive Framework for Deep Research Report Generation.pdf

The autonomous synthesis of deep research reports represents a critical frontier for Large Language Models (LLMs), demanding sophisticated information orchestration and non-linear narrative logic. Current approaches rely on rigid predefined linear workflows, which cause error accumulation, preclude global restructuring from subsequent insights, and ultimately limit in-depth multimodal fusion and report quality. We propose CogGen, a Cognitively inspired recursive framework for deep research report Generation. Leveraging a Hierarchical Recursive Architecture to simulate cognitive writing, CogGen enables flexible planning and global restructuring. To extend this recursivity to multimodal content, we introduce Abstract Visual Representation (AVR): a concise intent-driven language that iteratively refines visual-text layouts without pixel-level regeneration overhead. We further present CLEF, a Cognitive Load Evaluation Framework, and curate a new benchmark from Our World in Data (OWID). Extensive experiments show CogGen achieves state-of-the-art results among open-source systems, generating reports comparable to professional analysts’ outputs and surpassing Gemini Deep Research. Our code and dataset will be publicly available upon publication.

## 16. Seeing Beyond Words: MatVQA for Challenging Visual-Scientific Reasoning in Materials Science

- Authors: Sifan Wu, Huan Zhang, Yizhan Li, Farshid Effaty, Hongyuan Mei, Amirreza Ataei, Bang Liu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.9330817325591987
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1181/
- PDF: https://aclanthology.org/2026.findings-acl.1181.pdf
- Local PDF: pdf/2026-07-12_16_Seeing Beyond Words_ MatVQA for Challenging Visual-Scientific Reasoning in Materials Science.pdf

The emergence of Multimodal Large Language Models (MLLMs) that integrate vision and language modalities has unlocked new potentials for scientific reasoning, outperforming prior benchmarks in both natural language and coding domains. Current materials science evaluation datasets such as MaScQA and SciQA remain largely text-based and fail to capture the visual and research-level analytic complexity required in materials discovery and design. We introduce MatVQA, a scalable benchmark specifically designed to address this gap. Generated via an automated pipeline, MArxivAgent, from recent materials literature, MatVQA features 1672 questions across four critical structure-property-performance (SPP) reasoning tasks. Uniquely, MatVQA employs an iterative process to eliminate textual shortcuts, compelling MLLMs to perform fine-grained, low-level visual analysis of material imagery (e.g., microscopy, diffraction patterns) integrated with multi-step scientific reasoning. Benchmarking 19 open- and closed-source MLLMs on MatVQA reveals substantial gaps in current multimodal reasoning capabilities. The MatVQA benchmark is publicly available[<https://huggingface.co/datasets/trqcbf/matvqa_v2>] to facilitate further research on applying MLLMs to complex materials science problems.

## 17. LoRA on the Go: Instance-level Dynamic LoRA Selection and Merging

- Authors: Seungeon Lee, Soumi Das, Manish Gupta, Krishna P. Gummadi
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.9328983411198677
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1837/
- PDF: https://aclanthology.org/2026.acl-long.1837.pdf
- Local PDF: pdf/2026-07-12_17_LoRA on the Go_ Instance-level Dynamic LoRA Selection and Merging.pdf

Low-Rank Adaptation (LoRA) has emerged as a parameter-efficient approach for fine-tuning large language models. However, conventional LoRA adapters are typically trained for a single task, limiting their applicability in real-world settings, where inputs may span multiple, diverse task domains. At inference time, existing methods can combine multiple LoRAs to improve cross-task performance, but they require additional labeled data or task-specific training, which is expensive at scale.In this work, we introduce LoRA on the Go (LoGo), a training-free framework that dynamically selects and merges adapters at the instance level without any additional requirements. LoGo leverages signals extracted from a single forward pass through LoRA adapters, to identify the most relevant adapters and determine their contributions on-the-fly. Across 5 NLP benchmarks, 27 datasets, and 3 model families, LoGo outperforms training-based baselines on some tasks upto a margin of 3.6% while remaining competitive on other tasks and maintaining inference throughput, highlighting its effectiveness and practicality.

## 18. MACS: Modality-Aware Capacity Scaling for Efficient Multimodal MoE Inference

- Authors: Bo Li, Chuan Wu, Shaolin Zhu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.9328482562938167
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1012/
- PDF: https://aclanthology.org/2026.acl-long.1012.pdf
- Local PDF: pdf/2026-07-12_18_MACS_ Modality-Aware Capacity Scaling for Efficient Multimodal MoE Inference.pdf

Mixture-of-Experts Multimodal Large Language Models (MoE MLLMs) suffer from a significant efficiency bottleneck during Expert Parallelism (EP) inference due to the straggler effect. This issue is worsened in the multimodal context, as existing token-count-based load balancing methods fail to address two unique challenges: (1) Information Heterogeneity, where numerous redundant visual tokens are treated equally to semantically critical ones, and (2) Modality Dynamics, where varying visual to text ratios across tasks lead to resource misallocation. To address these challenges, we propose MACS (Modality-Aware Capacity Scaling), a training-free inference framework. Specifically, MACS introduces an Entropy-Weighted Load mechanism to quantify the semantic value of visual tokens, addressing information heterogeneity. Additionally, the Dynamic Modality-Adaptive Capacity mechanism allocates expert resources based on the real-time modal composition of the input. Extensive experiments demonstrate that MACS significantly outperforms existing methods on various multimodal benchmarks, providing a novel and robust solution for the efficient deployment of MoE MLLMs in EP inference.

## 19. Cost-aware LLM-based Online Dataset Annotation

- Authors: Elumar, Eray Can, Tekin, Cem, Yagan, Osman
- Source: neurips
- Venue type: conference
- Journal: NeurIPS 2025
- Publication status: formally_published
- Publication date: 2026-04-23
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.9322505023851098
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://proceedings.neurips.cc/paper_files/paper/2025/hash/054e9f9a286671ababa3213d6e59c1c2-Abstract-Conference.html
- PDF: https://proceedings.neurips.cc/paper_files/paper/2025/file/054e9f9a286671ababa3213d6e59c1c2-Paper-Conference.pdf
- Local PDF: pdf/2026-07-12_19_Cost-aware LLM-based Online Dataset Annotation.pdf

Recent advances in large language models (LLMs) have enabled automated dataset labeling with minimal human supervision. While majority voting across multiple LLMs can improve label reliability by mitigating individual model biases, it incurs high computational costs due to repeated querying. In this work, we propose a novel online framework, Cost-aware Majority Voting (CaMVo), for efficient and accurate LLM-based dataset annotation. CaMVo adaptively selects a subset of LLMs for each data instance based on contextual embeddings, balancing confidence and cost without requiring pre-training or ground-truth labels. Leveraging a LinUCB-based selection mechanism and a Bayesian estimator over confidence scores, CaMVo estimates a lower bound on labeling accuracy for each LLM and aggregates responses through weighted majority voting. Our empirical evaluation on the MMLU and IMDB Movie Review datasets demonstrates that CaMVo achieves comparable or superior accuracy to full majority voting while significantly reducing labeling costs. This establishes CaMVo as a practical and robust solution for cost-efficient annotation in dynamic labeling environments.

## 20. Cross-Modal Coreference Alignment: Enabling Reliable Information Transfer in Omni-LLMs

- Authors: Hongcheng Liu, Yuhao Wang, Zhe Chen, Pingjie Wang, Zhiyuan Zhu, Yixuan Hou, Yanfeng Wang, Yu Wang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.932057284570985
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1217/
- PDF: https://aclanthology.org/2026.acl-long.1217.pdf
- Local PDF: pdf/2026-07-12_20_Cross-Modal Coreference Alignment_ Enabling Reliable Information Transfer in Omni-LLMs.pdf

Omni Large Language Models (Omni-LLMs) have demonstrated impressive capabilities in holistic multi-modal perception, yet they consistently falter in complex scenarios requiring synergistic omni-modal reasoning. Beyond understanding global multimodal context, effective reasoning also hinges on fine-grained cross-modal alignment, especially identifying shared referents across modalities, yet this aspect has been largely overlooked. To bridge this gap, we formalize the challenge as a cross-modal coreference problem, where a model must localize a referent in a source modality and re-identify it in a target modality. Building on this paradigm, we introduce CrossOmni, a dataset comprising nine tasks equipped with human-designed reasoning rationales to evaluate and enhance this capability. Experiments on 13 Omni-LLMs reveal systematic weaknesses in cross-modal coreference, which we attribute to the absence of coreference-aware thinking patterns. To address this, we enhance cross-modal alignment via two strategies: a training-free In-Context Learning method and a training-based SFT+GRPO framework designed to induce such thinking patterns. Both approaches yield substantial performance gains and generalize effectively to collaborative reasoning tasks. Overall, our findings highlight cross-modal coreference as a crucial missing piece for advancing robust omni-modal reasoning.

## 21. SCVQ: Sparse-Compensated Vector Quantization for Large Language Models

- Authors: Zixuan Zhou, Yujun Diao, Zicheng Kong, Dehua Ma, Zhenbo Xu, Pei Pei Li, Zhaofeng He
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.932033876037395
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.403/
- PDF: https://aclanthology.org/2026.acl-long.403.pdf
- Local PDF: pdf/2026-07-12_21_SCVQ_ Sparse-Compensated Vector Quantization for Large Language Models.pdf

Large Language Models (LLMs) are primarily constrained by memory and bandwidth bottlenecks during deployment. Although Vector Quantization (VQ) has emerged as a promising solution, existing methods incur inference overhead due to massive codebook storage and intensive index lookups. Moreover, these methods typically suffer from non-negligible performance degradation under ultra-low bitwidth regimes. To bridge this gap, we propose Sparse-Compensated Vector Quantization (SCVQ), a novel framework designed for high-efficiency LLM vector quantization. SCVQ introduces a salience-aware weighted K-means clustering scheme with symmetry constraints to reduces codebook size and indexing costs. Central to our approach is a unified structured representation that consolidates outliers, salient weights, and quantization residuals into a single sparse compensation matrix. This design effectively preserves critical model information while leveraging VQ-specific properties to enable efficient custom kernels. Extensive experiments across multiple benchmarks demonstrate SCVQ’s superior performance. Specifically, SCVQ achieves a perplexity of 5.78 on WikiText-2 for LLaMA-2-7B at 2-bit quantization, while delivering a 1.4× end-to-end inference speedup over existing baselines.

## 22. ResearchBench: Benchmarking LLMs in Scientific Discovery via Inspiration-Based Task Decomposition

- Authors: Yujie Liu, Zonglin Yang, Tong Xie, Jinjie Ni, Ben Gao, Yuqiang Li, Shixiang Tang, Wanli Ouyang, Erik Cambria, Dongzhan Zhou
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.9316137862621083
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.644/
- PDF: https://aclanthology.org/2026.findings-acl.644.pdf
- Local PDF: pdf/2026-07-12_22_ResearchBench_ Benchmarking LLMs in Scientific Discovery via Inspiration-Based Task Decomposition.pdf

Large language models (LLMs) have shown potential in assisting scientific research, yet their ability to discover high-quality research hypotheses remains unexamined due to the lack of a dedicated benchmark. To address this gap, we introduce the first large-scale benchmark for evaluating LLMs on a sufficient set of scientific discovery sub-tasks—inspiration retrieval, hypothesis composition, and hypothesis ranking—where sufficient means that perfectly solving these sub-tasks perfectly solves the overall discovery task. We develop an automated LLM-based framework that extracts critical components—research questions, background surveys, inspirations, and hypotheses—from papers across 12 disciplines, with expert validation confirming its accuracy. To prevent data contamination, we focus exclusively on publications from 2024 onward, ensuring minimal overlap with LLM pretraining data; our automated framework further enables automatic extraction of even more recent papers as LLM pretraining cutoffs advance, supporting scalable and contamination-free automatic renewal of this discovery benchmark. Our evaluation shows that, across disciplines, LLMs excel at inspiration retrieval—an out-of-distribution task—suggesting their ability to surface novel knowledge associations.

## 23. Chain-of-Relations: Faithful and Efficient LLM Reasoning over Knowledge Graphs via Relation-Centric Exploration

- Authors: Chenhui Liu, Jianpeng Zhou, Jiahai Wang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.9311660155511077
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.2138/
- PDF: https://aclanthology.org/2026.findings-acl.2138.pdf
- Local PDF: pdf/2026-07-12_23_Chain-of-Relations_ Faithful and Efficient LLM Reasoning over Knowledge Graphs via Relation-Centric Exploration.pdf

Knowledge graph question answering (KGQA) serves as an essential benchmark for KG-enhanced large language models. Among various approaches, agent-based methods have emerged as an effective solution.Existing methods adopt entity-centric exploration that incrementally constructs reasoning paths by selecting and connecting intermediate entities. However, they face two critical limitations. (1) Entity incompleteness vulnerability arises when some intermediate entities lack semantic information beyond opaque IDs, preventing relevance evaluation and leading to discarding valid reasoning paths.(2) Premature entity pruning occurs because beam search retains only top-ranked entities at each step, eliminating candidates before their relevance can be verified.To address these challenges, this paper proposes Chain-of-Relations (CoR) with relation-centric exploration and global entity filtering, reducing dependence on entity completeness and ensuring complete candidate retrieval before constraint validation.Experiments on three benchmark datasets show that CoR consistently outperforms strong baselines in both F1 score and KG-grounded Rate.

## 24. AGSC: Adaptive Granularity and Semantic Clustering for Uncertainty Quantification in Long-text Generation

- Authors: Guanran Luo, Wentao Qiu, Wanru Zhao, Wenhan Lv, Zhongquan Jian, Meihong Wang, Qingqiang Wu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.930666076472602
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.434/
- PDF: https://aclanthology.org/2026.acl-long.434.pdf
- Local PDF: pdf/2026-07-12_24_AGSC_ Adaptive Granularity and Semantic Clustering for Uncertainty Quantification in Long-text Generation.pdf

Large Language Models (LLMs) have demonstrated impressive capabilities in long-form generation, yet their application is hindered by the hallucination problem. While Uncertainty Quantification (UQ) is essential for assessing reliability, the complex structure makes reliable aggregation across heterogeneous themes difficult, in addition, existing methods often overlook the nuance of neutral information and suffer from the high computational cost of fine-grained decomposition. To address these challenges, we propose **AGSC** (**A**daptive **G**ranularity and GMM-based **S**emantic **C**lustering), a UQ framework tailored for long-form generation. AGSC first uses NLI neutral probabilities as triggers to distinguish irrelevance from uncertainty, reducing unnecessary computation. It then applies Gaussian Mixture Model (GMM) soft clustering to model latent semantic themes and assign topic-aware weights for downstream aggregation. Experiments on BIO and LongFact show that AGSC achieves state-of-the-art correlation with factuality while reducing inference time by about 60% compared to full atomic decomposition.

## 25. MMTabReal: Real-World Benchmark for Multimodal Table Understanding

- Authors: Prasham Yatinkumar Titiya, Jainil Trivedi, Chitta Baral, Vivek Gupta
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.928808028823803
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.2047/
- PDF: https://aclanthology.org/2026.findings-acl.2047.pdf
- Local PDF: pdf/2026-07-12_25_MMTabReal_ Real-World Benchmark for Multimodal Table Understanding.pdf

Multimodal tables i.e. tabular layouts interleaved with charts, maps, icons, and color encodings are ubiquitous in real applications yet remain difficult for Multimodal Large Language Models (MLLMs). Despite advances in text and image understanding, systematic evaluation of table-centric multimodal reasoning is limited. We introduce MMTabReal, a MultiModal Table Benchmark, human-curated suite of 500 real-world tables paired with 4021 question–answer pairs. MMtabReal spans four question types, five reasoning categories, and eight structural archetypes. Evaluations of state-of-the-art models reveal substantial gaps, especially in visual grounding, spatial alignment, and multi-step inference, with 20–40% performance drops relative to existing benchmarks. These results highlight the need for architectures that more tightly fuse vision with tabular structure and support explicit numeric/logical operations. MMtabReal is released for evaluation only, providing a rigorous, reproducible testbed that reflects the linguistic, structural, and reasoning complexity of real-world multimodal tables. Code and data are available at: https://coral-lab-asu.github.io/mmtabreal/

## 26. Learning to Evolve: A Self-Improving Framework for Multi-Agent Systems via Textual Parameter Graph Optimization

- Authors: Shan He, Runze Wang, Zhuoyun Du, Huiyu Bai, Zouying Cao, Yu Cheng, Bo Zheng
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.9284557159401126
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1534/
- PDF: https://aclanthology.org/2026.findings-acl.1534.pdf
- Local PDF: pdf/2026-07-12_26_Learning to Evolve_ A Self-Improving Framework for Multi-Agent Systems via Textual Parameter Graph Optimization.pdf

Designing and optimizing multi-agent systems (MAS) is a complex, labor-intensive process of "Agent Engineering." Existing automatic optimization methods, primarily focused on flat prompt tuning, lack the structural awareness to debug the intricate web of interactions in MAS. More critically, these optimizers are static; they do not learn from experience to improve their own optimization strategies. To address these gaps, we introduce Textual Parameter Graph Optimization (TPGO), a framework that enables a multi-agent system to learn to evolve. TPGO first models the MAS as a Textual Parameter Graph (TPG), where agents, tools, and workflows are modular, optimizable nodes. To guide evolution, we derive "textual gradients," structured natural language feedback from execution traces, to pinpoint failures and suggest granular modifications. The core of our framework is Group Relative Agent Optimization (GRAO), a novel meta-learning strategy that learns from historical optimization experiences. By analyzing past successes and failures, GRAO becomes progressively better at proposing effective updates, allowing the system to learn how to optimize itself. Extensive experiments on complex benchmarks like GAIA and MCP-Universe show that TPGO significantly enhances the performance of state-of-the-art agent frameworks, achieving higher success rates through automated, self-improving optimization.

## 27. Bidirectional Semantic Enhancement for Schema Routing Across Large-Scale Databases

- Authors: Yuyang Wu, Xiaoliang Wang, Cam-Tu Nguyen
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.927717407825972
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.369/
- PDF: https://aclanthology.org/2026.findings-acl.369.pdf
- Local PDF: pdf/2026-07-12_27_Bidirectional Semantic Enhancement for Schema Routing Across Large-Scale Databases.pdf

With the prevalence of Large Language Models (LLMs), Text-to-SQL has made significant progress, yet applying it to massive, real-world databases remains a challenge. While previous works adopt a retrieve-then-generate framework, they struggle with the profound semantic gap between user queries and vague schema definitions. Existing methods relying on unidirectional query expansion often fail to bridge lexical mismatches, while graph-based approaches struggle to navigate schemas when explicit structural links (e.g., foreign keys) are missing. To address this, we propose Bi-SR, a retrieval framework that bridges this gap through a bidirectional semantic enhancement strategy. We simultaneously enrich vague table schemas offline and perform online generative query expansion—specifically predicting potential schema structures—to align user intent. Crucially, we introduce a dual-augmented contrastive training objective for the dense retriever, which trains the dense retriever to recognize the semantic correspondence between the LLM-expanded query intent and the detailed schema descriptions. Experiments on massive schema routing benchmarks constructed from BIRD and Spider demonstrate that Bi-SR achieves state-of-the-art performance and significantly empowers smaller models for cost-effective deployment.

## 28. Unlocking the Black Box of Latent Reasoning: An Interpretability-Guided Approach to Intervention

- Authors: Shuochen Chang, Tong Bai, Xiaofeng Zhang, Qianli Ma, Qingyang Liu, Zhaohe Liao, Yibo Miao, Li Niu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.927587169467283
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1568/
- PDF: https://aclanthology.org/2026.acl-long.1568.pdf
- Local PDF: pdf/2026-07-12_28_Unlocking the Black Box of Latent Reasoning_ An Interpretability-Guided Approach to Intervention.pdf

Latent reasoning enables Large Language Models (LLMs) to perform multi-step inference within continuous hidden states, offering efficiency gains over explicit Chain-of-Thought (CoT). However, the opacity of these continuous thought vectors hinders their reliability and controllability. This paper bridges the gap between mechanistic interpretability and actionable control. We first present a systematic analysis using structural, causal, and geometric probes, revealing that latent vectors encode compressed, faithful representations of reasoning steps, with early vectors acting as critical causal hubs. Building on this, we operationalize these interpretability insights into a suite of training-free, decode-time interventions that refine the latent reasoning process by imposing the identified geometric and semantic priors. Extensive experiments across multiple model scales and diverse task domains demonstrate that our approaches consistently improve reasoning accuracy. Our interpretability-guided interventions consistently unlock latent capabilities and improve reasoning accuracy without any parameter updates.

## 29. Chain-of-Thought Compression Should Not Be Blind: V-Skip for Efficient Multimodal Reasoning via Dual-Path Anchoring

- Authors: Dongxu Zhang, Yiding Sun, Cheng Tan, Wenbiao Yan, Ning Yang, Jihua Zhu, Haijun Zhang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.927531830800217
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.887/
- PDF: https://aclanthology.org/2026.acl-long.887.pdf
- Local PDF: pdf/2026-07-12_29_Chain-of-Thought Compression Should Not Be Blind_ V-Skip for Efficient Multimodal Reasoning via Dual-Path Anchoring.pdf

While Chain-of-Thought (CoT) reasoning significantly enhances the performance of Multimodal Large Language Models (MLLMs), its autoregressive nature incurs prohibitive latency constraints. Current efforts to mitigate this via token compression often fail by blindly applying text-centric metrics to multimodal contexts. We identify a critical failure mode termed Visual Amnesia, where linguistically redundant tokens are erroneously pruned, leading to hallucinations. To address this, we introduce V-Skip that reformulates token pruning as a Visual-Anchored Information Bottleneck (VA-IB) optimization problem. V-Skip employs a dual-path gating mechanism that weighs token importance through both linguistic surprisal and cross-modal attention flow, effectively rescuing visually salient anchors. Extensive experiments on Qwen2-VL and Llama-3.2 families demonstrate that V-Skip achieves a speedup with negligible accuracy loss. Specifically, it preserves fine-grained visual details, outperforming other baselines over 30% on the DocVQA.

## 30. PO-KGQA: Preference Optimization for Low-Resource Complex Knowledge Graph Question Answering

- Authors: Prerna Agarwal, Ayushman Kumar Singh, Srikanta Bedathur
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.9269433703743353
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.2083/
- PDF: https://aclanthology.org/2026.findings-acl.2083.pdf
- Local PDF: pdf/2026-07-12_30_PO-KGQA_ Preference Optimization for Low-Resource Complex Knowledge Graph Question Answering.pdf

Existing low-resource in-context learning-based knowledge graph question answering (KGQA) methods rely heavily on large language models (LLMs) to convert the natural language question into its corresponding logical form (LF), such as SPARQL, KoPL, etc. Recently, a few alignment techniques have been introduced that enable instruction-based fine-tuning of language models. They provide explicit negative signals and comparative objectives to learn how to avoid negative signals using preference optimization methods. Exploring such fine-tuning techniques with LLMs becomes very challenging due to the high computational resource requirements associated with them. Due to this, the focus has been shifted towards Small Language Models (SLMs), which offer advantages such as ease of (i) deployment for practical applications and (ii) instruction fine-tuning for specialized tasks. Motivated by this, in this work, we propose PO-KGQA: An SLM-based preference optimization framework for the complex KGQA task in a low-resource setting. Our extensive experiments demonstrate how PO-KGQA outperforms other fine-tuning alignment techniques on complex benchmarks such as KQA Pro by approximately 9% (avg).
