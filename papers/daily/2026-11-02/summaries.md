# Paper Daily Reading - 2026-11-02

## 1. A Multi-Agent Framework for Feature-Constrained Difficulty Control in Reading Comprehension Item Generation

- Authors: Seonjeong Hwang, Jun Seo, Hyounghun Kim, Gary Lee
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.5881626954278496
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1267/
- PDF: https://aclanthology.org/2026.acl-long.1267.pdf
- Local PDF: pdf/2026-11-02_01_A Multi-Agent Framework for Feature-Constrained Difficulty Control in Reading Comprehension Item Generation.pdf

Recent studies in difficulty-controlled reading comprehension item generation have leveraged large language models (LLMs) to produce items by adjusting difficulty-related features. However, existing methods typically rely on a single-agent prompting approach, which often fails to consistently satisfy specified feature constraints, resulting in items that deviate from the target difficulty level. To address this limitation, we introduce MAFIG, a Multi-agent Framework for Feature-constrained Item Generation, where multiple LLM agents and feature-specific evaluators collaborate to generate and iteratively revise items based on intended constraints. Furthermore, to verify the efficacy of MAFIG in difficulty control, we propose a method for constructing a sequence of feature constraint sets that yield items with monotonically increasing difficulty. Experimental results demonstrate that MAFIG generates items that adhere to target constraints at a significantly higher rate than baselines, achieving robust difficulty control through the difficulty-calibrated constraint sequence.

## 2. Step Potential Advantage Estimation: Harnessing Intermediate Confidence and Correctness for Efficient Mathematical Reasoning

- Authors: Fei Wu, Zhenrong Zhang, Qikai Chang, Jianshu Zhang, Quan Liu, Jun Du
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.5878733623733803
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.317/
- PDF: https://aclanthology.org/2026.findings-acl.317.pdf
- Local PDF: pdf/2026-11-02_02_Step Potential Advantage Estimation_ Harnessing Intermediate Confidence and Correctness for Efficient Mathematical Reaso.pdf

Reinforcement Learning with Verifiable Rewards (RLVR) elicits long chain-of-thought reasoning in large language models (LLMs), but outcome-based rewards lead to coarse-grained advantage estimation. While existing approaches improve RLVR via token-level entropy or sequence-level length control, they lack a semantically grounded, step-level measure of reasoning progress. As a result, LLMs fail to distinguish necessary deduction from redundant verification: they may continue checking after reaching a correct solution and, in extreme cases, overturn a correct trajectory into an incorrect final answer. To remedy the lack of process supervision, we introduce a training-free probing mechanism that extracts intermediate confidence and correctness and combines them into a Step Potential signal that explicitly estimates the reasoning state at each step. Building on this signal, we propose Step Potential Advantage Estimation (SPAE), a fine-grained credit assignment method that amplifies potential gains, penalizes potential drops, and applies penalty after potential saturates to encourage timely termination. Experiments across multiple benchmarks show SPAE consistently improves accuracy while substantially reducing response length, outperforming strong RL baselines and recent efficient reasoning and token-level advantage estimation methods. The code is available at https://github.com/cii030/SPAE-RL .

## 3. GenesisFunc: Multi-Agent Data Generation for Accurate and Generalizable Function-Calling

- Authors: Hao-Xiang Xu, Chong Deng, Jiaqing Liu, Wen Wang, Qian Chen, Lujia Bao, Xiangang Li, Zhen-Hua Ling
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.5876135874181854
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1319/
- PDF: https://aclanthology.org/2026.acl-long.1319.pdf
- Local PDF: pdf/2026-11-02_03_GenesisFunc_ Multi-Agent Data Generation for Accurate and Generalizable Function-Calling.pdf

Large Language Models (LLMs) extend their capabilities through function-calling (FC), which relies on training data with high quality, diversity, and broad coverage of scenario. However, obtaining and annotating real function-calling data is challenging, while synthetic data from existing pipelines often suffers from unreliable APIs, limited tool scalability, insufficient diversity, and weak quality control. To address these, we present GenesisFunc, an automated pipeline for generating FC training data. Starting from reliable tools in widely used public benchmarks, our GenesisFunc employs a multi-agent framework to support a dialogue generation system that produces conversations spanning diverse scenarios, while maintaining both diversity and quality throughout the process. The accuracy of the data is further reinforced through a multi-stage evaluation system. We fine-tune an 8B LLM on the synthetic dataset and show through extensive experiments that it outperforms similarly sized open-source models in in-domain FC performance and out-of-domain generalization, while reaching FC capabilities comparable to some of the latest API-based models. In addition, our method demonstrates strong potential to scale effectively across downstream tools, underscoring its real-world applicability.

## 4. DecoCal: Decoding with Calibration in Diffusion Large Language Models

- Authors: Fan Xu, Huixuan Zhang, Xiaojun Wan
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.5876026400163354
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.545/
- PDF: https://aclanthology.org/2026.acl-long.545.pdf
- Local PDF: pdf/2026-11-02_04_DecoCal_ Decoding with Calibration in Diffusion Large Language Models.pdf

Diffusion Large Language Models (DLLMs) generate text via iterative masked-token denoising, supporting parallel prediction and bidirectional context modeling. Despite these advantages, decoding remains challenging: many tokens appear predictable early, yet single-step predictions are often unstable, exhibiting temporal oscillations or overconfidence, making it difficult to determine which tokens can be safely committed. To address these challenges, we propose DecoCal , a Decoding framework that explicitly performs Calibration of token-level confidence across diffusion steps and leverages the calibrated results to guide decoding decisions. Specifically, DecoCal aggregates historical predictions to maintain calibrated confidence, triggering unmasking only when a token is sufficiently stable, while a remasking mechanism allows revision of premature commitments. This calibration-based design enables early decoding of reliably converged tokens while deferring or correcting unstable ones, balancing reliability and speed. Experiments on multiple DLLMs and benchmarks show that DecoCal improves generation accuracy compared to existing strategies. Our results highlight the importance of temporal calibration in unlocking the full potential of diffusion-based language generation.

