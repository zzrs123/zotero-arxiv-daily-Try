# Paper Daily Reading - 2026-07-13

## 1. Reinforcement Learning Enhanced Muti-hop Reasoning for Temporal Knowledge Question Answering

- Authors: Weiheng Wen, Chao Xue, Su Pan, Yuwei Sun, Minlong Peng
- Source: openalex
- Venue type: conference
- Journal: Proceedings of the AAAI Conference on Artificial Intelligence
- Publication status: formally_published
- Publication date: 2026-03-14
- DOI: https://doi.org/10.1609/aaai.v40i40.40680
- Categories: Advanced Graph Neural Networks, Topic Modeling, Multimodal Machine Learning Applications
- Relevance: 3.1330638916724105
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://doi.org/10.1609/aaai.v40i40.40680
- PDF: https://ojs.aaai.org/index.php/AAAI/article/download/40680/44641
- Local PDF: Not downloaded

Temporal knowledge graph question answering (TKGQA) involves multi-hop reasoning over temporally constrained entity relationships in the knowledge graph to answer a given question. However, at each hop, large language models (LLMs) retrieve subgraphs with numerous temporally similar and semantically complex relations, increasing the risk of suboptimal decisions and error propagation. To address these challenges, we propose the multi-hop reasoning enhanced (MRE) framework, which enhances both forward and backward reasoning to improve the identification of globally optimal reasoning trajectories. Specifically, MRE begins with prompt engineering to guide LLM in generating diverse reasoning trajectories for the given question. Valid reasoning trajectories are then selected for supervised fine-tuning, serving as a cold-start strategy. Finally, we introduce Tree-Group Relative Policy Optimization (T-GRPO)—a recursive, tree-structured learning-by-exploration approach. At each hop, exploration establishes strong causal dependencies on the previous hop, while evaluation is informed by multi-path exploration feedback from subsequent hops. Experimental results on two TKGQA benchmarks indicate that the proposed MRE-based model consistently surpasses state-of-the-art (SOTA) approaches in handling complex multi-hop queries. Further analysis highlights improved interpretability and robustness to noisy temporal annotations.

## 2. Exploring Layer Activation Dynamic of CoT via Knowledge Probe

- Authors: Chuanxin Zhang, Jiajun Liu, Yao He, Wenjun Ke, Peng Wang, Yankun Le, Sirui Liu, Zhaoyu Yang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.9267893057432346
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.542/
- PDF: https://aclanthology.org/2026.acl-long.542.pdf
- Local PDF: pdf/2026-07-13_02_Exploring Layer Activation Dynamic of CoT via Knowledge Probe.pdf

Chain-of-thought (CoT) reasoning has emerged as a crucial paradigm for enhancing large language model (LLM) performance on multi-step reasoning tasks.However, the internal mechanisms by which LLMs invoke knowledge and propagate information across different steps of the CoT are poorly understood.To fill this gap, we propose a multi-stage probing framework that enforces structured reasoning with three explicit stages: keyword extraction, theorem generation, and computation execution.The framework integrates attention knockout to trace cross-layer information flow and theorem probing to examine how specific contents are encoded within representations.To enable controlled and stage-aligned analysis, we construct a structured CoT dataset that covers the mathematics and physics domains. Experiments on four instruction-tuned LLMs reveal distinct stage-specific patterns.First, keyword information is progressively aggregated into the final token in later layers.Second, theorem semantics are encoded in the mid-to-late layers and undergo two stages of propagation.Finally, parameter substitution is achieved through joint extraction by the final token and other tokens.The first parameter predominantly relies on the final token, whereas later parameters increasingly depend on information extracted by other tokens.Overall, our findings shed light on the neural implementation of CoT reasoning and provide actionable insights for developing more interpretable and reasoning-capable LLMs.We further evaluate a free-form prompting setting without labeled fields and observe consistent qualitative trends.

## 3. A Data-Efficient Path to Multilingual LLMs: Language Expansion via Post-training PARAM 𝛥 Integration into Upcycled MoE

- Authors: Hao Zhou, Tianhao Li, Zhijun Wang, Shuaijie She, Linjuan Wu, Hao-Ran Wei, Baosong Yang, Jiajun Chen, Shujian Huang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.9263448056048746
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1238/
- PDF: https://aclanthology.org/2026.acl-long.1238.pdf
- Local PDF: pdf/2026-07-13_03_A Data-Efficient Path to Multilingual LLMs_ Language Expansion via Post-training PARAM 𝛥 Integration into Upcycled MoE.pdf

Expanding Large Language Models(LLMs) to new languages is a costly endeavor, demanding extensive Continued Pre-Training(CPT) and data-intensive alignment. While recent data-free merging techniques attempt to bypass alignment by fusing a multilingual CPT-enhanced model with its instruct counterpart, they are plagued by a critical trade-off: mitigating parameter conflicts to preserve original abilities inevitably dilutes new language acquisition, and vice-versa. To resolve this conflict, we introduce , which upcycles a dense model into a Mixture-of-Experts(MoE) architecture, allocating different experts to different languages. Alignment ability is then transferred by grafting a MoE-expanded parameter delta( 𝛥 instruct ) to the CPT-enhanced base model, bypassing the complex alignment phase. Experiments demonstrate ’s superiority even against baselines with similar FLOPs or number of parameters; it improves performance on expanded languages while effectively preserving original capabilities. We further show our approach is highly applicable across different models and Post-training deltas.

## 4. HCSpec: Two-Tier Horizontal Cascade Speculative Decoding for High-Efficiency Large Language Model Inference

- Authors: Yizhou Zhang, Siming Chen, Hao Ye, Erhu Feng
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.9256414997544478
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.353/
- PDF: https://aclanthology.org/2026.acl-long.353.pdf
- Local PDF: pdf/2026-07-13_04_HCSpec_ Two-Tier Horizontal Cascade Speculative Decoding for High-Efficiency Large Language Model Inference.pdf

