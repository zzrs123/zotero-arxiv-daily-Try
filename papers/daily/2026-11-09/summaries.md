# Paper Daily Reading - 2026-11-09

## 1. Retrospective single cell lineage tracing with highly mutable homopolymers

- Authors: Pin-Chung Cheng, Dmitrii Kamenev, Polina Kameneva, Conor Fitzpatrick, Igor I. Adameyko, Peter V. Kharchenko, Kun Zhang
- Source: openalex
- Venue type: journal
- Journal: Nature Communications
- Publication status: published
- Publication date: 2026-11-07
- DOI: https://doi.org/10.1038/s41467-026-79104-5
- Categories: Single-cell and spatial transcriptomics, Cancer Genomics and Diagnostics, Epigenetics and DNA Methylation
- Relevance: 2.721474977197573
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://doi.org/10.1038/s41467-026-79104-5
- PDF: Unavailable
- Local PDF: Not downloaded

Abstract Retrospective reconstruction of cell lineages from somatic mutations holds substantial promise for understanding development, tissue homeostasis, and disease. Yet, current approaches are often constrained by low marker density, technical noise, and incomplete molecular readouts that limit the resolution and accuracy of inferred lineages. Here, we present RETrace2, a single-cell dual-omic method for simultaneous lineage tracing and cell-type identification. By identifying and targeting highly mutable homopolymers, which we show are approximately twice as informative as conventional microsatellite repeats, combined with technical improvements to increase marker coverage and reduce experimental errors of reading and amplifying homopolymers, RETrace2 can trace lineage continuously at an estimated resolution of fewer than five cell divisions in microsatellite-unstable organisms. Simultaneously, sparse methylation profiles were obtained from the same cells for cell-type identification. We validated the method using in vitro ground-truth models and demonstrated its utility in vivo by reconstructing multi-organ lineage trees from the brain, kidney and liver of Msh2 -deficient mice.

## 2. LiveLongBench: Tackling Long-Context Understanding for Spoken Texts from Live Streams

- Authors: Yongxuan Wu, Runyu Chen, Peiyu Liu, Hongjin Qian
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.5785679560897465
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1485/
- PDF: https://aclanthology.org/2026.findings-acl.1485.pdf
- Local PDF: pdf/2026-11-09_02_LiveLongBench_ Tackling Long-Context Understanding for Spoken Texts from Live Streams.pdf

Long-context understanding poses significant challenges in natural language processing, particularly for real-world dialogues characterized by high redundancy and uneven information density. Although large language models (LLMs) achieve impressive results on existing benchmarks, these datasets fail to reflect the complexities of such texts, limiting their applicability to practical scenarios. To bridge this gap, we construct the first spoken long-text dataset, derived from live streams, designed to reflect the redundancy-rich and conversational nature of real-world scenarios. We construct tasks in three categories: retrieval, reasoning, and hybrid tasks. We then evaluate both popular LLMs and specialized methods to assess their ability to understand long contexts in these tasks. Our results show that current methods exhibit strong task-specific preferences and perform poorly on highly redundant inputs, with no single method consistently outperforming others. We propose a new baseline that better handles redundancy in spoken text and achieves strong performance across tasks. Our findings highlight key limitations of current methods and suggest future directions for improving long-context understanding. Finally, our benchmark fills a gap in evaluating long-context spoken language understanding and provides a practical foundation for developing real-world e-commerce systems. The code and benchmark are available at https://github.com/Yarayx/livelongbench .

## 3. Meeseeks: A Feedback-Driven, Iterative Self-Correction Benchmark evaluating LLMs’ Instruction Following Capability

- Authors: Jiaming Wang, Yunke Zhao, Peng Ding, Jun Kuang, Yibin Shen, Zhe Tang, Yilin Jin, ZongYu Wang, Xiaoyu Li, Xuezhi Cao
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.5714581441713653
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.725/
- PDF: https://aclanthology.org/2026.findings-acl.725.pdf
- Local PDF: pdf/2026-11-09_03_Meeseeks_ A Feedback-Driven, Iterative Self-Correction Benchmark evaluating LLMs’ Instruction Following Capability.pdf

The capability to precisely adhere to instructions is a cornerstone for Large Language Models (LLMs) to function as dependable agents in real-world scenarios. However, confronted with complex prompts, LLMs frequently encounter difficulties in fulfilling all specified requirements within a single response. Drawing inspiration from recent advancements in Chain-of-Thought (CoT) prompting and self-correction methodologies, we introduce Meeseeks, a fully automated iterative instruction-following benchmark equipped with an integrated feedback mechanism. Meeseeks identifies erroneous components in model responses and provides corresponding feedback accurately, thereby iteratively guiding the model toward self-correction. The dataset contains over 700 curated instances annotated by 32 distinct capability tags in Chinese and English. Extensive experimental results reveal that different state-of-the-art commercial and open-source LLMs exhibit vastly disparate performance, and even after 20 turns of iterative feedback-driven self-correction, nearly all models demonstrate suboptimal performance. We conducted comprehensive analysis and uncovered numerous common issues prevalent in current state-of-the-art models, as well as several counterintuitive phenomena. Meeseeks has been open-sourced on https://github.com/ADoublLEN/Meeseeks .

## 4. Can AI Be a Good Peer Reviewer? A Survey of Peer Review Process, Evaluation, and the Future

- Authors: Sihong Wu, Owen Jiang, Yilun Zhao, Tiansheng Hu, Yiling Ma, Kaiyan Zhang, Manasi Patwardhan, Arman Cohan
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.5708551539321665
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1504/
- PDF: https://aclanthology.org/2026.acl-long.1504.pdf
- Local PDF: pdf/2026-11-09_04_Can AI Be a Good Peer Reviewer_ A Survey of Peer Review Process, Evaluation, and the Future.pdf