## 5. Efficient Hallucination Detection in Automatic Code Generation

- Authors: Georgii Andriushchenko, Roman Garaev, Lyudmila Rvanova, Artem Shelmanov, Vladimir V. Ivanov
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.5875337924027924
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.2143/
- PDF: https://aclanthology.org/2026.findings-acl.2143.pdf
- Local PDF: pdf/2026-11-02_05_Efficient Hallucination Detection in Automatic Code Generation.pdf

Large language models (LLMs) frequently produce source code that seems correct and well-formed, yet includes hallucinated elements that cause downstream test failures. In this study, we benchmark state-of-the-art uncertainty quantification methods and existing baselines for the task of hallucination detection in source code and introduce a diff-based pipeline to construct a code dataset annotated with line-level hallucinations. Building on this, we train a lightweight Transformer-based detector that uses LLM internal representations to identify hallucinations, substantially outperforming existing methods across several code generation domains. The detector also shows particular promise for enabling self-correction in LLM-based coding agents. We release the first publicly available dataset of line-level code hallucinations, along with the corresponding source code and trained hallucination detectors https://github.com/datapaf/CodeHallucinationDetection

## 6. Beyond Static Artifacts: An Evolutionary Framework for Synthetic Claim Generation

- Authors: Yeqing Teng, Jiasheng Si, Shuxia Lin, Linhai Zhang, Weiyu Zhang, Wenpeng Lu, Deyu Zhou, Xiaoming Wu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.5863198618714223
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1548/
- PDF: https://aclanthology.org/2026.acl-long.1548.pdf
- Local PDF: pdf/2026-11-02_06_Beyond Static Artifacts_ An Evolutionary Framework for Synthetic Claim Generation.pdf

With the generative capabilities of large language models (LLMs) reshaping the information ecosystem, the concern with the sociological validity of claim detection benchmarks is increasing. Current claim detection benchmarks predominantly treat claims as static textual artifacts, overlooking the sociological etiology of how information naturally emerges and mutates. In this paper, we propose an evolutionary paradigm that models claims as socially evolving entities. In specific, we introduce a socially generative framework for synthetic claim generation, a multi-agent simulation grounded in the Open Claims Model. By decomposing claims into context, utterance, and proposition, our approach enables the precise simulation of unmitigated propagation to capture truth decay, and intervened propagation with multi-auditor oversight for targeted generation. Furthermore, we propose the background-user-perspective (BUP) framework, which reformulates check-worthiness as a condition-dependent probability rooted in social environment. Experiments on our datasets verify the data quality and reveal how network topology and user attributes systematically shape veracity drift.

## 7. Hierarchical Policy Optimization for Simultaneous Translation of Unbounded Speech

- Authors: Siqi Ouyang, Shuoyang Ding, Oleksii Hrinchuk, Vitaly Lavrukhin, Brian Yan, Boris Ginsburg, Lei Li
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.5854025699027936
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.80/
- PDF: https://aclanthology.org/2026.acl-long.80.pdf
- Local PDF: pdf/2026-11-02_07_Hierarchical Policy Optimization for Simultaneous Translation of Unbounded Speech.pdf

Simultaneous speech translation (SST) generates translations while receiving partial speech input. Recent advances show that large language models (LLMs) can substantially improve SST quality, but at the cost of high computational overhead. To reduce this cost, prior work reformulates SST as a multi-turn dialogue task, enabling full reuse of the LLM’s key–value (KV) cache and eliminating redundant feature recomputation. However, this approach relies on supervised fine-tuning (SFT) data in dialogue form, for which few human annotations exist, and existing synthesis methods cannot guarantee data quality. In this work, we propose a Hierarchical Policy Optimization (HPO) approach that post-train models trained on imperfect SFT data. We introduce a hierarchical reward that balances translation quality and latency objectives. Experiments on English to Chinese/German/Japanese demonstrate improvements of over +7 COMET score and +1.25 MetricX score at a latency of 1.5 seconds. Comprehensive ablation studies further validate the effectiveness of different quality rewards, hierarchical reward formulations, and segmentation strategies.

## 8. SSG: Logit-Balanced Vocabulary Partitioning for LLM Watermarking

- Authors: Chenxi Gu, Xiaoning Du, John C. Grundy
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.5850208493000326
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1702/
- PDF: https://aclanthology.org/2026.acl-long.1702.pdf
- Local PDF: pdf/2026-11-02_08_SSG_ Logit-Balanced Vocabulary Partitioning for LLM Watermarking.pdf

Watermarking has emerged as a promising technique for tracing the authorship of content generated by large language models (LLMs). Among existing approaches, the KGW scheme is particularly attractive due to its versatility, efficiency, and effectiveness in natural language generation.However, KGW’s effectiveness degrades significantly under low-entropy settings such as code generation and mathematical reasoning. A crucial step in the KGW method is random vocabulary partitioning, which enables adjustments to token selection based on specific preferences. Our study revealed that the next-token probability distribution plays an critical role in determining how much, or even whether, we can modify token selection and, consequently, the effectiveness of watermarking.We refer to this characteristic, associated with the probability distribution of each token prediction, as watermark strength. In cases of random vocabulary partitioning, the lower bound of watermark strength is dictated by the next-token probability distribution. However, we found that, by redesigning the vocabulary partitioning algorithm, we can potentially raise this lower bound. In this paper, we propose SSG ( S ort-then- S plit by G roups), a method that partitions the vocabulary into two logit-balanced subsets. This design lifts the lower bound of watermark strength for each token prediction, thereby improving watermark detectability. Experiments on code generation and mathematical reasoning datasets demonstrate the effectiveness of SSG.

