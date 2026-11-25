# Paper Daily Reading - 2026-11-25

## 1. THETA: Heat Diffusion as a Structural Prior for Cross-Domain Transfer in Graph Foundation Models

- Authors: Haonan Liu, Shuo Wang, Zhao Kang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-22
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.8058071212339395
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.29210v1
- PDF: https://arxiv.org/pdf/2611.29210v1
- Local PDF: pdf/2026-11-25_01_THETA_ Heat Diffusion as a Structural Prior for Cross-Domain Transfer in Graph Foundation Models.pdf

Graph foundation models (GFMs) aim to learn transferable representations across domains with heterogeneous node attributes and graph structures. However, relations inferred from node attributes can rely on domain-specific feature semantics, limiting their transferability to unseen graphs, particularly in low-label regimes. We propose THETA (Topology-aware HEat-based TrAnsfer), a graph foundation model that leverages Heat Kernel Signatures (HKS) as a topology-based structural prior for cross-domain transfer. By characterizing nodes' heat-return behavior across diffusion scales, HKS provides a common structural descriptor across graphs without requiring aligned attribute semantics, complementing feature-based relations with information about local and multiscale connectivity. THETA incorporates this prior into both pre-training and few-shot adaptation. During pre-training, it combines HKS with node attributes to construct refined graph views and trains a shared encoder via contrastive learning. During adaptation, it uses HKS to guide edge-weight adjustment and prototype refinement while keeping the encoder frozen and retaining the contribution of labeled support nodes. Through HKS, THETA uses structural information from heat diffusion to guide both representation learning and few-shot adaptation with unlabeled target-domain data. Extensive experiments across diverse graph domains demonstrate that THETA consistently outperforms existing baselines on downstream tasks, highlighting the value of heat diffusion as a structural prior for transferable graph representations.

## 2. LeCellModel: Interpretable Density Estimation over the Gene Expression Manifold

- Authors: Gil Karin, Artemii Bakulin, Nir Yosef
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-23
- DOI: Unavailable
- Categories: q-bio.GN, cs.LG
- Relevance: 3.453630562705273
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.30955v1
- PDF: https://arxiv.org/pdf/2611.30955v1
- Local PDF: pdf/2026-11-25_02_LeCellModel_ Interpretable Density Estimation over the Gene Expression Manifold.pdf

Representation learning for single-cell RNA-seq has been evaluated by the identities representations capture -- cell types, lineages, perturbations -- rather than how faithfully they model the distribution of cell states on the gene expression manifold. As a result, density estimation, rare-state detection, perturbation scoring, and gene-level attribution are bolted onto frozen embeddings as separate models, disconnected from the geometry of the data. We argue that modeling the distribution of cell states should be the primary objective, and that representation quality follows from it. Building on LeJEPA, whose SIGReg objective enforces a provably optimal isotropic Gaussian latent, we introduce LeCellModel, which reads the encoder's Jacobian log-volume (JEPA-SCORE) under this Gaussian latent as a relative typicality score. Across several datasets, LeCellModel outperforms established methods on the scIB benchmark for representation quality. Furthermore, we show that LeCellModel enables detection of rare expression states using JEPA-SCORE as a typicality measure, applying it to a controlled cytokine panel, where it identifies stimulated cells across minority fractions and tracks pathway-response magnitude. We introduce gene-level interpretability of the typicality score -- to our knowledge, the first method for analyzing JEPA-SCORE in feature space. Leveraging this framework, LeCellModel recapitulates the known association of a profibrotic macrophage program with idiopathic pulmonary fibrosis, and discovers a CD177+ activated regulatory T cell subpopulation previously described only in tumor contexts. Both findings emerge directly from the geometry of the learned embedding, without relying on supervised annotations.

## 3. Vasicek Graph Diffusion Model

- Authors: Junyi Tang, Chang Liu, Kun Zhan
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-23
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.4447731375296486
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.30605v2
- PDF: https://arxiv.org/pdf/2611.30605v2
- Local PDF: pdf/2026-11-25_03_Vasicek Graph Diffusion Model.pdf

Diffusion-based graph generation models progressively transform Gaussian noise into structured graphs through stochastic dynamics. We observe that the effectiveness of this transformation is fundamentally determined by the evolution of the diffusion trajectory. Existing graph diffusion models often suffer from excessive uncertainty during diffusion and delayed growth of the signal-to-noise ratio, causing useful structural information to emerge only in the later stages of generation. To address this issue, we propose the Vasicek Graph Diffusion (VGD), a graph diffusion process derived from the Vasicek dynamics. The key insight of VGD is data-anchored mean dynamics with a closed-form solution, which analytically establishes a continuous transition from Gaussian noise to the target graph distribution. Unlike conventional graph diffusion processes that rely predominantly on stochastic evolution, VGD introduces a data-anchored drift that continuously steers the latent state toward the target distribution throughout diffusion. As a consequence, VGD maintains a smoothly evolving uncertainty while rapidly increasing the signal-to-noise ratio throughout diffusion, allowing informative graph structures to emerge much earlier during generation. Extensive experiments on multiple graph generation benchmarks demonstrate that VGD outperforms existing diffusion-based graph generative models in terms of generation quality and structural fidelity.

## 4. Learning Multimodal Representations from Partially Paired, Small-Scale Data

- Authors: Merel Kuijs, Till Richter, Rushin H. Gindra, Korbinian Traeuble, Christian Matek, Rebeka Luknárová, Tingying Peng, Fabian J. Theis
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-23
- DOI: Unavailable
- Categories: cs.AI, q-bio.GN
- Relevance: 3.4069366275059676
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.30601v2
- PDF: https://arxiv.org/pdf/2611.30601v2
- Local PDF: pdf/2026-11-25_04_Learning Multimodal Representations from Partially Paired, Small-Scale Data.pdf

