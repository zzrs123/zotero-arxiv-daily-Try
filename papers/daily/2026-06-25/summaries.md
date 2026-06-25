# Paper Daily Reading - 2026-06-25

## 1. Cog-RAG: Cognitive-Inspired Dual-Hypergraph with Theme Alignment Retrieval-Augmented Generation

- Authors: Hao Hu, Yifan Feng, Ruoxue Li, Rundong Xue, Xiaochen Hou, Zhiqiang Tian, Yue Gao, Shaoyi Du
- Source: openalex
- Venue type: conference
- Journal: Proceedings of the AAAI Conference on Artificial Intelligence
- Publication status: formally_published
- Publication date: 2026-03-14
- DOI: https://doi.org/10.1609/aaai.v40i37.40363
- Categories: Advanced Graph Neural Networks, Topic Modeling, Multimodal Machine Learning Applications
- Relevance: 3.4844851009287465
- Article: https://doi.org/10.1609/aaai.v40i37.40363
- PDF: https://ojs.aaai.org/index.php/AAAI/article/download/40363/44324
- Local PDF: Not downloaded

Retrieval-Augmented Generation (RAG) enhances the response quality and domain-specific performance of large language models (LLMs) by incorporating external knowledge to combat hallucinations. In recent research, graph structures have been integrated into RAG to enhance the capture of semantic relations between entities. However, it primarily focuses on low-order pairwise entity relations, limiting the high-order associations among multiple entities. Hypergraph-enhanced approaches address this limitation by modeling multi-entity interactions via hyperedges, but they are typically constrained to inter-chunk entity-level representations, overlooking the global thematic organization and alignment across chunks. Drawing inspiration from the top-down cognitive process of human reasoning, we propose a theme-aligned dual-hypergraph RAG framework (Cog-RAG) that uses a theme hypergraph to capture inter-chunk thematic structure and an entity hypergraph to model high-order semantic relations. Furthermore, we design a cognitive-inspired two-stage retrieval strategy that first activates query-relevant thematic content from the theme hypergraph, and then guides fine-grained recall and diffusion in the entity hypergraph, achieving semantic alignment and consistent generation from global themes to local details. Our extensive experiments demonstrate that Cog-RAG significantly outperforms existing state-of-the-art baseline approaches.

## 2. Stable-Shift: Biologically Structured Prediction of Transcriptional Responses to Unseen Gene Perturbations

- Authors: Sajib Acharjee Dip, Liqing Zhang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-06-22
- DOI: Unavailable
- Categories: q-bio.GN, cs.AI, cs.LG
- Relevance: 3.377566511360872
- Article: http://arxiv.org/abs/2606.24940v1
- PDF: https://arxiv.org/pdf/2606.24940v1
- Local PDF: pdf/2026-06-25_02_Stable-Shift_ Biologically Structured Prediction of Transcriptional Responses to Unseen Gene Perturbations.pdf

Predicting transcriptional responses to genetic perturbations could reduce the experimental burden of functional genomics, but extrapolation to genes that were never perturbed during training remains difficult. We present Stable-Shift, a structured method for estimating unseen-gene responses. Stable-Shift aggregates single-cell measurements into perturbation-level expression shifts, fits a low-rank response basis using training perturbations only, and predicts an unseen gene's coordinates in that basis from biological context. The context combines STRING interactions, network structure, control-cell expression statistics, and Gene Ontology annotations; the evaluated implementation uses graph convolution to integrate these inputs. On the supplied K562 Perturb-seq benchmark, Stable-Shift obtained 0.592 cosine similarity, compared with 0.569 for GEARS, together with higher Spearman correlation and top-gene precision among the evaluated methods. Its mean cosine similarity over five unseen-gene splits was 0.589 +/- 0.008. The same ordering was observed in the supplied graph-aware, residualized, gene-space, and Norman-dataset comparisons. These results support further study of biologically structured latent-response prediction, while the lower gene-space accuracy and sensitivity to sparse graph neighborhoods limit the scope of the present conclusions.

## 3. Role Hypergraph Contrastive Learning for Multivariate Time-Series Analysis

- Authors: Rundong Xue, Hao Hu, Zhitao Zeng, Xiangmin Han, Zhiqiang Tian, Shaoyi Du, Yue Gao
- Source: openalex
- Venue type: conference
- Journal: Proceedings of the AAAI Conference on Artificial Intelligence
- Publication status: formally_published
- Publication date: 2026-03-14
- DOI: https://doi.org/10.1609/aaai.v40i32.39965
- Categories: Time Series Analysis and Forecasting, Machine Learning in Healthcare, Statistical and numerical algorithms
- Relevance: 3.3292172986697564
- Article: https://doi.org/10.1609/aaai.v40i32.39965
- PDF: Unavailable
- Local PDF: Not downloaded

Multivariate Time-Series (MTS) analysis is crucial across various domains. Considering the spatial and temporal consistency of MTS, existing methods leverage graph structures with temporal augmentation and contrastive learning to achieve robust learning of spatial dependencies and temporal patterns. Given the inherent high-order correlations in MTS, hypergraphs present a promising approach. However, two key challenges limit their further development: 1) Feature-based perspectives capture limited spatial information, while structural perspectives encode richer spatial consistency and evolution dependency; 2) Various semantic patterns (e.g., synergy, inhibition) entangle in sensor correlations, leading to semantic ambiguity. The underlying reason is that conventional hypergraph structures cannot distinguish specific semantic roles within or across hyperedges. Thus, we propose Role Hypergraph Contrastive Learning for MTS analysis. Specifically, we introduce the concept of role to generalize hypergraphs to Role Hypergraphs, enabling precise modeling of sensor correlations by assigning each vertex-hyperedge pair with a semantic role. Building on this structure, we design a role hypergraph contrastive learning paradigm to comprehensively capture the spatial and temporal dependencies: From a structural perspective, role hypergraph structural contrasting captures spatial short-term consistency and long-term evolution; from a feature perspective, alignment of complementary role information ensures sensor-level temporal consistency. Experiments on classification and forecasting tasks demonstrate the effectiveness and interpretability of our method.