## 9. RAP-ID: Mechanistic Prompt Injection Detection via Impostor Behavior Analysis

- Authors: Yuchen Yang, Lei Peng, Yujie He, Yang yu, Zhongxin Wu, Yanlei Shi
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.584742911944613
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.738/
- PDF: https://aclanthology.org/2026.findings-acl.738.pdf
- Local PDF: pdf/2026-11-02_09_RAP-ID_ Mechanistic Prompt Injection Detection via Impostor Behavior Analysis.pdf

Large Language Models are increasingly integrated into critical applications, yet they remain vulnerable to prompt injection attacks where meticulously designed adversarial inputs bypass safety alignment. Existing defenses often rely on externally deployed guardrail models or response inspection, which incur significant computational overhead and latency. We propose RAP-ID (Robust Alignment Preservation via Injection Defense), a mechanistic, train-free detection framework that operates exclusively on internal state dynamics during the initial forward pass. RAP-ID identifies attacks by detecting their inevitable “impostor” behavior: they must mimic system instruction semantics (Directive Likeness), usurp attention from the true system prompt (Counterfactual Gain), and trigger latent risk concepts (Policy Conflict). By fusing these three internal signals, RAP-ID achieves effective detection across diverse attack vectors—from direct jailbreaks to stealthy agentic manipulations—without requiring text generation. Comprehensive evaluations demonstrate that RAP-ID achieves competitive performance with significant overall improvements compared to heuristic methods. Crucially, as a train-free solution, it incurs minimal computational overhead and delivers fast response times, making it well-suited for real-time deployment.

## 10. Efficient KL Divergence Estimation via Truncated Top-K Integration for Large Language Models

- Authors: Xinyuan Wang, Luozhijie Jin, Bo Wang, Yuan Li, Zhangyue Yin, Xipeng Qiu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.584514479565497
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.405/
- PDF: https://aclanthology.org/2026.acl-long.405.pdf
- Local PDF: pdf/2026-11-02_10_Efficient KL Divergence Estimation via Truncated Top-K Integration for Large Language Models.pdf

Kullback-Leibler (KL) divergence regularization is essential for stabilizing reinforcement learning from human feedback (RLHF) in large language models (LLMs), yet its exact computation requires summing over vocabularies of all tokens, incurring prohibitive memory costs during training. Existing stochastic estimators circumvent this bottleneck by estimating KL divergence using only the sampled token from the trajectory, but suffer from high variance ( k 1 ) or systematic bias ( k 2 ). We propose TIKE (Top- k Importance-weighted KL Estimator), which exploits the Zipfian structure of language model distributions: by deterministically integrating over only the top- k tokens, TIKE captures most of the probability mass while effectively reducing memory cost. To ensure correctness in off-policy settings characteristic of Group Relative Policy Optimization (GRPO), we incorporate importance sampling weights that correct for distribution shift between rollout and optimization policies. Experiments on models across diverse benchmarks demonstrate that TIKE consistently outperforms stochastic baselines, while exhibiting substantially lower gradient variance. Our analysis reveals that TIKE closely tracks the exact Rao-Blackwellized estimator with near-zero variance, offering a practical path toward stable, memory-efficient KL regularization for reasoning-intensive LLMs training.

## 11. Large-Scale Diverse Synthesis for Mid-Training

- Authors: Xuemiao Zhang, Chengying Tu, Can Ren, Rongxiang Weng, Hongfei Yan, Jingang Wang, Xunliang Cai
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.5845010119631464
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.814/
- PDF: https://aclanthology.org/2026.findings-acl.814.pdf
- Local PDF: pdf/2026-11-02_11_Large-Scale Diverse Synthesis for Mid-Training.pdf

Mid-training has become critical for enhancing the knowledge and reasoning ability of large language models (LLMs), especially through the utilization of large-scale synthetic data. However, existing data synthesis methods often generate simplistic and homogeneous QA pairs, with limited scale and diversity. To address this, we propose BoostQA, a novel framework designed to synthesize large-scale, diverse, and high-quality QA data for mid-training. BoostQA introduces model probes during mid-training for the first time and implements STEM-focused multi-grade synthesis to boost data diversity as well as high-difficulty synthesis to alleviate difficulty degradation, followed by answer refinement to further improve quality. Extensive experiments by mid-training Llama-3 8B demonstrate that using only 20B-token BoostQA data achieves a significant average improvement of 12.74% on MMLU and CMMLU over the pre-training baseline. After mid-training on 500B tokens, including 100B-token BoostQA data, our model achieves SOTA average results across benchmarks among mainstream models of comparable size. BoostQA also demonstrates robust scalability, with performance consistently improving as model size, data volume, and initial FLOPs scale.

## 12. Agent Newsroom: Efficient Chronological Report Generation via Dynamic Multi-Agent Collaboration

- Authors: Zhenhua Wang, Chunlei Wang, Yue Geng, Bang Wang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.583041794734351
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1149/
- PDF: https://aclanthology.org/2026.acl-long.1149.pdf
- Local PDF: pdf/2026-11-02_12_Agent Newsroom_ Efficient Chronological Report Generation via Dynamic Multi-Agent Collaboration.pdf

