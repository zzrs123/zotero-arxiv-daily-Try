# Paper Daily Reading - 2026-08-27

## 1. MolEmb: Multimodal Large Language Models Can Be Strong Molecular Embedding Models

- Authors: Xinjian Zhao, Xiangru Jian, Yaoyao Xu, Xiaozhuang Song, Wei Pang, Lei Bai, Tianshu Yu
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-24
- DOI: Unavailable
- Categories: cs.AI, cs.LG
- Relevance: 3.397334773204233
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.23646v1
- PDF: https://arxiv.org/pdf/2608.23646v1
- Local PDF: pdf/2026-08-27_01_MolEmb_ Multimodal Large Language Models Can Be Strong Molecular Embedding Models.pdf

Molecular embedding models can serve as foundational infrastructure for computational chemistry and drug discovery, where reusable vector representations support property prediction, virtual screening, and retrieval. Most molecular encoders are specialist models built around a single molecular view, producing unconditional vectors with no language interface for varying the representation. We ask whether multimodal large language models (MLLMs), which natively process images, text, and symbolic inputs, can instead serve as \emph{general molecular embedding models} that produce embeddings conditioned on both a molecular profile and a natural-language semantic context. We introduce \textbf{MolEmb}, a lightweight framework that adapts MLLMs by aligning molecular profiles with textual descriptions in a shared embedding space using a bidirectional contrastive objective. The resulting embedding model is competitive on molecular property prediction and supports cross-modal molecule--text retrieval in the same space. We further introduce \textbf{MolCAR}, a diagnostic benchmark for context-aware retrieval, and find that context-aware molecular embedding is primarily a data property of the supervision. These results suggest that MLLMs are not merely chemistry assistants or generators, but a viable and extensible route to general molecular embedding models.

## 2. FedV-KGQA: Multi-Hop Question Answering over Vertically Partitioned Knowledge Graphs

- Authors: Md Saikat Islam Khan Bappy, Oshani Seneviratne
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-25
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 3.3581946215916556
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.24846v1
- PDF: https://arxiv.org/pdf/2608.24846v1
- Local PDF: pdf/2026-08-27_02_FedV-KGQA_ Multi-Hop Question Answering over Vertically Partitioned Knowledge Graphs.pdf

Real-world data for knowledge graph question answering is often distributed across different organizations due to governance and data sovereignty constraints. While centralized systems exist, they cannot answer multi-hop questions when the required facts are split across vertically partitioned silos. In this paper, we propose FedV-KGQA, a framework for multi-hop reasoning over knowledge graphs in which organizations share entities but own disjoint sets of relations. Our approach combines local graph enrichment and knowledge graph embeddings to ensure raw triples and relation parameters never leave each silo, establishing a structural data boundary without requiring centralized graph access. We further introduce a topic entity anchoring mechanism that grounds questions in the correct graph neighborhood without any runtime inter-silo communication. We evaluate 12 model configurations across three benchmarks and show that FedV-KGQA performs strongly, remains close to centralized performance, generalizes to 3-hop reasoning, and is robust to embedding perturbations.

## 3. HMGCLIP: Heterogeneous Multi-Granularity Contrastive Learning for E-commerce Representation Learning

- Authors: Qiuyu Zhu, Yi Gao, Zhichao Wan, Mingyang Ma
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-25
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 3.3484296742395534
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.24467v1
- PDF: https://arxiv.org/pdf/2608.24467v1
- Local PDF: pdf/2026-08-27_03_HMGCLIP_ Heterogeneous Multi-Granularity Contrastive Learning for E-commerce Representation Learning.pdf

Although recent Multimodal Large Language Models (MLLMs) have advanced general product understanding, they implicitly encode product information into global embeddings, thereby limiting their ability to capture fine-grained attributes. This limitation hinders performance in tasks requiring precise attribute discrimination, such as distinguishing subtle material differences among visually similar products. To address this challenge, we propose HMGCLIP, a unified multimodal embedding framework. By constructing a heterogeneous hypergraph, we leverage hypergraph topology to mine structure-aware hard negatives and align multi-granular semantics at both relation and hyperedge levels. This design enables a dual-granularity inference mechanism that dynamically fuses attribute evidence for both fine-grained and coarse-grained downstream tasks. Furthermore, we release a comprehensive fine-grained e-commerce dataset to facilitate future benchmarking. Extensive experiments on this new dataset and the public MAVE benchmark show that HMGCLIP outperforms strong multimodal encoders, MLLMs, and e-commerce baselines, validating the superiority of HMGCLIP.

## 4. MDTE: Minority-Aware Diffusion over Temporal Edge Events for Imbalanced Node Classification

- Authors: Zhou Zelong, Zhang Tianming, Yang Zhengyi, Tang Yifu, Hou Chenyu, Cao Bin, Fan Jing
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-25
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.2454664947919722
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.24812v1
- PDF: https://arxiv.org/pdf/2608.24812v1
- Local PDF: pdf/2026-08-27_04_MDTE_ Minority-Aware Diffusion over Temporal Edge Events for Imbalanced Node Classification.pdf

Class-imbalanced node classification on temporal graphs is challenging because majority-dominated temporal propagation progressively assimilates minority representations, while conventional node and neighborhood information provides insufficient discriminative evidence for minority classes. To address these issues, we propose MDTE, a minority-aware diffusion framework that reconstructs stable and discriminative temporal edge-event representations through conditional diffusion denoising. Specifically, MDTE introduces Distribution-Aware Selective Propagation, which combines Local Outlier Factor (LOF)-based propagation filtering with cluster-aware low-frequency propagation. The module preserves informative neighborhood dependencies while mitigating harmful propagation and majority-class information assimilation. It further develops Multi-View Discriminative Fusion, which exploits feature reconstruction and topology prediction to characterize class-wise differences in distribution learning and extracts complementary discriminability signals to guide denoising. Experiments on five real-world datasets demonstrate that MDTE consistently achieves the best performance on minority-class-oriented metrics, improving minority-class recall by up to 23.53 percentage points, minority-class F1 by 8.68 percentage points, and AUPRC by 2.67 percentage points over the strongest baselines.

## 5. Giraffe: A Mapping Architecture from Hidden Text Representations to Visual Embeddings for Efficient Graphic Design

- Authors: Nejla Ghaboosi
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-25
- DOI: Unavailable
- Categories: cs.AI, cs.LG
- Relevance: 3.1831533171226987
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.23970v1
- PDF: https://arxiv.org/pdf/2608.23970v1
- Local PDF: pdf/2026-08-27_05_Giraffe_ A Mapping Architecture from Hidden Text Representations to Visual Embeddings for Efficient Graphic Design.pdf

