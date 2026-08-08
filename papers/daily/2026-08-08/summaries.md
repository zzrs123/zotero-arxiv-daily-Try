# Paper Daily Reading - 2026-08-08

## 1. BioM-JEPA: joint-embedding prediction of graph-connected gene blocks in single cells

- Authors: Yuhao Wang, Zelin Zang, Yuxuan Liu, Zhen Lei, Stan Z. Li
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-06
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.87581631454327
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.05928v1
- PDF: https://arxiv.org/pdf/2608.05928v1
- Local PDF: pdf/2026-08-08_01_BioM-JEPA_ joint-embedding prediction of graph-connected gene blocks in single cells.pdf

Single-cell transcriptomes are sparse observations of coordinated biological programmes, yet most self-supervised models learn by reconstructing individual genes. Here we present BioM-JEPA, a joint-embedding predictive architecture that instead predicts aggregate representations of graph-connected gene blocks defined by protein-association and corpus-derived coexpression evidence. A student network infers each target-block representation from the remaining genes in a cell, while a slowly updated teacher supplies the corresponding target from the full observed gene set. Under the reported extraction procedure, block-level prediction produced embeddings with higher effective rank and weaker association with detected-gene depth in the tested diagnostics than token-prediction, random-block and reconstruction controls. Across CellBench tasks, frozen BioM-JEPA embeddings retained expression, pathway and neighbourhood information and achieved the lowest aggregate perturbation-response error among the evaluated models. Representation diagnostics were also consistent with canonical pancreatic programmes and compositional relationships between genetic perturbations. Linear attention avoids constructing a quadratic gene-by-gene attention matrix; in a matched one-epoch hPancreas experiment at batch size 8, BioM-JEPA provided 5.75-fold higher fine-tuning throughput and 3.76-fold higher held-out embedding throughput than scFoundation. Together, these results support graph-connected gene blocks as useful prediction units for JEPA-style representation learning in single-cell biology.

## 2. ViSR-KGC: Visual Subgraph Reasoning with Vision-Language Models for Multimodal Knowledge Graph Completion

- Authors: Jiafan Li, Mengxue Yang, Jiaqi Zhu, Liang Chang, Ying Li, Hongan Wang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-06
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 3.6356792904199753
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.05833v1
- PDF: https://arxiv.org/pdf/2608.05833v1
- Local PDF: pdf/2026-08-08_02_ViSR-KGC_ Visual Subgraph Reasoning with Vision-Language Models for Multimodal Knowledge Graph Completion.pdf

Knowledge graph completion (KGC) aims to infer missing entities or relations from incomplete graph structures, and has evolved into multimodal knowledge graph completion (MMKGC), where entities are associated with multiple modalities such as text and images. Traditional representation learning approaches follow the embedding-based paradigm and may struggle when relation-specific evidence is limited. Meanwhile, LLM-based reasoning methods typically linearize graph structures into textual prompts, which obscures structural topology and neglects vital visual information. While vision-language models (VLMs) excel at multimodal reasoning, they cannot natively interpret structured graph topology, particularly when it comes to knowledge graphs where nodes and edges carry complex semantics. To bridge this gap, we propose ViSR-KGC, a visual subgraph reasoning approach for KGC. It integrates three complementary capabilities to capture semantic correlations: identifying global topology dependencies via representation learning, analyzing local multimodal evidence using VLMs, and providing necessary commonsense knowledge inherent in pre-trained models. Based on learned multimodal embeddings, our framework first extracts a compact and query-aware subgraph from the MMKG. Then, this subgraph is transformed into a visually interpretable image using a layout strategy selected through empirical comparison.Finally, the visualized subgraph, entity images, textual descriptions, and candidate answers are combined into a unified prompt, enabling the VLM to infer the missing entity.

## 3. MetaboLLM: a metabolomics-specialized large language model for biochemical knowledge integration and predictive metabolite graph construction

- Authors: Dohyun Ku, Min Gu Kwak, Francisco J. Pasquel, Jing Li
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-06
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.5073184640234767
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.06253v1
- PDF: https://arxiv.org/pdf/2608.06253v1
- Local PDF: pdf/2026-08-08_03_MetaboLLM_ a metabolomics-specialized large language model for biochemical knowledge integration and predictive metaboli.pdf

Metabolomics knowledge is distributed across heterogeneous resources and remains difficult to translate into predictive representations. We developed MetaboLLM, a metabolomics-specialized large language model adapted through continual pretraining, supervised fine-tuning, and structured retrieval, together with MetaboLLM-GIN, which converts generated biochemical descriptions into metabolite graphs for patient-level prediction using a graph isomorphism network. Across four backbone families, MetaboLLM outperformed corresponding base and medically adapted models on metabolomics knowledge, relational, and description tasks, and transferred to an external public benchmark. MetaboLLM-GIN achieved the highest AUC for stress hyperglycemia prediction after coronary artery bypass grafting (0.8616) and postmenopausal hormone-regimen classification (0.8123), outperforming conventional models, alternative graph constructions, and graphs generated from unadapted or non-retrieval LLM configurations. Model interpretation further produced biologically meaningful findings in both applications. These results show that domain-specialized language models can organize heterogeneous biochemical knowledge into predictive and interpretable metabolite graph representations.

## 4. RxnCLF: Contrastive Transformation-Aware Reaction Foundation Model for Improved Reactivity Prediction

- Authors: Yiting Zheng, Cheng Fang, Anthony Donofrio, Haote Li
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-06
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.277811448553213
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.06259v1
- PDF: https://arxiv.org/pdf/2608.06259v1
- Local PDF: pdf/2026-08-08_04_RxnCLF_ Contrastive Transformation-Aware Reaction Foundation Model for Improved Reactivity Prediction.pdf

Reaction yield prediction remains challenging because labeled data are scarce and reaction space is both combinatorially large and sparsely populated, limiting the generalization of existing reaction representations. String-, fingerprint-, and graph-based reaction encodings only partially capture chemical transformations, making accurate prediction difficult for reactions with complex substrates. We propose reaction contrastive learning foundation (RxnCLF), a self-supervised contrastive framework for reaction representation learning. RxnCLF is built on a condensed reaction graph (CRG) that unifies reactant and product information into a single graph, enabling the model to learn explicit and enriched transformation structure rather than disconnected graphs. Pretrained on 1.7 million Pistachio reactions, RxnCLF learns a compact and continuous latent space that captures both reaction-center features and broader side chain contexts, making it transformation-aware and chemically interpretable. Fine-tuned on multiple yield prediction benchmarks, including Buchwald-Hartwig, Pd-catalyzed BH coupling, and proprietary HTE C-N coupling and amide formation datasets, RxnCLF consistently outperforms graph and sequence-based baselines, improving R2 and achieving the best performance overall. Our results highlight the promise of CRG-based RxnCLF as a scalable reaction foundation model, with the potential to generalize across broader reaction spaces and support diverse downstream reaction informatics tasks, including regioselectivity prediction, enantioselectivity prediction, and reaction condition optimization.

## 5. SLIM: A small linear model with STRING embeddings for single-cell genetic perturbation prediction

- Authors: Hu, D., Pielies Avelli, M., Jensen, L. J., Rasmussen, S.
- Source: biorxiv
- Venue type: preprint
- Journal: biorxiv
- Publication status: preprint
- Publication date: 2026-08-07
- DOI: 10.64898/2026.08.07.743481
- Categories: bioinformatics
- Relevance: 3.26721628852201
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://www.biorxiv.org/content/10.64898/2026.08.07.743481v1.full.pdf
- PDF: https://www.biorxiv.org/content/10.64898/2026.08.07.743481v1.full.pdf
- Local PDF: Not downloaded

Predicting cellular responses to genetic perturbations is central to understanding gene function and prioritizing therapeutic targets, but experimental screens cannot exhaustively cover genes, cell types, and perturbation combinations. Recent benchmarks have shown that simple baselines can match or outperform substantially more complex models, suggesting that informative biological priors may be as important as model capacity. Here we present SLIM, a lightweight extension of the bilinear model of Ahlmann-Eltze et al. SLIM represents perturbations with 64-dimensional embeddings derived from the STRING protein network and predicts mean transcriptional responses through a closed-form ridge-regression estimator. It then constructs single-cell populations by retrieving training cells and rescaling each gene to match the predicted mean. We evaluated SLIM against four deep learning models and two simple baselines on four single-gene perturbation datasets and one combinatorial perturbation dataset. Across these within-dataset benchmarks, SLIM achieved competitive mean-response accuracy, ranked first in eight of twelve single-gene dataset-metric comparisons, and produced substantially lower maximum mean discrepancy values than the evaluated alternatives. The model has 640 trainable parameters and fitted each benchmark dataset in under 10 seconds on a CPU. These results show that compact biological representations can support accurate and computationally efficient perturbation prediction. Code is available at https://github.com/RasmussenLab/SLIM.

## 6. Cross-Architecture Steering Transfer in Language Models: A Systematic Empirical Study

- Authors: Ayushi Agarwal
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-05-26
- DOI: Unavailable
- Categories: cs.CL, cs.LG
- Relevance: 3.2248896730297387
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.05164v1
- PDF: https://arxiv.org/pdf/2608.05164v1
- Local PDF: pdf/2026-08-08_06_Cross-Architecture Steering Transfer in Language Models_ A Systematic Empirical Study.pdf

Independently trained large language models may develop shared internal representations of semantic concepts despite architectural differences -- but whether this geometric similarity has functional consequences for cross-model behavioural control remains untested. We present the first systematic evaluation of cross-model steering transfer and show that shared LLM geometry is functionally exploitable, conditionally: concept directions from one model can steer a different independently trained model when sufficient representational capacity exists. We study five open-weight models spanning three parameter scales (0.8B--8B) and two architectural lineages, training one Sparse Autoencoder per model across 15 semantic domains and testing alignment across all 20 directed model pairs. We observe a suggestive discontinuity near 1.7B parameters: at >= 1.7B scale, 47--49% of cross-model feature pairs validate (Pearson r >= 0.60, Procrustes cosines 0.895--0.956), while alignment degrades sharply below 0.8B. Cross-model steering vectors (B3-TI) achieve a 71.0% win rate across 15 supervised concepts versus 68.0% for same-model native vectors; a single universal vector achieves 67.3% in 4 of 5 models without any per-model supervision. Transfer degrades for models below 1.7B and for one model with generation instability, confirming that functional exploitability requires sufficient representational capacity. Our findings underscore the importance of scale thresholds in mechanistic interpretability: tools validated at 7B scale may not transfer to smaller models without revalidation. We provide the first functional complement to the Platonic Representation Hypothesis -- geometric convergence across independently trained LLMs supports cross-model behavioural control without fine-tuning, under the identified scale conditions.

## 7. Benchmarking single-cell foundation models in a zero-shot setting

- Authors: Gaballa, Y., Ahmed, S., Abdelaal, T.
- Source: biorxiv
- Venue type: preprint
- Journal: biorxiv
- Publication status: preprint
- Publication date: 2026-08-07
- DOI: 10.64898/2026.08.03.739553
- Categories: bioinformatics
- Relevance: 3.1954802277494645
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://www.biorxiv.org/content/10.64898/2026.08.03.739553v1.full.pdf
- PDF: https://www.biorxiv.org/content/10.64898/2026.08.03.739553v1.full.pdf
- Local PDF: Not downloaded

