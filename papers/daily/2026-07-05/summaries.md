# Paper Daily Reading - 2026-07-05

## 1. Dynamic PMI-Guided Contrastive Decoding Reduces Hallucination in Large Language Models: A Unified Framework of Fine-Grained Input Transformations

- Authors: Dongsheng Chen, Yingqi Zhu, Xingyue Zhang, Wenqing Zhou, Lei Li
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.025344573473757
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1212/
- PDF: https://aclanthology.org/2026.findings-acl.1212.pdf
- Local PDF: pdf/2026-07-05_01_Dynamic PMI-Guided Contrastive Decoding Reduces Hallucination in Large Language Models_ A Unified Framework of Fine-Grai.pdf

Despite the remarkable generation capabilities demonstrated by large language models (LLMs), the issue of hallucination remains a critical challenge. This is largely attributed to the models’ tendency to fit spurious dependencies in pre-training data rather than underlying causal logic. To address this, from an information-theoretic perspective, this paper proposes a unified contrastive decoding framework based on dynamic pointwise mutual information (Dynamic PMI). Under this framework, we design three fine-grained input transformation strategies targeting context, syntax, and semantics to construct dynamic background distributions. These strategies systematically disentangle and suppress spurious dependencies induced by context priors, lexical co-occurrences, and syntactic structures, thereby guiding the model to prioritize underlying causal logic. Experiments on extensive discriminative and generative benchmarks demonstrate that our method significantly improves the model’s factuality and reasoning robustness. Notably, despite employing a single-model architecture, our framework surpasses state-of-the-art dual-model strategies while maintaining high computational efficiency. Furthermore, the framework exhibits strong cross-model generalizability and effectively alleviates the over-refusal tendency in open-ended generation.

## 2. Multi-Drafter Speculative Decoding with Alignment Feedback

- Authors: Taehyeon Kim, Hojung Jung, Se-Young Yun
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.024896358640845
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1629/
- PDF: https://aclanthology.org/2026.findings-acl.1629.pdf
- Local PDF: pdf/2026-07-05_02_Multi-Drafter Speculative Decoding with Alignment Feedback.pdf

Speculative decoding (SD) accelerates large language model (LLM) inference by using a smaller model to draft future tokens, which are then verified by the target LLM. This preserves generation quality by accepting only aligned tokens. However, individual drafters, often trained for specific tasks or domains, exhibit limited effectiveness across diverse applications. To address this, we introduce MetaSD, a unified framework that integrates multiple drafters into the SD process. MetaSD dynamically allocates computational resources to heterogeneous drafters by leveraging alignment feedback and framing drafter selection as a multi-armed bandit problem. Extensive experiments show MetaSD consistently outperforms single-drafter approaches.

## 3. Visual Attention Reasoning via Hierarchical Search and Self-Verification

- Authors: Wei Cai, Jian Zhao, Yuchen Yuan, Tianle Zhang, Ming Zhu, Haichuan Tang, Xuelong Li
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.0230891482724624
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.406/
- PDF: https://aclanthology.org/2026.acl-long.406.pdf
- Local PDF: pdf/2026-07-05_03_Visual Attention Reasoning via Hierarchical Search and Self-Verification.pdf

Multimodal Large Language Models (MLLMs) frequently hallucinate due to their reliance on fragile, linear reasoning and weak visual grounding. We propose Visual Attention Reasoning (VAR), a reinforcement learning framework that reformulates reasoning as a hierarchical search with self-verification. VAR enforces traceable evidence grounding by generating explicit bounding boxes, guided by a novel reward function combining geometric precision and semantic sufficiency. Furthermore, it replaces linear Chain-of-Thought with a tree-search policy capable of backtracking to correct logical errors. Theoretical analysis validates the framework’s reliability, and extensive experiments demonstrate that VAR significantly outperforms state-of-the-art methods on complex hallucination and safety benchmarks.

## 4. CoMoL: Efficient Mixture of LoRA Experts via Dynamic Core Space Merging

- Authors: Jie Cao, Zhenxuan Fan, Zhuonan Wang, Tianwei Lin, Ziyuan Zhao, Rolan Yan, Wenqiao Zhang, Feifei Shao, Hongwei Wang, Jun Xiao, Siliang Tang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.022260927346725
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.811/
- PDF: https://aclanthology.org/2026.findings-acl.811.pdf
- Local PDF: pdf/2026-07-05_04_CoMoL_ Efficient Mixture of LoRA Experts via Dynamic Core Space Merging.pdf

Large language models (LLMs) achieve remarkable performance on diverse downstream and domain-specific tasks via parameter-efficient fine-tuning (PEFT). However, existing PEFT methods, particularly MoE-LoRA architectures, suffer from limited parameter efficiency and coarse-grained adaptation due to the proliferation of LoRA experts and instance-level routing. To address these issues, we propose Core Space Mixture of LoRA ( CoMoL ), a novel MoE-LoRA framework that incorporates expert diversity, parameter efficiency, and fine-grained adaptation. Specifically, CoMoL introduces two key components: core space experts and core space routing. Core space experts store each expert in a compact core matrix, preserving diversity while controlling parameter growth. Core space routing dynamically selects and activates the appropriate core experts for each token, enabling fine-grained, input-adaptive routing. Activated core experts are then merged via a soft-merging strategy into a single core expert, which is combined with a shared LoRA to form a specialized LoRA module. Besides, the routing network is projected into the same low-rank space as the LoRA matrices, further reducing parameter overhead without compromising expressiveness. Extensive experiments demonstrate that CoMoL retains the adaptability of MoE-LoRA architectures while achieving parameter efficiency comparable to standard LoRA, consistently outperforming existing methods across multiple tasks. Our code is available at https://github.com/DCDmllm/CoMoL .

## 5. M 3 -VQA: A Benchmark for Multimodal, Multi-Entity, Multi-Hop Visual Question Answering

