# Researcher Tracking - 2026-10-06 (daily)

Total new tracked papers: 2
Highlighted papers: 2

## 1. FreeSpeed: Training-Free Speed Control for Generative Robot Policies

- Authors: Yuxuan Hu, Shilin Shan, Qiheng Wang, Jinghan Yang, Junqiao Fan, Hao Wan, Jianfei Yang
- Source hits: arxiv
- Matched researchers: Yuxuan Hu
- Matched groups: N/A
- Confidence: medium (author_alias)
- Topic keywords: N/A
- Journal/source: arxiv
- Publication date: 2026-10-05
- Article: http://arxiv.org/abs/2610.05734v1

Online control of execution speed is essential for deploying robot policies in real-world scenarios, as robots may need to speed up under time constraints or slow down to facilitate human interaction and improve safety. However, imitation-learned policies inherit the execution speed of their demonstrations, and test-time speed modification can introduce unrecoverable out-of-distribution observations, reducing task success. We observe that the directional inconsistency of action chunks reflects task-phase criticality, indicating how aggressively action step lengths can be modified while preserving task success. Based on this observation, we introduce FreeSpeed, a training-free module that post-processes action chunks from pretrained policies. FreeSpeed resamples each predicted chunk at the requested rate, then uses directional inconsistency between adjacent actions as the primary signal for rescaling. This signal adaptively determines how closely the execution speed can approach the requested speed, allowing flexible speed adjustment within the evaluated limits without compromising task success. Across three policy families and 50 simulated tasks, FreeSpeed supports online speed changes, with realized execution rates spanning 0.22x to 2.53x among settings that preserve per-task success. Across four real-world manipulation tasks, FreeSpeed achieves an average success rate of 94.0%, matching the frozen policy's 93.8%, while realizing execution rates from 0.38x to 1.97x.

## 2. EchoChat: Structured Cognitive Reasoning in Empathetic Spoken Dialogue

- Authors: Dingdong Wang, Shujie Liu, Yayue Deng, Yuxuan Hu, Yunrui Cai, Jincenzi Wu, Jianwei Yu, Jinyu Li, Helen Meng
- Source hits: arxiv
- Matched researchers: Yuxuan Hu
- Matched groups: N/A
- Confidence: medium (author_alias)
- Topic keywords: N/A
- Journal/source: arxiv
- Publication date: 2026-10-04
- Article: http://arxiv.org/abs/2610.04826v1

Empathetic spoken dialogue is a sophisticated cognitive process that requires not only recognizing emotions but also inferring a user's latent mental states to provide appropriate support. However, current SpeechLLMs often treat empathy as a direct input-to-response mapping, leading to "superficially warm" but emotionally hollow interactions. In addition, since empathy relies on a multi-stage process with strong inter-step dependency, errors at any intermediate step can cascade through subsequent steps and lead to inappropriate responses, while existing training paradigms lack mechanisms to precisely localize and improve such errors. In this work, we propose EchoChat, a unified framework that reformulates empathetic spoken dialogue as a structured cognitive reasoning process integrating perception, mental-state reasoning, and response generation. To support this paradigm, we first construct EchoDialogue-400K, an acoustically rich dataset for multi-stage empathetic supervision. During the SFT stage, we strengthen acoustic grounding through proposed Acoustic-Anchored Attention (AAA). During the RL stage, we further introduce a novel stage-aware optimization objective with Step-Decomposed Credit Assignment (SDCA) to localize reasoning errors and mitigate cascaded error propagation. In addition, we introduce EchoEval, an expert-annotated benchmark for multi-dimensional empathy evaluation. Extensive experiments demonstrate that EchoChat achieves state-of-the-art performance in perception, reasoning, and response alignment. Project page: https://github.com/dingdongwang/EchoChat
