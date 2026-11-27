# Paper Daily Reading - 2026-11-27

## 1. A gene informed benchmark for BioScoring of pathology foundation models

- Authors: Paul Vilars, Vincent Quoc-Huy Trinh, Maria Vakalopoulou, Dimitris Samaras, Stergios Christodoulidis, Mahdi S. Hosseini
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-25
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.4562582476414025
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.34930v1
- PDF: https://arxiv.org/pdf/2611.34930v1
- Local PDF: pdf/2026-11-27_01_A gene informed benchmark for BioScoring of pathology foundation models.pdf

Pathology foundation models are usually compared by their performance on downstream tasks such as classification and retrieval. While such benchmarks measure how useful a model is, they provide no insight into the biology it represents. We introduce BioScore, a benchmark that quantifies how well an image encoder captures cell identities, with spatial transcriptomics of the same tissue as the reference. A sparse autoencoder splits the encoder's patch embeddings into sparse features, which we cluster into a fixed number of groups. BioScore then measures, for each of 52 cell identities defined by marker genes, how specifically one group follows the identity's expression over the tissue. Because the autoencoder training is fully unsupervised, a match shows that the model represents the cell identity from the image alone. We score 8 pathology foundation models and 3 natural-image models. Every pathology model scores above every natural-image model (0.299--0.371 \vs 0.214--0.232), and paired tests separate three tiers among the pathology models. Unlike a supervised probe, BioScore needs no labels, builds its reference from the data and scores even from few sections, yet it ranks the encoders as a probe does. Its per-identity breakdown indicates which cell identities each encoder captures or misses.

## 2. From Shared Patterns to Individual Evidence: Two-Stage Reasoning for Emerging Entities in Temporal Knowledge Graphs

- Authors: Jinchuan Zhang, Lei Gao, Hongyu Jiang, Chong Mu, Chenang Cai, Ke Yan
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-25
- DOI: Unavailable
- Categories: cs.AI, cs.CL, cs.LG
- Relevance: 3.4005287242798463
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.34708v1
- PDF: https://arxiv.org/pdf/2611.34708v1
- Local PDF: pdf/2026-11-27_02_From Shared Patterns to Individual Evidence_ Two-Stage Reasoning for Emerging Entities in Temporal Knowledge Graphs.pdf

Temporal knowledge graphs (TKGs) continually introduce emerging entities whose interaction histories evolve from zero-shot debuts into sparse, bursty few-shot trajectories. However, current paradigms are fragmented: pattern-transfer methods lack catalog-wide event memory, whereas online memory models suffer from endpoint-role asymmetry that degrades unseen-answer ranking. Furthermore, sparse early interactions exhibit both long-range dispersion and local redundancy under skewed distribution. To address these challenges, we propose INSPIRE (Integrating Shared Patterns and Individual Evidence for Reasoning), a two-stage forecasting framework over a known catalog. In Stage I, INSPIRE learns an availability-aware shared-pattern predictor that fuses event-updated memory across the full candidate catalog while applying coordinated query- and catalog-side masking. Subsequently, Stage II freezes this predictor and optimizes a lightweight individual-evidence adapter (EA) combining textual semantic priors with correlation-weighted long-range event statistics under support- and role-balanced co-answer supervision with prior-odds debiasing and soft residual alignment. In addition, we decompose evaluation by endpoint roles and track longitudinal emerging-answer cohorts via query-micro and answer-entity macro metrics. Across four benchmarks based on the ICEWS and GDELT event datasets, INSPIRE improves Emerging MRR by 16.73%-88.83% over the strongest baselines. Relative to paired Stage I predictors, EA further increases Emerging MRR by 8.28%-32.63%, Answer-new MRR by 7.81%-41.24%, and cohort macro MRR by 9.64%-39.94%, gains attributed to semantic priors and candidate-level score competition suppressing mismatched established competitors without zero-support prior shortcuts. The official code is publicly available at https://github.com/KcAcoZhang/INSPIRE.

## 3. A Causal Energy Prior for Learning Directed Acyclic Graphs

- Authors: Marco Scutari, Noriaki Sato, Shuichi Kawano, Rui Yamaguchi, Seiya Imoto
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-24
- DOI: Unavailable
- Categories: stat.ML, cs.LG, math.ST
- Relevance: 3.3466314645572517
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.33225v1
- PDF: https://arxiv.org/pdf/2611.33225v1
- Local PDF: pdf/2026-11-27_03_A Causal Energy Prior for Learning Directed Acyclic Graphs.pdf

Bayesian learning of directed acyclic graphs (DAGs) has long relied on non- or weakly informative priors, on the assumption that the information needed for an informative one is rarely available. In genetics and systems biology, annotation databases now make it possible to assemble a prior DAG before learning from data. Existing informative priors are local: they score a DAG arc by arc and cannot encode how interventions propagate along its paths. Thus, we propose the local-global energy prior (LGE), a Gibbs distribution over DAGs whose energy combines a local divergence from the prior DAG, the Structural Hamming Distance, and a causal one, the Structural Intervention Distance. We derive rules to calibrate its decay and the weight of the two divergences from the prior DAG alone. We quantify how much prior mass stays on the true DAG, and how much data overturn the prior, when the prior DAG is partially incorrect. In simulations, LGE improves both the structural accuracy of maximum a posteriori DAGs and the fit of the corresponding Bayesian networks to the true distribution over non- and weakly informative priors, even when half of the arcs of the prior DAG are wrong. We also showcase LGE on a gene regulatory network learned from single-cell kidney data.

## 4. Adaptive attention routing multimodal expert graph neural network for drug-drug interaction prediction

- Authors: Jingyi Yang, Chengcheng Yan, Hongri Cong, Feifei Zhao
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-17
- DOI: Unavailable
- Categories: q-bio.QM, cs.LG
- Relevance: 3.2252725876778134
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.33200v1
- PDF: https://arxiv.org/pdf/2611.33200v1
- Local PDF: pdf/2026-11-27_04_Adaptive attention routing multimodal expert graph neural network for drug-drug interaction prediction.pdf

Accurate prediction of drug-drug interactions (DDIs) is essential for drug safety in combination therapy. Multimodal methods built on knowledge graphs (KGs) already combine molecular structures, substructures, targets and biomedical relations into drug representations, but they still face three problems: features are heterogeneous across modalities, fusion does not adapt to individual drug pairs, and modality-specific information is diluted during integration. We propose the adaptive attention routing multimodal expert graph neural network (AARME-GNN) to address them. A Feature Adaptive Calibration Module (FACM) reduces within-modality noise in each representation through bottleneck reparameterization and channelwise recalibration before fusion. A Multimodal Weight Router (MMWR) then sets the modality weights of each drug pair, with an entropy constraint that prevents the weights from collapsing onto one modality. A Routing-Aware Weighted Distillation (RAWD) mechanism builds a soft target from the unimodal branches, so that the fusion classifier retains the knowledge held by each modality. On Dataset 1, AARME-GNN improves precision over MKG-FENN by 3.71 and 6.57 percentage points in known drug and known new drug prediction, and the area under the receiver operating characteristic curve (AUC) by 4.53 in new drug prediction. On Dataset 2, the advantage is concentrated in the two cold-start settings and in precision.

