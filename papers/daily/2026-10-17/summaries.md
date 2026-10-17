# Paper Daily Reading - 2026-10-17

## 1. Mapping cell-type-specific spatial gene programs uncovers tissue architecture and microenvironment organization

- Authors: Yeqin Zeng, Zhiwei Wang, Yuyao Liu, Yuheng Chen, Jiguang Wang, Hao Chen, Can Yang
- Source: openalex
- Venue type: journal
- Journal: Nature Communications
- Publication status: published
- Publication date: 2026-10-14
- DOI: https://doi.org/10.1038/s41467-026-78447-3
- Categories: Single-cell and spatial transcriptomics, Genomics and Chromatin Dynamics, Gene Regulatory Network Analysis
- Relevance: 3.89191165464113
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://doi.org/10.1038/s41467-026-78447-3
- PDF: https://www.nature.com/articles/s41467-026-78447-3_reference.pdf
- Local PDF: pdf/2026-10-17_01_Mapping cell-type-specific spatial gene programs uncovers tissue architecture and microenvironment organization.pdf

The complex organization of tissues is shaped by the spatial arrangement of diverse cell types executing specialized gene programs. Cell-type-specific spatial gene programs (SGPs) are transcriptional modules that capture spatial expression co-variation within cell types. However, identifying these SGPs remains challenging in spatial transcriptomics. Here we present MacSGP, a scalable framework that integrates deep graph neural networks with probabilistic modeling to identify cell-type-specific SGPs through low-rank structures while accounting for cell type mixtures. Through comprehensive simulations and real data analyses spanning diverse tissues and technologies, we demonstrate that MacSGP effectively distinguishes cell-type-specific SGPs from cell-type marker gene expression patterns while uncovering tissue architecture and cellular microenvironments. In a mouse brain dataset, we identify replicable SGPs reflecting subregional neuronal specializations, with these genes significantly enriched for heritabilities associated with brain-related phenotypes. Across colorectal cancer datasets from various platforms, MacSGP identifies consistent SGPs that define distinct cellular niches within the tumor microenvironment. MacSGP identifies cell-type-specific spatial gene programs, capturing coordinated gene activity that varies across locations within cell types. This study dissects gene programs that reveal patterns of tissue organisation and cellular environments within brain and tumour contexts.

## 2. Panoramic modelling of single-cell transcriptomes at scale with CellNet

- Authors: Xiaoqing Lian, Pei Liu, Jiahui Tan, Luoda Tan, Chaoyi Li, Quan Zou, Chen Lin, Xiangxiang Zeng
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-15
- DOI: Unavailable
- Categories: q-bio.GN
- Relevance: 3.668017617918477
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.21943v1
- PDF: https://arxiv.org/pdf/2610.21943v1
- Local PDF: pdf/2026-10-17_02_Panoramic modelling of single-cell transcriptomes at scale with CellNet.pdf

Comprehensively characterizing cellular diversity is critical for understanding tissue development, identifying disease-associated populations and investigating gene programmes linked to specialized functions. Advances in single-cell profiling reveal additional cell-specific transcripts and molecular associations, yet many foundation models represent only a restricted portion of this increasingly rich molecular information. Here we present CellNet, which enables panoramic modelling of single-cell transcriptomes by integrating DNA-derived gene identities and measured RNA expression in a shared image representation. Pretrained on 231 million cell profiles spanning 40 species, CellNet improves rare-population and condition-associated state recognition in evaluated cohorts while retaining competitive general cell representations. It predicts withheld coding-gene expression and selected non-coding targets in total-RNA data, and recovers lineage-specific expression patterns in spatial measurements. Prediction also extends across species, including to targets without expression-pretraining exposure. Its gene representations retrieve known non-coding modules and developmental or neural programmes, including from sparsely detected RNA queries. Together, these results establish CellNet as a scalable framework for interpreting cellular diversity through increasingly comprehensive transcriptomic measurements.

## 3. Interpretable and scalable spatial gene set activity analysis with GESSO uncovers functional tissue architecture

- Authors: Andrew I. Yang, Chichun Tan, Ying Ma
- Source: openalex
- Venue type: journal
- Journal: Nature Communications
- Publication status: published
- Publication date: 2026-10-14
- DOI: https://doi.org/10.1038/s41467-026-78316-z
- Categories: Single-cell and spatial transcriptomics, Bioinformatics and Genomic Networks, Gene expression and cancer classification
- Relevance: 3.3991112714683895
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://doi.org/10.1038/s41467-026-78316-z
- PDF: Unavailable
- Local PDF: Not downloaded

Spatially resolved transcriptomics (SRT) measures gene expression within tissues. Existing methods that summarize the activity of functionally related genes often ignore relationships between neighboring locations and offer limited statistical testing, gene-level interpretation, or scalability. Here we present GESSO, a method that incorporates spatial information to estimate gene set activity within tissues, quantify how strongly each gene contributes to the resulting activity scores, and perform location-specific statistical tests for elevated pathway activity. In simulations and analyses of 13 datasets from five SRT platforms, GESSO better recovers known spatial patterns, provides well-calibrated statistical tests and interpretable gene-level contributions, and scales more efficiently than existing methods. Applications across tumor, embryonic, and lymphoid tissues reveal localized biological programs, including epithelial-to-mesenchymal transition at tumor-stroma interfaces, developmental signaling gradients, and coordinated immune pathways within germinal centers. Therefore, GESSO enables interpretable and scalable spatial mapping of gene set activity across diverse SRT technologies and biological settings. Spatial transcriptomics measures gene activity while preserving tissue structure. Here, the authors present GESSO, a scalable method that uses spatial information to quantify pathway activity and detect localized biological programs.

## 4. Complete or Sparse: A Tale of Two Identifiabilities

- Authors: Junze Zhou, David Klindt
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-14
- DOI: Unavailable
- Categories: stat.ML, cs.LG
- Relevance: 3.3103797320582
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.20851v1
- PDF: https://arxiv.org/pdf/2610.20851v1
- Local PDF: pdf/2026-10-17_04_Complete or Sparse_ A Tale of Two Identifiabilities.pdf

