# Paper Daily Reading - 2026-11-10

## 1. Glyph: An Interpretability Engine for AI-Driven Scientific Discovery in Clinical Data

- Authors: Robbie Holland, Ashwin Kumar, Mateus A. Esmeraldo, David Le, Andrea Fisher, Jiazhen Pan, Louisa Fay, Magdalini Paschali, Vasiliki Sideri-Lampretsa, Ates Fettahoglu, Stefania Moroianu, Philipp Wesp, Ivan Lopez, Tom Nuno Wolf, McKenzie S. White, Eduardo Pontes Reis, Fatima Rodriguez, Curtis P. Langlotz, Vasilis Syrgkanis, Imon Banerjee, Akshay S. Chaudhari, Sergios Gatidis
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-06
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 3.5717922332198953
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.08922v1
- PDF: https://arxiv.org/pdf/2611.08922v1
- Local PDF: pdf/2026-11-10_01_Glyph_ An Interpretability Engine for AI-Driven Scientific Discovery in Clinical Data.pdf

Automated scientific discovery has the potential to advance understanding of disease mechanisms and accelerate identification of early disease markers. Manual data annotation is infeasible at population scale, motivating methods that automatically extract pre-defined phenotypes in multimodal and unstructured clinical data. Such pre-defined feature sets determine and limit which associations these approaches can discover. This limitation extends to agentic AI systems that use these tools to query population-scale data. In contrast, foundation models (FMs) trained on large volumes of clinical data can perform tasks beyond their training objectives. This suggests their latent embeddings may represent novel or unexplored features that could yield insights into disease mechanisms, yet such latent features remain difficult to interpret. To address this challenge, we introduce Glyph, an automated multistage framework that extracts features from multimodal and unstructured clinical data using FMs and sparse autoencoders, interprets them as coded clinical concepts, and evaluates their value for clinical scientific discovery. We applied Glyph to abdominal CT volumes, CT radiology reports and laboratory measurements from 41,628 patients across different institutions. We identified 397 predictive concepts supported by 4,463 Bonferroni-significant associations. Moreover, a majority of discovered associations were automatically reproducible in held-out cohorts across different sites. Glyph concepts provided complementary associations to literature-derived markers, leading to gains in predictive power. We envision that interpretability can extend beyond a mechanistic understanding of neural networks to connecting implicitly learned features with clinical knowledge and establishing their significance for patient outcomes. We release Glyph at https://github.com/StanfordMIMI/Glyph.

## 2. MEDALLION: Manifold Embedding Distillation and Attributions for Low-dimensional Latent InterpretatiON

- Authors: Vicky Jung, Claire M. He, Irene Chang, Genevera I. Allen
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-05
- DOI: Unavailable
- Categories: cs.LG, stat.ML
- Relevance: 3.441907547684197
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.08767v1
- PDF: https://arxiv.org/pdf/2611.08767v1
- Local PDF: pdf/2026-11-10_02_MEDALLION_ Manifold Embedding Distillation and Attributions for Low-dimensional Latent InterpretatiON.pdf

Dimensionality reduction is widely used to visualize high-dimensional data and guide scientific discovery, yet interpreting which original features contribute to low-dimensional representations remains challenging, particularly for black-box methods such as t-SNE and UMAP. We introduce \textbf{MEDALLION} (Manifold Embedding Distillation and Attributions for Low-dimensional Latent InterpretatiON), a novel framework for interpreting low-dimensional embeddings through knowledge distillation and neural feature attribution. MEDALLION distills any given embedding with a neural encoder which we explain via a broad range of existing neural feature attribution methods. Through experiments on MNIST and applications in single-cell transcriptomics, we show MEDALLION provides informative feature attributions that cast additional insights into the underlying embedding and compare its performance with existing interpretability approaches.

## 3. Not All Latents Are Equal: Importance-Weighted Latent Graph Generation

- Authors: Biraaj Rout, Jay Revolinsky, Han Liu, Harry Shomer
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-05
- DOI: Unavailable
- Categories: cs.LG, cs.AI
- Relevance: 3.4239568727225898
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.08788v1
- PDF: https://arxiv.org/pdf/2611.08788v1
- Local PDF: pdf/2026-11-10_03_Not All Latents Are Equal_ Importance-Weighted Latent Graph Generation.pdf

Graph generation has shown tremendous effectiveness in modeling complex scientific tasks ranging from molecule generation to optimized circuit design. Most recent advancements have developed models that learn to denoise noisy graphs using either discrete diffusion or flow matching. However, discrete graph diffusion scales quadratically with the number of nodes, making it difficult to use such models on larger graphs. On the other hand, latent graph generation instead seeks to denoise noisy graph latents, which scale better to more nodes due to their lower dimension. However, in practice, latent graph generation models lag behind their discrete counterparts in performance. We study this problem, finding that it is caused by the unequal distribution of that different latent dimensions have on graph reconstruction. the impact. We observe that the vast majority of impact is contained in only a smaller number of latent dimensions. Since equal emphasis is placed on reconstructing the entire latent in the loss function, existing models are optimized to reconstruct information irrelevant to the downstream task. To tackle this problem, we propose Latent Importance Reweighting ({\bf LIR)} which weights each latent dimensions via it's importance to final graph reconstruction. Importance is calculated as the relative influence of a single latent unit on graph reconstruction, which is represented via the Jacobian of the decoder relative to the latent. Our method is model-agnostic and requires no additional model parameters or hyperparameters. Experiments show that LIR can boost performance and lead to faster training convergence when applied to two different autoencoders on various benchmark datasets. Code: https://github.com/biraaj/GraphGenLatentReweight

## 4. Generative Latent Priors for Interpreting and Steering Protein Language Models

- Authors: Daniel Hinjos, Lucía Urcelay
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-06
- DOI: Unavailable
- Categories: cs.AI, cs.LG
- Relevance: 3.3577923260366966
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.09818v1
- PDF: https://arxiv.org/pdf/2611.09818v1
- Local PDF: pdf/2026-11-10_04_Generative Latent Priors for Interpreting and Steering Protein Language Models.pdf

