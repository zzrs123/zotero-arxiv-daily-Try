# Researcher Tracking - 2026-11-24 (daily)

Total new tracked papers: 4
Highlighted papers: 4

## 1. Verifiable On-Policy Distillation

- Authors: Juntong Shi, Stefano Ermon, Jure Leskovec, Minkai Xu
- Source hits: arxiv
- Matched researchers: Jure Leskovec
- Matched groups: N/A
- Confidence: medium (author_alias)
- Topic keywords: N/A
- Journal/source: arxiv
- Publication date: 2026-11-23
- Article: http://arxiv.org/abs/2611.30325v1

Reinforcement learning with verifiable rewards (RLVR) has become a powerful approach for improving language-model reasoning, but its supervision is inherently sparse: a sequence-level verifier reward is propagated only through sampled trajectories and provides no direct signal for alternative actions. On-policy distillation (OPD) offers a complementary form of supervision by providing dense teacher feedback over the full next-token distribution, but this signal is not grounded in verified task outcomes. Simply co-optimizing the two objectives does not couple these signals: verifier feedback remains sparse and does not inform the dense teacher supervision. We introduce Verifiable On-Policy Distillation (VOPD), which transfers sparse verifier feedback into dense, verifier-grounded supervision. Our key observation is that the implicit-reward view of OPD places teacher supervision and verifier feedback in a common reward space while retaining a reward signal available for every next-token action. Under this view, VOPD projects verifier preference onto the teacher's implicit-reward direction and Rao--Blackwellizes the resulting signal over the full vocabulary, propagating verifier-grounded supervision to actions that were never sampled. The resulting objective can also be interpreted as adaptively extrapolating the distillation target according to teacher--verifier agreement. Across two teacher--student configurations and eight mathematical reasoning benchmarks, VOPD consistently improves both final performance and learning efficiency over vanilla OPD and other on-policy distillation baselines. Our code is available at https://github.com/juntongshi48/VOPD.

## 2. Voice Agents: From Auditory Intelligence to Auditory Agency

- Authors: Kele Xu, Qisheng Xu, Xinwang Liu, Huaimin Wang
- Source hits: arxiv
- Matched researchers: Xinwang Liu
- Matched groups: N/A
- Confidence: medium (author_alias)
- Topic keywords: N/A
- Journal/source: arxiv
- Publication date: 2026-11-22
- Article: http://arxiv.org/abs/2611.29465v1

Voice systems increasingly combine streaming speech, persistent state, reasoning, tool use, and embodied control. Once these functions share a runtime, spoken input can change digital or physical state, and recognition or response quality alone no longer characterizes the system. This article studies the interfaces through which spoken evidence becomes consequential. \emph{Auditory intelligence} denotes the capabilities required to perceive, understand, coordinate, and generate spoken interaction; \emph{auditory agency} denotes the causal path from that interaction to stateful decisions and observable consequences. The \emph{commitment boundary} marks where revisable auditory evidence becomes persistent state, a plan, or an executable request. \emph{Agency closure} then follows an authorized action through observation, verification, recovery or compensation, and communication of the outcome. Evidence from full-duplex interaction, reasoning, memory, tools, embodiment, and human control shows a consistent systems-level mismatch: integration is advancing faster than end-to-end observation of what the integrated system actually does. The resulting design problem is to preserve a trace from spoken evidence to consequence while keeping commitment, execution, and verification attributable.

## 3. $ζ_0$: A Framework for World Action Models with Joint Scene and Body Foresight in Humanoid Control

- Authors: Yizhi Chen, Zhanxiang Cao, Yitong Wang, Junyu Liu, Hongchu Zeng, Xinyi Peng, Chuxuan Huang, Yicheng Su, Zihao Zhou, Shengcheng Fu, Haoyang Li, Liyun Yan, Tianyue Zhan, Jianming Ma, Yang Zhang, Keqi Zhu, Xiaxi Si, Jinming Yao, Qiao Sun, Shizeng Zhang, Jiangwei Zhong, Yue Gao
- Source hits: arxiv
- Matched researchers: Yue Gao
- Matched groups: N/A
- Confidence: medium (author_alias)
- Topic keywords: N/A
- Journal/source: arxiv
- Publication date: 2026-11-22
- Article: http://arxiv.org/abs/2611.29277v1

World Action Models anticipate visual outcomes to guide robot actions, yet humanoid interaction also depends on how the robot's body responds. Visual foresight alone can miss body motion, while latent-distance losses do not directly supervise action responses. We present $ζ_0$, a framework that turns vision-language-action policies into World Action Models by foreseeing future visual features and measured joint trajectories in a shared latent representation. During training, a teacher conditioned on recorded futures provides a reference action response, and dual-response transfer trains the causal predictor to match it through the teacher and the executing policy. All components are trained jointly, and deployment uses only causally predicted futures. On seven HumanoidArena tasks, $ζ_0$ built on $Ψ_0$ and GR00T N1.7 reaches 63.6% and 79.5% mean success, 18.8 and 9.0 points above these bases. On six real-world tasks, it reaches 78.3% and 85.0%, gains of 16.7 and 10.0 points. On GR00T, its 79.5% tops all compared seven-task joint policies. Project page: https://chenyizhi123.github.io/zeta0-project/

## 4. Contact Harness: Enabling VLM Agents to Perform Contact-Rich Manipulation

- Authors: Shilin Shan, Yuxuan Hu, Chuhao Zhou, Yimeng Dong, Bohan Hou, Jiaqi Bai, Boyu Ma, Jiahua Dong, Jianfei Yang
- Source hits: arxiv
- Matched researchers: Yuxuan Hu
- Matched groups: N/A
- Confidence: medium (author_alias)
- Topic keywords: N/A
- Journal/source: arxiv
- Publication date: 2026-11-22
- Article: http://arxiv.org/abs/2611.29377v1

Agents built on pretrained VLMs have demonstrated zero-shot control of real robots, but vision alone is often insufficient for reliable contact-state assessment in contact-rich manipulation. Force and tactile feedback provide complementary information, but their semantic ambiguity makes them difficult for agents to use directly. These signals must be interpreted according to their physical meaning, together with task phase and visual evidence. We propose Contact Harness, which uses reusable, optimized skills to guide a VLM agent in assessing contact states from multimodal feedback and selecting subsequent actions. A compliant execution mechanism regulates in-contact motions using real-time force feedback. The framework requires no model fine-tuning, task demonstrations, or simulation training. We conduct zero-shot real-robot evaluations using GPT-6 Astra on Rokae and Franka robots. With a single prompt skill, Contact Harness achieves a full-insertion rate of 90.7% across 15 connector types, with further evaluations on a real PC under variations in lighting, background, and position. Across four additional contact-rich tasks, including whiteboard wiping, writing, peeling, and pivoting, Contact Harness achieves an average success rate of 100%. On six simulated tasks, Contact Harness reaches 96.7% success, compared with at most 68.3% for pretrained VLA baselines fine-tuned on task demonstrations, showing the potential of agent-based manipulation for contact-rich real-world deployment.
