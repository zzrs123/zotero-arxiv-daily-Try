# Paper Daily Reading - 2026-09-15

## 1. DCRA: Diffusion-Conditioned Representation Alignment for Robust Time-Series Learning

- Authors: Wenrui Xu, Anas Enanaa, Keshab K. Parhi
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-09
- DOI: Unavailable
- Categories: cs.LG, stat.ML
- Relevance: 2.8382070628527885
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.11997v1
- PDF: https://arxiv.org/pdf/2609.11997v1
- Local PDF: pdf/2026-09-15_01_DCRA_ Diffusion-Conditioned Representation Alignment for Robust Time-Series Learning.pdf

Learning robust representations for time-series signals under noise and distribution shifts remains challenging, especially in clinical applications such as electroencephalogram (EEG) and electrocardiogram (ECG) analysis. We propose Diffusion-Conditioned Representation Alignment (DCRA), a training framework that repurposes the forward diffusion process as a structured corruption scheduler for representation learning. Different from conventional augmentation and consistency-based methods that rely on independently sampled perturbations, DCRA introduces a structured corruption trajectory via the diffusion forward process, which enables continuous and controlled representation evolution across noise levels. We introduce a feature-level consistency objective that aligns representations across noise levels while preserving class-discriminative structure. This mechanism promotes structure-preserving consistency, which enables smooth and semantically coherent feature trajectories in latent space. The proposed framework is encoder-agnostic and can be integrated with state space models and Transformer architectures. The seizure detection experiments on the CHB-MIT EEG dataset show that DCRA consistently improves performance under multiple noise conditions and achieves higher sensitivity at low false-positive rates. Analysis reveals that DCRA produces more balanced and structured representations compared to baseline and diffusion-only models. These findings highlight the benefit of combining structured corruption with representation alignment for robust time-series learning.

## 2. Fixed State, Long Reach: What a Constant-Size Cache Buys Block Diffusion at Scale

- Authors: Vaibhav Singh, Pierre-André Noël, Torsten Scholak, Eugene Belilovsky, Oleksiy Ostapenko
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-09
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 2.8167945683699296
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.11998v1
- PDF: https://arxiv.org/pdf/2609.11998v1
- Local PDF: pdf/2026-09-15_02_Fixed State, Long Reach_ What a Constant-Size Cache Buys Block Diffusion at Scale.pdf

Diffusion language models decode tokens in parallel, but their bidirectional denoiser rules out the naive key--value (KV) cache behind fast autoregressive inference. Block diffusion restores caching by decoding block-by-block, and the block caches deployed on it so far are tied to attention: O(L)in memory and, if used as training-free retrofits, only an approximation of the model's computation. Both constraints can be overcome: sequence mixers that summarize finalized blocks into a reusable state support block caching, and the corresponding block-causal training objective makes the cache exact. We study this recipe at scale, pretraining three 3B block-diffusion denoisers (attention, mamba, and hybrid) on 300B tokens under one single-frontier objective and decoding all three through a single cached interface. Only the state-space cache is O(1) in sequence length: its memory and per-step latency stay constant at any context length, while an attention cache remains O(L). At 256k tokens (where attention has grown to 82GB and 29 ms/step), the Mamba cache delivers 4.3x lower latency, 11x less memory, and 2.6x higher single-stream throughput; and because that footprint is constant it scales with batch as well, reaching 14x the aggregate throughput, where attention cannot run beyond a single stream. The same linear-state bias lets the Mamba and hybrid backbones keep retrieving out to 8-16x their training length, whereas attention's retrieval collapses at 2x, at no measured quality cost.

## 3. Explainable Prediction from Mobile Sensing Data through LLM-guided Concept Integration

- Authors: Yuning Wang, Iman Azimi, Amir M. Rahmani, Pasi Liljeberg
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-09
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 2.7111606995945174
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.11995v1
- PDF: https://arxiv.org/pdf/2609.11995v1
- Local PDF: pdf/2026-09-15_03_Explainable Prediction from Mobile Sensing Data through LLM-guided Concept Integration.pdf

Mobile sensing enables longitudinal monitoring of behavioral and physiological patterns in everyday settings. However, accurate prediction remains challenging in small-cohort health-sensing studies, where task-specific outcome supervision is limited relative to heterogeneous sensing data. Interpretability is also important, as model outputs should reflect meaningful behavioral and physiological patterns rather than predictive scores alone. We develop a Concept-Integrated Transformer (CIT) with LLM-guided concept supervision for explainable prediction from mobile sensing data. CIT uses a pretrained large language model to generate baseline-aware concept abnormality targets with confidence weights without manual concept annotation. Across two longitudinal datasets, CIT achieves the highest F1 score on AFFECT (0.756) and ties for the highest on a PHQ-9 dataset (0.765). The learned concept scores also reveal interpretable behavioral and physiological patterns; in AFFECT, sleep quantity and quality show the clearest difference between high and low negative affect groups. These findings support LLM-guided concept integration for accurate and interpretable prediction in small-cohort mobile sensing studies.

## 4. Editing the Moving World: Model Editing for Video LLMs

- Authors: Qian Zhang, Xinye Li, Xiaokai Wu, Junhao Xu, Zhanyue Qin, Qingbin Liu, Junxian Cai, Xi Chen, Bolin Zhang, Zhiying Tu, Dianhui Chu, Xiaoyan Yu, Dianbo Sui
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.693974283605123
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.274/
- PDF: https://aclanthology.org/2026.acl-long.274.pdf
- Local PDF: pdf/2026-09-15_04_Editing the Moving World_ Model Editing for Video LLMs.pdf

