# Paper Daily Reading - 2026-10-21

## 1. An Analysis of Semantic and Spatio-Temporal Co-evolution for Edge Classification on Dynamic Text-Attributed Graphs

- Authors: Tyler Bonnet, Marek Rei
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-19
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.5294893806899
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.25906v1
- PDF: https://arxiv.org/pdf/2610.25906v1
- Local PDF: pdf/2026-10-21_01_An Analysis of Semantic and Spatio-Temporal Co-evolution for Edge Classification on Dynamic Text-Attributed Graphs.pdf

Dynamic edge classification on text-attributed Web graphs, such as review networks, community forums, and news-derived knowledge graphs, requires high quality, adaptive semantic representations in the context of network evolution. Existing dynamic graph architectures typically initialize text feature vectors with pretrained language models and hold them static during training to preserve their semantic structure, forgoing the potential benefits of allowing them to co-evolve with network topology. In this work, we investigate the effects of enabling such co-evolution with a unified text-graph alignment framework that integrates a lightweight Transformer adapter to update token-level text representations via spatio-temporal gradients from a contrastive pretraining objective. To prevent detrimental semantic distortion, a language model maintenance objective anchors the evolving text embeddings to their original semantic structure. Evaluations on the Dynamic Text-Attributed Graph Benchmark demonstrate that this anchored text-graph co-evolution consistently improves upon the edge classification performance of frozen-text baselines across diverse Web-related domains. Representational analyses reveal that the framework reduces anisotropy, improving the linear separability of text embeddings, and effectively encodes structural and temporal information into the semantic space. A computational efficiency analysis confirms that this beneficial semantic and spatio-temporal co-evolution is achieved without incurring the prohibitive computational overhead typical of end-to-end joint training.

## 2. MCDA: Multi-View Graph Contrastive Learning with Dynamic Topology Augmentation for Functional MRI Analysis

- Authors: Hao Zhang, Xiaoyun Liu, Shuo Huang, Yue Ma, Liang Cao, Mingxia Liu, Li Zhang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-19
- DOI: Unavailable
- Categories: cs.CV, cs.AI
- Relevance: 3.4263503164477624
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.26322v1
- PDF: https://arxiv.org/pdf/2610.26322v1
- Local PDF: pdf/2026-10-21_02_MCDA_ Multi-View Graph Contrastive Learning with Dynamic Topology Augmentation for Functional MRI Analysis.pdf

