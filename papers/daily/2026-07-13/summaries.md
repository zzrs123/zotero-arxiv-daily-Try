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

## 31. Geometric-aware deep learning for deciphering tissue structure from spatially resolved transcriptomics

- Authors: Xingyi Li, Xiangting Jia, Dongmin Zhao, Jialuo Xu, Gaoming Du, Yang Qi, Yingfu Wu, Yiqi Chen, Junnan Zhu, Jia Gu, Xuequn Shang
- Source: openalex
- Venue type: journal
- Journal: Communications Biology
- Publication status: published
- Publication date: 2026-07-11
- DOI: https://doi.org/10.1038/s42003-026-10667-1
- Categories: Single-cell and spatial transcriptomics, Cell Image Analysis Techniques, Gene expression and cancer classification
- Relevance: 3.714214417874433
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://doi.org/10.1038/s42003-026-10667-1
- PDF: https://www.nature.com/articles/s42003-026-10667-1_reference.pdf
- Local PDF: pdf/2026-07-13_31_Geometric-aware deep learning for deciphering tissue structure from spatially resolved transcriptomics.pdf

Recent advances in spatially resolved transcriptomics have enabled large-scale measurement of gene expression while preserving spatial context, facilitating the investigation of spatial heterogeneity within tissues. In this study, we propose SpatialGEO, a geometric-aware deep learning framework that integrates gene expression profiles with spatial coordinates to generate biologically meaningful low-dimensional embeddings, enabling the dissection of complex tissue architectures. We systematically evaluate SpatialGEO across multiple tissue types and diverse SRT platforms. Results show that SpatialGEO achieves superior performance in tissue structure dissection and data denoising compared to state-of-the-art methods. Moreover, when applied to human breast cancer samples, SpatialGEO precisely delineates the tumor microenvironment and uncovers molecular heterogeneity within tumors and intercellular communication between invasive ductal carcinoma and tumor edge. In mouse embryogenesis, SpatialGEO accurately reconstructs spatiotemporal tissue architectures, highlighting organ-specific developmental programs and elucidating molecular drivers of early neural development.

## 32. COAST: Context-Aware Differential Learning for Gene Expression Prediction in Spatial Transcriptomics

- Authors: Keunho Byeon, Sunhong Park, Jeewoo Lim, Jin Tae Kwak
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-10
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.69513741250443
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.09166v1
- PDF: https://arxiv.org/pdf/2607.09166v1
- Local PDF: pdf/2026-07-13_32_COAST_ Context-Aware Differential Learning for Gene Expression Prediction in Spatial Transcriptomics.pdf

Spatial transcriptomics enables profiling of spatial gene expression but is limited by high cost and low throughput, motivating prediction from H&E histopathology images. Existing context-aware methods mainly supervise absolute expression, while relative expression relationships between spots are rarely used explicitly. We propose COAST, a context-aware differential learning framework for spatial gene expression prediction. COAST conditions the local and global context features with type-specific modulation and aggregates the target and context spot tokens using a Transformer encoder to capture both fine-grained local patterns and slide-level structure. It is trained with a joint objective that combines absolute expression regression with signed differential regression between the target and context spots. Experiments on multiple spatial transcriptomics datasets show consistent improvements in correlation- and distribution-based metrics, demonstrating the effectiveness of context-aware differential learning for histology-based spatial gene expression prediction.

## 33. ALICE: Learning a General-Purpose Pathology Foundation Model from Vision, Vision-Language, and Slide-Level Experts

- Authors: Jiawen Li, Tian Guan, Huijuan Shi, Xitong Ling, Mingxi Fu, Anjia Han, Chao He, Yonghong He
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-10
- DOI: Unavailable
- Categories: cs.CV, cs.AI
- Relevance: 3.4001920199341065
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.09526v1
- PDF: https://arxiv.org/pdf/2607.09526v1
- Local PDF: pdf/2026-07-13_33_ALICE_ Learning a General-Purpose Pathology Foundation Model from Vision, Vision-Language, and Slide-Level Experts.pdf

Foundation models are reshaping computational pathology, yet their capabilities remain shaped by pretraining objectives, data sources, and spatial scales, fragmenting complementary expertise across separate backbones. Here we present ALICE, a unified foundation model trained through multi-stage agglomerative distillation that sequentially distills eight vision-only, vision-language, and slide-level teacher models into dedicated modules of a single backbone. ALICE is pretrained on 24,985,184 tile-level pathology images and 155,604 high-resolution images, and evaluated across 21 task scenarios, 96 downstream tasks, and 48 data sources, spanning region-of-interest tissue analysis, vision-language multimodal evaluation, and whole-slide clinical assessment. In all three evaluation settings, ALICE achieved the best average rank among task-matched pathology foundation models. These results demonstrate that agglomerative distillation can consolidate complementary capabilities from specialized models into a unified backbone for broad computational pathology applications. The model is available at https://github.com/WonderLandxD/ALICE.

## 34. Integrating Large Language Models and Graph Convolutional Networks for Semi-Supervised Image Classification

- Authors: Camila Piscioneri Magalhães, Lucas Pascotti Valem
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-10
- DOI: Unavailable
- Categories: cs.CV, cs.AI
- Relevance: 3.377651107965523
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.09104v1
- PDF: https://arxiv.org/pdf/2607.09104v1
- Local PDF: pdf/2026-07-13_34_Integrating Large Language Models and Graph Convolutional Networks for Semi-Supervised Image Classification.pdf

While the growing availability of image data has driven significant advances, labeling datasets remains costly and time-consuming. Therefore, semi-supervised approaches such as Graph Convolutional Networks (GCNs), which learn from both labeled and unlabeled data, have emerged as a promising solution. One of the primary challenges in applying GCNs to image classification is graph construction, since, unlike in citation networks or similar domains, images typically do not come with a predefined structural representation. For visual data, most studies construct graphs based on the similarity between feature vectors from pretrained deep learning backbones, typically by employing kNN or reciprocal kNN algorithms. Although Large Language Models (LLMs) have shown remarkable capability in capturing high-level semantics, their integration with GCNs for image classification remains underexplored. Aiming to fill this gap, our approach uses a Vision Language Model (VLM) to generate textual image descriptions, which are then processed by an LLM to estimate semantic similarity scores between connected images. These scores guide the pruning of edges in kNN and reciprocal kNN graphs, filtering out semantically irrelevant neighbors. Experimental results reveal that leveraging LLMs for graph refinement can improve classification accuracy, particularly for kNN graphs and some backbones. The source code is publicly available at http://gcnllm.lucasvalem.com.

