# Paper Daily Reading - 2026-11-21

## 1. FG-GraphBench: Benchmarking and Enhancing Fine-Grained Visual Understanding with Multimodal Scene Graphs

- Authors: Sicheng Liu, Xunkai Li, Ziyu Han, Xingnan Zhang, Ru Zhang, Rong-Hua Li
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-19
- DOI: Unavailable
- Categories: cs.LG, cs.AI, cs.CV
- Relevance: 3.7097543323467495
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.25408v1
- PDF: https://arxiv.org/pdf/2611.25408v1
- Local PDF: pdf/2026-11-21_01_FG-GraphBench_ Benchmarking and Enhancing Fine-Grained Visual Understanding with Multimodal Scene Graphs.pdf

Fine-grained visual understanding requires multimodal large language models (MLLMs) to recognize small visual entities and understand their relationships. Scene graphs offer a natural way to represent this information, organizing visual entities as nodes and their relationships as edges. However, we identify two challenges: existing scene graph benchmarks provide insufficient coverage of fine-grained entities and the relationships among them, and existing methods for fine-grained visual understanding have yet to effectively leverage such graph-structured information in MLLMs. To address these challenges, we introduce Fine-Grained Multimodal Scene Graph Benchmark (FG-GraphBench) and FiGRA. FG-GraphBench is a benchmark comprising three complementary tasks: fine-grained visual question answering (FG-QA), image captioning (FG-Caption), and image description generation (FG-Description). We develop a two-stage construction pipeline that discovers and grounds fine-grained entities and establishes their relations to construct the fine-grained multimodal scene graphs (MSGs) in FG-GraphBench. Building on these MSGs, we propose FiGRA, a Fine-grained Graph Representation Augmentation method for MLLMs. FiGRA adopts a two-stage training strategy. It encodes multimodal entity and relation features as continuous graph tokens, and integrates them into the MLLM. Experiments show that FiGRA significantly outperforms strong baselines across three tasks of FG-GraphBench. Further analyses confirm the effectiveness of FG-GraphBench and highlight the importance of preserving fine-grained entity and relation information for visual understanding.

## 2. Adding layers of information to scRNA-seq data using pre-trained language models

- Authors: Sonia Maria Krissmer, Jasper Menger, Johan Rollin, Tanja Vogel, Harald Binder, Maren Hackenberg
- Source: openalex
- Venue type: journal
- Journal: Genome biology
- Publication status: published
- Publication date: 2026-11-19
- DOI: https://doi.org/10.1186/s13059-026-04353-y
- Categories: Single-cell and spatial transcriptomics, Bioinformatics and Genomic Networks, Biomedical Text Mining and Ontologies
- Relevance: 3.462331489420503
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://doi.org/10.1186/s13059-026-04353-y
- PDF: Unavailable
- Local PDF: Not downloaded

Pre-trained language models promise to enrich single-cell analyses with contextual information from large biomedical text corpora, but it remains unclear how to optimally align this knowledge with quantitative single-cell RNA sequencing (scRNA-seq) data. To address this, we construct text-based training datasets from both scRNA-seq data and biomedical literature targeted to the experimental setting at hand. We then fine-tune lightweight encoder-only biomedical language models to learn a shared, literature-enriched representation. Controlled evaluations across immune and developmental datasets show that this representation preserves cell identity while adding robust and interpretable contextual layers of functional, disease-associated, and developmental information to single-cell analysis workflows.

## 3. Learning from Context: Leave-One-Out Prediction in Jump Diffusions

- Authors: Christian Wald
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-19
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.3268250749960124
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.26359v1
- PDF: https://arxiv.org/pdf/2611.26359v1
- Local PDF: pdf/2026-11-21_03_Learning from Context_ Leave-One-Out Prediction in Jump Diffusions.pdf

Continuous diffusion models generate discrete data through stochastic dynamics in an embedding space. We consider jump diffusions that additionally reset coordinates to embeddings of categorical values. A coordinate's own corrupted state can make prediction easy, potentially reducing the pressure to learn dependencies between coordinates. We study leave-one-out (LOO) prediction, in which each coordinate is predicted from the corrupted states of the other coordinates. We show that, under stated assumptions, jump diffusions with complete coordinate resets and state-independent clocks preserve the prescribed marginals when reset destinations use exact LOO probabilities and the drift uses the full endpoint posterior. We further show that this drift can be constructed from LOO probabilities by analytic likelihood completion without additional network evaluations. We evaluate unrestricted, LOO, and completed predictions on Text8 and LM1B text generation and ZINC250k molecular graph generation. LOO-based variants improve key generation metrics over matched unrestricted controls on all three datasets. Controlled interventions assess reliance on local inputs and context, and we analyze the effect of analytic likelihood completion.

## 4. From Sequence Uncertainty to Phenotype Hypotheses: Uncertainty-Conditioned Inference over Biomedical Knowledge Graphs

- Authors: Huixin Zhan, Jason H. Moore
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-19
- DOI: Unavailable
- Categories: cs.LG, q-bio.GN
- Relevance: 3.293426026530451
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.25422v1
- PDF: https://arxiv.org/pdf/2611.25422v1
- Local PDF: pdf/2026-11-21_04_From Sequence Uncertainty to Phenotype Hypotheses_ Uncertainty-Conditioned Inference over Biomedical Knowledge Graphs.pdf

Genomic foundation models provide variant-level evidence, but connecting that evidence to phenotype hypotheses requires accounting for uncertainty throughout structured reasoning. We introduce an uncertainty-conditioned path-energy framework that converts sequence predictions and calibrated predictive uncertainty into explicit distributions over graph-supported phenotype hypotheses, without patient-level phenotype supervision. An interpretable learned energy scores admissible gene--disease--phenotype routes, query uncertainty controls the target temperature, and path probabilities are aggregated into phenotype hypotheses. This formulation makes evidence quality an explicit determinant of hypothesis breadth while retaining traceable multi-path support. Exact normalization over enumerable candidate sets provides a reference for evaluating a Hastings-corrected learned revision operator. On AlzKB and Hetionet, phenotype-level entropy tracks upstream uncertainty, with Spearman correlations of 0.951 and 0.878, respectively; ablations identify the contribution of uncertainty conditioning. In masked-edge recovery, the model exceeds chance and degree-matched probability-permutation controls. Training the energy under the uncertainty-dependent temperature yields higher held-out recall@10 than training under a constant temperature of comparable magnitude. Under gene hold-out, recall@10 exceeds that of a trained DistMult embedding on 24 of 30 graph masks (0.183 versus 0.123); this difference is attributable mainly to three genes with many variants and is not established for all genes. These results establish an uncertainty-aware interface from genomic predictions to graph-supported phenotype hypotheses that combines interpretable probability allocation with held-out association recovery of explicitly stated scope.

