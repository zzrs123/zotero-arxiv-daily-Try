# Paper Daily Reading - 2026-09-08

## 1. Dynamic Heterogeneous Graph Representation Learning: A Survey

- Authors: Huan Liu, Pengfei Jiao, Jie Yin, Hongjiang Chen, Zhidong Zhao
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-04
- DOI: Unavailable
- Categories: cs.LG, cs.AI, cs.SI
- Relevance: 3.969350911471048
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.04779v1
- PDF: https://arxiv.org/pdf/2609.04779v1
- Local PDF: pdf/2026-09-08_01_Dynamic Heterogeneous Graph Representation Learning_ A Survey.pdf

Graph representation learning (GRL) serves as a canonical paradigm for modeling complex networks. However, real-world AI systems inherently manifest as evolving heterogeneous entities with complex interactions, posing significant challenges to static or homogeneous modeling. To address these complexities, representation learning for Dynamic Heterogeneous Graphs (DHGs) has emerged as a vital approach for learning low-dimensional representations that simultaneously preserve structural semantics and temporal dynamics. This survey presents the first systematic review of DHG representation learning methods. We first introduce a unified formal definition that encompasses both discrete-time and continuous-time DHGs from the perspective of temporal granularity. Building upon this formulation, we propose a novel algorithm-centric taxonomy that categorizes existing literature, including early embedding-based approaches, graph neural network (GNN)-based models, and relatively recent Transformer-based DHG methods, while explicitly highlighting their intrinsic modeling biases with respect to dynamic granularity. Furthermore, we summarize representative applications of DHG representation learning, along with commonly used datasets and benchmarks. Finally, we discuss promising research directions that guide future advances in this rapidly evolving field.

## 2. Embedded Graph Flows for Categorical Graph Generation

- Authors: Ethan Ma, Zihan Wang, Chris Siu Yeung Chow, Xinguo Feng, Qingqing Li, Rui Jiang, Naipeng Dong, Guangdong Bai
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-04
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.559234973206291
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.05328v1
- PDF: https://arxiv.org/pdf/2609.05328v1
- Local PDF: pdf/2026-09-08_02_Embedded Graph Flows for Categorical Graph Generation.pdf

Generating categorical graphs requires choosing node and edge types that form a coherent structure without depending on node order. Many graph generators encode categories as fixed one-hot vectors, which can impose an artificial geometry in which categories are equidistant. We propose Embedded Graph Flows (EGF), a generative model that learns continuous embeddings for node and unordered-edge categories and transports Gaussian noise towards these learnt endpoints using a permutation-equivariant graph transformer. A terminal readout maps the embeddings back to discrete graph categories. Across molecular benchmarks, EGF achieved competitive performance. On QM9, EGF gives the best result on all four reported metrics among the three methods, including a Fréchet ChemNet Distance (FCD) of 0.150, compared with 0.717 for the categorical-diffusion baseline DiGress and 0.812 for the bridge-based baseline GruM. When applied to larger molecules in ZINC250k, EGF retains the lowest maximum mean discrepancy (MMD) using the neighbourhood subgraph pairwise distance kernel (NSPDK), indicating close agreement with the local substructures of the reference molecules. Our code is available at https://github.com/Trusted-System-Lab/EGF.

## 3. Hakken: Predicting future discoveries to fill the gaps in today's knowledge

- Authors: Tarek R. Besold, Uchenna Akujuobi, Pablo Sanchez, Alessandra Toniato, Kana Maruyama, Jihun Choi, Samy Badreddine, Frederick Gifford, Daniel Evans-Yamamoto, Sucheendra K. Palaniappan, Miquel Ferrer, Kae Nagano, Iris Rossell, Tom Joy, Hatem ElShazly, Chrysa Iliopoulou, Christoph Wehner, Thiviyan Thanapalasingam, Susana Nunes, Pedro G. Cotovio, Peter Wurman, Peter Stone, Hiroaki Kitano, Michael Spranger
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-03
- DOI: Unavailable
- Categories: cs.LG, cs.AI
- Relevance: 3.409917413663245
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.04494v1
- PDF: https://arxiv.org/pdf/2609.04494v1
- Local PDF: pdf/2026-09-08_03_Hakken_ Predicting future discoveries to fill the gaps in today's knowledge.pdf

We present Hakken, a domain-agnostic prediction and explanation system performing knowledge prediction, i.e., growing scientific knowledge by establishing novel relationships, ones that are not limited to the deductive hull of previous knowledge. Hakken uses a transformer-based prediction model built on temporal sequences of knowledge graphs extracted from vast bodies of research publications, fused with an LLM's semantic knowledge, to predict the presence and define the type of as-yet undocumented relationships between scientific concepts. It then calls a model-agnostic explanation framework to provide accompanying information for each prediction that allows scientists to evaluate the suggested new relationship. While general purpose, we demonstrate Hakken's practical capabilities by applying it to the biomedical domain. There, Hakken's prediction model establishes a new benchmark for time-aware multi-label relation prediction, and we show that the model's output stays coherent and informative over extended time spans in historic data. In addition, we scored 1.5 million above-confidence-threshold hypotheses related to aging, qualitatively validated batches of these predictions with biologists and progressed three of them for empirical validation in wet-lab. Two predictions with potentially significant impact in the context of drug discovery and repurposing were confirmed, introducing previously undocumented interactions between TP53 and BAMBI, and between RAF1 and TNF, to biomedical science.

## 4. VizIt: A multi-view framework for exploring single-cell, spatial, and genetic data online

- Authors: Chenhang Christopher Zhang, Yanqing Lou, Jie Yuan, Mingming Lu, Jacob Parker, Himanshu Chintalapudi, Zechuan Lin, Clemens R. Scherzer, Yuxuan Hu, Ruifeng Hu, Xianjun Dong
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-04
- DOI: Unavailable
- Categories: cs.IR, q-bio.GN
- Relevance: 3.313100941689624
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.04658v1
- PDF: https://arxiv.org/pdf/2609.04658v1
- Local PDF: pdf/2026-09-08_04_VizIt_ A multi-view framework for exploring single-cell, spatial, and genetic data online.pdf

Multi-omic studies increasingly require data to be examined from complementary biological perspectives, yet interactive exploration remains fragmented across modalities and tools. We present VizIt, an open-source framework for multi-view exploration of single-cell and spatial transcriptomic, epigenomic and genetic data. VizIt connects gene-, cell type-, condition-, spatial-, genomic region- and variant-centered views, enabling seamless navigation across biological perspectives. We demonstrate VizIt through the Parkinson's Cell Atlas, a customizable interactive multi-omic resource.