## 4. LADR: Locality-Aware Dynamic Rescue for Efficient Text-to-Image Generation with Diffusion Large Language Models

- Authors: Chenglin Wang, Yucheng Zhou, Shuang Chen, Tao Wang, Kai Zhang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.258461024304512
- Article: https://aclanthology.org/2026.acl-long.1251/
- PDF: https://aclanthology.org/2026.acl-long.1251.pdf
- Local PDF: pdf/2026-06-25_04_LADR_ Locality-Aware Dynamic Rescue for Efficient Text-to-Image Generation with Diffusion Large Language Models.pdf

Discrete Diffusion Language Models have emerged as a compelling paradigm for unified multimodal generation, yet their deployment is hindered by high inference latency arising from iterative decoding. Existing acceleration strategies often require expensive re-training or fail to leverage the 2D spatial redundancy inherent in visual data. To address this, we propose Locality-Aware Dynamic Rescue (LADR), a training-free method that expedites inference by exploiting the spatial Markov property of images. LADR prioritizes the recovery of tokens at the “generation frontier”, regions spatially adjacent to observed pixels, thereby maximizing information gain. Specifically, our method integrates morphological neighbor identification to locate candidate tokens, employs a risk-bounded filtering mechanism to prevent error propagation, and utilizes manifold-consistent inverse scheduling to align the diffusion trajectory with the accelerated mask density. Extensive experiments on four text-to-image generation benchmarks demonstrate that our LADR achieves an approximate 4 × speedup over standard baselines. Remarkably, it maintains or even enhances generative fidelity, particularly in spatial reasoning tasks, offering a state-of-the-art trade-off between efficiency and quality.

## 5. Building LLMs Like LEGO: Two-dimensional Architecture Reassembly of Large Language Models

- Authors: Xingyu Wu, Yu Zhou, KC Tan
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.253328461965752
- Article: https://aclanthology.org/2026.acl-long.2081/
- PDF: https://aclanthology.org/2026.acl-long.2081.pdf
- Local PDF: pdf/2026-06-25_05_Building LLMs Like LEGO_ Two-dimensional Architecture Reassembly of Large Language Models.pdf

Pretrained large language models (LLMs) are typically reused as indivisible artifacts, adapted, merged, or ensembled as a whole. In this study, we show that LLMs can instead be structurally recomposed as modular building blocks to create new architectures without access to original training data. We introduce architecture-level reassembly as a new reuse paradigm, in which Transformer blocks from heterogeneous models are treated as reusable components. This idea is formalized through a two-dimensional reassembly space that supports both vertical recombination across depth and horizontal composition within layers. To make this space tractable, we propose a chromosome-based architectural encoding and perform a bi-level multi-objective evolutionary optimization over vertical structure and horizontal composition. To resolve representation incompatibility across heterogeneous blocks, we introduce lightweight glue layers trained via data-free knowledge distillation, enabling valid information flow without modifying pretrained parameters. Our results demonstrate that architecture-level reassembly unlocks a new dimension of flexibility in model reuse, pointing toward a modular and evolutionary view of LLM design.

## 6. Correct When Paired, Wrong When Split: Decoupling and Editing Modality-Specific Neurons in MLLMs

- Authors: Tingchao Fu, Wenkai Wang, Fanxiao Li, Huadong Zhang, Jinhong Zhang, Dayang Li, Yunyun Dong, Renyang Liu, Wei Zhou
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.2516826058963866
- Article: https://aclanthology.org/2026.acl-long.456/
- PDF: https://aclanthology.org/2026.acl-long.456.pdf
- Local PDF: pdf/2026-06-25_06_Correct When Paired, Wrong When Split_ Decoupling and Editing Modality-Specific Neurons in MLLMs.pdf

Although Knowledge Editing provides an efficient mechanism for updating the knowledge of Multimodal Large Language Models (MLLMs), we find that current paradigms still suffer from an important yet remain underexplored issue : editing decoupling failure, where entity-related knowledge can be updated when the model is triggered by multimodal inputs (text–image query pairs), however, it often reverts to outdated pre-edit facts when the paired inputs are split into unimodal ones. Our in-depth empirical analysis reveals that the entity knowledge in MLLMs is not stored as a unified representation, but is instead distributed across disentangled modality-specific pathways. As a result, updates biased toward multimodal queries fail to propagate effectively to unimodal circuits. To bridge this gap, we propose DECODE, which explicitly disentangles and localizes modality-specific neuron groups for targeted knowledge. Extensive experiments demonstrate that DECODE consistently achieves effective knowledge updates under different modality triggers, thereby mitigating editing decoupling failures.

## 7. Multi-component Causal Tracing in Large Language Models

- Authors: Zirui Yan, Dennis Wei, Dmitriy A Katz, Prasanna Sattigeri, Ali Tajer
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.2507423451003663
- Article: https://aclanthology.org/2026.acl-long.154/
- PDF: https://aclanthology.org/2026.acl-long.154.pdf
- Local PDF: pdf/2026-06-25_07_Multi-component Causal Tracing in Large Language Models.pdf

Causal tracing systematically intervenes on a large language model’s (LLM’s) internal representations to uncover and quantify the causal pathways linking specific inputs or computations to specific metrics of interest, quantifying the LLM’s behavior. Building on previous single-component or single-layer studies, this paper presents a unified framework for causally tracing multiple components simultaneously. This framework systematically identifies the subsets of components (e.g., attention heads and multi-layer perceptron neurons) most critical to a desired target performance metric (e.g., accuracy and fairness). This is achieved by incorporating flexible interventions applied to a wide range of desired metrics. To address the combinatorial complexity of the multi-component problem, an efficient algorithm is designed that leverages soft interventions and a carefully designed metric transformation, converting the combinatorial search problem into a continuous one that can be solved efficiently under proper constraints, thereby generating proper binary decisions for selecting components. Experimental results demonstrate that the proposed method efficiently identifies subsets of the model’s components that have a high impact on the target metric, outperforming existing baseline approaches.