Multimodal large language models (MLLMs) have made significant progress in understanding and interpreting mul- timedia content. However, their ability to generate me- dia remains limited. Recent approaches have attempted to bridge this gap by translating the hidden representations of token sequences into the embedding space of visual models or directly into raw image data. However, these methods often represent each image using multiple specialised to- kens which significantly increases the input length. This be- comes a major limitation for tasks such as graphic design generation where the output typically involves a seamless blend of thousands of tokens across text, multiple images, and layout information. To address this challenge, a novel architecture is proposed that maps hidden token represen- tations to the embedding space of visual models, such as CLIP ViT-L/14, using a single [IMG] token per image. The architecture employs two shallow MLP blocks, each with a separate compression module followed by a shared expan- sion module, trained with six distinct loss functions. One block aids the other during training and is omitted during inference, resulting in a lightweight solution. Strong perfor- mance is demonstrated in both image-to-design and text-to- design generation tasks.

## 6. Do Recipes Have Personas? Characterizing and Generating Creator Style in Attributed Procedural Graphs

- Authors: Lei Jiang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-25
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 3.1805969187907515
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.24369v1
- PDF: https://arxiv.org/pdf/2608.24369v1
- Local PDF: pdf/2026-08-27_06_Do Recipes Have Personas_ Characterizing and Generating Creator Style in Attributed Procedural Graphs.pdf

While large language models (LLMs) possess vast zero-shot procedural knowledge, their tendency to produce homogenized logic often obscures the unique, idiosyncratic execution processes of individual human creators. In this paper, we investigate the computational discovery of procedural personas from unstructured data. To achieve this, we introduce ViralRecipesTrans, a new dataset of procedurally aligned execution flow graphs extracted from popular culinary video transcripts and explicitly mapped to specific creators. We formulate procedural stylometry as a graph learning and process discovery task, revealing a fundamental duality: while traditional lexical classifiers overfit via semantic leakage, discrete topological metrics successfully capture the rigid physical constraints of a creator's workflow. Building upon this characterization, we extend our framework into a novel generative task--predicting a creator's exact structural execution graph for unseen dishes. We expose a fundamental dichotomy in style generation between global macro-planning and local structural execution. Our results demonstrate that few-shot LLMs dominate semantic assignment but suffer from persistent macro-planning deficits, whereas our structured two-stage model achieves superior topological control via rigid Markovian priors. Together, an ensemble approach to procedural generation combines the strengths from both sides, dynamically synthesizing global semantic reasoning with localized topological footprints to automate the discovery and generation of personalized workflows.

## 7. Constraint-Guided Enterprise Data Mapping with Large Language Models

- Authors: Sebastian Monka, Pramod Anantharam, Thien Vo Minh, Lavdim Halilaj
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-25
- DOI: Unavailable
- Categories: cs.AI, cs.CL
- Relevance: 3.167889590071558
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.24218v1
- PDF: https://arxiv.org/pdf/2608.24218v1
- Local PDF: pdf/2026-08-27_07_Constraint-Guided Enterprise Data Mapping with Large Language Models.pdf

Enterprise entity alignment must handle semi-structured records, implicit attributes, and unit or granularity mismatches. Manual matching is still common in practice, but does not scale as schemas and providers evolve. LLM-only matching improves semantic recall, yet can violate structural and physical invariants, producing fluent yet operationally invalid correspondences.
  We propose constraint-guided mapping (CGM), a neuro-symbolic method with three stages: (i) schema-grounded admissibility constraints with metadata mc = <tau_c, delta_c>, where tau_c denotes the constraint type and delta_c provides executable relation and normalization logic; (ii) constraint-restricted candidate generation with cascade relaxation to guarantee a nonempty feasible set under noise; and (iii) neural ranking with bounded LLM disambiguation restricted to that feasible set.
  Methodologically, constraints operate as hypothesis-space operators rather than post-hoc validators, enabling controlled degradation under relaxation and auditable, human-guidable decisions. On a controlled structural-decoy benchmark, hard admissibility shrinks the candidate space by ~480x without dropping the GT, and a layer-by-layer ablation shows this gate, not the LLM, is the decisive lift (F1 0.08 to 0.66). The benefit is model-independent and adds no extra inference cost: a small model with constraints matches a frontier LLM used without them at ~28x lower cost. The method, not a single tuned configuration, transfers across seven enterprise makes (macro F1 0.70), each under its own automatically discovered, expert-refinable constraints, and lowers expert effort by ~7x versus spreadsheet workflows. Public Valentine results add an external ranking sanity check and mark the boundary: constraints should be hard only where structural invariants are match-determining.

## 8. COCI: Conference Organisers and Content Identifier

- Authors: Angelo Salatino, Francesco Osborne, Alexis Vizcaino, Aliaksandr Birukou, Enrico Motta
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-25
- DOI: Unavailable
- Categories: cs.DL, cs.AI
- Relevance: 3.072222258241031
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.24559v1
- PDF: https://arxiv.org/pdf/2608.24559v1
- Local PDF: pdf/2026-08-27_08_COCI_ Conference Organisers and Content Identifier.pdf

Despite the critical role of grey literature in scholarly communication, artefacts such as Calls for Papers (CfPs) remain largely isolated from modern Scholarly Knowledge Graphs. The unstructured and highly heterogeneous nature of these documents has traditionally hindered their large-scale processing. In this demo paper, we present the Conference Organisers and Content Identifier (COCI), an AI-based framework designed to extract fine-grained, structured metadata from raw CfP texts. COCI employs a multi-stage pipeline that combines Large Language Models (LLMs) with semantic mapping techniques to integrate extracted entities with established knowledge bases, including OpenAlex, DBLP, TIB ConfIDent, and the AIDA Dashboard. By disambiguating authors and semantically aligning topics and conference series, COCI bridges the gap between informal scholarly dissemination and structured Semantic Web resources, laying the foundation for systematic analysis of non-publisher-based academic events.

## 9. PhysMLLMs: Spatial Priors for Unified Referring Segmentation and Grounded Reasoning of Images and Videos

- Authors: Siyao Yan, Bo Han, Jisheng Dang, Bimei Wang, Shude Wang, Hong Peng, Yulan Guo, Jianhuang Lai, Bin Hu, Tat-SengChua
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-25
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 3.008238458419494
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.24574v1
- PDF: https://arxiv.org/pdf/2608.24574v1
- Local PDF: pdf/2026-08-27_09_PhysMLLMs_ Spatial Priors for Unified Referring Segmentation and Grounded Reasoning of Images and Videos.pdf