## 5. GRACE: Graph-Grounded Reflective Agent Copilot Engine for Expert-in-the-Loop Knowledge Expansion

- Authors: John Seon Keun Yi, Joshua R. Minot, Dokyun Lee
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-03
- DOI: Unavailable
- Categories: cs.CL, cs.AI
- Relevance: 3.1732183731115553
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.04442v1
- PDF: https://arxiv.org/pdf/2609.04442v1
- Local PDF: pdf/2026-09-08_05_GRACE_ Graph-Grounded Reflective Agent Copilot Engine for Expert-in-the-Loop Knowledge Expansion.pdf

Large language models deployed in high-stakes settings frequently generate plausible but ungrounded claims. Standard retrieval-augmented generation (RAG) pipelines offer limited remedy, since they retrieve isolated passages without tracking cross-document evidence relationships or quantifying uncertainty. We introduce GRACE (Graph-grounded Reflective Agent Copilot Engine), a framework that deconstructs LLM responses into atomic claims and grounds them against trusted knowledge priors within a weighted bipartite graph. Edge weights encode the closeness of each claim to the priors, enabling weighted centrality analysis that classifies claims as Grounded, Refuted, or Boundary. Such classification identifies not just hallucinations but also novel or contested claims at the frontier of the model's knowledge. To efficiently allocate human or agent resources, we formulate a Return on Attention (RoA) objective that defers a claim to expert review only when its priority-weighted uncertainty exceeds the cost of verification. Claims verified by experts are promoted to new evidence anchors, closing a validator-LLM evolutionary loop that expands the knowledge base across iterations. We evaluate GRACE across multiple language models and on datasets spanning both general and domain-specific knowledge. Our results show that our knowledge base serves as a reliable foundation for retrieval that outperforms RAG baselines, and that the RoA framework efficiently selects valuable boundary knowledge for expert verification. These findings demonstrate that graph-structured representations combined with expert-in-the-loop verification can mitigate hallucination at the system level rather than at the generation level. Code available at https://github.com/johnsk95/grace_code

## 6. Diffusion Language Models for Mobile Edge Agentic AI: Foundations, Applications, and Challenges

- Authors: Chenqi Li, Minghui Min, Dusit Niyato, Wei Ni
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-04
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 3.049243314931909
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.04778v1
- PDF: https://arxiv.org/pdf/2609.04778v1
- Local PDF: pdf/2026-09-08_06_Diffusion Language Models for Mobile Edge Agentic AI_ Foundations, Applications, and Challenges.pdf

Diffusion language models (DLMs) offer a non-autoregressive alternative for mobile edge agentic artificial intelligence (AI) by refining tokens through iterative denoising rather than left-to-right decoding. Compared with autoregressive Transformer-based large language models (LLMs), DLMs can update multiple uncertain tokens in parallel and exploit bidirectional context throughout the generation process, enabling more flexible quality-latency trade-offs beyond fixed sequential decoding. These properties are particularly attractive for edge agents, where partial refinement, early exit, and constraint-guided correction can reduce response delay and communication overhead while improving robustness under noisy, incomplete, or dynamic contexts. This survey reviews DLM foundations and analyzes their suitability for edge settings under latency, memory, energy, bandwidth, privacy, and reliability constraints. We cover resource-efficient architectures, training and inference acceleration, compression, edge/cloud deployment, communication-aware serving, Internet of Things (IoT)/wireless applications, and evaluation of DLM-based agents. We further discuss open issues in long-context state management, split inference, trustworthy execution, multimodal grounding, and reproducible benchmarking. The goal is to connect DLM modeling properties, including bidirectionality, parallel refinement, controllability, and quality-latency elasticity, with system-level requirements of future mobile edge intelligence.

## 7. Molecular Déjà Vu: Digit-Level Retrieval of Published Values in Frontier Language Models

- Authors: Matthias Busch, Marius Tacke, Sviatlana V. Lamaka, Mikhail L. Zheludkevich, Christian J. Cyron, Roland C. Aydin, Christian Feiler
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-04
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 3.036829767711123
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.05381v1
- PDF: https://arxiv.org/pdf/2609.05381v1
- Local PDF: pdf/2026-09-08_07_Molecular Déjà Vu_ Digit-Level Retrieval of Published Values in Frontier Language Models.pdf

Large language models (LLMs) are increasingly evaluated on molecular property benchmarks, but accuracy cannot distinguish a model that predicts a property from one that retrieves a published number. We audit 22 frontier models on 12 regression benchmarks for verbatim retrieval and find that it is widespread but relatively benchmark-specific: on five datasets more than $50\%$ of the LLMs show verbatim retrieval, while on the remaining datasets it appears only in isolated cells. We run our experiments at two reasoning levels and find that reasoning changes retrieval. The same experiments, on the same molecules and with the same prompt, are flagged $89\%$ more often at the higher reasoning level than at the lowest one. Finally, we test a way to interrupt retrieval in our most contaminated cases, and find that the strongest models in some cases still recognise a combination of transformed SMILES strings and original labels. Furthermore, suppressing retrieval moves the prediction errors of the different models closer together in relative terms, while their differing use of verbatim retrieval spreads them apart. This indicates that the general predictive capability of an LLM is not determined solely by the amount of memorised values. This work provides an overview of the amount and depth of verbatim retrieval in molecular regression benchmarks using LLMs.

## 8. IPGeoAI: Transformer-Based Geolocation with LLM Semantic Fusion

- Authors: Avinash Kadimisetty, Andy Jinqing Yu, Philip Favaloro, Wenlong Liu, Xiaolu Xiong
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-03
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 3.021999127849634
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.04559v1
- PDF: https://arxiv.org/pdf/2609.04559v1
- Local PDF: pdf/2026-09-08_08_IPGeoAI_ Transformer-Based Geolocation with LLM Semantic Fusion.pdf