## 8. Logic Matters in Lightweight Hallucination Classification for RAG System

- Authors: Ningyuan Yang, Kaizhu Huang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.243039908077212
- Article: https://aclanthology.org/2026.acl-long.73/
- PDF: https://aclanthology.org/2026.acl-long.73.pdf
- Local PDF: pdf/2026-06-25_08_Logic Matters in Lightweight Hallucination Classification for RAG System.pdf

We propose a lightweight, modular framework for hallucination detection in Retrieval-Augmented Generation (RAG) systems, addressing the critical challenge where logical dependencies span across fragmented retrieval results. To address the inherent limitations of compact models in processing long-context information and performing multi-hop reasoning, our approach systematically analyzes the logical relationships among retrieved documents within the vector space. By capturing these geometric patterns through a novel feature extraction framework, the proposed classifier significantly enhances context-aware hallucination detection without requiring complex architectures or pre-training on datasets. Meanwhile, to evaluate multi-document reasoning, we release HotPotQA-derived, a hallucination dataset preserving separate retrieved texts. Experimental results on HotPotQA-derived and several open-source datasets demonstrate that our framework can achieve results comparable to or even surpassing those of large language models (LLMs) on the task of hallucination detection.

## 9. Analytical FFN-to-MoE Restructuring via Activation Pattern Analysis

- Authors: Zehua Pei, Hui-Ling Zhen, Lancheng Zou, Xianzhi Yu, Wulong Liu, Sinno Jialin Pan, Mingxuan Yuan, Bei Yu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.239100566895176
- Article: https://aclanthology.org/2026.acl-long.218/
- PDF: https://aclanthology.org/2026.acl-long.218.pdf
- Local PDF: pdf/2026-06-25_09_Analytical FFN-to-MoE Restructuring via Activation Pattern Analysis.pdf

Scaling large language models (LLMs) improves performance but significantly increases inference costs, with feed-forward networks (FFNs) consuming the majority of computational resources. While Mixture-of-Experts (MoE) architectures can reduce this cost through sparse activation, restructuring existing dense models into MoEs typically requires extensive retraining on hundreds of billions of tokens.We propose an analytical post-training framework that rapidly restructures FFNs into sparse MoE architectures using only a small calibration dataset. The method analyzes neuron activation patterns to partition neurons into always-active shared experts and conditionally activated routed experts, then constructs a router analytically from representative neuron statistics, enabling immediate deployment or optional lightweight fine-tuning. This approach applies both to dense models and recursively to existing MoE models for hierarchical sparsity.Experiments demonstrate up to 1.17× speedup in compute-bound scenarios with only minutes of processing and 2k-sample fine-tuning, outperforming methods requiring orders of magnitude more resources.

## 10. Diffusion-CAM: Faithful Visual Explanations for dMLLMs

- Authors: Haomin Zuo, Yidi Li, Luoxiao Yang, Xiaofeng Zhang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.235477294610768
- Article: https://aclanthology.org/2026.acl-long.553/
- PDF: https://aclanthology.org/2026.acl-long.553.pdf
- Local PDF: pdf/2026-06-25_10_Diffusion-CAM_ Faithful Visual Explanations for dMLLMs.pdf

While diffusion Multimodal Large Language Models (dMLLMs) have recently achieved remarkable strides in multimodal generation, the development of interpretability mechanisms has lagged behind their architectural evolution. Unlike traditional autoregressive models that produce sequential activations, diffusion-based architectures generate tokens via parallel denoising, resulting in smooth, distributed activation patterns across the entire sequence. Consequently, existing Class Activation Mapping (CAM) methods, which are tailored for local, sequential dependencies, are ill-suited for interpreting these non-autoregressive behaviors. To bridge this gap, we propose Diffusion-CAM, the first interpretability method specifically tailored for dMLLMs. We derive raw activation maps by differentiably probing intermediate representations in the transformer backbone, accordingly capturing both latent features and their class-specific gradients. To address the inherent stochasticity of these raw signals, we incorporate four key modules to resolve spatial ambiguity and mitigate intra-image confounders and redundant token correlations. Extensive experiments demonstrate that Diffusion-CAM significantly outperforms SoTA methods in both localization accuracy and visual fidelity, establishing a new standard for understanding the parallel generation process of diffusion multimodal systems.

## 11. Agent-based Substructure Counting under Local Differential Privacy

- Authors: Yuting Zhang, Kai Wang, Wei Ni, Ying Zhang, Wenjie Zhang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.2331846478058504
- Article: https://aclanthology.org/2026.acl-long.1032/
- PDF: https://aclanthology.org/2026.acl-long.1032.pdf
- Local PDF: pdf/2026-06-25_11_Agent-based Substructure Counting under Local Differential Privacy.pdf

Recent studies have demonstrated the ability of Large Language Models (LLMs) in processing various graph problems. Substructure counting remains challenging in both scalability and accuracy. Incorporating sensitive edge information into the input prompts also introduces significant privacy risks of exposing the private information of user connections in real-world applications. This paper, for the first time, studies substructure counting for LLMs under edge local differential privacy (LDP) in a multi-agent framework. Unlike the Naive approach whose estimation relies entirely on overly dense noisy graphs, the proposed PSC framework decomposes substructure counting into node-level tasks distributed among node agents, and embeds the knowledge of distributed algorithms and DP frameworks in the curator agent and privacy controller, respectively. Thus, we can leverage the local neighboring information and reasoning capabilities of node agents to improve the estimation accuracy. Extensive experiments on 6 real-world datasets validate the effectiveness of PSC framework for substructure counting tasks under 𝜀 -edge LDP. Moreover, the non-DP version of PSC also demonstrated superior performance over a single LLM on standard substructure counting tasks.

## 12. EA-Agent: A Structured Multi-Step Reasoning Agent for Entity Alignment

