# Paper Daily Reading - 2026-11-24

## 1. Modeling Human-Like Cognition for Stance Detection: Integrating Intuitive Judgment and Analytical Reasoning

- Authors: Zhaodan Zhang, Jin Zhang, Jiafeng Guo, Xueqi Cheng
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.51693161377308
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.264/
- PDF: https://aclanthology.org/2026.acl-long.264.pdf
- Local PDF: pdf/2026-11-24_01_Modeling Human-Like Cognition for Stance Detection_ Integrating Intuitive Judgment and Analytical Reasoning.pdf

Stance detection aims to identify the attitude expressed in text towards a given target, with applications in public opinion analysis and misinformation mitigation. Despite recent advances in large language models (LLMs), two key challenges remain: (1) spurious correlations between superficial features and stance labels, and (2) lack of cognitive modeling that simulates the transition from intuitive perception to deliberate reasoning. To address these issues, we propose Cognitive-Driven Stance Detection (CDSD), inspired by Kahneman’s Dual-Process Theory. CDSD integrates fast intuitive judgment (System 1) and analytical reasoning (System 2), enhanced by three key modules: attention-based cognitive alignment to compare system focus, uncertainty-aware belief update using Bayesian inference, and self-doubt-triggered counterfactual reasoning for re-evaluation under low consistency or high uncertainty. Experimental results on SEM16, P-Stance, and VAST show that CDSD outperforms state-of-the-art methods across multiple LLMs. Notably, CDSD exhibits strong robustness against textual perturbations such as emotional word removal and rhetorical restructuring. By integrating cognitive theory with NLP, our work provides a promising path toward more reliable and interpretable stance detection systems.

## 2. Multi-lingual Functional Evaluation for Large Language Models

- Authors: Victor Ojewale, Inioluwa Deborah Raji, Suresh Venkatasubramanian
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.5167042688752894
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1731/
- PDF: https://aclanthology.org/2026.findings-acl.1731.pdf
- Local PDF: pdf/2026-11-24_02_Multi-lingual Functional Evaluation for Large Language Models.pdf

Multi-lingual competence in large language models is often evaluated via static data benchmarks such as Belebele, M-MMLU and M-GSM. However, these evaluations often fail to provide an adequate understanding of the practical performance and robustness of models across multi-lingual settings. In response, we create multi-lingual functional benchmarks – Cross-Lingual Grade School Math Symbolic (CL-GSM Symbolic) and Cross-Lingual Instruction-Following Eval (CL-IFEval)– by translating existing functional benchmark templates from English to five additional languages that span the range of resources available for NLP: French, Spanish, Hindi, Arabic and Yoruba. Our results show that the gap between static and functional evaluations is highly uneven: across models, performance drops from M-GSM to CL-GSM Symbolic by 24%, 17%, and 18% in English, French, and Spanish, while the drop from Belebele to CL-IFEval ranges from 15% to 24% across languages, and the drop from M-MMLU to CL-IFEval is much smaller (0.5% to 3%).Similarly, we find that model robustness across languages varies significantly, with certain languages (eg. Arabic, English) being the most consistently well performing across evaluation iterations.

## 3. TravelBehaviorQA: A Benchmark Dataset for Behavioral Interpretation of GPS Trajectories

- Authors: Dongyang Zhen, Niping Duan, Huan Zhou, Qingbin Cui
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.5137320811441843
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1604/
- PDF: https://aclanthology.org/2026.findings-acl.1604.pdf
- Local PDF: pdf/2026-11-24_03_TravelBehaviorQA_ A Benchmark Dataset for Behavioral Interpretation of GPS Trajectories.pdf

GPS trajectories encode rich behavioral information about how people move, organize activities, and form daily routines. Recent advances in large language models (LLMs) raise a natural question: can such models infer and summarize travel behavior directly from mobility traces? This paper introduces TravelBehaviorQA, a large-scale benchmark dataset that reframes trajectory analysis as a language-based behavioral understanding task. The dataset links raw GPS trajectories with human-grounded question-answering (QA) pairs that capture travel intensity, temporal structure, activity patterns, mode usage, and behavioral routines. Unlike prior mobility datasets focused on prediction or classification, TravelBehaviorQA emphasizes semantic interpretation through a unified mix of deterministic and open-ended questions. In this benchmark, we construct over 143k QA instances spanning users and years, and evaluate a broad range of state-of-the-art LLMs under controlled settings. Our results reveal substantial gaps between factual extraction and genuine behavioral reasoning, showing that model scale alone is insufficient and that trajectory representation is a primary bottleneck. TravelBehaviorQA exposes critical limitations of current models and establishes a rigorous benchmark for advancing language-based understanding of human mobility behavior.

## 4. Creative Synthesis of Kinematic Mechanisms

- Authors: Lin, Jiong, Ning, Jialong, Goldfeder, Judah, Lipson, Hod
- Source: neurips
- Venue type: conference
- Journal: NeurIPS 2025
- Publication status: formally_published
- Publication date: 2026-08-14
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.513456022172627
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://proceedings.neurips.cc/paper_files/paper/2025/hash/adc67a34eb47147e37229543df7b5b26-Abstract-Creative_AI_Track.html
- PDF: https://proceedings.neurips.cc/paper_files/paper/2025/file/adc67a34eb47147e37229543df7b5b26-Paper-Creative_AI_Track.pdf
- Local PDF: pdf/2026-11-24_04_Creative Synthesis of Kinematic Mechanisms.pdf

