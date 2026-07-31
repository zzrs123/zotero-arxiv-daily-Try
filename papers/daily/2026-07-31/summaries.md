# Paper Daily Reading - 2026-07-31

## 1. Toward a Unified Statistical Theory of Unsupervised Pretraining and Supervised Neural Knowledge Graph Learning

- Authors: Jifan Zhang, Miklos Racz, Suqi Liu
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-28
- DOI: Unavailable
- Categories: math.ST, cs.SI, stat.ME, stat.ML
- Relevance: 3.7464033585548924
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.26346v1
- PDF: https://arxiv.org/pdf/2607.26346v1
- Local PDF: pdf/2026-07-31_01_Toward a Unified Statistical Theory of Unsupervised Pretraining and Supervised Neural Knowledge Graph Learning.pdf

Knowledge graph learning provides a powerful framework for representing and inferring structured knowledge, with broad practical applications. However, the scarcity of relation-specific labeled triples per entity hinders the training of expressive models, and the ad hoc design of scoring functions limits generalizability and lacks theoretical grounding. We address both issues with a theoretically grounded, end-to-end training framework that extends and subsumes existing methods. Our framework is a two-stage procedure: unsupervised pretraining over heterogeneous corpora followed by supervised learning with multiple relation types. We establish a nonasymptotic risk bound that disentangles pretraining representation error from labeled-sample complexity, formally quantifying the benefit of large-scale unlabeled data for downstream knowledge prediction. Synthetic experiments validate each theoretical component, and real-world experiments confirm the effectiveness of our approach on large-scale knowledge graph benchmarks.

## 2. RKMR: A Rapid Kernel Machine Regression Framework for Optimal Marker Detection in Spatial Omics Data

- Authors: Seal, S., Neelon, B., Chakraborty, A., Mattila, C., Rubinstein, M., Chung, D., Angel, P., Ghosh, D.
- Source: biorxiv
- Venue type: preprint
- Journal: biorxiv
- Publication status: preprint
- Publication date: 2026-07-30
- DOI: 10.64898/2026.07.27.740999
- Categories: bioinformatics
- Relevance: 3.5470273369388963
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://www.biorxiv.org/content/10.64898/2026.07.27.740999v1.full.pdf
- PDF: https://www.biorxiv.org/content/10.64898/2026.07.27.740999v1.full.pdf
- Local PDF: pdf/2026-07-31_02_RKMR_ A Rapid Kernel Machine Regression Framework for Optimal Marker Detection in Spatial Omics Data.pdf

High-throughput spatial omics technologies enable molecular profiling within intact tissue architecture, yet identifying concise, predictive, and biologically interpretable marker panels for cell types, tissue domains, and disease-associated tissue classes remains challenging. This limitation hinders the development of actionable panels for targeted validation and downstream translation. Existing pipelines rely largely on univariate differential-expression analyses, which ignore joint molecular structure and provide limited predictive insight. Multivariate machine-learning methods, including random forest, XGBoost, elastic net, and specialized single-cell panel-selection approaches, can capture predictive patterns but typically lack explicit spatial modeling and probabilistic feature selection, relying instead on model-specific importance scores or user-specified panel sizes. We develop rapid kernel machine regression (RKMR), a scalable framework for spatial-omics marker discovery that integrates nonlinear kernel modeling, spike-and-slab variable selection, and spatial dependence. RKMR uses automatic relevance determination (ARD) kernels and sparsity-inducing priors to capture nonlinear marker-outcome relationships and implicit feature interactions while producing approximate posterior inclusion probabilities (PIPs) that quantify model-based uncertainty in feature inclusion. To scale inference to large spatial datasets, RKMR combines low-rank kernel approximations with stochastic variational optimization. In simulations, RKMR consistently achieves higher AUPRC than competing methods across a range of molecular-signal and spatial-effect settings. Across spatial transcriptomics and scRNA-seq datasets, RKMR identifies parsimonious marker sets that recover reported cell-type signatures and reproducible tissue-layer markers. These results establish RKMR as a scalable and uncertainty-aware framework for translating high-dimensional spatial omics data into robust, experimentally actionable marker panels.

## 3. LLM-powered Functional Gene Set Summarization with genesetGPT

- Authors: Leary, J. R., Pattey, S., Bacher, R.
- Source: biorxiv
- Venue type: preprint
- Journal: biorxiv
- Publication status: preprint
- Publication date: 2026-07-30
- DOI: 10.64898/2026.07.27.741117
- Categories: genomics
- Relevance: 3.5134838483346553
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://www.biorxiv.org/content/10.64898/2026.07.27.741117v1.full.pdf
- PDF: https://www.biorxiv.org/content/10.64898/2026.07.27.741117v1.full.pdf
- Local PDF: pdf/2026-07-31_03_LLM-powered Functional Gene Set Summarization with genesetGPT.pdf

Transcriptomics datasets generated using next-generation sequencing techniques such as single cell RNA-sequencing (scRNA-seq) and spatially-resolved transcriptomics (SRT) allow researchers to study patterns in gene expression across celltypes, temporal processes, and spatial organization at ever-higher resolutions and depths. scRNA-seq analyses produce gene expression profiles and celltype-specific gene sets that require annotation to provide biological meaning, a process that has traditionally relied on the manual interpretations of clinical scientists. Similarly, SRT experiments typically require subjective, time-consuming annotation of spatial domains. Recent advances in large language model (LLM) methods offer opportunities to assist in the interpretation of such datasets. Many current LLM-based approaches aim to annotate transcriptomics-derived gene sets by integrating information from publicly available and online biological resources. While these approaches can be effective, they often struggle when presented with weakly-related or fully uncorrelated genes, sometimes inferring and justifying biological relationships that are not supported by existing literature. Additionally, the quality of LLM-generated interpretations is dependent on the provision of appropriate biological context and careful prompt design, both of which can present significant barriers to effective use. To address these limitations we propose genesetGPT, an efficient, LLM-based framework that emphasizes both curated biological context and iterative prompt construction, thus enabling realistic summarization of heterogeneous gene sets at scale. genesetGPT is implemented as an open-source Python package available for download at https://github.com/jr-leary7/genesetGPT.

## 4. AgentGFM: A Graph Foundation Model with Node-Agent Information-Flow Control

