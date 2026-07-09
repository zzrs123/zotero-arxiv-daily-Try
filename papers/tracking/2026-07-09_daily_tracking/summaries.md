# Researcher Tracking - 2026-07-09 (daily)

Total new tracked papers: 2
Highlighted papers: 2

## 1. Point as Skeleton: Accumulated Point Cloud Enhanced Autoregressive Generation for Closed-Loop Autonomous Driving Simulation

- Authors: Songbur Wong, Xiaosong Jia, Junqi You, Bo Zhang, Pei Xu, Renqiu Xia, Yuping Qiu, Shaofeng Zhang, Zelin Zhao, Xuechao Yan, Yuchen Zhou, Yurui Chen, Wen Guo, Hang Xu, Junchi Yan
- Source hits: arxiv
- Matched researchers: Hang Xu
- Matched groups: N/A
- Confidence: medium (author_alias)
- Topic keywords: diffusion
- Journal/source: arxiv
- Publication date: 2026-07-07
- Article: http://arxiv.org/abs/2607.06516v1

Evaluating end-to-end autonomous driving (E2E-AD) remains challenging, as existing driving simulation methods often trade off closed-loop interactivity (e.g., CARLA) and real-world visual fidelity (e.g., nuScenes). We present \textbf{\emph{Point as Skeleton}}, a generative sensor simulation framework for state-updated autoregressive driving video generation, in which an autoregressive generator synthesizes visual observations from step-wise updated ego states, actor states, scene maps, and point-cloud skeleton conditions. To support closed-loop rollout, we introduce Reset-and-Roll, which adapts rolling diffusion inference to simulation by preventing future-conditioned latent states from being committed across simulation steps. To stabilize error accumulation during step-wise autoregressive rollout, we introduce point-cloud skeletons that decouple foreground and background assets and project them into camera-view painted-point and template-depth conditions, providing appearance and geometric cues. We further implement a nuPlan-based renderer-level closed-loop generative interface for evaluating generation under ego deviations from the original log. Experiments on nuScenes and nuPlan show that \textit{Point as Skeleton} improves autoregressive generation quality during closed-loop rollout, demonstrating its potential for visually faithful closed-loop driving simulation. The code is available at https://github.com/krauwu/point-as-skeleton.

## 2. FORGE: Towards Functional Tool-Use Generalization via Keypoint Trajectory Reasoning

- Authors: Chuhao Zhou, Liquan Wang, Shuxin Cao, Xiangyu Chen, Yuxuan Hu, Boyu Ma, Animesh Garg, Jianfei Yang
- Source hits: arxiv
- Matched researchers: Yuxuan Hu
- Matched groups: N/A
- Confidence: medium (author_alias)
- Topic keywords: N/A
- Journal/source: arxiv
- Publication date: 2026-07-07
- Article: http://arxiv.org/abs/2607.05780v1

While humans readily repurpose a book, a stone, or a shoe to drive a nail, robots trained on specific tools fail to transfer the same function to novel ones -- a gap we formalize as functional generalization. Such tools share a common functional intent that is visually recognizable, yet this perceptual similarity does not carry over to action space, where each tool demands an entirely different motor pattern. To bridge this gap, we explore intermediate representations including affordance images, human video prompts, and 2D keypoint trajectories, finding that keypoint trajectories best balance functional expressiveness and action groundability. Building on this, we propose FunctiOnal Reasoning and Grounded Execution (FORGE), a two-stage policy that decouples functional reasoning from action execution: predicting generalizable keypoint trajectories from action-free data, then grounding them into robot actions with limited demonstrations. On a seven-tool hitting-function benchmark, FORGE consistently outperforms state-of-the-art methods on unseen tools in both simulation and the real world, achieving over 2X improvement in average success rate.
