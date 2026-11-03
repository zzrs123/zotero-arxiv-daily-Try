# Paper Daily Reading - 2026-11-03

## 1. From WSIs to Bulk, Spatial and Single-Cell Transcriptomics via Multi-Scale Graph Neural Networks

- Authors: Miguel Andrade, José Almeida, Carlos Santiago, Catarina Barata
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-30
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.8502982880312118
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.41692v1
- PDF: https://arxiv.org/pdf/2610.41692v1
- Local PDF: pdf/2026-11-03_01_From WSIs to Bulk, Spatial and Single-Cell Transcriptomics via Multi-Scale Graph Neural Networks.pdf

Understanding the spatial distribution of gene expression is key to studying complex diseases like cancer. While Spatial Transcriptomics (ST) and Single-Cell Transcriptomics (scT) provide high-resolution insights, they remain expensive and scarce. In contrast, standard histopathology Whole-Slide Images (WSIs) paired with bulk RNA sequencing are widely available. This work introduces a Multi-Scale Graph Neural Network (GNN) capable of simultaneously predicting bulk, spatial, and single-cell transcriptomics directly from WSIs. By extracting morphological features using a Pathology Foundation Model (PFM) (UNI2-h) and constructing spatial graphs at both patch and cell levels, the model learns the hierarchical relationships within the tissue. The network is trained on a combined dataset of The Cancer Genome Atlas Program (TCGA), Visium, and Xenium samples across lung, kidney, and breast tissues. A hybrid training strategy is employed, leveraging direct supervision alongside weakly supervised consistency losses to ensure predictions align across biological scales. Results show the model accurately predicts gene expression at the slide level and moderately at the patch level (strongest on Xenium), and achieves moderate correlation at the challenging single-cell level. Furthermore, downstream tasks explore the clinical relevance of these predictions, demonstrating their utility in survival analysis, spatial hazard mapping, and tumor classification via molecular signatures.

## 2. Co$^2$ODE: Conditionally Coarse-Grained Model Discovery for Rewiring in Biochemical Networks

- Authors: Theodore de Pomereu, Fabian Fröhlich
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-30
- DOI: Unavailable
- Categories: q-bio.QM, cs.LG
- Relevance: 3.5368882803743262
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.41634v1
- PDF: https://arxiv.org/pdf/2610.41634v1
- Local PDF: pdf/2026-11-03_02_Co$^2$ODE_ Conditionally Coarse-Grained Model Discovery for Rewiring in Biochemical Networks.pdf

Biochemical networks propagate the signals that regulate cellular behaviour, and which routes carry them depends on cellular context: a shift in context rewires the network's effective dynamics. Mechanistic simulators are misspecified here because the effective dynamics emerge from an interaction structure that is only partially known. Model discovery instead learns the dynamics from data, but sparse, correlated measurements poorly identify a full network model. What matters is narrower: the portion the context rewires. We introduce conditionally coarse-grained ODEs (Co$^2$ODE), which model that portion as a sparse neural or symbolic ODE: a conditional mask selects the markers carrying the rewiring, and a variational autoencoder compresses the remaining markers into a learnt closure term. On single-cell phosphoproteomic data spanning 30 cancer-relevant overexpressions, Co$^2$ODE compresses a 30-marker panel into a 10-dimensional state while matching the predictive accuracy of a neural ODE fit to the full panel. The closure absorbs what the mask drops, hence the accuracy is insensitive to which markers are kept. Adding a prior score to the loss shifts the selected markers at no cost in fit, indicating the data are not interventional enough to identify the underlying biology.

## 3. DIFFNAS: Predictor-Free Neural Architecture Search via Diffusion Model and Zero-Cost Evaluation

- Authors: Yize Sun, Hanzhang Ma, Zixin Wu, Xuechun Li, Volker Tresp, Yunpu Ma
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-30
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.3422895016207645
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.41818v1
- PDF: https://arxiv.org/pdf/2610.41818v1
- Local PDF: pdf/2026-11-03_03_DIFFNAS_ Predictor-Free Neural Architecture Search via Diffusion Model and Zero-Cost Evaluation.pdf

Neural Architecture Search (NAS) has advanced the automated design of deep networks, but remains computationally expensive due to reliance on model training or performance predictors. We introduce DIFFNAS, a predictor-free NAS framework that leverages a discrete graph diffusion model guided by zero-cost performance proxies. Unlike prior diffusion-based NAS methods that require learned performance predictors, DIFFNAS conditions the generative process on training-free metrics such as MeCo and SWAP, enabling efficient architecture search with minimal computational overhead. Experiments on NAS-Bench-201 show that DIFFNAS finds the optimal architectures for CIFAR-10 and CIFAR-100 (94.37% and 73.51%) without a pretrained predictor, while reducing search cost by up to 17.5x compared to DiffusionNAG. On the MobileNetV3 search space, its accuracy is lower than that of DiffusionNAG. These results highlight the promise of diffusion models combined with zero-cost proxies for scalable and effective architecture search.

## 4. Connectivity-Aware Client Selection in Decentralized Federated Learning

- Authors: Usevalad Milasheuski, Monica Nicoli, Stefano Savazzi
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-30
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 3.3313995425905416
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.41570v1
- PDF: https://arxiv.org/pdf/2610.41570v1
- Local PDF: pdf/2026-11-03_04_Connectivity-Aware Client Selection in Decentralized Federated Learning.pdf

Decentralized federated learning (DFL) has emerged as a scalable alternative to centralized federated learning, removing the single point of failure and communication bottleneck at the server. However, most existing decentralized approaches rely on full-neighborhood broadcasting, where each client transmits its model update to all of its neighbors in each communication round. While effective, this results in significant communication overhead and high energy consumption. This paper applies spectral graph tools as lightweight client selection methods that leverage the graph topology by analyzing the spectral properties of the graph Laplacian over a fixed communication graph. Specifically, we exploit eigenvector embeddings and heat/diffusion kernel similarities to guide each client in selecting only a subset of structurally relevant neighbors, i.e., those that are most beneficial for the convergence of the federation process. This topology aware randomization matches or outperforms uniform neighborhood subsampling and approaches the accuracy of full broadcasting. The largest gains, about $3$ percentage points, emerge under strong data heterogeneity on larger, structurally rich graphs, while the total number of transmitted messages is reduced by $50\%$ compared to naive broadcasting.