Modeling multimodal data from partially paired samples is critical for advancing domains like biomedicine, where vast unimodal datasets and foundation models exist but paired data remains scarce. Existing fusion methods rely on large-scale paired datasets, limiting their use in scenarios with incomplete pairing. We introduce CAMEO, an adversarial learning-based modality fusion framework that integrates modalities from small, partially paired datasets. Combining any pre-trained unimodal encoder with a cross-modal latent alignment mechanism, CAMEO learns shared representations requiring only minimal paired samples. Evaluated on computational pathology tasks such as niche classification and cell type composition prediction, CAMEO achieves superior data efficiency, outperforming contrastive approaches like CLIP in low paired-data regimes, and highlighting the benefits of adversarial alignment when paired annotations are scarce. To facilitate further research, we additionally release a fully annotated HuggingFace dataset comprising three organs and paired image and gene expression modalities. By extending fusion methods to address limited pairing and small-scale datasets, we provide a framework that advances multimodal learning and broadens its applicability to real-world biomedical problems.

## 5. Learning Heterogeneous Reasoning in Large Language Models: From Mode Compatibility to Local Bottlenecks

- Authors: Sunbowen Li, Dandan Song, Shengkun Ma, Xuanning Cao
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-23
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 3.195121767116928
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.30281v1
- PDF: https://arxiv.org/pdf/2611.30281v1
- Local PDF: pdf/2026-11-25_05_Learning Heterogeneous Reasoning in Large Language Models_ From Mode Compatibility to Local Bottlenecks.pdf

Post-training large language models routinely pools reasoning trajectories from diverse teachers or algorithms, yet it remains unclear whether standard supervised fine-tuning (SFT) can learn such heterogeneous strategies without explicit mode conditioning. We study the learnability and local bottlenecks of heterogeneous reasoning through a formal mixture formulation and controlled experiments. We first formalize the representational compatibility of the optimal autoregressive model with latent reasoning mixtures: the target next-token distribution weights modes by their prefix posteriors and concentrates on a single mode once alternative modes assign negligible likelihood to the prefix. In a verifiable symbolic graph-search environment with paired breadth-first and depth-first search trajectories, no consistent disadvantage is observed for unlabeled mixed SFT relative to homogeneous or labeled baselines under matched token budgets while preserving both modes. Scaling across 0.6B--14B models and data budgets largely eliminates global mode confusion, shifting the primary bottleneck to local state-tracking transitions. Because a local mistake affects the final outcome only when subsequent reasoning is sensitive to that step, we find that only a small fraction of local errors are outcome-determining \emph{Critical Reasoning Nodes (CRNs)}, and that single-step repairs at these nodes rescue failing trajectories across symbolic search and natural language benchmarks whenever the model has sufficient downstream competence to complete the remaining derivation. Our environment is open-sourced at https://github.com/Bowen1911/Symbolic_graph_env.

## 6. Learning the Projection onto the Data Support: Distribution Learning that Avoids Memorization

- Authors: Lin Chen, Dejan Slepčev
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-20
- DOI: Unavailable
- Categories: cs.LG, stat.ML
- Relevance: 3.1441748725878735
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.28234v1
- PDF: https://arxiv.org/pdf/2611.28234v1
- Local PDF: pdf/2026-11-25_06_Learning the Projection onto the Data Support_ Distribution Learning that Avoids Memorization.pdf

We introduce a framework for learning distributions supported on manifolds based on estimating the nearest-point projection onto the data support. Specifically, we define an objective functional over a class of functions whose minimizer recovers this projection. The proposed framework automatically adapts to the intrinsic dimension and allows for data supported on unions of manifolds with varying dimensions. The resulting objective can be optimized using standard neural network architectures. We present population-level results establishing recovery of the manifold projection and prove finite-sample Wasserstein generalization bounds. Furthermore, we validate the approach empirically across a range of settings. In contrast to widely used generative models such as diffusion models, whose objectives can be minimized by memorizing training samples, our formulation excludes such behavior. We also introduce a direct memorization metric to verify that the learned projection generates new samples rather than reproducing the training set.

## 7. Reward Tilting via Semantic Noising

- Authors: Rafał Karczewski, Peter Blohm, Markus Heinonen, Vikas Garg
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-22
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.104989986101376
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.29318v1
- PDF: https://arxiv.org/pdf/2611.29318v1
- Local PDF: pdf/2026-11-25_07_Reward Tilting via Semantic Noising.pdf

Steering a generative model toward a desired property typically requires separate fine-tuning for each reward or additional computation during sampling. We propose semantic noising, which conditions generation on a noisy semantic representation of the data. The resulting posteriors correspond to exponential tilts by linear-quadratic rewards in semantic space, allowing a single model to support objectives and strengths chosen after training. A conditional generator can be trained to approximate these posteriors directly, while models that generate semantic representations by diffusion provide analytic tilted denoisers for the same family of rewards. We illustrate semantic noising in three settings. An autoregressive molecular generator trained with semantic noising controls properties individually and jointly, with a better reward--KL trade-off than property-conditioned models. On ImageNet, a joint diffusion model of images and their CLIP embeddings achieves FID comparable to REG, and tilting it toward a higher aesthetic score matches the best of 16 samples at the cost of a single sample. Finally, pretrained factorized models such as Kandinsky 2.2 support the same tilts without retraining.

## 8. TowerBridge: Bridging the Dual-Encoder Modality Gap via Weight-Space Programming

- Authors: Hani Alomari, Md Atabuzzaman, Chris Thomas
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-23
- DOI: Unavailable
- Categories: cs.CV, cs.LG
- Relevance: 3.1017717723034783
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.31233v1
- PDF: https://arxiv.org/pdf/2611.31233v1
- Local PDF: pdf/2026-11-25_08_TowerBridge_ Bridging the Dual-Encoder Modality Gap via Weight-Space Programming.pdf