## 35. TheBioCollection: Unified Pre-Training Scale LLM Corpus for Biology

- Authors: Hyunjin Seo, Hyeon Hwang, Gyubok Lee, Jay Shin, Jimin Park, Taesoo Kim, Sanghoon Lee, Hongjoon Ahn, Sungjun Han, Sangwon Jung
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-09
- DOI: Unavailable
- Categories: q-bio.QM, cs.AI, cs.LG
- Relevance: 3.344374625061093
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.08803v1
- PDF: https://arxiv.org/pdf/2607.08803v1
- Local PDF: pdf/2026-07-13_35_TheBioCollection_ Unified Pre-Training Scale LLM Corpus for Biology.pdf

The push toward large language models for biology (BioLM) has created a need for training corpora that can endow models with a genuine understanding of biology. However, existing biological resources, such as molecular databases, protein repositories, genomic annotations, single-cell atlases, and pathway databases, are scattered across heterogeneous formats and remain unorganized into a cohesive corpus for language model training. We present TheBioCollection, a 52.6B-token pre-training-scale corpus that converts these disparate resources into a unified, training-ready form spanning small molecules, proteins, genomic sequences, cells, and pathways. Beyond consolidating existing data, TheBioCollection enriches each record with tool-computed biological properties and introduces new instruction tasks for capabilities that current corpora barely cover. We pair the corpus with TheBioCollection-Eval, a matched suite probing recognition, generation, and prediction across molecular, protein, genomic, cellular, and cross-domain settings. Holding the base Gravity-16B-A3B architecture fixed, training on TheBioCollection more than doubles its overall score on TheBioCollection-Eval with gains in every domain, while leaving general linguistic ability nearly intact.

## 36. Mixture of Probes: Learning from Privileged Modalities in Multimodal LLMs Through Probing

- Authors: Dominick Reilly, Qiyu Wu, Hiromi Wakaki, Srijan Das, Yuki Mistufuji
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-09
- DOI: Unavailable
- Categories: cs.CV, cs.LG
- Relevance: 3.1695856729565213
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.08839v1
- PDF: https://arxiv.org/pdf/2607.08839v1
- Local PDF: pdf/2026-07-13_36_Mixture of Probes_ Learning from Privileged Modalities in Multimodal LLMs Through Probing.pdf

Multimodal Large Language Models (MLLMs) are typically designed under the assumption that all modalities available during training will also be accessible at inference. However, many real-world settings violate this assumption, requiring models to operate under a privileged modality setting, where auxiliary modalities are available only during training. While these modalities contain valuable information, existing MLLMs largely fail to leverage them effectively, as they treat modalities as interchangeable inputs rather than sources of complementary supervision. We propose Mixture of Probes (MoP), a novel framework that disentangles modality-specific and modality-general signals within the MLLM, allowing the model to preserve modality-dependent structure while learning transferable representations across modalities. At its core, MoP achieves this through a structured probing mechanism that extracts and organizes information from intermediate representations of a shared modality encoder, rather than relying only on final-layer alignment as done in existing MLLMs. To support this disentanglement, we further introduce MoP Cross-modal Training (MoP-X), a training strategy for MoP centered around a probe disentanglement loss that prevents probe collapse and encourages cross-modal learning. We evaluate MoP across two domains spanning eight tasks and four modalities under a comprehensive evaluation protocol tailored to the privileged modality setting, where each modality is independently treated as the sole input at inference time. MoP consistently outperforms strong MLLM baselines, achieving up to 65% relative improvement, demonstrating that auxiliary modalities, even when unavailable at inference, can provide substantial gains when effectively leveraged during training. Code, model checkpoints, and evaluation protocols will be made available at https://github.com/Sony/MoP.

## 37. Temporal Knowledge Graph Forecasting under Distribution Shifts: A Synthetic Evaluation

- Authors: Konrad Özdemir, Julia Gastinger, Lukas Kirchdorfer, Heiner Stuckenschmidt
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-10
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.155181501995573
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.09232v1
- PDF: https://arxiv.org/pdf/2607.09232v1
- Local PDF: pdf/2026-07-13_37_Temporal Knowledge Graph Forecasting under Distribution Shifts_ A Synthetic Evaluation.pdf

Temporal knowledge graphs (TKGs) represent evolving relational systems, whose underlying data-generating processes often change over time. Yet, TKG forecasting models are commonly evaluated only on empirical benchmark datasets that provide limited insight into the models' robustness to such distribution shifts. Recognising this issue, we study TKG forecasting under controlled shift environments using a synthetic TKG generator that encodes three temporal and structural properties -- recurrence, homophily, and periodicity -- as data-generating mechanisms. This allows us to evaluate seven forecasting architectures under stationary and shifting regimes. Our experiments suggest that robustness in TKG forecasting is highly signal-dependent. Recurrence-based and periodic regularities are largely recoverable under stationary conditions, and simple memory-based baselines can be competitive when recurrence dominates the data. However, structural breaks reveal limitations in model adaptivity, with shifts in latent entity-community structure posing the strongest challenge in our study. Overall, our findings improve the understanding of the capabilities and limitations of current TKG models confronted with temporal distribution shifts.

## 38. What VGGT Knows About Overlap: Probing Geometric Foundation Models for Co-Visibility

- Authors: Filippo Ziliotto, Luciano Serafini, Lamberto Ballan, Tommaso Campari
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-10
- DOI: Unavailable
- Categories: cs.CV, cs.AI
- Relevance: 3.1508504714395045
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.09503v1
- PDF: https://arxiv.org/pdf/2607.09503v1
- Local PDF: pdf/2026-07-13_38_What VGGT Knows About Overlap_ Probing Geometric Foundation Models for Co-Visibility.pdf

