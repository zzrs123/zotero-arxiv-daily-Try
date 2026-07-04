# Paper Daily Reading - 2026-07-04

## 1. Interpretable spatial multi-omics data integration and dimensionality reduction with SpaMV

- Authors: Yang Liu, Kexin Ma, Haoran Xu, Ke Xu, Yunfei Hu, Zhenhan Lin, Jiangli Lin, Bo Han, S. Li, Zhixiang Lin, Xin Zhou, Lu Zhang
- Source: openalex
- Venue type: journal
- Journal: Nature Communications
- Publication status: published
- Publication date: 2026-07-01
- DOI: https://doi.org/10.1038/s41467-026-74718-1
- Categories: Bioinformatics and Genomic Networks, Gene expression and cancer classification, Single-cell and spatial transcriptomics
- Relevance: 3.9298667822706013
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://doi.org/10.1038/s41467-026-74718-1
- PDF: Unavailable
- Local PDF: Not downloaded

Spatial multi-omics technologies revolutionized our understanding of biological systems by providing spatially resolved molecular profiles from multiple perspectives. Existing spatial multi-omics integration methods often assume that data from different omics share a common underlying distribution and aim to project them into a single unified latent space. This assumption, however, obscures the unique insights offered by each omics, thereby limiting the full potential of multi-omics analyses. To address this limitation, we develop the Spatial Multi-View (SpaMV) representation learning algorithm, which explicitly captures both shared information across omics and the distinct, omics-specific information, enabling a more comprehensive and interpretable representation of spatial multi-omics data. Through extensive evaluation on both simulated and real-world datasets, SpaMV demonstrates superior spatial domain clustering performance and offers topic modeling with more interpretable dimensionality reduction for downstream analysis. Moreover, our method more effectively discovers interpretable omics-specific biomarkers than existing approaches, highlighting its strength in disentangling multi-omics signals. Spatial multi-omics tools can reveal complementary molecular information across tissues, but integrating shared and omics-specific signals remains challenging. Here, the authors develop SpaMV, an interpretable representation learning framework that disentangles shared and omics-specific information to improve spatial multi-omics integration, spatial domain analysis, and biologically meaningful topic discovery.

## 2. Khan-GCL: Kolmogorov–Arnold Network Based Graph Contrastive Learning with Hard Negatives

- Authors: Zihu Wang, Boxun Xu, Hejia Geng, Peng Li
- Source: openalex
- Venue type: conference
- Journal: Proceedings of the AAAI Conference on Artificial Intelligence
- Publication status: formally_published
- Publication date: 2026-03-14
- DOI: https://doi.org/10.1609/aaai.v40i32.39890
- Categories: Advanced Graph Neural Networks, Graph Theory and Algorithms, Machine Learning in Healthcare
- Relevance: 3.783452532937938
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://doi.org/10.1609/aaai.v40i32.39890
- PDF: Unavailable
- Local PDF: Not downloaded

Graph contrastive learning (GCL) has demonstrated great promise for learning generalizable graph representations from unlabeled data. However, conventional GCL approaches face two critical limitations: (1) the restricted expressive capacity of multilayer perceptron (MLP) based encoders, and (2) suboptimal negative samples that either from random augmentations—failing to provide effective 'hard negatives'—or generated hard negatives without addressing the semantic distinctions crucial for discriminating graph data. To this end, we propose Khan-GCL, a novel framework that integrates the Kolmogorov–Arnold Network (KAN) into the GCL encoder architecture, substantially enhancing its representational capacity. Furthermore, we exploit the rich information embedded within KAN coefficient parameters to develop two novel critical feature identification techniques that enable the generation of semantically meaningful hard negative samples for each graph representation. These strategically constructed hard negatives guide the encoder to learn more discriminative features by emphasizing critical semantic differences between graphs. Extensive experiments demonstrate that our approach achieves state-of-the-art performance compared to existing GCL methods across a variety of datasets and tasks.

## 3. MKGR: Multimodal Knowledge-Graph Representation Learning for Cold-Start Protein-Protein Interaction Prediction

- Authors: Wenbo Zhang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-02
- DOI: Unavailable
- Categories: cs.LG, cs.AI
- Relevance: 3.647565471224093
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.01627v1
- PDF: https://arxiv.org/pdf/2607.01627v1
- Local PDF: pdf/2026-07-04_03_MKGR_ Multimodal Knowledge-Graph Representation Learning for Cold-Start Protein-Protein Interaction Prediction.pdf

Accurate protein-protein interaction (PPI) prediction is central to functional genomics, disease mechanism discovery, and drug development. A difficult setting arises when candidate interactions include proteins that have no observed PPI edges during training, where models relying on network topology alone often lose useful context. This paper presents \method, a multimodal representation framework for cold-start PPI prediction. \method\ combines region-aware protein sequence encoding with four protein-centered biomedical knowledge graphs, including protein-drug, protein-disease, protein-miRNA, and protein-lncRNA associations. The sequence branch extracts contextual representations from structurally informed sequence regions, while graph attention encoders learn modality-specific protein embeddings from sparse biomedical associations. A bridge reconstruction objective regularizes graph learning by recovering shared protein-entity associations, and a pair-level gating module adaptively integrates sequence and graph evidence for each candidate protein pair. Experiments on two benchmark datasets under novel-old and novel-novel cold-start settings show that \method\ consistently outperforms competitive sequence, network, and knowledge-graph baselines across ACC, F1, AUC, AUPR, and MCC.

## 4. SABER: A Semantic-Aligned Brain Network Analysis Framework via Multi-scale Hypergraphs

- Authors: Yidan Xu, Xiangmin Han, Rundong Xue, Huihui Ye
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-02
- DOI: Unavailable
- Categories: cs.LG, cs.AI, cs.MM
- Relevance: 3.41700887681262
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.01901v1
- PDF: https://arxiv.org/pdf/2607.01901v1
- Local PDF: pdf/2026-07-04_04_SABER_ A Semantic-Aligned Brain Network Analysis Framework via Multi-scale Hypergraphs.pdf