Understanding when neural networks learn interpretable representations is central to mechanistic interpretability. We study this through identifiability: when can supervised learning recover the true latent variables underlying the data? We introduce two data generating processes distinguished by their causal direction where either labels cause latents (generative) or latents cause labels (discriminative). When the representation has at least as many dimensions as the latent space, we prove that the optimal encoders are linear in the latents. Conversely, when dimensions are insufficient, identifiability generically fails and encoders become nonlinear. We then show that additional constraints yield recovery of individual latent variables, not just linear mixtures. In the generative setting, non-negative activations and energy efficiency force each neuron to encode exactly one latent, providing a precise account of selective grandmother cell-like responses. In the discriminative setting, when latents are sparse and the true measurement matrix satisfies the spark condition, the learned encoder inherits compressed sensing structure, enabling sparse dictionary learning to perfectly recover individual latents. This constitutes, to our knowledge, the first identifiability result for undercomplete nonlinear independent component analysis. Our framework unifies nonlinear ICA, compressed sensing, and neural network interpretability, delineating exactly when representations transition from nonlinear distortions to linear representations and, under additional constraints or steps, to clean, axis-aligned codes. Theoretical predictions are validated on synthetic benchmarks and on activations drawn from vision models, large language models, and macaque inferotemporal cortex.

## 5. Causal Integrated Gradients: Scalable Feature Attribution Along Causal Paths

- Authors: Joran Michiels, Anis Ismail, Maarten De Vos, Alejandro Sifrim
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-15
- DOI: Unavailable
- Categories: cs.LG, cs.AI
- Relevance: 3.29995672911711
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.22126v1
- PDF: https://arxiv.org/pdf/2610.22126v1
- Local PDF: pdf/2026-10-17_05_Causal Integrated Gradients_ Scalable Feature Attribution Along Causal Paths.pdf

Existing feature attribution methods that account for feature dependencies do not scale to high dimensions. We propose causal integrated gradients (CIG) and causal expected gradients (CEG), which extend integrated gradients to incorporate prior causal structure among input features while retaining its computational efficiency and, under conditions on the causal graph, its axiomatic guarantees. In many settings, some causal structure between features is already known, for example, that a transcription factor causally regulates a target gene's expression. Yet existing gradient-based methods cannot exploit this structure, instead crediting a feature's downstream effects over its true upstream cause, such as ranking the target gene above the transcription factor that regulates it. Our key idea is to embed this causal structure by routing the integration path along the causal graph. The method thereby decomposes each feature's attribution into a direct effect and effects mediated through its causal descendants. We evaluate CIG in three settings of increasing realism. First, on a synthetic benchmark with a known causal model, CIG's attributions best match the ground-truth causal effect from Pearl's do-calculus, matching the accuracy of causal Shapley values at a fraction of the computational cost. Second, on simulated single-cell gene expression data with a known gene regulatory network (Dyngen), CIG most accurately recovers the transcription factors driving the simulation. Third, on real interferon-$β$ stimulation data, where only an approximate causal graph is available, CIG better prioritizes the transcription factors driving the measured response than DeepSHAP and integrated gradients. Together, these results show that incorporating causal structure into gradient-based attributions recovers upstream drivers that existing methods miss, without sacrificing scalability.

## 6. Functional Subnetwork Localization for Efficient Continual Learning in Large Language Models

- Authors: Shuoran Jiang, Wentao Zhu, Yang Xiang, Dongfeng Li, Yunan Zhang, Mengchen Zhao, Yuhui Guo, Kai Chen, Youcheng Pan, Xiangping Wu, Qingcai Chen
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-15
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 3.2763629694150853
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.21537v1
- PDF: https://arxiv.org/pdf/2610.21537v1
- Local PDF: pdf/2026-10-17_06_Functional Subnetwork Localization for Efficient Continual Learning in Large Language Models.pdf

Biological intelligence continually adapts to new information while retaining prior skills through localized plasticity. In contrast, continual learning in large language models (LLMs) remains vulnerable to catastrophic forgetting. A promising direction is to identify functionally specialized subnetworks within LLMs that enable targeted and resource-efficient adaptation. Using gradient-attribution profiling, we localize cognition-associated functional subnetworks exhibiting extremely low mutual overlap. Building on this finding, we propose Function-isolated Memory-Efficient Optimization (CiMEO), a continual learning framework that routes each training example to its corresponding functional subnetwork, restricting parameter updates and optimizer states to selected regions. Across 1.4 million sequential instructions, CiMEO achieves the highest average performance among the compared methods on five generative benchmarks spanning programming, examination-style tasks, and mathematical reasoning, while mitigating catastrophic forgetting. Subspace-overlap and principal-angle analyses further indicate that localized updates help preserve pre-trained representations, highlighting functional subnetwork localization as a practical approach to efficient and stable continual learning in LLMs.

## 7. CausalCellInfer: Prioritizing Cell‐Type‐Specific Disease Associations From Genetically Predicted Transcriptomes in Biobank Cohorts

- Authors: Liangying Yin, Yujia Shi, Ruoyu Zhang, Yong Xiang, Jinghong Qiu, Pak-Chung Sham, Hon‐Cheong So
- Source: openalex
- Venue type: journal
- Journal: Advanced Science
- Publication status: published
- Publication date: 2026-10-14
- DOI: https://doi.org/10.1002/advs.78197
- Categories: Single-cell and spatial transcriptomics, Genetic Associations and Epidemiology, Bioinformatics and Genomic Networks
- Relevance: 3.164717042600753
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://doi.org/10.1002/advs.78197
- PDF: https://onlinelibrary.wiley.com/doi/pdfdirect/10.1002/advs.78197
- Local PDF: Not downloaded

Integrating single-cell RNA sequencing(scRNA-seq) with the phenotypic depth of population-scale biobanks is essential for elucidating the cellular basis of complex diseases. However, this is hindered by limited scRNA-seq sample size and the lack of cellular resolution in biobanks. We present CausalCellInfer, a scalable computational framework bringing cellular resolution to bulk and genotype-imputed transcriptomes. CausalCellInfer employs an invariant causal prediction-inspired method(scRNA-seq-based invariant generalized covariance measure, scI-GCM) to select environment-stable marker genes, a parsimonious deep neural network for cell-fraction deconvolution, and regularized matrix completion to reconstruct cell-type-specific (CTS) expression profiles. This design is optimized for biobank-scale data with technical heterogeneity and limited gene overlap. Validated across simulated data, pseudo-bulk and real peripheral blood mononuclear cell (PBMC) datasets, CausalCellInfer demonstrated superior accuracy and efficiency over existing methods. Applied to ∼500 000 UK Biobank (UKBB) participants across 29 traits, it captured known pathological shifts, such as reduced pancreatic β-cell proportions in type 2 diabetes, and identified novel biological signals, including disrupted excitatory neuron-oligodendrocyte interactions in depression. Inferred CTS differential expression patterns showed significant concordance with independent single-cell studies and were enriched for Open Targets disease genes. Overall, CausalCellInfer bridges single-cell insights and population-scale genomics, enabling systematic discovery of putative disease mechanisms at cellular resolution.