## 5. SparseKG‐Flow: A Virtual Cell Generative Architecture Unifying Structural Causal Models and Knowledge Graph Priors for Single‐Cell Drug Perturbation Prediction

- Authors: Chong-Xiao Peng, Menglong Gao, Xinkang Li, Ke Zhang, Hongliang Duan, Henry H. Y. Tong, Yuguang Mu, Jingjing Guo
- Source: openalex
- Venue type: journal
- Journal: Advanced Science
- Publication status: published
- Publication date: 2026-11-24
- DOI: https://doi.org/10.1002/advs.78922
- Categories: Computational Drug Discovery Methods, Single-cell and spatial transcriptomics, Gene Regulatory Network Analysis
- Relevance: 3.210124602468949
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://doi.org/10.1002/advs.78922
- PDF: https://onlinelibrary.wiley.com/doi/pdfdirect/10.1002/advs.78922
- Local PDF: Not downloaded

Predicting single‐cell responses to new drugs is essential for mechanism‐aware virtual cell modeling, yet existing models often fail on unseen drugs or cell types by relying on memorized correlations rather than transferable mechanisms. SparseKG‐Flow addresses this out‐of‐distribution (OOD) challenge as a generative architecture integrating three inductive biases: a sparse drug‐effect encoder with Gumbel–Softmax gating, a heterogeneous graph adapter for drug–target–pathway knowledge, and a mechanism‐guided residual flow decoder. On Tahoe‐100M, it achieves Pearson of 0.942 and 0.920 under Test‐NewDrug and Test‐NewCell settings, respectively, outperforming the next‐best baseline by 16.6% and 14.8%. It also reduces error by 89.0% and 91.7%, respectively, and more than doubles held‐out‐drug top‐gene recovery (Overlap@50 = 0.210). Frozen‐model evaluation on high‐grade serous ovarian cancer patient data provides preliminary evidence of transfer beyond the Tahoe‐100M panel. Ablations confirm all components aid OOD generalization, with the molecular knowledge adapter contributing the most. SparseKG‐Flow further reorganizes pharmacological priors into interpretable, task‐trained representations and highlights Abemaciclib, Capmatinib, and Gemcitabine in A549 analysis. It thus serves as both an accurate perturbation predictor and a mechanism‐grounded virtual cell platform for therapeutic prioritization.

## 6. The Missing Root: Geometric Imagination Without Images in Large Language Models

- Authors: Loïc Magnan, Tomasz Kozlowski
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-25
- DOI: Unavailable
- Categories: cs.CV, cs.CL, cs.LG
- Relevance: 3.1612082706993805
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.33841v1
- PDF: https://arxiv.org/pdf/2611.33841v1
- Local PDF: pdf/2026-11-27_06_The Missing Root_ Geometric Imagination Without Images in Large Language Models.pdf

This paper proposes a new paradigm and method for giving large language models spatial understanding. Standard language models operate exclusively over discrete words (secondary representations of things rather than continuous space itself), forcing them to guess geometry verbally. Whereas most multimodal approaches equate spatial grounding with camera images or video frames, spatial structure itself is not a picture: it consists of coordinate frames, solid boundaries, and how objects move and relate to each other in continuous space. Motivated by this distinction, we place continuous object tokens combining pose (position, orientation, and scale) and signed-distance shape embeddings alongside word tokens inside a single uninterrupted transformer sequence, allowing language and geometry to attend to each other as object scenes are built and updated step by step. Control tokens switch output automatically between natural-language words and continuous object state updates to a persistent object workspace, while an attention mask blocks earlier prose when generating the answer, so responses must be read directly from settled geometry. To prove this method works, we attach a narrow parallel spatial stream (+4.4% weights) alongside unfrozen Qwen3-1.7B layers. In our two-dimensional tests, the model spawns and transforms multi-object scenes from English descriptions, transfers shapes to held-out nouns, and relies causally on the workspace to answer spatial questions.

## 7. Stranger Things: When Objects Appear Without Their Typical Neighbors

- Authors: Siddhartha Gairola, Jiahao Xie, Anna Kukleva, Francesco Locatello, Bernt Schiele
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-25
- DOI: Unavailable
- Categories: cs.CV, cs.LG
- Relevance: 3.1543597766596165
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.34881v1
- PDF: https://arxiv.org/pdf/2611.34881v1
- Local PDF: pdf/2026-11-27_07_Stranger Things_ When Objects Appear Without Their Typical Neighbors.pdf

Visual context is a powerful cue for object recognition: scenes inform what, where, and at what scale objects are likely to appear. Yet over-reliance on context becomes a failure mode when models predict objects based on their typical neighbors rather than the objects' own visual features, which we call typicality bias. While extensively studied in the pre-Transformer era, it has often been assumed that architectural and scale improvements would naturally solve it, and a systematic diagnostic across the modern vision stack remains absent. We provide such a diagnostic framework. We measure typicality bias via normalized pointwise mutual information (NPMI) over object pairs, and introduce STRANGE-Bench (Synthetic Typicality-RANked Grounded Evaluation Benchmark): a photorealistic, layout-controlled benchmark spanning 17 sub-tiers from typical to never-co-occurring object pairs. Across five model families (specialist detectors, open-vocabulary detectors, self-supervised, vision-language, and multimodal large language models) and three recognition tasks (supervised detection, open-vocabulary detection, and classification), the bias is prevalent: gaps of 5-11 p.p. persist when objects appear outside their typical company, and do not consistently shrink with scale. To mitigate it, we turn to data augmentation: existing augmentations are designed for visual diversity, not for breaking co-occurrence shortcuts, and sample from the very distribution that produces typicality bias. We propose Anchor-Atypicality Sampling (AAS), a simple sampling rule for paste-based augmentations that uses the NPMI signal to tilt the training-time co-occurrence distribution toward atypical partners. AAS reduces the typicality gap by up to 1.6 p.p. on natural-image COCO splits and 23.0 p.p. on synthetic STRANGE-Bench across three model families, without sacrificing overall performance.

## 8. Uncovering directionally and temporally variable genes with STAVAG

- Authors: Qunlun Shen, Kuo Gai, Shang Li, Fangkun Yang, Hanbin Cui, Shuqin Zhang, Shihua Zhang
- Source: openalex
- Venue type: journal
- Journal: Nature Genetics
- Publication status: published
- Publication date: 2026-11-25
- DOI: https://doi.org/10.1038/s41588-026-02853-y
- Categories: Single-cell and spatial transcriptomics, Gene expression and cancer classification, Gene Regulatory Network Analysis
- Relevance: 3.1500410016566804
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://doi.org/10.1038/s41588-026-02853-y
- PDF: https://www.nature.com/articles/s41588-026-02853-y.pdf
- Local PDF: pdf/2026-11-27_08_Uncovering directionally and temporally variable genes with STAVAG.pdf