In this paper, we formulate the problem of kinematic synthesis for planar linkages as a cross-domain image generation task. We develop a planar linkages dataset using RGB image representations, covering a range of mechanisms: from simple types such as crank-rocker and crank-slider to more complex eight-bar linkages like Jansen’s mechanism. A shared-latent variational autoencoder (VAE) is employed to explore the potential of image generative models for synthesizing unseen motion curves and simulating novel kinematics. By encoding the drawing speed of trajectory points as color gradients, the same architecture also supports kinematic synthesis conditioned on both trajectory shape and velocity profiles. We validate our method on three datasets of increasing complexity: a standard four-bar linkage set, a mixed set of four-bar and crank-slider mechanisms, and a complex set including multi-loop mechanisms. Preliminary results demonstrate the effectiveness of image-based representations for generative mechanical design, showing that mechanisms with revolute and prismatic joints, and potentially cams and gears, can be represented and synthesized within a unified image generation framework.

## 5. XLSR-MamBo: Scaling the Hybrid Mamba-Attention Backbone for Audio Deepfake Detection

- Authors: Kwok-Ho Ng, Tingting Song, Yongdong WU, Zhihua Xia
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.5124427396063815
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1573/
- PDF: https://aclanthology.org/2026.findings-acl.1573.pdf
- Local PDF: pdf/2026-11-24_05_XLSR-MamBo_ Scaling the Hybrid Mamba-Attention Backbone for Audio Deepfake Detection.pdf

Advanced speech synthesis technologies have enabled highly realistic speech generation, posing security risks that motivate research into audio deepfake detection (ADD). While state space models (SSMs) offer linear complexity, pure causal SSMs architectures often struggle with the content-based retrieval required to capture global frequency-domain artifacts. To address this, we explore the scaling properties of hybrid architectures by proposing XLSR-MamBo, a modular framework integrating an XLSR front-end with synergistic Mamba-Attention backbones. We systematically evaluate four topological designs using advanced SSM variants, Mamba, Mamba2, Hydra, and Gated DeltaNet. Experimental results demonstrate that the MamBo-3-Hydra-N3 configuration achieves competitive performance compared to other state-of-the-art systems on the ASVspoof 2021 LA, DF, and In-the-Wild benchmarks. This performance benefits from Hydra’s native bidirectional modeling, which captures holistic temporal dependencies more efficiently than the heuristic dual-branch strategies employed in prior works. Furthermore, evaluations on the DFADD dataset demonstrate robust generalization to unseen diffusion- and flow-matching-based synthesis methods. Crucially, our analysis reveals that scaling backbone depth effectively mitigates the performance variance and instability observed in shallower models. These results demonstrate the hybrid framework’s ability to capture artifacts in spoofed speech signals, providing an effective method for ADD. Codes are publicly available at https://github.com/saki-ciallo/XLSR-MamBo .

## 6. How Do Inpainting Artifacts Propagate to Language?

- Authors: Pratham Yashwante, Davit Abrahamyan, Shresth Grover, Sukruth Rao
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.5123910838067
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-short.60/
- PDF: https://aclanthology.org/2026.acl-short.60.pdf
- Local PDF: pdf/2026-11-24_06_How Do Inpainting Artifacts Propagate to Language.pdf

We study how visual artifacts introduced by diffusion-based inpainting affect language generation in vision-language models. We use a two-stage diagnostic setup in which masked image regions are reconstructed and then provided to captioning models, enabling controlled comparisons between captions generated from original and reconstructed inputs. Across multiple datasets, we analyze the relationship between reconstruction fidelity and downstream caption quality. We observe consistent associations between pixel-level and perceptual reconstruction metrics and both lexical and semantic captioning performance. Additional analysis of intermediate visual representations and attention patterns shows that inpainting artifacts lead to systematic, layer-dependent changes in model behavior. Together, these results provide a practical diagnostic framework for examining how visual reconstruction quality influences language generation in multimodal systems.

## 7. ZARA: Training-Free Motion Time-Series Reasoning via Evidence-Grounded LLM Agents

- Authors: Zechen Li, Baiyu Chen, Hao Xue, Flora D. Salim
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.511498034678655
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.684/
- PDF: https://aclanthology.org/2026.acl-long.684.pdf
- Local PDF: pdf/2026-11-24_07_ZARA_ Training-Free Motion Time-Series Reasoning via Evidence-Grounded LLM Agents.pdf

Motion sensor time-series are central to Human Activity Recognition (HAR), yet conventional approaches are constrained to fixed activity sets and typically require costly parameter retraining to adapt to new behaviors. While Large Language Models (LLMs) offer promising open-set reasoning capabilities, applying them directly to numerical time-series often leads to hallucinations and weak grounding. To address this challenge, we propose ZARA (Zero-training Activity Reasoning Agents), a knowledge- and retrieval-augmented agentic framework for motion time-series reasoning in a training-free inference setting. Rather than relying on black-box projections, ZARA distills reference data into a statistically grounded textual knowledge base that transforms implicit signal patterns into verifiable natural-language priors. Guided by retrieved evidence, ZARA iteratively selects discriminative cues and performs grounded reasoning over candidate activities. Extensive experiments on eight benchmarks show that ZARA generalizes robustly to unseen subjects and across datasets, demonstrating strong transferability across heterogeneous sensor domains. These results mark a step toward trustworthy, plug-and-play motion understanding beyond dataset-specific artifacts. Our code is available at https://github.com/zechenli03/ZARA .

## 8. On the Robustness of Morphosyntactic Transformation with Large Language Models: The Case of Quechua Collao