Peer review is a multi-stage process involving reviews, rebuttals, meta-reviews, final decisions, and subsequent manuscript revisions. Recent advances in large language models (LLMs) have motivated methods that assist or automate different stages of this pipeline. In this survey, we synthesize techniques for (i) peer review generation, including fine-tuning strategies, agent-based systems, RL-based methods, and emerging paradigms to enhance generation; (ii) after-review tasks including rebuttals, meta-review and revision aligned to reviews; and (iii) evaluation methods spanning human-centered, reference-based, LLM-based and aspect-oriented. We catalog datasets, compare modeling choices, and discuss limitations, ethical concerns, and future directions. The survey aims to provide practical guidance for building, evaluating, and integrating LLM systems across the full peer review workflow.

## 5. What Makes a Good Curriculum? Disentangling the Effects of Data Ordering on LLM Mathematical Reasoning

- Authors: Yaning Jia, Chunhui Zhang, Xingjian Diao, Xiangchi Yuan, Zhongyu Ouyang, Chiyu Ma, Soroush Vosoughi
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.5703767373947075
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1591/
- PDF: https://aclanthology.org/2026.acl-long.1591.pdf
- Local PDF: pdf/2026-11-09_05_What Makes a Good Curriculum_ Disentangling the Effects of Data Ordering on LLM Mathematical Reasoning.pdf

Curriculum learning (CL), which orders training data from easy to hard, has become a popular strategy for improving reasoning in large language models (LLMs). Yet prior work employs disparate difficulty metrics and training setups, leaving open fundamental questions: When does curriculum help? Which direction—forward or reverse—is better? And does the answer depend on what we measure? We address these questions through a unified offline evaluation framework that decomposes curriculum difficulty into five complementary dimensions: Problem Difficulty, Model Surprisal, Confidence Margin, Predictive Uncertainty, and Decision Variability. Through controlled post-training experiments on mathematical reasoning benchmarks with Llama3.1-8B, Mistral-7B, and Gemma3-4B, we find that: (i) no curriculum strategy dominates universally—the relative effectiveness of forward versus reverse CL depends jointly on model capability and task complexity; (ii) even within a single metric, samples at different difficulty levels produce distinct gains depending on task demands; and (iii) Task-aligned curricula focus on shaping the model’s final representations and generalization, whereas inner-state curricula modulate internal states such as confidence and uncertainty. Our findings challenge the notion of a universal curriculum strategy and offer actionable guidance across model and task regimes, with some metrics indicating that prioritizing decision-uncertain samples can further enhance learning outcomes.

## 6. Enhancing Hallucination Detection via Future Context

- Authors: Joosung Lee, Cheonbok Park, Hwiyeol Jo, Jeonghoon Kim, Joonsuk Park, Kang Min Yoo
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.5701906731755404
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.35/
- PDF: https://aclanthology.org/2026.findings-acl.35.pdf
- Local PDF: pdf/2026-11-09_06_Enhancing Hallucination Detection via Future Context.pdf

Large Language Models (LLMs) are widely used to generate plausible text on online platforms, without revealing the generation process.As users increasingly encounter such black-box outputs, detecting hallucinations has become a critical challenge.To address this challenge, we focus on developing a hallucination detection framework for black-box generators.Motivated by the observation that hallucinations, once introduced, tend to persist, we sample future contexts.The sampled future contexts provide valuable clues for hallucination detection and can be effectively integrated with various sampling-based methods.We extensively demonstrate performance improvements across multiple methods using our proposed sampling approach.

## 7. Inferring Events from Time Series using Language Models

- Authors: Mingtian Tan, Mike A Merrill, Zachary Gottesman, Tim Althoff, David Evans, Thomas Hartvigsen
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.57012136676982
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.157/
- PDF: https://aclanthology.org/2026.acl-long.157.pdf
- Local PDF: pdf/2026-11-09_07_Inferring Events from Time Series using Language Models.pdf

A common goal in analyzing time series data is to understand how events cause observed variations. We study whether Large Language Models (LLMs) can infer natural language events associated with time series data.We introduce an automated method for generating tasks that test a model’s ability to reason about events associated with time series data based on sports data, and develop a new benchmarking method. In experiments spanning 18 LLMs, we prompt LLMs to infer unobserved events given time series data and observe surprising successes, even when providing minimal context. We then show that combining distillation with Reinforcement Learning (RL) can improve the performance for small language models to approach that of large proprietary reasoning models. All resources needed to reproduce our work are available: https://github.com/hartvigsen-group/GAMETime .

## 8. MAC-Reasoner: A Multi-Agent Collaborative Framework for Enhancing Logical Reasoning in Large Language Models

- Authors: Yehua Lin, Liping Zheng, Yin Chen
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.5700238072233983
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.233/
- PDF: https://aclanthology.org/2026.findings-acl.233.pdf
- Local PDF: pdf/2026-11-09_08_MAC-Reasoner_ A Multi-Agent Collaborative Framework for Enhancing Logical Reasoning in Large Language Models.pdf