Spatially variable genes (SVGs) are crucial for understanding spatial heterogeneity in spatial transcriptomics. Yet SVGs are challenging to align with established biological axes and lack straightforward mechanistic interpretation, thereby limiting their ability to inform downstream experiments or clinical applications. Here, we introduce the concept of directionally variable genes (DVGs) and temporally variable genes (TVGs). In addition, we propose a unified framework, STAVAG (spatial- or temporal-aided framework for identifying directionally and temporally variable g enes), that models spatial or temporal information to identify DVGs and TVGs. STAVAG effectively identifies biologically meaningful DVGs for uncovering prognostically relevant gene modules that align with the malignant–immune–stroma structure in the tumor microenvironment, identifying marker genes in three-dimensional brain data and detecting 12 polarization genes regulating planarian regeneration. Furthermore, by tracking the progression of myocardial infarction and tissue development, STAVAG reveals critical TVGs that can serve as candidate biomarkers for the ultra-acute phase of myocardial infarction. STAVAG also identifies both global and local gene modules involved in mouse placentation, as well as tissue-specific and interactive TVG modules that dynamically evolve during mouse embryonic development.

## 9. Resolving cell states in spatial transcriptomics with SCATTER

- Authors: Lei Huang, Yun Gong, Weiqiang Lin, Lindong Jiang, Hui Shen, Chaoyang Zhang, Hong-Wen Deng
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-25
- DOI: Unavailable
- Categories: q-bio.QM
- Relevance: 3.13467529029563
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.34798v1
- PDF: https://arxiv.org/pdf/2611.34798v1
- Local PDF: pdf/2026-11-27_09_Resolving cell states in spatial transcriptomics with SCATTER.pdf

A capture spot can contain transcripts from multiple cell types. Differences between spots may reflect changes in cell-type proportions, expression within a cell type, or both, making local cell-type expression difficult to infer from mixed counts. We developed SCATTER to estimate cell-type proportions and relative expression profiles for each cell type at each spot from spatial transcriptomic counts, coordinates, and annotated single-cell reference data. SCATTER weights reference cell profiles using local spatial context, then jointly fits the resulting profiles and cell-type proportions to reconstruct spot counts. Cell2location estimates regularize the proportions. After fitting, SCATTER uses learned gene-specific calibration factors and fitted proportions to allocate observed counts among cell types. In five pseudo-spot benchmarks constructed from imaging data, SCATTER achieved higher cross-spot correlations with measured expression for 82.8-99.8% of evaluated gene-cell type pairs in pairwise comparisons with DestVI, PANDA, and STged. In breast cancer Xenium data, it recovered gene expression associated with the tumor neighborhood and regulon scores. In breast cancer Visium data, inferred stromal and macrophage expression showed distinct associations with neighborhood malignant cell proportions. In multiple sclerosis brain tissue, SCATTER recovered lesion-associated glial expression programs. In colorectal cancer Visium HD data, it mapped cell-type-specific programs at the invasive front and ranked candidate ligand-receptor pairs. SCATTER enables analysis of spatial expression variation within cell types from mixed tissue measurements.

## 10. Knowledge-Base Gradient Descent: Self-Structuring Learning through Question Answering

- Authors: Masahiro Kato
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-25
- DOI: Unavailable
- Categories: cs.AI, cs.LG
- Relevance: 3.1195273543049655
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.34841v1
- PDF: https://arxiv.org/pdf/2611.34841v1
- Local PDF: pdf/2026-11-27_10_Knowledge-Base Gradient Descent_ Self-Structuring Learning through Question Answering.pdf

We consider the problem of constructing knowledge bases for applications based on large language models, in which the structure of a knowledge base determines how an application can retrieve and connect the information needed to answer a question. We study Self-Structuring Learning, a setting in which questions and expected answers guide the construction of a persistent knowledge base whose editable structure can be a graph schema or the organization of linked knowledge documents. We propose Knowledge-Base Gradient Descent, which diagnoses discrepancies between expected answers and responses obtained through the current knowledge base. At each round, the method proposes a structural edit, rebuilds the knowledge base, and adopts the edit when the learning loss decreases. The retained structure is evaluated on other questions about the same sources. By randomizing over candidate edits, we express the loss change of an edit as a derivative with respect to the probability of selecting it, and we evaluate joint edits as single candidates because their changes interact. Schema Descent instantiates the method for graph schemas. In experiments on large documents, each a bundle of research papers, the updated knowledge cards and graph schemas obtain higher mean Answer F1 on held-out generated questions than their initial structures, with schema gains in every document. On human questions, mean F1 rises for schemas and falls for cards: the updated structures serve the kind of question they were learned from.

## 11. FIG-MAC: A Fine-grained Inspiration Graph Empowered Multi-Agent Collaboration for Automated Scientific Hypothesis Generation

- Authors: Siyuan Chen, Yuping Gao, Tai Huang, Yuling Zhou, Dongyu Su, Tongguan Wang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-25
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 3.11185949890299
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.33563v1
- PDF: https://arxiv.org/pdf/2611.33563v1
- Local PDF: pdf/2026-11-27_11_FIG-MAC_ A Fine-grained Inspiration Graph Empowered Multi-Agent Collaboration for Automated Scientific Hypothesis Genera.pdf

Automated Scientific Hypothesis Generation (ASHG) leveraging large language models (LLMs) aims to harness their strengths in knowledge integration, logical reasoning, and text generation for efficiently producing innovative, verifiable scientific hypotheses. However, existing approaches face three critical limitations: (i) insufficient fine-grained knowledge representation, as unstructured context impairs LLM comprehension and reasoning; (ii) lack of knowledge evolution traceability, constraining the generation of innovative cross-domain conjectures; (iii) absence of human-inspired and role-specialized multi-agent collaboration, failing to leverage the efficient innovation mechanisms arising from cognitive diversity and division of labor among expert roles to complete the full ASHG-evaluation loop. To address these limitations, we propose the Fine-grained Inspiration Graph-empowered Multi-Agent Collaboration framework (FIG-MAC) including: (i) Fine-grained Inspiration Graph module (FIG), to obtain fine-grained structured knowledge representations, where nodes represent academic semantic units and edges encode heuristic relationships among them; (ii) ontology-guided hybrid reasoning module, which follows the FIG ontology to construct structured reasoning paths and uses vector search to enrich them with semantic evidence, to obtain the traceable scientific conjecture paths; (iii) role-specialized Multi-Agent framework, inspired by real scientific teamwork, enabling a closed-loop process of scientific conjecture generation, screening, and validation. Experimental results demonstrate that FIG-MAC significantly outperforms state-of-the-art methods on source diversity, provenance-adjusted novelty, and raw novelty.

## 12. Can Its Own Misses Teach an MLLM to Find Small Brain Metastases?