- Authors: Yixuan Nan, Xixun Lin, Yanmin Shang, Ge Zhang, Zheng Fang, Fang Fang, Yanan Cao
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.229437681410556
- Article: https://aclanthology.org/2026.acl-long.1420/
- PDF: https://aclanthology.org/2026.acl-long.1420.pdf
- Local PDF: pdf/2026-06-25_12_EA-Agent_ A Structured Multi-Step Reasoning Agent for Entity Alignment.pdf

Entity alignment (EA) aims to identify entities across different knowledge graphs (KGs) that refer to the same real-world object and plays a critical role in knowledge fusion and integration. Traditional EA methods mainly rely on knowledge representation learning, but their performance is often limited under noisy or sparsely supervised scenarios. Recently, large language models (LLMs) have been introduced to EA and achieved notable improvements by leveraging rich semantic knowledge. However, existing LLM-based EA approaches typically treat LLMs as black-box decision makers, resulting in limited interpretability, and the direct use of large-scale triples substantially increases inference cost. To address these challenges, we propose EA-Agent , a reasoning-driven agent for EA. EA-Agent formulates EA as a structured reasoning process with multi-step planning and execution, enabling interpretable alignment decisions. Within this process, it introduces attribute and relation triple selectors to filter redundant triples before feeding them into the LLM, effectively addressing efficiency challenges. Experimental results on three benchmark datasets demonstrate that EA-Agent consistently outperforms existing EA methods and achieves state-of-the-art performance. The source code is available at https://anonymous.4open.science/r/EA-Agent-5696.

## 13. Anatomically-conditioned Latent Diffusion Model for Data-Efficient Few-Shot Cross-Domain 3D Glioma MRI Synthesis

- Authors: Salman Shaik, Truong Thanh Hung Nguyen, Hung Cao
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-06-24
- DOI: Unavailable
- Categories: cs.CV, cs.AI
- Relevance: 3.224903281956145
- Article: http://arxiv.org/abs/2606.25390v1
- PDF: https://arxiv.org/pdf/2606.25390v1
- Local PDF: pdf/2026-06-25_13_Anatomically-conditioned Latent Diffusion Model for Data-Efficient Few-Shot Cross-Domain 3D Glioma MRI Synthesis.pdf

Accurate classification of diffuse gliomas is often hindered by domain shifts across centers and a lack of large, annotated datasets. We propose the Anatomically-conditioned Latent Diffusion Model (ALDM), a novel framework for data-efficient, few-shot 3D volumetric MRI synthesis. ALDM utilizes a two-stage approach: a 3D variational autoencoder learns anatomical priors from a data-rich source domain, while a conditional latent diffusion model, guided by tumor masks via a ControlNet, generates structurally coherent volumes for a data-scarce target domain. Evaluated in an extreme few-shot setting with only 16 target images, ALDM outperformed GAN and hybrid baselines, achieving a superior Frechet Inception Distance (FID) of 85.40 and a downstream classification AUC of 0.987. Qualitative results confirm that the model preserves sharp pathology boundaries and cross-modal consistency, with visual fidelity improving progressively during training. By capturing essential diagnostic features, ALDM provides a robust tool for clinical data augmentation in low-resource settings. Our implementation is available at https://github.com/Analytics-Everywhere-Lab/anatomically-conditioned-LDM.

## 14. Learning Invariant Modality Representation for Robust Multimodal Learning from a Causal Inference Perspective

- Authors: Sijie Mai, Shiqin Han
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.2156253236306718
- Article: https://aclanthology.org/2026.acl-long.2119/
- PDF: https://aclanthology.org/2026.acl-long.2119.pdf
- Local PDF: pdf/2026-06-25_14_Learning Invariant Modality Representation for Robust Multimodal Learning from a Causal Inference Perspective.pdf

Multimodal affective computing aims to predict humans’ sentiment, emotion, intention, and opinion using language, acoustic, and visual modalities. However, current models often learn spurious correlations that harm generalization under distribution shifts or noisy modalities. To address this, we propose a causal modality-invariant representation (CmIR) learning framework for robust multimodal learning. At its core, we introduce a theoretically grounded disentanglement method that separates each modality into ‘causal invariant representation’ and ‘environment-specific spurious representation’ from a causal inference perspective. CmIR ensures that the learned invariant representations retain stable predictive relationships with labels across different environments while preserving sufficient information from the raw inputs via invariance constraint, mutual information constraint, and reconstruction constraint. Experiments across multiple multimodal benchmarks demonstrate that CmIR achieves state-of-the-art performance. CmIR particularly excels on out-of-distribution data and noisy data, confirming its robustness and generalizability.

## 15. Not All Directions Matter: Towards Structured and Task-Aware Low-Rank Model Adaptation

- Authors: Xi Xiao, Chenrui Ma, Yunbei Zhang, Chen Liu, Zhuxuanzi Wang, Yanshu Li, Lin Zhao, Guosheng Hu, Tianyang Wang, Hao Xu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.215415858912394
- Article: https://aclanthology.org/2026.acl-long.97/
- PDF: https://aclanthology.org/2026.acl-long.97.pdf
- Local PDF: pdf/2026-06-25_15_Not All Directions Matter_ Towards Structured and Task-Aware Low-Rank Model Adaptation.pdf

Low-Rank Adaptation (LoRA) has become a cornerstone of parameter-efficient fine-tuning (PEFT). Yet, its efficacy is hampered by two fundamental limitations: semantic drift , arising from treating all update directions with equal importance, and structural incoherence , due to adapting layers independently, resulting in uncoordinated and suboptimal updates. To address these issues, we propose StructLoRA , a framework that tackles both limitations through a principled dual-component design: (1) an Information Bottleneck-guided filter that prunes task-irrelevant directions to mitigate semantic drift, and (2) a lightweight, training-only graph-based coordinator that enforces inter-layer consistency to resolve structural incoherence. Extensive experiments across large language models, vision language models, and vision models (including LLaMA, LLaVA, and ViT) demonstrate that StructLoRA consistently establishes a new state of the art, outperforming not only vanilla LoRA but also advanced dynamic rank allocation and sparsity-based methods. Notably, the gains are particularly pronounced in challenging low-rank and low-data regimes. Crucially, since the proposed modules operate only during training, StructLoRA improves performance with zero additional inference cost , shifting the focus of PEFT from mere parameter compression to a more holistic optimization of information quality and structural integrity.