- Authors: Jiatong Ma, Longteng Guo, Yuchen Liu, Zijia Zhao, Dongze Hao, Xuanxu Lin, Jing Liu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.020664842907172
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1888/
- PDF: https://aclanthology.org/2026.acl-long.1888.pdf
- Local PDF: pdf/2026-07-05_05_M 3 -VQA_ A Benchmark for Multimodal, Multi-Entity, Multi-Hop Visual Question Answering.pdf

We present M 3 -VQA, a novel knowledge-based Visual Question Answering (VQA) benchmark, to enhance the evaluation of multimodal large language models (MLLMs) in fine-grained multimodal entity understanding and complex multi-hop reasoning. Unlike existing VQA datasets that focus on coarse-grained categories and simple reasoning over single entities, M 3 -VQA introduces diverse multi-entity questions involving multiple distinct entities from both visual and textual sources. It requires models to perform both sequential and parallel multi-hop reasoning across multiple documents, supported by traceable, detailed evidence and a curated multimodal knowledge base. We evaluate 16 leading MLLMs under three settings: without external knowledge, with gold evidence, and with retrieval-augmented input. The poor results reveal significant challenges for MLLMs in knowledge acquisition and reasoning. Models perform poorly without external information but improve markedly when provided with precise evidence. Furthermore, reasoning-aware agentic retrieval surpasses heuristic methods, highlighting the importance of structured reasoning for complex multimodal understanding. M 3 -VQA presents a more challenging evaluation for advancing the multimodal reasoning capabilities of MLLMs. Our code and dataset are available at https://github.com/CASIA-IVA-Lab/M3VQA.

## 6. Beyond Single View: A Comprehensive Benchmark for Medical Multimodal Large Language Models on Multi-Image Understanding

- Authors: Dexuan Xu, Yuan Jiayin, Jianing Wang, Yanyuan Chen, Hanpin Wang, Yu Huang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.019377262249537
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1263/
- PDF: https://aclanthology.org/2026.acl-long.1263.pdf
- Local PDF: pdf/2026-07-05_06_Beyond Single View_ A Comprehensive Benchmark for Medical Multimodal Large Language Models on Multi-Image Understanding.pdf

Recent advancements in Multimodal Large Language Models (MLLMs) have demonstrated impressive capabilities in interpreting single medical images. However, real-world clinical diagnosis is intrinsically a multi-view process, requiring the synthesis of information across volumetric slices, temporal sequences, and comparative modalities. Existing benchmarks fail to capture this complexity, limiting the assessment of models in realistic clinical workflows. To bridge this gap, we introduce MedMultiBench, the first large-scale benchmark specifically designed for medical multi-image understanding. Comprising 11,392 expert-curated samples, MedMultiBench evaluates MLLMs across four distinct dimensions: Joint Reasoning, Comparative Analysis, Comprehensive Perception, and In-Context Learning. We benchmark 13 state-of-the-art MLLMs, revealing that while current models excel in single-view tasks, they struggle significantly with multi-image contexts. Our experiments identify a performance degradation in open-source models when processing increased visual loads, whereas closed-source models demonstrate better scalability. MedMultiBench provides a robust framework to facilitate the development of MLLMs capable of holistic clinical reasoning.

## 7. The Dominance of Text Space: Unveiling the Asymmetric Nature of Cross-Modal Alignment in Large Language Models

- Authors: Linqing Chen, Hanmeng Zhong, Wentao Wu, Peng Zhou
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.0193339943488775
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1699/
- PDF: https://aclanthology.org/2026.acl-long.1699.pdf
- Local PDF: pdf/2026-07-05_07_The Dominance of Text Space_ Unveiling the Asymmetric Nature of Cross-Modal Alignment in Large Language Models.pdf

Recent advancements in Multimodal Large Language Models (MLLMs) have largely been driven by aligning visual encoders with pre-trained Large Language Models (LLMs). While effective, the geometric nature of this alignment remains under-explored. Existing methods often assume a symmetric interaction between visual and textual modalities, implying that both spaces adapt to each other. In this paper, we challenge this assumption and propose the "Text Space as Anchor" hypothesis. We argue that the semantic space of LLMs is rigid, anisotropic, and dominant; thus, effective cross-modal alignment may be an asymmetric projection of visual features onto this pre-existing text manifold without distorting it. We identify a potential issue in current parameter-efficient tuning paradigms where task-specific visual adjustments inadvertently disrupt the projector’s geometry, leading to "catastrophic forgetting" of the alignment mechanism itself. To address this, we introduce Anchor-Preserving Projection (APP), a novel method that regularizes the projector to maintain the geometric structure of the text embedding space via spectral filtering. Extensive experiments on 8 diverse cross-modal tasks and 3 pure language benchmarks demonstrate that APP preserves the LLM’s inherent linguistic capabilities (e.g., MMLU, GSM8K) and reduces object hallucination significantly better than standard fine-tuning methods. We release our code.

## 8. MASFactory: A Graph-centric Framework for Orchestrating LLM-Based Multi-Agent Systems with Vibe Graphing

- Authors: Yang Liu, Jinxuan Cai, Yishen Li, Qi Meng, Zedi Liu, Xin Li, Chen Qian, Chuan Shi, Cheng Yang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.0185843426120424
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-demo.35/
- PDF: https://aclanthology.org/2026.acl-demo.35.pdf
- Local PDF: pdf/2026-07-05_08_MASFactory_ A Graph-centric Framework for Orchestrating LLM-Based Multi-Agent Systems with Vibe Graphing.pdf

