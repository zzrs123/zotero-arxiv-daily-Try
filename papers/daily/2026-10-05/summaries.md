# Paper Daily Reading - 2026-10-05

## 1. ACBQ: Adaptive Cross-Block Quantization of Large Language Models

- Authors: Hailing Wang, Jianglin Lu, Yitian Zhang, Huimin Zeng, Yun Fu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.6573636765723614
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1971/
- PDF: https://aclanthology.org/2026.acl-long.1971.pdf
- Local PDF: pdf/2026-10-05_01_ACBQ_ Adaptive Cross-Block Quantization of Large Language Models.pdf

Post-training quantization (PTQ) has emerged as a promising approach for reducing the memory footprint and computational cost of large language models (LLMs), enabling efficient deployment without full model retraining. However, existing PTQ methods struggle to simultaneously support weight–activation joint quantization and extreme low-bit weight quantization. This limitation primarily arises from the depth of LLMs and their strong cross-layer dependencies, which cause quantization errors to propagate and accumulate across layers, ultimately leading to significant performance degradation. In this paper, we present ACBQ, a simple yet effective framework that simultaneously addresses weight–activation joint quantization and extreme weight quantization. We first propose a granular quantization strategy that treats self-attention and FFN as separate quantization units with module-specific optimization objectives. To mitigate the propagation and accumulation of quantization errors across layers, we introduce an adaptive cross-block quantization strategy that explicitly accounts for cross-layer dependencies by encouraging consistency across blocks. Extensive experiments across diverse LLMs, including OPT and the LLaMA family, demonstrate that ACBQ achieves superior performance under both W4A4 and highly aggressive W2 settings, while incurring negligible additional computational overhead.

## 2. Progra: Progress-Aware Reinforcement Learning for Multi-Turn Function Calling

- Authors: Huacan Chai, Zijie Cao, Maolin Ran, Yingxuan Yang, Jianghao Lin, Xin Peng, Hairui Wang, Renjie Ding, Ziyu Wan, Muning Wen, Weiwen Liu, Weinan Zhang, Fei Huang, Ying Wen
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.655527527118876
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.325/
- PDF: https://aclanthology.org/2026.findings-acl.325.pdf
- Local PDF: pdf/2026-10-05_02_Progra_ Progress-Aware Reinforcement Learning for Multi-Turn Function Calling.pdf

Large language models (LLMs) have achieved impressive success in single-turn function calling, yet real-world applications such as travel planning or multi-stage data analysis typically unfold across multi-turn conversations. In these settings, LLMs must not only issue accurate function calls at each step but also maintain progress awareness, the ability to summarize past interactions and plan future actions to ensure coherent, long-horizon task execution. Existing approaches, however, either reduce multi-turn training to isolated single-turn samples, which neglects task-level planning, or employ end-to-end reinforcement learning (RL) that struggles with redundancy and lacks explicit integration of progress awareness. To overcome these limitations, we introduce Progra, a framework that explicitly incorporates progress awareness into LLM training for multi-turn function calling. Progra combines (i) a Progress Awareness Generation (PAG) pipeline, which automatically constructs datasets coupling conversation summaries with future task planning, and (ii) a Progress Awareness-Guided Reinforcement Learning (PAG-RL) algorithm, which integrates progress awareness into RL training to reduce contextual redundancy and improve alignment between local actions and global task completion. Empirical results on two public benchmarks demonstrate that Progra significantly outperforms existing methods, highlighting the effectiveness of progress awareness in enabling robust and efficient multi-turn function calling. Our code is available at https://github.com/FatCatCHC/Progra .

## 3. DMN: A Compositional Framework for Jailbreaking Multimodal LLMs with Multi-Image Inputs

- Authors: Wenzhuo Xu, Zhipeng Wei, Zonghao Ying, Deyue Zhang, Dongdong Yang, Xiangzheng Zhang, Quanchen Zou
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.654870091764801
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.514/
- PDF: https://aclanthology.org/2026.acl-long.514.pdf
- Local PDF: pdf/2026-10-05_03_DMN_ A Compositional Framework for Jailbreaking Multimodal LLMs with Multi-Image Inputs.pdf

Multimodal Large Language Models (MLLMs) are vulnerable to jailbreak attacks, which can elicit harmful responses from MLLMs. Many MLLMs support multi-image inputs, inadvertently introducing new vulnerabilities due to less efforts on multi-image safety alignment. Previous MLLM jailbreak methods only uses a single image, which restricts the attack space: they cannot distribute harmful requests across multiple images, carry abundant information, or exploit additional visual reasoning tasks to distract MLLMs. To address these limitations, in this paper, we propose a compositional jailbreak framework, DMN , which leverages D istributed instruction, M ultimodal evidence and a N umber chain task to fully enhance the jailbreak performance. Extensive experiments show that DMN is highly effective for MLLM jailbreaking, e.g. achieving attack success rates of over 90% on GPT-4o, Gemini-2.5-pro and Claude Sonnet 4, surpassing other baselines by a large margin. This compositional, multi-image jailbreak strategy reveals fundamental weaknesses in their safety mechanisms.

## 4. CAP: Controllable Alignment Prompting for Unlearning in LLMs

- Authors: Zhaokun Wang, Jinyu Guo, Jingwen Pu, Hongli Pu, Meng Yang, Xunlei Chen, Jie Ou, Wenyi Li, Guangchun Luo, Wenhong Tian
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.6547766803698183
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1882/
- PDF: https://aclanthology.org/2026.acl-long.1882.pdf
- Local PDF: pdf/2026-10-05_04_CAP_ Controllable Alignment Prompting for Unlearning in LLMs.pdf