Model Editing, also known as knowledge editing, is receiving increasing attention in the field of Large Language Models (LLMs). However, existing model editing approaches predominantly focus on knowledge-level or static visual domains, overlooking dynamic semantics. This paper exploratively applies six representative model editing methods (FT, IKE, MEND, SERAC, MEMIT and AlphaEdit) to Video Large Language Models (Vid-LLMs) and introduces the first benchmark specifically designed for Vid-LLMs editing—VMEB (Vid-LLMs Model Editing Benchmark)—systematically extending model editing research from static modalities to dynamic video scenarios. We position this work as a forward-looking benchmark and a foundational diagnostic study: in the video paradigm, our evaluation dimensions encompass traditional metrics including Reliability, Locality, and Generality, while also introducing a video-specific metric: Robustness. Based on experimental results, we analyze the strengths and limitations of existing model editing approaches, and identify new challenges and research directions for the future development of the model editing field within the context of multimodal and video paradigms. Our benchmark is available at https://github.com/Sakabamrisa/VMEB .

## 5. Can Large Language Models Keep Up? Benchmarking Online Adaptation to Continual Knowledge Streams

- Authors: Jiyeon Kim, Hyunji Lee, Dylan Zhou, Sue Hyun Park, Seunghyun Yoon, Trung Bui, Franck Dernoncourt, Sungmin Cha, Minjoon Seo
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.6932523483993487
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1956/
- PDF: https://aclanthology.org/2026.acl-long.1956.pdf
- Local PDF: pdf/2026-09-15_05_Can Large Language Models Keep Up_ Benchmarking Online Adaptation to Continual Knowledge Streams.pdf

LLMs operating in dynamic real-world contexts often encounter knowledge that evolves continuously or emerges incrementally. To remain accurate and effective, models must adapt to newly arriving information on the fly. We introduce Online Adaptation to Continual Knowledge Streams(OAKS) to evaluate this capability, establishing a benchmark for online adaptation over streaming, continually updating knowledge. Specifically, the benchmark is structured as a sequence of fine-grained context chunks where facts change dynamically across time intervals. OAKS comprises two datasets: OAKS-BABI and OAKS-Novel, where individual facts evolve multiple times across context chunks. These datasets include dense annotations to measure whether models track changes accurately. Evaluating 14 models with varied inference approaches, we observe significant limitations in current methodologies. Both state-of-the-art models and agentic memory systems fail to adapt robustly on OAKS, demonstrating delays in state-tracking and susceptibility to distraction within streaming environments. We will open-source the code and datasets.

## 6. CodeRise: Bootstrapping LLMs for Ultra Low-Resource Programming Languages via Progressive Self-Refinement Curriculum

- Authors: Tengfei Wen, Xuanang Chen, Ben He, Xiaoliang Cong, Le Sun
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.6921928061898015
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1840/
- PDF: https://aclanthology.org/2026.findings-acl.1840.pdf
- Local PDF: pdf/2026-09-15_06_CodeRise_ Bootstrapping LLMs for Ultra Low-Resource Programming Languages via Progressive Self-Refinement Curriculum.pdf

Large Language Models (LLMs) struggle with code generation for Ultra Low-Resource Programming Languages (ULRPLs) due to the scarcity of training data. Existing synthetic data generation methods fail in this context, suffering from a severe cold-start problem and resulting in samples that lack diversity. To overcome these challenges, we propose CodeRise, a novel two-stage framework that autonomously generates a high-quality, diverse, and progressively complex curriculum for ULRPLs. The framework first tackles the cold-start and distribution issues by leveraging the full formal syntax of the target language as structural guidance and applying a biased sampling strategy over library modules. Building on this foundation, we fine-tune the model to generate increasingly complex code without explicit syntax input, using an adaptive curriculum and multi-turn self-debugging to progressively improve code quality.We evaluate on two ULRPLs, Tengo and Janet, using migrated HumanEval-Tengo and MBPP-Tengo, as well as our new benchmarks, TengoEval and JanetEval. Experiments show that CodeRise significantly outperforms both training-free and training-based baselines in ultra low-resource environments.

## 7. Hi-ZFO: Hierarchical Zeroth- and First-Order LLM Fine-Tuning via Importance-Guided Tensor Selection

- Authors: Feihu Jin, Ying Tan
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.69213962667411
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.239/
- PDF: https://aclanthology.org/2026.findings-acl.239.pdf
- Local PDF: pdf/2026-09-15_07_Hi-ZFO_ Hierarchical Zeroth- and First-Order LLM Fine-Tuning via Importance-Guided Tensor Selection.pdf

Fine-tuning large language models (LLMs) using standard first-order (FO) optimization oftendrives training toward sharp, poorly generalizing minima. Conversely, zeroth-order (ZO) methods offer stronger exploratory behaviorwithout relying on explicit gradients, yet suffer from slow convergence. More critically, our analysis reveals that in generative tasks, the vast output and search space significantly amplify estimation variance, rendering ZO methods both noisy and inefficient. To address these challenges, we propose Hi-ZFO (Hierarchical Zeroth- and First-Order optimization), a hybrid framework designed to synergize the precision of FO gradients with the exploratory capability of ZO estimation. Hi-ZFO adaptively partitions the model through layer-wise importance profiling, applying precise FO updates to critical layers while leveraging ZO optimization for less sensitive ones. Notably, ZO in Hi-ZFO is not merely a memory-saving surrogate; it is intentionally introduced as a source of “beneficial stochasticity” to help the model escape the local minima where pure FO optimization tends to stagnate. Validated across diverse generative, mathematical, and code reasoning tasks, Hi-ZFO consistently achieves superior performance while significantly reducing the training time. These results demonstrate the effectiveness of hierarchical hybrid optimization for LLM fine-tuning.

## 8. Synthetic Data Generation for Training Diversified Commonsense Reasoning Models

- Authors: Tianhui Zhang, Bei Peng, Danushka Bollegala
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.6918202054005222
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1520/
- PDF: https://aclanthology.org/2026.acl-long.1520.pdf
- Local PDF: pdf/2026-09-15_08_Synthetic Data Generation for Training Diversified Commonsense Reasoning Models.pdf

Conversational agents are required to respond to their users not only with high quality (i.e. commonsense bearing) responses, but also considering multiple plausible alternative scenarios, reflecting the diversity in their responses. Despite the growing need to train diverse commonsense generators, the progress of this line of work has been significantly hindered by the lack of large-scale high-quality diverse commonsense training datasets. Due to the high annotation costs, existing Generative Commonsense Reasoning (GCR) datasets are created using a small number of human annotators, covering only a narrow set of commonsense scenarios. To address this training resource gap, we propose a two-stage method to create the first-ever synthetic dataset CommonSyn for diversified (GCR). The model fine-tuned on our synthetic data jointly increase both generation diversity and quality compared with vanilla models and the model fine-tuned on human-crafted dataset across different size Large Language Models (LLMs)