Dominant methods for interpreting large models impose strong structural assumptions. Generative Latent Priors (GLP) are a complementary approach: a diffusion model that learns the distribution of a frozen model's activations directly, imposing no assumptions. We port GLP to ESM-2 activations (UniRef50) and evaluate it at two host scales (ESM-2-8M and -650M), both as a lens for protein representations and as a prior for editing them. Generation quality scales smoothly with depth and compute. As a lens, single GLP "meta-neurons" are the strongest probes of discrete Swiss-Prot concepts at both hosts, beating InterPLM's released SAE features, and lead on continuous properties at 8M though not at 650M; falsification tests show this is mostly concentration, not new information. As an editing prior, the on-manifold correction makes DiffMean steering of three biochemical properties effective and restores on-manifoldness, but only in isolation: re-embedding the sequences actually produced after several rounds of decoding, the structural plausibility is compromised. This is mainly reproduced in additional SAE-based clamping structural steering experiments, where only Helix motif succeeds. The naturalness failure is traced to the rewriting coverage and the decoder rather than the prior, highlighting what the method must clear before it can serve for both discovery-by-editing and discovery-by-exploration. Trained GLPs are released on huggingface.co/collections/HPAI-BSC/glprot.

## 5. Improving Contextual Retrieval for Long Documents using Semantic Chunking and Hybrid Retrieval Strategies

- Authors: Sakshi Garg, William B. Andreopoulos
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-19
- DOI: Unavailable
- Categories: cs.IR, cs.CL, cs.LG
- Relevance: 3.309642398038149
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.08498v1
- PDF: https://arxiv.org/pdf/2611.08498v1
- Local PDF: pdf/2026-11-10_05_Improving Contextual Retrieval for Long Documents using Semantic Chunking and Hybrid Retrieval Strategies.pdf

The vast amount of information available in lengthy, distributed documents makes finding relevant answers difficult, especially when the answer requires connecting evidence from multiple sources. Standard Retrieval-Augmented Generation (RAG) systems often struggle with this type of "multi-hop" reasoning and frequently face issues with context fragmentation. In this paper, we propose a hybrid RAG framework that integrates the structured reasoning of knowledge graphs with the broad semantic coverage of dense vector retrieval. Our approach employs a multi-stage pipeline using transformer-based summarization and semantic chunking to improve context retention. We construct a dynamic knowledge graph to capture explicit relationships between entities while simultaneously maintaining a dense vector index. During inference, the system uses a hierarchical mechanism that prioritizes graph traversal for precision and falls back to vector retrieval when necessary. We evaluated our framework on the MultiHop-RAG dataset. The results show that this hybrid approach outperforms standalone vector and graph-based baselines, achieving higher Exact Match scores and improved retrieval accuracy for complex queries. This confirms that merging structured reasoning with standard vector retrieval creates a more robust system for handling complex knowledge-intensive questions.

## 6. Typed-Centrality Grounding for Agentic GraphRAG: A Symbolic Approach for Agentic Reasoning

- Authors: Rosario Napoli, Antonio Celesti, Massimo Villari, Maria Fazio
- Source: arxiv
- Venue type: preprint
- Journal: 2026 IEEE Symposium on Computers and Communications (ISCC), pp. 1-7, 2026
- Publication status: preprint
- Publication date: 2026-11-06
- DOI: 10.1109/ISCC70364.2026.11739974
- Categories: cs.AI
- Relevance: 3.286597587877095
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.09414v1
- PDF: https://arxiv.org/pdf/2611.09414v1
- Local PDF: pdf/2026-11-10_06_Typed-Centrality Grounding for Agentic GraphRAG_ A Symbolic Approach for Agentic Reasoning.pdf

Knowledge Graphs (KGs) and Large Language Models (LLMs) represent two approaches for knowledge representation and reasoning over heterogeneous data. Recent research has explored their integration through Graph Retrieval-Augmented Generation (GraphRAG) systems, which use KGs to provide structured context to LLMs. However, existing GraphRAG approaches treat KGs as homogeneous graphs and rely on textual similarity between the input prompt and the context, rather than using it as a source of deterministic knowledge.
  This work proposes an agent-based GraphRAG system that introduces a symbolic layer to integrate deterministic reasoning alongside text similarities. This approach is based on the definition of typed centralities for KGs, where centrality measures are computed separately for each specific KG's class. This information is used to construct a symbolic representation that is provided to the LLM as a deterministic source. The proposed system was mathematically validated and evaluated on a real-world POLE (Person, Object, Location, Event) dataset, comparing reasoning and information retrieval with and without the symbolic layer. The results indicate that the our approach leads to responses that are more consistent with the context, improving the generated outputs.

## 7. StreamTab: Training-Free Temporal Link Prediction with Tabular Foundation Models

- Authors: Mingqi Yang, Renqi Wu
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-06
- DOI: Unavailable
- Categories: cs.LG, cs.DB, cs.SI
- Relevance: 3.2689778698758722
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.09052v1
- PDF: https://arxiv.org/pdf/2611.09052v1
- Local PDF: pdf/2026-11-10_07_StreamTab_ Training-Free Temporal Link Prediction with Tabular Foundation Models.pdf

Temporal link prediction uses past interactions to predict whether two nodes will interact in the future. Temporal graph neural networks achieve strong results on this task, but they are trained separately for each graph. How a model should use interaction history also depends on the candidates it is compared with. A past interaction can distinguish a recurring link from a random pair that has never interacted, but when the negative candidates have also interacted before, other signals are needed. We propose StreamTab, a training-free framework built on a frozen tabular foundation model pretrained only on synthetic tables. StreamTab describes each candidate pair by statistics of its past interactions and shows the model recent observed interactions and sampled negative pairs as labeled examples, from which the model scores new candidates. Its central design, regime conditioning, samples the negative examples according to how the candidates are sampled, so the examples show the distinction the model must make. As new interactions arrive, StreamTab updates the statistics and refreshes the examples while the model parameters stay fixed. On thirteen datasets against 21 temporal graph baselines, StreamTab achieves the highest average precision on twelve datasets under historical sampling and eleven under inductive sampling, and ranks first or stays within one point of the best on seven datasets under random sampling. With the same features and model, regime conditioning raises average precision over examples with random negatives by a median of 12.6 points under historical sampling.

## 8. Emergent Low-Dimensional Topological Dynamics Dictate Generalization and Escape Mechanics in Billion-Parameter Neural Networks

- Authors: Dongqing Cao
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-09-07
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.2137864443673414
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.08502v1
- PDF: https://arxiv.org/pdf/2611.08502v1
- Local PDF: pdf/2026-11-10_08_Emergent Low-Dimensional Topological Dynamics Dictate Generalization and Escape Mechanics in Billion-Parameter Neural Ne.pdf