- Authors: Pool Pocco, Arturo Oncevay
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.509715686903765
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.americasnlp-6.12/
- PDF: https://aclanthology.org/2026.americasnlp-6.12.pdf
- Local PDF: pdf/2026-11-24_08_On the Robustness of Morphosyntactic Transformation with Large Language Models_ The Case of Quechua Collao.pdf

We present a morphosyntactically controlled transformation dataset for Quechua Collao and evaluate large language models on a sentence-level transformation task under varying prompting conditions. Results show that performance depends on the interaction between model behavior, context size, and linguistic complexity, with smaller models benefiting more from additional examples and morphological hints providing selective gains.

## 9. Disentangling the Effects of Unlearning in Measuring Parametric Faithfulness of Chain-of-Thought

- Authors: Ryo Mitsuhashi, Gaku Morio, Ayana Niwa, Masahiro Kaneko, Kentaro Inui, Terufumi Morishita, Yuta Koreeda, Yasuhiro Sogawa
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.509271101130093
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-srw.36/
- PDF: https://aclanthology.org/2026.acl-srw.36.pdf
- Local PDF: pdf/2026-11-24_09_Disentangling the Effects of Unlearning in Measuring Parametric Faithfulness of Chain-of-Thought.pdf

Chain-of-Thought (CoT) in large language models (LLMs) has been widely debated in terms of whether it faithfully reflects an internal reasoning process of models. Parametric faithfulness is a recently proposed metric that uses unlearning to assess whether a model encodes parametric beliefs corresponding to a reasoning chain. This paper refines this metric by accounting for the unintended artifacts of unlearning. We introduce control tasks that unlearn irrelevant knowledge and word-shuffled content and show that these control tasks yield substantial parametric faithfulness values, suggesting the non-negligible effect of unlearning. We also found that control tasks help explain the significant variations in parametric faithfulness observed across different model sizes and CoT lengths. We conclude that the effects of unlearning need to be considered when measuring parametric faithfulness.

## 10. MetFuse: Figurative Fusion between Metonymy and Metaphor

- Authors: Saptarshi Ghosh, Tianyu Jiang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.5092549790040195
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.700/
- PDF: https://aclanthology.org/2026.acl-long.700.pdf
- Local PDF: pdf/2026-11-24_10_MetFuse_ Figurative Fusion between Metonymy and Metaphor.pdf

Metonymy and metaphor often co-occur in natural language, yet computational work has studied them largely in isolation. We introduce a framework that transforms a literal sentence into three figurative variants: metonymic, metaphoric, and hybrid. Using this framework, we construct MetFuse, the first dedicated dataset of figurative fusion between metonymy and metaphor, containing 1,000 human-verified meaning-aligned quadruplets totaling 4,000 sentences. Extrinsic experiments on eight existing benchmarks show that augmenting training data with MetFuse consistently improves both metonymy and metaphor classification, with hybrid examples yielding the largest gains on metonymy tasks. Using this dataset, we also analyze how the presence of one figurative type impacts another. Our findings show that both human annotators and large language models better identify metonymy in hybrid sentences than in metonymy-only sentences, demonstrating that the presence of a metaphor makes a metonymic noun more explicit.

## 11. Characterizing and Evaluating Working Emotion Vocabularies in Multilingual Large Language Models

- Authors: Nicholas Deas, Ivan Ernesto Perez Mejia, Ellie Yang, Kathleen McKeown
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.508928660361714
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.2188/
- PDF: https://aclanthology.org/2026.acl-long.2188.pdf
- Local PDF: pdf/2026-11-24_11_Characterizing and Evaluating Working Emotion Vocabularies in Multilingual Large Language Models.pdf

Prior work evaluating emotion and affective understanding in large language models (LLMs) typically rely on predetermined label sets or focus on a singular evaluation task (e.g., emotion detection). We consider affective states, referring to the much broader variety of terms people use to label their emotional experiences. We evaluate multilingual language models’ understanding of affective states in English and Spanish through three different tasks: 1) identification , where models predict an affective state given text, 2) expression , where models generate text expressing a given affective state, and 3) verification , where models report whether a given term refers to an affective state. We show that performance on one task is not necessarily predictive of performance on another. Using these three tasks, we then begin to explore when and why models struggle to understand particular affective states compared to others. We examine systematic patterns in the affective state terms that are well and poorly understood by models, characterizing the working emotion vocabulary of LLMs.

## 12. Challenging the Myth: A Research Arc on LLMs as Human Simulacra

- Authors: Simon Münker, Achim Rettinger, Damian Trilling
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.5088225321355178
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.bigpicture-main.4/
- PDF: https://aclanthology.org/2026.bigpicture-main.4.pdf
- Local PDF: pdf/2026-11-24_12_Challenging the Myth_ A Research Arc on LLMs as Human Simulacra.pdf

When Large Language Models (LLMs) combined with prompt-based approaches as human simulacra emerged, they promised revolutionary shortcuts. Models trained on vast internet corpora may replicate human behavior and communication through text-based alignment. The initial optimism of the NLP community positioned LLMs as universal human proxies capable of replacing participants in surveys, generating authentic social media content, and simulating diverse cultural perspectives. We systematically dismantle this “myth of universal generalization” and document a shift toward methodological rigor. Our research reveals fundamental limitations: LLMs exhibit inhuman response patterns in psychometric assessments and produce detectable synthetic content. We analyze the difference between superficial linguistic fluency and genuine human-like representation, and reframe the current paradigm from asking “can LLMs replace humans?” to “under what validated conditions might LLMs serve as useful research components in social sciences?” Our work shows how interconnected research efforts challenge foundational assumptions and establishes best practices for deploying LLMs as human simulacra.