- Authors: Yixuan Duan, Kexin Geng, Hanwen Xu, Wei Qiu
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-25
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 3.1006398657529792
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.33836v1
- PDF: https://arxiv.org/pdf/2611.33836v1
- Local PDF: pdf/2026-11-27_12_Can Its Own Misses Teach an MLLM to Find Small Brain Metastases.pdf

Multimodal large language models (MLLMs) are becoming general readers of medical images, yet they remain weak at locating small abnormalities. Brain metastases expose this gap: at 384 px a 0.1 mL lesion covers less than a quarter of one visual token, and at one false positive per scan frontier MLLMs find fewer than 30% of lesions of 0.1-1 mL. Fine-tuning on one dataset helps but transfers poorly, and improving it further is slow trial and error steered by a single score. We introduce LANTERN (Lesion-finding AgeNt Through Error-driven Recursive learNing), a framework in which an MLLM improves recursively from its own misses. LANTERN recasts model development as an error-driven loop: a failure census attributes every missed lesion to one of four causes, an LLM mentor revises one of four levels (evidence acquisition, visual representation, learning policy, decision aggregation) per round, and a rule frozen before the first round decides what is kept, without test data and with every tool call audited. Over 15 unattended rounds, LANTERN raises a fine-tuned 4B MLLM from finding 75% to 94% of lesions at one false positive per scan on BraTS-MET, and 91% of those of 0.1-1 mL, compared with at most 51% and 29% for five frontier MLLMs read under the starting protocol; the gains hold on an external cohort (89%) and on unseen meningiomas (77%). These results show that an MLLM's own misses, attributed to their causes, can drive its reliable recursive self-improvement.

## 13. Q-Zoom: Query-Aware Adaptive Perception for Efficient Multimodal Large Language Models

- Authors: Yuheng Shi, Xiaohuan Pei, Linfeng Wen, Minjing Dong, Chang Xu
- Source: openalex
- Venue type: journal
- Journal: IEEE Transactions on Pattern Analysis and Machine Intelligence
- Publication status: published
- Publication date: 2026-11-24
- DOI: https://doi.org/10.1109/tpami.2026.3756943
- Categories: Multimodal Machine Learning Applications, Advanced Neural Network Applications, Handwritten Text Recognition Techniques
- Relevance: 3.053842218728323
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://doi.org/10.1109/tpami.2026.3756943
- PDF: https://arxiv.org/pdf/2604.06912
- Local PDF: pdf/2026-11-27_13_Q-Zoom_ Query-Aware Adaptive Perception for Efficient Multimodal Large Language Models.pdf

Multimodal Large Language Models (MLLMs) require high-resolution visual inputs for fine-grained tasks like document understanding and dense scene perception. However, current global resolution scaling paradigms indiscriminately flood the quadratic self-attention mechanism with visually redundant tokens, severely bottlenecking inference throughput while ignoring spatial sparsity and query intent. To overcome this, we propose Q-Zoom, a query-aware adaptive high-resolution perception framework that operates in an efficient coarse-to-fine manner. First, a lightweight Dynamic Gating Network adaptively bypasses high-resolution processing when coarse global features suffice. Second, for queries demanding fine-grained perception, a Self-Distilled Region Proposal Network (SD-RPN) localizes the task-relevant Region-of-Interest (RoI) directly from intermediate feature spaces. To optimize these modules efficiently, the gating network uses a consistency-aware generation strategy to derive routing labels, while the SD-RPN employs a fully self-supervised distillation paradigm. A continuous spatio-temporal alignment scheme and targeted fine-tuning then fuse the dense local RoI with the coarse global layout. Extensive experiments demonstrate that Q-Zoom establishes a new Pareto frontier. Using Qwen2.5-VL-7B as a primary testbed, Q-Zoom accelerates inference by $2.5\times$ on Document & OCR benchmarks and $4.7\times$ in High-Resolution scenarios in accuracy-matched comparisons against the baseline's peak-accuracy token budget. Furthermore, at its largest visual-token budget, Q-Zoom surpasses the baseline's peak performance by 1.1% and 8.1% on these respective benchmarks, while keeping about $0.8\times$ of the base model's throughput at a matched token budget. These robust improvements transfer consistently to LLaVA, Qwen3-VL, encoder-free Gemma-4, and RL-based thinking-with-image models.

## 14. Verified experience improves materials prediction with large language models

- Authors: Yiming Zhang, Koji Tsuda
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-16
- DOI: Unavailable
- Categories: cs.CL, cond-mat.mtrl-sci, cs.AI
- Relevance: 3.0385671530544323
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.33195v1
- PDF: https://arxiv.org/pdf/2611.33195v1
- Local PDF: pdf/2026-11-27_14_Verified experience improves materials prediction with large language models.pdf

Materials discovery is an iterative loop: experiments and calculations verify predictions, and each outcome can inform the next. Yet most predictors are specialized single-task models fixed after training. Large language models have recently emerged as predictors across heterogeneous tasks but generally underperform specialized models, and retrieval-augmented variants discard their own outcomes. Benchmarks also score queries in isolation, leaving improvement from outcomes untested. Here we construct MatMemBench, a sequential benchmark of 22 materials tasks that reveals outcomes only after prediction and tests online adaptation, memory retention and cross-task transfer. We present MatRecall, a framework that lets large language models store verified predictions, with evidence, outcome and error, as episodes and recall them without retraining. MatRecall improved median performance by 62% over a memory-free model, exceeded specialized models on 11 tasks, remained useful after feedback stopped and transferred between related tasks. Verified experience could become a reusable resource for self-improving discovery loops.

## 15. Not Every Input Needs Everything: Unifying Expert Gating, Model Cascades, and Agent Orchestration

- Authors: Dat Tat Mai, Hung Tran Quy, Thai Viet Pham, James Jin Kang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-25
- DOI: Unavailable
- Categories: cs.AI, cs.LG, cs.MA
- Relevance: 3.0098611888732463
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.34112v1
- PDF: https://arxiv.org/pdf/2611.34112v1
- Local PDF: pdf/2026-11-27_15_Not Every Input Needs Everything_ Unifying Expert Gating, Model Cascades, and Agent Orchestration.pdf

Executing monolithic neural weights, frontier foundation models, or entire multi-agent workflows uniformly on every input incurs substantial computational, latency, and monetary overhead. Conditional computation mitigates this cost by deciding dynamically which internal experts, model endpoints, or specialized agents to invoke per request. Yet token-level gating in sparse neural architectures, query-level model cascades, and task-level multi-agent coordination have largely progressed in disconnected research silos, obscuring recurring system failures and transferable fixes. In this systematic review, we synthesize 2,289 studies published between 2017 and September 2026 (selected from 13,884 unique records) across 20 methodological families under a unified two-step inspect-then-allocate framework. Discrete hard selection accounts for 70%, 83%, and 91% of token-, query-, and task-scale literature respectively, and computational overhead appears as a top operational bottleneck across every layer. Engineering safeguards remain sharply asymmetric: intra-layer gating prioritizes load balancing while rarely incorporating uncertainty estimation, whereas model selection and agent orchestration rely on confidence thresholds and budget rules while confronting miscalibration and cascading errors. At the same time, publication volume is accelerating fastest in agentic task delegation, where routing mechanisms are least often isolated experimentally and methodological bias risk is highest.