The remarkable generalization of modern over-parameterized neural networks defies classical statistical learning bounds. Here we establish that optimization trajectories in billion-parameter models do not sample the ambient dimension $\mathbb{R}^N$ homogeneously; instead, they are dynamically constrained to a low-dimensional execution submanifold $\mathcal{M}_{\text{exec}}$ (with empirically observed effective dimension $d_{\text{eff}} \le 12$). By equipping the parameter space with a regularized Hessian metric $g_{ij} = \nabla_i \nabla_j L + εδ_{ij}$ and analyzing stochastic Langevin diffusion on loss sublevel sets, we derive a rigorous Topological Generalization Bound grounded in projected subspace persistent homology. Furthermore, by linking Morse index transitions to Betti number annihilation ($β_1 \to 0$), we formulate an exact mathematical mechanism for exponential escape from strict saddles under anisotropic noise. We validate our framework across 80+ architectures (ResNets, Vision Transformers, and 7B LLMs). To bridge theoretical topology with computational feasibility, we resolve the curse of dimensionality by computing projected persistent homology proxies via randomized Lanczos iterations restricted strictly within active Hessian subspaces. Building upon this mathematical foundation, we introduce Topological-Adaptive Optimization (Top-SGD and Top-AdamW)---a family of wrapper algorithms that dynamically modulate learning rates using active curvature signatures. Extensive benchmarks demonstrate a 14.1\% reduction in total wall-clock training time on ImageNet with all computational and memory overheads fully accounted for. Code is publicly available at https://github.com/imslab-research/Topological-SGD.

## 9. Causal graph fusion across incomplete cohorts and causal steering of tabular foundation models

- Authors: Yanke Li, Dhiyaa Al Jorf, Ayoube Ighissou, Anke Scheel-Sailer, Robert Riener, Diego Paez-Granados
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-06
- DOI: Unavailable
- Categories: cs.LG, stat.AP
- Relevance: 3.198075005600238
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.09400v1
- PDF: https://arxiv.org/pdf/2611.09400v1
- Local PDF: pdf/2026-11-10_09_Causal graph fusion across incomplete cohorts and causal steering of tabular foundation models.pdf

Clinical data are split across incomplete cohorts with partially overlapping variables. Causal discovery under missing data and multi-source integration have developed separately, and tabular foundation models cannot take a causal graph without retraining. We make two contributions. First, causal graph fusion learns a partial ancestral graph on the shared variables, fuses it into each cohort's graph under temporal background knowledge and lets Markov blankets guide re-imputation, so missing data are handled inside discovery. Second, causal attention steering compiles the learned graph into the attention of a frozen tabular foundation model at inference. Against known ground truth, fusion dominates pooled and per-cohort baselines in every missingness and heterogeneity condition tested (p<0.001), and steering improves discrimination under distribution shift (p<10^{-5}), a gain that a random graph does not produce. In two spinal cord injury cohorts, fusion orients age, albumin and hemoglobin as ancestors of length of stay, a set no single cohort orients in full, and yields compact, temporally ordered predictor sets that match or exceed automatic feature selection on four of five outcomes.

## 10. Federated training performs as well as centralized for 3D Latent Diffusion for Diagnosis-Conditioned Brain MRI Synthesis

- Authors: Abhijith Shaji, Paul Kurian, Greg Ver Steeg, Paul M. Thompson, Jose-Luis Ambite
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-05
- DOI: Unavailable
- Categories: cs.CV, cs.AI
- Relevance: 3.1354820845464433
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.08771v1
- PDF: https://arxiv.org/pdf/2611.08771v1
- Local PDF: pdf/2026-11-10_10_Federated training performs as well as centralized for 3D Latent Diffusion for Diagnosis-Conditioned Brain MRI Synthesis.pdf

Generative models of brain MRI are useful to understand brain conditions, and to enrich scarce and imbalanced neuroimaging data. However, training these models requires large, multi-site training sets, which is challenging. Federated learning (FL) allows for training deep learning models without sharing data. We show that training a 3D conditional latent model federatedly (where data is kept private at each site) performs similarly to centralized training (where all the data have been copied to a single site). We evaluate three metrics: conditional fidelity (how well generated MRIs perform in classification), diversity (how the generated images match the real data distribution, using MultiScale-SSIM), and realism (how close generated images are to real images, using Fréchet Inception Distance). Our results show that federated training is a viable route to develop multi-site generative models of brain MRI.

## 11. Differentially Private GraphRAG: Protecting Relation Connectivity and Semantics

- Authors: Jie Fu, Yuan Hong, Yue Ning, Wendy Hui Wang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-06
- DOI: Unavailable
- Categories: cs.CR, cs.AI
- Relevance: 3.133406219704394
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.09658v1
- PDF: https://arxiv.org/pdf/2611.09658v1
- Local PDF: pdf/2026-11-10_11_Differentially Private GraphRAG_ Protecting Relation Connectivity and Semantics.pdf

Graph Retrieval-Augmented Generation (GraphRAG) connects information across documents through entity relationships to support relational reasoning. However, black-box access to GraphRAG systems can enable adversaries to reconstruct knowledge graphs and recover both structural connectivity between entities and the semantics of their relationships. Existing defenses lack formal privacy guarantees and provide limited protection against such reconstruction attacks. We propose RelGuard, the first differentially private framework for GraphRAG, which provides formal privacy guarantees by mitigating connectivity leakage and protecting relations and their semantic meaning through relation removal. We formalize relation differential privacy (relation-DP), which bounds the distinguishability of mechanism outputs according to the semantic distance between alternative relations while accounting for relation removal. Building on this definition, we develop a four-step defense mechanism that sanitizes source documents before GraphRAG indexing by perturbing relation predicates or removing their associated connectivity using the exponential mechanism. Experiments across three GraphRAG systems and two targeted reconstruction attacks demonstrate that RelGuard provides stronger protection against reconstruction attacks than four existing defense mechanisms while better preserving downstream utility.

## 12. CID: Measuring Cognitive Work Through Semantic State Change

- Authors: Ron Fulbright
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-06
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 3.12205619603261
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.09542v1
- PDF: https://arxiv.org/pdf/2611.09542v1
- Local PDF: pdf/2026-11-10_12_CID_ Measuring Cognitive Work Through Semantic State Change.pdf