Single-cell foundation models have recently emerged as a promising approach for learning general-purpose representations from large-scale transcriptomic data. These models are trained on millions of cells and are designed to transfer their learned representations to a wide range of downstream tasks. However, their practical benefits compared to traditional approaches are still not fully understood. This study evaluates four foundation models, namely scGPT, SCimilarity, UCE, and Transcriptformer, across four downstream tasks: cell type annotation, human data integration, cross-species data integration, and protein expression prediction. Embeddings generated by each model were assessed using multiple public single-cell datasets and compared against conventional machine learning baselines. Performance was measured using task-specific evaluation metrics, including classification, integration, and regression metrics. The results showed that foundation model embeddings did not consistently outperform traditional approaches. In the cell type annotation task, baseline methods achieved the strongest performance across most datasets. For protein expression prediction, however, embeddings from the foundation models generally produced more accurate predictions than the baseline, with SCimilarity achieving the lowest prediction error and Transcriptformer obtaining the highest correlation scores. In the data integration task, all foundation models produced moderate results, while scVI (the baseline) achieved the strongest integration performance. Overall, the results suggest that current single-cell foundation models provide useful representations for some downstream tasks in zero-shot conditions but do not yet offer a universal replacement for task-specific methods. Their effectiveness remains dependent on the application and evaluation setting.

## 8. PRISM: Distribution-Gated Flow Matching for Controllable Unpaired Image Translation

- Authors: Elad Yoshai, Natan T. Shaked
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-06
- DOI: Unavailable
- Categories: cs.CV, cs.AI
- Relevance: 3.1374995123569027
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.06240v1
- PDF: https://arxiv.org/pdf/2608.06240v1
- Local PDF: pdf/2026-08-08_08_PRISM_ Distribution-Gated Flow Matching for Controllable Unpaired Image Translation.pdf

Unpaired image-to-image translation must decide, per image, what to change and what to preserve without paired supervision. Many diffusion-based unpaired translators control preservation through a single global noise or guidance value applied across the image, which cannot separate content to keep from appearance to change. We present PRISM, a GAN-free flow-matching framework that replaces this global control with a learned per-feature gate. The gate's spatial prior is derived from each source feature's standardized distance to the target feature distribution, so features far from the target are freed while target-consistent features are preserved. The same gate controls both the initialization, which mixes the real source latent with a task-matched corruption, and the transport timing during Ordinary Differential Equation (ODE) integration. The corruption is matched to the task, content-anchored (AdaIN) for structure-preserving translation and partially anchored for structure-changing translation, and the gate can be overridden locally at inference from text or a detector without retraining, preserving important structures of the original image while still generating realistic results. We evaluate PRISM on five natural and biomedical benchmarks (AFHQ cat->dog, CelebA-HQ appearance translation, day->night relighting, virtual staining, and breast frozen->permanent histopathology). Among the evaluated methods under a shared same-split protocol, PRISM attains the best Inception FID and KID on four benchmarks and a competitive result on the fifth, and on histopathology yields the nuclei-count ratio closest to the ideal, supporting a favorable balance between target realism and structural preservation.

## 9. A Six-Dimensional Taxonomy of Post-Training Adaptation Techniques with Applications in AI Governance

- Authors: Fardin Afdideh, Fernando Seoane, Farhad Abtahi
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-06
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.1257561540812735
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.06246v1
- PDF: https://arxiv.org/pdf/2608.06246v1
- Local PDF: pdf/2026-08-08_09_A Six-Dimensional Taxonomy of Post-Training Adaptation Techniques with Applications in AI Governance.pdf

Post-training adaptation has become central to modern machine learning practice and includes techniques such as retraining, fine-tuning, parameter-efficient adaptation, alignment, retrieval augmentation, model editing, unlearning, calibration, and Multimodal Instruction Tuning. However, the literature remains fragmented across technique families, model classes, and deployment contexts, making it difficult to compare methods or describe how a trained model has been modified. This survey synthesizes the post-training adaptation literature and introduces a six-dimensional taxonomy organized by mechanism, goal, data requirement, persistence, structural scope, and model type. The taxonomy distinguishes commonly conflated terms such as fine-tuning, retrieval augmentation, and prompting, and shows how adaptation strategies evolve from traditional machine learning through deep learning, foundation models, large language models, and multimodal large language models. It also maps relationships among techniques, including inheritance, supersession, hybridization, and layered deployment stacks. The resulting vocabulary can support technical documentation, model-change tracking, and governance analysis. The survey concludes by identifying open challenges in evaluation, reproducibility, persistent inference-time adaptation, unlearning, multimodal adaptation, and governance-aware post-training workflows.

## 10. Comparative Approaches to Agent Retrieval over Large Skill Libraries

- Authors: Indivara Kolluru, Nathan Sportsman
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-06
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 3.1170303443773135
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.06196v1
- PDF: https://arxiv.org/pdf/2608.06196v1
- Local PDF: pdf/2026-08-08_10_Comparative Approaches to Agent Retrieval over Large Skill Libraries.pdf

Agents backed by large skill libraries must decide which skills to load and in what order. Loading the entire library into context is expensive and provides no structure for autonomous sequencing. We study two systems for this problem over a corpus of 690 skills: a hybrid ranker combining lexical and dense-embedding retrieval for sparse, on-demand loading, and a typed knowledge graph encoding workflow relations such as prerequisites, data flow, and ordering. On a set of 117 realistic, non-echoing queries, the hybrid ranker retrieves the correct skill within the top five in 73.5% +/- 8.0 of cases, leaving roughly a quarter of queries unserved. When used as the design intended (substituting graph neighbours for additional ranked results at matched token budget), the graph is significantly worse (-11.2 points, p = 0.0007). Its LLM-generated edge layer adds nothing over neighbours obtained free from a local embedding pass, and 73% of the queries the ranker misses are not reachable through the graph at all. We attribute this to a pre-filter topology bound. Because the graph's candidate edges are drawn from the same embedding neighbourhood the ranker already searches, 98.6% of typed edges connect skills the ranker had already surfaced together. The graph can enrich relation semantics but cannot extend retrieval reach. We further show that evaluating on author-written queries overstates hit@5 by up to 44 points, which would have hidden these results entirely. Our contribution is a mechanistic account of why added structure does not improve retrieval over a strong ranker, and identify the conditions under which adding structural interdependence into the retrieval is optimal.

## 11. Frozen but Not Always Accessible: A Representation Analysis of Genomic Language Models

- Authors: Nirjhor Datta, Swakkhar Shatabda, M. Sohel Rahman
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-05
- DOI: Unavailable
- Categories: q-bio.GN
- Relevance: 3.0716505035142605
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.05329v1
- PDF: https://arxiv.org/pdf/2608.05329v1
- Local PDF: pdf/2026-08-08_11_Frozen but Not Always Accessible_ A Representation Analysis of Genomic Language Models.pdf

Genomic foundation models are increasingly reused as frozen feature extractors for downstream sequence prediction, offering a compute-efficient alternative to full fine-tuning. However, it remains unclear when biological information encoded by these models is accessible without task-specific adaptation. We present a representation-accessibility analysis of frozen genomic language models across regulatory, epigenetic, promoter, splice-site, and variant-effect prediction tasks. We evaluate DNABERT-2, Nucleotide Transformer, HyenaDNA, GENERATOR-v2, and Omni-DNA under unified frozen-probing protocols, while separating diagnostic readout analyses from validation-selected checks. Our results reveal a consistent task-dependent pattern: frozen probes recover 95-100 % of fine-tuned performance on promoter tasks, but average splice-site recovery drops to 60-88 %. Frozen embeddings are also competitive on broad Genomic Benchmark tasks such as coding-region and species-discrimination classification, but show larger gaps on some regulatory and OCR tasks. Layer-wise probing, in-silico mutagenesis, variant-effect prediction, and embedding geometry show that local biological signal is partially present in frozen representations, but is not always accessible through final pooled embeddings.

## 12. Disentangling 3D Modeling from Spatial Reasoning

- Authors: Haoze Sun, Jiequan Cui, Qingshan Xu, Richang Hong
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-05
- DOI: Unavailable
- Categories: cs.LG, cs.CV
- Relevance: 3.0410877606053455
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.05242v1
- PDF: https://arxiv.org/pdf/2608.05242v1
- Local PDF: pdf/2026-08-08_12_Disentangling 3D Modeling from Spatial Reasoning.pdf

In this work, we explore an alternative paradigm for spatial reasoning by explicitly disentangling 3D perception from reasoning, rather than jointly acquiring implicit 3D perception and reasoning through large-scale training. Our key observation is that modern perception models excel at estimating continuous 3D geometry, whereas large language models (LLMs) are particularly effective at compositional and symbolic reasoning. Motivated by these complementary strengths, we propose the Disentangled Spatial Reasoner (DiSR), a simple yet effective framework that reconstructs the physical world into structured 3D evidence using off-the-shelf expert perception models and fine-tunes an LLM with LoRA to perform reasoning solely over this explicit geometric evidence. Without large-scale 3D VQA training or complex tool-use policies, DiSR achieves competitive performance on popular spatial reasoning benchmarks. Beyond its strong performance, DiSR offers improved interpretability, modularity, and computational efficiency, demonstrating that explicit separation of perception and reasoning is a scalable and effective alternative paradigm to end-to-end modeling for spatial intelligence.

## 13. THBKG: A Temporal Biomedical Knowledge Graph for Decision-Aligned Clinical Advancement Prediction

- Authors: Pui Chung Siu, Claudia Cabrera, Mani Mudaliar, Arkaitz Zubiaga
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-06
- DOI: Unavailable
- Categories: cs.LG, q-bio.QM
- Relevance: 3.0125279509989396
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.05982v1
- PDF: https://arxiv.org/pdf/2608.05982v1
- Local PDF: pdf/2026-08-08_13_THBKG_ A Temporal Biomedical Knowledge Graph for Decision-Aligned Clinical Advancement Prediction.pdf

Inadequate target--disease linkage accounts for 40--50\% of Phase~II efficacy failures, so anticipating which programmes will advance would let sponsors back the hypotheses most likely to reach patients. What a programme can be judged on is the evidence that supported its linkage \emph{when it entered the clinic}. No existing biomedical knowledge graph allows that evidence profile to be assembled as of a past date. We present the Temporal Heterogeneous Biomedical Knowledge Graph (THBKG), which describes and predicts therapeutic target--disease links through time: 110,396 entities and 11.1M edges across nineteen relation types, each edge carrying the year its evidence changed, so a pair's profile can be recovered as it stood when its own decision fell due. On this graph we define a decision-aligned benchmark that predicts, for a target--disease pair entering Phase~II, whether it advances to Phase~III on evidence datable before that decision. Graph propagation over the THBKG outranks every direct-evidence reference scored under the same decision-aligned protocol, reaching a relative success of 4.3--4.5 at the top ten pairs per therapeutic area. The gain concentrates on the 72.8\% of pairs with no direct target--disease evidence at their decision point, where a direct-edge model has nothing to read: the encoders still rank five- to sixfold above chance, recovering the signal by propagating over the intervening biology. Adapting a path-based explainer to the decision-time subgraph decomposes each prediction into the evidence landscape behind the hypothesis for explainable prediction. We release the THBKG as a continually updated substrate for studying therapeutic target hypotheses by retrospective validation.

## 14. Mean-Field Dynamics of Chain-of-Thought Reasoning in Large Language Models

- Authors: Hao Ai
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-05-20
- DOI: Unavailable
- Categories: cs.CL, cs.AI
- Relevance: 3.0097473093501037
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.05152v1
- PDF: https://arxiv.org/pdf/2608.05152v1
- Local PDF: pdf/2026-08-08_14_Mean-Field Dynamics of Chain-of-Thought Reasoning in Large Language Models.pdf

Large language models (LLMs) with chain-of-thought reasoning have been widely applied in recent years, and theoretical explanations of their behavior may help deepen our understanding and guide model optimization. In this study, we introduce a framework that seeks statistical regularities and theoretical interpretations in LLM reasoning without simplifying the model architecture or making analogies to existing physical systems. We formulate LLM reasoning as a guided discovery process on a clue graph, and derive a one-dimensional ordinary differential equation for the fraction of discovered clues using the mean-field approximation. Experimentally, clue tokens are identified using the normalized surprisal of a student LLM on the outputs of a teacher LLM, and statistical regularities are obtained by averaging over many reasoning chains of thought. Our experiments show that the resulting statistical regularities are reproducible within the same dataset and can be fitted by the solving the proposed theoretical equation.

