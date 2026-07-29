# Researcher Tracking - 2026-07-29 (daily)

Total new tracked papers: 3
Highlighted papers: 3

## 1. HiSkill: Empowering LLM Agents with Hierarchical Skill Graphs

- Authors: Yu Hao, Jinxuan Cai, Qi Zhang, Yawen Li, Zhiqiang Zhang, Chuan Shi, Cheng Yang
- Source hits: arxiv
- Matched researchers: Chuan Shi
- Matched groups: N/A
- Confidence: medium (author_alias)
- Topic keywords: large language model, llm agent
- Journal/source: arxiv
- Publication date: 2026-07-28
- Article: http://arxiv.org/abs/2607.25853v1

Skills have become an important abstraction for enabling large language model (LLM) agents to reuse past experience in long-horizon interactive tasks. However, existing trajectory-to-skill methods often produce flat collections of high-level textual skills that are stored and retrieved independently, leaving skill relations underutilized and maintaining a gap between high-level skills and executable actions. In this paper, we propose HiSkill, a hierarchical skill graph framework that organizes interaction trajectories into a directed graph with skill nodes, AtomicOp nodes, and typed edges. Specifically, the graph connects reusable high-level skills with executable action templates, while also capturing decomposition, temporal transition, compatibility, support, and recovery relations among them. At inference time, HiSkill retrieves a compact task-relevant subgraph and performs subgraph-guided task execution, where a symbolic task state, an active skill, and the retrieved subgraph guide the LLM agent to switch skills, select AtomicOps, and ground executable actions iteratively. Experiments on three interactive environments show that HiSkill outperforms state-of-the-art baselines while reducing inference token consumption, demonstrating the effectiveness of bridging high-level skills and executable action grounding through a hierarchical skill graph. Our data and code is available at https://github.com/BUPT-GAMMA/HiSkill.

## 2. Decompose and Reorganize: Planning with Primitives and Visuomotor Policies Learned from Demonstrations

- Authors: Yizhou Chen, Hang Xu, Dongjie Yu, Yupu Lu, Tengye Xu, Zeqing Zhang, Wei Zhang, Yi Ren, Ben M. Chen, Jia Pan
- Source hits: arxiv
- Matched researchers: Hang Xu
- Matched groups: N/A
- Confidence: medium (author_alias)
- Topic keywords: N/A
- Journal/source: arxiv
- Publication date: 2026-07-28
- Article: http://arxiv.org/abs/2607.25397v1

Successfully automating dexterous, long-horizon robotic manipulation requires frameworks capable of both high-level reasoning and fine-grained execution. Traditional task and motion planning (TAMP), while excellent at symbolic planning, is often brittle in contact-rich operations. Simultaneously, imitation learning (IL), while effective in manipulation tasks with visual feedback, is limited by its low capability in spatial generalization and multi-stage operation. To reconcile their complementary strengths and limitations, we propose DR-LfD (Decomposed and Reorganized Skills Learned from Demonstrations), a framework that seamlessly integrates visuomotor policies into a TAMP-gated decision-making system. Based on contact relationships, DR-LfD decomposes human demonstrations into atomic skills, which are reproduced as visuomotor policies or object-centric primitives. The initiation, termination, and constraints of the visuomotor policies are carefully modeled and implemented in a TAMP-compatible form, enabling reorganization of skills learned from different sources. DR-LfD transforms the learning problem from one requiring exponential demonstration data over possible skill sequences to one whose demonstration burden scales with the number of distinct skill types, with limited data for each skill. Through comprehensive real-world and simulation benchmarking across diverse scenarios, we demonstrate the strong performance of DR-LfD on tasks involving multiple steps, unseen setups, and physical constraints. Project website: https://dr-lfd.github.io/DR-LfD-website.

## 3. P3: Probabilistic Policy Propagation for Stable VAE-Based Robot Learning

- Authors: Liyun Yan, Jianming Ma, Yang Zhang, Shengcheng Fu, Zhanxiang Cao, Keqi Zhu, Yizhi Chen, Yue Gao
- Source hits: arxiv
- Matched researchers: Yue Gao
- Matched groups: N/A
- Confidence: medium (author_alias)
- Topic keywords: variational autoencoder
- Journal/source: arxiv
- Publication date: 2026-07-28
- Article: http://arxiv.org/abs/2607.25541v1

Variational Autoencoders are widely used to encode high-dimensional and noisy observations in robotics. However, their stochastic latent creates a mismatch with Proximal Policy Optimization (PPO): an effective policy marginalizes over the latent distribution, whereas former implementations estimate its probability ratio and KL divergence using only one latent sample. We identify a fundamental but overlooked theoretical cause: naive single-sample approximations in stochastic latent space induce significant variance and bias in the surrogate loss. To address this, we introduce P^3 (Probabilistic Policy Propagation), a distribution-aware optimization framework for VAE-based policies. $P^3$ couples moment-based probabilistic method for stable and efficient learning with sampling-based calibration for robust policy behavior under latent uncertainty. In our experiments, P^3 boosts data efficiency from 64.6% to >96%, reduces convergence steps by >20%. Furthermore, P^3 is evaluated on challenging humanoid parkour tasks and shows an effective foundation for VAE-based PPO. Code is available at https://github.com/ylyem9x/P3_Open.