## 16. Evaluating LLMs on Large-Scale Graph Property Estimation via Random Walks

- Authors: Sunil Kumar Maurya, Xin Liu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.2150867967855454
- Article: https://aclanthology.org/2026.acl-long.1846/
- PDF: https://aclanthology.org/2026.acl-long.1846.pdf
- Local PDF: pdf/2026-06-25_16_Evaluating LLMs on Large-Scale Graph Property Estimation via Random Walks.pdf

With the rapidly improving reasoning abilities of Large Language Models (LLMs), there is also a rising demand to use them in a wide variety of domains. This brings about the need to carefully evaluate the limits of the capabilities of these models with various tests and benchmarks. Graph structures are ubiquitous in real-world data, and are often used to represent and analyze relationship patterns within data. Many benchmarks have already been proposed in the graph literature to test the reasoning ability of LLMs to follow and execute graph algorithms. However, due to the limited context length of LLMs, these benchmarks consist of very small graphs. In real-world data, the size of graphs can be significantly larger, and in many cases, not fully accessible. In this paper, we examine a class of problems that arises with very large graphs having limited accessibility. We propose a large graph benchmark dataset, EstGraph, and introduce four distinct tasks designed to estimate large graph properties. We evaluate the reasoning abilities of LLMs on these tasks using a wide variety of graph datasets. In addition, we provide task-specific prompt constructions based on random walk sampling of large graphs (up to millions of nodes) that effectively convey sufficient information to LLMs within the limits of context length.

## 17. Crosscoding Through Time: Tracking Emergence & Consolidation Of Linguistic Representations Throughout LLM Pretraining

- Authors: Deniz Bayazit, Aaron Mueller, Antoine Bosselut
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.214615452413432
- Article: https://aclanthology.org/2026.acl-long.60/
- PDF: https://aclanthology.org/2026.acl-long.60.pdf
- Local PDF: pdf/2026-06-25_17_Crosscoding Through Time_ Tracking Emergence & Consolidation Of Linguistic Representations Throughout LLM Pretraining.pdf

Large language models (LLMs) learn non-trivial abstractions during pretraining, such as detecting irregular plural noun subjects. However, because traditional evaluation methods (e.g., benchmarking) fail to reveal how models acquire these concepts and capabilities, it is not well understood when and how these specific linguistic abilities emerge. To bridge this gap and better understand model training at the concept level, we use sparse crosscoders to discover and align features across model checkpoints. Using this approach, we track the evolution of linguistic features during pretraining. We train crosscoders between open-sourced checkpoint triplets with significant performance and representation shifts, and introduce a novel metric, Relative Indirect Effects (RelIE), to trace training stages at which individual features become causally important for task performance. We show that crosscoders can detect feature emergence, maintenance, and discontinuation during pretraining. Our approach is architecture-agnostic and scalable, offering a promising path toward more interpretable and fine-grained analysis of representation learning throughout pretraining.

## 18. KG-MuLQA: A Framework for KG-based Multi-Level QA Extraction and Long-Context LLM Evaluation

- Authors: Nikita Tatarinov, Vidhyakshaya Kannan, Haricharana Srinivasa, Arnav Raj, Harpreet Singh Anand, Varun Singh, Aditya Luthra, Ravij Lade, Agam Shah, Sudheer Chava
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.2133769748843957
- Article: https://aclanthology.org/2026.acl-long.151/
- PDF: https://aclanthology.org/2026.acl-long.151.pdf
- Local PDF: pdf/2026-06-25_18_KG-MuLQA_ A Framework for KG-based Multi-Level QA Extraction and Long-Context LLM Evaluation.pdf

We introduce KG-MuLQA (Knowledge-Graph-based Multi-Level Question-Answer Extraction): a framework that (1) extracts QA pairs at multiple complexity levels (2) along three key dimensions – multi-hop retrieval, set operations, and answer plurality, (3) by leveraging knowledge-graph-based document representations. This approach enables fine-grained assessment of model performance across controlled difficulty levels. Using this framework, we construct a dataset of 20,139 QA pairs based on financial credit agreements and evaluate 16 proprietary and open-weight Large Language Models, observing that even the best-performing models struggle with set-based comparisons and multi-hop reasoning over long contexts. Our analysis reveals systematic failure modes tied to semantic misinterpretation and inability to handle implicit relations.

## 19. CoG: Controllable Graph Reasoning via Relational Blueprints and Failure-Aware Refinement over Knowledge Graphs

- Authors: Yuanxiang Liu, Songze Li, Xiaoke Guo, Zhaoyan Gong, Qifei Zhang, Huajun Chen, Wen Zhang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.211597103225442
- Article: https://aclanthology.org/2026.acl-long.708/
- PDF: https://aclanthology.org/2026.acl-long.708.pdf
- Local PDF: pdf/2026-06-25_19_CoG_ Controllable Graph Reasoning via Relational Blueprints and Failure-Aware Refinement over Knowledge Graphs.pdf

Large Language Models (LLMs) have demonstrated remarkable reasoning capabilities but often grapple with reliability challenges like hallucinations. While Knowledge Graphs (KGs) offer explicit grounding, existing paradigms of KG-augmented LLMs typically exhibit cognitive rigidity—applying homogeneous search strategies that render them vulnerable to instability under neighborhood noise and structural misalignment leading to reasoning stagnation. To address these challenges, we propose CoG, a training-free framework inspired by Dual-Process Theory that mimics the interplay between intuition and deliberation. First, functioning as the fast, intuitive process, the Relational Blueprint Guidance module leverages relational blueprints as interpretable soft structural constraints to rapidly stabilize the search direction against noise. Second, functioning as the prudent, analytical process, the Failure-Aware Refinement module intervenes upon encountering reasoning impasses. It triggers evidence-conditioned reflection and executes controlled backtracking to overcome reasoning stagnation. Experimental results on three benchmarks demonstrate that CoG significantly outperforms state-of-the-art approaches in both accuracy and efficiency.