Effective brain disease diagnosis requires the synergy of brain connectivity patterns and high-level semantic knowledge. Existing methods, however, largely treat semantics from large language models (LLMs) as auxiliary features or supervision, limiting their direct role in decision-making and constraining classification stability and robustness. To overcome this, we propose a semantic-aligned brain network framework that actively integrates LLM-derived semantics into the prediction process. Specifically, ROI-level semantics are first incorporated via global self-attention to enrich node representations and provide whole-brain context. Multi-scale hypergraphs are then constructed to explicitly model functional subnetworks and multi-ROI interactions, addressing the locality limitations of traditional GNNs and capturing high-order dependencies. Finally, a decision-level semantic alignment mechanism selectively injects patient-specific textual embeddings into graph representations, enabling semantics to directly guide predictions without perturbing the underlying network structure. Experiments on public brain network datasets ABIDE and ADHD-200 demonstrate state-of-the-art performance, enhanced stability, and improved interpretability, particularly in small-sample settings.

## 5. MolSight: A Graph-Aware Vision-Language Model for Unified Chemical Image Understanding

- Authors: Wenda Wang, Yihan Tong, Yuwei Hu, Zhewei Wei
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-02
- DOI: Unavailable
- Categories: cs.CV, cs.AI, q-bio.BM
- Relevance: 3.400186526713076
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.01982v1
- PDF: https://arxiv.org/pdf/2607.01982v1
- Local PDF: pdf/2026-07-04_05_MolSight_ A Graph-Aware Vision-Language Model for Unified Chemical Image Understanding.pdf

Using molecular large language models (LLMs) as a unified framework for understanding molecular structures and functions is emerging as a new trend in tasks such as molecular design and drug discovery. However, these models struggle to fully capture the visual representation of molecular structures, limiting their potential. While existing molecular vision-language models (VLMs) show promise, they still face challenges in structural alignment and lack the necessary topological modeling for accurate molecular understanding. To address this, we propose MolSight, a graph-aware vision-language model framework designed to enhance the understanding of molecular images by VLMs. MolSight integrates a Molecular Topology Module to inject chemical-bond adjacency information into vision tokens, and a Molecular Grounding Module to align visual features with chemical symbolic semantics. Our experiments demonstrate that MolSight significantly outperforms existing VLMs, molecular LLMs, and specialized tools across multiple chemical visual understanding tasks, achieving a new level of molecular image reasoning.

## 6. MERLIN-SUITE: Probabilistic modular GRN inference from multi-omics data integrating regulatory priors and transcription factor activity

- Authors: Suvojit Hazra, Marina Kotvanova, Kirstan Gimse, Sushmita Roy
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-02
- DOI: Unavailable
- Categories: q-bio.MN
- Relevance: 3.3449504714605105
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.01791v1
- PDF: https://arxiv.org/pdf/2607.01791v1
- Local PDF: pdf/2026-07-04_06_MERLIN-SUITE_ Probabilistic modular GRN inference from multi-omics data integrating regulatory priors and transcription.pdf