Video multimodal large language models support language guided video segmentation, but they often show spatio temporal inconsistencies, e.g., jitter, drift, and identity switches. These failures are more common when targets are partly hidden or when similar objects appear nearby.One likely reason is that current training lacks explicit spatial priors, which makes it difficult to maintain stable spatial identity and shape over time. We present PhysMLLMs, a training-stage prior injection architecture that injects physics-inspired spatial continuity priors into Video MLLMs. PhysMLLMs is designed to encourage more stable object-centered representations by aligning the student global visual representation with a frozen teacher model during training. Our core mechanism, Global Representation Prior Alignment (REPA-Global), distills global visual representations from a frozen DINOv2 teacher using an offline embedding cache and a scheduled distillation plan. This design keeps inference unchanged and does not add inference time cost. Across multiple video benchmarks, PhysMLLMs improves video segmentation mask quality and cross-frame consistency, with larger gains on challenging cases involving small targets, fast motion, occlusion, distractors, and reasoning queries. On single-frame referring image segmentation and representative general VLM benchmarks, PhysMLLMs maintains comparable performance, demonstrating that the injected spatial prior improves video consistency without compromising image-level grounding or general multimodal capability. These results suggest that physics-inspired spatial prior injection can improve temporal stability while preserving general capability. The code is available at https://github.com/tusu-code/20260121-icml2026-2.git.

## 10. MoTE: Mixture of Task Experts for Multi-Task Video Understanding

- Authors: Muhammad Asad Ali, Umar Khan, Nadia Robertini, Didier Stricker
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-25
- DOI: Unavailable
- Categories: cs.CV, cs.LG
- Relevance: 2.9920235773053494
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.24763v1
- PDF: https://arxiv.org/pdf/2608.24763v1
- Local PDF: pdf/2026-08-27_10_MoTE_ Mixture of Task Experts for Multi-Task Video Understanding.pdf

Procedural video-language models must solve heterogeneous tasks from the same visual evidence, including action recognition, forecasting, and procedure prediction. Dense transformer decoders share the same feed-forward networks across tasks, which can entangle task behavior and make controlled capability expansion difficult. Sparse Mixture-of-Experts (MoE) decoders provide conditional computation, but token-level learned routing is not naturally aligned with task-level procedural objectives. We propose MoTE (Mixture of Task Experts), a decoder architecture that converts large language model feed-forward networks into task-specific experts while keeping the multimodal backbone shared. Each example follows one sample-level task route, so active task-expert computation remains independent of the number of stored task experts. We instantiate this design as VideoLLM-MoTE and evaluate it on five COIN benchmarks using explicit task routes. The five-expert model activates ~2B LLM parameters per sample and achieves higher average top-1 accuracy than recent VideoLLM baselines. Under the same expert topology, it improves over dense all-expert activation and learned sparse-routing controls. These results show that task-structured routing provides an interpretable and compute-efficient decoder alternative for multi-task video-language learning.

## 11. Matched Excess-Outranker Regularization for Candidate-Set Interference in Continual Knowledge Graph Embedding

- Authors: Hao Ren, Junbin Gao, Jiaojiao Jiang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-25
- DOI: Unavailable
- Categories: cs.AI, cs.DB, cs.IR
- Relevance: 2.9873416529472334
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.24273v2
- PDF: https://arxiv.org/pdf/2608.24273v2
- Local PDF: pdf/2026-08-27_11_Matched Excess-Outranker Regularization for Candidate-Set Interference in Continual Knowledge Graph Embedding.pdf

Continual knowledge graph embedding updates entity and relation representations as a graph grows. Existing methods primarily address catastrophic forgetting, but entity admission also changes the candidate universe of every compatible query. A historical answer can therefore lose rank even when its score and its ordering among old entities are preserved. We formalize this effect as candidate-set interference and introduce Matched Excess-Outranker Regularization (MEOR), a host-level objective that compares smooth answer-relative newcomer pressure with score-blind, structurally matched old references. Its one-sided penalty acts only when newcomer competition exceeds the matched reference, preserving the host learner's signal for legitimate new entities. Across eight paired runs on ENTITY-ComplEx, MEOR improves historical current-universe mean reciprocal rank (MRR) by 0.0057 over replay and reduces candidate-set interference by 0.0055, with one-sided 95% lower bounds of 0.0052 and 0.0051, respectively. It satisfies the preservation criteria for old-universe ranking and newcomer acquisition and improves historical current-universe MRR over persistent calibration, matched maximum regularizer (MMR), and unmatched old regularizer (UOR). Direct ablations support each component of its reference construction and aggregation. Adding MEOR also improves historical ranking in all ten reported FBInc-S and FBInc-L host and backbone settings, with every paired 95% confidence interval excluding zero. These results establish candidate admission as a distinct source of continual rank loss and show that it can be controlled without replacing the underlying embedding architecture or continual learner.

## 12. Renormalization Group Flow Matching for Scalable Local Generative Modeling

- Authors: Kanta Masuki, Yuto Ashida
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-24
- DOI: Unavailable
- Categories: cs.LG, cond-mat.stat-mech
- Relevance: 2.9629963607841914
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.23696v1
- PDF: https://arxiv.org/pdf/2608.23696v1
- Local PDF: pdf/2026-08-27_12_Renormalization Group Flow Matching for Scalable Local Generative Modeling.pdf

Despite their remarkable success in modeling complex data, generative models face a fundamental tradeoff. Global approaches can capture full structural coherence but suffer from high computational costs, while local models are efficient but often fail to reproduce long-range correlations and global coherence. The renormalization group (RG) bridges this gap by seamlessly connecting spatial structures across different length scales, retaining quasi-local descriptions at each step while preserving long-range correlations. We introduce renormalization group flow matching (RGFM), a generative framework that systematically structures data generation across different spatial scales. By using an exact RG flow as the probability path, RGFM progressively generates data from long- to short-wavelength structures. To reconcile scalability with global structure, we exploit two key properties of the RG: quasi-locality and scale separation. We rigorously show that the RGFM probability flow can be accurately approximated by local velocity fields acting over a spatial range $O(Λ^{-1}[\ln L+\ln(1/\varepsilon)])$ for RG wavenumber scale $Λ$, linear system size $L$, and prescribed error tolerance $\varepsilon$. This property enables local generative modeling with patches of size $O(\ln L)$ and a computational cost that scales nearly linearly with the system volume. We numerically demonstrate that local RGFM reproduces long-range correlations far beyond its receptive field in representative one-dimensional distributions, while conventional local flow matching exhibits substantial errors at long distances. On FFHQ images, RGFM yields far more coherent and higher-quality samples than local flow matching at 64x64 and 256x256. Our results establish RG-guided probability flows as a promising route toward scalable generative modeling that captures long-range structure using only local computation.

## 13. FlowNeg: GFlowNet-Guided Diverse Hard Negative Sampling for Knowledge Graph Embedding

- Authors: Ibne Farabi Shihab, Naoshin Anzum Hridi, Joyanta Jyoti Mondal
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-24
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 2.958095013201797
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.23849v1
- PDF: https://arxiv.org/pdf/2608.23849v1
- Local PDF: pdf/2026-08-27_13_FlowNeg_ GFlowNet-Guided Diverse Hard Negative Sampling for Knowledge Graph Embedding.pdf

