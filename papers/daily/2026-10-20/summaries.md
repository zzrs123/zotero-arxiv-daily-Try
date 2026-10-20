# Paper Daily Reading - 2026-10-20

## 1. Path to Prior-Data Fitted Relational Models via Learned Latent Multi-table Representations

- Authors: Mohammad Sadeq Abolhasani, Viswanath Ganapathy
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-16
- DOI: Unavailable
- Categories: cs.LG, cs.AI
- Relevance: 3.327360383663059
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.23073v1
- PDF: https://arxiv.org/pdf/2610.23073v1
- Local PDF: pdf/2026-10-20_01_Path to Prior-Data Fitted Relational Models via Learned Latent Multi-table Representations.pdf

Prior-data fitted networks (PFNs) show that pretraining on large populations of synthetic tasks can enable generalization to unseen datasets with little or no downstream fine-tuning. This paradigm is effective for transformer-based tabular and relational foundation models such as RDB-PFN, but remains largely unexplored for graph-based relational models built on message passing. We pretrain the graph-based relational foundation model Griffin on large collections of synthetic relational databases and ask whether curriculum learning, which benefits transformer-based relational learners, also improves message-passing representations. Rather than fine-tune on downstream tasks, we use the pretrained encoder as a general-purpose relational representation learner and pass its latent representations to a frozen in-context predictor (\ticl{}); no component is trained on the target task. On 16 real-world relational classification tasks, evaluated over five seeds against raw-feature and untrained-encoder baselines, a purely synthetic curriculum that begins with schema-guided data and continues with schema-agnostic data gives the strongest frozen in-context performance\rev{, outperforming real-data-only pretraining and every unordered single-stage mixture of the corpora; when appended after real-data pretraining, it yields the best encoders overall}. These results provide initial evidence that PFN-style synthetic pretraining transfers to graph-based relational foundation models.

## 2. Rethinking User Encoders: Routing Diffusion States for Scenario-Adaptive User Representation

- Authors: Junru Zhang, Jinyong Wen, Bin Dou, Wuliang Huang, Baokun Wang, Yu Cheng, Weiqiang Wang, Cheng Peng
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-14
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 3.2870882900259324
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.22400v1
- PDF: https://arxiv.org/pdf/2610.22400v1
- Local PDF: pdf/2026-10-20_02_Rethinking User Encoders_ Routing Diffusion States for Scenario-Adaptive User Representation.pdf

Existing large language model (LLM)-based user encoders serialize heterogeneous behavioral logs and compress them into static representations through autoregressive (AR) prediction. However, their unidirectional constraint limits bidirectional information flow, hindering cross-modal interactions and the joint preservation of multi-source signals. Consequently, the learned static representations struggle to accommodate the distinct evidence requirements of diverse downstream scenarios. We address these limitations by unlocking the iterative denoising process of diffusion language models (dLLMs) as a multi-granularity reconstruction space. Based on this insight, we propose FINDERS (FactorIzatioN of Diffusion statEs for Routing across Scenarios), a router-equipped dLLM framework comprising four operations: denoise, factorize, route, and compress. Learnable meta-slots organize complementary denoising states into transferable cross-modal semantics and modality-specific behavioral factors. To provide grounded supervision, we construct BehaviorQA, a large-scale corpus containing explicit behavioral rationales. Guided by scenario queries, a lightweight router dynamically emphasizes relevant slot directions via an input-level residual pathway before cross-source fusion and final compression. Extensive experiments and online A/B tests across ten industrial scenarios demonstrate that FINDERS consistently outperforms state-of-the-art methods in both unified and scenario-adaptive settings. This work effectively pushes the boundaries of dLLMs beyond language generation, demonstrating their immense potential as powerful user representation learners.

## 3. Logic-Guided Graph Denoising Diffusion Models

- Authors: Samuel Cognolato, Luciano Serafini, Alessandro Sperduti, Andrea Cavallaro
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-16
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.277392621941997
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.23766v1
- PDF: https://arxiv.org/pdf/2610.23766v1
- Local PDF: pdf/2026-10-20_03_Logic-Guided Graph Denoising Diffusion Models.pdf

Graph diffusion models are competitive approaches for generating complex graph-structured data. However, when such distributions have strict structural constraints, diffusion models may fail to capture them exactly, resulting in the generation of invalid graphs. In this paper, we propose a method for grounding graph diffusion models in domain-specific knowledge via First Order Logic (FOL), leveraging its expressive and interpretable formalism to impose structural constraints on the generative process. We incorporate domain knowledge using classifier guidance, a technique that conditions the diffusion model's distribution on external variables to exert control over the sampled data. During the generative process, classifier guidance steers the denoising trajectory to optimize an objective function, which we define as a fuzzy and differentiable relaxation of the logical rules. Our methodology requires only the specification of constraints in FOL, whose satisfaction is encouraged at inference time to guide a pre-trained generative model. We evaluate our approach by comparing the unconditional generation of knowledge graphs with our logic-guided framework, which incorporates domain ontologies as structural constraints during inference. This approach significantly increases the proportion of generated graphs that satisfy the ontological constraints.

## 4. S-GAP: Stealthy Graph Attack Primitives for Graph Large Language Models

- Authors: Wenda Li, Tongya Zheng, Shunyu Liu, Hanyang Yuan, Kaixuan Chen, Yu Wang, Yuchen Ying, Haoze Jiang, Huan Li, Gang Chen, Zujie Ren
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-16
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 3.2749594581145747
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.23465v1
- PDF: https://arxiv.org/pdf/2610.23465v1
- Local PDF: pdf/2026-10-20_04_S-GAP_ Stealthy Graph Attack Primitives for Graph Large Language Models.pdf