Accurately reconstructing gene regulatory networks (GRNs) is essential for understanding transcriptional processes in development and disease. MERLIN-SUITE (https://github.com/Roy-lab/MERLIN-SUITE) represents a collection of algorithmic extensions based on MERLIN (Modular regulatory network learning with per gene information) a probabilistic framework that infers gene-specific and module-specific regulatory programs of co-regulated modules, capturing both detailed and modular aspects of transcriptional networks. While expression-based inference is effective, it often aligns poorly with experimentally validated regulatory interactions. MERLIN-P addresses this by integrating external regulatory priors, such as motif, ChIP, and perturbation data, to enhance biological relevance and predictive accuracy. MERLIN-P-TFA further advances the framework by incorporating regularized estimation of latent transcription factor activity (TFA), overcoming the limitation that TF mRNA levels may not represent protein activity. By integrating expression data, prior knowledge, and activity-aware modeling, this unified approach supports robust GRN reconstruction in both bulk and single-cell datasets. This chapter presents the MERLIN-SUITE with a focus on MERLIN-P-TFA and demonstrates its use on a single-cell, multi-modal dataset of mouse cellular reprogramming to infer GRNs and identify key regulators.

## 7. OntoLearner: A Modular Python Library for Ontology Learning with Large Language Models

- Authors: Hamed Babaei Giglou, Jennifer D'Souza, Andrei Aioanei, Nandana Mihindukulasooriya, Sören Auer
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-02
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 3.3213754550256027
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.01977v1
- PDF: https://arxiv.org/pdf/2607.01977v1
- Local PDF: pdf/2026-07-04_07_OntoLearner_ A Modular Python Library for Ontology Learning with Large Language Models.pdf

Ontology learning (OL) aims to automatically construct structured knowledge models from text, yet progress remains fragmented across methods, domains, and evaluation practices. Despite decades of research, OL lacks a shared infrastructure for systematic evaluation and ontology access. This absence has hindered progress and fragmented research, leaving the central challenges of OL largely unaddressed. We introduce OntoLearner, a modular, cross-domain, and first-of-its-kind framework that unifies ontology access, large language model (LLM)-driven learning pipelines, and standardized benchmarking. OntoLearner releases 180 machine-readable ontologies spanning 22 domains and provides pipeline-ready datasets with train/dev/test splits for three core OL tasks: term typing, taxonomy discovery, and non-taxonomic relation extraction. Using this infrastructure, we conduct a large-scale empirical study of OL, evaluating 22 retrieval models and 12 LLMs across domains and tasks. The results converge on a finding that reframes the central challenge of OL: failure modes scale with ontological complexity rather than model size or architectural sophistication. The primary bottleneck is not model capability, but a structural mismatch between how models encode knowledge and how ontologies organize it. These findings establish that effective OL is reachable through the cross-domain, multi-task benchmarking enabled by OntoLearner. OntoLearner is open-source (MIT license) at https://github.com/sciknoworg/OntoLearner/.

## 8. scMTNI: Leveraging cellular trajectory and context to infer dynamic GRNs from single-cell multi-omics data

- Authors: Suvojit Hazra, Chandrani Kumari, Sushmita Roy
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-01
- DOI: Unavailable
- Categories: q-bio.MN
- Relevance: 3.315302129275909
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.01508v1
- PDF: https://arxiv.org/pdf/2607.01508v1
- Local PDF: pdf/2026-07-04_08_scMTNI_ Leveraging cellular trajectory and context to infer dynamic GRNs from single-cell multi-omics data.pdf

Transcriptional gene regulatory networks (GRNs) depict the directed relationships between regulators and target genes, determining gene expression patterns in a cell-type-specific manner. Single-cell multi-omics technologies, such as single-cell RNA sequencing (scRNA-seq) and single-cell Assay for Transposase-Accessible Chromatin using sequencing (scATAC-seq), enable high-resolution measurement of cell-type-specific gene expression and regulation in an unprecedented way. However, tools for inferring cell-type-specific GRNs and modeling their dynamics remain scarce. To facilitate the inference and analysis of cell-type-specific GRNs in contexts such as cellular development or disease progression, where cell lineage structure and dynamics are important, we developed a multi-task learning framework, single-cell Multi-Task Network Inference (scMTNI). scMTNI and its associated network analyses tools offer a comprehensive package to define cell-type-specific GRNs and examine their dynamics. This book chapter describes the scMTNI tool and demonstrates its application to an existing cellular reprogramming single cell multi-modal dataset to infer cell-type-specific GRNs and identify key regulators of cellular fate transitions during cellular reprogramming.

## 9. Do LLMs Truly Generalize in the Molecular Domain? A Perturbation-Based Analysis

- Authors: Jiatong Li, Weida Wang, Changmeng Zheng, Shufei Zhang, Yatao Bian, Xiao-yong Wei, Qing Li
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-02
- DOI: Unavailable
- Categories: cs.LG, cs.CL
- Relevance: 3.2524797984244818
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.01800v1
- PDF: https://arxiv.org/pdf/2607.01800v1
- Local PDF: pdf/2026-07-04_09_Do LLMs Truly Generalize in the Molecular Domain_ A Perturbation-Based Analysis.pdf

Large Language Models (LLMs) have recently shown promise in molecular discovery, yet a gap remains between their probabilistic nature over discrete sequential tokens and the rigid topological constraints of chemical space. This raises the question of whether molecular LLMs can generalize beyond the local neighborhoods induced by their sequence-based representations. To systematically investigate this question, we introduce a Molecular Perturbation framework that generates syntax-valid structural variants of training molecules under controlled Graph Edit Distance (GED) to probe the manifold regularity of molecular LLMs. Our analysis shows that even a single edit can cause substantial performance drops on common molecular tasks, revealing a narrow local trust region and fragile sensitivity to structural changes. Since similar molecules tend to exhibit similar properties, In-Context Tuning (ICT), which anchors predictions on structurally similar molecules, offers a natural way to mitigate such fragility. Our experiments also examine whether ICT confers robustness under controlled structural perturbations, and the results suggest that it can partially expand the local trust region and offer a promising direction for stabilizing molecular LLMs against structural variation.

## 10. Affinage: genome-scale mechanistic gene annotation from the published literature

- Authors: Matteo Di Bernardo, Iain M. Cheeseman
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-02
- DOI: Unavailable
- Categories: q-bio.GN
- Relevance: 3.170513498985371
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.02217v1
- PDF: https://arxiv.org/pdf/2607.02217v1
- Local PDF: pdf/2026-07-04_10_Affinage_ genome-scale mechanistic gene annotation from the published literature.pdf

Understanding the mechanistic function of a gene is a critical starting point for biology. However, for much of the human proteome that knowledge is scattered across thousands of primary papers or remains poorly established, while the curated databases biologists rely on can lag years behind recent literature. Large language models can now read and synthesize that literature on demand, but doing so faithfully for many genes is an expensive, non-reproducible retrieval session that does not scale across users. Here, we present Affinage, an LLM pipeline that performs this retrieval and mechanistic reasoning once per gene--from the primary literature alone--and stores the result as a reusable, structured annotation. A biologist-designed reading pass extracts only direct experimental evidence, and a synthesis pass reasons over those findings alone. Applied across the genome, Affinage annotates 19,293 human protein-coding genes. This analysis provides mechanism for thousands of genes whose UniProt function is empty or a stub, beating the curated reference on 99.1% of head-to-head genes as scored by a cross-family LLM judge. Affinage also delineates the 10% of the proteome that remains mechanistically uncharacterized and will serve as a continuously-updated, literature-grounded census of gene function. All records are released openly at https://affinage.wi.mit.edu . More broadly, Affinage serves as an example of how domain experts can encode their expertise into scalable LLM pipelines to improve the publicly available data that guides biological hypotheses and experimentation.

## 11. EO-Agents: A Three-Agent LLM Pipeline for Earth Observation Hypothesis Generation

- Authors: Mahyar Ghazanfari, Amin Tabrizian, Armin Mehrabian, Peng Wei
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-02
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 3.1006848808974774
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.01584v1
- PDF: https://arxiv.org/pdf/2607.01584v1
- Local PDF: pdf/2026-07-04_11_EO-Agents_ A Three-Agent LLM Pipeline for Earth Observation Hypothesis Generation.pdf

Large language models have recently been explored for scientific hypothesis generation, but most prior work relies on unstructured literature and free-form textual claims. We present a pipeline for Earth observation that grounds hypothesis generation directly in the NASA Earth Observation Knowledge Graph. A heterogeneous graph neural network trained on historical co-usage relations ranks candidate dataset pairings, and a three-agent LLM pipeline filters, generates, and evaluates structured research hypotheses. Applied to 1,475 NASA datasets, the system produces 160 hypotheses spanning multiple Earth-science domains, including ecohydrology, glaciology, aerosol--cloud interactions, vegetation phenology, and stratospheric chemistry. Model-predicted novel dataset pairings are rated nearly as plausible as held-out real co-usages from the literature, indicating that the pipeline surfaces scientifically coherent yet unexplored combinations. A 2*2*2 factorial experiment across GPT-5.2 and Claude Sonnet 4.6 shows that hypothesis rankings remain stable, while absolute scores depend strongly on judge identity, highlighting limitations of single-judge LLM evaluation.

## 12. CausalSteward: An Agentic Divide-Conquer-Combine Copilot for Causal Discovery

- Authors: Nicholas Tagliapietra, Gian Lorenzo Marchioni, Moritz Willig, Juergen Luettin, Lavdim Halilaj, Kristian Kersting
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-02
- DOI: Unavailable
- Categories: cs.MA, cs.AI
- Relevance: 3.0607855749952986
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.01936v1
- PDF: https://arxiv.org/pdf/2607.01936v1
- Local PDF: pdf/2026-07-04_12_CausalSteward_ An Agentic Divide-Conquer-Combine Copilot for Causal Discovery.pdf

Learning causal models from high-dimensional data is a significant challenge, particularly in real-world settings where violations of core assumptions lead to causal identifiability issues. Although massive amounts of prior knowledge are available, and contain valuable causal information, effectively integrating this knowledge into the causal discovery process remains an open problem. We introduce CausalSTeward (CAST), a novel human-in-the-loop framework for interactively assembling large causal models. CausalSteward is a multi-agent collaborative system that tackles high-dimensional causality through a divide-and-conquer approach where large clusters of variables are iteratively partitioned and then separately analyzed. Our framework fuses prior knowledge with a data-driven approach by using tailored tools such as retrieval augmented generation and conditional independence tests. Finally, we use this work to examine the capabilities and limitations of causal reasoning in multi-agent frameworks, and how the human-in-the-loop can contribute to accurate and trustworthy results.

## 13. A solvable model of learning generative diffusion: theory and insights

- Authors: Cui, Hugo, Pehlevan, Cengiz, Lu, Yue
- Source: neurips
- Venue type: conference
- Journal: NeurIPS 2025
- Publication status: formally_published
- Publication date: 2026-04-23
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.035058245718405
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://proceedings.neurips.cc/paper_files/paper/2025/hash/082d3d795520c43214da5123e56a3a34-Abstract-Conference.html
- PDF: https://proceedings.neurips.cc/paper_files/paper/2025/file/082d3d795520c43214da5123e56a3a34-Paper-Conference.pdf
- Local PDF: pdf/2026-07-04_13_A solvable model of learning generative diffusion_ theory and insights.pdf

In this manuscript, we analyze a solvable model of flow or diffusion-based generative model. We consider the problem of learning a model parametrized by a two-layer auto-encoder, trained with online stochastic gradient descent, on a high-dimensional target density with an underlying low-dimensional manifold structure. We derive a tight asymptotic characterization of low-dimensional projections of the distribution of samples generated by the learned model, ascertaining in particular its dependence on the number of training samples. Building on this analysis, we discuss how mode collapse can arise, and lead to model collapse when the generative model is re-trained on generated synthetic data.

## 14. InferenceDynamics: Adaptive LLM Routing through Structured Capability and Knowledge Profiling

- Authors: Haochen Shi, Tianshi Zheng, Weiqi Wang, Baixuan Xu, Chunyang Li, Chunkit Chan, Tao Fan, Yangqiu Song
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.033803954430468
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.383/
- PDF: https://aclanthology.org/2026.acl-long.383.pdf
- Local PDF: pdf/2026-07-04_14_InferenceDynamics_ Adaptive LLM Routing through Structured Capability and Knowledge Profiling.pdf

Large Language Model (LLM) routing is a pivotal technique for navigating a diverse landscape of LLMs, enabling the selection of the best-performing LLMs for specific user queries while balancing performance and cost. However, current routing approaches often face limitations in scalability when dealing with a large pool of specialized LLMs, or in their adaptability to extending model scope and evolving capability domains. To overcome those challenges, we propose **InferenceDynamics**, a flexible and scalable multi-dimensional routing framework by modeling the capability and knowledge of models. We operate it on our comprehensive dataset **RouteMix**, and demonstrate its effectiveness and generalizability in group-level routing using modern benchmarks including MMLU-Pro, GPQA, BigGenBench, and LiveBench, showcasing its ability to identify and leverage top-performing models for given tasks, leading to superior outcomes with cost efficiency. The broader adoption of InferenceDynamics can empower users to harness the full specialized potential of the LLM ecosystem, and our code will be made publicly available to encourage further research.

## 15. Self-Correcting RAG: Enhancing Faithfulness via MMKP Context Selection and NLI-Guided MCTS

- Authors: Shijia Xu, Zhou Wu, Xiaolong Jia, Yu Wang, Kai Liu, April Xiaowen Dong
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.0333230686972943
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1052/
- PDF: https://aclanthology.org/2026.findings-acl.1052.pdf
- Local PDF: pdf/2026-07-04_15_Self-Correcting RAG_ Enhancing Faithfulness via MMKP Context Selection and NLI-Guided MCTS.pdf

Retrieval-augmented generation (RAG) substantially extends the knowledge boundary of large language models. However, it still faces two major challenges when handling complex reasoning tasks: low context utilization and frequent hallucinations. To address these issues, we propose Self-Correcting RAG, a unified framework that reformulates retrieval and generation as constrained optimization and path planning. On the input side, we move beyond traditional greedy retrieval and, for the first time, formalize context selection as a multi-dimensional multiple-choice knapsack problem (MMKP), thereby maximizing information density and removing redundancy under a strict token budget. On the output side, we introduce a natural language inference (NLI)-guided Monte Carlo Tree Search (MCTS) mechanism, which leverages test-time compute to dynamically explore reasoning trajectories and validate the faithfulness of generated answers. Experiments on six open-domain and multi-hop QA datasets demonstrate that our method significantly improves reasoning accuracy on complex queries while effectively reducing hallucinations, outperforming strong existing baselines. Our code is available at https://github.com/xjiacs/Self-Correcting-RAG .

## 16. Beyond Variance: Knowledge-Aware LLM Compression via Fisher-Aligned Subspace Diagnostics

- Authors: Ibne Farabi Shihab, Sanjeda Akter, Anuj Sharma
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.0326021228535023
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.2214/
- PDF: https://aclanthology.org/2026.acl-long.2214.pdf
- Local PDF: pdf/2026-07-04_16_Beyond Variance_ Knowledge-Aware LLM Compression via Fisher-Aligned Subspace Diagnostics.pdf

Post-training activation compression is essential for deploying Large Language Models (LLMs) on resource-constrained hardware. However, standard methods like Singular Value Decomposition (SVD) are gradient-blind: they preserve high-variance dimensions regardless of their impact on factual knowledge preservation. We introduce Fisher-Aligned Subspace Compression (FASC), a knowledge-aware compression framework that selects subspaces by directly modeling activation-gradient coupling, minimizing a second-order surrogate of the loss function. FASC leverages the Fisher Information Matrix to identify dimensions critical for factual knowledge, which often reside in low-variance but high-gradient-sensitivity subspaces. We propose the Dependence Violation Score (ρ) as a general-purpose diagnostic metric that quantifies activation-gradient coupling, revealing where factual knowledge is stored within transformer architectures. Extensive experiments on Mistral-7B and Llama-3-8B demonstrate that FASC preserves 6–8% more accuracy on knowledge-intensive benchmarks (MMLU, LAMA) compared to variance-based methods at 50% rank reduction, effectively enabling a 7B model to match the factual recall of a 13B uncompressed model. Our analysis reveals that ρ serves as a fundamental signal of stored knowledge, with high-ρ layers emerging only when models internalize factual associations during training

## 17. Generative-to-Discriminative Test-Time Adaptation via Manifold-Aware Diffusion and Bayesian Distillation

- Authors: Boyun Zhang, Zequn Xie, Fangming Feng, Zihan Zhang, Yongbo He, Chuxin Wang, Sihang Cai, Tao Jin, Qifei Zhang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.0318340371061074
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.350/
- PDF: https://aclanthology.org/2026.findings-acl.350.pdf
- Local PDF: pdf/2026-07-04_17_Generative-to-Discriminative Test-Time Adaptation via Manifold-Aware Diffusion and Bayesian Distillation.pdf

Multimodal Sentiment Analysis (MSA) models typically suffer significant performance degradation under domain shifts. While Test-Time Adaptation (TTA) aims to mitigate this, existing discriminative approaches often succumb to “confident but wrong” predictions on out-of-distribution samples. Conversely, generative models offer robust calibration but incur prohibitive computational costs. To bridge this gap, we propose GD-Adapt (Generative-Discriminative Adaptation), a novel TTA framework that harmonizes the robustness of generative diffusion models with the efficiency of discriminative regression networks via Bayesian Diffusion Distillation (BDD). Specifically, we introduce Auxiliary Generative Regularization (AGR) during pretraining to enforce manifold-aware feature learning. Extensive experiments across five cross-domain scenarios demonstrate our method’s superiority. For instance, on the challenging MOSI to SIMS shift, GD-Adapt reduces Mean Absolute Error (MAE) from 0.6872 to 0.5673 and boosts binary accuracy by 5.81 percentage points (reaching 57.33%). Notably, in scenarios such as SIMS to MOSI, we achieve an 11.18-point gain over the non-adapted baseline.

## 18. LearnerCoMPASS: Intelligent Tutoring System with Dynamic Cognitive Diagnosis and Multi-Model Path Planning

- Authors: Ziji Sheng, Guiyao Tie, Weidong Wang, Pan Zhou, Daizong Liu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.0316791264262184
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.408/
- PDF: https://aclanthology.org/2026.acl-long.408.pdf
- Local PDF: pdf/2026-07-04_18_LearnerCoMPASS_ Intelligent Tutoring System with Dynamic Cognitive Diagnosis and Multi-Model Path Planning.pdf

Existing adaptive learning systems struggle to simultaneously achieve deep personalization, dynamic adaptability, and content trustworthiness, particularly in logically rigorous STEM fields where Large Language Models (LLMs) are prone to "hallucination". This paper introduces LearnerCoMPASS (Cognitive Multi-model Planning Adaptive System), an integrated, end-to-end framework for adaptive learning. At its core, the framework features a novel multi-model path planning algorithm that orchestrates and fuses the outputs of heterogeneous LLM experts to generate and optimize learning sequences. To enable deep personalization, we design a dynamic cognitive diagnosis module that employs an innovative encoder-decoder architecture to generate precise, multi-dimensional cognitive state vectors for learners. To ensure trustworthiness, the system leverages an adaptively constructed dynamic knowledge graph and a Graph-RAG mechanism to provide factual anchors and logical constraints for LLM reasoning, thereby mitigating hallucinations. Extensive experiments demonstrate that LearnerCoMPASS significantly outperforms state-of-the-art baselines in generating high-quality personalized learning paths. Furthermore, ablation studies validate the critical contributions of our dynamic cognitive diagnosis and multi-model planning components.

## 19. EvoSci: A Bio-Inspired Multi-Agent Framework for the Evolution of Scientific Discovery

- Authors: Xiaoyu Xiong, Yuqi Ren, Deyi Xiong
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.0301320541078614
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.447/
- PDF: https://aclanthology.org/2026.acl-long.447.pdf
- Local PDF: pdf/2026-07-04_19_EvoSci_ A Bio-Inspired Multi-Agent Framework for the Evolution of Scientific Discovery.pdf

Large language models (LLMs), have shown strong potential in scientific discovery, yet existing methods still face substantial challenges in the design of research workflows and multi-role collaboration mechanisms. To mitigate these issues, we propose EvoSci, a multi-agent scientific collaboration framework, which integrates bio-inspired evolution with knowledge graph modeling. To iteratively generate, evaluate, and refine research ideas, EvoSci incorporates multiple role-based agents, including mentor, researcher, and reviewer. By combining collaborative reasoning, shared memory, and evolutionary feedback, EvoSci significantly enhances the coherence and creativity of scientific exploration. Experiments on real-world research topics demonstrate that EvoSci significantly outperforms strong baselines in LLM-based structured peer-review and comparative ranking evaluations, achieving the highest overall peer-review score (ICLR 4.90) and top ranking (Top-10 = 54). These results suggest its superiority in both scientific idea generation and continuous discovery.

## 20. Iterative Knowledge Graph Refinement and Integration for Medical Question Answering

- Authors: Haochen Zou, Yongli Wang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.0299615113996117
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.408/
- PDF: https://aclanthology.org/2026.findings-acl.408.pdf
- Local PDF: pdf/2026-07-04_20_Iterative Knowledge Graph Refinement and Integration for Medical Question Answering.pdf

Large Language Models (LLMs) are challenged by generating hallucinations and factually incorrect responses, particularly in complex and specialized medical question answering (QA). Integrating knowledge graphs (KGs) through retrieval-augmented generation (RAG) methods has emerged as a promising direction. However, existing graph-based RAG methods heuristically retrieve and refine question-relevant subgraphs, potentially introducing redundant and noisy factual information that is difficult for LLMs to process, ultimately limiting reasoning capability. To incorporate a concise yet informative evidence subgraph, we propose an iterative medical QA framework. It optimizes graph-based RAG methods by selectively retrieving focused knowledge from KGs to construct a precise evidence subgraph and progressively pruning it utilizing structured feature representations. The targeted KG integration maintains coherent and reliable inference. Experiments on three medical QA benchmark datasets demonstrate that the framework achieves state-of-the-art performance against representative baseline competitors, highlighting the importance of efficient KG integration.

## 21. Hallucination Detection in Long-Form Text Generated by LLMs: A Benchmark and a Hyper-Relational Knowledge Graph Approach

- Authors: Zituo Li, Guangzhou Chen, Jianbin Sun, Qi Song, Yang Kewei
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.0292235383141106
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1673/
- PDF: https://aclanthology.org/2026.findings-acl.1673.pdf
- Local PDF: pdf/2026-07-04_21_Hallucination Detection in Long-Form Text Generated by LLMs_ A Benchmark and a Hyper-Relational Knowledge Graph Approach.pdf

Hallucination detection has attracted increasing attention, particularly in long-form text generation, where language models are more prone to producing factually inaccurate content. Prior studies reveal two limitations: (1) current benchmarks focus on short-form content, lacking the structural complexity required in long-form scenarios; (2) existing methods are constrained by coarse-grained consistency checks and fail to capture long-range and hyper-relational dependencies. To address these challenges, we provide LHD, a benchmark for long-form hallucination detection that contains diverse entity types and intricate factual dependencies spanning extended contexts. We further propose HRKG-HD, a zero-resource, black-box framework that models responses as fact-centric hyper-relational knowledge graphs and detects hallucinations through relation-aware multi-hop reasoning over these graphs. By linking distant facts through shared entities and qualifiers, this design enables a global and dependency-aware verification of factual consistency. Extensive experiments demonstrate that HRKG-HD not only outperforms existing baselines but also exhibits robust and consistent performance across various LLMs.

## 22. Towards Hierarchical Multi-Step Reward Models for Enhanced Reasoning in Large Language Models

- Authors: Teng Wang, Jiang Zhangyi, Zhenqi He, Hailei Gong, Shenyang Tong, Wenhan Yang, Zeyu Li, Yanan Zheng, Zifan He, Zewen Ye, Shengjie Ma, Jianping Zhang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.028737491545831
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.27/
- PDF: https://aclanthology.org/2026.findings-acl.27.pdf
- Local PDF: pdf/2026-07-04_22_Towards Hierarchical Multi-Step Reward Models for Enhanced Reasoning in Large Language Models.pdf

Large Language Models (LLMs) have demonstrated strong mathematical reasoning abilities through supervised fine-tuning and reinforcement learning. However, existing Process Reward Models (PRMs) are vulnerable to reward hacking and require expensive, large-scale annotation of reasoning steps, limiting their reliability and scalability. To address the first problem, we propose a novel reward model approach, Hierarchical Reward Model (HRM), which evaluates both individual and consecutive reasoning steps from fine-grained and coarse-grained level. HRM excels at assessing multi-step mathematical reasoning coherence, particularly in cases where a flawed step is later corrected through self-reflection. Furthermore, to address the inefficiency of autonomously annotating PRM training data via Monte Carlo Tree Search (MCTS), we propose a lightweight data augmentation strategy, Hierarchical Node Compression (HNC), which merges consecutive reasoning steps within the tree structure. Applying HNC to MCTS-generated reasoning trajectories increases the diversity and robustness of HRM training data, while introducing controlled noise with minimal computational overhead. Empirical results on the PRM800K dataset demonstrate that HRM, in conjunction with HNC, achieves superior stability and reliability in evaluation compared to PRM. Furthermore, cross-domain evaluations on MATH500 and GSM8K dataset confirm HRM’s superior generalization and robustness across diverse mathematical reasoning tasks.

## 23. SymbolicThought: Integrating Language Models and Symbolic Reasoning for Consistent and Interpretable Human Relationship Understanding

- Authors: Runcong Zhao, Qinglin Zhu, Hainiu Xu, Bin Liang, Lin Gui, Yulan He
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.028439155770265
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-demo.4/
- PDF: https://aclanthology.org/2026.acl-demo.4.pdf
- Local PDF: pdf/2026-07-04_23_SymbolicThought_ Integrating Language Models and Symbolic Reasoning for Consistent and Interpretable Human Relationship.pdf

Understanding character relationships is essential for interpreting complex narratives and conducting socially grounded AI research. However, manual annotation is time-consuming and low in coverage, while large language models (LLMs) often produce hallucinated or logically inconsistent outputs. We present SymbolicThought, a human-in-the-loop framework that combines LLM-based extraction with symbolic reasoning. The system constructs editable character relationship graphs, refines them using seven types of logical constraints, and enables real-time validation and conflict resolution through an interactive interface. To support logical supervision and explainable social analysis, we release a dataset of 160 interpersonal relationships with corresponding logical structures. Experiments show that SymbolicThought improves annotation accuracy and consistency while significantly reducing time cost, offering a practical tool for narrative understanding, explainable AI, and LLM evaluation. The source code and dataset are publicly available on GitHub (https://github.com/BLPXSPG/SymbolicThought).

## 24. One Cognitive Loop Is Enough: SODA unlocks Pure-Text Spatial Reasoning in Large Language Models

- Authors: Shunwen Bai, Jiahuan Zhang, Haoran Huang, Yurun Wang, Jiale Liu, Yanxi Wu, Ningzhe Yu, Yudong Gao, Mingjun Cheng
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.0283203778016077
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1382/
- PDF: https://aclanthology.org/2026.acl-long.1382.pdf
- Local PDF: pdf/2026-07-04_24_One Cognitive Loop Is Enough_ SODA unlocks Pure-Text Spatial Reasoning in Large Language Models.pdf

Currently, large language models (LLMs) have significant limitations in spatial reasoning, particularly in the absence of visual input. To address this issue, we introduce SODA (Spatial OODA), which draws inspiration from the OODA cognitive loop (Observe, Orient, Decide, Act), originally designed to enhance human decision-making in dynamic environments. Specifically, we embed the OODA loop into multiple control tasks, generating the SPOD-143k dataset, and successfully integrate it into LLMs through a two-phase and spatia-aware training strategy (SFT and GRPO). Furthermore, to fill the gap in evaluating spatial reasoning in purely text-based LLMs, we introduce the SPOD-Bench benchmark, including multiple tasks divided into three levels of difficulty. Experimental results show that SODA significantly enhances the spatial reasoning capabilities of LLMs across testing scenarios including SPOD-Bench, SPACE and applications, providing a replicable and effective paradigm for improving the spatial cognition of LLMs.

## 25. AFMRL: Attribute-Enhanced Fine-Grained Multi-Modal Representation Learning in E-commerce

- Authors: Biao Zhang, Lixin Chen, Bin Zhang, Wang Zongwei, Tong Liu, Bo Zheng
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.0282931029501308
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.704/
- PDF: https://aclanthology.org/2026.findings-acl.704.pdf
- Local PDF: pdf/2026-07-04_25_AFMRL_ Attribute-Enhanced Fine-Grained Multi-Modal Representation Learning in E-commerce.pdf

Multimodal representation is crucial for E-commerce tasks such as identical product retrieval. Large representation models (e.g., VLM2Vec) demonstrate strong multimodal understanding capabilities, yet they struggle with fine-grained semantic comprehension, which is essential for distinguishing highly similar items. To address this, we propose Attribute-Enhanced Fine-Grained Multi-Modal Representation Learning (AFMRL), which defines product fine-grained understanding as an attribute generation task. It leverages the generative power of Multimodal Large Language Models (MLLMs) to extract key attributes from product images and text, and enhances representation learning through a two-stage training framework: 1) Attribute-Guided Contrastive Learning (AGCL), where the key attributes generated by the MLLM are used in the image-text contrastive learning training process to identify hard samples and filter out noisy false negatives. 2) Retrieval-aware Attribute Reinforcement (RAR), where the improved retrieval performance of the representation model post-attribute integration serves as a reward signal to enhance MLLM’s attribute generation during multimodal fine-tuning. Extensive experiments on large-scale E-commerce datasets demonstrate that our method achieves state-of-the-art performance on multiple downstream retrieval tasks, validating the effectiveness of harnessing generative models to advance fine-grained representation learning.

