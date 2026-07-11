# Paper Daily Reading - 2026-07-11

## 1. Structure Learning on Clustered Data

- Authors: Ryan Thompson, Matt P. Wand, Veerabhadran Baladandayuthapani
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-09
- DOI: Unavailable
- Categories: cs.LG, stat.ME, stat.ML
- Relevance: 3.792830238313878
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.08238v1
- PDF: https://arxiv.org/pdf/2607.08238v1
- Local PDF: pdf/2026-07-11_01_Structure Learning on Clustered Data.pdf

Recent algorithmic advances have made directed acyclic graph (DAG) structure learning scalable for causal discovery. Yet, the currently available techniques assume a completely homogeneous population, precluding their application to clustered data where cluster-specific variations (e.g., patient-specific effects) are common. We address this issue by introducing a new approach that estimates a global structure while accounting for local cluster-level effects. The key idea is to extend the fixed- and random-effects framework of classical mixed models to the structure learning setting. Towards this end, we present a differentiable graph coupling mechanism that guarantees the union of the fixed- and random-effects graphs remains acyclic. Computationally, we provide a provably convergent first-order method and leverage efficient batched updates across clusters. Statistically, we establish identifiability of the model and show that our approach recovers the true structure asymptotically. In experiments on real and synthetic data, our proposal detects dependencies missed by alternative estimators, underscoring its value for structure learning in clustered settings.

## 2. An exact information theory of generalization phase transitions in Bayesian diffusion models

- Authors: Henry Hunt, Mason Kamb, Surya Ganguli
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-09
- DOI: Unavailable
- Categories: cs.LG, cond-mat.dis-nn
- Relevance: 3.3239930238157256
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.08041v1
- PDF: https://arxiv.org/pdf/2607.08041v1
- Local PDF: pdf/2026-07-11_02_An exact information theory of generalization phase transitions in Bayesian diffusion models.pdf

How diffusion models circumvent the curse of dimensionality to learn complex distributions over high dimensional spaces from a finite training set, instead of memorizing it, remains a fundamental mystery. To address this, we introduce analytically tractable Bayesian information restricted diffusion (BIRD) models, in which each pixel observes restricted information about noisy data. A BIRD model time-reverses diffusion by inferring which past training sample produced its current restricted observation using the Bayesian posterior. This model class generalizes existing analytical diffusion models that use spatially local information restriction. We show that spatially local BIRD models closely approximate trained diffusion models \textit{early in training}, across different architectures such as UNets and DiTs. Under minimal assumptions on the data distribution, we identify an information-theoretic phase boundary between memorization and generalization in the joint space of amount of training data, time in the reverse generative process, and amount of information restriction: a BIRD model memorizes when the mutual information between its restricted noisy observations and the training data exceeds the log number of training points, and it generalizes otherwise. Experiments across a range of datasets confirm our theoretically predicted location for the transition. We find that generation proceeds near the edge of memorization: both spatially local BIRD models and early-training diffusion models track the memorization-generalization phase boundary by increasingly restricting information over time. Overall, our results reveal a fundamental role for information restriction in generative AI to circumvent the curse of dimensionality.

## 3. AutoAnchor: Stable Diffusion Unlearning Using Cross-Attention as a Manifold Surrogate

- Authors: Siyuan Wen, Jiahao Zeng, Ningning Ding
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-09
- DOI: Unavailable
- Categories: cs.LG, stat.ML
- Relevance: 3.186459244039539
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.08337v1
- PDF: https://arxiv.org/pdf/2607.08337v1
- Local PDF: pdf/2026-07-11_03_AutoAnchor_ Stable Diffusion Unlearning Using Cross-Attention as a Manifold Surrogate.pdf

Diffusion unlearning is essential for mitigating the generation of harmful or copyrighted content in text-to-image models. Current diffusion unlearning techniques determine the model update direction by either using alternatives of the target concept as an anchor or using empty prompts. The anchor-based method relies on manually and semantically-chosen anchors that risk biased unlearning, while the anchor-free method inherently suffers from unrobust unlearning due to unconstrained latent updates. In this work, we theoretically formalize such unstable diffusion unlearning issues under the manifold hypothesis and prove that lacking a manifold-proximal anchor inevitably induces significant normal-space drift that degrades unlearning performance. To achieve stable unlearning, we propose \mysysn, a two-stage framework that automatically synthesizes manifold-proximal anchors. However, direct geometric manifold optimization is computationally intractable. To address this challenge, \mysys introduces a novel cross-attention consistency loss which serves as a highly efficient surrogate of manifold proximity. Experimental results demonstrate that \mysys effectively achieves robust and unbiased unlearning across various state-of-the-art baselines, significantly improving targeted concept removal (by up to 31.04\% in CLIP score) and non-target utility (by up to 4.18\% in CLIP score). Moreover, \mysys can also be easily integrated into existing diffusion unlearning methods to enhance their unlearning performance (by 6.30\% for concept removal and 6.65\% for utility on average).

## 4. Agentic Neural Architecture Search

- Authors: Seokhoon Jeong, Mijung Kim, Taehwan Kim
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-08
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 3.1577487640102095
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.07984v1
- PDF: https://arxiv.org/pdf/2607.07984v1
- Local PDF: pdf/2026-07-11_04_Agentic Neural Architecture Search.pdf

Neural architecture search (NAS) methods have grown increasingly efficient, yet they remain bounded by manually engineered search spaces that require substantial domain expertise and must be rebuilt for every new task. Large language models (LLMs) can generate architectures in an open-ended space, but how to optimally divide the labor between LLM-driven design and NAS-driven search remains unexplored. We propose a mechanism that bridges these two paradigms: an LLM produces a high-quality seed architecture, then decomposes it into a "slotted architecture", a scaffold with named, interchangeable module slots that automatically defines a bounded, task-specific search space for conventional NAS to explore, without manual engineering. We instantiate this mechanism in AgentNAS, a modular three-phase pipeline in which each component's contribution can be measured independently. On 17 tasks spanning classification, dense regression, segmentation, and multi-label tagging across diverse modalities (NAS-Bench-360 and Unseen NAS), AgentNAS establishes a new state of the art on 11 tasks, outperforming published baselines including task-specific expert designs. Ablation studies show that the two search mechanisms are broadly complementary: the LLM-generated seed already surpasses published baselines on the majority of tasks, and NAS delivers additional gains in most cases through combinatorial recombination across slots, a mode of search that independent LLM samples cannot replicate. These patterns hold across three LLMs of different capability levels, confirming that the division of labor is robust. Our code is available at https://github.com/alroimfebruary/AgentNAS.