Large language models (LLMs) trained on unfiltered corpora inherently risk retaining sensitive information, necessitating selective knowledge unlearning for regulatory compliance and ethical safety. However, existing parameter-modifying methods face fundamental limitations: high computational costs, uncontrollable forgetting boundaries, and strict dependency on model weight access. These constraints render them impractical for closed-source models, yet current non-invasive alternatives remain unsystematic and reliant on empirical experience. To address these challenges, we propose the Controllable Alignment Prompting for Unlearning (CAP) framework, an end-to-end prompt-driven unlearning paradigm. CAP decouples unlearning into a learnable prompt optimization process via reinforcement learning, where a prompt generator collaborates with the LLM to suppress target knowledge while preserving general capabilities selectively. This approach enables reversible knowledge restoration through prompt revocation. Extensive experiments demonstrate that CAP achieves precise, controllable unlearning without updating model parameters, establishing a dynamic alignment mechanism that overcomes the transferability limitations of prior methods.

## 5. When Facts Change: Temporal Knowledge Conflict Resolution in LLMs

- Authors: Jonas Wallat, Wolfgang Nejdl, Sandipan Sikdar
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.6545445524989986
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.103/
- PDF: https://aclanthology.org/2026.findings-acl.103.pdf
- Local PDF: pdf/2026-10-05_05_When Facts Change_ Temporal Knowledge Conflict Resolution in LLMs.pdf

Retrieval-augmented generation (RAG) systems require large language models (LLMs) to reconcile discrepancies between their parametric memory—knowledge encoded during training—and contextual inputs provided at inference. When these sources conflict, models often exhibit unstable reasoning and inconsistent factual behavior. We investigate how LLMs resolve such conflicts when the discrepancy arises from temporal misalignment—facts that have changed since the model’s knowledge cutoff—and whether mutability, the changeability of facts, can serve as a mediating signal in this process. To do so, we provide WIKIRECENTCHANGES, a temporally grounded benchmark with stable and recently updated facts derived from Wikidata.Our results show that while models spontaneously produce temporal reasoning for facts that actually changed — but almost never for stable ones — this differentiation rarely propagates to their final predictions. Explicitly prompting them to consider mutability increases references to temporal change but does not improve factual accuracy, revealing a disconnect between verbalized reasoning and prediction behavior. We further show that the failure point is scale-dependent: smaller models rarely detect the underlying conflict, while larger models detect it but fail to act on their mutability judgments.

## 6. Prompting Test-Time Scaling Is A Strong LLM Reasoning Data Augmentation

- Authors: Sondos Mahmoud Bsharat, Zhiqiang Shen
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.654522047960225
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.474/
- PDF: https://aclanthology.org/2026.findings-acl.474.pdf
- Local PDF: pdf/2026-10-05_06_Prompting Test-Time Scaling Is A Strong LLM Reasoning Data Augmentation.pdf

Large language models (LLMs) exhibit strong reasoning when guided by chain-of-thought exemplars, yet collecting large, high-quality reasoning datasets remains laborious and resource-intensive. We introduce Prompting Test-Time Scaling (P-TTS), a prompt-space data augmentation framework for enhancing LLM reasoning via fine-tuning. In P-TTS, scaling refers to systematic expansion of the prompt space during offline teacher-data generation, not to increased inference-time compute for the deployed student. Rather than collecting thousands of examples, P-TTS starts from a small pool of 90 manually selected reasoning instances and applies principled instruction templates and paraphrased prompt variants to elicit diverse reasoning trajectories from a teacher model, producing a compact synthetic training set. We fine-tune Qwen-2.5 models of multiple sizes on the resulting data. On reasoning benchmarks including AIME25, MATH500, and GPQA-Diamond, P-TTS consistently improves accuracy over competitive small-data baselines such as S1 and S1.1 (1K-shot), with the largest gains on AIME25 while remaining strong on MATH500 and GPQA-Diamond. P-TTS also improves generalization on out-of-domain reasoning evaluations. Ablations show that exemplar diversity and prompt-space scaling are critical drivers of improvement, suggesting that prompt scaling explores the latent space of reasoning patterns, amplifying LLM problem-solving with minimal annotation overhead. P-TTS offers a practical, low-cost way to elicit strong LLM reasoning in resource-constrained or rapidly evolving domains. Our code and data are available at https://github.com/VILA-Lab/PTTS .

## 7. ReList: A Multi-objective Reasoning Framework for Diversified Listwise Query Recommendation

- Authors: Shuxian Bi, Chenxu Wang, Wenjie Wang, Yueqi Mou, Fuli Feng, Tang Biao, Peng Yan
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.6545156177781335
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-industry.97/
- PDF: https://aclanthology.org/2026.acl-industry.97.pdf
- Local PDF: pdf/2026-10-05_07_ReList_ A Multi-objective Reasoning Framework for Diversified Listwise Query Recommendation.pdf

Related search query recommendation is essential for enhancing user engagement and information discovery on digital platforms. While Large Language Models (LLMs) have shifted the field toward generative retrieval, existing methods suffer from two primary limitations: (1) pointwise generation via beam search often leads to semantic redundancy and wasted retrieval quota, and (2) current listwise approaches lack explicit reasoning, relying on superficial click-through rate (CTR) rewards. In this paper, we propose ReList, a novel framework that transforms related search into a reasoning-enhanced listwise generation task. ReList follows a two-stage training paradigm: first, Reasoning Activation constructs a high-quality dataset by back-translating diverse query lists into Chain-of-Thought (CoT) rationales; second, Alternative Training iteratively evolves the model using Reinforcement Learning with a Gated Multi-Objective Reward and a Corrective SFT mechanism to handle hard samples. Experimental results on real-world search benchmarks and online A/B tests demonstrate that ReList significantly outperforms state-of-the-art methods in both query diversity and user engagement, providing more insightful and logically grounded query recommendations.

## 8. DUD: Decoupled Update Dynamics for Reliable Uncertainty Quantification in Large Language Models