Graph Large Language Models (GraphLLMs) enable powerful semantic understanding and reasoning over Text-Attributed Graphs (TAGs), while their semantic reasoning may exhibit vulnerabilities to perturbations in node text and graph structure under adversarial attack evaluation. Existing attacks typically construct textual and structural perturbations in separate stages guided by distinct realization intents. However, this separation results in attack-intent fragmentation, causing semantic incoherence between the two perturbation types, thereby undermining attack stealth and making them easier for GraphLLMs to identify and disregard, ultimately weakening attack effectiveness. To avoid attack-intent fragmentation, we propose the Graph Attack Primitive (GAP), an atomic semantic representation that unifies textual and structural perturbations under a coherent attack intent. By carefully calibrating the semantic composition of a GAP, we can achieve strong attack effectiveness while maintaining sufficient attack stealth. Furthermore, we introduce S-GAP (Stealthy GAP), a multi-agent framework that iteratively refines the semantic content of the GAP. The framework unifies GAP planning and realization and continuously refines this process through surrogate evaluation and textual feedback. Extensive experiments across four datasets, three GraphLLMs, and two attack settings show that S-GAP improves ASR over the strongest baselines by 7.02% on average while producing more relationally plausible perturbations, exposing critical vulnerabilities in current GraphLLMs and motivating more robust defenses.

## 5. Benchmarking and Enhancing Agentic Causal Discovery

- Authors: Pingchuan Ma, Rui Ding, Shuai Wang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-16
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.2076072028058467
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.22846v1
- PDF: https://arxiv.org/pdf/2610.22846v1
- Local PDF: pdf/2026-10-20_05_Benchmarking and Enhancing Agentic Causal Discovery.pdf

LLM agents can now run causal discovery algorithms on a dataset and report what comes out. Whether they do more than that, such as noticing where an algorithm went wrong and fixing it with further tests, is hard to tell from current benchmarks. Most of them give the variables meaningful names, and an LLM shown only the names of the Tübingen cause-effect pairs already gets 99% of the directions right. With the names removed, the data are usually clean enough that picking a better algorithm than PC closes most of the gap. We introduce Heuresis, a benchmark of anonymous simulated datasets whose mechanisms range from linear Gaussian to heavy-tailed. For each family of datasets it separates what a better existing algorithm can gain from what only a closer look at the data can gain, and it traces every edge an agent changes. Every family leaves a gap that none of the algorithms, the router and the two causal-discovery foundation models we ran can close, so a score above the best chosen algorithm has to come from using the data. We instantiate the benchmark with an agent harness and three LLMs, GPT-6.1 Sol, Claude Opus 5.5 and Qwen 3.8 Flash. GPT-6.1 Sol surpasses the best chosen algorithm on all six families, by 14% adjacency F1 on the most difficult one, and Claude Opus 5.5 does so by 7.4% there. A third of the true edges the two agents restore on the two hardest families appear in no algorithm's output. The code and data will be publicly released to facilitate future work.

## 6. Information Estimation with Discrete Diffusion

- Authors: Alberto Foresti, Giulio Franzese, Pietro Michiardi
- Source: arxiv
- Venue type: preprint
- Journal: International Conference on Learning Representations (ICLR), 2026
- Publication status: preprint
- Publication date: 2026-10-16
- DOI: Unavailable
- Categories: cs.LG, cs.IT
- Relevance: 3.1176777449628057
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.23404v1
- PDF: https://arxiv.org/pdf/2610.23404v1
- Local PDF: pdf/2026-10-20_06_Information Estimation with Discrete Diffusion.pdf

Information-theoretic measures, such as Mutual Information (MI), play a crucial role in understanding non-linear relationships between random variables and are widely used across scientific disciplines. Yet, their use on real-world discrete data remains challenging. Existing methods typically rely on embedding discrete data into a continuous space and apply neural estimators originally designed for continuous distributions. This process requires careful engineering for both the embedding model and estimator architecture, but suffers from issues related to high data dimensionality. In this work, we introduce InfoSEDD, a discrete diffusion-based approach that bridges information-theoretic estimation and generative modeling such that they can be used to compute Kullback-Leibler divergences. Backed by Continuous Time Markov Chains theory principles, the design of InfoSEDD is lightweight and scalable and allows seamless integration with pretrained models. We showcase the versatility of our approach through applications on motif discovery in genetic promoter data, semantic-aware model selection in text summarization, and entropy estimation in Ising models. Finally, we construct consistency tests on real-world textual and genomics data. Our experiments demonstrate that InfoSEDD outperforms alternatives that rely on the "embedding trick". Our results position InfoSEDD as a robust and scalable tool for information-theoretic analysis of discrete data.

## 7. Learning to Be Guided: Shaping Latent Geometry for Classifier-Free Guidance

- Authors: Haoming Liu, Junhao Zhu, Shaoyi Zheng, Yuanhe Guo, Jinnuo Liu, Shenji Wan, Hongyi Wen
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-16
- DOI: Unavailable
- Categories: cs.LG, cs.AI
- Relevance: 3.0861707044424747
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.22885v1
- PDF: https://arxiv.org/pdf/2610.22885v1
- Local PDF: pdf/2026-10-20_07_Learning to Be Guided_ Shaping Latent Geometry for Classifier-Free Guidance.pdf

Classifier-free guidance (CFG) is a standard component of conditional diffusion models, and guided generation performance has become the \textit{de facto} measure of state-of-the-art models. Recent work on latent diffusion models seeks to learn latent spaces that are easier to model with diffusion. However, under CFG, generation additionally depends on how conditions are arranged in the latent space. We study this arrangement under discrete class conditions, termed \emph{class geometry}, and investigate what class geometry allows a latent space to work well with CFG. Under a Gaussian class model, we show that shifting variance from intra- to inter-class at fixed total variance makes classes more distinguishable under noise, and derive a noisy posterior objective whose per-sample descent direction is proportional to the oracle CFG correction. Based on the analysis, we propose Prototype Regularization (PR), a lightweight surrogate for the intractable noisy posterior objective, which applies a cosine prototype classifier to spatially pooled latents. With a controlled training budget (20 epochs for VAE, 80 epochs for DiT), adding PR to an LDM baseline reduces guided gFID on ImageNet from 3.31 to 2.28, surpassing a DINOv3-aligned VA-VAE (2.44) with negligible overhead. We further demonstrate that PR generalizes to pseudo-labels derived from clustering, continuous text-embedding conditions, and video latents. Together, our findings highlight class geometry as a critical factor in guided generation and take a first step toward CFG-compatible representation learning. Our project page is available at: https://maps-research.github.io/cfg-geometry/.