Many real-world applications require generating a chronological report from an evolving document stream; Timeline Summarization (TLS) provides a standard testbed for this setting. While large language models (LLMs) improve event synthesis, most LLM-based TLS systems remain monolithic: they repeatedly process overlapping evidence and often mirror the corpus’ bursty reporting patterns, producing redundant timelines with temporal/topical imbalance and high cost. We propose MAS-TLS , a multi-agent framework that casts TLS as a newsroom-like collaboration. A master editor steers balanced coverage by allocating system-visible evidence with a coverage–diversity objective; specialist reporter agents independently draft time-anchored, evidence-grounded events while cross-reviewing to limit redundancy; an adjudication round reconciles competing drafts and consolidates duplicates into a global timeline; and a non-stationary Bayesian controller adaptively staffs agents under token/time budgets. Experiments on three benchmarks show that MAS-TLS improves semantic coverage and temporal grounding while substantially reducing token usage and latency.

## 13. ReFL: Reflective Feedback Learning for Hallucination Detection of Large Language Models

- Authors: Cunhang Fan, Jun Zhang, Xue Zhang, Shuai Zhang, Zhao Lv, Jianhua Tao, Zhengqi Wen
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.582760659191912
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.899/
- PDF: https://aclanthology.org/2026.acl-long.899.pdf
- Local PDF: pdf/2026-11-02_13_ReFL_ Reflective Feedback Learning for Hallucination Detection of Large Language Models.pdf

Large Language Models (LLMs) often generate factually incorrect content, known as “hallucinations”, which undermine the reliability and safety of their outputs. Existing hallucination detection methods either depend on external knowledge sources, incurring high computational costs and limiting real-time applicability, or extract the model’s internal states, leading to poor generalization. To address these issues, this paper proposes ReFL, a hallucination detection framework. ReFL leverages corrective in-context learning to dynamically guide LLMs to recognize their own prediction errors and adjust internal representations, critically without updating model weights. Specifically, by introducing a corrective in-context learning strategy, where triplets of input text, model prediction, and ground-truth label are embedded into the prompt to make the model explicitly aware of its own errors. The model reflects on prior outputs to adjust its internal states and generate semantically structured representations better aligned with factuality. This feedback mechanism encourages the model to shape a more coherent semantic space and enhances the LLM’s internal sensitivity to hallucinations. Experimental results on two benchmark datasets demonstrate that ReFL consistently outperforms existing methods, achieving state-of-the-art performance.

## 14. Whose Facts Win? LLM Source Preferences under Knowledge Conflicts

- Authors: Jakob Schuster, Vagrant Gautam, Katja Markert
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.58195367553375
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1357/
- PDF: https://aclanthology.org/2026.acl-long.1357.pdf
- Local PDF: pdf/2026-11-02_14_Whose Facts Win_ LLM Source Preferences under Knowledge Conflicts.pdf

As large language models (LLMs) are more frequently used in retrieval-augmented generation pipelines, it is increasingly relevant to study their behavior under knowledge conflicts. Thus far, the role of the source of the retrieved information has gone unexamined. We address this gap with a novel framework to investigate how source preferences affect LLM resolution of inter-context knowledge conflicts in English, motivated by interdisciplinary research on credibility. By using synthetic sources, we study preferences for different types of sources without inheriting the biases of specific real-world sources. With a comprehensive, tightly-controlled evaluation of 13 open-weight LLMs, we find that LLMs prefer institutionally-corroborated information (e.g., government or newspaper sources) over information from people and social media. However, these source preferences can be reversed by simply repeating information from less credible sources. To mitigate repetition effects and maintain consistent preferences, we propose a novel method that reduces repetition bias by up to 79.2%, while also maintaining at least 72.5% of original preferences. We release all data and code to encourage future work on credibility and source preferences in knowledge-intensive NLP.

## 15. HyperAdaLoRA: Accelerating LoRA Rank Allocation During Training via Hypernetworks without Sacrificing Performance

- Authors: Hao Zhang, Zhenjia Li, Yifan Gao, Xi Xiao, Heng Zhang, Shuyang Zhang, Xiaoxincc, Bo Huang, Yuhang Wu, Tianyang Wang, Hao Xu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.5818206107117603
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1648/
- PDF: https://aclanthology.org/2026.findings-acl.1648.pdf
- Local PDF: pdf/2026-11-02_15_HyperAdaLoRA_ Accelerating LoRA Rank Allocation During Training via Hypernetworks without Sacrificing Performance.pdf

Parameter-Efficient Fine-Tuning (PEFT), especially Low-Rank Adaptation (LoRA), has emerged as a promising approach to fine-tuning large language models(LLMs) while reducing computational and memory overhead. However, LoRA assumes a uniform rank r for each incremental matrix, not accounting for the varying significance of weight matrices across different modules and layers. AdaLoRA leverages Singular Value Decomposition (SVD) to parameterize updates and employs pruning of singular values to introduce dynamic rank allocation, thereby enhancing adaptability. However, during the training process, it often encounters issues of slow convergence speed and high computational overhead. To address this issue, we propose HyperAdaLoRA, a novel framework that accelerates the convergence of AdaLoRA by leveraging a hypernetwork. Instead of directly optimizing the components of Singular Value Decomposition (P, 𝛬, Q) , HyperAdaLoRA employs a hypernetwork based on attention mechanisms to dynamically generate these parameters. By pruning the outputs of the hypernetwork that generates the singular values, dynamic rank allocation is achieved. Comprehensive experiments on various datasets and models demonstrate that our method achieves faster convergence without sacrificing performance. Moreover, our method generalizes well to other LoRA-based approaches, highlighting its strong generalization capability.