- Authors: Yixin Bu, Runze Xia, Guanyun Zou, Yupeng Ji, Hongliang Dai, Haodong Liu, Piji Li
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.6539207532626197
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1665/
- PDF: https://aclanthology.org/2026.acl-long.1665.pdf
- Local PDF: pdf/2026-10-05_08_DUD_ Decoupled Update Dynamics for Reliable Uncertainty Quantification in Large Language Models.pdf

Accurate Uncertainty Quantification (UQ) is critical for reliable deployment of Large Language Models (LLMs), yet traditional probability-based metrics often fail to capture the model’s true epistemic state. While recent mechanistic approaches leverage hidden state dynamics, they typically aggregate residual stream updates, conflating the distinct roles of parametric memory (Feed-Forward Networks) and contextual processing (Attention). We argue that this aggregation obscures fine-grained mechanistic conflicts, such as memory-context misalignment, that are fundamental indicators of uncertainty. To address this, we introduce D ecoupled U pdate D ynamics ( DUD ), a framework that explicitly decouples FFN and Attention contributions via noise-induced causal interventions. By quantifying the independent restoration capabilities of each module, we construct a dual-stream dynamic profile that captures the model’s internal fragility. Extensive experiments demonstrate that DUD significantly outperforms state-of-the-art baselines in both uncertainty estimation and calibration, while exhibiting superior cross-dataset generalization, validating decoupled dynamics as a robust proxy for model faithfulness.

## 9. Forget What Matters, Keep the Rest: Selective Unlearning of Informative Tokens

- Authors: Seunghee Koh, Sunghyun Baek, Youngdong Kim, Junmo Kim
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.6531915682127893
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1175/
- PDF: https://aclanthology.org/2026.acl-long.1175.pdf
- Local PDF: pdf/2026-10-05_09_Forget What Matters, Keep the Rest_ Selective Unlearning of Informative Tokens.pdf

Unlearning in large language models (LLMs) has emerged as a promising safeguard against adversarial behaviors. When the forgetting loss is applied uniformly without considering token-level semantic importance, model utility can be unnecessarily degraded. Recent studies have explored token-wise loss regularizers that prioritize informative tokens, but largely rely on ground-truth confidence or external linguistic parsers, which limits their ability to capture contextual information or the model’s overall predictive state. Intuitively, function words like “the” primarily serve syntactic roles and are highly predictable with little ambiguity, but informative words admit multiple plausible alternatives with greater uncertainty. Based on this intuition, we propose Entropy-guided Token Weighting (ETW), a token-level unlearning regularizer that uses entropy of the predictive distribution as a proxy for token informativeness. We demonstrate that informative tokens tend to have higher entropy, whereas structural tokens tend to have lower entropy. This behavior enables ETW to achieve more effective unlearning while better preserving model utility than existing token-level approaches.

## 10. AMATA: Adaptive Multi-Agent Trajectory Alignment for Knowledge-Intensive Question Answering

- Authors: Taolin Zhang, Dongyang Li, Chen Chen, Qizhou Chen, Jiuheng Wan, Xiaofeng He, Chengyu Wang, Richang Hong
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.652853269024267
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.359/
- PDF: https://aclanthology.org/2026.acl-long.359.pdf
- Local PDF: pdf/2026-10-05_10_AMATA_ Adaptive Multi-Agent Trajectory Alignment for Knowledge-Intensive Question Answering.pdf

Despite substantial advances in large language models (LLMs), producing factually consistent responses for knowledge-intensive question answering remains challenging. These difficulties are primarily due to hallucination and the limitations of LLMs in bridging long-tail knowledge gaps. To address this, we propose AMATA, an Adaptive Multi-Agent Trajectory Alignment framework that dynamically integrates external knowledge to improve response interpretability and factual grounding. Our architecture leverages six specialized agents that collaboratively perform structured actions for complex question reasoning. We formalize multi-agent collaboration with external tools as a trajectory preference alignment problem, incorporating question-aware agent customization and inter-agent preference harmonization. AMATA introduces two principal innovations: (1) Intra-Trajectory Preference Learning, which learns objective-oriented preferences to prioritize critical agents, and (2) Inter-Agent Dependency Learning, which captures cross-agent tool dependencies through a novel dependency-aware direct preference optimization technique. Empirical results show that AMATA consistently outperforms baseline approaches, knowledge-augmented frameworks, and LLM-based trajectory systems on five established knowledge-intensive QA benchmarks. Further analysis demonstrates the efficiency of our method in reducing token consumption.

## 11. DiffCL: Difference-Aware Contrastive Learning for Automatic Answer Grading with Multi-Level Semantic Modeling

- Authors: Lei Chen, BoYu Gao, Zitao Liu, Tingjie Wan, Weiqi Luo
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.652577643327605
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.979/
- PDF: https://aclanthology.org/2026.findings-acl.979.pdf
- Local PDF: pdf/2026-10-05_11_DiffCL_ Difference-Aware Contrastive Learning for Automatic Answer Grading with Multi-Level Semantic Modeling.pdf

Automated Answer Grading (AAG) is a fundamental task in intelligent education, requiring accurate semantic understanding and reliable modeling of student deviations from reference answers. Despite recent progress, large language models (LLMs) remain insensitive to missing key concepts, exhibit unstable scoring scales, and lack structured scoring semantics in their representation space. To overcome these limitations, we propose a difference-aware AAG framework that integrates heuristic difference labeling with dual-contrastive learning. Semantic difference levels between student and reference answers are automatically inferred through similarity-based heuristics and injected into the model input as explicit prompts, enabling fine-grained perception of semantic deviations. In addition, an InfoNCE-based contrastive objective enforces representation consistency among samples with identical scores, while a hierarchical contrastive constraint guided by score gaps promotes structured separation across different scoring levels. Experiments on benchmark datasets, including SciEntsBank and Beetle, show that the proposed method consistently outperforms cross-entropy–based baselines in accuracy, weighted accuracy, and relevance metrics. Further analyses demonstrate improved robustness and generalization, even when applied to small-scale models. We have made all datasets and the corresponding code publiclyaccessible at: https://github.com/leibnizchen/DiffCL