## 13. Zero-Shot Detection of LLM-Generated Text using Temperature Sensitivity

- Authors: Shixuan Ma, Jiahao Li, Zhendong Mao, Quan Wang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.508817502428262
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1748/
- PDF: https://aclanthology.org/2026.acl-long.1748.pdf
- Local PDF: pdf/2026-11-24_13_Zero-Shot Detection of LLM-Generated Text using Temperature Sensitivity.pdf

The widespread deployment of Large Language Models (LLMs) has spurred significant progress in the detection of LLM-generated text. However, existing detection methods often rely on statistical features that are insufficient for reliable detection; for example, even though LLM-generated and human-written texts exhibit different probability distributions in surrogate models, they can produce nearly identical entropy values, thereby conflating the two types of text. In this paper, we propose that modulating the decoding temperature and monitoring how the probability distributions respond can better probe the intrinsic discrepancies between two types of text. Building upon this insight, we introduce a new feature termed Temperature Sensitivity (TS) and demonstrate that LLM-generated text tends to exhibit higher TS than human-written text. Finally, we propose NTS, a novel and simple zero-shot detector built upon normalized temperature sensitivity. Extensive experiments across three datasets, multiple domains, and various source models demonstrate the superior effectiveness and robustness of our proposed approach. Code avaliable at: https://github.com/Shixuan-Ma/NTS .

## 14. All That Glisters Is Not Gold: A Benchmark for Reference-Free Counterfactual Financial Misinformation Detection

- Authors: Yuechen Jiang, Zhiwei Liu, Yupeng Cao, Yueru He, Ziyang Xu, Chen Xu, Zhiyang Deng, Prayag Tiwari, Xi Chen, Alejandro Lopez-Lira, Jimin Huang, Junichi Tsujii, Sophia Ananiadou
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.508285557742023
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.492/
- PDF: https://aclanthology.org/2026.acl-long.492.pdf
- Local PDF: pdf/2026-11-24_14_All That Glisters Is Not Gold_ A Benchmark for Reference-Free Counterfactual Financial Misinformation Detection.pdf

We introduce RFC-Bench, a benchmark for evaluating large language models on financial misinformation under realistic news. RFC-Bench operates at the paragraph level and captures the contextual complexity of financial news where meaning emerges from dispersed cues. The benchmark defines two complementary tasks: reference-free misinformation detection and comparison-based diagnosis using paired original–perturbed inputs. Experiments reveal a consistent pattern: performance is substantially stronger when comparative context is available, while reference-free settings expose significant weaknesses, including unstable predictions and elevated invalid outputs. These results indicate that current models struggle to maintain coherent belief states without external grounding. By highlighting this gap, RFC-Bench provides a structured testbed for studying reference-free reasoning and advancing more reliable financial misinformation detection in real-world settings.

## 15. MSIA: Adaptive Medical Multimodal Multi-turn Semantic Jailbreak

- Authors: Zhiheng Han, Yao Zhang, Jun Wang, Zhenglu Yang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.5076446529907175
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1096/
- PDF: https://aclanthology.org/2026.findings-acl.1096.pdf
- Local PDF: pdf/2026-11-24_15_MSIA_ Adaptive Medical Multimodal Multi-turn Semantic Jailbreak.pdf

Medical multimodal large language models are increasingly deployed in high-stakes clinical settings, yet current safety evaluations largely overlook a critical failure mode: covert semantic drift that accumulates across clinically plausible multi-turn interactions. Such drift can lead models to gradually exaggerate or conceal critical medical findings without triggering explicit safety mechanisms. We propose MSIA (Medical Semantic Infiltration Attack), a framework for modeling and inducing multi-turn medical semantic jailbreaks in clinical dialogues. MSIA enables the controlled optimization of cumulative semantic drift under stealth constraints through adaptive strategy selection and closed-loop reward feedback grounded in medical evidence. Experiments on chest X-ray–based multimodal medical dialogues show that MSIA consistently outperforms existing jailbreak methods across GPT-4o, Claude, and Gemini, achieving an average attack success rate of 76.67%. These results expose substantial and previously underestimated vulnerabilities of medical LLMs in realistic multi-turn clinical interactions. Code is available here: https://github.com/HeYamo/MSIA .

## 16. Principled Detection of Hallucinations in Large Language Models via Multiple Testing

- Authors: Jiawei Li, Akshayaa Magesh, Venugopal Veeravalli
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.5068848675836106
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1705/
- PDF: https://aclanthology.org/2026.findings-acl.1705.pdf
- Local PDF: pdf/2026-11-24_16_Principled Detection of Hallucinations in Large Language Models via Multiple Testing.pdf

While Large Language Models (LLMs) have emerged as powerful foundational models to solve a variety of tasks, they have also been shown to be prone to hallucinations, i.e., generating responses that sound confident but are actually incorrect or even nonsensical. Existing hallucination detectors propose a wide range of empirical scoring rules, but their performance varies across models and datasets, and it is hard to determine which ones to rely on in practice or to treat as a reliable detector. In this work, we formulate the problem of detecting hallucinations as a hypothesis testing problem and draw parallels with the problem of out-of-distribution detection in machine learning models. We then propose a multiple-testing-inspired method that systematically aggregates multiple evaluation scores via conformal p-values, enabling calibrated detection with controlled false alarm rate. Extensive experiments across diverse models and datasets validate the robustness of our approach against state-of-the-art methods.