Negative sampling determines whether a knowledge graph embedding (KGE) model learns from informative counterexamples or wastes updates on implausible corruptions. Uniform negatives are diverse but easy, whereas hard-negative miners concentrate on few entities and collide more with held-out positives. We introduce FlowNeg, a context-conditioned hierarchical generative flow network that amortizes reward-proportional sampling without normalizing a composite reward over the entity set: given a positive triple and corruption side, it selects a type, then an entity. Its terminal reward combines bounded model-based hardness with a training-only structural score for held-out-positive collision, over a relation-specific type-compatible support. We derive the reward, specialize standard trajectory balance, and bound multiplicatively how residual imbalance perturbs terminal and mode probability. Across a descriptive five-seed grid of five architectures and five benchmarks, FlowNeg has higher mean MRR than EMU and than IF-NS in 24 of 25 cells ($+0.0172$ and $+0.0160$ on average). A separate 15-seed FB15k-237/RotatE control fixing negative count, diagnostic budget, and compute gives FlowNeg $0.359\pm0.001$ MRR against $0.346\pm0.002$ for EMU, with near-uniform fixed-partition diversity, high gradient informativeness, and low collision. The evidence supports mode-covering negative generation without treating structural similarity as an open-world truth oracle.

## 14. A Multimodal Foundation Model for Longitudinal Patient Representation and Scalable Insight Generation in Oncology

- Authors: Eugene Vorontsov, Yi Kan Wang, Alican Bozkurt, Adam Casson, Ludmila Tydlitatova, Michal Zelechowski, Ezra E. W. Cohen, Jyoti D. Patel, Max Banaszak, Caitlin McWilliams, Shane Colley, Kate Sasser, Ryan Fukushima, Eric Lefkofsky, Razik Yousfi, Siqi Liu
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-25
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 2.9485637357298766
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.24688v1
- PDF: https://arxiv.org/pdf/2608.24688v1
- Local PDF: pdf/2026-08-27_14_A Multimodal Foundation Model for Longitudinal Patient Representation and Scalable Insight Generation in Oncology.pdf

Precision oncology necessitates a longitudinal model of patient state that captures cancer evolution and treatment over time, integrating multimodal observations. We introduce the oFM, a foundation model developed on a real-world oncology cohort of 1.67 million cancer patients that integrates clinical trajectories with DNA, RNA, and H&E pathology. Patient-level partitions were reserved for training, validation, and testing, with over one million patients used for training. The oFM encodes daily clinical and molecular episodes and, along with pathology images, integrates them over time to produce a patient state embedding. We evaluate frozen oFM embeddings against expert-curated clinical and molecular baseline features. In prognostic benchmarks, the oFM improved AUC for treatment response, progression-free survival, and overall survival (0.774 vs. 0.563 for overall survival). Across 11 comparative-treatment cohorts, the oFM embeddings achieved a three-fold higher pooled and scale-normalized treatment-benefit AUTOC than baseline features with improved benefit ranking in 9 of 11 cohorts, and provided stronger prognostic discrimination within both treatment arms. We also evaluated a mechanism discovery framework that interprets downstream models built on oFM embeddings by linking their predicted outcomes to clinically and biologically grounded mechanisms through an evidence-grounded temporal graph, enabling evaluation in clinical and drug-development applications.

## 15. Tissue‐Agnostic Cellular Morphometric Biomarkers for Risk‐Adapted Management Across Gastrointestinal Precancerous Lesions and Cancers

- Authors: Pin Wang, Chengfei Jiang, Aiqin Mao, Qi Sun, Yijun Lu, Jingjing Wei, Jamie L. Inman, S Celniker, Antoine M. Snijders, David W. Threadgill, Allan Balmain, Bo Hang, Hang Chang, Lei Wang, Jian‐Hua Mao
- Source: openalex
- Venue type: journal
- Journal: Advanced Science
- Publication status: published
- Publication date: 2026-08-25
- DOI: https://doi.org/10.1002/advs.77353
- Categories: Single-cell and spatial transcriptomics, Cancer Cells and Metastasis, Cancer Immunotherapy and Biomarkers
- Relevance: 2.928256465429842
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://doi.org/10.1002/advs.77353
- PDF: Unavailable
- Local PDF: Not downloaded

While precision oncology increasingly adopts tissue-agnostic paradigms, current strategies remain heavily reliant on molecular alterations, with limited relevance to early-stage cancers and precancerous lesion management. Here we present an unsupervised and interpretable artificial intelligence framework that defines tissue-agnostic cellular morphometric biomarkers (CMBs) capturing conserved tumor microenvironment (TME) architectures associated with cancer progression across gastrointestinal (GI) organs. Discovered from colorectal cancer whole-slide images and validated in gastric and esophageal malignancies within a multi-center cohort of 2,602 patients, a 13-CMB signature demonstrates robust cross-GI tissue transferability and prognostic impact. Importantly, beyond prognostic value in pan-GI cancers, the 13-CMB signature enables risk stratification of precancerous lesions and early-stage cancers, addressing a key unmet need in clinical decision-making where molecular profiling is often impractical or insufficient. The CMB-based risk scores support risk-adapted management, including individualized surveillance intervals and tailored intervention strategies. Integrative analyses using bulk and single-cell RNA sequencing and immunohistochemistry profiling show that CMBs correspond to biologically interpretable morphological states of the TME, including immune-excluded and stromal-dominant architectures. Together, this study establishes a biologically transparent, tissue-agnostic CMB framework that links conserved TME organization to clinically actionable risk assessment, providing a scalable approach for early cancer management and precision oncology.

## 16. Generalization, memorization, and overfitting for diffusion models trained in the lazy high-dimensional regime

- Authors: Hugo Latourelle-Vigeant, Sinho Chewi, Aram-Alexandre Pooladian, John Sous, Theodor Misiakiewicz
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-25
- DOI: Unavailable
- Categories: stat.ML, cs.LG, math.ST
- Relevance: 2.923487773424803
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.23938v1
- PDF: https://arxiv.org/pdf/2608.23938v1
- Local PDF: pdf/2026-08-27_16_Generalization, memorization, and overfitting for diffusion models trained in the lazy high-dimensional regime.pdf