## 12. SATQuest: A Verifier for Logical Reasoning Evaluation and Reinforcement Fine-Tuning of LLMs

- Authors: Yanxiao Zhao, Yaqian Li, Zihao Bo, Rinyoichi Takezoe, Haojia Hui, Mo Guang, Lei Ren, Xiaolin Qin, Kaiwen Long
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.652422582570521
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.96/
- PDF: https://aclanthology.org/2026.acl-long.96.pdf
- Local PDF: pdf/2026-10-05_12_SATQuest_ A Verifier for Logical Reasoning Evaluation and Reinforcement Fine-Tuning of LLMs.pdf

Large language models (LLMs) exhibit strong general reasoning, yet the community lacks controllable, scalable, and verifiable tools to analyze and improve these abilities. We present SATQuest, a verifier that generates diverse SAT-based reasoning tasks directly from Conjunctive Normal Form (CNF) instances and checks answers objectively with PySAT. SATQuest factorizes evaluation along three orthogonal dimensions—instance, problem type, and question format—enabling fine-grained, multi-dimensional analysis and reinforcement fine-tuning. Randomized CNF generation mitigates memorization and supports reproducible experiments. Using SATQuest, we benchmark a range of open- and closed-weight LLMs and uncover persistent gaps in logical reasoning, particularly on higher-complexity tasks and in transfer beyond familiar mathematical notation to machine or narrative formats. We further show that reinforcement fine-tuning with SATQuest rewards substantially boosts targeted performance and generalizes to larger instances, while cross-format robustness remains challenging. Collectively, SATQuest provides verifier-backed infrastructure for controlled, scalable, and reproducible empirical research on LLM logical reasoning and its training.

## 13. Learning from Mistakes: Negative Reasoning Samples Enhance Out-of-Domain Generalization

- Authors: Tian Xueyun, MingHua Ma, Bingbing Xu, Nuoyan Lyu, Wei Li, Heng Dong, Zheng Chu, Yuanzhuo Wang, Huawei Shen
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.6514644842623065
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1370/
- PDF: https://aclanthology.org/2026.acl-long.1370.pdf
- Local PDF: pdf/2026-10-05_13_Learning from Mistakes_ Negative Reasoning Samples Enhance Out-of-Domain Generalization.pdf

Supervised fine-tuning (SFT) on chain-of-thought (CoT) trajectories demonstrations is a common approach for enabling reasoning in large language models. Standard practices typically only retain trajectories with correct final answers ( positives ) while ignoring the rest ( negatives ). We argue that this paradigm discards substantial supervision and exacerbates overfitting, limiting out-of-domain (OOD) generalization. Specifically, we surprisingly find that incorporating negative trajectories into SFT yields substantial OOD generalization gains over positive-only training, as these trajectories often retain valid intermediate reasoning despite incorrect final answers. To understand this effect in depth, we systematically analyze data, training dynamics, and inference behavior, identifying 22 recurring patterns in negative chains that serve a dual role: they moderate loss descent to mitigate overfitting during training and boost policy entropy by 35.67% during inference to facilitate exploration. Motivated by these observations, we further propose Gain-based LOss Weighting (GLOW), an adaptive, sample-aware scheme that exploits such distinctive training dynamics by rescaling per-sample loss based on inter-epoch progress. Empirically, GLOW efficiently leverages unfiltered trajectories, yielding a 5.51% OOD gain over positive-only SFT on Qwen2.5-7B and boosting MMLU from 72.82% to 76.47% as an RL initialization. Code is available at Github .

## 14. Achieving Multi-Hop Calculation and Safe Abstention in Financial Numerical Reasoning by Metric Graph Constrained LLMs

- Authors: Aoyuan Jiang, Liang Hong, Haoxuan Liu, Rui Wang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.651311568942444
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1273/
- PDF: https://aclanthology.org/2026.acl-long.1273.pdf
- Local PDF: pdf/2026-10-05_14_Achieving Multi-Hop Calculation and Safe Abstention in Financial Numerical Reasoning by Metric Graph Constrained LLMs.pdf

Financial numerical reasoning demands rigorous adherence to domain-specific logic and precise evidence foundation. However, large language models (LLMs) are prone to forced generation when confronting ambiguous evidence or complex recursive dependencies, often hallucinating values to bridge information gaps. To address this, we propose graph-bounded financial reasoning (GBFR), a neuro-symbolic framework that imposes semantic and structural constraints via a financial metric knowledge graph (FMKG). Unlike sequential generation paradigms, our approach employs a parallel graph-constrained reasoning algorithm that orchestrates specialized operators to simultaneously explore heterogeneous derivation paths of complex financial metrics. Through cross-path verification, the framework aggregates only semantically consistent results, ensuring reasoning is bounded by available context. Crucially, this approach enables safe abstention by distinguishing genuine data absence from retrieval failure, thereby preventing ungrounded fabrication. To evaluate this capability, we further construct counterfactual samples by perturbing entities, times, and metrics to synthesize unanswerable scenarios. Empirical evaluations on standard benchmarks demonstrate that GBFR significantly outperforms state-of-the-art baselines.

## 15. ZoomR: Memory Efficient Reasoning through Multi-Granularity Key Value Retrieval

- Authors: David H. Yang, Yuxuan Zhu, Mohammad Mohammadi Amiri, Keerthiram Murugesan, Tejaswini Pedapati, Subhajit Chaudhury, Pin-Yu Chen
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.651267421916762
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.76/
- PDF: https://aclanthology.org/2026.acl-long.76.pdf
- Local PDF: pdf/2026-10-05_15_ZoomR_ Memory Efficient Reasoning through Multi-Granularity Key Value Retrieval.pdf