## 17. M3TQA: Massively Multilingual Multitask Table Question Answering

- Authors: Daixin Shu, Jian Yang, Zhenhe Wu, Xianjie Wu, Xianfu Cheng, Guan Xiangyuan, Yanghai Wang, Pengfei Wu, Tingyang Yang, Hualei Zhu, Wei Zhang, Ge Zhang, Jiaheng Liu, Zhoujun Li
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.50538402078734
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1134/
- PDF: https://aclanthology.org/2026.findings-acl.1134.pdf
- Local PDF: pdf/2026-11-24_17_M3TQA_ Massively Multilingual Multitask Table Question Answering.pdf

Tabular data is a fundamental component of real-world information systems. However, existing multilingual table benchmarks suffer from geolinguistic imbalance - overrepresenting certain languages and lacking sufficient scale for rigorous cross-lingual analysis. To address these limitations, we introduce M3TQA, which is a comprehensive framework for massively multilingual multitask table question answering, including subsequent datasets M3TQA-BENCH and M3TQA-INSTRUCT, featuring tables expanded to 97 languages from Chinese and English sources. M3TQA-BENCH includes 6,606 professionally annotated question-answering pairs across four tasks designed to evaluate nuanced table reasoning capabilities. Additionally, we synthesized the training set M3TQA-INSTRUCT in 97 languages using Large Language Model (LLM). Experiments on state-of-the-art LLMs reveal critical insights into cross-lingual generalization, demonstrating that synthetically generated, unannotated training data can significantly boost performance, particularly for low-resource languages. M3TQA establishes a new standard for multilingual table understanding, providing both a challenging evaluation platform and a scalable methodology for future research.

## 18. Entropy Ratio Clipping as a Soft Global Constraint for Stable Reinforcement Learning

- Authors: Zhenpeng Su, Leiyu Pan, Minxuan Lv, Tiehua Mei, Zijia Lin, Yuntao Li, Wenping Hu, Ruiming Tang, Kun Gai, Guorui Zhou
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.5053514435271214
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1559/
- PDF: https://aclanthology.org/2026.findings-acl.1559.pdf
- Local PDF: pdf/2026-11-24_18_Entropy Ratio Clipping as a Soft Global Constraint for Stable Reinforcement Learning.pdf

Large language model post-training relies on reinforcement learning to improve model capability and alignment quality. However, the off-policy training paradigm introduces distribution shift, which often pushes the policy beyond the trust region, leading to training instabilities manifested as fluctuations in policy entropy and unstable gradients. Although PPO-Clip mitigates this issue through importance clipping, it still overlooks the global distributional shift of actions. To address these challenges, we propose using the entropy ratio between the current and previous policies as a new global metric that effectively quantifies the relative change in policy exploration throughout updates. Building on this metric, we introduce an Entropy Ratio Clipping (ERC) mechanism that imposes bidirectional constraints on the entropy ratio. This stabilizes policy updates at the global distribution level and compensates for the inability of PPO-clip to regulate probability shifts of un-sampled actions. We integrate ERC into both DAPO and GPPO reinforcement learning algorithms. Experiments across multiple benchmarks show that ERC consistently improves performance.

## 19. Orchestrating Tokens and Sequences: Dynamic Hybrid Policy Optimization for RLVR

- Authors: Zijun Min, Bingshuai Liu, Ante Wang, Long Zhang, Anxiang Zeng, Haibo Zhang, Jinsong Su
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.504953697280583
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1883/
- PDF: https://aclanthology.org/2026.findings-acl.1883.pdf
- Local PDF: pdf/2026-11-24_19_Orchestrating Tokens and Sequences_ Dynamic Hybrid Policy Optimization for RLVR.pdf

Reinforcement Learning with Verifiable Rewards (RLVR) offers a promising framework for optimizing large language models in reasoning tasks. However, existing RLVR algorithms focus on different granularities, and each has complementary strengths and limitations. Group Relative Policy Optimization (GRPO) updates the policy with token-level importance ratios, which preserves fine-grained credit assignment but often suffers from high variance and instability. In contrast, Group Sequence Policy Optimization (GSPO) applies single sequence-level importance ratios across all tokens in a response that better matches sequence-level rewards, but sacrifices token-wise credit assignment. In this paper, we propose Dynamic Hybrid Policy Optimization (DHPO) to bridge GRPO and GSPO within a single clipped surrogate objective. DHPO combines token-level and sequence-level importance ratios using weighting mechanisms. We explore two variants of the mixing mechanism, including an averaged mixing and an entropy-guided mixing. To further stabilize training, we employ a branch-specific clipping strategy that constrains token-level and sequence-level ratios within separate trust regions before mixing, preventing outliers in either branch from dominating the update. Across seven challenging mathematical reasoning benchmarks, experiments on both dense and MoE models from the Qwen3 series show that DHPO consistently outperforms GRPO and GSPO. Our code is publicly available at https://github.com/XMUDeepLIT/DHPO .

## 20. VecInfer: Efficient LLM Inference with Low-Bit KV Cache via Outlier-Suppressed Vector Quantization

- Authors: Dingyu Yao, Chenxu Yang, Zhengyang Tong, Zheng Lin, Wei Liu, Jian Luan, Weiping Wang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.5044574485822837
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1454/
- PDF: https://aclanthology.org/2026.acl-long.1454.pdf
- Local PDF: pdf/2026-11-24_20_VecInfer_ Efficient LLM Inference with Low-Bit KV Cache via Outlier-Suppressed Vector Quantization.pdf