## 5. Space-map: 3D single-cell atlas reconstruction from serial sections

- Authors: Rongduo Han, Cihan Ruan, Bingqing Zhao, Yuqi Tan, Emma Monte, Bei Wei, Joanna Bi, Thomas V. Karathanos, Rozelle Laquindanum, Gregory W. Charville, Yiing Lin, Nam Ling, James M. Ford, Garry P. Nolan, Meng Wang, Chenchen Zhu, Michael P. Snyder
- Source: openalex
- Venue type: journal
- Journal: Nature Methods
- Publication status: published
- Publication date: 2026-11-19
- DOI: https://doi.org/10.1038/s41592-026-03310-8
- Categories: Single-cell and spatial transcriptomics, Cell Image Analysis Techniques, Medical Image Segmentation Techniques
- Relevance: 3.291167551192778
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://doi.org/10.1038/s41592-026-03310-8
- PDF: Unavailable
- Local PDF: Not downloaded

High-resolution three-dimensional (3D) tissue atlases promise to link cellular architecture to tissue function, but assembling them from serial sections containing millions of cells remains challenging. Here we present Space-map, an accurate and efficient method for reconstructing 3D tissue models from high-content spatial molecular profiles. Space-map combines multiscale feature matching with large deformation diffeomorphic metric mapping to automate global alignment across serial sections while preserving local microanatomy. We generate spatial transcriptomics (Xenium; ~2.7 million cells) and proteomics (CODEX; ~4.8 million cells) datasets from serial sections to build 3D models of a colon polyp and healthy intestinal tissues. These models reveal cell-type heterogeneity in the polyp and preserved crypt and glandular architecture and mucosal-cavity continuity in healthy intestines. Benchmarking on our own and publicly available datasets demonstrates that Space-map achieves substantially higher registration accuracy and up to a tenfold speedup over existing methods, supporting its use as a robust framework for constructing 3D human tissue atlases at single-cell resolution.

## 6. C-LiTE: A Lightweight Foundation Model for Cellular feature learning in Histopathology

- Authors: Esha Sadia Nasir, Jiaqi Lv, Gozde N. Gunesli, Shan E Ahmed Raza
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-19
- DOI: Unavailable
- Categories: cs.CV, cs.AI
- Relevance: 3.258553078984741
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.26316v1
- PDF: https://arxiv.org/pdf/2611.26316v1
- Local PDF: pdf/2026-11-21_06_C-LiTE_ A Lightweight Foundation Model for Cellular feature learning in Histopathology.pdf

Characterising individual cells is fundamental to computational pathology, as cellular morphology informs tasks such as tumour grading, mitotic assessment and immune profiling. However, most pathology foundation models are trained on tissue patches and capture cellular features only implicitly, while existing cell-level models are either restricted to specific cell populations or rely on computationally expensive architectures with hundreds of millions of parameters. Applying ViTs directly to small cellular crops also presents an architectural challenge: upsampling increases computational cost without adding morphological information and may introduce interpolation artefacts. To address these limitations, we introduce C-LiTE, a lightweight foundation model for cellular representation learning in H&E-stained histopathology, with only 22 million parameters. C-LiTE employs a native-resolution tokenisation strategy tailored to cellular inputs, processing 64 x 64 px cell-centred crops using a 4 x 4 patch embedding to produce a 16 x 16 token grid without image upsampling. To transfer visual knowledge from large-scale pre-training, we adapt the patch embedding weights of a pre-trained ViT-5-S using a pseudoinverse-based transformation, enabling weight initialisation at the finer patch resolution. We further assemble a pre-training dataset of 60 million cell-centred crops from TCGA, balanced across 19 cancer types and 16 tissue types. To our knowledge, this represents the largest public dataset for self-supervised pre-training on H&E images at the cellular level. We evaluate C-LiTE on seven public datasets spanning mitotic figure recognition, nucleus and cell-type classification, and immune cell phenotyping. Under frozen-feature evaluation, C-LiTE achieves a mean macro-F1 of 0.670, approaching CytoFormer (0.682) with approximately 30x fewer parameters.

## 7. HiUni: Harmonizing Understanding and Generation in Shared Visual Space

- Authors: Jiahao Hu, Jingdong Du, Yichen Zhang, Yi Song, Zhenyu Zhang, Jiaxin Niu, Ruihang Li, Xiangzhao Hao, Yiqian Zhang, Yong Huang, Zefeng Zhang, Zheyuan Gu, Shuohuan Wang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-19
- DOI: Unavailable
- Categories: cs.CV, cs.AI
- Relevance: 3.2249173992316416
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.26107v1
- PDF: https://arxiv.org/pdf/2611.26107v1
- Local PDF: pdf/2026-11-21_07_HiUni_ Harmonizing Understanding and Generation in Shared Visual Space.pdf

Unified multimodal models aim to support visual understanding and generation within a single framework. However, prevailing approaches often separate their visual representations or backbone computation to accommodate the different requirements of these two tasks, which limits the degree of unification. In this paper, we present HiUni, which revisits this design choice and explores whether a pretrained vision language model can be directly extended into a unified model with extensive parameter sharing. Specifically, HiUni reuses the same language-aligned ViT and dense Transformer backbone for both capabilities, while confining task-specific computation to the output side. Yet such a design introduces two key challenges. Generation in pixel space is difficult to optimize, and semantic abstraction in pretrained ViT discards fine spatial details required for synthesis. To address these challenges, HiUni introduces a \emph{Pixel Diffusion Head} tailored to direct pixel-space optimization and a lightweight \emph{HiGate} pathway that provides fine-grained spatial details near the output stage. Extensive experiments show that HiUni achieves a similar average understanding score to the pretrained VLM while attaining competitive performance on image generation and editing. Controlled comparisons and analyses further demonstrate that a single dense backbone can effectively support both capabilities without task-specific backbone computation, highlighting a simpler path toward unified multimodal modeling.

