# Researcher Tracking - 2026-11-06 (daily)

Total new tracked papers: 6
Highlighted papers: 6

## 1. Continuous-time q-Learning for Finite-Horizon Portfolio Choice with Optimal Stopping in Jump-Diffusion Markets

- Authors: Tingting Zhang, Can Yang
- Source hits: arxiv
- Matched researchers: Can Yang
- Matched groups: N/A
- Confidence: medium (author_alias)
- Topic keywords: diffusion
- Journal/source: arxiv
- Publication date: 2026-11-05
- Article: http://arxiv.org/abs/2611.07362v1

We develop a structured continuous-time q-learning framework for finite-horizon investment and optimal stopping under jump-diffusion dynamics with unknown parameters. A penalty approximation transforms the Hamilton-Jacobi-Bellman variational inequality into an HJB equation with a binary control for the stopping penalty. An auxiliary state incorporates the resulting control-dependent discount factor into a Markovian formulation. We randomize controls on the mixed action space and introduce Shannon entropy regularization, establishing policy improvement and martingale characterizations of the continuous-time q-function. These results motivate a structured q-learning algorithm that constructs the q-function from the penalty HJB equation and jointly learns the value function and unknown generator parameters from sample paths. We apply the method to portfolio choice with optimal stopping in a simulation study. We further conduct a two-asset empirical study, evaluating learned strategies on bootstrap paths from held-out test returns versus an MLE-finite difference benchmark.

## 2. WeightLoop: Weight-Space Programming with Experimental Feedback

- Authors: Mengran Li, Bo Li, Weijing Zhao, Chengyang Zhang, Boyu Zhang, Jinfeng Xu, Zelin Zang, Victor C. M. Leung, Stan Z. Li
- Source hits: arxiv
- Matched researchers: Stan Z. Li
- Matched groups: N/A
- Confidence: medium (author_alias)
- Topic keywords: N/A
- Journal/source: arxiv
- Publication date: 2026-11-05
- Article: http://arxiv.org/abs/2611.07319v1

Weight-space programming (WSP) shows that language models can reason about and rewrite neural network weights; recursive self-improvement (RSI) motivates feedback-driven improvement. Models guiding experiments receive concrete feedback: completed assays reveal prediction errors and inform what to test next. We introduce WeightLoop, a framework that turns experimental feedback into persistent updates to deployed predictors. GPT-6 Astra inspects a task specification and the model implementation, then writes a bounded, reusable parameter-editing program. As new measurements arrive, the program identifies prediction discrepancies, validates candidate edits using observed outcomes, and writes the selected changes back to the original model. The editor remains fixed while the predictor evolves, enabling repeated updates without further LLM calls or gradient retraining while preserving the original inference interface. In offline replay, targeted edits improve mean ranking utility in seven of eight endpoint-budget settings (all eight versus random edits) and mean final discovery across three sequential tasks. WeightLoop connects WSP with an RSI-inspired improvement loop, making experimental evidence a direct driver of model change and subsequent decisions.

## 3. AtlasULP: Domain-aware Universal Link Prediction via Relation Atlas

- Authors: Yujing Liu, Yixin Liu, Yu Zheng, Lianhua Chi, Alan Wee-Chung Liew, Heng Tao Shen, Shirui Pan
- Source hits: arxiv
- Matched researchers: Yixin Liu
- Matched groups: N/A
- Confidence: medium (author_alias)
- Topic keywords: N/A
- Journal/source: arxiv
- Publication date: 2026-11-05
- Article: http://arxiv.org/abs/2611.07347v1

Link prediction (LP) is a widely applied task in graph learning. Conventional LP approaches typically follow a dataset-specific paradigm, requiring independent training for each graph and incurring high computational and maintenance costs in large-scale applications. Motivated by these limitations, recent work explores Universal Link Prediction (ULP), aiming to enable training-free inference on arbitrary unseen graphs. However, existing methods primarily rely on subgraph sampling strategies to construct universal representations, which are unable to capture higher-order information due to the exponential growth of higher-order neighborhoods. As a result, they often under-perform on graphs where long-range signals are essential, such as biological networks. Moreover, their prediction models are typically domain-agnostic and lack the ability to adapt to different graph domains, leading to limited generalization. To address these challenges, we propose an Atlas-based Universal Link Prediction framework (AtlasULP), which introduces the relation atlas to capture structural associations between node pairs from both global and local perspectives, enabling a comprehensive characterization of connectivity signals across diverse graph domains. Building upon this representation, we develop a domain-guided prompting ULP model, which generates domain-aware prompt tokens from contextual structures and performs prompt-guided in-context prediction for adaptive link inference. Extensive experiments demonstrate that AtlasULP consistently outperforms state-of-the-art methods across diverse graph domains.