## 9. Can Small LLMs Learn a Robust Theory of Mind via RLVR? Investigating Generalization through the False-Belief Task

- Authors: Sneheel Sarangi, Hanan Salam
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.691727404683099
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.2061/
- PDF: https://aclanthology.org/2026.findings-acl.2061.pdf
- Local PDF: pdf/2026-09-15_09_Can Small LLMs Learn a Robust Theory of Mind via RLVR_ Investigating Generalization through the False-Belief Task.pdf

Recent advancements in large language models (LLMs) have demonstrated emergent capabilities in complex reasoning, largely spurred by rule-based Reinforcement Learning (RL) techniques applied during post-training. This has raised the question of whether similar methods can instill more nuanced, human-like social intelligence, such as a Theory of Mind (ToM), in LLMs. This paper investigates whether small- scale LLMs can acquire a robust and generalizable ToM capability through RL with verifiable rewards (RLVR). We conduct a systematic evaluation by training models on various combinations of prominent ToM benchmarks (HiToM, ExploreToM, FANToM) and testing for generalization on held-out benchmarks (e.g., Open- ToM). Our findings indicate that small LLMs struggle to develop a generic ToM capability. While performance on in-distribution tasks improves, this capability fails to transfer to unseen ToM tasks with different characteristics. Even observed out-of-distribution (OOD) performance improvements occur unpredictably across the training run, and don’t generalize across other OOD benchmarks. Furthermore, we conduct analysis to show that the learned behavior is likely a form of narrow overfitting rather than the acquisition of a true, abstract ToM capability.

## 10. Hail to the Thief: Exploring Attacks and Defenses in Decentralised GRPO

- Authors: Nikolay Blagoev, Oguzhan Ersoy, Lydia Chen
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.6916833747732993
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1950/
- PDF: https://aclanthology.org/2026.findings-acl.1950.pdf
- Local PDF: pdf/2026-09-15_10_Hail to the Thief_ Exploring Attacks and Defenses in Decentralised GRPO.pdf

Group Relative Policy Optimization (GRPO) has demonstrated wide adoption in the post-training of Large Language Models (LLMs). In GRPO, prompts are answered by the model and preferred behaviour is learnt via reinforcement learning. Owing to the small communication volume, GRPO is inherently suitable for decentralised training as the prompts can be concurrently answered by multiple nodes and these completions are exchanged in the form of strings. In this work, we explore the robustness of decentralised GRPO by presenting the first adversarial attacks and countermeasures. We present a diverse set of attacks where malicious nodes poison benign models by sharing their poisoned completions. We demonstrate these attacks on math and coding tasks and show that an adversary can achieve attack success rates of up to (100%) in as few as 50 iterations. Moreover, to mitigate the attacks, we propose two defense mechanisms that check logit probabilities of completions or utilize an LLM judge to filter completions. The defenses prevent all but the DoS attack that causes unnecessarily lengthy but conceptually correct completions. The code of both attacks and defenses can be found at: https://github.com/gensyn-ai/HTTT .

## 11. The Bitter Lesson of Diffusion Language Models for Agentic Workflows: A Comprehensive Reality Check

- Authors: Qingyu Lu, Liang Ding, Kanjian Zhang, Jinxia Zhang, Dacheng Tao
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.6916615995973228
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.2036/
- PDF: https://aclanthology.org/2026.acl-long.2036.pdf
- Local PDF: pdf/2026-09-15_11_The Bitter Lesson of Diffusion Language Models for Agentic Workflows_ A Comprehensive Reality Check.pdf

The pursuit of real-time agentic interaction has driven interest in Diffusion-based Large Language Models (dLLMs) as alternatives to auto-regressive backbones, promising to break the sequential latency bottleneck. However, does such efficiency gains translate into effective agentic behavior? In this work, we present a comprehensive evaluation of dLLMs (e.g., LLaDA, Dream) across two distinct agentic paradigms: Embodied Agents (requiring long-horizon planning) and Tool-Calling Agents (requiring precise formatting).Contrary to the efficiency hype, our results on Agentboard and BFCL reveal a “ bitter lesson ”: current dLLMs fail to serve as reliable agentic backbones, frequently leading to systematically failure. (1) In Embodied settings , dLLMs suffer repeated attempts, failing to branch under temporal feedback. (2) In Tool-Calling settings , dLLMs fail to maintain symbolic precision (e.g. strict JSON schemas) under diffusion noise. To assess the potential of dLLMs in agentic workflows, we introduce DiffuAgent , a multi-agent evaluation framework that integrates dLLMs as plug-and-play cognitive cores. Our analysis shows that dLLMs are effective in non-causal roles (e.g., memory summarization and tool selection) but require the incorporation of causal, precise, and logically grounded reasoning mechanisms into the denoising process to be viable for agentic tasks.

## 12. FARSS: Fisher-Optimized Adaptive Low-Rank and Singular-Vector Selection for Knowledge-Preserving Fine-Tuning

- Authors: Renxing Chen, Ziwei Xiang, Peisong Wang, Hongjian Fang, Meng Li, Fanhu Zeng, Yanan Zhu, Peipei Yang, Xu-Yao Zhang, Jian Cheng
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.6916509347939988
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.883/
- PDF: https://aclanthology.org/2026.findings-acl.883.pdf
- Local PDF: pdf/2026-09-15_12_FARSS_ Fisher-Optimized Adaptive Low-Rank and Singular-Vector Selection for Knowledge-Preserving Fine-Tuning.pdf