## 15. MACRO: Markov Chain Routing of Transformer Layers

- Authors: Paweł Batorski, Abtin Pourhadi, Akylgali Aitaza, Przemysław Spurek, Paul Swoboda
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-06
- DOI: Unavailable
- Categories: cs.CL, cs.AI
- Relevance: 2.995758015634691
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.05872v1
- PDF: https://arxiv.org/pdf/2608.05872v1
- Local PDF: pdf/2026-08-08_15_MACRO_ Markov Chain Routing of Transformer Layers.pdf

Standard Large Language Models (LLMs) execute layers sequentially. Dynamic layer routing, i.e. search for a different execution path through layers involving layer repetitions, skips and other moves, can improve performance. Existing routing approaches often require updating model weights, running expensive search loops per test instance, or demand ground-truth labels during inference. In this work, we propose Markov Chain Routing of Transformer Layers (MACRO), a framework that learns task-specific routes over LLM architectures without modifying underlying parameters. MACRO models layer routing as a context-dependent Markov policy conditioned on layer indices, computation budget phases, directional displacements, and operator context, supporting skip, repeat, and residual hidden-state addition operations. The Markov route distribution is updated via feedback on training data and decoded using a top-k Viterbi algorithm to isolate high-probability candidate programs. We evaluate MACRO across diverse reasoning and knowledge benchmarks on multiple open-weight LLMs. MACRO achieves a +5.0% average accuracy improvement over the unrouted baselines, with largest gains on small models. We outperform the best dynamic routing approach Dr. LLM by +7.2%, while reducing route-search time 9.4x (from 14.8 to 1.6 hours). Our code is publicly available at https://github.com/Batorskq/MACRO.

## 16. Task-Conditional Flow Matching for Balanced Multilingual Text Embedding Adaptation

- Authors: Tirth Bhatt, Naren Kumar S, Mayank Singh
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-06
- DOI: Unavailable
- Categories: cs.CL, cs.AI
- Relevance: 2.956965140949472
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.05785v1
- PDF: https://arxiv.org/pdf/2608.05785v1
- Local PDF: pdf/2026-08-08_16_Task-Conditional Flow Matching for Balanced Multilingual Text Embedding Adaptation.pdf

Multilingual text embedding models are commonly adapted using a single training objective across diverse tasks, despite different tasks requiring fundamentally different optimization strategies. We introduce Task-Conditional Flow Matching (TCFM), a multilingual embedding adaptation framework that selectively applies Flow Matching to translation tasks while optimizing retrieval, classification, and pair-classification tasks with objectives better aligned to their learning dynamics. TCFM further combines teacher-guided representation preservation with a three-stage curriculum to enable stable adaptation. Evaluated on the Indic Massive Text Embedding Benchmark, TCFM establishes a new state-of-the-art, consistently improving embedding quality across a diverse set of multilingual tasks and generalizing across embedding model families. We will publicly release the codebase and datasets upon acceptance of the paper.

## 17. CircuitSteer: Geometrically Aligned Multi-Layer Steering via Sparse Autoencoder Circuits

- Authors: Mehrshad Saadatinia, Parsa Razmara, Ardalan Aryashad, Ali Abbasi, Seyedarmin Azizi
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-06
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 2.9315981097164006
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.05732v1
- PDF: https://arxiv.org/pdf/2608.05732v1
- Local PDF: pdf/2026-08-08_17_CircuitSteer_ Geometrically Aligned Multi-Layer Steering via Sparse Autoencoder Circuits.pdf

Controlling the behavior of large language models (LLMs) remains a critical challenge for AI alignment. Existing steering methods, such as Contrastive Activation Addition (CAA), typically rely on fixed single-layer interventions derived from aggregate activation differences. These methods impose a single intervention across semantically diverse inputs and often fail to sustain consistent behavioral changes across layers, limiting the effectiveness of the steering. In this work, we introduce CircuitSteer, a novel framework that leverages Sparse Autoencoders (SAEs) to identify and manipulate coherent semantic circuits distributed across multiple layers. By constructing a feature flow circuit based on feature co-activation and the geometric alignment of decoder directions, we isolate the specific multi-layer subcircuits responsible for a target behavior. We then synthesize dense steering vectors from these sparse features and apply multi-point interventions to guide the model's internal semantic trajectory. We evaluate CircuitSteer using contrastive examples across a diverse set of tasks, including toxicity, emotion-intensity, sycophancy, and refusal, spanning two model families. Across all models and datasets, CircuitSteer is the only method to consistently produce fluency-preserving interventions; competing methods either sacrifice text quality or lack coverage, failing entirely on complex behaviors like sycophancy and refusal. These results demonstrate that multi-layer circuit steering, enabled by enforcing geometric alignment among selected features, yields strictly more robust and effective behavioral control than static single-point interventions. Code is available at https://github.com/mehrshad-sdtn/CircuitSteer.

## 18. Learning Globally Reusable Skills for Coding Agents

- Authors: Chen Yang, Jiashuo Tian, Ziqi Wang, Xinyin Liu, Meiru Ye, Junjie Chen
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-06
- DOI: Unavailable
- Categories: cs.SE, cs.AI
- Relevance: 2.9314577049002377
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.06153v1
- PDF: https://arxiv.org/pdf/2608.06153v1
- Local PDF: pdf/2026-08-08_18_Learning Globally Reusable Skills for Coding Agents.pdf

Automated skill evolution enables Large Language Model (LLM) agents to continuously improve without expensive retraining. However, existing approaches typically treat skill evolution as a sequence of local updates, overlooking relationships among skills and often producing overfitted skill updates that fail to generalize across tasks. We propose GSE, a globalized skill evolution framework that jointly optimizes skill compatibility and skill generalization. To preserve consistency across the skill bank, GSE maintains a Skill Relation Graph (SRG) that explicitly models and co-evolves inter-skill relationships. To improve generalization, GSE performs cluster-based skill consolidation to abstract reusable capabilities from local updates and employs replay-driven verification to prevent overfitting and behavioral regressions. We evaluate GSE on two representative software engineering tasks: bug-revealing test generation and false-positive bug report filtering. Across two state-of-the-art coding agents, OpenHands and mini-SWE-agent, GSE consistently achieves the best precision, recall, and F1-score. Compared with existing evolution techniques, GSE improves precision and recall by 6.1%~34.1% and 31.8%~180.0% for test generation, and by 15.4%~96.4% and 13.1%~19.8% for false-positive filtering. Deployment on an internal industrial agent further yields a 61.4% improvement in F1-score, demonstrating the effectiveness and generalizability of GSE for evolving effective skills.

## 19. Big, Bright, or Invisible: A Frozen-Feature Benchmark of 3D CT Foundation Models

- Authors: Maulik Chevli, Johannes Brandt, Rickmer Braren, Daniel Rueckert, Philip Müller
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-06
- DOI: Unavailable
- Categories: cs.CV, cs.AI
- Relevance: 2.9282549752772677
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.05960v1
- PDF: https://arxiv.org/pdf/2608.05960v1
- Local PDF: pdf/2026-08-08_19_Big, Bright, or Invisible_ A Frozen-Feature Benchmark of 3D CT Foundation Models.pdf

Routine CT interpretation is inherently comprehensive, capturing incidental findings across the entire scan volume. 3D CT foundation models could assist this process by providing generalizable representations of anatomy and pathology. To evaluate their diagnostic breadth, we benchmark ten frozen CT encoders across three cohorts of thoracic CT scans, including an unseen internal clinical dataset, using $k$-nearest neighbors, zero-shot prompting, and linear probing. We find no universal state-of-the-art, with rankings fluctuating significantly depending on the evaluation context. While models combining fine-grained image tokenization with vision-language alignment generally perform best, a lightweight supervised encoder remains highly competitive, demonstrating that explicit labels can effectively substitute for scale. Crucially, rather than model architecture, we observe that the primary determinant of performance is a physical bottleneck: a finding's detectability scales with its contrast against surrounding tissue and its spatial extent. Through controlled within-organ comparisons, we empirically demonstrate that widespread or high-contrast abnormalities, such as devices and effusions, are reliably recovered. Conversely, small, low-contrast focal lesions remain a persistent challenge across all evaluated encoders. We attribute this to the inherent limitations of globally pooled embeddings, suggesting that accurately representing small, low-contrast structures will require region- or lesion-level pretraining.

## 20. CohortHijack: Robustness of Single Cell Annotation to Companion Cell Removal

- Authors: Arash Vashagh, Yasmin Vashagh
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-06
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 2.900635146940754
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.05900v1
- PDF: https://arxiv.org/pdf/2608.05900v1
- Local PDF: pdf/2026-08-08_20_CohortHijack_ Robustness of Single Cell Annotation to Companion Cell Removal.pdf

Many single-cell annotation tools refine an initial cell label using nearby cells or cluster-level voting. We study whether this refinement can be manipulated without changing the target cell. We introduce CohortHijack, a robustness audit that removes selected non-target cells from the query cohort while preserving the target expression profile, base prediction, and trained model. We evaluate random and structured removal methods, together with greedy, multi-start, and beam search, on PBMC3K and Paul15 using logistic regression and calibrated linear SVM classifiers. Structured removal was consistently stronger than random removal on Paul15. Multi-start search changed 24.33% of linear-SVM targets and 19.67% of logistic-regression targets while removing a small fraction of the cohort and keeping mean collateral changes below 0.4%. Ablations confirmed that the effect disappeared when neighborhood refinement was disabled. We also evaluated CellTypist majority voting, where independent predictions remained unchanged across all evaluations, but refined labels changed after small companion-cell removals. These findings identify query cohort composition as a target-preserving attack surface in single-cell annotation.

## 21. C$^3$PO: Evaluating Cross-Modal Composition and Counterfactual Performance in Omnimodal Models

- Authors: Swapnanil Mukherjee, Agyeya Negi, Tanuja Ganu, Ponnurangam Kumaraguru
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-05
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 2.8944726339697704
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.05381v1
- PDF: https://arxiv.org/pdf/2608.05381v1
- Local PDF: pdf/2026-08-08_21_C$^3$PO_ Evaluating Cross-Modal Composition and Counterfactual Performance in Omnimodal Models.pdf

Current Multimodal Large Language Models (MLLMs) can process diverse sensory inputs, yet their reasoning remains heavily biased toward a dominant modality, resulting in brittle cross-modal reasoning. We introduce C$^3$PO, a benchmark of 3,404 samples spanning video, audio, image, and text, evaluating two abilities: information composition (fusing dispersed evidence) and counterfactual conflict (resolving deliberate contradictions). C$^3$PO's paired IC/CC structure and four-tier design enable targeted diagnosis of when and why cross-modal reasoning fails. Built through a fully automatic pipeline using 25 logically grounded templates, C$^3$PO reveals that while humans achieve 88.64% accuracy, the best model (Gemini-3.1-Pro) reaches only 73.17%, with open-source models collapsing under conflict. Through attention probes, we find 86-95% of failures stem from modality dominance: models commit to one modality while ignoring contradictory evidence, concentrating 87-95% of attention on text. Mid-layer attention entropy predicts correctness-sustained exploration succeeds, premature collapse fails. The 56-point accuracy gap between equally complex templates reveals that performance depends on modalities' structural roles in conflict resolution, not combinations. These findings show multimodal perception does not guarantee robust reasoning; architectures must enable sustained cross-modal attention to avoid premature

## 22. BALANCE: Hybrid Autoregressive-Speculative LLM Inference in Wireless Edge Networks