## 16. Few-Shot Adaptation of Vision-Language Models via Agentic Model Editing

- Authors: Yusheng Zhao, Xiao Luo, Zhiping Xiao, Ming Zhang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-25
- DOI: Unavailable
- Categories: cs.AI, cs.LG
- Relevance: 2.94201231745867
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.34036v1
- PDF: https://arxiv.org/pdf/2611.34036v1
- Local PDF: pdf/2026-11-27_16_Few-Shot Adaptation of Vision-Language Models via Agentic Model Editing.pdf

Few-shot adaptation transfers pretrained Vision-Language Models (VLMs) to new domains using a small set of labeled images. Most methods fit prompts, representations, or classifiers within an adaptation procedure specified in advance. Yet the visual distinctions needed for recognition can differ substantially across domains, motivating the question: Can an LLM agent use few-shot examples and model observations to design the adaptation procedure itself? We propose Agentic Model Editing (AME), an agentic framework that jointly designs input transformations, encoder edits, feature computation, and classifier fitting as an executable, domain-customized adaptation program. The agent inspects images, class semantics, model parameters, intermediate representations, and activations to formulate hypotheses about the target task. It implements and tests candidate programs on the support set, with aggregate validation accuracy guiding refinement and selection. Each program fits a complete domain model that is fixed before testing. The agent and its tools are shared across domains, while each domain receives its own adaptation program. Across eleven datasets with CLIP ViT-B/16, AME achieves the highest average accuracies of 81.2% without back-propagation and 81.9% with back-propagation among the compared methods. Further experiments demonstrate applicability across VLM backbones and LLM agents.

## 17. Dynamic Reasoning in Next-Gen Detection and Response: An Empirical Study of LLM Triage, Reinforcement Tuning, and Adversarial Evasion

- Authors: Jeremy Canale
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-24
- DOI: Unavailable
- Categories: cs.AI, cs.CR
- Relevance: 2.933480266266038
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.33470v1
- PDF: https://arxiv.org/pdf/2611.33470v1
- Local PDF: pdf/2026-11-27_17_Dynamic Reasoning in Next-Gen Detection and Response_ An Empirical Study of LLM Triage, Reinforcement Tuning, and Advers.pdf

We present an end-to-end empirical study of dynamic reasoning in next-generation detection and response pipelines, evaluating how static classifiers, graph-based signal fusion, and large language model (LLM) triage agents perform under strict human-analyst attention budgets (Recall at B alerts/day). Across 56 reproducible experiments spanning a multi-layer enterprise-and-cloud simulator and four public datasets (SOREL-20M, BODMAS, LANL, and DARPA Transparent Computing), we test twelve architectural claims governing modern fleet-scale defense. First, we show that fleet growth halves recall at a fixed analyst budget even at negligible compute cost (<$0.0003 per million events), and that rarity-weighted graph risk propagation outperforms GraphSAGE without neural training. Second, evaluating frontier reasoning models (Gemini) and fine-tuned open-weight models (Qwen3-4B) for alert triage reveals that unconstrained LLM auto-closure eliminates 90% of false positives while silently discarding 31-44% of true attack cases. Third, post-training with Group Relative Policy Optimization (GRPO) causes severe reward hacking on unseen attack classes, suppressing up to 86% of novel attacks compared to two-epoch supervised fine-tuning. Finally, against an adaptive adversary generating plausible cover stories in benign telemetry fields, LLM triage evasion rises sharply unless gated by a deterministic policy harness prior to model invocation.

## 18. Sparse Adaptation for In-Context Learning on Data Streams

- Authors: João Neves, Afonso Lourenço, Lizy K. John, Eric P. Xing, João Gama
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-24
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 2.926160133702891
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.33325v1
- PDF: https://arxiv.org/pdf/2611.33325v1
- Local PDF: pdf/2026-11-27_18_Sparse Adaptation for In-Context Learning on Data Streams.pdf

The Internet of Things (IoT) generates massive data streams, making edge computing essential for low-latency applications and 5G networks. Tabular foundation models (TFMs) enable adaptation through in-context examples rather than parameter updates, but evolving streams challenge context relevance and computational efficiency. This work introduces SAIL, a framework for sparse adaptation of TFMs that reuses the model's key--value cache between adaptation events. SAIL reconstructs its support set only when drifts in stream structure indicate potential context inadequacy, while the structural representation itself is updated by changes in predictive performance. SAIL combines prequential error monitoring with online, class-specific micro-clustering to detect changes in cluster mass, class separability, and feature-space coverage. Upon adaptation, a context budget is allocated proportionally to class mass, and the most recently updated micro-clusters provide representative observations for refitting. This limits context redundancy and computational cost while preserving recent structural information.

## 19. Cell-Type-Specific Expression Is Hard to Predict from Bulk, but It Is Still Useful

- Authors: Gadi Naveh, Amit Miller, Gal Keinan
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-25
- DOI: Unavailable
- Categories: cs.LG, q-bio.QM, stat.ML
- Relevance: 2.865720958623486
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.34166v1
- PDF: https://arxiv.org/pdf/2611.34166v1
- Local PDF: pdf/2026-11-27_19_Cell-Type-Specific Expression Is Hard to Predict from Bulk, but It Is Still Useful.pdf

Single-cell-informed deconvolution provides cell-type-resolved features for clinical bulk RNA cohorts. Most existing methods predict the proportions $π_k$ of the $K$ constituent cell types (CTs). Fewer predict cell-type-specific expression (CTSE) $μ_{kg}$ of gene $g$ in CT $k$, which can capture cell states that proportions miss, but recent benchmarks find it much harder. We explain this gap with closed-form accuracy bounds. For CTSE, we derive an $R^2$ ceiling for per-gene linear estimators. For proportions, the best linear estimator, which pools evidence across genes, has a closed-form $R^2$, and a computable lower bound on it predicts which CTs are learnable. We study targeted deconvolution of 106 biologically curated (CT, gene) pairs, found post hoc to have higher learnability scores. On overall survival in non-small cell lung cancer, estimation difficulty does not predict prognostic value across these targets. Yet a sparse survival model on deconvolved features, mostly CTSE, predicts survival as well as a sparse model on the bulk genes themselves, while attributing its signal to specific cell types. Some deconvolved CTSE features reveal prognostic signal not seen in the corresponding bulk gene.

## 20. Teaching Students to Stand on Their Own: Distilling Vision Foundation Models for Fine-Grained Few-Shot Class-Incremental Learning