Speculative decoding accelerates large language model (LLM) inference by using a draft model to propose token candidates for parallel verification by the target model. However, current state-of-the-art self-distilled draft models adopt a homogeneous architecture across all drafting positions, failing to account for a critical empirical observation: the expected utility of drafting decays rapidly after the initial positions. To exploit this imbalance, we propose Two-tier Horizontal Cascade Speculative Decoding (HCSpec), a novel framework that organizes heterogeneous, position-specialized draft modules into a horizontal cascade. The first tier employs a dual-layer, dual-path transformer that enhances early-step fidelity by decoupling token-logit prediction from recurrent feature propagation, while the second tier adopts a lightweight single-layer transformer that deliberately trades marginal accuracy for improved efficiency at later drafting steps. Extensive experiments on Qwen series models and Llama3.1-8B-Instruct, across multiple tasks and diverse inference configurations, demonstrate that HCSpec consistently outperforms the previous state-of-the-art (EAGLE-3). It delivers 15–30% higher end-to-end speedup over EAGLE-3 and achieves up to 3.72x acceleration over vanilla autoregressive decoding. Our code is provided in the supplementary materials.

## 5. GrAInS: Gradient-based Attribution for Inference-Time Steering of LLMs and VLMs

- Authors: Duy Nguyen, Archiki Prasad, Elias Stengel-Eskin, Mohit Bansal
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.9251436362072103
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.2159/
- PDF: https://aclanthology.org/2026.acl-long.2159.pdf
- Local PDF: pdf/2026-07-13_05_GrAInS_ Gradient-based Attribution for Inference-Time Steering of LLMs and VLMs.pdf

Inference-time steering provides a lightweight alternative to fine-tuning large language models (LLMs) and vision-language models (VLMs) by modifying model activations without updating weights. However, existing methods often rely on a global intervention vector, overlook token-level causal influence, and underutilize model logits, especially in multimodal settings where visual and textual inputs contribute unevenly. We propose GrAInS, a contrastive, gradient-based approach that leverages Integrated Gradients to identify top-k influential tokens and construct directional steering vectors based on their contribution to preferred over dispreferred outputs. These vectors guide activation intervention at each layer, preserving the representational scale. GrAInS outperforms fine-tuning and prior steering methods on both LLM and VLM tasks: improving TruthfulQA accuracy by 13.22% (Llama-3.1-8B), reducing MMHal-Bench hallucinations from 0.624 to 0.514 (LLaVA-1.6-7B), and increasing SPA-VL alignment by 8.11%, all without degrading fluency or general capabilities.

## 6. Revealing the Attention Floating Mechanism in Masked Diffusion Models

- Authors: Xin Dai, Pengcheng Huang, Zhenghao Liu, Shuo Wang, Yukun Yan, Chaojun Xiao, Yu Gu, Ge Yu, Maosong Sun
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.9249185300180214
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.404/
- PDF: https://aclanthology.org/2026.findings-acl.404.pdf
- Local PDF: pdf/2026-07-13_06_Revealing the Attention Floating Mechanism in Masked Diffusion Models.pdf

Masked diffusion models (MDMs), which leverage bidirectional attention and a denoising process, are narrowing the performance gap with autoregressive models (ARMs). However, their internal attention mechanisms remain under-explored. This paper investigates the attention behaviors in MDMs, revealing the phenomenon of Attention Floating. Unlike ARMs, where attention converges to a fixed sink, MDMs exhibit dynamic, dispersed attention anchors that shift across denoising steps and layers. Further analysis reveals its Shallow Structure-Aware, Deep Content-Focused attention mechanism: shallow layers utilize floating tokens to build a global structural framework, while deeper layers allocate more capability toward capturing semantic content. Empirically, this distinctive attention pattern provides a mechanistic explanation for the strong in-context learning capabilities of MDMs, allowing them to double the performance compared to ARMs in knowledge-intensive tasks. All codes and datasets are available at https://github.com/NEUIR/Attention-Floating .

## 7. Grammar as Control: Modular Language Generation for the Long Tail

- Authors: Ndapa Nakashole
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.9237068412846656
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1725/
- PDF: https://aclanthology.org/2026.acl-long.1725.pdf
- Local PDF: pdf/2026-07-13_07_Grammar as Control_ Modular Language Generation for the Long Tail.pdf

Large language models (LLMs) can, in principle, bootstrap language technologies for long-tail languages due to their pattern recognition capabilities. Yet in practice, without structured guidance, they produce narrow, unrepresentative samples that fail to cover the morphosyntactic space of typologically underrepresented languages.We propose Modular Typology-Informed Generation (mTIG), a prompting framework that transforms descriptive grammars into explicit control mechanisms that guide LLMs to generate typologically balanced synthetic data for downstream training. mTIG decomposes grammars into modular grammar slices, each targeting a specific morphosyntactic phenomenon (e.g., passive voice, causative morphology).Across three low-resource languages, mTIG improves typological entropy by up to 19% and yields a "student-beats-teacher" effect, where distilled models outperform the source LLM by up to +20 chrF in machine translation. These findings show that grammar-as-control can construct training corpora wherever formal linguistic descriptions exist.

## 8. CrisPrune: Combining Contextual Relevance and Intrinsic Saliency for Efficient Visual Token Pruning in MLLMs

- Authors: Ziniu Liu, Shuheng Zhou, Mingqing Liu, Hao Deng, Huijia Zhu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.9231648280163993
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.663/
- PDF: https://aclanthology.org/2026.findings-acl.663.pdf
- Local PDF: pdf/2026-07-13_08_CrisPrune_ Combining Contextual Relevance and Intrinsic Saliency for Efficient Visual Token Pruning in MLLMs.pdf