Large language models (LLMs) have shown great performance on complex reasoning tasks but often require generating long intermediate thoughts before reaching a final answer. During generation, LLMs rely on a key-value (KV) cache for autoregressive decoding. However, the memory footprint of the KV cache grows with output length. Prior work on KV cache optimization mostly focus on compressing the long input context, while retaining the full KV cache for decoding. For tasks requiring long output generation, this leads to increased computational and memory costs. In this paper, we introduce ZoomR, a novel approach that enables LLMs to adaptively compress verbose reasoning thoughts into summaries and uses a dynamic KV cache selection policy that leverages these summaries while also strategically “zooming in” on fine-grained details. By using summary keys as a coarse-grained index during decoding, ZoomR uses the query to retrieve details for only the most important thoughts. This hierarchical strategy significantly reduces memory usage by avoiding full-cache attention at each step. Experiments across math and reasoning tasks show that our approach achieves competitive performance compared to baselines, while reducing inference memory requirements by more than 4 × . These results demonstrate that a multi-granularity KV selection enables more memory efficient decoding, especially for long output generation.

## 16. Latent Agents: A Post-Training Procedure for Internalized Multi-Agent Debate

- Authors: John Seon Keun Yi, Aaron Mueller, Dokyun Lee
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.650542713756984
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.709/
- PDF: https://aclanthology.org/2026.acl-long.709.pdf
- Local PDF: pdf/2026-10-05_16_Latent Agents_ A Post-Training Procedure for Internalized Multi-Agent Debate.pdf

Multi-agent debate has been shown to improve reasoning in large language models (LLMs). However, it is compute-intensive, requiring generation of long transcripts before answering questions. To address this inefficiency, we develop a framework that distills multi-agent debate into a single LLM through a two-stage fine-tuning pipeline combining debate structure learning with internalization via dynamic reward scheduling and length clipping. Across multiple models and benchmarks, our internalized models match or exceed explicit multi-agent debate performance using up to 93% fewer tokens. We then investigate the mechanistic basis of this capability through activation steering, finding that internalization creates agent-specific subspaces: interpretable directions in activation space corresponding to different agent perspectives. We further demonstrate a practical application: by instilling malicious agents into the LLM through internalized debate, then applying negative steering to suppress them, we show that distillation makes harmful behaviors easier to localize and control with smaller reductions in general performance compared to steering base models. Our findings offer a new perspective for understanding multi-agent capabilities in distilled models and provide practical guidelines for controlling internalized reasoning behaviors.

## 17. PRISM: Probing Reasoning, Instruction, and Source Memory in LLM Hallucinations

- Authors: Yuhe Wu, Guangyu Wang, Yuran Chen, Jiatong Zhang, Yutong Zhang, Yujie Chen, Jiaming Shang, Guang Zhang, Zhuang Liu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.6503608362845803
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1551/
- PDF: https://aclanthology.org/2026.acl-long.1551.pdf
- Local PDF: pdf/2026-10-05_17_PRISM_ Probing Reasoning, Instruction, and Source Memory in LLM Hallucinations.pdf

As large language models (LLMs) evolve from conversational assistants into agents capable of handling complex tasks, they are increasingly deployed in high-risk domains. However, existing benchmarks largely rely on mixed queries and posterior evaluation, output-level scoring, which quantifies hallucination severity but offers limited insight into where and why hallucinations arise in the generation pipeline. We therefore reformulate hallucination evaluation as a diagnostic problem and propose PRISM, a controlled benchmark that disentangles hallucinations into four dimensions: knowledge missing, knowledge errors, reasoning errors, and instruction-following errors, grounded in three stages of generation (memory, instruction, and reasoning). PRISM contains 9,448 instances across 65 tasks and supports fine-grained, stage-aware diagnostic evaluation. Evaluating 24 mainstream open-source and proprietary LLMs, we uncover consistent trade-offs across instruction following, memory retrieval, and logical reasoning, showing that mitigation strategies often improve specific dimensions at the expense of others.We hope PRISM provides a framework for understanding the specific mechanisms behind LLMs hallucinations, ultimately accelerating the development of trustworthy large language models.

## 18. VideoPro: Adaptive Program Reasoning for Long Video Understanding

- Authors: Chenglin Li, Feng Han, Yikun Wang, Ruilin Li, Shuai Dong, Haowen Hou, Haitao Li, Qianglong Chen, Feng Tao, Jingqi Tong, Yin Zhang, Jiaqi Wang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.650313572468472
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.341/
- PDF: https://aclanthology.org/2026.acl-long.341.pdf
- Local PDF: pdf/2026-10-05_18_VideoPro_ Adaptive Program Reasoning for Long Video Understanding.pdf

Understanding long videos remains challenging due to the sparsity of visual evidence relevant to a given query. Prior work has explored program-based visual grounding, typically relying on executable programs generated by auxiliary large language models. However, when scaling to long videos, existing approaches face several critical limitations: (1) frame-centric vision modules are often insufficient for long video processing; (2) naively applying program-based reasoning to all queries incurs considerable computational overhead; and (3) errors arising from low-confidence predictions and imperfect program execution are difficult to recover from. To address these challenges, we propose VideoPro, a unified framework that enables VideoLLMs to adaptively reason over long videos and refine their predictions through executable programs. VideoPro first performs adaptive reasoning, dynamically determining whether a query can be resolved directly by the native VideoLLM or requires explicit multi-step program reasoning. For complex queries, the model decomposes the task into executable programs that invoke specialized vision modules for precise temporal and semantic grounding. To further improve robustness, VideoPro incorporates a self-refinement mechanism that leverages execution feedback and confidence signals to correct erroneous executions and refine low-confidence reasoning programs. By tightly integrating adaptive reasoning with self-refinement, VideoPro consistently outperforms prior methods across multiple long-video understanding benchmarks, yielding an average 6.7% improvement for Qwen3-VL-8B.

