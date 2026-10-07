# Researcher Tracking - 2026-10-07 (daily)

Total new tracked papers: 3
Highlighted papers: 3

## 1. Global Transport Couplings for Classifier-Free Guided Flows

- Authors: Katarina Petrović, Zander W. Blasingame, Danyal Rehman, İsmail İlkan Ceylan, Michael Bronstein, Stephen Y. Zhang, Lazar Atanackovic, Alexander Tong
- Source hits: arxiv
- Matched researchers: Michael Bronstein
- Matched groups: N/A
- Confidence: medium (author_alias)
- Topic keywords: foundation model
- Journal/source: arxiv
- Publication date: 2026-10-06
- Article: http://arxiv.org/abs/2610.07555v1

Optimal-transport couplings have been shown to reduce training variance in unconditional flow models, but their role in conditional generation remains unclear. A natural approach constructs separate couplings for each condition, but this is impractical for large or continuous conditioning spaces found in modern image foundation models. We introduce Global Transport (GT), a global class-agnostic optimal-transport coupling, computed without class labels. GT can associate different conditions with different regions of the source noise, and consequently worsens performance without guidance. However, when combined with classifier-free guidance (CFG), GT consistently improves generation across domains, model scales, and sampling budgets. This reversal suggests that couplings for conditional flows should be evaluated both empirically and theoretically under the guided flow used at inference, rather than on unguided generation. We evaluate GT over both discrete class and continuous text conditioned image generation across model scales, and investigate how coupling choice alters guided trajectories. These results identify coupling design in the guided flow setting as a simple training time axis to improve performance without modifying existing architectures, samplers, or guidance mechanisms.

## 2. DecepEval: A Benchmark for Evaluating Deception in LLM Agents

- Authors: Yiming Xu, Hongyue Yu, Beihua Yang, Zihan Chen, Yixin Liu, Zhen Peng, Bin Shi, Bo Dong, Chao Shen, Irwin King, Qinghua Zheng
- Source hits: arxiv
- Matched researchers: Yixin Liu
- Matched groups: N/A
- Confidence: medium (author_alias)
- Topic keywords: large language model, llm agent
- Journal/source: arxiv
- Publication date: 2026-10-06
- Article: http://arxiv.org/abs/2610.07967v1

As large language model (LLM) agents become increasingly autonomous, they may pursue task performance through deception, raising concerns about their reliable deployment. Existing evaluations show that LLM agents can deceive, but often examine isolated scenarios or narrowly defined conditions, limiting systematic understanding of when deception becomes more likely. To address this gap, we introduce DecepEval, a benchmark comprising 1,532 instances across 3 task families and 28 professional scenarios. Drawing on classical fraud theories, we propose the LLM Deception Diamond framework, which characterizes four external conditions that may induce deception: pressure, incentive, opportunity, and conflict. DecepEval pairs neutral and induced versions of each instance to measure condition-dependent changes in deception rates, while explicit task facts and observable agent behavior help distinguish deception from capability-related errors. Evaluations of nine frontier LLMs show that inducements increase deception across models and task families, even among models with low baseline deception rates. DecepEval makes these vulnerabilities measurable, providing a shared benchmark for progress toward trustworthy artificial intelligence.

## 3. AuraSE: Low-Hallucination Generative Speech Enhancement via Multimodal Flow Matching and Inference Policy Optimization

- Authors: Yingda Shen, Yao Qian, Yuxuan Hu, Junan Zhang, Yuxiang Wang, Hardik Hansrajbhai Chauhan, Yudong Li, Yufei Xia, Yufei Liu, Zhizheng Wu
- Source hits: arxiv
- Matched researchers: Yuxuan Hu
- Matched groups: N/A
- Confidence: medium (author_alias)
- Topic keywords: diffusion, flow matching
- Journal/source: arxiv
- Publication date: 2026-10-05
- Article: http://arxiv.org/abs/2610.06632v1

Generative speech enhancement models can produce cleaner and more natural-sounding speech than conventional discriminative approaches, but may hallucinate by changing speech content or speaker identity, even with transcript conditioning. We present AuraSE, a flow-matching framework that addresses hallucination through complementary modality and inference designs. First, a double-stream-to-single-stream multimodal Diffusion Transformer (MMDiT) allows transcript and acoustic representations to interact while preserving a dedicated pathway for the degraded input. Second, we find that the best decoder configuration, governed by guidance scale, sampling temperature, and step count, varies substantially across utterances. This observation motivates Inference Policy Optimization (IPO), an online, on-policy preference optimization method. IPO generates multiple candidates from the current model under different inference configurations, ranks them with a multi-objective reward, and learns from their relative preferences. AuraSE-IPO ranks first on 11 of 12 metrics across the synthetic test sets and obtains the highest DNSMOS and blind-listening scores among the evaluated systems on the real DNS blind test set. At deployment, it uses a fixed $10$-step ODE decoder without classifier-free guidance (CFG) or per-utterance configuration search.
