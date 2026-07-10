# Paper Daily Reading - 2026-07-10

## 1. Diffusion enabled Optimal Transport distances for graph matching

- Authors: Iman Seyedi, Francesco Archetti
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-07
- DOI: Unavailable
- Categories: cs.LG, cs.AI
- Relevance: 3.607700554693045
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.06646v1
- PDF: https://arxiv.org/pdf/2607.06646v1
- Local PDF: pdf/2026-07-10_01_Diffusion enabled Optimal Transport distances for graph matching.pdf

This paper introduces Diffusion Semi-Relaxed Fused Gromov-Wasserstein (DsrFGW), a novel method for graph comparison that unifies node features and structural connectivity through optimal transport. While traditional Gromov-Wasserstein and semi-relaxed variants (srGW, srFGW) capture graph structure, they often struggle with sparse, noisy, or partially observed graphs. Inspired by Graph Diffusion Distance, which posits graphs are similar if they enable similar information transmission patterns, DsrFGW incorporates diffusion processes allowing information propagation across nodes, capturing local and global structural patterns while reducing sensitivity to noise or missing edges. An extensive evaluation on 36 synthetic pairwise graph matching tasks (easy, medium, hard) demonstrates consistent superiority over srFGW, achieving accuracy improvements of 0-20 percentage points and dramatic Adjusted Rand Index (ARI) gains: in medium-difficulty scenarios, srFGW often achieves negative ARI (worse than random) while DsrFGW offers better performance in terms of both internal and external clustering quality measures (i.e., Adjusted Rank Index and Accuracy with respect to the true underlying clusters, respectively). Even under severe noise, DsrFGW improves clustering quality in 92% of the synthetic tasks with optimal diffusion scales adapting to problem difficulty, establishing DsrFGW as a robust framework for graph comparison under structural uncertainty.

## 2. Generative Diffusion Models of Stochastic Graph Signals

- Authors: Yiğit Berkay Uslu, Samar Hadou, Sergio Rozada, Shirin Saeedi Bidokhti, Alejandro Ribeiro
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-07
- DOI: Unavailable
- Categories: cs.LG, eess.SP
- Relevance: 3.5884912042344097
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.06833v1
- PDF: https://arxiv.org/pdf/2607.06833v1
- Local PDF: pdf/2026-07-10_02_Generative Diffusion Models of Stochastic Graph Signals.pdf

Sampling stochastic signals supported on a graph underlies many graph machine learning tasks, including recommender systems, forecasting in financial markets, and wireless network optimization. In these settings, the target signals are realizations of unknown conditional distributions. However, prevailing approaches rely mostly on intricate, application-tailored designs that often regress to a conditional mean instead of sampling from the conditional law. This paper unifies such problems as conditional graph signal generative modeling and tackles them with a single denoising diffusion framework. We learn a reverse diffusion process, parametrized by graph neural networks (GNNs), that draws graph signals conditioned directly on the graph topology and on node-feature side information. The reverse process is realized by a novel architecture, the U-Graph Neural Network (U-GNN), which generalizes the image-convolutional U-Net to graph-structured signals. The U-GNN performs multi-resolution encoder--decoder processing in which pooling and unpooling reduce to a learned node selection, expressed by nested selection matrices, and a zero-padded lifting of coarse signals back to the full node set. The graph convolutions are carried out on the original graph, with a stride that sets their hop reach, so the U-GNN bypasses explicit graph coarsening at every resolution. We demonstrate our method on two generative tasks: stock price forecasting and optimal wireless resource allocation, with extensive numerical results in both domains.

## 3. Latent graph encoding of multimodal neuroimaging features with generative AI architectures

- Authors: Ishaan Batta, Meenu Ajith, Vince Calhoun
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-08
- DOI: Unavailable
- Categories: cs.LG, cs.AI, cs.CV
- Relevance: 3.442914074541309
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.07027v1
- PDF: https://arxiv.org/pdf/2607.07027v1
- Local PDF: pdf/2026-07-10_03_Latent graph encoding of multimodal neuroimaging features with generative AI architectures.pdf

While generative models enable encoding of complex neuroimaging data for feature generation and reconstruction, developing optimal architectural frameworks with appropriate encoding and latent space processes is crucial for studying structural and functional properties of the brain. We design a multimodal generative framework for structural and functional magnetic resonance imaging (MRI) features through systematic evaluation of encoding strategies, latent multimodal fusion, and generative model selection. Using structural gray matter volume (GMV) and static functional network connectivity (sFNC) features from a large neuroimaging dataset, we analyze generative frameworks involving variational autoencoders (VAEs), transformers, generative adversarial networks (GANs), and diffusion models. Architectures that employ modality-aware graph encoding of functional connectivity into a lower-dimensional latent space outperform vectorized encoders or direct data space approaches. The proposed multimodal graph VAE (gMMVAE) surpasses alternative generative variants across multiple metrics for generation fidelity, reconstruction quality, efficiency, and latent space discriminability, highlighting its potential for robust multimodal neuroimaging analysis.

## 4. SpaR3D-MoE: Adaptive 3D Spatial Reasoning from Sparse Views Meets Geometry-Inductive Mixture-of-Experts

- Authors: Haida Feng, Hao Wei, Haolin Wang, Shiwei Li, Chade Li, Yihong Wu
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-07
- DOI: Unavailable
- Categories: cs.CV, cs.AI
- Relevance: 3.430974327869299
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.06620v1
- PDF: https://arxiv.org/pdf/2607.06620v1
- Local PDF: pdf/2026-07-10_04_SpaR3D-MoE_ Adaptive 3D Spatial Reasoning from Sparse Views Meets Geometry-Inductive Mixture-of-Experts.pdf

Recent Multimodal Large Language Models (MLLMs) struggle to bridge the representational gap between 2D semantic understanding and 3D spatial geometry. Existing 3D-aware models either rely on costly 3D-specific data or utilize RGB-only inputs with heuristic sampling and monolithic, shallow fusion, which respectively disrupt essential spatiotemporal connectivity and induce modality contention across diverse spatial tasks. To overcome these bottlenecks, we introduce SpaR3D-MoE, an end-to-end framework that enables adaptive spatial reasoning by equipping MLLMs with geometry-aware capabilities from only sparse RGB inputs. First, we propose an adaptive spatiotemporal manifold sampling mechanism that constructs a geometry-aware spatiotemporal graph to extract informative keyframes, effectively mitigating sequence redundancy while preserving the scene's topological connectivity. Second, we introduce the heterogeneous geometry-inductive Mixture-of-Experts driven by an instruction-pose aware router, which adaptively routes multimodal tokens to specialized experts, resolving the cross-modal contention inherent in monolithic fusion. Extensive experiments on VSI-Bench, ScanQA, and SQA3D demonstrate that our method achieves state-of-the-art performance. Notably, SpaR3D-MoE achieves the highest average score of 63.5 on VSI-Bench, outperforming the strongest baseline by 7.8 absolute points, alongside relative improvements of 35.4% and 51.4% in Route Plan and Relative Direction tasks, respectively.

