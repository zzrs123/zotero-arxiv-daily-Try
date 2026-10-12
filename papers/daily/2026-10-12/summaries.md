# Paper Daily Reading - 2026-10-12

## 1. SearchGym: Bootstrapping Real-World Search Agents via Cost-Effective and High-Fidelity Environment Simulation

- Authors: Xichen Zhang, Ziyi He, Yinghao Zhu, Sitong Wu, Shaozuo Yu, Meng Chu, Wenhu Zhang, Haoru Tan, Jiaya Jia
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.6437680442962748
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.848/
- PDF: https://aclanthology.org/2026.acl-long.848.pdf
- Local PDF: pdf/2026-10-12_01_SearchGym_ Bootstrapping Real-World Search Agents via Cost-Effective and High-Fidelity Environment Simulation.pdf

Search agents have emerged as a pivotal paradigm for solving open-ended, knowledge-intensive reasoning tasks. However, training these agents via Reinforcement Learning (RL) faces a critical dilemma: interacting with live commercial Web APIs is prohibitively expensive, while relying on static data snapshots often introduces noise due to data misalignment. This misalignment generates corrupted reward signals that destabilize training by penalizing correct reasoning or rewarding hallucination. To address this, we propose SearchGym, a simulation environment designed to bootstrap robust search agents. SearchGym employs a rigorous generative pipeline to construct a verifiable knowledge graph and an aligned document corpus, ensuring that every reasoning task is factually grounded and strictly solvable. Building on this controllable environment, we introduce SearchGym-RL, a curriculum learning methodology that progressively optimizes agent policies through purified feedback, evolving from basic interactions to complex, long-horizon planning. Extensive experiments across the Llama and Qwen families demonstrate strong Sim-to-Real generalization. Notably, our Qwen2.5-7B-Base model trained within SearchGym surpasses the web-enhanced ASearcher baseline across nine diverse benchmarks by an average relative margin of 10.6%. Our results validate that high-fidelity simulation serves as a scalable and highly cost-effective methodology for developing capable search agents.

## 2. Less is More: Improving LLM Reasoning with Minimal Test-Time Intervention

- Authors: Zhen Yang, Mingyang Zhang, Feng Chen, Ganggui Ding, Liang Hou, Xin Tao, Ying-Cong Chen
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.643361166932756
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.921/
- PDF: https://aclanthology.org/2026.acl-long.921.pdf
- Local PDF: pdf/2026-10-12_02_Less is More_ Improving LLM Reasoning with Minimal Test-Time Intervention.pdf

Recent progress in large language models (LLMs) has focused on test-time scaling to improve reasoning via increased inference computation, but often at the cost of efficiency. We revisit test-time behavior and uncover a simple yet underexplored phenomenon: reasoning uncertainty is highly localized—only a small subset of high-entropy tokens dominantly affects output correctness. Motivated by this, we propose Minimal Test-Time Intervention (MTI), a training-free framework that enhances reasoning accuracy and stability with minimal overhead. MTI includes: (i) Selective CFG intervention, applying classifier-free guidance only at uncertain positions; and (ii) Lightweight negative-prompt guidance, reusing the main model’s KV cache to approximate unconditional decoding efficiently. MTI yields consistent gains across general, coding, and STEM tasks—e.g., +9.28% average improvement on six benchmarks for DeepSeek-R1-7B and +11.25% on AIME2024 using Ling-mini-2.0—while remaining highly efficient.

## 3. HalluGuard: Evidence-Grounded Small Reasoning Models to Mitigate Hallucinations in Retrieval-Augmented Generation

- Authors: Loris Bergeron, Ioana Buhnila, Jerome Francois, Radu State
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.6418522903739805
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.835/
- PDF: https://aclanthology.org/2026.findings-acl.835.pdf
- Local PDF: pdf/2026-10-12_03_HalluGuard_ Evidence-Grounded Small Reasoning Models to Mitigate Hallucinations in Retrieval-Augmented Generation.pdf

Large Language Models excel at NLP tasks but remain prone to hallucinations, limiting trust in real-world applications. We present HalluGuard, a 4B-parameter Small Reasoning Model (SRM) designed as a guardrail for Retrieval-Augmented Generation (RAG) pipelines, which classify document-claim pairs as grounded or hallucinated in closed-book, document-grounded settings and produces evidence-grounded justifications. Our approach combines (i) a domain-agnostic synthetic dataset derived from FineWeb and refined through multi-stage curation and data reformation, (ii) synthetic grounded and hallucinated claims, and (iii) preference-based fine-tuning with Odds Ratio Preference Optimization (ORPO) to distill large-model reasoning into a smaller backbone. On the RAGTruth subset of the LLM-AggreFact benchmark, HalluGuard achieves 84.4% balanced accuracy (BAcc), surpassing specialized models, MiniCheck (7B; 84.0%) and Granite Guardian 3.3 (8B; 82.2%) while using roughly half their parameters. Across the benchmark, it reaches 77.1% BAcc, surpassing larger general-purpose LLMs such as GPT-4o (75.9%). HalluGuard and datasets will be released upon acceptance.

## 4. AgentOCR: Reimagining Agent History via Optical Self-Compression

- Authors: Lang Feng, Fuchao Yang, Feng Chen, Xin Cheng, Haiyang Xu, Zhenglin Wan, Ming Yan, Bo An
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.641238649523369
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.230/
- PDF: https://aclanthology.org/2026.acl-long.230.pdf
- Local PDF: pdf/2026-10-12_04_AgentOCR_ Reimagining Agent History via Optical Self-Compression.pdf