CLIP-style dual encoders map images and text through two separate towers into a shared embedding space, where the two modalities occupy distinct regions separated by a modality gap. Retrieval fails when wrong matches, or hard negatives, outrank the correct one, and the gap is the usual suspect. Yet removing it post hoc degrades retrieval on every CLIP checkpoint we test. We introduce a paired statistic that identifies directions where the two towers agree more on hard negatives than on matched pairs. Mildly attenuating these directions improves retrieval while largely preserving the gap. We arrive at this correction through weight-space programming: guided by the statistic, an LLM agent inspects both towers and writes closed-form weight edits without backpropagation. Free to edit any component, the agent improves COCO test retrieval on all 13 CLIP checkpoints and edits an output projection in 12 of the 13. We distill and refine its recurring correction into TowerBridge, a closed-form recipe motivated by a first-order analysis of the hard-negative margin. Computed in seconds from 25,000 labelled pairs, it requires no model-specific tuning and leaves the architecture and inference cost unchanged. TowerBridge improves COCO test retrieval by 16.8 RSUM and Flickr30k test retrieval by 6.6 on average across all 21 evaluated CLIP checkpoints, including 8 unseen by the agent, while limiting any drop in ImageNet zero-shot accuracy to 0.5 points. It also reduces hubness on all 21 checkpoints and improves retrieval on 4 of 5 dual encoders from other families.

## 9. Stochastic non-metric MDS for noisy high-dimensional data

- Authors: Sebastian Damrich, Dmitry Kobak
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-21
- DOI: Unavailable
- Categories: cs.LG, stat.ME
- Relevance: 3.0961640094030924
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.28985v1
- PDF: https://arxiv.org/pdf/2611.28985v1
- Local PDF: pdf/2026-11-25_09_Stochastic non-metric MDS for noisy high-dimensional data.pdf

Multidimensional scaling (MDS) constructs low-dimensional embeddings that approximate pairwise distances in a high-dimensional dataset. MDS exists in several flavors, with metric MDS approximating distances directly and non-metric MDS additionally optimizing for an arbitrary monotonic transformation of the high-dimensional distances. Empirically, metric MDS is known to suffer from the curse of dimensionality. Here we extend prior theoretical results for metric MDS on fully uninformative data to a more general case of finite, high-dimensional data with concentrated distances. We show that the metric MDS embeddings of such datasets stay distributionally close to the data-independent limit case. We then show that non-metric MDS is more robust to high-dimensional noise and can yield informative embeddings of such data. While existing implementations of non-metric MDS are slow, we develop a fast implementation using stochastic gradient descent in PyTorch. Using our implementation, we conduct an empirical study using multiple simulated and real-world datasets, including population-genomic and scRNA-seq data, and show that non-metric MDS can strongly outperform other methods in terms of global structure preservation.

## 10. RoFE: Rotated Frozen Embeddings for Low-Data Multimodal Tabular Learning

- Authors: Yihao Qiao, Jiajian Ma, Wushuang Rui, Abhishek Jha, Aarti Darji, Yiqiu Shen
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-23
- DOI: Unavailable
- Categories: cs.LG, cs.CV, stat.ML
- Relevance: 3.0858099407307638
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.31049v1
- PDF: https://arxiv.org/pdf/2611.31049v1
- Local PDF: pdf/2026-11-25_10_RoFE_ Rotated Frozen Embeddings for Low-Data Multimodal Tabular Learning.pdf

Multimodal tabular learning combines tabular data with images and text, often in settings where labeled data are scarce. Tabular foundation models such as prior-data fitted networks (PFNs) offer a promising solution via in-context learning without task-specific training. However, modern image and text encoders produce embeddings with hundreds or thousands of dimensions, far exceeding the number of features encountered during PFN pretraining. Existing approaches bridge this gap using principal component analysis (PCA) to compress frozen embeddings. Surprisingly, we find that this PCA interface can underperform simple linear classifiers when labeled examples are scarce, even though PFNs are designed for small datasets. We identify the underlying failure mechanism: the PFN's per-column standardization removes the variances of the PCA scores. When the PCA keeps every direction of the labeled examples, the examples collapse into a regular simplex in which all pairwise distances are equal. To address this problem, we propose Rotated Frozen Embeddings (RoFE), a training-free method that rotates PCA scores before PFN inference. We theoretically show that rotation makes the column variances nearly equal, so that standardization approximately preserves the embedding geometry. Across image and text classification tasks, encoders, and tabular foundation models, RoFE improves low-data performance over the PCA interface and outperforms baselines that require task-specific training. The improvements also extend to regression.

## 11. Interaction Retention and Output-Likelihood Training in Parallel Sampling

- Authors: Da Li, Bo Jin, Xiaopeng Wei, Hui Wang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-21
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.057503624548648
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.28858v1
- PDF: https://arxiv.org/pdf/2611.28858v1
- Local PDF: pdf/2026-11-25_11_Interaction Retention and Output-Likelihood Training in Parallel Sampling.pdf

Parallel samplers such as masked diffusion language models generate several coordinates per step from conditional marginals and randomize which coordinates are generated together, so even exact conditionals return a distorted distribution. We give an exact local account of this distortion. Around any full-support product law, the Gram operator of the sampler's response is diagonal in the interaction decomposition, and its eigenvalues are retention probabilities: the probability that an interaction has a unique latest-revealed coordinate. This retention spectrum determines the exact frontier between output accuracy and conditional calibration, its regularization path, and the population response of finite-mixture likelihood training. For pairwise interactions it yields a sharp dichotomy. Under homogeneous retention, output-likelihood training is equivalent to a single context gain; heterogeneous retention opens correction directions beyond any scalar, with an advantage bounded by an explicit heterogeneity gap. On binarized digits and MNIST, output-likelihood training within a heterogeneous schedule library lowers calibrated test negative log-likelihood in all twelve paired comparisons, and the gain survives pair-specific recalibration and a stronger path optimizer. For a frozen 169.6-million-parameter masked diffusion language model, serially normalized context gains are 1.070 and 1.056 at 8 and 16 rounds, against the predicted values 1.134 and 1.058.

## 12. Test-Time Latent Computation to Improve Visual Perception in Multimodal Large Language Models

- Authors: Chen Yang, Zheng Fang, Wenqi Fan, Jun Xia
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-23
- DOI: Unavailable
- Categories: cs.CV, cs.AI
- Relevance: 3.0431245130585207
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.30480v1
- PDF: https://arxiv.org/pdf/2611.30480v1
- Local PDF: pdf/2026-11-25_12_Test-Time Latent Computation to Improve Visual Perception in Multimodal Large Language Models.pdf