- Authors: Jingbo Cui, Jitao Zhao, Di Jin, Dongxiao He
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-29
- DOI: Unavailable
- Categories: cs.LG, cs.AI
- Relevance: 3.477212704620377
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.26533v1
- PDF: https://arxiv.org/pdf/2607.26533v1
- Local PDF: pdf/2026-07-31_04_AgentGFM_ A Graph Foundation Model with Node-Agent Information-Flow Control.pdf

Graph Foundation Models (GFMs) aim to learn transferable knowledge from multi-domain graphs and adapt to unseen scenarios. As a fundamental source of relational semantics in graphs, the transferability of topological patterns has long been central to GFM research. However, local structural patterns may vary across graphs and even among nodes within the same graph. Despite such structural variation, most existing GFMs rely on manually designed propagation schemes and apply them to new graphs largely unchanged. Such fixed schemes may not suit the diverse structural patterns of different nodes. This raises a key question: can each node autonomously determine how information should be propagated through the graph? We refer to this capability as information-flow control. Inspired by recent advances in agent technology, we formulate this problem as agent-based decision making and treat each node as an agent. Accordingly, we propose AgentGFM, in which all node agents follow a shared end-to-end trainable policy rather than using independent models. For adaptive information-flow control, each node interacts with the graph through a predict-act-observe-correct process. During the act stage, the node makes three decisions: source reception, signal-channel selection and gain-aware node-wise halting. The resulting observation is compared with the prediction and their discrepancy is used to correct the node state and guide subsequent interactions. Extensive experiments across node-level, graph-level and large-scale transfer scenarios demonstrate the effectiveness of AgentGFM across diverse graph topologies.

## 5. Scale-Aware Compositional Inference Improves Reproducibility and Uncovers Convergent Aging Programs in Spatial Transcriptomics

- Authors: Parmaksiz, D., Manjila, S. B., McGovern, K., Shin, D., Bjerke, I. E., Paul, A., Silverman, J., Kim, Y.
- Source: biorxiv
- Venue type: preprint
- Journal: biorxiv
- Publication status: preprint
- Publication date: 2026-07-30
- DOI: 10.64898/2026.07.27.740958
- Categories: genomics
- Relevance: 3.438348441236024
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://www.biorxiv.org/content/10.64898/2026.07.27.740958v1.full.pdf
- PDF: https://www.biorxiv.org/content/10.64898/2026.07.27.740958v1.full.pdf
- Local PDF: pdf/2026-07-31_05_Scale-Aware Compositional Inference Improves Reproducibility and Uncovers Convergent Aging Programs in Spatial Transcrip.pdf

Spatial transcriptomics enables analysis of molecular organization with anatomical context. Existing spatial differential expression methods are restricted to within-sample inference, forcing between-sample comparisons to rely on approaches adapted from single-cell RNA-seq. Here, we establish a scale-aware inference framework for spatial differential expression by modeling compositional constraints and variation in total RNA abundance rather than removing them through normalization, enabling calibrated between-sample inference at cell-level resolution. Our method produces more reliable results in simulated data and different spatial platforms. When applied to aged mouse brains, the analysis reveals converging aging-associated programs involving cellular signaling, membrane homeostasis, and neurovasculature across independent datasets.

## 6. Temporally Centered SIGReg Improves Multi-Task LeWorldModel Learning: From Analysis to Method

- Authors: Chang Liu, Fei Suo, Yanzhou Jin, Yusuke Iwasawa, Yutaka Matsuo, Yaonan Zhu
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-29
- DOI: Unavailable
- Categories: cs.LG, cs.RO
- Relevance: 3.2893578817069704
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.26924v1
- PDF: https://arxiv.org/pdf/2607.26924v1
- Local PDF: pdf/2026-07-31_06_Temporally Centered SIGReg Improves Multi-Task LeWorldModel Learning_ From Analysis to Method.pdf

Recent work on LeWorldModel (LeWM) has shown that the Sketched Isotropic Gaussian Regularizer (SIGReg) enables stable end-to-end world-model learning from pixels by regularizing the latent marginal distribution toward an isotropic Gaussian, thereby preventing representation collapse. While effective and elegant in single-task settings, this recipe does not extend reliably to multi-task training, leading to substantially worse downstream behavior-cloning performance. In this paper, we show that marginal Gaussianization compresses the separation between task-dependent latent clusters relative to within-cluster variation. This compression introduces representation aliasing across tasks and states, and makes the learned representations highly sensitive to small visual perturbations. To address this problem, we apply SIGReg to temporally centered residuals rather than to the latent marginal distribution. This surrogate target places no direct regularization pressure on the separation among cluster centers, removes the requirement that the full latent follow a single isotropic Gaussian, and retains the anti-collapse effect of SIGReg. On the LIBERO benchmark, our method improves downstream success on the long-horizon suite by 1.7x and raises the average success rate across four suites from 53.2% to 73.6%. Without external pretraining, it slightly outperforms Diffusion Policy trained from scratch and approaches the performance of large-scale pretrained policy baselines. These results reveal a structural incompatibility between marginal Gaussian priors and multi-task latent structure, and provide a simple route toward stable and scalable end-to-end multi-task world-model learning.

## 7. Using large language models to probe the limits of atom-centered structural descriptors

- Authors: Michelangelo Domina, Michele Ceriotti
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-29
- DOI: Unavailable
- Categories: physics.chem-ph, cs.LG
- Relevance: 3.2758075860380584
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.26984v1
- PDF: https://arxiv.org/pdf/2607.26984v1
- Local PDF: pdf/2026-07-31_07_Using large language models to probe the limits of atom-centered structural descriptors.pdf

Mapping an atomic structure to a compact set of geometric descriptors is an essential step in any machine-learning application to atomic-scale modeling. A powerful and widely-used approach can be understood as a discretization of the histogram of pair distances, triangles, etc., that results in a hierarchy of symmetry-invariant atom-centered descriptors. Unfortunately, the lower rungs on this hierarchy (two, three, four-neighbor clusters) were found to be incomplete, with symmetry-unrelated pairs of structures having exactly the same descriptors. However, all the ``descriptor degeneracies'' reported so far are resolved by considering larger clusters of neighbors to build the descriptors. We report examples of 3D structures that are indistinguishable even if one considers clusters of up to seven neighbors, and to arbitrary order when considering a practical level of discretization of the descriptors, discovered with the assistance of large language models. The key ingredients in their construction can be traced to results that have been known for decades in different communities; the model was able to find the references and recognize their significance for the problem at hand. We believe this experiment exposes an extremely fruitful usage pattern for AI in science: translating results between different communities and application domains, accelerating the process by which serendipitous discoveries in a field become paradigm-shifting breakthroughs in another.

