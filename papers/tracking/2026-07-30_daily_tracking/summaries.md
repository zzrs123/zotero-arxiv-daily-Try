# Researcher Tracking - 2026-07-30 (daily)

Total new tracked papers: 4
Highlighted papers: 4

## 1. Equilibrium Training of Energy-Based Models with Parallel Trajectory Tempering

- Authors: Nicolas Béreux, Aurélien Decelle, Cyril Furtlehner, Beatriz Seoane
- Source hits: arxiv
- Matched researchers: Nicolas Béreux
- Matched groups: N/A
- Confidence: medium (author_alias)
- Topic keywords: deep generative model, energy-based model
- Journal/source: arxiv
- Publication date: 2026-07-29
- Article: http://arxiv.org/abs/2607.27077v1

Energy-Based Models (EBMs) provide an interpretable framework for generative modeling of scientific data, but poor Markov Chain Monte Carlo mixing often limits their reliability. We introduce a training algorithm based on Parallel Trajectory Tempering (PTT), which exploits the continuity of the optimization path to maintain equilibrium sampling throughout learning. This enables stable and fast training on highly multimodal and data-scarce scientific datasets. Combined with reservoir sampling and adaptive optimization, PTT has a computational cost comparable to Persistent Contrastive Divergence, making it a practical replacement for standard training methods. It also provides direct estimates of thermalization times, equilibrium samples from trained models, and accurate log-likelihoods at essentially no additional cost. Experiments on Restricted Boltzmann Machines show that PTT consistently outperforms existing EBM training approaches. On discrete tabular data, it also surpasses state-of-the-art deep generative models, yielding higher-quality samples and greater robustness to overfitting and limited data. Our results make equilibrium maximum-likelihood training of EBMs practical and computationally efficient.

## 2. FedTopo: Relation-Level Topology Sharing for Model-Heterogeneous Federated Learning

- Authors: Zhaoyang Ma, Zhihao Wu, Xin Gao, Lipo Wang, Youfang Lin, Jing Wang
- Source hits: arxiv
- Matched researchers: Xin Gao
- Matched groups: N/A
- Confidence: medium (author_alias)
- Topic keywords: N/A
- Journal/source: arxiv
- Publication date: 2026-07-29
- Article: http://arxiv.org/abs/2607.26801v1

Federated learning (FL) enables collaborative learning over decentralized data silos without centralizing raw data. However, heterogeneous local architectures often induce non-aligned representation spaces, making it difficult to transfer global knowledge across silos. Existing paradigms share this knowledge as model parameters, distilled predictions, or class prototypes, yet all encode it in an absolute space that must be aligned across clients. Heterogeneous backbones break this alignment, so the shared knowledge becomes unreliable and misleads local training. We propose FedTopo, a relation-level framework that encodes global knowledge as class relation topology, capturing how classes relate within each client rather than where they lie in feature space. Each client builds its relation topology from local prototypes and uploads it with class statistics. The server then aggregates these relations in a reliability-aware manner that down-weights weakly supported ones, and broadcasts the global topology to clients. The global topology guides local training by emphasizing topology-similar negative classes. Experiments on three datasets under eight heterogeneous backbones show that FedTopo consistently outperforms parameter-, distillation-, and prototype-sharing baselines, with low communication and no inference overhead. Our code is available at https://github.com/Zhaoyang-Ma/FedTopo.

## 3. Registration-Grounded Spectral Fusion for Unregistered WLI/NBI Endoscopic Lesion Segmentation

- Authors: Pengyu Jie, Wanquan Liu, Rui He, Pengcheng Li, Weiping Wen, Deyu Meng, Junwei Han, Chenqiang Gao
- Source hits: arxiv
- Matched researchers: Junwei Han
- Matched groups: N/A
- Confidence: medium (author_alias)
- Topic keywords: N/A
- Journal/source: arxiv
- Publication date: 2026-07-29
- Article: http://arxiv.org/abs/2607.26395v1

White-light imaging (WLI) and narrow-band imaging (NBI) provide complementary views of endoscopic lesions, but their paired observations are often spatially misaligned due to viewpoint changes, tissue deformation, and sequential handheld acquisition. This makes direct WLI/NBI fusion prone to mixing non-corresponding regions and may even degrade segmentation around lesion boundaries. To address this problem, we propose a reliability-aware complex-domain fusion framework for paired-but-unregistered WLI/NBI lesion segmentation. The framework first establishes topology-regularized feature correspondence and further estimates where the cross-modal correspondence is reliable. Guided by this reliability, the model selectively fuses WLI and NBI features in a learnable complex representation. In this representation, WLI-derived cues mainly provide appearance-related magnitude responses, while NBI-derived cues provide structure-sensitive phase responses. Unlike conventional real-valued or symmetric multimodal fusion, the proposed method explicitly models the different roles of WLI and NBI and suppresses unreliable cross-modal interaction in locally mismatched regions. Experiments on paired WLI/NBI endoscopic datasets show that the proposed reliability-aware registration grounding and complex-domain fusion consistently improve lesion segmentation performance. Role-reversal and module ablation studies further validate the necessity of both the modality-role design and reliability-guided cross-modal interaction.

## 4. GPTQ-2D: Cubic-Time Two-Sided Adaptive Rounding

- Authors: Jiale Chen, Torsten Hoefler, Dan Alistarh
- Source hits: arxiv
- Matched researchers: Torsten Hoefler
- Matched groups: N/A
- Confidence: medium (author_alias)
- Topic keywords: N/A
- Journal/source: arxiv
- Publication date: 2026-07-29
- Article: http://arxiv.org/abs/2607.27042v1

Adaptive rounding methods such as GPTQ, or equivalently Babai's nearest plane algorithm, round a real matrix to integers under a quadratic metric. They process the entries in a fixed order, one at a time, propagating each rounding error to the entries not yet processed through a triangular feedback matrix. We study the two-sided version of this task, in which fixed nonsingular basis matrices act on both the left and the right of the residual; the familiar one-sided case is the special case of an identity right basis. Vectorizing the matrix turns the two-sided objective into a quadratic metric whose Gram matrix is a Kronecker product, so the one-dimensional algorithm applies verbatim, but takes quartic time in the matrix dimension. We present GPTQ-2D, which produces the identical rounded matrix in cubic time. It rounds the entries anti-diagonal by anti-diagonal; entries on the same anti-diagonal are independent and are rounded in parallel.