Recent work on Large Language Models (LLMs) suggests that reasoning capabilities can be enhanced at test time not only through longer token-level reasoning traces, but also through additional computation in latent space. This raises a natural question for Multimodal Large Language Models (MLLMs): can additional computation in latent space improve visual perception at test time? In this work, we first verify that MLLMs contain stable reusable layers that can be re-forwarded at inference time without disrupting normal generation. Based on this observation, we propose \textbf{Lo}ok \textbf{Ba}ck in the \textbf{L}atent \textbf{S}pace (\textbf{Lobals}), a training-free decoding method that identifies the contiguous layer window with the strongest visual-token attention and re-forwards through it, allowing the model to revisit visual evidence in latent space. We demonstrate that this latent-space revisit strategy can improve MLLMs' performance across diverse multimodal settings, including general vision-language tasks, visual hallucination tasks, and vision-centric tasks.

## 13. Interpreting Diffusion Model Activations in Natural Language

- Authors: Yukinori Yamamoto, Kotaro Yoshida, Ryotaro Shimizu
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-21
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.0397002528123203
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.28621v2
- PDF: https://arxiv.org/pdf/2611.28621v2
- Local PDF: pdf/2026-11-25_13_Interpreting Diffusion Model Activations in Natural Language.pdf

Interpreting the intermediate activations of diffusion models (DMs) is key to understanding how they generate images. Existing interpretability methods for DMs provide limited support for open-ended interrogation, making it difficult to extract human-interpretable insights. We extend LatentQA, the task of answering natural-language questions about Large Language Model activations, to DM activations. We introduce the Diffusion-specific Activation Oracle (DAO), which translates DM activations into natural-language answers to open-ended questions about the ongoing generation. Our experiments show that DAO can effectively describe the content of the final image from activations at early denoising steps. Additionally, we demonstrate that DAO captures the structure of the DM's activation space well enough to steer image generation toward target attributes. Furthermore, we show that attribution patching through DAO identifies DM components that contribute to visual attributes specified in natural language. Our code is available at https://github.com/yamanoko/dao/tree/main.

## 14. Contrastive Gradient Guidance for Test-Time Multi-Preference Alignment of Diffusion Models

- Authors: Po-Yi Lu, Jui-Chao Lu, Paul Kuo-Ming Huang, Shih-Hsin Wang, Chun-Liang Li, Hsuan-Tien Lin
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-21
- DOI: Unavailable
- Categories: cs.CV, cs.LG
- Relevance: 3.0216852210949963
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.28764v1
- PDF: https://arxiv.org/pdf/2611.28764v1
- Local PDF: pdf/2026-11-25_14_Contrastive Gradient Guidance for Test-Time Multi-Preference Alignment of Diffusion Models.pdf

Aligning pre-trained diffusion models with multiple context-dependent preferences requires adapting generation at test time rather than relying on offline fine-tuning, which requires hyperparameter tuning and a new training run for each preference trade-off. Existing approaches compress diverse preferences into a single scalar reward objective for fine-tuning or test-time guidance rather than directly reusing existing generative experts released for different purposes and obtained through different fine-tuning methods. In this work, we propose Contrastive Gradient Guidance (CGG), a test-time compositional generative framework that reformulates multi-preference alignment as a composition of distributions. CGG represents each preference as a contrastive preference pair of favored experts and unfavored anti-experts, whose score difference forms a contrastive gradient guidance signal that combines denoising directions (gradients) from off-the-shelf diffusion models during sampling. Experiments show that CGG reuses pre-trained and fine-tuned models as favored experts or anti-experts to control output style and safety, and that it can be combined with existing sampling-based reward guidance. With a single fixed scale per pair, CGG composes five preferences at once and gives a more balanced trade-off across text-image preference, concept control, photographic fidelity, and safety than offline fine-tuning, weight-space merging, and reward steering.

## 15. BEND: Spectral Bregman Losses for Multi-Image Unlearning in Diffusion Models

- Authors: Mohamed-Hicham Leghettas, Markus Püschel
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-23
- DOI: Unavailable
- Categories: cs.CV, cs.LG
- Relevance: 3.018332176893211
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.30532v1
- PDF: https://arxiv.org/pdf/2611.30532v1
- Local PDF: pdf/2026-11-25_15_BEND_ Spectral Bregman Losses for Multi-Image Unlearning in Diffusion Models.pdf

Diffusion models memorize training images and reproduce them almost verbatim when prompted, creating copyright and privacy liabilities. Data unlearning erases the influence of specific training samples from a trained model without retraining, and is two-sided: it must forget the targets while preserving generation quality on everything else. Prior methods use the squared-L2 diffusion loss, at most with a hand-set frequency mask; however, it is known that every Bregman divergence is a mathematically valid choice and the squared-L2 is only the simplest example. BEND is the first to search this family: it fits a spectral Bregman divergence to the unlearning task through a bilevel loop, so the loss itself is shaped to forget thoroughly while protecting quality. It also redirects a memorized image to the mean of its retain images, where ReTrack, the state of the art, redirects it to a single near-copy. On Stable Diffusion, a single BEND model erases all 48 verifiably memorized benchmark images at once. It forgets at least as much as per-target, sequential, and jointly trained ReTrack (SSCD 0.084 versus 0.094-0.120), at the quality of the model before unlearning (CLIP-IQA 0.81 versus 0.64-0.69). BEND also outperforms the state of the art on CelebA-HQ in all three measures of the benchmark, and matches or exceeds it on MNIST and CIFAR-10.

## 16. Decoding Transformer Dynamics via Koopman Subspaces

- Authors: Subhradeep Kayal, Ali Dashti
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-22
- DOI: Unavailable
- Categories: cs.CL, cs.AI
- Relevance: 2.9849386010754704
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.29113v1
- PDF: https://arxiv.org/pdf/2611.29113v1
- Local PDF: pdf/2026-11-25_16_Decoding Transformer Dynamics via Koopman Subspaces.pdf