## 16. Bayesian Social Deduction with Graph-Informed Language Models

- Authors: Shahab Rahimirad, Guven Gergerli, Lucia Romero, Angela Qian, Matthew Lyle Olson, Simon Stepputtis, Joseph Campbell
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.5815764095616
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1497/
- PDF: https://aclanthology.org/2026.acl-long.1497.pdf
- Local PDF: pdf/2026-11-02_16_Bayesian Social Deduction with Graph-Informed Language Models.pdf

Social reasoning—inferring unobservable beliefs and intentions from partial observations of other agents—remains a challenging task for large language models (LLMs). We evaluate the limits of current reasoning language models in the social deduction game Avalon and find that while the largest models demonstrate strong performance, they require extensive test-time inference and degrade sharply when distilled to smaller, real-time-capable variants. To address this, we introduce a hybrid reasoning framework that externalizes belief inference to a structured probabilistic model, while using an LLM for language understanding and interaction. Our approach achieves competitive performance with much larger models in Agent-Agent play and, notably, is the first language agent to defeat human players in a controlled study—achieving a 67% win rate and receiving higher qualitative ratings than both reasoning baselines and human teammates. We release code, models, and a dataset to support future work on social reasoning in LLM agents.

## 17. What If Consensus Lies? Selective-Complementary Reinforcement Learning at Test Time

- Authors: Dong Yan, Jian Liang, Yanbo Wang, Shuo Lu, Ran He, Tieniu Tan
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.58112128908891
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1337/
- PDF: https://aclanthology.org/2026.acl-long.1337.pdf
- Local PDF: pdf/2026-11-02_17_What If Consensus Lies_ Selective-Complementary Reinforcement Learning at Test Time.pdf

Test-Time Reinforcement Learning (TTRL) enables Large Language Models (LLMs) to enhance reasoning capabilities on unlabeled test streams by deriving pseudo-rewards from majority voting consensus.However, existing TTRL methods rely exclusively on positive pseudo-labeling strategies.Such reliance becomes vulnerable under challenging scenarios where answer distributions are highly dispersed, resulting in weak consensus that inadvertently reinforces incorrect trajectories as supervision signals.In this paper, we propose SCRL (Selective-Complementary Reinforcement Learning), a robust test-time reinforcement learning framework that effectively mitigates label noise amplification.SCRL develops Selective Positive Pseudo-Labeling, which enforces strict consensus criteria to filter unreliable majorities. Complementarily, SCRL introduces Entropy-Gated Negative Pseudo-Labeling, the first negative supervision mechanism in TTRL, to reliably prune incorrect trajectories based on generation uncertainty. Extensive experiments on mathematical reasoning benchmarks demonstrate that SCRL achieves substantial improvements over baselines, while maintaining robust generalization and training stability under constrained rollout budgets.

## 18. OjaKV: Context-Aware Online Low-Rank KV Cache Compression

- Authors: Yuxuan Zhu, David H. Yang, Mohammad Mohammadi Amiri, Keerthiram Murugesan, Tejaswini Pedapati, Pin-Yu Chen
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.5805269532680715
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.494/
- PDF: https://aclanthology.org/2026.findings-acl.494.pdf
- Local PDF: pdf/2026-11-02_18_OjaKV_ Context-Aware Online Low-Rank KV Cache Compression.pdf

The expanding long-context capabilities of large language models are constrained by a significant memory bottleneck: the key-value (KV) cache required for autoregressive generation. This bottleneck is substantial; for instance, a Llama-3.1-8B model processing a 32K-token prompt at a batch size of 4 requires approximately 16 GB for its KV cache, exceeding the model’s weights. While KV-cache compression via low-rank projection is promising, existing methods rely on a static, offline-learned subspace that performs poorly under distribution shifts. To overcome these limitations, we introduce OjaKV, a novel framework integrating a hybrid storage policy with online subspace adaptation. OjaKV preserves crucial tokens in full rank as high-fidelity anchors, while applying low-rank compression to intermediate tokens by adapting the projection basis using Oja’s algorithm for online PCA. This adaptation involves a comprehensive update during prefilling and lightweight periodic updates during decoding, ensuring the subspace remains aligned with evolving context. Our framework is fully compatible with FlashAttention. Experiments demonstrate that OjaKV maintains or improves zero-shot accuracy at high compression ratios, achieving the strongest gains on long-context benchmarks requiring complex reasoning. Furthermore, our approach combines with token-selection methods for compounded memory savings, establishing a practical, plug-and-play solution for memory-efficient long-context inference without fine-tuning.

## 19. DuIVRS-2: An LLM-based Interactive Voice Response System for Large-scale POI Attribute Acquisition

- Authors: Le Zhang, Shengming Zhang, Rui Zha, Wu Yunpeng, Jingbo Zhou, Jizhou Huang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.580370575987457
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-industry.44/
- PDF: https://aclanthology.org/2026.acl-industry.44.pdf
- Local PDF: pdf/2026-11-02_19_DuIVRS-2_ An LLM-based Interactive Voice Response System for Large-scale POI Attribute Acquisition.pdf