## 8. VoxForge: A Unified Foundation Model for Dense 3D Features Across MRI, CT and PET

- Authors: Rushil Anirudh, Jayaraman J. Thiagarajan
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-19
- DOI: Unavailable
- Categories: cs.CV, cs.LG
- Relevance: 3.220185692353078
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.25309v1
- PDF: https://arxiv.org/pdf/2611.25309v1
- Local PDF: pdf/2026-11-21_08_VoxForge_ A Unified Foundation Model for Dense 3D Features Across MRI, CT and PET.pdf

A unified 3D medical foundation model promises reusable, frozen features that serve a wide variety of tasks such as segmentation, classification and registration on MRI, CT and PET as well as specialist models do. Generalist models still need separate backbones for localized and global tasks, specialist models are confined to a single modality, with the concern that spanning modalities under-emphasizes fine anatomy, and both typically rely on end-to-end fine-tuning to be competitive. We present VoxForge, a single encoder that integrates recent advances in 3D architecture, self-distillation and cross-modal curricula to learn transferable features from permissively licensed MRI and CT volumes. We evaluate it strictly frozen, the test a reusable foundation model must pass, against state-of-the-art generalist and specialist models on segmentation, classification and registration across MRI and CT, and on PET, which it never sees. VoxForge has the best or tied-best average rank in every task group, serves localized and global tasks across modalities at the level of state-of-the-art specialists, and is extremely label-efficient, matching top-performing models on TotalSegmentator CT with a tenth of the labels.

## 9. SPiCe: integrative spatial modelling of cellular plasticity using graph neural networks and geostatistics

- Authors: Eloise Withnell, Cenk Celik, Maria Secrier
- Source: openalex
- Venue type: journal
- Journal: Genome biology
- Publication status: published
- Publication date: 2026-11-19
- DOI: https://doi.org/10.1186/s13059-026-04350-1
- Categories: Single-cell and spatial transcriptomics, Gene expression and cancer classification, Gene Regulatory Network Analysis
- Relevance: 3.195288283156566
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://doi.org/10.1186/s13059-026-04350-1
- PDF: Unavailable
- Local PDF: Not downloaded

Cellular plasticity, the ability of cells to change phenotype in response to intrinsic and environmental cues, is central to development and disease, yet remains difficult to quantify. We present SPiCe, a framework that integrates graph neural networks and spatial regression models to predict and explain cell state variation in spatial transcriptomics data. Applied to epithelial-mesenchymal plasticity (EMP) in breast cancer, SPiCe shows that mesenchymal states are stabilised by copy number alterations and microenvironmental cues, whereas hybrid states remain unpredictable, and uncovers long-range myofibroblast influences on EMP. Together, these analyses provide a framework for quantifying cellular plasticity and its spatial determinants.

## 10. STARK: Moving towards Personalized Agents That Truly Learn and Remember

- Authors: Aryan Jain, Abhishek Jha, Anish Nediyanchath, Promod Yenigalla
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-19
- DOI: Unavailable
- Categories: cs.CL, cs.AI, cs.IR
- Relevance: 3.1893669697092095
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.25705v1
- PDF: https://arxiv.org/pdf/2611.25705v1
- Local PDF: pdf/2026-11-21_10_STARK_ Moving towards Personalized Agents That Truly Learn and Remember.pdf

Long-term memory is essential for personalized agentic systems that interact with users over long time periods, yet current architectures only capture what happened while leaving the reasoning of why it happened to be derived later by underlying LLMs.%, and silo knowledge within individual users. These events can, however, convey not only what a user experienced but also how that experience shaped their behavioral patterns. We introduce STARK, a dual-graph memory architecture which treats these events not just as nodes but also as edges between behavioral insights. STARK maintains an Episodic Graph which records interactions as temporally, causally, and semantically linked episodes; and an Insight Graph which represents LLM-extracted behavioral signals scored by how many events support them, connected by the very events that led to them. At inference, behavioral knowledge is retrieved directly from insight nodes grounded by event-as-edges, eliminating repeated episodic traversal. The event-as-edge structure also naturally enables projecting the knowledge graph into a relational embedding space where cross-user transfer becomes possible under shared contextual circumstances, allowing the system to infer missing insights for cold-start users. Evaluations show that STARK improves by 1.48 judge score on LongMemEval information extraction and 0.93 on LoCoMo open domain questions over state of the art. On the public LongLaMP abstract-generation benchmark, cross-user transfer improves open-ended judge scores by 0.7 points and ROUGE-L by 3 at 5% graph sparsity.

## 11. ProtoDiffusion: Token-per-Layer Generative Modeling of Multi-Layer Images

- Authors: Adrià Ciurana Lanau, Harleen Hanspal, Lusine Abrahamyan, Emilio Tylson Baixauli, Yu Cao, Danai Triantafyllidou, Stefano Zorzi, Gustavo Zanoni Felipe, Peter Griger, Stefan Sietzen, Petru-Daniel Tudosiu
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-19
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 3.181093081305221
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.26586v1
- PDF: https://arxiv.org/pdf/2611.26586v1
- Local PDF: pdf/2026-11-21_11_ProtoDiffusion_ Token-per-Layer Generative Modeling of Multi-Layer Images.pdf

Graphic designs are ordered compositions of RGBA layers whose separation enables selection, movement, and reuse. Existing layered models represent each layer with a full-canvas or region-sized spatial latent grid, so representation size grows with the cumulative spatial extent of the layers. We present ProtoDiffusion, a latent-diffusion framework built on ProtoVAE, a multi-layer variational autoencoder that encodes a design into one shared spatial prototype and one candidate vector per layer. Each candidate conditions a shared decoder to reconstruct its corresponding RGBA layer. For $N$ layers, the representation contains $HW+N$ tokens before backbone-specific packing, compared with $NHW$ for full-grid-per-layer representations. ProtoDiffusion jointly denoises the prototype and a fixed set of candidate slots, conditioned on an image or text, with bounding boxes as optional layout guidance. The model leaves unneeded slots empty and determines the number of layers and, in absence of boxes, their layout, requiring neither as input. The same architecture supports both image-to-design and text-to-design. ProtoVAE achieves high-fidelity reconstruction from its compact shared latent representation, reaching 40.43 dB PSNR on layer crops. On the LayerD evaluation split, image-to-design achieves RGB L1 scores of 0.040 with bounding boxes and 0.057 without, with box-guided alpha soft IoU (0.850) comparable to the strongest fine-tuned baseline (0.871). On merged images, text-to-design reaches 66.41 FID versus 86.84 for FLUX.2 [klein], achieves a 0.860 text-accuracy score, and runs $19.1\times$ faster than the same-backbone generation-then-decomposition cascade.