## 5. scAnyOmics: Foundation-Model Distillation for Any-to-Any Completion of Multi-omics Virtual Cells

- Authors: Zhaoqi Song, Ye Du, Yusuke Iwasawa, Yutaka Matsuo, Qian Niu
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-30
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 3.3221966207081395
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.41399v1
- PDF: https://arxiv.org/pdf/2610.41399v1
- Local PDF: pdf/2026-11-03_05_scAnyOmics_ Foundation-Model Distillation for Any-to-Any Completion of Multi-omics Virtual Cells.pdf

Recent advances in single-cell technologies have enabled the profiling of multiple molecular modalities, including transcriptomics, proteomics, and chromatin accessibility, providing a more comprehensive understanding of cellular states. However, integrating heterogeneous modalities and predicting missing molecular information remain challenging, particularly when paired measurements are limited. Here, we introduce scAnyOmics, a generative framework that distills knowledge from a frozen single-cell foundation model into a multimodal student model. scAnyOmics integrates scRNA-seq, protein-marker measurements, and scATAC-seq into a shared representation, enabling cross-modal prediction and reconstruction of missing modalities. We assembled 690,880 cells from six publicly available studies, covering both paired and partially paired multi-omics measurements, to systematically evaluate its predictive performance. We further evaluated scAnyOmics on held-out donor data, where it outperformed baseline methods across multiple evaluation metrics. Beyond cross-modal reconstruction, we explored its applications in cell-type annotation, perturbation-response prediction, and biological age estimation. Overall, scAnyOmics provides a unified framework for integrating incomplete single-cell multi-omics data and transferring pretrained biological knowledge, supporting the development of virtual cell models across diverse cellular contexts and experimental platforms.

## 6. Differential rank preservation manifold learning

- Authors: Henry Han, Luyu Niu, Diane Li, Jiacun Wang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-30
- DOI: Unavailable
- Categories: cs.AI, cs.LG
- Relevance: 3.281905830740776
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.41107v1
- PDF: https://arxiv.org/pdf/2610.41107v1
- Local PDF: pdf/2026-11-03_06_Differential rank preservation manifold learning.pdf

Manifold learning methods like t-SNE and UMAP preserve local neighborhoods, but they do not preserve the ranking of the neighbors inside them. Two embeddings can return the same neighbor set while disagreeing on which point is closest. This loss of order degrades downstream applications that value the order in the embedding. We propose Smooth Rank t-SNE (SR-tSNE), which adds a differentiable rank term to the standard t-SNE loss. To enable efficient training, this term uses a sigmoid rank approximation to explicitly force a point's true high-dimensional neighbors to outrank unrelated intruders and retain their original order. We also introduce Ordinal DLP (O-DLP), an extension of the Degree of Locality Preservation (DLP) metric that credits a neighbor only when it returns at its original rank. Across eight benchmarks spanning image, text, speech, remote-sensing and single-cell data, SR-tSNE outperforms 12 baselines in rank preservation and neighborhood overlap. Ablation studies demonstrate our rank term alone boosts O-DLP by 5% to 28%, a gain not achievable using standard pairwise loss. This advantage transfers to downstream applications. SR-tSNE achieves the best label-transfer performance across seven vision datasets. For cell-type discovery across six single-cell datasets, it ranks first in 17 of 18 dataset-metric combinations, whether clustering resolution is selected with or without cell-type labels. In intraday trading, SR-tSNE achieves higher returns, lower risk, and lower turnover than the baselines. To our knowledge, SR-tSNE is the first t-SNE-family method with explicit order preservation.

## 7. ReX-GG: a LLM Ensemble Pipeline for Relation-extraction and Graph Generation

- Authors: Giacomo Magnifico, Eduard Barbu
- Source: arxiv
- Venue type: preprint
- Journal: Proceedings of the Knowledge Graphs and Large Language Models Workshop (KG-LLM) @ LREC26, Palma, Mallorca, Spain, 2026, pp. 93-101
- Publication status: preprint
- Publication date: 2026-10-30
- DOI: 10.63317/2qkh8idwebsv
- Categories: cs.AI
- Relevance: 3.273714351702371
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.41901v1
- PDF: https://arxiv.org/pdf/2610.41901v1
- Local PDF: pdf/2026-11-03_07_ReX-GG_ a LLM Ensemble Pipeline for Relation-extraction and Graph Generation.pdf

Current LLM ensemble frameworks focus on multi-step setups with additional modules for answer ranking, often opting for token and span analysis rather than structured outputs, leading to heavyweight architectures with potential fail states along the pipeline. Faster, lighter solutions are more vulnerable to hallucination propagation and can lack output control in more complex pipelines. This paper proposes a customisable, lightweight ensemble workflow of coordinated Large Language Models that leverages JSON-structured outputs and anonymous peer-review ranking to mitigate hallucinatory outputs and single-model failure points. The pipeline is demonstrated on a relation extraction task applied to popular science articles in English, targeting four ontologically-grounded relation types (strong causation, weak causation, contrastive, and compositional), with semantic node canonicalisation and interactive, colour-coded HTML causal graphs as the final output. Performance is evaluated through an anonymous user study, achieving an average perceived accuracy of 0.778 against a human-annotated gold standard. The modular architecture supports flexible deployment across both API-based and in-house LLM setups, and the full framework is released under an open license to foster reproducibility and collaborative research.

## 8. Implicit Assumptions About Tasks in Continual Learning

- Authors: Kathrin Korte, Christian Metzner, Akshay Bedhotiya, Viet Anh Khoa Tran, Eleni Nisioti, Sebastian Risi
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-30
- DOI: Unavailable
- Categories: cs.LG, cs.AI
- Relevance: 3.228940932255088
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.41792v1
- PDF: https://arxiv.org/pdf/2610.41792v1
- Local PDF: pdf/2026-11-03_08_Implicit Assumptions About Tasks in Continual Learning.pdf