## 5. StackingNet: Collective Inference Across Independent AI Foundation Models

- Authors: Siyang Li, Chenhao Liu, Dongrui Wu, Zhigang Zeng, Lieyun Ding
- Source: openalex
- Venue type: journal
- Journal: Advanced Science
- Publication status: published
- Publication date: 2026-07-09
- DOI: https://doi.org/10.1002/advs.76488
- Categories: Explainable Artificial Intelligence (XAI), Multimodal Machine Learning Applications, Domain Adaptation and Few-Shot Learning
- Relevance: 3.1357507849517785
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://doi.org/10.1002/advs.76488
- PDF: Unavailable
- Local PDF: Not downloaded

Artificial intelligence (AI) built on large foundation models has transformed language understanding, computer vision, and reasoning, yet these systems remain isolated and cannot readily share their capabilities. Coordinating the complementary strengths of independently developed, black-box foundation models is essential for trustworthy intelligent systems, yet no established method exists. Here we show that such coordination can be achieved through a meta-ensemble framework termed StackingNet, which aggregates the output predictions of independent models at inference. StackingNet improves accuracy, reduces individual-model error and group-wise disparities, ranks model reliability, and identifies or prunes models that degrade performance, all without access to internal parameters or training data. Across language comprehension, visual attribute estimation, and academic paper rating, it consistently outperforms individual models and classic ensembles, with gains that persist when the base models are uniformly strong. These gains stem from variance reduction and consensus alignment among independent models rather than from any emergent group cognition, and they widen as the model pool grows more diverse. By turning model diversity from a source of inconsistency into a resource for cooperation, StackingNet offers a practical path toward coordinated AI, where progress emerges not only from larger single models but from principled cooperation among many specialized ones.

## 6. Structured Pruning of Large Language Models via Power Transformation and Sign-Preserving Score Aggregation with Adaptive Feature Retention

- Authors: Ryota Kobayashi, Tsubasa Hirakawa, Takayoshi Yamashita, Hironobu Fujiyoshi, Yasunori Ishii, Tomoyuki Okuno, Kazuki Kozuka
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-09
- DOI: Unavailable
- Categories: cs.CL, cs.AI
- Relevance: 3.029877291821284
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.08027v1
- PDF: https://arxiv.org/pdf/2607.08027v1
- Local PDF: pdf/2026-07-11_06_Structured Pruning of Large Language Models via Power Transformation and Sign-Preserving Score Aggregation with Adaptive.pdf

This paper proposes an improved structured pruning method for large language models (LLMs) that addresses key challenges in adapting Adaptive Feature Retention (AFR), an unstructured pruning technique, to structured pruning. When applying AFR to structured pruning, three major problems arise: distribution mismatch between heterogeneous pruning scores, loss of sign information indicating optimization direction consistency, and influence of outliers. To address these issues, we propose a unified approach combining power transformation for nonlinear distribution alignment, sign-preserving score aggregation, and percentile-based outlier removal. Experiments on Llama-3-8B, Vicuna-v1.5-13B, and LLaVA-v1.5-13B demonstrate that our method maintains accuracy comparable to unstructured pruning while achieving practical inference speedup through structured pruning.

## 7. Reinforcing the Generation Order of Multimodal Masked Diffusion Models

- Authors: Yidong Ouyang, Zhe Wang, Sourav Bhabesh, Dmitriy Bespalov
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-09
- DOI: Unavailable
- Categories: cs.LG, cs.AI, stat.ML
- Relevance: 3.0202340082292745
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.08056v1
- PDF: https://arxiv.org/pdf/2607.08056v1
- Local PDF: pdf/2026-07-11_07_Reinforcing the Generation Order of Multimodal Masked Diffusion Models.pdf

Diffusion Language Models (DLMs) have recently achieved substantial progress in natural language generation tasks. Recent research demonstrates that adaptive token generation ordering can significantly improve performance in mathematical reasoning and code synthesis applications. In this work, we investigate the optimization of generation order for both text-to-image synthesis and multimodal understanding. We first establish that, unlike structured problems in language generation such as Sudoku puzzles, model logits alone are insufficient for determining optimal generation sequences in text-to-image generation and multimodal understanding. To address this challenge, we introduce a learnable control module trained via Group Relative Policy Optimization (GRPO) to determine the generation order. Our results demonstrate that learning this control block substantially improves both text-to-image alignment and multimodal understanding in DLMs. In particular, it enhances the model's ability to capture fine-grained spatial relationships in generated images while also strengthening performance on multimodal reasoning and comprehension tasks. We evaluate our framework on GenEval, an object-focused benchmark for text-to-image alignment, where it achieves 4.08% relative improvements. In addition, experiments on VLMEvalKit confirm 4.85% relative improvements in multimodal understanding, highlighting the broad effectiveness of our approach.

## 8. Joint estimation of high-dimensional spiked covariance matrices via a partially shared subspace

- Authors: Changwon Yoon, Minwoo Kim, Sungkyu Jung, Jeongyoun Ahn
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-09
- DOI: Unavailable
- Categories: stat.ME, stat.AP, stat.ML
- Relevance: 3.014697493862114
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.08123v1
- PDF: https://arxiv.org/pdf/2607.08123v1
- Local PDF: pdf/2026-07-11_08_Joint estimation of high-dimensional spiked covariance matrices via a partially shared subspace.pdf

Statistical analysis of high-dimensional data is often hampered by limited sample sizes, yet auxiliary datasets from related sources are often readily available. When two such datasets share part of their covariance structure, but not all of it, exploiting the shared part can substantially improve estimation. We propose a spiked covariance model that explicitly captures this partial sharing: two datasets share a subspace of unknown rank and arbitrary position in the spectrum, while each retains its own distinct spiked directions. The model treats the two datasets symmetrically and strictly generalizes existing models for shared covariance structure. We develop a complete estimation procedure that includes joint estimation of the shared subspace and its rank, a closed-form pooling weight for combining the two datasets, and asymptotic guarantees derived from random matrix theory in the proportional-growth regime. The framework also resolves a gap in contrastive dimension reduction by providing a principled estimator for high-dimensional settings. We illustrate the methodology on portfolio construction during the early COVID-19 pandemic and on contrastive analysis of brain tumor gene expression.