## 20. GASim: A Graph-Accelerated Hybrid Framework for Social Simulation

- Authors: Xuan Zhou, Yanhui Sun, Hantao Yao, Allen He, Yongdong Zhang, Wu Liu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.2083873774832323
- Article: https://aclanthology.org/2026.acl-long.569/
- PDF: https://aclanthology.org/2026.acl-long.569.pdf
- Local PDF: pdf/2026-06-25_20_GASim_ A Graph-Accelerated Hybrid Framework for Social Simulation.pdf

Large-scale social simulators are essential for studying complex social patterns. Prior work explores hybrid methods to scale up simulations, combining large language models (LLM)-based agents with numerical agent-based models (ABM). However, this incurs high latency due to expensive memory retrieval and sequential ABM execution. To address this challenge, we propose GASim, a graph-accelerated hybrid multi-agent framework for large-scale social simulations. For core agents driven by LLM, GASim introduces Graph-Optimized Memory (GOM) to replace intensive LLM-based retrieval pipelines with lightweight propagation over a sparse memory graph. For the majority of ordinary agents, GASim employs Graph Message Passing (GMP), substituting sequential ABM execution with parallel updates by fine-grained feature aggregation and Graph Attention Network. We further introduce Entropy-Driven Grouping (EDG) that coordinates this hybrid partitioning, leveraging information entropy to dynamically identify emergent core agents situated in information-diverse neighborhoods. Extensive experiments show that GASim not only delivers a substantial 9.94× end-to-end speedup over the traditional hybrid framework but also consumes less than 20% of baseline tokens, significantly reducing costs while preserving strong alignment with real-world public opinion trends.

## 21. SRA: Span Representation Alignment for Large Language Model Distillation

- Authors: Quoc Phong Dao, Hoang Son Nguyen, Pham Khanh Chi, Tung Nguyen, Linh Ngo Van, Nguyen Thi Ngoc Diep, Trung Le
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.2044266632083356
- Article: https://aclanthology.org/2026.acl-long.1522/
- PDF: https://aclanthology.org/2026.acl-long.1522.pdf
- Local PDF: pdf/2026-06-25_21_SRA_ Span Representation Alignment for Large Language Model Distillation.pdf

Cross-Tokenizer Knowledge Distillation (CTKD) enables knowledge transfer between a large language model and a smaller student, even when they employ different tokenizers. While existing approaches mainly focus on token-level alignment strategies, which are often brittle and sensitive to discrepancies between tokenizers, we argue that the method of aggregating tokens into more robust representations before distillation is of equal importance. In this paper, we introduce SRA ( S pan R epresentation A lignment for Large Language Model Distillation), a novel framework that reframes CTKD through the physical lens of Multi-Particle Dynamical Systems. SRA shifts the fundamental unit of alignment from tokens to robust, tokenizer-agnostic spans. We model each span as a cluster of particles and represent its state by its Center of Mass (CoM) - an attention-weighted average that captures rich semantic information. We leverage the concept of span centers of mass with attention-derived weighting to prioritize the most salient spans. In addition, we employ a geometric regularizer to preserve the structural integrity of the representation space and introduce aligned span logit distillation to enhance knowledge transfer across models. In challenging cross-architecture distillation experiments, SRA consistently and significantly outperforms state-of-the-art CTKD baselines, validating our physically-grounded approach.

## 22. GAM: Hierarchical Graph-based Agentic Memory for LLM Agents

- Authors: Zhaofen Wu, Hanrong Zhang, Fulin Lin, Wujiang Xu, Xinran Xu, Yankai Chen, Henry Peng Zou, Shaowen Chen, Weizhi Zhang, Xue Liu, Philip S. Yu, Hongwei Wang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.204083008894348
- Article: https://aclanthology.org/2026.acl-long.1600/
- PDF: https://aclanthology.org/2026.acl-long.1600.pdf
- Local PDF: pdf/2026-06-25_22_GAM_ Hierarchical Graph-based Agentic Memory for LLM Agents.pdf

To sustain coherent long-term interactions, Large Language Model (LLM) agents must navigate the tension between acquiring new information and retaining prior knowledge. Current unified stream-based memory systems facilitate context updates but remain vulnerable to interference from transient noise. Conversely, discrete structured memory architectures provide robust knowledge retention but often struggle to adapt to fluid narrative evolution. To address this, we propose GAM, a hierarchical Graph-based Agentic Memory framework that explicitly decouples memory encoding from consolidation to effectively resolve the conflict between rapid context perception and stable knowledge retention. By isolating ongoing dialogue in a event progression graph and integrating it into a topic associative network only upon semantic shifts, our approach minimizes interference while preserving long-term consistency. Additionally, we introduce a Graph-guided, Multi-factor Retrieval strategy to enhance context precision. Experiments on LoCoMo and LongDialQA benchmarks indicate that our method consistently outperforms state-of-the-art baselines in both reasoning accuracy and computational efficiency.

## 23. Project Auto-World: Towards Automated Benchmarking of Neural Relational Reasoners

- Authors: Anirban Das, Joanne Boisson, Irtaza Khalid, Sumita Garai, Steven Schockaert
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-06-23
- DOI: Unavailable
- Categories: cs.AI, cs.LG
- Relevance: 3.202886674387164
- Article: http://arxiv.org/abs/2606.24965v1
- PDF: https://arxiv.org/pdf/2606.24965v1
- Local PDF: pdf/2026-06-25_23_Project Auto-World_ Towards Automated Benchmarking of Neural Relational Reasoners.pdf