Resting-state fMRI (rs-fMRI) is a vital non-invasive tool for diagnosing brain disorders and uncovering pathological mechanisms. However, existing graph contrastive learning (GCL) methods often underexploit augmentation histories across training epochs and the relationships among different augmented views. In this paper, we introduce a topology-guided Multi-view graph Contrastive learning framework with Dynamic graph topology Augmentation (MCDA) for fMRI analysis. Unlike traditional GCL that uses fixed noise or edge-dropping, MCDA employs a Dynamic Augmentation Update (DAU) module that iteratively refines the augmented topology. Specifically, we incorporate self-aware and cross-sample augmentation strategies to simultaneously capture individual-specific functional signatures and inter-subject heterogeneity. We then design a topology-guided multi-view graph contrastive learning scheme that explores interrelationships not only between the original network and its augmented views, but also across different augmented views to maximize structural information preservation. We characterize the score-level optimization directions and establish a lower bound for the contrastive objective. The framework combines classification and contrastive losses for brain disorder diagnosis and examines discriminative functional connectivity patterns as potential biomarkers. Experiments on two public rs-fMRI datasets comprising 1,236 subjects demonstrate that MCDA outperforms the state-of-the-art methods. The code has been made publicly available at: \url{https://github.com/goodcodingagoodboy/MCDA}.

## 3. Bridging Concepts: Multi-Agent Reasoning over Scientific Concept Graphs for High-Impact Research Prediction

- Authors: Donggyu Yoon, Minsung Hwang, Juneha Baek, Donghyuk Shin, Joyce Jiyoung Whang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-18
- DOI: Unavailable
- Categories: cs.AI, cs.IR, cs.LG
- Relevance: 3.352459528509359
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.25281v1
- PDF: https://arxiv.org/pdf/2610.25281v1
- Local PDF: pdf/2026-10-21_03_Bridging Concepts_ Multi-Agent Reasoning over Scientific Concept Graphs for High-Impact Research Prediction.pdf

Within a research community, new topics often emerge when previously unconnected concepts are first studied together. We construct scientific concept graphs (SCGs)--domain knowledge graphs whose nodes are fine-grained research concepts extracted from paper text by LLMs and whose edges capture their co-occurrence in papers--and study the task of forecasting high-impact concept pairs, i.e., discovering concept pairs that are currently unconnected but will have high impact when connected. To this end, we introduce new benchmark datasets constructed from CIKM, KDD, and SIGIR conference papers, with varied prediction settings, including impact forecasting for emerging concepts unseen during training. We propose MiroGraph, a Multi-agent reasoning framework with scientific concept Graphs, in which a feature designer agent designs predictive features for a given concept pair from structural, semantic, and trend perspectives, and then three LLM agents compute the actual feature values from the enclosing subgraph of the concept pair. Using these feature values, a classifier designer agent constructs a classifier that predicts the final impact labels. MiroGraph outperforms various impact forecasting and temporal link prediction methods.

## 4. FTFM: Factorized Tabular Foundation Models

- Authors: Josif Grabocka
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-18
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.336924618434267
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.25558v1
- PDF: https://arxiv.org/pdf/2610.25558v1
- Local PDF: pdf/2026-10-21_04_FTFM_ Factorized Tabular Foundation Models.pdf

Tabular foundation models (TFMs) are becoming a powerful alternative to conventional tabular learning, adapting to new datasets in context without task-specific training. Current architectures, however, face a trade-off: models that preserve cell-level representations are expensive because they repeatedly attend across rows and columns, while faster models collapse each row into a fixed embedding and lose this fine-grained state. We introduce Factorized Tabular Foundation Models (FTFM), which preserve cell representations while factorizing their computation through one contextual latent per row and one per column. Cells no longer attend to one another directly; instead, each cell is updated through the interaction of its row and column latents, reducing repeated attention while retaining feature-specific information. FTFM achieves competitive predictive performance in tabular classification on major benchmarks such as TabArena and BeyondArena.

## 5. spora: A Unified Multimodal Dataset and Platform for Spatial Proteomics

- Authors: Benedikt von Querfurth, Johann Wenckstern, Eeshaan Jain, Lukas Klein, Phil Cheng, Yexiang Cheng, Cedric Vincent-Cuaz, Martina Haberecker, Pascal Frossard, Andreas Wicki, Olivier Michielin, Charlotte Bunne
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-15
- DOI: Unavailable
- Categories: cs.CV, cs.AI
- Relevance: 3.286377202985687
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.24002v1
- PDF: https://arxiv.org/pdf/2610.24002v1
- Local PDF: pdf/2026-10-21_05_spora_ A Unified Multimodal Dataset and Platform for Spatial Proteomics.pdf

Spatial proteomics (SP) captures the molecular composition and spatial organization of tissues at single-cell resolution, opening a direct view of the cellular ecosystems that drive disease. Protein panels, acquisition platforms, and tissue contexts differ from one cohort to the next, and a coherent picture of tissue biology can only emerge from models trained to bridge this heterogeneity. Foundation models offer the natural path forward, but their training depends on large, harmonized corpora that span platforms, panels, and cohorts. No public resource currently approaches that scale; available data sit in small, narrowly scoped releases with incompatible formats and conventions. We present $\texttt{spora}$, a large-scale multimodal SP dataset of 13,546 standardized multiplex images from 5,477 patients across 35 cohorts and five major SP technologies. Curated with biomedical experts, $\texttt{spora}$ provides model training-ready formats together with cell and tissue segmentations, structured clinical metadata, and, where available, paired H&E enabling the training of virtual staining models. It is complemented by $\texttt{spora [io]}$, a unified interface for tiling, sampling, and standardization across all cohorts and modalities, and $\texttt{spora [bench]}$, a benchmark suite spanning cell phenotyping, diagnostic and therapeutic prediction as well as virtual staining tasks across twelve cohorts that places current SP foundation models on common ground against task specific baselines.

## 6. Graph-to-Table Interfaces Control Relational Generalisation

- Authors: Alessandro Cagiano, Lorenzo Molfetta, Gianluca Moro, Matteo Zignani, Pasquale Minervini
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-19
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.24252111253828
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.25993v1
- PDF: https://arxiv.org/pdf/2610.25993v1
- Local PDF: pdf/2026-10-21_06_Graph-to-Table Interfaces Control Relational Generalisation.pdf

Graph-to-table systems combine three design choices: an encoder that maps relational evidence to feature rows, a context constructor that selects labelled examples, and a tabular decoder. We investigate whether these components can be evaluated independently through matched comparisons that change one component while holding the rest of the pipeline and the evaluation constant. Across logistic regression, CATBOOST, and TABPFN-3 on CLUTRR, 57 GraphLog worlds, and 57 knowledge graphs, we show that conclusions about one component can change when the others change. On CLUTRR, absolute positional encodings maintain all distinctions among the evaluated queries and fit the short-path setting nearly perfectly; yet, they generalise worse than relation-count features because the supported prefix acts as a shortcut that breaks down on longer paths. On GraphLog, encoder preference depends on the decoder, while the relation-count representation degrades as CatBoost tree depth increases. Across different knowledge graphs, adding the frozen ULTRA score to local features is consistently useful, whereas adding local features to the score has a smaller and less stable effect. A pointwise TABPFN-3 readout using the full encoder underperforms native ULTRA on 48 of 57 datasets. These results show that encoder assessment depends jointly on context and decoder, while panel-level conclusions can also depend on evaluation and aggregation protocols.

## 7. Pack and Extract: An Effective Graph-Based Approach for Feature Selection

- Authors: Faisal N. Abu-Khzam, Joseph R. Barr, Cynthia Chaaya, Nadim Obeid, Peter Shaw
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-07
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.224312145188163
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.23938v1
- PDF: https://arxiv.org/pdf/2610.23938v1
- Local PDF: pdf/2026-10-21_07_Pack and Extract_ An Effective Graph-Based Approach for Feature Selection.pdf

Many molecular biology data sets contain thousands of features, such as genes in single-cell experiments or other omics data. Standard predictive models often perform poorly in such settings, as they tend to retain a large number of features and fail to adequately handle correlations among them. Combinatorial approaches, such as feature selection based on the Independent Dominating Set (IDS) model, have shown promising results, but appear to have been largely overlooked, possibly due to their high computational complexity. In this paper, we propose an improvement to IDS-based feature selection that (i) favors features exhibiting greater diversity and (ii) generalizes the notion of independent dominating set to a node packing model. The resulting formulation is used as an intermediate step within the feature selection process. We evaluate our approach on five genetic data sets and compare the results with those obtained using existing methods. Our experimental results demonstrate notable improvements in predictive accuracy over traditional models, as well as increased stability of the selected feature sets.

## 8. Spectral Adaptive Graph Transformer for Efficient and Scalable Traffic Forecasting

- Authors: Amirhossein Ghaffari, Susanna Pirttikangas, Ekaterina Gilman
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-18
- DOI: Unavailable
- Categories: cs.AI, cs.LG
- Relevance: 3.2074744995635127
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.25140v1
- PDF: https://arxiv.org/pdf/2610.25140v1
- Local PDF: pdf/2026-10-21_08_Spectral Adaptive Graph Transformer for Efficient and Scalable Traffic Forecasting.pdf

Traffic forecasting models based on spectral graph convolution offer an interpretable account of how information is mixed between sensors, but they rely on an eigendecomposition of the graph Laplacian. It costs cubic time, is fixed by the road network, and provides a symmetric operator that cannot represent the directed propagation of traffic congestion. Attention-based spatio-temporal transformers remove these limitations but generate a dense sensor-by-sensor attention map at each layer and time step, so memory, rather than accuracy, becomes the binding constraint on large networks. We introduce the spectral adaptive graph transformer, whose spatial operator is learned rather than derived from the Laplacian, directed rather than symmetric, and conditioned on the current traffic state rather than a static state, at a cost linear in the number of sensors. A sparse road graph diffusion branch provides the strictly local propagation that a low-rank operator cannot express, and a zero-initialized gate learns the balance between the two. Before spatial mixing, a unit-mean-gain frequency-bin attention module reweights each sensor's short-term periodicities according to its identity and current context. Across six public benchmarks spanning 170 to 1843 sensors, evaluated over three random seeds, the proposed model attains the lowest error of any single end-to-end model on one benchmark and remains competitive with the strongest current attention models on the others, while using about a quarter of their memory and training about twice as fast.

## 9. Reranking Answers of Large Language Models with Knowledge Graphs

- Authors: Mikhail Salnikov, Hai Le, Olga Tsymboi, Ivan Lazichny, Dmitrii Iarosh, Egor Cheremiskin, Andrey Savchenko, Dmitry Simakov, Alexander Panchenko
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-18
- DOI: Unavailable
- Categories: cs.CL, cs.AI
- Relevance: 3.1986376608216993
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.25185v1
- PDF: https://arxiv.org/pdf/2610.25185v1
- Local PDF: pdf/2026-10-21_09_Reranking Answers of Large Language Models with Knowledge Graphs.pdf

Answering natural language questions over knowledge graph data is challenging due to the vast number of facts, which can be difficult to process and navigate. One potential solution for this issue is to use mined subgraphs related to the query, although this process still requires extracting these subgraphs. This research presents a solution for extracting subgraphs related to entity candidates from a question-and-answer set, which can be obtained by inferring a large language model by calculating the shortest paths between entities. The proposed approaches detail various features that can be extracted from the subgraphs and reranking models to select the most probable answers from a list of candidates. Experiments were conducted on Wikidata to evaluate the effectiveness of the proposed approaches. This involved enumerating all the main feature types that can be extracted from mined subgraphs and a detailed analysis of the proposed features and reranking method combinations. In addition, a public web application that provides a useful web tool for studying the graph space between question and answer entities has been developed to work with subgraphs. This includes visualization of the extracted subgraph and automatic generation of natural language text to describe it.

## 10. Cognitive Map in Large Language Models

- Authors: Albert Qin, Jonathan Cohen, Gautam Reddy
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-19
- DOI: Unavailable
- Categories: cs.CL, cs.LG
- Relevance: 3.1946027279831837
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.25596v1
- PDF: https://arxiv.org/pdf/2610.25596v1
- Local PDF: pdf/2026-10-21_10_Cognitive Map in Large Language Models.pdf

It has long been proposed that animals construct cognitive maps to support flexible behavior in novel environments. We tested whether large language models form similar representations using relational reasoning tasks and causal "mosaic experiments" that manipulate internal activations in open-weight language models. Models beyond the ten-billion-parameter scale successfully inferred unstated relationships between entities and generalized to synthetic entity names. Across model and task families, models generated abstract representations of relational structure and combined them additively with representations of entity identity, binding entities to roles within that structure. Models stored observed relationships as pairwise links that they composed retrospectively when queried, rather than prospectively positioning each entity in a global coordinate system. Binding was mediated by a sparse, distributed set of key--value pairs; by perturbing these pairs, we implanted "false memories" that altered model behavior in predictable ways. Overall, our findings reveal an internal organization analogous to a cognitive map that explains how language models reason with limited information.

## 11. Procedural Memory for Language Agents: A Neurosymbolic Perspective on Explicit Goal Structure

- Authors: Jonathan Leung, Zhiqi Shen, Deheng Ye
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-19
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 3.187893197036866
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.25996v1
- PDF: https://arxiv.org/pdf/2610.25996v1
- Local PDF: pdf/2026-10-21_11_Procedural Memory for Language Agents_ A Neurosymbolic Perspective on Explicit Goal Structure.pdf

Large language models remain unreliable on long-horizon tasks requiring procedural reasoning. We argue that a key cause is the absence of explicit procedural memory: accessible, modifiable knowledge of how tasks are accomplished, distinct from semantic and episodic memory. Goal-Oriented Graphs offer such a representation, encoding goals and prerequisite dependencies as inspectable symbolic structure. We examine their construction, the challenges they pose, and principles for integrating them with neural reasoning.

## 12. OrderGPT: Generation Order as a Learnable Modeling Choice

- Authors: Chenhe Yang, Yuhuan Lyu, Tianyang Hu
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-19
- DOI: Unavailable
- Categories: cs.AI, cs.LG
- Relevance: 3.185041609238855
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.25949v1
- PDF: https://arxiv.org/pdf/2610.25949v1
- Local PDF: pdf/2026-10-21_12_OrderGPT_ Generation Order as a Learnable Modeling Choice.pdf

Generative modeling of discrete data has two popular paradigms: autoregressive models such as GPT, which factorize a sequence in a left-to-right (L2R) order, and masked diffusion models, which are essentially any-order autoregressive modeling. Rather than competing methods, these are the two extreme points of a single axis -- the generation order. For structured discrete domains without a natural traversal, both extremes may be suboptimal, yet the intermediate choice -- a single well-adapted order -- remains largely unexplored. We introduce OrderGPT, which builds on Any-Order GPT to learn a task-level generation order without canonical-order supervision. Our key observation is that predicting variables from randomly sampled reveal prefixes produces recurring attention patterns in the backbone that provide a model-dependent signal of predictive dependencies. We aggregate this signal into a reciprocal dependency graph and use a spectral teacher to derive continuous generation priorities. A lightweight OrderMLP integrated into the GPT backbone learns to predict these priorities from attention, incorporating order learning into the architecture within a single training run. Training gradually shifts toward the learned order, which is then frozen for subsequent autoregressive training and generation. The same mechanism adapts across modalities: adaptively it recovers near-L2R dependency structure in language, learns anatomically organized factorizations on human pose, and discovers a factorization on tabular data that places statistically and semantically related fields nearby, while improving downstream modeling metrics across all domains. The code is available at https://github.com/Chenhe-yang/OrderGPT/.

## 13. Geometry-Aware Interpolation for Inverse Problems

- Authors: Pourya Shamsolmoali, Masoumeh Zareapoor
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-17
- DOI: Unavailable
- Categories: cs.CV, cs.LG
- Relevance: 3.1491949613798518
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.24687v1
- PDF: https://arxiv.org/pdf/2610.24687v1
- Local PDF: pdf/2026-10-21_13_Geometry-Aware Interpolation for Inverse Problems.pdf

Recovering missing visual information from incomplete or degraded images remains a challenging problem, particularly when spatial variations and complex image structures affect reconstruction accuracy. Although Spatial Transformer Networks (STNs) facilitate spatial feature alignment, their reliance on conventional linear or bilinear interpolation limits their ability to capture the underlying geometric characteristics of image data. Furthermore, interpolation based on a restricted set of neighbouring pixels can introduce inconsistencies in gradient propagation, potentially affecting optimisation stability. To address these limitations, we propose a Geometry-Aware Interpolation Network (GAIN), a variational autoencoder-based framework that incorporates manifold geometry into spatial transformation and image reconstruction. Rather than estimating pixel intensities solely from fixed spatial neighbours, GAIN exploits the local tangent structure of the data manifold to construct geometry-informed intensity approximations. An entropy-based regularisation mechanism further guides the estimation of spatial transformation parameters, promoting more adaptive interpolation. In addition, a convolutional normalisation strategy is introduced to regulate the magnitude of non-zero activations and improve gradient stability during training. Extensive experiments on challenging image completion and classification benchmarks demonstrate the effectiveness of GAIN in improving predictive accuracy while reducing computational cost compared with existing methods.

## 14. Estimating Causal Bounds from Observational Data With Neural Generative Models

- Authors: Max Zhu, Srivathsan Amruth, Sina Akbari, Qingyuan Zhao
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-18
- DOI: Unavailable
- Categories: stat.ME, cs.LG
- Relevance: 3.140837001073181
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.25246v1
- PDF: https://arxiv.org/pdf/2610.25246v1
- Local PDF: pdf/2026-10-21_14_Estimating Causal Bounds from Observational Data With Neural Generative Models.pdf

Identifying causal bounds from discrete observational data is a fundamental problem in causal inference. While exact analytical bounds exist for certain graphs, this is not generally the case. In this paper, we introduce a framework for estimating such bounds using neural generative models together with a new extrapolation procedure to estimate these bounds more accurately. Across multiple causal inference settings, it produces bounds that are consistently closer to the true bounds than those obtained with existing general neural approaches. We validate the framework on a range of benchmark problems for which exact bounds are available.

## 15. Do LMs Know What Variables Do? Interpreting Code Representations via Variable Roles

- Authors: Célian Vasson, Daniil Ognev, Kentaro Inui, Benjamin Heinzerling
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-16
- DOI: Unavailable
- Categories: cs.CL, cs.LG
- Relevance: 3.1279225818350254
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.24118v1
- PDF: https://arxiv.org/pdf/2610.24118v1
- Local PDF: pdf/2026-10-21_15_Do LMs Know What Variables Do_ Interpreting Code Representations via Variable Roles.pdf

Variable roles describe recurring behaviors such as accumulation, traversal, and retaining the best candidate encountered. We use Sajaniemi's independently defined taxonomy to study which role distinctions can be recovered from large language models, how sparse autoencoders (SAEs) retain those distinctions, and whether associated directions support control of generation. We introduce static annotation rules for all eleven roles and a corpus of 126,926 natural-code files across five languages. Across five model-SAE systems, residual probes outperform individual SAE features and tested lexical baselines, with modest losses after neutral target renaming. Combining SAE features closes much of the single-feature gap, but probes on SAE reconstructions are less sensitive to role-changing edits reviewed by LLMs. High paired ranking accuracy coexists with frequent false positives at fixed thresholds. During generation, interventions often change role annotations at the cost of correctness; changes accompanied by passing tests show no clear aggregate advantage over random controls. The benchmark separates role-related recoverability, SAE fidelity, and correctness-preserving control through matched prediction, source edits, and generation interventions.

## 16. Modaliff: A Unified Token Diffusion Model for Any-to-Any Generation

- Authors: Duc Kieu, Kien Do, Minh Khoa Le, Tung Kieu, Dang Nguyen, Thin Nguyen
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-18
- DOI: Unavailable
- Categories: cs.CV, cs.AI
- Relevance: 3.11569354587522
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.25533v1
- PDF: https://arxiv.org/pdf/2610.25533v1
- Local PDF: pdf/2026-10-21_16_Modaliff_ A Unified Token Diffusion Model for Any-to-Any Generation.pdf

Any-to-any generation seeks a single model that translates flexibly among text, image, and audio, yet existing approaches either require fully aligned multimodal tuples or a shared representation that suppresses modality-specific structure. We introduce Modaliff, a novel token-based diffusion model that learns from widely available bimodal pairs while preserving each modality in its native latent sequence. Modaliff assembles conditions and targets into a unified token sequence, with per-token attributes to disambiguate token identities and role-based positional embedding to preserve each modality's internal structure across sequence layouts. This design enables a single denoiser to support diverse generation tasks without task-specific architectural changes or a shared cross-modal latent space. Beyond one-to-one generation, Modaliff supports multiple conditions either by combining single-condition predictions at inference or by lightweight finetuning on captions that jointly describe multiple inputs. Experiments across text, image, and audio show that Modaliff achieves the best fidelity among any-to-any models on most generation tasks while using substantially fewer parameters and training data.

## 17. OpenVLHarness: Real World Visual Agentic Tool-Use with Multimodal Memory

- Authors: Yu Zhou, Cheng-Fu Yang, Rui Sun, Di Wu, Sibo Peng, Mingyang Zhang, Zhen Yang, Ruiyi Zhang, Nanyun Peng, Zhe Gan, Kai-Wei Chang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-19
- DOI: Unavailable
- Categories: cs.CL, cs.AI, cs.CV, cs.LG, cs.MM
- Relevance: 3.1133902117689463
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.26860v1
- PDF: https://arxiv.org/pdf/2610.26860v1
- Local PDF: pdf/2026-10-21_17_OpenVLHarness_ Real World Visual Agentic Tool-Use with Multimodal Memory.pdf

Multimodal large language models (MLLMs) have made rapid progress on visual reasoning, yet many tasks require evidence that is difficult to obtain through internal reasoning alone: our controlled study on 22 benchmarks shows that simply increasing the inference budget of the base model yields only modest gains. Such tasks demand grounded perception, external knowledge, and numerical measurements obtained through heterogeneous tools, whose outputs must be made interpretable to the model and retained across reasoning steps. We introduce OpenVLHarness, a multimodal reasoning harness organized around a capability layer and persistent multimodal memory. The capability layer combines task-level tool interfaces with evidence rendering, providing consistent access to heterogeneous backends and converting their outputs into model-readable observations. Persistent multimodal memory retains the corresponding images, structured data, and web references as addressable artifacts throughout each query. A coding interface executes generated programs over stored data, enabling computations that combine results from multiple tools. Together, these mechanisms support an iterative process of acquiring, inspecting, and composing multimodal evidence. Evaluated on 22 benchmarks with eight open and proprietary backbones, OpenVLHarness improves average scores by 9.7-12.6 points over matched no-tool baselines, including +11.2 with Qwen3-VL-8B, +9.7 with Kimi K3, and +9.9 with GPT-6 Astra. With GPT-6 Luna at medium reasoning effort, OpenVLHarness outperforms the base model, Codex, and Visual Sketchpad at maximum effort by 7.7-8.5 points while incurring at most 37% of their model-token cost.

## 18. ReTrace: Visual Backtracking for Efficient Multimodal Large Language Models

- Authors: Guangzong Si, Dong Wang, Yifan Yu, Miao Liu, Panwang Pan, Wentao Zhu
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-18
- DOI: Unavailable
- Categories: cs.CV, cs.AI
- Relevance: 3.0833302500774895
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.25005v1
- PDF: https://arxiv.org/pdf/2610.25005v1
- Local PDF: pdf/2026-10-21_18_ReTrace_ Visual Backtracking for Efficient Multimodal Large Language Models.pdf

Multimodal Large Language Models (MLLMs) encode images into dense visual token sequences, creating substantial attention and KV-cache overhead. Existing visual token compression methods reduce this cost by pruning low-saliency tokens in shallow layers, but this practice couples temporary computational deactivation with irreversible information deletion. We show that this coupling breaks an intrinsic inference pattern in MLLMs. Through layer-wise attention analysis, we identify \textbf{Visual Backtracking}: visual pivots remain spatially stable, yet in middle layers they actively retrieve context from tokens that appeared unimportant earlier. Thus, early low-saliency tokens can be inactive for computation while still being useful for later reasoning. Motivated by this finding, we propose \textbf{ReTrace}, a backtracking-aware compression framework that introduces a dormant token state. ReTrace caches non-pivot tokens outside expensive layer-wise computation, restores them during the backtracking window, and prunes only after their information has been absorbed. Experiments on Qwen2.5-VL and InternVL3 demonstrate nearly 90\% reductions in FLOPs and KV cache, a 2.83$\times$ prefilling speedup, and strong performance retention across complex vision-language benchmarks.

## 19. Simulation-free approximate Bayesian computation for stochastic reaction networks

- Authors: Zekai Li, Mauricio Barahona, Philipp Thomas
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-19
- DOI: Unavailable
- Categories: q-bio.QM, math.DS, math.OC, physics.bio-ph, stat.ME
- Relevance: 3.0829235504307495
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.26361v1
- PDF: https://arxiv.org/pdf/2610.26361v1
- Local PDF: pdf/2026-10-21_19_Simulation-free approximate Bayesian computation for stochastic reaction networks.pdf

Uncovering stochastic reaction networks from data is central to single-cell biology. Simulation-based inference has evolved into a flexible paradigm for this purpose, circumventing the computational intractability of the likelihood. Notably, approximate Bayesian computation performs this inference by carrying out extensive Gillespie simulations, usually at a high computational cost. Here, we propose a simulation-free approximate Bayesian computation (SFABC) framework that avoids both simulation and explicit likelihood solutions of the network dynamics. Instead, SFABC exploits the Chemical Master Equation to formulate a tractable convex optimization with ensuing constraints, which are then used to accept sampled parameters consistent with the observed data. The resulting posterior approximation comes with theoretical guarantees: it can be tightened systematically, and it provably converges to the exact Bayesian posterior distributions. Using synthetic benchmarks, we show that SFABC matches the accuracy of standard simulation-based algorithms at a substantially reduced computational cost. We then showcase the applicability of SFABC to experimental systems biology by analyzing gene transcription bursting kinetics from snapshot, time-resolved, and cell-cycle-resolved single-cell data.

## 20. Knowledge Manifold Optimization for Scientific Discovery

- Authors: Shigeru Obayashi, Yoshiaki Kawagoe, Kazuhiko Komatsu, Tomonaga Okabe
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-19
- DOI: Unavailable
- Categories: cs.IR, cs.LG
- Relevance: 3.0599012454422816
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.25662v1
- PDF: https://arxiv.org/pdf/2610.25662v1
- Local PDF: pdf/2026-10-21_20_Knowledge Manifold Optimization for Scientific Discovery.pdf

The rapid expansion and specialization of scientific literature make it increasingly difficult to identify not only what is known, but where new and still supportable knowledge may emerge. We introduce Knowledge Manifold Optimization (KMO), a discovery-oriented extension of the Knowledge Manifold framework that treats scientific discovery as a multiobjective search over a continuous, literature-derived knowledge space. Candidate locations are evaluated using four complementary objectives: persistent knowledge-regime boundary strength, band-pass white-space novelty, semanticgradient magnitude, and evidential support. Rather than collapsing these criteria into a single weighted score, KMO identifies Pareto-optimal Supported Knowledge Gaps, defined as corpus-relative unoccupied regions that remain sufficiently supported by surrounding literature. The method is demonstrated on a 99-paper corpus in aerodynamics and aerodynamic design. On a 21 x 21 grid, exact Pareto analysis produced 19 non-dominated points, of which 16 formed the practical front after excluding points with zero white-space score. These solutions exhibited distinct discovery modes, including methodology bridges, aero-structural topology/FSI integration, functional aerodynamic-device integration, and rear-wake/vehicle flow-control integration. A distance-maximization baseline preferentially selected extrapolative regions with substantially lower support and reliability, demonstrating why emptiness alone is insufficient. Representative Pareto locations were converted into auditable evidence packages and then verbalized by a constrained large language model into candidate research hypotheses. The results show that scientific discovery can be formulated as structured multi-objective search in an explicit knowledge space, while keeping novelty corpus-relative and separating numerical discovery from downstream language generation.

## 21. Muse Glimmer 30B: An On-Device Agentic Model

- Authors: Arash Ebrahim Abtahizadeh, Muna Aghamelu, Adil Ahmed, Juan C. Angeles Acuna, Alexis Audran-Reiss, Asaf Avrahamy, Yoram Bachrach, Can Balioglu, Amar Budhiraja, Onur Çelebi, Gaurav Chaurasia, Joy Chen, Lynn Cherif, Lucia Cipolina-Kun, Gal Cohen, Timothée Darcet, Beto de Paola, Digant Desai, Sam Devlin, Derek Dunfield, Ivan Evtimov, Maryam Fazel-Zarandi, Rob Fergus, Jean-Christophe Gagnon-Audet, Grant Gardner, Bhavul Gauri, Paris Giampouras, Sujan Kumar Gonugondla, Antoine Grosnit, Young Han, Michael Hassid, Monuril Islam, Masoud Jalili Sabet, Songhao Jia, Narine Kokhlikyan, Svetlana Kurtsman, Sandra Lefdal, Chee Hau Leow, Noam Levi, Mike Lewis, Sanae Lotfi, Xiyang Luo, Despoina Magka, Saeed Mahloujifar, Neal Mangaokar, Ishita Mediratta, Alexander H. Miller, Hela Momand, Saba Nazir, Kelvin Niu, Mattia Opper, Parth Pathak, Alberto Pepe, Danielle Pintz, Mikhail Plekhanov, Sidhartha Reddy Potu, Anton Protopopov, Shengyi Qian, Shashank Rajput, Joseph Rocca, Scott Roy, Luca Sbordone, Amin Shakeri, Tatiana Shavrina, Michael Shvartsman, Ruan Silva, Anya Sims, Eric Michael Smith, Hugo Touvron, Mabel Ubong, Isabel Urrego, Yanzheng Xiang, Zhiyuan Yao, Alex Yarmula, He Ye, Jade Yu, Luke Zettlemoyer, Arman Zharmagambetov, Perpetua Fathima Ahlijah, Tremo Ahmed, Enrique Alfonseca, Pedram Bashiri, Nikolay Bashlykov, Aaron Berman, Rohith Bhatia, Siddharth Bhattacharya, Prashant Bhende, Chloe Bi, Shuchao Bi, Clement Anthonioz Blanc, Allen Bolourchi, Andrea Caciolai, Erica Cai, Xiang Tony Cao, Yue Cao, Andrew Caples, Jinzhao Chang, Lele Chen, Moya Chen, Weijie Chen, Wenhu Chen, Xiaobai Chen, Yinyin Chen, Zhengxing Chen, Wei Cheng, Pavel Chikulaev, Edward Chou, Sy Choudhury, Brian Clerkin, Marta R. Costa-jussà, Curtis Davis, Myra Deng, Dujian Ding, Hantian Ding, Shuangrui Ding, Jesse Dodge, Shweta Doshi, Shirin Eghtesadi, Faith Eischen, Athyu Eleti, Alex Fabbri, Han Fang, Paula Farani, Aiman Farooq, Christoph Feichtenhofer, Darius Feher, Amanda Felix, Carl Chengyan Fu, Sean Gahagan, Yifan Gao, Itai Gat, Akashdeep Goel, Ahuva Goldstand, Bo He, David Heineman, Dylan Herman, Irene Hjelt, Joonas Hjelt, Alexander Holz, Rui Hou, Annie Hu, Yuan-Ting Hu, Bernie Huang, Jing Huang, Kun Huang, Pere-Lluís Huguet Cabot, Ashley Hunter, Srinivasan Iyer, Somya Jain, Michael Jiang, Song Jiang, Wenwen Jiang, Lin Jin, Jacob Kahn, Melanie Kambadur, Yingxin Kang, Justine Kao, Stephane Kasriel, Hossein Kavianihamedani, Ameya Khandekar, Yash Khare, Gefen Kohavi, Kavya Kopparapu, Praveen Krishnan, Venu Kuchibhotla, Ananya Kumar, Leona Lan, Jack Lanchantin, Hunter Lang, Nikolay Pavlovich Laptev, Yuanzhi Li, Yunlu Li, Asad Liaqat, Johnson Lin, Runwei Lin, Zhichao Lin, Shaun Lindsay, Yaron Lipman, Frederick Liu, Mengchen Liu, Qiang Liu, Yinghai Lu, Yujie Lu, Christopher Luc, Faye Ma, Pingchuan Ma, Tengyu Ma, Wufei Ma, Xiaodong Ma, Damir Maksyutov, Josh Malone, Udeep Manchanda, Thomas Mann, Kalyani Marathe, Roberto-Rafael Maura-Rivero, Ruslan Mavlyutov, Thomas Mesnard, Julian Michael, Sagar Miglani, Todor Mihaylov, Naureen Mitha, Archi Mitra, Leo Mok, Naila Murray, Muthukumaravel Muthuraman, Mergen Nachin, Nese Demir Nalci, Saaketh Narayan, Alyssa Newcomb, Peter Ney, Joycelyn Ng, Devin Norder, Maxwell Nye, Rajvardhan Oak, Cody Ohlsen, Artidoro Pagnoni, Yi Pan, Nilesh Pandey, Guan Pang, Richard Yuanzhe Pang, Mahesh Pasupuleti, Parth Patel, Yash Patel, Vladan Petrovic, Norman Ponte, Yundi Qian, Zengyi Qin, Jack Rae, Emmanuel Ramirez, Ramya Raghavendra, Nikhila Ravi, Hongyu Ren, Riandy Riandy, Harrison Rudolph, Kalyan Saladi, Eduardo Sánchez, Karthik Abinav Sankararaman, Aman Shankar, Paresh Shenoy, Alana Shine, Hamid Shojanazeri, Iva Simon-Bubalo, Mitesh Kumar Singh, Tiffany Siqi, Pawan Sisodiya, Ali Sol, Sten Sootla, Leslie St. Pierre, DiJia Su, Suraj Subramanian, Brian Sun, Tony Sun, Zhiqing Sun, Natacha Supper, Jason Talpalar, Ellen Xiaoqing Tan, Liang Tan, Jean-Christophe Testud, Parth Thakkar, Joseph Tighe, Ty Toledano, T Tse, Igor Tufanov, Alex Vaughan, Josh Walters, Alex Wang, Bethany Wang, Meng Wang, Rocky Wang, Weiyue Wang, Xiaolan Wang, Xin Wang, Zijian Wang, Bram Wasti, Quentin Wellens, Yeming Wen, Mary Williamson, Yuncheng Wu, Fei Xia, Tian Xie, David Xu, Jacob Xu, Puxin Xu, Zheng Xu, Shen Yan, Megan Yang, Yining Yang, Nick Yannopoulos, Kevin Yao, Michihiro Yasunaga, Haoxuan You, Michael You, Dingli Yu, Tianhe Yu, Summer Yue, Xiang Yue, Shuwei Zeng, Hanwen Zha, Chen Zhang, Hongming Zhang, Kaiyu Zhang, Meng Zhang, Mingyang Zhang, Yi Zhang, Shengjia Zhao, Chao Zhou, Claire Zhou, Shuyan Zhou, Yanjun Zhou, Yaxuan Zhou, Rosalie Zhu, Yun Zhu
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-17
- DOI: Unavailable
- Categories: cs.CL, cs.AI
- Relevance: 3.0045052231378717
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.24628v1
- PDF: https://arxiv.org/pdf/2610.24628v1
- Local PDF: pdf/2026-10-21_21_Muse Glimmer 30B_ An On-Device Agentic Model.pdf

We introduce Muse Glimmer, an open-source 30B parameter causal language model with perception encoder, purpose-built for autonomous agentic tasks on consumer hardware. Muse Glimmer integrates multi-step reasoning, reliable tool use and failure recovery into a single model that runs locally on consumer devices without requiring cloud infrastructure. The model accepts text and image inputs and produces text outputs, was trained on data from over a hundred languages, and is quantized to approximately 4-bit precision for efficient single-GPU inference. Muse Glimmer achieves state-of-the-art performance for its size class on agentic benchmarks, setting a new standard compared to the models of its size: Gemma4-31B and Qwen3.6-27B on tool use, multi-step planning, and agentic task completion. We release the model under the Apache 2.0 license to foster open-source development of capable, safe, local AI agents.

## 22. MELD: Recursive Self-Improvement via Hierarchical Coordination for Multi-Agent Scientific Discovery

- Authors: Sizhe Tang, Zuyuan Zhang, Zeyu Fang, Tian Lan
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-17
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 3.0018821260982254
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.24454v1
- PDF: https://arxiv.org/pdf/2610.24454v1
- Local PDF: pdf/2026-10-21_22_MELD_ Recursive Self-Improvement via Hierarchical Coordination for Multi-Agent Scientific Discovery.pdf

Multi-agent scientific discovery with large language models raises a coupled learning problem: research assignments determine both which experiments are pursued and the experiences from which agents adapt. We introduce MELD, a unified hierarchical test-time training framework that jointly adapts a team-level Coordinator policy and agent-level individual Scientist policies within a single discovery process. The Coordinator generates a joint portfolio of search branches and research directives over a shared derivation tree, while Scientists develop hypotheses and execution plans implemented by a shared frozen Executor. Both levels receive alternating GRPO-style parameter updates under a shared smooth best-of-budget objective, allowing team organization and individual research behavior to co-evolve in a recursive self-improvement loop. Our analysis establishes objective alignment for the hierarchy, characterizes conditions for coordination gains over independent parallel discovery and the first-order benefit of private adaptation, and derives a finite-budget regret bound for adapted models. On 22 MLGym and MLE-bench tasks, MELD is best on 20 of them and achieves the highest aggregate normalized scores on MLGym, using a 4B backbone for coordination and research. Most baselines use proprietary Scientists, and all systems share one frozen Executor.

## 23. Learning to Couple: Context-Adaptive Joint Denoising for Diffusion Language Models

- Authors: Zilei Shao, Ian Li, Heng Zhao, Kewei Lian, Guy Van den Broeck, Zhe Zeng, Anji Liu
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-19
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.0011253681547396
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.25723v1
- PDF: https://arxiv.org/pdf/2610.25723v1
- Local PDF: pdf/2026-10-21_23_Learning to Couple_ Context-Adaptive Joint Denoising for Diffusion Language Models.pdf

Diffusion language models accelerate generation by predicting multiple tokens in parallel, but factorized denoisers treat simultaneous predictions as conditionally independent. Decoding heuristics reduce the resulting errors by controlling which tokens are committed, but leave the underlying distribution factorized. Joint modeling addresses the source of the problem, yet existing methods attach separately learned layers to frozen denoisers, leaving the backbone unadapted to the joint objective and the coupling parameters fixed across contexts. We propose Codpula, a context-parameterized denoiser combining a Transformer with a tractable probabilistic inference layer. Given a partially masked input, the Transformer produces token potentials that shape per-position predictions and compact gates that modulate the layer's coupling parameters, yielding a context-dependent joint distribution while retaining exact conditional inference. We jointly optimize both components under a conditional denoising objective using a dual-flow multiplicative update that preserves valid probabilistic parameters. At inference, Codpula supports standard heuristics and uses conditional queries to adapt commitments to dependencies among proposed tokens without extra Transformer evaluations within a step. Codpula sets new state-of-the-art results across a broad suite of reasoning benchmarks while advancing the accuracy-latency Pareto frontier in mathematical reasoning and code generation.

## 24. Think, Compress, Answer: Reinforcement Learning for Multimodal Grounding via Reasoning Compression

- Authors: Jinbae Seo, Hyeongjun Kwon, Jiyoung Lee, Hyunsung Jang, Namkoo Ha, Jungin Park, Kwanghoon Sohn
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-19
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 3.0005470571990194
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.25640v1
- PDF: https://arxiv.org/pdf/2610.25640v1
- Local PDF: pdf/2026-10-21_24_Think, Compress, Answer_ Reinforcement Learning for Multimodal Grounding via Reasoning Compression.pdf

Extended reasoning has substantially improved multimodal large language models (MLLMs) on tasks requiring compositional and relational inference. However, multimodal grounding imposes a distinct requirement: reasoning must ultimately converge on a target-specific compact representation that supports precise localization. As reasoning trajectories grow longer, they often expand into broad scene narratives and peripheral relational details, which can dilute grounded perceptual evidence and lead to ambiguous or incorrect predictions. Motivated by the information bottleneck principle, we propose Think-Compress-Answer (TCA), a reinforcement learning framework that decomposes multimodal grounding into three phases: free-form reasoning, target-aware context compression, and answer generation conditioned on the compressed context. TCA is optimized through a multi-stage Group Relative Policy Optimization (GRPO) with progressive rewards that establish the structured output protocol, minimize reasoning-specific information while preserving target-relevant content, and directly improve localization accuracy. This staged design enables MLLMs to retain the benefits of extended reasoning while distilling it into the minimal context required for grounding. Experiments across six multimodal grounding benchmarks show that TCA attains substantial zero-shot performance gains, demonstrating the effectiveness of reasoning compression.

## 25. Reducing double-dipping in single-cell topic models with three-way count splitting

- Authors: Zheng Qu
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-16
- DOI: Unavailable
- Categories: q-bio.GN, cs.LG
- Relevance: 2.9789954607102014
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.24130v1
- PDF: https://arxiv.org/pdf/2610.24130v1
- Local PDF: pdf/2026-10-21_25_Reducing double-dipping in single-cell topic models with three-way count splitting.pdf

Topic models learn gene programs from single-cell RNA sequencing (scRNA-seq) data, and the same counts are then used to test which genes and donors are associated with those programs. Count splitting is the standard remedy for this reuse, but it has not been tested when an encoder reads each cell's counts. On a 104,400-cell lupus cohort with 300 permuted null genes per run, naive tests rejected 36% of null gene-topic pairs at a nominal 5% level, and the usual two-way split rejected 38%, because the encoder sees the tested gene's own held-out count. Encoding topic usage on a separate third of the counts, with beta-binomial thinning, lowered this to 7.7% (6.7% for genes outside the model); for two other models, LDVAE and scETM, the rate was 7.0-7.3% (naive 51-59%). A label-free interferon program shifts in held-out counts in the lupus cohort and in a pre-specified COVID-19 cohort, and donor-level topic usage predicts disease (AUROC 0.96) beyond cell-type proportions (0.86 and 0.58 in the two cohorts). Calibration and prediction did not depend on the model. We do not claim better clustering, prediction or topic stability. Code, figures and result tables are public (MIT license; DOI 10.5281/zenodo.23307193).

## 26. NADS: Navigator-Guided Data Selection for Mitigating Catastrophic Forgetting in Fine-Tuning

- Authors: Jianhao Zhang, Ou Wu, Yi Du
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-19
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 2.969358233188406
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.25751v1
- PDF: https://arxiv.org/pdf/2610.25751v1
- Local PDF: pdf/2026-10-21_26_NADS_ Navigator-Guided Data Selection for Mitigating Catastrophic Forgetting in Fine-Tuning.pdf

Catastrophic forgetting is a central obstacle in single-stage fine-tuning of large language models (LLMs) on a new task, especially when the original pretraining data are unavailable. Synthetic data offers a practical mitigation path, but candidate pools are often noisy and redundant, making effective selection essential. Existing methods often rely on indirect proxy signals whose alignment with actual training benefit can be limited, while utility--diversity selection over large candidate pools remains computationally demanding. To address these challenges, we propose NAvigator-guided Data Selection (NADS), a fine-tuning framework for LLMs. NADS first follows the target fine-tuning recipe without preservation regularization to obtain a navigator model, whose deviation from the pretrained model exposes recipe-induced capability drift. It then uses the predictive divergence between the navigator and the pretrained model to score forgetting-aware utility for each synthetic candidate, and constructs a constraint set through an efficient utility--diversity selection strategy. Finally, NADS fine-tunes on the new-task data while distilling pretrained behavior on the selected constraints to preserve general capabilities. Experiments show that NADS delivers a stronger balance between new-task performance and general capability preservation, while reducing utility--diversity selection overhead. Code at: https://github.com/zjh-vinky/NADS.

## 27. HybridResearcher: Bridging the Structured-Unstructured Boundary for Deep Research Agents

- Authors: Soyoung Yoon, Peiran Xu, Han Wang, Ruofan Wu, Xiaodong Yu, Feng Yan, Mohit Bansal, Debiao Li, Seung-Won Hwang, Yuxiong He, Zhewei Yao
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-17
- DOI: Unavailable
- Categories: cs.AI, cs.CL
- Relevance: 2.9607794650657326
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.24899v1
- PDF: https://arxiv.org/pdf/2610.24899v1
- Local PDF: pdf/2026-10-21_27_HybridResearcher_ Bridging the Structured-Unstructured Boundary for Deep Research Agents.pdf

While LLM agents are increasingly capable of gathering and synthesizing evidence from a single homogeneous source, such as structured tables or unstructured data, real-world analytical questions frequently span heterogeneous sources. For example, answering one enterprise question may require both a result computed over an internal database and evidence found on the web. Recent evaluations on benchmarks like HybridDeepResearch show that even frontier agents struggle when evidence must cross this boundary. While these benchmarks have exposed the limitation, methodologies to explicitly teach cross-source reasoning remain absent. To address this, we introduce HybridResearcher, a 4B agent trained to bridge evidence across the structured and unstructured boundary. To build it, we synthesize cross-source bridge trajectories by starting with validated single-source tasks-such as existing text-to-SQL or web search queries-and fabricating the missing source around a bridge entity drawn from the seed's own output. We retain a sample only when strict construction gates confirm that neither side alone suffices, ensuring the data requires true cross-source interdependence. Finally, we train on this curated dataset using supervised fine-tuning followed by reinforcement learning. Evaluated on the existing HybridDeepResearch benchmark, HybridResearcher improves over our base model, Qwen3.5-4B, by 30.0 points pass@8 and surpasses the far larger Qwen3.5-397B-A17B by 8.3 points, while also improving over its base model on established, held-out single-source benchmarks (BrowseComp and BrowseComp-Plus), demonstrating that this complex cross-source reasoning can be taught directly to small models without triggering catastrophic forgetting.

## 28. BEM: Learning Bregman Divergences for Concept Erasure in Flow Matching Models

- Authors: Mohamed-Hicham Leghettas, Markus Püschel
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-17
- DOI: Unavailable
- Categories: cs.LG, cs.CV
- Relevance: 2.9441395257805447
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.24508v1
- PDF: https://arxiv.org/pdf/2610.24508v1
- Local PDF: pdf/2026-10-21_28_BEM_ Learning Bregman Divergences for Concept Erasure in Flow Matching Models.pdf

Concept erasure removes harmful, private, or copyrighted concepts from text-to-image models while preserving their other abilities. Leading models such as FLUX and Stable Diffusion 3 are trained with flow matching, and erasure methods for them fine-tune the model toward a guided teacher's velocities under a Euclidean loss. Yet the squared distance is only one member of a larger family: Bregman divergences are exactly the losses under which flow matching recovers the correct velocity field, and each member shapes differently what is erased and what is preserved. We introduce BEM (Bregman erasure matching), which is, to our knowledge, the first to learn this divergence through bi-level optimization, so that the fine-tuned model forgets the concept on unseen prompts while its unrelated generations stay unchanged. In the experiments we target the suppression of nudity, violence, real identities, and copyrighted characters. Under the evaluation protocol of GEM, BEM removes more of the concept than GEM on most settings, cutting the unsafe rate on bloody gore from 53.9% to 14.4% and the FID on nudity from 8.64 to 6.64, while retention holds on some concepts and degrades on others.

## 29. TamedFlow: Trajectory-Aware Distillation\\for Teacher-Assisted Diffusion Sampling

- Authors: Shuaiqi Cheng, Jiahao Zhang, Boyuan Gu, Siyu You, Yuxi Chen, Haiying Xu, Zexin Lu, Huiyu Zhou, Xuming Hu
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-19
- DOI: Unavailable
- Categories: cs.CV, cs.AI
- Relevance: 2.939542039502313
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.26025v1
- PDF: https://arxiv.org/pdf/2610.26025v1
- Local PDF: pdf/2026-10-21_29_TamedFlow_ Trajectory-Aware Distillation__for Teacher-Assisted Diffusion Sampling.pdf

Diffusion Transformers (DiTs) deliver high-fidelity image and video generation, but inference requires many sequential model evaluations. Two acceleration strategies are increasingly important: model compression makes each evaluation cheaper, while adaptive inference avoids selected teacher computation through reuse, forecasting, or speculative execution. Their combination, however, is brittle: directly applying the evaluated adaptive methods to a compressed student can degrade quality, an observed failure mode we call the \textbf{Combination Gap}. We link this gap to a mismatch between pointwise distillation and short-horizon execution: a student trained at teacher states need not remain reliable when its own predictions are chained. We propose \textbf{TamedFlow}, which trains a compressed DiT for this deployed role through cross-architecture feature alignment, a near-identity Velocity Alignment Head, and randomized rollout supervision. At inference, a lightweight Learnable Trajectory Estimator routes completed drafts: accepted drafts bypass the teacher, while rejected drafts roll back and receive one teacher rescue step. Distilling DiT-XL/2 into DiT-B/2, TamedFlow reaches FID $2.58$ at $2.25\times$ measured speedup over DDIM-50 on ImageNet $256\times256$. Ablations support trajectory supervision, and routing controls favor LTE over random decisions at nearly matched latency. Evaluations on ImageNet $512\times512$, MS-COCO, and Latte/FaceForensics extend the empirical scope.

## 30. Steered Not Stirred: Effective Reward Tilting using Surrogate Reward Mixing

- Authors: Alec Sargood, Olivia Gallup, Georg Maierhofer, Noam Ghenassia, Paul Duckworth, Krisztina Sinkovics, Avishek Joey Bose
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-18
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 2.9253836487149467
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.25502v1
- PDF: https://arxiv.org/pdf/2610.25502v1
- Local PDF: pdf/2026-10-21_30_Steered Not Stirred_ Effective Reward Tilting using Surrogate Reward Mixing.pdf

Continuous-time generative models, from diffusion models, flow matching, and now flow maps, owe their practical value to high-fidelity generation and steerability. In many applications, a ground-truth latent ``oracle'' reward $R^*$ is unavailable or expensive to evaluate, e.g., human judgments or experimental measurements. Although the oracle reward is not directly observable, it can often be approximated through multiple cheaper surrogates that, individually, provide incomplete characterizations but collectively reveal substantial information about the downstream task. In this paper, we present a method for composing such surrogates to steer a pretrained model toward the distribution tilted by an unavailable $R^*$. Given a small feedback set of oracle rankings or numerical rewards, we introduce Mixing And Reward Tilting for INference-time Improvement (MARTINI), which learns a surrogate composition for plug-and-play use with standard inference-time steering methods. Our theory characterizes surrogate information limits and relates population recovery error to ideal-target KL at small tilt strength. For preferences, the bound additionally accounts for an irreducible mismatch between the Plackett-Luce population target and the conditional mean. Experiments demonstrate improved oracle-tilt fidelity in language generation and ImageNet alignment, and improved joint pose accuracy and validity in protein-ligand cofolding, without inference-time oracle queries.