Visual token pruning has emerged as a pivotal strategy to alleviate the computational bottleneck in Multimodal Large Language Models (MLLMs), yet it frequently compromises the integrity of visual understanding in pursuit of efficiency. Existing methods face a fundamental tension: vision-centric approaches are susceptible to the attention sink phenomenon and operate in a query-agnostic manner, whereas text-guided methods often create an overly narrow focus, discarding essential background context and failing on ambiguous queries. In this paper, we propose CrisPrune, a training-free and model-agnostic method that reconciles efficiency with understanding by integrating visual saliency and text relevance. Specifically, we introduce intrinsic visual saliency with robust normalization to identify information-rich regions characterized by significant visual features. Simultaneously, we design dual-source text relevance to synergize explicit instruction alignment with implicit scene priors. Finally, we reformulate the selection process using a Determinantal Point Process (DPP) to balance token quality and spatial diversity. Extensive experiments demonstrate that CrisPrune significantly outperforms state-of-the-art methods. On LLaVA-NeXT, it achieves a 13 × decrease in FLOPs while maintaining 97% of the original performance with 94.4% of visual tokens pruned, effectively bridging the gap between efficiency and holistic understanding.

## 9. Spotlight and Shadow: Attention-Guided Dual-Anchor Introspective Decoding for MLLM Hallucination Mitigation

- Authors: Yebo Wu, Han Jin, Zhijiang Guo, Li Li
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.9226689859685244
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.646/
- PDF: https://aclanthology.org/2026.findings-acl.646.pdf
- Local PDF: pdf/2026-07-13_09_Spotlight and Shadow_ Attention-Guided Dual-Anchor Introspective Decoding for MLLM Hallucination Mitigation.pdf

Multimodal Large Language Models (MLLMs) have demonstrated remarkable reasoning capabilities yet continue to suffer from hallucination, where generated text contradicts visual content. In this paper, we introduce Dual-Anchor Introspective Decoding (DaID), a novel contrastive decoding framework that dynamically calibrates each token generation by mining the model’s internal perceptual discrepancies. Specifically, DaID identifies a Spotlight layer to amplify visual factual signals and a Shadow layer to suppress textual inertia. By leveraging visual attention distributions to guide this dual-anchor selection process, our method ensures precise, token-specific adaptation. Experimental results across multiple benchmarks and MLLMs demonstrate that DaID significantly mitigates hallucination while enhancing general reasoning capabilities.

## 10. ToMMeR - Efficient Entity Mention Detection from Large Language Models

- Authors: Victor Morand, Nadi Tomeh, Josiane Mothe, Benjamin Piwowarski
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.9214257262139602
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1268/
- PDF: https://aclanthology.org/2026.acl-long.1268.pdf
- Local PDF: pdf/2026-07-13_10_ToMMeR - Efficient Entity Mention Detection from Large Language Models.pdf

Identifying which text spans refer to entities - mention detection- is both foundational for information extraction and a known performance bottleneck. We introduce ToMMeR, a lightweight model (<300K parameters) probing mention detection capabilities from early LLM layers. Across 13 NER benchmarks, ToMMeR achieves 93% recall zero-shot, with an estimated 90% precision under a human-calibrated LLM-judge protocol, showing that ToMMeR rarely produces spurious predictions despite high recall. Cross-model analysis reveals that diverse architectures (14M-15B parameters) converge on similar mention boundaries (DICE >75%), confirming that mention detection emerges naturally from language modeling. When extended with span classification heads, ToMMeR achieves competitive NER performance (80-87% F1 on standard benchmarks). Our work provides evidence that structured entity representations exist in early transformer layers and can be efficiently recovered with minimal parameters.

## 11. Illusions of Confidence? Diagnosing LLM Truthfulness via Neighborhood Consistency

- Authors: Haoming Xu, Ningyuan Zhao, Yunzhi Yao, Weihong Xu, Hongru Wang, Xinle Deng, Shumin Deng, Jeff Z. Pan, Huajun Chen, Ningyu Zhang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.92118635804488
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.203/
- PDF: https://aclanthology.org/2026.acl-long.203.pdf
- Local PDF: pdf/2026-07-13_11_Illusions of Confidence_ Diagnosing LLM Truthfulness via Neighborhood Consistency.pdf

As Large Language Models (LLMs) are increasingly deployed in real-world settings, correctness alone is insufficient. Reliable deployment requires maintaining truthful beliefs under contextual perturbations. Existing evaluations largely rely on point-wise confidence like Self-Consistency, which can mask brittle belief. We show that even facts answered with perfect self-consistency can rapidly collapse under mild contextual interference. To address this gap, we propose Neighbor-Consistency Belief (NCB) , a structural measure of belief robustness that evaluates response coherence across a conceptual neighborhood. To validate the efficiency of NCB, we introduce a new cognitive stress-testing protocol that probes outputs stability under contextual interference. Experiments across multiple LLMs show that the performance of high-NCB data is relatively more resistant to interference. Finally, we present Structure-Aware Training (SAT) , which optimizes context-invariant belief structure and reduces long-tail knowledge brittleness by approximately 30% .

## 12. Decoupled Reasoning with Implicit Fact Tokens (DRIFT): A Dual-Model Framework for Efficient Long-Context Inference

- Authors: Wenxuan Xie, Xuhong Wang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.9209921308479085
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1897/
- PDF: https://aclanthology.org/2026.findings-acl.1897.pdf
- Local PDF: pdf/2026-07-13_12_Decoupled Reasoning with Implicit Fact Tokens (DRIFT)_ A Dual-Model Framework for Efficient Long-Context Inference.pdf

The integration of extensive, dynamic knowledge into Large Language Models (LLMs) remains a significant challenge due to the inherent entanglement of factual data and reasoning patterns. Existing solutions, ranging from non-parametric Retrieval-Augmented Generation (RAG) to parametric knowledge editing, are often constrained in practice by finite context windows, retriever noise, or the risk of catastrophic forgetting. In this paper, we propose DRIFT , a novel dual-model architecture designed to explicitly decouple knowledge extraction from the reasoning process. Unlike static prompt compression, DRIFT employs a lightweight knowledge model to dynamically compress document chunks into implicit fact tokens conditioned on the query. These dense representations are projected into the reasoning model’s embedding space, replacing raw, redundant text while maintaining inference accuracy. Extensive experiments show that DRIFT significantly improves performance on long-context tasks , outperforming strong baselines among comparably sized models. Our approach provides a scalable and efficient paradigm for extending the effective context window and reasoning capabilities of LLMs. Our code and data will be made public upon publication.