Modern score-based generative models have achieved remarkable empirical success in high-dimensional tasks such as image, audio, and video synthesis. These models reduce distribution learning to a sequence of regression problems that, if solved exactly on finite data, would ultimately reproduce the training samples. Their ability to generalize must therefore arise from the implicit or explicit regularization during training. In this work, we develop a generative counterpart to the theory of benign overfitting and algorithmic regularization for overparameterized neural networks in the supervised lazy-training regime. We study denoising score matching in a vector-valued reproducing kernel Hilbert space with an inner-product kernel. In the proportional high-dimensional regime $n\asymp d$, we derive exact risk trajectories under gradient flow training. These trajectories exhibit three phases governed by qualitatively distinct estimators: a spectral estimator that generalizes, a pure-noise score with localized peaks that interpolate the training objective, and an empirical Bayes estimator that memorizes the data. We then analyze how these estimators combine along the reverse-time SDE and characterize the distribution of the resulting samples. The analysis reveals familiar mechanisms from supervised learning, including kernel linearization and self-induced regularization from the nonlinear part of the kernel, but also reveals a distinct phenomenology specific to generative modeling.

## 17. A Theory of Speciation in Generative Diffusion Models on Compact Riemannian Manifolds

- Authors: Alessio Marta, Paola Causin
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-24
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 2.9231491184196132
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.23798v2
- PDF: https://arxiv.org/pdf/2608.23798v2
- Local PDF: pdf/2026-08-27_17_A Theory of Speciation in Generative Diffusion Models on Compact Riemannian Manifolds.pdf

Speciation in generative diffusion models denotes the emergence of distinct stable branches during denoising, through which initially undifferentiated trajectories progressively commit to different data classes. In this work we develop an intrinsic theory of speciation for diffusion models supported on compact Riemannian manifolds: the aim is to go beyond existing theoretical descriptions, which usually identify speciation with a symmetric pitchfork bifurcation and assume to work in a large-dimensional space. We characterize speciation by bifurcations of the critical points of the evolving probability density. A spectral heat-kernel representation makes explicit the role of the manifold geometry, while Poincaré-Hopf and Morse theory impose global constraints on the number and type of score equilibria and reveal topologically-imposed geometrical modes. For mixtures of heat kernels, we prove that generic speciation events have a one-dimensional critical kernel and admit an A2 fold normal form; pitchforks and simultaneous multidirectional transitions arise from nongeneric symmetric configurations. We derive geometry-dependent estimates of speciation times for bimodal mixtures and Riemannian regular simplices. We further establish structural stability of nondegenerate folds under score perturbations and show that the first-order time shift is determined solely by the component of the score error along the critical direction. The theory is illustrated on the sphere using mixtures of von Mises-Fisher distributions, where pitchfork and saddle-node bifurcations, topological modes, and hierarchical multiple speciations are observed. Finally, a chart-based intrinsic score-learning scheme based on neural networks contrasts the theoretically predicted transitions on prototypal and more complex datasets.

## 18. Scalable and Versatile Identification for Hierarchical Structural Causal Models: A New Look at Project STAR

- Authors: Janis Aiad, Aghiles Drali, Aymen El Ouadrhiri, Anass Ettahiri, Yasser Oufqir, Simon Patry, David Cortes, Marianne Clausel, Emilie Devijver
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-25
- DOI: Unavailable
- Categories: stat.ML, cs.AI
- Relevance: 2.919902535594173
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.24500v1
- PDF: https://arxiv.org/pdf/2608.24500v1
- Local PDF: pdf/2026-08-27_18_Scalable and Versatile Identification for Hierarchical Structural Causal Models_ A New Look at Project STAR.pdf

The STAR (Student-Teacher Achievement Ratio) experiment (1985, Tennessee, USA) is a landmark hierarchical dataset designed to assess the impact of class size on student outcomes, with observations nested within classes. To encode class-level interventions in such hierarchical settings, we develop a complete, scalable, open-source pipeline for Hierarchical Structural Causal Models (HSCM) that bridges symbolic identification and practical estimation. Our approach integrates graph transformations, pyAgrum's do-calculus for automatic identification of causal effects, adaptation of symbolic expression into closed-form HSCM formulas, and numerical estimation from fitted local probability models. A key innovation is our adapted Abstract Syntax Tree (AST), which decomposes pyAgrum's identified formulas into independent density, expectation, and marginalization tasks, enabling parallel and scalable computation. We validate the pipeline on canonical HSCM motifs and benchmark scenarios with known ground truth, then apply it to STAR kindergarten mathematics outcomes. The results show that flat baselines (ignoring hierarchy) recover associations but fail to encode class-level interventions, and that symbolic identification alone is not enough for practical Hierarchical Structural Causal inference; scalable estimation and numerical stability checks are central parts of the scientific object.

## 19. Incorporating Cognitive Load and Knowledge Transfer for Multi-Domain Knowledge Tracing

- Authors: Haotian Zhang, Shucun Wang, Jinze Wu, Liang Ding, Shuochen Liu, Zhenya Huang, Jing Sha, Shijin Wang, Qi Liu
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-25
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 2.899208165130125
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.24005v1
- PDF: https://arxiv.org/pdf/2608.24005v1
- Local PDF: pdf/2026-08-27_19_Incorporating Cognitive Load and Knowledge Transfer for Multi-Domain Knowledge Tracing.pdf

Knowledge Tracing (KT) aims to assess students' dynamic knowledge states from their learning histories. While most existing KT methods focus on single-domain learning with notable success, real-world learning scenarios often involve multiple domains simultaneously, introducing two critical factors: 1) Cognitive load, arising from managing learning across domains in both temporal and knowledge dimensions. 2) Knowledge transfer, where knowledge states in one domain influence related states both within and across domains. In this paper, we focus on exploring these factors to improve students' knowledge state assessment in multi-domain learning scenarios and propose a novel method incorporating cognitive Load and knowledge Transfer for Multi-domain Knowledge Tracing (LT-MKT). Specifically, to bridge isolated domains, LT-MKT first integrates textual information from questions and their associated concepts to construct a Multi-domain Hierarchical Graph, leveraging the advanced representational capabilities of large language models (LLMs). Then, cross-domain features in both the temporal and knowledge dimensions are explicitly modeled to capture the effects of cognitive load. Additionally, a knowledge transfer module is designed to model the propagation of knowledge states within and across domains. By jointly modeling these factors, LT-MKT enables more accurate prediction of students' future performance. Finally, extensive experiments on real-world datasets demonstrate that our method achieves state-of-the-art performance.

## 20. Compression Trinity: Exploring Sparsity, Quantization, and Low-Rank Approximations for LLM Compression

- Authors: Mohammad Mozaffari
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-25
- DOI: Unavailable
- Categories: cs.AI, cs.DC, cs.LG, cs.PF
- Relevance: 2.8803572634574093
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.24070v1
- PDF: https://arxiv.org/pdf/2608.24070v1
- Local PDF: pdf/2026-08-27_20_Compression Trinity_ Exploring Sparsity, Quantization, and Low-Rank Approximations for LLM Compression.pdf