Continual learning is the study of how a model accumulates knowledge from data received over time, rather than all at once. In practice, this is typically achieved by dividing a dataset into tasks and presenting them sequentially. Explanations of the resulting measurements take into account factors such as the similarity between segments, the rate at which the data changes and the order of presentation. Each of these factors can be defined in terms of the underlying data, the partition imposed on it, or the learner that encounters it. These levels do not necessarily coincide, and it is usually left implicit which level a reported quantity refers to. We separate these and identify which properties acquire a value at each level. In controlled teacher--student experiments, we demonstrate that partitioning the same underlying trajectory at different levels of granularity, changing the order of presentation, and varying the similarity structure of the underlying data all result in different measured outcomes. We review representative benchmarks to determine which of these properties are stated. Where the underlying data cannot be inspected, as in foundation models built on undisclosed pre-training corpora, its properties are inherited by the model's initial state, and the training applied on top of it can be described.

## 9. When Everyone Can Build a Model: Mechanistic Inference in the Age of AI

- Authors: Marvin van Aalst, Adèle H. Ribeiro, Anna Matuszyńska
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-30
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.2071184770311683
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.41454v1
- PDF: https://arxiv.org/pdf/2610.41454v1
- Local PDF: pdf/2026-11-03_09_When Everyone Can Build a Model_ Mechanistic Inference in the Age of AI.pdf

Modern deep learning and AI-assisted code generation are lowering the technical barrier to building mathematical models of biological systems that reproduce complex observations. This lets researchers with domain expertise build semi-mechanistic, hybrid models constrained by prior knowledge and augmented with learned structure without extensive training in modelling. However, easier construction does not make interpretation easier: predictive success of such so-called grey-box models does not establish that an inferred mechanism corresponds to the one that generated the data, and the learned component can absorb errors in the mechanistic part. Many biological modelling problems are underdetermined, so several, possibly infinitely many, models may reproduce the same data equally well. This ambiguity enters at two modelling choices: which variables can affect others, and which response function describes the underlying mechanism. For the first choice, causal inference provides a formal framework stating which causal relationships and intervention effects are identifiable from the data and available knowledge. For the second, ensemble analyses quantify the uncertainty and the range of behaviours still allowed by models that fit equally well. Together, they turn a single good fit into an explicit account of what is supported, what remains open, and which experiment would decide.

## 10. Breaking Information Islands in Sparse Tuning via Small-World Connectivity

- Authors: Xianchao Guan, Zijun Xiong, Yifeng Wang, Yubo Cui, Yaowei Wang, Guo-Sen Xie, Xin Li, Zheng Zhang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-30
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 3.1814356970894764
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.41665v1
- PDF: https://arxiv.org/pdf/2610.41665v1
- Local PDF: pdf/2026-11-03_10_Breaking Information Islands in Sparse Tuning via Small-World Connectivity.pdf

Sparse tuning is widely used to adapt large language models due to its parameter efficiency. However, its effectiveness depends not only on the number of trainable parameters, but also on the feature-interaction topology of the sparse update's structural support. Limited or uneven connectivity in this support may isolate subsets of feature dimensions, forming information islands that restrict direct task-specific interactions through the trainable update. To address this issue, we propose Small-World Induced Fine-Tuning (SWIFT), a sparse tuning framework inspired by small-world connectivity. SWIFT combines block-diagonal sparse updates for local feature mixing with a fixed deterministic scattering permutation that routes the mixed outputs across feature groups without additional trainable parameters. We further show theoretically that certain random sparse-update models and block-diagonal updates can exhibit information islands, whereas a sufficiently scattering permutation guarantees positive block-level expansion when the trainable block-diagonal factor consists of equal-sized, structurally dense square blocks. Extensive experiments on commonsense reasoning, natural language generation, and image classification demonstrate that SWIFT outperforms the evaluated parameter-efficient fine-tuning (PEFT) baselines on average and can match or surpass full fine-tuning. Implementation is available at https://github.com/xianchaoguan/SWIFT

## 11. When Links Mislead: Label-Free Structural Polarity for Zero-Shot Classification of Web Pages

- Authors: Hanshuai Cui, Zhiqing Tang, Zhi Yao, Weijia Jia, Jun Luo
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-30
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.1573502006336556
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.41464v1
- PDF: https://arxiv.org/pdf/2610.41464v1
- Local PDF: pdf/2026-11-03_11_When Links Mislead_ Label-Free Structural Polarity for Zero-Shot Classification of Web Pages.pdf

Web platforms such as digital libraries, online stores and university sites must classify new pages before anyone labels them. Large language models (LLMs) can label each page from its text, but these labels are noisy, and links could correct them only where linked pages share classes. Existing zero-shot methods ignore the links, or pull a page toward its neighbours as label propagation and graph neural networks (GNNs) do, which hurts where linked pages differ in class. Others weight propagation by an LLM-estimated homophily that costs extra calls and drifts across LLMs. We find that the sign with which links should enter a prediction, which we call structural polarity, is readable without true labels. It is the excess agreement of LLM labels and text-prototype predictions along links. We thus propose ZeroPolar, which gates one signed propagation step by this statistic. Training-free ZeroPolar mixes prototype scores with any number of LLM labels, and ZeroPolar-T denoises the labels with a text classifier once half of the pages carry one. With one GPT-4o label per page, ZeroPolar-T reaches the highest mean accuracy on eleven graphs (73.99%), 6.01 points above LLM-BP and significantly above all eighteen baselines we compare. With LLM labels on only 5% of the pages, training-free ZeroPolar leads a GNN trained on these labels by 10.80 points.

## 12. ImplicitHop: Evaluating knowledge integration across context and memory

- Authors: Alexander Detkov, Dashiel Karish, Matthew Oleynikov, Matt Thomson
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-30
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 3.1463141534889294
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.41169v1
- PDF: https://arxiv.org/pdf/2610.41169v1
- Local PDF: pdf/2026-11-03_12_ImplicitHop_ Evaluating knowledge integration across context and memory.pdf

The ability to integrate new information and deduce its consequences is central to learning, understanding, and reasoning in large language models (LLMs). Whether information arrives during training or in-context, models must not only store local facts, but propagate their long-range implications globally. To explore information integration in LLMs, we introduce two complementary natural language benchmarks for large-scale evaluation of deductive reasoning as a function of inference depth. The first is a formal graph benchmark enabling controlled evaluation over a wide range of graph topologies and integration tasks; the second is a knowledge composition benchmark grounded in real-world knowledge graphs. We use these benchmarks to compare knowledge integration from information encoded in context versus information encoded in model weights during pretraining, evaluating a set of open models implicitly, without chain of thought. We find that accuracy decays sharply with increased composition length for both pretrained and in-context knowledge. Information presented in-context, however, substantially outperforms deduction over information encoded in weights. These results quantify a fundamental limitation of current models with direct implications for prompt-based control of agent behavior and for continual learning strategies, and they provide a foundation for developing training, prompting, and integration methods that support deeper reasoning.