## 19. Thesis Proposal: Intentional Inference for Insight Generation

- Authors: Kristýna Onderková
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.649730258803645
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-srw.109/
- PDF: https://aclanthology.org/2026.acl-srw.109.pdf
- Local PDF: pdf/2026-10-05_19_Thesis Proposal_ Intentional Inference for Insight Generation.pdf

Large language models show strong capabilities in natural language generation (NLG) and have been applied to translate complex structured data into human-readable insights. While these models excel at surface-level fluency, they remain unreliable as they produce factually inaccurate outputs and struggle with consistent logical inference beyond surface-level patterns. Moreover, they often lack a clear sense of relevance and produce shallow or uninformative insights.This proposal argues that a key source of these limitations is task underspecification, which requires models to make implicit assumptions about missing context.We investigate how such underspecification leads to unintentional assumptions and how these affect faithfulness and evaluation.We examine how models can identify missing premises and surface multiple plausible interpretations to make evaluation more rigorous. We also explore how to improve reasoning to enable deeper inferences, focusing on code generation and qualitative reasoning. Finally, we will evaluate how the underlying assumptions and depth of inference influence the perceived interestingness of the insights. By shifting focus from surface-level generation to assumption-aware deeper inferences, this work aims to improve reliability, interpretability, and user controlability in NLG.

## 20. Discovery and Reinforcement of Tool-Integrated Reasoning Chains via Rollout Trees

- Authors: Kun Li, Zenan Xu, Junan Li, Zengrui Jin, Jinghao Deng, Zexuan Qiu, Bo Zhou
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.6495431302879338
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.649/
- PDF: https://aclanthology.org/2026.acl-long.649.pdf
- Local PDF: pdf/2026-10-05_20_Discovery and Reinforcement of Tool-Integrated Reasoning Chains via Rollout Trees.pdf

Tool-Integrated Reasoning has emerged as a key paradigm to augment Large Language Models (LLMs) with computational capabilities, yet integrating tool-use into long Chain-of-Thought (long CoT) remains underexplored, largely due to the scarcity of training data and the challenge of integrating tool-use without compromising the model’s intrinsic long-chain reasoning. In this paper, we introduce DART (Discovery And Reinforcement of Tool-Integrated Reasoning Chains via Rollout Trees), a reinforcement learning framework that enables spontaneous tool-use during long CoT reasoning without additional human annotation. DART operates by constructing dynamic rollout trees during training to discover valid tool-use opportunities, branching out at promising positions to explore tool-integrated trajectories. Subsequently, a tree-based process advantage estimation identifies and credits specific sub-trajectories where tool invocation positively contributes to the solution, effectively reinforcing these beneficial behaviors during training. Extensive experiments on challenging benchmarks like AIME and GPQA-Diamond demonstrate that DART significantly outperforms existing methods, successfully harmonizing tool execution with long CoT reasoning.

## 21. Late Code Chunking: A Code Chunking Strategy for Repository-Level Code Completion

- Authors: Seungmin Oh, Eunseok Lee
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.6494939496792007
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-short.64/
- PDF: https://aclanthology.org/2026.acl-short.64.pdf
- Local PDF: pdf/2026-10-05_21_Late Code Chunking_ A Code Chunking Strategy for Repository-Level Code Completion.pdf

This paper introduces Late Code Chunking (LC 2 ), a chunking strategy designed to improve the semantic understanding of code segments for Large Language Models (LLMs). Repository-level code completion requires predicting the completion of unfinished code by leveraging cross-file context spread across a repository. However, when retrieved fragments have missing semantics—the loss of structural or behavioral information during chunking—LLMs struggle to interpret the target code. To address this, LC 2 refines retrieved chunks by constructing a dual context: a “Code Retrieval Context” optimized for similarity-based search, and a “Code Comprehension Context” that serves as a late enrichment step through context expansion and augmentation. This dual-context design reduces information loss due to chunking and enhances the ability of LLMs to utilize retrieved code. Additionally, we introduce an Asymmetric Query-Chunk Sizing strategy to further optimize retrieval quality by minimizing query noise. Our experiments demonstrate that LC 2 provides robust performance gains, achieving a statistically significant 19.7% improvement in Exact Match accuracy on the CrossCodeEval benchmark compared to the best existing chunking method.

## 22. All Changes May Have Invariant Principles: Improving Ever-Shifting Harmful Meme Detection via Design Concept Reproduction

- Authors: Ziyou Jiang, Mingyang Li, Junjie Wang, Yuekai Huang, Jie Huang, Zhiyuan Chang, Zhaoyang Li, Qing Wang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.649443178401723
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.800/
- PDF: https://aclanthology.org/2026.acl-long.800.pdf
- Local PDF: pdf/2026-10-05_22_All Changes May Have Invariant Principles_ Improving Ever-Shifting Harmful Meme Detection via Design Concept Reproductio.pdf

Harmful memes are ever-shifting in the Internet communities, which are difficult to analyze due to their type-shifting and temporal-evolving nature. Although these memes are shifting, we find that different memes may share invariant principles, i.e., the underlying design concept of malicious users, which can help us analyze why these memes are harmful. In this paper, we propose RepMD, an ever-shifting harmful meme detection method based on the design concept reproduction. We first refer to the attack tree to define the Design Concept Graph (DCG), which describes steps that people may take to design a harmful meme. Then, we derive the DCG from historical memes with design step reproduction and graph pruning. Finally, we use DCG to guide the Multimodal Large Language Model (MLLM) to detect harmful memes. The evaluation results show that RepMD achieves the highest accuracy with 81.1% and has slight accuracy decreases when generalized to type-shifting and temporal-evolving memes. Human evaluation shows that RepMD can improve the efficiency of human discovery on harmful memes, with 15 ∼ 30 seconds per meme.