A fundamental challenge in 3D reconstruction and robotic localization is co-visibility: determining which image pairs share overlapping visible surfaces, particularly in scenarios with minimal overlap. We demonstrate that VGGT implicitly encodes co-visibility as an emergent behavior: without any supervision for this task, its internal representations exhibit a clear hierarchical structure mirroring that of large language models, i.e. early layers build a 3D-aware scene representation, while late layers act as dedicated co-visibility reasoners. In particular, we identify layer L17 as a negative anchor that consistently routes non-co-visible pairs for this backbone, regardless of the evaluation setting, providing task-grounded evidence of layer specialization in a geometry-grounded foundation model. Building on this, we introduce Co-VGGT, which freezes VGGT and trains only a lightweight layer-wise mixture-of-experts head (less than 7.5M parameters) to classify co-visibility from RGB alone, treating each layer as a specialized expert whose geometric abstraction is adaptively weighted per input pair. On the Co-VisiON benchmark, Co-VGGT surpasses the human annotation baseline and improves over prior work by more than 25% pairwise and 10% multiview. Pairwise predictions are well-calibrated (ECE=0.030), enabling direct use as edge weights in visibility graphs for downstream SfM and SLAM pipelines without post-hoc correction. Code and data are available.

## 39. Autoregressive latent diffusion for 3D molecule generation

- Authors: Federico Ottomano, Gaopeng Ren, Yingzhen Li, Kim E. Jelfs, Alex M. Ganose
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-10
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.1298955621445232
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.09277v1
- PDF: https://arxiv.org/pdf/2607.09277v1
- Local PDF: pdf/2026-07-13_39_Autoregressive latent diffusion for 3D molecule generation.pdf

Three-dimensional (3D) molecule generation has been dominated by diffusion models, which achieve strong generation quality but typically require the molecular size to be specified a priori. Recent autoregressive approaches have substantially narrowed the performance gap while naturally supporting variable-length generation and conditioning on partial molecular context. However, balancing unconditional and context-conditioned generation remains challenging. We introduce KRONOS, a latent autoregressive diffusion framework that generates molecules in the latent space of a pre-trained autoencoder, jointly modeling molecular graph topology and geometry, while retaining the flexibility of autoregressive generation. We further introduce a mixed training strategy inspired by Fill-in-the Middle (FIM) paradigm, enabling both unconditional and fragment-conditioned molecular generation within a single left-to-right autoregressive model. Experiments on QM9 and GEOM-Drugs demonstrate that KRONOS achieves leading unconditional generation performance among autoregressive methods, while remaining competitive with diffusion models. Moreover, fragment-conditioned generation is achieved with negligible impact on unconditional generation performance, demonstrating that both generation paradigms can be supported within a single architecture.

## 40. A Unified Approach to Interpreting Knowledge Distillation for Large Language Models via Interactions

- Authors: Qingzhuo Wang, Ruiyang Qin, Zhenxin Qin, Wen Shen, Zhihua Wei
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-05-05
- DOI: Unavailable
- Categories: cs.LG, cs.AI, cs.CL, cs.GT
- Relevance: 3.048183754852874
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.08776v1
- PDF: https://arxiv.org/pdf/2607.08776v1
- Local PDF: pdf/2026-07-13_40_A Unified Approach to Interpreting Knowledge Distillation for Large Language Models via Interactions.pdf

Despite the success of knowledge distillation (KD) in Large Language Models (LLMs), the underlying mechanism behind its efficacy remains unclear. In this paper, we propose a unified approach to explore the common mechanism of various KD methods using interactions. Specifically, we decompose the output score of the LLM into the sum of numerous interactions. Each interaction represents a nonlinear relationship involving a set of input variables (e.g., words). Based on the decomposed interactions, we discover that the common mechanism underlying various KD methods is the sparsification of interactions, i.e., student models retain fewer interactions for inference while suppressing other interactions to zero effects. Furthermore, we discover that the performance variance across different KD methods arises from their capabilities in handling complex interactions. A KD method typically yields better performance if it enables the student model to achieve higher sparsity of complex interactions. Motivated by these insights, we propose a plug-and-play loss function called Complex Interaction Penalty (CIP) to explicitly enforce the sparsity of complex interactions during the distillation process. Extensive experiments demonstrate that integrating CIP consistently improves the performance of diverse KD methods on both in-domain and out-of-distribution benchmarks.

## 41. Sensitivity-Aware Thresholding and Token Routing for Activation Sparsification in Large Language Models

- Authors: Bishmoy Paul, Youngmin Yi, Hoeseok Yang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-09
- DOI: Unavailable
- Categories: cs.LG, cs.CL
- Relevance: 2.973153821228464
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.08991v1
- PDF: https://arxiv.org/pdf/2607.08991v1
- Local PDF: pdf/2026-07-13_41_Sensitivity-Aware Thresholding and Token Routing for Activation Sparsification in Large Language Models.pdf

Efficient inference in Large Language Models (LLMs) requires deciding where computation can be reduced while preserving model quality. We study this problem through multilayer perceptron (MLP) activation sparsification and token-level conditional routing. We first propose Sensitivity-Aware Thresholding for Sparsity (SATS), a threshold calibration method to choose layerwise gate thresholds using a local MLP output sensitivity proxy rather than calibrating thresholds directly from activation percentiles. While SATS retains the existing mechanism of sparsifying MLP activations by thresholding gate activations, it replaces percentile-based calibration with a sensitivity-aware selection rule. We then introduce a lightweight token routing framework that dynamically selects between a base path and a modified path on a per-token basis, rather than applying the modified computation uniformly to all tokens. We evaluate both methods on multiple recent open-weight LLMs. Our results show that SATS improves over the threshold-based sparsification baseline at matched actual sparsity and that token routing yields a more favorable quality-throughput trade-off than static activation modification baselines. Overall, our results suggest that improved threshold calibration and token routing can improve the quality-throughput trade-off in LLMs.

## 42. TSRouter: Dynamic Modality-Model Selection for Time Series Reasoning