- Authors: Guanqiao Qu, Shuo Chen, Qian Chen, Kin K. Leung, Xianhao Chen
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-06
- DOI: Unavailable
- Categories: cs.NI, cs.AI
- Relevance: 2.8789577227600596
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.05926v1
- PDF: https://arxiv.org/pdf/2608.05926v1
- Local PDF: pdf/2026-08-08_22_BALANCE_ Hybrid Autoregressive-Speculative LLM Inference in Wireless Edge Networks.pdf

Edge inference is a promising paradigm to provide large language model (LLM) inference services in next-generation mobile networks. LLM inference mainly relies on two approaches: Autoregressive decoding (AD) generates output tokens sequentially, resulting in long latency; Speculative decoding (SD) accelerates inference by using a small language model (SLM) to generate multiple draft tokens for LLM verification, but incurs extra memory costs. Due to this latency-memory tradeoff, neither approach alone can efficiently serve users with heterogeneous demands under limited edge computing resources. To address this challenge, we propose a hybrid autoregressive-speculative inference (BALANCE) framework for edge LLM inference. In BALANCE, an edge server hosts both an SLM and an LLM, assigns each user to AD or SD, and performs the two modes simultaneously. To maximize the number of served users, we formulate a task throughput maximization problem to jointly determine user scheduling and computing resource allocation between AD and SD under user latency requirements and server memory constraints. Since the problem is NP-hard, we develop a polynomial-time algorithm that transforms the original problem into two sub-problems and obtains a sub-optimal solution with a constant approximation guarantee. Experiments demonstrate that BALANCE consistently outperforms conventional AD and SD and significantly improves task throughput.

## 23. GROM: Gradient-Free Rapid One-Shot Machine Unlearning

- Authors: Paweł Batorski, Przemysław Spurek, Paul Swoboda
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-06
- DOI: Unavailable
- Categories: cs.LG, cs.AI, cs.CL
- Relevance: 2.8564200277715193
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.05783v1
- PDF: https://arxiv.org/pdf/2608.05783v1
- Local PDF: pdf/2026-08-08_23_GROM_ Gradient-Free Rapid One-Shot Machine Unlearning.pdf

Machine unlearning has become a critical capability for safely removing specific, sensitive knowledge from large language models (LLMs). Current state-of-the-art approaches primarily rely on iterative, training-time unlearning via fine-tuning. However, even when utilizing parameter-efficient dimensionality reduction techniques like LoRA, gradient-based optimization remains computationally expensive and lacks explicit analytical formulations. It can also leave the targeted knowledge merely hidden rather than removed, to the point that simply quantizing the unlearned model restores much of what it was supposed to have erased. To resolve this, we propose a novel one-shot unlearning approach, abandoning iterative optimization in favor of a direct, exact analytical solution. We frame the unlearning process as a ridge-regularized least-squares optimization problem, deriving a closed-form additive update for targeted weight matrices. This update forces the selected layer to suppress unwanted content while strictly preserving its behavior on retained data. Computed from gradient-free forward passes alone, with no backpropagation and no iteration to convergence, GROM applies the weight edit in mere seconds, which makes it orders of magnitude faster than traditional fine-tuning. Extensive evaluations demonstrate that GROM achieves state-of-the-art forgetting-utility trade-offs on TOFU-5%, TOFU-10%, MUSE-Books, MUSE-News and WMDP, significantly reducing computational overhead without sacrificing overall model performance. Because the update removes the targeted content from the weights instead of masking it, GROM also withstands the low-bit quantization attack that recovers much of the content a gradient-based baseline had appeared to forget. Our code is publicly available at https://github.com/Batorskq/GROM.

## 24. Lightweight Haar Wavelet Subband Pruning for LLMs

- Authors: Jiang Li, Pengfei Cao, Chenxi Zhou, Tian Lan, Xiangdong Su, Kang Liu, Jun Zhao, Guanglai Gao
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.8128390664498055
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.798/
- PDF: https://aclanthology.org/2026.findings-acl.798.pdf
- Local PDF: pdf/2026-08-08_24_Lightweight Haar Wavelet Subband Pruning for LLMs.pdf

Large language models (LLMs) reach state-of-the-art performance across many NLP tasks, but their large parameter counts introduce heavy computational and memory overhead, which complicates deployment in resource-constrained settings. Pruning is a standard compression strategy that induces sparsity to lower these costs. However, most pruning methods for LLMs depend on calibration data and expensive weight updates, which limits practical scalability. To address these limitations, we introduce H aar W avelet S ubband P runing (), a post-training framework that requires no calibration data and no weight updates. applies a two-dimensional Haar wavelet transform to each weight matrix and decomposes it into four frequency subbands. It then assigns a uniform sparsity ratio to all subbands so that both low- and high-frequency components are retained in a balanced manner. Our theoretical analysis shows that the subband design of provides a deterministic per-subband retention guarantee, which helps mitigate the potential bias of global magnitude pruning toward dominant frequency components. Experiments on the LLaMA, OPT and Qwen model families show that achieves competitive accuracy relative to strong pruning baselines while substantially reducing pruning time. Compared with magnitude pruning, which serves as a simple calibration-free baseline, generally achieves better downstream performance across a wide range of sparsity levels and model scales.

## 25. Improving Interoperability among Defence and National Security Ontologies: Analysis and Evaluation Tasks

- Authors: Jonathon Dilworth, Pedro Giesteira Cotovio, David Herron, Paul Cripps, Nigel Dewdney, Catia Pesquita, Ernesto Jiménez-Ruiz
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-06
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 2.8122448124938018
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.05867v1
- PDF: https://arxiv.org/pdf/2608.05867v1
- Local PDF: pdf/2026-08-08_25_Improving Interoperability among Defence and National Security Ontologies_ Analysis and Evaluation Tasks.pdf

The use of ontologies and knowledge graphs is becoming increasingly widespread in the defence and national security domain. Numerous ontologies have been developed through initiatives led by academia, industry, and government. Achieving interoperability across diverse defence and national security ontologies remains a major challenge due to the domain's breadth and specialisation. In this work, we analyse and document over 60 publicly available ontologies and introduce a new track for the Ontology Alignment Evaluation Initiative (OAEI). This track comprises eight matching tasks, consensus alignments and manually-curated (silver-standard) mappings. The consensus alignments are derived by aggregating the outputs of several state-of-the-art ontology alignment systems. The silver-standard is obtained from the manual validation of the consensus alignment together with a subset of the unique mappings (i.e., mappings suggested by only one system).

## 26. Learning from Evolving Training Dynamics: An Entropy-Maximizing Data Curation Strategy for LLM Supervised Post-Training

- Authors: Mengxiang Zhang, Lingyuan Liu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.8086675941937034
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.505/
- PDF: https://aclanthology.org/2026.acl-long.505.pdf
- Local PDF: pdf/2026-08-08_26_Learning from Evolving Training Dynamics_ An Entropy-Maximizing Data Curation Strategy for LLM Supervised Post-Training.pdf

Supervised post-training is essential for refining Large Language Models (LLMs), yet its effectiveness relies heavily on strategic data curation. Traditional Curriculum Learning (CL) strategies often fail to account for the evolving proficiency of the learner, relying instead on static, single dimensional metrics. We propose EVO-Curate, a dynamic data curation framework that synchronizes sample complexity with the maturing capacity of the LLM. EVO-Curate employs an Adaptive Dynamics Measurer to synthesize instantaneous difficulty and historical variability into a multidimensional utility score. To maintain representational diversity, we introduce an Evolutionary Sampling Scheduler based on an entropy maximizing mechanism. Empirical evaluations across instruction following, mathematical reasoning, and code generation demonstrate that EVO-Curate consistently outperforms standard training baselines and traditional CL methods across various architectures and scales. Specifically, our framework achieves relative performance gains of up to about 10% while maintaining manageable computational overhead. These results establish EVO-Curate as a scalable and model agnostic solution for enhancing the efficiency of modern LLM training pipelines.

## 27. ConsistRM: Improving Generative Reward Models via Consistency-Aware Self-Training

- Authors: Yu Liang, Liangxin Liu, Longzheng Wang, Wangyan, Zhang Yueyang, Long Xia, Zhiyuan Sun, Daiting Shi
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.8049326518782487
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1830/
- PDF: https://aclanthology.org/2026.acl-long.1830.pdf
- Local PDF: pdf/2026-08-08_27_ConsistRM_ Improving Generative Reward Models via Consistency-Aware Self-Training.pdf

Generative reward models (GRMs) have emerged as a promising approach for aligning Large Language Models (LLMs) with human preferences by offering greater representational capacity and flexibility than traditional scalar reward models. However, GRMs face two major challenges: reliance on costly human-annotated data restricts scalability, and self-training approaches often suffer from instability and vulnerability to reward hacking. To address these issues, we propose ConsistRM, a self-training framework that enables effective and stable GRM training without human annotations. ConsistRM incorporates the Consistency-Aware Answer Reward, which produces reliable pseudo-labels with temporal consistency, thereby providing more stable model optimization. Moreover, the Consistency-Aware Critique Reward is introduced to assess semantic consistency across multiple critiques and allocates fine-grained and differentiated rewards. Experiments on five benchmark datasets across four base models demonstrate that ConsistRM outperforms vanilla Reinforcement Fine-Tuning (RFT) by an average of 1.5%. Further analysis shows that ConsistRM enhances output consistency and mitigates position bias caused by input order, highlighting the effectiveness of consistency-aware rewards in improving GRMs.Our implementation is available at https://github.com/yuliangCarmelo/ConsistRM .

## 28. COMPEL: Compensated Mixture-of-Experts Pruning with Expert-Layer distribution

- Authors: Seohee Yoon, Yong Suk Choi
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.804722970613805
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1521/
- PDF: https://aclanthology.org/2026.findings-acl.1521.pdf
- Local PDF: pdf/2026-08-08_28_COMPEL_ Compensated Mixture-of-Experts Pruning with Expert-Layer distribution.pdf

Mixture-of-Experts (MoE) architectures have emerged as an effective approach for scaling Large Language Models (LLMs) by activating only a subset of experts during inference. Despite their computational efficiency, MoE models incur a substantial memory bottleneck from maintaining all expert parameters during inference. To address this challenge, numerous MoE pruning methods have been proposed. However, most existing methods adopt uniform pruning across layers, which fails to capture layer-wise variations in expert importance and redundancy. In this paper, we propose COmpensated MoE Pruning with Expert-Layer distribution (COMPEL). COMPEL performs layer-adaptive expert pruning by estimating expert importance using Fisher information and deriving layer importance from layer-wise outlier distributions, enabling pruning decisions that capture layer-wise heterogeneity. Furthermore, to mitigate performance degradation resulting from expert pruning, we propose a Fisher information guided expert weight compensation method. Experimental results on the Qwen1.5-MoE-A2.7B achieve near lossless performance at 25% expert pruning and maintains performance within a 4% margin even at 50% pruning. Moreover, COMPEL consistently outperforms existing pruning methods while substantially reducing inference latency and peak GPU memory usage.

## 29. Revitalizing Black-Box Interpretability: Actionable Interpretability for LLMs via Proxy Models

- Authors: Junhao Liu, Haonan Yu, Zhenyu Yan, Xin Zhang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.8038790139775163
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.220/
- PDF: https://aclanthology.org/2026.acl-long.220.pdf
- Local PDF: pdf/2026-08-08_29_Revitalizing Black-Box Interpretability_ Actionable Interpretability for LLMs via Proxy Models.pdf