Parameter-efficient fine-tuning (PEFT) has become a prevalent approach for adapting large language models (LLMs). However, low-rank adaptation methods face an inherent trade-off: improving target task performance can compromise pre-trained world knowledge, while aggressively constraining updates to preserve world knowledge may hinder improvements in the target task. Furthermore, most current methods fail to account for layer-wise differences in adaptation sensitivity, resulting in suboptimal preservation of world knowledge and task adaptation. To address these challenge, we propose Fisher-Optimized Adaptive Low Rank and Singular-VectorSelection (FARSS), an effective framework for knowledge-preserving fine-tuning. This framework introduces two key innovations. First, we propose a Fisher-guided adaptive rank allocation strategy, which assigns smaller ranks to shallow layers that are critical for preserving world knowledge, and larger ranks to deep layers that are essential for task adaptation. Second, we introduce a task-aware initialization method that integrates singular value information with layer-specific second-order statistics estimated from activation and gradient covariances, enabling efficient and task-sensitive low-rank updates. We evaluated several models across various tasks, and the experimental results show that our approach outperforms existing PEFT methods, including LoRA, Corda, and KaSA, achieving a balance between preserving world knowledge and enhancing target task performance. The code is available at https://github.com/chenyehuang/FARSS .

## 13. DaMo: Data Mixing Optimizer in Fine-tuning Multimodal LLMs for Mobile Phone Agents

- Authors: Kai Shi, Jun Yang, Ni Yang, Binqiang Pan, Qingsong Xie, Zhangchao, Zhenyu Yang, Tianhuang Su, Haonan Lu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.691158232605132
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1439/
- PDF: https://aclanthology.org/2026.findings-acl.1439.pdf
- Local PDF: pdf/2026-09-15_13_DaMo_ Data Mixing Optimizer in Fine-tuning Multimodal LLMs for Mobile Phone Agents.pdf

Mobile Phone Agents (MPAs) have emerged as a promising research direction due to their broad applicability across diverse scenarios. While Multimodal Large Language Models (MLLMs) serve as the foundation for MPAs, their effectiveness in handling multiple mobile phone tasks simultaneously remains limited. Although multitask supervised fine-tuning (SFT) is widely adopted for multitask learning, existing approaches struggle to determine optimal training data compositions for peak performance. To address this challenge, we propose DaMo (Data Mixture Optimizer) – a novel solution employing a trainable network that predicts optimal data mixtures by forecasting downstream task performance for any given dataset ratio. To support comprehensive evaluation, we introduce PhoneAgentBench, the first specialized benchmark to evaluate MLLMs on multimodal mobile phone tasks, comprising 1,235 QA pairs spanning diverse real-world industrial mobile application scenarios. Demonstrating strong predictive capability (R²=0.81) in small-scale pilot experiments, DaMo efficiently extrapolates optimal data mixing configurations. Our results show DaMo achieves 3.06% average score improvement on PhoneAgentBench and open-source benchmarks, including BFCL-v3, MME-Reasoning, MME-Perception, and OCRBench, compared to alternative methods. Through predicting optimal data mixture only on open-source benchmarks, DaMo outperforms other approaches by 6.70% in terms of average score. Moreover, DaMo improves the metrics by 12.74% than other methods when used solely for MLLM optimization on the BFCL-v3 task. Notably, DaMo maintains robust scalability, preserving its effectiveness when applied to other model architectures.

## 14. SOCIA-EVO: Automated Simulator Construction via Dual-Anchored Bi-Level Optimization

- Authors: Yuncheng Hua, Sion Weatherhead, Mehdi Jafari, Hao Xue, Flora D. Salim
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.6908641019256283
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1274/
- PDF: https://aclanthology.org/2026.acl-long.1274.pdf
- Local PDF: pdf/2026-09-15_14_SOCIA-EVO_ Automated Simulator Construction via Dual-Anchored Bi-Level Optimization.pdf

Automated simulator construction requires distributional fidelity, distinguishing it from generic code generation. We identify two failure modes in long-horizon LLM agents: contextual drift and optimization instability arising from conflating structural and parametric errors. We propose SOCIA-EVO, a dual-anchored evolutionary framework. SOCIA-EVO introduces: (1) a static blueprint to enforce empirical constraints; (2) a bi-level optimization to decouple structural refinement from parameter calibration; and (3) a self-curating Strategy Playbook that manages remedial hypotheses via Bayesian-weighted retrieval. By falsifying ineffective strategies through execution feedback, SOCIA-EVO achieves robust convergence, generating simulators that are statistically consistent with observational data. SOCIA-EVO’s code and data are available here: https://github.com/cruiseresearchgroup/SOCIA/tree/evo .

## 15. TiMem: Temporal-Hierarchical Memory Consolidation for Long-Horizon Conversational Agents

- Authors: Kai Li, Xuanqing Yu, Ziyi Ni, Yi Zeng, Yao Xu, Zheqing Zhang, Xin Li, Jitao Sang, Xiaogang Duan, Xuelei Wang, Chengbao Liu, Jie Tan
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.6908199876936134
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1091/
- PDF: https://aclanthology.org/2026.findings-acl.1091.pdf
- Local PDF: pdf/2026-09-15_15_TiMem_ Temporal-Hierarchical Memory Consolidation for Long-Horizon Conversational Agents.pdf

Long-horizon conversational agents have to manage ever-growing interaction histories that quickly exceed the finite context windows of large language models (LLMs). Existing memory frameworks provide limited support for temporally structured information across hierarchical levels, often leading to fragmented memories and unstable long-horizon personalization. We present TiMem, a temporal–hierarchical memory framework that organizes conversations through a Temporal Memory Tree (TMT), enabling systematic memory consolidation from raw conversational observations to progressively abstracted persona representations. TiMem is characterized by three core properties: (1) temporal–hierarchical organization through TMT; (2) semantic-guided consolidation that enables memory integration across hierarchical levels without fine-tuning; and (3) complexity-aware memory recall that balances precision and efficiency across queries of varying complexity. Under a consistent evaluation setup, TiMem achieves state-of-the-art accuracy on both benchmarks, reaching 75.30% on LoCoMo and 76.88% on LongMemEval-S. It outperforms all evaluated baselines while reducing the recalled memory length by 52.20% on LoCoMo. Manifold analysis indicates clear persona separation on LoCoMo and reduced dispersion on LongMemEval-S. Overall, TiMem treats temporal continuity as a first-class organizing principle for long-horizon memory in conversational agents. The code is available at https://github.com/TiMEM-AI/timem .