- Authors: Fangxu Yu, Tao Feng, Dehai Min, Lu Cheng, Ge Liu, Tianyi Zhou
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-09
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 2.9537001972973376
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.08940v1
- PDF: https://arxiv.org/pdf/2607.08940v1
- Local PDF: pdf/2026-07-13_42_TSRouter_ Dynamic Modality-Model Selection for Time Series Reasoning.pdf

Time series reasoning is essential for real-world problem-solving. While both Large Language Models (LLMs) and Vision-Language Models (VLMs) can reason about time-series data, their capabilities are complementary: LLMs process time series as text sequences and thus preserve exact numerical understanding, but struggle with global patterns, whereas VLMs efficiently capture these patterns by visualizing time series but may lose fine-grained details. Moreover, models vary significantly in task-specific expertise and inference costs. Dynamically selecting the most suitable modality and model for each query is therefore crucial, yet challenging because it requires modeling the complex interactions among tasks, queries, modalities, and models, which carry rich contextual signals. To this end, we introduce TSRouter, a graph-based dynamic routing framework. TSRouter constructs a heterogeneous graph of task, query, modality, and model nodes to contextualize the interactions among query characteristics, modality attributes, and model capabilities. TSRouter formulates routing as a candidate scoring problem, where each modality-model pair is evaluated based on user-defined performance-cost preferences to select the optimal candidate. Comprehensive evaluations on 4 distinct time series reasoning tasks reveal that TSRouter substantially outperforms diverse baselines with 16\% to 46\% relative improvements. Furthermore, TSRouter demonstrates robust zero-shot plug-and-play generalization to unseen models and novel tasks and preserves high performance while reducing computational overhead through cost-aware optimization. Our code is available at https://github.com/tianyi-lab/TSRouter.

## 43. Scalable Visual Pretraining for Language Intelligence

- Authors: Yiming Zhang, Zhonghan Zhao, Wenwei Zhang, Haiteng Zhao, Tianyang Lin, Yunhua Zhou, Demin Song, Kuikun Liu, Haochen Ye, Haian Huang, Yuzhe Gu, Haijun Lv, Qipeng Guo, Bin Liu, Gaoang Wang, Kai Chen
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-10
- DOI: Unavailable
- Categories: cs.CV, cs.AI, cs.MM
- Relevance: 2.9423111210312025
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.09657v1
- PDF: https://arxiv.org/pdf/2607.09657v1
- Local PDF: pdf/2026-07-13_43_Scalable Visual Pretraining for Language Intelligence.pdf

The rapid progress of large foundation models has been driven predominantly by pretraining on large-scale text corpora. However, many forms of knowledge are conveyed through visual representations, where figures, typeset equations, and page layouts carry rich information that cannot be faithfully or completely captured by text alone. Yet current pretraining approaches discard these visual cues by converting visually rich sources, such as documents and web pages, into plain text for learning language intelligence. This paper challenges the default assumption that language models must be trained on text-only representations and shows that Visual Pretraining is a scalable learner for foundation model intelligence. To this end, we conduct a systematic study of unsupervised visual pretraining paradigms that directly leverage visual documents without text extraction. Across multiple backbones and benchmarks, visual pretraining on the same underlying corpora consistently outperforms text-only pretraining, offering an efficient pathway to scalable language intelligence.

## 44. MTRouter: Cost-Aware Multi-Turn LLM Routing with History–Model Joint Embeddings

- Authors: Yiqun Zhang, Hao Li, Zihan Wang, Shi Feng, Xiaocui Yang, Daling Wang, Bo Zhang, Lei Bai, Shuyue Hu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.9098354864551923
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.2045/
- PDF: https://aclanthology.org/2026.acl-long.2045.pdf
- Local PDF: pdf/2026-07-13_44_MTRouter_ Cost-Aware Multi-Turn LLM Routing with History–Model Joint Embeddings.pdf

Multi-turn, long-horizon tasks are increasingly common for large language models (LLMs), but solving them typically requires many sequential model invocations, accumulating substantial inference costs. Here, we study cost-aware multi-turn LLM routing: selecting which model to invoke at each turn from a model pool, given a fixed cost budget. We propose MTRouter, which encodes the interaction history and candidate models into joint history–model embeddings, and learns an outcome estimator from logged trajectories to predict turn-level model utility. Experiments show that MTRouter improves the performance–cost trade-off: on ScienceWorld, it surpasses GPT-5 while reducing total cost by 58.7%; on Humanity’s Last Exam (HLE), it achieves competitive accuracy while reducing total cost by 43.4% relative to GPT-5, and these gains even carry over to held-out tasks. Further analyses reveal several mechanisms underlying its effectiveness: relative to prior multi-turn routers, MTRouter makes fewer model switches, is more tolerant to transient errors, and exhibits emergent specialization across models.Code: https://github.com/ZhangYiqun018/MTRouter

## 45. Beyond Monolingual Assumptions: A Survey on Code-Switched NLP in the Era of Large Language Models across Modalities

- Authors: Rajvee Sheth, Samridhi Raj Sinha, Mahavir Patil, Himanshu Beniwal, Mayank Singh
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.9090079044037305
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.386/
- PDF: https://aclanthology.org/2026.acl-long.386.pdf
- Local PDF: pdf/2026-07-13_45_Beyond Monolingual Assumptions_ A Survey on Code-Switched NLP in the Era of Large Language Models across Modalities.pdf

Amidst the rapid advances of large language models (LLMs), most LLMs still struggle with mixed-language inputs, limited Code-switching (CSW) datasets, and evaluation biases, which hinder their deployment in multilingual societies. This survey provides the first comprehensive analysis of CSW-aware LLM research, reviewing 327 studies spanning five research areas, 15+ NLP tasks, 30+ datasets, and 80+ languages. We classify recent advances by architecture, training strategy, and evaluation methodology, outlining how LLMs have reshaped CSW modelling and what challenges persist. The paper concludes with a roadmap emphasizing the need for inclusive datasets, fair evaluation, and linguistically grounded models to achieve truly multilingual intelligence. A curated collection of all resources is maintained at https://github.com/lingo-iitgn/awesome-code-mixing/.