Post-hoc explanations provide transparency and are essential for guiding model optimization, such as prompt engineering and data sanitation. However, applying model-agnostic techniques to Large Language Models (LLMs) is hindered by prohibitive computational costs, rendering these tools dormant for real-world applications. To revitalize model-agnostic interpretability, we propose a budget-friendly proxy framework that leverages efficient models to approximate the decision boundaries of expensive LLMs. We introduce a screen-and-apply mechanism to statistically verify local alignment before deployment. Our empirical evaluation confirms that proxy explanations achieve over 90% fidelity with only 9.5% of the oracle’s cost. Building on this foundation, we demonstrate the actionable utility of our framework in prompt compression and poisoned example removal. Results show that reliable proxy explanations effectively guide optimization, transforming interpretability from a passive observation tool into a scalable primitive for LLM development. Additionally, we open-source code and datasets to facilitate future research.

## 30. TARo: Token-level Adaptive Routing for LLM Test-time Alignment

- Authors: Arushi Rai, Qiang Zhang, Hanqing Zeng, Yunkai Zhang, Dipesh Tamboli, Xiangjun Fan, Zhuokai Zhao, Lizhu Zhang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.803639066339155
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.50/
- PDF: https://aclanthology.org/2026.findings-acl.50.pdf
- Local PDF: pdf/2026-08-08_30_TARo_ Token-level Adaptive Routing for LLM Test-time Alignment.pdf

Large language models (LLMs) exhibit strong reasoning capabilities but typically require expensive post-training to reach high performance. Recent test-time alignment methods offer a lightweight alternative, but have been explored mainly for preference alignment rather than reasoning. To bridge this gap, we propose Token-level Adaptive Routing (TARo), which steers frozen LLMs toward structured reasoning entirely at inference time. Specifically, we first train reward models on step-wise mathematical traces to capture fine-grained logical consistency signals, then introduce a learnable token-level router that automatically controls the guidance of the reward model to the base model. Extensive experiments show that TARo significantly improves reasoning performance by up to +22.4% over base model and +8.4% over existing token-level test-time alignment methods, while also boosting out-of-distribution clinical reasoning (MedXpertQA) and instruction following (AlpacaEval). Furthermore, TARo also generalizes from small to large backbones without retraining, extending test-time alignment from preference optimization to robust, cross-domain reasoning.

## 31. RAG in the Wild: On the (In)effectiveness of LLMs with Mixture-of-Knowledge Retrieval Augmentation

- Authors: Ran Xu, Yuchen Zhuang, Yue Yu, Haoyu Wang, Wenqi Shi, Carl Yang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.8075575071387027
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.849/
- PDF: https://aclanthology.org/2026.findings-acl.849.pdf
- Local PDF: pdf/2026-08-08_31_RAG in the Wild_ On the (In)effectiveness of LLMs with Mixture-of-Knowledge Retrieval Augmentation.pdf

Retrieval-augmented generation (RAG) enhances large language models (LLMs) by integrating external knowledge retrieved at inference time. While RAG demonstrates strong performance on benchmarks largely derived from general-domain corpora like Wikipedia, its effectiveness under realistic, diverse retrieval scenarios remains underexplored. We evaluate RAG systems using MassiveDS, a large-scale datastore with mixture of knowledge, and identified critical limitations: retrieval mainly benefits smaller models, rerankers add minimal value, and no single retrieval source consistently excels. Moreover, current LLMs struggle to route queries across heterogeneous knowledge sources. These findings highlight the need for adaptive retrieval strategies before deploying RAG in real-world settings.

## 32. SOS-LoRA: Static Orthogonal-Subspace Low-Rank Adaptation with Fixed Multi-Scale Scaling

- Authors: Yupeng Chang, Yuan Wu, Yi Chang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.8068603616207333
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.184/
- PDF: https://aclanthology.org/2026.acl-long.184.pdf
- Local PDF: pdf/2026-08-08_32_SOS-LoRA_ Static Orthogonal-Subspace Low-Rank Adaptation with Fixed Multi-Scale Scaling.pdf

Low-Rank Adaptation (LoRA) is a widely used parameter-efficient fine-tuning (PEFT) method for large language models. Under a fixed rank budget, LoRA parameterizes each adapted weight through a single low-dimensional input-side pathway, which may couple heterogeneous behaviors through shared input directions and induce interference during optimization. We propose Static Orthogonal Subspace LoRA (SOS-LoRA), a drop-in extension that reparameterizes a rank- r tot update as a sum of K static (always-on, non-routed) low-rank experts. SOS-LoRA (i) decomposes the total rank across experts, (ii) applies a fixed multi-scale scaling scheme to encourage scale-separated optimization dynamics, and (iii) promotes diverse input-side directions via cross-expert orthogonal initialization and a lightweight regularizer. SOS-LoRA remains fully mergeable, adding no inference-time parameters or latency after merging. Experiments on reasoning and knowledge-intensive benchmarks (Llama 2/3), encoder-based NLU (GLUE), and math reasoning (GSM8K/MATH) show consistent gains over matched-budget LoRA baselines and recent variants.

## 33. AGTAO: Robust and Stabilized LLM Unlearning via Adversarial Gating Training with Adaptive Orthogonality

- Authors: Pengyu Li, Lingling Zhang, Zhitao Gao, Yanrui Wu, Yuxuan Dong, Huan Liu, Bifan Wei, Jun Liu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.8063466451656494
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.665/
- PDF: https://aclanthology.org/2026.findings-acl.665.pdf
- Local PDF: pdf/2026-08-08_33_AGTAO_ Robust and Stabilized LLM Unlearning via Adversarial Gating Training with Adaptive Orthogonality.pdf