## 12. Beyond Entity Recognition: Vision-Centric Knowledge Visual Question Answering

- Authors: Jiatong Ma, Yuchen Liu, Longteng Guo, Yichen Yuan, Yuze Wu, Dongze Hao, Ru Zhen, Yanhao Zhang, Haonan Lu, Jing Liu
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-19
- DOI: Unavailable
- Categories: cs.CV, cs.AI
- Relevance: 3.121478058279661
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.25680v1
- PDF: https://arxiv.org/pdf/2611.25680v1
- Local PDF: pdf/2026-11-21_12_Beyond Entity Recognition_ Vision-Centric Knowledge Visual Question Answering.pdf

We propose VC-VQA, a large-scale benchmark for vision-centric knowledge reasoning, aiming to systematically evaluate the capabilities of Multimodal Large Language Models (MLLMs) in fine-grained visual knowledge acquisition and complex multi-stage reasoning. Unlike existing benchmarks that primarily treat visual information as entity recognition and rely on text-based external knowledge, VC-VQA explicitly models the role of visual information by considering both its source (internal vs. external images) and stage of involvement (pre-retrieval vs. post-retrieval). Specifically, VC-VQA requires models to retrieve external visual evidence, identify visual clues before retrieval, and localize, verify, or match retrieved knowledge against the internal image. We further construct a controlled multimodal knowledge base with traceable textual and visual evidence for each sample. We evaluate 21 representative MLLMs under four settings: no external knowledge, with provided evidence, knowledge base retrieval, and open-web search. Experimental results lead to three key findings: current models still struggle with vision-centric knowledge reasoning; fine-grained visual knowledge acquisition remains the primary bottleneck; and agentic retrieval highlights the value of multi-step planning and cross-modal knowledge integration. Overall, VC-VQA provides a more challenging benchmark for evaluating vision-centric knowledge reasoning in MLLMs. Our code and dataset are available at https://github.com/CASIA-IVA-Lab/VC-VQA.

## 13. GenSPARQL: A Generative Extension of SPARQL for Incomplete Knowledge Graphs

- Authors: Jingcheng Wu, Yi Wang, Hongkuan Zhou, Steffen Staab, Bo Xiong
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-19
- DOI: Unavailable
- Categories: cs.DB, cs.AI
- Relevance: 3.1167479621659
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.26062v1
- PDF: https://arxiv.org/pdf/2611.26062v1
- Local PDF: pdf/2026-11-21_13_GenSPARQL_ A Generative Extension of SPARQL for Incomplete Knowledge Graphs.pdf

Knowledge graphs on the Web are incomplete, and SPARQL answers a query only from the stored triples. Large language models (LLMs) can predict missing facts, but an LLM returns names instead of IRIs and requires one call per binding of a query variable. We present GenSPARQL, a generative extension of SPARQL 1.1 with an operator GENOP that binds values generated by an LLM to query variables during query evaluation. A similarity join maps generated names to entities of the graph, and the query planner invokes the LLM only for the bindings selected by the other graph patterns and filters. In a web workbench, attendees query two graphs built from Wikidata and inspect generated values, mapped entities and LLM calls. In our evaluation with three open-weight LLMs, the embedding similarity maps 83% of the entities named by the LLMs and yields only one incorrect match.

## 14. From Geographic Memory to Spatial Generalization in Large Language Models

- Authors: Chen Chu, Zhaonan Wang, Cyrus Shahabi, Hengcai Zhang, Feng Lu
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-19
- DOI: Unavailable
- Categories: cs.CL, cs.AI, cs.LG
- Relevance: 3.1108254670941813
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.25703v1
- PDF: https://arxiv.org/pdf/2611.25703v1
- Local PDF: pdf/2026-11-21_14_From Geographic Memory to Spatial Generalization in Large Language Models.pdf

Large language models (LLMs) can associate places with geographic descriptions, but recovering an observed association does not establish an ability to generalize across geographic space. We distinguish geospatial memory, the recovery of location--description associations observed during training, from spatial generalization, the prediction of descriptions for locations in unobserved regions. We investigate whether continuous location representations improve this generalization and encourage geographic knowledge to become spatially organized within an LLM. We frame this organization as a latent spatial field: a learned mapping from locations to descriptions connected through spatial dependencies. Building on a continuous spatial encoder, we project location representations into the model's embedding space and supply them as spatial tokens. We evaluate the resulting models on two newly curated geo-text benchmarks for Los Angeles and London using two complementary assessments. Geospatial captioning tests both memory and spatial generalization by generating descriptions at observed locations and at locations beyond the spatial coverage of the training observations. A separate geospatial grounding model tests whether generated location--description pairs provide useful additional supervision for mapping text to geographic space. Across multiple LLM families, continuous location representations improve captioning at unobserved locations relative to textual coordinates, while their generated descriptions yield modest but consistent improvements in downstream grounding. Layer-wise probing and representation clustering provide additional evidence consistent with spatially organized geographic representations. Together, these findings show the value of evaluating spatial generalization separately from memory and of incorporating continuous spatial representations into language models.

## 15. LIFT: Latent Flow Matching for Probabilistic Cell Fate Dynamics with Single Cell Snapshots

- Authors: Bowen Yang, Junda Ying, Yuxuan Wang, Peijie Zhou, Lei Zhang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-19
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.0881624811885118
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.25917v1
- PDF: https://arxiv.org/pdf/2611.25917v1
- Local PDF: pdf/2026-11-21_15_LIFT_ Latent Flow Matching for Probabilistic Cell Fate Dynamics with Single Cell Snapshots.pdf

Lineage tracing links cell states through clonal ancestry, but does not generally identify unique source-descendant pairings. Learning from such data therefore requires a model of conditional outcomes, rather than only the terminal population distribution. We introduce LIFT, a latent flow framework for probabilistic cell-state generation from lineage-informed couplings. Variational inference encodes alternative outcomes in a latent space, while a conditional prior enables sampling from the initial state alone. A Mean Flow decoder predicts future cell state directly, requiring one decoder evaluation per sampling, which makes it convenient to predict cell fate through large scale Monte-Carlo sampling. This construction combines a representation of one-to-many relationships with efficient sampling and an analysis of conditional prediction error. Experiments on synthetic and real datasets demonstrate LIFT's ability to recover both population distribution and cell fate probabilities.