Recent advances in large language models (LLMs) enable agentic systems trained with reinforcement learning (RL) over multi-turn interaction, but practical deployment is bottlenecked by rapidly growing textual histories that inflate token and memory costs. We introduce AgentOCR, a framework that exploits visual tokens’ superior information density by representing the accumulated observation-action history as a compact rendered image. To make multi-turn rollouts scalable, AgentOCR proposes segment optical caching. By decomposing history into hashable segments and maintaining a visual cache, this mechanism eliminates redundant re-rendering. Beyond fixed rendering, AgentOCR introduces agentic self-compression, where the agent actively emits a compression rate and is trained with compression-aware reward to adaptively balance task success and token efficiency. We conduct extensive experiments on challenging agentic benchmarks, ALFWorld and search-based QA. Remarkably, AgentOCR preserves over 95% of text-based agent performance while substantially reducing token consumption (>50%), yielding consistent token and memory efficiency. Further analysis validates a 20 × rendering speedup from optical caching and effective self-compression balancing. Our code is available at https://github.com/langfengQ/AgentOCR .

## 5. Placing Puzzle Pieces Where They Matter: A Question Augmentation Framework for Reinforcement Learning

- Authors: Yangyi Fang, Haolin Shi
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.64096406425214
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.969/
- PDF: https://aclanthology.org/2026.acl-long.969.pdf
- Local PDF: pdf/2026-10-12_05_Placing Puzzle Pieces Where They Matter_ A Question Augmentation Framework for Reinforcement Learning.pdf

Reinforcement learning has become a powerful approach for enhancing large language model reasoning, but faces a fundamental dilemma: training on easy problems can cause overfitting and pass@k degradation, while training on hard problems often results in sparse rewards. Recent question augmentation methods address this by prepending partial solutions as hints. However, uniform hint provision may introduce redundant information while missing critical reasoning bottlenecks, and excessive hints can reduce reasoning diversity, causing pass@k degradation. We propose PieceHint , a hint injection framework that strategically identifies and provides critical reasoning steps during training. By scoring the importance of different reasoning steps, selectively allocating hints based on problem difficulty, and progressively withdrawing scaffolding, PieceHint enables models to transition from guided learning to independent reasoning. Experiments on six mathematical reasoning benchmarks show that our 1.5B model achieves comparable average performance to 32B baselines while preserving pass@k diversity across all k values.

## 6. LiveCLKTBench: Towards Reliable Evaluation of Cross-Lingual Knowledge Transfer in Multilingual LLMs

- Authors: Pei-Fu Guo, Yun-Da Tsai, Chun-Chia Hsu, Kai-Xin Chen, Ya An Tsai, Kai-Wei Chang, Nanyun Peng, Mi-Yen Yeh, Shou-De Lin
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.6399440645397014
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.694/
- PDF: https://aclanthology.org/2026.acl-long.694.pdf
- Local PDF: pdf/2026-10-12_06_LiveCLKTBench_ Towards Reliable Evaluation of Cross-Lingual Knowledge Transfer in Multilingual LLMs.pdf

Evaluating cross-lingual knowledge transfer in large language models (LLMs) is challenging, as correct answers in a target language may arise either from genuine transfer or from prior exposure during pre-training. We present LiveCLKTBench, an automated generation pipeline specifically designed to isolate and measure cross-lingual knowledge transfer. Our pipeline identifies self-contained, time-sensitive knowledge entities from real-world domains, filters them based on temporal occurrence, and verifies them against the model’s knowledge. The documents of these valid entities are then used to generate factual questions, which are translated into multiple languages to evaluate transferability across linguistic boundaries. Using LiveCLKTBench, we evaluate several LLMs across five languages and observe that cross-lingual transfer is strongly influenced by linguistic distance and often asymmetric across language directions. While larger models improve transfer, the gains diminish with scale and vary across domains. These findings provide new insights into multilingual transfer and demonstrate the value of LiveCLKTBench as a reliable benchmark for future research.

## 7. MobileLLM-Flash: Latency-Guided On-Device LLM Design for Industry Scale Deployment

- Authors: Hanxian Huang, Igor Fedorov, Andrey Gromov, Bernard Beckerman, Naveen Suda, David Eriksson, Maximilian Balandat, Rylan Conway, Patrick Huber, Chinnadhurai Sankar, Ayushi Dalmia, Zechun Liu, Lemeng Wu, Tarek Elgamal, Adithya Sagar, Vikas Chandra, Raghuraman Krishnamoorthi
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.639055271357992
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-industry.51/
- PDF: https://aclanthology.org/2026.acl-industry.51.pdf
- Local PDF: pdf/2026-10-12_07_MobileLLM-Flash_ Latency-Guided On-Device LLM Design for Industry Scale Deployment.pdf

Real-time AI experiences call for on-device large language models (OD-LLMs) optimized for efficient deployment on resource-constrained hardware. The most useful OD-LLMs produce near-real-time responses and exhibit broad hardware compatibility, maximizing user reach. We present a methodology for designing such models using hardware-in-the-loop architecture search under mobile latency constraints. This system is amenable to industry-scale deployment: it generates models deployable without custom kernels and compatible with standard mobile runtimes like Executorch. Our methodology avoids specialized attention mechanisms and instead uses attention skipping for long-context acceleration. Our approach jointly optimizes model architecture (layers, dimensions) and attention pattern. To efficiently evaluate candidates, we treat each as a pruned version of a pretrained backbone with inherited weights, thereby achieving high accuracy with minimal continued pretraining. We leverage the low cost of latency evaluation in a staged process: learning an accurate latency model first, then searching for the Pareto-frontier across latency and quality.This yields MobileLLM-Flash, a family of foundation models (350M, 650M, 1.4B) for efficient on-device use with strong capabilities, supporting up to 8k context length. MobileLLM-Flash delivers up to 1.8x and 1.6x faster prefill and decode on mobile CPUs with comparable or superior quality. Our analysis of Pareto-frontier design choices offers actionable principles for OD-LLM design.

## 8. Do LLMs Know Tool Irrelevance? Demystifying Structural Alignment Bias in Tool Invocations