We apply Koopman operator theory and Dynamic Mode Decomposition (DMD) to characterise how large language models (LLMs) process different input topics. Treating the layer-to-layer evolution of hidden states as a dynamical system, we fit a linear Koopman operator and take the subspace spanned by its dominant modes as a per-topic spectral fingerprint. Four findings emerge. First, the depth map is near-linear: a single linear operator predicts each next-layer state to within approx. 18% relative error (interior variance explained approx. 0.99). Second, over the 57 MMLU subjects the fingerprint is topic-discriminative, matching the MMLU taxonomy at 0.72 nearest-neighbour purity and each subject's semantic neighbourhood at 0.75 any-hit@3. Third, it is a reproducible signature (split-half self-retrieval approx. 0.97$). Finally, these findings are consistent across seven base models (Qwen2.5 0.5-7B, Llama-3 1-8B), with a suggestive trend of alignment rising with MMLU accuracy. The spectral fingerprint thus provides a probe of how transformers process different topics across depth. Code is available at https://github.com/DeepK/koopman-llm-eacl27.

## 17. SPROUT: Predicting Objective-Grounded Prompt Utility for Efficient Text-to-Image Preference Tuning

- Authors: Kangping Hu, Akshay Mehra, Stephen Mussmann
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-23
- DOI: Unavailable
- Categories: cs.CV, cs.LG
- Relevance: 2.981025362780873
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.31163v1
- PDF: https://arxiv.org/pdf/2611.31163v1
- Local PDF: pdf/2026-11-25_17_SPROUT_ Predicting Objective-Grounded Prompt Utility for Efficient Text-to-Image Preference Tuning.pdf

Preference tuning of text-to-image diffusion models spends most of its compute generating candidate images, yet training prompts are typically sampled uniformly at random, wasting compute generating images that provide too little signal for model alignment. To best utilize the available compute, we study prompt selection, where at each iteration we identify the most useful prompts for preference tuning. We separate prompt selection into a utility score, an estimator of that utility score, and batch selection. Within this framework, we propose Selection by PRedicting Objective-grounded UTility (SPROUT). The utility score is predicted on every prompt in the pool, including unseen prompts, by a text-only model, refit after every iteration on all utilities observed so far. A randomized acceptance rule then turns these predictions into a batch, so no images are generated beyond those used for training. For direct group preference optimization (DGPO), the objective-grounded utility is the norm of the gradient that the objective produces from a prompt's group of images. Fine-tuning Stable Diffusion 1.5 with DGPO on GenEval, SPROUT matches the final score of uniform sampling in about 44% of the iterations and improves the area under the learning curve with respect to both uniform sampling and CGPO, a recent variance-based prompt sampler. The efficiency gains hold under four held-out reward models never used in training, and the ranking of methods carries over to DPG-Bench and T2I-CompBench++. Our code is available at https://github.com/ADDAPT-ML/SPROUT.

## 18. Uncovering the Tells: Efficient Black-Box Audits for LLM Data Contamination

- Authors: Dominik Bernard Lau, Filip Pawlicki, Jan Dubiński, Sebastian Cygert
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-23
- DOI: Unavailable
- Categories: cs.LG, cs.AI, cs.CL
- Relevance: 2.938828888610886
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.30639v1
- PDF: https://arxiv.org/pdf/2611.30639v1
- Local PDF: pdf/2026-11-25_18_Uncovering the Tells_ Efficient Black-Box Audits for LLM Data Contamination.pdf

Existing methods for assessing training data contamination in Large Language Models achieve high accuracy, but fundamentally rely on gray-box access, rendering them inapplicable to fully black-box environments. This limitation forces auditors to rely on full-sequence sampling or rigid heuristics, both of which incur prohibitive inference costs and struggle to isolate the underlying memorization signal. To overcome this, we propose a generation-based black-box framework that infers context-induced information gain from targeted token discrepancies. We introduce a budget-constrained auditing regime, building on the empirical observation that the membership signal is highly sparse and concentrated in a few highly informative tokens. We formalize this sparsity, showing why uniform sampling needs many more samples than a policy that targets informative positions. Empirically, our approach achieves state-of-the-art black-box separation accuracy while needing about 3x fewer queries than uniform position sampling. Finally, we apply this methodology to closed frontier models, exploring its capacity and limits in surfacing potential training data overlaps on commercial APIs.

## 19. What Do Co-Folding Models Learn? Insights from Enhanced Transition Path Sampling

- Authors: Muhammad R. Hasyim
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-23
- DOI: Unavailable
- Categories: physics.chem-ph, cs.LG, q-bio.BM
- Relevance: 2.9385578123490683
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.30062v1
- PDF: https://arxiv.org/pdf/2611.30062v1
- Local PDF: pdf/2026-11-25_19_What Do Co-Folding Models Learn_ Insights from Enhanced Transition Path Sampling.pdf

Co-folding models are diffusion-based generative models that sample biomolecular complexes from distributions learned on a large corpus of experimental data. Although these models are powerful for structure prediction, it remains unclear whether the conformational ensembles they learn resemble physically meaningful statistical ensembles. To understand what these models learn, we introduce transition path sampling (TPS), which uses Markov chain Monte Carlo over denoising trajectories to sample the learned distribution. Because its Monte Carlo trajectories resemble biomolecular dynamics, TPS couples directly with enhanced-sampling techniques to recover the full conformational ensemble. Applied to Boltz-2, enhanced TPS reveals physical conformational changes biased toward crystal-like states near the training data, indicating both learned physics and memorization. These results suggest new ways to evaluate and improve co-folding models by jointly assessing structural recovery, proximity to training data, and conformational ensembles.

## 20. OAT3D: A Generative Model for 3D Shape- and Resolution-Free Structural Topology Optimization

- Authors: Hongrui Chen, Kittipong Thiamchaiboonthawee, Zhen Wei, Amin Heyrani Nobari, Faez Ahmed
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-22
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 2.921202052562823
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.29253v1
- PDF: https://arxiv.org/pdf/2611.29253v1
- Local PDF: pdf/2026-11-25_20_OAT3D_ A Generative Model for 3D Shape- and Resolution-Free Structural Topology Optimization.pdf