## 8. Anatomy Contextualized Adaption of CT Foundation Models

- Authors: Roshan Kenia, Stephanie L McNamara, William Lotter
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-29
- DOI: Unavailable
- Categories: cs.CV, cs.AI
- Relevance: 3.1705263282182097
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.27154v1
- PDF: https://arxiv.org/pdf/2607.27154v1
- Local PDF: pdf/2026-07-31_08_Anatomy Contextualized Adaption of CT Foundation Models.pdf

CT vision-language foundation models have demonstrated promising performance across downstream tasks, but are typically trained with whole-volume representations that dilute fine-grained anatomical signals. Fine-grained vision-language pre-training addresses this by aligning anatomy-level visual features with anatomy-specific text, but in doing so discards the global context that whole-volume models provide. Furthermore, existing fine-grained approaches train from scratch, making them computationally expensive. We introduce Anatomy Contextualized Adaptation (ACA), a lightweight framework that adapts frozen CT foundation model representations for anatomy-level vision-language alignment while enhancing global contextualization. ACA uses TotalSegmentator to decompose CT volumes into anatomy-level embeddings, which are refined via a transformer that captures cross-anatomy relationships, and aligned to both per-anatomy and scan-level text extracted from radiology reports. Evaluated on Merlin and CT-RATE, ACA consistently outperforms both the frozen foundation model baselines and existing fine-grained methods in zero-shot finding classification, while requiring less than one hour of training once embeddings are cached. The attention weights learned by ACA's inter-anatomy transformer additionally indicate plausible cross-anatomy context routing. Altogether, these results support ACA as a lightweight approach for adapting CT foundation models to anatomically grounded vision-language alignment while preserving and enhancing global anatomical context.

## 9. High-Order Markov Blanket Discovery via a k-Order Relaxation of the Faithfulness Assumption

- Authors: Loong Kuan Lee, Ragavi Krishnamoorthy, Nico Piatkowski
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-29
- DOI: Unavailable
- Categories: cs.LG, cs.AI, stat.ML
- Relevance: 3.097034466903038
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.26357v1
- PDF: https://arxiv.org/pdf/2607.26357v1
- Local PDF: pdf/2026-07-31_09_High-Order Markov Blanket Discovery via a k-Order Relaxation of the Faithfulness Assumption.pdf

The problem of learning the graphical Markov blanket (MB) of a variable from data has applications in many areas such as structure learning for Bayesian networks and Markov random fields, causal discovery, and feature selection. However, a common assumption most methods make is that the conditional independencies in the distribution imply the same separation in the graphical structure -- also known as the faithfulness assumption. Unfortunately, this assumption can be violated by higher-order dependencies such as XOR and parity-type relations, and -- on finite samples -- by empirical violations that, in extreme cases, even induce spurious dependencies absent from the true distribution. Therefore, in this paper we propose a "k-order" relaxation of the faithfulness assumption that captures parity type relationships between k+2 variables. We then propose a proof of concept algorithm called k-order Markov blanket (kOMB) that uses this relaxation for MB discovery. Finally, we empirically show how kOMB can recover the MB of a variable under both true and empirical violations of faithfulness. Code available at: https://github.com/lklee9/k-order-Markov-blanket

## 10. TraceCLIP: Recovering Local Semantics from Patch-to-CLS Contributions

- Authors: Xinran Liu, Shouqian Shi, Yutong Chen, Ge Wang, Xin-Wei Yao, Sheng Zhong
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-28
- DOI: Unavailable
- Categories: cs.CV, cs.AI
- Relevance: 3.0760750935183645
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.26107v1
- PDF: https://arxiv.org/pdf/2607.26107v1
- Local PDF: pdf/2026-07-31_10_TraceCLIP_ Recovering Local Semantics from Patch-to-CLS Contributions.pdf

Dense vision-language understanding, including object localization, region recognition, and open-vocabulary semantic segmentation, requires associating language concepts with spatially grounded visual regions. CLIP provides a strong foundation for these tasks by learning a shared image-text embedding space from large-scale contrastive pre-training. However, its image-level objective aligns text with a CLS-derived global representation, leaving local vision-language correspondence only indirectly constrained. Existing methods either introduce additional supervision, external models, or task-specific adaptation, while training-free approaches mainly recover dense responses from existing patch features without examining where local semantics become most accessible within CLIP. We introduce TraceCLIP, a training-free framework that recovers latent patch-level semantic evidence by isolating the patch-specific terms written into the CLS attention output. TraceCLIP further converts contribution-derived semantic responses into a semantic-geodesic topology gate that calibrates final-layer patch affinity for dense feature reconstruction. Diagnostic experiments show that these contribution features exhibit strong local semantic discrimination and text-conditioned spatial alignment. On eight zero-shot semantic segmentation benchmarks, TraceCLIP achieves gains of 1.3 to 4.5 points in average mIoU over the strongest prior training-free methods across both backbones and background settings, without additional training, external vision foundation models, or region-level supervision. More broadly, these findings suggest that spatially localized semantics may remain accessible within the internal construction of globally aligned representations.

## 11. UrbanDS: A Graph-Guided LLM Multi-Agent System for Data-Intensive Urban Tasks

- Authors: Zhilun Zhou, Jianghao Yu, Yuming Lin, yongjun yang, Sun Yongquan, Depeng Jin, Yong Li
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-29
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 3.071195502473354
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.26724v1
- PDF: https://arxiv.org/pdf/2607.26724v1
- Local PDF: pdf/2026-07-31_11_UrbanDS_ A Graph-Guided LLM Multi-Agent System for Data-Intensive Urban Tasks.pdf