Prohibitive computational and environmental costs impede the scalable deployment of Large Language Models (LLMs). Traditional compression techniques (sparsity, quantization, low-rank approximations) are typically applied in isolation, and each hits an accuracy-efficiency wall. This thesis proposes the "Compression Trinity," a unified framework that applies the three pillars jointly: sparsity to reduce computation, quantization to minimize memory bandwidth, and low-rank approximations to recover accuracy. To accelerate pretraining, we apply the Trinity to the optimizer and model architecture. MKOR approximates curvature via block-diagonal sparsity and low-rank inversion, maintaining numerical stability for quantized states; it reduces curvature update complexity from $O(d^3)$ to $O(d^2)$ and accelerates convergence by up to 1.85x over KFAC. SLoPe accelerates training by up to 1.25x via a double-pruned backward pass for N:M sparsity, using low-rank "lazy" adapters in the final 1% of training to recover accuracy. For post-training compression, OPTIMA stabilizes static masks in a zero-training regime by formulating weight reconstruction as globally optimal column-wise quadratic programs, improving zero-shot accuracy by up to 3.97%. Given a fine-tuning budget, PATCH breaks the ceiling of static masks by learning a dynamic hybrid sparsity ratio between 0% and 50%, yielding up to 1.38x speedups. Finally, SLiM realizes the full Compression Trinity in one shot, using mathematically derived low-rank adapters to recover information lost to quantization and sparsity, improving accuracy by up to 5.66% over state-of-the-art methods and outperforming uncompressed dense models at equal parameter budgets by 0.6%. Together, these results show that jointly applying the Compression Trinity is essential for efficient, scalable, high-performance LLMs.

## 21. Automata from Agent Traces: Failure and Next-Step Prediction

- Authors: Seonglae Cho, Franklin Cardenoso Fernandez, Umar Mohammed, Zekun Wu, Kleyton Da Costa, Ilham Wicaksono, Adriano Koshiyama
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-24
- DOI: Unavailable
- Categories: cs.AI, cs.CL, cs.LG
- Relevance: 2.8768536185621785
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.23670v1
- PDF: https://arxiv.org/pdf/2608.23670v1
- Local PDF: pdf/2026-08-27_21_Automata from Agent Traces_ Failure and Next-Step Prediction.pdf

LLM-based agents execute multi-step tasks, but their behavioral structure remains opaque: long unstructured traces resist the safety auditing and runtime monitoring that deployment requires. Existing approaches operate per-trace or success-only, so they miss the cross-run topology that links next-step and failure prediction. To recover that shared structure, we collapse an entire trace corpus into a single, compact finite-state machine (FSM) that serves as a structural substrate for the otherwise unpredictable behavior of LLM agents. Across twelve public datasets, the FSMs are compact (7-43 states), replay held-out data at >=0.997 fitness with near-identical topology across splits, and build in milliseconds. This substrate addresses both prediction goals. For next-step prediction, FSM-state context outperforms Agent Workflow Memory on every ground-truth-matched dataset. For failure prediction, per-state behavioral features reach held-out AUROC up to 0.94, and an online monitor ranks failing runs above passing ones from a partial trace, triggering early stopping well before completion. Behavioral topology thus appears shaped more by the deployment harness than by the LLM, providing a model-agnostic structural primitive for safety auditing and runtime monitoring.

## 22. VisCache: Visual KV Cache Pruning for Efficient Vision Large Language Model Inference

- Authors: Lyuke Wang, Zhuo Li, Guangxu Zhu
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-25
- DOI: Unavailable
- Categories: cs.CV, cs.AI
- Relevance: 2.8692358105554794
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.24063v1
- PDF: https://arxiv.org/pdf/2608.24063v1
- Local PDF: pdf/2026-08-27_22_VisCache_ Visual KV Cache Pruning for Efficient Vision Large Language Model Inference.pdf

While Vision Large Language Models (VLLMs) have achieved remarkable success in multimodal reasoning, their long-context inference remains prohibitively expensive due to the massive computation and memory overhead of visual Key-Value (KV) caches. Existing KV compression methods often apply uniform pruning across visual tokens and layers, leading to substantial information loss and degraded performance.To address this challenge, we propose \textbf{VisCache}, a plug-and-play framework for coarse-to-fine \textbf{Vis}ual KV \textbf{Cache} pruning without training, which consists of two synergistic stages. First, a lightweight VLM filters temporal redundancy by selectively forwarding semantically informative keyframes. Second, we introduce {PruneKV}, a surgical KV compression algorithm tailored to the attention dynamics of VLLMs. Unlike rigid pruning strategies, PruneKV adopts a parabolic layer-wise budget allocation together with an asymmetric update mechanism that selectively prunes keys while fusing values, thereby preserving critical contextual information. Extensive experiments demonstrate that VisCache substantially improves inference efficiency, achieving up to {2.35$\times$ speedup} and significant memory reduction while maintaining competitive performance with only {19--28\%} KV cache retention. VisCache consistently outperforms existing baselines, establishing a new Pareto frontier between efficiency and performance for long-context VLLM inference. Code is available at https://github.com/Wlklk/VisCache

## 23. Data Mixing as Mixture Experiment: Response Surface Methodology and Optimal Design for Large Language Model Pretraining

- Authors: Yicheng Mao, Hongru Du
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-24
- DOI: Unavailable
- Categories: cs.AI, stat.ML
- Relevance: 2.8507991034207416
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.23922v1
- PDF: https://arxiv.org/pdf/2608.23922v1
- Local PDF: pdf/2026-08-27_23_Data Mixing as Mixture Experiment_ Response Surface Methodology and Optimal Design for Large Language Model Pretraining.pdf

Data mixing is a central design problem in large language model pretraining: given a fixed token budget, practitioners must decide how much data to allocate to each domain. Recent proxy-based methods address this problem by training small models on candidate mixtures, fitting a response model, and using the response to select mixtures for larger-scale training. We show that this workflow has the structure of a classical mixture experiment. Under this view, data domains are mixture components, token shares are component proportions, proxy-training runs are experimental design points, and validation loss defines a response surface over the probability simplex. We develop this formulation using sparse second-order Scheffé response-surface models and construct model-robust $\mathcal{I}$-optimal designs for proxy data-mixing experiments. Using RegMix as an empirical case study, we demonstrate how the framework can both interpret observed mixture responses and design more efficient proxy experiments. The Scheffé analysis shows that domain value is strongly relational: several domains that are weak under additive effects become favourable through pairwise interactions, especially through combinations with web-derived text. The sparse Scheffé model preserves mixture rankings across model scales and remains competitive with a flexible machine-learning predictor while providing an explicit decomposition of additive and interaction effects. In a simulation study calibrated to observed proxy-training responses, model-robust $\mathcal{I}$-optimal designs recover the relevant mixture ordering after removing about 25\% of the original proxy runs. These results suggest that LLM data mixing should be treated not only as a prediction problem, but also as an experimental-design problem in which the proxy mixtures themselves can be chosen to improve statistical efficiency.