## 9. Game Theory Driven Multi-Agent Framework Mitigates Language Model Hallucination

- Authors: Runzhe Liu, Biquan Bie, Zihao Wang, Yuchao Ma, Yexin Liu, Xinghai Li, Harry Yang, Wenbo Yang, Jinzhe Cao, Shengyang Tao
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-09
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 3.0128092434743152
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.08403v1
- PDF: https://arxiv.org/pdf/2607.08403v1
- Local PDF: pdf/2026-07-11_09_Game Theory Driven Multi-Agent Framework Mitigates Language Model Hallucination.pdf

The application of lightweight Large Language Models in rule-based scientific domains remains severely limited by their tendency to mimic linguistic patterns rather than reproduce axiomatic reasoning, causing frequent hallucinations. Here, we show that G-Frame, an adaptive multi-agent framework integrating Bayesian and team game principles, establishes an automated closed-loop for high-quality data synthesis and model training. By forcing the internalization of domain constraints through structured reasoning, we synthesized a specialized corpus of 363,045 chains-of-thought and 199,589 question-answer pairs. The resulting 7B model OmniChem achieves performance parity with GPT 4o mini on custom benchmarks and ChemBench while exhibiting a 79.46% reduction in hallucinations relative to its base architecture. We further demonstrate the advanced capabilities of OmniChem in molecular design and synthesis planning. This work establishes a scalable paradigm utilizing adaptive multi-agents to overcome inherent reasoning deficiencies, offering a feasible pathway for accelerating knowledge discovery in specialized scientific fields.

## 10. MulVul: Retrieval-augmented Multi-Agent Code Vulnerability Detection via Cross-Model Prompt Evolution

- Authors: Zihan Wu, Jie Xu, Yun Peng, Chun Yong Chong, Xiaohua Jia
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.95024347637907
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.391/
- PDF: https://aclanthology.org/2026.acl-long.391.pdf
- Local PDF: pdf/2026-07-11_10_MulVul_ Retrieval-augmented Multi-Agent Code Vulnerability Detection via Cross-Model Prompt Evolution.pdf

Large Language Models (LLMs) struggle to automate real-world vulnerability detection due to two key limitations: the heterogeneity of vulnerability patterns undermines the effectiveness of a single unified model, and manual prompt engineering for massive weakness categories is unscalable.To address these challenges, we propose MulVul, a retrieval-augmented multi-agent framework designed for precise and broad-coverage vulnerability detection. MulVul adopts a coarse-to-fine strategy: a Router agent first predicts the top- coarse categories and then forwards the input to specialized Detector agents, which identify the exact vulnerability types. Both agents use evidence retrieved from vulnerability knowledge bases to mitigate hallucinations. Crucially, to automate the generation of specialized prompts, we design Cross-Model Prompt Evolution, a prompt optimization mechanism where a generator LLM iteratively refines candidate prompts while a distinct executor LLM validates their effectiveness. This decoupling mitigates the self-correction bias inherent in single-model optimization. Evaluated on 130 CWE types, MulVul achieves 34.79% Macro-F1, outperforming the best baseline by 41.5%. Ablation studies validate cross-model prompt evolution, which boosts performance by 51.6% over manual prompts by effectively handling diverse vulnerability patterns.

## 11. Pixel Reasoner: Incentivizing Pixel Space Reasoning via Curiosity-Driven Reinforcement Learning

- Authors: Su, Alex, Wang, Haozhe, Ren, Weiming, Lin, Fangzhen, Chen, Wenhu
- Source: neurips
- Venue type: conference
- Journal: NeurIPS 2025
- Publication status: formally_published
- Publication date: 2026-04-23
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.9494818058920877
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://proceedings.neurips.cc/paper_files/paper/2025/hash/0c38f54740062529aa4117a04b583f3c-Abstract-Conference.html
- PDF: https://proceedings.neurips.cc/paper_files/paper/2025/file/0c38f54740062529aa4117a04b583f3c-Paper-Conference.pdf
- Local PDF: pdf/2026-07-11_11_Pixel Reasoner_ Incentivizing Pixel Space Reasoning via Curiosity-Driven Reinforcement Learning.pdf

Chain-of-thought reasoning has significantly improved the performance of Large Language Models (LLMs) across various domains. However, this reasoning process has been confined exclusively to textual space, limiting its effectiveness in visually intensive tasks. To address this limitation, we introduce the concept of pixel-space reasoning. Within this novel framework, Vision-Language Models (VLMs) are equipped with a suite of visual reasoning operations, such as zoom-in and select-frame. These operations enable VLMs to directly inspect, interrogate, and infer from visual evidences, thereby enhancing reasoning fidelity for visual tasks. Cultivating such pixel-space reasoning capabilities in VLMs presents notable challenges, including the model’s initially imbalanced competence and its reluctance to adopt the newly introduced pixel-space operations. We address these challenges through a two-phase training approach. The first phase employs instruction tuning on synthesized reasoning traces to familiarize the model with the novel visual operations. Following this, a reinforcement learning (RL) phase leverages a curiosity-driven reward scheme to balance exploration between pixel-space reasoning and textual reasoning. With these visual operations, VLMs can interact with complex visual inputs, such as information-rich images or videos to proactively gather necessary information. We demonstrate that this approach significantly improves VLM performance across diverse visual reasoning benchmarks. Our 7B model, Pixel-Reasoner, achieves 84% on V* bench, 74% on TallyQA-Complex, and 84% on InfographicsVQA, marking the highest accuracy achieved by any open-source model to date. These results highlight the importance of pixel-space reasoning and the effectiveness of our framework.

## 12. Lil: Less is Less When Applying Post-Training Sparse-Attention Algorithms in Long-Decode Stage