Large language models (LLMs) face challenges in logical reasoning where correctness requires strict deductive procedures. Purely model-based approaches often suffer from hallucinations, while neuro-symbolic methods typically delegate deduction to external solvers, reducing the LLM to a mere translator. To address this, we propose MAC-Reasoner, a multi-agent framework that constructs a Logic-Augmented Context to enhance LLMs’ reasoning. In this framework, a translator agent converts problems into executable symbolic programs. Symbolic information from solver execution is transformed into the Logic-Augmented Context, serving as a verification reference where logical conflicts trigger heightened attention to violated constraints. We evaluate MAC-Reasoner with three backbone LLMs on four challenging benchmarks. Results show consistent and robust improvements over baselines. Furthermore, reasoning traces from MAC-Reasoner can be used for supervised fine-tuning of LLMs to achieve more accurate and efficient logical reasoning.

## 9. The Best of Both Worlds: Combining Parallel and Sequential Inference Scaling via Aggregation Fine-Tuning

- Authors: Yafu Li, Zhilin Wang, Tingchen Fu, Ganqu Cui, Sen Yang, Yu Cheng
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.5700219956957513
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1568/
- PDF: https://aclanthology.org/2026.findings-acl.1568.pdf
- Local PDF: pdf/2026-11-09_09_The Best of Both Worlds_ Combining Parallel and Sequential Inference Scaling via Aggregation Fine-Tuning.pdf

Scaling data and model size has been proven effective for boosting the performance of large language models. In addition to training-time scaling, recent studies have revealed that increasing test-time computational resources can further improve performance. In this work, we introduce Aggregation Fine-Tuning (AFT), a supervised fine-tuning paradigm where the model learns to synthesize multiple draft responses, referred to as proposals, into a single, refined answer, termed aggregation. At inference time, we apply a propose-and-aggregate strategy that iteratively generates and aggregates proposals, effectively scaling inference-time computation without relying on external guidance such as a reward model. Empirical results across benchmark datasets demonstrate that AFT-trained models achieve substantial gains with test-time scaling, outperforming best-of-N baselines while eliminating the need for external reward signals. Notably, an AFT model, fine-tuned from Llama3.1-8B-Base with only 64k data, achieves a 41.3% LC win rate on AlpacaEval 2, surpassing significantly larger LLMs such as Llama3.1-405B-Instruct and GPT-4. By combining sequential refinement and parallel sampling, the propose-and-aggregate framework scales inference-time computation in a flexible manner.

## 10. MemoBrain: Executive Memory as an Agentic Brain for Reasoning

- Authors: Hongjin Qian, Zhao Cao, Zheng Liu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.5698789441717222
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.127/
- PDF: https://aclanthology.org/2026.findings-acl.127.pdf
- Local PDF: pdf/2026-11-09_10_MemoBrain_ Executive Memory as an Agentic Brain for Reasoning.pdf

Complex reasoning in tool-augmented agent frameworks is inherently long-horizon, causing reasoning traces and transient tool artifacts to accumulate and strain the bounded working context of large language models. Without explicit memory mechanisms, such accumulation disrupts logical continuity and undermines task alignment. This positions memory not as an auxiliary efficiency concern, but as a core component for sustaining coherent, goal-directed reasoning over long horizons.We propose MemoBrain, an executive memory model for tool-augmented agents that constructs a dependency-aware memory over reasoning steps, capturing salient intermediate states and their logical relations. Operating as a co-pilot alongside the reasoning agent, MemoBrain organizes reasoning progress without blocking execution and actively manages the working context. Specifically, it prunes invalid steps, folds completed sub-trajectories, and preserves a compact, high-salience reasoning backbone under a fixed context budget. Together, these mechanisms enable explicit cognitive control over reasoning trajectories rather than passive context accumulation.We evaluate MemoBrain on challenging long-horizon benchmarks, including GAIA, WebWalker, and BrowseComp-Plus, demonstrating consistent improvements over strong baselines.

## 11. Dual Alignment Between Language Model Layers and Human Sentence Processing

- Authors: Tatsuki Kuribayashi, Alex Warstadt, Yohei Oseki, Ethan Gotlieb Wilcox
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.569518057135567
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.2143/
- PDF: https://aclanthology.org/2026.acl-long.2143.pdf
- Local PDF: pdf/2026-11-09_11_Dual Alignment Between Language Model Layers and Human Sentence Processing.pdf

A recent study (CITATION) has shown that human sentence processing behavior, typically measured on syntactically unchallenging constructions, can be effectively modeled using surprisal from early layers of large language models (LLMs). This raises the question of whether such advantages of internal layers extend to more syntactically challenging constructions, where surprisal has been reported to underestimate human cognitive effort.In this paper, we begin by exploring internal layers that better estimate human cognitive effort observed in syntactic ambiguity processing in English.Our experiments show that, in contrast to naturalistic reading, later layers better estimate such a cognitive effort, but still underestimate the human data. This dual alignment sheds light on different modes of sentence processing in humans and LMs: naturalistic reading employs a somewhat weak prediction akin to earlier layers of LMs, while syntactically challenging processing requires more fully-contextualized representations, better modeled by later layers of LMs.Motivated by these findings, we also explore several probability-update measures using shallow and deep layers of LMs, showing a complementary advantage to single-layer’s surprisal in reading time modeling.

## 12. Making MLLMs Blind: Adversarial Smuggling Attacks in MLLM Content Moderation

- Authors: Zhiheng Li, Zongyang Ma, Yuntong Pan, Ziqi Zhang, Xiaolei Lv, Bo Li, Jun Gao, Jianing Zhang, Chunfeng Yuan, Bing Li, Weiming Hu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.569377318631835
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1006/
- PDF: https://aclanthology.org/2026.findings-acl.1006.pdf
- Local PDF: pdf/2026-11-09_12_Making MLLMs Blind_ Adversarial Smuggling Attacks in MLLM Content Moderation.pdf