Reasoning about relational structures remains a significant challenge for neural models, particularly when they must systematically apply learned knowledge to problem instances that are harder than those seen in training. Progress is hampered by the difficulty of evaluating such generalization, since a priori, it is rarely clear what makes an instance hard. We study how this issue can be addressed by using large language models (LLMs) to automate benchmark generation, learning to produce increasingly challenging instances in an end-to-end manner. Concretely, given a world parametrized by Datalog rules, and an Edge Transformer as the reasoning evaluator, we use LLM-driven evolutionary search (based on FunSearch) and autonomous agentic search to discover sampling functions that yield hard problem instances. We also show that the Edge Transformer can be improved using this data such that it generalizes well to further data perturbations. Finally, we show that the same machinery can be applied to novel worlds proposed by LLMs, opening the door to autonomous research on neural relational reasoning.

## 24. LLMs Underperform Graph-Based Parsers on Supervised Relation Extraction for Complex Graphs

- Authors: Paolo Gajo, Domenic Rosati, Hassan Sajjad, Alberto Barrón-Cedeño
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.2018447805637162
- Article: https://aclanthology.org/2026.acl-short.17/
- PDF: https://aclanthology.org/2026.acl-short.17.pdf
- Local PDF: pdf/2026-06-25_24_LLMs Underperform Graph-Based Parsers on Supervised Relation Extraction for Complex Graphs.pdf

Relation extraction represents a fundamental component in the process of creating knowledge graphs, among other applications. Large language models (LLMs) have been adopted as a promising tool for relation extraction, both in supervised and in-context learning settings. However, in this work we show that their performance still lags behind much smaller architectures when the linguistic graph underlying a text has great complexity. To demonstrate this, we evaluate four LLMs against a graph-based parser on six relation extraction datasets with sentence graphs of varying sizes and complexities. Our results show that the graph-based parser increasingly outperforms the LLMs, as the number of relations in the input documents increases. This makes the much lighter graph-based parser a superior choice in the presence of complex linguistic graphs.

## 25. MegaRAG: Multimodal Knowledge Graph-Based Retrieval Augmented Generation

- Authors: Chi-Hsiang Hsiao, Yi-Cheng Wang, Tzung-Sheng Lin, Yi-Ren Yeh, Chu-song Chen
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.199426760754581
- Article: https://aclanthology.org/2026.acl-long.2218/
- PDF: https://aclanthology.org/2026.acl-long.2218.pdf
- Local PDF: pdf/2026-06-25_25_MegaRAG_ Multimodal Knowledge Graph-Based Retrieval Augmented Generation.pdf

Retrieval-augmented generation (RAG) enables large language models (LLMs) to dynamically access external information, which is powerful for answering questions over previously unseen documents. Nonetheless, they struggle with high-level conceptual understanding and holistic comprehension due to limited context windows, which constrain their ability to perform deep reasoning over long-form, domain-specific content such as full-length books. To solve this problem, knowledge graphs (KGs) have been leveraged to provide entity-centric structure and hierarchical summaries, offering more structured support for reasoning. However, existing KG-based RAG solutions remain restricted to text-only inputs and fail to leverage the complementary insights provided by other modalities such as vision. On the other hand, reasoning from visual documents requires textual, visual, and spatial cues into structured, hierarchical concepts. To address this issue, we introduce a multimodal knowledge graph-based RAG that enables cross-modal reasoning for better content understanding. Our method incorporates visual cues into the construction of knowledge graphs, the retrieval phase, and the answer generation process. Experimental results across both global and fine-grained question answering tasks show that our approach consistently outperforms existing approaches on both textual and multimodal benchmarks.

## 26. SGPVT: Self-Generated Proximal Visual Tokens for Mitigating Proximal Collateral Damage in MLLM Unlearning

- Authors: Jiaqi Li, Zhijing Zhang, Jiahui Geng, Sheng Bi, Chuanyi Zhang, Fan Liu, Guilin Qi
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.1936837742219555
- Article: https://aclanthology.org/2026.acl-long.442/
- PDF: https://aclanthology.org/2026.acl-long.442.pdf
- Local PDF: pdf/2026-06-25_26_SGPVT_ Self-Generated Proximal Visual Tokens for Mitigating Proximal Collateral Damage in MLLM Unlearning.pdf

Machine unlearning in multimodal large language models (MLLMs) aims to remove specific concepts while preserving overall utility. However, existing approaches focus primarily on general utility metrics, overlooking the preservation of semantically related concepts. We present the first systematic analysis of this proximal collateral damage, revealing that forgetting vulnerability correlates strongly with visual embedding similarity in a smooth gradient across the semantic space. Based on this insight, we propose a novel unlearning framework that introduces Self-Generated Proximal Visual Tokens (SGPVTs), which are synthetically perturbed visual representations around the target concept. Our method employs an adaptive cosine-band curriculum with a dual-stream objective: forgetting the target via gradient ascent while distilling knowledge from a frozen teacher model into proximal tokens to prevent degradation. Extensive experiments demonstrate that our approach significantly outperforms existing methods in preserving semantically related concepts while achieving effective target unlearning, eliminating the need for manual retention set curation. Our source code will be released in the near future.

## 27. Interleaved Latent Visual Reasoning with Selective Perceptual Modeling

- Authors: Shuai Dong, Siyuan Wang, Xingyu Liu, Chenglin Li, Haowen Hou, Zhongyu Wei
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.1931280920607157
- Article: https://aclanthology.org/2026.acl-long.1351/
- PDF: https://aclanthology.org/2026.acl-long.1351.pdf
- Local PDF: pdf/2026-06-25_27_Interleaved Latent Visual Reasoning with Selective Perceptual Modeling.pdf