## 8. Normalizing Flow Maps

- Authors: Francesco M. Ruscio, Timothy James Hitge, Fred Zhangzhi Peng, Danyal Rehman, Zander W. Blasingame, Nicholas M. Boffi, Michael M. Bronstein, Alexander Tong, Avishek Joey Bose
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-15
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.0758665551554043
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.22711v1
- PDF: https://arxiv.org/pdf/2610.22711v1
- Local PDF: pdf/2026-10-20_08_Normalizing Flow Maps.pdf

Scalable approaches to learning neural dynamical systems have placed diffusion, flow matching, and few-step generators in flow maps at the forefront of generative modeling. Such state-of-the-art models have limited access to explicit model densities despite evolving from classical generative modeling approaches that leveraged tractable likelihoods, e.g., Normalizing Flows and Autoregressive models. In this paper, we combine these threads of few-step generation and tractable sample likelihoods and introduce Normalizing Flow Maps (NFM), a class of exactly invertible pushforward maps that generalizes normalizing flows and flow maps. More precisely, NFMs learn the integrator of an underlying dynamical system, but crucially, they provide efficient exact likelihood evaluation by construction. To enable scalable training of NFMs, we derive two complementary axes of consistency inherent to NFMs that yield (self) distillation objectives: (1) pointwise matching, which unlocks $\ell_2$-based flow-map style regression losses, and (2) distributional matching, which matches pushforward distributions to the marginals of a prescribed forward process. On conditional image generation on CIFAR-10 and ImageNet-64, NFMs achieve state-of-the-art sample quality among parameter-matched normalizing flows, while supporting likelihood-based RLHF. For equilibrium sampling in Boltzmann Generators, NFMs outperform prior state-of-the-art normalizing flows on both single-system and transferable peptide benchmarks.

## 9. DeDiCa: A Scalable Deconfounding Discrete Causal Generative Model

- Authors: Kunchangtai Liang, Adrián Javaloy, Antonio Vergari, Isabel Valera
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-16
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.0728407502588406
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.23272v1
- PDF: https://arxiv.org/pdf/2610.23272v1
- Local PDF: pdf/2026-10-20_09_DeDiCa_ A Scalable Deconfounding Discrete Causal Generative Model.pdf

We introduce DeDiCa, a practical framework for efficient causal inference with discrete variables and hidden confounding that revisits classical probabilistic modeling through a tensorized parameterization of causal Bayesian networks, enabling tractable inference. Given a causal graph, DeDiCa is trained once on observational data by maximum likelihood, exactly marginalizing over hidden confounders, and can then estimate any (proxy-)identifiable interventional query. Despite this deliberately simple parameterization, DeDiCa matches state-of-the-art neural causal generative models in ATE estimation, while supporting memory-efficient CPU training and exact interventional inference in milliseconds. Compared with causal foundation models, DeDiCa scales more effectively with additional observational samples and achieves competitive accuracy at substantially lower inference time and memory. DeDiCa provides a tractable, accurate, and scalable approach to causal inference in discrete settings with hidden confounding.

## 10. Data-Efficient Classifier Pretraining Through Diffusion Models

- Authors: Qinyu Li, Yee Whye Teh, Chris Holmes, Joel Jaskari
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-16
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.065394988593532
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.23289v1
- PDF: https://arxiv.org/pdf/2610.23289v1
- Local PDF: pdf/2026-10-20_10_Data-Efficient Classifier Pretraining Through Diffusion Models.pdf

Machine learning with limited data is susceptible to overfitting, especially with modern deep neural networks. Prior to the introduction of AlexNet, reconstruction-based pretraining with auto-encoder and denoising auto-encoder were found to be beneficial, partially due to the limited size of the training sets at the time. Motivated by these traditional approaches, we propose DiffPT, a simple diffusion modeling approach to pretrain a given classifier backbone for limited domain-specific training data. We experiment on time-series data, standard natural-image benchmarks, and medical imaging datasets, and contrast the diffusion approach to a multitude of modern and traditional un/self-supervised methods. While contrastive pretraining performs better on CIFAR-10 and Tiny ImageNet in low-data regimes, DiffPT is particularly effective on medical imaging and time-series tasks, where it outperforms self-supervised baselines across a range of low-data regimes. Our results suggest that DiffPT is a simple and effective approach for data-efficient classifier pretraining on different modalities.

## 11. Graph Serializations for Reasoning LLMs: A Study Across Knowledge Extraction and Structural Reasoning

- Authors: Julien Yu, Mihaela Bornea, Avirup Sil, Katrin Kirchhoff
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-15
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 3.059799527871454
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.22734v1
- PDF: https://arxiv.org/pdf/2610.22734v1
- Local PDF: pdf/2026-10-20_11_Graph Serializations for Reasoning LLMs_ A Study Across Knowledge Extraction and Structural Reasoning.pdf

The way a knowledge graph is serialized as text for inclusion into LLM context can substantially affect downstream LLM performance, with prior work reporting tens of percentage points variations across formats. However, existing studies consider only a limited set of representations and predate frontier reasoning models, which now offer stronger reasoning, instruction-following, and long-context capabilities. We evaluate 15 graph representation formats across nine frontier LLM configurations on ontology-based knowledge extraction and structural graph reasoning tasks. While knowledge extraction is relatively insensitive to different serialization formats, the choice of the optimal format for structural reasoning tasks significantly affects accuracy. We demonstrate that the optimal representation choice depends on model, query, and task and propose to approach graph serialization as a dynamic orchestration decision.

## 12. LEMON: Equivariant Learning over Attention Maps for Zero-Shot Misbehavior Monitoring on New LLMs