## 8. Optimal Hydra: Model Heterogeneous Federated Learning for LLMs using Data-Informed Hydra-Nets

- Authors: Gwen Legate, Rahaf Aljundi, Eugene Belilovsky
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-14
- DOI: Unavailable
- Categories: cs.LG, cs.AI
- Relevance: 3.1426405499941943
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.20753v1
- PDF: https://arxiv.org/pdf/2610.20753v1
- Local PDF: pdf/2026-10-17_08_Optimal Hydra_ Model Heterogeneous Federated Learning for LLMs using Data-Informed Hydra-Nets.pdf

Large language models (LLMs) trained on vast amounts of data have demonstrated impressive performance over a range of tasks, but future performance gains will require increasing amounts of data and compute. Federated Learning (FL) facilitates training on decentralized private data, but client resource limitations can make training impractical, particularly as model sizes continue to expand. These resource constraints make the assumption of a shared server-client architecture impractical. Model heterogeneous FL offers a promising alternative by adapting model size to client capabilities; however, previous work is limited to the pre-training setting, and conclusions on sub-network selection do not necessarily hold for fine-tuning. Furthermore, prior approaches create client sub-networks without considering their unique data distributions, thereby overlooking the opportunity to tailor sub-network architecture to local data. Motivated by evidence that attention heads exhibit task dependency within layer defined feature spaces, we propose Optimal Hydra, a transformer based heterogeneous FL framework for fine-tuning that combines global layer selection with client specific attention head selection, aligned with local data distributions. Optimal Hydra makes explicit use of client data to produce client-specific sub-networks we call Hydra-nets. To our knowledge, this is the first model heterogeneous FL approach tailored to LLM fine-tuning. Experiments on three datasets show significant improvements over baseline methods while also reducing local resource demands.

## 9. GraphBEAT: Graph-based Bucketized Event Aggregation Over Time for Early Risk Stratification of Gastrointestinal Cancers

- Authors: Leo Y. Li-Han, Chris Varghese, Elizabeth B. Habermann, Mark J. Truty, William R. G. Perry, Cornelius A. Thiels, Hojjat Salehinejad
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-15
- DOI: Unavailable
- Categories: cs.LG, cs.AI, eess.SP
- Relevance: 3.1412890921963523
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.22014v1
- PDF: https://arxiv.org/pdf/2610.22014v1
- Local PDF: pdf/2026-10-17_09_GraphBEAT_ Graph-based Bucketized Event Aggregation Over Time for Early Risk Stratification of Gastrointestinal Cancers.pdf

Longitudinal electronic health records (EHRs) contain complementary diagnostic and laboratory information about patient health. However, irregularity, sparsity, heterogeneity, and incompleteness in documentation complicate EHR modeling. To address the problem, we introduce GraphBEAT (Graph-based Bucketized Event Aggregation over Time), a temporal graph representation learning framework that groups clinical events into time buckets and transforms observed features into patient-specific, temporally directed graphs to enable early risk stratification for gastrointestinal cancers. Each node in an EHR graph encodes feature identity, observed value, and temporal position of clinical events. A context-aware, time-decay message-passing mechanism models transitions between successive buckets, followed by multi-head attention pooling to generate patient-level representations. GraphBEAT was trained and evaluated on multi-site longitudinal diagnosis codes and laboratory tests to predict pancreatic, liver, and intestinal cancer at 12-, 24-, and 36-month diagnostic lead times. In all experimental setups, GraphBEAT consistently outperformed baseline graph neural networks (GraphSAGE, GAT, and GCN) and sequence modeling approaches (Transformer and long short-term memory [LSTM]). GraphBEAT also required over 250x fewer floating-point operations per patient and over 20x fewer parameters than the Transformer and LSTM baselines. These results support GraphBEAT as an accurate and computationally efficient approach for cancer risk stratification from sparse, heterogeneous longitudinal health records.

## 10. EigDiff: Eigensample Diffusion - or how to significantly reduce training dataset size with marginal performance variation?

- Authors: Andrei Jarca, Vlad Hondru, Florinel-Alin Croitoru, Radu Tudor Ionescu
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-14
- DOI: Unavailable
- Categories: cs.CV, cs.AI, cs.LG
- Relevance: 3.135146569239221
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.20999v1
- PDF: https://arxiv.org/pdf/2610.20999v1
- Local PDF: pdf/2026-10-17_10_EigDiff_ Eigensample Diffusion - or how to significantly reduce training dataset size with marginal performance variatio.pdf

Diffusion models are notoriously expensive to train, requiring large-scale datasets to learn how to gradually reverse the noise from images over multiple small denoising steps. Current approaches focus on distilling the number of diffusion steps, neglecting potential redundancies of the training data. In this paper, we explore the potential of harnessing eigensamples to train diffusion models on significantly smaller datasets, while preserving model performance. To mitigate the sensitivity to affine transformations of eigenimages, we harness the latent space of a pre-trained CLIP model. We next compute latent eigenvectors by performing principal component analysis (PCA) in CLIP space. Further, we employ eigenvectors as reference points to guide the selection of a representative training set comprising comprising both exemplars (images whose embeddings are closest to eigenvectors) and diverse images. Our comprehensive experiments with different diffusion models applied on multiple datasets indicate that our approach (EigDiff) can reduce training data by up to 14x and accelerate subset selection by up to 1607x, with marginal performance differences.

## 11. CART: Compatible Routing for Multimodal Continual Instruction Tuning

- Authors: Ling-Xiang Zhang, Tao Hu, Da-Wei Zhou
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-15
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 3.123965909620203
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.22137v1
- PDF: https://arxiv.org/pdf/2610.22137v1
- Local PDF: pdf/2026-10-17_11_CART_ Compatible Routing for Multimodal Continual Instruction Tuning.pdf