Large language model-based (LLM-based) multi-agent systems (MAS) are increasingly used to extend agentic problem solving via role specialization and collaboration. MAS workflows can be naturally modeled as directed computation graphs, where nodes execute agents or sub-workflows and edges encode dependencies and message passing. However, implementing complex graph workflows in current frameworks still requires substantial manual effort, offers limited reuse, and makes it difficult to integrate heterogeneous external context sources. To overcome these limitations, we present MASFactory, a graph-centric framework for orchestrating LLM-based MAS. It introduces Vibe Graphing, a human-in-the-loop approach that compiles natural-language intent into an editable workflow specification and then into an executable graph. In addition, the framework provides reusable components, skill support, multimodal message handling, and pluggable context integration, as well as a visualizer for topology preview, runtime tracing, and human-in-the-loop interaction. We evaluate MASFactory on seven public benchmarks, validating both reproduction consistency for representative MAS methods and the effectiveness of Vibe Graphing. Our code (https://github.com/BUPT-GAMMA/MASFactory, licensed under Apache-2.0) and video demonstration (https://youtu.be/ANynzVfY32k) are publicly available.

## 9. Language Acquisition Device in Large Language Models

- Authors: Masato Mita, Taiga Someya, Ryo Yoshida, Yohei Oseki
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.018558857207921
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.895/
- PDF: https://aclanthology.org/2026.acl-long.895.pdf
- Local PDF: pdf/2026-07-05_09_Language Acquisition Device in Large Language Models.pdf

Large Language Models (LLMs) remain substantially less data-efficient than humans. Pre-pretraining (PPT) on synthetic languages has been proposed to close this gap, with prior work emphasizing highly expressive formal languages such as k -Shuffle Dyck. Inspired by the Language Acquisition Device (LAD) hypothesis, which posits that innate constraints preemptively restrict the learner’s hypothesis space to natural-language-like structure, we propose LAD-inspired PPT: pre-pretraining on MP-STRUCT, a formal language whose strings encode hierarchical composition, feature-based dependencies, and long-distance displacement via MERGE, AGREE, and MOVE. A brief 500-step PPT with MP-STRUCT matches strong formal-language baselines in token efficiency while additionally imparting a human-like resistance to structurally implausible languages. Analyzing simplified variants, we find that MP-STRUCT CORE outperforms k -Shuffle Dyck despite not being definable in C-RASP (a formal bound on transformer expressivity), challenging the prior hypothesis that effective PPT languages must be both hierarchically expressive and circuit-theoretically learnable. We show that functional landmarks, which reduce dependency resolution ambiguity, are a key driver, suggesting that effective PPT design depends not only on expressivity but also on the accessibility of dependency resolution.

## 10. LLM-Aligned Geographic Item Tokenization for Local-Life Recommendation

- Authors: Hao Jiang, GuoQuan Wang, Donglin Zhou, Sheng Yu, Yang Zeng, Wencong Zeng, Kun Gai, Guorui Zhou
- Source: openalex
- Venue type: conference
- Journal: Proceedings of the AAAI Conference on Artificial Intelligence
- Publication status: formally_published
- Publication date: 2026-03-14
- DOI: https://doi.org/10.1609/aaai.v40i17.38514
- Categories: Recommender Systems and Techniques, Advanced Graph Neural Networks, Topic Modeling
- Relevance: 3.017619233945651
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://doi.org/10.1609/aaai.v40i17.38514
- PDF: https://ojs.aaai.org/index.php/AAAI/article/download/38514/42476
- Local PDF: Not downloaded

Recent advances in Large Language Models (LLMs) have enhanced text-based recommendation by enriching traditional ID-based methods with semantic generalization capabilities. Text-based methods typically encode item textual information via prompt design and generate discrete semantic IDs through item tokenization. However, in domain-specific tasks such as local-life services, simply injecting location information into prompts fails to capture fine-grained spatial characteristics and real-world distance awareness among items. To address this, we propose LGSID, an LLM-Aligned Geographic Item Tokenization Framework for Local-life Recommendation. This framework consists of two key components: (1) RL-based Geographic LLM Alignment, and (2) Hierarchical Geographic Item Tokenization. In the RL-based alignment module, we initially train a list-wise reward model to capture real-world spatial relationships among items. We then introduce a novel G-DPO algorithm that uses pre-trained reward model to inject generalized spatial knowledge and collaborative signals into LLMs while preserving their semantic understanding. Furthermore, we propose a hierarchical geographic item tokenization strategy, where primary tokens are derived from discrete spatial and content attributes, and residual tokens are refined using the aligned LLM’s geographic representation vectors. Extensive experiments on real-world Kuaishou industry datasets show that LGSID consistently outperforms state-of-the-art discriminative and generative recommendation models. Ablation studies, visualizations, and case studies further validate its effectiveness.

## 11. Memorization, Emergence, and Explaining Reversal Failures: A Controlled Study of Relational Semantics in LLMs

- Authors: Yihua Zhu, Qianying Liu, Jiaxin Wang, Fei Cheng, Chaoran Liu, Akiko Aizawa, Sadao Kurohashi, Hidetoshi Shimodaira
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.0161905871529044
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1688/
- PDF: https://aclanthology.org/2026.acl-long.1688.pdf
- Local PDF: pdf/2026-07-05_11_Memorization, Emergence, and Explaining Reversal Failures_ A Controlled Study of Relational Semantics in LLMs.pdf

Autoregressive LLMs perform well on relational tasks that require linking entities via relational words (e.g., father/son, friend), but it is unclear whether they learn the logical semantics of such relations (e.g., symmetry and inversion logic) and, if so, whether reversal-type failures arise from missing relational semantics or left-to-right order bias. We propose a controlled Knowledge Graph-based synthetic framework that generates text from symmetric/inverse triples, train GPT-style autoregressive models from scratch, and evaluate memorization, logical inference, and in-context generalization to unseen entities to address these questions. We find a sharp phase transition in which relational semantics emerge with sufficient logic-bearing supervision, even in shallow (2–3 layer) models, and that successful generalization aligns with stable intermediate-layer signals. Finally, order-matched forward/reverse tests and a diffusion baseline indicate that reversal failures are primarily driven by autoregressive order bias rather than deficient inversion semantics.

## 12. Can LLMs Reason Over Non-Text Modalities in a Training-Free Manner? A Case Study with In-Context Representation Learning

- Authors: Zhang, Tianle, Fang, Wanlong, Woo, Jonathan, Latawa, Paridhi, Subramanian, Deepak, Chan, Alvin
- Source: neurips
- Venue type: conference
- Journal: NeurIPS 2025
- Publication status: formally_published
- Publication date: 2026-04-23
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.016073981866004
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://proceedings.neurips.cc/paper_files/paper/2025/hash/0904c7edde20d7134a77fc7f9cd86ea2-Abstract-Conference.html
- PDF: https://proceedings.neurips.cc/paper_files/paper/2025/file/0904c7edde20d7134a77fc7f9cd86ea2-Paper-Conference.pdf
- Local PDF: pdf/2026-07-05_12_Can LLMs Reason Over Non-Text Modalities in a Training-Free Manner_ A Case Study with In-Context Representation Learning.pdf

The remarkable performance of Large Language Models (LLMs) can be enhanced with test-time computation, which relies on external tools and even other deep learning models. However, existing approaches for integrating non-text modality representations into LLMs typically require additional costly supervised training, restricting on-the-fly adaptation to new domains and modalities. In this work, we explore the feasibility of integrating representations from non-text foundational models (FMs) into text-based LLMs in a training-free manner. We propose In-Context Representation Learning (ICRL) as a proof-of-concept to allow LLMs to adaptively utilize non-text modality representations with few-shot learning. Unlike traditional in-context learning, which incorporates text-label pairs, ICRL replaces text inputs with FM representations, enabling the LLM to perform multi-modal inference without fine-tuning. We evaluate ICRL on a suite of tasks in the molecular domain, investigating three core research questions: (i) how to map FM representations into LLMs in a training-free manner, (ii) what factors influence ICRL performance, and (iii) what mechanisms underlie the effectiveness of ICRL. To the best of our knowledge, ICRL is the first training-free framework for integrating non-text modality representations into text-based LLMs, presenting a promising direction for adaptable, multi-modal generalization.

## 13. RATION: Entropy-Driven Task-Adaptive Visual Attention Allocation Framework for Multimodal Reasoning

- Authors: Xingle Xu, Fanheng Kong, Dexian Cai, Shi Feng, Xiaocui Yang, Daling Wang, Yifei Zhang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.015445680424552
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1238/
- PDF: https://aclanthology.org/2026.findings-acl.1238.pdf
- Local PDF: pdf/2026-07-05_13_RATION_ Entropy-Driven Task-Adaptive Visual Attention Allocation Framework for Multimodal Reasoning.pdf

Multimodal Large Language Models (MLLMs) integrate visual encoders with Large Language Models (LLMs) and enable multimodal reasoning. However, for tasks that heavily rely on visual information, the model’s utilization of visual information remains unstable, which leads to reasoning failures. Prior works mainly strengthen multimodal reasoning by improving representation alignment or increasing computation. However, these methods do not explicitly characterize the differences in visual demands across tasks, making it difficult for the model to decide where and how strongly to attend to visual information. Consequently, visual attention allocation becomes a key factor that affects multimodal reasoning. To address these, we propose RATION, an entropy-driven task-adaptive visual attention allocation framework. First, we use a task routing strategy to infer the task type of each sample and identify the key layers. We use visual attention entropy as a control signal to dynamically allocate attention according to task demands. Experiments show that RATION achieves consistent performance gains across diverse reasoning tasks, datasets, and models, providing a clear direction toward more reliable multimodal reasoning.

## 14. Data-Centric Perspectives on Agentic Retrieval-Augmented Generation: A Survey

- Authors: Jingwen Deng, Jihao Huang, Zhen Hao Wong, Hao Liang, Quanqing Xu, Bin Cui, Wentao Zhang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.015047399189987
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.78/
- PDF: https://aclanthology.org/2026.findings-acl.78.pdf
- Local PDF: pdf/2026-07-05_14_Data-Centric Perspectives on Agentic Retrieval-Augmented Generation_ A Survey.pdf

Large Language Models (LLMs) excel at natural language understanding and generation, yet their reliance on static pre-training corpora may lead to outdated knowledge, hallucinations, and limited adaptability. Retrieval-Augmented Generation (RAG) mitigates these issues by grounding model outputs with external retrieval, but conventional RAG remains constrained by a fixed retrieve-then-generate routine and struggles with multi-step reasoning and tool calls. **Agentic RAG** addresses these limitations by enabling LLM agents to actively decompose tasks, issue exploratory queries, and refine evidence through iterative retrieval. Despite growing interest, the development of Agentic RAG is impeded by *data scarcity*: unlike traditional RAG, it requires challenging tasks that require planning, retrieval, and multiple reasoning decisions, and corresponding rich, interactive agent trajectories. This survey presents the first data-centric overview of Agentic RAG, framing its data lifecycle—data collecting, data preprocessing and task formulation, task construction, data for evaluation, and data enhancement for training—and cataloging representative training datasets and benchmarks in different domains (e.g. question answering, web, software engineering). From data perspectives, we aim to guide the creation of scalable, high-quality datasets for the next generation of adaptive, knowledge-seeking LLM agents. The project page is at https://github.com/fatty-belly/Awesome-AgenticRAG-Data/.

## 15. LatentGate: Low-Latency Semantic Routing via Frozen-Backbone Probing of Small Language Models

- Authors: Shivam Ratnakar, Abhiroop Talasila, Vinayak K Doifode
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.015002465707901
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-industry.153/
- PDF: https://aclanthology.org/2026.acl-industry.153.pdf
- Local PDF: pdf/2026-07-05_15_LatentGate_ Low-Latency Semantic Routing via Frozen-Backbone Probing of Small Language Models.pdf

As Multi-Agent Systems scale to hundreds of specialized agents, routing becomes a critical bottleneck. Prompt-based LLM routers deliver strong semantic reasoning but incur prohibitive latency (~1500–2000ms) and cost that scales with agent count, while embedding-based routers are fast (25–50ms) but collapse semantically similar yet functionally distinct agents. We identify *representation anisotropy*, the geometric collapse of hidden-state vectors into a narrow cone, as a key mechanism underlying embedding-based routing failure. We propose **LatentGate**, a non-generative router that extracts mean-pooled hidden states from a frozen small language model (SLM), applies PCA-whitening to resolve the anisotropy, and trains a lightweight linear probe for agent classification. Across 5 SLM backbones and 100 enterprise agents, LatentGate achieves 98.8% in-domain and 80.0% OOD accuracy on natural queries, 13–22 absolute points above embedding baselines, and 92.9% on CLINC150. It takes ~28ms to run on a T4 GPU, with the SLM forward pass independent of agent count and classification adding a negligible O(Ck) term. We demonstrate the potential of using a lightweight linear probe to enable sub-10ms warm-start retraining from user feedback, providing a foundation for continual learning in production environments. Benchmarking prompt-based routing with GPT-4.1, GPT-4.1-nano, and Gemini 2.5 Flash confirms degradation to 70–77% accuracy at 100 agents with 1500–2000ms latency, motivating non-generative alternatives.

## 16. On the Bias of Next-Token Predictors Toward Systematically Inefficient Reasoning: A Shortest-Path Case Study

- Authors: Alberghi, Riccardo, Demyanenko, Elizaveta, Biggio, Luca, Saglietti, Luca
- Source: neurips
- Venue type: conference
- Journal: NeurIPS 2025
- Publication status: formally_published
- Publication date: 2026-04-23
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.012724077711302
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://proceedings.neurips.cc/paper_files/paper/2025/hash/090298ec38fee9b8ced6dad1e1c3a7d8-Abstract-Conference.html
- PDF: https://proceedings.neurips.cc/paper_files/paper/2025/file/090298ec38fee9b8ced6dad1e1c3a7d8-Paper-Conference.pdf
- Local PDF: pdf/2026-07-05_16_On the Bias of Next-Token Predictors Toward Systematically Inefficient Reasoning_ A Shortest-Path Case Study.pdf

Recent advances in natural language processing highlight two key factors for improving reasoning in large language models (LLMs): (i) allocating more test-time compute tends to help on harder problems but often introduces redundancy in the reasoning trace, and (ii) compute is most effective when reasoning is systematic and incremental, forming structured chains of thought (CoTs) akin to human problem-solving. To study these factors in isolation, we introduce a controlled setting based on shortest-path tasks in layered graphs. We train decoder-only transformers on question–trace–answer triples using a custom tokenizer, comparing models trained on optimal bottom-up dynamic programming traces with those trained on longer, valid traces involving backtracking. Surprisingly, under the same training-token budget, the latter models generalize better to unseen graphs. This benefit is not due to length alone—injecting arbitrary redundancy into reasoning traces fails to help and can even hurt performance. Instead, we find that generalization correlates with the model's confidence in next-token prediction, suggesting that long, coherent, and locally incremental traces make the training signal easier to optimize.

## 17. CAGenMol: Condition-Aware Diffusion Language Model for Goal-Directed Molecular Generation

- Authors: Yanting Li, Zhuoyang Jiang, Enyan Dai, Lei Wang, Wen-Cai Ye, Li Liu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.0119336726956947
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.232/
- PDF: https://aclanthology.org/2026.findings-acl.232.pdf
- Local PDF: pdf/2026-07-05_17_CAGenMol_ Condition-Aware Diffusion Language Model for Goal-Directed Molecular Generation.pdf

Goal-directed molecular generation requires satisfying heterogeneous constraints such as protein–ligand compatibility and multi-objective drug-like properties, yet existing methods often optimize these constraints in isolation, failing to reconcile conflicting objectives (e.g., affinity vs. safety), and struggle to navigate the non-differentiable chemical space without compromising structural validity. To address these challenges, we propose CAGenMol, a condition-aware discrete diffusion framework over molecular sequences that formulates molecular design as conditional denoising guided by heterogeneous structural and property signals. By coupling discrete diffusion with reinforcement learning, the model aligns the generation trajectory with non-differentiable objectives while preserving chemical validity and diversity. The non-autoregressive nature of diffusion language model further enables iterative refinement of molecular fragments at inference time. Experiments on structure-conditioned, property-conditioned, and dual-conditioned benchmarks demonstrate consistent improvements over state-of-the-art methods in binding affinity, drug-likeness, and success rate, highlighting the effectiveness of our framework. The code is available at https://github.com/Lee612-1/CAGenMol .

## 18. InstructDiff: Domain-Adaptive Data Selection via Contrastive Entropy for Efficient LLM Fine-Tuning

- Authors: Junyou Su, He Zhu, Xiao Luo, Liyu Zhang, Hong-Yu Zhou, Yun Chen, Peng Li, Yang Liu, Guanhua Chen
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.011568142755414
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.486/
- PDF: https://aclanthology.org/2026.acl-long.486.pdf
- Local PDF: pdf/2026-07-05_18_InstructDiff_ Domain-Adaptive Data Selection via Contrastive Entropy for Efficient LLM Fine-Tuning.pdf

Supervised fine-tuning (SFT) is fundamental to adapting large language models, yet training on complete datasets incurs prohibitive costs with diminishing returns. Existing data selection methods suffer from severe domain specificity: techniques optimized for general instruction-following fail on reasoning tasks, and vice versa. We observe that measuring contrastive entropy between base models and minimally instruction-tuned calibrated models reveals a pattern—samples with the lowest contrastive entropy consistently yield optimal performance across domains, yet this principle manifests domain-adaptively: reasoning tasks favor entropy increase (cognitive expansion), while general tasks favor entropy decrease (cognitive compression). We introduce InstructDiff, a unified framework that operationalizes contrastive entropy as a domain-adaptive selection criterion through warmup calibration, bi-directional NLL filtering, and entropy-based ranking. Extensive experiments show that InstructDiff achieves 17% relative improvement over full data training on mathematical reasoning and 52% for general instruction-following, outperforming prior baselines while using only 10% of the data.

## 19. Cognitive Scaffold: From Fluid Context to Crystallized Memory for Long-Horizon DeepResearch Agents

- Authors: Qiuyuan Ai, Zenghuang Fu, Zhaoyang Li, Ping Jiang, Haoyu Wu, Jie Song, Guannan He
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.0103612189024007
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1170/
- PDF: https://aclanthology.org/2026.acl-long.1170.pdf
- Local PDF: pdf/2026-07-05_19_Cognitive Scaffold_ From Fluid Context to Crystallized Memory for Long-Horizon DeepResearch Agents.pdf

Scaling LLM-based agents to long-horizon deep research is constrained by the context-noise trade-off, where linear history accumulation degrades reasoning and dilutes fine-grained evidence. To address this, we introduce the Cognitive Scaffold, a factorized memory architecture that decouples the cognitive state into a Fluid Working Context for immediate reasoning and a persistent Knowledge Graph for long-term retention. Unlike unstructured summarization, our framework employs a Rejection Sampling Fine-Tuning (RFT) pipeline to crystallize saturated context into structured event snapshots, strictly enforcing atomic constraints to preserve numerical values and entities. During reasoning, a thought-driven dual-path retrieval mechanism enables the agent to proactively recover precise evidence. Empirical evaluations on Xbench-DeepSearch, BrowseComp-ZH, and GAIA demonstrate that Cognitive Scaffold consistently outperforms baselines, achieving 74.7% Avg@3 and 87.0% Pass@3 on Xbench-DeepSearch, 48.5% Avg@3 and 65.9% Pass@3 on BrowseComp-ZH, and 72.8% Avg@3 and 88.3% Pass@3 on GAIA, while reducing compression hallucinations to 5.3%. We open-source our codebase to facilitate future research.

## 20. Unleashing Spatial Reasoning in Multimodal Large Language Models via Textual Representation Guided Reasoning

- Authors: Jiacheng Hua, Yishu Yin, Yuhang Wu, Tai Wang, Yifei Huang, Miao Liu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.009606754188931
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.620/
- PDF: https://aclanthology.org/2026.acl-long.620.pdf
- Local PDF: pdf/2026-07-05_20_Unleashing Spatial Reasoning in Multimodal Large Language Models via Textual Representation Guided Reasoning.pdf

Existing Multimodal Large Language Models (MLLMs) struggle with 3D spatial reasoning, as they fail to construct structured abstractions of the 3D environment depicted in video inputs. To bridge this gap, drawing inspiration from cognitive theories of allocentric spatial reasoning, we investigate how to enable MLLMs to model and reason over text-based spatial representations of video. Specifically, we introduce Textual Representation of Allocentric Context from Egocentric Video (TRACE), a prompting method that induces MLLMs to generate text-based representations of 3D environments as intermediate reasoning traces for more accurate spatial question answering. TRACE encodes meta-context, camera trajectories, and detailed object entities to support structured spatial reasoning over egocentric videos. Extensive experiments on VSI-Bench and OST-Bench demonstrate that TRACE yields notable and consistent improvements over prior prompting strategies across a diverse range of MLLM backbones, spanning different parameter scales and training schemas. We further present ablation studies to validate our design choices, along with detailed analyses that probe the bottlenecks of 3D spatial reasoning in MLLMs.

## 21. A Universal Avoidance Method for Diverse Multi-branch Generation

- Authors: Kyeongman Park, Minha Jhang, Kyomin Jung
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.0092839346160973
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.777/
- PDF: https://aclanthology.org/2026.findings-acl.777.pdf
- Local PDF: pdf/2026-07-05_21_A Universal Avoidance Method for Diverse Multi-branch Generation.pdf

Modern generative models still lack human-level creativity, particularly in multi-branch diversity. Prior approaches to address this problem often incur heavy computation or strong dependency on model architecture. Therefore, we introduce **UAG**(**U**niversal **A**voidance **G**eneration), a model-agnostic and computationally efficient generation strategy that penalizes similarity among previously generated outputs. Thus, UAG can enhance multi-branch diversity across both diffusion and transformer models, with minimal additional computation. In experiments, our method achieves up to 1.9 times higher diversity, runs 4.4 times faster, and requires only 1/64 of the FLOPs compared to state-of-the-art methods.

## 22. Adaptive Zooming via Relevance-Informed Positional Resource Allocation for Training-free LLM Context Extension

- Authors: Hongbo Zhao, Huibin Wang, Bin Tang, Xianming Hu, Yihong Huang, Yijun Shen, Nuoyi Chen, Ping Li, Kai Zhang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.0090075164581567
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1058/
- PDF: https://aclanthology.org/2026.findings-acl.1058.pdf
- Local PDF: pdf/2026-07-05_22_Adaptive Zooming via Relevance-Informed Positional Resource Allocation for Training-free LLM Context Extension.pdf

Large Language Models exhibit degraded performance when extrapolating beyond training context lengths. Existing training-free methods like positional reuse or interpolation can alleviate this issue in an efficient manner. However, these strategies are semantics-agnostic by only considering relative token distances, which could indiscriminately blur semantically relevant and irrelevant tokens alike.To address this, we introduce an adaptive positional zooming method called **Relevance-Informed Positional Resource Allocation (RiPRA)**. RiPRA formulates positional encoding as a constrained resource allocation, in which a fixed positional budget is distributed across tokens in a longer context based on their semantic relevance to the query: relevant tokens get higher positional resolution, while irrelevant tokens (positions) are compressed. By doing this, RiPRA enables a dynamic and nonparametric positional zooming where the positional resolution is adaptively modulated across queries and network layers, effectively improving long-range context modeling and retrieval capacity. Besides, an isotonic smoothing is used to further enforce a global linear ordering relationship to preserve stability and generalization, together with a chunk-based hierarchical approximation to further reduce inference overhead. Extensive experiments across comprehensive benchmarks including LongBench, L-Eval, Passkey Retrieval, and PG19 demonstrate that RiPRA consistently outperforms existing training-free extrapolation methods, showing the value of relevance-conditioned positional encoding for long-context generalization.

## 23. LLMs Meet Isolation Kernel: Lightweight, Learning-free Binary Embeddings for Fast Retrieval

- Authors: Zhibo Zhang, Yang Xu, Kai Ming Ting, Cam-Tu Nguyen
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.0088131476347506
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.666/
- PDF: https://aclanthology.org/2026.findings-acl.666.pdf
- Local PDF: pdf/2026-07-05_23_LLMs Meet Isolation Kernel_ Lightweight, Learning-free Binary Embeddings for Fast Retrieval.pdf

Large language models (LLMs) have recently enabled remarkable progress in text representation. However, their embeddings are typically high-dimensional, leading to substantial storage and retrieval overhead. Although recent approaches such as Matryoshka Representation Learning (MRL) and Contrastive Sparse Representation (CSR) alleviate these issues to some extent, they still suffer from retrieval accuracy degradation. This paper proposes Isolation Kernel Embedding or IKE, a learning-free method that transforms an LLM embedding into a binary embedding using Isolation Kernel (IK). Lightweight and based on binary encoding, IKE offers a low memory footprint and fast bitwise computation, lowering retrieval latency. Experiments on multiple text retrieval datasets demonstrate that IKE offers up to 16.7 × faster retrieval and 16 × lower memory usage than the original LLM embeddings, while maintaining comparable accuracy. Theoretically, we show that IKE works because it satisfies four essential criteria for effective binary hashing that other methods do not possess. Compared to CSR, IKE consistently achieves better retrieval efficiency and effectiveness. IKE also works effectively with graph-based indexing, demonstrating its superiority in balancing accuracy and latency compared to alternative compression techniques in the approximate nearest neighbor (ANN) search setting.

## 24. GUARDIAN: Safeguarding LLM Multi-Agent Collaborations with Temporal Graph Modeling

- Authors: Zhou, Jialong, Wang, Lichao, Yang, Xiao
- Source: neurips
- Venue type: conference
- Journal: NeurIPS 2025
- Publication status: formally_published
- Publication date: 2026-04-23
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.0062868325577563
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://proceedings.neurips.cc/paper_files/paper/2025/hash/0bc795afae289ed465a65a3b4b1f4eb7-Abstract-Conference.html
- PDF: https://proceedings.neurips.cc/paper_files/paper/2025/file/0bc795afae289ed465a65a3b4b1f4eb7-Paper-Conference.pdf
- Local PDF: pdf/2026-07-05_24_GUARDIAN_ Safeguarding LLM Multi-Agent Collaborations with Temporal Graph Modeling.pdf

The emergence of large language models (LLMs) enables the development of intelligent agents capable of engaging in complex and multi-turn dialogues. However, multi-agent collaboration faces critical safety challenges, such as hallucination amplification and error injection and propagation. This paper presents GUARDIAN, a unified method for detecting and mitigating multiple safety concerns in GUARDing Intelligent Agent collaboratioNs. By modeling the multi-agent collaboration process as a discrete-time temporal attributed graph, GUARDIAN explicitly captures the propagation dynamics of hallucinations and errors. The unsupervised encoder-decoder architecture incorporating an incremental training paradigm learns to reconstruct node attributes and graph structures from latent embeddings, enabling the identification of anomalous nodes and edges with unparalleled precision. Moreover, we introduce a graph abstraction mechanism based on the Information Bottleneck Theory, which compresses temporal interaction graphs while preserving essential patterns. Extensive experiments demonstrate GUARDIAN's effectiveness in safeguarding LLM multi-agent collaborations against diverse safety vulnerabilities, achieving state-of-the-art accuracy with efficient resource utilization. The code is available at https://github.com/JialongZhou666/GUARDIAN.

## 25. UCGRec: User-Centric Graph Learning for LLM-based Sequential Recommendation

- Authors: HanBeul Kim, CheolWon Na, Suyoung Bae, YunSeok Choi, Jee-Hyong Lee
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.005954783230348
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.175/
- PDF: https://aclanthology.org/2026.findings-acl.175.pdf
- Local PDF: pdf/2026-07-05_25_UCGRec_ User-Centric Graph Learning for LLM-based Sequential Recommendation.pdf

Recently, Large Language Models (LLM) have emerged as a promising paradigm for sequential recommendation. In sequential recommendation, effectively integrating diverse user preferences is essential for improving LLM performance, as users often exhibit multiple interests across different contexts. However, most existing LLM-based methods rely primarily on item descriptions or utilize user preferences independently. As a result, they overlook the relationships among preferences and fail to filter out less-relevant items that introduce noise. This makes it difficult to accurately capture the user’s interests, leading to suboptimal recommendations. To overcome these limitations, we propose UCGRec (User-Centric Graph Learning for LLM-based Sequential Recommendation), a novel method that effectively integrates diverse user-relevant preference signals into a unified user-centric graph. Then, we inject the graph-based knowledge into the LLM through end-to-end training with graph neural networks. We conduct extensive experiments on four widely used sequential real-world recommendation datasets. Our experimental results demonstrate that UCGRec significantly outperforms conventional and state-of-the-art LLM-based methods.

## 26. Hetero-Designer: Automated Design of Multi-Agent Systems with Heterogeneous LLMs

- Authors: Zhiheng Zhang, Yuanzhe Zhang, Bohan Yu, Daojian Zeng, Kang Liu, Jun Zhao
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.005843274457835
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1272/
- PDF: https://aclanthology.org/2026.acl-long.1272.pdf
- Local PDF: pdf/2026-07-05_26_Hetero-Designer_ Automated Design of Multi-Agent Systems with Heterogeneous LLMs.pdf

LLM-based Multi-agent systems (MAS) have shown strong capabilities across a wide range of domains. Their success largely hinges on the collaboration topology design, which has emerged as a central research focus in the automated MAS design.However, existing approaches are fundamentally constrained by their reliance on homogeneous LLMs, which significantly limits overall system intelligence.In response to this limitation, we for the first time propose the concept of **Automated Design of Heterogeneous-LLMs-based MAS (ADHM)**.ADHM sheds light on a promising avenue for advancing collective intelligence, which focuses on the automated design of cost-effective MAS composed of diverse LLMsand roles to suit various queries.Toward this challenging goal, we propose **Hetero-Designer**, a novel pipeline that efficiently encodes intricate dependencies among queries, LLMs and roles through a novel Binary-Star Transformer and constructs Hetero-MAS in an autoregressive graph generation process. Extensive experiments demonstrate that **Hetero-Designer** is: (1) high-performing on various benchmarks, (2) economical in reducing overhead, (3) extensible to unseen LLMs and roles.

## 27. From Experts to Bases: Orthogonal Subspace Mixture for Continual Multimodal Instruction Tuning

- Authors: Pei Chen, Xilai Wang, Shiqixu, Zejian Li, Lingyun Sun
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.0056464217437022
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.481/
- PDF: https://aclanthology.org/2026.acl-long.481.pdf
- Local PDF: pdf/2026-07-05_27_From Experts to Bases_ Orthogonal Subspace Mixture for Continual Multimodal Instruction Tuning.pdf

Multimodal Continual Instruction Tuning (MCIT) is essential for adapting Multimodal Large Language Models (MLLMs) to dynamic data streams, yet preventing catastrophic forgetting remains a major challenge. Existing parameter-efficient approaches often face a dilemma: fixed architectures suffer from knowledge interference, while dynamic strategies incur inefficient capacity expansion, limiting scalability. We propose MoBLoRA (Mixture-of-Bases LoRA), a novel framework for MCIT. Motivated by our geometric analysis revealing subspace redundancy across sequential tasks, MoBLoRA shifts the paradigm from expert selection to subspace mixing: it decomposes adaptation weights into a globally shared pool of orthonormal bases to capture task-invariant knowledge, and lightweight mixing matrices to encode task-specific variations. This design effectively decouples knowledge accumulation from task reconstruction. Experiments on standard benchmarks show MoBLoRA significantly outperforms state-of-the-art methods while maintaining superior parameter efficiency.

## 28. ModularMoE: Fast LLM Customization with Parameter-Sharing Mixture-of-Experts for Low-Resource Settings

- Authors: Jiaxing Liu, Qi Qi, Haifeng Sun, Dunjun Li, Zirui Zhuang, Bo He, Xiang Yang, Cong Liu, Jianxin Liao, Jingyu Wang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.0052010863219456
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.174/
- PDF: https://aclanthology.org/2026.findings-acl.174.pdf
- Local PDF: pdf/2026-07-05_28_ModularMoE_ Fast LLM Customization with Parameter-Sharing Mixture-of-Experts for Low-Resource Settings.pdf

The massive size of Large Language Models (LLMs) imposes substantial computational and storage burdens, particularly on devices with limited hardware resources. Compared to foundation models, smaller and more specialized models are often more suitable for practical deployment. Existing customization approaches, such as the conventional “prune-then-finetune” paradigm or task-agnostic deployment strategies, either incur excessive computational costs or lead to suboptimal task performance. The recently popular Mixture-of-Experts (MoE) architecture exhibits a strong ability to mitigate inter-task interference, offering a new perspective on model deployment. In this paper, we introduce ModularMoE, a training framework that converts pre-trained LLMs into parameter-sharing MoE models for lightweight deployment. Exploiting the emergent modularity within LLMs, we split the feed-forward layers into multiple disjoint modules. Each expert is then constructed as a combination of such modules, enabling knowledge sharing across experts and thereby improving parameter efficiency within MoEs. Extensive experiments across multiple downstream tasks demonstrate that ModularMoE outperforms other state-of-the-art baselines at the same sparsity level, achieving an average performance improvement of 4.10% to 28.75% while delivering up to 2.71× inference speedup.

## 29. From Personal to Collective: On the Role of Local and Global Knowledge in LLM Personalization

- Authors: Zehong Wang, Junlin Wu, Zhaoxuan Tan, Bolian Li, Xianrui Zhong, Zheli Liu, Qingkai Zeng
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.0050131980922923
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1478/
- PDF: https://aclanthology.org/2026.findings-acl.1478.pdf
- Local PDF: pdf/2026-07-05_29_From Personal to Collective_ On the Role of Local and Global Knowledge in LLM Personalization.pdf

Large language model (LLM) personalization typically relies on modeling each user in isolation, conditioning on their historical interactions to adapt model behavior. However, this user-centric formulation overlooks the collective knowledge shared across users, limiting generalization for users with sparse histories and amplifying overfitting for those with highly skewed behaviors. We argue that effective personalization requires leveraging both individual preferences and population-level patterns. To this end, we propose LoGo, a Local–Global knowledge framework that augments user-specific signals with a global knowledge encoding collective behavioral trends. LoGo models global knowledge through a temporally evolving process that captures how population-wide preferences change over time, and a community-aware structure that organizes users into coherent groups with shared interests. To balance potentially conflicting local and global signals, LoGo employs a mediator module that adaptively fuses the two knowledge sources. Experiments on five personalization benchmarks show that LoGo consistently enhances personalization quality, outperforming existing methods by improving generalization in users with limited histories and mitigating bias in users with abundant histories. These results demonstrate the central role of collective knowledge in advancing LLM personalization. Our code is publicly available at https://github.com/Zehong-Wang/LoGo.

## 30. AutoGraph-R1: End-to-End Reinforcement Learning for Knowledge Graph Construction

- Authors: Hong Ting Tsang, Jiaxin Bai, Haoyu Huang, Qiao Xiao, Tianshi Zheng, Baixuan Xu, Shujie Liu, Yangqiu Song
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.0048235793024163
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1070/
- PDF: https://aclanthology.org/2026.acl-long.1070.pdf
- Local PDF: pdf/2026-07-05_30_AutoGraph-R1_ End-to-End Reinforcement Learning for Knowledge Graph Construction.pdf

Building effective knowledge graphs (KGs) for Retrieval-Augmented Generation (RAG) is pivotal for advancing question answering (QA) systems. However, its effectiveness is hindered by a fundamental disconnect: the knowledge graph (KG) construction process is decoupled from its downstream application, yielding suboptimal graph structures. To bridge this gap, we introduce AutoGraph-R1, the first framework to directly optimize KG construction for task performance using Reinforcement Learning (RL). AutoGraph-R1 trains an LLM constructor by framing graph generation as a policy learning problem, where the reward is derived from the graph’s functional utility in a RAG pipeline. We design two novel, task-aware reward functions, one for graphs as knowledge carriers and another as knowledge indices. Across multiple QA benchmarks, AutoGraph-R1 consistently enables graph RAG methods to achieve significant performance gains over using task-agnostic baseline graphs. Our work shows it is possible to close the loop between construction and application, shifting the paradigm from building intrinsically ‘good‘ graphs to building demonstrably ‘useful‘ ones.