Traditional information theory provides powerful tools for analyzing statistical properties of information but offers limited insight into meaning and semantic transformation. It has never been possible to quantify the meaning of an arbitrary piece of information. Large language models represent information as vectors embedded within high-dimensional semantic spaces, enabling meaning to be analyzed geometrically. This paper defines semantic state as the vector representation of information within a model's semantic space and defines cognitive work as the transformation between semantic states, movement through semantic space. To quantify this transformation, we introduce the Contextual Information Differential (CID), a covariance-aware metric based on Mahalanobis distance measuring semantic displacement relative to the structure of the embedding manifold. By treating meaning as a geometric property of semantic space, CID provides a practical method for measuring semantic change, cognitive transformation, and information processing. This framework establishes a foundation for analyzing cognitive processing, learning, reasoning, knowledge generation, synthetic expertise, and human/AI collaboration through implementation-independent measurement of semantic state change in both human and artificial systems.

## 13. BrainCoT: A Multi-Task Zero-Shot Brain Signal Foundation Model with Neurometric-Anchored Chain-of-Thought Reasoning

- Authors: Yiyu Gui, Mingzhi Chen, Guibo Luo, Yuchao Yang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-06
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.120401351667766
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.09082v1
- PDF: https://arxiv.org/pdf/2611.09082v1
- Local PDF: pdf/2026-11-10_13_BrainCoT_ A Multi-Task Zero-Shot Brain Signal Foundation Model with Neurometric-Anchored Chain-of-Thought Reasoning.pdf

Brain signals exhibit substantial multi-center heterogeneity, strong inter-subject variability, and highly diverse task settings, which makes it difficult to build models that generalize beyond a single task. While recent brain signal foundation models leverage large-scale pretraining to learn generalizable representations, they often fall short in practice because they still require target-data-specific supervised adaptation, lack multi-task zero-shot capability, and rarely provide verifiable evidence to support their predictions. In this work, we present BrainCoT, a multi-task zero-shot Brain signal foundation model with neurometric-anchored Chain-of-Thought (CoT) reasoning. BrainCoT unifies heterogeneous tasks into an instruction-driven framework so that, after pretraining, a single model can be directly applied to multiple tasks in zero-shot settings without additional adaptation. It further introduces neurometric-anchored chain-of-thought grounded in neurometric evidence for verifiable reasoning, and adopts Decision-Consistent Rationale Training to keep process learning aligned with correct predictions. Across extensive evaluations, BrainCoT achieves an average ACC of 67.41% and AUC of 74.33% in zero-shot classification without downstream training data, outperforming the strongest linear-probing baseline trained with 1% labeled downstream data by 3.85% in ACC and 5.97% in AUC.

## 14. Controllable Molecule Generation via Sparse Representation Editing: An Interpretability-Driven Perspective

- Authors: Zhuoran Li, Xu Sun, Chang Wen Chen, Wanyu Lin
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-06
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.0629129645825417
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.09235v1
- PDF: https://arxiv.org/pdf/2611.09235v1
- Local PDF: pdf/2026-11-10_14_Controllable Molecule Generation via Sparse Representation Editing_ An Interpretability-Driven Perspective.pdf

Controllable molecule generation is crucial for diverse scientific applications, such as drug discovery and materials design. While large language models (LLMs) show great promise, their dense and entangled representations impede precise control over the generation of molecules with bespoke substructures or properties. To address this, we propose Sparse Representation Editing (SpaRE), an interpretability-driven framework for fine-grained and precise control in LLM-based molecule generation. The crux of SpaRE is to learn an overcomplete sparse feature space that disentangles LLM representations into a compact set of latent features corresponding to chemically meaningful concepts. Within this space, we can directly manipulate these concept-aligned latent features to achieve (1) local control, by generating target atoms and functional groups at specified positions; and (2) global control, by customizing the overall structural and physicochemical properties within defined ranges. In this way, our framework advances interpretability from post-hoc analysis to actionable generative control. Experiments show that SpaRE can generate chemically desirable molecules under complex constraints in real-world scenarios, while offering mechanistic insights for quantitative structure-property analysis. The code and demo are available at https://github.com/WanyuGroup/ICML2026_SpaRE.

## 15. Learning Generative Dynamics for 3D Molecule Generation via Sequential Neuro-Symbolic Constraints

- Authors: Zhuoran Li, Xu Sun, Chang Wen Chen, Wanyu Lin
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-06
- DOI: Unavailable
- Categories: cs.LG, cs.AI
- Relevance: 3.0483723421052584
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.09142v1
- PDF: https://arxiv.org/pdf/2611.09142v1
- Local PDF: pdf/2026-11-10_15_Learning Generative Dynamics for 3D Molecule Generation via Sequential Neuro-Symbolic Constraints.pdf

Diffusion models have recently emerged as a powerful paradigm for generating 3D molecules. Despite showing remarkable promise, they learn atomic distributions implicitly from data, without explicitly encoding physicochemical rules into their generative dynamics. Consequently, generated samples can be statistically plausible yet chemically invalid. To address this problem, we propose Sequential Neuro-Symbolic Constrained Diffusion (SensDiff), a framework that integrates symbolic rules into generative modeling, enabling the model to internalize scientific priors during training. Central to SensDiff is the observation that the diffusion trajectory of 3D molecule generation exhibits a coarse-to-fine evolution: valid molecules arise by first mitigating macroscopic geometric conflicts and then refining structures toward microscopic chemical consistency through iterative denoising. Accordingly, SensDiff mirrors this dynamic by sequentially enforcing constraints with adaptive weighting during training, progressively steering generation toward valid molecular geometries. Moreover, SensDiff translates domain knowledge into interpretable generative controls, grounding opaque neural denoising in scientific principles. Experiments on molecular benchmarks and real-world constrained generation tasks confirm that SensDiff consistently improves chemical validity while adhering to physicochemical rules and user-specified targets. The code is publicly available at https://github.com/WanyuGroup/NeurIPS2026_SensDiff.

## 16. Cross-Layer TopK: Dynamically Allocating Sparsity Across Layers in Transcoders

- Authors: Anyuan Zhuo, Shaohua Zhang, Tianle Li, Yuan Lin, Diandian Gu, Jun Wang, Pinyan Lu
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-06
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.0480232627508466
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.09233v1
- PDF: https://arxiv.org/pdf/2611.09233v1
- Local PDF: pdf/2026-11-10_16_Cross-Layer TopK_ Dynamically Allocating Sparsity Across Layers in Transcoders.pdf