- Authors: Junhao Hu, Fangze Li, Mingtao Xu, Feifan Meng, Shiju Zhao, Tiancheng Hu, Ting Peng, Anmin Liu, Wenrui Huang, Chenxu Liu, Ziyue Hua, Tao Xie
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.948912418460078
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.91/
- PDF: https://aclanthology.org/2026.findings-acl.91.pdf
- Local PDF: pdf/2026-07-11_12_Lil_ Less is Less When Applying Post-Training Sparse-Attention Algorithms in Long-Decode Stage.pdf

Large language models (LLMs) demonstrate strong capabilities across a wide range of complex tasks and are increasingly deployed at scale, placing significant demands on inference efficiency. Prior work typically decomposes inference into prefill and decode stages, with the decode stage dominating total latency. To reduce time and memory complexity in the decode stage, a line of work introduces sparse-attention algorithms. In this paper, we show, both empirically and theoretically, that sparse attention can paradoxically increase end-to-end complexity: information loss often induces significantly longer sequences, a phenomenon we term “Less is Less” (Lil). To mitigate the Lil problem, we propose an early-stopping algorithm that detects the threshold where information loss exceeds information gain during sparse decoding. Our early-stopping algorithm reduces token consumption by up to 90% with a marginal accuracy degradation of less than 2% across reasoning-intensive benchmarks.

## 13. Enhanced Reasoning for Biomedical Document-Level Relation Extraction via a Novel Cascade Language Model Framework

- Authors: Haohua Song, Wenhao Gu, Zhijing Li, Yunwenyu, Tiantian Zhu, Xiao Yang, Zexuan Zhu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.948909202474754
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1517/
- PDF: https://aclanthology.org/2026.acl-long.1517.pdf
- Local PDF: pdf/2026-07-11_13_Enhanced Reasoning for Biomedical Document-Level Relation Extraction via a Novel Cascade Language Model Framework.pdf

Biomedical document-level relation extraction poses significant challenges beyond sentence-level tasks, as it necessitates the integration of evidence from entire documents and the ability for coherent cross-sentence reasoning. While pretrained language models (PLMs) demonstrate efficiency in handling local contexts, they often struggle with global dependency modeling. Conversely, large language models (LLMs) exhibit strong reasoning capabilities but tend to generate hallucinations in knowledge-intensive biomedical domains. This paper introduces CoRE, a novel cascade framework that leverages the complementary strengths of PLMs and LLMs through a detect-then-rethink paradigm. The PLM serves as an efficient detector for high-confidence relations, while challenging cases are forwarded to an LLM enhanced with semantic retrieval and iterative reasoning mechanisms. Experimental results on BioRED and CDR datasets show that CoRE achieves substantial improvements over state-of-the-art baselines, validating the effectiveness of the proposed cascade paradigm for complex biomedical relation extraction.

## 14. A Survey of Reinforcement Learning for Large Language Models under Data Scarcity: Challenges and Solutions

- Authors: Zhiyin Yu, Yuchen Mou, Juncheng Yan, Junyu Luo, Chunchun Chen, Xing Wei, Yunhui Liu, Hongru Sun, Yuxing Zhang, Jun Xu, Yatao Bian, Ming Zhang, Wei Ye, Tieke He, Jie Yang, Guanjie Zheng, Zhonghai Wu, Bo Zhang, Lei Bai, Xiao Luo
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.948776977768674
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1045/
- PDF: https://aclanthology.org/2026.acl-long.1045.pdf
- Local PDF: pdf/2026-07-11_14_A Survey of Reinforcement Learning for Large Language Models under Data Scarcity_ Challenges and Solutions.pdf

Reinforcement learning (RL) has emerged as a powerful post-training paradigm for enhancing the reasoning capabilities of large language models (LLMs). However, reinforcement learning for LLMs faces substantial data scarcity challenges, including the limited availability of high-quality external supervision and the constrained volume of model-generated experience. These limitations make data-efficient reinforcement learning a critical research direction. In this survey, we present the first systematic review of reinforcement learning for LLMs under data scarcity. We propose a bottom-up hierarchical framework built around three complementary perspectives: the data-centric perspective, the training-centric perspective, and the framework-centric perspective. We develop a taxonomy of existing methods, summarize representative approaches in each category, and analyze their strengths and limitations. Our taxonomy aims to provide a clear conceptual foundation for understanding the design space of data-efficient RL for LLMs and to guide researchers working in this emerging area. We hope this survey offers a comprehensive roadmap for future research and inspires new directions toward more efficient and scalable reinforcement learning post-training for LLMs.

## 15. Share Your Attention: Transformer Weight Sharing via Matrix-based Dictionary Learning

- Authors: Magauiya Zhussip, Dmitriy Shopkhoev, Ammar Ali, Stamatios Lefkimmiatis
- Source: openalex
- Venue type: conference
- Journal: Proceedings of the AAAI Conference on Artificial Intelligence
- Publication status: formally_published
- Publication date: 2026-03-14
- DOI: https://doi.org/10.1609/aaai.v40i34.40165
- Categories: Advanced Neural Network Applications, Big Data and Digital Economy, Domain Adaptation and Few-Shot Learning
- Relevance: 2.9486359877284674
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://doi.org/10.1609/aaai.v40i34.40165
- PDF: https://ojs.aaai.org/index.php/AAAI/article/download/40165/44126
- Local PDF: Not downloaded

Large language models (LLMs) have revolutionized AI applications, yet their high computational and memory demands hinder their widespread deployment. Existing compression techniques focus on intra-block optimizations (e.g., low-rank approximation or attention head pruning), while the repetitive layered structure of transformers implies significant inter-block redundancy - a dimension largely unexplored beyond key-value (KV) caching. Inspired by dictionary learning in convolutional networks, we propose a framework for structured weight sharing across transformer layers. Our approach decomposes attention projection matrices (Q, K, V, O) into shared dictionary atoms, reducing the attention module's parameters by 66.7% (e.g., 226.5M -&gt; 75M in a 700M-parameter model) while achieving on-par performance. Unlike complex methods requiring distillation or architectural changes, MASA (Matrix Atom Sharing in Attention) operates as a drop-in replacement - trained with standard optimizers - and represents each layer's weights as linear combinations of shared matrix atoms. Experiments across scales (100M-700M parameters) show that MASA achieves better benchmark accuracy and perplexity than grouped-query attention (GQA), low-rank baselines and recently proposed Repeat-all-over/Sequential sharing at comparable parameter budgets. Ablation studies confirm robustness to the dictionary size and the efficacy of shared representations in capturing cross-layer statistical regularities. Extending to Vision Transformers (ViT), MASA matches performance metrics on image classification tasks with 66.7% fewer attention parameters. By combining dictionary learning strategies with transformer efficiency, MASA offers a scalable blueprint for parameter-efficient models without sacrificing performance. Finally, we investigate the possibility of employing MASA on large pretrained models to reduce their number of parameters without experiencing any significant drop in their performance.