Multimodal Large Language Models (MLLMs) are increasingly being deployed as automated content moderators. Within this landscape, we uncover a critical threat: Adversarial Smuggling Attacks. Unlike adversarial perturbations (for misclassification) and adversarial jailbreaks (for harmful output generation), adversarial smuggling exploits the Human-AI capability gap. It encodes harmful content into human-readable visual formats that remain AI-unreadable, thereby evading automated detection and enabling the dissemination of harmful content. We classify smuggling attacks into two pathways: (1) Perceptual Blindness, disrupting text recognition; and (2) Reasoning Blockade, inhibiting semantic understanding despite successful text recognition. To evaluate this threat, we constructed SmuggleBench, the first comprehensive benchmark comprising 1,700 adversarial smuggling attack instances. Evaluations on SmuggleBench reveal that both proprietary (e.g., GPT-5) and open-source (e.g., Qwen3-VL) SOTA models are vulnerable to this threat, producing Attack Success Rates (ASR) exceeding 90%. By analyzing the vulnerability through the lenses of perception and reasoning, we identify three root causes: the limited capabilities of vision encoders, the robustness gap in OCR, and the scarcity of domain-specific adversarial examples. We conduct a preliminary exploration of mitigation strategies, investigating the potential of test-time scaling (via CoT) and adversarial training (via SFT) to mitigate this threat.

## 13. Calibrated Progressive Distillation: Co-Designing Curriculum and Target Mixing for Knowledge Distillation of Large Language Models

- Authors: Mengxiang Zhang, Lingyuan Liu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.568605213777185
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.335/
- PDF: https://aclanthology.org/2026.findings-acl.335.pdf
- Local PDF: pdf/2026-11-09_13_Calibrated Progressive Distillation_ Co-Designing Curriculum and Target Mixing for Knowledge Distillation of Large Langu.pdf

Knowledge distillation (KD) is a key technique for compressing large language models (LLMs), yet it faces challenges stemming from the teacher–student capacity gap. While existing KD methods address these challenges either by mixing teacher and student distributions in the distillation target or by using curriculum learning to sequence training from easy to hard examples, they typically design these two strategies independently, missing the opportunity for synergistic co-design. To bridge this gap, we propose Calibrated Progressive Distillation (CPD), a white-box KD framework that co-designs curriculum scheduling and target mixing through a unified difficulty-aware principle. CPD uses a difficulty profile to select epoch-specific subsets that ensure a uniform increase in average difficulty, adapting to the dataset’s intrinsic hardness structure. Simultaneously, the mixing coefficient in the distillation target and the distillation temperature are synchronized with this progression, gradually shifting supervision from teacher-dominated to student-informed signals as training advances. Theoretically, CPD ensures bounded gradients and induces an implicit attention shift from easy to hard samples. Empirically, CPD consistently outperforms advanced KD methods across diverse tasks, while reducing training runtime by over 10%. Our work demonstrates that aligning data scheduling with distillation signal design is crucial for effective and efficient LLM distillation.

## 14. LLM-as-Scheduler: Agentic Workflow Dynamic Scheduling

- Authors: Dawei Xiang, Kexin Chu, Wenyan Xu, Wenhui Zhang, Wei Zhang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.5683975060945343
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.581/
- PDF: https://aclanthology.org/2026.acl-long.581.pdf
- Local PDF: pdf/2026-11-09_14_LLM-as-Scheduler_ Agentic Workflow Dynamic Scheduling.pdf

As large language models (LLMs) improve, many applications are moving from a single LLM call to multi-agent systems. These systems often rely on either hand-designed or automatically optimized workflows with multiple verification and testing steps. While those extra steps can improve accuracy, they also increase latency and token costs. In practice, many queries do not need such heavy processing and can be handled well by a single strong agent.To address this inefficiency, we propose LLM-as-Scheduler (LAS), a system that dynamically chooses the right workflow for each query. LAS uses a two-stage cascade: first, a lightweight gate quickly evaluates each agent’s output; then, an LLM-based scheduler uses query features and gate signals to make more detailed routing decisions. Experiments show that LAS cuts token usage by 43% and reduces end-to-end latency by more than 36%, while causing at most a 1.4 percentage-point drop in accuracy compared with a strong fixed workflow.

## 15. ThinkBooster: A Unified Framework for Seamless Test-Time Scaling of LLM Reasoning

- Authors: Vladislav Smirnov, Quang-Chieu Nguyen, Sergey Senichev, Minh Ngoc Ta, Ekaterina Fadeeva, Artem Vazhentsev, Daria Galimzianova, Nikolai Rozanov, Viktor Mazanov, Jingwei Ni, Tianyi Wu, Igor Kiselev, Mrinmaya Sachan, Iryna Gurevych, Preslav Nakov, Timothy Baldwin, Artem Shelmanov
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.568219995909093
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-demo.70/
- PDF: https://aclanthology.org/2026.acl-demo.70.pdf
- Local PDF: pdf/2026-11-09_15_ThinkBooster_ A Unified Framework for Seamless Test-Time Scaling of LLM Reasoning.pdf

Test-time compute (TTC) scaling has emerged as a powerful paradigm for improving large language model (LLM) reasoning by allocating additional compute during inference, e.g., via multi-sample generation and verifier-based reranking. Existing TTC scaling strategies and reasoning scorers remain fragmented, evaluated under inconsistent protocols, and are rarely analyzed through the lens of quality-cost trade-offs. We introduce ThinkBooster, a unified framework for seamless test-time compute scaling of LLM reasoning, which consists of (i) a modular Python library implementing state-of-the-art TTC scaling strategy and scorer families, (ii) a benchmark that jointly evaluates performance and computational efficiency, and (iii) a deployable OpenAI-compatible proxy service that enables drop-in integration of adaptive reasoning into real-world applications. We further provide a demo visual debugger for inspecting the reasoning trajectories, intermediate selection decisions, and alternative reasoning paths. Empirical results on mathematical and coding tasks reveal the performance-compute trade-offs of TTC scaling strategies and scoring methods and demonstrate that ThinkBooster provides practical gains in real-world tasks. The code is available online under an MIT license.