## 4. Editing Large Language Models with Geometry-Aware Regularization

- Authors: Bingqing Liu, Wei Liu, Jun Wang, Xiaobo Sun, Yuhua Li, Ruixuan Li
- Source hits: arxiv
- Matched researchers: Sun Xiaobo
- Matched groups: N/A
- Confidence: medium (author_alias)
- Topic keywords: large language model
- Journal/source: arxiv
- Publication date: 2026-11-04
- Article: http://arxiv.org/abs/2611.06185v1

Knowledge editing has become a key technique for updating knowledge in large language models. However, existing methods neglect the geometric structure of the knowledge representation space, leading to two key limitations: they cannot distinguish which pre-trained knowledge should be preferentially preserved (core vs. non-core) nor which new edits are inherently difficult (hard vs. easy). To address this, we propose GEdit, a geometry-aware framework built on a Low-Rank Plus Diagonal (LR+D) factor model that captures the intrinsic low-rank structure of Transformer FFN hidden representations. GEdit features two complementary mechanisms. First, the low-rank regularization applies targeted protection on a low-rank core knowledge subspace. Second, the adaptive regularization dynamically adjusts the regularization strength based on each edit request's editability: relaxing constraints for hard edits to ensure success, and tightening them for easy edits to better preserve pretrained knowledge. Extensive experiments on GPT2-XL, GPT-J, and LLaMA-3-8B under large-scale editing scenarios, including both mini-batch and fully sequential editing settings with up to 10,000 continuous updates, show that GEdit consistently and significantly outperforms state-of-the-art baselines in both editing success and knowledge preservation.

## 5. Spin swapping mediated by spin-orbital textures in centrosymmetric multiorbital materials

- Authors: Chengyuan Cai, Hanchen Wang, Rui-Chun Xiao, Tao Yu
- Source hits: arxiv
- Matched researchers: Hanchen Wang
- Matched groups: N/A
- Confidence: medium (author_alias)
- Topic keywords: N/A
- Journal/source: arxiv
- Publication date: 2026-11-04
- Article: http://arxiv.org/abs/2611.06163v1

Spin swapping converts a primary spin current into a secondary one by interchanging its flow and spin-polarization directions, attributed to spin-orbit scattering or spin-band splitting. Here we uncover a fundamentally distinct route to spin swapping arising from the orbital degree of freedom in the spin pumping to centrosymmetric multiorbital materials \textit{without spin-band splitting}. When the dynamical proximity ferromagnet injects a longitudinal spin current flowing normal to the interface, spin-orbit-entangled orbital textures redirect the injected spins into longitudinal and transverse orbital currents. Their subsequent conversion back to the spin sector generates transverse spin currents with propagation and polarization directions swapped relative to the primary spin current. The swapping efficiency achieves $50\%$ for Ge and Si. Governed by a fourth-rank tensor constrained by crystalline symmetry and without requiring spin-orbit scattering or inversion symmetry breaking, our finding reveals spin-orbital textures as hidden intermediate channels of spin swapping with unexplored material choices and functionalities.

## 6. UniRestorer++: Scalable Universal Image Restoration with Multi-Granularity Degradation Modeling

- Authors: Jingbo Lin, Zhilu Zhang, Fan Li, Renjing Pei, Wenbo Li, Hang Xu, Hongzhi Zhang, Wangmeng Zuo
- Source hits: arxiv
- Matched researchers: Hang Xu
- Matched groups: N/A
- Confidence: medium (author_alias)
- Topic keywords: N/A
- Journal/source: arxiv
- Publication date: 2026-11-04
- Article: http://arxiv.org/abs/2611.06042v1

Universal image restoration aims to handle diverse degradations within a single model, but a reliable scaling strategy remains underexplored. Increasing backbone depth and width can lead to performance saturation, while degradation-aware specialization depends on accurate degradation estimation and is vulnerable to errors on out-of-distribution and real-world inputs. We propose UniRestorer++, a scalable framework based on multi-granularity degradation modeling. It progressively refines degradation groups and introduces group-specific experts, coupling capacity growth with specialization. Degradation-estimation-based routing selects a root-to-leaf path, while granularity-estimation-based routing chooses a level along that path to balance specialization and robustness. Spatially dense degradation representation maps further enable region-aware routing for spatially non-uniform corruptions. We develop CDD-50, a benchmark covering 50 degradation categories from single to penta-degradation. Experiments show approximately log-linear PSNR trends over the evaluated model-size range and stronger scaling gains on out-of-distribution and real-world data than vanilla MoE scaling. UniRestorer++ achieves state-of-the-art performance across benchmarks and demonstrates zero-shot generalization and few-shot transfer on real-world images. Code: https://github.com/mrluin/UniRestorer_plusplus