## 13. Sparse Text Diffusion under Dual Budgets: Context Connectivity and Expert Activation

- Authors: Alexandros Christoforos, Chadbourne Davis, Paul Raj
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-30
- DOI: Unavailable
- Categories: cs.CL, cs.AI
- Relevance: 3.1289540877455133
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.41487v1
- PDF: https://arxiv.org/pdf/2610.41487v1
- Local PDF: pdf/2026-11-03_13_Sparse Text Diffusion under Dual Budgets_ Context Connectivity and Expert Activation.pdf

Long-context diffusion repeatedly pays for both token interaction and feed-forward computation. We formulate these costs as two separate budgets: the edges available to an attention graph and the experts activated for each token. This view connects local, dilated, and global attention with conditional expert computation without assuming that sparsity alone preserves document-level information. We specify normalized masked attention, distinguish denoising depth from sampling iterations, and derive graph and compute bounds. A reported sparse-expert configuration, denoted DualBudget, is analyzed across scientific summarization, multi-hop question answering, dialogue, and sentence-pair prediction. All supplied table measurements are retained. The length study shows gains over the listed baselines through 16K, together with measurable degradation as length increases. Ablations reveal mixed changes across the three reported scores, while the cost record indicates a 20% reduction relative to DiffuSeq under an unspecified timing convention. The analysis separates these observations from unmeasured claims about training speed, absorbing states, global coherence, and deployment memory.

## 14. Characterizing Recoverable Expert-Utilization Signatures in Fine-Tuned Mixture-of-Experts LLMs

- Authors: Fei Wang, Baochun Li, Bo Li
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-29
- DOI: Unavailable
- Categories: cs.LG, cs.AI, cs.CR
- Relevance: 3.0486640203872932
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.41039v1
- PDF: https://arxiv.org/pdf/2610.41039v1
- Local PDF: pdf/2026-11-03_14_Characterizing Recoverable Expert-Utilization Signatures in Fine-Tuned Mixture-of-Experts LLMs.pdf

As Mixture-of-Experts (MoE) large language models are increasingly deployed in distributed environments, from federated learning to edge-cloud systems, their architecture harbors an underexplored landscape of security vulnerabilities. Moving beyond textual analysis, we uncover structural memorization: a novel vulnerability where a fine-tuned model memorizes not only its training data but also the internal pathway used to process it, creating a characteristic routing fingerprint unique to the training process. We provide comprehensive empirical evidence that structural memorization emerges consistently even from a few samples, and that its intensity is directly influenced by the choice of trainable modules.
  We show that these memorized expert pathways can be stealthily recovered through the model's unconditional generation, using only routing and output logits, with no knowledge of the fine-tuning data or procedure. In distributed deployments, this vulnerability is amplified as routing information is exposed at multiple trust boundaries, including federated aggregation points, edge-cloud interfaces, and multi-tenant monitoring systems. Recovery exposes a critical blind spot: traditional membership inference metrics, viewed through the lens of expert routing, fail to identify memorized data corresponding to these structural pathways. To close this gap, we devise composite metrics combining reference model tail likelihood with complexity-aware normalization, significantly improving detection of memorized routing structures. This enables adversaries to pinpoint critical experts shaped by fine-tuning, whether dominant or dormant, and execute targeted attacks such as router manipulation or backdoor injection in realistic distributed settings where attackers lack training data but can observe routing patterns across system components.

## 15. Aligning MLLMs with the Latent Structure of Human Cognition via Behavior-Derived Semantic Dimensions

- Authors: Ning E, Changde Du, Yizhuo Lu, Huiguang He
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-30
- DOI: Unavailable
- Categories: cs.CL, cs.AI
- Relevance: 3.0427427971314347
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.41951v1
- PDF: https://arxiv.org/pdf/2610.41951v1
- Local PDF: pdf/2026-11-03_15_Aligning MLLMs with the Latent Structure of Human Cognition via Behavior-Derived Semantic Dimensions.pdf