## 13. Two-Stage Regularization-Based Structured Pruning for LLMs

- Authors: Mingkuan Feng, Jinyang Wu, Siyuan Liu, Shuai Zhang, Hongjian Fang, Ruihan Jin, Feihu Che, Pengpeng Shao, Zhengqi Wen, Jianhua Tao
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.9207634035849384
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.136/
- PDF: https://aclanthology.org/2026.acl-long.136.pdf
- Local PDF: pdf/2026-07-13_13_Two-Stage Regularization-Based Structured Pruning for LLMs.pdf

The deployment of large language models (LLMs) is largely hindered by their large number of parameters. Structural pruning has emerged as a promising solution. Prior structured pruning methods directly remove unimportant parameters based on certain metrics, which often causes knowledge loss and necessitates extensive retraining. To overcome this, we introduce a novel pruning method **TRSP**: **T**wo-Stage **R**egularization-Based **S**tructured **P**runing for LLMs. Specifically, we multiply the output of each transformer layer by an initial learnable weight and iteratively learn these weights by adding their ℓ 1 -norm as a regularization term to the loss function, serving as the first-stage regularization. Subsequently, we apply additional regularization to the difference between the output and input of layers with smaller weights, encouraging the shift of knowledge to the preserved layers. This serves as the second-stage regularization. TRSP retains more knowledge and better preserves model performance than direct parameter elimination. Through extensive experimentation we show that TRSP outperforms strong layer-wise structured pruning methods without requiring retraining. As a layer-wise pruning method, it delivers notable end-to-end acceleration, making it a promising solution for efficient LLM deployment.

## 14. TA-GRPO-d: Trajectory-Aware GRPO for Optimizing Denoising Trajectories in Diffusion LLMs

- Authors: Gyunyeop Kim, Sangwoo Kang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.9204641881642504
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1723/
- PDF: https://aclanthology.org/2026.acl-long.1723.pdf
- Local PDF: pdf/2026-07-13_14_TA-GRPO-d_ Trajectory-Aware GRPO for Optimizing Denoising Trajectories in Diffusion LLMs.pdf

Diffusion large language models (dLLMs) generate text by repeatedly unmasking a partially noised sequence in parallel, promising lower latency than autoregressive decoding. However, most discrete dLLMs still rely on fixed denoising schedules, which are non-adaptive to input difficulty and cannot learn efficient unmasking orders. This paper introduces a reinforcement learning (RL) framework that transforms dLLM decoding into a trajectory-aware, learnable policy. We propose a confidence-gated denoising strategy that dynamically decides which tokens to unmask and how many to unmask per step, enabling adaptive exploration of denoising trajectories. Building on Group Relative Policy Optimization, we reformulate it into a trajectory-aware variant, TA-GRPO- d , which combines a trajectory-level signal—captured as the z-score of the AUC over intermediate rewards—with a token-level unmasking-time weight. This design allows the model to learn not only the final output quality but also the efficiency of the decoding path itself. Experiments on MATH-500, Countdown, Sudoku, and code benchmarks (HumanEval, MBPP) show that TA-GRPO- d maintains or improves accuracy while reducing average denoising steps by up to half, achieving both faster inference and lower computational cost. Our approach provides an RL framework for optimizing dLLM decoding policies toward adaptive, efficient reasoning. Code is available at our GitHub.

## 15. RACER: Retrieval-Augmented Contextual Rapid Speculative Decoding

- Authors: Zihong Zhang, Zuchao Li, Lefei Zhang, Ping Wang, Hai Zhao
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.9200913805371713
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.998/
- PDF: https://aclanthology.org/2026.findings-acl.998.pdf
- Local PDF: pdf/2026-07-13_15_RACER_ Retrieval-Augmented Contextual Rapid Speculative Decoding.pdf

Autoregressive decoding in Large Language Models (LLMs) generates one token per step, causing high inference latency. Speculative decoding (SD) mitigates this through a guess-and-verify strategy, but existing training-free variants face trade-offs: retrieval-based drafts break when no exact match exists, while logits-based drafts lack structural guidance. We propose RACER ( R etrieval- A ugmented C ont e xtual R apid Speculative Decoding), a lightweight and training-free method that integrates retrieved exact patterns with logit-driven future cues. This unification supplies both reliable anchors and flexible extrapolation, yielding richer speculative drafts. Experiments on Spec-Bench, HumanEval, and MGSM-ZH demonstrate that RACER consistently accelerates inference, achieving more than 2× speedup over autoregressive decoding, and outperforms prior training-free methods, offering a scalable, plug-and-play solution for efficient LLM decoding. Our source code is available at https://github.com/hkr04/RACER.

## 16. LLM Reasoning as Trajectories: Step-Specific Representation Geometry and Correctness Signals

- Authors: Lihao Sun, Hang Dong, Bo Qiao, Qingwei Lin, Dongmei Zhang, Saravan Rajmohan
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.919995957609167
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1237/
- PDF: https://aclanthology.org/2026.acl-long.1237.pdf
- Local PDF: pdf/2026-07-13_16_LLM Reasoning as Trajectories_ Step-Specific Representation Geometry and Correctness Signals.pdf

This work characterizes large language models’ chain-of-thought generation as a structured trajectory through representation space. We show that mathematical reasoning traverses functionally ordered, step-specific subspaces that become increasingly separable with layer depth. This structure already exists in base models, while reasoning training primarily accelerates convergence toward termination-related subspaces rather than introducing new representational organization. While early reasoning steps follow similar trajectories, correct and incorrect solutions diverge systematically at late stages. This late-stage divergence enables mid-reasoning prediction of final-answer correctness with ROC–AUC up to 0.87. Furthermore, we introduce trajectory-based steering, an inference-time intervention framework that enables reasoning correction and length control based on derived ideal trajectories. Together, these results establish reasoning trajectories as a geometric lens for interpreting, predicting, and controlling LLM reasoning behavior.