The Key-Value (KV) cache introduces substantial memory overhead during large language model (LLM) inference. Although existing vector quantization (VQ) methods reduce KV cache usage and provide flexible representational capacity across bit-widths, they suffer severe performance degradation at ultra-low bit-widths due to key cache outliers that hinder effective codebook utilization. To address this challenge, we propose VecInfer, a novel VQ method for aggressive KV cache compression while enabling efficient inference. By applying smooth and Hadamard transformations, VecInfer suppresses outliers in the key cache, enabling the codebook to comprehensively cover the original data distribution and thereby reducing quantization difficulty. To facilitate efficient deployment, we design an optimized CUDA kernel that fuses computation with dequantization to minimize memory access overhead. Extensive evaluations demonstrate that VecInfer consistently outperforms existing quantization baselines across both long-context understanding and mathematical reasoning tasks. With only 2-bit quantization, VecInfer achieves performance comparable to full precision, while delivering up to 2.7× speedup in large-batch self-attention computation and 8.3× reduction in single-batch end-to-end latency on Llama-3.1-8B with a 196k sequence length.

## 21. LLM Prompt Duel Optimizer: Efficient Label-Free Prompt Optimization

- Authors: Yuanchen Wu, Saurabh Verma, Justin Lee, Fangzhou Xiong, Poppy Zhang, Amel Awadelkarim, Xu Chen, Yubai Yuan, Shawndra Hill
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.5042054088362993
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.490/
- PDF: https://aclanthology.org/2026.findings-acl.490.pdf
- Local PDF: pdf/2026-11-24_21_LLM Prompt Duel Optimizer_ Efficient Label-Free Prompt Optimization.pdf

Large language models (LLMs) are highly sensitive to prompts, but most automatic prompt optimization (APO) methods assume access to ground-truth references (e.g., labeled validation data) that are costly to obtain. We propose the Prompt Duel Optimizer (PDO), a sample-efficient framework for label-free prompt optimization based on pairwise preference feedback from an LLM judge. PDO casts prompt selection as a dueling-bandit problem and combines (i) Double Thompson Sampling to prioritize informative comparisons under a fixed judge budget, with (ii) top-performer guided mutation to expand the candidate pool while pruning weak prompts. Experiments on BIG-bench Hard (BBH) and MS MARCO show that PDO consistently identifies stronger prompts than label-free baselines, while offering favorable quality–cost trade-offs under constrained comparison budgets.

## 22. PibE-MPP: A Play-it-by-Ear Masking Performance Plug-in for LLMs

- Authors: Mengwei Wang, Simin Niu, Xun Liang, Yuefeng Ma, Sensen Zhang, Jiawei Yang, Shichao Song, Hanyu Wang, Huayi Lai
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.5040913028995524
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.105/
- PDF: https://aclanthology.org/2026.findings-acl.105.pdf
- Local PDF: pdf/2026-11-24_22_PibE-MPP_ A Play-it-by-Ear Masking Performance Plug-in for LLMs.pdf

Treating random masking as a performance plug-in for large language models (LLMs) offers three advantages: low coupling to the task, the model, and training resources. However, the critical drawback is that its gains are highly stochastic. Motivated by this, we propose play-it-by-ear masking performance plug-in (PibE-MPP), which enables LLMs to adaptively select masking target combinations for each task, retaining these advantages and mitigating the drawback. Specifically, we pose two core questions—what are the masking targets and what is the masking strategy under 7 constraints obtained from these advantages and a drawback. For the first question, we select all attention heads in the last layer as masking targets by constructing a first-order Markov process with alternating hidden state and information fusion. The feasibility of this target is validated by random masking experiments. For the second question, we first construct a small yet interpretable candidate set by proposing a three-axis mapping and a mean-based criterion for fusion features of masking targets. We then propose an axis-variance minimization to select a compact masking-target combination, reducing sensitivity to outlier targets. Experiments on 6 LLMs (Qwen and LLaMA) and 24 datasets demonstrate PibE-MPP’s effectiveness and generality, gain stability, and domain performance, and verify the necessity of its final module, providing empirical evidence of its transferability across tasks and models. The code is available at https://github.com/wtctcop/PibE-MPP .

## 23. BIASEDTALES-ML: A Multilingual Dataset for Analyzing Narrative Attribute Distributions in LLM-Generated Stories

- Authors: Yuxuan Ouyang, Yingfeng Luo, JingBo Zhu, Tong Xiao
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.503871375938794
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.862/
- PDF: https://aclanthology.org/2026.findings-acl.862.pdf
- Local PDF: pdf/2026-11-24_23_BIASEDTALES-ML_ A Multilingual Dataset for Analyzing Narrative Attribute Distributions in LLM-Generated Stories.pdf

Large Language Models (LLMs) are increasingly used to generate narrative content, including children’s stories, which play an important role in social and cultural learning. Despite growing interest in AI safety and alignment, most existing evaluations focus primarily on English, leaving the cross-lingual generalization of aligned behavior underexplored. In this work, we introduce BiasedTales-ML, a large-scale parallel corpus of approximately 350,000 children’s stories generated across eight typologically and culturally diverse languages using a full-permutation prompting design. We propose a structured generator-extractor pipeline and a multi-dimensional distributional analysis framework to examine how narrative attributes vary across languages, models, and social conditions.Our analysis reveals substantial cross-lingual variability in narrative generation patterns, indicating that distributions observed in English do not always exhibit similar characteristics in other languages, particularly in lower-resource settings. At the narrative level, we identify recurring structural patterns involving character roles, settings, and thematic emphasis, which manifest differently across linguistic contexts.These findings highlight the limitations of English-centric evaluation for characterizing socially grounded narrative generation in multilingual settings. We release the dataset, code, and an interactive visualization tool to support future research on multilingual narrative analysis and evaluation.