- Authors: Guy Bar-Shalom, Mor Geva, Fabrizio Frasca, Haggai Maron
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-15
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 3.0443713173249165
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.22723v1
- PDF: https://arxiv.org/pdf/2610.22723v1
- Local PDF: pdf/2026-10-20_12_LEMON_ Equivariant Learning over Attention Maps for Zero-Shot Misbehavior Monitoring on New LLMs.pdf

Large language models exhibit misbehaviors that hinder deployment in high-stakes settings. One approach to monitor such failures is to use an external LLM as a monitor, but this is prohibitively expensive. A well-known and efficient class of monitors can detect such failures from internal representations (such as activation probes), but are tied to the model they were trained on, requiring costly re-annotation as new LLMs appear. A natural way to avoid this repeated annotation cost is to develop internal-representation based monitors that transfer zero-shot across LLMs. However, such transfer is challenging because internal representations are not naturally aligned across models; in particular, attention maps, known to contain signals of misbehavior, may differ in head function, ordering, and model depth. In this work, we characterize those cross-model attention mismatches as algebraic symmetries and use geometric deep learning principles to build LEMON (Language-model Equivariant MOnitoring Network) an online graph neural network-based monitor, whose predictions are invariant under these symmetries. LEMON processes attention maps token-by-token, as they are produced and outputs a score after every token (or every window of $W$ tokens) at negligible cost. Across 16 LLMs and six datasets, in the zero-shot cross-model setting, LEMON outperforms all baselines on both hallucination and jailbreak monitoring tasks, improving over the strongest by up to 14 ROC-AUC points.

## 13. Causal Discovery beyond Conditional Independence: Identifiability, Algorithms, and Statistical Inference for Directed Acyclic and Cyclic Graphs

- Authors: Yang Ni
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-16
- DOI: Unavailable
- Categories: stat.ME, cs.LG, stat.ML
- Relevance: 3.035423130371174
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.23543v1
- PDF: https://arxiv.org/pdf/2610.23543v1
- Local PDF: pdf/2026-10-20_13_Causal Discovery beyond Conditional Independence_ Identifiability, Algorithms, and Statistical Inference for Directed Ac.pdf

Learning causal structure from data requires assumptions about mechanisms, noises, observation schemes, and interventions. Historically, causal discovery has relied primarily on conditional independence. This review focuses on modern causal discovery methods that exploit properties of distributions beyond conditional independence. Our organizing principle separates the source of identification from the statistical estimator and its computational implementation. This perspective connects conditional-independence methods with distributional asymmetries, conditional-moment restrictions, and variation across environments or individuals. We examine discovery under latent confounding and feedback, distinguishing causal information about observed variables from reconstruction of latent structure and emphasizing the additional semantics required by cyclic models. We also distinguish population identification, frequentist and Bayesian consistency, uncertainty quantification, and algorithmic guarantees. Throughout, examples show why the same observational distribution can support different conclusions under different model classes. We conclude with guidance for comparing methods at their identifiable targets and a research agenda for uncertainty, heterogeneous populations, non-scalar variables, and the intersection of discrete data, feedback, and hidden confounding.

## 14. Self-Reflective Chain-of-Thought (SRCoT): Evidence-Based Text Generation via a Closed-Loop Retrieve--Reflect--Revise Pipeline on Edge LLMs

- Authors: Fabian Broszio, Michael Hoffmann, Adrian Paschke
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-16
- DOI: Unavailable
- Categories: cs.AI, cs.CL
- Relevance: 3.023933049279006
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.23311v1
- PDF: https://arxiv.org/pdf/2610.23311v1
- Local PDF: pdf/2026-10-20_14_Self-Reflective Chain-of-Thought (SRCoT)_ Evidence-Based Text Generation via a Closed-Loop Retrieve--Reflect--Revise Pip.pdf

Large language models (LLMs) can generate fluent outputs that lack source support or conflict with local operational constraints. We introduce Self-Reflective Chain-of-Thought (SRCoT), a modular architecture that organizes generation as a closed Retrieve--Reflect--Revise loop. SRCoT separates environment state, persistent knowledge, accumulated experience, and short-term memory into provenance-labeled stores. BM25 retrieval supplies local context; subsequent passes expose intermediate drafts, missing-information markers, follow-up queries, and optional claim--evidence mappings. These artifacts inform retrieval, revision, clarification, or abstention decisions. We examine the architecture through qualitative, trace-based case studies in two fully synthetic settings: emergency medical services and Munich-Sim, an emergency-operations simulation. Local prototype runs on an Apple M4-family laptop with 128 GB memory illustrate source-labeled documentation, explicit gap marking, and structured dispatch-style outputs. The traces also reveal provenance-assignment errors, incomplete evidence coverage, and unsafe assumptions that remain possible despite prompting constraints. These cases demonstrate report-level inspectability and local execution, not comparative superiority, hallucination reduction, clinical validity, or operational safety. The architecture separates retrieval and control from the model interface, but behavior across different models remains to be evaluated. SRCoT is a research proof of concept requiring human review, with its principal contribution lying in an inspectable control procedure rather than a new model.

## 15. Blitz: Accelerating the Diffusion Modules of AlphaFold3 and Boltz-2

- Authors: Vinay Saji Mathew, Soundar Kumara, Gretta Kellogg, William K. M. Lai
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-16
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.0202208836466338
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.23703v1
- PDF: https://arxiv.org/pdf/2610.23703v1
- Local PDF: pdf/2026-10-20_15_Blitz_ Accelerating the Diffusion Modules of AlphaFold3 and Boltz-2.pdf

Diffusion-based protein structure prediction models produce all-atom structures in about 200 denoising steps, and that cost has driven a number of few-step samplers. We present Blitz, a few-step distillation framework that uses a geometric noise schedule to distribute steps more evenly across noise scales, then learns those updates through multistep consistency training. Physical steering and target-free candidate selection help reduce the remaining geometric defects at inference. We apply Blitz to AlphaFold 3 and Boltz-2, reducing denoising from 200 steps to eight. Because published few-step results use different benchmarks and scoring procedures, we compare both distilled models with their teachers and other few-step methods under a common evaluation protocol covering structural accuracy, interface quality, ligand placement, and stereochemical validity. Blitz retains teacher-level structural accuracy, with AF3-Blitz outperforming all evaluated few-step baselines and exceeding its teacher on several accuracy metrics.