## 16. SOLAR-RL: Semi-Online Long-horizon Assignment Reinforcement Learning

- Authors: Jichao Wang, Liuyang Bian, Yufeng Zhou, Han Xiao, Yue Pan, Guozhi Wang, Hao Wang, Zhaoxiong Wang, Yafei Wen, Xiaoxin Chen, Shuai Ren, Lingfang Zeng
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.690740358522774
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1222/
- PDF: https://aclanthology.org/2026.findings-acl.1222.pdf
- Local PDF: pdf/2026-09-15_16_SOLAR-RL_ Semi-Online Long-horizon Assignment Reinforcement Learning.pdf

As Multimodal Large Language Models (MLLMs) mature, GUI agents are evolving from static interactions to complex navigation. While Reinforcement Learning (RL) has emerged as a promising paradigm for training MLLM agents on dynamic GUI tasks, its effective application faces a dilemma.Standard Offline RL often relies on static step-level data, neglecting global trajectory semantics such as task completion and execution quality. Conversely, Online RL captures the long-term dynamics but suffers from high interaction costs and potential environmental instability. To bridge this gap, we propose SOLAR-RL (Semi Online Long-horizon RL). Instead of relying solely on expensive online interactions, our framework integrates global trajectory insights directly into the offline learning process. Specifically, we reconstruct diverse rollout candidates from static data, detect the first failure point using per-step validity signals, and retroactively assign dense step-level rewards with target-aligned shaping to reflect trajectory-level execution quality—effectively simulating online feedback without interaction costs.Extensive experiments demonstrate that SOLAR-RL significantly improves long-horizon task completion rates and robustness compared to strong baselines, offering a sample-efficient solution for autonomous GUI navigation.

## 17. GCA Framework: A GCC Countries–Grounded Dataset and Agentic Pipeline for Climate Decision Support

- Authors: Muhammad Umer Sheikh, Khawar Shehzad, Salman Khan, Fahad Shahbaz Khan, Muhammad Haris Khan
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.6904637890829
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1967/
- PDF: https://aclanthology.org/2026.acl-long.1967.pdf
- Local PDF: pdf/2026-09-15_17_GCA Framework_ A GCC Countries–Grounded Dataset and Agentic Pipeline for Climate Decision Support.pdf

Climate decision-making in the GCC states increasingly demands systems that can translate heterogeneous scientific and policy evidence into actionable guidance, yet general-purpose large language models (LLMs) remain weak both in region-specific climate knowledge and grounded interaction with geospatial and forecasting tools. We present the GCA framework, which unifies (i) GCA-DS, a curated multimodal dataset grounded in the GCC states, and (ii) Gulf Climate Agent (GCA), a tool-augmented agent for climate analysis. GCA-DS comprises nearly 200k question-answer pairs spanning governmental policies and adaptation plans, NGO and international frameworks, academic literature, and event-driven reporting on heatwaves, dust storms, and floods, complemented with remote-sensing inputs that couple imagery with textual evidence. Building on this foundation, the GCA agent orchestrates a modular tool pipeline grounded in real-time and historical signals and geospatial processing that produces derived indices and interpretable visualizations. Finally, we benchmark open and proprietary LLMs on climate tasks in the GCC states and show that domain fine-tuning and tool integration substantially improve reliability over general-purpose baselines.

## 18. MM-ShiftKV: Decode-Aware Prefill-Stage KV Selection for Multimodal Large Language Models

- Authors: Jinsong Shu, Chenyang Wu, Zhongle Xie, Baokun Wang, Lidan Shou
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.690453701755071
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1447/
- PDF: https://aclanthology.org/2026.findings-acl.1447.pdf
- Local PDF: pdf/2026-09-15_18_MM-ShiftKV_ Decode-Aware Prefill-Stage KV Selection for Multimodal Large Language Models.pdf

Key-Value (KV) caching is essential for efficient inference in multimodal large language models (MLLMs), yet its memory footprint grows linearly with context length and becomes a major bottleneck due to the large number of visual tokens. Recent prefill-stage KV selection methods estimate KV importance from prefilling statistics, implicitly assuming that prefilling-time queries are representative of those encountered during decoding. We show that this assumption breaks down in multimodal inference, where decoding-time queries exhibit substantially larger variance than prefilling-stage representations, leading to unstable KV importance estimation under tight cache budgets. As a result, small ranking errors can disproportionately discard semantically critical visual tokens and degrade grounding and reasoning performance. We propose MM-ShiftKV, a training-free, decode-aware and strictly prefill-only KV selection method. MM-ShiftKV approximates decoding-time query behavior during prefilling by constructing variance-expanded query proxies and estimates prompt KV importance based on their aggregated attention mass. Experiments on multimodal benchmarks demonstrate that MM-ShiftKV consistently outperforms existing methods under strict KV-cache budgets.

## 19. CoTEvol: Self-Evolving Chain-of-Thoughts for Data Synthesis in Mathematical Reasoning

- Authors: Zhuo Wang, Zhuo Zhang, Yafu Li, Yu Cheng, Lizhen Qu, Zenglin Xu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.689862196254913
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1903/
- PDF: https://aclanthology.org/2026.findings-acl.1903.pdf
- Local PDF: pdf/2026-09-15_19_CoTEvol_ Self-Evolving Chain-of-Thoughts for Data Synthesis in Mathematical Reasoning.pdf

Large Language Models (LLMs) exhibit strong mathematical reasoning when trained on high-quality Chain-of-Thought (CoT) that articulates intermediate steps, yet costly CoT curation hinders further progress. While existing remedies such as distillation from stronger LLMs and self-synthesis based on test-time search alleviate this issue, they often suffer from diminishing returns or high computing overhead. In this work, we propose CoTEvol, a genetic evolutionary framework that casts CoT generation as a population-based search over reasoning trajectories. Candidate trajectories are iteratively evolved through reflective global crossover at the trajectory level and local mutation guided by uncertainty at the step level, enabling holistic recombination and fine-grained refinement. Lightweight, task-aware fitness functions are designed to guide the evolutionary process toward accurate and diverse reasoning. Empirically, improves correct-CoT synthesis success by over 30% and enhances structural diversity, with markedly improved efficiency. LLMs trained on these evolutionary CoT data achieve an average gain of 6.6% across eight math benchmarks, outperforming previous distillation and self-synthesis approaches. These results underscore the promise of evolutionary CoT synthesis as a scalable and effective method for mathematical reasoning tasks.