Accurate city-level IP Geolocation is an important enabler for the modern digital ecosystem, underpinning services ranging from local content delivery and targeting to digital rights enforcement. However, traditional heuristic and database-driven methods often struggle to resolve the complex, non-linear allocation patterns of modern network infrastructures, particularly within the exploding IPv6 address space and transient mobile networks. In this paper, we introduce IPGeoAI, a novel deep learning model architecture that reframes geolocation from a static lookup problem to a sequential modeling task. Our approach utilizes the Transformer Encoder to capture hierarchical dependencies inherent in IP subnet structures. We propose a method to resolve geographic ambiguity by integrating unstructured semantic context via a Zero-Shot LLM Feature Extraction pipeline. We utilize Large Language Models to transform raw, noisy Autonomous Systems (AS) descriptions into structured, domain-specific metadata (such as 'University' vs. 'ISP' or 'Global' vs. 'Local') via an offline pre-computation process. By fusing these semantic signals into the network via a Multi-Head Cross-Attention module, we bridge the gap between numerical network topology and real-world semantic identity. Extensive offline evaluation on a proprietary dataset spanning 200,000 cities demonstrates that IPGeoAI significantly outperforms a leading external vendor in city-level granularity. By adopting a hierarchical inference strategy that refines coarse-grained country signals, our model achieves a 6% improvement in city-level accuracy while extending coverage to 100% of the traffic. Furthermore, in large-scale online production tests, the model drove a statistically significant +0.35% improvement in our 1st-tier downstream use cases metric.

## 9. GUT: Quantifying and Optimizing the Reasoning Uncertainty of LLMs via Graph Complexity

- Authors: Shuang Liang, Xin-Yu Hu, Xiang-Jun Ou, Shao-Qun Zhang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-04
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 2.9997868403078822
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.05284v1
- PDF: https://arxiv.org/pdf/2609.05284v1
- Local PDF: pdf/2026-09-08_09_GUT_ Quantifying and Optimizing the Reasoning Uncertainty of LLMs via Graph Complexity.pdf

Recent years have witnessed great advances in the reasoning ability of Large Language Models (LLMs). However, the reasoning processes of LLMs often exhibit uncertainty, where LLMs often produce a proliferation of divergent branches at each reasoning step even when fed the same prompting inputs, and certain branches exhibit evidently incredible, even nonsensical, reasoning chains and results. In this paper, we propose the Graph-complexity-based UncerTainty (GUT) method for investigating the reasoning uncertainty of LLMs. The key idea of GUT is to characterize the potential branches of each reasoning chain with a directed acyclic graph, thereby ensuring that all potential branches are comprehensively covered within the graph space. Building upon this recognition, we further build two modules of GUT, that is, a Quantification (GUT-Q) module and an Optimization (GUT-O) module, for quantifying and reducing the reasoning uncertainty of LLMs, respectively. GUT-Q measures LLM reasoning uncertainty by approximating the reasoning space complexity with graph complexity. GUT-O implements uncertainty optimization by treating negative uncertainty as the reward function in reinforcement learning. Experimental results conducted on four LLMs and five datasets validate the effectiveness of GUT.

## 10. LLM-Guided Program Evolution for Circle Packing: Breaking 10 Packomania Records for $28

- Authors: Wes Sander
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-04
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 2.9929990697659177
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.05093v1
- PDF: https://arxiv.org/pdf/2609.05093v1
- Local PDF: pdf/2026-09-08_10_LLM-Guided Program Evolution for Circle Packing_ Breaking 10 Packomania Records for $28.pdf

We present Discovery Loop, a lightweight system that uses a large language model (LLM) to iteratively evolve optimization algorithms. Starting from a simple seed solver, the LLM proposes algorithmic improvements guided by a scoreboard of results and a history of prior ideas. Each candidate is evaluated against an independent verifier; improvements are kept and failures discarded. Applied to the Packomania circle-packing benchmark (csqv: maximize the sum of radii of N variable-radius circles in the unit square), the system improved the best known solutions for 10 values of N in the range 101-114, with gains of 2.4%-5.4% over prior records, all within 15 iterations and at a total LLM cost of $27.72. These results have been independently accepted by Packomania. We describe the method, analyze cost-efficiency dynamics including an adaptive plateau-detection mechanism, and discuss implications for democratizing automated scientific discovery.

## 11. When Genomic Masking Priors Fail to Transfer: Strong Variant Prediction, Weak Functional Generation

- Authors: Susu Hu, Preetam Gattogi, Jens Lehmann, Sahar Vahdati, Stefanie Speidel, Julien Vibert
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-04
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 2.9925664918111474
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.04861v1
- PDF: https://arxiv.org/pdf/2609.04861v1
- Local PDF: pdf/2026-09-08_11_When Genomic Masking Priors Fail to Transfer_ Strong Variant Prediction, Weak Functional Generation.pdf

Bidirectional discrete diffusion model appears naturally suited to genomic modeling because it can reconstruct missing sequence from both flanks. We developed GenDA (Genomic Density-optimized Absorbing Diffusion) under the additional hypothesis that entropy-guided span placement would concentrate reconstruction pressure on compositionally complex regions, improving both downstream variant-effect prediction and functional sequence generation. Our results only partially support this premise. After supervised fine-tuning, the 202M-parameter GenDA model reaches a pooled ClinVar SNV AUROC of 0.774, exceeding a similarly scaled autoregressive model by 0.103. However, a matched random-span variant reaches 0.777, providing no evidence that entropy guidance causes the ClinVar improvement. More unexpectedly, GenDA fails a zero-shot functional inpainting stress test: across promoters, enhancers, exon boundaries, and intron boundaries, it does not consistently outperform a control that shuffles the native gap while exactly preserving 3-mer composition. Failure is already present for 50--500-bp gaps, although enhancer degradation worsens at longer gaps. Diagnostics identify several boundary conditions: entropy measures local sequence complexity rather than functional importance; 1-mer tokenization limits physical context; training spans are capped at 300 bp; and high absolute AlphaGenome fidelity can coexist with negative control-normalized restoration. These results show that strong fine-tuned variant prediction, a plausible corruption prior, and functional generation are distinct claims that require separate validation.

## 12. REFINE: LLM Refinement over Budgeted Text-Attributed Graphs for Personalized Medical Concept Representation

- Authors: Mohsen Nayebi Kerdabadi, Arya Hadizadeh Moghaddam, Dongjie Wang, Zijun Yao
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-03
- DOI: Unavailable
- Categories: cs.LG, cs.AI
- Relevance: 2.98713509758921
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.04415v1
- PDF: https://arxiv.org/pdf/2609.04415v1
- Local PDF: pdf/2026-09-08_12_REFINE_ LLM Refinement over Budgeted Text-Attributed Graphs for Personalized Medical Concept Representation.pdf