## 26. GMSA: Enhancing Context Compression via Group Merging and Layer Semantic Alignment

- Authors: Jiwei Tang, Zhicheng Zhang, Shunlong Wu, Jingheng Ye, Lichen Bai, Zitai Wang, Tingwei Lu, Lin Hai, Yiming Zhao, Hai-Tao Zheng, Hong-Gee Kim
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.0273118485129027
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1324/
- PDF: https://aclanthology.org/2026.acl-long.1324.pdf
- Local PDF: pdf/2026-07-04_26_GMSA_ Enhancing Context Compression via Group Merging and Layer Semantic Alignment.pdf

Large Language Models (LLMs) have achieved remarkable performance across a wide range of Natural Language Processing (NLP) tasks. However, in long-context scenarios, they face two challenges: high computational cost and information redundancy. To address these challenges, we propose GMSA, an encoder-decoder context compression framework that generates a compact sequence of soft tokens for downstream tasks. GMSA introduces Group Merging to achieve more uniform aggregation, mitigating semantic dominance during autoencoder pretraining, and Layer Semantic Alignment (LSA) to bridge the semantic gap between high-level abstract semantics and low-level input semantics. We first pretrain GMSA as an autoencoder and then fine-tune it for downstream tasks. Experiments demonstrate that GMSA improves context reconstruction compared to existing soft prompt compression paradigm and outperforms baselines on multiple long-context question answering and summarization benchmarks across two backbone models, while maintaining low end-to-end latency.