## 46. From AR to Diffusion: Efficiently Adapting Large Language Models with Strictly Causal and Elastic Horizons

- Authors: Xiangyu Ma, Teng Xiao, Zuchao Li, Lefei Zhang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.908475986228305
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.958/
- PDF: https://aclanthology.org/2026.acl-long.958.pdf
- Local PDF: pdf/2026-07-13_46_From AR to Diffusion_ Efficiently Adapting Large Language Models with Strictly Causal and Elastic Horizons.pdf

Diffusion models promise efficient parallel text generation but rely on bidirectional attention, creating a structural mismatch with pre-trained Autoregressive (AR) models. This incompatibility precludes reusing robust AR priors, necessitating prohibitive pre-training from scratch. To bridge this gap, we propose FLUID, a framework that efficiently adapts AR backbones to the diffusion paradigm. By enforcing Strictly Causal Alignment, FLUID enables seamless initialization from standard GPT-style checkpoints, circumventing the need for massive pre-training. Furthermore, we introduce Elastic Horizons, an entropy-driven mechanism that dynamically modulates denoising strides based on local information density rather than fixed schedules. Experiments demonstrate that FLUID achieves state-of-the-art performance while reducing training costs by orders of magnitude, effectively reconciling established AR foundations with efficient parallel generation. Our code is available at https://huggingface.co/MYTH-Lab/FLUID.

## 47. Decoupling Generalization and Adaptation in Meta-Learning for Large Language Models

- Authors: Nitin Vetcha, Binqian Xu, Dianbo Liu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.9076477427648157
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-short.69/
- PDF: https://aclanthology.org/2026.acl-short.69.pdf
- Local PDF: pdf/2026-07-13_47_Decoupling Generalization and Adaptation in Meta-Learning for Large Language Models.pdf

Fine-tuning large language models (LLMs) for downstream tasks remains expensive, even with parameter-efficient methods like Low-Rank Adaptation (LoRA). In this regard, meta-learning approaches such as Model-Agnostic Meta-Learning for LLMs (MAML-en-LLM) and Amortized Bayesian Meta-Learning for LoRA (ABMLL) have emerged as promising solutions for rapid downstream LLM adaptation. However, these methods fundamentally couple two distinct objectives: learning generalizable initializations and enabling efficient task adaptation. We argue that this coupling limits both the quality of learned representations and adaptation efficiency. In this paper, we introduce **DeGAML-LLM** (**De**coupled **G**eneralization and **A**daptation in **M**eta-**L**earning for **LLM**s), a novel framework that explicitly separates these two objectives through dedicated parameter spaces. Specifically, we maintain a generalization module that learns task-agnostic representations across the task distribution, and an adaptation module that specializes in rapid task-specific adjustment. Extensive experiments on common-sense reasoning, mathematics, logic, social, medical and coding benchmarks across model scales demonstrate that DeGAML-LLM outperforms existing meta-learning and standard multi-task baselines.

## 48. CircuitSynth: Reliable Synthetic Data Generation

- Authors: Zehua Cheng, Wei Dai, Jiahao Sun, Thomas Lukasiewicz
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.907170342834272
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1770/
- PDF: https://aclanthology.org/2026.findings-acl.1770.pdf
- Local PDF: pdf/2026-07-13_48_CircuitSynth_ Reliable Synthetic Data Generation.pdf

The generation of high-fidelity synthetic data is a cornerstone of modern machine learning, yet Large Language Models (LLMs) frequently suffer from hallucinations, logical inconsistencies, and mode collapse when tasked with structured generation. Existing approaches, such s prompting or retrieval-augmented generaon, lack the mechanisms to balance linguistic expressivity with formal guarantees regarding validity and coverage. To address this, we propose CircuitSynth, a novel neuro-symbolic framework that decouples semantic reasoning from surface realization. By distilling the reasoning capabilities of a Teacher LLM into a Probabilistic Sentential Decision Diagram (PSDD), CircuitSynth creates a tractable semantic prior that structurally enforces hard logical constraints. Furthermore, we introduce a convex optimization mechanism to rigorously satisfy soft distributional goals. Empirical evaluations across diverse benchmarks demonstrate that CircuitSynth achieves 100% Schema Validity even in complex logic puzzles where unconstrained baselines fail (12.4%) while significantly outperforming state-of-the-art methods in rare-combination coverage.

## 49. OmniVDiff: Omni Controllable Video Diffusion for Generation and Understanding

- Authors: Dianbing Xi, Jiepeng Wang, Yuanzhi Liang, Xi Qiu, Yuchi Huo, Rui Wang, Chi Zhang, Xuelong Li
- Source: openalex
- Venue type: conference
- Journal: Proceedings of the AAAI Conference on Artificial Intelligence
- Publication status: formally_published
- Publication date: 2026-03-14
- DOI: https://doi.org/10.1609/aaai.v40i13.38068
- Categories: Generative Adversarial Networks and Image Synthesis, Multimodal Machine Learning Applications, Face recognition and analysis
- Relevance: 2.9060396724174264
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://doi.org/10.1609/aaai.v40i13.38068
- PDF: Unavailable
- Local PDF: Not downloaded

In this paper, we propose a novel framework for controllable video diffusion, OmniVDiff , aiming to synthesize and comprehend multiple video visual content in a single diffusion model. To achieve this, OmniVDiff treats all video visual modalities in the color space to learn a joint distribution, while employing an adaptive control strategy that dynamically adjusts the role of each visual modality during the diffusion process, either as a generation modality or a conditioning modality. Our framework supports three key capabilities: (1) Text-conditioned video generation, where all modalities are jointly synthesized from a textual prompt; (2) Video understanding, where structural modalities are predicted from rgb inputs in a coherent manner; and (3) X-conditioned video generation, where video synthesis is guided by finegrained inputs such as depth, canny and segmentation. Extensive experiments demonstrate that OmniVDiff achieves state-of-the-art performance in video generation tasks and competitive results in video understanding. Its flexibility and scalability make it well-suited for downstream applications such as video-to-video translation, modality adaptation for visual tasks, and scene reconstruction.