## 24. Unlocking the Potential of Diffusion Language Models through Template Infilling

- Authors: Junhoo Lee, Seungyeon Kim, Nojun Kwak
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.5038284798887034
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.284/
- PDF: https://aclanthology.org/2026.acl-long.284.pdf
- Local PDF: pdf/2026-11-24_24_Unlocking the Potential of Diffusion Language Models through Template Infilling.pdf

Diffusion Language Models (DLMs) have emerged as a promising alternative to Autoregressive Language Models, yet their inference strategies largely rely on prefix-based prompting inherited from the autoregressive paradigm. In this paper, we propose Template Infilling (TI), a conditioning methodology tailored for DLMs. Unlike conventional prefix prompting, TI distributes structural anchors across the target response, establishing a global template before infilling masked segments. This enables structured conditioning that leverages the bidirectional generation process of DLMs. We evaluate TI on diverse benchmarks, including mathematical reasoning, code generation, and trip planning, achieving consistent improvements of 9.40%p over baseline prompting strategies. Furthermore, TI naturally supports multi-token generation settings, providing practical speed advantages while maintaining generation quality and robustness. Overall, our results highlight a DLM-specific conditioning paradigm for structured generation, suggesting a promising direction for inference methods tailored to diffusion-based language models.

## 25. ROSCO-Omni: Multimodal LLM-Based Communication Understanding for Non- and Minimally-Speaking Autistic Individuals

- Authors: Siddhant Bikram Shah, Kristina T. Johnson
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.5035399859061886
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.2011/
- PDF: https://aclanthology.org/2026.findings-acl.2011.pdf
- Local PDF: pdf/2026-11-24_25_ROSCO-Omni_ Multimodal LLM-Based Communication Understanding for Non- and Minimally-Speaking Autistic Individuals.pdf

Approximately 30% of autistic individuals remain non- or minimally-speaking throughout their lives, yet communicate richly through gestures, vocalizations, facial expressions, and augmentative devices. Interpreting this communication is an inherently multimodal task: caregivers rely on the simultaneous integration of visual cues, auditory signals, and contextual understanding to infer intent. Despite this natural alignment with multimodal large language models (MLLMs), research in this intersection remains narrowly focused on diagnosis rather than communication understanding. We address this gap by reframing the problem around two complementary dimensions: communicative actions (the physical modality) and communicative functions (the pragmatic intent). We analyze the ROSCO dataset, containing 2,903 caregiver-annotated video samples from 27 non- and minimally-speaking individuals, with multi-label annotations capturing up to three concurrent actions and two functions per sample across 6 action and 6 function classes. We further propose ROSCO-Omni, a teacher-student distillation framework that generates label-guided instruction data from a high-capability teacher MLLM and uses it to finetune a student MLLM for domain-specialized inference. ROSCO-Omni achieves performance comparable to closed-source models, demonstrating that open-source MLLMs can be adapted to understand communication in this underserved population.

## 26. GSM-Noise: Exploring and Enhancing Large Language Models’ Reasoning under Noisy Inputs

- Authors: Zhengxin Zhang, Chengyu Huang, Xufu Liu, Dan Zhao, Jinyan Su, Claire Cardie
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.5032440760449504
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1748/
- PDF: https://aclanthology.org/2026.findings-acl.1748.pdf
- Local PDF: pdf/2026-11-24_26_GSM-Noise_ Exploring and Enhancing Large Language Models’ Reasoning under Noisy Inputs.pdf

Large language models (LLMs) have demonstrated impressive reasoning capabilities, yet they often struggle when dealing with complex, ill-formed, or noisy inputs that frequently occur in interactions with real users. LLMs typically lack crucial refining capabilities needed to filter out irrelevant details, restructure key points before reasoning over the text and responding, resulting in suboptimal performance and incorrect answers. From an information theory perspective, this behavior is akin to decoding a high-entropy problem without first reducing its entropy. In this work, we first introduce GSM-Noise, a benchmark featuring grade-school math problems systematically perturbed to reflect real-world input variability. We show that the reasoning ability of open-source models (e.g., LLaMA and Qwen series) can be compromised by noise, while closed-source models are more robust. To improve LLM robustness under noisy conditions, we propose that LLMs first refine inputs — thereby reducing their entropy — before engaging in in-depth analysis. We investigate three approaches to instill this refinement capability: prompt engineering (PE), supervised finetuning (SFT), and reinforcement learning (RL). Experimental results show that input refinement leads to consistent performance gains: 2–12% with PE, 4–13% with SFT, and 3–25% with RL. These results highlight the importance of incorporating an explicit refinement phase to enhance the robustness and reliability of LLM reasoning in real-world scenarios.

## 27. Boosting Self-Consistency with Ranking

- Authors: Maria Marina, Daniil Moskovskiy, Sergey Pletenev, Mikhail Salnikov, Alexander Panchenko, Viktor Moskvoretskii
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.502399542153616
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-srw.89/
- PDF: https://aclanthology.org/2026.acl-srw.89.pdf
- Local PDF: pdf/2026-11-24_27_Boosting Self-Consistency with Ranking.pdf