## 16. SafetyMem: Adaptive Jailbreak Defense via Dual-Component Safety Memory

- Authors: Hao Wang, Ziyi Ni, Huacan Wang, Pin Lyu, Lei Sha
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.567831552615921
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1168/
- PDF: https://aclanthology.org/2026.acl-long.1168.pdf
- Local PDF: pdf/2026-11-09_16_SafetyMem_ Adaptive Jailbreak Defense via Dual-Component Safety Memory.pdf

Current defenses for Large Language Models (LLMs) often suffer from a ”memory gap”: parameter-modifying methods are computationally rigid, while inference-time filters cannot retain or reuse defense knowledge across interactions. To address this, we propose SafetyMem, a novel framework that secures LLMs through a dual-component safety memory system. SafetyMem consists of Semantic Safety Memory (SSM), which consolidates diverse jailbreak attempts into a structured knowledge base of attack patterns, and Episodic Safety Memory (ESM), which maintains an evolving set of procedural rules refined from historical detection failures. Unlike static defenses, SafetyMem allows the model to ”remember” and adapt to emerging adversarial strategies without parameter retraining. To further enhance robustness, we introduce an adversarial memory expansion mechanism that proactively generates challenging variants to solidify these memories. Experiments on standard and stealthy jailbreak benchmarks show that SafetyMem substantially reduces attack success rates while preserving efficiency and interpretability, consistently outperforming state-of-the-art baselines across multiple LLMs.

## 17. TInR: Exploring Tool-Internalized Reasoning in Large Language Models

- Authors: Qiancheng Xu, Yongqi Li, Fan Liu, Hongru Wang, Min Yang, Wenjie Li
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.5678195209911827
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.2077/
- PDF: https://aclanthology.org/2026.acl-long.2077.pdf
- Local PDF: pdf/2026-11-09_17_TInR_ Exploring Tool-Internalized Reasoning in Large Language Models.pdf

Tool-Integrated Reasoning (TIR) has emerged as a promising direction by extending Large Language Models’ (LLMs) capabilities with external tools during reasoning. Existing TIR methods typically rely on external tool documentation during reasoning. However, this leads to tool mastery difficulty, tool size constraints, and inference inefficiency. To mitigate these issues, we explore Tool-Internalized Reasoning (TInR), aiming at facilitating reasoning with tool knowledge internalized into LLMs. Achieving this goal presents notable requirements, including tool internalization and tool-reasoning coordination. To address them, we propose TInR-U, a tool-internalized reasoning framework for unified reasoning and tool usage. TInR-U is trained through a three-phase pipeline: 1) tool internalization with a bidirectional knowledge alignment strategy; 2) supervised fine-tuning warm-up using high-quality reasoning annotations, and 3) reinforcement learning with TInR-specific rewards. We comprehensively evaluate our method across in-domain and out-of-domain settings. Experiment results show that TInR-U achieves superior performance in both settings, highlighting its effectiveness and efficiency. The codes are attached in the supplementary file for review.

## 18. Rendering Data Unlearnable by Exploiting LLM Alignment Mechanisms

- Authors: Ruihan Zhang, Jun Sun
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.5678165391384375
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1885/
- PDF: https://aclanthology.org/2026.acl-long.1885.pdf
- Local PDF: pdf/2026-11-09_18_Rendering Data Unlearnable by Exploiting LLM Alignment Mechanisms.pdf

Large language models (LLMs) are increasingly trained on massive, heterogeneous text corpora, raising serious concerns about the unauthorised use of proprietary or personal data during model training. In this work, we address the problem of data protection against unwanted model learning in a realistic black-box setting. We propose Disclaimer Injection, a novel data-level defence that renders text unlearnable to LLMs. Rather than relying on model-side controls or explicit data removal, our approach exploits the models’ own alignment mechanisms: by injecting carefully designed alignment-triggering disclaimers to prevent effective learning. Through layer-wise analysis, we find that fine-tuning on such protected data induces persistent activation of alignment-related layers, causing alignment constraints to override task learning even on common inputs. Consequently, models trained on such data exhibit substantial and systematic performance degradation compared to standard fine-tuning. Our results identify alignment behaviour as a previously unexplored lever for data protection and, to our knowledge, present the first practical method for restricting data learnability at LLM scale without requiring access to or modification of the training pipeline.

## 19. Towards semantic reliable clinical QA: Query pipeline optimization for cancer patient question answering systems

- Authors: MaoLin He, Rena Wei Gao, Mike Conway, Brian E. Chapman
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.5669584022470278
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1429/
- PDF: https://aclanthology.org/2026.findings-acl.1429.pdf
- Local PDF: pdf/2026-11-09_19_Towards semantic reliable clinical QA_ Query pipeline optimization for cancer patient question answering systems.pdf