Multimodal Large Language Models (MLLMs) achieve strong performance through instruction tuning, yet real-world applications often require them to continually acquire new capabilities from sequential tasks, i.e., Multimodal Continual Instruction Tuning (MCIT). In typical MLLMs, a projector is employed to align visual representations with the language model. However, existing methods primarily protect the language model from forgetting while continuously updating the projector across tasks. Such asymmetric adaptation can cause substantial representation drift in the projector, increasing the mismatch between the projector and language model and consequently exacerbating catastrophic forgetting. To address this issue, we propose Compatible Routing (CART), which explicitly coordinates the adaptation of the projector and language model. Specifically, CART maintains task-specific experts for both modules and combines them through weighted mixtures. CART jointly infers their weights by considering both expert relevance and cross-module compatibility, thereby promoting coordinated adaptation between the two modules. To further control model growth, we introduce relevance-guided expert consolidation, which merges experts exhibiting similar relevance profiles across samples within each module. Extensive experiments demonstrate that CART achieves state-of-the-art performance.

## 12. MSP: Modality Self-Play for Training Multimodal LLMs Without Paired Cross-Modal Data

- Authors: Robert Moseley, Md Kaykobad Reza, Ameya Patil, Edward Ayrapetian, Salman Asif
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-14
- DOI: Unavailable
- Categories: cs.AI, cs.CV
- Relevance: 3.0994795894475335
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.20965v1
- PDF: https://arxiv.org/pdf/2610.20965v1
- Local PDF: pdf/2026-10-17_12_MSP_ Modality Self-Play for Training Multimodal LLMs Without Paired Cross-Modal Data.pdf

Large multimodal models have achieved remarkable progress by scaling model capacity and training on massive paired multimodal data. However, this paradigm introduces a fundamental bottleneck: aligned multimodal datasets are expensive to curate, difficult to scale across diverse modality combinations, and increasingly constrain further progress. We introduce Modality Self-Play (MSP), a training framework for multimodal foundation models based on proxy-mediated modality composition. Instead of relying on paired cross-modal data, MSP uses anchor-supporting proxy textual descriptions of unseen modalities as semantic bridges during training. Given an observed modality (e.g., image or audio), the model generates proxy descriptions for complementary unseen modalities, which are then encoded and aligned with the observed modality through learned bridges, enabling cross-modal interaction without real paired non-text supervision.
  Our central hypothesis is that proxy text, combined with contrastively trained pretrained encoders, provides sufficient semantic structure for multimodal composition to emerge. We show that MSP enables zero-shot modality composition: models trained only with a real anchor modality and accompanying proxy descriptions can integrate and reason over multiple modalities at inference time despite never observing real paired non-text data during training. Empirically, MSP achieves state-of-the-art or competitive performance on multiple multimodal benchmarks. Ablation studies further demonstrate that learned bridges improve alignment, while anchor-supporting proxy descriptions enable effective cross-modal composition. MSP removes the need for real paired non-text (e.g., audio-vision) supervision, while continuing to rely on modality-text pairs, pretrained contrastive encoders, and modality-distribution bridge calibration.

## 13. Semantic Latent Alignment for Flow Matching with Invertible Bi-Lipschitz Adapters

- Authors: Felix Nützel, Mischa Dombrowski, Luca Hagen, Bernhard Kainz
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-15
- DOI: Unavailable
- Categories: cs.CV, cs.LG
- Relevance: 3.0916055834928575
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.21332v1
- PDF: https://arxiv.org/pdf/2610.21332v1
- Local PDF: pdf/2026-10-17_13_Semantic Latent Alignment for Flow Matching with Invertible Bi-Lipschitz Adapters.pdf

Pretrained latent spaces trade compression, reconstruction, and the learnability of the coordinates a downstream generator has to work in, which complicates adapting these spaces to different domains or tasks: continued training is expensive, and without a new alignment objective it often fails to improve downstream generation. We instead leave the encoder and decoder fixed and change only the coordinates between them, using an invertible bi-Lipschitz adapter aligned offline to a semantic teacher and frozen during class-conditional flow matching. Invertibility preserves compatibility with the pretrained autoencoder, while the bi-Lipschitz constraint limits how far alignment can distort its latent geometry. This provides a simple way to improve semantic organization while retaining the compression and reconstruction properties of the original latent space. On two medical imaging datasets, constrained latent adaptation improves feature metrics, seed stability and counterfactual edit strength, while remaining competitive on downstream classification. In contrast, unconstrained adaptation can become highly anisotropic and sensitive despite remaining invertible, highlighting the importance of controlling geometric distortion. Our results suggest that carefully constrained post-hoc adaptation offers a parameter-efficient and tuning-free alternative to jointly modifying the representation during generative training.

## 14. SSR: Structural Signal Retriever for Scalable Agent Discovery in LLM-Orchestrated Multi-Agent Systems

- Authors: Giancarlo Maldonado Cárdenas, Carlos A. Astudillo, Nelson L. S. da Fonseca
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-15
- DOI: Unavailable
- Categories: cs.MA, cs.AI, cs.IR
- Relevance: 3.087033268476514
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.21113v1
- PDF: https://arxiv.org/pdf/2610.21113v1
- Local PDF: pdf/2026-10-17_14_SSR_ Structural Signal Retriever for Scalable Agent Discovery in LLM-Orchestrated Multi-Agent Systems.pdf

Large-scale multi-agent ecosystems require mechanisms for discovering suitable agents without exposing entire registries to a large language model (LLM) orchestrator. The challenge is not only to retrieve relevant Agent Cards from a growing registry, but also to maintain a compact candidate context, since each additional candidate increases prompt size, inference cost, latency, and the risk of exceeding the model context window. We formulate this problem as candidate-context scalability and propose the Structural Signal Retriever (SSR), our deterministic and training-free retrieval method designed for Agent Card discovery. SSR derives structural lexical signals from capability-bearing Agent Card fields, weights them using inverse document frequency (IDF), and uses an Inverted Signal Index (ISI) for selective candidate scoring. We evaluate SSR using a synthetic agent benchmark, a public MS MARCO adaptation, and end-to-end LLM orchestration. At 1,000 agents, SSR reduces LLM input by 98.8% and orchestration latency by 70.9% relative to full-catalog orchestration. On MS MARCO, IDF improves retrieval effectiveness within the structural representation, while the ISI preserves retrieval effectiveness and reduces explicitly scored passages by 96.8%. End-to-end experiments show that candidate pre-selection maintains a compact candidate context as registry size grows and avoids the operational failures observed with full-catalog orchestration. These results support SSR as an Agent-Card-native, traceable retrieval mechanism for candidate-context scalability.

## 15. Recursive Offline Distillation via Entropy Gain Sampling and Answer Mixing

