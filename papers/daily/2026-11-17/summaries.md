# Paper Daily Reading - 2026-11-17

## 1. More Genes, Faster Inference: Efficient Large-Panel Spatial Transcriptomics Prediction from Histology

- Authors: Songming Zhang, Yuxiao Luo, Shifu Luo, Siran Chen, Shuquan Su, Jinyan Li
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-13
- DOI: Unavailable
- Categories: cs.CV, cs.AI, q-bio.QM
- Relevance: 3.720149598200896
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.17899v1
- PDF: https://arxiv.org/pdf/2611.17899v1
- Local PDF: pdf/2026-11-17_01_More Genes, Faster Inference_ Efficient Large-Panel Spatial Transcriptomics Prediction from Histology.pdf

Spatial transcriptomics (ST) prediction from histology aims to infer spatially resolved gene expression profiles directly from tissue images. This is a challenging problem that is currently often addressed with complicated model architectures, additional inputs, and complicated training procedures, while remaining limited to fixed, small gene panels. This raises a natural question: Is there an efficient method for large-panel ST prediction? Here, we present GeneFlow, a simpler yet effective framework for large-scale spatial gene expression prediction that unifies flow-matching generative modeling with structured multimodal fusion. Specifically, GeneFlow first encodes both histological morphology and cross-gene interactions in spatial spots through histology and gene tokenizers. The model directly predicts spatial gene expression, rather than an intermediate velocity field, while being trained with a velocity-based flow-matching objective. We show that, even without relying on heavy generative pipelines, GeneFlow achieves state-of-the-art performance across multiple ST benchmarks, with up to 56.8% gains in 1,000-gene prediction. Extensive experiments further show that GeneFlow produces biologically meaningful spot profiles while reducing computational cost by orders of magnitude, thereby improving efficiency and scalability, particularly in clinical settings. We believe GeneFlow provides an opportunity for leveraging widely available histology images for downstream biological discovery. Code is available at: https://github.com/ZZhangsm/GeneFlow

## 2. Dancing Tokens on the Vocabulary Network from LLM Generation

- Authors: Yuan-Chao Hu
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-13
- DOI: Unavailable
- Categories: cs.AI, cond-mat.dis-nn
- Relevance: 3.505649927065693
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.18248v1
- PDF: https://arxiv.org/pdf/2611.18248v1
- Local PDF: pdf/2026-11-17_02_Dancing Tokens on the Vocabulary Network from LLM Generation.pdf

Large language models (LLMs) generate text one token at a time, yet how a particular generation relates to the geometry learned in pre-training remains unclear. The fundamental explainability of LLMs is elusive. Here, we build a similarity network from the input embeddings of six open LLMs and map generation onto it. The token-embedding network is scale-free while heavy-tailed, as are random embeddings with matched covariance, but far more fragmented. Distillation barely changes this topology because input embeddings are largely inherited. The knowledge space is thus deterministic from pre-training. Consecutive generated tokens are rarely graph neighbours and, in most models, no more often than in shuffled order, so generation is not a walk on the predefined network, although the tokens it visits are concentrated within it. Through the logit lens in a layer- wise manner, tokens settle late in depth in most models, and repetitive models remain confined to small domain-specific sub-graphs. These observables could serve as inference-time monitors of degeneration. We thus provide a fresh perspective on understanding LLM generation in the microscopic way from node or link prediction by graph learning.

## 3. Efficient and Practical Clustering of Variables in Causal Graphs

- Authors: Otto Tabell, Jani Nykänen, Santtu Tikka, Juha Karvanen
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-13
- DOI: Unavailable
- Categories: stat.ML, cs.LG, stat.ME
- Relevance: 3.388573627937572
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.17971v1
- PDF: https://arxiv.org/pdf/2611.17971v1
- Local PDF: pdf/2026-11-17_03_Efficient and Practical Clustering of Variables in Causal Graphs.pdf

Clustering variables in a graph may improve visual clarity and simplify causal inference. Harnessing the full potential of clustering requires an automated method to detect useful clusters in a graph. We introduce a novel class of clusters called conduits, and present a sound, complete and efficient algorithm for detecting all conduits in the graph. In addition to algorithmic detectability, conduits appear naturally in causal graphs stemming from real-world applications, enabling substantial size reduction. Furthermore, the structure of conduits enables the application of known identifiability results regarding clustering. We demonstrate these properties in a simulation study with real-world graphs.

## 4. Experts Across Schemas: Agent-Guided Mixture-of-Relational-Experts for Cross-Database Generalization

- Authors: Hiren Madhu, Sukanta Ganguly, Kiran Srinivasan, Smita Krishnaswamy, Rex Ying
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-13
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 3.2991926046909867
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.18315v1
- PDF: https://arxiv.org/pdf/2611.18315v1
- Local PDF: pdf/2026-11-17_04_Experts Across Schemas_ Agent-Guided Mixture-of-Relational-Experts for Cross-Database Generalization.pdf

Web platforms record user and item activity in relational databases whose schemas differ from platform to platform, which makes it difficult to transfer predictive models between them. Relational foundation models address this through cross-database pretraining, yet recent improvements have relied on increasingly large pretraining corpora. We ask whether a better architecture, together with features specific to the target database, can deliver comparable gains from far less pretraining data. We introduce MoREGT, a mixture-of-relational-experts graph transformer that represents both rows and cells as tokens, adds the log-ages of rows and the names of foreign-key relationships to attention, and routes cells and rows to experts by column metadata rather than by values. A label-blind LLM agent complements the model: it reads the target database's schema and column statistics and adds validated single-row derived columns, without access to labels or model scores. On 21 RelBench tasks with leave-one-database-out pretraining on six databases, the MoREGT backbone improves on the Relational Transformer pretrained on the same databases by 2.25 points of mean AUROC and 5.83 points of mean nMAE. The agent's columns raise mean AUROC from 78.45 to 79.63 and lower mean nMAE from 27.91 to 26.98, the highest means on both metrics among the compared methods, including RT-J, which pretrains on about 400 times as many databases.

## 5. Distilling Transformers: A Survey

- Authors: Jianping Gou, Liyuan Sun, Baosheng Yu, Philip H. S. Torr, Ming-Hsuan Yang, Dacheng Tao
- Source: openalex
- Venue type: journal
- Journal: IEEE Transactions on Pattern Analysis and Machine Intelligence
- Publication status: published
- Publication date: 2026-11-06
- DOI: https://doi.org/10.1109/tpami.2026.3751310
- Categories: Advanced Neural Network Applications, Domain Adaptation and Few-Shot Learning, Topic Modeling
- Relevance: 3.178820557712365
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://doi.org/10.1109/tpami.2026.3751310
- PDF: Unavailable
- Local PDF: Not downloaded