Topology optimization determines how material should be distributed within a design domain to optimize structural performance under prescribed loads, supports, and constraints. The problems are highly nonconvex, and conventional solvers require repeated finite element analyses, making high-resolution 3D topology optimization computationally expensive. Data-driven approaches face an additional bottleneck: generating training datasets requires solving large numbers of these costly problems, so existing work in data-driven topology optimization primarily focuses on 2D problems. Large-scale 3D datasets remain scarce, and existing models remain limited in problem scale and boundary-condition diversity. Here, we introduce Optimize Any Topology-3D (OAT3D), a generative model for high-resolution 3D structural topology optimization. OAT3D introduces a novel sparse problem encoding to represent load and fixity conditions and combines a sparse volumetric variational autoencoder with a conditional diffusion transformer. We construct a dataset of 501,865 optimized topologies, generated using 51,800 GPU-hours and encompassing structures with up to one million elements and substantially more complex loading and support configurations than any existing structural topology optimization dataset. To our knowledge, this is the largest dataset for 3D topology optimization structures. Trained on this dataset, OAT3D generates structures at 512$^3$ resolution and achieves a $44.9\times$ speedup for raw candidate structure generation or $3.65\times$ speedup to reach similar compliance over conventional topology optimization. These contributions expand the scale and diversity of data-driven topology optimization for three-dimensional structural design.

## 21. TriSegAgent: Context-Efficient 3D Annotation with MLLMs via Tri-Planes

- Authors: Qingqiao Hu, Jialin Li, Meilong Xu, Kehan Qi, Yipeng Zhang, Lin Tian, Hongwei Bran Li, Klaus Mueller, Xiaoling Hu
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-23
- DOI: Unavailable
- Categories: cs.CV, cs.LG
- Relevance: 2.8969623680517964
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.30240v1
- PDF: https://arxiv.org/pdf/2611.30240v1
- Local PDF: pdf/2026-11-25_21_TriSegAgent_ Context-Efficient 3D Annotation with MLLMs via Tri-Planes.pdf

Interactive segmentation models turn a few clicks into a segmentation prediction across domains, so annotators only decide where the prediction still needs correction. Annotation thus becomes a loop of inspecting the prediction and clicking again. Each step of this loop is a visual judgment, which suits general-purpose multimodal large language model (MLLM) agents. In this work, we focus on letting these agents run this loop on 3D volumes. However, the MLLM in such an agent takes only 2D images as input, so the agent must observe the 3D volume in 2D. Since the loop calls the MLLM many times, this observation must be token-compact enough to keep every call cheap, yet informative enough to show error regions in the 3D prediction. We meet both needs with tri-planes, the three orthogonal planes that cross at one point in the volume. We show, both theoretically and empirically, that tri-planes are context-efficient yet keep sufficient detail to show error regions in the 3D prediction. Building on tri-planes, we introduce TriSegAgent, an MLLM agent that refines the 3D prediction iteratively. Within the agent, the MLLM only judges the prediction on tri-planes, while a visual harness turns each judgment into a 3D action in code. To make the loop reliable, the harness places each click at an exact voxel in the volume and checks whether to accept the 3D prediction. To evaluate the agent, we build a diverse benchmark of 690 regions of interest (ROIs) from 35 public medical datasets across three imaging modalities. With frontier MLLMs, TriSegAgent reaches an overall Dice about 10 points above the strongest baseline, and its lead is even larger on targets below 3 cm. With flash-level MLLMs, it outperforms a recent 3D segmentation agent built on a frontier MLLM.

## 22. Similarity-Constrained Reweighting for Complex Query Answering on Knowledge Graphs

- Authors: Daniel Daza, Alberto Bernardi, Luca Costabello, Christophe Gueret, Michael Cochez, Martijn Schut
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-22
- DOI: Unavailable
- Categories: cs.AI, cs.LG
- Relevance: 2.8962165772873583
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.29596v1
- PDF: https://arxiv.org/pdf/2611.29596v1
- Local PDF: pdf/2026-11-25_22_Similarity-Constrained Reweighting for Complex Query Answering on Knowledge Graphs.pdf

Machine learning models for Complex Query Answering (CQA) on knowledge graphs estimate the likelihood of answers that are not reachable via direct traversal. Recent work has proposed extending such queries with soft entity constraints, which require the target variable to be similar or dissimilar to specified sets of entities. We study a more general formulation where similarity constraints are specified on an arbitrary variable in a query, and introduce SCORE: a computationally efficient and interpretable method for incorporating similarity constraints on an arbitrary variable of a query. SCORE is based on a lightweight and interpretable score adjustment function that only requires tuning two hyperparameters on a validation set. Our experiments show that SCORE effectively incorporates preferences while maintaining strong query answering performance. It significantly improves ranking quality when constraints apply to the target variable and performs effectively in the more general case involving constraints on intermediate variables, and its performance remains robust when applied to several existing methods for CQA. Our implementation is available at https://github.com/dfdazac/score.

## 23. Engram: Multi-Stage Memory for Agentic Tuning of Heterogeneous Models

- Authors: Huanran Li, Nhat X. T. Le, Kevin De Angeli, Yao Xuan, Alireza Vahdatpour, Djordje Gligorijevic
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-20
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 2.894075913363852
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.28356v1
- PDF: https://arxiv.org/pdf/2611.28356v1
- Local PDF: pdf/2026-11-25_23_Engram_ Multi-Stage Memory for Agentic Tuning of Heterogeneous Models.pdf

Large language model (LLM) agents can now tune neural networks, yet without cross-session memory they spend costly trials rediscovering known lessons. Reuse is difficult because production models differ in architecture, training setup and inference budget. We present Engram, a memory system that links past trial outcomes with the hypotheses and rationale behind them and assesses whether this evidence applies to the current model. An online agent curates evidence at the decision points where it is needed: Initial Guidance supplies validated lessons at the start, Session Retrieval supplies related past sessions before each batch of hypotheses is generated, and Trial Candidate Review checks each trial candidate against matching past trials. Between sessions, an offline agent distills validated lessons, making the memory self-improving. On two ads models, Engram reaches the 32-trial result of a no-memory control with 47% fewer trials and also ends with a better model on average.