- Authors: Junsu Kim, Seungryul Baek
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-25
- DOI: Unavailable
- Categories: cs.CV, cs.AI
- Relevance: 2.864232994777031
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.33749v1
- PDF: https://arxiv.org/pdf/2611.33749v1
- Local PDF: pdf/2026-11-27_20_Teaching Students to Stand on Their Own_ Distilling Vision Foundation Models for Fine-Grained Few-Shot Class-Incremental.pdf

Fine-grained few-shot class-incremental learning (FG-FSCIL) aims to incrementally learn visually similar new classes from limited images without catastrophic forgetting. Prior work typically learns strong representations on base classes or leverages vision foundation models (VFMs) directly as backbones or via knowledge distillation. However, VFM backbones incur high computational costs and do not guarantee fine-grained recognition. Although knowledge distillation reduces inference cost, our preliminary experiments reveal that distilled students still lag substantially behind their VFM teachers, particularly on new classes. To address this limitation, we propose STAND, a systematic VFM-to-student distillation design tailored for FG-FSCIL. Specifically, STAND connects the teacher and student by equipping the student with a fixed copy of the teacher's classifier, aligning their outputs via projectors, and feeding both models composite images that combine different training images. On these composite images, relation distillation matches how the teacher and the student relate each image to other images, while difference distillation matches how this relation changes between two composite images. Finally, we freeze the student and classify new classes using length-calibrated prototypes, which restore the reduced similarity of few-shot prototypes. Extensive evaluations demonstrate that STAND achieves state-of-the-art performance across FG-FSCIL datasets at low computational cost, while generalizing across student backbones and broader datasets.

## 21. Lost in the Grid: Where Multimodal LLMs Fail Between Seeing and Planning

- Authors: Luoxi Zhang, Tianyi Tan, Jiawei Liu, Xingyu Zeng, Min Yang, Shiwen Ni
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-25
- DOI: Unavailable
- Categories: cs.CV, cs.AI
- Relevance: 2.8560196487471528
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.34152v1
- PDF: https://arxiv.org/pdf/2611.34152v1
- Local PDF: pdf/2026-11-27_21_Lost in the Grid_ Where Multimodal LLMs Fail Between Seeing and Planning.pdf

Multimodal large language models (MLLMs) excel at static visual understanding and are increasingly applied to spatial planning, where a model interprets a visual layout and outputs an action sequence to reach a goal. Grid games are a common testbed for this ability because their rules are explicit and a solver can verify every move. Yet existing benchmarks mostly report end-to-end success rates, which hide whether a failure stems from visual perception, rule application, or multi-step planning. We introduce GridProbe, a diagnostic benchmark that 1) locates the failing stage between visual perception and planning and 2) verifies the diagnosis by targeted fine-tuning. On Sokoban, GridProbe pairs end-to-end solving with four probes (recognition, localization, single-step prediction, and state tracking) and gives every board both as an image and as an equivalent text grid. Evaluating seven MLLMs on Sokoban and a maze game reveals distinct bottlenecks behind similar success rates: proprietary models are limited by multi-step planning, whereas open-source models are limited by rule application or by visual grid indexing, i.e., counting rows and columns. Planning failures also hide perception failures: when planning is easier, the visual cost of the same model grows from 7.6 to 37.7 points. The diagnosis identifies what to train: fine-tuning only the vision module of the perception-limited model on board reading raises its interactive Sokoban success 3.5-fold (5.8% to 20.4%) and transfers zero-shot to the unseen maze game (single-turn success 13.8% to 67.1%), whereas the same data does not help a rule-limited model and training on solver solutions brings no gain. We will release the benchmark and code at https://github.com/suat-llm/GridProbe.

## 22. MolGPAO: Molecular Generative Pre-trained Autoregressive Octree with Speculative Decoding and Sub-Millisecond Seam Healing for 3D Molecules

- Authors: Shangqian Chen, Guojiang Zhao, Zheng Cheng, Jiankun Wang, Hongshuai Wang, Zhifeng Gao
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-25
- DOI: Unavailable
- Categories: cs.LG, cs.AI, q-bio.BM
- Relevance: 2.842636780924904
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.33985v1
- PDF: https://arxiv.org/pdf/2611.33985v1
- Local PDF: pdf/2026-11-27_22_MolGPAO_ Molecular Generative Pre-trained Autoregressive Octree with Speculative Decoding and Sub-Millisecond Seam Heali.pdf

Autoregressive generation over adaptive 3D octrees (Uni-3DAR) offers an intrinsic $O(N \log N)$ sparsity advantage over dense $O(N^2)$ equivariant diffusion and flow models on large drug-like molecules, yet lags in geometric equilibrium, closed-shell valence stability, and property fidelity due to Morton-seam coordinate jumps, leaf-heavy compute with root-count trapping, and target-shortcut collapse in internal critics. We introduce MolGPAO (Molecular Generative Pre-trained Autoregressive Octree), a standalone 3D octree architecture and single-output speculative tree-decoding engine using zero external surrogates, zero reinforcement learning, and zero inference-time MLIP relaxation. MolGPAO unifies: (1) non-trapping 6-D ScaleFreeBudgetEmbedding with L5-to-L1 covalent packing priors; (2) a FlashAttention-2 pause-and-gather speculative octree funnel ($m_{s1} \to m_{s2} \to 1$, $M_{\mathrm{out}} = 1$); (3) an anti-shortcut ground-truth TwoStageOctreeProcessCritic with 64-RBF covalent edge gating and $SO(3)$-invariant 12-channel multipole norms (blind QM9 $r = 0.9867$--$0.9989$); (4) a $<0.5$ ms 4-layer $SE(3)$ PostTreeGraphRefiner for Morton-seam healing, expected-XYZ bonded supervision, selective CFG, and zero-heavy-displacement valence reconciliation; and (5) bubble-free stride-2 GPU leaf decoding. Across GEOM-Drugs (0.49 GPU-h), disjoint 50k/50k QM9 (0.43 GPU-h), and PBE0/def2-TZVP-verified OE62 (0.56 GPU-h), MolGPAO lifts drug-scale valid-connected yield 6.78x (12.7% to 86.2%, 99.83% atom stability), runs 7.3x faster (or 1.65x faster at 2.0x yield) than 100-step FlowMol at $N=100$, beats 156 GPU-h PropMolFlow on QM9 HOMO (-12.7%) and dipole (-21.0%) at 362x lower compute, and doubles live DFT hit rate on OE62 (33.3% vs. 16.7%) at 92.8x lower compute.

## 23. Motion Beyond Pixels: Learning Future Visual Representations for Object-Centric Dynamics

- Authors: Chengzhi Zhao, Juelin Li, Zhennan Wang, Sheng Wang, Zhuoman Liu, Yuhao Lu, Jiongxu Chen, Haitang Feng, Yanjie Li, Lin Shao
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-25
- DOI: Unavailable
- Categories: cs.CV, cs.AI, cs.RO
- Relevance: 2.8398260346146365
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.34644v1
- PDF: https://arxiv.org/pdf/2611.34644v1
- Local PDF: pdf/2026-11-27_23_Motion Beyond Pixels_ Learning Future Visual Representations for Object-Centric Dynamics.pdf