Large language model (LLM) agents have been widely applied in automating data science tasks. However, existing methods typically rely on a limited set of provided datasets, and they face challenges in data-intensive scenarios that require discovering and leveraging relevant information from large-scale and heterogeneous data repositories. Urban tasks are representative examples of such scenarios, as urban data are not only large-scale and multi-sourced, but also exhibit complex spatial, temporal, and semantic relationships. To address these challenges, we propose UrbanDS, a graph-guided LLM multi-agent system for data-intensive urban tasks. We first construct a unified dataset graph to organize reusable dataset skills and the relationships among datasets. Specifically, we develop a Data Profiling Agent that constructs a skill for each dataset. Moreover, a Relation Agent identifies relationships among datasets and integrates these relationships into the dataset graph. At runtime, a Planner Agent retrieves task-relevant datasets from the graph and generates execution plans. Multiple Execution Agents then perform data processing and analysis, while their execution progress and intermediate results are shared through a common memory. Finally, a Report Agent synthesizes the experimental logs into a report, which can be further refined based on user feedback. To systematically evaluate the capability of agents in handling data-intensive urban scenarios, we further construct UrbanDS-Bench, an urban data science benchmark covering representative data analysis and modeling tasks. Experiments on both general and urban benchmarks demonstrate that UrbanDS consistently outperforms existing data science agents on data-intensive tasks. Furthermore, UrbanDS has been deployed on the urban operations platform of Dongxihu District, Wuhan, demonstrating its effectiveness in real-world urban applications.

## 12. Progressive Multimodal Alignment for Continual Instruction Tuning

- Authors: Duzhen Zhang, Yahan Yu, Qiaoyi Su, Jiahua Dong, Tielin Zhang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-29
- DOI: Unavailable
- Categories: cs.CV, cs.AI
- Relevance: 3.0618911721164714
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.26947v1
- PDF: https://arxiv.org/pdf/2607.26947v1
- Local PDF: pdf/2026-07-31_12_Progressive Multimodal Alignment for Continual Instruction Tuning.pdf

Multimodal Large Language Models (MLLMs) rely on a projector to align visual representations with the language embedding space, making it central to cross-modal understanding. In Multimodal Continual Instruction Tuning (MCIT), however, shifting visual distributions and evolving instruction semantics cause this shared projector to drift, leading to projector-level forgetting, an issue largely overlooked by methods that focus primarily on the LLM backbone. We introduce Progressive Multimodal Alignment (PMA), a framework that enables the projector to adapt continually while preserving previously learned alignment. PMA detects multimodal distribution shifts via a lightweight representation descriptor and progressively expands projector experts only when needed. An expandable router integrates expert outputs based on multimodal features, while the original pretrained projector is retained as a stable alignment anchor. This progressive mechanism balances stability and plasticity with sub-linear parameter growth and serves as a method-agnostic add-on to existing MCIT approaches. Extensive experiments on two recent MCIT benchmarks demonstrate that mitigating projector-level forgetting yields consistent gains over prior state-of-the-art methods when combined with PMA. Moreover, PMA scales across diverse MLLM backbones, demonstrating robust and broadly applicable MCIT performance.

## 13. Neural Architecture Search for Traffic Prediction: A Survey of Methods, Challenges, and Future Directions

- Authors: Truong Giang Vu, Li Yang, Richard W. Pazzi
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-29
- DOI: Unavailable
- Categories: cs.LG, cs.NE
- Relevance: 3.0581143888787694
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.26467v1
- PDF: https://arxiv.org/pdf/2607.26467v1
- Local PDF: pdf/2026-07-31_13_Neural Architecture Search for Traffic Prediction_ A Survey of Methods, Challenges, and Future Directions.pdf

Traffic prediction is a core task in intelligent transportation systems, supporting applications such as adaptive signal control, route guidance, and ride-hailing dispatch. Deep learning models, including graph convolutional networks, recurrent networks, and Transformers, achieve strong results on standard benchmarks, but their architectures are designed by hand, requiring significant expert effort and producing models that often generalize poorly across cities and datasets. Neural Architecture Search (NAS) offers a systematic alternative to manual design. It automates the search over candidate architectures of deep learning models, finding designs that match the spatial-temporal structure of traffic data without manual trial and error. This survey reviews NAS methods applied to traffic prediction, organized by search strategy: gradient-based methods, evolutionary methods, and one-shot weight-sharing methods. For each category, we analyze how the search space is designed to cover spatial and temporal traffic operators, and how the search strategy balances cost against architecture quality. We also discuss open challenges, computational scalability to large road networks, manual search space design, cross-city generalization, dynamic graph structure, and the open question of NAS for spatial-temporal foundation models, and identify directions for future research.

## 14. Amortized Moment Matching for Visual Generation

- Authors: Wenze Liu, Xintao Wang, Pengfei Wan, Xiangyu Yue
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-29
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.0515489180750515
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.26860v1
- PDF: https://arxiv.org/pdf/2607.26860v1
- Local PDF: pdf/2026-07-31_14_Amortized Moment Matching for Visual Generation.pdf

We propose amortized moment matching, utilizing neural networks to learn data moments as distributional training signals. By casting diffusion denoisers through polynomial projections, we establish a general framework for moment amortization, revealing that an $n$-th degree projection explicitly identifies data moments up to order $n+1$. Derived from the tractable affine case, we instantiate the Amortized Fréchet Distance (AMFD) loss. Unlike FD-loss which relies on explicit marginal moment calculations, AMFD is able to dynamically learn conditional moments via an alternating, matrix-free optimization pipeline that effortlessly scales to high-dimensional data. When operating on global representation features, AMFD serves as a powerful post-training objective; empirically, its neural formulation yields more robust training dynamics than exact statistical matching, substantially surpassing the FD baseline on the FDr$^6$ metric and achieving superior one-step generation on ImageNet. Furthermore, it unlocks direct exploration within native generative spaces, suggesting that the first two moments can identify target distributions only in spaces with strong semantics. Finally, when scaled to text-to-image generation, the condition-aware nature of AMFD unlocks massive gains in instruction-following capabilities, enabling our one-step models to outperform their multi-step FLUX.2 [klein] 4B teachers on the GenEval benchmark while achieving on-par performance on PickScore. Code and checkpoints are available at https://github.com/poppuppy/amfd.

## 15. AgentMap: Joint Equivalence and Subsumption Discovery for Ontology Matching

- Authors: Yiping Song, Jiaoyan Chen, Renate Schmidt, Hui Yang, Wen Zhang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-29
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 3.0395166560804485
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.27130v1
- PDF: https://arxiv.org/pdf/2607.27130v1
- Local PDF: pdf/2026-07-31_15_AgentMap_ Joint Equivalence and Subsumption Discovery for Ontology Matching.pdf