Transformers have gained widespread recognition across sectors and academic fields for their innovative self-attention mechanism, which effectively captures long-range dependencies, and for their scalability and exceptional performance across diverse applications. However, their high computational cost and time requirements limit their adoption in resource-constrained environments. Knowledge distillation provides a straightforward yet effective approach for compressing traditional network architectures, such as CNNs, by transferring knowledge from a large teacher model to a smaller student model. This paper explores the potential for model compression by combining novel Transformer architectures with knowledge distillation. Specifically, we categorize, summarize, and present the substantial body of work on Transformer knowledge and distillation schemes. Furthermore, this survey extends its coverage to widely used knowledge-distillation pipelines for large language models (LLMs) and systematically analyses six major distillation targets. We also review popular applications in various domains, including natural language processing, computer vision, and speech recognition. Finally, we provide forward-looking perspectives, highlighting potential directions for future research on developing highly efficient yet performance-competitive Transformer models through knowledge distillation techniques.

## 6. Interpretable weight-space programming builds transparent transformers and brain encoding models

- Authors: Yash Mehta, Chandan Singh, Weijia Xu, Richard J. Antonello, Adeen Flinker, Nima Mesgarani, Michael F. Bonner, Nebojsa Jojic, Jianfeng Gao
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-13
- DOI: Unavailable
- Categories: cs.CE, cs.AI
- Relevance: 3.168332959656243
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.18114v1
- PDF: https://arxiv.org/pdf/2611.18114v1
- Local PDF: pdf/2026-11-17_06_Interpretable weight-space programming builds transparent transformers and brain encoding models.pdf

Neural networks are powerful predictors, yet their opacity limits their usefulness in science, where the goal is explanation rather than mere prediction. In neuroscience, for example, deep encoding models accurately predict brain activity in response to natural stimuli, but struggle to reveal which stimulus features drive those predictions. Here we introduce interpretable weight-space programming (iWSP), a method in which an LLM agent iteratively builds interpretable models by explicitly programming their weights and features in code, without gradient-based training (backpropagation). Without backpropagation to tune parameters, the agent must draw on its prior knowledge and reason over previous trials to hypothesize, hand-craft, and refine human-interpretable computations mirroring the workflow of a human scientist. LLM audits confirm the interpretability of the hand-crafted models. We first validate iWSP by tasking it with constructing transformers for canonical benchmarks such as arithmetic and sentiment classification, finding that LLM agents can successfully craft compact, accurate networks directly. Next, we apply iWSP to build neural encoding models across vision, language, and audition. In the visual cortex, iWSP outpredicts existing interpretable baselines, uncovers distinct computations across early/higher visual areas, and generalizes to unseen data. In language fMRI, iWSP surfaces a confound in the data and in auditory ECoG, it systematically discovers interpretable acoustic features that predict neural activity. Together, these results establish iWSP as a general paradigm for aligning high predictive performance with human-interpretable scientific discovery.

## 7. JaRS: Contrast-Free Localization of Memorized Regions in Diffusion Models via Jacobian Row Sums

- Authors: Saisuchith Mahajan, Aditey Nandan, Rohit Singh, Nishanth Shetty, Chandra Sekhar Seelamantula
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-13
- DOI: Unavailable
- Categories: cs.CV, cs.LG
- Relevance: 3.1478368948987345
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.18024v1
- PDF: https://arxiv.org/pdf/2611.18024v1
- Local PDF: pdf/2026-11-17_07_JaRS_ Contrast-Free Localization of Memorized Regions in Diffusion Models via Jacobian Row Sums.pdf

Diffusion models sometimes memorize and reproduce regions of their training images, raising privacy and copyright concerns. We aim to localize these regions. Existing contrast-based methods use the diagonal of the denoiser Jacobian, which reflects the posterior variance of each pixel. However, a small diagonal entry is ambiguous: it signals either memorization or averaging over many neighboring pixels in smooth or predictable regions. To resolve this ambiguity, these methods subtract a reference map, which requires a second evaluation with a null prompt or an earlier checkpoint. Unconditional models have no null prompt, and earlier checkpoints are unavailable in general. We show that Jacobian row sums (JaRS), unlike the diagonal, separate memorization from local averaging without a reference map. Pairing JaRS with an image-level detection score that uses the same statistic at an early denoising step yields JaRS+. Across Stable Diffusion v1.4 and v2.1, Realistic Vision v5.1, and an unconditional diffusion Transformer (DiT), JaRS+ outperforms contrast-based localization methods.

## 8. Training-Free Acceleration of Multi-View 3D Transformers via Regime-Aware Attention Approximation

- Authors: Muhammed Izzet Sezer, Sevval Belkis Dikkaya
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-13
- DOI: Unavailable
- Categories: cs.CV, cs.AI
- Relevance: 3.103427563326039
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.17629v1
- PDF: https://arxiv.org/pdf/2611.17629v1
- Local PDF: pdf/2026-11-17_08_Training-Free Acceleration of Multi-View 3D Transformers via Regime-Aware Attention Approximation.pdf

Multi-view 3D transformers such as VGGT reconstruct a scene from a set of unposed images in a single forward pass, predicting camera poses, depth and 3D points, but the cost of their global attention grows quadratically with the num- ber of images. Accelerators borrowed from large language models assume that each token attends to only a few oth- ers; on these models they lose accuracy or gain little speed. We study the global attention of three multi-view transform- ers on seven datasets and find that every layer plays one of three roles: it averages over the whole scene, matches points across many images, or anchors on the first image, whose coordinates the outputs use. Building on this anal- ysis, we propose Regime-AWare ATTention Approximation (RAWATTA), a training-free method that runs attention in 8- bit precision and keeps 16-bit precision only in the layers where a worst-case calibration check requires it. Its fast set- ting, RAWATTA-Fast, also approximates attention in a few averaging and anchoring layers, while matching layers and the first image keep all their keys. On a 12 GB GPU at 50 im- ages, RAWATTA runs VGGT faster than the released code, mostly through our CUDA engine, and loses at most about one point of pose accuracy (AUC@3) on any dataset; RAWATTA-Fast is slightly faster and less accurate. Both fit 200 images, where the released code runs out of memory at 100.