Accurate Point of Interest (POI) attribute acquisition is essential for location-based services, yet traditional modular Interactive Voice Response (IVR) systems suffer from error accumulation and high maintenance overhead. We present DuIVRS-2, a large language model (LLM)-based end-to-end framework designed for large-scale POI attribute acquisition at Baidu Maps. To address the long-tail distribution of real-world interactions, our methodology first employs a finite state machine (FSM)-guided data augmentation strategy to synthesize a balanced and diverse training dataset. We then streamline dialogue management via a selective generation scheme combined with a Chain-of-Thought (CoT) mechanism, which ensures output stability and effectively eliminates hallucinations in industrial settings. To facilitate continuous policy refinement with minimal manual effort, we design a cooperative iterative learning framework that leverages a dual-evaluator voting system. Deployed in production for two months, DuIVRS-2 processed 0.4 million calls daily and achieved a 83.9% Task Success Rate (TSR), outperforming its predecessor by 4 percentage points while maintaining a low reaction time of 130ms. This work provides a production-proven reference for developing robust, cost-effective LLM agents for large-scale industrial dialogue applications.

## 20. BracketRank: Large Language Model Document Ranking via Reasoning-based Competitive Elimination

- Authors: Abdelrahman Abdallah, Mohammed Ali, Bhawna Piryani, Adam Jatowt
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.5803154082730515
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.153/
- PDF: https://aclanthology.org/2026.acl-long.153.pdf
- Local PDF: pdf/2026-11-02_20_BracketRank_ Large Language Model Document Ranking via Reasoning-based Competitive Elimination.pdf

Although Large Language Models (LLMs) show strong potential for zero-shot document ranking, current listwise approaches face three critical limitations. First, context length constraints prevent processing many documents simultaneously. Second, sequential generation creates bottlenecks that cannot run in parallel. Third, ranking results depend heavily on initial document order, leading to inconsistent performance. We introduce BracketRank, a reasoning-driven competitive elimination framework that addresses these challenges through systematic group competition. Our method uses adaptive grouping to automatically optimise group sizes based on LLM context limits, reasoning-enhanced prompts that require explicit relevance explanations, and bracket-style elimination where documents compete through winner and loser brackets. This structure ensures every document has fair advancement opportunities regardless of initial positioning while allowing for parallel processing across competition stages. We evaluate BracketRank on TREC DL 19, TREC DL 20, and eight BEIR benchmark datasets. Results show that BracketRank achieves 77.90 NDCG@5 on TREC DL 19 and 75.85 NDCG@5 on TREC DL 20, outperforming RankGPT and other state-of-the-art methods. On BEIR datasets, BracketRank reaches 54.66 average NDCG@10, demonstrating robust performance across diverse domains.

## 21. Red Teaming Large Reasoning Models

- Authors: Jiawei Chen, Yang Yang, Chao Yu, Yu Tian, Zhi Cao, Xue Yang, Linghao Li, Hang Su, Zhaoxia Yin
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.5796955888827804
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1034/
- PDF: https://aclanthology.org/2026.acl-long.1034.pdf
- Local PDF: pdf/2026-11-02_21_Red Teaming Large Reasoning Models.pdf

Large Reasoning Models (LRMs) have emerged as a powerful advancement in multi-step reasoning tasks, offering enhanced transparency and logical consistency through explicit chains of thought (CoT). However, these models introduce novel safety and reliability risks, such as CoT-hijacking and prompt-induced inefficiencies, which are not fully captured by existing evaluation methods. To address this gap, we propose Rt-LRM, a unified benchmark designed to assess the trustworthiness of LRMs. Rt-LRM evaluates three core dimensions: truthfulness, safety and efficiency. Beyond metric-based evaluation, we further introduce the training paradigm as a key analytical perspective to investigate the systematic impact of different training strategies on model trustworthiness. We achieve this by designing a curated suite of 30 reasoning tasks from an observational standpoint. We conduct extensive experiments on 26 models and identify several valuable insights into the trustworthiness of LRMs. For example, LRMs generally face trustworthiness challenges and tend to be more fragile than Large Language Models (LLMs) when encountering reasoning-induced risks. These findings uncover previously underexplored vulnerabilities and highlight the need for more targeted evaluations. In addition, we release a scalable toolbox for standardized trustworthiness research to support future advancements in this important field.

## 22. Towards Reliable Paper Contributions Annotation in the ACL Rolling Review

- Authors: Julien Aubert-Béduchaud, Florian Boudin, Akiko Aizawa, Beatrice Daille, Richard Dufour
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.579460295352001
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.178/
- PDF: https://aclanthology.org/2026.findings-acl.178.pdf
- Local PDF: pdf/2026-11-02_22_Towards Reliable Paper Contributions Annotation in the ACL Rolling Review.pdf

With the rapid growth of scientific publications, researchers struggle to efficiently assess the relevance of numerous papers. Identifying the types of contributions an article makes can help readers quickly grasp its significance. The ACL Rolling Review (ARR) introduced a typology requiring authors to specify their contributions to improve review quality and fairness. However, the current typology lacks clear definitions and guidance, leading to inconsistent labeling and raising concerns about its reliability.Our re-annotation campaign reveals substantial disagreement between authors and domain experts. Moreover, the predictions of large language models (LLMs), when compared with expert annotations, tend to be close to those provided by the authors. These findings suggest a potential path toward better annotation reliability within the ARR process.

## 23. FastKV: Decoupling of Context Reduction and KV Cache Compression for Prefill-Decoding Acceleration

- Authors: Dongwon Jo, Jiwon Song, Yulhwa Kim, Jae-Joon Kim
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.5793735931472126
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1610/
- PDF: https://aclanthology.org/2026.findings-acl.1610.pdf
- Local PDF: pdf/2026-11-02_23_FastKV_ Decoupling of Context Reduction and KV Cache Compression for Prefill-Decoding Acceleration.pdf