Learning rich medical concept representations is essential for EHR prediction. Text-attributed knowledge graphs (TKGs) provide a natural foundation by organizing heterogeneous medical relations together with textual semantics. However, most existing encoders process concepts uniformly across patients, despite the fact that a code's meaning and predictive value depend on patient-specific clinical context and trajectory. Learning patient-personalized concept representations from TKGs introduces two key challenges: (1) deciding how much KG context to incorporate for each observed code, and (2) aligning semantic information with the patient-specific relational structure. We propose REFINE, a KG-aware budgeted LLM graph refinement framework for patient-personalized medical concept encoding. Starting from a global TKG, REFINE constructs patient-specific temporal graphs. A sequential reinforcement learning policy selects a personalized KG expansion budget for each observed code. The resulting patient graph is processed by a heterogeneous GNN to capture relation-aware structural dependencies, while a frozen LLM uses graph-aware soft prompts to semantically refine concept representations. Experiments on MIMIC-III and MIMIC-IV show that REFINE consistently improves diverse EHR backbones, outperforms strong baselines, and demonstrates robust gains across component ablation, KG selection, and data insufficiency.

## 13. Continual Graph Memory for Adaptive Recommendation under Intent Drift

- Authors: Hao Nguyen Ngoc, Tung Nguyen, Nguyen Thi Hanh, Hoang Thai Dinh, Nguyen Xuan Tung
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-04
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 2.951897278917323
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.04651v1
- PDF: https://arxiv.org/pdf/2609.04651v1
- Local PDF: pdf/2026-09-08_13_Continual Graph Memory for Adaptive Recommendation under Intent Drift.pdf

This paper studies adaptive recommendation under intent drift, where feedback from each recommendation outcome can reveal whether the relational evidence used for ranking is useful, missing, or misleading. While Knowledge Graphs (KGs) provide essential semantic structure to handle these shifts, traditional KG-enhanced systems treat the graph as a static retrieval substrate, making it brittle to evolving intents, noisy metadata, and recurring failure patterns. This paper proposes CGM-Rec, a continual graph memory framework for adaptive recommendation. CGM-Rec treats the graph state as a writable memory and maintains two complementary components. Therein, a Semantic Graph Memory is updated conservatively through quality-gated typed operations for storing stable and high-confidence relational knowledge. Meanwhile, an Episodic Lesson Memory acts as a fast reactive memory that learns recent outcomes, failure cases, and corrective hints. During testing, model parameters remain frozen and adaptation occurs only through memory writes. We evaluate CGM-Rec under a frozen-parameter, one-pass reranking protocol, where encoders and prompts remain fixed during testing and adaptation occurs only through memory writes. Experiments across multiple recommendation settings show that CGM-Rec improves over evaluated neural and LLM-based baselines on most metrics. Particularly, under sampled-candidate reranking, CGM-Rec improves HR@1 by up to 29.58% over the strongest LLM baseline on Bundle, and outperforms K-RagRec on metadata-rich ML-100K with HR@5 of 0.5941 versus 0.4746.

## 14. Commonsense Reasoning in Computer Vision: Foundations, Recent Advancements, and Future Directions

- Authors: Bahar Uddin Mahmud, Sumit Barua, Guan Yue Hong, Ajay Gupta, Hexu Liu
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-04
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 2.921426822605296
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.05257v1
- PDF: https://arxiv.org/pdf/2609.05257v1
- Local PDF: pdf/2026-09-08_14_Commonsense Reasoning in Computer Vision_ Foundations, Recent Advancements, and Future Directions.pdf

Commonsense reasoning in computer vision encompasses integrating visual data and contextual knowledge, crucial for enhancing AI's understanding of everyday scenarios. This understanding not only improves machine learning models but also enhances their ability to interact meaningfully with humans and the environment. Unlike CNN-based conventional vision models, which are designed to identify objects within a specific image, incorporating commonsense knowledge enables models to interpret scenes in a more holistic manner, thereby improving their spatial ability to reason about relationships among objects and actions. This integration not only enhances object recognition but also facilitates a deeper understanding of the contextual factors, ultimately leading to more precise predictions and interactions in real-world applications. This paper presents a comprehensive survey of recent developments that integrate commonsense knowledge into computer vision tasks. We systematically review approaches based on knowledge graphs, scene graphs, neuro-symbolic models, and commonsense-augmented transformers. We also outline current limitations related to dataset bias, knowledge incompleteness, and integration challenges. Finally, we highlight prospective research trajectories in cross-modal reasoning, scalable commonsense knowledge injection, and neuro-symbolic hybrid architectures to develop truly intelligent visual systems.

## 15. Recovering molecules from coarse-grained beads: free-energy-conditioned generative backmapping across chemical space

- Authors: Luis Itza Vazquez-Salazar, Tristan Bereau
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-03
- DOI: Unavailable
- Categories: physics.chem-ph, cond-mat.soft, cs.LG, physics.bio-ph
- Relevance: 2.902109841771135
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.04432v1
- PDF: https://arxiv.org/pdf/2609.04432v1
- Local PDF: pdf/2026-09-08_15_Recovering molecules from coarse-grained beads_ free-energy-conditioned generative backmapping across chemical space.pdf

Transferable coarse-grained (CG) force fields compress chemical space: by aggregating atoms into a reduced set of interaction beads, models such as MARTINI reduce the number of distinguishable compounds by roughly three orders of magnitude, making high-throughput screening of thermodynamic properties tractable across soft matter, with drug--membrane permeability as a well-developed example. The compression is lossy and, so far, one-way: a screen returns a combination of beads, with no established route back to the compounds it stands for. Recovering those compounds--compositional backmapping--is a one-to-many inverse map, distinct from the better-studied conformational problem of rebuilding atomic coordinates from a known mapping. Here we formulate compositional backmapping as conditional graph generation by introducing juniper, a discrete denoising diffusion model over molecular graphs conditioned on the octanol--water partition free energy $ΔG_{\mathrm{W} \mapsto \mathrm{O}}$, the principal driver of MARTINI bead type assignment and hence a proxy for bead identity. Trained on molecules of up to 9 heavy atoms mapped onto one or two beads, juniper generates molecules that are 93\% valid and 92\% unique for two-bead targets, and whose $ΔG_{\mathrm{W} \mapsto \mathrm{O}}$ distributions track the target $ΔG^{\mathrm{CG}}_{\mathrm{W} \mapsto \mathrm{O}}$ linearly ($r^{2} \geq 0.96$), departing only in the hydrophobic and hydrophilic tails. Although the model receives no chemical information beyond a single scalar, the functional groups shift systematically with the imposed free energy, from branched hydrocarbons at the apolar end to amides, imides, and isocyanates at the polar end. A bead combination flagged by a CG screen can therefore be turned into candidate molecules for atomistic study or synthesis.