While Large Language Models (LLMs) have achieved remarkable capabilities, they unintentionally memorize sensitive data, posing critical privacy and security risks.Machine unlearning is pivotal for mitigating these risks, yet existing paradigms face a fundamental dilemma: aggressive unlearning often induces catastrophic forgetting that degrades model utility, whereas conservative strategies risk superficial forgetting, leaving models vulnerable to adversarial recovery. To address this trade-off, we propose AGTAO (Adversarial Gating Training with Adaptive Orthogonality), a unified framework designed to reconcile robust erasure with utility preservation. Specifically, our approach introduces Adaptive Orthogonality (AO) to dynamically mitigate geometric gradient conflicts between forgetting and retention objectives, thereby minimizing unintended knowledge degradation. Concurrently, Adversarial Gating Training (AGT) formulates unlearning as a latent-space min-max game, employing a curriculum-based gating mechanism to simulate and counter internal recovery attempts. Extensive experiments demonstrate that AGTAO achieves a superior trade-off between unlearning efficacy (KUR ≈ 0.01) and model utility (MMLU 58.30).[Code is available at ." class=acl-markup-url>https://anonymous.4open.science/r/AGT-unlearning>. ].

## 34. Aligning What LLMs Do and Say: Towards Self-Consistent Explanations

- Authors: Sahar Admoni, Ofra Amir, Assaf Hallak, Yftah Ziser
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.805907359839063
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.49/
- PDF: https://aclanthology.org/2026.findings-acl.49.pdf
- Local PDF: pdf/2026-08-08_34_Aligning What LLMs Do and Say_ Towards Self-Consistent Explanations.pdf

Large language models (LLMs) seem to offer an easy path to interpretability: just ask them to explain their answers. Yet the features driving an answer often differ from those emphasized in its explanation, meaning post-hoc rationales can misrepresent what actually shaped the model’s output. We quantify this gap by comparing the feature-importance distributions of answers and their explanations. Prior analyses reveal such discrepancies, but large-scale study has been limited by the high computational cost of attribution methods. To address this, we introduce the Post-hoc Self-Consistency Bank (PSCB), a large-scale benchmark linking model decisions with diverse explanations and attribution vectors across datasets, methods, and model families. Using PSCB, we find that Spearman rank correlation provides a more reliable signal of alignment than cosine similarity. Building on this insight, we apply Direct Preference Optimization (DPO) to attribution-based preference data, improving alignment without degrading task accuracy, and show that standard supervised fine-tuning on the same data fails to achieve comparable gains. These improvements generalize robustly across domains, paving the way toward scalable and faithful alignment between LLM decisions and their natural language explanations.

## 35. APEX: Learning Adaptive Priorities for Multi-Objective Alignment in Vision-Language Generation

- Authors: Dongliang Chen, Xinlin Zhuang, Junjie Xu, Luojian Xie, Zehui Wang, Jiaxi Zhuang, Haolin Yang, Liang Dou, Xiao He, Xingjiao Wu, Ying Qian
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.8050622179604288
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.243/
- PDF: https://aclanthology.org/2026.findings-acl.243.pdf
- Local PDF: pdf/2026-08-08_35_APEX_ Learning Adaptive Priorities for Multi-Objective Alignment in Vision-Language Generation.pdf

Multi-objective alignment for text-to-image generation is commonly implemented via static linear scalarization, but fixed weights often fail under heterogeneous rewards, leading to optimization imbalance where models overfit high-variance, high-responsiveness objectives (e.g., OCR) while under-optimizing perceptual goals. We identify two mechanistic causes: variance hijacking , where reward dispersion induces implicit reweighting that dominates the normalized training signal, and gradient conflicts , where competing objectives produce opposing update directions and trigger seesaw-like oscillations. We propose APEX ( A daptive P riority-based E fficient X -objective Alignment), which stabilizes heterogeneous rewards with Dual-Stage Adaptive Normalization and dynamically schedules objectives via 𝒫 3 Adaptive Priorities that combine learning potential, conflict penalty, and progress need. On Stable Diffusion 3.5, APEX achieves improved Pareto trade-offs across four heterogeneous objectives, with balanced gains of +1.31 PickScore , +0.35 DeQA , and +0.53 Aesthetics while maintaining competitive OCR accuracy, mitigating the instability of multi-objective alignment.

## 36. SwissGov-RSD: A Human-annotated, Cross-lingual Benchmark for Token-level Recognition of Semantic Differences Between Related Documents

- Authors: Michelle Wastl, Jannis Vamvas, Rico Sennrich
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.8029868082409393
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1437/
- PDF: https://aclanthology.org/2026.acl-long.1437.pdf
- Local PDF: pdf/2026-08-08_36_SwissGov-RSD_ A Human-annotated, Cross-lingual Benchmark for Token-level Recognition of Semantic Differences Between Rel.pdf

Recognizing semantic differences across documents is crucial for text generation evaluation and content alignment, especially in cross-lingual settings. However, as a standalone task, it has received little attention. We address this by introducing SwissGov-RSD, the first naturalistic, document-level, cross-lingual dataset for semantic difference recognition. It encompasses a total of 224 multi-parallel documents in English–German, English–French, and English–Italian with token-level difference annotations by human annotators.We evaluate a variety of open-source and closed-source large language models as well as encoder models across different fine-tuning settings on this new benchmark. Our results show that current automatic approaches perform poorly compared to their performance on monolingual, sentence-level, and synthetic benchmarks, revealing a considerable gap for both LLMs and encoder models.

## 37. When 20 Agents Fail to Sort: The Distributed Sorting Benchmark for Scalable Multi-Agent Systems

- Authors: Xin Yang, Junhao Wang, Bintao Tang, Xuxin Cheng, Cao Liu, Ke Zeng, Wenyuan Jiang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.802578012989991
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1698/
- PDF: https://aclanthology.org/2026.findings-acl.1698.pdf
- Local PDF: pdf/2026-08-08_37_When 20 Agents Fail to Sort_ The Distributed Sorting Benchmark for Scalable Multi-Agent Systems.pdf

Current LLM-based multi-agent systems remain fragile under scaling, even on algorithmically trivial tasks. We introduce MAS-BENCH, a distributed-sorting benchmark that isolates coordination under explicit communication constraints: each agent observes only a local segment and must collectively produce a globally consistent order via broadcasting, peer-to-peer messaging, or a shared key-value store. Across LLM-based agents, success drops sharply as the number of agents grows, exposing persistent failures in shared state, convention alignment, and consistent termination. To mitigate these breakdowns, we propose CAMOC, a lightweight, drop-in proof-of-concept built on collaboration-aware information sharing, early global metadata exchange, and single-commit verification. CAMOC substantially improves coordination success and efficiency across backends, with the largest gains under shared-state interaction. Overall, MAS-BENCH provides a diagnostic benchmark and CAMOC offers a practical step toward more reliable large-scale LLM collaboration, highlighting a gap between individual reasoning and collective correctness.

## 38. SecureGate: Learning When to Reveal PII Safely via Token-Gated Dual-Adapters for Federated LLMs

- Authors: Mohamed Shaaban, Mohamed Elmahallawy
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.8024225701554197
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1972/
- PDF: https://aclanthology.org/2026.acl-long.1972.pdf
- Local PDF: pdf/2026-08-08_38_SecureGate_ Learning When to Reveal PII Safely via Token-Gated Dual-Adapters for Federated LLMs.pdf

Federated learning (FL) enables collaborative training across organizational silos without sharing raw data, making it attractive for privacy-sensitive applications. With the rapid adoption of large language models (LLMs), federated fine-tuning of generative LLMs has gained attention as a way to leverage distributed data while preserving confidentiality. However, this setting introduces fundamental challenges: (i) privacy leakage of personally identifiable information (PII) due to LLM memorization, and (ii) a persistent tension between global generalization and local utility under heterogeneous data. Existing defenses, such as data sanitization and differential privacy, reduce leakage but often degrade downstream performance. We propose SecureGate, a privacy-aware federated fine-tuning framework for LLMs that provides fine-grained privacy control without sacrificing utility. SecureGate employs a dual-adapter LoRA architecture: a secure adapter that learns sanitized, globally shareable representations, and a revealing adapter that captures sensitive, organization-specific knowledge. A token-controlled gating module selectively activates these adapters at inference time, enabling controlled information disclosure without retraining. Extensive experiments across multiple LLMs and real-world datasets show that SecureGate improves task utility while substantially reducing PII leakage, achieving up to a 31.66x reduction in inference attack accuracy and a 17.07x reduction in extraction recall for unauthorized requests. Additionally, it maintains 100% routing reliability to the correct adapter and incurs only minimal computational and communication overhead. Code is available at https://github.com/wsu-cyber-security-lab-ai/SecureGate .

## 39. LAD-RAG: Layout-aware Dynamic RAG for Visually-Rich Document Understanding

- Authors: Zhivar Sourati, Zheng Wang, Marianne Menglin Liu, Yazhe Hu, Mengqing Guo, Sujeeth Bharadwaj, Kyu J. Han, Tao Sheng, Sujith Ravi, Morteza Dehghani, Dan Roth
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.8015892787688856
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.724/
- PDF: https://aclanthology.org/2026.acl-long.724.pdf
- Local PDF: pdf/2026-08-08_39_LAD-RAG_ Layout-aware Dynamic RAG for Visually-Rich Document Understanding.pdf

Question answering over visually rich documents (VRDs) requires reasoning not only over isolated content but also over documents’ structural organization and cross-page dependencies. However, conventional retrieval-augmented generation (RAG) methods encode content in isolated chunks during ingestion, losing structural and cross-page dependencies, and retrieve a fixed number of pages at inference, regardless of the specific demands of the question or context. This often results in incomplete evidence retrieval and degraded answer quality for multi-page reasoning tasks. To address these limitations, we propose LAD-RAG, a novel Layout-Aware Dynamic RAG framework. During ingestion, LAD-RAG constructs a symbolic document graph that captures layout structure and cross-page dependencies, adding it alongside standard neural embeddings to yield a more holistic representation of the document. During inference, an LLM agent dynamically interacts with the neural and symbolic indices to adaptively retrieve the necessary evidence based on the query. Experiments on MMLongBench-Doc, LongDocURL, DUDE, and MP-DocVQA demonstrate that LAD-RAG improves retrieval, achieving over 90% perfect recall on average without any top- k tuning, and outperforming baseline retrievers by up to 20% in recall at comparable noise levels, yielding higher QA accuracy with minimal latency.

## 40. Tandem: Riding Together with Large and Small Language Models for Efficient Reasoning

- Authors: Zichuan Fu, Xian Wu, Guojing Li, Yejing Wang, Yijun Chen, Zhao Zihao, Luo Yixuan, Hanyu Yan, Yefeng Zheng, Xiangyu Zhao
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.8015407921685282
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.2098/
- PDF: https://aclanthology.org/2026.findings-acl.2098.pdf
- Local PDF: pdf/2026-08-08_40_Tandem_ Riding Together with Large and Small Language Models for Efficient Reasoning.pdf

Recent advancements in large language models (LLMs) have catalyzed the rise of reasoningintensive inference paradigms, where models perform explicit step-by-step reasoning before generating final answers. While such approaches improve answer quality and interpretability, they incur substantial computational overhead due to the prolonged generation sequences. In this paper, we propose Tandem, a novel collaborative framework that synergizes large and small language models (LLMs and SLMs) to achieve high-quality reasoning with significantly reduced computational cost. Specifically, the LLM serves as a strategic coordinator, efficiently generating a compact set of critical reasoning insights. These insights are then used to guide a smaller, more efficient SLM in executing the full reasoning process and delivering the final response. To balance efficiency and reliability, Tandem introduces a cost-aware termination mechanism that adaptively determines when sufficient reasoning guidance has been accumulated, enabling early stopping of the LLM’s generation. Experiments on mathematical reasoning and code generation benchmarks demonstrate that Tandem reduces computational costs by approximately 40% compared to standalone LLM reasoning, while achieving superior or competitive performance. Furthermore, the sufficiency classifier trained on one domain transfers effectively to others without retraining. The code is available at: https://github.com/Applied-MachineLearning-Lab/ACL2026_Tandem .

## 41. The Digital Dunning-Kruger Effect: Decoupling Hallucinations via Geometric Hidden-state Observation for Semantic Truthfulness

- Authors: Yueheng Mao, Min Yu, Gengwang Li, Jianguo Jiang, Gang Li, Meng Zhang, Zhen Xu, Weiqing Huang, Ming Liu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.8011210057872034
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.993/
- PDF: https://aclanthology.org/2026.acl-long.993.pdf
- Local PDF: pdf/2026-08-08_41_The Digital Dunning-Kruger Effect_ Decoupling Hallucinations via Geometric Hidden-state Observation for Semantic Truthfu.pdf

Large Language Models (LLMs) often generate overconfident yet factually incorrect hallucinations. Current detection paradigms suffer from a trade-off between the high accuracy of computationally expensive black-box methods and the inability of white-box methods to detect stubborn hallucinations. To bridge this gap, we propose GHOST (Geometric Hidden-state Observation for Semantic Truthfulness), an efficient white-box framework for hallucination detection in LLMs. We primarily target confused hallucinations marked by internal reasoning instability, while also capturing stubborn hallucinations characterized by premature layer-wise convergence as a complementary signal. By integrating internal geometric dynamics with output probability distributions, GHOST constructs a high-dimensional feature space for non-linear truthfulness classification. Extensive evaluations on FinanceBench, RAGTruth, HaluEval, and PopQA show that GHOST outperforms white-box baselines and achieves competitive black-box performance while reducing computational overhead by over 90%, offering a robust solution for real-time detection.

## 42. Long-Context Reasoning Through Proxy-Based Chain-of-Thought Tuning

- Authors: Miao Li, Irina Saparina, Alexander Gurung, Mirella Lapata
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.800841115498721
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1917/
- PDF: https://aclanthology.org/2026.acl-long.1917.pdf
- Local PDF: pdf/2026-08-08_42_Long-Context Reasoning Through Proxy-Based Chain-of-Thought Tuning.pdf

Recent large language models support inputs of up to 10 million tokens, yet they perform poorly on long-context tasks that require complex reasoning. Such tasks can be solved using only a subset of the input — a proxy context — rather than the full sequence. Despite sharing the same underlying reasoning process, models exhibit a significant performance disparity between proxy and full contexts. To improve long-context reasoning, we propose ProxyCoT, a novel training framework that transfers reasoning capabilities from short proxy contexts to full long contexts. Specifically, we first obtain high-quality chain-of-thought reasoning traces on proxy contexts through reinforcement learning or distillation from a larger teacher model, and then ground the generated traces in full long contexts with supervised fine-tuning. Experiments across different datasets demonstrate that ProxyCoT consistently outperforms strong baselines with reduced computational overhead. Furthermore, models trained with ProxyCoT generalize their long-context reasoning capabilities to out-of-domain tasks.

## 43. G-LoRA: Global-Local Decoupled Low-Rank Adaptation

- Authors: Jiahao Xiong, Yihong Huang, Yihe Liu, Xianming Hu, Hongbo Zhao, Kai Zhang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.8007947483885465
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1005/
- PDF: https://aclanthology.org/2026.findings-acl.1005.pdf
- Local PDF: pdf/2026-08-08_43_G-LoRA_ Global-Local Decoupled Low-Rank Adaptation.pdf

Low-Rank Adaptation (LoRA) has achieved remarkable progress in improving the fine-tuning efficiency and downstream performance of large language models (LLMs). Although prior work has recognized that different weight update matrices 𝛥 𝐖 exhibit varying importance and therefore should be allocated different ranks, parameters within the same update matrix are still typically constrained to a uniform rank configuration, neglecting fine-grained parameter-level heterogeneity. To address this limitation, we propose G-LoRA (Global-Local Decoupled LoRA), which decomposes each update matrix into global and local adapters. The key idea is to reorganize the rows and columns of the update matrix using a first-order Taylor approximation of parameter importance, such that highly influential parameters are clustered into a local sub-block of 𝛥 𝐖 . During training, the local adapter then focuses on this high-importance sub-region and is allocated a higher rank, whereas the global adapter captures the residual updates for the entire update matrix with relatively lower rank. By allocating higher representational capacity to more critical parameters, G-LoRA enables more efficient utilization of model resources. Extensive evaluations on benchmarks spanning commonsense reasoning, mathematical reasoning, and code generation demonstrate that G-LoRA achieves up to 2.7% absolute accuracy improvement over LoRA and its variants, validating its effectiveness for LLM fine-tuning.

## 44. SCALER: Synthetic Scalable Adaptive Learning Environment for Reasoning

- Authors: Caijun Xu, Changyi Xiao, Zhongyuan Peng, Xinrun Wang, Yixin Cao
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.8002047684147415
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1596/
- PDF: https://aclanthology.org/2026.findings-acl.1596.pdf
- Local PDF: pdf/2026-08-08_44_SCALER_ Synthetic Scalable Adaptive Learning Environment for Reasoning.pdf

Reinforcement learning (RL) offers a principled way to enhance the reasoning capabilities of large language models, yet its effectiveness hinges on training signals that remain informative as models evolve. In practice, RL progress often slows when task difficulty becomes poorly aligned with model capability or when training is dominated by a narrow set of recurring problem patterns.To jointly address these issues, we propose SCALER ( S ynthetic s C alable A daptive L earning E nvironment for R easoning), a framework that sustains effective learning signals through adaptive environment design.SCALER introduces a scalable synthesis pipeline that converts real-world programming problems into verifiable reasoning environments with controllable difficulty and unbounded instance generation, enabling RL training beyond finite datasets while preserving strong correctness guarantees. Building on this, SCALER further employs an adaptive multi-environment RL strategy that dynamically adjusts instance difficulty and curates the active set of environments to track the model’s capability frontier and maintain distributional diversity. This co-adaptation prevents reward sparsity, mitigates overfitting to narrow task patterns, and supports sustained improvement throughout training. Extensive experiments show that SCALER consistently outperforms other RL baselines across diverse reasoning benchmarks and exhibits more stable, long-horizon training dynamics.

## 45. Search-P1: Path-Centric Reward Shaping for Stable and Efficient Agentic RAG Training

- Authors: Tianle Xia, Ming Xu, Lingxiang Hu, Yiding Sun, Wenwei Li, Linfang Shang, Liqun Liu, Peng Shu, Huan Yu, Jie Jiang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.7998651627004003
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-industry.36/
- PDF: https://aclanthology.org/2026.acl-industry.36.pdf
- Local PDF: pdf/2026-08-08_45_Search-P1_ Path-Centric Reward Shaping for Stable and Efficient Agentic RAG Training.pdf

Retrieval-Augmented Generation (RAG) enhances large language models (LLMs) by incorporating external knowledge, yet traditional single-round retrieval struggles with complex multi-step reasoning.Agentic RAG addresses this by enabling LLMs to dynamically decide when and what to retrieve, but current RL-based training methods suffer from sparse outcome rewards that discard intermediate signals and low sample efficiency where failed samples contribute nothing.We propose Search-P1, a framework that introduces path-centric reward shaping for agentic RAG training, comprising two key components: (1) Path-Centric Reward, which evaluates the structural quality of reasoning trajectories through order-agnostic step coverage and soft scoring that extracts learning signals even from failed samples, and (2) Dual-Track Path Scoring with offline-generated reference planners that assesses paths from both self-consistency and reference-alignment perspectives.Experiments on multiple QA benchmarks demonstrate that Search-P1 achieves significant improvements over Search-R1 and other strong baselines, with an average accuracy gain of 7.7 points.

## 46. Schoenfeld’s Anatomy of Mathematical Reasoning by Language Models

- Authors: Ming Li, Chenrui Fan, Yize Cheng, Soheil Feizi, Tianyi Zhou
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.799531347907951
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1513/
- PDF: https://aclanthology.org/2026.acl-long.1513.pdf
- Local PDF: pdf/2026-08-08_46_Schoenfeld’s Anatomy of Mathematical Reasoning by Language Models.pdf

Large language models increasingly expose reasoning traces, yet their underlying cognitive structure and steps remain difficult to identify and analyze beyond surface-level statistics. We adopt Schoenfeld’s Episode Theory as an inductive, intermediate-scale lens and introduce ThinkARM (Anatomy of Reasoning in Models), a scalable framework that explicitly abstracts reasoning traces into functional reasoning steps such as Analysis, Explore, Implement, Verify, etc. When applied to mathematical problem solving by diverse models, this abstraction reveals reproducible thinking dynamics and structural differences between reasoning and non-reasoning models, which are not apparent from token-level views. We further present two diagnostic case studies showing that exploration functions as a critical branching step associated with correctness, and that efficiency-oriented methods selectively suppress evaluative feedback steps rather than uniformly shortening responses. Together, our results demonstrate that episode-level representations make reasoning steps explicit, enabling systematic analysis of how reasoning is structured, stabilized, and altered in modern language models.

## 47. Localized Low-Rank Adaptation within Clustered Parameter Subspaces

- Authors: Jiahao Xiong, Yihe Liu, Xianming Hu, Hongbo Zhao, Nuoyi Chen, Jie Zhang, Kai Zhang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.799132856811749
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1223/
- PDF: https://aclanthology.org/2026.acl-long.1223.pdf
- Local PDF: pdf/2026-08-08_47_Localized Low-Rank Adaptation within Clustered Parameter Subspaces.pdf

Low-Rank Adaptation (LoRA) for large language models (LLMs) has achieved significant success in various domains. So far, most algorithms in the LoRA-family rely on global low-rank factors spanning the entire update weight matrix ( 𝛥 𝐖 ). Through careful analysis, however, we observe that the 𝛥 𝐖 during fine-tuning typically exhibit heterogeneous subspace clusters, each corresponding to specific sub-sets of rows and columns. This structural heterogeneity suggests that global low-rank factors may not optimally capture the local variations needed for effective model adaptation. To address this limitation, we propose LoRA within Clustered Parameter Subspaces, or CPS-LoRA, which performs independent low-rank updates within clustered blocks of parameter matrices. The key idea is to group the rows/columns of the update matrix into locally coherent, and maximally uncorrelated subspaces, perform low-rank adaptations in each subspace, and iteratively update the partition and local adaptations. This allows adapting to local structures more precisely while preserving high efficiency. Theoretical analysis reveals that in case 𝛥 𝐖 can be partitioned into subspace blocks with non-overlapping basis, CPS-LoRA have superior parameter efficiency than global adaptations. Empirical evaluations further demonstrate better rank utilization of CPS-LoRA and its consistent improvements against LoRA (and variants) by up to 3.0% in absolute accuracy in various benchmarks.

## 48. DEFT: Demystifying VLN Failures via a Unified Dual-View Explainability Framework for LLM-based Agents

- Authors: Yawen Wang, Yihan Dai, Jianming Chen, Junjie Wang, Qing Wang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.7984322454311874
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1363/
- PDF: https://aclanthology.org/2026.acl-long.1363.pdf
- Local PDF: pdf/2026-08-08_48_DEFT_ Demystifying VLN Failures via a Unified Dual-View Explainability Framework for LLM-based Agents.pdf

Large Language Models (LLMs) have emerged as central planners in Vision-and-Language Navigation (VLN), yet their complexity increasingly obscures their internal decision-making. Existing interpretability methods typically isolate temporal criticality from feature salience, creating an alignment gap and failing to account for the behavioral instability of black-box agents. To address this, we propose DEFT, a unified dual-view framework that demystifies agent behavior by jointly analyzing when a decision is pivotal and what visual evidence grounds it. Featuring a dual-head architecture with a shared latent representation, DEFT employs a Mask Head for counterfactual-based criticality detection and an Action Head that leverages an ensemble of surrogates to recover robust visual cues. Extensive experiments on MatterPort3D across three LLM-based agents demonstrate that DEFT outperforms baselines in both temporal and feature fidelity. User studies further validate its utility, showing 78% alignment with human intuition.

## 49. EfficientLLM: Unified Pruning-Aware Pretraining for Auto-Designed Compact Language Models

- Authors: Xingrun Xing, Zheng Liu, Shitao Xiao, Boyan Gao, Yiming Liang, Haokun Lin, Xianlin Zeng, Guoqi Li, Jiajun Zhang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.798277610123354
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.355/
- PDF: https://aclanthology.org/2026.acl-long.355.pdf
- Local PDF: pdf/2026-08-08_49_EfficientLLM_ Unified Pruning-Aware Pretraining for Auto-Designed Compact Language Models.pdf

Modern large language models (LLMs) driven by scaling laws achieve emergent intelligence in large model sizes. Recently, the increasing concerns about cloud costs, latency and privacy make it an urgent requirement to develop compact edge language models. Distinguished from direct pretraining that bounded by parameter scaling law, this work proposes the unified pruning-aware pretraining, focusing on pretraining compact models while preserving performance of much larger source models, termed EfficientLLM. It features following characteristics: 1) Pruning in Pretraining Corpus: we introduce minimal parameter groups to decouple LLMs and continuously optimize model architecture with classic pruning methods like LLM-Pruner and SparseGPT during pretraining. We reveal that it achieves top-quality compact language models to scale up LLM pruning to large scale pretraining. 2) Auto-Designed Architecture: the LLM architecture is auto-designed during saliency-driven pruning, unifying pretraining, architectural design, and parameter pruning into a single process. Based on these, EfficientLLM significantly outperforms directly pretrained baselines with 100M ∼ 1B parameters, such as MobileLLM, SmolLM, Qwen2.5-0.5B, OLMo-1B, Llama3.2-1B in commen sense benchmarks, which bridges the performance gap between traditional LLM compression and direct pretraining. We open source on https://github.com/Xingrun-Xing2/EfficientLLM .