## 23. From Implicit to Explicit: Token-Efficient Logical Supervision for Mathematical Reasoning in LLMs

- Authors: Shaojie Wang, Liang Zhang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.649266794062097
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1420/
- PDF: https://aclanthology.org/2026.findings-acl.1420.pdf
- Local PDF: pdf/2026-10-05_23_From Implicit to Explicit_ Token-Efficient Logical Supervision for Mathematical Reasoning in LLMs.pdf

Recent studies reveal that large language models (LLMs) exhibit limited logical reasoning abilities in mathematical problem-solving, instead often relying on pattern-matching and memorization. We systematically analyze this limitation, focusing on logical relationship understanding, which is a core capability underlying genuine logical reasoning, and reveal that errors related to this capability account for over 90% of incorrect predictions, with Chain-of-Thought Supervised Fine-Tuning (CoT-SFT) failing to substantially reduce these errors. To address this bottleneck, we propose F irst- S tep L ogical R easoning ( FSLR ), a lightweight training framework targeting logical relationship understanding. Our key insight is that the first planning step-identifying which variables to use and which operation to apply-encourages the model to derive logical relationships directly from the problem statement. By training models on this isolated step, FSLR provides explicit supervision for logical relationship understanding, unlike CoT-SFT which implicitly embeds such relationships within complete solution trajectories. Extensive experiments across multiple models and datasets demonstrate that FSLR consistently outperforms CoT-SFT under both in-distribution and out-of-distribution settings, with average improvements of 3.2% and 4.6%, respectively. Moreover, FSLR achieves 4-6× faster training and reduces training token consumption by over 80%.

## 24. Position: Multimodal Large Language Models Can Significantly Advance Scientific Reasoning

- Authors: Yibo Yan, Shen Wang, Jiahao Huo, Jingheng Ye, Zhendong Chu, Xuming Hu, Philip S. Yu, Carla P Gomes, Bart Selman, Qingsong Wen
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.648977889845191
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1228/
- PDF: https://aclanthology.org/2026.findings-acl.1228.pdf
- Local PDF: pdf/2026-10-05_24_Position_ Multimodal Large Language Models Can Significantly Advance Scientific Reasoning.pdf

Scientific reasoning, the process through which humans apply logic, evidence, and critical thinking to explore and interpret scientific phenomena, is essential in advancing knowledge reasoning across diverse fields. However, despite significant progress, current scientific reasoning models still struggle with generalization across domains and often fall short of multimodal perception. Multimodal Large Language Models (MLLMs), which integrate text, images, and other modalities, present an exciting opportunity to overcome these limitations and enhance scientific reasoning. Therefore, this position paper argues that MLLMs can significantly advance scientific reasoning across disciplines such as mathematics, physics, chemistry, and biology . We highlight the current state of MLLM applications in scientific reasoning, noting their ability to integrate and reason over diverse data types. However, challenges such as multimodal alignment, data diversity, and reasoning depth remain obstacles to achieving their full potential. To address these challenges, we propose actionable suggestions in the near future. Overall, our work offers a novel perspective on MLLM integration with scientific reasoning, providing the LLM community with valuable insights for achieving Artificial General Intelligence (AGI).

## 25. CURE: Critique-Driven Unified Reinforcement Learning for Test-Time Self-Improvement

- Authors: Guirong Chen, Shuqi Ye, Wenkai Yang, Shiqi Shen, Guangyao Shen, Yankai Lin
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.6488875086707644
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1321/
- PDF: https://aclanthology.org/2026.acl-long.1321.pdf
- Local PDF: pdf/2026-10-05_25_CURE_ Critique-Driven Unified Reinforcement Learning for Test-Time Self-Improvement.pdf

The evolution paradigm of Large Language Models (LLMs) is shifting from scaling training compute to scaling inference-time compute. While Reinforcement Learning with Verifiable Rewards (RLVR) has become a key engine for this transition, standard approaches often fail to equip models with the autonomous improvement capabilities required for test-time scaling. Existing critique-guided methods attempt to mitigate this by leveraging external feedback or ground-truth signals; however, these dependencies are unavailable at test time, fundamentally limiting the model’s capacity for continuous self-improvement. To bridge this gap, we propose CURE (Critique-driven Unified REinforcement Learning), a framework that jointly optimizes a single policy for standard solving, critiquing, and guided re-exploration. Uniquely, CURE facilitates re-exploration by generating strategic hints while discarding initial incorrect solutions to mitigate anchoring bias.Empirical results across diverse mathematical reasoning and code generation benchmarks demonstrate that CURE not only maintains competitive single-turn performance but, more importantly, unlocks effective inference-time scaling, enabling the model to significantly boost accuracy through iterative self-improvement.

## 26. ReEfBench: Quantifying the Reasoning Efficiency of LLMs

- Authors: Zhizhang Fu, Yuancheng Gu, Chenkai Hu, Hanmeng Liu, Yue Zhang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.6484973106563725
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.931/
- PDF: https://aclanthology.org/2026.acl-long.931.pdf
- Local PDF: pdf/2026-10-05_26_ReEfBench_ Quantifying the Reasoning Efficiency of LLMs.pdf

Test-time scaling has enabled Large Language Models (LLMs) to tackle complex reasoning, yet the limitations of current Chain-of-Thought (CoT) evaluation obscure whether performance gains stem from genuine reasoning or mere verbosity. To address this, (1) we propose a novel neuro-symbolic framework for the non-intrusive, comprehensive process-centric evaluation of reasoning grounded in First-Order Logic. (2) Through this lens, we identify four distinct behavioral prototypes and diagnose the failure modes. (3) We examine the impact of inference mode, training strategy, and model scale. Our analysis reveals that extended token generation is not a prerequisite for deep reasoning. Furthermore, we reveal critical constraints: mixing long and short CoT data in training risks premature saturation and collapse, while distillation into smaller models captures behavioral length but fails to replicate logical efficacy due to intrinsic capacity limits.