Self-consistency improves large language models by sampling multiple reasoning paths and selecting the most frequent answer, but majority vote often fails to recover correct answers that are already present among samples. In this work, we reformulate answer selection in self-consistency as a ranking problem. Instead of relying on a single uncertainty or confidence signal, we train a lightweight reranker to score candidate answers using five carefully designed features that capture answer-level frequency, semantic centrality, and reasoning-trace consistency. We instantiate this approach with a LambdaRank model and evaluate it on three datasets under a range of test-time budgets. Across datasets, the proposed method consistently achieves a better accuracy-efficiency trade-off than standard self-consistency and strong baselines, with particularly large gains on question answering benchmarks. Further analysis shows that the proposed features are individually useful and, more importantly, complementary, highlighting the value of learning to combine multiple informative signals for test-time answer selection.

## 28. LRBench and Judge-R1: Principled Evaluation and Training of LLM-Based Judges for Long-Context Reasoning

- Authors: Xinyi Zhao, Haoqi Hu, Ziyu Wang, Jinfeng Xiao
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.5018371181900854
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.2029/
- PDF: https://aclanthology.org/2026.findings-acl.2029.pdf
- Local PDF: pdf/2026-11-24_28_LRBench and Judge-R1_ Principled Evaluation and Training of LLM-Based Judges for Long-Context Reasoning.pdf

Large language models (LLMs) are increasingly used as judges to evaluate, rank, and supervise other models, yet their reliability in judging LLMs’ reasoning process under long-context settings remains underexplored. Existing benchmarks either overly rely on human annotators, who may miss subtle flaws in lengthy reasoning chains, or focus solely on final responses while ignoring the underlying context and reasoning process. We introduce Long-Reason Bench (LRBench), a large-scale benchmark for evaluating LLM-based judges. LRBench comprises over 100K annotated instances spanning medical, legal, and academic-review scenarios, with fine-grained labels indicating violations of six core principles: Logical Correctness, Factual Consistency, Bias and Fairness, Groundedness, Helpfulness, and Harmlessness. Experimental results reveal that state-of-the-art LLM judges struggle to identify nuanced reasoning errors in long contexts. To improve judge reliability, we further present Judge-R1, which combines reinforcement learning with multi-turn search to enable grounded and principle-aware evaluation. Across domains and principles, Judge-R1 consistently outperforms single-turn baselines, enabling scalable and trustworthy evaluation of LLM reasoning. Our dataset and code are available at https://github.com/Xinyi-0724/Judge-R1 .

## 29. Preconditioned Test-Time Adaptation for Out-of-Distribution Debiasing in Narrative Generation

- Authors: Hanwen Shen, Ting Ying, Jiajie Lu, Shanshan Wang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.5010194094292366
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.919/
- PDF: https://aclanthology.org/2026.acl-long.919.pdf
- Local PDF: pdf/2026-11-24_29_Preconditioned Test-Time Adaptation for Out-of-Distribution Debiasing in Narrative Generation.pdf

Although debiased large language models (LLMs) excel at handling known or low-bias prompts, they often fail on unfamiliar and high-bias prompts. We demonstrate via out-of-distribution (OOD) detection that these high-bias prompts cause a distribution shift, degrading static model performance. To enable real-time correction, we propose CAP-TTA, a test-time adaptation framework. CAP-TTA triggers context-aware LoRA updates only when a bias-risk score exceeds a set threshold. By utilizing an offline precomputed diagonal preconditioner, it ensures fast and stable optimization. Across multiple benchmarks and human evaluations, CAP-TTA effectively reduces toxicity/bias score with significantly lower latency than standard optimization methods (e.g., AdamW or SGD). Furthermore, it prevents catastrophic forgetting, and substantially improves narrative fluency over state-of-the-art baselines without compromising debiasing performance.

## 30. Understanding New-Knowledge-Induced Factual Hallucinations in LLMs: Analysis and Interpretation

- Authors: Renfei Dang, Peng Hu, Zhejian Lai, Changjiang Gao, Min Zhang, Shujian Huang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.500796221237604
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.358/
- PDF: https://aclanthology.org/2026.findings-acl.358.pdf
- Local PDF: pdf/2026-11-24_30_Understanding New-Knowledge-Induced Factual Hallucinations in LLMs_ Analysis and Interpretation.pdf

Prior works have shown that fine-tuning on new knowledge can induce factual hallucinations in large language models (LLMs), leading to incorrect outputs when evaluated on previously known information. However, the specific manifestations of such hallucination and its underlying mechanisms remain insufficiently understood. Our work addresses this gap by designing a controlled dataset Biography-Reasoning, and conducting a fine-grained analysis across multiple knowledge types and two task types, including knowledge question answering (QA) and knowledge reasoning tasks. We find that hallucinations not only severely affect tasks involving newly introduced knowledge, but also propagate to other evaluation tasks. Moreover, when fine-tuning on a dataset in which a specific knowledge type consists entirely of new knowledge, LLMs exhibit elevated hallucination tendencies. This suggests that the degree of unfamiliarity within a particular knowledge type, rather than the overall proportion of new knowledge, is a stronger driver of hallucinations. Through interpretability analysis, we show that learning new knowledge weakens the model’s attention to key entities in the input question, leading to an over-reliance on surrounding context and a higher risk of hallucination. Conversely, reintroducing a small amount of known knowledge during the later stages of training restores attention to key entities and substantially mitigates hallucination behavior. Finally, we demonstrate that disrupted attention patterns can propagate across lexically similar contexts, facilitating the spread of hallucinations beyond the original task.