## 17. Every Token Counts: Generalizing 16M Ultra-Long Context in Large Language Models

- Authors: Xiang Hu, Zhanchao Zhou, Ruiqi Liang, Zehuan Li, Wei Wu, Jianguo Li
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.9194620654147303
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.464/
- PDF: https://aclanthology.org/2026.acl-long.464.pdf
- Local PDF: pdf/2026-07-13_17_Every Token Counts_ Generalizing 16M Ultra-Long Context in Large Language Models.pdf

This work explores efficient ultra-long context modeling. We posit that an effective solution requires three fundamental properties: sparsity, random-access flexibility, and length generalization. To achieve this, we leverage Hierarchical Sparse Attention (HSA), a novel attention mechanism that satisfies all three properties. We integrate HSA into the Transformer architecture to develop HSA-UltraLong, an 8B-parameter Mixture-of-Experts (MoE) model trained on over 8 trillion tokens. We rigorously evaluate the model across tasks with both in-domain and out-of-domain context lengths to validate its capabilities. Our model demonstrates comparable performance to full-attention baselines on in-domain sequence lengths. Crucially, it achieves over 90% accuracy on most in-context retrieval tasks with contexts up to 512 times the pre-training context length. This work reports our findings and remaining issues throughout the experiments, offering insights for future research in ultra-long context modeling.

## 18. Scaling Performance and Low-Resource Annotation with Many-Shot In-Context Learning for Named Entity Recognition

- Authors: Qi Zhang, Fangping Lan, Cornelia Caragea, Longin Jan Latecki, Eduard Dragut
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.919424896026542
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1431/
- PDF: https://aclanthology.org/2026.findings-acl.1431.pdf
- Local PDF: pdf/2026-07-13_18_Scaling Performance and Low-Resource Annotation with Many-Shot In-Context Learning for Named Entity Recognition.pdf

In-context learning (ICL) with large language models (LLMs) has emerged as a powerful alternative to fine-tuning for Named Entity Recognition (NER), achieving strong performance with minimal annotation and no additional training. However, prior work has shown that despite their adaptability, LLMs still lag behind fully supervised models such as fine-tuned BERT in structured tasks like NER. While existing studies on ICL for NER have mainly explored few-shot settings, the potential of scaling to hundreds of demonstrations has not been thoroughly investigated. To address this gap, we conduct a comprehensive investigation of many-shot ICL for NER and further explore its effectiveness in annotating and refining data for low-resource NER tasks. Specifically, we evaluate various LLMs across multiple domains using hundreds of ICL examples and then assess the feasibility of using many-shot ICL as a data annotation framework. Our experiments demonstrate that: (1) scaling to hundreds of in-context examples enables LLMs to match or even surpass the performance of fully supervised BERT models; and (2) using about one hundred human-labeled examples as demonstrations, many-shot in-context annotation can generate high-quality labeled data, leading to approximately 10% absolute F1 improvement over existing state-of-the-art approaches when used to fine-tune BERT on low-resource NER.

## 19. BOSCH: Black-Box Binary Optimization for Short-Context Attention-Head Selection in LLMs

- Authors: Abbas Ghaddar, Ivan Kobyzev, Boxing Chen, Yufei Cui
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.9184407142442947
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1877/
- PDF: https://aclanthology.org/2026.acl-long.1877.pdf
- Local PDF: pdf/2026-07-13_19_BOSCH_ Black-Box Binary Optimization for Short-Context Attention-Head Selection in LLMs.pdf

Post-training hybridization of large language models (LLMs) often replaces quadratic self-attention with sliding-window attention (SWA) to reduce KV cache usage and improve latency. Existing hybridization schemes are typically defined either at the layer level (e.g., interleaving) or at the head level via static rankings from local to global. Layer-level schemes ignore that local and global dependencies are routed through heads within the same layer, while static head-level rankings suffer from entanglement: a head’s local/global behavior can change after hybridization. We propose BOSCH, Black-box Binary Optimization for Short-context Head Selection, a training-free method that formulates the problem as a Large Neighborhood Search and decomposes it into three subproblems: (i) layer-importance detection via small-budget black-box probes, (ii) adaptive per-layer SWA-ratio assignment based on these sensitivities, and (iii) grouped head-level optimization within ratio buckets. Extensive experiments on 4 LLMs ranging from 1.7B to 30B parameters, across 4 SWA ratios, show that BOSCH consistently outperforms layer-level heuristics and 6 strong static head-level methods, with larger gains at higher SWA ratios. Under continual pretraining, BOSCH recover original long-context performance faster and to a higher level. Analysis of the selected heads reveals substantial turnover for BOSCH across different SWA ratios, underscoring the importance of performing head-level selection for each target ratio rather than relying on fixed locality rankings.

## 20. Chain-of-Memory: Lightweight Memory Construction with Dynamic Evolution for LLM Agents

- Authors: Xiucheng Xu, Bingbing Xu, Tian Xueyun, Zihe Huang, Rongxin Chen, Li Yunfan, Huawei Shen
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.9177244308349004
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.534/
- PDF: https://aclanthology.org/2026.acl-long.534.pdf
- Local PDF: pdf/2026-07-13_20_Chain-of-Memory_ Lightweight Memory Construction with Dynamic Evolution for LLM Agents.pdf