Many embodied world models predict future states in latent spaces optimized for RGB reconstruction, which do not explicitly prioritize object-level semantics and geometry relevant to motion generation. We present MotionRep, a visual representation world model that jointly generates future DINO representations and 3D object flow, coupling semantic and geometric information with object-centric dynamics. To make high-dimensional DINO features amenable to generative modeling, we introduce DINO-VAE, which combines temporal and channel compression with latent regularization to produce compact latents while preserving semantic and geometric information. Conditioned on an initial observation, object query points, and a language instruction, a unified diffusion transformer predicts future visual representations and 3D object flow through joint attention. MotionRep employs asymmetric modality-specific noise schedules to keep the visual stream ahead of 3D object flow during joint denoising, allowing progressively refined future visual representations to guide flow generation. Experiments on simulated and real-world manipulation benchmarks demonstrate that MotionRep outperforms pixel-based baselines in 3D object flow accuracy and generalization to unseen scenes, while requiring only three denoising steps for inference. These results support predictive visual representations as an effective future-state space for object-centric dynamics modeling.

## 24. EraseAnything++: Enabling Concept Erasure in Rectified Flow Transformers Leveraging Multi-Object Optimization

- Authors: Zhaoxin Fan, Nanxiang Jiang, Daiheng Gao, Shiji Zhou, Wenjun Wu
- Source: openalex
- Venue type: journal
- Journal: IEEE Transactions on Pattern Analysis and Machine Intelligence
- Publication status: published
- Publication date: 2026-11-24
- DOI: https://doi.org/10.1109/tpami.2026.3757200
- Categories: Generative Adversarial Networks and Image Synthesis, Adversarial Robustness in Machine Learning, Digital Media Forensic Detection
- Relevance: 2.82446884643785
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://doi.org/10.1109/tpami.2026.3757200
- PDF: Unavailable
- Local PDF: Not downloaded

Removing undesired concepts from large-scale text-to-image (T2I) and text-to-video (T2V) diffusion models-while preserving overall generative quality-remains a major challenge, particularly as modern models such as Stable Diffusion v3, Flux, and OpenSora employ flow-matching and transformer-based architectures, as well as extending to long-horizon video generation. Existing concept erasure methods, designed for earlier T2I/T2V models, often fail to generalize to these paradigms. To address this, we propose EraseAnything++, a unified framework for concept erasure in both image and video diffusion models with flow-matching objectives. Central to our approach is formulating concept erasure as a constrained multi-objective optimization problem, explicitly balancing concept removal with the preservation of generative utility. To solve such problem with conflicting objectives, we introduce an efficient utility-preserving unlearning strategy based on implicit gradient surgery. Furthermore, by integrating LoRA-based parameter tuning with attention-level regularization, our method anchors erasure on key visual representations and propagates it consistently across spatial and temporal dimensions. In the video setting, we further enhance consistency through an anchor-and-propagate mechanism, which initializes erasure on reference frames and enforces it throughout subsequent transformer layers, thereby mitigating temporal drift. Extensive experiments on both image and video benchmarks demonstrate that EraseAnything++ substantially outperforms prior methods in erasure effectiveness, generative fidelity, and temporal consistency, establishing a new state of the art for concept erasure in next-generation diffusion models.

## 25. Semantic Density Does Not Predict Agent-Memory Collapse

- Authors: Saksham Gupta, Yash Choudhary, Arpit Upadhyay
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-28
- DOI: Unavailable
- Categories: cs.LG, cs.AI, cs.CL
- Relevance: 2.8239775743221776
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.33184v1
- PDF: https://arxiv.org/pdf/2611.33184v1
- Local PDF: pdf/2026-11-27_25_Semantic Density Does Not Predict Agent-Memory Collapse.pdf

Persistent textual memory can improve LLM agents, but repeated updates can erode task performance. We ask whether memory-store statistics warn before held-out accuracy declines. We registered mean pairwise cosine similarity ($ρ$) and 13 additional geometry, retrieval, and graph statistics on 805 snapshots from 13 memory methods across ALFWorld, AppWorld, ScienceWorld, WebShop, and two ARC-AGI settings. These methods store trajectories, rules, workflows, strategies, or linked records, using selective retrieval or whole-store prompting. No such statistic reliably predicted early signs of task accuracy decline, and $ρ$ had zero median lead. With the checkpoint after peak accuracy as a secondary decline point, measures of highly similar pairs and nearest-neighbor crowding changed earlier but did not consistently outperform stored-item count. We trained classifiers on this corpus and applied them unchanged to PropWorld runs of up to 5,000 crafting tasks. They falsely flagged 56.9% of checkpoints from size-limited stores with stable accuracy and detected only 18% of checkpoints after task success fell to zero. Thus, global semantic density did not provide a reliable warning, while local crowding did not transfer consistently across memory designs. In these long-horizon runs, size-limited stores remained stable, while the sole failure arose when unbounded whole-store prompting exceeded model input capacity, which token growth predicted directly.

## 26. CypherMAS: Benchmarking Routing Reliability in LLM-Based Multi-Agent Systems

- Authors: Danil Kostromin, Andrey Sakhovskiy, Semen Budennyy
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-24
- DOI: Unavailable
- Categories: cs.MA, cs.AI, cs.CL
- Relevance: 2.810404387585939
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.33242v1
- PDF: https://arxiv.org/pdf/2611.33242v1
- Local PDF: pdf/2026-11-27_26_CypherMAS_ Benchmarking Routing Reliability in LLM-Based Multi-Agent Systems.pdf

Multi-agent systems (MAS) built on large language models (LLMs) distribute reasoning across specialized agents that must exchange messages and invoke tools reliably. Existing evaluations typically couple communication with open domain tasks, making it difficult to determine whether a failure arises from reasoning, malformed tool use, lost messages, or forgotten requests. Prior benchmarks do not isolate communication execution or measure routing redundancy against a known optimal path. We introduce CypherMAS, a synthetic benchmark that isolates communication and routing in fixed multi-agent graphs. Agents in chain, star, bipartite, or ring graphs route cyphered messages to remote peers holding the matching decoders; since the optimal route is known, redundant LLM calls can be measured and routing failures may be easily tracked. Across eleven open-weight models from 4B to 753B, small models fail at routing and tool use, dense models above 27B degrade with diameter, and successful runs exceed minimum LLM calls. These findings identify communication reliability as a distinct scaling bottleneck for multi-agent systems and provide a controlled diagnostic for complex multi-agent systems. The source code is freely available: https://github.com/Andoree/CypherMAS.

## 27. Kolpona: An Agentic Framework with Gradient-Free Neuron Programming for RTL Generation