## 50. On-Policy Self-Distillation for Efficient Diffusion Language Models with Early-Stage Calibration

- Authors: Huaisheng Zhu, MingYu Liu, Junze Liu, Zhen Ge, Tian Wang, Jiri Gesi, Dakuo Wang, Weiqi Zhang, Houyu Zhang, Yufan Guo, Xian Li, Bing Yin, Sujay Sanghavi
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.798033954737173
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1344/
- PDF: https://aclanthology.org/2026.findings-acl.1344.pdf
- Local PDF: pdf/2026-08-08_50_On-Policy Self-Distillation for Efficient Diffusion Language Models with Early-Stage Calibration.pdf

Diffusion Large Language Models (DLLMs) have recently achieved strong performance, e.g., masked diffusion models (MDMs) can surpass autoregressive models (ARMs) in various tasks. However, DLLMs often struggle with inaccurate early-stage predictions due to limited context, which hinders both the model’s inference efficiency and the output’s overall quality. We propose Calibrated On-Policy Self-Distillation (COPSD) for DLLMs, a simple and efficient method to calibrate early token predictions without requiring demonstration data. COPSD distills an unnormalized target distribution derived from later decoding steps into the original model, enabling more accurate early predictions during inference. Experiments on math, planning, and RLHF tasks show that COPSD improves both effectiveness and efficiency, and further enhances performance when combined with supervised fine-tuning.

## 51. Uncertainty-Aware Test-Time Search for Optimization Problem Solving

- Authors: Linlin Yu, Xujiang Zhao, Dong Li, Yanchi Liu, Wei Cheng, Zhengzhang Chen, Chen Zhao, Feng Chen, Haifeng Chen
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.797912387564282
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1975/
- PDF: https://aclanthology.org/2026.acl-long.1975.pdf
- Local PDF: pdf/2026-08-08_51_Uncertainty-Aware Test-Time Search for Optimization Problem Solving.pdf

Automatically solving optimization problems from natural language descriptions with both efficiency and reliability is highly desirable but remains challenging. Language model hallucinations and the limited availability of labeled datasets often result in misaligned formulations, code errors, and feasibility failures We propose UMCTS , an Uncertainty-aware Monte Carlo Tree Search framework that combines the language understanding capability of large language models with the reliability of well-established solvers. UMCTS structures the solution process into four stages: global instruction, assumptions, mathematical formulation, and solver code generation. It employs Monte Carlo Tree Search with semantic-equivalence pruning, prior-guided exploration, and solver-based feasibility checks. An LLM judge provides numerical reward signals, qualitative error information, and uncertainty estimates. These signals are backpropagated to guide the search and flag unreliable outputs. Across six public benchmarks, UMCTS achieves state-of-the-art solution accuracy, improves efficiency by reducing token usage.

## 52. EvoCoT: Overcoming the Exploration Bottleneck in Reinforcement Learning for LLMs

- Authors: Huanyu Liu, Jia Li, Yihong Dong, Chang Yu, Taozhi Chen, Lecheng Wang, Yongding Tao, Bin Gu, Ge Li
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.797738034718224
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1031/
- PDF: https://aclanthology.org/2026.findings-acl.1031.pdf
- Local PDF: pdf/2026-08-08_52_EvoCoT_ Overcoming the Exploration Bottleneck in Reinforcement Learning for LLMs.pdf

Reinforcement learning with verifiable reward (RLVR) has become a promising paradigm for post-training large language models (LLMs) to improve their reasoning capability. However, when the rollout accuracy is low on hard problems, the reward becomes sparse, limiting learning efficiency and causing exploration bottlenecks. Existing approaches either rely on teacher models for distillation or filter out difficult problems, which limits scalability or restricts reasoning improvement through exploration.We propose EvoCoT, a self-evolving curriculum learning framework based on two-stage chain-of-thought (CoT) reasoning optimization. EvoCoT constrains the exploration space by self-generating and verifying CoT trajectories, then gradually shortens CoT steps to expand the space in a controlled way. The framework enables LLMs to stably learn from initially unsolved hard problems under sparse rewards. We apply EvoCoT to multiple LLM families, including Qwen, DeepSeek, and Llama. Experiments show that EvoCoT enables LLMs to solve previously unsolved problems, improves reasoning capability without external CoT supervision, and is compatible with various RL fine-tuning methods. We release the source code to support future research.

## 53. Position: From Noise to Signal to Selbstzweck - Reframing Human Label Variation in the Era of Post-training in NLP