Ontology matching (OM) has traditionally been formulated as either equivalence discovery or subsumption matching. The existing OM systems identify only one type of semantic correspondence and cannot simultaneously discover equivalence and subsumption mappings. In this paper, we introduce Hybrid Ontology Matching (HOM), a new OM task that unifies equivalence and subsumption discovery, and accordingly propose a Large Language Model (LLM)-based multi-agent OM framework AgentMap that is implemented by a series of interdependent semantic decisions. Given a concept in the source ontology, AgentMap integrates semantic retrieval, hierarchical search, and collaborative multi-agent LLM reasoning to progressively explore the target ontology, identifying either the equivalent concept, if one exists, or the most fine-grained subsumer. We further extend four OM datasets for a HOM benchmark and evaluate AgentMap under hybrid, equivalence-only, and subsumption-only settings. Experimental results show that AgentMap achieves promising performance on the hybrid setting, and at the same time outperforms equivalence matching and subsumption matching baselines on the equivalence-only and subsumption-only settings, respectively.

## 16. Mol-CADiff: text-conditional molecule generation via causality-aware autoregressive diffusion

- Authors: Md Atik Ahamed, Qiang Ye, Qiang Cheng
- Source: openalex
- Venue type: journal
- Journal: Nature Communications
- Publication status: published
- Publication date: 2026-07-29
- DOI: https://doi.org/10.1038/s41467-026-75702-5
- Categories: Machine Learning in Materials Science, Computational Drug Discovery Methods, Topic Modeling
- Relevance: 3.013044348664635
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://doi.org/10.1038/s41467-026-75702-5
- PDF: Unavailable
- Local PDF: Not downloaded

Abstract The design of molecules with desired properties is a key challenge in drug discovery and materials science. Traditional methods rely on trial-and-error, while recent deep-learning approaches accelerate molecular generation. However, existing models struggle with generating molecules based on specific textual descriptions. We introduce Mol-CADiff, a diffusion-based framework that uses causal attention mechanisms for text-conditional molecular generation. Our approach explicitly models the causal relationship between textual prompts and molecular structures, overcoming limitations in existing methods. We enhance dependency modeling both within and across modalities, enabling precise control over the generation process. While primarily designed for text-guided tasks, this architecture inherently supports unconditional generation, providing the added capability to autonomously sample the broader chemical space without explicit constraints. Here we show that Mol-CADiff outperforms alternative methods in generating diverse, chemically valid molecules, with better alignment to specified properties, enabling more intuitive language-driven molecular design. By bridging these modalities, our framework provides a versatile method for drug discovery.

## 17. Decoupled Visual Processing: Efficient Multimodal Adaptation via Modality-Specific Transformer Substitution

- Authors: Mingkuan Feng, Zhengqi Wen, Jianhua Tao
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-29
- DOI: Unavailable
- Categories: cs.CV, cs.AI
- Relevance: 2.9366497575319936
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.26596v1
- PDF: https://arxiv.org/pdf/2607.26596v1
- Local PDF: pdf/2026-07-31_17_Decoupled Visual Processing_ Efficient Multimodal Adaptation via Modality-Specific Transformer Substitution.pdf

Multimodal large language models (MLLMs) have demonstrated remarkable capabilities by integrating visual and textual understanding within a unified transformer architecture. However, fine-tuning all parameters of these models for visual instruction tuning is computationally expensive and often unnecessary, as the representation requirements for visual and textual tokens diverge significantly in the deeper layers of the network. In this paper, we propose Decoupled Visual Processing (DVP), an efficient training framework that replaces the upper decoder layers of a pretrained LLM with a lightweight, independently trainable single transformer block dedicated exclusively to visual token processing. Specifically, after shared processing through the first half of the decoder layers, visual and textual tokens are split: visual tokens are routed through a newly initialized single transformer block while textual tokens continue through the original frozen decoder layers. The two streams are then concatenated before the language modeling head. During training, only the single transformer block is updated, dramatically reducing the number of trainable parameters. Experiments on the LLaVA-1.5 framework demonstrate that DVP achieves competitive performance on MME, POPE, and ChartQA benchmarks while training only a fraction of the total parameters, suggesting that visual representations in MLLMs can be effectively learned through a decoupled, parameter-efficient pathway.

## 18. Flow Map Learning via Nongradient Vector Flow

- Authors: Mark Goldstein, Anshuk Uppal, Raghav Singhal, Aahlad Puli, Rajesh Ranganath
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-29
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 2.934158747367628
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.26398v1
- PDF: https://arxiv.org/pdf/2607.26398v1
- Local PDF: pdf/2026-07-31_18_Flow Map Learning via Nongradient Vector Flow.pdf

Diffusion and flow-based models benefit from simple regression losses, but inference incurs significant overhead because sampling requires integration. Consistency models address this by directly learning the flow maps along the ODE trajectory, opening a design space between one-step and many-step approaches. However, existing methods face computational challenges such as requiring model inverses or backpropagation through iterated model calls, and do not always prove that the desired ODE flow map is a solution to the loss. We introduce SGFlow, an approach for learning flow maps that bypasses explicit invertibility constraints and expensive differentiation through model iteration. SGFlow trains a model to compute both the ODE solutions and the implied velocity from scratch by following non-conservative dynamics with a stationary point at the desired flow map. On the CIFAR image benchmark, no single method attains the best FID at every step count: SGFlow attains the best FID at 10 sampling steps and remains competitive with flow matching, Meanflow, and Lagrangian map matching at other step counts, while being the only one with a proven stationary-point guarantee for its stopgrad-based dynamics.

## 19. Scientific Knowledge Discovery in the Age of Large Language Models

- Authors: Eleni Adamidi, Serafeim Chatzopoulos, Thanasis Vergoulis
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-29
- DOI: Unavailable
- Categories: cs.DL, cs.AI, cs.CL, cs.IR
- Relevance: 2.9023796715130397
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.26670v1
- PDF: https://arxiv.org/pdf/2607.26670v1
- Local PDF: pdf/2026-07-31_19_Scientific Knowledge Discovery in the Age of Large Language Models.pdf

The rapid growth of scholarly literature has made identifying relevant publications increasingly difficult, and conventional search systems still depend heavily on manually formulated queries and effortful manual inspection. Generative large language models (LLMs) offer a more flexible alternative, supporting literature retrieval and the screening of candidate studies against eligibility criteria. This chapter surveys 34 peer-reviewed papers applying generative LLMs to these two tasks, identified via a Boolean search over the OpenAIRE Graph (1,589 records screened to 34 inclusions). Reviewed studies are characterised by LLMs employed, model access and adaptation, prompting and architectural techniques, ground-truth sources, and evaluation metrics.