## 16. GRODE-RTL: Source-Mapped Dependency Views for LLM-Based RTL Repair

- Authors: Jingyi Zhou, Yi Liu, Bin Sun, Hongji Zhang, Dongsheng Zuo, Qiang Xu
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-19
- DOI: Unavailable
- Categories: cs.AR, cs.AI, cs.MA
- Relevance: 3.014508140166904
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.25661v1
- PDF: https://arxiv.org/pdf/2611.25661v1
- Local PDF: pdf/2026-11-21_16_GRODE-RTL_ Source-Mapped Dependency Views for LLM-Based RTL Repair.pdf

Large Language Models show great potential for automated Register-Transfer Level repair, yet they struggle with non-local faults where root causes and failing outputs reside far apart in source code. Treating RTL as a flat token sequence obscures hardware dataflows, whereas exposing complete synthesized graphs overwhelms the model with fine-grained metadata. To resolve this representation dilemma, we propose GRODE-RTL, an anchor-centric representation that extracts the single-clock-stage fan-in cone of a suspect register from the netlist, maps netlist nodes back to editable source lines, and organizes them into a compact hop-partitioned dependency view. By prioritizing direct drivers and folding distant hops, GRODE-RTL guides standard tool-using agents without exposing ground-truth hints or oracle feedback. We evaluate GRODE-RTL across 30 formally validated non-local faults using three LLMs (DeepSeek-V4-Flash, GLM-5.2, and MiniMax-M3) alongside a controlled six-configuration ablation study. GRODE-RTL improves pass@1 over source-level exploration by 16.7% on DeepSeek, by 26.7% on GLM-5.2, and by 20.0% on MiniMax-M3, with consistent gains on the hard-to-retrieve far-distance and indirect-anchor subsets of all three models. Our controls isolate structural relevance from generic context expansion, proving that selective dependency organization rather than full graph exposure is key to effective RTL repair.

## 17. DSFlow: A Neuro-Symbolic Data Workflow Agent with Statistical Diagnostic Guardrails

- Authors: Junfeng Nie, Xiaohui Chen
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-18
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 2.9389298432911373
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.25111v1
- PDF: https://arxiv.org/pdf/2611.25111v1
- Local PDF: pdf/2026-11-21_17_DSFlow_ A Neuro-Symbolic Data Workflow Agent with Statistical Diagnostic Guardrails.pdf

Data science workflows often require tools that presume non-trivial technical knowledge. Large language models (LLMs) reduce this barrier, but a gap remains between flexible general-purpose agents and statistically controlled pipelines. We introduce DSFlow, a LangGraph-based neuro-symbolic data-agent platform that combines reusable, LLM-selected skills with deterministic diagnostic guardrails. Skills provide extensible task knowledge. Symbolic validation can accept a proposed method, request clarification or replanning, override an unsuitable method, or supply a safe fallback. Regression and clustering case studies illustrate how DSFlow uses diagnostic evidence to correct method choices and documents those decisions in auditable reports.

## 18. MatVerse: A Foundation Model for Materials Science

- Authors: Xuanyu Zhu, Qian Tan, Bo Chen, Jiaqing Xie, Yang Han, Mei Wu, Wanhao Liu, Xuanze Lin, Yuchen Zhou, Shijie Wang, Biqing Qi, Shixiang Tang, Wenwei Zhang, Tianfan Fu, Kai Yu, Lu Chen, Yuqiang Li, Xin Chen
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-19
- DOI: Unavailable
- Categories: cs.AI, cond-mat.mtrl-sci
- Relevance: 2.9336554253907856
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.25651v1
- PDF: https://arxiv.org/pdf/2611.25651v1
- Local PDF: pdf/2026-11-21_18_MatVerse_ A Foundation Model for Materials Science.pdf

Materials science involves highly heterogeneous scientific information, including textual knowledge, molecular and crystal structures, experimental characterization data, microscopy images, and structure-property relationships. Developing a general-purpose foundation model capable of understanding and reasoning over these diverse materials representations remains challenging. In this technical report, we introduce MatVerse, a materials foundation model built upon Intern-S2-Preview and further specialized through large-scale materials-domain post-training. We construct a large-scale multimodal training corpus covering materials knowledge, scientific reasoning, quantitative problem solving, structural understanding, and multimodal scientific interpretation. To improve domain adaptation, we develop a unified data construction pipeline combining teacher-guided reasoning distillation, scientific problem synthesis, consistency-based filtering, and retrieval-based multimodal data construction. We evaluate MatVerse on three representative materials-science benchmarks: our human-calibrated OmniMatBench, MatSciBench, and MaCBench. Results demonstrate consistent improvements after materials-specific post-training over the base model on all three benchmarks, alongside improved inference efficiency on calculation-intensive problems. These results show that targeted domain-specific post-training can effectively enhance scientific reasoning, materials knowledge understanding, and multimodal scientific capabilities of foundation models. MatVerse provides a unified language-and-vision interface for materials science and serves as a foundation for future AI-assisted materials research workflows.

## 19. STAGE: Spatio-Temporal Augmented Graph Expansion for Weakly Supervised Cross-Tweet Event Causality Discovery

- Authors: Hieu Minh Duong, Todd Gary, Eugene Levin, Long Nguyen
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-19
- DOI: Unavailable
- Categories: cs.CL, cs.AI
- Relevance: 2.927730612744041
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.26255v1
- PDF: https://arxiv.org/pdf/2611.26255v1
- Local PDF: pdf/2026-11-21_19_STAGE_ Spatio-Temporal Augmented Graph Expansion for Weakly Supervised Cross-Tweet Event Causality Discovery.pdf