## 9. Contrastive latent representation learning with denoising score matching

- Authors: Christopher Marouani, Grigory Bartosh, Christian A. Naesseth
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-13
- DOI: Unavailable
- Categories: stat.ML, cs.LG
- Relevance: 3.0807491788153567
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.18469v1
- PDF: https://arxiv.org/pdf/2611.18469v1
- Local PDF: pdf/2026-11-17_09_Contrastive latent representation learning with denoising score matching.pdf

Contrastive representation learning methods operate by pulling different views of the same data sample together while pushing them away from views of different samples. A fundamental challenge is the estimation of the repulsive force, which typically requires large batch sizes, can exhibit high variance, and is susceptible to the curse of dimensionality. We introduce ScoreCLR, a contrastive representation learning method that offers a novel way to estimate this repulsion term. We consider the framework of representation learning by maximizing the mutual information between two latent views of a sample. By deriving the gradient of the Shannon entropy with respect to the encoder parameters, we obtain an equivalent objective that involves the score of the latent representation. We then use denoising score matching techniques to estimate this score with a lightweight network that is trained jointly with the encoder. We further propose regularization techniques using different noise levels and a Gaussian prior on the latent representation. ScoreCLR replaces the batch of explicit negative samples in contrastive methods with a learned repulsion whose cost is linear in the batch size rather than quadratic. On CIFAR-10 and ImageNet-100 it does so with minimal loss of linear-probe accuracy compared to SimCLR under a shared recipe, while producing projector outputs of higher effective rank, closer to the Gaussian prior.

## 10. DECODE: Diagnosing Interpretability Failures in Automated Interpretation Process

- Authors: Dohyun Kim, Jaeung Lee, Donghee Hong, Jaemin Jo
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-13
- DOI: Unavailable
- Categories: cs.AI, cs.HC
- Relevance: 3.0761680956528235
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.17856v1
- PDF: https://arxiv.org/pdf/2611.17856v1
- Local PDF: pdf/2026-11-17_10_DECODE_ Diagnosing Interpretability Failures in Automated Interpretation Process.pdf

Tools for interpreting the internal representations of Large Language Models (LLMs) increasingly rely on LLMs themselves to both generate and evaluate explanations, creating a self-referential automated interpretation process with minimal human oversight. This automation raises significant reliability concerns, which are exacerbated by the absence of ground truth. In practice, it is difficult to validate explanations or to attribute interpretability failures to their source -- whether they originate from the tool's extracted representations or from the LLM used in the process. To address these challenges, we present DECODE, a visual analytics system that reintroduces human oversight into the automated interpretation process. Our approach decomposes the diagnostic workflow into three progressive stages, isolating failure sources ranging from structural defects to explanation-level misalignments. Drawing inspiration from inter-coder consensus in qualitative analysis, we utilize consensus among independently generated explanations and their evaluation metrics as a proxy for reliability. To further scale human inspection, we employ a three-phase active seeding protocol that strategically recommends high-priority instances for manual review. Finally, we demonstrate the effectiveness of our approach through a case study on 16,384 Sparse Autoencoder features, showing that it can efficiently identify and attribute interpretability failures at scale.

## 11. Understanding Contextual Bias in Agricultural CNNs Through Hidden-Neuron Concept Induction

- Authors: Abhilekha Dalal, Avishek Das, Samatha Ereshi Akkamahadevi
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-13
- DOI: Unavailable
- Categories: cs.CV, cs.LG
- Relevance: 3.022030678889261
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.18530v1
- PDF: https://arxiv.org/pdf/2611.18530v1
- Local PDF: pdf/2026-11-17_11_Understanding Contextual Bias in Agricultural CNNs Through Hidden-Neuron Concept Induction.pdf

Convolutional Neural Networks (CNNs) can classify images using background-dominated patches that contain little or none of the target object, showing that they exploit contextual information. Previous studies detected this behavior through classification accuracy but say little about what CNN hidden layers represent. We investigate whether Concept Induction can reveal interpretable visual properties associated with hidden-neuron activations on contextual image patches. Using five agricultural datasets with high, moderate, and low contextual bias, we analyze four CNN architectures at three network depths and five patch locations. Quantitative image descriptors of each patch are encoded in a knowledge graph and used as background knowledge for Concept Induction, which derives logical expressions characterizing neuron activation. These expressions are tested on held-out images using the Mann-Whitney U test and Cliff's delta. Of 48,013 tested neuron-feature pairs, 13,164 (27.4%) were validated. Validation was most frequent at intermediate depths (mean 40.2% at mid layers versus 12.0% at deep layers), and no patch location dominated across datasets. Among the tested descriptors, edge, Gabor, and Tamura texture features had the highest validation rates. Stronger contextual bias did not correspond to higher neuron-feature validation rates: moderately biased Sugarcane had the highest rate (40.5%) and highly biased Cassava the lowest (19.2%). These results suggest that behavioral context dependence and the semantic interpretability of hidden neurons capture different aspects of CNN behavior, and that Concept Induction can complement patch-based bias detection.

## 12. LightTAR: Light and Fast Target-Aware Representations for Multimodal Tabular Learning

- Authors: Eilam Shapira, Alan Arazi, Shoham Grunblat, Roi Reichart
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-12
- DOI: Unavailable
- Categories: cs.LG, cs.CL, cs.CV
- Relevance: 2.9992680778487553
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.17600v1
- PDF: https://arxiv.org/pdf/2611.17600v1
- Local PDF: pdf/2026-11-17_12_LightTAR_ Light and Fast Target-Aware Representations for Multimodal Tabular Learning.pdf

Multimodal tabular learning involves classification and regression on tables combining structured numerical and categorical features with unstructured text and images. These unstructured fields are commonly represented by pretrained encoder embeddings reduced with principal component analysis (PCA). This reduction prioritizes input variance but may overlook information relevant to predicting the target. We introduce LightTAR, a simple, inexpensive method that adapts dimensionality reduction to the prediction task. LightTAR augments the standard PCA representation with a few target-aware features extracted jointly from the final and an intermediate encoder layer using regularized partial least squares (PLS). We evaluate LightTAR with 21 tabular models, including tree ensembles, neural networks, and tabular foundation models. LightTAR improves average predictive performance for all models and, averaged across models, improves prediction on almost every MulTaBench dataset. These gains come with a small increase in total runtime relative to PCA representations. LightTAR integrates directly into existing encoding pipelines, improving tabular learners' predictive performance without modifying the encoder or the learner.