## 16. Beyond Stationarity in Time Series: Discovering Causal Structures and Latent Regimes via Markov Blankets

- Authors: Lei Zan, Charles K. Assaad, Emilie Devijver, Eric Gaussier
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-04
- DOI: Unavailable
- Categories: cs.LG, cs.AI
- Relevance: 2.872098844078146
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.05150v1
- PDF: https://arxiv.org/pdf/2609.05150v1
- Local PDF: pdf/2026-09-08_16_Beyond Stationarity in Time Series_ Discovering Causal Structures and Latent Regimes via Markov Blankets.pdf

This paper introduces Regime-aware Constraint-Based and Noise-Based causal discovery with Markov Blankets (RCBNB-MB), a novel causal discovery algorithm for time series that relaxes the common assumption of a single, time-consistent causal structure. Time series are typically observed at discrete time points and often exhibit regime changes that challenge the assumption of a static causal structure, a limitation in many real-world dynamic systems. To address this challenge, RCBNB-MB identifies latent causal regimes, defined as subsets of time points within which a stable causal structure holds. The algorithm follows an iterative strategy that segments the time series into regimes and discovers the causal graph within each regime. By leveraging the Markov blanket rather than direct parents, RCBNB-MB gains robustness to errors in causal discovery and preserves predictive information. We provide theoretical guarantees for RCBNB-MB's ability to recover both regime transitions and causal graphs under reasonable assumptions. Furthermore, we validate its effectiveness through extensive experiments on simulated datasets with known ground truth and real-world IT monitoring data, where taking into account regime shifts is critical. Empirical results show that RCBNB-MB systematically outperforms baseline approaches in accurately detecting regime changes and their associated causal graphs, positioning it as a robust and versatile framework for non-stationary time series analysis.

## 17. Disentangling Attention in Deep Operator Learning: A Controlled Study of Data-Driven and Physics-Informed Architectures

- Authors: Amar Alem Koric, Qibang Liu, Seid Koric
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-03
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 2.8647307064297003
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.04407v1
- PDF: https://arxiv.org/pdf/2609.04407v1
- Local PDF: pdf/2026-09-08_17_Disentangling Attention in Deep Operator Learning_ A Controlled Study of Data-Driven and Physics-Informed Architectures.pdf

Deep neural operators learn mappings between input functions and complete PDE solution fields, enabling forward evaluations of new problem instances orders of magnitude faster than conventional numerical solvers. Attention mechanisms have recently been introduced into neural operators, but most studies change several architectural components at once, making it difficult to identify what actually improves accuracy. This work presents a controlled and systematic study of five deep operator network (DeepONet) variants with distinct attention mechanisms, trained under both data-driven and physics-informed regimes, to isolate the effects of cross-attention, self-attention, tokenization, and attention depth. We evaluate them on a source-driven transient one-dimensional nonlinear diffusion-reaction equation, a transient one-dimensional viscous Burgers equation with variable initial conditions, and a two-dimensional Poisson heat-conduction problem with heterogeneous source fields. Per-sensor tokenization with cross-attention reduces the mean relative L_2 error of the classical DeepONet in all benchmark-training combinations by factors of 2.4-28.0, while the best attention configurations reach 3.5-32.3. Branch self-attention paired only with dot-product fusion is inconsistent, degrading the one-dimensional problems while helping the more complex two-dimensional source field; added on top of cross-attention it improves all six cases, though by less than cross-attention fusion alone. Global pre-mixing provides no consistent benefit. Increasing cross-attention depth further improves accuracy, but with diminishing returns and a substantially higher cost under physics-informed training. Overall, query-dependent cross-attention is the most reliable mechanism, whereas branch self-attention is most useful for large, spatially complex functional inputs.

## 18. DODR: Deterministic Operator-Driven Reasoning in Latent Space

- Authors: Weicai Huang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-04
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 2.854505032758331
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.04782v1
- PDF: https://arxiv.org/pdf/2609.04782v1
- Local PDF: pdf/2026-09-08_18_DODR_ Deterministic Operator-Driven Reasoning in Latent Space.pdf

Autoregressive (AR) large language models formulate reasoning as token-level probabilistic sampling, which induces three fundamental defects in complex logical reasoning: error accumulation, probability substituting necessity, and the linear-chain information bottleneck. This paper proposes the Deterministic Operator-Driven Reasoning in Latent Space architecture (DODR), which reconstructs reasoning as reasoning-graph computation in a high-dimensional linear-algebraic space. Reasoning states are represented as snapshot vectors whose primitives are semantic units (phrases or sentences) rather than tokens, and each inference step is a deterministic matrix operation with no token sampling. Peirce's three inference types are formalized as three trainable matrix operators: a rank-deficient deduction operator (information collapse), a full-rank induction operator (information expansion), and an abduction operator defined as the Moore-Penrose pseudo-inverse of deduction (information hypothesizing). We prove that the operator set is minimal and complete given Peirce's trichotomy, that no single "super-operator" can realize all three types (a rank obstruction), and that reasoning graphs are Turing-complete with contractive backflow converging by Banach's fixed-point theorem. Experiments on 503 sample records (420 deduplicated samples) across dedicated and end-to-end settings show: deduction loss converges to 1.40e-05; induction achieves 0.9996 generalization coverage with 20/20 hard vetoes on counterexamples; abduction solutions exceed the random baseline by 28x with judgment accuracies of 72.5% (58/80, Wilson 95% CI [61.9%, 81.1%]) and 81.7% (49/60, CI [70.1%, 89.4%]); frozen operators attain 100% (60/60) on unseen cross-domain deduction. The architecture provides a structural zero-hallucination guarantee and a three-layer continual-learning mechanism. All data and code are released.

## 19. Dynamic Adaptation of the LLM Context for Generating Routines with Coupled Semantics