- Authors: Yilong Liu, Xixun Lin, Pengfei Cao, Ge Zhang, Fang Fang, Yanan Cao
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.638189874531424
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1473/
- PDF: https://aclanthology.org/2026.acl-long.1473.pdf
- Local PDF: pdf/2026-10-12_08_Do LLMs Know Tool Irrelevance_ Demystifying Structural Alignment Bias in Tool Invocations.pdf

Large language models (LLMs) have demonstrated impressive capabilities in utilizing external tools. In practice, however, LLMs are often exposed to tools that are irrelevant to the user’s query, in which case the desired behavior is to refrain from invocations. In this work, we identify a widespread yet overlooked mechanistic flaw in tool refusal, which we term structural alignment bias: Even when a tool fails to serve the user’s goal, LLMs still tend to invoke it whenever query attributes can be validly assigned to tool parameters. To systematically study this bias, we introduce SABEval, a new dataset that decouples structural alignment from semantic relevance. Our analysis shows that structural alignment bias induces severe tool-invocation errors in LLMs, yet remains largely unaccounted for in existing evaluations. To investigate the internal mechanisms underlying this bias, we propose Contrastive Attention Attribution, which reveals two competing pathways for semantic checking and structural matching. The relative strength of these pathways drives LLMs’ tool invocation decisions. Based on these findings, we further introduce a rebalancing strategy that effectively mitigates structural alignment bias, as demonstrated by extensive experiments, without degrading general tool-use capabilities.

## 9. OneRec-Think: In-Text Reasoning for Generative Recommendation

- Authors: Zhanyu Liu, Shiyao Wang, Xingmei Wang, Rongzhou Zhang, Jiaxin Deng, Honghui Bao, Jinghao Zhang, Wuchao Li, PengFei Zheng, Xiangyu Wu, Yifei Hu, Qigen Hu, Xinchen Luo, Lejian Ren, Zhang Zixing, Qianqian Wang, Kuo Cai, Yunfan Wu, Hongtao Cheng, Zexuan Cheng, Lu Ren, Huanjie Wang, Yi Su, Ruiming Tang, Kun Gai, Guorui Zhou
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.6378895379284515
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.123/
- PDF: https://aclanthology.org/2026.acl-long.123.pdf
- Local PDF: pdf/2026-10-12_09_OneRec-Think_ In-Text Reasoning for Generative Recommendation.pdf

The powerful generative capacity of Large Language Models (LLMs) has instigated a paradigm shift in recommendation. However, existing generative models (e.g., OneRec) operate as implicit predictors, critically lacking the capacity for explicit and controllable reasoning—a key advantage of LLMs. To bridge this gap, we propose OneRec-Think, a unified framework that seamlessly integrates dialogue, reasoning, and personalized recommendation. OneRec-Think incorporates: (1) Itemic Alignment: cross-modal Item-Textual Alignment for semantic grounding; (2) Reasoning Activation: Reasoning Scaffolding to activate LLM reasoning within the recommendation context; and (3) Reasoning Enhancement, where we design a recommendation-specific reward function that accounts for the multi-validity nature of user preferences. Experiments across public benchmarks show state-of-the-art performance. Moreover, our proposed “Think-Ahead” architecture enables effective industrial deployment, achieving a 0.159% gain in APP Stay Time and validating the practical efficacy of the model’s explicit reasoning capability.

## 10. Efficient Multi-Agent System Training with Data Influence-Oriented Tree Search

- Authors: Wentao Shi, Zichun Yu, Fuli Feng, Xiangnan He, Chenyan Xiong
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.637761154675837
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.296/
- PDF: https://aclanthology.org/2026.acl-long.296.pdf
- Local PDF: pdf/2026-10-12_10_Efficient Multi-Agent System Training with Data Influence-Oriented Tree Search.pdf

Large Language Model (LLM) based multi-agent systems (MAS) show strong potential for tackling complex tasks through collaborative intelligence. Monte Carlo Tree Search (MCTS) based methods provide promising approaches for enhancing MAS self-training by generating synthetic data, using Q-values to estimate agent contributions. However, relying solely on Q-values may misalign with the goal of selecting data most beneficial for MAS improvement. To address this discrepancy, we propose D ata I nfluence-oriented T ree S earch ( DITS ), a novel framework that incorporates influence scores to guide both tree search and data selection in data synthesis. By leveraging influence scores, we effectively identify the most impactful data for MAS improvement, thereby enhancing model performance. Furthermore, we derive a novel influence score estimation method tailored for non-differentiable metrics, significantly reducing computational overhead by calculating performance changes on the validation set. Extensive experiments on three different multi-agent tasks demonstrate the robustness and effectiveness of the proposed methods. Notably, our findings reveal that allocating more resources to estimate influence scores, rather than Q-values, during data synthesis can more effectively and efficiently enhance model training. The code is available at https://anonymous.4open.science/r/DITS-F1C4/ .

## 11. Where Paths Split: Localized, Calibrated Control of Moral Reasoning in Large Language Models

- Authors: Chenchen Yuan, Zheyu Zhang, Gjergji Kasneci
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.63757495849548
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1933/
- PDF: https://aclanthology.org/2026.acl-long.1933.pdf
- Local PDF: pdf/2026-10-12_11_Where Paths Split_ Localized, Calibrated Control of Moral Reasoning in Large Language Models.pdf

Large language models often display heterogeneous moral preferences across settings. We study inference-time steering toward a desired ethical framework while preserving general competence. We present Convergent-Divergent Routing, which traces and edits minimal branch points inside transformer blocks where ethical-framework-related pathways first converge and then diverge. Gating non-target branches at these loci blocks the downstream propagation while leaving upstream computations intact. We find that this intervention alone increases targeted ethical-framework reasoning. To achieve fine-grained control, we adapt Common Spatial Patterns to the residual stream and extract, for each branch-point layer, a pair of directions that discriminate between utilitarian and deontological frameworks. We then introduce Dual Logit Calibration, a closed-form, minimum- ℓ 2 -norm update that moves the residual within this two-dimensional subspace so the resulting directional projections align with user-specified preference weights. Experiments on real-life moral dilemmas show that our method reliably achieves preference calibration and largely preserves general capabilities, outperforming recent baselines while providing an interpretable mechanism.