## 27. Reasoning Over Space: Enabling Geographic Reasoning for LLM-Based Generative Next POI Recommendation

- Authors: Dongyi Lv, Qiuyu Ding, Heng-Da Xu, Zhaoxu Sun, Zhi Wang, Feng Xiong, Mu Xu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.0269492477151823
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.332/
- PDF: https://aclanthology.org/2026.acl-long.332.pdf
- Local PDF: pdf/2026-07-04_27_Reasoning Over Space_ Enabling Geographic Reasoning for LLM-Based Generative Next POI Recommendation.pdf

Generative recommendation with large language models (LLMs) reframes prediction as sequence generation, yet existing LLM-based recommenders remain limited in leveraging geographic signals that are crucial in mobility and local-services scenarios. Here, we present Reasoning Over Space (ROS), a framework that utilizes geography as a vital decision variable within the reasoning process. ROS introduces a Hierarchical Spatial Semantic ID (SID) that discretizes coarse-to-fine locality and POI semantics into compositional tokens, and endows LLM with a three-stage Mobility Chain-of-Thought (CoT) paradigm that models user personality, constructs an intent-aligned candidate space, and performs locality informed pruning. We further align the model with real world geography via spatial-guided Reinforcement Learning (RL). Experiments on three widely used location-based social network (LBSN) datasets show that ROS achieves over 10% relative gains in hit rate over strongest LLM-based baselines and improves cross-city transfer, despite using a smaller backbone model.