- Authors: Andrey Goncharov, Daniil Vyazhev, Simon Epanov, Alexey Zaytsev
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-14
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.052994541619954
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.20914v1
- PDF: https://arxiv.org/pdf/2610.20914v1
- Local PDF: pdf/2026-10-17_15_Recursive Offline Distillation via Entropy Gain Sampling and Answer Mixing.pdf

Distillation of reasoning chains from Large Language Models (LLMs) into their smaller siblings is a standard training approach. Frequently, researchers do not have full access to a teacher model and its internal representations, which limits the resulting performance. We propose a recursive offline distillation method combining two components: entropy-based sampling for selective distillation and answer mixing. Specifically, for three open models (3-4B), at each epoch, we sample reasoning chains weighted by entropy difference with an auxiliary medium model (70-72B) and, next, supplement thinking traces with single-token ground truth answers. Our approach consistently outperforms naive distillation with comparable data budgets ($57.15 \pm 1.01$ vs 51.61 on average) and offers a much steeper learning curve. Additionally, we present a comparative analysis of methods to generate and normalize distillation traces.

## 16. Librarian Agents: Training LLMs to Curate Long-Context Workspaces that Anticipate Future Queries

- Authors: Anikait Singh, Teresa Zhang, Yoonho Lee, Roshen Sanjay Nair, Aviral Kumar, Chelsea Finn
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-15
- DOI: Unavailable
- Categories: cs.LG, cs.AI, cs.CL
- Relevance: 3.032241093394968
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.22273v1
- PDF: https://arxiv.org/pdf/2610.22273v1
- Local PDF: pdf/2026-10-17_16_Librarian Agents_ Training LLMs to Curate Long-Context Workspaces that Anticipate Future Queries.pdf

Reasoning over long document contexts remains a challenge for large language models (LLMs). Standard retrieval methods are inherently reactive, bottlenecking agents with complex, cross-document reasoning at inference time, while precomputed structures like knowledge graphs often fall short because they rely on rigid heuristics. Instead, can we allow agents to perform anticipatory directed curation: learning to proactively reorganize unstructured corpora prior to inference to efficiently serve diverse future queries. We build on a key asymmetry in modern agentic harnesses (e.g., Claude Code): while LLM agents are adept at navigating existing filesystems to solve an immediate task, they are rarely trained to construct reusable workspaces for future use. To instantiate this capability, we introduce Librarian Agents, a framework in which a builder agent transforms raw documents into a hierarchical filesystem of synthetic files and reference links, which forms a workspace tailored for a downstream answering agent. We formulate workspace construction as a Markov decision process and optimize the builder policy via reinforcement learning to directly maximize downstream answering accuracy. Empirically, Librarian Agents outperforms the strongest retrieval and precomputation baselines by 33 percentage points on BrowseComp-Plus, amortizes upfront construction costs across repeated queries, and generalizes zero-shot to unseen domains on BRIGHT with a 31-point average accuracy improvement.

## 17. Pixels to Tokens: Token Space Efficient Active Learning for Low-Budget Semantic Segmentation

- Authors: Utku Cicek, Mahip Singh, Ziyao Shang, Kimathi Kaai, C Thomas, Pedro Pablo Guerrero Vela, Alexander Wong, Sirisha Rambhatla
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-14
- DOI: Unavailable
- Categories: cs.CV, cs.LG
- Relevance: 3.025460798685424
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.20881v1
- PDF: https://arxiv.org/pdf/2610.20881v1
- Local PDF: pdf/2026-10-17_17_Pixels to Tokens_ Token Space Efficient Active Learning for Low-Budget Semantic Segmentation.pdf

While foundation models and vision transformers (ViTs) have redefined visual representations, current active learning (AL) strategies for these backbones largely operate at the patch or region level, where annotation requirements remain high due to extensive pixel labeling. Extending ViT-based AL to the pixel-level, low-budget regime is uniquely challenging: with as little as one pixel query per image, a method must simultaneously identify the most informative locations and train a reliable decoder head from an extremely sparse signal. We introduce TEAL (Token-space Efficient Active Learning), the first pixel-level AL framework built around ViT representations. TEAL uses a frozen ViT backbone and performs diversity-based selection directly on its native token lattice, avoiding the artifacts introduced by interpolating token embeddings to dense pixel resolutions. Our framework applies a two-level MaxHerding strategy over multi-layer token descriptors to select representative candidates, followed by margin-based uncertainty refinement on a finer decoder grid. Across CamVid, Cityscapes, ADE20K, and Pascal Context, TEAL consistently outperforms previous baselines under extreme label scarcity, improving over the strongest baseline by up to +24.36 mIoU with a single labeled pixel (px) per image, and reaching up to 97% of fully supervised performance with just 10 px. To rigorously establish the source of the gains, we further show that the improvements persist when all baselines are equipped with the same DINOv3 backbone, demonstrating that coupling token-space selection with uncertainty refinement on the decoder grid makes ViT token geometry an effective foundation for extremely low-budget active segmentation.

## 18. Explaining the Roles of Experts in Mixture-of-Experts LLMs for Personalization

- Authors: Sekh Mainul Islam, Pepa Atanasova, Isabelle Augenstein
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-15
- DOI: Unavailable
- Categories: cs.CL, cs.AI
- Relevance: 3.0217949861148865
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.22127v1
- PDF: https://arxiv.org/pdf/2610.22127v1
- Local PDF: pdf/2026-10-17_18_Explaining the Roles of Experts in Mixture-of-Experts LLMs for Personalization.pdf

Personalization of Large Language Models (LLMs) is increasingly important for user-centric applications, yet prior methods mainly adapt dense LLMs, whose polysemantic neurons, each encoding multiple unrelated concepts, hinder localizing the components behind personalization, and thus understanding and controlling it. We propose to personalize Mixture-of-Experts (MoE) LLMs, which sparsely route each token to a few specialized experts, reducing polysemanticity and enabling such localization. We adapt three open-weight MoE LLMs on a large-scale personalization dataset and train crosscoders on paired activations of the personalized and non-personalized models to learn interpretable personalized latents, from which we identify the experts encoding distinct personalization features. The personalized MoE LLMs perform competitively with dense LLMs while activating only a fraction of their parameters, exhibit lower polysemanticity than dense LLMs with similar active parameters, and, within the same model family, yield personalized latents that are less shared with the non-personalized model. Causal interventions show that these latents suffice to recover the personalized model's behavior and that boosting their associated experts moves the non-personalized model toward it, revealing distinct routing paths for different personalization features.

## 19. Two-Stage Score Estimation for Group-Specific Diffusion Models