## 13. Graph diffusion transformer for interpretable generation and inverse design of disordered atomic structures

- Authors: Jiani Hu, Chenyan Wang, Yongkun Yang, Guanyu Hou, Jihaochen Zhang, Lei Liu, Ji Chen
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-13
- DOI: Unavailable
- Categories: cond-mat.mtrl-sci, cond-mat.dis-nn, cond-mat.mes-hall, cs.LG, physics.comp-ph
- Relevance: 2.984464182110837
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.18420v1
- PDF: https://arxiv.org/pdf/2611.18420v1
- Local PDF: pdf/2026-11-17_13_Graph diffusion transformer for interpretable generation and inverse design of disordered atomic structures.pdf

Atomic disorder offers a potent degree of freedom to tailor material properties, yet the resulting vast configuration space obscures structure-property relations and hinders rational inverse design. Here we introduce Graph Amorphous Diffusion Transformer (GaDiT), a generative model that combines dynamic periodic graphs, masked conditioning and an interval-weighted training-noise distribution. GaDiT generates high-quality disordered structures while accelerating sampling by two orders of magnitude compared with existing corrector-based approaches, as demonstrated across two-dimensional amorphous carbon and three-dimensional amorphous silicon and silica. Moreover, GaDiT supports conditional generation under single or combined structural features, physical properties and preparation conditions in a unified model, and enables inverse design that expands accessible structure-property ranges beyond the training distribution. To interpret these structures and the trained network, we propose a conditioned atomic response mapping analysis, revealing both the global structural descriptors and the local atomic environments that govern target properties. Overall, GaDiT establishes a general framework for interpretable generation, inverse design and structure-property discovery for disordered atomic structures.

## 14. NeoResearch: Literature- and Experience-Guided Autonomous Time Series Model Discovery

- Authors: Ze Guo, Mingyue Cheng, Xiaoyu Tao, Shuo Yu, Shangtong Ye
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-13
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 2.971940428919533
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.18235v1
- PDF: https://arxiv.org/pdf/2611.18235v1
- Local PDF: pdf/2026-11-17_14_NeoResearch_ Literature- and Experience-Guided Autonomous Time Series Model Discovery.pdf

Developing effective forecasting models for diverse time-series domains requires substantial expert knowledge, evidence from scientific literature on the web, and iterative experimentation. However, translating this knowledge and research experience into model designs requires preserving source context and testing applicability under task-specific assumptions. In this paper, we propose NeoResearch, a literature- and experience-guided autonomous research framework that leverages large language models (LLMs) as researchers to discover lightweight, domain-specific forecasting models. Specifically, NeoResearch establishes an expert-inspired dual-loop research workflow, coupling hypothesis-driven architecture exploration with iterative training and hyperparameter optimization through experimental feedback. To enable knowledge-grounded discovery, the agent autonomously mines scientific literature from the Web, extracting modeling mechanisms, empirical evidence, and applicability conditions to formulate task-grounded, testable architecture hypotheses. Furthermore, a hierarchical experience memory links literature findings to experimental outcomes and consolidates conditional lessons, guiding architecture discovery and training optimization while supporting reuse across forecasting tasks. Experiments on ten datasets show competitive performance and support dual loops, literature extraction, and memory reuse. Our code is available.

## 15. Classifier-Guided Latent Diffusion for Small-Molecule Generation

- Authors: Ali Forooghi, Luis Rueda, Alioune Ngom
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-13
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 2.9551925185471664
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.17650v1
- PDF: https://arxiv.org/pdf/2611.17650v1
- Local PDF: pdf/2026-11-17_15_Classifier-Guided Latent Diffusion for Small-Molecule Generation.pdf

Diffusion models have emerged as a promising class of generative models for molecular design because of their ability to learn complex chemical distributions and support conditional or guided generation. In this work, we investigate a latent diffusion pipeline for property-guided small-molecule generation. The proposed framework represents canonicalized SMILES strings using a frozen ChemBERTa encoder, trains a Transformer-based decoder to reconstruct SELFIES strings from molecular latent embeddings, and learns an unconditional denoising diffusion model in the ChemBERTa latent space. To enable property-directed generation, a differentiable latent property predictor is used to guide the diffusion sampling process. Generated SELFIES strings are converted to SMILES, validated using RDKit, and evaluated using molecular validity, uniqueness, novelty, and predicted property scores. We study guidance toward two drug-relevant binary endpoints: blood--brain barrier permeability and inhibition of human $β$-secretase 1. The results suggest that latent diffusion over pretrained molecular embeddings can generate chemically valid and novel molecules while enabling controllable steering toward desired molecular properties.

## 16. CoPre-MoE: Consolidating and Preserving MoE for Multimodal Continual Instruction Tuning

- Authors: Tao Hu, Ling-Xiang Zhang, Da-Wei Zhou
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-13
- DOI: Unavailable
- Categories: cs.CV, cs.AI, cs.LG
- Relevance: 2.9315681714215422
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.18417v1
- PDF: https://arxiv.org/pdf/2611.18417v1
- Local PDF: pdf/2026-11-17_16_CoPre-MoE_ Consolidating and Preserving MoE for Multimodal Continual Instruction Tuning.pdf

Multimodal continual instruction tuning requires multimodal large language models to sequentially acquire new capabilities without catastrophic forgetting. Mixture-of-experts (MoE) architectures offer a promising way to mitigate task interference through expert specialization and combination. However, while existing MoE-based methods avoid overwriting shared parameters by allocating separate experts for each task, this progressive expansion incurs severe cross-task redundancy and linear parameter growth. Specifically, experts across tasks often learn overlapping functions alongside task-specific capabilities. For instance, ScienceQA and TextVQA both locate relevant image regions. To curb parameter redundancy without inducing forgetting, we propose Consolidating and Preserving MoE (CoPre-MoE). For each incoming task, CoPre-MoE first learns task-specific MoE to capture specialized capabilities. To eliminate redundancy and reduce parameter growth across tasks, we design a shared-and-private expert architecture. Specifically, we first evaluate functional overlap to selectively consolidate overlapping experts across tasks into a fixed-capacity generic expert pool. We then factorize the remaining task-specific experts into shared projection bases and compact task-specific cores within a private expert pool. To mitigate forgetting, we construct the router by pairing each expert with learnable retrieval keys, where historical keys remain frozen during continual updates while newly added keys are regularized with an orthogonality penalty. At inference, input-dependent routing dynamically combines both pools without test-time task labels. Extensive experiments demonstrate that CoPre-MoE achieves superior performance while substantially reducing parameter overhead.