## 24. Equivariant Cellular Sheaves for Molecular Electronic Structure: Bridging Sheaf Cohomology and E(3)-Equivariant Hamiltonian Learning

- Authors: Krishna Harish
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-06-14
- DOI: Unavailable
- Categories: cs.LG, physics.chem-ph
- Relevance: 2.849889048839832
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.23571v1
- PDF: https://arxiv.org/pdf/2608.23571v1
- Local PDF: pdf/2026-08-27_24_Equivariant Cellular Sheaves for Molecular Electronic Structure_ Bridging Sheaf Cohomology and E(3)-Equivariant Hamilton.pdf

Equivariant message-passing networks are the standard model for molecular property and interatomic-potential prediction, and recent work predicts the electronic Hamiltonian itself in an E(3)-equivariant way. Separately, topological deep learning has extended graph networks to cellular sheaves. Our central observation is structural: in a localized atomic-orbital basis, the molecular single-particle Hamiltonian, after a constant shift that makes it positive semidefinite, is the Laplacian of a cellular sheaf on a regular cell complex built from the molecule. Making the restriction maps O(3)-steerable two-center kernels from bond geometry recovers the Slater-Koster form as a special case and yields an E(3)- and permutation-equivariant operator. Three consequences follow. First, the zeroth sheaf cohomology H^0 = ker L is a topological invariant equal to the non-bonding (zero-mode) orbitals, recovering the classical alternant non-bonding-orbital count as a lower bound. Second, the Hodge 1-Laplacian lets higher cells (rings) carry cycle and delocalization information through H^1. Third, the model strictly generalizes E(3)-equivariant message-passing networks and CW networks, and inherits the anti-oversmoothing of non-trivial sheaf diffusion. We prove equivariance, expressivity, and cohomological-correspondence results for the Equivariant Cellular Sheaf Networks, and validate them numerically: the Hamiltonian-to-sheaf embedding is exact to machine precision, the cohomology dimension reproduces non-bonding-orbital counts across eleven conjugated molecules, the sheaf Laplacian is O(3)-equivariant to machine precision, and the equivariant model attains lower error and rotation generalization on a directional electronic target. Our contribution is this sheaf-theoretic formalization and its invariants, not equivariant Hamiltonian prediction itself.

## 25. From Causal Plausibility to Causal Reliability: Evaluating LLMs as Calibrated Direct Causal-Edge Classifiers

- Authors: Amit Kumar, Elnur Adl Zarabi, Suranjana Trivedy, Zhiqian Chen, Lei Zhang, Kaiqun Fu, Taoran Ji
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-24
- DOI: Unavailable
- Categories: cs.LG, cs.AI, stat.ME
- Relevance: 2.8426192023722097
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.23660v1
- PDF: https://arxiv.org/pdf/2608.23660v1
- Local PDF: pdf/2026-08-27_25_From Causal Plausibility to Causal Reliability_ Evaluating LLMs as Calibrated Direct Causal-Edge Classifiers.pdf

Large language models (LLMs) are increasingly used to provide prior causal knowledge for structural causal discovery, yet whether their direct-edge judgments and confidence can be trusted remains unclear. We systematically evaluate 12 instruction-tuned open-weight models across six benchmark causal graphs, five prompting strategies, and four confidence sources: verbalized, logit-based, cross-prompt agreement, and cross-model agreement. Under our language-only pairwise protocol, our evaluation yields three key findings. (i) LLM-based causal judgments are strongly recall-dominant: models predict overly dense graphs with many false-positive edges, while prompting mainly shifts the precision-recall trade-off rather than resolving overprediction. Gains from model scale diminish on the largest graphs and do not eliminate miscalibration. (ii) LLMs often capture causal relatedness without reliably identifying directness or orientation. Relative to published reference graphs, models misclassify 40.0% of indirect and 36.0% of reversed non-edges as direct edges, versus 28.2% of other non-edges. Moreover, 80.8% and 84.6% of these false positives receive verbalized confidence of at least 80%, revealing substantial overconfidence in structurally incorrect predictions. (iii) Conventional confidence estimates are unreliable, whereas agreement offers a more promising signal. Logit-based confidence frequently collapses near 1.0 regardless of correctness, while cross-prompt and cross-model agreement achieve better mean calibration and discrimination, though their advantages are not statistically significant after Holm correction. A benchmark-familiarity audit further identifies potential familiarity in five model-dataset pairs, all involving AsiaM. Overall, our results suggest LLMs are better viewed as sources of externally validated soft causal priors than as direct evidence of causal structure.

## 26. Evidence Blindness in Direct Corpus Interaction: Persistent Navigation with AtlasNav

- Authors: Hongyu Guo, Zhiyu Zheng, Zhao Cao
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-25
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 2.83009845107004
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.24764v1
- PDF: https://arxiv.org/pdf/2608.24764v1
- Local PDF: pdf/2026-08-27_26_Evidence Blindness in Direct Corpus Interaction_ Persistent Navigation with AtlasNav.pdf

Large language model agents are moving beyond conventional retrieval-augmented generation toward direct interaction with external corpora. Direct Corpus Interaction (DCI) keeps the full corpus accessible, yet reachable evidence can remain unusable under finite interaction budgets. Required evidence may fail to surface, a surfaced supporting document may remain unopened, or an opened document may fail to expose its decisive fragment. We call this progressive silent loss Evidence Blindness and quantify it through stage-wise evidence realization. Within the DCI paradigm, raw interaction adds little reusable corpus organization, while dynamic-workspace methods reconstruct a query-conditioned interaction space from each query and trajectory. In both cases, useful structure is recovered largely online. We instead formulate large-scale agentic search as finite-budget navigation over reusable corpus structure. We introduce AtlasNav, a persistent multi-view corpus-navigation framework that retains direct corpus interaction but organizes the corpus once into a Corpus Atlas, allowing each query to navigate adaptively rather than reconstruct shared structure. On BrowseComp-Plus, AtlasNav achieves 92.05% strict accuracy while reducing recorded online inference cost by 30.21% relative to the prior dynamic-workspace state of the art. Under matched budgets, it realizes the complete required evidence earlier and approaches the same model's evidence-supplied empirical reference more rapidly. The same representation principle remains effective under PhantomWiki's distinct corpus organization and controlled 10K-1M scaling, and transfers competitively to heterogeneous enterprise knowledge. These results show that agentic search depends not only on accessible evidence, but also on how the corpus is represented so that limited interaction becomes effective navigation.

## 27. Hybrid Semantic Tool Discovery for Enterprise MCP Gateway: Architecture and Implementation