Large Language Models (LLMs) show promise in medical Question-Answering (QA) but suffer from hallucinations that jeopardize patient safety. While Retrieval-Augmented Generation (RAG) mitigates this by grounding outputs in external evidence, existing pipelines struggle with the complex, rapidly evolving nature of oncology. We present CoMeta , a three-level controllable metadata-aware framework optimized for Cancer Patient QA (CPQA). We introduce Clinical Hybrid Semantic-Symbolic Document Retrieval (CHSDR), which synergizes real-time Boolean search via NCBI E-Utilities with semantic retrieval to overcome metadata blindness. Additionally, we propose Semantic Enhanced Overlap Segmentation (SEOS) to prevent contextual fragmentation. Our results demonstrate that CHSDR significantly improves retrieval performance, CoMeta improved the answer accuracy of Claude-3-haiku by 5.24% over chain-of-thought prompting and about 3% over a naive RAG setup. This study highlights the importance of domain-specific query optimization in realizing the full potential of RAG and provides a robust framework for building more reliable CPQA systems.

## 20. Hybrid Autoregressive-Diffusion Model for Real-Time Sign Language Production

- Authors: Maoxiao Ye, Xinfeng Ye, Sathiamoorthy Manoharan
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.5664011642250557
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.31/
- PDF: https://aclanthology.org/2026.acl-long.31.pdf
- Local PDF: pdf/2026-11-09_20_Hybrid Autoregressive-Diffusion Model for Real-Time Sign Language Production.pdf

Earlier Sign Language Production (SLP) models typically relied on autoregressive methods that generate output tokens one by one, which inherently provide temporal alignment. Although techniques like Teacher Forcing can prevent model collapse during training, they still cannot solve the problem of error accumulation during inference, since ground truth is unavailable at that stage. In contrast, more recent approaches based on diffusion models leverage step-by-step denoising to enable high-quality generation. However, the iterative nature of these models and the requirement to denoise entire sequences limit their applicability in real-time tasks like SLP. To address it, we propose a hybrid autoregressive-diffusion model for Sign Language Production (SLP), combining sequential dependency modeling with iterative refinement. A Multi-Scale Pose Representation module captures fine-grained articulator features, while a Confidence-Aware Causal Attention mechanism guides generation using joint-level confidence scores. Experiments on PHOENIX14T and How2Sign show improved generation quality and real-time efficiency.

## 21. PURE: Post-hoc Unlocking and REfinement for Discrete Diffusion Decoding

- Authors: Yangryeol Park, Kunhui Lee, Hanback Choi, Cheoneum Park, Donghyeon Jeon, Inho Kang, Seung-Hoon Na
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.5663847813409735
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1234/
- PDF: https://aclanthology.org/2026.findings-acl.1234.pdf
- Local PDF: pdf/2026-11-09_21_PURE_ Post-hoc Unlocking and REfinement for Discrete Diffusion Decoding.pdf

Masked diffusion language models (MDLMs) enable efficient parallel decoding but are limited by a monotonic unmasking policy, where committed tokens cannot be revised. While remasking-based methods mitigate early errors, they mainly intervene during generation. In this work, we study post-hoc refinement of a completed draft and find that naive correction often fails because of contextual lock-in, a phenomenon in which local error patterns become self-reinforcing. To address this, we propose PURE (Post-hoc Unlocking and REfinement), a training-free inference algorithm for two-phase decoding. PURE profiles confidence dynamics during drafting to identify unstable regions via an instability score ( 𝛥 i ), then unlocks them through deterministic window masking and stochastic leftward relaxation. On reasoning benchmarks, PURE substantially improves accuracy when applied to LLaDA-8B-Instruct, including a gain of +12.9 points over the baseline on GSM8K. These gains require only a small refinement budget, yielding a favorable compute-quality trade-off for discrete diffusion decoding.

## 22. CodeWiki: Evaluating AI’s Ability to Generate Holistic Documentation for Large-Scale Codebases

- Authors: Anh Nguyen Hoang, Minh Le-Anh, Bach Le, Nghi D. Q. Bui
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.5652944865975535
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.288/
- PDF: https://aclanthology.org/2026.findings-acl.288.pdf
- Local PDF: pdf/2026-11-09_22_CodeWiki_ Evaluating AI’s Ability to Generate Holistic Documentation for Large-Scale Codebases.pdf

Comprehensive software documentation is crucial yet costly to produce. Despite recent advances in large language models (LLMs), generating holistic, architecture-aware documentation at the repository level remains challenging due to complex and evolving codebases that exceed LLM context limits. Existing automated methods struggle to capture rich semantic dependencies and architectural structure. We present CodeWiki , a unified framework for automated repository-level documentation across seven mainstream programming languages. CodeWiki combines top-down hierarchical decomposition with a divide-and-conquer agent system to preserve architectural context and scale documentation generation, and a bottom-up synthesis that integrates textual descriptions with visual artifacts such as architecture and data-flow diagrams. We also introduce CodeWikiBench , a benchmark with hierarchical rubrics and LLM-based evaluation protocols. Experiments show that CodeWiki achieves a 68.79% quality score with proprietary models, outperforming the closed-source DeepWiki baseline by 4.73%, with especially strong gains on scripting languages. CodeWiki is released as open source to support future research.

## 23. BoYaEval: Evaluating Multimodal Large Language Models on Understanding Ancient Chinese Musical Scores

- Authors: Jiajia Li, Weizhi Xue, Yao Yao, Qiwei Li, Chong Chen, Zuchao Li, Ping Wang, Hai Zhao
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.5651095305177387
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.997/
- PDF: https://aclanthology.org/2026.acl-long.997.pdf
- Local PDF: pdf/2026-11-09_23_BoYaEval_ Evaluating Multimodal Large Language Models on Understanding Ancient Chinese Musical Scores.pdf