## 24. Pixel Auto-Encoder: Reconstructing Language Model Activations Through Pixel Art

- Authors: Haru Furuichi, Phan Xuan Tan
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-21
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 2.8905156130726093
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.28822v1
- PDF: https://arxiv.org/pdf/2611.28822v1
- Local PDF: pdf/2026-11-25_24_Pixel Auto-Encoder_ Reconstructing Language Model Activations Through Pixel Art.pdf

Interpreting the high-dimensional internal representations of large language models (LLMs) remains a challenging problem. Recent approaches have explored translating these representations into human-understandable forms, particularly natural language. In this work, we explore the use of images as an alternative target modality for interpreting LLM activations. As a first step toward this goal, we introduce Pixel Auto-Encoder, which converts intermediate LLM activations into $32 \times 32$, 32-color pixel art and reconstructs them for subsequent computation within the model. By encouraging the intermediate representations to resemble predefined concept images, we investigate whether LLM activations can be expressed visually while preserving the model's language capabilities. We find that the model can produce target-aligned images for some concepts, and that replacing pixel representations with concept images can influence next-token predictions. However, we also observe a trade-off between visual alignment and language-model performance, as well as sensitivity to pixel-level changes that are difficult to interpret visually. These findings demonstrate the feasibility and limitations of image-based representations of LLM activations.

## 25. When Can a Rewiring Control Test LLM Weight Readers? C2 and an Eligibility Protocol

- Authors: Vaishak Girish Kumar, Sanika Vilas Najan
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-22
- DOI: Unavailable
- Categories: cs.LG, cs.AI, cs.CL
- Relevance: 2.886031841325465
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.29120v1
- PDF: https://arxiv.org/pdf/2611.29120v1
- Local PDF: pdf/2026-11-25_25_When Can a Rewiring Control Test LLM Weight Readers_ C2 and an Eligibility Protocol.pdf

Large language models can predict the outputs of small neural networks from raw weights, but success could reflect recognition of weight-space regularities (fingerprints) rather than computation, and function-preserving controls cannot tell these apart. We propose C2, a counterfactual that permutes the columns of a network's final linear readout: every other parameter, and the readout's singular values, norms and entry multiset, are unchanged, and the function can change in an exactly recomputable way; we verify that each evaluated permutation does. C2 separates fingerprinting from computation only under three conditions, which we state as an eligibility protocol: a strategy restricted to C2-invariant summaries must already predict the target; C2 must change a property specific to the rewiring; and the reader's identity must be attested. No natural setting we tested is eligible. On tiny MLPs a frontier reader route followed the rewired function on all 24 networks, but invariant baselines were near chance and its backend could not be attested. In two public CNN zoos the conditions traded off: weight statistics predicted CIFAR-10 accuracy in-distribution, but C2's effect on accuracy was not specific to the swap, while per-image targets were specific but not predictable from invariant summaries. On a constructed population where a planted fingerprint rule works, all conditions hold and C2 separates a rule-following reader from an executor. A self-hosted Qwen3.8-27B followed the rewired function rather than the shortcut, and showed no evidence of using the weights with thinking disabled. A registered replication on fresh networks confirmed both findings (tracking minus stuck 0.875, 95% interval [0.750, 1.000]), and DeepSeek-R1-Distill-Qwen-14B also followed the rewiring (tracking minus stuck 0.729 [0.552, 0.885]). The transforms, audits and raw records are available from the authors.

## 26. Ontology-Compiled 2D Clinical State Fields with Bidirectional Diffusion Encoders for Zero-Training Cross-Ontology Medical Coding

- Authors: Zeqiang Wang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-23
- DOI: Unavailable
- Categories: cs.CL, cs.IR, cs.LG
- Relevance: 2.8792558252669127
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.30218v1
- PDF: https://arxiv.org/pdf/2611.30218v1
- Local PDF: pdf/2026-11-25_26_Ontology-Compiled 2D Clinical State Fields with Bidirectional Diffusion Encoders for Zero-Training Cross-Ontology Medica.pdf

Healthcare systems continually revise clinical taxonomies, update reimbursement schedules, and harmonize cross-border registries. Existing automated coding models bind clinical text understanding to fixed vocabulary-specific heads, requiring manual relabeling and retraining whenever code sets change. We introduce Ontology-Compiled 2D Clinical State Fields (OCSF), a vocabulary-free framework that decouples clinical document reading from target ontology indexing so one trained encoder can switch across arbitrary medical vocabularies in seconds without target training. A single-pass bidirectional diffusion-pretrained encoder and vocabulary-free decoder map each clinical note into a fixed-dimension two-dimensional state matrix with zero code-specific parameters. Any target ontology is compiled offline on CPU from public text descriptions into a scale-invariant Tikhonov deconvolution operator that suppresses sibling-code interference while preserving source decision thresholds. Trained solely on English MIMIC-IV ICD-9 discharge summaries and evaluated without target tuning across 58,706 held-out test notes and five unseen ontologies spanning English ICD-10, MS-DRG, Spanish, Greek, and Chinese (115-185,458 codes), OCSF reaches 63.15% Micro-F1 on in-domain ICD-9 (outperforming a matched closed-vocabulary classifier and eliminating late-epoch tail overfitting) and transfers directly to 26,085 English ICD-10 codes (29.23% recall at gold cardinality), MS-DRG groups, and multilingual terminologies, compiling up to 185,458 codes in under 10 seconds on CPU with sub-millisecond GPU readout.

## 27. From Vanishing Gradients to Recursive Self-Improvement: Evaluating the Most Influential Papers in Large Language Model Evolution (1997-2026)