- Authors: Shanshan Xu, Santosh T.Y.S.S, Barbara Plank
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.7974509250496142
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1190/
- PDF: https://aclanthology.org/2026.findings-acl.1190.pdf
- Local PDF: pdf/2026-08-08_53_Position_ From Noise to Signal to Selbstzweck - Reframing Human Label Variation in the Era of Post-training in NLP.pdf

Human Label Variation (HLV) refers to legitimate disagreement in annotation that reflects the diversity of human perspectives rather than mere error. Long treated in NLP as noise to be eliminated, HLV has only recently been reframed as a signal for improving model robustness. With the rise of large language models (LLMs) and post-training methods such as human feedback-based alignment, the role of HLV has become increasingly consequential. Yet current preference-learning datasets routinely collapse multiple annotations into a single label, flattening diverse perspectives into artificial consensus. Preserving HLV is necessary not only for pluralistic alignment but also for sociotechnical safety evaluation, where model behavior must be assessed in relation to human interaction and societal context.This position paper argues that preserving HLV as an embodiment of human pluralism must be treated as a Selbstzweck , an intrinsic value in itself. We analyze the limitations of existing preference datasets and propose actionable strategies for incorporating HLV into dataset construction to better preserve pluralistic human values.

## 54. Agentic Episodic Control

- Authors: Xidong Yang, Wenhao Li, Junjie Sheng, Yun Hua, Haosheng Chen, Chuyun Shen, Xiangfeng Wang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.7971399569267
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.654/
- PDF: https://aclanthology.org/2026.findings-acl.654.pdf
- Local PDF: pdf/2026-08-08_54_Agentic Episodic Control.pdf

Reinforcement learning (RL) remains fundamentally limited by poor data efficiency and weak generalization. Prior episodic RL methods attempt to alleviate this via external memory modules, yet they suffer from two key limitations: a representation bottleneck caused by shallow encoders, and a retrieval dilemma where episodic memory is accessed indiscriminately.To address these challenges, we propose Agentic Episodic Control (AEC), a novel architecture that integrates large language models (LLMs) into episodic RL.AEC uses an LLM-based semantic augmenter to generate semantic representations from raw observations, and a critical state recognizer to selectively retrieve valuable experiences.This transforms memory usage from passive similarity matching into strategic, context-aware recall.Across five BabyAI-Text environments, AEC achieves 2–6× higher data efficiency than baselines and is the only method to solve complex tasks like UnlockLocal with over 90% success.It further demonstrates strong cross-task and cross-environment generalization, maintaining performance even under distribution shifts.AEC shows that combining LLM-derived priors with reinforcement learning yields more sample-efficient and adaptable agents. Code is available at https://github.com/Xidong-Yang/Agentic_Episodic_Control .

## 55. The GaoYao Benchmark: A Comprehensive Framework for Evaluating Multilingual and Multicultural Abilities of Large Language Models

- Authors: Yilun Liu, Chunguang Zhao, Mengyao Piao, Lingqi Miao, Shimin Tao, Minggui HE, Chenxin Liu, Zhang Li, Mahongxia, Jiaxin Guo, Chen Liu, Liqun Deng, Jiansheng Wei, Xiaojun Meng, Fanyi Du, Daimeng Wei, Yanghua Xiao
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.7968993059317757
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.977/
- PDF: https://aclanthology.org/2026.acl-long.977.pdf
- Local PDF: pdf/2026-08-08_55_The GaoYao Benchmark_ A Comprehensive Framework for Evaluating Multilingual and Multicultural Abilities of Large Languag.pdf

Evaluating the multilingual and multicultural capabilities of Large Language Models (LLMs) is essential for their global utility. However, current benchmarks face three critical limitations: (1) fragmented evaluation dimensions that often neglect deep cultural nuances; (2) insufficient language coverage in subjective tasks relying on low-quality machine translation; and (3) shallow analysis that lacks diagnostic depth beyond simple rankings. To address these, we introduce GaoYao, a comprehensive benchmark with 182.3k samples, 26 languages and 51 nations/areas. First, GaoYao proposes a unified framework categorizing evaluation tasks into three cultural layers (General Multilingual, Cross-cultural, Monocultural) and nine cognitive sub-layers. Second, we achieve native-quality expansion by leveraging experts to rigorously localize subjective benchmarks into 19 languages and synthesizing cross-cultural test sets for 34 cultures, surpassing prior coverage by up to 111%. Third, we conduct an in-depth diagnostic analysis on 20+ flagship and compact LLMs. Our findings reveal significant geographical performance disparities and distinct gaps between tasks, offering a reliable map for future work. We release the benchmark.

## 56. RanLoRA: Residual-aware Nonlinear Low-Rank Adaptation

- Authors: Xu Luo, Yongbin Liu, Chunping Ouyang, Ying Yu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.7967760950530822
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.852/
- PDF: https://aclanthology.org/2026.findings-acl.852.pdf
- Local PDF: pdf/2026-08-08_56_RanLoRA_ Residual-aware Nonlinear Low-Rank Adaptation.pdf

Low-Rank Adaptation (LoRA) is a widely adopted approach for parameter-efficient fine-tuning of large language models, enabling effective adaptation with a small number of trainable parameters. However, its reliance on linear low-rank projections restricts adaptation to linear subspaces, which can limit flexibility on complex downstream tasks. To address this, we propose RanLoRA, a Residual-aware nonlinear Low-Rank Adaptation approach that leverages the decomposition structure of pretrained weights. We used Singular Value Decomposition (SVD) to decompose pretrained weights into principal components that are kept frozen and residual components that are used for task-specific adaptation. To enhance the expressiveness of linear low-rank updates, RanLoRA incorporates a nonlinear activation layer together with a Hadamard-product-based vector modulation. This design supports an implicit progressive adaptation behavior, where optimization evolves from coarse approximation of dominant components toward residual alignment and fine-grained nonlinear refinement. Experiments on benchmarks covering commonsense reasoning, natural language understanding, image classification, and mathematical reasoning show that RanLoRA consistently outperforms vanilla LoRA and representative variants under comparable parameter budgets. These results suggest that incorporating structured nonlinearity into adapter design can enhance representational flexibility and generalization across tasks in large models.

## 57. APEX-MEM: Agentic Semi-Structured Memory with Temporal Reasoning for Long-Term Conversational AI

- Authors: Pratyay Banerjee, Masud Moshtaghi, Shivashankar Subramanian, Amita Misra, Ankit Chadha
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.7967339431252762
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.749/
- PDF: https://aclanthology.org/2026.acl-long.749.pdf
- Local PDF: pdf/2026-08-08_57_APEX-MEM_ Agentic Semi-Structured Memory with Temporal Reasoning for Long-Term Conversational AI.pdf

Large language models still struggle with reliable long-term conversational memory: simply enlarging context windows or applying naïve retrieval often introduces noise and destabilizes responses. We present APEX-MEM, a conversational memory system that combines three key innovations: (1) a property graph which use domain-agnostic ontology to structure conversations as temporally grounded events in an entity-centric framework, (2) append-only storage that preserves the full temporal evolution of information, and (3) a multi-tool retrieval agent that understands and resolves conflicting or evolving information at query time, producing a compact and contextually relevant memory summary. This retrieval-time resolution preserves the full interaction history while suppressing irrelevant details. APEX-MEM achieves 88.88% accuracy on LOCOMO and 86.2% on LongMemEval, outperforming state-of-the-art session-aware approaches and demonstrating that structured property graphs enable more temporally coherent long-term conversational reasoning.

## 58. QuDAR: Query-Wise Dual-Perspective Adaptive Retrieval

- Authors: Joeun Kim, Seunghyouk Yoon, Xuan-Bach Le, Youngeun Nam, Doyoung Kim, Hwanjun Song, Jae-Gil Lee
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.7966501954245535
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1791/
- PDF: https://aclanthology.org/2026.acl-long.1791.pdf
- Local PDF: pdf/2026-08-08_58_QuDAR_ Query-Wise Dual-Perspective Adaptive Retrieval.pdf

Retrieval-augmented generation(RAG) systems depend on retrieval modules to supply grounding evidence for large language models. While hybrid approaches combining sparse and dense retrievers improve performance, most rely on fixed weights that ignore query-specific and corpus-specific variation. Similarly, query expansion has long been used to enrich recall, but its integration with original queries is usually static and can introduce noise. We present QuDAR, a dual-perspective adaptive retrieval framework that adapts along two perspectives: retriever type (sparse vs. dense) and query format (original vs.expanded). Leveraging margin-derived confidence (e.g., top-1–top-2 score gaps) and blind LLM-based relevance scoring, QuDAR dynamically assigns query-specific weights, fusing lexical specificity with semantic breadth while mitigating noise. QuDAR is lightweight, retriever-agnostic, and broadly applicable. Experiments show consistent gains over static baselines, improving overall retrieval quality and yielding more stable performance across queries.

## 59. Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection

- Authors: Xiao Pu, Zepeng Cheng, Lin Yuan, Yu Wu, Xiuli Bi
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.796472997899204
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.120/
- PDF: https://aclanthology.org/2026.acl-long.120.pdf
- Local PDF: pdf/2026-08-08_59_Breaking the Generator Barrier_ Disentangled Representation for Generalizable AI-Text Detection.pdf

As large language models (LLMs) generate text that increasingly resembles human writing, the subtle cues that distinguish AI-generated content from human-written content become increasingly challenging to capture. Reliance on generator-specific artifacts is inherently unstable, since new models emerge rapidly and reduce the robustness of such shortcuts. This generalizes unseen generators as a central and challenging problem for AI-text detection. To tackle this challenge, we propose a progressively structured framework that disentangles AI-detection semantics from generator-aware artifacts. This is achieved through a compact latent encoding that encourages semantic minimality, followed by perturbation-based regularization to reduce residual entanglement, and finally a discriminative adaptation stage that aligns representations with task objectives. Experiments on MAGE benchmark, covering 20 representative LLMs across 7 categories, demonstrate consistent improvements over state-of-the-art methods, achieving up to 24.2% accuracy gain and 26.2% F 1 improvement. Notably, performance continues to improve as the diversity of training generators increases, confirming strong scalability and generalization in open-set scenarios. Our source code will be publicly available at https://github.com/PuXiao06/DRGD .

## 60. CCD: Mitigating Hallucinations in Radiology MLLMs via Clinical Contrastive Decoding

- Authors: Xi Zhang, Zaiqiao Meng, Jake Lever, Edmond S. L. Ho
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.7963365472824346
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1755/
- PDF: https://aclanthology.org/2026.findings-acl.1755.pdf
- Local PDF: pdf/2026-08-08_60_CCD_ Mitigating Hallucinations in Radiology MLLMs via Clinical Contrastive Decoding.pdf

Multimodal large language models (MLLMs) have recently achieved remarkable progress in radiology by integrating visual perception with natural language understanding. However, they often generate clinically unsupported descriptions, known as medical hallucinations, which pose serious risks in medical applications that demand accuracy and image-grounded outputs. Through empirical analysis, we find that prompt-induced hallucinations remain prevalent in radiology MLLMs, largely due to over-sensitivity to clinical sections. To address this, we introduce C linical C ontrastive D ecoding ( CCD ), a training-free and retrieval-free inference framework that integrates structured clinical signals from task-specific radiology expert models. CCD introduces a dual-stage contrastive mechanism to refine token-level logits during generation, thereby enhancing clinical fidelity without modifying the base MLLM. Experiments on three datasets and multiple models demonstrate that CCD consistently improves overall performance on radiology report generation (RRG). On the MIMIC-CXR dataset, it yields up to a 17% improvement in RadGraph-F1 when applied to state-of-the-art RRG models. Our approach provides a lightweight and generalisable solution for mitigating medical hallucinations, effectively bridging expert models and MLLMs in radiology.