## 50. Language on Demand, Knowledge at Core: Composing LLMs with Encoder-Decoder Translation Models for Extensible Multilinguality

- Authors: Mengyu Bu, Yang Feng
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.9051859981972816
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.955/
- PDF: https://aclanthology.org/2026.acl-long.955.pdf
- Local PDF: pdf/2026-07-13_50_Language on Demand, Knowledge at Core_ Composing LLMs with Encoder-Decoder Translation Models for Extensible Multilingua.pdf

Large language models (LLMs) exhibit strong general intelligence, yet their multilingual performance remains highly imbalanced. Although LLMs encode substantial cross-lingual knowledge in a unified semantic space, they often struggle to reliably interface this knowledge with low-resource or unseen languages. Fortunately, pretrained encoder-decoder translation models already possess balanced multilingual capacity, suggesting a natural complement to LLMs. In this work, we propose XBridge, a compositional encoder-LLM-decoder architecture that offloads multilingual understanding and generation to external pretrained translation models, while preserving the LLM as an English-centric core for general knowledge processing and reasoning. To address the resulting representation misalignment across models, we introduce lightweight cross-model mapping layers together with an optimal transport-based alignment objective, enabling fine-grained semantic consistency for multilingual generation. Experiments on four LLMs across multilingual understanding, reasoning, and generation indicate that XBridge outperforms strong baselines, especially on low-resource and previously unseen languages, without retraining the LLM.

## 51. Demystifying Data Organization for Enhanced LLM Training

- Authors: Yalun Dai, Yangyu Huang, Tongshen Yang, Yonghan Wang, Xin Zhang, Wenshan Wu, Qihao Zhao, Hao Li, Yuanyuan Gao, Kim-Hui Yap, Scarlett Li
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.905097260155223
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1262/
- PDF: https://aclanthology.org/2026.acl-long.1262.pdf
- Local PDF: pdf/2026-07-13_51_Demystifying Data Organization for Enhanced LLM Training.pdf

Large Language Models (LLMs) have revolutionized various fields, yet their training efficiency is heavily reliant on effective data curation. While data selection has been widely studied, the strategic data organization for enhanced training remains an underexplored area, particularly since current LLMs are often trained for only one or a few epochs. This paper systematically explores the influence of data organization on LLM training by reusing pre-computed sample-level scores originally generated for data efficiency, thereby incurring minimal additional computational overhead. We identify and formalize four key guidances for optimizing data organization: Boundary Sharpening, Cyclic Scheduling, Curriculum Continuity, and Local Diversity. Guided by them, we introduce two novel data ordering methods termed STR and SAW. Extensive experiments across different model scales and data sizes, encompassing both pre-training and SFT stages, validate the effectiveness of our summarized guidances. They also demonstrate the robustness of our proposed data ordering methods in enhancing the stability and performance of LLM training.

## 52. SAMoRA: Semantic-Aware Mixture of LoRA Experts for Task-Adaptive Learning

- Authors: Boyan Shi, Wei Chen, Shuyuan Zhao, Junfeng Shen, Shengnan Guo, Shaojiang Wang, Huaiyu Wan
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.90468206706176
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1404/
- PDF: https://aclanthology.org/2026.findings-acl.1404.pdf
- Local PDF: pdf/2026-07-13_52_SAMoRA_ Semantic-Aware Mixture of LoRA Experts for Task-Adaptive Learning.pdf

The combination of Mixture-of-Experts (MoE) and Low-Rank Adaptation (LoRA) has shown significant potential for enhancing the multi-task learning capabilities of Large Language Models. However, existing methods face two primary challenges: (1)Imprecise Routing in the current MoE-LoRA method fails to explicitly match input semantics with expert capabilities, leading to weak expert specialization. (2)Uniform weight fusion strategies struggle to provide adaptive update strengths, overlooking the varying complexity of different tasks. To address these limitations, we propose SAMoRA ( S emantic- A ware M ixture o f Lo RA Experts), a novel parameter-efficient fine-tuning framework tailored for task-adaptive learning. Specifically, A Semantic-Aware Router is proposed to explicitly align textual semantics with the most suitable experts for precise routing. A Task-Adaptive Scaling mechanism is designed to regulate expert contributions based on specific task requirements dynamically. In addition, a novel regularization objective is proposed to jointly promote expert specialization and effective scaling. Extensive experiments on multiple multi-task benchmarks demonstrate that SAMoRA significantly outperforms the state-of-the-art methods and holds excellent task generalization capabilities. Code is available at https://github.com/boyan-code/SAMoRA

## 53. LogicPoison: Logical Attacks on Graph Retrieval-Augmented Generation

- Authors: Yilin Xiao, Jin Chen, Qinggang Zhang, Yujing Zhang, Chuang Zhou, Longhao Yang, Lingfei Ren, Xin Yang, Xiao Huang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.904207069867934
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.252/
- PDF: https://aclanthology.org/2026.acl-long.252.pdf
- Local PDF: pdf/2026-07-13_53_LogicPoison_ Logical Attacks on Graph Retrieval-Augmented Generation.pdf

Graph-based Retrieval-Augmented Generation (GraphRAG) enhances the reasoning capabilities of Large Language Models (LLMs) by grounding their responses in structured knowledge graphs. Leveraging community detection and relation filtering techniques, GraphRAG systems demonstrate inherent resistance to traditional RAG attacks, such as text poisoning and prompt injection. However, in this paper, we find that the security of GraphRAG systems fundamentally relies on the topological integrity of the underlying graph, which can be undermined by implicitly corrupting the logical connections, without altering surface-level text semantics. To exploit this vulnerability, we propose LogicPoison, a novel attack framework that targets logical reasoning rather than injecting false contents. Specifically, LogicPoison employs a type-preserving entity swapping mechanism to perturb both global logic hubs for disrupting overall graph connectivity and query-specific reasoning bridges for severing essential multi-hop inference paths. This approach effectively reroutes valid reasoning into dead ends while maintaining surface-level textual plausibility. Comprehensive experiments across multiple benchmarks demonstrate that LogicPoison successfully bypasses GraphRAG’s defenses, significantly degrading performance and outperforming state-of-the-art baselines in both effectiveness and stealth. Our code is available at <https://github.com/Jord8061/logicPoison>.