- Authors: Gnaneswar Villuri, Hashmath Shaik, Alex Doboli
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-03
- DOI: Unavailable
- Categories: cs.SE, cs.AI
- Relevance: 2.8396979301798577
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.04570v1
- PDF: https://arxiv.org/pdf/2609.04570v1
- Local PDF: pdf/2026-09-08_19_Dynamic Adaptation of the LLM Context for Generating Routines with Coupled Semantics.pdf

LLM-based code generation fails when correctness depends on execution-dependent coupling: the meaning of one routine is defined by the runtime behavior of another, a relationship that cannot be resolved from textual descriptions alone. This limitation, which we call static binding, is not confined to explicitly coupled problems; it appears to varying degrees whenever correctness depends on joint execution behavior across components, from explicit cross-coupled optimizers to subtler joint constraints in packing, routing, and symbolic search. This paper proposes dynamic context adaptation, a sample-efficient validation-generation loop designed for this setting. A validation agent extracts structured diagnostic information from execution traces, providing gradient-like guidance to a generation agent that proposes multiple candidates per iteration. A knowledge graph derived from the problem description supplies semantic constraints to the generation agent. Simulated annealing selects among candidates to avoid greedy collapse. Our method outperforms zero-shot, Reflexion, and OpenEvolve on seven of eight problems at both 300 and 600 evaluations (p < 0.01), a regime where population-based search has not yet accumulated sufficient diversity to compete. Notably, on the primary motivating problem (cross-coupled optimization), our method also achieves the best score at 1000 evaluations, consistent with the hypothesis that structured execution feedback is most beneficial when correctness depends on runtime coupling. Ablation results confirm that structured execution feedback is the primary driver.

## 20. A Generalizable Feature Extractor for Alzheimer's-Related Brain MRI Tasks

- Authors: Reza Rajabli, D. Louis Collins
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-04
- DOI: Unavailable
- Categories: cs.CV, q-bio.QM
- Relevance: 2.8047725869476214
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.05400v1
- PDF: https://arxiv.org/pdf/2609.05400v1
- Local PDF: pdf/2026-09-08_20_A Generalizable Feature Extractor for Alzheimer's-Related Brain MRI Tasks.pdf

When there is not enough labeled data to properly train deep learning models, transfer learning can help. We still do not fully understand how effective it is in neuroimaging, especially for Alzheimer's disease research. It is also not clear if these transferred models can work on new datasets without being retrained for each specific task. We evaluate whether a compact, supervised pretrained model can serve as a reusable foundation model for downstream neuroimaging tasks. We freeze the 7.18 million weights of a 3D CNN previously trained for brain-age prediction, and adapt it to each task using Low-Rank Adaptation (LoRA), requiring only ~1% additional trainable parameters. We evaluate generalizability in six experiments. Adapting the model to classify cognitively normal versus Dementia on ADNI gave an AUC of 0.964 on held-out folds (Experiment #1). Applying that adapted model unchanged to OASIS-3, with no retraining, gave an AUC of 0.871 (Experiment #2). Reusing its output logit together with age and a cognitive score distinguished stable from progressing MCI with an AUC of 0.828 (Experiment #3). Adapting the same backbone to predict amyloid positivity from structural MRI gave an AUC of 0.804 (Experiment #4). Finally, the same approach estimated ICV-normalized hippocampal and white matter hypointensity volumes directly from the T1w image, with R^2 of 0.80 and 0.91 respectively, tasks normally addressed with much larger U-Net networks (Experiments #5 and #6). A compact model supervised on brain age can therefore serve as a reusable backbone, adapting to each task with ~1% additional parameters and transferring to an unseen cohort without any training. Our findings suggest that a carefully trained brain age model can serve as an effective foundation model for Alzheimer's related tasks, even under strict data constraints.

## 21. Corporate Language Model (CLM): Transforming Tacit and Fragmented Enterprise Knowledge into a Sovereign, Auditable, and Executable Corporate Intelligence Layer

- Authors: Fabricio C. Avini, Guilherme Trez
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-03
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 2.7868899204192275
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.04377v1
- PDF: https://arxiv.org/pdf/2609.04377v1
- Local PDF: pdf/2026-09-08_21_Corporate Language Model (CLM)_ Transforming Tacit and Fragmented Enterprise Knowledge into a Sovereign, Auditable, and.pdf

Enterprise AI deployments fail not from model inadequacy, but because organizations lack a structured substrate encoding how they decide, negotiate, and execute. Generic LLMs carry no firm-specific ontological priors; RAG remains brittle, with no path to executable action; static playbooks encode logic but cannot reason or adapt. This demands an architecture treating tacit-knowledge capture, ontological grounding, sovereign deployment, and auditable actuation as co-designed from the start. This paper introduces the Corporate Language Model (CLM), a framework transforming a firm's structured, unstructured, multimodal, and tacit knowledge into an ontology-grounded enterprise foundation upon which reasoning and governed execution are composed. CLM has five capability planes and four architectural pillars: a Neurosymbolic Mesh coupling generative models with a knowledge graph; a Skill Graph where reusable tactics, personas, objections, and goals are typed and composed; Living Digital Twins modeling functional areas as reasoning surrogates; and a Deep Security Layer enforcing sovereignty, traceability, and human oversight. A Spec-as-Code paradigm bridges grounded intent and executable artifact. CLM is one instantiation of this foundation-centric class. Four contributions follow: CLM is defined as a distinct object of study; the Skill Graph is introduced for compositional explainability by construction; the Wisdom Listener effect is proposed, whereby tacit-capable foundations compound in value with use, connecting to dynamic capabilities and organizational learning; and evidence from a JCI-accredited tertiary hospital in Brazil instantiates three of the six maturity stages under LGPD.

## 22. Unifying ICL, SFT, KL-Regularized RL Through a Bayesian Lens

- Authors: Junxin Fan
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-04
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 2.777046674124804
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.05111v1
- PDF: https://arxiv.org/pdf/2609.05111v1
- Local PDF: pdf/2026-09-08_22_Unifying ICL, SFT, KL-Regularized RL Through a Bayesian Lens.pdf