Multimodal Large Language Models (MLLMs) have achieved impressive performance across a wide range of reasoning tasks, yet it remains unclear whether their internal representations and decision criteria align with the latent structure of human cognition. In this work, we propose a novel framework to align MLLMs with the multidimensional mental representations underlying human similarity judgements. We build on a previously established behavior-derived semantic embedding space, in which objects are represented along 66 interpretable dimensions derived from 4.70 million human Odd-One-Out (O1O) judgements. For each triplet, we infer the most salient decision dimension and convert it into a dimension-grounded linguistic rationale. This enables MLLMs to learn both the final choice and a justification consistent with the inferred behavioral criterion. Experimental results demonstrate that our approach improves model consistency with human similarity judgements while retaining competitive performance on standard multimodal benchmarks. Furthermore, using searchlight Representational Similarity Analysis (RSA) on an independent fMRI Natural Scenes Dataset (NSD), we observe increased representational alignment between model and human. Ultimately, our findings point to a data-driven route for incorporating human cognitive structure into MLLMs alignment. The code is available \href{https://github.com/ening-open/cogalign}{here}.

## 16. Subquadratic Attention with a Hierarchical Tree-Structured Indexer

- Authors: Leon Lufkin, Cutter Dawes, Alexander Speicher, Kamesh Krishnamurthy, Tomás Figliolia, Beren Millidge
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-30
- DOI: Unavailable
- Categories: cs.CL, cs.AI
- Relevance: 3.0423165391778664
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.42112v1
- PDF: https://arxiv.org/pdf/2610.42112v1
- Local PDF: pdf/2026-11-03_16_Subquadratic Attention with a Hierarchical Tree-Structured Indexer.pdf

The quadratic scaling of attention is a fundamental bottleneck limiting the long-context capabilities of large language models (LLMs). A variety of approaches have attempted to circumvent this, but they either fail to match attention's expressiveness (e.g., sliding-window or linear attention variants with fixed-size state) or only achieve constant-factor speedups (e.g., sparse attention methods whose indexers themselves scale quadratically). In this paper, we derive an asymptotically subquadratic sparse attention method based on a hierarchical, tree-structured indexer, which we call Zyphra Hierarchical Attention (ZHA). ZHA constructs a tree of recursively compressed key summaries over the KV cache, which future queries traverse from the top down to retrieve a sparse subset of keys. Crucially, by iteratively growing the tree's depth, the total cost including routing and final attention grows sublinearly in sequence length, resulting in overall subquadratic (but superlinear) scaling for attention. We demonstrate that ZHA can be cheaply applied to existing pretrained models with only a short KL distillation training stage over a few billion tokens, and maintains performance on long-context retrieval and challenging reasoning, mathematical, and agentic coding evaluation tasks. Moreover, we show that our method is highly robust to tree geometry including very deep trees of up to 6 levels. Finally, we develop a detailed performance model and show that our approach scales subquadratically, dramatically outperforms competing methods beyond 1 million context, and ultimately has the potential to extend effective context windows to the hundreds of millions or billions of tokens.

## 17. WebOverlay: High-Throughput Vision-Only Distillation for Extreme Aspect-Ratio Web Overlay Detection

- Authors: Jiannan Huang, Jerry Ding, Li Yu, Zhenting Li
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-29
- DOI: Unavailable
- Categories: cs.CV, cs.AI, cs.IR
- Relevance: 3.041510812342305
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.41037v1
- PDF: https://arxiv.org/pdf/2610.41037v1
- Local PDF: pdf/2026-11-03_17_WebOverlay_ High-Throughput Vision-Only Distillation for Extreme Aspect-Ratio Web Overlay Detection.pdf

Web overlays, such as cookie consent banners, newsletter prompts, and age gates, obstruct automated web crawlers and degrade downstream document representations. While proprietary multimodal Large Language Models (MLLMs) can accurately identify overlays, their latency and inference cost preclude web-scale ingestion. Conversely, lightweight vision models struggle with full-page renderings characterized by extreme vertical aspect ratios, where standard isotropic resizing collapses critical text features and causes false positives. In this work, we present WebOverlay, a high-throughput vision-only detector trained via distillation from a frontier vision-language teacher. We establish a dynamic tiling strategy that partitions extreme aspect-ratio web renders into aspect-preserving patches with spatial overlap, coupled with an aspect-ratio-aware boundary adjudication mechanism to eliminate boundary artifacts. To eliminate cross-modal latency overheads, our student model relies purely on visual cues, bypassing DOM tree parsing. WebOverlay significantly outperforms DOM-based heuristics and achieves competitive precision and recall against heavy proprietary MLLM baselines while delivering multiple orders of magnitude higher throughput and substantially reduced deployment costs.

## 18. Latent Reasoning in Continuous Space for Unified Multimodal Models

- Authors: Byungwoo Jeon, Yoonwoo Jeong, Hyunseok Lee, Minsu Cho, Jinwoo Shin
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-30
- DOI: Unavailable
- Categories: cs.CV, cs.CL, cs.LG
- Relevance: 3.0212469412002365
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.42149v1
- PDF: https://arxiv.org/pdf/2610.42149v1
- Local PDF: pdf/2026-11-03_18_Latent Reasoning in Continuous Space for Unified Multimodal Models.pdf

Unified Multimodal Models (UMMs) achieve remarkable success on diverse multimodal understanding and generation tasks, yet they still struggle to effectively leverage language-based chain-of-thought reasoning for image generation. As a result, existing reasoning-augmented UMMs often fail to inherit the test-time scaling and fine-grained controllability observed in large language models. We attribute this failure to a fundamental modality mismatch: reasoning is performed in a discrete token space, whereas image generation operates in a continuous space. To bridge this gap, we introduce a Latent Reasoning framework in Continuous space (LARC), which alleviates the token-level bottleneck by reasoning over continuous hidden states. Specifically, the training framework consists of two stages: (i) curriculum supervised fine-tuning (SFT), and (ii) information-gain reinforcement learning (RL). First, the curriculum SFT stage gradually converts token-level reasoning into latent reasoning. Subsequently, the information-gain RL stage self-evolves latent reasoning without ground truth supervision. Experiments across diverse text-to-image generation benchmarks show that LARC consistently improves generation quality, prompt following, and compositional fidelity. Notably, LARC achieves state-of-the-art performance on GenEval with a 7%p gain over BAGEL and demonstrates clear test-time scaling behavior, outperforming token-based generation under both parallel and sequential test-time scaling strategies.

## 19. Automatic Construction of Strong Simple Baselines

- Authors: Caleb N. Ellington, Jiaqi Wang, Sohan Addagudi, Elijah Cole
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-28
- DOI: Unavailable
- Categories: cs.LG, q-bio.QM
- Relevance: 3.0029297150139596
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.40700v1
- PDF: https://arxiv.org/pdf/2610.40700v1
- Local PDF: pdf/2026-11-03_19_Automatic Construction of Strong Simple Baselines.pdf

To rigorously establish the value of a novel deep learning method, it must be compared against appropriate baselines. As deep learning has become increasingly common in the physical and life sciences, there have been numerous cases in which apparent progress has turned out to be an artifact of omitted or missing baselines. In this work, we investigate whether this problem can be mitigated by using large language models to automate the construction of baselines. We assemble 36 supervised classification and regression tasks from peer-reviewed studies in Nature, Science, and Cell-family journals that investigate novel deep learning methods for scientific applications. We then use a language model to construct simple baselines for each task. These automatically constructed baselines are strong, recovering a median of 95.5% (mean 85.7%) of the gap between a trivial predictor and the score of the deep learning model. The median simple baseline matches or exceeds the performance of the deep learning model in 12 studies. We further examine the variation across scientific domains and publication venues and we characterize the effects of test-time compute and access to different levels of study context. As human peer review has struggled to keep up with the rapidly increasing volume of research articles in recent years, our results suggest that automated baseline construction is a practical and scalable check on deep learning contributions in the physical and life sciences.

## 20. MEMIG: Self-evolving Memory Construction for Antibody Optimization

- Authors: Yunhui Jang, Zach Wang, Jai Doshi, Kangway Chuang, Sidney Lisanza, Taylor Joren
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-30
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 2.9993138770514935
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.41245v1
- PDF: https://arxiv.org/pdf/2610.41245v1
- Local PDF: pdf/2026-11-03_20_MEMIG_ Self-evolving Memory Construction for Antibody Optimization.pdf

Memory has become central to self-evolving LLM agents, which store and retrieve experience from past rollouts to guide future decisions. Existing systems represent this experience as free-form natural language and maintain it by rewriting, which fits tasks whose experience is narratable. However, in scientific discovery and optimization, experience is often a quantity measured by an oracle under a specific context. Rewriting it as text leaves no index for where a record should be, replaces a measurement with a description, and cannot express how interventions interact. To address this, we argue that agent memory for biomolecule optimization should instead be indexable, quantitative, and structured, and we introduce MEMIG. This memory construction framework realizes these three properties. In detail, MEMIG addresses each insight with a domain-grounded identifier and accumulates the quantitative effect measured by a property oracle, so that updates remain local and retrieval becomes an exact lookup. Next, MEMIG connects insights whose interventions are applied together and measures their epistasis by decomposing each evaluated set. Our results show that MEMIG improves performance in most settings across in silico antibody optimization tasks.

## 21. Latent-Lens: Visual Perception in Small Language Models Through Latent Communication

- Authors: Mo Shahdloo, Faegheh Sardari, Mathew Salvaris
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-30
- DOI: Unavailable
- Categories: cs.LG, cs.AI
- Relevance: 2.9837408432687185
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.41751v1
- PDF: https://arxiv.org/pdf/2610.41751v1
- Local PDF: pdf/2026-11-03_21_Latent-Lens_ Visual Perception in Small Language Models Through Latent Communication.pdf

Bridging independent vision-language models (VLMs) and small language models (SLMs) in a modular multi-agent system typically forces them to exchange information as discrete text, which creates a lossy bottleneck for spatial and fine-grained details. This constraint is especially acute for SLMs, whose limited capacity makes them more reliant on the quality of the input signal. Recent latent-communication methods exchange states between language models. How a VLM can pass visual information to a separately pretrained text-only SLM though remains unexplored. We propose \textbf{Latent-Lens}, a lightweight codec that bridges the representation gap between a frozen VLM and a frozen SLM directly in latent space, enabling them to communicate purely through hidden states. The codec consists of a domain encoder that projects hidden states from the VLM into the SLM's embedding space, and an attention decoder formalised as a LoRA that teaches the SLM to attend to these visual prefixes, while training only ${\sim}1.6$M parameters (0.2\% of the combined model size). On visual question answering (CLEVR, GQA), Latent-Lens achieves $81.0\pm7.9$\% and $65.4\pm5.4$\%, compared with $58.3\pm5.7$\% and $61.8\pm1.0$\% for text communication with the same LoRA budget (+30.2--69.8pp relative to frozen text communication), while on image captioning (Flickr8k) it improves over the same baseline by +16.5 (+18.8 frozen). We also evaluate Latent-Lens with TinyLlama-1.1B and InternVL2-1B, which use different architectures, vocabularies, and hidden dimensions.

## 22. Isoform-resolved spatial transcriptomics on a lab-made high-density array via a single-chip NGS-TGS workflow

- Authors: Zhiliang Yue, Min Liu, Yongqi Liu, Dongdong Lu, wenjun ji, Menglong Zhang, Yuntong Wang, Yan Shi, Yuanyuan Miao, Suchen Wang, Yifan Jiang, Zhe Ma, Yue Wang, Jun Zhao, Naixu Liu, Chunyu Lv, Jixian Zhai, Bosheng Li
- Source: openalex
- Venue type: journal
- Journal: Nature Communications
- Publication status: published
- Publication date: 2026-11-01
- DOI: https://doi.org/10.1038/s41467-026-79323-w
- Categories: Single-cell and spatial transcriptomics, Genomics and Phylogenetic Studies, RNA Research and Splicing
- Relevance: 2.9724929424508986
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://doi.org/10.1038/s41467-026-79323-w
- PDF: Unavailable
- Local PDF: Not downloaded

Spatial transcriptomics maps gene expression within tissue sections, but dominant short-read approaches have limited ability to resolve full-length transcript structures such as alternative splicing. Long-read sequencing provides transcript-structure information, although its higher sequencing error rates can complicate spatial-barcode identification on high-density arrays. Here, we show a lab-made, high-density spatial transcriptomics system that uses a tri-part combinatorial barcode design to expand barcode capacity and facilitate spatial assignment of long reads. By splitting full-length complementary DNA generated from a single capture chip, the workflow combines high-depth short-read quantification with single-molecule long-read profiling within the same spatial coordinate system. In incompatible tomato–pepper grafts and mouse embryos, the approach identifies spatially localized unannotated isoforms and intron-retention events, and reveals regional differences in isoform usage that are not apparent from gene-level expression alone. Together, this system provides a framework for combining spatial gene-expression quantification with full-length transcript-structure analysis in the same tissue. Existing spatial transcriptomics technologies typically rely on either short-read or long-read sequencing platforms. Here, the authors develop a high-density spatial transcriptomics system that integrates short-read quantitative profiling with long-read transcript isoform analysis at the same spatial coordinates.

## 23. Latent Sparse Attention: Towards Subquadratic Ultra-Long Context Attention

- Authors: Ales Kubicek, Andrea Caciolai, Liangzu Peng, Sukrit Sumant, Benjamin Hoover, Fraser Greenlee, Ruairidh M. Battleday, Radim Urban, Torsten Hoefler, James C. R. Whittington
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-30
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 2.9668617111008437
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.42147v1
- PDF: https://arxiv.org/pdf/2610.42147v1
- Local PDF: pdf/2026-11-03_23_Latent Sparse Attention_ Towards Subquadratic Ultra-Long Context Attention.pdf

Agentic workflows are increasingly shifting towards long-horizon tasks, such as open-ended scientific work, where models benefit from long context windows. However, at ultra-long context (above 1M tokens), full attention is prohibitively expensive. A promising approach is sparse attention, in which a dedicated indexer selects a subset of keys for the attention. Yet current methods of indexing either still have quadratic cost in context size or lose accuracy at ultra-long context scale. We address this with Latent Sparse Attention (LSA), an efficient attention method that maintains accuracy at ultra-long context. In LSA, keys are hierarchically clustered in a learned latent space, and queries score the hierarchy of clusters instead of scoring every key, making prefill, decode and training faster at long context. We propose two variants, Distilled-LSA (D-LSA), which can be applied to pre-trained models via distillation, and Native-LSA (N-LSA), which is trained natively on the next-token loss alone. On GLM-5.3-FLASH (QWEN-3.8-27B) at 10M tokens, D-LSA speeds up one attention layer by 22.7x (72.4x) in prefill and 4.6x (42.5x) in decode over its original sparse attention (full attention), while keeping similar accuracy across a variety of tasks. N-LSA matches the accuracy of full attention with a training speedup of 1.6x per layer at 128k tokens. LSA offers practical and efficient attention for models to benefit from ultra-long context.

## 24. Coarse-Graining Optimal Transport for Rollout-Free Post-Training of Flow Matching

- Authors: Soon Hoe Lim, Aditi Gupta, Michael W. Mahoney, N. Benjamin Erichson
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-30
- DOI: Unavailable
- Categories: stat.ML, cs.LG
- Relevance: 2.9645443039102854
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.41269v1
- PDF: https://arxiv.org/pdf/2610.41269v1
- Local PDF: pdf/2026-11-03_24_Coarse-Graining Optimal Transport for Rollout-Free Post-Training of Flow Matching.pdf

Flow matching depends critically on the coupling used to pair source and target samples. Optimal transport (OT) couplings can reduce velocity conflict and straighten trajectories; but, in practice, challenges remain: the source comes from a continuous distribution, only a finite number of target samples data are accessible, and the neural network has finite capacity. For these reasons, making the coupling more OT-like may not consistently improve sampling quality, in particular in the low number-of-function-evaluation (NFE) regime. Motivated by this, we introduce ReCouple, a controllable framework that constructs coarse-grained OT couplings, to better understand rollout-free OT-based post-training. We also consider extensions of this basic framework: ReCouple+ extends this toward the continuous-source setting by increasing source resolution, converging to semi-discrete OT in the appropriate limit; and ReCouple++ further adds spatial regularization, motivated by the observation that straight trajectories need not correspond to spatially simple velocity fields. Empirical validation demonstrates the effectiveness of these methods, and it reveals an NFE-dependent interplay between coupling optimality, neural realizability, and generation quality.

## 25. Experts Exhibit Structured Redundancy: Structure-Preserving Expert Pruning for Mixture-of-Experts Large Language Models

- Authors: Tian Wang, Yongding Tao, Yihong Dong, Xiaoming Wu, Ying Guo, Ge Li
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-30
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 2.9308651211017622
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.41236v1
- PDF: https://arxiv.org/pdf/2610.41236v1
- Local PDF: pdf/2026-11-03_25_Experts Exhibit Structured Redundancy_ Structure-Preserving Expert Pruning for Mixture-of-Experts Large Language Models.pdf

Sparse MoE mechanism significantly improves the trade-off between model capacity and inference efficiency. However, practical deployment still requires storing all experts, resulting in substantial memory overhead. We show that expert outputs in MoE layers exhibit structured redundancy. Across different models and task categories, the stable rank and entropy effective rank of expert outputs are consistently far below the nominal number of experts, while expert output distributions also exhibit fewer effective modes. Motivated by these observations, we reformulate expert pruning as a structure-preserving expert subset selection problem and efficiently optimize it via a greedy strategy, rather than only independently scoring and ranking individual experts or exhaustively searching over expert combinations. We propose two expert pruning methods under the unified structure-preserving framework: Projection Energy Expert Pruning (PEEP), which preserves the functional subspace by maximizing weighted projection energy, and Distributional Coverage Expert Pruning (DCEP), which preserves the distributional geometry by minimizing weighted coverage error. Both methods incorporate router-derived weights as priors, enabling them to jointly preserve the global structural relationships among experts while accounting for the local importance of individual experts. Experiments on DeepSeek-V2-Lite and Qwen3-30B-A3B demonstrate that, at the expert retention ratios of 75% and 50%, our methods outperform the state-of-the-art baselines on the majority of benchmarks and consistently achieve the best average performance across both general tasks and mathematical reasoning tasks.

## 26. CausalGrade: Evidence-Guided Causal Graph Scoring with Jev

- Authors: Jiangming Zhong, Jiawei Zhu, Guanting Wu, Qiaoxi Cai, Wanyi Chen, Jiale Li
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-28
- DOI: Unavailable
- Categories: stat.ML, cs.AI, cs.LG
- Relevance: 2.925116414583351
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.40692v1
- PDF: https://arxiv.org/pdf/2610.40692v1
- Local PDF: pdf/2026-11-03_26_CausalGrade_ Evidence-Guided Causal Graph Scoring with Jev.pdf

Evaluating the structural quality of candidate causal graphs when the true causal structure is unknown is an important problem in applying causal discovery results. This paper proposes CausalGrade, a causal graph scoring method based on the probabilistic judgment model Jev. The method jointly provides Jev with evidence of association, conditional dependence, and directionality from observational data and edge probabilities produced by the causal discovery foundation model CDFM. Jev produces probabilistic judgments about direct causal edges, and a graph-level score is obtained by measuring the agreement between the adjacency structure of the graph under evaluation and these edge-level judgments. Across 300 synthetic datasets, the score exhibits a relatively strong negative correlation with structural error in all 20 combinations of four causal discovery algorithms and five variable counts, indicating that higher scores generally correspond to smaller structural errors. In 500 synthetic graph selection tasks, CausalGrade achieves a best-candidate hit rate of 54.4\%, exceeding the 48.4\% achieved by the Self-Compatibility metric \(κ_G\), further supporting its ability to discriminate the structural quality of graphs under evaluation.

## 27. Structure-Aware Skill Retrieval and Arbitration for Optimization Modeling

- Authors: Anran Liu, Benzhao Hou, Zongsheng Cao, Daichao Wang, Lang Chen, Shitong Chen
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-30
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 2.9189809177242636
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.41909v1
- PDF: https://arxiv.org/pdf/2610.41909v1
- Local PDF: pdf/2026-11-03_27_Structure-Aware Skill Retrieval and Arbitration for Optimization Modeling.pdf

Large Language Models (LLMs) can turn natural-language optimization tasks into solver-checked answers, but current agents remain brittle under narrative rewrites and often store reusable experience at the instance level. We introduce \textsc{ArchOR}, an archetype-centric skill agent that builds on \textsc{OptSkills} by adding two retrieval-focused modules. \emph{Centroid-Aware Representation Learning} (CARL) refines the ordering of cached skill representations through a low-rank prototype residual. \emph{Signature-Guided Retrieval} (S\textsuperscript{3}R) attaches open-dimensional structural signatures to skills, prioritizes candidates by weighted Jaccard overlap, and bounds semantic re-ranking to a top-$K$ set. A baseline-preserving arbitration rule determines when the structural route should replace the original selector. With the same DeepSeek-V4.1-Flash backbone and released skill library, \textsc{ArchOR} reaches 65.00\% Micro-Avg.\ Pass@1 across five benchmarks, improving over \textsc{OptSkills} by 1.64~pp Micro-Avg.\ and 2.68~pp Macro-Avg.

## 28. Attention Maps Know When to Think: Training-Free Difficulty-Aware Chain-of-Thought for Reasoning Segmentation

- Authors: Chanseul Cho, Jaesung Jun, Dongheon Lee, Youngmin Ro
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-30
- DOI: Unavailable
- Categories: cs.CV, cs.AI
- Relevance: 2.912875663146031
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.41618v1
- PDF: https://arxiv.org/pdf/2610.41618v1
- Local PDF: pdf/2026-11-03_28_Attention Maps Know When to Think_ Training-Free Difficulty-Aware Chain-of-Thought for Reasoning Segmentation.pdf

Chain-of-Thought (CoT) prompting has become a standard reasoning strategy in Multi-modal Large Language Models (MLLMs), showing strong performance in complex vision-language tasks such as reasoning segmentation. However, our analysis reveals that indiscriminate CoT usage can lead to degraded performance by inducing unnecessary reasoning, a phenomenon we term overthinking. In reasoning segmentation, overthinking often leads to misalignment between the query's intent and visual grounding. To address this, we propose Difficulty-Aware Chain-of-Thought (DA-CoT), a training-free adaptive framework that selectively triggers CoT based on the input's intrinsic difficulty. We find that the entropy of the model's attention maps reliably reflects task difficulty: low entropy indicates confident, localized grounding, while high entropy suggests uncertainty and potential benefit from CoT. DA-CoT uses this entropy signal to determine whether to apply CoT prompting. Additionally, we introduce a Bidirectional Rethinking mechanism that enables the model to automatically flip its reasoning decision when the initial output fails, enhancing robustness by recovering from failures induced by overthinking and underthinking. DA-CoT demonstrates its effectiveness by achieving state-of-the-art performance on the Reasoning Segmentation benchmarks while significantly improving inference efficiency.

## 29. What Should LLMs Forget: Reinforcement Unlearning of Knowledge Associations

- Authors: Wutong Xu, Yun Qu, Haiyan Feng, Qi Wang, Xiangyang Ji
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-30
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 2.8988598185378853
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.41616v1
- PDF: https://arxiv.org/pdf/2610.41616v1
- Local PDF: pdf/2026-11-03_29_What Should LLMs Forget_ Reinforcement Unlearning of Knowledge Associations.pdf

Large language models (LLMs) acquire extensive factual knowledge during pre-training, which may include sensitive, private, or copyrighted information, motivating the development of unlearning methods that selectively remove specific knowledge while preserving general capabilities. However, existing approaches typically optimize entire responses without explicitly identifying the knowledge to be forgotten, resulting in coarse and uncontrolled forgetting. To address this, we revisit the forgetting target of LLM unlearning and introduce Knowledge Association (KA), which characterizes the association between a query context and its target knowledge and is instantiated by the corresponding conditional predictive distribution, as the fundamental target of forgetting. Based on KA, we propose Knowledge Association Reinforcement Unlearning (KARU), a unified reinforcement learning framework that suppresses forgotten knowledge associations while preserving retained ones. Specifically, KARU derives complementary mechanisms from the KA-based formulation: token-level reward construction for finer-grained forgetting supervision, distribution-level regularization for precise knowledge suppression, and proximity-aware retain sampling to mitigate collateral degradation. Experiments across diverse LLMs on representative benchmarks demonstrate that KARU consistently improves forgetting effectiveness over existing baselines while maintaining comparable retention performance and general utility.

## 30. LLM Detoxification via Transition-Aware Reward-Guided Representation Sampling

- Authors: Aishan Liu, Yisong Xiao, Xianglong Liu, Yongxin Huang, Siyuan Liang, Zonghao Ying, Yang Qu, Jian Yang, Yaodong Yang, Dacheng Tao
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-30
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 2.8950623808170346
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.41165v1
- PDF: https://arxiv.org/pdf/2610.41165v1
- Local PDF: pdf/2026-11-03_30_LLM Detoxification via Transition-Aware Reward-Guided Representation Sampling.pdf

Large Language Models (LLMs) can generate toxic content, motivating effective test-time detoxification. Existing representation steering methods often rely on static or coarse interventions and provide imprecise guidance because they inadequately model transitions between toxic and non-toxic generations. We propose Transition-Aware Reward-Guided Representation Sampling (TARGRS), a test-time framework that learns reward guidance over toxicity transitions in latent representation space. During exploration, progressive steering along the toxicity direction constructs trajectories from non-toxic to toxic states. Toxicity scores along these trajectories turn sparse annotations into dense, listwise supervision for a transition-aware token-level reward model. During inference, TARGRS uses this model to guide coarse-to-fine sampling along the opposite, non-toxic direction: coarse sampling identifies the intervention needed to reach non-toxic regions, and refinement selects a detoxified representation with minimal perturbation. Experiments on 10 LLMs across RealToxicityPrompts, BOLD, and AttaQ show that TARGRS consistently outperforms state-of-the-art baselines, reducing toxicity by up to 69.38% on RealToxicityPrompts. TARGRS runs nearly as fast as the original LLM while preserving its core capabilities with minimal impact. By intervening in the language decoder space, TARGRS also extends to Large Vision-Language Models (LVLMs), reducing toxicity by up to 64.23% across 3 representative LVLMs.