## 12. SynthFix: Adaptive Neuro-Symbolic Code Vulnerability Repair

- Authors: Yifan Zhang, Jieyu Li, Kexin Pei, Yu Huang, Kevin Leach
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.6374010652997737
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1339/
- PDF: https://aclanthology.org/2026.findings-acl.1339.pdf
- Local PDF: pdf/2026-10-12_12_SynthFix_ Adaptive Neuro-Symbolic Code Vulnerability Repair.pdf

Large Language Models (LLMs) show promise for automated code repair but often struggle with the complex semantic and structural correctness required. We present SynthFix, a hybrid neural-symbolic framework that improves LLM-based vulnerability repair by unifying code synthesis with compiler-informed symbolic feedback. The core of our approach is an adaptive training strategy where a neural Router Model directs code samples to either Supervised Fine-Tuning (SFT) to learn common patterns or Reward Fine-Tuning (RFT) with symbolic rewards for complex, iterative refinement. On the FixJS (JavaScript) and CodeFlaws (C) benchmarks, SynthFix achieves up to 18% relative improvement in CodeBLEU/CrystalBLEU and 32% in Exact Match over strong SFT and RFT baselines. Our results show that this adaptive combination of training strategies, which mirrors how developers alternate between pattern application and tool feedback, significantly improves the accuracy and efficiency of LLM-based vulnerability repair. Our code and data are available at https://github.com/CoderDoge1108/SynthFix .

## 13. Empowering Multi-Turn Tool-Integrated Agentic Reasoning with Group Turn Policy Optimization

- Authors: Yifeng Ding, Hung Le, Songyang Han, Kangrui Ruan, Zhenghui Jin, Varun Kumar, Zijian Wang, Anoop Deoras
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.636897858665355
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1962/
- PDF: https://aclanthology.org/2026.acl-long.1962.pdf
- Local PDF: pdf/2026-10-12_13_Empowering Multi-Turn Tool-Integrated Agentic Reasoning with Group Turn Policy Optimization.pdf

Training Large Language Models (LLMs) for multi-turn Tool-Integrated Reasoning (TIR) – where models iteratively reason, generate code, and verify through execution – remains challenging for existing reinforcement learning (RL) approaches. Current RL methods, exemplified by Group Relative Policy Optimization (GRPO), suffer from coarse-grained, trajectory-level rewards that provide insufficient learning signals for complex multi-turn interactions, leading to training stagnation. To address this issue, we propose Group Turn Policy Optimization (GTPO), a novel RL algorithm specifically designed for training LLMs on multi-turn TIR tasks. GTPO introduces three key innovations: (1) turn-level reward assignment that provides fine-grained feedback for individual turns, (2) return-based advantage estimation where normalized discounted returns are calculated as advantages, and (3) self-supervised reward shaping that exploits self-supervision signals from generated code to densify sparse binary outcome-based rewards. Our comprehensive evaluation demonstrates that GTPO outperforms GRPO by 3.0% across diverse math reasoning benchmarks, establishing its effectiveness. GTPO also improves GRPO by 3.9% on commonsense reasoning and program synthesis tasks, demonstrating its generalizability to non-math domains. Importantly, GTPO incurs negligible overhead, ensuring its practicality for real-world scenarios.

## 14. Distilling the Essence, Discarding the Dross: Improving Fairness in Multimodal Large Language Models via Historical Reflection-Guided Prompt Optimization

- Authors: Juncheng Hu, Jiming Yu, Rui Song, Kedi Lyu, Yingji Li, Zheli Liu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.636660924280179
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1459/
- PDF: https://aclanthology.org/2026.findings-acl.1459.pdf
- Local PDF: pdf/2026-10-12_14_Distilling the Essence, Discarding the Dross_ Improving Fairness in Multimodal Large Language Models via Historical Refl.pdf

ocial bias in Multimodal Large Language Models (MLLMs) has become an increasingly important concern. Prompt-based approaches offer a lightweight solution for debiasing; however, existing methods rely heavily on handcrafted prompts that are brittle, highly context-sensitive, and difficult to generalize across tasks, bias types, and multimodal settings. In this work, we propose Historical Reflection-Guided Prompt Optimization (HRPO), an adaptive self-debiasing framework for black-box MLLMs that automatically optimizes task-specific debiasing prompts to suppress stereotypical outputs. To mitigate forgetting during prompt optimization, we introduce Historical Contrastive Self-Reflection (HCSR), which performs contrastive reflection over positive and negative optimization histories, enabling the model to retain effective prompts and avoid redundant exploration, thereby improving optimization efficiency. Experiments on three benchmarks involving eight open-source and two closed-source MLLMs, covering ten singular and two intersectional bias types, demonstrate that HRPO achieves strong debiasing performance while offering improved interpretability, generalization, and robustness. Code is available at: https://github.com/liyingji1996/HRPO .

## 15. Bridging the Culture Gap: A Framework for LLM-Driven Socio-Cultural Localization of Math Word Problems in Low-Resource Languages

- Authors: Israel Abebe Azime, Tadesse Destaw Belay, Dietrich Klakow, Philipp Slusallek, Anshuman Chhabra
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.6365554343629705
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.42/
- PDF: https://aclanthology.org/2026.findings-acl.42.pdf
- Local PDF: pdf/2026-10-12_15_Bridging the Culture Gap_ A Framework for LLM-Driven Socio-Cultural Localization of Math Word Problems in Low-Resource L.pdf