Multimodal Large Language Models (MLLMs) excel in general tasks but struggle with specialized, structured cultural symbols. We introduce BoYaEval, the first comprehensive benchmark dedicated to deciphering diverse Ancient Chinese musical notations, including five types of ancient Chinese music notation systems. These systems utilize unique spatial layouts and specialized ideograms to encode pitch and intricate playing techniques. BoYaEval comprises 3,175 high-quality images across these notation styles and establishes a three-tier evaluation: Structural Parsing (symbol recognition), Instructional Translation (technique mapping), and Musical Reasoning (melody derivation). We evaluate 21 leading MLLMs. Results indicate that while models perform adequately in basic recognition, they fail in cross-system compositional logic, scoring only around 27% on reasoning tasks. BoYaEval highlights the limitations of current MLLMs in processing diverse spatial-symbolic dependencies, bridging the gap between ancient wisdom and modern AI for digitizing intangible cultural heritage. The BoYaEval benchmark is publicly available at https://huggingface.co/datasets/MYTH-Lab/BoYaEval .

## 24. GOAT: A Training Framework for Goal-Oriented Agent with Tools

- Authors: Hyunji Min, Sangwon Jung, Junyoung Sung, Dosung Lee, Leekyeung Han, Paul Hongsuck Seo
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.564707691743575
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1150/
- PDF: https://aclanthology.org/2026.findings-acl.1150.pdf
- Local PDF: pdf/2026-11-09_24_GOAT_ A Training Framework for Goal-Oriented Agent with Tools.pdf

Large language models (LLMs) have evolved from pure text generators into interactive agents capable of invoking external tools. However, LLM agents still struggle with goal-oriented queries, which require decomposing high-level objectives into sequences of interdependent API calls with accurate planning and execution. Current approaches rely on zero-shot evaluation due to the absence of training data; while proprietary models such as GPT-4 exhibit strong reasoning capabilities, smaller open-source models remain ineffective at complex tool use. To address this limitation, we propose a novel training framework GOAT, that enables fine-tuning LLM agents without human annotation. GOAT automatically synthesizes goal-oriented API execution data from API documents using a novel call-first generation paradigm, that constructs training data based on executed API call sequences. Through extensive experiments, we show that GOAT-trained agents achieve state-of-the-art performance across multiple existing goal-oriented benchmarks. In addition, we introduce GOATBench, a new goal-oriented API execution benchmark, and demonstrate that agents trained with GOAT also excel in this setting. These results highlight GOAT as a practical path toward building robust open-source LLM agents capable of complex reasoning and tool use.

## 25. G 2 RPO-A: Guided Group Relative Policy Optimization with Adaptive Guidance

- Authors: Yongxin Guo, Wenbo Deng, Zhenglin Cheng, Xiaoying Tang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.56416966627405
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.206/
- PDF: https://aclanthology.org/2026.acl-long.206.pdf
- Local PDF: pdf/2026-11-09_25_G 2 RPO-A_ Guided Group Relative Policy Optimization with Adaptive Guidance.pdf

Reinforcement Learning with Verifiable Rewards (RLVR) has markedly enhanced the reasoning abilities of large language models (LLMs). Its success, however, largely depends on strong base models with rich world knowledge, yielding only modest improvements for small-size language models (SLMs). To address this limitation, we investigate Guided GRPO, which injects ground-truth reasoning steps into roll-out trajectories to compensate for SLMs’ inherent weaknesses. Through a comprehensive study of various guidance configurations, we find that naively adding guidance delivers limited gains. These insights motivate G 2 RPO-A, an adaptive algorithm that automatically adjusts guidance strength in response to the model’s evolving training dynamics. Experiments on mathematical reasoning and code-generation benchmarks confirm that G 2 RPO-A substantially outperforms vanilla GRPO. Our code and models at available at https://github.com/T-Lab-CUHKSZ/G2RPO-A .

## 26. Fair-CCD: Mitigating Bias in Large Language Models for Tabular Classification Through Context-Contrastive Decoding

- Authors: Donghan Liu, Han Sun, Zhaohui Wang, Qin Li, Min Zhang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.564018286615105
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1317/
- PDF: https://aclanthology.org/2026.acl-long.1317.pdf
- Local PDF: pdf/2026-11-09_26_Fair-CCD_ Mitigating Bias in Large Language Models for Tabular Classification Through Context-Contrastive Decoding.pdf

While recent studies show the effectiveness of in-context learning (ICL) for tabular data prediction, they also reveal significant fairness issues in large language models (LLMs). Prior work to mitigate fairness issues often employs interventions relying on subjective demonstration selection. Its effectiveness varies significantly with the specific demonstration content, leading to low controllability. Moreover, the improvement of fairness is highly unstable across different models and tasks. To address the challenges of low controllability and limited stability in fairness interventions, we propose Fairness-Aware Context-Contrastive Decoding (Fair-CCD). Fair-CCD first constructs Structural Bias Templates (SBTs), motivated by behavioral patterns observed in demonstrations, to encode the relationship between sensitive attributes and predicted labels in a structured and controllable form. During inference, Fair-CCD injects multiple SBTs and contrasts the model’s responses, generating two differential signals that guide fairness adjustment and preserve task performance. By leveraging attention signals to scale decoding adjustments guided by the difference signals, Fair-CCD achieves stable and adaptive bias mitigation across models and tasks. Extensive experimental results demonstrate that Fair-CCD consistently improves fairness metrics without degrading task accuracy.

## 27. NeuroSym-Cal: Bridging the Reasoning-Execution Gap in Code Generation via Hierarchical Calibration

- Authors: Peiyang Liu, Yining Wang, Youru Li, Long Li, Zhi Cai, Wei Ye
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.563883076214681
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.305/
- PDF: https://aclanthology.org/2026.findings-acl.305.pdf
- Local PDF: pdf/2026-11-09_27_NeuroSym-Cal_ Bridging the Reasoning-Execution Gap in Code Generation via Hierarchical Calibration.pdf