## 5. Gen4U: Unifying Video Generation and Understanding via Diffusion

- Authors: Michael King, Aravindh Mahendran, Matthew Koichi Grimes, Fedor Kitashov, Adham Elarabawy, Pedro Velez, Maks Ovsjanikov, Viorica Pătrăucean
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-07
- DOI: Unavailable
- Categories: cs.CV, cs.LG
- Relevance: 3.377511287813223
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.06856v1
- PDF: https://arxiv.org/pdf/2607.06856v1
- Local PDF: pdf/2026-07-10_05_Gen4U_ Unifying Video Generation and Understanding via Diffusion.pdf

Prior work suggests that diffusion representations capture low-level geometry but struggle with high-level semantics. We demonstrate that state-of-the-art video diffusion models overcome this limitation. By systematically probing their intermediate activations using recent mutual-kNN alignment metrics, we reveal a highly structured latent space where visual representations evolve across both network depth and noise levels. We show that while moderate noise levels yield linearly separable global semantics, fine-grained details persist at lower noise levels but become spatially scattered, requiring attention mechanisms to decode. Building on these insights, we introduce Gen4U (Generation for Understanding), a framework that repurposes these generative representations with a single forward pass. Our experiments establish that frozen, large-scale video diffusion models function as highly competitive video encoders across a wide spectrum of tasks, spanning semantic and non-semantic objectives (video classification, depth estimation, camera pose estimation, image and video captioning). Bypassing fine-tuning, Gen4U unifies the generation and understanding paradigms, achieving strong perception performance while fully preserving the model's ability to generate high-quality video.

## 6. Gene expression profiling enables refined parcellation of cortical layers in the heterogeneous human cerebral cortex

- Authors: Yanrong Wei, Youzhe He, Yuyang Liu, Langjian Zhu, Tiannan Feng, Zhiming Shen, Wu Wei, Longqi Liu, Lei Han, Lifang Wang
- Source: openalex
- Venue type: journal
- Journal: Genome Medicine
- Publication status: published
- Publication date: 2026-07-08
- DOI: https://doi.org/10.1186/s13073-026-01704-z
- Categories: Single-cell and spatial transcriptomics, Neurogenesis and neuroplasticity mechanisms, Functional Brain Connectivity Studies
- Relevance: 3.366467160733454
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://doi.org/10.1186/s13073-026-01704-z
- PDF: Unavailable
- Local PDF: Not downloaded