## 16. Designing for Imperfect Prompts: A Simulation-Based Evaluation of an LLM-Based Enterprise Data Assistant Using Knowledge Graphs

- Authors: Niklas Wagner, Alexander Mädche
- Source: arxiv
- Venue type: preprint
- Journal: Proceedings of the 34th European Conference on Information Systems (ECIS 2026), 5
- Publication status: preprint
- Publication date: 2026-10-16
- DOI: Unavailable
- Categories: cs.HC, cs.AI, cs.DB
- Relevance: 2.996981356720334
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.23304v1
- PDF: https://arxiv.org/pdf/2610.23304v1
- Local PDF: pdf/2026-10-20_16_Designing for Imperfect Prompts_ A Simulation-Based Evaluation of an LLM-Based Enterprise Data Assistant Using Knowledge.pdf

Enterprise data assistants using large language models (LLMs) promise democratized data access in organizations. Yet in our real-world deployment within the CFO unit's data lake at an industry partner, we observed that business users frequently pose imperfect prompts that include domain-specific vocabulary and lack schema references or structural information. This Design Science Research study examines automatic resolution using a semantic mediation layer. We design and evaluate two design variants: schema-based mediation via semantic similarity, and knowledge graph-based mediation leveraging an automatically constructed knowledge graph from the data lake. Our simulation-based evaluation using real-world data, supported by LLM-as-a-Judge assessments and human validation, shows that knowledge graph-based mediation outperforms the schema-based approach in Precision, Recall, F1, and preserving user intent. We propose a design principle for knowledge graph-based mediation, demonstrating that structured knowledge representation bridges user intent and database structure and guides the design of enterprise data assistants across skill levels.

## 17. Boundary Detection for High-Dimensional Point Clouds

- Authors: Abigail Hickok, Valerio Galanti, Osama Al Dalahmah, Andrew J. Blumberg
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-16
- DOI: Unavailable
- Categories: cs.LG, cs.CG, stat.ML
- Relevance: 2.979880353480424
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.23590v1
- PDF: https://arxiv.org/pdf/2610.23590v1
- Local PDF: pdf/2026-10-20_17_Boundary Detection for High-Dimensional Point Clouds.pdf

We introduce two new methods for boundary detection in high-dimensional point cloud data, intended to work in situations with non-uniform density, high ambient dimension, and substantial noise. Our first method fits a separating hyperplane on local neighborhoods after doing local dimension reduction---this method works best when one can reliably estimate the intrinsic dimension of the data. Our second method measures the directional uniformity of local neighborhoods, and has the best overall performance on synthetic data. In addition to pointwise numerical boundary scores, our algorithms yield an estimated normal vector at each boundary point. We validate our methodology on synthetic data as well as two real examples: we analyze spatial transcriptomics data, where we show that we can detect the boundary of a tumor, and we also study LLM activation geometry.

## 18. CoLU: Confidence-Weighted Layerwise Unlearning for Large Language Models

- Authors: Jingkai Guo, Ziyi Zhao, Chaitali Chakrabarti, Deliang Fan
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-15
- DOI: Unavailable
- Categories: cs.CL, cs.LG
- Relevance: 2.9433659769470655
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.22721v1
- PDF: https://arxiv.org/pdf/2610.22721v1
- Local PDF: pdf/2026-10-20_18_CoLU_ Confidence-Weighted Layerwise Unlearning for Large Language Models.pdf

Large language model (LLM) unlearning aims to forget certain information while preserving others, without retraining from scratch. SoTA methods such as NPO, SimNPO, and SatImp balance forgetting and retain through whole model fine-tuning, while FOM-UL explores selective layer updates. Prior works show that suppressing target information can damage retained knowledge. This trade-off can vary across layers even under the same unlearning loss. In this work, we propose Confidence-Weighted Layerwise Unlearning (CoLU), which combines a novel confidence-weighted forgetting and retain regularization while updating a single selected transformer layer, rather than the whole model for unlearning. To reduce CoLU compute cost, we further propose Brief Layer Screening (BLS), which uses a newly defined normalized forgetting-retention (NFR) score to first rank layers through a brief unlearning trials using a subset of forgetting dataset and fewer epochs. BLS pre-selects top-k ranked layer candidates, which will then be fully profiled using full data analysis. BLS is proven to reduce the runtime of CoLU by 60.2-79.7% with almost the same performance. On TOFU dataset, CoLU improves both forgetting and retention over NPO, SatImp, and GA-based FOM-UL in all six TOFU settings, and over SimNPO in five of the six settings. On MUSE Books and News datasets, CoLU achieves the highest retained KnowMem and the PrivLeak closest to zero among the compared SOTA unlearning methods. CoLU presents a new record performance in both unlearning and retain in most settings up to date. Moreover, across the measured settings, average CoLU GPU memory usage is 77.4% to 79.5% lower than full-model unlearning.

## 19. Local proxies for memory-efficient training

- Authors: Wu S. Zihan, Brian A. Yuan, Guillaume Bellec
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-16
- DOI: Unavailable
- Categories: cs.LG, cs.AI
- Relevance: 2.9403589624221285
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.23145v1
- PDF: https://arxiv.org/pdf/2610.23145v1
- Local PDF: pdf/2026-10-20_19_Local proxies for memory-efficient training.pdf