- Authors: Huitao Yang, Oscar Hernan Madrid Padilla
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-14
- DOI: Unavailable
- Categories: stat.ML, cs.LG, math.ST
- Relevance: 3.019681524389565
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.20979v1
- PDF: https://arxiv.org/pdf/2610.20979v1
- Local PDF: pdf/2026-10-17_19_Two-Stage Score Estimation for Group-Specific Diffusion Models.pdf

Generative modeling across related distributions raises a question: how can shared structure support accurate generation for a target distribution with limited observations? We develop a statistical framework for diffusion transfer that analyzes a shared pooled score together with a target-specific offset. Under Besov regularity of the pooled density and a stable hierarchical composition model for the offset, we derive convergence rates that separate the costs of learning these components and identify when a simpler offset yields a faster risk-bound rate than separate fitting. Under suitable boundary and regularity assumptions, we prove that the offset remains bounded and jointly regular as diffusion time approaches zero. These results allow the lower time cutoff to vanish polynomially and provide total-variation guarantees for diffusion models as density estimators. Synthetic simulations and image benchmarks provide a proof of concept for the framework.

## 20. N-Gram Memories at Two Bits: Quantizing Lookup Tables in Large Language Models

- Authors: Donghoon Han, Minseop Jung, Dong Woo Kwak, SeungJae Lee, Junhoo Lee
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-15
- DOI: Unavailable
- Categories: cs.LG, cs.CL
- Relevance: 3.0058866851405885
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.21810v1
- PDF: https://arxiv.org/pdf/2610.21810v1
- Local PDF: pdf/2026-10-17_20_N-Gram Memories at Two Bits_ Quantizing Lookup Tables in Large Language Models.pdf

Conditional memory expands language-model capacity through selective lookup, but the full embedding table must remain available for every possible input. We introduce Conditional Program (CP), a compressed representation that reconstructs only the rows an input requests. CP represents each row by a short code and a local scale, with a reconstruction program shared across the table. We instantiate this representation with a Gaussian trellis, norm restoration and independently decodable row records. CP's two-bit code lowers output KL by 41--63\% relative to 2-bit round-to-nearest. Analysis across three trained n-gram memory families shows that Gaussian-like coordinate statistics coexist with learned relationships among rows; at matched storage budgets, the shared trellis outperforms the fitted codebooks and low-rank residual variants we test. For DeepSeek, it reduces table storage from 203GB to 51GB, leaving room for larger workloads when the table is kept on GPU.

## 21. ManiFusion: Unlocking the High-Throughput Generation via Superposition in Manifold Space

- Authors: Minkyu Kim, Baekseung Kim, Junhoo Lee, Jangho Kim, Nojun Kwak
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-15
- DOI: Unavailable
- Categories: cs.CV, cs.LG
- Relevance: 3.000257659021646
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.21433v1
- PDF: https://arxiv.org/pdf/2610.21433v1
- Local PDF: pdf/2026-10-17_21_ManiFusion_ Unlocking the High-Throughput Generation via Superposition in Manifold Space.pdf

Diffusion models achieve high-quality image generation but remain computationally expensive due to iterative denoising across many timesteps. Existing acceleration methods mainly reduce per-sample latency, but gains along this axis are becoming saturated. We instead explore an orthogonal throughput-oriented direction by processing multiple samples within a single denoising evaluation. To this end, we propose ManiFusion, a backbone-agnostic framework for multi-sample generation through fused-space computation. ManiFusion jointly processes multiple samples by fusing them before the denoising backbone and separating them afterward through unfusion. We provide a geometric perspective on how multiple samples can share a fused representation while retaining the information needed to guide their individual generation trajectories. To better align fusion allocation with denoising stages, ManiFusion uses Trajectory-Fusion Scheduling (TFS), which dynamically adjusts fusion factors throughout sampling. ManiFusion generalizes across diffusion families, including both U-Net and transformer backbones in pixel and latent spaces. We further show that ManiFusion composes with existing acceleration methods and reaches throughput regimes unattainable by prior approaches with minimal quality degradation.

## 22. Rethinking the Role of Tool Graph Memory in Multi-Turn Tool Use

- Authors: Uiji Hwang, Richeng Xuan, Taeuk Kim
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-15
- DOI: Unavailable
- Categories: cs.CL, cs.AI
- Relevance: 2.9559910224427783
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.21571v1
- PDF: https://arxiv.org/pdf/2610.21571v1
- Local PDF: pdf/2026-10-17_22_Rethinking the Role of Tool Graph Memory in Multi-Turn Tool Use.pdf

Large language model (LLM) agents solve complex tasks by calling external tools over multiple turns. Recent work has proposed tool graph memory, which stores past experience as tool transitions to guide subsequent selection. However, it remains unclear whether this component consistently improves agents' tool use or undermines it. We evaluate tool graph memory on nine models and two benchmarks, finding that it seldom improves significantly over baselines, and that its gains, where present, cost over twice the LLM calls. The memory's guidance is often incorrect, and random or no guidance retains most of the gain, implying that the benefit stems from extra computation rather than the memory itself. Moreover, even with the correct next tool suggested, many failures remain, such as giving up without a tool call. Storing the same experience instead as textual insights outperforms tool graph memory with almost no extra LLM calls. This suggests that memory serves better as a soft prior than as a prescription of the next tool, leading to a more effective and generalizable solution.

## 23. OmicsBench: a long-horizon multi-turn benchmark of AI agents on research-study-scale bioinformatics

- Authors: Gideon Shaked, Siddharth Nagisetty
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-15
- DOI: Unavailable
- Categories: cs.AI, q-bio.GN, q-bio.QM
- Relevance: 2.9532246692069215
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.21074v1
- PDF: https://arxiv.org/pdf/2610.21074v1
- Local PDF: pdf/2026-10-17_23_OmicsBench_ a long-horizon multi-turn benchmark of AI agents on research-study-scale bioinformatics.pdf