## 20. Mistake Notebook Learning: Batch-Clustered Failures for Training-Free Agent Adaptation

- Authors: Xuanbo Su, Yingfang Zhang, Hao Luo, Xiaoteng Liu, Leo Huang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.6898199946332073
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.719/
- PDF: https://aclanthology.org/2026.findings-acl.719.pdf
- Local PDF: pdf/2026-09-15_20_Mistake Notebook Learning_ Batch-Clustered Failures for Training-Free Agent Adaptation.pdf

With the growing adoption of Large Language Model (LLM) agents in persistent, real-world roles, they naturally encounter continuous streams of tasks and inevitable failures. A key limitation, however, is their inability to systematically learn from these mistakes, forcing them to repeat identical errors in similar contexts. Unlike prior training-free methods that primarily store raw instance-level experience or focus on retrieving successful trajectories, we propose Mistake Notebook Learning (MNL), a novel memory framework that enables agents to self-curate generalizable guidance from batch-clustered failures. This mechanism allows agents to distill shared error patterns into structured “mistake notes”, updating an external memory only when batch performance improves to ensure stability. To further amplify adaptability, we integrate MNL with test-time scaling, leveraging aggregated failure patterns to actively steer the search process away from known pitfalls. Experiments on mathematical reasoning, Text-to-SQL, and interactive agent benchmarks show that MNL achieves competitive performance compared to existing memory mechanisms in both effectiveness and efficiency. These findings position structured mistake abstraction as a critical lever for robust agent evolution, enabling continuous improvement without the cost of parameter updates.

## 21. Debate-of-Thoughts: Resolving Knowledge Conflicts in LLMs Through Internal Deliberation

- Authors: Guocong Li, Qirui Hu, Ping Wang, Guofeng Zhang, Jian Wu, Hongxia Xu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.6893071940220636
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1651/
- PDF: https://aclanthology.org/2026.acl-long.1651.pdf
- Local PDF: pdf/2026-09-15_21_Debate-of-Thoughts_ Resolving Knowledge Conflicts in LLMs Through Internal Deliberation.pdf

Large Language Models enhanced with Retrieval Augmented Generation show strong potential in knowledge intensive tasks. However, they often encounter knowledge conflicts, where retrieved information contradicts the model’s internal knowledge or exhibits internal inconsistencies. Existing methods treat this as a simplistic binary choice, forcing models to blindly trust external contexts or rigidly rely on memory, resulting in unreliable predictions that swing between sycophancy and stubbornness. We argue that a more principled approach is to embrace contradictions as opportunities for deeper reasoning. To this end, we introduce Debate-of-Thoughts (DoT), a framework that transforms conflict resolution into an active deliberation process. DoT guides a single model through three phases: 1) hypothesis generation, which forms competing perspectives; 2) internal debate, where the model acts as both a proponent and a critic to stress test each view; and 3) adjudication, where a judge module evaluates arguments based on evidence and logical consistency. We implement DoT via two complementary strategies: inference time prompt chaining and supervised fine tuning. Experiments across multiple conflict benchmarks show that DoT consistently outperforms state-of-the-art methods, while generating transparent debate transcripts that explain its decisions. By improving both accuracy and interpretability under knowledge conflicts, DoT establishes a more reliable paradigm for retrieval augmented generation systems.

## 22. Web Sitemap Knowledge Can Enhance Autonomous Browsing

- Authors: Yuyao Zhang, Hongyu Lu, Jiajie Jin, Hongjin Qian, Shiyu Li, Zhao Yang, Yutao Zhu, Ji-Rong Wen, Zhicheng Dou
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.68919069374975
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1465/
- PDF: https://aclanthology.org/2026.findings-acl.1465.pdf
- Local PDF: pdf/2026-09-15_22_Web Sitemap Knowledge Can Enhance Autonomous Browsing.pdf

Recent advances in large language models (LLMs) have enabled web agents to perform interactive tasks on real-world websites. However, existing agents still suffer from limited robustness, efficiency, and task success, largely due to their lack of structural understanding of websites and the absence of browsing priors in pre-trained models. To address these challenges, this paper proposes the Web Agent Sitemap Protocol (WASP), an agent-oriented sitemap that integrate structured website knowledge into web agents. WASP adopts a dual-granularity design, providing global site-level structure and local page-level semantic and interaction guidance. We also introduce a framework LightASM for constructing such sitemaps by identifying core pages and generating concise semantic summaries and block-level descriptions. Experiments on real-world browsing benchmarks demonstrate that WASP substantially improves the robustness, efficiency, and effectiveness of LLM-based web agents without extra training.

## 23. Beyond Majority Voting: Towards Fine-grained and More Reliable Reward Signal for Test-Time Reinforcement Learning

- Authors: Weiqin Wang, Yile Wang, Kehao Chen, Hui Huang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.6890013328991675
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1727/
- PDF: https://aclanthology.org/2026.acl-long.1727.pdf
- Local PDF: pdf/2026-09-15_23_Beyond Majority Voting_ Towards Fine-grained and More Reliable Reward Signal for Test-Time Reinforcement Learning.pdf