Local learning algorithms can reshape resource requirements of artificial intelligence. The memory bottleneck of standard end-to-end backpropagation lies in the need to store all network activations until the loss gradient has been propagated back through. Local learning avoids this, but typically at a cost in accuracy. We study how to achieve accurate and memory efficient local learning in transformers. For each transformer block, we train a local proxy network to predict the global network output via distillation. Gradients can be independently propagated through this local proxy while estimating well the backpropagation gradients. In theory, this approach is exact for deep linear networks; in non-linear residual models, the gradient error can be bounded when using the appropriate residual proxy. We verify this numerically and demonstrate that optimizing the distillation loss improves gradient estimation. Evaluating the performance of proxy propagation on CIFAR-100 in vision transformers, we find that it achieves a better accuracy/memory trade-off compared to other local algorithms. Finally, we show that the method is further relevant for fine-tuning large language models on a small memory budget. Our method trains faster and achieves higher performance than memory-efficient zeroth-order learning algorithms with comparable memory cost.

## 20. Characterising and Analysing Retrieval-Augmented Generation Techniques

- Authors: Emmanuel Igbekele, Olawande Daramola
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-16
- DOI: Unavailable
- Categories: cs.AI, cs.LG
- Relevance: 2.9380889257086507
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.23226v1
- PDF: https://arxiv.org/pdf/2610.23226v1
- Local PDF: pdf/2026-10-20_20_Characterising and Analysing Retrieval-Augmented Generation Techniques.pdf

The advent of Large Language Models (LLMs) across many application domains has increased the need for Retrieval-Augmented Generation (RAG) to reduce hallucinations and improve LLM performance. Thus far, several RAG techniques with impressive features and capabilities have been proposed in the literature, making it a herculean task to select the most appropriate RAG techniques for specific problem scenarios. Thus, we propose a conceptual framework comprising main dimensions and sub-dimensions for characterising (defining "what it is") and analysing (defining "how well it does") existing RAG techniques. The conceptual framework was developed through a qualitative analysis of the attributes of RAG techniques reported in the literature. It can serve as a pre-empirical filtering mechanism for researchers and practitioners in selecting the highest-fit RAG candidates that meet specific user and task requirements before empirical benchmarking of RAG techniques, which can be computationally and financially expensive.

## 21. Sep-Latent: Separator Tokens as Natural Compression Anchors for Implicit Reasoning

- Authors: Yinlong Xu, Jianfeng Huang, Zhengdong Zhou, Mingjie Lin, Fuyu Lv, Dan Ou, Hongxia Xu, Jian Wu
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-16
- DOI: Unavailable
- Categories: cs.AI, cs.CL
- Relevance: 2.923779413041141
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.22924v1
- PDF: https://arxiv.org/pdf/2610.22924v1
- Local PDF: pdf/2026-10-20_21_Sep-Latent_ Separator Tokens as Natural Compression Anchors for Implicit Reasoning.pdf

Large Language Models (LLMs) have demonstrated remarkable success in complex reasoning through explicit Chain-of-Thought (CoT), but the associated computational overhead and token verbosity remain significant barriers to efficiency. While implicit reasoning in continuous latent spaces offers a promising alternative, existing methods like Coconut and CODI often rely on fixed-length latent sequences and suffer from representational collapse. In this paper, we propose Sep-Latent, an adaptive implicit reasoning framework that utilizes separator tokens as structural semantic anchors. By introducing an Attention-Decay mechanism, we force the model to aggregate and compress reasoning logic into these anchors during training. We then align explicit and implicit pathways through multi-level distillation across all layers to ensure logical consistency. Crucially, Sep-Latent enables dynamic reasoning depth by adaptively terminating the latent thinking phase based on query complexity. Experimental results on the GSM8k-Aug benchmark show that Sep-Latent achieves an accuracy of 56.8\% with an average of only 5.4 tokens, significantly outperforming prior fixed-length implicit models in efficiency while narrowing the performance gap with explicit CoT. Further analysis via PCA and symbolic variant testing confirms that our method ensures semantic grounding and exhibits superior robustness to perturbations.

## 22. CoTA++: Understanding the Repeat Curse in dMLLMs from an Information Flow Perspective

- Authors: Qiyan Zhao, Xiaofeng Zhang, Xu-Yao Zhang, Shijie Han, Zhepeng Li, Shunzhi Zhu, Da-Han Wang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-16
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 2.918732648594436
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.23290v1
- PDF: https://arxiv.org/pdf/2610.23290v1
- Local PDF: pdf/2026-10-20_22_CoTA++_ Understanding the Repeat Curse in dMLLMs from an Information Flow Perspective.pdf

Diffusion-based multimodal large language models (dMLLMs) decode by iterative denoising with bidirectional attention, which precludes the standard autoregressive key--value cache. Practical deployments therefore rely on approximate caching that reuses intermediate states across denoising steps. Such caching, however, often makes a response repeat one token at adjacent positions in a run that breaks the sentence, a failure we term the \emph{Repeat Curse}. Tracing the context-token information flow reveals three disruptions. Within a step, caching disperses the attention that anchors a position on nearby context tokens. Across steps, similarity-based refresh is not staleness-aware, so some positions are decoded against stale key--value states. Across layers, the deep-layer entropy of the context fails to converge where repetition arises. We accordingly propose CoTA++, a training-free, plug-and-play framework that counteracts each disruption where it originates: Context-Token Attention Re-anchoring re-forms the attention routing against the current context, Decode-Aware Refresh reserves part of the cache's refresh budget for the positions about to be committed, and Context-Token Entropy-Guided Voting discounts the confidence of a position by the deep-layer entropy of its context, which reorders the unmasking. The three components act at non-overlapping stages of a decoding step and compose freely with existing dMLLMs and caches. Across three dMLLMs and two caching backends, CoTA++ reduces the sample repetition rate of long responses from up to 99.6\% to at most 17.0\%, recovers most of the accuracy lost to caching on nine benchmarks, and keeps the speedup of caching at under 15\% overhead, making approximate caching reliable for dMLLMs.

## 23. Controlling the Diversity-Quality Trade-Off of LLMs by Merging Models Before and After Alignment