## 16. CheMM-R1: Enhancing Chemical Structure Recognition and Elucidation with Reasoning Multimodal Large Language Models

- Authors: Liting Huang, Zhihao Zhang, Shoujin Wang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.9480561156775185
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1341/
- PDF: https://aclanthology.org/2026.findings-acl.1341.pdf
- Local PDF: pdf/2026-07-11_16_CheMM-R1_ Enhancing Chemical Structure Recognition and Elucidation with Reasoning Multimodal Large Language Models.pdf

While Multimodal Large Language Models (MLLMs) demonstrate strong reasoning capabilities, they lack domain-specific expertise to effectively perform chemical tasks. For example, existing MLLMs struggle with both the lower-level task of molecular structure recognition and the higher-level task of chemical spectral data elucidation. When faced with complex molecular structures and multimodal chemical data (including spectral images and texts), they often fail to provide reliable inference, resulting in poor performance. Moreover, there are no benchmark datasets for evaluating multi-step multimodal reasoning capacities in the chemistry domain. To this end, we establish CheMM-Bench, a comprehensive benchmark dataset with 48,500 reasoning steps across four chemical tasks (SmilesQA, IupacQA, MwQA, SpectraQA) for evaluating visual reasoning in both molecular structure recognition and spectral analysis. On top of this, we present CheMM-R1, a state-of-the-art chemistry-specific MLLM trained with CheMMGRPO, a novel adaptation of Group Relative Policy Optimisation tailored for chemical reasoning. CheMMGRPO employs domain-specific reward functions to assess chemical validity, structural accuracy, format compliance, and factual correctness. CheMM-R1 surpasses leading proprietary models (GPT-o3, Gemini-2.5-Pro, Claude-3.5-Sonnet, and Grok-2) across all CheMM-Bench tasks. The evaluation code and model are publicly available.

## 17. CondenseFlow: Scalable Latent Space Collaboration via Semantic Compression for Multi-Agent Systems

- Authors: Xiaoyu Chen, Fengge Wu, Zhao Junsuo, Yun Fan
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.947871107775022
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.669/
- PDF: https://aclanthology.org/2026.findings-acl.669.pdf
- Local PDF: pdf/2026-07-11_17_CondenseFlow_ Scalable Latent Space Collaboration via Semantic Compression for Multi-Agent Systems.pdf

Full-state latent communication in LLM-based multi-agent systems offers richer semantics than text but suffers from memory overhead scaling linearly with collaboration rounds. We propose CondenseFlow , which introduces the Latent Thought Condenser (LTC) —a lightweight module using learnable semantic probes to compress KV caches into fixed-size representations, achieving 𝒪(1) communication complexity regardless of context length. We theoretically prove that compression error is bounded by attention concentration and accumulates controllably across rounds. On seven benchmarks spanning six models, CondenseFlow reduces KV cache memory by over 99% and inference latency by approximately 20% compared to dense transfer with negligible accuracy degradation, while outperforming text-based methods by 1.7 percentage points on average across all configurations. Code is available at https://github.com/xxy33/condenseflow.

## 18. Beyond Task-Level Context: Class-Conditional Context Vectors for Implicit In-Context Learning

- Authors: Jianxin Zhang, Yilu Hu, Teng Liu, Pei Guo, Juntao Li
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.9478435295889605
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1527/
- PDF: https://aclanthology.org/2026.findings-acl.1527.pdf
- Local PDF: pdf/2026-07-11_18_Beyond Task-Level Context_ Class-Conditional Context Vectors for Implicit In-Context Learning.pdf

Implicit In-Context Learning compresses demonstration examples into a single context vector and injects it into the model’s activation space, achieving few-shot-level performance at near zero-shot inference cost. However, existing approaches typically aggregate demonstrations from all classes into a shared, task-level context vector, capturing global task information but without explicitly preserving fine-grained, class-conditional semantic distinctions. In this work, we propose Class-Conditional Context Vectors (C3V), a simple yet effective extension to implicit in-context learning that explicitly models class-specific contextual information by constructing separate context vectors for each class, without relying on explicit prompts. These class-conditional context vectors are additively injected into the model’s residual streams in a single forward pass, enabling contextual contributions to be modulated in a class-aware manner while keeping the backbone frozen. We evaluate C3V on multiple text classification benchmarks across several families of large language models. Experimental results demonstrate that C3V consistently outperforms task-level context vector baselines, and achieves higher average accuracy than conventional few-shot learning on most models.

## 19. Latent-Condensed Transformer for Efficient Long Context Modeling

- Authors: Zeng You, Yaofo Chen, Qiuwu Chen, Ying Sun, Shuhai Zhang, Yingjian Li, Yaowei Wang, Mingkui Tan
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.9471896646931137
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1176/
- PDF: https://aclanthology.org/2026.acl-long.1176.pdf
- Local PDF: pdf/2026-07-11_19_Latent-Condensed Transformer for Efficient Long Context Modeling.pdf

Large language models (LLMs) face significant challenges in processing long contexts due to the linear growth of the key-value (KV) cache and quadratic complexity of self-attention. Existing approaches address these bottlenecks separately: Multi-head Latent Attention (MLA) reduces the KV cache by projecting tokens into a low-dimensional latent space, while sparse attention reduces computation. However, sparse methods cannot operate natively on MLA’s compressed latent structure, missing opportunities for joint optimization. In this paper, we propose Latent-Condensed Attention (LCA), which directly condenses context within MLA’s latent space, where the representation is disentangled into semantic latent vectors and positional keys. LCA separately aggregates semantic vectors via query-aware pooling and preserves positional keys via anchor selection. This approach jointly reduces both computational cost and KV cache without adding parameters. Beyond MLA, LCA’s design is architecture-agnostic and readily extends to other attention mechanisms such as GQA. Theoretically, we prove a length-independent error bound. Experiments show LCA achieves up to **2.5×** prefilling speedup and **90%** KV cache reduction at 128K context while maintaining competitive performance.