- Authors: Saadh Jawwadh
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-22
- DOI: Unavailable
- Categories: cs.CL, cs.AI
- Relevance: 2.869750105798783
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.29303v1
- PDF: https://arxiv.org/pdf/2611.29303v1
- Local PDF: pdf/2026-11-25_27_From Vanishing Gradients to Recursive Self-Improvement_ Evaluating the Most Influential Papers in Large Language Model E.pdf

The rapid proliferation of Large Language Model (LLM) research makes it increasingly difficult to distinguish incremental refinements from true paradigm shifts. This review evaluates 22 of the most influential publications spanning nearly three decades (1997-2026), organized through a causal, chronologically anchored taxonomy centered on the author's birth year (1999). Beginning "before 1999" with how recurrent neural networks (RNNs) forgot earlier context (much like forgetting Chapter 1 by the time a reader reaches Chapter 9), we trace how Long Short-Term Memory (LSTM) networks introduced a "bouncer" mechanism of forget, input, and output gates to selectively preserve long-term memory. We then examine how Word2Vec turned language into vector mathematics (king - male + female ~ queen), why sequential RNNs hit a parallelization wall, and how the Transformer's all-to-all attention weights launched the modern LLM era alongside a quadratic bottleneck. Next, we analyze why scaling parameters alone leaves capacity under-trained unless data scales equally (Chinchilla), how Reinforcement Learning from Human Feedback (RLHF) left alignment superficial, and how that gap compounded into adversarial jailbreaks and single-direction refusal subspaces (J-space), where instructing a model not to think of a restricted concept surfaces it much like the human "red ball" paradox. Finally, we synthesize the current state of AI (2024-2026), encompassing recursive model collapse, autonomous reasoning-model jailbreak agents, machine-speed agentic intrusions, and closed-loop recursive self-improvement (AIDE^2).

## 28. MMMem: Self-Improving Agents with Task-Aware Multimodal Experience Consolidation

- Authors: Yuxuan Chen, Changwei Lv, Yunfei Li, Zhongjing Du, Kehui Tan, Zijun Liao, Ruochong Zheng, Hao Chen, Can Deng, Zheni Zeng, Chang Liu, Jie Chen
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-23
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 2.866478148139488
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.30287v1
- PDF: https://arxiv.org/pdf/2611.30287v1
- Local PDF: pdf/2026-11-25_28_MMMem_ Self-Improving Agents with Task-Aware Multimodal Experience Consolidation.pdf

AI agents accumulate conversations, images, and documents through long-term interactions with users. Answering later questions often requires connecting evidence across these records, yet the resulting understanding is rarely retained, allowing mistakes to recur on related questions. Existing multimodal memory methods largely focus on storing and retrieving records, with limited mechanisms for learning from completed tasks and consolidating task-specific experience. We therefore propose MMMem, a task-aware multimodal memory framework that extracts and consolidates experience from completed tasks through four complementary strategies. First, source-linked multi-view memory organizes original text, images, and rendered pages alongside generated scene images that combine clues across records for retrieval. Second, source-generated tasks support knowledge alignment at two levels: warm-up consolidates source knowledge into task-relevant experiences in external memory, while self-training adapts the model's parametric knowledge to task demands. Third, the same vision-language model distills completed tasks into experiences that record the task context, conclusion, and support links. Finally, task-aware retrieval recalls source views and relevant experiences for answering and verification, while source-supported reuse guides long-term retention. Across three memory benchmarks and two vision-language readers, MMMem outperforms eight baselines. With Qwen3.5-9B, MMMem achieves relative gains of 36.9%, 17.6%, and 15.2% over the best-performing baselines on LoCoMo, Mem-Gallery, and LooGLE v2, respectively. Ablations show consistent gains from training and memory warm-up, while case studies illustrate how individual components work in practice.

## 29. Diversity over Scale: Recursive Self-Improvement with Ensembles of Small Open-Weight Models

- Authors: Navapat Nananukul, Mayank Kejriwal
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-20
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 2.8661990186741844
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.28420v1
- PDF: https://arxiv.org/pdf/2611.28420v1
- Local PDF: pdf/2026-11-25_29_Diversity over Scale_ Recursive Self-Improvement with Ensembles of Small Open-Weight Models.pdf

The advancement of large language models (LLMs) has significantly enhanced the capabilities of agents across various tasks. Recursive self-improvement (RSI) loops, in which a language model repeatedly rewrites a program and builds on its previous version, now perform well in machine-learning tasks, but they rely on frontier models and hundreds of calls per run. Small open-weight models are far cheaper, yet when used alone, their programs often crash and their improvements stall. We propose DiVE (diverse models evolve), an ensemble method for RSI that aims to improve creativity and diversity of generated solutions. DiVE uses three components: a shared memory, a failure log, and best-idea-wins rounds. This allows models to write candidate solutions from the same context and retain the best idea at each iteration. On 22 MLE-bench Lite competitions, an ensemble of five 8-12B open-weight models has 25.4% less test error than its average member and 16.7% less than Llama 3.3 70B, and comes within 7.1% of Qwen 3.5 122B-A10B at 75% of its cost. Diversity among small models can thus stand in for part of the scale that RSI relies on.

## 30. PFN-Syn: Generating Synthetic Tabular Data with Prior-Data Fitted Networks

- Authors: Michael Zuo, Inwon Kang, Oshani Seneviratne, Stacy Patterson
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-21
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 2.860901791308603
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.28440v1
- PDF: https://arxiv.org/pdf/2611.28440v1
- Local PDF: pdf/2026-11-25_30_PFN-Syn_ Generating Synthetic Tabular Data with Prior-Data Fitted Networks.pdf

Synthetic tabular data can help enable data sharing and model development in privacy-sensitive domains, but existing generators often require dataset-specific training and substantial computation. We introduce PFN-Syn, a training-free framework for synthetic tabular data generation based on prior-data fitted networks. We evaluate PFN-Syn against training-based generators on eight binary classification datasets. PFN-Syn achieves the highest average downstream utility among evaluated synthetic generators, with higher generation throughput than training-based baselines, while maintaining competitive distributional similarity and distance-to-closest-record privacy behavior. Our results suggest that tabular foundation models can serve as useful building blocks for practical synthetic tabular data generation.