While large language models (LLMs) excel at handling long-context sequences, they require substantial prefill computation and key-value (KV) cache, which can heavily burden computational efficiency and memory usage in both prefill and decoding stages.Recent works that compress KV caches with prefill acceleration reduce this cost but inadvertently tie the prefill compute reduction to the decoding KV budget. This coupling arises from overlooking the layer-dependent variation of critical context, often leading to accuracy degradation. To address this issue, we introduce FastKV, a KV cache compression framework designed to reduce latency in both prefill and decoding by leveraging the stabilization of token importance in later layers.FastKV performs full-context computation until a Token-Selective Propagation (TSP) layer, which forwards only the most informative tokens to subsequent layers.From these propagated tokens, FastKV independently selects salient KV entries for caching, thereby decoupling KV budget from the prefill compute reduction based on the TSP decision.This independent control of the TSP rate and KV retention rate enables flexible optimization of efficiency and accuracy.Experimental results show that FastKV achieves speedups of up to 1.82 × in prefill and 2.87 × in decoding compared to the full-context baseline, while matching the accuracy of the decoding-only baselines.Our code is available at https://github.com/dongwonjo/FastKV .

## 24. CaBSALLM: Efficient Context-Aware Batch Annotation of Conversational Streams with Large Language Models

- Authors: Mohammadsadegh Abolhasani, Reza Mousavi, Paul Jen-Hwa Hu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.57931793838645
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-short.51/
- PDF: https://aclanthology.org/2026.acl-short.51.pdf
- Local PDF: pdf/2026-11-02_24_CaBSALLM_ Efficient Context-Aware Batch Annotation of Conversational Streams with Large Language Models.pdf

Analyses of parasocial cues in live-stream chats require accurate, efficient, and scalable annotation. However, manual annotation is tedious, and large language models (LLMs) often make mistakes when applying subjective, discourse-dependent labels. This study proposes Context-aware Batching for Stream Annotation with LLMs (CaBSALLM), an efficient pipeline that incorporates lightweight conversational context and a novel dynamic batching method to improve throughput and scalability. Compared with state-of-the-art pipelines, this generalizable approach is significantly more time- and cost-efficient while achieving comparable or better predictive performance and agreement.

## 25. MINTQA: A Multi-Hop Question Answering Benchmark for Evaluating LLMs on New and Long-tail Knowledge

- Authors: Jie He, Nan Hu, Wanqiu Long, Jiaoyan Chen, Jeff Z. Pan
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.5792751665849654
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.18/
- PDF: https://aclanthology.org/2026.acl-long.18.pdf
- Local PDF: pdf/2026-11-02_25_MINTQA_ A Multi-Hop Question Answering Benchmark for Evaluating LLMs on New and Long-tail Knowledge.pdf

Retrieval-Augmented Generation (RAG) enhances large language models (LLMs) by integrating external knowledge, enabling them to tackle knowledge-intensive tasks. However, limited research has explored how LLMs effectively leverage RAG techniques for multi-hop question answering (QA), particularly when handling knowledge with with varying degrees of familiarity. In this paper, we introduce MINTQA (Multi-hop Question Answering on New and Tail Knowledge), a benchmark designed to evaluate multi-hop QA performance on questions involving 10,479 question-answer pairs for evaluating old/new knowledge and 17,887 pairs for assessing popular/unpopular knowledge, with each question equipped with corresponding sub-questions and answers. This benchmark primarily evaluates the multi-hop reasoning ability of LLMs and their capacity to handle knowledge with varying levels of familiarity during the reasoning process. We evaluate 22 state-of-the-art LLMs using three distinct QA strategies: LLM-based parameterized knowledge QA, direct RAG-enhanced QA, and multi-hop RAG-enhanced QA. Our experiments reveal key challenges in how LLMs handle knowledge with different familiarity and offer insights into improving their multi-hop reasoning capabilities when combined with RAG techniques.

## 26. Erasing Without Remembering: Implicit Knowledge Forgetting in Large Language Models

- Authors: Huazheng Wang, Yongcheng Jing, Haifeng Sun, Yingjie Wang, Jingyu Wang, Jianxin Liao, Dacheng Tao
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.5792457981795067
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.88/
- PDF: https://aclanthology.org/2026.acl-long.88.pdf
- Local PDF: pdf/2026-11-02_26_Erasing Without Remembering_ Implicit Knowledge Forgetting in Large Language Models.pdf

In this paper, we investigate knowledge forgetting in large language models with a focus on its generalisation—ensuring that models forget not only specific training samples but also related implicit knowledge. To this end, we begin by identifying a broader unlearning scope that includes both target data and logically associated samples, including rephrased, subject-replaced, relation-reversed, and one-hop reasoned data. We then conduct a rigorous evaluation of 15 state-of-the-art methods across three datasets, revealing that unlearned models still recall paraphrased answers and retain target facts in their intermediate layers. This motivates us to take a preliminary step toward more generalised implicit knowledge forgetting by proposing PERMU—a novel probability perturbation-based unlearning paradigm. PERMU simulates adversarial unlearning samples to eliminate fact-related tokens from the logit distribution, collectively reducing the probabilities of all answer-associated tokens. Experiments are conducted on a diverse range of datasets, including TOFU, Harry Potter, ZsRE, WMDP, and MUSE, using models ranging from 1.3B to 13B in scale. The results demonstrate that PERMU delivers up to a 50.40% improvement in unlearning vanilla target data while maintaining a 40.73% boost in forgetting implicit knowledge. Our code can be found in the supplementary material.

## 27. Reason-Code: Reliable Code Generation via Test-Driven Monte Carlo Tree Search

- Authors: Zixu Li, Zhiqi Peng
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.5790687048307688
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-industry.30/
- PDF: https://aclanthology.org/2026.acl-industry.30.pdf
- Local PDF: pdf/2026-11-02_27_Reason-Code_ Reliable Code Generation via Test-Driven Monte Carlo Tree Search.pdf