Interleaved reasoning paradigms enhance Multimodal Large Language Models (MLLMs) with visual feedback but are hindered by the prohibitive computational cost of re-encoding pixel-dense images. A promising alternative, latent visual reasoning, circumvents this bottleneck yet faces limitations: methods either fail to capture intermediate state evolution due to single-step, non-interleaved structures, or sacrifice precise perceptual modeling by over-compressing features. We introduce Interleaved Latent Visual Reasoning (ILVR), a framework that unifies dynamic state evolution with precise perceptual modeling. ILVR interleaves textual generation with latent visual representations that act as specific, evolving cues for subsequent reasoning. Specifically, we employ a self-supervision strategy where a momentum teacher model selectively distills relevant features from ground-truth intermediate images into sparse supervision targets. This adaptive selection mechanism guides the model to autonomously generate context-aware visual signals. Extensive experiments on multimodal reasoning benchmarks demonstrate that ILVR outperforms existing approaches, effectively bridging the gap between fine-grained perception and sequential multimodal reasoning.

## 28. LinkQA: Synthesizing Diverse QA from Multiple Seeds Strongly Linked by Knowledge Points

- Authors: Xuemiao Zhang, Can Ren, Chengying Tu, Rongxiang Weng, Hongfei Yan, Jingang Wang, Xunliang Cai
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.191444946988477
- Article: https://aclanthology.org/2026.acl-long.1036/
- PDF: https://aclanthology.org/2026.acl-long.1036.pdf
- Local PDF: pdf/2026-06-25_28_LinkQA_ Synthesizing Diverse QA from Multiple Seeds Strongly Linked by Knowledge Points.pdf

The advancement of large language models (LLMs) struggles with the scarcity of high-quality, diverse training data. To address this limitation, we propose LinkSyn, a KP-graph-based synthesis framework that for the first time enables flexible control over discipline and difficulty distributions while balancing KP coverage and popularity. LinkSyn extracts KPs from question-answering (QA) seed data and constructs a KP graph to synthesize diverse QA data from multiple seeds strongly linked by KPs and sampled from graph walks. Specifically, LinkSyn incorporates (1) a knowledge value function to guide the adjustment of path sampling probability and balance KP coverage and popularity during graph walks; (2) diffusion-based synthesis via a strong reasoning model by leveraging multiple seeds with dense logical associations along each path; and (3) high-difficulty QA enhancement within given disciplines by flexible difficulty adjustments. By executing LinkSyn, we synthesize LinkQA, a diverse multi-disciplinary QA dataset with 50B tokens. Extensive experiments on Llama-3 8B demonstrate that continual pre-training with LinkQA yields an average improvement of 11.51% on MMLU and CMMLU, establishing new SOTA results. LinkQA consistently enhances performance across model size and initial FLOPs scales.

## 29. LLMSurgeon: Diagnosing Data Mixture of Large Language Models

- Authors: Yaxin Luo, Jiacheng Cui, Xiaohan Zhao, Xinyi Shang, Jiacheng Liu, Xinyue Bi, Zhaoyi Li, Zhiqiang Shen
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.1881549918915697
- Article: https://aclanthology.org/2026.acl-long.1964/
- PDF: https://aclanthology.org/2026.acl-long.1964.pdf
- Local PDF: pdf/2026-06-25_29_LLMSurgeon_ Diagnosing Data Mixture of Large Language Models.pdf

The pretraining data mixture of Large Language Models (LLMs) constitutes their "digital DNA", shaping model behaviors, capabilities, and failure modes. Yet this composition is rarely disclosed, making post-hoc auditing of data combination or provenance difficult. In this work, we formalize Data Mixture Surgery (DMS) : given only generated text from a target LLM, estimate the domain-level distribution of its pretraining corpus under a predefined taxonomy. We propose LLMSurgeon , a strong framework that casts DMS as an inverse problem under the label-shift assumption. Rather than directly aggregating classifier outputs, LLMSurgeon estimates a calibrated soft confusion matrix and solves a constrained inverse problem to correct systematic domain confusion and recover the latent mixture prior. To evaluate, we introduce LLMScan , a recipe-verifiable evaluation suite built from open-source LLMs with transparent pretraining mixtures. Across LLMScan, LLMSurgeon recovers domain mixtures with high fidelity under fixed protocols. Our work presents a practical, post-hoc approach for auditing the digital DNA of foundation models without access to their training data. Code is available at: https://github.com/Yaxin9Luo/LLMSurgeon.

## 30. STK-Adapter: Incorporating Evolving Graph and Event Chain for Temporal Knowledge Graph Extrapolation

- Authors: Shuyuan Zhao, Wei Chen, Weijie Zhang, Xinrui Hou, Junfeng Shen, Boyan Shi, Shengnan Guo, Youfang Lin, Huaiyu Wan
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.1866119024160575
- Article: https://aclanthology.org/2026.acl-long.905/
- PDF: https://aclanthology.org/2026.acl-long.905.pdf
- Local PDF: pdf/2026-06-25_30_STK-Adapter_ Incorporating Evolving Graph and Event Chain for Temporal Knowledge Graph Extrapolation.pdf

Temporal Knowledge Graph (TKG) extrapolation aims to predict future events based on historical facts. Recent studies have attempted to enhance TKG extrapolation by integrating TKG’s evolving structural representations and textual event chains into Large Language Models (LLMs). Yet, two main challenges limit these approaches: (1) The loss of essential spatial-temporal information due to shallow alignment between TKG’s graph evolving structural representation and the LLM’s semantic space, and (2) the progressive dilution of the TKG’s evolving structural features during LLM fine-tuning. To address these challenges, we propose the Spatial-Temporal Knowledge Adapter (STK-Adapter), which flexibly integrates the evolving graph encoder and the LLM to facilitate TKG reasoning. In STK-Adapter, a Spatial-Temporal MoE is designed to capture spatial structures and temporal patterns inherent in TKGs. An Event-Aware MoE is employed to model intricate temporal semantics dependencies within event chains. In addition, a Cross-Modality Alignment MoE is proposed to facilitate deep cross-modality alignment by TKG-guided attention experts. Extensive experiments on benchmark datasets demonstrate that STK-Adapter significantly outperforms state-of-the-art methods and exhibits strong generalization capabilities in cross-dataset task. The code is available at https://github.com/Zhaoshuyuan0246/STK-Adapter.