Causal relations in disaster-related social media of- ten span independent posts, making cross-tweet causal discovery difficult to supervise and model at scale. We propose STAGE, a framework that separates scalable cross-tweet weak-supervision construction from spatio-temporal relational learning over event occurrences. Starting from local causal seeds, STAGE retrieves semantically related event occurrences across tweets and uses a causal scorer to construct weakly labeled cross-tweet pairs. These pairs supervise a multi-head Graph Attention Network over semantically enriched event representations and a spatio- temporal context graph. We evaluate STAGE on California Wildfire and Hurricane Harvey using human-gold cross-tweet test sets and 15 baselines. Compared with local-only supervision, the constructed cross-tweet supervision improves STAGE AUPRC by 0.340 on Wildfire and 0.107 on Hurricane. STAGE achieves in-domain AUROC of 0.885 on Wildfire and 0.710 on Hurricane. Cross-disaster experiments reveal asymmetric transfer, highlighting sensitivity to dataset-specific spatio-temporal shifts. These results demonstrate the value of scalable cross-tweet supervision combined with relational event modeling for causal learning across fragmented disaster reports.

## 20. Evidence from a Multi-Regime Causal Discovery Benchmark: UCMT Algorithms, Comparative Performance, and Controlled Ablation Studies

- Authors: Mahyar Eslami
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-19
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 2.918084266463901
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.26383v1
- PDF: https://arxiv.org/pdf/2611.26383v1
- Local PDF: pdf/2026-11-21_20_Evidence from a Multi-Regime Causal Discovery Benchmark_ UCMT Algorithms, Comparative Performance, and Controlled Ablati.pdf

We present an internal, pre-registered evaluation of the UCMT causal discovery algorithm family alongside established alternatives across heterogeneous benchmark regimes, complemented by a separately pre-registered, controlled study of UCMT v2 Global components. The contribution is both empirical and methodological: a family-stratified comparison of three actively developed algorithm configurations and targeted evidence about which internal stages affect their outcomes. In the main benchmark, UCMT v2 Global has higher directed F1 than NOTEARS and DAGMA in selected real, semi-synthetic and Gaussian-network comparisons at the paired-run level, while trailing leading permutation-search methods in other settings. The BOSS-based UCMT v4 produces a CSuite-specific directed-F1 improvement over BOSS (mean paired difference +0.279; pair-level Holm p < 0.001), but the dataset-level adjusted result is not significant (p = 0.188). In a separate fixed-skeleton ablation, UCMT v2 Global exceeds an adapted R^2-SortnRegress orientation baseline on standardized iSCM data (directed F1 0.537 vs 0.468, dataset-level Holm p = 0.031); absolute orientation accuracy is 0.563 and there is no established broad advantage over RESIT, ANM or DirectLiNGAM. Controlled ablations show that sparsity and BIC-based refinement materially affect some outcomes, whereas the examined arbitration and automatic regime-selection mechanisms do not yield confirmed general improvements. We report performance shortcomings, multiple-testing correction, runtime costs, evaluation limitations and reproducibility checks. The results support UCMT as an implemented and empirically investigated algorithm family, not a claim of overall superiority, independent validation or demonstrated commercial impact.

## 21. Automated data to model transformation for constraint programming with AI

- Authors: Zhengqi Shi, Jin Huang, Xinyu Li, Hao Zhang, Mingming Peng, Xinyi Yang, Qihao Liu, Shaosen Su, Chunjiang Zhang, Peigen Li, Liang Gao
- Source: openalex
- Venue type: journal
- Journal: Nature Communications
- Publication status: published
- Publication date: 2026-11-19
- DOI: https://doi.org/10.1038/s41467-026-78715-2
- Categories: Constraint Satisfaction and Optimization, AI-based Problem Solving and Planning, Topic Modeling
- Relevance: 2.901229411334798
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://doi.org/10.1038/s41467-026-78715-2
- PDF: https://www.nature.com/articles/s41467-026-78715-2_reference.pdf
- Local PDF: pdf/2026-11-21_21_Automated data to model transformation for constraint programming with AI.pdf

Artificial intelligence for combinatorial optimization depends on high-quality, structured training data, yet transforming ambiguous natural-language descriptions into precise, executable formal models remains a major bottleneck, traditionally requiring extensive manual effort and domain expertise. We develop CPAM-LLM, an automated constraint-programming modeling framework based on large language models that converts unstructured problem specifications into validated and executable formal models. The framework integrates retrieval-augmented generation grounded in formal concept analysis for structural validation, chaos-mapping-based data augmentation to enhance cross-domain generalization, and dynamic constraint adaptation to accommodate evolving problem settings. We demonstrate its effectiveness across five scenarios, including DNA sequence design, reconfigurable energy storage systems, and unmanned vehicle logistics. The results show that the framework can automate the data-to-model pipeline while adapting reliably to changing requirements, providing a practical approach to automated data formalization and indicating the importance of accessible, high-quality structured data for reliable downstream artificial intelligence applications.

## 22. Coordinated Use of Large Language Models in Academic Research

- Authors: Vladislav Marinov
- Source: arxiv
- Venue type: preprint
- Journal: Media and Language (2026), no. 00, pp. 1-28 (original Bulgarian publication)
- Publication status: preprint
- Publication date: 2026-11-19
- DOI: 10.58894/dvzte852
- Categories: cs.AI, cs.CY
- Relevance: 2.8828000359333448
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.25502v1
- PDF: https://arxiv.org/pdf/2611.25502v1
- Local PDF: pdf/2026-11-21_22_Coordinated Use of Large Language Models in Academic Research.pdf

This study proposes a methodological framework for the coordinated use of multiple large language models in academic research. Its central argument is that involving more models does not in itself guarantee more reliable results; what matters is how cognitive and verification operations are organised. The framework is based on seven principles (procedural independence, functional allocation, the diagnostic value of divergence, the diagnostic value of convergence, external verification, proportionality of checking, and human epistemic responsibility) and sets out a non-linear multi-LLM protocol in which independently obtained results are compared, critically examined and, where necessary, verified against external sources. The approach is illustrated through real-world cases drawn from research practice. The study concludes that moving from a single language model to a coordinated multi-LLM process represents a change in the organisation of research, in which the researcher makes the final decisions and bears scholarly responsibility.

## 23. Invertible Transport Between Sample-Only Distributions via Projected Characteristic Functions

- Authors: Juan Gutiérrez, Victor Gutiérrez-García, José Luis Blanco-Murillo
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-19
- DOI: Unavailable
- Categories: cs.LG, cs.CV
- Relevance: 2.879633000027371
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.26187v1
- PDF: https://arxiv.org/pdf/2611.26187v1
- Local PDF: pdf/2026-11-21_23_Invertible Transport Between Sample-Only Distributions via Projected Characteristic Functions.pdf