## 28. RedOne 2.0: Rethinking Domain-specific LLM Post-Training in Social Networking Services

- Authors: Fei zhao, Chonggang Lu, Haofu Qian, Fangcheng Shi, Zijie Meng, Jianzhao Huang, Zheyong Xie, Shaosheng Cao
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.026056773381471
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-industry.90/
- PDF: https://aclanthology.org/2026.acl-industry.90.pdf
- Local PDF: pdf/2026-07-04_28_RedOne 2.0_ Rethinking Domain-specific LLM Post-Training in Social Networking Services.pdf

As a primary medium for human interaction and information exchange, social networking services (SNS) present distinct challenges for large language models (LLMs): rapidly evolving norms and slang, and culturally diverse content that causes knowledge distribution shift. While supervised fine-tuning (SFT) can improve in-domain performance, it often induces a ”seesaw” trade-off with out-of-domain robustness, especially for smaller models. To address these challenges, we present RedOne 2.0, an SNS-oriented LLM developed with a progressive, RL-prioritized post-training paradigm for fast and stable adaptation. Our pipeline has three stages: (1) Exploratory Learning on curated SNS corpora to establish initial alignment and surface systematic weaknesses; (2) Targeted Fine-Tuning that applies SFT only to diagnosed gaps while mixing a small amount of general data to reduce forgetting; and (3) Refinement Learning that re-applies RL with SNS-centric signals to consolidate gains and balance trade-offs across tasks. Across various tasks in three categories, our 4B model improves by 2.41 on average over the prior 7B RedOne baseline. It also yields an 8.74 average gain over its Qwen3-4B base while using less than half the data required by the SFT-centric method, demonstrating superior data efficiency and stability at compact scales. Overall, RedOne 2.0 provides a competitive, cost-effective baseline for SNS-specific LLMs, improving capability without sacrificing robustness.