## 20. Glyph: Scaling Context Windows via Visual-Text Compression

- Authors: Jiale Cheng, Yusen Liu, Xinyu Zhang, Yulin Fei, Wenyi Hong, Ruiliang Lyu, Weihan Wang, Zhe Su, Xiaotao Gu, Xiao Liu, Yushi Bai, Jie Tang, Hongning Wang, Minlie Huang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.947120701353936
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1722/
- PDF: https://aclanthology.org/2026.acl-long.1722.pdf
- Local PDF: pdf/2026-07-11_20_Glyph_ Scaling Context Windows via Visual-Text Compression.pdf

Large language models (LLMs) conventionally represent text as sequences of discrete tokens, making long-context scaling largely a matter of processing more tokens more efficiently.We instead explore a complementary direction: increasing how much original context each token represents.To this end, we introduce Glyph, a framework that renders long texts into compact visual pages and processes them with a vision-language model (VLM), allowing a fixed context window to cover substantially more text.To make visual compression practical, Glyph combines continual pre-training on rendered long-text data, an LLM-driven genetic search to identify rendering configurations that balance compression and task performance, and post-training with supervised fine-tuning and reinforcement learning.Across multiple long-context benchmarks, Glyph achieves 3–4× token compression while maintaining performance comparable to strong text-only LLMs such as Qwen3-8B, with over 4× faster prefilling and decoding and 2× faster supervised fine-tuning.Under more aggressive compression, a VLM with a 128K context window can handle tasks that would otherwise require up to 1M input tokens.Our code and model are released at https://github.com/thu-coai/Glyph.

## 21. RoMA: Scaling up Mamba-based Foundation Models for Remote Sensing

- Authors: Wang, Fengxiang, Wang, Yulin, Chen, Mingshuo, Wang, Haotian, Wang, Hongzhen, Zhao, Haiyan, Sun, Yangang, Wang, Shuo, Wang, Di, Lan, Long, Yang, Wenjing, Zhang, Jing
- Source: neurips
- Venue type: conference
- Journal: NeurIPS 2025
- Publication status: formally_published
- Publication date: 2026-04-23
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.946768155873347
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://proceedings.neurips.cc/paper_files/paper/2025/hash/065c00e902f3f0117d1a4da0a9b0e497-Abstract-Conference.html
- PDF: https://proceedings.neurips.cc/paper_files/paper/2025/file/065c00e902f3f0117d1a4da0a9b0e497-Paper-Conference.pdf
- Local PDF: pdf/2026-07-11_21_RoMA_ Scaling up Mamba-based Foundation Models for Remote Sensing.pdf

Recent advances in self-supervised learning for Vision Transformers (ViTs) have fueled breakthroughs in remote sensing (RS) foundation models. However, the quadratic complexity of self-attention poses a significant barrier to scalability, particularly for large models and high-resolution images. While the linear-complexity Mamba architecture offers a promising alternative, existing RS applications of Mamba remain limited to supervised tasks on small, domain-specific datasets. To address these challenges, we propose RoMA, a framework that enables scalable self-supervised pretraining of Mamba-based RS foundation models using large-scale, diverse, unlabeled data. RoMA enhances scalability for high-resolution images through a tailored auto-regressive learning strategy, incorporating two key innovations: 1) a rotation-aware pretraining mechanism combining adaptive cropping with angular embeddings to handle sparsely distributed objects with arbitrary orientations, and 2) multi-scale token prediction objectives that address the extreme variations in object scales inherent to RS imagery. Systematic empirical studies validate that Mamba adheres to RS data and parameter scaling laws, with performance scaling reliably as model and data size increase. Furthermore, experiments across scene classification, object detection, and semantic segmentation tasks demonstrate that RoMA-pretrained Mamba models consistently outperform ViT-based counterparts in both accuracy and computational efficiency. The source code and pretrained models have be released at https://github.com/MiliLab/RoMA.

## 22. Markovian Linguistic-Temporal Bridge: Unlocking the Potential of LLMs for Time Series Forecasting

- Authors: Siming Sun, Kai Zhang, Xuejun Jiang, Wenchao Meng, Qinmin Yang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.9462382172595976
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1014/
- PDF: https://aclanthology.org/2026.acl-long.1014.pdf
- Local PDF: pdf/2026-07-11_22_Markovian Linguistic-Temporal Bridge_ Unlocking the Potential of LLMs for Time Series Forecasting.pdf

Adapting pretrained Large Language Models (LLMs) for time series forecasting primarily relies on token-level linguistic-temporal alignment, leading to the stacking of logically disjointed tokens as input. While empirically effective, these methods overlook a fundamental capability of LLMs: modeling linguistic logic and structure, rather than merely processing token features. To address this limitation, we propose the M arkovian- G uided S tructure- A ware A lignment ( MGSAA ). Our core contribution is a framework that transcends pointwise feature matching to achieve global structural isomorphism between the linguistic and temporal domains. Specifically, MGSAA distills latent evolutionary patterns of language within LLMs into a Markovian state transition graph, which is transferred as a structural prior to the time series domain. Under this prior, time series patches are decoded into latent states and then aligned via state-constrained cross-attention. Ultimately, MGSAA generates a token sequence topologically isomorphic to the LLM’s inherent mental structure, reactivating its reasoning capabilities for forecasting. Comprehensive evaluations across multiple benchmarks demonstrate that MGSAA achieves state-of-the-art performance, providing an innovative solution for cross-modal alignment in LLM for time series forecasting. Code is available at https://github.com/sunzju/MGSAA.

## 23. Multimodal DeepResearcher: Generating Text-Chart Interleaved Reports from Scratch with Agentic Framework