Large language models (LLMs) have demonstrated significant capabilities in solving mathematical problems expressed in natural language. However, multilingual and culturally-grounded mathematical reasoning in low-resource languages lags behind English due to the scarcity of socio-cultural task datasets that reflect accurate native entities such as person names, organization names, and currencies. Existing multilingual benchmarks are predominantly produced via translation and typically retain English-centric entities, owing to the high cost associated with human annotator-based localization. Moreover, automated localization tools are limited, and hence, truly localized datasets remain scarce. To bridge this gap, we introduce a framework for LLM-driven cultural localization of math word problems that automatically constructs datasets with native names, organizations, and currencies from existing sources. We find that translated benchmarks can obscure true multilingual math ability under appropriate socio-cultural contexts. Through extensive experiments, we also show that our framework can help mitigate English-centric entity bias and improve robustness when native entities are introduced across various languages.

## 16. T2I-ReasonBench: Benchmarking Reasoning-Informed Text-to-Image Generation

- Authors: Kaiyue Sun, Rongyao Fang, Chengqi Duan, Xian Liu, Aoxue Li, Xihui Liu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.636302525589635
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.433/
- PDF: https://aclanthology.org/2026.findings-acl.433.pdf
- Local PDF: pdf/2026-10-12_16_T2I-ReasonBench_ Benchmarking Reasoning-Informed Text-to-Image Generation.pdf

Text-to-image (T2I) generative models have achieved remarkable progress, demonstrating exceptional capability in synthesizing high-quality images from textual prompts. While existing research and benchmarks have extensively evaluated the ability of T2I models to follow the literal meaning of prompts, their ability to reason over prompts with domain knowledge to uncover implicit meaning and contextual nuances remains underexplored. To bridge this gap, we introduce T2I-ReasonBench, a novel benchmark designed to explore the knowledge-driven reasoning capabilities of T2I models.T2I-ReasonBench comprises 800 meticulously designed prompts organized into four dimensions: (1) Idiom Interpretation , (2) Textual Image Design , (3) Entity Reasoning , and (4) Scientific Reasoning . These dimensions challenge models to integrate domain knowledge, infer implicit meaning, and resolve contextual ambiguities. To quantify the performance, we introduce a two-stage evaluation framework: a large language model (LLM) generates prompt-specific question-criterion pairs that evaluate if the image includes the essential elements resulting from correct reasoning; a multimodal LLM (MLLM) then scores the generated image against these criteria. Our comprehensive study across 16 state-of-the-art diffusion and unified multimodal models (UMMs) reveal two primary bottlenecks. First, many models lack the foundational reasoning ability to fully comprehend complex prompts. Second, even models with stronger reasoning modules exhibit a persistent gap between their internal understanding and the final generated image. This highlights an urgent need for the next generation of T2I systems to not only improve their reasoning capability but also to enhance integration between reasoning and synthesis.

## 17. SHAPE: Unifying Safety, Helpfulness and Pedagogy for Educational LLMs

- Authors: Sihang Zhao, Kangrui Yu, Youliang Yuan, Pinjia He, Hongyi Wen
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.6361005201863352
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.529/
- PDF: https://aclanthology.org/2026.acl-long.529.pdf
- Local PDF: pdf/2026-10-12_17_SHAPE_ Unifying Safety, Helpfulness and Pedagogy for Educational LLMs.pdf

Large Language Models (LLMs) have been widely explored in educational scenarios. We identify a critical vulnerability in current educational LLMs, pedagogical jailbreaks, where students use answer-inducing prompts to elicit solutions rather than scaffolded instructions. To enable systematic study, we unify and formalize safe, helpful, and pedagogical behaviors with a knowledge-mastery graph and introduce SHAPE, a benchmark of 9,087 student-question pairs for evaluating tutoring behavior under adversarial pressure. We propose a graph-augmented tutoring pipeline that infers prerequisite concepts from queries, identifies mastery gaps, and routes generation between instructing and problem-solving via explicit gating. Experiments across multiple LLMs show that our method yields significantly improved safety under two pedagogical jailbreak settings, while maintaining near-ceiling helpfulness under the same evaluation protocol. Our code and data are available at https://github.com/MAPS-research/SHaPE

## 18. Data Efficient RLVR via Off-Policy Influence Guidance

- Authors: Erle Zhu, Dazhi Jiang, Yuan Wang, Xujun Li, Jiale Cheng, Yuxian Gu, Yilin Niu, Aohan Zeng, Jie Tang, Minlie Huang, Hongning Wang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.6360215002368097
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.2141/
- PDF: https://aclanthology.org/2026.acl-long.2141.pdf
- Local PDF: pdf/2026-10-12_18_Data Efficient RLVR via Off-Policy Influence Guidance.pdf

Data selection is a critical aspect of Reinforcement Learning with Verifiable Rewards (RLVR) for enhancing the reasoning capabilities of large language models (LLMs). Current data selection methods are largely heuristic-based, lacking theoretical guarantees and generalizability. This work proposes a theoretically-grounded approach using influence functions to estimate the contribution of each data point to the learning objective. To overcome the prohibitive computational cost of policy rollouts required for online influence estimation, we introduce an off-policy influence estimation method that efficiently approximates data influence using pre-collected offline trajectories. Furthermore, to manage the high-dimensional gradients of LLMs, we employ sparse random projection to reduce dimensionality and improve storage and computation efficiency. Leveraging these techniques, we develop Curriculum RL with Off-Policy Influence guidance (CROPI), a multi-stage RL framework that iteratively selects the most influential data for the current policy. Experiments on models up to 7B parameters demonstrate that CROPI significantly accelerates training. On a 1.5B model, it achieves a 2.66x step-level acceleration while using only 10% of the data per stage compared to full-dataset training. Our results highlight the substantial potential of influence-based data selection for efficient RLVR.

## 19. Learn Like Humans: Use Meta-cognitive Reflection for Efficient Self-Improvement

- Authors: Xinmeng Hou, Bohao Qu, Wuqi Wang, Peiliang Gong, Qing Guo, Yang Liu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.6358835187885004
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1329/
- PDF: https://aclanthology.org/2026.acl-long.1329.pdf
- Local PDF: pdf/2026-10-12_19_Learn Like Humans_ Use Meta-cognitive Reflection for Efficient Self-Improvement.pdf