Cross-Layer Transcoders (CLTs) decompose the activations of large language models into human-interpretable features and trace how these features interact across layers to form circuits, making them a key tool for mechanistic interpretability. However, training CLTs effectively and efficiently is hard. Beyond the usual trade-off between sparsity and reconstruction quality, a CLT has to model all layers at once, which adds a further challenge. The common JumpReLU recipe controls sparsity only indirectly through a penalty, while the direct extension of TopK selects a fixed number of latents in every layer. Yet reconstruction difficulty differs widely across layers, and intermediate layers are much harder than others, so giving every layer the same budget is suboptimal. We propose Cross-Layer TopK, which sets a single L0 budget for the whole model and dynamically allocates it across layers during training. In a comparison with JumpReLU and other TopK variants on Qwen3-8B-Base, this gives lower FVU while using 20% fewer active latents than JumpReLU. The better reconstruction carries over to circuit tracing, yielding more complete circuits with higher replacement and completeness scores. The fixed per-token budget of Cross-Layer TopK also makes it easy to pair with sparse decoding, which cuts both computation and communication and gives a 2.9x speedup per training step. We further show that Cross-Layer TopK follows scaling laws in both latent size and sparsity. We have open-sourced the weights of our CLT at https://huggingface.co/ByteDance-Seed/Cross-Layer-TopK-CLT.

## 17. ChainFlow: Few-Step Latent Flow Matching for Speculative Decoding

- Authors: Selim Aktas, Yusuf Erdem Erdem, Ahmed Zeer, Himmet Toprak Kesgin, Muzaffer Kaan Yuce, Mehmet Fatih Amasyali
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-05
- DOI: Unavailable
- Categories: cs.AI, cs.CL
- Relevance: 3.0444569055053003
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.08669v1
- PDF: https://arxiv.org/pdf/2611.08669v1
- Local PDF: pdf/2026-11-10_17_ChainFlow_ Few-Step Latent Flow Matching for Speculative Decoding.pdf

Speculative decoding has become a standard way to accelerate LLM inference: a lightweight drafter proposes tokens that the target verifies in one parallel pass. Existing drafters face trade-offs that limits their speedups: autoregressive drafters generate tokens one at a time, so drafting cost grows with draft length, while diffusion drafters generate tokens in parallel but predict each position independently, ignoring inter-token dependencies. We introduce ChainFlow, a new speculative decoding paradigm and the first flow-matching drafter conditioned on the target's hidden states. ChainFlow treats drafting as a short transport over hidden states, needing one or two flow steps instead of the many denoising steps of generation from noise. A variational autoencoder compresses these states so drafting cost barely grows with target size, lightweight feedback heads restore inter-token dependencies, and tree drafting raises acceptance. On Qwen3.5 models, at matched drafter size and training data, ChainFlow outperforms EAGLE-3 and DFlash in vLLM by 39% and 11%, respectively. These gains further widen as drafters are adapted to new languages sequentially. Our ablations cover drafter design and concurrent serving, and we open-source our code and drafter models.

## 18. Attend at the Right Resolution: Head-Adaptive Sparse Attention via Query-Key Interaction Structure

- Authors: Wajih Hassan Raza, Ahsan Bilal, Yidan Shen, Renjie Hu, Xin Fu, Yu Wen
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-06
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 3.021502433302281
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.09700v1
- PDF: https://arxiv.org/pdf/2611.09700v1
- Local PDF: pdf/2026-11-10_18_Attend at the Right Resolution_ Head-Adaptive Sparse Attention via Query-Key Interaction Structure.pdf

Attention is a major scalability bottleneck in large language models (LLMs), with its computational cost and key-value (KV) memory traffic becoming increasingly prohibitive as context length grows. Sparse attention addresses this bottleneck by restricting each query to a subset of the context, but its effectiveness hinges on identifying relevant regions both cheaply and reliably. Existing training-free methods primarily rely on runtime relevance estimates, with selection dimensionality and granularity typically governed by fixed heuristics rather than the intrinsic interaction structure of pretrained attention heads. We take a different perspective: the query-key operator of each pretrained head defines a characteristic response structure that determines the resolution needed for sparse selection, both across feature directions and across context tokens. Building on this insight, we propose Head-Adaptive Sparse Attention (HASA), a training-free sparse attention framework that jointly adapts selection resolution along these two dimensions. Along the feature dimension, the singular spectrum of each head's query-key operator determines an effective rank, yielding a compact, head-specific response space. Along the sequence dimension, neighboring regions are progressively merged according to the directional coherence of their token responses in this same space, while heterogeneous regions remain separate. Exact attention is then computed using the original full-dimensional KV states of the selected regions. HASA captures 88.1% of dense-attention mass and, compared with UNIQUE, a strong recent sparse-attention baseline, improves accuracy by up to 3.47 and 2.57 points on RULER and LongBench-Pro, respectively, and accelerates self-attention by up to 1.32x, while achieving up to 14.07x speedup over dense attention.

## 19. Synchronized Optimal Transport Reconstructs Coupled Transcriptomic and Chromatin Dynamics

- Authors: Jingfeng Wang, Yanxiang Zhao, Qing Nie, Zixuan Cang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-06
- DOI: Unavailable
- Categories: q-bio.GN, math.OC
- Relevance: 2.9982662750987608
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.08853v1
- PDF: https://arxiv.org/pdf/2611.08853v1
- Local PDF: pdf/2026-11-10_19_Synchronized Optimal Transport Reconstructs Coupled Transcriptomic and Chromatin Dynamics.pdf

Single-cell RNA and ATAC data collected across developmental stages provide time-course snapshots of transcriptional and regulatory states. Since sequencing is destructive, trajectories between these snapshots must be inferred from independently sampled cell populations. Existing approaches typically infer continuous dynamics in a single modality or integrate RNA and ATAC in a shared representation. Here we present Cross-Omics Aligned Trajectory Inference (COATI), which extends unbalanced synchronized dynamical optimal transport to time-dependent cross-modal maps for reconstructing coupled trajectories in distinct RNA and ATAC state spaces. We evaluated COATI on synthetic benchmarks and four developmental datasets using held-out-stage reconstruction and lineage analyses. COATI improved reconstruction of cell populations at held-out stages, including recovery of chromatin-state heterogeneity within cell types, and better preserved developmental lineage relationships. The unbalanced formulation allows the inference of population mass changes, which were shown to associate with DNA-replication programs at early stages and lineage-maturation programs later in development. The coupled trajectories enabled analysis of lineage-specific transcriptional and chromatin changes and their temporal relationships during development. Lineage responses inferred by COATI agreed with independent CRISPR perturbation results, and the inferred regulatory patterns were consistent with independent epigenetic data.

## 20. Flow-Guided Target-Space Alignment via Path Consistency