- Authors: Zhaorui Yang, Bo Pan, Han Wang, Yiyao Wang, Xi Liu, Luoxuan Weng, Yingchaojie Feng, Haozhe Feng, Minfeng Zhu, Bo Zhang, Weiqiu Chen
- Source: openalex
- Venue type: conference
- Journal: Proceedings of the AAAI Conference on Artificial Intelligence
- Publication status: formally_published
- Publication date: 2026-03-14
- DOI: https://doi.org/10.1609/aaai.v40i40.40734
- Categories: Data Visualization and Analytics, Multimodal Machine Learning Applications, Computational and Text Analysis Methods
- Relevance: 2.9449313289894
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://doi.org/10.1609/aaai.v40i40.40734
- PDF: Unavailable
- Local PDF: Not downloaded

Visualizations play a crucial part in effective communication of concepts and information. Recent advances in reasoning and retrieval augmented generation have enabled Large Language Models (LLMs) to perform deep research and generate comprehensive reports. Despite its progress, existing deep research frameworks primarily focus on generating text-only content, leaving the automated generation of interleaved texts and visualizations underexplored. This novel task poses key challenges in designing informative visualizations and effectively integrating them with text reports. To address these challenges, we propose Formal Description of Visualization (FDV), a structured textual representation of charts that enables LLMs to learn from and generate diverse, high-quality visualizations. Building on this representation, we introduce Multimodal DeepResearcher, an agentic framework that decomposes the task into four stages: (1) researching, (2) exemplar report textualization, (3) planning and (4) multimodal report generation. For the evaluation of the generated reports, we develop MultimodalReportBench which contains 100 diverse topics as inputs, and a set of dedicated metrics for report and chart evaluation. Extensive experiments across models and evaluation methods demonstrate the effectiveness of Multimodal DeepResearcher. Notably, utilizing the same Claude 3.7 Sonnet model, Multimodal DeepResearcher achieves an 82% overall win rate over the baseline method.

## 24. Reason in Chains, Learn in Trees: Self-Rectification and Grafting for Multi-turn Agent Policy Optimization

- Authors: Yu Li, Sizhe Tang, Tian Lan
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.9446702910316294
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.229/
- PDF: https://aclanthology.org/2026.findings-acl.229.pdf
- Local PDF: pdf/2026-07-11_24_Reason in Chains, Learn in Trees_ Self-Rectification and Grafting for Multi-turn Agent Policy Optimization.pdf

Reinforcement learning for Large Language Model agents is often hindered by sparse rewards in multi-step reasoning tasks. Existing approaches like Group Relative Policy Optimization treat sampled trajectories as independent chains, assigning uniform credit to all steps in each chain and ignoring the existence of critical steps that may disproportionally impact reasoning outcome. In this paper, we propose T-STAR(Tree-structured Self-Taught Agent Rectification), a framework that recovers the latent correlated reward structure across seemingly independent trajectories. Specifically, we consolidate trajectories into a unified Cognitive Tree by identifying and merging functionally similar steps/nodes. It enables an Introspective Valuation mechanism that back-propagates trajectory-level rewards through the tree to obtain a new notion of variance-reduced relative advantage at step-level. Using the Cognitive Tree, we also develop In-Context Thought Grafting to synthesize corrective reasoning by contrasting successful and failed branches at critical divergence points/steps. Our proposed Surgical Policy Optimization then capitalizes on the rich policy gradient information concentrated at these critical points/steps through a Bradley-Terry type of surgical loss. Extensive experiments across embodied, interactive, reasoning, and planning benchmarks demonstrate that T-STAR achieves consistent improvements over strong baselines, with gains most pronounced on tasks requiring extended reasoning chains.

## 25. CaRL-EM: Cost-Aware Reinforcement Learning for Entity Matching with LLMs

- Authors: Chaohui Guo, Michel C. A. Klein, Zhisheng Huang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.9433459535628654
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1258/
- PDF: https://aclanthology.org/2026.acl-long.1258.pdf
- Local PDF: pdf/2026-07-11_25_CaRL-EM_ Cost-Aware Reinforcement Learning for Entity Matching with LLMs.pdf

Entity matching (EM) requires fine-grained contextual understanding and domain knowledge. Recent work shows that large language models (LLMs) can serve as strong matchers across domains, but most methods either make independent pairwise decisions or rely on manually designed composite pipelines, thus lacking flexibility in realistic multi-candidate settings. At the same time, they typically ignore inference cost at scale. We formulate LLM-based EM with candidates as a cost-aware sequential decision problem and propose CaRL-EM, a reinforcement learning controller that manages LLM operations. Given the state of an anchor record, its candidate set, and the cost, CaRL-EM adaptively chooses among different operators (Match/Compare/Select/Decide) and model capacities to maximize a quality–cost objective. The policy interacts with abstract operators, allowing the same controller to be reused with different underlying LLM backends at inference time without retraining. Experiments on 7 benchmarks show that CaRL-EM (i) learns to dynamically plan the usage of inexpensive and expensive operators based on task complexity, (ii) achieves robust zero-shot transfer across diverse datasets and domains, and (iii) consistently achieves a better quality–cost trade-off than strong LLM-based baselines and manually designed pipelines, yielding a lower inference cost at comparable or higher quality.

## 26. EverMemOS: A Self-Organizing Memory Operating System for Structured Long-Horizon Reasoning

- Authors: Chuanrui Hu, Xingze Gao, Zuyi Zhou, Dannong Xu, Yi Bai, Xintong Li, Hui Zhang, Tong Li, Chong Zhang, Lidong Bing, Yafeng Deng
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.94308343627516
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.2125/
- PDF: https://aclanthology.org/2026.acl-long.2125.pdf
- Local PDF: pdf/2026-07-11_26_EverMemOS_ A Self-Organizing Memory Operating System for Structured Long-Horizon Reasoning.pdf

Large Language Models (LLMs) are increasingly deployed as long-term interactive agents, yet their limited context windows make it difficult to sustain coherent behavior over extended interactions. Existing memory systems for LLMs often store isolated records and retrieve fragments, limiting their ability to consolidate evolving experience and resolve conflicts. We introduce EverMemOS, a self-organizing memory operating system that implements an engram-inspired lifecycle for computational memory. First, Episodic Trace Formation converts dialogue streams into MemCells that capture episodic traces, atomic facts, and time-bounded foresight. Second, Semantic Consolidation organizes MemCells into thematic MemScenes, distilling stable semantic structures and updating user profiles. Finally, Reconstructive Recollection performs MemScene-guided agentic retrieval to compose the necessary and sufficient context for downstream reasoning. Experiments on LoCoMo, LongMemEval, and PersonaMem-v2 show that EverMemOS significantly outperforms state-of-the-art methods on memory-augmented reasoning tasks.