## 27. Lost in Translation, and Found: Detecting and Interpreting Translation Effects

- Authors: Shira Wein, Anna Serbina, Jiyuan Ji, Nathan Wolf, Jason DeGraaff, Prajakta Kini, Maria Leonor Pacheco
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.648341970701822
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.781/
- PDF: https://aclanthology.org/2026.acl-long.781.pdf
- Local PDF: pdf/2026-10-05_27_Lost in Translation, and Found_ Detecting and Interpreting Translation Effects.pdf

Translationese refers to the statistical patterns that distinguish translated texts from original texts, which are often subtle and imperceptible to human readers. When translated texts appear in either training or testing data, these patterns can negatively affect model performance or warp model evaluation. We approach the task of discerning whether a text was originally written in English or translated into English by fine-tuning contemporary foundation models at distinct item lengths and achieve state-of-the-art performance (94% Macro F1). Given that these linguistic cues are subtle and often imperceptible to humans, we analyze the features which enable our model’s high performance. Employing a suite of interpretability-based techniques, we find that: (1) our high accuracy is enabled by a collection of linguistic features, a number of which correspond with linguistic theories of translationese, and (2) pretrained neural models are adept at picking up these features without any fine-tuning.

## 28. B-APO: Bias-Targeted Adversarial Preference Optimization for Debiasing Multimodal Large Language Models

- Authors: Pinlong Zhao, Zike Ding, Zengshu Ye, Zhou Zhaoting
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.6480608335478606
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1843/
- PDF: https://aclanthology.org/2026.findings-acl.1843.pdf
- Local PDF: pdf/2026-10-05_28_B-APO_ Bias-Targeted Adversarial Preference Optimization for Debiasing Multimodal Large Language Models.pdf

Multimodal Large Language Models (MLLMs) often suffer from modality bias, where the model disproportionately relies on one modality while neglecting critical information from others. Existing debiasing methods via modality masking create biased responses by completely removing an entire modality, forming an extreme and static training environment. However, real-world multimodal bias often emerges under subtle perturbations (e.g., mild occlusion, noisy instructions), where both modalities are present but the model is tempted to rely on spurious shortcuts. We propose B-APO (Bias-Targeted Adversarial Preference Optimization), which casts debiasing as a bias-targeted min-max game: we generate hard negatives by applying small adversarial perturbations in the latent space to maximally induce language-vision-prior reliance, and then perform preference alignment to enlarge the margin between clean and adversarial responses. This encourages the model to anchor on true cross-modal evidence even under the most adversarial conditions. Extensive experiments on bias and hallucination benchmarks demonstrate that B-APO achieves superior debiasing performance while maintaining general capabilities.

## 29. ACR: Adaptive Context Refactoring via Context Refactoring Operators for Multi-Turn Dialogue

- Authors: Jiawei Shen, Jia Zhu, Hanghui Guo, Weijie Shi, Yue Cui, Qingyu Niu, Guoqing Ma, Jingjiang Liu, Yidan Liang, Yilin Wang, Shimin Di, Jiajie Xu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.647850147720395
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.155/
- PDF: https://aclanthology.org/2026.findings-acl.155.pdf
- Local PDF: pdf/2026-10-05_29_ACR_ Adaptive Context Refactoring via Context Refactoring Operators for Multi-Turn Dialogue.pdf

Large Language Models (LLMs) have shown remarkable performance in multi-turn dialogue. However, in multi-turn dialogue, models still struggle to stay aligned with what has been established earlier, follow dependencies across many turns, and avoid drifting into incorrect facts as the interaction grows longer. Existing approaches primarily focus on extending the context window, introducing external memory, or applying context compression, yet these methods still face limitations such as contextual inertia and state drift. To address these challenges, we propose the Adaptive Context Refactoring (ACR) Framework, which dynamically monitors and reshapes the interaction history to mitigate contextual inertia and state drift actively. ACR is built on a library of context refactoring operators and a teacher-guided self-evolving training paradigm that learns when to intervene and how to refactor, thereby decoupling context management from the reasoning process. Extensive experiments on multi-turn dialogue demonstrate that our method significantly outperforms existing baselines while reducing token consumption. Our code is available at https://github.com/ClannadKno/multi-turn .

## 30. PDTrim: Targeted Pruning for Prefill-Decode Disaggregation in Inference

- Authors: Hao Zhang, Lyu Mengsi, Zhuo Chen, Yulong Ao, Yonghua Lin
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.6476918060032673
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1842/
- PDF: https://aclanthology.org/2026.acl-long.1842.pdf
- Local PDF: pdf/2026-10-05_30_PDTrim_ Targeted Pruning for Prefill-Decode Disaggregation in Inference.pdf

Large Language Models (LLMs) demonstrate exceptional capabilities across various tasks, but their deployment is constrained by high computational and memory costs. Model pruning provides an effective means to alleviate these demands. However, existing methods often ignore the characteristics of prefill-decode (PD) disaggregation in practice. In this paper, we propose a pruning method that is highly integrated with PD disaggregation, enabling more precise pruning of blocks. Our approach constructs pruning and distillation sets to perform iterative block removal, obtaining better pruning solutions. Moreover, we analyze the pruning sensitivity of the prefill and decode stages and identify removable blocks specific to each stage, making it well suited for PD disaggregation deployment. Extensive experiments demonstrate our approach consistently achieves strong performance in both PD disaggregation and PD unified (non-PD disaggregation) settings, and can also be extended to other non-block pruning methods. Under the same settings, our method achieves improved performance and faster inference.