- Authors: Ruizhi Yuan, Zeqiu Yu, Wei Gao, Wei Chen, Xiwei Tang, Lu Tang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-06
- DOI: Unavailable
- Categories: cs.AI, cs.CV, cs.LG
- Relevance: 2.9882961710062474
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.09863v1
- PDF: https://arxiv.org/pdf/2611.09863v1
- Local PDF: pdf/2026-11-10_20_Flow-Guided Target-Space Alignment via Path Consistency.pdf

Many multimodal alignment problems require mapping a source modality into a fixed space defined by a target modality, where the target space is not merely an intermediate embedding but is used directly for downstream analysis. In this setting, successful alignment should preserve both the global structure of the target distribution and the instance-level correspondence observed in paired source--target training data. Existing objectives typically address only part of this goal: contrastive losses encourage relative similarity, distribution-matching losses improve marginal agreement, and pointwise regression fits each source sample to its paired target without explicitly modeling target-space path geometry. We propose FlowAlign, a flow-guided target-space alignment method that repurposes conditional flow matching as a training-time alignment signal rather than an inference-time transport model. FlowAlign uses the learned flow field to guide the alignment of source-side representations with the fixed target space, encouraging them to preserve paired correspondence while remaining compatible with the global target-space structure. We further provide theoretical analysis showing how FlowAlign helps improve paired correspondence by controlling endpoint accuracy and capturing local target-space geometry. Experiments on synthetic data, paired single-cell multiome benchmarks, and image--text alignment demonstrate that FlowAlign improves instance level correspondence while preserving target-space structure across different modality settings.

## 21. Zero-Shot Weight-Space Programming Across a Difficulty-Graded Ladder of Two-Player Games

- Authors: Eduardo C. Garrido-Merchán
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-06
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 2.9682873823781595
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.09271v1
- PDF: https://arxiv.org/pdf/2611.09271v1
- Local PDF: pdf/2026-11-10_21_Zero-Shot Weight-Space Programming Across a Difficulty-Graded Ladder of Two-Player Games.pdf

Weight-space programming sets every weight of a feed-forward network by hand, from an explicit specification of the desired computation, with no gradient descent and no training data anywhere in the construction. We ask how far a large language model can carry this practice, zero-shot, across games of deliberately increasing difficulty. We design a four-rung ladder (Nim, tic-tac-toe, two sizes of Connect Four, and a chess endgame) spanning four axes of difficulty, and build a second, independent network at each rung, using a structurally unrelated game at matched difficulty, to separate what a rung's finding says about the difficulty level from what it says about the one game used to measure it. Ten networks are built and independently verified. Six admit a complete, non-statistical proof of correctness against an independent oracle. The chess-endgame rung is exact where correctness is cheap, move legality and, in one network, an exact one-ply mate detector, and collapses where it is expensive, composing a multi-move mating plan, from 84.1-100% success at the one-ply tactics it was built to get right down to 0.57-9.13% in full adversarial play; its replicate shows this collapse is an order of magnitude less severe under a shorter required plan and exact rather than heuristic safety checks. The standard-sized rung confirms, by holding hand-set evaluation weights fixed and adding only shallow search, that the remaining gap is an architectural ceiling rather than a matter of engineering effort, and this exact collapse reproduces across two structurally unrelated games. We release all ten networks, their independent oracles, construction-cost measurements, and a cold-prompt protocol for a future cross-model comparison

## 22. KnowEvo: Knowledge Evolution for Protein Optimization

- Authors: Zijie Xing, Xingyue Liu, Runze Wang, Luoming Hu, Yanming Shen
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-06
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 2.964083029116261
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.09013v1
- PDF: https://arxiv.org/pdf/2611.09013v1
- Local PDF: pdf/2026-11-10_22_KnowEvo_ Knowledge Evolution for Protein Optimization.pdf

Large language models (LLMs) have shown promise in scientific discovery, yet systematically accumulating and refining reusable scientific knowledge remains challenging. Existing approaches primarily improve LLM-based problem solving through parameter optimization or feedback-driven refinement of prompts, programs, and solution trajectories, leaving acquired expertise either embedded in model weights or scattered across iterative problem-solving processes. As a result,knowledge is difficult to systematically inspect, evaluate, and refine. We propose KnowEvo, a framework that treats externalized knowledge itself as the optimization target. Our key insight is that scientific knowledge is inherently modular: multiple interacting mechanisms jointly determine the design outcomes. This makes knowledge evolution fundamentally challenging, as improvements cannot be attributed to individual components in isolation. To address this, KnowEvo represents knowledge as executable expertise blocks and organizes their refinements into strategy mutation trees, enabling structured exploration over a combinatorial knowledge space. The framework combines a Thompson-style forward allocation strategy that adaptively distributes evaluation budgets across strategy variants with a backward revision process, in which a code agent operates in an isolated sandbox to translate rollout evidence into localized program updates. This design enables persistent accumulation, evaluation, and refinement of mechanistic expertise across iterative experimentation. We evaluate KnowEvo on protein optimization tasks including stability and solubility. Results show that knowledge evolution consistently improves over initial strategy blocks and outperforms monolithic program evolution and prior LLM-guided evolution baselines across metrics such as pass@k, MRR, MAP,and NDCG@5. Code is available at https://github.com/recynie/KnowEvo.

## 23. Reconstructing LLM Lineage Trees via Fine-Tuning Path Inference

- Authors: Sota Ogawa, Shojiro Yamabe, Daiki Nishiyama, Jun Sakuma
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-06
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 2.9550808473146697
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.08866v1
- PDF: https://arxiv.org/pdf/2611.08866v1
- Local PDF: pdf/2026-11-10_23_Reconstructing LLM Lineage Trees via Fine-Tuning Path Inference.pdf

Fine-tuned (FT) derivatives of large language models (LLMs) are now released in large numbers, yet their provenance relies on self-reports and cannot be verified. Misattributed lineage leaves a verifier unable to audit outsourced fine-tuning, confirm license compliance of derived models, or trace vulnerabilities that a parent passes to its children. All three require the direction of derivation, not merely its presence. Existing output-only methods are limited to pairwise derivation tests or undirected lineage estimation, while recovering a directed tree requires white-box access to model weights. We formalize the problem of reconstructing a directed model tree, including internal nodes, under gray-box access, where only teacher-forced log-likelihoods are observed and weights are never inspected. Fine-tuning raises the log-likelihood of the training data, and a child inherits this increase from its parent. Building on this property, we define an asymmetric per-task log-likelihood deviation between any two models as a trace of fine-tuning history, and derive from it an edge weight for each ordered pair of models. We propose TRACE-Edge, which exactly solves for the maximum spanning directed tree under these edge weights, with neither hyperparameters nor tree-structure constraints. We evaluate it on five configurations totaling 25 model trees built from three base models and seven tasks. TRACE-Edge achieves a parent-match accuracy of 0.74 when probed with the fine-tuning examples, and on average outperforms an output-similarity baseline even with held-out probes drawn from the same distribution as the training data.