- Authors: Musa Tur Farazi, Md Nasir Uddin, Soumik Bhattacharjee, Tishna Sabrina, Chowdhury Mohammad Rakin Haider
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-25
- DOI: Unavailable
- Categories: cs.LG, cs.AI, cs.AR
- Relevance: 2.782511691088322
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.33973v1
- PDF: https://arxiv.org/pdf/2611.33973v1
- Local PDF: pdf/2026-11-27_27_Kolpona_ An Agentic Framework with Gradient-Free Neuron Programming for RTL Generation.pdf

Open-weight large language models (LLMs) for register-transfer level (RTL) design are usually improved by fine-tuning on curated Verilog corpora, which needs large sets of verified designs and GPU training. We present Kolpona, an agentic framework that improves such models without gradient training. Its first component is neuron programming, a new form of weight-space programming (WSP) that writes single neurons in closed form into the weights to remove failure habits found on practice tasks, and keeps each edit only when testbench results on fresh tasks favour it. At inference time, tool-using agents propose designs, and a label-free selection stage delivers one design per task from the specification, the candidates and their simulations alone. On Qwen3.5-4B, edits to 16 neurons raise the VerilogEval v2 pass@1 of the model alone from 31.7% to 55.4%, and the full framework reaches 77.6%. On Qwen3.8-27B, Kolpona lifts pass@1 from 73.1% to 94.9% on VerilogEval v2 and from 66.0% to 92.0% on RTLLM v2.1 on a single 32 GB GPU, above every published system in our comparison. The RTL edits also carry over to Python and raise the pass@1 of the 4B model alone from 84.8% to 91.5% on HumanEval+ and from 67.7% to 77.5% on MBPP+.

## 28. Federated Learning with Uncertainty Quantification on Pseudo Label Exchange

- Authors: Jingqiao Tang, Phuoc-Toan Huynh, Richard Archibald, Feng Bao
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-24
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 2.777488591377014
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.33395v1
- PDF: https://arxiv.org/pdf/2611.33395v1
- Local PDF: pdf/2026-11-27_28_Federated Learning with Uncertainty Quantification on Pseudo Label Exchange.pdf

In this work, we investigate federated stochastic operator learning for stochastic partial differential equations (SPDEs), with an emphasis on heterogeneous client data distributions and uncertainty quantification. Federated learning enables clients to collaboratively train models without exchanging their original solution data, but conventional federated averaging can suffer significant performance degradation when client distributions differ, particularly when their input function supports are disjoint. To address these challenges, we propose the Federated Stochastic Operator Network (FedSON), a two-phase framework that combines auxiliary data construction with stochastic operator learning. In the first phase, locally trained deterministic neural operators and their corresponding input functions are exchanged to generate pseudolabeled auxiliary data, enabling the federated model to learn across heterogeneous input distributions without sharing original solution trajectories. In the second phase, a stochastic operator network is trained on top of the frozen deterministic operator to characterize stochastic fluctuations and quantify uncertainty in the predicted solutions. Numerical experiments involving the heat equation, viscous Burgers' equation, and two-dimensional advection-diffusion equation demonstrate the FedSON substantially improves deterministic prediction accuracy under heterogeneous client distributions while producing uncertainty estimates comparable to those obtained through centralized training.

## 29. How Many Samples Is RL Worth? Best-of-N versus RL Post-Training for Text-to-Image Models

- Authors: Salil Bhatnagar
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-24
- DOI: Unavailable
- Categories: cs.CV, cs.AI, cs.LG
- Relevance: 2.7766027827486854
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.33232v1
- PDF: https://arxiv.org/pdf/2611.33232v1
- Local PDF: pdf/2026-11-27_29_How Many Samples Is RL Worth_ Best-of-N versus RL Post-Training for Text-to-Image Models.pdf

Reinforcement learning (RL) on a reward that can be checked automatically has become a common last step in the training of text-to-image models. A simpler way to get more correct images is best-of-N: draw N images from the base model and keep the one that a picker prefers. We ask how many base model samples one RL sample is worth, and call this number the exchange rate. We measure it for Stable Diffusion 3.5 Medium and its public Flow-GRPO checkpoint on 398 new prompts in the style of GenEval, the benchmark behind the RL reward, with human labels on every prompt and two automatic judges other than the reward. The answer depends on the prompt. Four fifths of the prompts do not ask for a position (for example, one object left of another). On these, the base model catches up: best-of-16 with an off-the-shelf vision-language model (VLM) as the picker is about as good as one RL image. A person who looks through up to 3 base images finds a correct one as often as one RL image is correct. On the prompts that ask for a position, RL is far ahead: a person finds a correct image among 8 base images for only 52% of the prompts, against 92% for one RL image. Over all prompts, our primary test, which we fixed in advance, finds best-of-16 with the VLM picker 9.3 points behind one RL image when both automatic judges must pass an image. People see a smaller gap, 5.5 and 6.5 points in two checks. FLUX.1-dev shows a similar gap in the same test. RL also solves 20 prompts that the base model misses in 128 tries, and 1,024 tries recover half of them. The automatic judges are wrong in opposite directions: a detector-based judge like the reward, as used in our primary test, reports a larger gap than people see, and VLM judges report little or none. Comparisons of RL with best-of-N should therefore check the selected images by hand.

## 30. WebVibe: Multimodal Interactive Website Generation via Reverse Synthesis and Visual Self-Distillation

- Authors: Tianxiang Jiang, Sheng Xia, Yilin Long, Kanghui Tian, Linquan Wu, Yongheng Zhang, Daixian Liu, Di Yin, Yi Wang, Yu Qiao, Qinglong Zhang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-25
- DOI: Unavailable
- Categories: cs.CV, cs.AI
- Relevance: 2.740757574266336
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.34292v1
- PDF: https://arxiv.org/pdf/2611.34292v1
- Local PDF: pdf/2026-11-27_30_WebVibe_ Multimodal Interactive Website Generation via Reverse Synthesis and Visual Self-Distillation.pdf

Although multimodal large language models translate single screenshots into static HTML, generating interactive functional websites from design specifications still struggles with multi-page routing and stateful widget transitions. Examining existing training pipelines reveals two bottlenecks: (1) in forward data synthesis (X -> Y), writing the specification X before code execution leaves unimplemented or altered requirements in X as supervision noise; and (2) in reinforcement learning, scalar rewards discard the rich state transitions observed during replay. Based on these findings, we introduce WebVibe and Interactive-SDPO to train InteractiveCoder. WebVibe reverses synthesis into Y -> X by verifying cross-page and in-page interactions in the browser before deriving multimodal inputs from replay-confirmed states to build the 31,542-site WebVibe-32K corpus with reusable execution contracts. Interactive-SDPO then conditions a weight-sharing self-teacher on the replay trace and a 2x2 state-transition montage to provide token-level supervision at zero inference-time overhead. On the public Vision2Web L2, one-shot InteractiveCoder-9B nearly 3x its base model's functional score (20.2 to 55.2 FS) and matches a 1T-parameter coding agent in a single pass with 111x fewer total parameters and 78x fewer tokens. On our WebVibeBench, InteractiveCoder-4B and 9B further outperform all evaluated baselines by over 23 points.