Test-time reinforcement learning mitigates the reliance on annotated data by using majority voting results as pseudo-labels, emerging as a complementary direction to reinforcement learning with verifiable rewards (RLVR) for improving reasoning ability of large language models (LLMs). However, this voting strategy often induces confirmation bias and suffers from sparse rewards, limiting the overall performance. In this work, we propose subgroup-specific step-wise confidence-weighted pseudo-label estimation (SCOPE), a framework integrating model confidence and dynamic subgroup partitioning to address these issues. Specifically, SCOPE integrates the proposed step-wise confidence into pseudo-label estimation, prioritizing high-quality reasoning paths over simple frequency count. Furthermore, it dynamically partitions the candidate outputs pool into independent subgroups by balancing reasoning quality against exploration diversity. By deriving local consensus via repeat sampling for each subgroup, SCOPE provides diverse supervision targets to encourage broader exploration. We conduct experiments across various models and benchmarks, experimental results show that SCOPE consistently outperforms recent baselines. Notably, SCOPE achieves relative improvements of 13.1% on challenging AIME 2025 and 8.1% on AMC.

## 24. Context-attended Adversarial Reinforcement Learning for Robust Multi-step Retrieval Augmented Generation

- Authors: Yingtao Ren, Xiao Luo, Yu-Cheng Chang, Chin-teng Lin
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.688953577972899
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.856/
- PDF: https://aclanthology.org/2026.findings-acl.856.pdf
- Local PDF: pdf/2026-09-15_24_Context-attended Adversarial Reinforcement Learning for Robust Multi-step Retrieval Augmented Generation.pdf

Multi-step retrieval-augmented generation has attracted increasing attention due to its capacity to improve the factuality of large language models with iterative retrieved knowledge. However, the performance of multi-step RAG systems is susceptible to potential retrieval noise and fabricated documents in real-world scenarios. Current approaches usually utilize supervised fine-tuning on predetermined noisy contexts to enhance the robustness. However, their performance remains inadequate when it comes to more complicated long-context scenarios due to the lack of adaptability. Towards this end, we propose a novel framework named Context-attended Adversarial Reinforcement Learning (CARE) for multi-step RAG systems against attacks. The core of our CARE is to conduct reinforcement learning on adversarial samples which are alternatingly enhanced with text gradients. In particular, our CARE includes a reward model to identify the accuracy of responses, which is minimized for the generation of adversarial samples with text gradients. These context-attended noisy samples are then utilized for reinforcement learning to maximize the rewards. The whole framework is conducted alternatingly from easy to hard samples to ensure the smoothness of the optimization. Extensive experiments on multi-step RAG benchmark datasets are conducted to validate the superiority of our proposed CARE in multiple noisy scenarios. Our code is available at https://github.com/yingtaoren/CARE .

## 25. MatchTIR: Fine-Grained Supervision for Tool-Integrated Reasoning via Bipartite Matching

- Authors: Changle Qu, Sunhao Dai, Hengyi Cai, Jun Xu, Shuaiqiang Wang, Dawei Yin
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.6889052748810096
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.549/
- PDF: https://aclanthology.org/2026.acl-long.549.pdf
- Local PDF: pdf/2026-09-15_25_MatchTIR_ Fine-Grained Supervision for Tool-Integrated Reasoning via Bipartite Matching.pdf

Tool-Integrated Reasoning (TIR) empowers large language models (LLMs) to tackle complex tasks by interleaving reasoning steps with external tool interactions. However, existing reinforcement learning methods typically rely on outcome- or trajectory-level rewards, assigning uniform advantages to all steps within a trajectory. This coarse-grained credit assignment fails to distinguish effective tool calls from redundant or erroneous ones, particularly in long-horizon multi-turn scenarios. To address this, we propose MatchTIR, a framework that introduces fine-grained supervision via bipartite matching-based turn-level reward assignment and dual-level advantage estimation. Specifically, we formulate credit assignment as a bipartite matching problem between predicted and ground-truth traces, utilizing two assignment strategies to derive dense turn-level rewards. Furthermore, to balance local step precision with global task success, we introduce a dual-level advantage estimation scheme that integrates turn-level and trajectory-level signals, assigning distinct advantage values to individual interaction turns. Extensive experiments on three benchmarks demonstrate the superiority of MatchTIR. Notably, our 4B model surpasses the majority of 8B competitors, particularly in long-horizon and multi-turn tasks. Our codes are available at https://anonymous.4open.science/r/MatchTIR .

## 26. OSCR-Attack: One-Shot Character Level Attacks through Self-Optimizing Continuous Relaxation

- Authors: Lingyi Kong, Zhuo Liu, Zhanghao Hu, Qilong Qiu, Yutao Yang, Jingjing Xue, Zheng Wang, Lin Gui, Feiping Nie
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.6885261074827356
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1235/
- PDF: https://aclanthology.org/2026.findings-acl.1235.pdf
- Local PDF: pdf/2026-09-15_26_OSCR-Attack_ One-Shot Character Level Attacks through Self-Optimizing Continuous Relaxation.pdf

Adversarial attacks have attracted growing attention across domains, including natural language processing (NLP). Character-level adversarial attacks preserve semantics, but they have received less attention because the discrete operations they use are costly and inefficient. Challenging these beliefs, we introduce two adaptively learnable matrices that transform discrete choices into continuous representations, enabling automatic one-shot multi-position, multi-character insertion. To optimize the two learnable matrices, we propose OSCR-Attack, an end-to-end framework based on gradient-based optimization, with a conflict resolution strategy that maps the optimized continuous distributions back into discrete insertion operations. Extensive experiments on three benchmarks with three open-source large language models (LLMs) show that OSCR-Attack improves attack success rate (ASR) by up to 21.45% points and accelerates the attack by up to 3.66 times compared to recent baselines.

## 27. Agent-GWO: Collaborative Agents for Dynamic Prompt Optimization in Large Language Models

- Authors: Xudong Wang, Chaoning Zhang, Chenghao Li, Shuxu Chen, Qigan Sun, Jiaquan Zhang, Fachrina Dewi Puspitasari, Tae-Ho Kim, Jiwei Wei, Malu Zhang, Guoqing Wang, Yang Yang, Heng Tao Shen
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.688226290184673
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.821/
- PDF: https://aclanthology.org/2026.findings-acl.821.pdf
- Local PDF: pdf/2026-09-15_27_Agent-GWO_ Collaborative Agents for Dynamic Prompt Optimization in Large Language Models.pdf