While Large Language Models (LLMs) enable complex autonomous behavior, current agents remain constrained by static, human-designed prompts that limit adaptability. Existing self-improving frameworks attempt to bridge this gap but typically rely on inefficient, multi-turn recursive loops that incur high computational costs. To address this, we propose Metacognitive Agent with Reflective Self-improvement (MARS), a framework that achieves efficient self-evolution within a single recurrence cycle. Inspired by educational psychology, MARS mimics human learning by integrating principle-based reflection (abstracting normative rules to avoid errors) and procedural reflection (deriving step-by-step strategies for success). By synthesizing these insights into optimized instructions, MARS allows agents to systematically refine their reasoning logic without continuous online feedback. Extensive experiments on six benchmarks demonstrate that MARS outperforms state-of-the-art self-evolving systems while significantly reducing computational overhead. Code is available at https://github.com/Paparare/MARS/tree/main

## 20. BWLA: Breaking the Barrier of W1AX Post-Training Quantization for LLMs

- Authors: Zhixiong Zhao, Zukang Xu, Dawei Yang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.635462459305194
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.880/
- PDF: https://aclanthology.org/2026.acl-long.880.pdf
- Local PDF: pdf/2026-10-12_20_BWLA_ Breaking the Barrier of W1AX Post-Training Quantization for LLMs.pdf

Large language models (LLMs) have driven major progress in NLP, yet their substantial memory and compute demands still hinder practical deployment. Binarization can compress weights to 1 bit, fundamentally lowering compute and bandwidth cost. However, existing methods cannot address activation heavy tails and thus must keep activations in high precision, preventing true end-to-end acceleration. To overcome this limitation, we propose BWLA, the first post-training quantization framework that preserves high accuracy while achieving 1-bit weight quantization together with low-bit activations (e.g., 6 bits). The Orthogonal-Kronecker Transformation (OKT) learns an orthogonal mapping via EM minimization, converting unimodal weights into symmetric bimodal forms while suppressing activation tails and incoherence. The Proximal SVD Projection (PSP) then performs lightweight low-rank refinement through proximal SVD projection, further enhancing quantizability with minimal overhead. On Qwen3-32B, BWLA reaches a Wikitext2 perplexity of 11.92 under 6-bit activations (vs. 38 from SOTA), improves five zero-shot tasks by more than 70%, and delivers 3.26× inference speedup, demonstrating strong potential for real-world LLM compression and acceleration. The code will be available at BWLA .

## 21. Lost in Diffusion: Uncovering Hallucination Patterns and Failure Modes in Diffusion Large Language Models

- Authors: Zhengnan Guo, Fei Tan
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.63543084018303
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.882/
- PDF: https://aclanthology.org/2026.findings-acl.882.pdf
- Local PDF: pdf/2026-10-12_21_Lost in Diffusion_ Uncovering Hallucination Patterns and Failure Modes in Diffusion Large Language Models.pdf

While Diffusion Large Language Models (dLLMs) have emerged as a promising non-autoregressive paradigm comparable to auto-regressive (AR) models, their faithfulness, specifically regarding hallucination, remains largely underexplored. To bridge this gap, we present the first controlled comparative study to evaluate hallucination patterns in dLLMs. Our results demonstrate that current dLLMs exhibit a higher propensity for hallucination than AR counterparts controlled for architecture, scale, and pre-training weights. Furthermore, an analysis of inference-time compute reveals divergent dynamics: while quasi-autoregressive generation suffers from early saturation, non-sequential decoding unlocks potential for continuous refinement. Finally, we identify distinct failure modes unique to the diffusion process, including premature termination, incomplete denoising, and context intrusion. Our findings underscore that although dLLMs have narrowed the performance gap on general tasks, their distinct hallucination mechanisms pose a critical challenge to model reliability.

## 22. Context-Agent: Dynamic Discourse Trees for Non-Linear Dialogue

- Authors: Junan Hu, Shudan Guo, Wenqi Liu, Jianhua Yin, Yinwei Wei
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.635151604087937
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1472/
- PDF: https://aclanthology.org/2026.findings-acl.1472.pdf
- Local PDF: pdf/2026-10-12_22_Context-Agent_ Dynamic Discourse Trees for Non-Linear Dialogue.pdf

Large Language Models demonstrate outstanding performance in many language tasks but still face fundamental challenges in managing the non-linear flow of human conversation. The prevalent approach of treating dialogue history as a flat, linear sequence is misaligned with the intrinsically hierarchical and branching structure of natural discourse, leading to inefficient context utilization and a loss of coherence during extended interactions involving topic shifts or instruction refinements. To address this limitation, we introduce Context-Agent, a novel framework that models multi-turn dialogue history as a dynamic tree structure. This approach mirrors the inherent non-linearity of conversation, enabling the model to maintain and navigate multiple dialogue branches corresponding to different topics. Furthermore, to facilitate robust evaluation, we introduce the Non-linear Task Multi-turn Dialogue (NTM) benchmark, specifically designed to assess model performance in long-horizon, non-linear scenarios. Our experiments demonstrate that Context-Agent enhances task completion rates and improves token efficiency across various LLMs, underscoring the value of structured context management for complex, dynamic dialogues. The dataset and code is available at GitHub.

## 23. DP 3 : Differentially Private Prompt Perturbation for Multi-turn LLM Inference

- Authors: Lele Zheng, Chao Zhang, Feiyang Yuan, Ke Cheng, Tao Zhang, Anxiao Song, Yulong Shen
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.6349913630584307
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.924/
- PDF: https://aclanthology.org/2026.findings-acl.924.pdf
- Local PDF: pdf/2026-10-12_23_DP 3 _ Differentially Private Prompt Perturbation for Multi-turn LLM Inference.pdf