Computational biologists increasingly delegate substantial analyses to AI agents in long-horizon, multi-turn sessions, yet most benchmarks of agents' bioinformatics capabilities pose a single short task with a single-shot prompt. We present OmicsBench, a long-horizon, multi-turn bioinformatics benchmark for AI agents. Each of its 97 tasks links dependent subtasks into a directed acyclic graph, for 662 underlying subtasks in all. Each subtask is posed as one user turn and graded deterministically against an answer key, with optional in-context feedback on incorrect answers. Across 12 models on three harnesses, the slowest agent averages 3.6 hours per task, and no combination comes near saturating the benchmark, with mean scores of 0.43 to 0.57 out of a possible 1 without in-context feedback and 0.54 to 0.67 with it. Multi-turn evaluation also uncovers behavior that single-shot prompts cannot, as agents score lower on subtasks that depend on earlier subtasks, and in-context feedback helps agents recover some of that loss. Because deterministic scoring gives no qualitative account of how an agent failed, we also introduce an unsupervised failure mode discovery pipeline that describes, embeds, and clusters agents' failed attempts to surface emergent failure modes. Applied to OmicsBench, this pipeline exposes qualitative shortcomings in how agents carry out bioinformatics analyses, ranging from agents applying their own statistical filters in place of the specified ones to agents writing whole answers from memory.

## 24. CARA: Causally Guided Retrieval Agent for Question Answering

- Authors: Weicheng Liu, Xiangcheng Wu, Depeng Xu, Haopeng Zhang, Xi Niu
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-15
- DOI: Unavailable
- Categories: cs.AI, cs.IR
- Relevance: 2.928898111717886
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.22017v1
- PDF: https://arxiv.org/pdf/2610.22017v1
- Local PDF: pdf/2026-10-17_24_CARA_ Causally Guided Retrieval Agent for Question Answering.pdf

Retrieval-augmented generation over text-rich knowledge graphs requires identifying evidence that contributes to answering a question, rather than merely matching its textual content. Existing agentic retrievers adaptively balance global search and multi-hop exploration but primarily rely on textual similarity to guide retrieval. We propose CARA, a training-free, CAusally guided Retrieval Agent that explicitly evaluates the causal relevance of retrieved evidence through two complementary criteria: consequentiality, measuring whether adding evidence improves answerability, and essentiality, assessing whether removing evidence weakens answerability. CARA integrates these assessments with path consistency to guide graph exploration and employs reciprocal rank fusion to aggregate evidence from multiple agents. We evaluate CARA on three STaRK datasets and augment STaRK with ground-truth answers to enable downstream question answering evaluation. Experimental results demonstrate that CARA consistently outperforms existing retrievers. CARA also improves answer quality and faithfulness while examining fewer graph nodes and requiring fewer retrieval operations. These findings demonstrate that causal relevance assessment enables more focused and effective agentic graph retrieval, improving both retrieval performance and downstream question answering.

## 25. Graph Dirichlet Energy for Fitting-Free Bivariate Causal Inference

- Authors: Povilas Daniušis
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-15
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 2.925492701315739
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.21892v1
- PDF: https://arxiv.org/pdf/2610.21892v1
- Local PDF: pdf/2026-10-17_25_Graph Dirichlet Energy for Fitting-Free Bivariate Causal Inference.pdf

We propose the Graph Dirichlet Energy Causal Inference (GDECI) criterion for distinguishing cause from effect in bivariate settings. For a candidate direction $X\to Y$, we construct a kernel similarity graph from $X$ and treat $Y$ as a graph signal. The score is the Dirichlet energy of this signal, induced by the unnormalized graph Laplacian. The reverse score swaps the variables, and the lower-energy direction is inferred as causal. The method requires neither regression fitting nor independence testing. After the empirical probability integral transform, its decisions are invariant under strictly monotone transformations of either variable, and the graph operations reduce to convolutions, allowing exact evaluation in $O(n\log n)$ time and $O(n)$ memory. At the population level, GDECI compares degree-weighted Bayes squared prediction errors plus a non-negative smoothness term of the regression function. As the bandwidth tends to zero, the weights become uniform and the smoothness term vanishes, reducing the criterion to a RECI-type comparison of expected conditional variances in copula space. Empirically, we compare GDECI with QCCD, GRCI, CAM, IGCI (two variants), RESIT, LOCI, QPE-k, and RECI (two variants), in accuracy on 1899 cause--effect pairs and in inference speed. GDECI ranked fifth of eleven methods in macro-averaged accuracy on 12 synthetic suites ($0.776$). On the real-world Tuebingen pairs, it ranked third in unweighted accuracy ($0.684$) and fifth in weighted accuracy ($0.678$). It was also the fastest of the compared methods up to $n\approx10^{4}$. The accompanying code repository: https://github.com/povidanius/gdeci.

## 26. GraphACM: Graph-based Action Consistency Measurement for Uncertainty Quantification in LLM Agents

- Authors: Yaxin Ma, Wenbo Zhang, Satya Krishna Pothapragada, Alina Zare
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-15
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 2.9103920998063493
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.22031v1
- PDF: https://arxiv.org/pdf/2610.22031v1
- Local PDF: pdf/2026-10-17_26_GraphACM_ Graph-based Action Consistency Measurement for Uncertainty Quantification in LLM Agents.pdf

Behavioral consistency across repeated executions provides an informative signal for assessing the reliability of large language model (LLM) agents. However, existing approaches typically summarize consistency with a single task-level score, without identifying where behavioral differences occur or whether actions are compared under equivalent decision contexts. We propose a graph-based framework for fine-grained behavioral consistency measurement and uncertainty quantification. Given multiple rollouts of the same task, we merge equivalent states into a directed, action-labeled graph, enabling action comparisons at shared decision states. We introduce node-level and global measures of action consistency, using the global consistency score as a proxy for uncertainty to predict task success or failure. Experiments across three LLMs on ALFWorld, AppWorld, and WebShop demonstrate that our measure is positively associated with task success and achieves an average AUROC of 0.811 for task-success prediction, outperforming the strongest behavioral-consistency baseline (0.729) and verbalized confidence (0.769). These results highlight the effectiveness of state-conditioned behavioral consistency and pinpoint where agent actions agree.

## 27. Attention over noisy examples: generalization and memorization in the exponential Hopfield network

- Authors: Francesco Alemanno
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-15
- DOI: Unavailable
- Categories: cond-mat.dis-nn, cs.LG, cs.NE
- Relevance: 2.8692453140356218
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.22191v1
- PDF: https://arxiv.org/pdf/2610.22191v1
- Local PDF: pdf/2026-10-17_27_Attention over noisy examples_ generalization and memorization in the exponential Hopfield network.pdf