## 17. LoRAWeaver: Directional Adapter Routing in LoRA Representation Space

- Authors: Inish Melroy D Souza, Tom Jackson, Vitor Castro, Rebecca Higginson, Andrea Soltoggio
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-01
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 2.920079047002166
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.17340v1
- PDF: https://arxiv.org/pdf/2611.17340v1
- Local PDF: pdf/2026-11-17_17_LoRAWeaver_ Directional Adapter Routing in LoRA Representation Space.pdf

Large language models are expensive to update through full retraining. Parameter-efficient fine-tuning reduces the cost of adaptation, but repeated adaptation creates a growing pool of task-specific LoRA adapters. This pool complicates adapter selection during inference. Existing routing and encoder-based methods often require retraining when new adapters are added, which limits their use in dynamic settings. This paper treats adapter routing as a representation alignment problem in the adapter-output space. The proposed training-free method selects adapters by matching adapter-conditioned query representations against task prototypes using cosine similarity. Experiments with LLaMA-2-7B and LLaMA-2-13B on a 48-task FLAN-v2 benchmark and on out-of-distribution tasks show that the method outperforms training-free baselines in the cross-task setting and approaches a trained retrieval encoder without learning a router. An ablation confirms the benefit of directional alignment in the adapter-output space.

## 18. A Synthetic Benchmark for Target-Centric Causal Discovery in Industrial Processes

- Authors: Angelo Ziletti
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-12
- DOI: Unavailable
- Categories: cs.LG, cs.AI
- Relevance: 2.908236110263647
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.17556v1
- PDF: https://arxiv.org/pdf/2611.17556v1
- Local PDF: pdf/2026-11-17_18_A Synthetic Benchmark for Target-Centric Causal Discovery in Industrial Processes.pdf

Causal discovery promises to find which recorded variables drive a process target such as product quality, yield or energy use. Process data with known causes are rare, and in existing benchmarks the difficulty of identifying the causes of a target is either fixed by the recorded data or set for the whole graph. We present a synthetic benchmark for target-centric causal discovery in industrial processes. Its generator is a two-level structural causal model inspired by batch production, assembled from components that each model one phenomenon of process data, such as a control loop or a delayed effect. The graph is built around the target: without sensor error, every non-cause can be distinguished from the direct causes by conditioning on them or by time order. Each component is set independently, so the difficulty can be varied one condition at a time. We evaluate eight methods, from association measures to effect estimation, with an error analysis by the role of the selected candidate; all degrade as the difficulties combine, each in a way consistent with its assumptions.

## 19. Deep Latents, Long Memory: Latent persistence explains temporal correlations in transformer activations

- Authors: Francesco Cagnetta, Santiago Acevedo
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-13
- DOI: Unavailable
- Categories: cs.LG, cs.CL
- Relevance: 2.836259273092941
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.18089v1
- PDF: https://arxiv.org/pdf/2611.18089v1
- Local PDF: pdf/2026-11-17_19_Deep Latents, Long Memory_ Latent persistence explains temporal correlations in transformer activations.pdf

The hidden layers of Large Language Models (LLMs) are believed to encode representations of the data whose abstraction increases with depth. However, in the absence of an operational notion of abstraction, this statement is hard to test quantitatively. Here, we propose an alternative view, building on the principle that the correlations of a sequence reflect the structure of the process that generated it. We define the autocorrelation function of a layer as the average dot product between its activations at two context positions separated by a lag. Latent variables encoded persistently along the context create slowly decaying tails in the autocorrelation, and we find these tails to grow across layers in both synthetic and natural data. In synthetic data with controlled hierarchical latent structure, this growth stems from the encoding of abstract latent variables, which govern long stretches of the input. Indeed, the persistence of latent codes predicts the qualitative structure of autocorrelations and accounts for most of the empirical measures. In real text, we take sparse-autoencoder features as proxies for latent variables, and find that their persistence correlates strongly with the magnitude of autocorrelations across datasets and LLMs. In particular, the persistence time increases with depth, as do autocorrelations, implying that deeper latent features persist for longer context spans. We complement this analysis by explicitly ablating the persistent sparse-autoencoder features and observing a consequent decrease in the autocorrelations.

## 20. LLM-Guided Cluster Lifecycle Management: Deciding When and How to Evolve Behavioral Clusters

- Authors: Himanshu Kulkarni, Siddharth Krishnamurthy, Jianhong Xin
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-13
- DOI: Unavailable
- Categories: cs.AI, cs.LG
- Relevance: 2.817215530714014
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.17616v1
- PDF: https://arxiv.org/pdf/2611.17616v1
- Local PDF: pdf/2026-11-17_20_LLM-Guided Cluster Lifecycle Management_ Deciding When and How to Evolve Behavioral Clusters.pdf

Behavioral clusters learned over user or item interactions drift as behavior evolves: some fragment into sub-behaviors, some converge, some disappear, and new patterns emerge. Two paradigms dominate the maintenance of evolving clusterings. Threshold triggers fire a pre-specified action when a hardcoded statistic crosses a cutoff; refit-and-track (MONIC-style) re-clusters every window and infers transitions from how the new clusters align with the previous window's. Both hardwire the decision into a threshold or a re-clustering rule. We study an alternative in which a large language model (LLM) makes the lifecycle decision in place. Given a threshold-free, whole-population view of the current cluster set (statistical health, labels, member texts, residual mass), the LLM decides per cluster whether and how to act (split, merge, retire, create, or no-action) without re-clustering. Because the useful signal channel depends on how informative the labels are, we fix a richness-conditioned policy in advance: statistics when label distinctiveness is low, fused statistics+semantics when it is high. On three public datasets spanning label richness (YooChoose 0.17, MOOC 0.50, News-Category 0.70), the policy-selected LLM mode obtains the highest F1 on all three, with far fewer interventions and stronger restraint than tuned threshold heuristics and a MONIC steelman (paired Wilcoxon p <= 0.003, bootstrap 95% CIs excluding zero). The gain is concentrated more in precision than recall. The useful modality shifts from statistics to semantics/fusion as richness rises. Semantics hurt on YooChoose, fusion is roughly neutral on MOOC, and the semantic channel is required on News. One base prompt template and one fixed policy serve all three datasets, whereas the tuned baseline collapses when moved between them. We treat this shift as a practitioner diagnostic observed on three datasets, not a validated law.