- Authors: Olympia Saha, Amy Wang, Srinivasan Manoharan
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-25
- DOI: Unavailable
- Categories: cs.IR, cs.AI
- Relevance: 2.8276768098077194
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.23992v1
- PDF: https://arxiv.org/pdf/2608.23992v1
- Local PDF: pdf/2026-08-27_27_Hybrid Semantic Tool Discovery for Enterprise MCP Gateway_ Architecture and Implementation.pdf

Large language model (LLM) agents invoke external tools to retrieve and reason over information beyond pretrained knowledge. The Model Context Protocol (MCP) standardizes how such tools are surfaced, and a proxy MCP server aggregates many backend servers behind a single endpoint providing a secure, governable chokepoint for authentication, policy enforcement, and observability. This architecture creates two compounding challenges: a context-engineering bottleneck where full tool schemas saturate the model context window before any user query, and a tool discoverability barrier where users and agents cannot identify the best tool among 2,000+ indexed tools across 200+ MCP servers. Prompt caching reduces reprocessing cost but neither frees context capacity nor improves accuracy. We present SCOUT (Selective Context Optimization for Universal Tooling), which reframes tool exposure as a context-selection problem, injecting only tools relevant to the current step. SCOUT surfaces two MCP meta-tools -- tool_search and execute_tool -- where tool_search performs hybrid retrieval, fusing BM25 sparse matching with dense vector search via Reciprocal Rank Fusion to return the top-k relevant tools. Backed by zero-downtime catalog update pipelines, SCOUT resolves both context saturation and tool discovery challenges. In production at PayPal, SCOUT reduces MCP tool-token consumption from 140.2k tokens (70.1% of context) to 1.3k tokens (0.8%), a 99% reduction, cutting per-query inference cost at enterprise scale. Because SCOUT is surfaced as standard MCP tools, it is model-agnostic and requires no client-side modifications.

## 28. Diverse by Reasoning: Harnessing the Wisdom of LLM Crowds for Future Prediction

- Authors: Nirupam Chetlapalli, Yiming Liao, Min-Chun Chen, Keke Chen
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-25
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 2.7930737992540733
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.24001v2
- PDF: https://arxiv.org/pdf/2608.24001v2
- Local PDF: pdf/2026-08-27_28_Diverse by Reasoning_ Harnessing the Wisdom of LLM Crowds for Future Prediction.pdf

Large language models (LLMs) are increasingly used for future prediction, motivating the use of multiple models as a wisdom-of-the-crowd mechanism. However, simply increasing crowd size does not guarantee effective diversity, as different LLMs may exhibit redundant behaviors. We propose a behavior-aware framework for constructing diverse LLM crowds. The framework characterizes models using their reasoning traces on independent development tasks, clusters models by behavioral similarity, and selects representatives for collective prediction. We evaluate 25 LLMs using seven development benchmarks for behavioral diversity modeling and two future-prediction benchmarks for evaluating diverse crowds' performance. Our results show that crowd composition can matter more than crowd size: a three-model medoid crowd based on K-means++ behavioral clustering outperforms conventional voting over all 25 models on both prediction benchmarks, while reducing model calls by 88% and inference cost by approximately 80%. The results further suggest that representative behavioral diversity, rather than simply maximizing diversity, is important for constructing effective LLM crowds

## 29. PuzzleKV: Page-Wise Low-Rank Decomposition for KV Cache Compression

- Authors: Zizhong Wang, Jieying Wang, Zhao Zhang, Jiajia Li
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-24
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 2.7872424674117138
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.23843v1
- PDF: https://arxiv.org/pdf/2608.23843v1
- Local PDF: pdf/2026-08-27_29_PuzzleKV_ Page-Wise Low-Rank Decomposition for KV Cache Compression.pdf

Long-context inference in large language models (LLMs) is increasingly limited by the memory required for the key-value (KV) cache. KV cache compression addresses this problem by reducing the storage cost of previous tokens. Among existing approaches, low-rank compression is particularly attractive because it represents every token in reduced dimensions. Previous low-rank methods typically derive fixed projection spaces from model weights, construct fixed spaces from calibration activations, or construct a shared basis over a broad cache region. Such representations may not capture detailed but important information. We partition each per-head KV cache into fixed-length logical pages and observe substantial low-rank structure within individual pages. Based on this observation, we propose PuzzleKV, a training- and calibration-free method that treats each completed page as an independent compression unit. PuzzleKV decomposes pages within each layer and KV head, computes attention directly over dense and factorized pages, and incrementally compresses newly eligible pages during autoregressive decoding. Experiments across models, context lengths, and benchmarks demonstrate the effectiveness of PuzzleKV under matched storage budgets. At approximately 60% of the original KV cache storage, PuzzleKV achieves more than 96% of Full KV performance across both evaluated models and all benchmark settings, with substantial gains over Global SVD on RULER and competitive performance on LongBench. To achieve a more aggressive compression ratio, PuzzleKV can be further combined with quantization while retaining more than 93% of Full KV performance using only 18.7% of the original storage.

## 30. What Guides the Agent? Adjudicating Unauthorized Behavior via Localizing Behavior-Guiding Instructions

- Authors: Yichao Gao, Yumo Zhang, Yunhao Yao, Haohua Du, Puhan Luo, Ruiqi Li, Zhiqiang Wang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-25
- DOI: Unavailable
- Categories: cs.CR, cs.AI
- Relevance: 2.779699679166032
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.24022v1
- PDF: https://arxiv.org/pdf/2608.24022v1
- Local PDF: pdf/2026-08-27_30_What Guides the Agent_ Adjudicating Unauthorized Behavior via Localizing Behavior-Guiding Instructions.pdf

LLM agents integrated with external resources gain complex task capabilities, yet the unified natural-language context channel makes them vulnerable to injection attacks: untrusted external data may be dynamically parsed as behavior-guiding instructions during LLM inference, thereby subverting the agent's decision. Existing defenses focus on static detection or isolation of malicious content at the input/output level, remains insufficient for detecting such dynamic inducements that arise during model reasoning. We propose Attnlocate, a runtime framework for fine-grained localization of context spans that genuinely influence tool-calling decisions, i.e., behavior-guiding instructions. Attnlocate casts this localization problem as an object detection task, aiming to detect the distinctive activation traces induced by behavior-guiding instructions within the attention matrix. Specifically, we design a multi-head, multi-layer attention aggregation scheme to construct a token-level feature space tailored for object detection. Then, a 1-D U-Net equipped with an anchor-free detection head is deployed to detect these spans. Finally, based on the authority of the provider from which the detected behavior-guiding spans originate, Attnlocate dynamically adjudicates malicious invocation attempts. We evaluate Attnlocate across ten agent configurations from five LLM families, covering scenarios involving indirect prompt injection and tool poisoning. Attnlocate achieves a mean IoU of 0.743, an average AUROC of 0.956, and a 0.934 true-positive rate at 0.067 false-positive rate. It also transfers effectively across unseen models and supports authority policy adaptation without retraining.