External memory systems are pivotal for enabling Large Language Model (LLM) agents to maintain persistent knowledge and perform long-horizon decision-making. Existing paradigms typically follow a two-stage process: computationally expensive memory construction (e.g., structuring data into graphs) followed by naive retrieval-augmented generation. However, our empirical analysis reveals two fundamental limitations: complex construction incurs high costs with marginal performance gains, and simple context concatenation fails to bridge the gap between retrieval recall and reasoning accuracy. To address above challenges, we propose **CoM (Chain-of-Memory)**, a novel framework that advocates for a paradigm shift toward lightweight construction paired with sophisticated utilization. CoM introduces a *Chain-of-Memory* mechanism that organizes retrieved fragments into coherent inference paths through dynamic evolution, utilizing adaptive truncation to prune irrelevant noise. Extensive experiments on the LongMemEval and LoCoMo benchmarks demonstrate that CoM outperforms strong baselines with accuracy gains of 7.5%–10.4%, while drastically reducing computational overhead to approximately 2.7% of token consumption and 6.0% of latency compared to complex memory architectures.

## 21. Hallucinations as Orthogonal Noise: Inference-Time Manifold Alignment via Dynamic Contextual Orthogonalization

- Authors: Mingkuan Zhao, Wentao Hu, Tianchen Huang, Yuheng Min, Suquan Chen, Yide Gao, Yanbo Zhai, Shuangyong Song, Xuelong Li
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.9176474674597963
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1822/
- PDF: https://aclanthology.org/2026.findings-acl.1822.pdf
- Local PDF: pdf/2026-07-13_21_Hallucinations as Orthogonal Noise_ Inference-Time Manifold Alignment via Dynamic Contextual Orthogonalization.pdf

Hallucination in Large Language Models (LLMs)—characterized by the generation of content inconsistent with contextual facts or logical constraints—remains a persistent challenge for reliable deployment. In this work, we address this issue through a geometric framework rooted in the linear representation hypothesis. We propose that hallucinations manifest as orthogonal noise relative to the semantic manifold of the residual stream. Specifically, we hypothesize that while attention heads ideally propagate information congruent with the context subspace, hallucinations arise when specific heads introduce components orthogonal to this subspace, disrupting the coherence of the latent representation. Based on this formulation, we introduce Dynamic Contextual Orthogonalization (DCO), an inference-time intervention method. DCO utilizes the input residual stream as a dynamic context anchor to perform orthogonal decomposition on attention head outputs. To distinguish between context-aligned semantic updates and divergent noise, DCO employs a layer-wise Z-score suppression mechanism that selectively attenuates outlier orthogonal components based on statistical distributions. Evaluations on Llama-3-8B and 70B across benchmarks such as XSum, NQ-Swap, and IFEval demonstrate that DCO achieves superior contextual faithfulness compared to state-of-the-art intervention baselines. Furthermore, DCO maintains high performance on knowledge-intensive tasks like TriviaQA and TruthfulQA, effectively mitigating the trade-off between hallucination suppression and parametric knowledge retention often observed in existing methods. Our findings validate the geometric interpretation of hallucinations and establish DCO as a computationally efficient approach for enforcing manifold alignment.Our code is available at https://anonymous.4open.science/r/DCO-4AB0

## 22. Co-Reinforcement Learning for Unified Multimodal Understanding and Generation

- Authors: Jiang, Jingjing, Si, Chongjie, Luo, Jun, Zhang, Hanwang, Ma, Chao
- Source: neurips
- Venue type: conference
- Journal: NeurIPS 2025
- Publication status: formally_published
- Publication date: 2026-04-23
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.9175312211839124
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://proceedings.neurips.cc/paper_files/paper/2025/hash/08f6f963e993ee81625adb5aaac9403c-Abstract-Conference.html
- PDF: https://proceedings.neurips.cc/paper_files/paper/2025/file/08f6f963e993ee81625adb5aaac9403c-Paper-Conference.pdf
- Local PDF: pdf/2026-07-13_22_Co-Reinforcement Learning for Unified Multimodal Understanding and Generation.pdf