## 24. Rethinking Data Selection as Distribution Matching on Semantic Manifolds

- Authors: Peng Sun, Yi Yang, Mingshuo Chen, Chunxiao Li, Yao Zhu, Huawen Shen, Tianfan Fu
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-05
- DOI: Unavailable
- Categories: cs.LG, cs.CL
- Relevance: 2.9430242823588615
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.08495v1
- PDF: https://arxiv.org/pdf/2611.08495v1
- Local PDF: pdf/2026-11-10_24_Rethinking Data Selection as Distribution Matching on Semantic Manifolds.pdf

Instruction tuning of large language models and large vision language models relies on massive training data, which incurs substantial computational and storage costs. Meanwhile, training data often contains redundancy, noise, and low quality samples. Existing data selection methods mostly rely on diversity, importance, or a combination of both, without explicitly constraining the distributional consistency between the selected subset and the full data in the embedding space. We propose QMAC, a quality aware multiband characteristic function matching method that formulates data selection as a joint optimization problem of distribution matching and quality filtering. QMAC matches the empirical characteristic functions of the selected subset and the full data across multiple frequency scales, capturing both global semantic coverage and local perturbations, while using task related quality scores to filter noisy and low quality samples. We systematically evaluate QMAC on 4 data types, 8 target models, and 44 benchmarks. Experimental results show that QMAC outperforms existing data selection baselines on standard image-text instruction data, substantially surpasses random selection on standard text instruction, image-text reasoning, and text reasoning data, and exceeds full data training in multiple model and budget combinations. The code will be made publicly available upon acceptance of the paper.

## 25. Deep Learning Theory through the Lens of Statistical Physics: A Topical Review

- Authors: Wei Huang, Youjin Deng
- Source: arxiv
- Venue type: preprint
- Journal: Front. Phys. 22(1), 011302 (2027)
- Publication status: preprint
- Publication date: 2026-11-06
- DOI: 10.15302/frontphys.2027.011302
- Categories: cs.LG, cond-mat.stat-mech
- Relevance: 2.923863110306575
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.09138v1
- PDF: https://arxiv.org/pdf/2611.09138v1
- Local PDF: pdf/2026-11-10_25_Deep Learning Theory through the Lens of Statistical Physics_ A Topical Review.pdf

The recent success of foundation models and deep learning has far outpaced our theoretical understanding of how large-scale neural networks learn and generalize. Statistical physics provides a natural language for describing such high-dimensional, nonlinear, and strongly coupled systems, offering concepts such as mean-field theory, phase transitions, energy landscapes, and stochastic dynamics. In this topical review, we adopt a statistical-physics way of thinking -- from concepts including phases and criticality, and free-energy viewpoints, to methods such as kernel and Gaussian-process limits, mean-field and dynamical mean-field theories, random-matrix tools, and Fokker-Planck formalisms, and to a mindset emphasizing universality, scaling, and tractable limits with explicit validity regimes. We survey recent progress on understanding modern deep learning through this lens, including mean-field analyses of wide networks, spectral and geometric perspectives on loss landscapes, stochastic-gradient-based training viewed as a dynamical process, and phase-transition analogies that organize phenomena such as overparameterization, generalization, and representation change. Our goal is to synthesize these threads into a coherent framework that clarifies what each approximation explains, when it is expected to hold, and how apparently competing narratives relate or diverge. Together, these perspectives form a unified physical framework that views representation learning as a collective phenomenon in high-dimensional systems, bridging deterministic and stochastic regimes of gradient-based optimization.

## 26. SPSC: Zero-Shot Cross-Subject EEG-to-Image Reconstruction via Semantic Preservation and Subspace Calibration

- Authors: Yutang Lu, Shuai Jiang, Fei Su, Zhicheng Zhao
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-06
- DOI: Unavailable
- Categories: cs.CV, cs.AI
- Relevance: 2.911920781643191
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.09380v1
- PDF: https://arxiv.org/pdf/2611.09380v1
- Local PDF: pdf/2026-11-10_26_SPSC_ Zero-Shot Cross-Subject EEG-to-Image Reconstruction via Semantic Preservation and Subspace Calibration.pdf

Pretrained vision-language models and diffusion generators have driven rapid progress in brain-to-image generation, while EEG-based reconstruction is still constrained by low signal-to-noise ratio and cross-subject semantic shifts. Zero-shot cross-subject reconstruction poses even greater challenges: EEG semantic embeddings learned from source subjects deviate from the manifold of image embeddings of the unseen target subject, particularly when neither target labels nor target image embeddings are available. To address this issue, we introduce the Semantic Preservation and Subspace Calibration (SPSC) framework, which first uses Object Mask Contrastive Regularization (OMCR) with object identity for backend training, and then constructs Subspace Candidate Gate (SCG) to achieve label-free semantic correction for target subjects during inference. Specifically, OMCR regularizes the conditioning space with object-level positive samples to preserve object-level feature neighborhoods within the reconstruction prior and low-level branch, while SCG exploits training image prototypes and batch statistics of unlabeled target EEG to select candidates for each task within subspaces of image prototypes. Under the leave-one-subject-out (LOSO) setting across ten subjects on the THINGS-EEG dataset, SPSC improves the cross-subject reconstruction from 0.552 to 0.713 on CLIP and from 0.612 to 0.745 on Alex.5. These significant gains indicate that the semantically calibrated conditions can better support generation for the target subjects under label-free inference.

## 27. ROSE: Risk-Aware Orthogonal Subspace Navigation for Lifelong Knowledge Editing in Multimodal Large Language Models

- Authors: Lingyun Song, Ziyao Chen, Kang Pan, Xiaolin Han, Yifei Zhang, Xiaoqi Wang, Yudai Pan, Xuequn Shang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-06
- DOI: Unavailable
- Categories: cs.CL, cs.AI, cs.CV
- Relevance: 2.9069242731230482
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.09770v1
- PDF: https://arxiv.org/pdf/2611.09770v1
- Local PDF: pdf/2026-11-10_27_ROSE_ Risk-Aware Orthogonal Subspace Navigation for Lifelong Knowledge Editing in Multimodal Large Language Models.pdf