Many useful latent distributions can be sampled but do not have a tractable density. Such distributions may be represented by empirical collections of real-world observations or generated by scientific simulators and black-box generative models. These sample-only priors cannot be used directly in likelihood-based normalizing flows, which require evaluating the prior density. We propose Projected Characteristic-Function matching (PCF), a density-free framework for learning an invertible map between a data distribution and a prior specified only through samples.
  Our method aligns distributions using projected empirical characteristic functions, eliminating the need for density estimation, adversarial training, or paired observations. To address the non-uniqueness of the transport map, we introduce an optional transport regularizer that selects lower-displacement transformations while preserving endpoint alignment.
  We benchmark PCF on controlled transports, sample-efficiency studies, and high-dimensional alignment tasks. PCF matches the accuracy of kernel MMD on the controlled benchmark and on raw-pixel MNIST--USPS at a cost linear in the batch size, and it is more sample-efficient, achieving lower endpoint error than MMD in 13 of 15 paired runs across library sizes. By avoiding pairwise kernel evaluation, it reduces discrepancy memory by 29.8% and trains at batch sizes where kernel MMD exceeds GPU memory. These results show that PCF provides accurate and efficient invertible transport, particularly in sample- and memory-limited settings.

## 24. Causal Discovery with False Positive Error Control

- Authors: Erik Jahn, Venkat Chandrasekaran, Frederick Eberhardt, Leonard Schulman
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-19
- DOI: Unavailable
- Categories: stat.ML, cs.LG
- Relevance: 2.8627544534485496
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.25376v1
- PDF: https://arxiv.org/pdf/2611.25376v1
- Local PDF: pdf/2026-11-21_24_Causal Discovery with False Positive Error Control.pdf

Causal discovery methods produce data-driven hypotheses about causal relationships, which may become new scientific findings or inform decisions about downstream interventions. In such settings, false positive causal claims can be more consequential than false negatives. Yet few methods target false positive error control in causal discovery, and existing error guarantees are often asymptotic and require strong versions of the faithfulness assumption. We introduce the $m$-conservative PC algorithm and prove that it controls false discovery rate in the linear Gaussian setting under an extremely weak version of the faithfulness assumption. In our framework, false positive error for causal graphs is defined based on the conditional-independence information they entail, yielding a metric that penalizes both false adjacencies and incorrect edge orientations. The parameter $m$ quantifies a trade-off between algorithmic complexity and the strength of the required faithfulness assumption. The $m$-conservative PC algorithm combines undirected graph learning, a Benjamini-Yekutieli-style procedure for conditional independence testing, and a conservative orientation step that marks unresolved or contradictory edge directions as ambiguous. Our algorithm produces valid outputs and retains error guarantees even in the finite-sample setting, despite possible random errors in the conditional independence tests.

## 25. HiSA: Sparsifying the Hidden Dimension of RoPE Attention in LLMs

- Authors: Ambroise Borbely, Mathieu Salzmann, Olivier Verscheure
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-19
- DOI: Unavailable
- Categories: cs.LG, cs.CL
- Relevance: 2.8601381098607135
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.26363v1
- PDF: https://arxiv.org/pdf/2611.26363v1
- Local PDF: pdf/2026-11-21_25_HiSA_ Sparsifying the Hidden Dimension of RoPE Attention in LLMs.pdf

Attention in large language models (LLMs) scores every query against every key with a full dot product. We investigate whether this dot product must be computed completely for attention to be effective. We propose Hidden Sparse Attention (HiSA), which keeps the query and key projections intact but only computes a partial dot product, following a static, parameter-free rule set by the token positions: attention becomes sparse in the hidden (feature) dimension, an axis much less explored than token sparsity, rather than over tokens as in almost all sparse attention methods. Based on the structure of rotary position embeddings (RoPE), we decompose keys and queries into parts which can be omitted when computing attention. By training LLMs from scratch with HiSA, we find that this partial dot product does not hurt but improves performance compared with the complete product while computing only about a third of the query-key products. During inference HiSA improves decoding speed and shrinks memory footprint. We also extend HiSA to FlashAttention-3 kernels for training and inference. Finally, we motivate our approach by showing that dense attention learns to suppress the attention score parts that HiSA drops. Code is available at https://github.com/ambroise-b/hisa.

## 26. VisAlloc: Allocating Visual Supervision for On-Policy Self-Distillation

- Authors: Haoran Xu, Tian Chen, Yuhe Wu, Yanbo Zhao, Junchi Liao, Hongyu Wang, Jiaze Li, Wentao Wang, Yanfeng Li, Rui Qian
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-18
- DOI: Unavailable
- Categories: cs.CV, cs.AI
- Relevance: 2.8526866795445738
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.25069v1
- PDF: https://arxiv.org/pdf/2611.25069v1
- Local PDF: pdf/2026-11-21_26_VisAlloc_ Allocating Visual Supervision for On-Policy Self-Distillation.pdf

On-policy self-distillation (OPSD) offers a promising approach to improving visual reasoning in multimodal large language models (MLLMs). However, not all samples benefit equally from privileged visual guidance, and uniform token supervision can dilute visually grounded signals. We propose VisAlloc, a dual-level framework combining sample-level visual filtering with token-level counterfactual reweighting. A fixed paired-teacher filter retains samples answered correctly from an evidence-centered positive crop but incorrectly from a spatially displaced negative crop. At the token level, both EMA teachers score the same student-generated response, and their absolute log-probability differences measure view sensitivity. Additional supervision targets tokens admitted by sensitivity or teacher-distribution disagreement, with shared frozen-prior, template-bigram, and student--teacher divergence gates. Inverse-frequency redistribution preserves the total additional weight within each micro-batch, while the positive teacher remains the sole distillation target. Inference requires only the full-image student. Across eight benchmarks, our 4B and 9B models achieve macro-averages of 81.44 and 84.92, outperforming Vision-OPD reproductions by 0.97 and 0.52 points, respectively. Code on GitHub: https://github.com/Kaelyn01/VisAlloc

## 27. Goal-Guided Reinforcement Learning via Fine-Tuning Vision-Language Models

- Authors: Yajie Qi, Wei Wei, Lin Li, Lijun Zhang, Jianye Hao
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-19
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 2.847406373989576
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.25742v1
- PDF: https://arxiv.org/pdf/2611.25742v1
- Local PDF: pdf/2026-11-21_27_Goal-Guided Reinforcement Learning via Fine-Tuning Vision-Language Models.pdf