Large language models are now trained and evaluated under a diverse set of paradigms: supervised fine-tuning (SFT), few-shot in-context learning (ICL), KL-regularized RLHF/RLVR, on-policy distillation (OPD), and test-time reasoning with search and chain-of-thought. These methods are often discussed as fundamentally different, and recent empirical results--such as the mixed impact of few-shot prompting on RL-tuned reasoning models--can appear puzzling. This note develops a Bayesian perspective that puts these procedures on the same footing. At the core is a two-step template: (i) construct a (generalized) Bayes or Gibbs posterior q* over outputs or actions given a context, using a prior/reference model and a utility signal (log-likelihood, reward, or advantage); and (ii) approximate q* by a forward-KL projection onto a parametric family, either in-weights (SFT/RL) or in-context (ICL). Part I formalizes few-shot ICL and SFT as amortized and-weights projections onto the Bayes posterior predictive. Parts II-IV show that KL-regularized RLHF/RLVR, reward-weighted SFT, reward-weighted ICL (RW-ICL), and advantage-weighted SFT (AWSFT) are all instances of forward-KL projection onto posteriors induced by rewards or advantages. We disentangle where these equivalences hold (objectives and first-order updates) and where they do not (source and granularity of the learning signal). Part V sketches implications for modern reasoning pipelines: RLHF/RLVR recipes as "posterior design + projection", why cold-start or supervised warm-up is practically unavoidable for importance-weighted KL projections, and DeepSeek-R1 and o1-style reasoning models as combining test-time Bayesian search with training-time KL amortization.

## 23. Training Large Language Models for Small-Molecule Design with Synthetic Task Scaling

- Authors: Frank Hu, Shriram Chennakesavalu, Zichen Wang, Patricia Suriana, Bodhi Vani, Kirill Shmilovich, Kangway Chuang, Colin Grambow
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-04
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 2.7665036964228022
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.04735v1
- PDF: https://arxiv.org/pdf/2609.04735v1
- Local PDF: pdf/2026-09-08_23_Training Large Language Models for Small-Molecule Design with Synthetic Task Scaling.pdf

Designing viable drug candidates requires searching a combinatorially large and rugged chemical space for molecules that satisfy multiple, often competing, objectives. Large language models (LLMs) provide a useful generative prior for this problem because of their representational capacity, reasoning ability, and flexibility when incorporating information from the external environment. While reinforcement learning from verifiable rewards (RLVR) can be used to improve the capabilities of LLMs, many chemically relevant scoring functions require hours or even days per evaluation, making them prohibitively expensive to use directly during online training. Here, we investigate whether LLMs can learn molecular design strategies from cheaper synthetic tasks that generalize to expensive molecular lead optimization settings. We find that curriculum-based training recipes that gradually incorporate more challenging synthetic design tasks enable strong performance that surpasses that of much larger frontier models on structure-based lead optimization. Our results suggest that scaling post-training using synthetic tasks is an effective strategy for adapting LLMs to high-cost experimental scenarios that are too expensive to directly train on.

## 24. UniMate: One Unified Model to Animate Diverse Skeletons

- Authors: Linzhan Mou, Jiahui Lei, Zhiyang Dou, Chenyue Cai, Chaoyue Song, Adam Finkelstein, Szymon Rusinkiewicz
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-04
- DOI: Unavailable
- Categories: cs.CV, cs.GR, cs.LG
- Relevance: 2.7380997908539895
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2609.05415v1
- PDF: https://arxiv.org/pdf/2609.05415v1
- Local PDF: pdf/2026-09-08_24_UniMate_ One Unified Model to Animate Diverse Skeletons.pdf

Recent advances in automatic rigging now deliver animation-ready 3D assets at scale, yet generating the motion to drive them remains a bottleneck. Existing learned animators are topology-constrained: they rely on category-specific templates or require per-skeleton fine-tuning and reference motions at inference. We present UniMate, a unified foundation model that synthesizes articulated motion for arbitrary skeletons from a rigged 3D asset and a text prompt, with no test-time optimization or per-skeleton retraining. UniMate introduces a topology-aware diffusion transformer, which integrates skeletal topology into attention via three mechanisms: (1) a graph-aware attention bias from pairwise joint relations and geodesic distances; (2) a spectral rotary position embedding generalizing RoPE to arbitrary kinematic trees via the graph Laplacian; and (3) a global topological conditioner attention-pooled from the rest-pose skeleton. We also curate UniML3D, 13,006 motion sequences spanning bipedal, quadrupedal, avian, marine, insectoid, serpentine, and articulated rigid objects with unified canonicalization and text pairing. Trained on this dataset, UniMate outperforms state-of-the-art baselines in quality, generalization, and efficiency, and supports zero-shot cross-topology transfer, in-betweening, expansion, and text-guided editing. Our project page is available at https://linzhanmou.com/unimate/.

## 25. Fairness Evaluation and Inference Level Mitigation in LLMs

- Authors: Afrozah Nadeem, Mark Dras, Usman Naseem
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.7220314579395675
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1452/
- PDF: https://aclanthology.org/2026.findings-acl.1452.pdf
- Local PDF: pdf/2026-09-08_25_Fairness Evaluation and Inference Level Mitigation in LLMs.pdf

Large language models often display undesirable behaviors embedded in their internal representations, undermining fairness, inconsistency drift, amplification of harmful content, and the propagation of unwanted patterns during extended dialogue and conversations. Although training-time or data-centric methods attempt to reduce these effects, they are computationally expensive, irreversible once deployed, and slow to adapt to new conversational contexts. Pruning-based methods provide a flexible and transparent way to reduce bias by adjusting the neurons responsible for certain behaviors. However, most existing approaches are static; once a neuron is removed, the model loses the ability to adapt when the conversation or context changes. To address this, we propose a dynamic, reversible, pruning-based framework that detects context-aware neuron activations and applies adaptive masking to modulate their influence during generation. Our inference-time solution provides fine-grained, memory-aware mitigation with knowledge-preserved, more coherent behavior across multilingual single- and multi-turn dialogues, enabling dynamic fairness control in real-world conversational AI.

## 26. SpecAgent: A Speculative Retrieval and Forecasting Agent for Code Completion

- Authors: George Ma, Anurag Koul, Qi Chen, Yawen Wu, Sachit Kuhar, Yu Yu, Aritra Sengupta, Varun Kumar, Murali Krishna Ramanathan
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.7215378351663606
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.786/
- PDF: https://aclanthology.org/2026.acl-long.786.pdf
- Local PDF: pdf/2026-09-08_26_SpecAgent_ A Speculative Retrieval and Forecasting Agent for Code Completion.pdf