Multimodal Large Language Models (MLLMs) require continuous factual updates to stay current, yet lifelong knowledge editing remains a daunting challenge. The primary obstacle is the severe Locality Erosion and Catastrophic Forgetting, where sequential edits inevitably interfere with pre-trained capabilities and prior updates. In this paper, we propose \textbf{ROSE}, a \textbf{R}isk-aware \textbf{O}rthogonal \textbf{S}ubspace navigation framework for lifelong knowledge \textbf{E}diting. ROSE addresses forgetting by aiming to restrict parameter updates to the orthogonal complement of previously edited subspaces. Crucially, it introduces a risk-guided mechanism that utilizes a dynamically computed risk mask to safeguard specific factual parameter subspaces essential for model stability. During inference, ROSE employs a multi-granularity knowledge integration strategy, featuring prototype-anchored semantic gating and perturbation-driven subspace fusion to precisely activate edited knowledge for relevant queries while limiting interference on unrelated inputs. Comprehensive experiments on two prominent multimodal benchmarks show that ROSE is competitive with state-of-the-art approaches across five key metrics, while maintaining outstanding stability over $1,000$ sequential updates. Our code is available at https://github.com/sunlitsong/ROSE.

## 28. FinEvolveKG: Controlled and Attributable Prompt Evolution for Financial Knowledge Graph Construction

- Authors: Abhinav Arun, Jayita Bhattacharyya, Fabrizio Dimino, Bhaskarjit Sarmah, Stefano Pasquali
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-05
- DOI: Unavailable
- Categories: cs.CL, cs.AI
- Relevance: 2.903973741943729
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.08643v1
- PDF: https://arxiv.org/pdf/2611.08643v1
- Local PDF: pdf/2026-11-10_28_FinEvolveKG_ Controlled and Attributable Prompt Evolution for Financial Knowledge Graph Construction.pdf

Financial institutions construct knowledge graphs (KGs) from shared SEC 10-Ks to serve risk analysis, portfolio management, and investment research, whose analytical needs differ. Extraction must adapt without fragmenting shared grounding, typing, and temporal rules. Hand-authored persona prompts and fine-tuning add cost. Weight-free prompt optimization offers an alternative, but unconstrained evolution of a monolithic prompt can rewrite shared rules alongside persona guidance, obscuring changes and complicating review. We introduce FinEvolveKG, a KG-construction harness separating reusable general and persona-policy blocks and mechanically confining GEPA, a reflective prompt optimizer, to the designated block. During persona adaptation, the approved general block remains byte-stable and every optimizer edit is localized to a separately versioned persona policy. A dual objective balances generic temporal-KG quality with persona-relevant facts, motifs, and multi-hop connectivity. We evaluate five mutation scopes on ticker-disjoint 10-K splits, with three seeds for the persona-conditioned arms (v3-v5) across three personas. On the three-seed mean, the complete two-stage block-constrained workflow (v4) improves over the frozen prompt baseline (v1) by 19.4-30.9% and over the tested unconstrained full-prompt workflow (v5) by 2.2-6.4%, leading v5 on both objective components and winning all nine paired-seed comparisons with the lowest seed variance in every persona. Without further optimization, v4 also exceeds v5 across all evaluated out-of-distribution (OOD) shifts. An SME audit supports using the generated triplets as ground truth; a blinded two-SME audit favors v4 over v5 in 70.1% of contrast-enriched judgments. These results show that mechanically attributable evolution can coexist with strong empirical performance, without attributing the gains causally to the boundary.

## 29. Definitions, Label Names, or Demonstrations? Auditing What Governs LLM Annotation

- Authors: Viraj Mishra, Shubham Gupta, Dhruv Gupta, Yuehong Cassandra Tai, Qunhua Li
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-11-06
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 2.8742574340334897
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.09457v1
- PDF: https://arxiv.org/pdf/2611.09457v1
- Local PDF: pdf/2026-11-10_29_Definitions, Label Names, or Demonstrations_ Auditing What Governs LLM Annotation.pdf

Large language models (LLMs) are increasingly used to annotate social-science texts, but high accuracy does not establish that they apply researcher-supplied category definitions: predictions may instead reflect prior associations with category labels or labeled demonstrations. We introduce a counterfactual audit that reassigns definitions among output labels, distinguishing adherence to supplied definitions from preservation of a dataset's original mapping. Across three political-text datasets, models rarely follow reassigned definitions, and standard fine-tuning strengthens the original mapping without reliably increasing definition adherence. We then study retrieval-augmented annotation. Retrieving the nearest training examples generally outperforms retrieving examples separately within each category despite using fewer demonstrations. On the two tasks with substantial gains, direct \(k\)-nearest-neighbor classification recovers 74--93\% of the improvement, indicating that neighborhood labels provide much of the predictive signal. Relabeling fixed demonstrations redirects predictions, whereas aligning demonstrations with reassigned definitions substantially increases adherence to the new mapping. Thus, accuracy-improving interventions need not increase codebook adherence; definitions, category labels, demonstrations, retrieval, and training data should be aligned and validated jointly.

## 30. Know What You Need: Efficient Activation Checkpointing

- Authors: Danyal Ahmed, Edouard Oyallon
- Source: arxiv
- Venue type: preprint
- Journal: The Fortieth Annual Conference on Neural Information Processing Systems, 2026, Paris, France
- Publication status: preprint
- Publication date: 2026-11-06
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 2.8735706098359093
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2611.09614v1
- PDF: https://arxiv.org/pdf/2611.09614v1
- Local PDF: pdf/2026-11-10_30_Know What You Need_ Efficient Activation Checkpointing.pdf

Large Language Model training is increasingly constrained by memory capacity. Activation Checkpointing reduces activation memory by avoiding storing selected activations during the forward pass and rematerializing them during backpropagation, thereby trading memory savings for additional computation. Although this technique is essential for scaling model training, rematerialization can be prohibitively expensive, particularly for Transformer linear layers. Approximate computation could reduce this overhead, but conventional approaches either introduce errors that accumulate over the backward pass or fail to exploit information available from the initial forward pass. We introduce a novel approximate rematerialization method that can yield unbiased gradient estimates: using information collected during the initial forward pass, the method selectively recomputes only the most important layer components, either through greedy selection or randomized sketching. Ablation studies show that the resulting gradients closely match the exact gradients. When applied to feed-forward layers, attention layers, or both, our method can recompute only two-thirds of the layer components in a Llama-488M model, while increasing perplexity by just 1.7%, 1.2%, and 2.5%, respectively.