Large Language Models (LLMs) are widely used for code generation, but their performance degrades on tasks requiring multi-step logical reasoning. In practice, reliability is often improved through multi-sample inference, but its cost grows linearly with the sample size, making it impractical under strict latency constraints. To address this, we propose Reason-Code, an inference-time framework that formulates code generation as a search process guided by execution feedback. It integrates Monte Carlo Tree Search (MCTS) with a lightweight execution sandbox, where candidate programs are evaluated via unit tests. To control inference cost, Reason-Code adopts a conditional budgeting strategy that activates search only when greedy generation fails. Compared with large-sample Best-of- N sampling, Reason-Code is designed to improve reliability without paying the full linear cost of additional sampling under strict latency budgets. Experiments on HumanEval and MBPP show that Reason-Code matches strong sampling baselines (e.g., Best-of-10) with lower token cost and no regression. Additional matched-budget analyses show that execution-guided adaptive inference improves over independent sampling/filtering baselines, while differences between UCB-guided search and simpler iterative repair are limited at low budget.

## 28. Advancing Reasoning in Diffusion Language Models with Denoising Process Rewards

- Authors: Shaoan Xie, Lingjing Kong, Xiangchen Song, Xinshuai Dong, Guangyi Chen, Eric P. Xing, Kun Zhang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.5787427166562726
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1978/
- PDF: https://aclanthology.org/2026.acl-long.1978.pdf
- Local PDF: pdf/2026-11-02_28_Advancing Reasoning in Diffusion Language Models with Denoising Process Rewards.pdf

Diffusion-based large language models offer a non-autoregressive alternative for text generation, but enabling them to perform complex reasoning remains challenging. Reinforcement learning has recently emerged as an effective post-training strategy for improving their performance; however, existing methods rely primarily on outcome-based rewards, which provide no direct supervision over the denoising process and often result in poorly structured reasoning that is difficult to interpret and inconsistently supports the final prediction. To address this limitation, we introduce denoising process reward , a process-level reinforcement signal defined over the denoising trajectory of diffusion language models. This reward is obtained by estimating the contribution of intermediate denoising intervals to the final task outcome, encouraging the model to favor reasoning trajectories that consistently guide generation toward correct predictions. We further propose an efficient stochastic estimator that reuses standard training rollouts, enabling practical process-level supervision at scale. Experiments on challenging reasoning benchmarks demonstrate that our approach yields consistent improvements in reasoning stability, interpretability, and overall task performance.

## 29. Efficient Transformer Parameter Reuse via Zero-Token Mechanism

- Authors: Guanghao Li, Wenhao Jiang, Li Shen, Ming Tang, Chun Yuan
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.578187622397924
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.711/
- PDF: https://aclanthology.org/2026.findings-acl.711.pdf
- Local PDF: pdf/2026-11-02_29_Efficient Transformer Parameter Reuse via Zero-Token Mechanism.pdf

Resource constraints often limit the parameter capacity of Large Language Models (LLMs), thereby hindering their performance. Although existing approaches leverage parameter sharing to reuse a fixed set of parameters within constrained budgets, they typically require each layer to fulfill multiple roles over a fixed number of iterations. This design compromises both efficiency and adaptability. In this work, we propose the Zero Token Transformer (ZTT) , which employs a head-tail decoupled parameter cycling strategy. Specifically, we decouple the first (head) and last (tail) layers from the parameter cycling process, enabling iterative refinement solely within the intermediate layers. Furthermore, we introduce a Zero-Token Mechanism, wherein a virtual token with a trainable key and a zero-valued vector functions as a standard token. The resulting attention scores not only reflect the computational significance of each layer but also facilitate dynamic early exiting, thereby preserving overall model accuracy. Our approach achieves superior performance under strict parameter constraints, substantially reduces computational overhead via early exits, and can be seamlessly integrated into the fine-tuning of existing pre-trained models, improving both efficiency and adaptability.

## 30. Beyond Polarity: Continuous Affect-Enhanced Multimodal Aspect-Based Sentiment Classification

- Authors: Ling-Ang Meng, Tianyu Zhao, Dawei Song, Jingxu Cao, Youhui Zuo
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.578046574262264
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1979/
- PDF: https://aclanthology.org/2026.findings-acl.1979.pdf
- Local PDF: pdf/2026-11-02_30_Beyond Polarity_ Continuous Affect-Enhanced Multimodal Aspect-Based Sentiment Classification.pdf

Multimodal aspect-based sentiment classification (MABSC) requires aspect-level sentiment inference from textual-image data that jointly convey opinions. Yet most existing approaches primarily exploit discrete polarity patterns and generic visual embeddings, making them less effective when the affect is subtle, implicit, or expressed through imagery. In this work, we propose VADE , a Valence–Arousal–Dominance ~( VAD )- E nhanced MABSC framework that brings continuous VAD signals into multimodal sentiment reasoning and learns emotion-sensitive image representations. Specifically, we design a VAD encoder to extract continuous affect cues from text for aspect-level sentiment reasoning. Furthermore, we fine-tune a CLIP-based image encoder on affect-enriched image–text pairs to obtain visual representations that are more sensitive to sentiment cues. To support the fine-tuning process, we construct an affect-enriched image–text dataset Senti-COCO by rewriting MSCOCO captions with a multimodal large language model, which yields large-scale image-text pairs with richer affective expressions. Experiments on two mainstream datasets, Twitter-15 and Twitter-17, show that VADE achieves a new state-of-the-art performance, demonstrating the effectiveness of incorporating VAD signals for MABSC.