## 21. Disentangling Forgetting from Utility: Lightweight LLM Unlearning via Orthogonal Null-Space Projection

- Authors: Xiuyuan Wang, Weiming Liu, Zongxin Yang, Fan Wang, Liemiao Jin, Rubin Qin, Wei Chen, Bin Shi, Chaochao Chen, Xiaolin Zheng
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-13
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 2.8025967006049832
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.17864v1
- PDF: https://arxiv.org/pdf/2611.17864v1
- Local PDF: pdf/2026-11-17_21_Disentangling Forgetting from Utility_ Lightweight LLM Unlearning via Orthogonal Null-Space Projection.pdf

Large Language Models (LLMs) pose significant security risks by retaining private or hazardous information, creating an urgent need for unlearning techniques that excise specific knowledge without compromising general utility. However, prevailing fine-tuning-based unlearning methods struggle to achieve this balance, often suffering from computational inefficiency and unintended utility degradation due to the entangled nature of knowledge within model parameters. To disentangle forgetting from utility, we propose UUE, a theoretically grounded framework that reformulates unlearning as controllable model editing. First, UUE projects parameter updates into the orthogonal left null space of retained knowledge representations, strictly ensuring that the editing process causes minimal interference to the model's general capabilities. Second, distinct from targeted mapping, we introduce a convex untargeted objective that derives a closed-form analytical solution to effectively disrupt undesired knowledge by pushing forget-set embeddings toward their antipodal points. We implement UUE via lightweight, pluggable adapters (including a low-rank variant, UUE-L), enabling efficient deployment without modifying the frozen backbone. Extensive experiments on TOFU and WMDP benchmarks demonstrate that UUE and UUE-L achieve superior unlearning efficacy, significantly outperforming existing methods.

## 22. WeightBench: Evaluating Language Models as Weight-Space Programmers

- Authors: Aayush Marasini, Barsat Khadka, Nick Rahimi
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-13
- DOI: Unavailable
- Categories: cs.LG, cs.AI
- Relevance: 2.7986220888505713
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.18553v1
- PDF: https://arxiv.org/pdf/2611.18553v1
- Local PDF: pdf/2026-11-17_22_WeightBench_ Evaluating Language Models as Weight-Space Programmers.pdf

Recent work shows that large language models (LLMs) can operate directly on the parameters of other neural networks. They can read what a network was trained to do, fix a network that fails, and write working networks from scratch, all without gradient descent. This capability has been termed Weight-Space Programming (WSP). Exploring this new paradigm systematically requires a robust benchmark. We introduce WEIGHTBENCH, a benchmark that evaluates LLMs of increasing capability on 42 WSP tasks across five tracks: reading, fixing and writing weights, recognizing edits that are impossible, and data-free compression. The networks whose weights the LLMs read and edit range from 2K-parameter control policies to 7B-parameter language models. Experimental benchmark results show that frontier agents can already read small networks and write working control policies without ever running them, but cannot yet patch language models, compress them without data, or tell an impossible edit from a hard one. On all 42 tasks, Claude Opus 5.5 reaches a macro score of 0.535 (Sonnet 5.5 0.466, Haiku 5.5 0.402, DeepSeek v4-flash 0.215); on the 38 tasks it was run on, GPT-6.1-sol reaches 0.568 against Opus's 0.546. Code, the task registry, our OS-level sandbox harness, and the live leaderboard are publicly available at https://github.com/Aayush-Marasini/WeightBench.

## 23. T2ST: Data-Efficient Spatio-Temporal Foundation Models via Temporal Data and Knowledge Transfer

- Authors: Yue Xu, Kaiyun Wei, Wenying Duan, Zichen Xu, Shuai Ma, Xiaoxi He
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-13
- DOI: Unavailable
- Categories: cs.LG, cs.AI
- Relevance: 2.794721589829229
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.18199v1
- PDF: https://arxiv.org/pdf/2611.18199v1
- Local PDF: pdf/2026-11-17_23_T2ST_ Data-Efficient Spatio-Temporal Foundation Models via Temporal Data and Knowledge Transfer.pdf

Spatio-temporal foundation models (STFMs) require large-scale training corpora, yet synchronized observations and spatial metadata are costly to acquire and curate, limiting the availability of suitable data. By contrast, time-series data are abundant and easier to collect. Since observations at each location form a time series, this motivates a natural question: can abundant time-series data enhance STFMs when spatio-temporal observations are scarce? To bridge this gap, we propose T2ST, a data-efficient training framework that augments limited spatio-temporal observations with selected auxiliary time series and transfers knowledge from a frozen time-series foundation model. Our key insight is that temporal pattern learning can benefit from abundant external time series, while spatial dependency learning remains grounded in real spatio-temporal observations. Guided by this insight, T2ST retrieves matched sequences to reinforce sparsely observed temporal patterns and selects reliable complementary sequences to broaden temporal coverage. Temporal relation distillation aligns relationships among historical patches, while multi-scale prediction distillation transfers forecasting behavior at fine and coarse temporal resolutions, enabling knowledge transfer across heterogeneous architectures. Using only 10\% of the original spatio-temporal data, T2ST enables STFMs to achieve overall forecasting performance competitive with or superior to their full-data counterparts across six long-term and twelve short-term forecasting datasets. These results establish a new paradigm for data-efficient training of spatio-temporal foundation models. Code is available at https://anonymous.4open.science/r/T2ST-65F3/.

## 24. f-Divergence Self-Play for Tabular Anomaly Detection via Large Language Models

- Authors: Hoang Tran Vuong, Linh Ngo Van, Dang Nguyen, Thin Nguyen, Phuoc Nguyen, Mehrtash Harandi, Trung Le
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-13
- DOI: Unavailable
- Categories: cs.LG, cs.CL
- Relevance: 2.788053545417186
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.18370v1
- PDF: https://arxiv.org/pdf/2611.18370v1
- Local PDF: pdf/2026-11-17_24_f-Divergence Self-Play for Tabular Anomaly Detection via Large Language Models.pdf