## 20. When Do Learned Diffusion Proposals Help Constraint Solving? A Controlled Study on Continuous Algebraic Systems

- Authors: Quang Bui, Sparsh Roy, Akash Gundimeda, Davin Yin
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-29
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 2.886610332443582
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.27169v1
- PDF: https://arxiv.org/pdf/2607.27169v1
- Local PDF: pdf/2026-07-31_20_When Do Learned Diffusion Proposals Help Constraint Solving_ A Controlled Study on Continuous Algebraic Systems.pdf

Solving a continuous algebraic constraint system requires two decisions: which values satisfy the constraints, and which structural augmentation renders an unsolvable system solvable. Classical solvers answer the first well and the second only by enumeration. On that discrete decision, a candidate-conditioned repair ranker choosing among K augmentations reaches the exhaustive-search ceiling at a fraction of the calls, outperforming random (0.997 vs 0.236 balanced nonlinear menu accuracy; p < 10^-70; 0.982 +/- 0.006 across seeds) and beating a budget-matched per-candidate probe on accuracy and cost. MARC turns such a system into a factor graph, over which a graph-neural diffusion denoiser proposes assignments, descent on an exact computer-algebra energy polishes them, and an exact symbolic checker certifies solutions. Evaluations of diffusion-based proposals rarely include one control: random multi-start under the same refinement budget. Applied to our system, it sharply curtails what the learned proposal contributes on the value decision. Does it beat random multi-start at choosing satisfying assignments? Only narrowly, in a predictable regime. Across trapped low-dimensional families it ties with random restart, but dominates in high dimension, where random search fails. Once variables couple, the advantage is gone. Since all methods share one polish and one checker, best-of-K random multi-start succeeds with probability exactly 1 - (1 - q(n))^K, where q(n) is single-start reachability; one measured constant, with no free parameters, reproduces the entire curve (mean absolute error 0.012). The favorable regime is not specific to our synthetic families: across eight real-world systems in robotics, positioning, optimization, and algebra, classical multi-start solved all eight, none in the learning-favorable regime. We map the regimes in which learned proposals improve solvers.

## 21. From Interface to Inference: Eliciting Any-Order Inference from Any-Order Models

- Authors: Seunggeun Kim, Jaeyeon Kim, Taekyun Lee, Yuyuan Chen, Yilun Du, Sham Kakade, Sitan Chen
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-29
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 2.8846317277880216
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.26504v1
- PDF: https://arxiv.org/pdf/2607.26504v1
- Local PDF: pdf/2026-07-31_21_From Interface to Inference_ Eliciting Any-Order Inference from Any-Order Models.pdf

Many discrete reasoning tasks, such as code generation, are inherently non-causal: programmers move between high-level structure and local details, a process we call any-order inference. For autoregressive language models, which lack a native any-order interface, non-causal abilities such as infilling and next-edit prediction require hand-designed mechanisms. Can we instead design models that natively support any-order inference? Masked diffusion models have recently emerged as compelling candidates, as their any-order training objective naturally offers an any-order prediction interface. This interface, however, does not automatically yield any-order inference. We demonstrate that this interface-inference gap stems from positional uncertainty: fixed-canvas, token-level models may know what semantic component should appear without knowing where to place it. In light of this, we propose two complementary approaches: (1) Insertion-based masked diffusion, building on FlexMDM (Kim et al, 2025), relaxes fixed-position commitments via insertions, enabling generation across non-contiguous regions. (2) Latent-space masked diffusion shifts prediction to coarser semantic segments, enabling search over latent generation orders. Empirically, we train a 7B FlexMDM for Python coding and a 125M LatentMDM for GSM8K and show that both approaches induce distinct any-order inference behaviors and improve downstream performance. We release our codebase at https://github.com/SeunggeunKimkr/genuine-any-order.

## 22. See2Think: Do Multimodal Models Really Use Intermediate Visual States?

- Authors: Siyu Yan, Zhuoran Yan, Haiying Xu, Panhao Zhou, Jingyu Chen, Chenhao Ji, Shuo Cao, Yongheng Zhang, Haoze Liu, Siyu Zhang, Xiwen Gu, Yihao Liu, Alex Jinpeng Wang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-29
- DOI: Unavailable
- Categories: cs.CV, cs.AI
- Relevance: 2.877123789383975
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.26769v1
- PDF: https://arxiv.org/pdf/2607.26769v1
- Local PDF: pdf/2026-07-31_22_See2Think_ Do Multimodal Models Really Use Intermediate Visual States.pdf

Multimodal large language models increasingly use sketches, annotations, tools, and intermediate images during reasoning, but it remains unclear whether they truly rely on these visual states. Existing benchmarks are limited both by task collections with narrow coverage or partially text-solvable samples and by evaluations that emphasize final answers without diagnosing how intermediate visual states are generated, rendered, and used. We introduce See2Think, a unified evaluation framework comprising See2ThinkBench and Visual Action-of-Thought (VAoT). See2ThinkBench contains 1,200 open-ended, visually dependent problems across 12 task categories spanning 2D structured, 3D scene, and real-world reasoning. VAoT records textual thoughts, visual actions, rendered states, and subsequent reasoning under four controlled inference settings. Evaluating representative proprietary and open-source multimodal models, we find that visual reasoning is strongly model- and environment-dependent, with no single setting consistently dominating across tasks. Process analysis further shows that models usually select relevant visual operations, while faithful rendering remains the clearest bottleneck and high feedback uptake does not necessarily translate into accuracy gains. Under task-relevant corrupted feedback, models exhibit behavioral dependence on visual states, with accuracy dropping by over 10 percentage points in controlled interventions.

## 23. Existence-Field Diffusion Model for Spatial Point Processes with Variable Cardinality

- Authors: Xiaoyin Pan, Christian R. Shelton, Rakshith Mahishi, Chengkuan Hong
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-29
- DOI: Unavailable
- Categories: cs.LG, stat.ML
- Relevance: 2.869662141041874
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.26428v1
- PDF: https://arxiv.org/pdf/2607.26428v1
- Local PDF: pdf/2026-07-31_23_Existence-Field Diffusion Model for Spatial Point Processes with Variable Cardinality.pdf