While Chain-of-Thought (CoT) reasoning enhances code generation in Large Language Models (LLMs), it introduces a critical challenge in uncertainty estimation: Confidence Saturation. Existing calibration methods, such as Self-Consistency, rely on the assumption that consensus implies correctness. This assumption fails under systematic errors, where models confidently repeat flawed logic, leading to miscalibrated high-confidence predictions. To address this, we introduce NeuroSym-Cal, a hierarchical calibration framework. We posit that reliable confidence requires interrogating the model at two complementary levels: the extrinsic consensus of its symbolic outputs and the intrinsic sensitivity of its latent reasoning. Specifically, we propose Reasoning Sensitivity Analysis to measure the local curvature of the deductive process via latent perturbation, providing a fine-grained signal that persists even when output consensus saturates. These orthogonal features are fused by a Contextual Calibration Network to predict correctness. Experiments across state-of-the-art reasoning models (e.g., DeepSeek-R1) demonstrate that NeuroSym-Cal effectively de-saturates overconfident errors, achieving state-of-the-art Expected Calibration Error (ECE) and superior selective generation performance on Out-Of-Domain (OOD) benchmarks.

## 28. Two Pathways to Truthfulness: On the Intrinsic Encoding of LLM Hallucinations

- Authors: Wen Luo, Guangyue Peng, Wei Li, Shaohang Wei, Feifan Song, Liang Wang, Nan Yang, Xingxing Zhang, Jing Jin, Furu Wei, Houfeng Wang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.5638794107787177
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1173/
- PDF: https://aclanthology.org/2026.acl-long.1173.pdf
- Local PDF: pdf/2026-11-09_28_Two Pathways to Truthfulness_ On the Intrinsic Encoding of LLM Hallucinations.pdf

Despite their impressive capabilities, large language models (LLMs) frequently generate hallucinations. Previous work shows that their internal states encode rich signals of truthfulness, yet the origins and mechanisms of these signals remain unclear. In this paper, we demonstrate that truthfulness cues arise from two distinct information pathways: (1) a Question-Anchored pathway that depends on question–answer information flow, and (2) an Answer-Anchored pathway that derives self-contained evidence from the generated answer itself. First, we validate and disentangle these pathways through attention knockout and token patching. Afterwards, we uncover notable and intriguing properties of these two mechanisms. Further experiments reveal that (1) the two mechanisms are closely associated with LLM knowledge boundaries; and (2) internal representations are aware of their distinctions. Finally, building on these insightful findings, two applications are proposed to enhance hallucination detection performance. Overall, our work provides new insight into how LLMs internally encode truthfulness, offering directions for more reliable and self-aware generative systems.

## 29. QiMeng-PRepair: Precise Code Repair via Edit-Aware Reward Optimization

- Authors: Changxin Ke, Rui Zhang, Jiaming Guo, Yuanbo Wen, Li Ding, Shuo Wang, Xuyuan Zhu, Xiong Peng, Di Huang, Zidong Du, Xing Hu, Qi Guo, Yunji Chen
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.56327243910095
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1343/
- PDF: https://aclanthology.org/2026.acl-long.1343.pdf
- Local PDF: pdf/2026-11-09_29_QiMeng-PRepair_ Precise Code Repair via Edit-Aware Reward Optimization.pdf

Large Language Models (LLMs) achieve strong program repair performance but often suffer from over-editing, where excessive modifications overwrite correct code and hinder bug localization. We systematically quantify its impact and introduce precise repair task, which maximizes reuse of correct code while fixing only buggy parts. Building on this insight, we propose PRepair, a framework that mitigates over-editing and improves repair accuracy. PRepair has two components: Self-Breaking, which generates diverse buggy programs via controlled bug injection and min–max sampling, and Self-Repairing, which trains models with Edit-Aware Group Relative Policy Optimization (EA-GRPO) using an edit-aware reward to encourage minimal yet correct edits. Experiments show that PRepair improves repair precision by up to 31.4% under fix 1 @1 , a metric that jointly considers repair correctness and extent, and significantly increases decoding throughput when combined with speculative editing, demonstrating its potential for precise and practical code repair.

## 30. What Do LLMs Learn First? Asymmetric Learning Dynamics of Input Complexity and Output Ambiguity in Preference Alignment

- Authors: Mengyang Li, Jingwen Wang, Pinlong Zhao
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.563110219765805
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.789/
- PDF: https://aclanthology.org/2026.acl-long.789.pdf
- Local PDF: pdf/2026-11-09_30_What Do LLMs Learn First_ Asymmetric Learning Dynamics of Input Complexity and Output Ambiguity in Preference Alignment.pdf

Direct Preference Optimization (DPO) has become a standard approach for aligning large language models with human preferences, yet existing methods treat all preference pairs uniformly during training. We identify two distinct sources of learning difficulty: Input Complexity (IC), capturing prompt understanding challenges, and Output Ambiguity (OA), measuring preference discrimination difficulty. Through systematic analysis, we demonstrate that these dimensions induce asymmetric learning dynamics, with IC-related competencies developing rapidly in early training while OA-related competencies emerge more gradually. Building on this observation, we propose DECOPO, a training framework that maintains separate, adaptive pacing schedules for each dimension. Experiments on UltraFeedback show that DECOPO achieves 42.3% length-controlled win rate on AlpacaEval 2.0 and 7.66 on MT-Bench, outperforming curriculum baselines by 2.1% and 0.21 points respectively, while matching full-data baseline performance with only 75% of training samples.