Large language models (LLMs) are widely used for text understanding and generation, with increasing deployment in applications involving sensitive user inputs. This raises significant privacy concerns, motivating the adoption of differential privacy (DP) to protect prompts during LLM inference. However, most existing DP methods assume single-turn interactions, whereas real-world usage often relies on multi-turn dialogue. Consequently, these single-turn-based methods break down in multi-turn settings, where recurring tokens repeatedly consume the privacy budget under DP, leading to accumulated privacy loss and degraded cross-turn semantic coherence.To address these challenges, we propose DP 3 , a differentially private prompt perturbation framework for multi-turn LLM inference. DP 3 constructs a perturbation mapping table to reuse perturbations for recurring tokens, reducing redundant privacy costs. It also defines a context-aware utility function that combines embedding distance with attention-based contextual representations to maintain semantic consistency across turns. Additionally, DP 3 introduces a two-stage bucketed exponential mechanism to manage long-tail phenomena in large candidate spaces.Experimental results on multi-turn dialogue tasks demonstrate that DP 3 offers a better privacy-utility trade-off and stronger resistance to inference attacks compared to existing methods. Our code is publicly available at https://github.com/XidianNSS/DP3 .

## 24. Looking Beyond the One: Operationalizing and Eliciting Visual Ambiguity in VLLMs

- Authors: Yuchong Chen, Bowei Zou, Yuhan Chen, Yifan Fan, Xinyu Li, Shujun Cao, Yu Hong
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.634427383657827
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1115/
- PDF: https://aclanthology.org/2026.acl-long.1115.pdf
- Local PDF: pdf/2026-10-12_24_Looking Beyond the One_ Operationalizing and Eliciting Visual Ambiguity in VLLMs.pdf

Visual questions are often ambiguous: the same image–question pair may admit multiple valid answers depending on which region is referenced. However, current Visual Question Answering (VQA) systems typically collapse this ambiguity, committing to a single interpretation during decoding and evaluation. In this work, we study visual question ambiguity from a grounded, region-centric perspective. We operationalize ambiguity as the existence of multiple distinct answer-supporting regions in an image, each independently yielding a valid answer. This formulation makes ambiguity observable without requiring exhaustive multi-answer annotations. Based on this definition, we conduct a systematic empirical study of state-of-the-art Visual Large Language Models (VLLMs). We find that, under default decoding, VLLMs consistently under-report ambiguity—even when multiple valid visual groundings are present. Importantly, probing model hidden states reveals that ambiguity-related signals are already encoded in their internal representations, despite not being reliably expressed in outputs. Finally, we show that selectively activating multi-focus answering based on these signals can recover additional valid answers while avoiding excessive hallucination. Together, our results suggest that ambiguity in VQA is not merely an annotation artifact or capability limitation, but a property that VLLMs internally recognize yet often fail to surface under standard decoding assumptions.

## 25. Cultural Alien Sampler: Open-ended Art Generation Balancing Originality and Coherence

- Authors: Hernandez Artiles, Alejandro, Yakura, Hiromu, Brinkmann, Levin, Canet Sola, Mar, Alhaija, Hassan, Serna, Ignacio, Rahaman, Nasim, Schölkopf, Bernhard, Rahwan, Iyad
- Source: neurips
- Venue type: conference
- Journal: NeurIPS 2025
- Publication status: formally_published
- Publication date: 2026-08-14
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.634100863439342
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://proceedings.neurips.cc/paper_files/paper/2025/hash/ce57a4b9274d44d7692e715ed1876ded-Abstract-Creative_AI_Track.html
- PDF: https://proceedings.neurips.cc/paper_files/paper/2025/file/ce57a4b9274d44d7692e715ed1876ded-Paper-Creative_AI_Track.pdf
- Local PDF: pdf/2026-10-12_25_Cultural Alien Sampler_ Open-ended Art Generation Balancing Originality and Coherence.pdf

In open-ended domains like art, autonomous agents must generate ideas that are both original and internally coherent, yet current Large Language Models (LLMs) either default to familiar cultural patterns or sacrifice coherence when pushed toward novelty. We address this by introducing the Cultural Alien Sampler (CAS), a concept-selection method that explicitly separates compositional fit from cultural typicality. CAS uses two GPT-2 models fine-tuned on WikiArt concepts: a Concept Coherence Model that scores whether concepts plausibly co-occur within artworks, and a Cultural Context Model that estimates how typical those combinations are within individual artists’ bodies of work. CAS targets combinations that are high in coherence and low in typicality, yielding ideas that maintain internal consistency while deviating from learned conventions and embedded cultural context. In a human evaluation (N = 100), our approach outperforms random selection and GPT-4o baselines and achieves performance comparable to human art students in both perceived originality and harmony. Additionally, a quantitative study shows that our method produces more diverse outputs and explores a broader conceptual space than its GPT-4o counterpart, demonstrating that artificial cultural alienness can unlock creative potential in autonomous agents.

## 26. Edit-level Majority Voting Mitigates Over-Correction in LLM-based Grammatical Error Correction

- Authors: Takumi Goto, Yusuke Sakai, Taro Watanabe
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.634004992035723
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.bea-1.60/
- PDF: https://aclanthology.org/2026.bea-1.60.pdf
- Local PDF: pdf/2026-10-12_26_Edit-level Majority Voting Mitigates Over-Correction in LLM-based Grammatical Error Correction.pdf

Grammatical error correction using large language models often suffers from the over-correction issue. To mitigate this, we propose a training-free inference method that performs edit-level majority voting over multiple candidates generated by a single model, without requiring model modifications or additional training. Across nine benchmarks covering English, Czech, German, Ukrainian, Korean, Hindi, and Romanian, the proposed method outperforms both greedy and MBR decoding in most cases. Moreover, it yields stable correction quality regardless of the instruction prompts used. We release two repository supporting GEC datasets and LLM inference.

## 27. LLM-SLM Collaborative Framework of Idiomatic Expression Generation