We study generative modeling of spatial point processes (SPP), where both the number of points and their spatial configuration are governed by a joint distribution. While diffusion models have achieved strong performance in modeling complex distributions, extending them to variable-cardinality SPP remains challenging. Existing approaches either decouple the modeling of cardinality and spatial structure, or rely on discrete trans-dimensional operations to modify the number of points, resulting in inflexible and asymmetric generative dynamics. We propose the existence-field diffusion model (EFDM) for spatial point processes modeling, where each potential point is associated with an existence variable representing its degree of presence. This enables a unified diffusion process that jointly models both spatial locations and cardinality without requiring explicit discrete transitions. We demonstrate that our approach provides a flexible and general framework for generative modeling of spatial point processes, achieving improved modeling capability on datasets with varying cardinality.

## 24. DKME: Rethinking Coupled Knowledge Memory for Lifelong Model Editing of Large Language Models

- Authors: Guanyu Zheng, Wang Zhenyu, He Tingting, Xv Wang, Haochang Wang, Yaokai Huang, Tiejun Zhao
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.866445205653969
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.792/
- PDF: https://aclanthology.org/2026.findings-acl.792.pdf
- Local PDF: pdf/2026-07-31_24_DKME_ Rethinking Coupled Knowledge Memory for Lifelong Model Editing of Large Language Models.pdf

Lifelong knowledge editing aims to inject a stream of factual updates into large language models (LLMs) without retraining, yet existing memory-based editors often suffer from catastrophic forgetting as edits accumulate. We argue that a key factor is the coupled knowledge memory mechanism, where addressing (routing) and storage (writing via memory-module updates) are entangled. This entanglement makes it difficult to confine the effects of each edit to its intended scope, particularly in multi-domain and associated-fact editing streams, where updates either span diverse semantic domains or repeatedly modify related attributes of the same subject. Consequently, updating memory for one edit inadvertently alters the routing and stored representations of previously injected edits, leading to catastrophic forgetting as edits accumulate. We propose DKME , which decouples addressing from storage via two stages: decoupled semantic addressing learns a fact-aware manifold for scope-aware routing, and partitioned memory storage localizes edits to memory partitions identified by unsupervised clustering in the embedding space. Experiments on three benchmarks, including HalluEditBench, CKnowEdit, and WikiData counterfact , demonstrate that DKME consistently achieves a more favorable trade-off between editing success and locality compared to baselines, while maintaining more stable performance as the edit scale increases.

## 25. Equilibrium Training of Energy-Based Models with Parallel Trajectory Tempering

- Authors: Nicolas Béreux, Aurélien Decelle, Cyril Furtlehner, Beatriz Seoane
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-29
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 2.8633218877574196
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.27077v1
- PDF: https://arxiv.org/pdf/2607.27077v1
- Local PDF: pdf/2026-07-31_25_Equilibrium Training of Energy-Based Models with Parallel Trajectory Tempering.pdf

Energy-Based Models (EBMs) provide an interpretable framework for generative modeling of scientific data, but poor Markov Chain Monte Carlo mixing often limits their reliability. We introduce a training algorithm based on Parallel Trajectory Tempering (PTT), which exploits the continuity of the optimization path to maintain equilibrium sampling throughout learning. This enables stable and fast training on highly multimodal and data-scarce scientific datasets. Combined with reservoir sampling and adaptive optimization, PTT has a computational cost comparable to Persistent Contrastive Divergence, making it a practical replacement for standard training methods. It also provides direct estimates of thermalization times, equilibrium samples from trained models, and accurate log-likelihoods at essentially no additional cost. Experiments on Restricted Boltzmann Machines show that PTT consistently outperforms existing EBM training approaches. On discrete tabular data, it also surpasses state-of-the-art deep generative models, yielding higher-quality samples and greater robustness to overfitting and limited data. Our results make equilibrium maximum-likelihood training of EBMs practical and computationally efficient.

## 26. Don’t Tell the Answer, Truly Guide the Reasoning During RL Rollouts

- Authors: Xinyi Wang, Jinyi Han, Zishang Jiang, Tingyun li, Jiaqing Liang, Sihang Jiang, Zhaoqian Dai, Ma Shuguang, Fei Yu, Yanghua Xiao
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.8592783630768173
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.169/
- PDF: https://aclanthology.org/2026.findings-acl.169.pdf
- Local PDF: pdf/2026-07-31_26_Don’t Tell the Answer, Truly Guide the Reasoning During RL Rollouts.pdf

Reinforcement learning (RL) has emerged as a key approach for improving long chain-of-thought (CoT) reasoning in large language models (LLMs). However, existing methods such as GRPO often break down when task difficulty exceeds the model’s capacity, resulting in sparse rewards and inefficient training. While prior work attempts to address this issue using off-policy data, it frequently introduces distributional mismatch, leading to unstable policy updates.In this work, we identify a fundamental issue underlying these limitations, which we term low training affinity , and propose Affinity , the first quantitative metric for measuring the compatibility between external guidance and a model’s intrinsic policy. Based on this insight, we introduce HINT , an adaptive framework designed to enhance reasoning performance while explicitly preserving high Affinity.HINT consists of two key components. First, instead of providing partial answers, it introduces Meta-Hints , which serve as abstract cognitive scaffolding that guides the model to independently construct solutions. Second, we propose Affinity-Aware Policy Optimization (AAPO) , which dynamically adjusts the learning objective based on the Affinity signal to ensure stable training.Extensive experiments across diverse benchmarks demonstrate that HINT consistently outperforms strong baselines, while achieving improved training stability and robust generalization to out-of-distribution tasks. Code is available at: https://github.com/ViviqwerAsd/HINT

## 27. From Logical to Computational Sparsity: Structure-Aware Block-Sparse Attention for Long-Code Completion

- Authors: Yanli Wang, Yanlin Wang, Bowen Zhang, Yiwei Zhang, Daya Guo, Jiachi Chen, Hongyu Zhang, Zibin Zheng
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.857441880144984
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1189/
- PDF: https://aclanthology.org/2026.acl-long.1189.pdf
- Local PDF: pdf/2026-07-31_27_From Logical to Computational Sparsity_ Structure-Aware Block-Sparse Attention for Long-Code Completion.pdf