Large Language Models (LLMs) excel at code-related tasks but often struggle in realistic software repositories, where project-specific APIs and cross-file dependencies are crucial. Retrieval-augmented methods mitigate this by injecting repository context at inference time. Low inference time latency budget either affects retrieval quality or the added latency impacts user experience adversely. We address this limitation with SpecAgent, an agent that enhances both latency and code-generation quality by proactively exploring repository files during indexing and constructing speculative context that anticipates future edits in each file. This indexing-time asynchrony allows thorough context computation masking latency and the speculative nature of the context improves code-generation quality. Additionally, we identify the problem of future context leakage in existing benchmarks, which can inflate reported performance. To address this, we construct a synthetic, leakage-free benchmark that enables a more realistic evaluation of our agent against baselines. Experiments show that SpecAgent consistently achieves absolute gains of 9–11% (48–58% relative) compared to the best-performing baselines, while significantly reducing inference latency.

## 27. Personalizing LLMs with Binary Feedback: A Preference-Calibrated Optimization Framework

- Authors: Xilai Ma, Liye Zhao, Weijun Yao, Haibing Di, Wenya Wang, Jing Li
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.720984282262539
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1222/
- PDF: https://aclanthology.org/2026.acl-long.1222.pdf
- Local PDF: pdf/2026-09-08_27_Personalizing LLMs with Binary Feedback_ A Preference-Calibrated Optimization Framework.pdf

Large Language Model (LLM) personalization aims to align model behaviors with individual user preferences.Existing methods often focus on isolated user histories, neglecting the essential role of inter-user differences.We propose C-BPO, a framework that personalizes LLMs via preference-calibrated binary signals.By treating target user data as positive feedback and other users’ data as an auxiliary set of implicit negative signals, C-BPO captures distinct inter-user differences.To mitigate the preference overlap issue, where shared task knowledge is erroneously penalized, we derive an objective grounded in Positive-Unlabeled (PU) learning theory.This approach purifies negative signals by subtracting “positive bias”, ensuring alignment with unique idiosyncrasies without compromising general helpfulness.Empirical experiments across various personalization tasks and backbone LLMs show C-BPO consistently outperforms baselines, demonstrating the efficacy of preference-calibrated binary signals in modeling inter-user differences.

## 28. CLewR: Curriculum Learning with Restarts for Machine Translation Preference Learning

- Authors: Alexandra Dragomir, Florin Brad, Radu Tudor Ionescu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.720699805443489
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1024/
- PDF: https://aclanthology.org/2026.findings-acl.1024.pdf
- Local PDF: pdf/2026-09-08_28_CLewR_ Curriculum Learning with Restarts for Machine Translation Preference Learning.pdf

Large language models (LLMs) have demonstrated competitive performance in zero-shot multilingual machine translation (MT). Some follow-up works further improved MT performance via preference optimization, but they leave a key aspect largely underexplored: the order in which data samples are given during training. We address this topic by integrating curriculum learning into various state-of-the-art preference optimization algorithms to boost MT performance. We introduce a novel curriculum learning strategy with restarts (CLewR), which reiterates easy-to-hard curriculum multiple times during training to effectively mitigate the catastrophic forgetting of easy examples. We demonstrate consistent gains across several model families (Gemma2, Qwen2.5, Llama3.1) and preference optimization techniques. We publicly release our code at https://github.com/alexandra-dragomir/CLewR .

## 29. a1: Steep Test-time Scaling Law via Environment Augmented Generation

- Authors: Lingrui Mei, Shenghua Liu, Yiwei Wang, Baolong Bi, Yuyao Ge, Jun Wan, Yurong Wu, Xueqi Cheng
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.720686826125915
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1240/
- PDF: https://aclanthology.org/2026.findings-acl.1240.pdf
- Local PDF: pdf/2026-09-08_29_a1_ Steep Test-time Scaling Law via Environment Augmented Generation.pdf

Large Language Models (LLMs) have made remarkable breakthroughs in reasoning, yet continue to struggle with hallucinations, logical errors, and inability to self-correct during complex multi-step tasks. Current approaches like chain-of-thought prompting offer limited reasoning capabilities that fail when precise step validation is required. We propose Environment Augmented Generation (EAG), a framework that enhances LLM reasoning through: (1) real-time environmental feedback validating each reasoning step, (2) dynamic branch exploration for investigating alternative solution paths when faced with errors, and (3) experience-based learning from successful reasoning trajectories. Unlike existing methods, EAG enables deliberate backtracking and strategic replanning through tight integration of execution feedback with branching exploration. Our a1-32B model achieves state-of-the-art performance among similar-sized models across all benchmarks, matching larger models like o1 on competition mathematics while outperforming comparable models by up to 24.4 percentage points. Analysis reveals EAG’s distinctive scaling pattern: initial token investment in environment interaction yields substantial long-term performance dividends, with advantages amplifying proportionally to task complexity.

## 30. SMART: Evaluating LLMs’ Mathematical Reasoning via a Human Cognitive Process-Inspired Benchmark

- Authors: Yujie Hou, Mei Wang, Yaoyao Zhong, Ting Zhang, Xuetao Ma, Hua Huang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.720645838097868
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1638/
- PDF: https://aclanthology.org/2026.acl-long.1638.pdf
- Local PDF: pdf/2026-09-08_30_SMART_ Evaluating LLMs’ Mathematical Reasoning via a Human Cognitive Process-Inspired Benchmark.pdf

Large Language Models (LLMs) have achieved remarkable performance across a wide range of mathematical benchmarks. However, concerns remain as to whether these successes reflect genuine reasoning or superficial pattern recognition. Existing evaluation methods, which typically focus either on the final answer or on the intermediate reasoning steps, reduce mathematical reasoning to a shallow input–output mapping, overlooking its inherently multi-stage and multi-dimensional cognitive nature. Inspired by P’olya’s problem-solving theory, we propose SMART, a benchmark that decomposes mathematical problem-solving into four cognitive dimensions: S emantic Understanding, M athematical Reasoning, A rithmetic Computation, and R eflection Refinemen T , and introduces dimension-specific tasks to measure the corresponding cognitive processes of LLMs. We apply SMART to 22 state-of-the-art open- and closed-source LLMs and uncover substantial discrepancies in their capabilities across dimensions. Our findings reveal genuine weaknesses in current models and motivate a new metric, the All-Pass Score, designed to better capture true problem-solving capability.