## 54. Evolution of Accuracy and Visual-Cognitive Errors in a Decade of Vision-Language AI Models

- Authors: Shravan Murlidaran, Miguel P. Eckstein
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-10
- DOI: Unavailable
- Categories: cs.CV, cs.AI
- Relevance: 2.9038872997873266
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.09654v1
- PDF: https://arxiv.org/pdf/2607.09654v1
- Local PDF: pdf/2026-07-13_54_Evolution of Accuracy and Visual-Cognitive Errors in a Decade of Vision-Language AI Models.pdf

Vision language models (VLMs) have made remarkable progress in visual reasoning during the last decade. Most evaluations have used simple scenes (MS-COCO) that do not showcase complex human interactions or behaviors, only a handful of non-curated human descriptions as a benchmark, and have not focused on understanding the model's error types. Here, we introduce the Complex Social Behavior (CSB) dataset, containing 100 images depicting complex social interactions/behaviors. We analyze the progression of scene descriptions over a decade (2017-2025) of VLMs (four pre-Multimodal Large Language Models, MLLMs, and five MLLMs). We evaluate the accuracy of the models and 20 human descriptions relative to a gold standard on the CSB dataset and on a sample from MS-COCO. We analyzed five visual-cognitive error types: object detection, recognition, hallucination, scene understanding, and spatial dependence. The CSB dataset showed a more pronounced improvement than MS-COCO in scene description accuracy, with pre-MLLMs achieving much lower accuracy than the bottom-ranked human descriptions and MLLMs attaining accuracies similar to the top-ranked human descriptions. We show that MLLMs have eliminated the gap in scene description accuracy between simpler MS-COCO scenes and scenes depicting complex behaviors (CSB). MLLMs have almost eliminated all error types in our tested datasets, except for occasionally relying on different image regions for scene descriptions than humans do (spatial dependence error). We also show that detection, recognition, and hallucination errors have the highest impact on scene description accuracy. Together, our findings provide a more thorough evaluation of how visual language models have advanced over the last decade.

## 55. TiKMiX: Efficient Semi-Dynamic Data Mixture via Data Influence for LLM Pre-training

- Authors: Yifan Wang, Binbinliu, Fengze Liu, Yuanfan Guo, Jiyao Deng, Xuecheng Wu, Weidong Zhou, Xiaohuan Zhou, Taifeng Wang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.902093649347168
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.261/
- PDF: https://aclanthology.org/2026.acl-long.261.pdf
- Local PDF: pdf/2026-07-13_55_TiKMiX_ Efficient Semi-Dynamic Data Mixture via Data Influence for LLM Pre-training.pdf

The data mixture used in the pre-training of a language model is a cornerstone of its final performance. Static data mixing strategies in Large Language Model (LLM) pre-training are often suboptimal as they fail to adapt to the model’s evolving learning states. Conversely, fully online dynamic updates, while adaptive, incur prohibitive computational costs. To bridge this gap, we propose TiKMiX, an efficient semi-dynamic data mixing framework. Our approach is grounded in a key observation of influence ranking invariance: the relative importance of data domains exhibits strong temporal stability over long training intervals. Leveraging this insight, we propose Group Influence, an efficient approach for quantifying domain impact, and formulate data mixing as a periodic, low-overhead influence maximization problem. Compared with REGMIX, the proposed method reduces computational overhead by 80% and achieves an average performance gain of 2% across nine downstream benchmarks, thereby effectively mitigating data under-digestion.

## 56. Parallelism and Generation Order in Masked Diffusion Language Models: Limits Today, Potential Tomorrow

- Authors: Yangyang Zhong, Yanmei Gu, Zhengqing Zang, Xiaomeng Li, Yuqi Ding, Xibei Jia, Yuting Shen, Zhenzhong Lan, Liwang Zhu, Weiping Liu, Junlin Zhou, Haisheng Liu, Zhong Xin Yu, Pengxin Luo, Donglian Qi, Yunfeng Yan, Junbo Zhao
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.9020647991691155
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.357/
- PDF: https://aclanthology.org/2026.findings-acl.357.pdf
- Local PDF: pdf/2026-07-13_56_Parallelism and Generation Order in Masked Diffusion Language Models_ Limits Today, Potential Tomorrow.pdf

Masked Diffusion Language Models (MDLMs) promise parallel token generation and arbitrary-order decoding, yet it remains unclear to what extent current models truly realize these capabilities. We characterize MDLM behavior along two dimensions—parallelism strength and generation order—using Average Finalization Parallelism (AFP) and Kendall’s τ. We evaluate eight mainstream MDLMs (up to 100B parameters) on 58 benchmarks spanning knowledge, reasoning, and programming. The results show that MDLMs still lag behind comparably sized autoregressive models, mainly because parallel probabilistic modeling weakens inter-token dependencies. Meanwhile, MDLMs exhibit adaptive decoding behavior: their parallelism and generation order vary significantly with the task domain, the stage of reasoning, and whether the output is correct. On tasks that require “backward information” (e.g., Sudoku), MDLMs adopt a solution order that tends to fill easier Sudoku blanks first, highlighting their advantages. Finally, we provide theoretical motivation and design insights supporting a Generate-then-Edit paradigm, which mitigates dependency loss while retaining the efficiency of parallel decoding.

## 57. PolitNuggets: Benchmarking Agentic Discovery of Long-Tail Political Facts

- Authors: Yifei Zhu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.9020399439134548
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.2085/
- PDF: https://aclanthology.org/2026.acl-long.2085.pdf
- Local PDF: pdf/2026-07-13_57_PolitNuggets_ Benchmarking Agentic Discovery of Long-Tail Political Facts.pdf