Abstract Background Precise delineation of cortical layers is fundamental for understanding human brain organization, cell-type architecture, and disease-related tissue alterations. However, traditional anatomy-based methods often lack molecular resolution and suffer from inter-observer subjectivity. Methods Here, we present gene expression-defined cortical layers (GD-Ls) using the BayesSpace algorithm, a high-resolution framework for cortical parcellation based on spatial transcriptomics. Results Compared with traditional anatomy-based approaches, GD-Ls more accurately resolve laminar boundaries and capture fine-scale laminar heterogeneity, including sublayer-like domains within L1, L3, and L6, as well as a molecularly distinct transition zone at the gray-white matter interface. Validation across diverse cortical lobes, multiple spatial platforms, and independent healthy postmortem datasets demonstrates that GD-Ls capture the intrinsic molecular architecture of the cortex irrespective of tissue source. Furthermore, cross-species analyses show that this framework is extensible to macaque and mouse cortices. Crucially, GD-Ls successfully identify subtle laminar disorganization and aberrant cellular and molecular signatures in pathologically altered tissues, which are often missed by conventional histology. Conclusions Together, GD-Ls provide an objective and reproducible tool for standardized cortical mapping and for identifying early pathological signatures in the human brain. The source code is available on GitHub ( https://github.com/YanrongWei/GD-Ls ).

## 7. SpaCellAgent: A Self-Evolving LLM-Based Multi-Agent Framework for Trajectory Analysis

- Authors: Songhan Wang, Haoang Chi, He Li, Zhiheng Zhang, Jiayan Yuan, Cheems Wang, Hao Peng, Xinwang Liu, Wenjing Yang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-08
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 3.3454968160356726
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.07467v1
- PDF: https://arxiv.org/pdf/2607.07467v1
- Local PDF: pdf/2026-07-10_07_SpaCellAgent_ A Self-Evolving LLM-Based Multi-Agent Framework for Trajectory Analysis.pdf

Spatial and Single-cell transcriptomics are transformative in deciphering cellular dynamics. As the fundamental paradigm for reconstructing cell developmental paths, trajectory inference (TI) is critical. However, existing methods require extensive manual intervention and proficiency in heterogeneous tools, posing a significant barrier to efficient TI analysis. To bridge this gap, we propose SpaCellAgent, an autonomous large language model (LLM) multi-agent framework that automates end-to-end spatiotemporal analysis and narrative generation. SpaCellAgent utilizes a multi-agent architecture for strategic workflow planning, a dynamic tool-orchestration engine for adaptive algorithm selection, and a self-evolution module that iteratively refines performance through feedback. We evaluate SpaCellAgent on six heterogeneous datasets encompassing complex temporal developmental trajectories, diverse sequencing platforms, and spatially-resolved tissue architectures. SpaCellAgent consistently demonstrates over 40\% improvement in analytical efficiency while maintaining expert-aligned performance. By converting natural language specifications into optimized analytical workflows and fully automating the pipeline, SpaCellAgent democratizes advanced spatiotemporal modeling and establishes a scalable, agent-driven paradigm for computational biology. The code and materials are available at https://github.com/LittleXH-shw/SpaCellAgent.

## 8. Permutation Equivariant Framelet-based Hypergraph Neural Networks

- Authors: Ming Li, Yi Wang, Chengling Gao, Lu Bai, Yujie Fang, Xiaosheng Zhuang, Pietro Lio
- Source: openalex
- Venue type: conference
- Journal: Proceedings of the AAAI Conference on Artificial Intelligence
- Publication status: formally_published
- Publication date: 2026-03-14
- DOI: https://doi.org/10.1609/aaai.v40i27.39474
- Categories: Advanced Graph Neural Networks, Graph Theory and Algorithms, Complex Network Analysis Techniques
- Relevance: 3.3401176593076465
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://doi.org/10.1609/aaai.v40i27.39474
- PDF: Unavailable
- Local PDF: Not downloaded

Hypergraphs provide a natural and expressive framework for modeling high-order relationships, enabling the representation of group-wise interactions beyond pairwise connections. While hypergraph neural networks (HNNs) have shown promise for learning on such structures, existing models often rely on shallow message passing and lack the ability to extract multiscale patterns. Framelet-based techniques offer a principled solution by decomposing signals into multiple frequency bands. However, most prior framelet systems, particularly Haar-type ones, are sensitive to node ordering and fail to ensure consistent representations under permutation, leading to instability in hypergraph learning. To address this, we propose Permutation Equivariant Framelet-based Hypergraph Neural Networks (PEF-HNN), a novel framework that integrates multiscale framelet analysis with permutation-consistent learning. We construct a new family of permutation equivariant Haar-type framelets specifically designed for hypergraphs, supported by theoretical analysis of their stability and decomposition properties. Built upon these framelets, PEF-HNN incorporates both low-pass and high-pass components across multiple scales into a unified neural architecture. Extensive experiments on nine benchmark datasets, including three homophilic and four heterophilic hypergraphs, as well as two real-world datasets for visual object classification, demonstrate the effectiveness of our approach, consistently outperforming existing HNN baselines and highlighting the advantages of permutation equivariant framelet design in hypergraph representation learning.

## 9. DiPhon: Diffusion on Graphons for Scalable Graph Generation

- Authors: Sergio Rozada, Yiming Qin, Manuel Madeira, Pascal Frossard, Alejandro Ribeiro
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-08
- DOI: Unavailable
- Categories: stat.ML, cs.AI, cs.LG
- Relevance: 3.2850756739545677
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.07232v1
- PDF: https://arxiv.org/pdf/2607.07232v1
- Local PDF: pdf/2026-07-10_09_DiPhon_ Diffusion on Graphons for Scalable Graph Generation.pdf

Diffusion models represent a leading paradigm for graph generation, with notable impact in domains such as molecular design. Yet, scaling these models to large graphs remains an open problem. We approach this question in the dense-graph setting through the lens of graphons, the size-agnostic limit objects of dense graph sequences, to study how structural graph statistics behave across node-size scales. This perspective leads to DiPhon, a diffusion framework for size-scalable graph generation. Specifically, we formulate a continuous diffusion process on the graphon space via a Jacobi stochastic differential equation (SDE), and propose DiPhon, a discretized graph-level process that mimics these dynamics on finite graphs. We further derive the corresponding reverse-time process, which requires access to the marginal score. For the Jacobi process, this score interestingly admits a tractable form, which we estimate from data via graph denoising and plug into the reverse process to generate graph samples. We prove that DiPhon matches exactly the first moment of the marginal distributions induced by the continuous graphon process, and approximates the second moment up to a closed-form discrepancy. Thus, DiPhon inherits key size-agnostic statistical properties of the graphon dynamics, providing a principled route toward scalable graph generation. Empirically, we demonstrate this scalability by training on small graphs and generating progressively larger graphs at inference time, without retraining, while preserving their core topological properties.

## 10. Stability of Flow Models for Graph Signals

- Authors: Martin Schmidt, Gonzalo Mateos
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-08
- DOI: Unavailable
- Categories: eess.SP, cs.AI, cs.LG
- Relevance: 3.2393373985798393
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.07510v1
- PDF: https://arxiv.org/pdf/2607.07510v1
- Local PDF: pdf/2026-07-10_10_Stability of Flow Models for Graph Signals.pdf

Generating signals on graphs requires permutation-equivariant models that exhibit stability with respect to relative structural perturbations. While favorable stability properties of Graph Neural Networks (GNNs) have been well documented, it is unclear how structural errors propagate through the dynamics of continuous generative flow models that are gaining traction for graph signal generation. In this paper, we analyze continuous normalized flow models parameterized by GNNs and show that permutation equivariance is preserved for both the resulting continuous-time ordinary differential equations and their discrete numerical approximations used as graph signal samplers. Our primary contribution is to derive explicit stability bounds on the generated probability distributions, which quantify how relative graph perturbations affect the final sampled signals. Motivated by these theoretical bounds, we introduce a stability-promoting regularized flow matching strategy that actively penalizes the spatial Lipschitz constant of the vector field during model training. Experiments using synthetic smooth signals on stochastic block model graphs and real-world fMRI signals on brain connectomes demonstrate that this bound-oriented approach yields generative models that are more robust to structural noise, without sacrificing output quality.

## 11. Hypergraph Neural Stochastic Diffusion: An SDE Framework for Uncertainty Estimation

- Authors: Zhiheng Zhou, Mengyao Zhou, Dengyi Zhao, Xingqin Qi, Guiying Yan
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-08
- DOI: Unavailable
- Categories: cs.LG, cs.AI
- Relevance: 3.184267742163758
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.07330v1
- PDF: https://arxiv.org/pdf/2607.07330v1
- Local PDF: pdf/2026-07-10_11_Hypergraph Neural Stochastic Diffusion_ An SDE Framework for Uncertainty Estimation.pdf

Hypergraph neural networks have shown powerful capability in modeling higher-order relations, yet their predictive uncertainty remains underexplored. Unlike pairwise graphs, uncertainty in hypergraphs arises not only from noisy attributes and ambiguous labels, but also from variations in node-hyperedge incidence structures and complex higher-order dependencies. Existing approaches mainly estimate uncertainty from final predictions or rely on computationally expensive ensembles and Bayesian inference, limiting their ability to capture uncertainty evolution during representation learning. In this paper, we propose Hypergraph Neural Stochastic Diffusion(HyperNSD), a stochastic differential equation framework for uncertainty estimation on hypergraphs. HyperNSD models hypergraph representations as stochastic processes evolving over node-hyperedge incidence structures. A learnable drift function captures deterministic higher-order diffusion dynamics, while a learnable stochastic forcing function characterizes structural ambiguity and representation noise. Predictive uncertainty is directly quantified through the variability of stochastic representation trajectories, providing an intrinsic uncertainty measure beyond post-hoc confidence scores. We formulate HyperNSD with neural drift and diffusion networks, enabling joint learning of prediction and uncertainty propagation. Theoretical analyses establish well posedness, perturbation stability,permutation equivariance, and numerical convergence of the proposed stochastic dynamics. Experiments on multiple hypergraph benchmarks demonstrate that HyperNSD achieves reliable uncertainty estimation for out-of-distribution and misclassification detection while preserving competitive prediction accuracy. These results provide a principled stochastic-dynamical framework for trustworthy higher-order representation learning.

## 12. Accurate, Interdisciplinary and Transparent Structure-property Understanding with Deep Native Structural Reasoning

- Authors: Chen Tang, Yizhou Wang, Jianyu Wu, Lintao Wang, Shixiang Tang, Pengze Li, Encheng Su, Jun Yao, Jiabei Xiao, Yuqi Shi, Jielan Li, Hongxia Hao, Zhangyang Gao, Fang Wu, Ben Fei, Xiangyu Yue, Pan Tan, Bozitao Zhong, Jinouwen Zhang, Aoran Wang, Yan Lu, Jiaheng Liu, Xinzhu Ma, Liang Hong, Mingyue Zheng, Phil Torr, Bowen Zhou, Wanli Ouyang, Lei Bai
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-08
- DOI: Unavailable
- Categories: cs.CL, cs.AI, cs.CE, cs.LG
- Relevance: 3.1142756837053067
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.07708v1
- PDF: https://arxiv.org/pdf/2607.07708v1
- Local PDF: pdf/2026-07-10_12_Accurate, Interdisciplinary and Transparent Structure-property Understanding with Deep Native Structural Reasoning.pdf

Structure-property relationships are foundational to biology, chemistry and materials science, where function, reactivity and physical response emerge from spatial, chemical and periodic organization. Mechanistically explaining these relationships requires interpreting structural evidence through scientific principles and physical constraints, from stereochemistry and bonding to symmetry, energetics and periodic order. However, applying artificial intelligence to this process presents a joint challenge of representation and reasoning: models must preserve domain-native structural information while showing how specific evidence supports predictions under these constraints. Here we introduce SciReasoner, a multimodal scientific foundation model for native structural reasoning across proteins, small molecules and inorganic crystals. SciReasoner discretizes coordinates, topologies and periodic connectivities into a unified structure-aware vocabulary, treating structural tokens as addressable evidence units during reasoning. In homology-controlled Gene Ontology prediction, SciReasoner improves Cellular Component annotation for low-homology and orphan-like proteins, increasing $F_{\max}$ from 0.42 to 0.55. In chemistry, it raises single-step retrosynthesis accuracy from 0.63 to 0.72 while generating fragment-level disconnection and precursor-verification traces. In materials science, its representations separate elemental and compound phases and resolve high- and low-band-gap regimes. Across 86 benchmarks, SciReasoner achieves state-of-the-art performance on 67 tasks. Double-blind expert evaluation rates its reasoning traces as preferred or at least comparable to those of a frontier large language model in 98% of cases. By making structure an inspectable substrate for reasoning under scientific constraints, SciReasoner connects accurate prediction with interpretable scientific inference.

## 13. Reliable mechanistic operator recovery with biologically-informed neural networks: principles for architecture and optimisation design

- Authors: Rebecca M. Crossley, Yuan Yin, Sarah L. Waters, Ruth E. Baker
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-08
- DOI: Unavailable
- Categories: q-bio.QM, cs.LG
- Relevance: 3.031977000270971
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.07425v1
- PDF: https://arxiv.org/pdf/2607.07425v1
- Local PDF: pdf/2026-07-10_13_Reliable mechanistic operator recovery with biologically-informed neural networks_ principles for architecture and optim.pdf

Many biological processes are governed by complex dynamical mechanisms that remain incompletely understood despite increasing volumes of experimental data. Biologically-informed neural networks (BINNs) seek to address this challenge by embedding mechanistic differential equations into neural network training, enabling interpretable constitutive operators to be recovered directly from sparse and noisy observations. However, reliable operator recovery depends sensitively on network architecture, optimisation strategy, and data informativeness. Here, we present a systematic empirical study of how these factors influence mechanistic inference using BINNs applied to canonical one-dimensional advection-diffusion-reaction partial differential equation models. Across a suite of benchmark problems, we investigate how network expressivity, learning rate, loss weighting, and batch size influence optimisation behaviour and operator recovery. We show that successful mechanistic inference depends on balancing competing objectives rather than maximising any single aspect of the model or optimisation. Moderately expressive architectures outperform overly complex networks, intermediate learning rates improve optimisation stability, balanced data and PDE losses are essential for accurate operator recovery, and intermediate batch sizes provide the best compromise between computational efficiency and reproducibility. We further identify practical diagnostics for recognising common failure modes, including over-fitting, unstable optimisation, and poor mechanistic recovery when the ground truth is unavailable. Together, these findings provide evidence-based guidelines for deploying BINNs as credible tools for biological model discovery.

## 14. InductWave: Inductive Multi-Hop Logical Query Answering on Knowledge Graphs

- Authors: Mayank Kharbanda, Michael Cochez, Rajiv Ratn Shah, Raghava Mutharaju
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-08
- DOI: Unavailable
- Categories: cs.AI, cs.IR
- Relevance: 3.0268251044528394
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.07422v1
- PDF: https://arxiv.org/pdf/2607.07422v1
- Local PDF: pdf/2026-07-10_14_InductWave_ Inductive Multi-Hop Logical Query Answering on Knowledge Graphs.pdf

Logical Multi-Hop Query Answering over Knowledge Graphs (KGs) can be formulated as querying, with an implicit completeness assumption. Current works mainly focus on Existential First Order Logic (EFO) queries. These EFO queries contain conjunction, disjunction, and negation operators. Most existing works employ transductive reasoning, meaning they are not capable of reasoning over entities unseen during training. In the real world, there is a resource scarcity, and we cannot train a model with all the nodes of a large KG. Hence, we propose InductWave, a wavelet-based inductive embedding method for logical query answering on large KGs. Here, the training graph consists of fewer nodes than the test graph. Our model performs on par with the baseline models while having half the number of message-passing layers. It outperforms all of them in most cases, with 75% of the layers. These fewer resource requirements enable us to evaluate InductWave on massive graphs, such as Wiki-KG. We test our model using extensive experiments across varying train-test graph proportions of the FB15k-(237) dataset, comparing it with the state-of-the-art models. The code and datasets for the model are available at https://github.com/kracr/inductwave/.

## 15. LEMUR 2: Unlocking Neural Network Diversity for AI

- Authors: Tolgay Atinc Uzun, Waleed Khalid, Saif U Din, Sai Revanth Mulukuledu, Akashdeep Singh, Chandini Vysyaraju, Raghuvir Duvvuri, Avi Goyal, Yashkumar Rajeshbhai Lukhi, Muhammad A. Hussain, Krunal Jesani, Usha Shrestha, Yash Mittal, Roman Kochnev, Pritam Kadam, Mohsin Ikram, Harsh R. Moradiya, Alice Arslanian, Dmitry Ignatov, Radu Timofte
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-07
- DOI: Unavailable
- Categories: cs.LG, cs.CV
- Relevance: 3.023593402363422
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.06839v1
- PDF: https://arxiv.org/pdf/2607.06839v1
- Local PDF: pdf/2026-07-10_15_LEMUR 2_ Unlocking Neural Network Diversity for AI.pdf

Existing NAS benchmarks (e.g., NAS-Bench, NATS-Bench) cover only narrow, task-specific regions of the architectural design space and lack cross-domain or deployment-aware evaluation. LEMUR 2 introduces a large-scale, extensible framework unifying generative, evaluative, and deployment pipelines to unlock neural-network diversity. It comprises over 14,000 distinct architectures and more than 750,000 structured training records documenting model performance, hyperparameters, and task outcomes. These models were produced through AST-based code mutation, genetic and reinforcement-learning evolution, generation of fractal architectures, and synthesis guided by a Large Language Model (LLM). This includes deep models generated with the retrieval-augmented system NN-RAG, which derived and used architectural motifs from over 900 PyTorch modules extracted from public repositories. LEMUR 2 further employs NN-VR and NN-Lite pipelines for automated deployment and latency benchmarking on heterogeneous mobile and Unity-based VR platforms, providing real-device performance metadata. It spans multimodal tasks, image captioning, text-to-image synthesis, and language modeling, supporting cross-domain analysis of architectural transferability. By linking diverse architectures, tasks, and deployment data, LEMUR 2 provides the data foundation for LLM fine-tuning and coupling diverse architectural origins with large-scale, cross-platform empirical validation. This dataset defines a new basis for reproducible and data-driven AI design, advancing the emerging paradigm of LLM-driven AutoML and architectural generalization across modalities and hardware.

## 16. LoCA: Spatially-Aware Low-Rank Convolutional Adaptation of Vision Foundation Models

- Authors: Sojung An, Junha Lee, Sujeong You, Nam Ik Cho, Donghyun Kim
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-08
- DOI: Unavailable
- Categories: cs.CV, cs.AI, cs.LG
- Relevance: 3.011265418000084
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.06918v1
- PDF: https://arxiv.org/pdf/2607.06918v1
- Local PDF: pdf/2026-07-10_16_LoCA_ Spatially-Aware Low-Rank Convolutional Adaptation of Vision Foundation Models.pdf

Pre-trained Vision Foundation Models (VFMs) provide strong visual representations for diverse downstream tasks. The key challenge of VFM adaptation stems from the prohibitive costs of full fine-tuning and catastrophic forgetting. To address this, Low-Rank Adaptation (LoRA) has emerged as the prevailing paradigm for Parameter-Efficient Fine-Tuning (PEFT). However, LoRA is typically designed for transformer self-attention layers parameterized by 2D matrices. Since convolutional kernels inherently couple spatial and channel information within a 4D tensor, forcing them into a monolithic 2D matrix disrupts the inherent spatial topology. In this paper, we propose Low-Rank Convolutional Adaptation (LoCA), a convolution-aware PEFT framework that addresses spatial-channel entanglement by decoupling channel and spatial adaptation. LoCA introduces a low-rank channel adaptation for dense cross-channel mixing and refines spatial bases extracted from pre-trained kernels via Singular Value Decomposition (SVD). Experimental results show that LoCA preserves pre-trained spatial priors and achieves competitive or state-of-the-art performance across fine-grained classification, domain-generalized semantic segmentation, and generative benchmarks.

## 17. Tree-of-Thoughts Reasoning for Text-to-Image In-Context Learning

- Authors: Stepanida Alekseeva, Jenifer Kalafatovich, Seong-Whan Lee
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-08
- DOI: Unavailable
- Categories: cs.CV, cs.AI
- Relevance: 2.998619776950898
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.07117v1
- PDF: https://arxiv.org/pdf/2607.07117v1
- Local PDF: pdf/2026-07-10_17_Tree-of-Thoughts Reasoning for Text-to-Image In-Context Learning.pdf

In text-to-image in-context learning (T2I-ICL), a model has to infer a latent compositional pattern from fewshot demonstrations for generating a query image. Recent studies show that state-of-the-art multimodal large language models struggle with this setting, particularly due to limited compositional reasoning and sensitivity to prompt construction. In this work, we propose a Tree-of-Thoughts (ToT) reasoning framework for T2I-ICL that introduces a multi-stage reasoning and selection layer that generates, evaluates, and selects among multiple candidate hypotheses before constructing the final prompt for image synthesis. By exploring alternative reasoning branches and selecting a coherent interpretation, the proposed approach mitigates prompt ambiguity and compositional errors. We implement the proposed approach in a complete ToT-T2IICL inference pipeline and evaluate it on the CoBSAT benchmark. Both qualitative and quantitative results show that structured multi-branch reasoning leads to more consistent and semantically aligned image generation compared to baseline and Chain-of-Thought prompting strategies, without any additional training or fine-tuning.

## 18. SciMDR: Advancing Scientific Multimodal Document Reasoning

- Authors: Ziyu Chen, Yilun Zhao, Chengye Wang, Rilyn R. Han, Manasi Patwardhan, Arman Cohan
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.9607882679513624
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.2070/
- PDF: https://aclanthology.org/2026.acl-long.2070.pdf
- Local PDF: pdf/2026-07-10_18_SciMDR_ Advancing Scientific Multimodal Document Reasoning.pdf

Constructing scientific multimodal document reasoning datasets for foundation model training involves an inherent trade-off among scale, faithfulness, and realism. To address this challenge, we introduce the synthesize-and-reground framework, a two-stage pipeline comprising: (1) Claim-Centric QA Synthesis, which generates faithful, isolated QA pairs and reasoning on focused segments, and (2) Document-Scale Regrounding, which programmatically re-embeds these pairs into full-document tasks to ensure realistic complexity. We present SciMDR, a large-scale training dataset for cross-modal comprehension, comprising 300K QA pairs with explicit reasoning chains across 20K scientific papers. We further construct SciMDR-Eval, an expert-annotated benchmark to evaluate multimodal comprehension within full-length scientific workflows. Experiments demonstrate that models fine-tuned on SciMDR achieve significant improvements across multiple scientific QA benchmarks, particularly in tasks requiring complex document-level reasoning.

## 19. Chart-MRAG: Benchmarking Multimodal Retrieval Augmented Generation on Chart-based Documents

- Authors: Ymyang, Jiang Zhong, Li Jin, Xiao Sun, Jingwang Huang, Gaojinpeng, Qing Liu, Yang Bai, Jingyuan Zhang, Rui Jiang, Qin Lei, Kaiwen Wei
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.957858318790536
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1164/
- PDF: https://aclanthology.org/2026.acl-long.1164.pdf
- Local PDF: pdf/2026-07-10_19_Chart-MRAG_ Benchmarking Multimodal Retrieval Augmented Generation on Chart-based Documents.pdf

Multimodal Retrieval-Augmented Generation (MRAG) enhances reasoning capabilities by integrating external knowledge. However, existing benchmarks primarily focus on simple image-text interactions, overlooking complex visual formats like charts that are prevalent in real-world applications. In this work, we introduce a novel task, Chart-based MRAG , to address this limitation. To generate high-quality evaluation samples, we propose CHARGE ( CHAR t-based document question-answering GE neration), a semi-automatic framework for generating evaluation samples through multi-modal keypoint extraction, knowledge graph construction, and qa pair synthesis.By combining CHARGE with expert validation, we construct Chart-MRAG Bench , a comprehensive benchmark for chart-based MRAG evaluation, featuring 4,738 question-answering pairs across 8 domains from real-world documents.Our experiments reveal three critical limitations in current approaches: (1) unified multimodal embedding retrieval methods struggles in chart-based scenarios, (2) even with ground-truth retrieval, state-of-the-art Multimodal Large Language Models (MLLMs) achieve only 71.15% Correctness and 80.74% Coverage scores, and (3) Widely-used MLLMs demonstrate consistent text-over-visual modality bias. These findings highlight great challenges in processing information-dense visual formats. We will make our code and dataset publicly available.

## 20. Tracing the Light of Thought: A Probabilistic Self- and Cross-Consistency Verification Mechanism Improving Mathematical Reasoning in LLMs

- Authors: Xiaoyang Liu, Dawei Wang, Tian Li, Huizhi Liang, Gary Ushaw, Richard Davison
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.9570132426978857
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1126/
- PDF: https://aclanthology.org/2026.findings-acl.1126.pdf
- Local PDF: pdf/2026-07-10_20_Tracing the Light of Thought_ A Probabilistic Self- and Cross-Consistency Verification Mechanism Improving Mathematical.pdf

Reasoning capability is fundamental in enabling Large Language Models to perform complex multi-step inference. By sampling multiple reasoning paths and selecting the most frequent answer, Self Consistency (SC) remains highly effective but fails on challenging tasks where incorrect answers dominate the majority. Inspired by Metropolis Light Transport in physically-based rendering, where discovered high-contribution light paths guide subsequent sampling toward illumination sources, we propose Metropolis Self Consistency and its multi-LLM extension, Metropolis Cross Consistency, a probabilistic self- and cross-consistency verification framework for mathematical reasoning. Our approach employs an accept-reject mechanism to encourage high-quality reasoning paths, concentrating sampling in regions more likely to yield correct answers. Experiments on 9 LLMs across 4 challenging mathematical benchmarks demonstrate consistent improvements over SC. Even when combining models of vastly different capabilities, MCC maintains performance virtually matching the most capable model while significantly reducing computational cost compared to SC with the strongest model alone. While our implementation is training-free, adds minimal token overhead beyond SC, and requires no external reward model, our approach provides a flexible paradigm that can accommodate any scalar reward representing path correctness.

## 21. OptiCo: Adaptive Distributed Training Optimization via Collaborative Agent Reasoning

- Authors: Sheng Chen, Tang Zhe, Weixing Zhang, Fei Yang, Yuanyuan. Wang, Tianlin Li, Yang Liu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.9557325256320417
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1283/
- PDF: https://aclanthology.org/2026.acl-long.1283.pdf
- Local PDF: pdf/2026-07-10_21_OptiCo_ Adaptive Distributed Training Optimization via Collaborative Agent Reasoning.pdf

Optimizing distributed training strategies for large-scale deep learning models remains a critical challenge in both industry and academia, demanding extensive domain expertise and manual tuning. Existing automated distributed training frameworks are plagued by over-reliance on prior profiling, poor generalization across models/hardware, and scalability constraints stemming from vast search spaces, impeding real-world applicability. To address these challenges, we propose OptiCo, a model-driven multi-agent framework that leverages Large Language Models (LLMs) to enable automatic and explainable distributed training strategy configuration. OptiCo orchestrates a team of reasoning-driven agents, through a shared Global Message Pool facilitating persistent memory and coordination. By employing inception prompting and Chain-Of-Thought (COT) reasoning, agents iteratively refine configurations, detect bottlenecks, analyze failures, and optimize resource utilization. Evaluated across 25+ configurations spanning diverse model architectures, GPU types and scales, OptiCo outperforms expert-designed strategies within 20 iterations, achieving an average performance improvement of 1.84%, with gains ranging from 0.08% to 8.65%. The source codes are avaiable at https://github.com/TangZhe96/OptiCo-public.

## 22. Explore How to Inject Beneficial Noise in MLLMs

- Authors: Ruishu Zhu, Sida Huang, Ziheng Jiao, Hongyuan Zhang
- Source: openalex
- Venue type: conference
- Journal: Proceedings of the AAAI Conference on Artificial Intelligence
- Publication status: formally_published
- Publication date: 2026-03-14
- DOI: https://doi.org/10.1609/aaai.v40i34.40153
- Categories: Multimodal Machine Learning Applications, Topic Modeling, Speech and dialogue systems
- Relevance: 2.9553108270519113
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://doi.org/10.1609/aaai.v40i34.40153
- PDF: https://ojs.aaai.org/index.php/AAAI/article/download/40153/44114
- Local PDF: Not downloaded

Multimodal Large Language Models (MLLMs) have played an increasingly important role in multimodal intelligence. However, the existing fine-tuning methods often ignore cross-modal heterogeneity, limiting their full potential. In this work, we propose a novel fine-tuning strategy by injecting beneficial random noise, which outperforms previous methods and even surpasses full fine-tuning, with minimal additional parameters. The proposed Multimodal Noise Generator (MuNG) enables efficient modality fine-tuning by injecting customized noise into the frozen MLLMs. Specifically, we reformulate the reasoning process of MLLMs from a variational inference perspective, upon which we design a multimodal noise generator that dynamically analyzes cross-modal relationships in image-text pairs to generate task adaptive beneficial noise. Injecting this type of noise into the MLLMs effectively suppresses irrelevant semantic components, leading to significantly improved cross-modal representation alignment and enhanced performance on downstream tasks. Experiments on two mainstream MLLMs, QwenVL and LLaVA, demonstrate that our method surpasses full parameter fine-tuning and other existing fine-tuning approaches, while requiring adjustments to only about 1~2% additional parameters.

## 23. FLARE: Task-Agnostic Embedding Model Evaluation via Normalizing Flows

- Authors: Jingzhou Jiang, Yixuan Tang, Yi Yang, Kar Yan Tam
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.955173149883306
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1957/
- PDF: https://aclanthology.org/2026.findings-acl.1957.pdf
- Local PDF: pdf/2026-07-10_23_FLARE_ Task-Agnostic Embedding Model Evaluation via Normalizing Flows.pdf

Despite the widespread adoption of text embedding models, selecting the optimal model for a specific target corpus remains challenging due to the lack of task-specific labels. While task-agnostic evaluation offers a promising solution by relying on unlabeled data, existing approaches based on kernel estimators or Gaussian mixtures fail to model high-dimensional distributions effectively, resulting in unstable rankings. To address this limitation, we propose FLARE (Flow-based Label-free Assessment of Representation Embeddings), which employs normalizing flows to estimate information sufficiency in high-dimensional spaces. By learning invertible transformations, flows enable exact density estimation while mitigating the instability inherent in distance-based methods. We provide theoretical guarantees showing that our estimation error depends on the data’s intrinsic structure rather than its raw dimensionality. Experiments across 11 datasets demonstrate that FLARE achieves a strong Spearman’s ρ (up to 0.90) with supervised benchmarks, remaining robust even for high-dimensional embeddings (d ≥ 3,584).

## 24. Adaptive and Representative Multi-Interest Modeling for Recommendation with Large Language Model

- Authors: Ziyan Wang, Yingpeng Du, Tianjun Wei, Haoyan Chua, Jieyi Bi, Jie Zhang, Zhu Sun
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.954006621043109
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.117/
- PDF: https://aclanthology.org/2026.findings-acl.117.pdf
- Local PDF: pdf/2026-07-10_24_Adaptive and Representative Multi-Interest Modeling for Recommendation with Large Language Model.pdf

Large language models (LLMs) show potential for multi-interest analysis of users in recommender systems, going beyond heuristic assumptions in existing methods, e.g., co-occurring items indicate the same interest. Despite the effectiveness, two key challenges remain. First, the granularity of raw generation of LLMs for multi-interests is agnostic, possibly leading to overly fine or coarse interest grouping. Second, adopting LLM to analyze individual user behaviors lacks a global perspective on how items relate across users. In this paper, we propose an LLM-driven adaptive and representative multi-interest modeling framework to address these challenges. At the user-individual level, we exploit LLM analysis and alleviate the agnostic granularity by adaptively aggregating semantic clusters to collaborative multi-interests. At the user-crowd level, to mitigate the limited insights in individual behaviors, we formulate a max covering problem to expand the scope of LLM analysis with compactness and representativeness, disentangling interest representations from global perspectives. Experiments on real-world datasets show that our approach outperforms various baselines.

## 25. Rethinking Visual Token Reduction in LVLMs Under Cross-Modal Misalignment

- Authors: Rui Xu, Yunke Wang, Yong Luo, Bo Du
- Source: openalex
- Venue type: conference
- Journal: Proceedings of the AAAI Conference on Artificial Intelligence
- Publication status: formally_published
- Publication date: 2026-03-14
- DOI: https://doi.org/10.1609/aaai.v40i32.39949
- Categories: Multimodal Machine Learning Applications, Generative Adversarial Networks and Image Synthesis, Domain Adaptation and Few-Shot Learning
- Relevance: 2.953820819536133
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://doi.org/10.1609/aaai.v40i32.39949
- PDF: https://ojs.aaai.org/index.php/AAAI/article/download/39949/43910
- Local PDF: Not downloaded

Large Vision-Language Models (LVLMs) encode visual inputs as dense sequences of patch-level tokens to capture fine-grained semantics. These visual tokens often outnumber their textual counterparts by a large margin, leading to substantial computational overhead and limiting the scalability of LVLMs in practice. Previous efforts have explored visual token reduction either prior to or within the large language models (LLMs). However, most in-LLM reduction approaches rely on text-conditioned interactions, implicitly assuming that textual tokens can reliably capture the importance of visual tokens. In this work, we revisit this assumption and reveal causal, semantic, and spatial forms of cross-modal misalignment. These misalignments undermine the effectiveness of text-guided visual token reduction. To address this, we introduce VisionDrop, a training-free, visual-only pruning framework that selects informative visual tokens based on intra-modal (visual-to-visual) attention, without relying on textual signals. To further suppress redundancy throughout the model hierarchy, we treat the visual encoder and the LLM as a unified system and design a progressive pruning pipeline. Our method performs dominant token selection and lightweight contextual merging at multiple stages, enabling fine-grained visual information to be retained even under aggressive token budgets. Extensive experiments across diverse benchmarks show that VisionDrop achieves consistent improvements over existing approaches, despite requiring no additional training or complex modifications. Notably, when integrated with LLaVA-NeXT-7B, VisionDrop achieves a 2.7x reduction in inference latency and 6x in FLOPs, while retaining 95.71% of the original performance.

## 26. Memory Matters More: Event-Centric Memory as a Logic Map for Agent Searching and Reasoning

- Authors: Yuyang Hu, Jiongnan Liu, Jiejun Tan, Yutao Zhu, Zhicheng Dou
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.9526770930761668
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1123/
- PDF: https://aclanthology.org/2026.findings-acl.1123.pdf
- Local PDF: pdf/2026-07-10_26_Memory Matters More_ Event-Centric Memory as a Logic Map for Agent Searching and Reasoning.pdf

Large language models (LLMs) are increasingly deployed as intelligent agents that reason, plan, and interact with their environments. To effectively scale to long-horizon scenarios, a key capability for such agents is a memory mechanism that can retain, organize, and retrieve past experiences to support downstream decision-making. However, most existing approaches organize and store memories in a flat manner and rely on simple similarity-based retrieval techniques. Even when structured memory is introduced, existing methods often struggle to explicitly capture the logical relationships among experiences or memory units. Moreover, memory access is largely detached from the constructed structure and still depends on shallow semantic retrieval, preventing agents from reasoning logically over long-horizon dependencies. In this work, we propose CompassMem, an event-centric memory framework inspired by Event Segmentation Theory. CompassMem organizes memory as an Event Graph by incrementally segmenting experiences into events and linking them through explicit logical relations. This graph serves as a logic map, enabling agents to perform structured and goal-directed navigation over memory beyond superficial retrieval, progressively gathering valuable memories to support long-horizon reasoning. Experiments on LoCoMo and NarrativeQA demonstrate that CompassMem consistently improves both retrieval and reasoning performance across multiple backbone models.

## 27. NeuRAG: End-to-End Neural Knowledge Augmentation via Hyper-Neurons

- Authors: Liwei Zheng, Xuemin Liu, Jie Liu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.952241304796787
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1516/
- PDF: https://aclanthology.org/2026.findings-acl.1516.pdf
- Local PDF: pdf/2026-07-10_27_NeuRAG_ End-to-End Neural Knowledge Augmentation via Hyper-Neurons.pdf

Retrieval-Augmented Generation (RAG) systems have become a standard approach for grounding large language models in external knowledge. However, they are constrained by a decoupled architecture: retrieval and reasoning operate as separate stages, with retrieved text merely prepended as passive context. This prevents deep integration of knowledge into the model’s parametric reasoning, leading to fragmented responses for complex queries requiring multi-document synthesis or conflict resolution. To bridge this gap, we propose NeuRAG, an end-to-end Neuralized RAG framework that unifies knowledge retrieval and fusion through Hyper-Neurons—parameterized modules encoding entire documents directly into the model’s parameter space. In NeuRAG, each document is encoded as a lightweight LoRA module, conceptualized as a knowledge neuron. These neurons collectively form a document-adaptive Hyper-Layer, which dynamically activates and fuses knowledge neurons via an attention mechanism conditioned on the input hidden-state query. This enables the model to jointly retrieve and reason within a single forward pass, seamlessly integrating external knowledge into its inference pathway. Extensive experiments across multiple datasets and LLMs demonstrate NeuRAG’s strong and consistent performance as a promising novel RAG paradigm.

## 28. MathCanvas: Intrinsic Visual Chain-of-Thought for Multimodal Mathematical Reasoning

- Authors: Weikang Shi, Aldrich Yu, Rongyao Fang, Houxing Ren, Ke Wang, Aojun Zhou, Changyao Tian, Xinyu Fu, Yuxuan Hu, Zimu Lu, Linjiang Huang, Si Liu, Rui Liu, Hongsheng Li
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.950790656004605
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1287/
- PDF: https://aclanthology.org/2026.acl-long.1287.pdf
- Local PDF: pdf/2026-07-10_28_MathCanvas_ Intrinsic Visual Chain-of-Thought for Multimodal Mathematical Reasoning.pdf

While Large Language Models (LLMs) have excelled in textual reasoning, they struggle with mathematical domains like geometry that intrinsically rely on visual aids. Existing approaches to Visual Chain-of-Thought (VCoT) are often limited by rigid external tools or fail to generate the high-fidelity, strategically-timed diagrams necessary for complex problem-solving. To bridge this gap, we introduce MathCanvas, a comprehensive framework designed to endow unified Large Multimodal Models (LMMs) with intrinsic VCoT capabilities for mathematics. Our approach consists of two phases. First, a Visual Manipulation stage pre-trains the model on a novel 15.2M-pair corpus, comprising 10M caption-to-diagram pairs (MathCanvas-Imagen) and 5.2M step-by-step editing trajectories (MathCanvas-Edit), to master diagram generation and editing. Second, a Strategic Visual-Aided Reasoning stage fine-tunes the model on MathCanvas-Instruct, a new 219K-example dataset of interleaved visual-textual reasoning paths, teaching it when and how to leverage visual aids. To facilitate rigorous evaluation, we introduce MathCanvas-Bench, a challenging benchmark with 3K problems that require models to produce interleaved visual-textual solutions. Our model, BAGEL-Canvas, trained under this framework, achieves an 86% relative improvement over strong LMM baselines on MathCanvas-Bench, demonstrating excellent generalization to other public math benchmarks. Our work provides a complete toolkit—framework, datasets, and benchmark—to unlock complex, human-like visual reasoning in LMMs.

## 29. Learning What to Ignore: Mitigating Negative Transfer in Medical Knowledge Fusion via Clinical Task-Adaptive Selection

- Authors: Xinyan Deng, Shoubin Dong, Xiaorou Zheng
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.950720407335136
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1067/
- PDF: https://aclanthology.org/2026.acl-long.1067.pdf
- Local PDF: pdf/2026-07-10_29_Learning What to Ignore_ Mitigating Negative Transfer in Medical Knowledge Fusion via Clinical Task-Adaptive Selection.pdf

Integrating external medical knowledge into longitudinal electronic health record modeling is a prevailing paradigm to mitigate clinical data sparsity. However, existing approaches face a reliability-timeliness dilemma, struggling to balance the structural authority of static ontologies with the reasoning flexibility of large language models. Furthermore, most frameworks overlook the risk of relative negative transfer, where indiscriminately fusing task-irrelevant knowledge can introduce noise or even cause conflicts that weakens patient-specific signals. In this paper, we propose TrustKE, a Trustworthy Knowledge Enhancement framework. First, we construct a dual-layer knowledge graph that anchors dynamic, evidence-based chain-of-thought reasoning from medical literature within the stable structure of medical knowledge graph. Second, we introduce a task-adaptive knowledge selection mechanism that dynamically optimizes the graph, retaining only task-specific signals. Extensive experiments on MIMIC-III and MIMIC-IV across four clinical tasks show that TrustKE outperforms state-of-the-art baselines. Our analysis confirms that TrustKE effectively mitigates negative transfer while offering transparent reasoning for clinical decision-making.

## 30. Biomedical Question Answering via Multi-Level Summarization on a Local Knowledge Graph

- Authors: Lingxiao Guan, Yuanhao Huang, Jie Liu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.9505969243435057
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.743/
- PDF: https://aclanthology.org/2026.acl-long.743.pdf
- Local PDF: pdf/2026-07-10_30_Biomedical Question Answering via Multi-Level Summarization on a Local Knowledge Graph.pdf

In Question Answering (QA), Retrieval Augmented Generation (RAG) has revolutionized performance in various domains. However, how to effectively capture multi-document relationships remains an open question. This is particularly critical for biomedical tasks due to their reliance on information spread across multiple documents. In this work, we propose a novel method CLAIMS, which utilizes propositional claims to construct a local knowledge graph from retrieved documents. Summaries are then derived via layerwise summarization from the knowledge graph to contextualize a small language model to perform QA. The structured summaries effectively capture explicit and implicit relationships between entities in the documents, thus having a more comprehensive context to provide to LLMs. CLAIMS achieved comparable or superior performance over RAG baselines on several biomedical QA benchmarks. We also evaluated its generalizability and each individual step of our approach with a targeted set of metrics, demonstrating its effectiveness.