Code Large Language Models face critical Time-To-First-Token (TTFT) latency challenges when handling long code completion due to the quadratic complexity ( O(n 2 ) ) of attention mechanisms. While existing sparse attention methods attempt to address this issue, they suffer from three key limitations: (1) general sparse patterns cause excessive accuracy degradation without considering code structure, (2) code-specific methods achieve only logical sparsity without actual computational speedup, and (3) limited adaptation to complex scenarios such as repository-level completion. We propose SabreCoder , a training-free S tructure- a ware b lock-spa r s e attention mechanism that bridges the gap between logical and computational sparsity. SabreCoder parses code into semantic chunks, constructs chunk-level sparse patterns through dependency analysis and similarity matching, and maps them to GPU-friendly block-sparse formats. Extensive experiments on LCC and CrossCodeEval benchmarks demonstrate that SabreCoder reduces TTFT by 45-55% while maintaining accuracy within 3% of dense attention.

## 28. One Refiner to Unlock Them All: Inference-Time Reasoning Elicitation via Reinforcement Query Refinement

- Authors: Yixiao Zhou, Dongzhou Cheng, Zhiliang wu, Yi Yang, Yu Cheng, Hehe Fan
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.855887939594344
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1807/
- PDF: https://aclanthology.org/2026.acl-long.1807.pdf
- Local PDF: pdf/2026-07-31_28_One Refiner to Unlock Them All_ Inference-Time Reasoning Elicitation via Reinforcement Query Refinement.pdf

Large Language Models (LLMs) often fail to utilize their latent reasoning capabilities due to a distributional mismatch between ambiguous human inquiries and the structured logic required for machine activation. Existing alignment methods either incur prohibitive O(N) costs by fine-tuning each model individually or rely on static prompts that fail to resolve query-level structural complexity. In this paper, we propose ReQueR ( Re inforcement Que ry R efinement), a modular framework that treats reasoning elicitation as an inference-time alignment task. We train a specialized Refiner policy via Reinforcement Learning to rewrite raw queries into explicit logical decompositions, treating frozen LLMs as the environment. Rooted in the classical Zone of Proximal Development from educational psychology, we introduce the Adaptive Solver Hierarchy, a curriculum mechanism that stabilizes training by dynamically aligning environmental difficulty with the Refiner’s evolving competence. ReQueR yields consistent absolute gains of 1.3%–7.2% across diverse architectures and benchmarks, outperforming strong baselines by 2.1% on average. Crucially, it provides a promising paradigm for one-to-many inference-time reasoning elicitation, enabling a single Refiner trained on a small set of models to effectively unlock reasoning in diverse unseen Solvers. Code is available at https://github.com/newera-xiao/ReQueR .

## 29. SLoRA: Balancing Plasticity and Forgetting in Large Language Models for Continual Learning

- Authors: Lina Yang, Yusheng Liao, Yanfeng Wang, Yu Wang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.850290159432035
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.247/
- PDF: https://aclanthology.org/2026.acl-long.247.pdf
- Local PDF: pdf/2026-07-31_29_SLoRA_ Balancing Plasticity and Forgetting in Large Language Models for Continual Learning.pdf

Large language models (LLMs) have achieved remarkable success across diverse tasks through large-scale pretraining. However, they remain prone to catastrophic forgetting in continual learning. To the best of our knowledge, this is the first work to identify noise accumulation in LoRA updates as a key cause of forgetting in continual learning. A preliminary two-task experiment demonstrates that removing less important components of the second task’s LoRA parameters improves performance on the first task, suggesting that later updates introduce noisy interference. Building on this insight, we propose S ubspace-Denoised Lo w- R ank A daptation ( SLoRA ), a simple and effective framework that filters noisy components from LoRA updates via subspace similarity with the base model. SLoRA is a regularization-free method without accessing data or gradients from previous tasks or modifying the training process. It offers two variants, SLoRA-Pre and SLoRA-Post, for online and offline continual learning, respectively. Extensive experiments across tasks and models validate the effectiveness of SLoRA. It improves final accuracy by up to 12%, reduces forgetting by 29%, and filters out over 30% of LoRA parameters identified as noisy. Our code is available at https://github.com/alina1031/SLoRA .

## 30. Quantitative assessment of cell fate commitment in single-cell transcriptomics using scCS

- Authors: Kriukov, E., Ivleva, E., Baranov, P.
- Source: biorxiv
- Venue type: preprint
- Journal: biorxiv
- Publication status: preprint
- Publication date: 2026-07-30
- DOI: 10.64898/2026.07.27.741070
- Categories: bioinformatics
- Relevance: 2.8470705680097463
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://www.biorxiv.org/content/10.64898/2026.07.27.741070v1.full.pdf
- PDF: https://www.biorxiv.org/content/10.64898/2026.07.27.741070v1.full.pdf
- Local PDF: pdf/2026-07-31_30_Quantitative assessment of cell fate commitment in single-cell transcriptomics using scCS.pdf

Cell fate trajectory inference is one of the key downstream methods in single-cell RNA-sequencing data analysis. Multiple existing tools allow studying such and help identify continuous cell fate dynamics, important genes along the trajectory, and reconstruct the transcriptional states a cell passes to its estimated final state. These methods have been essential to study various biological systems, yet cell fate by itself currently presents mostly qualitative analysis, and existing tools do not allow to directly quantify the fate-related parameters, including commitment, transition speed, fate affinity and entropy. Such quantifications may be performed through multiple parameters and result in better understanding and description of cell fates. We present scCS (single-cell Commitment Scoring), a scverse-friendly Python framework for this problem. scCS introduces Discounted Future-Fate Propagation (DFFP), which models the source transition graph as a geometrically stopped random walk that can reach endpoint anchors or stop unresolved, with a user-defined finite expected graph horizon. For each cell, the resulting probabilities are separated into total fate reach, relative affinity among reached fates, entropy-based fate specificity and reach-supported resolved commitment, while Signed Ordering Flux independently quantifies local progression. scCS also provides endpoint-anchor, graph-coverage and horizon-sensitivity diagnostics, an instantaneous local-direction mode, standardized visualizations, gene-level analyses and replicate-aware comparisons across experimental conditions. Applications to pancreatic endocrinogenesis and neural crest-Schwann-cell differentiation illustrate the general framework. scCS converts an explicit biological fate hypothesis into auditable cell-, population- and replicate-level quantities without redefining the source dynamics.