## 29. dLLM: Simple Diffusion Language Modeling

- Authors: Zhanhui Zhou, Lingjie Chen, Hanghang Tong, Dawn Song
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.0251234660259163
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-demo.8/
- PDF: https://aclanthology.org/2026.acl-demo.8.pdf
- Local PDF: pdf/2026-07-04_29_dLLM_ Simple Diffusion Language Modeling.pdf

Although diffusion language models (DLMs) are evolving quickly, many recent models converge on a set of shared components. These components, however, are distributed across ad-hoc research codebases or lack transparent implementations, making them difficult to reproduce or extend. As the field accelerates, there is a clear need for a unified framework that standardizes these common components while remaining flexible enough to support new methods and architectures.To address this gap, we introduce dLLM, an open-source framework that unifies the core components of diffusion language modeling—training, inference, and evaluation—and makes them easy to customize for new designs. With dLLM, users can reproduce, finetune, deploy, and evaluate open-source large DLMs such as LLaDA and Dream through a standardized pipeline.The framework also provides minimal, reproducible recipes for building small DLMs from scratch with accessible compute—including converting any BERT-style encoder or autoregressive LM into a DLM. We also release the checkpoints of these small DLMs to make DLMs more accessible and accelerate future research.

## 30. Lost in Decomposition: Analyzing and Mitigating the Limitations of Long Context Methods via Context Dependency