- Authors: Hui Gao, Changhao Song, Peng Zhang, Jing Zhang, Chang Yang, Liuxian Ge
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.6337536896060056
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.555/
- PDF: https://aclanthology.org/2026.acl-long.555.pdf
- Local PDF: pdf/2026-10-12_27_LLM-SLM Collaborative Framework of Idiomatic Expression Generation.pdf

Idiomatic Expression Generation, which aims to produce idiomatic text from plain text, is a valuable yet challenging NLP task. However, existing methods suffer from the scarcity of parallel data and dependence on high-quality manual annotations. To address this, we propose an iterative LLM-SLM (Large Language Model-Small Language Model) collaborative framework — Auto-IDEA, that replaces human supervision for idiomatic expression data generation. In this self-improving cycle, the LLM constructs parallel corpora (idiomatic and plain text) via bidirectional semantic reconstruction, automatically generating “Locate-Then-Polish” (LTP) annotations; the SLM filters low-quality corpora while continuously enhancing its verification ability through incremental learning. We instantiate Auto-IDEA for Chinese Idiom Polishing (CIP), constructing CIP-200K, a large-scale dataset of 206K parallel sentences with LTP annotations. The Qwen3-8B fine-tuned on CIP-200K achieves a 25.2% absolute Idiom Polishing Accuracy (IPA) improvement over a supervised fine-tuning (SFT) baseline, outperforming DeepSeek-R1 by 6.2%. Extensive experiments (e.g., Chinese idiom cloze tests and English idiom generation tasks) and human evaluations verify the generalization and effectiveness of Auto-IDEA, demonstrating a new pathway for high-quality, annotation-free data generation through LLM-SLM collaboration.

## 28. Cogito: A Cognitive Agentic Framework Driven by Dynamic Graph of Thoughts for Financial Report Generation

- Authors: Chen Lifan, Wei Ding, Jingwen Yang, Xiuze Zhou, Jingan Chen, Fan Lin
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.6337303875865508
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.430/
- PDF: https://aclanthology.org/2026.findings-acl.430.pdf
- Local PDF: pdf/2026-10-12_28_Cogito_ A Cognitive Agentic Framework Driven by Dynamic Graph of Thoughts for Financial Report Generation.pdf

Financial report generation is a complex task that requires gathering and reasoning over multi-source information. Recent advances in Large Language Models have made them a promising solution for automating this process. However, the reasoning paths in traditional Chain-of-Thought paradigms are inherently constrained by predefined, static computational topologies, rendering them ill-equipped to handle the dynamic uncertainties of real-world financial environments. To tackle this challenge, we propose Cogito, a cognitively grounded agentic framework for professional financial report generation. At its core, Cogito is driven by Dynamic Graph of Thoughts, a novel reasoning mechanism that models the agent’s reasoning process as an evolving topology for adaptive exploration.We further introduce a Social Collaboration Mechanism to facilitate coordinated agent interaction. Finally, Cogito is instantiated as a multi-agent system, where four specialized agents collaboratively execute the end-to-end report generation task. Extensive experiments on enterprise- and industry-level financial report generation benchmarks demonstrate the superiority of Cogito in data quality, analytical validity, and presentation quality.

## 29. Memory-Efficient Structured Backpropagation for On-Device LLM Fine-Tuning

- Authors: JuneYoung Park, Yuri Hong, Seongwan Kim, Jaeho Lee
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.633666378961803
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-industry.62/
- PDF: https://aclanthology.org/2026.acl-industry.62.pdf
- Local PDF: pdf/2026-10-12_29_Memory-Efficient Structured Backpropagation for On-Device LLM Fine-Tuning.pdf

On-device fine-tuning enables privacy-preserving personalization of large language models, but mobile devices impose severe memory constraints, typically 6–12GB shared across all workloads. Existing approaches force a trade-off between exact gradients with high memory (MeBP) and low memory with noisy estimates (MeZO). We propose Memory-efficient Structured Backpropagation (MeSP), which bridges this gap by manually deriving backward passes that exploit LoRA’s low-rank structure. Our key insight is that the intermediate projection h = xA can be recomputed during backward at minimal cost since rank r ≪ d in , eliminating the need to store it. MeSP achieves 49% average memory reduction compared to MeBP on Qwen2.5 models (0.5B–3B) while computing mathematically identical gradients. Our analysis also reveals that MeZO’s gradient estimates show near-zero correlation with true gradients (cosine similarity ≈ 0.001), explaining its slow convergence. MeSP reduces peak memory from 361MB to 136MB for Qwen2.5-0.5B, enabling fine-tuning scenarios previously infeasible on memory-constrained devices.

## 30. Beyond the Final Actor: Modeling the Dual Roles of Creator and Editor for Fine-Grained LLM-Generated Text Detection

- Authors: Yang Li, Qiang Sheng, Zhengjia Wang, Yehan Yang, Danding Wang, Juan Cao
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.633248708033965
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.235/
- PDF: https://aclanthology.org/2026.acl-long.235.pdf
- Local PDF: pdf/2026-10-12_30_Beyond the Final Actor_ Modeling the Dual Roles of Creator and Editor for Fine-Grained LLM-Generated Text Detection.pdf

The misuse of large language models (LLMs) requires precise detection of synthetic text. Existing works mainly follow binary or ternary classification settings, which can only distinguish pure human/LLM text or collaborative text at best. This remains insufficient for the nuanced regulation, as the LLM-polished human text and humanized LLM text often trigger different policy consequences. In this paper, we explore fine-grained LLM-generated text detection under a rigorous four-class setting. To handle such complexities, we propose RACE (Rhetorical Analysis for Creator-Editor Modeling), a fine-grained detection method that characterizes the distinct signatures of creator and editor. Specifically, RACE utilizes Rhetorical Structure Theory (RST) to construct a logic graph for the creator’s foundation while extracting Elementary Discourse Unit (EDU)-level features for the editor’s style. Experiments show that RACE outperforms 12 baselines in identifying fine-grained types with low false alarms, offering a policy-aligned solution for LLM regulation.