In Hebbian learning from examples a Hopfield network of $N$ neurons is not supplied with the $K$ archetypes it has to retrieve but with $M$ blurred examples of each, of quality $r$, and whether it can infer them depends on the load $α=K/N$ (interference among them) and on the dataset entropy $ρ=(1-r^2)/(Mr^2)$ (how little the examples say about them). We transfer this protocol to the exponential Hopfield model, whose zero-temperature update is a step of softmax attention with the unlabelled examples as keys. A signal-to-noise analysis gives in closed form the overlap between the output and an unseen archetype, $m^{(1)}={\rm erf}(1/\sqrt{2ρ_{\rm eff}})$: the majority-rule law of the pairwise model at small load, with $ρ$ replaced by an attention entropy $ρ_{\rm eff}$ built from the weight the softmax gives to the correct class and the number of examples it spreads it over. Two consequences follow. First, in a window of inverse temperatures $β$ that widens as $\sqrt N$ the interference between archetypes is exponentially small in $Nβ$: the load drops out and the number of archetypes that can be learnt grows as $\exp(c\sqrt N)$. Second, learning fails differently: in the pairwise model through a spin-glass phase, in the exponential model through memorization: the softmax concentrates its weight on the training example closest to the input and returns it in place of the archetype. Seen from the input the softmax weights are those of the random energy model, and memorization is its freezing transition, at $β\sqrt{N(1-r^2)}\simeq\sqrt{2\ln M}$; it is measurable on a head whose keys are examples as the number of examples carrying weight. On MNIST the diagnostic follows the random-energy prediction; on fashion-MNIST it detects sub-clusters in the classes, and the best accuracy lies beyond the memorization threshold, where the softmax reads out a local sub-prototype.

## 28. Designing Transformers for Continuous Diffusion Language Models

- Authors: Weijian Luo, Yujian Chen, Hao Jiang, Guang Cheng, Tianyang Hu
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-15
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 2.84107786262674
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.22330v1
- PDF: https://arxiv.org/pdf/2610.22330v1
- Local PDF: pdf/2026-10-17_28_Designing Transformers for Continuous Diffusion Language Models.pdf

Continuous diffusion language models (CDLMs) offer an alternative approach to parallel language generation; however, most existing studies directly use transformer architectures from either causal large language models (LLMs) or Diffusion Transformers (DiTs) for image generation, which were not optimized for CDLMs. In this paper, we conduct a systematic study on Transformer architectures for CDLMs and introduce Language Diffusion Transformer (LangDiT), combining feature and query-key normalization, wider noise conditioning, likelihood-shortcut gradient routing and calibration, and confidence-gated training self-conditioning. LangDiT significantly reduces generation perplexity in matched LangFlow comparisons, establishing a new state of the art in continuous language generation across different model formulations. Using LangFlow as a representative CDLM, LangDiT as a plug-and-play backbone leads to a new state-of-the-art model with a generation perplexity (GenPPL) of 21.72 using 1024 NFEs and 44.72 GenPPL using 128 NFEs on the unconditional generation of 1024-token sequences on the OpenWebText dataset. When adapted to Plaid-style CDLM formulations, LangDiT results in a new leading GenPPL of 11.33 using 1024 denoising NFEs, and 27.51 GenPPL using 128 denoising NFEs. These gains are achieved while retaining each model's underlying representation, training objective, and inference sampler, isolating transformer architecture as a fundamental source of improvement. Our study identifies architectural design as an important source of improvement in continuous diffusion language models.

## 29. Ontology Refinement with Embeddings and LLMs: A Case Study on CASTON

- Authors: Hui Yang, Ziyu Li, Xuan Liu, Anders Jarfors, He Tan, Jiaoyan Chen
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-15
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 2.8230164547600367
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.21466v1
- PDF: https://arxiv.org/pdf/2610.21466v1
- Local PDF: pdf/2026-10-17_29_Ontology Refinement with Embeddings and LLMs_ A Case Study on CASTON.pdf

Ontologies are widely used to represent and organize complex knowledge in domains such as biomedicine and healthcare. However, constructing reliable ontologies remains challenging, as class hierarchies, whether manually or automatically constructed, may contain subtle subsumption errors that require careful refinement. We study this problem in CASTON, a casting-domain ontology, and present a lightweight but scalable refinement workflow that combines a fine-tuned ontology embedding model with Large Language Models (LLMs). The embedding model is used to extract a limited number of candidate axioms for refinement together with possible replacement candidates, and an LLM then returns repair suggestions. In a small expert evaluation, the default configuration using a CASTON-fine-tuned OnT embedding model and Qwen3-8B produced reliable high-confidence repairs: all six high-confidence replacements were accepted by both domain experts. The implementation is available at https://github.com/HuiYang1997/OntRefine.

## 30. SelectPFN: Amortized Bayesian Variable Selection for Sparse Nonlinear Regression with Prior-Data Fitted Networks

- Authors: Bin Luo
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-15
- DOI: Unavailable
- Categories: stat.ML, cs.LG
- Relevance: 2.820299304072263
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.21950v1
- PDF: https://arxiv.org/pdf/2610.21950v1
- Local PDF: pdf/2026-10-17_30_SelectPFN_ Amortized Bayesian Variable Selection for Sparse Nonlinear Regression with Prior-Data Fitted Networks.pdf

Tabular foundation models based on prior-data fitted networks (PFNs) predict on a new data set in a single forward pass, but they cannot report which inputs their predictions depend on. We propose SelectPFN, a PFN that performs Bayesian variable selection and prediction jointly for sparse nonlinear regression. In one forward pass it returns posterior inclusion probabilities for every variable, and its predictions are computed from sampled subsets only, so excluded variables provably cannot affect them; we show this is exactly what the Bayesian model prescribes. The network is pretrained once on synthetic tasks from a meta-prior built around a group spike-and-slab sparse-input neural network. Column-permutation equivariance combined with random interleaving of original and knockoff columns yields knockoff statistics with exact finite-sample false discovery rate control, even when the meta-prior is wrong. We develop theory for amortized selection: a Bayes-regret bound for the amortized median probability model, a characterization showing that the information needed to detect a variable grows like $(2/λ)\log(1/ω)$ in the prior weight $ω$ of structures that can use it, where $λ\le1$ is an efficiency, and a negative result showing that average-case training does not transfer to frequentist guarantees at a fixed truth. On out-of-prior nonlinear designs with p up to 500, SelectPFN improves the area under the precision-recall curve by 0.23-0.28 over the lasso, BART, DART, LassoNet and a group-penalized sparse neural network, at a false discovery proportion of about 0.07 and 0.04 seconds per data set. The advantage persists on real covariate matrices, and, as the theory predicts, detection of interaction-only variables rises monotonically with their prior weight.