Anomaly detection in tabular data poses significant challenges due to heterogeneous feature types-mixing numerical, categorical, and textual attributes, which complicate learning meaningful representations of normality. Recent work has applied large language models (LLMs) to this problem by serializing table rows as text sequences, yet these approaches rely on one-shot supervised fine-tuning that offers limited signal to tighten the model's description of normality. We propose DiSPaT, a self-play fine-tuning framework that strengthens the model's understanding of normal data. Building on the theoretical foundation of f-divergence minimization, we derive a tight approximation connecting our training objective to reducing the distributional gap between real normal data and model-generated samples. DiSPaT operates through an alternating optimization: at each iteration, the current policy generates synthetic samples that serve as pseudo-anomalies, while a critic discriminator learns to distinguish these from real normal samples; this signal drives policy updates that progressively align the model distribution with the true normal-data distribution. Extensive experiments on diverse benchmarks demonstrate that DiSPaT consistently outperforms prior LLM-based methods, deep learning approaches, and classical unsupervised detectors for tabular anomaly detection.

## 25. Vision-as-a-Tool: Visual Harness for Multimodal Agentic Coding

- Authors: Haolin Yang, Wenshan Wu, Jin Jiang, Yu Cheng, Yan Xia, Ting Song, Yangyu Huang, Zhiliang Peng, Wenhui Wang, Hangbo Bao, Yuzhe Zhang, Wen-Da Wei, Tengchao Lv, Li Dong, Lei Cui, Furu Wei
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-13
- DOI: Unavailable
- Categories: cs.AI, cs.CV
- Relevance: 2.770165424306371
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.17797v1
- PDF: https://arxiv.org/pdf/2611.17797v1
- Local PDF: pdf/2026-11-17_25_Vision-as-a-Tool_ Visual Harness for Multimodal Agentic Coding.pdf

Multimodal agentic coding requires robust visual reasoning to analyze observations and evaluate generated artifacts. Current frameworks largely rely on a Thinking-with-Images paradigm, where agents depend on their intrinsic vision to execute visually grounded tasks. However, this architectural coupling introduces a fundamental bottleneck. Agent performance remains strictly bounded by internal perceptual limitations. Furthermore, text-only agents lack native perception. Without specialized tools, they cannot perform visual reasoning. To overcome these constraints, we introduce the Vision-as-a-Tool (VaaT) paradigm. Prior visual tool-use merely manipulates images for an agent's intrinsic vision to read. In contrast, VaaT reframes general-purpose multimodal large language models (MLLMs) as callable external utilities. As a result, text-only agents can completely offload visual reasoning during agentic execution. Meanwhile, vision-capable agents can dynamically augment their native perception on demand. We instantiate this paradigm in VHarness, a unified framework driven by five atomic actions. We comprehensively evaluate VHarness across Image-to-HTML, Image-to-SVG, and Image-to-3D generation tasks. Experimental results demonstrate that VHarness consistently improves visual fidelity and geometric accuracy across both text-only and multimodal coding agents. These findings highlight that modularizing visual reasoning into callable utilities provides a flexible and scalable foundation for future agentic coding systems.

## 26. Right Token, Right Time: From Per-Token Gating to Trajectory-Aware Activation Steering

- Authors: Nima Eshraghi, Lovedeep Gondara, Sagarika Suresh, Xiaotong Xu, Jithin Pradeep, Fanny Chevalier
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-13
- DOI: Unavailable
- Categories: cs.LG, cs.AI
- Relevance: 2.7503083855002823
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.18274v1
- PDF: https://arxiv.org/pdf/2611.18274v1
- Local PDF: pdf/2026-11-17_26_Right Token, Right Time_ From Per-Token Gating to Trajectory-Aware Activation Steering.pdf

Activation steering via sparse autoencoders (SAEs) enables behavioral control of large language models without task-specific fine-tuning. Yet, standard methods apply the steering signal at every generated token, displacing representations from the distribution the model was trained on and eroding generation quality. We show that \emph{when} along a generation the intervention is applied is a decisive axis of control. We cast steering as a per-token allocation problem under a fixed budget of steerable tokens, so that methods differ only in which tokens they select, making allocation the sole variable. Within this framework we introduce two gates. The first, Contrastive Feature Projection (CFP), is memoryless and selects the tokens least aligned with the target behavior through a sparse, interpretable feature projection. The second, Closed-Loop Adaptive Bernoulli Steering (CLABS), is trajectory aware. It treats allocation as closed-loop feedback control, tracking the alignment a generation has accumulated so far and spending budget where the trajectory falls behind. On a linear steering-response model we derive an explicit gain region that guarantees closed-loop stability of CLABS and show that its integral term reduces the steady-state tracking offset. Empirically, CFP and CLABS achieve the largest behavioral shift among budgeted gates at matched budgets, with CLABS strongest under the tight budgets where allocation matters most, while best preserving fluency.

## 27. Bridging the Training Gap with Hyperion: A Training-Free Style Transfer Method on Diffusion Transformers

- Authors: Yi Li, Chengyan Li, Zhirui Fang, Junchuan Zhang, Xuan Wang, Huaibo Huang, Yan Luo, Yanqing Guo
- Source: openalex
- Venue type: journal
- Journal: IEEE Transactions on Pattern Analysis and Machine Intelligence
- Publication status: published
- Publication date: 2026-11-11
- DOI: https://doi.org/10.1109/tpami.2026.3752263
- Categories: Generative Adversarial Networks and Image Synthesis, Domain Adaptation and Few-Shot Learning, Advanced Neural Network Applications
- Relevance: 2.7260095453687514
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://doi.org/10.1109/tpami.2026.3752263
- PDF: Unavailable
- Local PDF: Not downloaded

Training-free style transfer on Multimodal Diffusion Transformers (MM-DiT) remains challenging due to the persistent gap between trained adapters and injection-based training-free methods. Existing training-free methods typically perform forward feature injection, and thus struggle to reproduce the rich painterly textures achieved by trained adapters, often leading to only faint hue shifts. In this paper, we trace this limitation to the absence of backpropagation-induced spatial coupling and propose Hyperion, a fully training-free style-transfer pipeline for MM-DiT. At the optimization level, the pipeline introduces Adam-in-loop, which iteratively optimizes the diffusion latent at each denoising step with a frozen MM-DiT. This process recovers the gradient-driven coupling effect produced through the self-attention value path, where neighboring tokens receive highly similar updates and form coherent brushstroke textures. At the distribution level, the pipeline introduces Sinkhorn Latent Transport (SLT), a single closed-form optimal-transport step that pre-aligns latent color distributions before Adam optimization, improving the operational efficiency of Adam-in-loop. To further enhance stylization quality, we develop a frequency-domain Sinkhorn loss to sharpen painterly textures and a layout-residual-suppression step to reduce layout interference. The pipeline can also be extended to image-to-image stylization. Extensive experiments on a 39-style × 6-prompt benchmark (234 pairs) demonstrate that Hyperion achieves CSD $= 0.640$ and CLIP-T $= 0.296$, improving CSD by +5.2% over Adam-8 at $2.5\times$ lower forward-pass cost and by +16.6% over Adam-only under an equal compute budget. Notably, Hyperion outperforms four pre-trained style adapters on 19 of 21 diverse style families, achieving a mean CSD of 0.657 versus 0.506 for the strongest baseline.