Large Reasoning Models (LRMs) embedded in agentic frameworks have transformed information retrieval from static, long-context question answering into open-ended exploration. Yet real-world use requires models to discover and synthesize “long-tail” facts from dispersed sources, a capability that remains under-evaluated. We introduce PolitNuggets, a multilingual benchmark for agentic information synthesis via constructing political biographies for 400 global elites, covering over 10000 political facts. We standardize evaluation with an optimized Supervisor–Searcher multi-agent system and propose FactNet, an evidence-conditional protocol that scores discovery, fine-grained accuracy, and efficiency. Across models and settings, we find that current systems often struggle with fine-grained details, and vary substantially in efficiency. Finally, using benchmark diagnostics, we relate agent performance to underlying model capabilities, highlighting the importance of short-context extraction, multilingual robustness, and reliable tool use.

## 58. Agent-Dice: Disentangling Knowledge Updates via Geometric Consensus for Agent Continual Learning

- Authors: Zheng Wu, Xingyu Lou, Xinbei Ma, Yansi Li, Weiwen Liu, Weinan Zhang, Jun Wang, Zhuosheng Zhang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.901617463614039
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.908/
- PDF: https://aclanthology.org/2026.findings-acl.908.pdf
- Local PDF: pdf/2026-07-13_58_Agent-Dice_ Disentangling Knowledge Updates via Geometric Consensus for Agent Continual Learning.pdf

Large Language Model (LLM)-based agents significantly extend the utility of LLMs by interacting with dynamic environments. However, enabling agents to continually learn new tasks without catastrophic forgetting remains a critical challenge, known as the stability–plasticity dilemma.In this work, we argue that this dilemma fundamentally arises from the failure to explicitly distinguish between common knowledge shared across tasks and conflicting knowledge introduced by task-specific interference. To address this, we propose Agent-Dice, a parameter fusion framework based on directional consensus evaluation.Concretely, Agent-Dice disentangles knowledge updates through a two-stage process: geometric consensus filtering to prune conflicting gradients, and curvature-based importance weighting to amplify shared semantics.We provide a rigorous theoretical analysis that establishes the validity of the proposed fusion scheme and offers insight into the origins of the stability–plasticity dilemma. Extensive experiments on GUI agents and tool-use agent domains demonstrate that Agent-Dice exhibits outstanding continual learning performance with minimal computational overhead and parameter updates.

## 59. Decoding cancer circulating transcriptomic signatures with language models

- Authors: Siwei Deng, Lei Sha, Yongcheng Jin, Tianyao Zhou, Chengen Wang, Liu Q, H H Guo, Chengjie Xiong, Yangtao Xue, Xiaoguang Li, Yuanming Li, Gao Y, Mengyu Hong, Junjie Xu, Shan-Wen Chen, Pengyuan Wang
- Source: openalex
- Venue type: journal
- Journal: Nature Communications
- Publication status: published
- Publication date: 2026-07-09
- DOI: https://doi.org/10.1038/s41467-026-74411-3
- Categories: Cancer Genomics and Diagnostics, Machine Learning in Bioinformatics, Single-cell and spatial transcriptomics
- Relevance: 2.9007325471302448
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://doi.org/10.1038/s41467-026-74411-3
- PDF: https://www.nature.com/articles/s41467-026-74411-3_reference.pdf
- Local PDF: pdf/2026-07-13_59_Decoding cancer circulating transcriptomic signatures with language models.pdf

Current liquid biopsy methods for multi-cancer detection using plasma cell-free RNA (cfRNA, short RNA fragments circulating in blood that can reflect disease states) typically rely on gene annotations, which can overlook signals from unannotated or repetitive genomic regions. We present GeneLLM, a Transformer-based model that directly processes the nucleotide sequences of human-mapped cfRNA reads to identify cancer-indicative signatures. By bypassing gene-level quantification, the model retains signals from transcriptomic dark matter. The model learns latent pseudo-biomarkers (prototype representations from aggregated cfRNA read embeddings) that serve as discriminative features for cancer classification, rather than corresponding to explicit genomic sequences. Here we show that, in a multi-centre cohort, GeneLLM achieves ROC-AUC values ranging from 0.9250 to 0.9962 across several cancers, while maintaining comparable performance at one-sixth of the typical sequencing depth. These results suggest that sequence-level modelling of plasma cfRNA can capture diagnostically relevant information beyond annotation-dependent approaches, enabling more cost-efficient and scalable cancer screening. Cell-freeRNA (cfRNA) can be a non-invasive and cost-effective biomarker for cancer therapy and clinical outcomes, but its analysis remains challenging. Here, the authors develop GeneLLM, a cfRNA-based large language model that processes raw cfRNA data and allows accurate cancer classification from plasma biopsies.

## 60. FedProxy: Federated Fine-Tuning of LLMs via Proxy SLMs and Heterogeneity-Aware Fusion

- Authors: Tao Fan, Guoqiang Ma, Yuanfeng Song, Lixin Fan, Kai Chen, Qiang Yang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.900343534259634
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.794/
- PDF: https://aclanthology.org/2026.acl-long.794.pdf
- Local PDF: pdf/2026-07-13_60_FedProxy_ Federated Fine-Tuning of LLMs via Proxy SLMs and Heterogeneity-Aware Fusion.pdf

Federated fine-tuning of Large Language Models (LLMs) is obstructed by a trilemma of challenges: protecting LLMs intellectual property (IP), ensuring client privacy, and mitigating performance loss on heterogeneous data. Existing methods like Offsite-Tuning (OT) secure the LLMs IP by having clients train only lightweight adapters, yet our analysis reveals they suffer from a fundamental performance bottleneck, leaving a significant gap compared to centralized training. To bridge this gap, we introduce FedProxy, a new federated adaptation framework. FedProxy replaces weak adapters with a unified, powerful Proxy Small Language Model (SLM), compressed from the proprietary LLM, to serve as a high-fidelity surrogate for collaborative fine-tuning. Our framework systematically resolves the trilemma through a three-stage architecture: (i) Efficient Representation via server-guided compression to create a resource-friendly proxy; (ii) Robust Optimization through an interference-mitigating aggregation strategy to handle data heterogeneity; and (iii) Effortless Fusion via a training-free "plug-in" mechanism to integrate learned knowledge back into the LLM. Experiments show FedProxy significantly outperforms OT methods and approaches centralized performance, establishing a new benchmark for secure and high-performance federated LLM adaptation.