This paper presents a pioneering exploration of reinforcement learning (RL) via group relative policy optimization for unified multimodal large language models (ULMs), aimed at simultaneously reinforcing generation and understanding capabilities. Through systematic pilot studies, we uncover the significant potential of ULMs to enable the synergistic co-evolution of dual capabilities within a shared policy optimization framework. Building on this insight, we introduce \textbf{CoRL}, a \textbf{Co}-\textbf{R}einforcement \textbf{L}earning framework comprising a unified RL stage for joint optimization and a refined RL stage for task-specific enhancement. With the proposed CoRL, our resulting model, \textbf{ULM-R1}, achieves average improvements of 7\% on three text-to-image generation datasets and 23\% on nine multimodal understanding benchmarks. These results demonstrate the effectiveness of CoRL and highlight the substantial benefits of reinforcement learning in facilitating cross-task synergy and optimization for ULMs. Code is available at \url{https://github.com/mm-vl/ULM-R1}.

## 23. MathFlow: Enhancing the Perceptual Flow of MLLMs for Visual Mathematical Problems

- Authors: Shuhang Chen, Hangjie Yuan, Yunqiu Xu, Pengwei Liu, Tao Feng, Jun Cen, Zeying Huang, Yi Yang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.91697685494945
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.43/
- PDF: https://aclanthology.org/2026.acl-long.43.pdf
- Local PDF: pdf/2026-07-13_23_MathFlow_ Enhancing the Perceptual Flow of MLLMs for Visual Mathematical Problems.pdf

Despite strong results on many tasks, multimodal large language models (MLLMs) still underperform on visual mathematical problem solving, especially in reliably perceiving and interpreting diagrams. Inspired by human problem-solving, we hypothesize that the ability to extract meaningful information from diagrams is pivotal, as it directly conditions subsequent inference.Hence, we introduce FlowVerse, a comprehensive benchmark that provides a fine-grained evaluation of MLLMs’ perception and reasoning capabilities. Our preliminary results on FlowVerse reveal that existing MLLMs exhibit substantial limitations when extracting essential information and reasoned properties from diagrams and performing complex reasoning based on these visual inputs. In response, we introduce MathFlow, a modular problem-solving pipeline that decouples perception and inference into distinct stages, thereby optimizing each independently. Given the perceptual limitations observed in current MLLMs, we trained MathFlow-P-7B as a dedicated perception model.Experimental results indicate that MathFlow-P-7B yields substantial performance gains when integrated with various closed-source and open-source inference models. This demonstrates the effectiveness of the MathFlow pipeline and its compatibility with diverse inference frameworks. Project page: https://github.com/MathFlow-zju/MathFlow.

## 24. SDAR: A Synergistic Diffusion-AutoRegression Paradigm for Scalable Sequence Generation

- Authors: Shuang Cheng, Yihan Bian, Dawei Liu, Yuhua Jiang, Yihao Liu, Linfeng Zhang, Qian Yao, Zhongbo Tian, Wenhai Wang, Qipeng Guo, Kai Chen, Biqing Qi, Bowen Zhou
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.9148917899668136
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1110/
- PDF: https://aclanthology.org/2026.findings-acl.1110.pdf
- Local PDF: pdf/2026-07-13_24_SDAR_ A Synergistic Diffusion-AutoRegression Paradigm for Scalable Sequence Generation.pdf

Autoregressive (AR) language modeling remains the dominant paradigm due to its dense supervision signal and highly optimized serving infrastructure, but its strictly causal, token-by-token decoding limits parallelism and non-causal modeling. While masked diffusion offers a promising path toward parallel generation, it faces two critical bottlenecks: training inefficiency stemming from sparse masked objectives, and high latency caused by iterative whole-sequence denoising. We present a systematic study of blockwise discrete diffusion, a pragmatic middle ground that preserves AR-compatible serving while enabling parallel intra-block generation. Our study proceeds in four steps: (i) a controlled, compute- and scale-matched comparison revealing that AR is a more effective backbone for blockwise hybrids than masked diffusion objectives; (ii) a scalable conversion recipe, SDAR , validating that AR models spanning 1.7B to 30B parameters can be adapted into block diffusion models with minimal compute while preserving backbone capabilities; and (iii) a systematic characterization of decoding dynamics , which reveals a virtuous cycle where larger models enable more aggressive parallel decoding, achieving theoretical speedups over 5 × and wall-clock speedups of 2.3 × on H200 GPUs in latency-critical regimes; and (iv) an investigation of local non-causal modeling capabilities , showing that SDAR’s local bidirectional attention overcomes causal bottlenecks in scientific domains (e.g., chemistry) and enables robust test-time scaling. We release the full model suite, the training framework, and our inference engines for further innovation in non-autoregressive generative paradigms.

## 25. DRIFT: Transferring Reasoning Priors for Efficient MLLM Fine-Tuning

- Authors: Chao Huang, Zeliang Zhang, Jiang Liu, Ximeng Sun, Jialian Wu, Xiaodong Yu, Ze Wang, Chenliang Xu, Emad Barsoum, Zicheng Liu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.9122109975802797
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1015/
- PDF: https://aclanthology.org/2026.findings-acl.1015.pdf
- Local PDF: pdf/2026-07-13_25_DRIFT_ Transferring Reasoning Priors for Efficient MLLM Fine-Tuning.pdf

Multimodal large language models (MLLMs) have made rapid progress, yet their reasoning ability often lags behind strong text-only LLMs. Bridging this gap typically requires large-scale multimodal reasoning data or reinforcement learning, incurring substantial cost. An appealing alternative is parameter-space model merging between reasoning-enhanced LLMs and MLLMs, but we show that naive merging is fragile: its effectiveness varies widely across model families and can significantly degrade performance (e.g., for Qwen-based MLLMs). We propose Directional Reasoning Injection for Fine-Tuning (DRIFT), a lightweight method that transfers reasoning knowledge in the gradient space while preserving multimodal alignment. DRIFT precomputes a reasoning prior from the parameter differences between text-only reasoning experts and multimodal models, and uses it to bias gradients during supervised fine-tuning. This design retains the simplicity of standard SFT pipelines while enabling efficient and stable reasoning transfer. Experiments on multimodal reasoning benchmarks, including MathVista and MathVerse, show that DRIFT consistently outperforms naive merging and standard SFT, and matches or surpasses training-intensive methods with substantially lower data and compute.

## 26. The Proxy Presumption: From Semantic Embeddings to Valid Social Measures

- Authors: Baishi Li, Ta Yu, Kelvin J.l. Koa, Ke-Wei Huang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.9119733548291666
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1048/
- PDF: https://aclanthology.org/2026.acl-long.1048.pdf
- Local PDF: pdf/2026-07-13_26_The Proxy Presumption_ From Semantic Embeddings to Valid Social Measures.pdf

Natural Language Processing is rapidly evolving into a primary instrument for Computational Social Science, with researchers increasingly using embeddings to measure latent constructs such as novelty, creativity, and bias. However, this transition faces a fundamental validity challenge: the “Proxy Presumption,” or the reliance on geometric properties (e.g., cosine distance) as direct measures of social concepts. We argue that without explicit validation, unsupervised representations remain entangled mixtures of the target construct ( C ) and confounding attributes ( Z ) like topic, style, and authorship. To bridge the gap between semantic embeddings and valid social measures, we introduce the Construct Validity Protocol (CVP). Drawing on causal representation learning and psychometrics, the CVP offers a rigorous pipeline from conceptualization to quantitative verification. We further propose Counterfactual Neutralization, a novel method using LLMs to reduce confounding in embedding space. By providing a standardized Validity Suite—including tests for discriminant, incremental, and predictive validity—this work offers the community a toolkit to transform heuristic proxies into robust, scientifically defensible instruments.

## 27. Structured Episodic Event Memory

- Authors: Zhengxuan Lu, Dongfang Li, Yukun Shi, Beilun Wang, Longyue Wang, Baotian Hu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.911931080307241
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.277/
- PDF: https://aclanthology.org/2026.acl-long.277.pdf
- Local PDF: pdf/2026-07-13_27_Structured Episodic Event Memory.pdf

Current approaches to memory in Large Language Models (LLMs) predominantly rely on static Retrieval-Augmented Generation (RAG), which often results in scattered retrieval and fails to capture the structural dependencies required for complex reasoning. For autonomous agents, these passive and flat architectures lack the cognitive organization necessary to model the dynamic and associative nature of long-term interaction. To address this, we propose **S**tructured **E**pisodic **E**vent **M**emory (**SEEM**), a hierarchical framework that synergizes a graph memory layer for relational facts with a dynamic episodic memory layer for narrative progression. Grounded in cognitive frame theory, SEEM transforms interaction streams into structured Episodic Event Frames (EEFs) anchored by precise provenance pointers. Furthermore, we introduce an agentic associative fusion and Reverse Provenance Expansion (RPE) mechanism to reconstruct coherent narrative contexts from fragmented evidence. Experimental results on the LoCoMo and LongMemEval benchmarks demonstrate that SEEM significantly outperforms baselines, enabling agents to maintain superior narrative coherence and logical consistency.

## 28. Failure Modes in Multi-Hop QA: The Weakest Link Effect and the Recognition Bottleneck

- Authors: Meiru Zhang, Zaiqiao Meng, Nigel Collier
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.9116435197113555
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1937/
- PDF: https://aclanthology.org/2026.acl-long.1937.pdf
- Local PDF: pdf/2026-07-13_28_Failure Modes in Multi-Hop QA_ The Weakest Link Effect and the Recognition Bottleneck.pdf

Despite scaling to massive context windows, Large Language Models (LLMs) struggle with multi-hop reasoning due to inherent position bias, which causes them to overlook information at certain positions. Whether these failures stem from an inability to locate evidence (recognition failure) or integrate it (synthesis failure) is unclear. We introduce Multi-Focus Attention Instruction (MFAI), a semantic probe to disentangle these mechanisms by explicitly steering attention towards selected positions. Across 5 LLMs on two multi-hop QA tasks (MuSiQue and NeoQA), we identify the "Weakest Link Effect": in our 18-document, 3-bucket setting, multi-hop reasoning performance collapses to the level of the least visible evidence, governed by absolute position rather than the linear distance between facts. While matched MFAI resolves recognition bottlenecks, improving accuracy by up to 11.49% in low-visibility positions, misleading MFAI yields divergent effects modulated by task topology: entity-centric tasks with vertical reasoning chains are vulnerable, whereas event-centric tasks with horizontal evidence structures are more resilient. Finally, we demonstrate that "thinking" models utilizing System-2 reasoning effectively locate and integrate the required information, matching gold-only baselines even in noisy, long-context settings. Supplementary experiments on 2WikiMultiHopQA, extended 3-4 hop counts, and a 32B model confirm these findings generalize across datasets, reasoning depths, and model scales.

## 29. MDC-Bench: A Multidisciplinary Causal Benchmark Based on Causal Structures for Evaluating Large Language Models

- Authors: Peng Wang, Yuxiong Yan, Xiao Ding, Kai Xiong, Bibo Cai, Chao Peng, Yutai Hou, Dandan Tu, Bing Qin, Ting Liu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.9115655667417046
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1409/
- PDF: https://aclanthology.org/2026.findings-acl.1409.pdf
- Local PDF: pdf/2026-07-13_29_MDC-Bench_ A Multidisciplinary Causal Benchmark Based on Causal Structures for Evaluating Large Language Models.pdf

Existing causal datasets primarily focus on the commonsense domain, where the questions mainly involve simple, single-hop direct causal relationships. When models possess the corresponding knowledge, even if they cannot understand the causal relationships, they can directly arrive at the correct answers through knowledge matching. However, LLMs often perform poorly when answering questions with complex causal structures and domain-specific expertise. To address the above challenges, we propose MDC-Bench, a multidisciplinary causal evaluation benchmark. MDC-Bench adopts a three-level causal framework consisting of 4 core causal tasks, while its sample content covers 7 representative disciplines and diverse causal structures. In view of the limited coverage of multidisciplinary knowledge during the pre-training phase, the model cannot answer questions relying on knowledge matching. The diverse causal structures force the models to grasp the internal causal logic. We also increase the task complexity through methods such as compound causal operations, aiming to enhance the discriminability among models. MDC-Bench achieves the improvement in terms of domain specialization, structural diversity, and task complexity. Through extensive evaluation, we observe that even the advanced models have substantial room for improvement. MDC-Bench not only establishes a standardized baseline for causal research but also provides valuable insights for the applying LLMs in multiple domains.

## 30. Reviving Iterative Refinement in Diffusion-based NER with an Initializer-Restorer Approach

- Authors: Long Hai Trieu, Phí Minh Hieu, Makoto Miwa
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.9109449783286703
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-short.72/
- PDF: https://aclanthology.org/2026.acl-short.72.pdf
- Local PDF: pdf/2026-07-13_30_Reviving Iterative Refinement in Diffusion-based NER with an Initializer-Restorer Approach.pdf

Diffusion models have introduced a generative paradigm for Named Entity Recognition (NER), formulating the task as refining entityspans from noise. While promising, our analysis on the ACE2004 dataset reveals a limitation when training with Exponential MovingAverage (EMA): the model performance often peaks at a single inference step (γ = 1) and plateaus or degrades with additional steps. Thissuggests that under standard stable training configurations, the model may function primarily as a one-step generator rather thanleveraging the iterative refinement capability characteristic of diffusion models. To address this, we propose an Initializer-Restorerapproach. Instead of initializing the reverse process from random Gaussian noise, we utilize a preliminary set of candidate spansgenerated by a standard NER model (e.g., BERT or GLiNER). This allows the diffusion model to start from an informed, diverse prior,enabling effective iterative restoration. We investigate different training strategies for the restorer and find that a hybrid strategy mixingground truth and noisy predictions is essential. Experiments on ACE2004, GENIA, and CleanCoNLL show that our approach improvesperformance over the baseline, particularly when multiple restoration steps are employed. For instance, on CleanCoNLL, our methodachieves an F1 score of 94.70%, compared to 93.79% for the baseline. Our code is available at https://github.com/longtrieu-ai/Initializer-Restorer-NER.