## 28. TIDE: Reclaiming Lost Performance In On-Policy Reinforcement Learning

- Authors: Mathew Jacob, Morgan Borjigin-Wang, Kan Zhu, Po Hao Chen, Yi Pan, Andy Ruan, Nayani Modugula, Ethan Lavi, Luis Ceze, Malte Schwarzkopf, Akshay Narayan, Deepti Raghavan, Stephanie Wang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-13
- DOI: Unavailable
- Categories: cs.LG, cs.DC, cs.PF
- Relevance: 2.719983975998903
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.17924v1
- PDF: https://arxiv.org/pdf/2611.17924v1
- Local PDF: pdf/2026-11-17_28_TIDE_ Reclaiming Lost Performance In On-Policy Reinforcement Learning.pdf

Synchronous, colocated RL post-training of large language models (LLMs) today suffers from severe under-utilization due to long-tail rollouts. Inference engines fall idle waiting for long-tail rollouts or decode at low, inefficient batch sizes. To address this, we present TIDE, an RL training system that preserves on-policy training semantics while recovering resource utilization. TIDE does so by two complementary techniques: (1) dynamically repurposing rollout GPUs for training while long-tail rollouts complete and (2) dynamically migrating rollouts between inference engines to boost decoding throughput. TIDE automatically determines the right time to repurpose rollout resources through an adaptive migration policy, obtaining performance improvements that generalize across multiple applications and hardware configurations without requiring bespoke configuration. In our evaluation, TIDE provides end-to-end speedups of up to 1.36x over colocated systems, outperforming all evaluated on-policy baselines and achieving up to 97% of optimal throughput.

## 29. Urban Architect: Steerable 3D Driving Scene Generation With Layout Prior

- Authors: Fan Lu, Kwan-Yee Lin, Yan Xu, Hongsheng Li, Guang Chen, Changjun Jiang
- Source: openalex
- Venue type: journal
- Journal: IEEE Transactions on Pattern Analysis and Machine Intelligence
- Publication status: published
- Publication date: 2026-11-06
- DOI: https://doi.org/10.1109/tpami.2026.3751349
- Categories: 3D Shape Modeling and Analysis, Generative Adversarial Networks and Image Synthesis, Computer Graphics and Visualization Techniques
- Relevance: 2.712189707249988
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://doi.org/10.1109/tpami.2026.3751349
- PDF: Unavailable
- Local PDF: Not downloaded

Text-to-3D generation has achieved remarkable success via large-scale text-to-image diffusion models. Nevertheless, scaling this methodology to large-scale driving scenes is underexplored. Driving scenes, characterized by numerous elements, intricate arrangement relationships, and vast scale, present a formidable barrier to the interpretability of ambiguous textual descriptions for effective model optimization. In this work, we surmount the limitations by introducing a compositional 3D layout representation into text-to-3D paradigm, serving as an additional prior. It comprises a set of semantic primitives with simple geometric structures and explicit arrangement relationships, complementing textual descriptions and enabling steerable generation. Specifically, we represent the scene via 2D Gaussian splatting and develop two innovative optimization strategies: (1) Layout-Guided Variational Score Distillation, which addresses model optimization inadequacies by conditioning the score distillation sampling process with geometric and semantic constraints of 3D layouts; (2) Semantic-Depth Score Distillation Sampling, which ensures alignment of semantics, geometry, and appearance by matching the rendered semantic and depth maps with 3D layouts. Extensive experiments substantiate the capability of our framework to scale text-to-3D generation to large-scale driving scenes that cover over 1000 m driving distance for the first time. We also present various scene editing demonstrations, showing the powers of steerable urban scene generation.

## 30. Image Quality Assessment for Machine-oriented Communication

- Authors: Chunyi Li, Xiaoyue Ling, Farong Wen, Haoyang Li, Guo Lu, Weisi Lin, Xiao-Ping Zhang, Guangtao Zhai, Wenjun Zhang
- Source: openalex
- Venue type: journal
- Journal: IEEE Transactions on Pattern Analysis and Machine Intelligence
- Publication status: published
- Publication date: 2026-11-13
- DOI: https://doi.org/10.1109/tpami.2026.3748556
- Categories: Image and Video Quality Assessment, Image Retrieval and Classification Techniques, Digital Media Forensic Detection
- Relevance: 2.7080185546430324
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://doi.org/10.1109/tpami.2026.3748556
- PDF: Unavailable
- Local PDF: Not downloaded

The rapid development of Multimoal Large Language Models (MLLMs) has driven the evolution of communication paradigms, making the transmission of visual information in extremely low-bandwidth possible. However, as it is oriented toward computer vision tasks rather than humans, there is no widely accepted metric for its evaluation. To address this issue, we conduct a comprehensive visual quality assessment of machine oriented communication systems. Specifically, we (1) at the source level: a generative codec framework is established, with a MLLM communication pipeline through cross-modal generation between images and text. (2) at the channel level: images are transmitted using channel encoding/decoding strategies in different physical environments, and construct a dataset with 12k pairs of reference/distorted images. (3) at the sink level: 50 computer vision models are implemented to conduct 600k inferences on 5 downstream tasks, to characterize the differences between refer ence/distorted image pairs. (4) at the evaluation level: benchmark 18 cutting-edge Image Quality Assessment (IQA) methods, and develop a novel Mixture-of-Experts metric, termed CFA-MoE, to serve as a strong baseline for this task. Experimental results show that the current IQA algorithms cannot accurately evaluate machine-oriented distortions, highlighting the importance and challenge of this task. It is expected this dataset and baseline to facilitate future IQA algorithms and promote the communication paradigms from human to machine preference. Code will be available at: https://github.com/aiben-ch/MoQAD.