- Authors: Yasuaki Sumita, Tomoharu Iwata, Toshiyuki Tanaka
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-16
- DOI: Unavailable
- Categories: cs.CL, cs.LG
- Relevance: 2.8931309238573952
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.22999v1
- PDF: https://arxiv.org/pdf/2610.22999v1
- Local PDF: pdf/2026-10-20_23_Controlling the Diversity-Quality Trade-Off of LLMs by Merging Models Before and After Alignment.pdf

Alignment is known to change the output characteristics of large language models (LLMs). Base models tend to generate more diverse outputs, whereas aligned models tend to produce higher-quality outputs. The appropriate balance between the two depends on the task. Existing methods either require costly fine-tuning or, like temperature sampling, mainly improve lexical diversity rather than semantic diversity. We introduce a depth-aware FrankenMerging approach for controlling the diversity--quality trade-off between an aligned model and its base model without additional training. This approach combines the lower layers of an aligned model with the higher layers of its base model based on the hypothesis that lexical diversity is more closely associated with lower layers and semantic diversity with higher layers. Experiments showed that varying the number of layers taken from each model adjusts both diversity and quality. In most cases, the merged models exhibited higher semantic diversity than the aligned model, and at some split positions, they showed higher lexical diversity than both original models. They also demonstrated a better diversity--quality trade-off than temperature sampling in most settings. A supporting ablation, in which we reversed the merging order, yielded results largely consistent with the hypothesis.

## 24. On the SPOT: Enhancing Speculative Decoding for Diffusion Language Models via Commit-Order Prediction

- Authors: Eliezer Shlomi, Eliron Rahimi, Avi Mendelson, Chaim Baskin
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-15
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 2.881168679821383
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.22543v1
- PDF: https://arxiv.org/pdf/2610.22543v1
- Local PDF: pdf/2026-10-20_24_On the SPOT_ Enhancing Speculative Decoding for Diffusion Language Models via Commit-Order Prediction.pdf

Diffusion language models (DLMs) promise parallel text generation, but in practice face an unresolved speed-quality trade-off. Exact decoding fills in only one masked position per model pass, while faster multi-token decoding schemes are lossy. Speculative decoding is the standard lossless acceleration for autoregressive models. However, it does not transfer directly to DLMs, which must choose both what to generate and where. We show that this order is the missing piece: the model's own predictions from the previous pass already give the right token at 92-100% of positions, but not which position comes next. Based on this observation, we introduce Speculating Positions Order Trajectory (SPOT), which learns to predict this order. A 0.62M-parameter model reads only the target's output distributions and proposes a tree of candidate continuations, and the target verifies all of them in a single pass by checking whether each equals its own next state. On the verification side, our analysis shows that prior block-diffusion verification approaches either assume $T=0$ or a sequential proposal interface. To support tree-based speculation at any temperature, we propose using coupled-noise match verification for diffusion blocks, following shared-Gumbel-noise coupling approaches. Our comprehensive experiments show that SPOT cuts target passes by up to 6.8x and reaches up to 3.2x the throughput of standard decoding, beating the calibrated and training-free drafting baselines in every task and budget at $T=0$ and $T=1$. In addition, we show that the learned drafter transfers across models, demonstrating successful transfer across six different DLMs. Project page: https://eliezer318.github.io/SPOT-dLLM/

## 25. Acquisition Function-Guided Generation for Bayesian Optimization over Discrete Spaces

- Authors: Tommaso Ancilli, Thomas Wedenig, Henry Moss, Robert Peharz
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-16
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 2.877729562476973
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.22763v1
- PDF: https://arxiv.org/pdf/2610.22763v1
- Local PDF: pdf/2026-10-20_25_Acquisition Function-Guided Generation for Bayesian Optimization over Discrete Spaces.pdf

Bayesian optimization (BO) over discrete spaces is challenging due to missing gradients and the sparsity of valid solutions. Latent-space BO sidesteps both issues by fitting a surrogate in the latent space of a generative model, which however substantially complicates the direct incorporation of domain knowledge that is naturally expressed in the original discrete space. In this work, we instead combine a pretrained generative model with a surrogate defined directly in data space, where inductive biases such as domain-specific kernels can be readily incorporated. Rather than maximizing the acquisition function over the discrete design space, our method samples candidates from the generative model under a distribution tilted by the acquisition function. To recover useful gradients for sampling, we embed this tilted distribution into a diffusion bridge that yields a smooth, posterior-averaged acquisition function. This leads to \emph{acquisition function guided generation} (AFGG), which we instantiate with a categorical diffusion model and an autoregressive normalizing flow. Across a broad suite of molecular benchmarks, the diffusion model variant performs on par with leading BO methods, while the flow model variant outperforms state-of-the-art methods in most cases and remains highly competitive otherwise. Our implementation is available at https://anonymous.4open.science/r/afgg.

## 26. ADT: All-Atom Diffusion Tokenizer for 3D Molecular Structures

- Authors: Xuantuo Huang, Encheng Su, Aoran Wang, Pan Tan, Shengyong Xu, Yizhou Wang, Chen Tang, Shixiang Tang, Mingxiao Li
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-16
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 2.870627455480404
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.23265v1
- PDF: https://arxiv.org/pdf/2610.23265v1
- Local PDF: pdf/2026-10-20_26_ADT_ All-Atom Diffusion Tokenizer for 3D Molecular Structures.pdf

Discrete structural tokenization provides a promising route to autoregressive 3D molecular generation. Yet, existing tokenizers face a trade-off between compact representation and all-atom reconstruction: atom-level tokens preserve atomic details but produce long sequences, while compact residue-level protein tokens typically omit side-chain geometry. To overcome this limitation, we propose All-atom Diffusion Tokenizer (ADT), which decouples token granularity from reconstruction resolution. ADT uses one structural token per atom for small molecules and one token per protein residue that jointly represents backbone and side-chain geometry. To mitigate geometric distortion introduced by quantization, we leverage the generative capacity of diffusion models to recover fine-grained atomic geometry beyond deterministic decoding from discrete tokens. Extensive experiments across small molecules and proteins demonstrate that ADT achieves strong reconstruction from compact discrete representations while enabling high-quality autoregressive generation of both small molecules and all-atom protein structures. These results establish compact structural tokens as an effective discrete interface for all-atom molecular reconstruction and generation.