Exploration remains a major challenge for reinforcement learning (RL) agents in Craftax-style environments due to sparse rewards and long horizons. Large language models (LLMs) can guide exploration by generating high-level goals, but methods using models without explicit task adaptation often rely on carefully designed prompts and may produce inconsistent or contextually inappropriate goals. We introduce CCGP-2M, a multimodal goal-preference dataset constructed from interaction trajectories in Craftax-Classic, and propose a vision-language model (VLM)-guided RL framework that learns environment-specific goal guidance from this dataset. The framework consists of two stages: offline VLM fine-tuning and online goal-guided RL. In the offline stage, we align the VLM with goal preferences using Kullback-Leibler Token-level Direct Preference Optimization (KLTDPO), which combines token-level KL regularization with distributionally robust reweighting. Experiments on Craftax-Classic show that our method collects diamonds earlier than state-of-the-art baselines, achieves the highest score and reward, and attains the highest success rates on most achievements.

## 28. Decoupled Knowledge Retrieval and Compact Memory Enable Reliable Lifelong Model Editing

- Authors: Yue Che, Jingze Wang, Chen Guoyi, Yujie Wu, Xuming Ran, Mingkun Xu
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-19
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 2.846071548421629
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.25861v1
- PDF: https://arxiv.org/pdf/2611.25861v1
- Local PDF: pdf/2026-11-21_28_Decoupled Knowledge Retrieval and Compact Memory Enable Reliable Lifelong Model Editing.pdf

Lifelong model editing requires continuously incorporating new facts into deployed large language models (LLMs) without expensive retraining or compromising existing capabilities. Memory-based editors offer an appealing solution by keeping the base parameters untouched, yet their practical use is hindered by linearly growing storage requirements and deteriorating retrieval performance as edits accumulate. To tackle these problems, we introduce BiSpace, a lifelong model editing framework that decouples memory retrieval from knowledge injection across two distinct representation spaces. BiSpace routes queries and identifies relevant edits in an external semantic space, while injecting the corresponding knowledge into the internal representation space of the LLM through sparse and storage-efficient updates. Extensive experiments show that BiSpace shrinks each entry's storage to only about 10.2% of the original and shows strong resilience to long edit sequences of up to 16K edits. On a more challenging benchmark, BiSpace further improves Overall Performance by more than 23% over existing methods. These results advance memory-based editing toward reliable long-term model maintenance at scale.

## 29. Asuka-FM: A System-Architectural Co-Design Framework for Efficient Text-to-Image Pretraining on Consumer Hardware

- Authors: Víctor Rodrigo González, Pablo M. Olmos, Ignacio Peis, Alejandro Lancho
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-19
- DOI: Unavailable
- Categories: cs.CV, cs.AI
- Relevance: 2.844604410349984
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.26437v1
- PDF: https://arxiv.org/pdf/2611.26437v1
- Local PDF: pdf/2026-11-21_29_Asuka-FM_ A System-Architectural Co-Design Framework for Efficient Text-to-Image Pretraining on Consumer Hardware.pdf

Frontier text-to-image (T2I) foundation models predominantly rely on multi-billion parameter Diffusion Transformers (DiTs) pretrained across massive compute clusters, creating an accessibility barrier for academic laboratories. When training DiTs from scratch on single consumer GPUs (e.g., an NVIDIA RTX 4090 with 24\,GB VRAM), practitioners encounter three primary bottlenecks: quadratic attention sequence costs, Just-In-Time (JIT) compilation graph breaks induced by variable aspect-ratio bucketing, and an autoencoder throughput wall where frozen Variational Autoencoder (VAE) operations dominate step latency. In this work, we introduce \textbf{Asuka-FM}, an end-to-end system and architectural framework demonstrating that competitive dual-stream DiTs ($\sim$206M parameters) can be pretrained from scratch on a single consumer GPU in $\sim$160 GPU hours for under \$55. Asuka-FM integrates four core designs: (i) an AdaLN-free dual-stream DiT backbone reducing parameter count; (ii) structured sequence sparsification via Sparse-Dense Residual Fusion (SPRINT) to cut attention FLOPs by over 50\%; (iii) continuous aspect-normalized Rotary Position Embeddings (RoPE) coupled with shifted square crop training, guaranteeing static tensor shapes while unlocking zero-shot virtual camera control; and (iv) a pixel adaptation phase utilizing a lightweight (10M parameter) Patch Detailer Head operating under velocity regression ($v$-prediction). Evaluated on open-domain benchmarks without benchmark-specific fine-tuning, Asuka-FM achieves GenEval 0.588 / DPG 78.96 scores at 256px and GenEval 0.609 / DPG 78.51 scores at 512px, setting a new Pareto-optimal efficiency standard for democratic foundation modeling.

## 30. Time Series Structure Learning with Local Causal Parent Discovery

- Authors: Jacqueline Maasch, Shu Wan, Hank Zhu, Huan Liu, Zhiguang Wang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-19
- DOI: Unavailable
- Categories: cs.LG, stat.ML
- Relevance: 2.8389156399023117
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.26232v1
- PDF: https://arxiv.org/pdf/2611.26232v1
- Local PDF: pdf/2026-11-21_30_Time Series Structure Learning with Local Causal Parent Discovery.pdf

Learning and inference on time series can pose significant statistical challenges, including autocorrelated observations, distribution shift over time, and the curse of dimensionality. These challenges complicate the practical application of causal discovery algorithms, which already suffer from high computational and sample complexity in the general case. To mitigate these issues, this work introduces Iterative Temporal Parent Discovery (ITPD): a sound and complete constraint-based procedure for causal structure learning on multivariate time series with causal nonstationarity. ITPD takes a local-to-global learning approach that discovers the global graph by sequentially discovering the parent set for each variable. ITPD exploits temporal structural priors, graph partitioning, and the local Markov condition to swap higher-order conditional independence tests for lower-order alternatives. With an exact oracle, ITPD performed the least number of tests and used the smallest average conditioning set sizes relative to baselines. In benchmarking simulations, ITPD sat on the Pareto frontier with respect to F1 and wall-clock time and was faster than baselines on large graphs ($\geq$ 1000 nodes). For graphs with 2000 nodes, ITPD ran $2.3\times$, $9.1\times$, and $40.9\times$ faster than iterative IAMB, DF-PC, and PCMCI, respectively.