- Authors: Jiayuan Guo, Yueyang Su, Yuyao Ge, Saiping Guan, Lei Yu, Jiafeng Guo, Xueqi Cheng
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 3.025073507705506
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.2097/
- PDF: https://aclanthology.org/2026.findings-acl.2097.pdf
- Local PDF: pdf/2026-07-04_30_Lost in Decomposition_ Analyzing and Mitigating the Limitations of Long Context Methods via Context Dependency.pdf

Long context large language models exhibit the “lost in the middle” problem, where models struggle to effectively utilize information located in the middle of long contexts. Although existing workflow-based long context methods (e.g., RAG) alleviate this problem and perform well on specific datasets, can their effectiveness generalize to all types of datasets? In this work, we systematically investigate the cross-dataset generalization of long context methods. Our evaluation reveals that these methods are not universally effective. Such substantial performance variability underscores the risks of performance degradation associated with the indiscriminate application of long context methods. We investigated the reason for the failure of long context methods. We found that the intrinsic decomposition mechanisms of long context methods hinder context dependency modeling, causing these methods to suffer performance declines on documents with strong context dependency. To address this issue, We propose CoDaR (**Co**ntext **D**ependency-**a**ware **R**outing), a training-free adaptive routing strategy. By analyzing the context dependency strength of documents, CoDaR adaptively invokes long context methods, thereby significantly enhancing their overall robustness across different types of datasets.