## 27. DIFFLET: A Fast Inference Engine for Diffusion Transformer Models on AWS Trainium

- Authors: Bin Ma, Min Yu, Vijay Kodamalla, Jialin Liu, Dong Li
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-16
- DOI: Unavailable
- Categories: cs.DC, cs.LG
- Relevance: 2.8697507394493114
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.23047v1
- PDF: https://arxiv.org/pdf/2610.23047v1
- Local PDF: pdf/2026-10-20_27_DIFFLET_ A Fast Inference Engine for Diffusion Transformer Models on AWS Trainium.pdf

On AWS Trainium2, every component of a diffusion model runs as a program compiled ahead of time for fixed shapes, while pipelines differ across models, prompt lengths across requests, and caching decisions across denoising steps. We present Difflet, a serving engine in which five model pipelines share one compilation backend, joint attention is split across cores by attention head, and a host controller decides at each denoising step whether to run the denoiser or reuse its earlier output. A small probe program computes the caching signal on the device and returns one number per step, and a resident model process keeps every program loaded across requests. Across five image and video model families, fused attention accelerates denoiser steps by 1.2-4.3x over the same framework using PyTorch/XLA attention, and at 32.8k visual tokens it is the only attention that compiles. On four of the five models, resident serving is 1.5-3.4x faster than standalone runs that reload weights from a warm file cache for each generation.

## 28. Explore Separately, Adopt Selectively: Execution-Guided Tool Use over Large Tool Libraries

- Authors: Anna Mazhar, Seiji Maekawa, Nikita Bhutani
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-15
- DOI: Unavailable
- Categories: cs.CL, cs.AI
- Relevance: 2.8649922045558918
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.22688v1
- PDF: https://arxiv.org/pdf/2610.22688v1
- Local PDF: pdf/2026-10-20_28_Explore Separately, Adopt Selectively_ Execution-Guided Tool Use over Large Tool Libraries.pdf

Large language model agents must discover relevant tools from large libraries, e.g., thousands of tools, as new needs arise during task execution. When several candidates could satisfy the same need, execution may be required to identify the relevant one. Investigating candidates in a shared trajectory can leave alternatives unexplored or allow failed attempts to influence subsequent reasoning. To address this, we present BRIA (BRanch-Inspect-Adopt), a simple yet effective agent that temporarily isolates candidate investigations in separate branches. Each branch retrieves and executes tools to investigate its candidate; a task agent inspects the resulting execution evidence and adopts only useful results into its continuing trajectory. BRIA retrieves additional tools as new capability needs arise during task execution. We evaluate BRIA on PlanBench-XL and MCP-Atlas using a shared pool of 1897 tools, three language models, and static and adaptive retrieval baselines. Across all settings, BRIA matches or exceeds the strongest retrieval baseline. On MCP-Atlas, it achieves an average claim score of 89.77, compared with 75.40 for MCP-Zero, a gain of 14.37 percentage points. BRIA also lies on the Pareto frontier for task performance and input-token cost.

## 29. Universal Semantic Enhancement for Weakly Supervised Anomaly Detection

- Authors: Siyu Zhou, Yuqin Xie, Hao Yuan, Yingjie Zhou
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-16
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 2.8598863893180617
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.23765v1
- PDF: https://arxiv.org/pdf/2610.23765v1
- Local PDF: pdf/2026-10-20_29_Universal Semantic Enhancement for Weakly Supervised Anomaly Detection.pdf

Weakly supervised anomaly detection on tabular data is an essential task in many label-scarce applications, since tabular data is widely encountered and it is commonly observed in practice that only a limited number of labeled anomalies are available alongside abundant unlabeled samples. Most existing methods try to learn features that capture the inherent distribution patterns in the target domain. However, such features often struggle to provide a complete description of possible abnormal characteristics and are highly susceptible to overfitting the extremely scarce labels. To address this challenge, we propose a weakly supervised anomaly detection method based on universal semantic enhancement for tabular data, which fuses the universal knowledge from a pre-trained tabular foundation model with the domain-specific knowledge learned on the target dataset. The two types of knowledge are naturally complementary: universal semantics describe the common patterns of tabular data across domains, while the domain-specific features capture the inherent distributions of normal and anomalous behaviors in the target dataset. A prototype-conditioned modulation mechanism is then designed to effectively integrate the two types of features, allowing them to reinforce each other for improved anomaly detection. Extensive experiments on public datasets show that the proposed method outperforms competitive methods when only eight labeled anomalies are available in the training procedure.

## 30. AgentOnto: Ontology-Guided LLM Agents for Enterprise Data Analytics

- Authors: Dayan Pan, Bincheng Zuo, Xiaojian Wang, Daogang Zhang, Jingyuan Wang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-16
- DOI: Unavailable
- Categories: cs.AI, cs.DB
- Relevance: 2.8498476406018214
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.23317v1
- PDF: https://arxiv.org/pdf/2610.23317v1
- Local PDF: pdf/2026-10-20_30_AgentOnto_ Ontology-Guided LLM Agents for Enterprise Data Analytics.pdf

Enterprise data analysis requires agents to connect analytical requests with knowledge distributed across databases, business documents, and existing example tasks. Without an explicit representation of this knowledge, an agent may produce incorrect analytical results and cannot reliably incorporate feedback. We present AgentOnto, an ontology-guided LLM agent for enterprise data analytics. AgentOnto organizes heterogeneous enterprise knowledge into an ontology that directly guides analysis and incorporates confirmed feedback. Iterative Ontology Preparation further improves the ontology through self-generated analysis tasks. We evaluate AgentOnto on two public data sources. AgentOnto substantially outperforms representative methods, while module-level evaluations confirm the effectiveness of ontology construction, analysis, and updating. A real-world deployment further demonstrates its practical value in enterprise analytics. These results demonstrate that explicitly constructing, using, and updating enterprise knowledge supports reliable and adaptable data analysis.