Large Language Models (LLMs) have demonstrated strong capabilities in complex reasoning tasks, while recent prompting strategies such as Chain-of-Thought (CoT) have further elevated their performance in handling complex logical problems. Despite these advances, high-quality reasoning remains heavily reliant on manual static prompts and is sensitive to decoding configurations and task distributions, leading to performance fluctuations and limited transferability. Existing automatic prompt optimization methods typically adopt single-agent local search, failing to simultaneously optimize prompts and decoding hyperparameters within a unified framework to achieve stable global improvements. To address this limitation, we propose Agent-GWO, a dynamic prompt optimization framework for complex reasoning. Specifically, we unify prompt templates and decoding hyperparameters as inheritable agent configurations. By leveraging the leader-follower mechanism of the Grey Wolf Optimizer (GWO), we automatically select three leader agents ( 𝛼 , 𝛽 , and 𝛿 ) to guide the collaborative updates of the remaining agents, enabling iterative convergence toward robust optimal reasoning configurations that can be seamlessly integrated for inference. Extensive experiments on multiple mathematical and hybrid reasoning benchmarks across diverse LLM backbones show that Agent-GWO consistently improves accuracy and stability over existing prompt optimization methods.

## 28. SILO-BENCH: A Scalable Environment for Evaluating Distributed Coordination in Multi-Agent LLM Systems

- Authors: Yuzhe Zhang, Feiran Liu, Yi Shan, Xinyi Huang, Xin Yang, Yueqi Zhu, Xuxin Cheng, Cao Liu, Ke Zeng, Terry Jingchen Zhang, Wenyuan Jiang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.688203603480085
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1354/
- PDF: https://aclanthology.org/2026.acl-long.1354.pdf
- Local PDF: pdf/2026-09-15_28_SILO-BENCH_ A Scalable Environment for Evaluating Distributed Coordination in Multi-Agent LLM Systems.pdf

Large language models are increasingly deployed in multi-agent systems to overcome context limitations by distributing information across agents. However, whether LLM-based agents can reliably coordinate when each observes only a fragment of the global problem remains unclear. Existing benchmarks often prescribe agent roles or interaction patterns, conflating coordination ability with role-based priors. We introduce SILO-BENCH, a role-free benchmark for evaluating free-form collaboration under information silos. The benchmark comprises 30 algorithmic tasks with exact ground-truth answers, organized into 3 complexity levels based on optimal communication complexity: aggregation, mesh, and global shuffle. To systematically probe coordination capabilities, we instantiate 54 configurations by varying 3 communication protocols, 6 agent scales and 3 frontier LLMs, conducting 1,620 experiments. We evaluate agent behavior along three dimensions: Success Rate, Token Consumption, and Communication Density. Our experiments reveal a fundamental Communication-Reasoning Gap: agents communicate actively, yet fail to translate interaction into effective distributed computation. Performance collapses as complexity increases, with Level-III tasks achieving zero success beyond 50 agents. These findings demonstrate that current LLMs cannot escape information silos through coordination alone. SILO-BENCH provides a foundation for tracking progress toward genuinely collaborative multi-agent systems. The code is available at https://github.com/jwyjohn/acl26-silo-bench .

## 29. Mechanistic Insights into Deferred Semantic Drift in LLMs

- Authors: Jingjie Zeng, Huayang Li, Liang Yang, Shaowu Zhang, Yuanyuan Sun, Hongfei Lin
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.688008177921961
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.57/
- PDF: https://aclanthology.org/2026.findings-acl.57.pdf
- Local PDF: pdf/2026-09-15_29_Mechanistic Insights into Deferred Semantic Drift in LLMs.pdf

Large Language Models (LLMs) face a fundamental challenge with delayed disambiguation: How is the meaning of an ambiguous word updated when clarifying context arrives only after it has been processed? While LLMs possess the latent capacity to resolve such ambiguities—as revealed when a full, non-causal context is provided—their unidirectional architecture prevents immediate updates. We investigate the underlying computational mechanism and show this semantic re-evaluation is deferred to subsequent tokens in a process we term “Deferred Semantic Drift (DSD)”. Through targeted analysis of attentional pathways, we find that later tokens actively retrieve context-dependent “informational packets” from the ambiguous word’s value vector to steer the final interpretation. We demonstrate this mechanism in metaphor comprehension and provide causal validation by steering model outputs towards literal or metaphorical meanings via targeted activation interventions. This research uncovers a key computational strategy for meaning construction, offering crucial insights for understanding and guiding the behavior of LLMs.

## 30. Memory-R1: Enhancing Large Language Model Agents to Manage and Utilize Memories via Reinforcement Learning

- Authors: Sikuan Yan, Xiufeng Yang, Zuchao Huang, Ercong Nie, Zifeng Ding, Zonggen Li, Xiaowen Ma, Jinhe Bi, Kristian Kersting, Jeff Z. Pan, Hinrich Schuetze, Volker Tresp, Yunpu Ma
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.687717097301906
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.583/
- PDF: https://aclanthology.org/2026.acl-long.583.pdf
- Local PDF: pdf/2026-09-15_30_Memory-R1_ Enhancing Large Language Model Agents to Manage and Utilize Memories via Reinforcement Learning.pdf

Large Language Models (LLMs) have demonstrated impressive capabilities across a wide range of NLP tasks, but they remain fundamentally stateless, constrained by limited context windows that hinder long-horizon reasoning. Recent efforts to address this limitation often augment LLMs with an external memory bank, yet most existing pipelines are static and heuristic-driven, lacking a learned mechanism for deciding what to store, update, or retrieve. We present Memory-R1, a reinforcement learning (RL) framework that equips LLMs with the ability to actively manage and utilize external memory through two specialized agents: a Memory Manager that learns structured operations, including ADD, UPDATE, DELETE, and NOOP; and an Answer Agent that pre-selects and reasons over relevant entries. Both agents are fine-tuned with outcome-driven RL (PPO and GRPO), enabling adaptive memory management with minimal supervision. With only 152 training QA pairs, Memory-R1 outperforms strong baselines and generalizes across diverse question types, three benchmarks (LoCoMo, MSC, LongMemEval), and multiple model scales (3B–14B).