## 27. A Survey of Reasoning-Intensive Retrieval: Progress and Challenges

- Authors: Yiyang Wei, Tingyu Song, Siyue Zhang, Yilun Zhao
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.9429794679567713
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1949/
- PDF: https://aclanthology.org/2026.acl-long.1949.pdf
- Local PDF: pdf/2026-07-11_27_A Survey of Reasoning-Intensive Retrieval_ Progress and Challenges.pdf

Reasoning-Intensive Retrieval (RIR) targets retrieval settings where relevance is mediated by latent inferential links between a query and supporting evidence, rather than semantic similarity. Motivated by the emergent reasoning abilities of Large Language Models (LLMs), recent work integrates these capabilities into the IR field, spanning the entire pipeline from benchmarks to retrievers and rerankers. Despite this progress, the field lacks a systematic framework to organize current efforts and articulate a clear path forward. To provide a clear roadmap for this rapidly growing yet fragmented area, this survey (1) systematizes existing RIR benchmarks by knowledge domains and modalities, providing a detailed analysis of the current landscape; (2) introduces a structured taxonomy that categorizes methods based on where and how reasoning is integrated into the retrieval pipeline, alongside an analysis of their trade-offs and practical applications; and (3) summarizes challenges and future directions to guide research in this evolving field.

## 28. Octopus: Gated Selective Attention for Memory-Bounded Long-Context Inference in Large Language Models

- Authors: Chien Van Nguyen, Ryan A. Rossi, Linh Ngo Van, Franck Dernoncourt, Thien Huu Nguyen
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.9429185908831537
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1631/
- PDF: https://aclanthology.org/2026.acl-long.1631.pdf
- Local PDF: pdf/2026-07-11_28_Octopus_ Gated Selective Attention for Memory-Bounded Long-Context Inference in Large Language Models.pdf

Transformer inference becomes increasingly memory-bound as the Key–Value (KV) cache grows linearly with sequence length. While subquadratic architectures offer constant-memory inference, they rely on aggressive state compression that degrades performance on complex reasoning tasks. We propose Octopus, a framework that confers fixed-memory inference onto pretrained Transformers without the information loss of linearization. Octopus retrofits attention layers with Gated Selective Attention, a learnable module that enforces an adaptive sparsity policy over the context history. By dynamically scoring and retaining only high-utility KV states, this mechanism transforms the unbounded cache into a compact, evolving memory budget that filters out uninformative noise. Empirically, on the GSM8K benchmark, it outperforms state-of-the-art linearized baselines by over 36 points under identical memory constraints. Remarkably, Octopus also surpasses its own full-cache teacher, demonstrating that learned sparse retention serves as an effective regularizer for long-horizon reasoning.

## 29. LoopTool: Closing the Data–Training Loop for Robust LLM Tool Calls

- Authors: Kangning Zhang, Weiwen Liu, Wenxiang Jiao, Kounianhua Du, Yuan Lu, Weinan Zhang, Yong Yu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.942204781810559
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.968/
- PDF: https://aclanthology.org/2026.acl-long.968.pdf
- Local PDF: pdf/2026-07-11_29_LoopTool_ Closing the Data–Training Loop for Robust LLM Tool Calls.pdf

Augmenting Large Language Models (LLMs) with external tools enables them to execute complex, multi-step tasks. However, tool learning is hampered by the static synthetic data pipelines, where data generation and model training are executed as two separate, non-interactive processes. This approach fails to focus on the model’s specific weaknesses adaptively and allows noisy labels to persist, degrading training efficiency. We introduce LoopTool , a fully automated, model-aware data evolution framework that closes this loop by tightly integrating data synthesis and model training. LoopTool iteratively evolves both the data and the model through three synergistic modules: (1) Greedy Capability Probing (GCP) diagnoses the model’s mastered and failed capabilities; (2) Judgement-Guided Label Verification (JGLV) uses an open-source judge model to find and correct annotation errors, progressively purifying the dataset; and (3) Error-Driven Data Expansion (EDDE) generates new, challenging samples based on identified failures. This closed-loop process is tightly integrated with reinforcement learning training and operates within a cost-efficient, open-source ecosystem, thereby eliminating reliance on costly APIs. Experiments show that LoopTool-8B significantly surpasses its 32B data generator and achieves new state-of-the-art results on the BFCL-v3 and ACEBench benchmarks for its scale. Our work demonstrates that closed-loop, self-refining data pipelines can dramatically enhance the tool-use capabilities of LLMs.

## 30. RetentiveKV: State-Space Memory for Uncertainty-Aware Multimodal KV Cache Eviction

- Authors: Sihao Liu, YuFan Xiong, Zhonghua Jiang, Zhaode Wang, Chengfei lv, Shengyu Zhang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.9421166094656432
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.934/
- PDF: https://aclanthology.org/2026.findings-acl.934.pdf
- Local PDF: pdf/2026-07-11_30_RetentiveKV_ State-Space Memory for Uncertainty-Aware Multimodal KV Cache Eviction.pdf

Multimodal Large Language Models face severe challenges in computational efficiency and memory consumption due to the substantial expansion of the visual KV cache when processing long visual contexts. Existing KV cache compression methods typically rely on the "persistence of importance" hypothesis to prune tokens. However, this approach proves fragile in multimodal settings due to two key issues: 1) Visual tokens display "deferred importance," initially exhibiting low salience but becoming pivotal during later decoding, which can lead to premature eviction. 2) Discrete pruning disrupts the inherent spatial continuity of visual cues. To address these challenges, we propose RetentiveKV, an entropy-driven KV cache optimization method that reformulates KV eviction from "discrete context truncation" to "continuous memory evolution" based on State Space Models. Our method leverages information entropy to quantify the information potential of low-attention tokens and integrates tokens scheduled for eviction into a continuous state space through entropy-guided state transitions, enabling their dynamic reactivation when semantic relevance arises during subsequent decoding. Extensive experiments on multimodal benchmarks demonstrate that RetentiveKV achieves 5.0 × KV cache compression and 1.5 × decoding acceleration.
