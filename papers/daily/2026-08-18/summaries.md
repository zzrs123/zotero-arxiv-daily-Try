# Paper Daily Reading - 2026-08-18

## 1. Disentangled Shared Representations Improve Morpho-Transcriptomic Integration

- Authors: Julian Ostermaier, Swann Ruyter, Reuben Dorent, Daniel Racoceanu
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-14
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 3.9250435654632128
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.14355v1
- PDF: https://arxiv.org/pdf/2608.14355v1
- Local PDF: pdf/2026-08-18_01_Disentangled Shared Representations Improve Morpho-Transcriptomic Integration.pdf

Spatial transcriptomics (ST) enables the simultaneous profiling of gene expression and tissue morphology, creating an opportunity to learn multimodal representations capturing shared morpho-transcriptomic structure. However, standard multimodal models often compress modalities into a common latent space without explicitly separating shared and modality-specific sources of variation, which may limit downstream utility. We investigate whether explicit disentanglement of shared and private latent components improves multimodal representation learning for paired Hematoxylin \& Eosin (H\&E) and ST data. We compare VAE-based and contrastive approaches, each in standard and disentangled variants, across two cancer cohorts under matched experimental conditions. Representations are evaluated using cross-modal reconstruction, downstream probing and cross-modal probe transfer. The experiments suggest two main trends. First, contrastive objectives yield higher downstream probing performance than VAE-based models. Second, disentangled variants improve the selected reconstruction and probing metrics, although the gains depend on the model family, task, direction, and disentanglement strength. Overall, our results suggest that explicitly factorizing shared and modality-specific information can improve multimodal representation learning for spatial transcriptomics and provides a useful evaluation framework for future foundation models.

## 2. Program-space Diffusion for Morphology-to-Transcriptomics Prediction

- Authors: Ruyter Swann, Dorent Reuben, Racoceanu Daniel
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-14
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 3.429506772130865
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.14330v1
- PDF: https://arxiv.org/pdf/2608.14330v1
- Local PDF: pdf/2026-08-18_02_Program-space Diffusion for Morphology-to-Transcriptomics Prediction.pdf

Spatial transcriptomics (ST) enables genome-wide gene expression profiling while preserving tissue architecture, but its cost and limited scalability remain major bottlenecks. This has motivated models that predict spatial expression directly from routine histology. Despite promising results, most existing approaches operate at the gene level without leveraging established transcriptomic modeling practices and rely on heterogeneous gene selection strategies, which complicates fair comparison across methods.
  We propose to reformulate morphology-to-transcriptomics prediction as conditional generation in transcriptional program space, thereby exploiting coordinated transcriptional variation instead of predicting genes independently. Using consensus non-negative matrix factorization (cNMF), we extract a low-dimensional set of transcriptional programs capturing coordinated expression variation in the training data, and train a conditional diffusion model to generate program activations from histology. This formulation exploits coordinated transcriptional variation and substantially lowers the dimensionality of the conditional generative task.

## 3. Concept Guidance: Precise, Training-Free Latent Control for Text-to-Image Generation

- Authors: Nikolai Röhrich, Isabell Hans, Felix Krause, Björn Ommer
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-14
- DOI: Unavailable
- Categories: cs.CV, cs.AI, cs.LG
- Relevance: 3.306222889841337
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.14172v1
- PDF: https://arxiv.org/pdf/2608.14172v1
- Local PDF: pdf/2026-08-18_03_Concept Guidance_ Precise, Training-Free Latent Control for Text-to-Image Generation.pdf

Text-to-image diffusion models have two major drawbacks that severely limit their practical utility: (1) standard models lack an intrinsic mechanism for continuous, concept-specific guidance (e.g., for precisely controlling how aesthetically pleasing an image looks), and (2) they lack reliability for tasks requiring high local coherence (e.g., generating text or human hands). To tackle these issues, we introduce a novel notion of concept-wise mutual information and find large, concept-dependent differences between individual layers, demonstrating that the generation of specific structures is localized in distinct parts of the network. We exploit this insight by reinforcing the impact of concept-relevant layers in Concept Guidance (CoG), a precise, target-specific guidance method that works for models out-of-the-box without additional training, external models, gradients, or prompt engineering. CoG first quantifies each layer's concept-specific impact and then guides denoising using a weighted combination of predictions generated with concept-relevant layers skipped. We demonstrate performance increases across various targets and popular models like PixArt-alpha, SD3, SD3.5, and FLUX.1-dev. Code is available at https://github.com/CompVis/concept_guidance

## 4. SDO: Subspace Deconflicting Operator for Multi-Adapter Composition

- Authors: Zhongsheng Wang, Zhedong Lin, Qian Liu, Xinyu Zhang, Jiamou Liu
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-13
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 3.294236366375596
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.13820v1
- PDF: https://arxiv.org/pdf/2608.13820v1
- Local PDF: pdf/2026-08-18_04_SDO_ Subspace Deconflicting Operator for Multi-Adapter Composition.pdf

Composing independently trained adapters within a shared diffusion backbone provides a modular approach to multi-character generation, but naive joint deployment often causes identity mixing, cross-character attribute leakage, and unstable scene composition. We study this interference from a parameter-space perspective and hypothesize that it arises partly from conflicts between overlapping dominant subspaces in shared layers. To address this issue, we propose \textbf{SDO}, a \textbf{S}ubspace \textbf{D}econflicting \textbf{O}perator for multi-adapter composition. SDO reconstructs layer-wise low-rank updates from the selected adapters, extracts compact subspace signatures, measures pairwise conflict through output-subspace overlap, and applies a permutation-equivariant transformation that suppresses harmful shared directions while retaining identity-specific characteristics. The resulting representations are mapped back to standard adapter updates and can be directly incorporated into existing diffusion inference pipelines. Experiments demonstrate that SDO consistently improves identity fidelity and compositional stability, with particularly clear gains as the number of jointly composed adapters increases.

## 5. AutoSchema: Live Schema Grounding for Agentic Text-to-Sparql over Heterogeneous Knowledge Graphs

- Authors: Yiming Zhang, Koji Tsuda
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-14
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.2909074195957655
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.14228v1
- PDF: https://arxiv.org/pdf/2608.14228v1
- Local PDF: pdf/2026-08-18_05_AutoSchema_ Live Schema Grounding for Agentic Text-to-Sparql over Heterogeneous Knowledge Graphs.pdf

Life science knowledge graphs make large collections of structured data available through SPARQL, but each resource uses its own schema, identifiers, and links. TogoMCP helps language model agents query these resources by providing curated Metadata Interoperability Exchange files. Creating and maintaining these files still requires language model assisted drafting, validation, and manual review. We study \emph{live schema grounding}, where an agent obtains the schema evidence needed for a question directly from the current endpoints. We present \textsc{autoschema}, a general framework for live schema grounding that requires no training. It inspects live schemas, maps entity names in a question to graph identifiers, explores relation paths, and finds possible connections between resources during iterative query construction. We use TogoMCP as our main comparison framework. We evaluate \textsc{autoschema} on Resource Focused Biomedical KGQA, Multi Resource Biomedical KGQA, Longitudinal Biomedical Semantic QA over BioASQ Task B, and Chemistry Knowledge Graph Transfer to a previously undocumented RDF graph. \textsc{autoschema} improves mean factoid accuracy over TogoMCP in the biomedical KGQA tasks and gives consistent gains in the longitudinal BioASQ evaluation. It also reduces iteration budget exhaustion and uses fewer tool calls on average in the core evaluation. The transfer study gives preliminary evidence that live schema grounding can support irregular and previously unseen graphs without first creating a curated schema file.

## 6. SheetCompass: Hierarchical Relation Graphs for Agentic Spreadsheet Reasoning

- Authors: Panjing He, Mingyue Cheng, Yucong Luo, Li Li, Xiaohan Zhang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-14
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 3.1568049673433025
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.14452v1
- PDF: https://arxiv.org/pdf/2608.14452v1
- Local PDF: pdf/2026-08-18_06_SheetCompass_ Hierarchical Relation Graphs for Agentic Spreadsheet Reasoning.pdf

Spreadsheets are widely used to organize, analyze, and manipulate semi-structured data, yet automated spreadsheet reasoning remains challenging for large language models (LLMs). Real-world workbooks often contain implicit cross-table associations, fine-grained column dependencies, and complex spatial layouts. Existing methods typically flatten these multidimensional structures into sequential strings, losing important intra-sheet boundaries and inter-sheet semantics. Consequently, LLMs cannot exploit the global spatial context that human experts naturally use when inspecting spreadsheets. We propose SheetCompass, a graph-guided and memory-driven agentic framework for spreadsheet reasoning and automation. SheetCompass explicitly models structural relationships within and across worksheets while maintaining task-relevant information in memory, enabling agents to reason more effectively over complex workbooks.

## 7. Modular Cognitive Architecture Emerges in Large Language Models

- Authors: Pengrui Han, Jacob Andreas, Evelina Fedorenko, Andrea Gregor de Varda
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-06-27
- DOI: Unavailable
- Categories: cs.AI, cs.CL, cs.LG
- Relevance: 3.1341722599965225
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.13567v1
- PDF: https://arxiv.org/pdf/2608.13567v1
- Local PDF: pdf/2026-08-18_07_Modular Cognitive Architecture Emerges in Large Language Models.pdf

The human brain exhibits a striking degree of functional specialization, with distinct networks supporting language, formal reasoning, reasoning about other minds, and reasoning about the physical world. Is this modular organization a fundamental principle of how intelligent systems must be built, or an evolutionary accident specific to biological brains? Here, we test whether a similar organization emerges in Large Language Models--another class of intelligent systems created through a very different optimization process. Using circuit analyses across N=46 tasks spanning four cognitive domains (language, formal reasoning, social reasoning, physical reasoning), we find that LLMs develop a modular architecture that mirrors the human brain: tasks drawing on the same network in humans recruit overlapping neurons in LLMs, whereas tasks drawing on different networks recruit distinct neurons. The convergent emergence of modularity in brains and neural networks suggests that it may be a fundamental property of intelligent systems.

## 8. In situ Discovery of Immune Repertoire Reveals Antitumor Immunity and Therapeutic Antibodies

- Authors: Zhang, H., Wang, P., Zhao, Y., Yang, L., Xue, T., Liu, L., Zhao, Y., Zhang, Z., Ma, J., Zeng, B., Zhang, P., Wang, C., Pan, D., Gao, Z., Liu, Z., Zeng, Z.
- Source: biorxiv
- Venue type: preprint
- Journal: biorxiv
- Publication status: preprint
- Publication date: 2026-08-17
- DOI: 10.64898/2026.08.11.744176
- Categories: bioinformatics
- Relevance: 3.085904775761775
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://www.biorxiv.org/content/10.64898/2026.08.11.744176v1.full.pdf
- PDF: https://www.biorxiv.org/content/10.64898/2026.08.11.744176v1.full.pdf
- Local PDF: Not downloaded

Spatial transcriptomics offers a glimpse into the immunology of tissues. However, limitations in spatial transcriptomics preclude the detection of highly diverse, low-abundance, and previously unknown sequences, including immune repertoires and microbiota. Here, we introduce Archimap, a spatial transcriptomic platform that simultaneously profiles spatial transcriptomes, immune repertoires, and microbiota from formalin-fixed paraffin-embedded (FFPE) tissues. Using Archimap, we profile the spatial localization of TCRs, BCRs, and the microbiota landscape in archived clinical tissues at single-cell resolution. Through comprehensive benchmarking, we validate Archimap's performance and fidelity. Archimap in situ assembles the immune complex and reconstructs the clonal evolution of antibodies. Together, Archimap shows the power of in situ discovery of functional immune repertoires for their antitumor immunity.

## 9. Geometric Filtering of LLM-Generated Samples for Few-Shot Text Classification

- Authors: Benjamín Schindler, Gonzalo A. Ruz
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-14
- DOI: Unavailable
- Categories: cs.LG, cs.CL
- Relevance: 3.0556272019305517
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.13866v1
- PDF: https://arxiv.org/pdf/2608.13866v1
- Local PDF: pdf/2026-08-18_09_Geometric Filtering of LLM-Generated Samples for Few-Shot Text Classification.pdf

Large language models (LLMs) can generate synthetic training data for text classification, but the quality of generated samples is heterogeneous: some fall in correct class regions of the embedding space while others land in peripheral or cross-class zones. We propose a geometric filtering framework that evaluates each LLM-generated sample by its Euclidean distance to real class examples in a sentence embedding space, selecting only geometrically consistent candidates. A soft weighting mechanism transforms filter scores into sample weights for classifier training. Evaluated across 13 datasets, 5 classifiers, 10 augmentation methods, and over 6,700 configurations, our method achieves +2.61 percentage points (pp) over SMOTE ($p<0.0001$, Cohen's $d=0.95$, 88.9% win rate). The approach generalizes to named entity recognition (+9.26pp, 100% win rate) without filter modification, and is robust across 5 LLMs from 4 providers. A key finding is that the simplest distance-based filter consistently outperforms complex multi-criteria alternatives.

## 10. Intern-S2-Mobius: Foundation Model with Decoupled Knowledge and Reasoning

- Authors: Kai Chen, Jifeng Ding, Ning Ding, Jiaye Ge, Lixin Gu, Yicheng Gu, Qipeng Guo, Ermo Hua, Haian Huang, Haozheng Hou, Jie Hou, Xiangyu Hong, Che Jiang, Minxi Jin, Cheng Liang, Dahua Lin, Dawei Liu, Kuikun Liu, Chengqi Lv, Haijun Lv, Han Lv, Ningsheng Ma, Biqing Qi, Jianmin Qian, Shiya Su, Youbang Sun, Huanze Tang, Zhongbo Tian, Hanjing Wang, Rui Wang, Ting Wang, Yi Wang, Baiting Wu, Jun Xu, Bowen Yang, Hui Wang, Weida Wang, Haochen Ye, Jiashuo Yu, Shan Yu, Xiaoyi Yu, Qirui Zeng, Qi Zhang, Ming Zhang, Wenwei Zhang, Bowen Zhou, Xinyu Zhou
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-14
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 3.044040834858548
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.14290v1
- PDF: https://arxiv.org/pdf/2608.14290v1
- Local PDF: pdf/2026-08-18_10_Intern-S2-Mobius_ Foundation Model with Decoupled Knowledge and Reasoning.pdf

We introduce Mobius-v0, an architecture that comprises a globally shared Memory (FFN) that stores knowledge vectors and multiple Reasoners (Self-Attn) that iteratively achieve compositional reasoning. Using hidden states as cache and carrier, reasoners repeatedly query memory for required knowledge-vectors, while the knowledge is transmitted back to reasoning operators. Through this knowledge-reasoning-separation architecture, Mobius achieves better knowledge compression and reasoning efficiency. Built upon Mobius-v0 architecture: 1) Our 7B model trained-from-scratch achieves similar downstream score as a 7B Transformer baseline with 62.6% of baseline's training data. 2) Our Intern-S2-Mobius, continually-pretrained from Qwen3.5-35B, achieves similar downstream score while delivering nearly 4x end-to-end inference speedup.

## 11. Think in Latent, Explain in Language: Self-Explainable Latent Reasoning

- Authors: Dayuan Zhao, Shengcao Cao, Yu-Xiong Wang, Liang-Yan Gui
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-01
- DOI: Unavailable
- Categories: cs.CL, cs.AI, cs.LG
- Relevance: 2.9607175727659643
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.13570v1
- PDF: https://arxiv.org/pdf/2608.13570v1
- Local PDF: pdf/2026-08-18_11_Think in Latent, Explain in Language_ Self-Explainable Latent Reasoning.pdf

Latent reasoning has emerged as a powerful alternative to text-based Chain-of-Thought (CoT), offering significant gains in computational efficiency by compressing verbose reasoning into compact embeddings. However, compressing reasoning into the latent space renders the thinking opaque, hindering its interpretability. Current methods present a stark trade-off: they either function as unexplainable ''black boxes'' (e.g., Coconut), where the latent reasoning is not human-readable, or rely on separate post-hoc decoders for explainability (e.g., Heima), introducing architectural overhead and decoupling the explanation from the actual reasoning process. In this work, we present a unified framework for Self-Explainable Latent Reasoning (SELR) that trains a single model to perform efficient and inherently explainable latent reasoning. Our core contribution is a novel multi-task training objective that optimizes for two goals simultaneously: (1) an Answer Loss that optimizes the latent reasoning trajectory to produce accurate final answers, and (2) a CoT Loss that explicitly trains the same model to decode its own latent representations back into human-understandable reasoning steps. This design ensures that generated latent representations are both task-effective and semantically interpretable, eliminating the need for external decoders. We validate the effectiveness of SELR on both Large Language Models (LLMs) and Vision-Language Models (VLMs), demonstrating that SELR achieves superior token efficiency and accuracy compared to baselines, while uniquely providing self-contained explainability without auxiliary models. Project page is available at https://jasondayuan.github.io/SELR/.

## 12. CytoBERT: A Foundation Model for Cytometry Data

- Authors: Syed Abdul Haseeb Qadri, Bjarne C. Hiller, Felix Blanke, Vanja Sophie Cangalovic, Kutalmış Coşkun, Amin Mirzaei, Tom Siegl, Sebastian Bader, Thomas Kirste, Martin Becker
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-14
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 2.9383724899385912
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.14414v1
- PDF: https://arxiv.org/pdf/2608.14414v1
- Local PDF: pdf/2026-08-18_12_CytoBERT_ A Foundation Model for Cytometry Data.pdf

Cytometry measures the complex characteristics of single cells (e.g., counts and protein expression of immune cells) and is widely used across immunological research and clinical settings. However, cytometry data is highly heterogeneous and unstandardized due to experimental protocols and the choice of measured features. While machine learning methods hold the potential to gain deeper insights into cell biology, these challenges make them difficult to apply and transfer across studies. Recent advances in foundation models can alleviate these issues, but corresponding approaches are still scarce in this field. To address this, we provide CytoBERT, a publicly available, open-source, open-weight foundation model for single-cell cytometry data with variable marker panels. CytoBERT is pretrained in a self-supervised manner on a large-scale cytometry corpus (15 human datasets with heterogeneous marker panels and more than 50 million cells) curated through marker standardization, enabling it to learn transferable inter-marker relationships within cells. Fine-tuning CytoBERT for sample-level classification demonstrates that transfer learning across heterogeneous cytometry datasets is feasible, providing a starting point for scalable, generalizable cytometry analysis. Code is available at GitHub.

## 13. Generating Benchmark Health Data Using a Tabular Diffusion Transformer

- Authors: Hao Yan, Lisa Pilgram, Dan Liu, Linglong Kong, Fida Dankar, Khaled El Emam
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-14
- DOI: Unavailable
- Categories: cs.LG, cs.AI
- Relevance: 2.9078015251236615
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.14496v1
- PDF: https://arxiv.org/pdf/2608.14496v1
- Local PDF: pdf/2026-08-18_13_Generating Benchmark Health Data Using a Tabular Diffusion Transformer.pdf

Cross-Tabular Data Generation (CTDG) seeks to learn a generative model from multiple heterogeneous tables and produce new synthetic tabular datasets. However, existing synthetic tabular data generation methods are largely restricted to single-input-table scenarios and struggle to effectively handle multiple heterogeneous tables with diverse feature sets. To address this limitation, we propose a two-stage framework for cross-tabular data generation. In the first stage, each heterogeneous raw table is transformed into a standardized statistical table with the same set of columns across all tables. Each statistical table captures the marginal distributions of the original columns and the pairwise correlations among them. In the second stage, a diffusion transformer model is trained to capture structural patterns across these homogeneous statistical tables and to generate synthetic statistical tables. Synthetic raw tables are subsequently reconstructed from the generated statistical tables via multivariate Gaussian sampling followed by an inverse probability integral transform. This two-stage CTDG framework enables the learning of a unified generative model from multiple heterogeneous tables and supports the generation of an unlimited number of realistic synthetic heterogeneous tables. Experimental results demonstrate high fidelity in the learned statistical representations and a favorable fidelity-diversity trade-off in the generated synthetic data, validating the effectiveness of the proposed approach.

## 14. Federated Prompt Learning: A Unified Framework, Empirical Analysis, and Future Directions

- Authors: Qinglin Yang, Chen Qiu, Hongyuan Zhang, Pengdeng Li, Yuan Liu, Zhihong Tian
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-14
- DOI: Unavailable
- Categories: cs.LG, cs.AI, cs.DC
- Relevance: 2.8995684262920385
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.13844v1
- PDF: https://arxiv.org/pdf/2608.13844v1
- Local PDF: pdf/2026-08-18_14_Federated Prompt Learning_ A Unified Framework, Empirical Analysis, and Future Directions.pdf

Large language models (LLMs) have become core components of cloud-based intelligent services in academia and industry, yet their training and deployment are hindered by high computational costs, data centralization, and privacy concerns. Federated learning (FL) offers a decentralized training paradigm that enables clients to collaboratively train a learning model without sharing raw data, making it a promising solution for privacy-preserving LLM training and reasoning. This paper presents a comprehensive survey of federated prompt learning (FPL) to review recent advances in integrating the federated learning paradigm and large language models, answering the following research questions: RQ1: The fundamental motivations, characteristics, and enabling technologies of FPL, and how it differs from conventional FL and full-model federated fine-tuning; RQ2: The trade-offs FPL approaches exhibit in performance, communication efficiency, computational overhead, scalability, personalization, and heterogeneity handling; RQ3: The remaining security, privacy, robustness, and system challenges, along with key future research directions. To this end, we systematically examine existing FPL methods across the full model lifecycle: pre-training, fine-tuning, and practical applications, while discussing security, privacy, and robustness issues and summarizing existing defense mechanisms. Finally, we highlight open challenges and future directions, aiming to help readers understand how the insights drive research in FPL.

## 15. CForce: Boosting Parallel Decoding for dLLMs via Consistency Forcing

- Authors: Yuji Ren, Chenkai Xu, Zhuocheng Gong, Jianguo Li, Zhijie Deng
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-14
- DOI: Unavailable
- Categories: cs.LG, cs.AI, cs.CL
- Relevance: 2.8891492649918646
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.13925v1
- PDF: https://arxiv.org/pdf/2608.13925v1
- Local PDF: pdf/2026-08-18_15_CForce_ Boosting Parallel Decoding for dLLMs via Consistency Forcing.pdf

Diffusion large language models (dLLMs) accelerate language generation by predicting multiple masks in a single forward pass. However, existing dLLMs can suffer from unreliable predictions in early denoising stages under aggressive parallelism strategies, leading to errors that can propagate to later stages. To tackle this issue, we present Consistency Forcing (CForce) for dLLMs, a distillation method to force the mask predictions of early stages to align with those of later stages. CForce trains the model on pre-collected self-rollout trajectories, thereby improving training-inference alignment. We introduce Confidence Adaptive KL Divergence as a distillation objective to conjoin the merits of forward and reverse KL. We further provide a theoretical analysis for the consistency objective to explain why CForce can approximately minimize the prediction error of early stages. Critically, the same formulation applies to both mask-to-token decoding and edit-capable decoding; in the edit-capable case, later token-to-token refinements provide additional supervision for earlier masked-state predictions. Experiments on non-edit and edit-capable LLaDA models show improved speed-quality trade-offs, especially under high-parallelism decoding budgets. Code is available at: https://github.com/inclusionAI/dFactory.

## 16. A Graph-Based Reinforcement Learning Framework for Structured Drift Diagnosis and Recovery in Autonomous LLM Agents

- Authors: Ismail El Hamraoui, Sagar Jose, Nicolas Bureau, Robert Plana
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-14
- DOI: Unavailable
- Categories: cs.AI, cs.LG, cs.MA
- Relevance: 2.88088802629912
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.14109v1
- PDF: https://arxiv.org/pdf/2608.14109v1
- Local PDF: pdf/2026-08-18_16_A Graph-Based Reinforcement Learning Framework for Structured Drift Diagnosis and Recovery in Autonomous LLM Agents.pdf

Autonomous LLM agents are increasingly deployed in complex real-world workflows, yet they remain vulnerable to runtime behavioral drift, a silent deviation from the original task that can lead to irreversible side effects on external systems. Existing approaches address drift at the prompt level but lack structured mechanisms for step-level detection, risk assessment, and recovery decision. Because the main task-executing agent is often a large and expensive model that cannot be re-trained on every deployment, this work targets a plug-and-play recovery module instead. It introduces a graph-based framework in which a single small language model is trained via reinforcement learning to specialize at each node of a recovery graph, external to the main agent. Each node has a precise role\,: drift classification, operation detection, risk evaluation, or final decision and the model learns to produce structured XML-formatted reasoning adapted to that role. Training combines rule-based structural rewards with an LLM-as-judge semantic-quality signal, so that the model is graded both on how it answers (schema and length) and on what it says. Experiments on the public AppWorld benchmark show that the method generally exploits information about the suspected drift onset to issue correct recovery decisions using a small language model. In addition, the trained small language model reliably respects the prescribed output schema and produces semantically appropriate content in each field according to its assigned node role.

## 17. Reaction-Transformation-Aware Flow Matching for Generalizable Transition State Generation

- Authors: Kaipeng Zeng, Wenxi Zhai, Shengrui Xu, Jie Zhao, Bowen Li, Shiyue Wang, Junchi Yan, Tong Zhu
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-14
- DOI: Unavailable
- Categories: physics.chem-ph, cs.AI
- Relevance: 2.875299187607074
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.14076v1
- PDF: https://arxiv.org/pdf/2608.14076v1
- Local PDF: pdf/2026-08-18_17_Reaction-Transformation-Aware Flow Matching for Generalizable Transition State Generation.pdf

Transition-state (TS) structures define the energetic barriers and mechanistic pathways of elementary chemical reactions, yet their identification remains computationally demanding because conventional saddle-point searches require expensive quantum-mechanical calculations. Recent machine-learning approaches have accelerated TS generation by predicting structures from reaction endpoint information, but they primarily learn geometric correspondence between endpoints and TSs, leaving the structural transformations underlying elementary reactions implicitly represented. To address this limitation, we introduce TransTS, a reaction-transformation-aware framework for generalizable TS generation from atom-mapped reactant-product pairs. TransTS explicitly learns atom-level structural transformations between reaction endpoints and integrates them with a unified atom-aligned geometric representation of reactants, TSs and products, enabling reaction-aware equivariant generation of TS geometries. TransTS is designed to provide reliable TS initial guesses for subsequent quantum-chemical refinement, where generated structures are evaluated not only by geometric similarity but also by their ability to converge to validated saddle points and recover the intended reaction pathways. Across IID and zero-shot OOD benchmarks, TransTS demonstrates improved TS initialization quality, with particularly strong generalization to unseen reaction distributions. On the challenging GDB-10-rxn and GDB-17-rxn OOD benchmarks, TransTS generates TS candidates that more frequently converge to validated saddle points and recover the intended elementary reactions after refinement than existing approaches under the same training regime. Scaling reaction coverage and model capacity further improves both geometric fidelity and refinement outcomes.

## 18. Adversarial Learning of Classifier-Free Guidance Schedules

- Authors: Ashwini Pokle, Alexandre Galashov, Arnaud Doucet, Mauricio Delbracio, Valentin De Bortoli
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-14
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 2.8719022414594164
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.14038v1
- PDF: https://arxiv.org/pdf/2608.14038v1
- Local PDF: pdf/2026-08-18_18_Adversarial Learning of Classifier-Free Guidance Schedules.pdf

Modern text-to-image diffusion models rely on classifier-free guidance (CFG) to achieve high image fidelity and text alignment. However, CFG typically applies a static, global scale across all timesteps, samples, and conditions -- a choice that is generally suboptimal and can introduce artifacts, as different states may benefit from different levels of guidance. While time-varying schedules are known to improve quality, designing them by hand is non-trivial and application-dependent. In this paper, we learn the guidance schedule as a function of diffusion time, conditioning and the current noisy sample, in order to better align sampled images with the text prompt. We frame this as a density ratio estimation problem: a discriminator is trained to estimate the time-dependent log-density ratio between the true and guided marginal distributions, while a lightweight generator network predicts the optimal, state-dependent guidance scale. Empirically, our approach outperforms both heuristic CFG schedules and prior methods for learning dynamic guidance on text-to-image generation benchmarks.

## 19. Catching the Imposter: Self-Supervised Learning of Physical Coherence with Cross-Entity Feature Permutations

- Authors: Aleksei Rozanov, Arvind Renganathan, Vipin Kumar
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-14
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 2.8489422897305063
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.14372v1
- PDF: https://arxiv.org/pdf/2608.14372v1
- Local PDF: pdf/2026-08-18_19_Catching the Imposter_ Self-Supervised Learning of Physical Coherence with Cross-Entity Feature Permutations.pdf

Scientific data often describe entities whose features are jointly governed by the laws of physics, yet existing self-supervised learning (SSL) objectives largely ignore this physical coherence. We introduce imposter, a discriminative pretext task that replaces subsets of an entity's features with real observations donated by another entity and trains the encoder to identify the swapped features. Because every donated value is individually plausible, the task can only be solved by learning cross-feature physical dependencies. We evaluate the proposed objectives on global ERA5-Land reanalysis data using 21 environmental variables and assess the learned representations on seven downstream tasks spanning climate classification, carbon flux estimation, and streamflow prediction. Our study includes, to our knowledge, the first systematic comparison of self-supervised objectives for land-surface modeling under a shared architecture and pre-training budget. We find that the most effective pretext task depends on the downstream task family rather than any single objective's superiority, and that imposter provides complementary information when combined with existing SSL objectives. These results suggest that physical coherence is a valuable new source of self-supervision for scientific foundation models.

## 20. Integration of proteomic data from cell lines and tumors

- Authors: Ta, C. Q., Auth, J. M., Schilling, M., Klingmueller, U., Raue, A.
- Source: biorxiv
- Venue type: preprint
- Journal: biorxiv
- Publication status: preprint
- Publication date: 2026-08-17
- DOI: 10.64898/2026.08.11.743858
- Categories: bioinformatics
- Relevance: 2.8348445450745388
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://www.biorxiv.org/content/10.64898/2026.08.11.743858v1.full.pdf
- PDF: https://www.biorxiv.org/content/10.64898/2026.08.11.743858v1.full.pdf
- Local PDF: Not downloaded

Cancer cell lines are widely used in preclinical research, yet the clinical translation of findings from cell lines remains limited. Identifying cell lines that best resemble patient tumors requires integration of molecular profiles across biologically distinct sample types. Recent advances in transcriptomic integration have demonstrated the potential of deep learning for aligning data across different sample types. However, comparable approaches for proteomic data integration remain lacking, potentially because of the prevalence of missing values in proteomic datasets. Here, we introduce ProtInt, a deep learning-based framework that integrates proteomic data from cell lines and patient tumors by combining principles from proteomic imputation and transcriptomic integration methods. We applied ProtInt to integrate label-free proteomic profiles from 771 cancer cell lines and 550 treatment-naive tumors. ProtInt outperformed batch correction and transcriptomic integration methods in aligning cell line and tumor proteomes. Comparison of the cell line proteomes before and after integration revealed recurrent increase of proteins associated with immune reaction, cell-cell communication, and interaction with the extracellular matrix, and reduction of proteins involved in transcription, post-transcriptional processing, and mitochondrial gene expression as proteomes of cell lines were adapted to resemble tumors. These results establish ProtInt as a framework for joint analysis of proteomic datasets across distinct sample types and may facilitate the identification of cell lines best suited for clinically relevant studies.

## 21. Generation-Powered Inference for Distribution-Valued Outcomes

- Authors: Yijiao Zhang, Hongzhe Li
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-08-14
- DOI: Unavailable
- Categories: stat.ME, stat.ML
- Relevance: 2.8248159752779833
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2608.14542v1
- PDF: https://arxiv.org/pdf/2608.14542v1
- Local PDF: pdf/2026-08-18_21_Generation-Powered Inference for Distribution-Valued Outcomes.pdf

Modern generative models increasingly produce distribution-valued outputs, such as predicted cellular responses to genetic perturbations in single-cell genomics. While these models provide valuable auxiliary information, they are inherently imperfect, creating a need for statistical methods that leverage their predictions without relying on their correctness. We propose generation-powered inference (GPI), a general framework for improving inference on distribution-valued parameters using auxiliary generative models. Focusing on Wasserstein barycenters and related distributional functionals, we introduce a function-valued bridge representation that transforms inference in the nonlinear Wasserstein space into estimation of a mean function in a Hilbert space, enabling an augmented estimation framework analogous to prediction-powered inference. We develop a family of GPI estimators with optimal information borrowing, establish consistency, asymptotic normality, and simultaneous confidence bands, and derive valid inference for linear functionals and Wasserstein distances. Simulation studies demonstrate efficiency gains over labeled-data-only methods and robust performance under generative model misspecification. We illustrate the proposed framework using a Perturb-seq study of K562 cells, where synthetic perturbation responses generated by the State foundation model are used to improve inference for pathway-level consensus gene expression distributions associated with perturbations of the 40S ribosome module.

## 22. AMA: Adaptive Memory via Multi-Agent Collaboration

- Authors: Weiquan Huang, Zixuan Wang, Hehai Lin, Sudong Wang, Bo Xu, Qian Li, Beier Zhu, Linyi Yang, Chengwei Qin
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.773865315720154
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.152/
- PDF: https://aclanthology.org/2026.findings-acl.152.pdf
- Local PDF: pdf/2026-08-18_22_AMA_ Adaptive Memory via Multi-Agent Collaboration.pdf

The rapid evolution of Large Language Model (LLM) agents has necessitated robust memory systems to support cohesive long-term interaction and complex reasoning. Benefiting from the strong capabilities of LLMs, recent research focus has shifted from simple context extension to the development of dedicated agentic memory systems. However, existing approaches typically rely on rigid retrieval granularity, accumulation-heavy maintenance strategies, and coarse-grained update mechanisms. These design choices create a persistent mismatch between stored information and task-specific reasoning demands, while leading to the unchecked accumulation of logical inconsistencies over time. To address these challenges, we propose Adaptive Memory via Multi-Agent Collaboration (AMA), a novel framework that leverages coordinated agents to manage memory across multiple granularities. AMA employs a hierarchical memory design that dynamically aligns retrieval granularity with task complexity. Specifically, the Constructor and Retriever jointly enable multi-granularity memory construction and adaptive query routing. The Judge verifies the relevance and consistency of retrieved content, triggering iterative retrieval when evidence is insufficient or invoking the Refresher upon detecting logical conflicts. The Refresher then enforces memory consistency by performing targeted updates or removing outdated entries. Extensive experiments on challenging long-context benchmarks show that AMA significantly outperforms state-of-the-art baselines while reducing token consumption by approximately 80% compared to full-context methods, demonstrating its effectiveness in maintaining retrieval precision and long-term memory consistency.

## 23. ChemAmp: Amplified Chemistry Tools via Composable Agents

- Authors: Zhucong Li, Powei Chang, Jin Xiao, Zhijian Zhou, Qianyu He, Jiaqing Liang, Fenglei Cao, Xu Yinghui, Yuan Qi
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.773389853160815
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.52/
- PDF: https://aclanthology.org/2026.findings-acl.52.pdf
- Local PDF: pdf/2026-08-18_23_ChemAmp_ Amplified Chemistry Tools via Composable Agents.pdf

Although LLM-based agents are proven to master tool orchestration in scientific fields, particularly chemistry, their single-task performance remains limited by underlying tool constraints. To this end, we propose tool amplification, a novel paradigm that enhances the collective capabilities of specialized tools through optimized, dynamic coordination within individual tasks. Instantiating this paradigm, we introduce ChemAmp, a computationally lightweight framework that dynamically treats chemistry tools (e.g., UniMol2, Chemformer) as composable building-block agents. It constructs task-specialized super-agents that transcend atomic tool constraints with limited data (≤10 samples). Our evaluations across four core chemistry tasks molecular design, molecule captioning, reaction prediction, and property prediction demonstrate that ChemAmp outperforms chemistry-specialized models, generalist LLMs, and agent systems with tool orchestration. Critically, this bottom-up construction strategy enables 94% inference token cost reductions versus vanilla multi-agent systems.

## 24. Decoding the Multimodal Mind: Generalizable Brain-to-Text Translation via Multimodal Alignment and Adaptive Routing

- Authors: Chunyu Ye, Yunhao Zhang, Jingyuan Sun, Chong Li, Yang Zhao, Shaonan Wang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.7721769444406794
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1131/
- PDF: https://aclanthology.org/2026.findings-acl.1131.pdf
- Local PDF: pdf/2026-08-18_24_Decoding the Multimodal Mind_ Generalizable Brain-to-Text Translation via Multimodal Alignment and Adaptive Routing.pdf

Decoding language from the human brain remains a grand challenge for Brain-Computer Interfaces (BCIs). Current approaches typically rely on unimodal brain representations, neglecting the brain’s inherently multimodal processing. Inspired by the brain’s associative mechanisms, where viewing an image can evoke related sounds and linguistic representations, we propose a unified framework that leverages Multimodal Large Language Models (MLLMs) to align brain signals with a shared semantic space encompassing text, images, and audio. A router module dynamically selects and fuses modality-specific brain features according to the characteristics of each stimulus. Experiments on various fMRI datasets with textual, visual, and auditory stimuli demonstrate state-of-the-art performance, achieving an 8.48% average improvement on the most commonly used benchmark. We further extend our framework to EEG and MEG data, demonstrating flexibility and robustness across varying temporal and spatial resolutions. To our knowledge, this is the first unified BCI architecture capable of robustly decoding multimodal brain activity across diverse brain signals and stimulus types, offering a flexible solution for real-world applications.

## 25. Follow the Flow: On Information Flow Across Textual Tokens in Text-to-Image Models

- Authors: Guy Kaplan, Michael Toker, Yuval Reif, Yonatan Belinkov, Roy Schwartz
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.771049845089398
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1575/
- PDF: https://aclanthology.org/2026.acl-long.1575.pdf
- Local PDF: pdf/2026-08-18_25_Follow the Flow_ On Information Flow Across Textual Tokens in Text-to-Image Models.pdf

Text-to-image generation models suffer from alignment problems, where generated images fail to accurately capture the objects and relations in the text prompt. Prior work has focused on improving alignment by refining the diffusion process, ignoring the role of the text encoder, which guides the diffusion. In this work, we investigate how semantic information is distributed across token representations in text-to-image prompts, analyzing it at two levels: (1) in-item representation—whether individual tokens represent their lexical item (i.e., a word or expression conveying a single concept), and (2) cross-item interaction—whether information flows between tokens of different lexical items. We use patching techniques to uncover encoding patterns, and find that information is usually concentrated in only one or two of the item’s tokens; for example, in the item “San Francisco’s Golden Gate Bridge”, the token “Gate” sufficiently captures the entire expression while the other tokens could effectively be discarded. Lexical items also tend to remain isolated; for instance, in the prompt “a green dog”, the token “dog” encodes no visual information about “green”. However, in some cases, items do influence each other’s representation, often leading to misinterpretations—e.g., in the prompt “a pool by a table”, the token “pool” represents a “pool table” after contextualization. Our findings highlight the critical role of token-level encoding in image generation, and demonstrate that simple interventions at the encoding stage can substantially improve alignment and generation quality.

## 26. KnowledgeBerg: Evaluating Systematic Knowledge Coverage and Compositional Reasoning in Large Language Models

- Authors: Xiao Zhang, Qianru Meng, Yongjian Chen, Yumeng Wang, Johan Bos
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.7707856022292203
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.548/
- PDF: https://aclanthology.org/2026.findings-acl.548.pdf
- Local PDF: pdf/2026-08-18_26_KnowledgeBerg_ Evaluating Systematic Knowledge Coverage and Compositional Reasoning in Large Language Models.pdf

Many real-world questions appear deceptively simple yet implicitly demand two capabilities: (i) systematic coverage of a bounded knowledge universe and (ii) compositional set-based reasoning over that universe, a phenomenon we term “the tip of the iceberg.” We formalize this challenge through two orthogonal dimensions: knowledge width, the cardinality of the required universe, and reasoning depth, the number of compositional set operations. We introduce KnowledgeBerg, a benchmark of 4,800 multiple-choice questions derived from 1,183 enumeration seeds spanning 10 domains and 17 languages, with universes grounded in authoritative sources to ensure reproducibility. Representative open-source LLMs demonstrate severe limitations, achieving only 5.26–36.88 F1 on universe enumeration and 16.00–44.19 accuracy on knowledge-grounded reasoning. Diagnostic analyses reveal three stages of failure: completeness, or missing knowledge; awareness, or failure to identify requirements; and application, or incorrect reasoning execution. This pattern persists across languages and model scales. Although test-time compute and retrieval augmentation yield measurable gains—up to 4.35 and 3.78 points, respectively—substantial gaps remain, exposing limitations in how current LLMs organize structured knowledge and execute compositional reasoning over bounded domains. The dataset is available at https://huggingface.co/datasets/2npc/KnowledgeBerg

## 27. Temporal Sampling for Forgotten Reasoning in LLMs

- Authors: Yuetai Li, Zhangchen Xu, Fengqing Jiang, Bhaskar Ramasubramanian, Luyao Niu, Bill Yuchen Lin, Xiang Yue, Radha Poovendran
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.770684499714291
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1305/
- PDF: https://aclanthology.org/2026.acl-long.1305.pdf
- Local PDF: pdf/2026-08-18_27_Temporal Sampling for Forgotten Reasoning in LLMs.pdf

Fine-tuning large language models (LLMs) is intended to improve their reasoning capabilities, yet we uncover a counterintuitive effect: models often forget how to solve problems they previously answered correctly during training. We term this phenomenon Temporal Forgetting and show that it is widespread across model sizes, fine-tuning methods (both Reinforcement Learning and Supervised Fine-Tuning), and multiple reasoning benchmarks. Our analysis reveals on average more than 20% of final errors were once solved correctly at an earlier checkpoint. Inspired by the phenomenon of Temporal Forgetting, we proposed Temporal Sampling, a simple decoding strategy that draws outputs from multiple checkpoints along the training trajectory. This approach recovers forgotten solutions and leads to significant improvements in reasoning performance than final-ckpt-sampling only, gains from 4 to 19 points in Pass@k and consistent gains for majority-voting and Best-of-N across several benchmarks. Temporal sampling also outperforms strong baselines such as model merging. By leveraging the temporal diversity inherent in training, Temporal Sampling offers a practical, compute-efficient way to surface hidden reasoning ability and rethink how we evaluate LLMs.

## 28. From Documents to Segments: A Contextual Reformulation for Topic Assignment

- Authors: Hoonsang Yoon, Takyoung Kim, Wonkee Lee, Ilmin Cho, Dilek Hakkani-Tür, Stanley Jungkyu Choi
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.77043048159363
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1278/
- PDF: https://aclanthology.org/2026.findings-acl.1278.pdf
- Local PDF: pdf/2026-08-18_28_From Documents to Segments_ A Contextual Reformulation for Topic Assignment.pdf

Traditional topic modeling treats each document as a single, coherent unit of topic, which can cause topic contamination when documents cover multiple topics. This becomes especially problematic when stakeholders are interested in identifying documents that focus on a specific topic. We introduce segment-based topic allocation, a novel paradigm that redefines topic assignment at the level of segments, coherent textual spans conveying distinct topical content. This granularity improves topic purity, interpretability, and applicability to multi-theme corpora such as reviews or survey responses. To support this paradigm, we construct SemEval-STM, a benchmark derived from aspect-based sentiment datasets, where segments are automatically extracted using large language models (LLMs) and post-processed with human supervision. We further propose the segment intrusion task (SIT), a novel evaluation method extending word intrusion to the span level, enabling human-centric assessment of topical coherence. Empirical results across diverse metrics and models demonstrate that SBTA significantly outperforms traditional document-based methods in clustering and interpretability. Our framework provides a practical and scalable solution for fine-grained topic analysis in heterogeneous text corpora.

## 29. LaMPE: Length-aware Multi-grained Positional Encoding for Adaptive Long-context Scaling Without Training

- Authors: Sikui Zhang, Guangze Gao, Ziyun Gan, Chunfeng Yuan, Zefeng Lin, Houwen Peng, Bing Li, Weiming Hu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.770300530541268
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1608/
- PDF: https://aclanthology.org/2026.findings-acl.1608.pdf
- Local PDF: pdf/2026-08-18_29_LaMPE_ Length-aware Multi-grained Positional Encoding for Adaptive Long-context Scaling Without Training.pdf

Large language models (LLMs) experience significant performance degradation when the input exceeds the pretraining context window, primarily due to the out-of-distribution (OOD) behavior of Rotary Position Embedding (RoPE). Recent studies mitigate this problem by remapping OOD positions into the in-distribution range with fixed mapping strategies, ignoring the dynamic relationship between input length and the model’s effective context window. To this end, we propose Length-aware Multi-grained Positional Encoding (LaMPE), a training-free method that fully utilizes the model’s effective context window for adaptive long-context scaling in LLMs. Motivated by the left-skewed frequency distribution of relative positions, LaMPE establishes a dynamic relationship between mapping length and input length through a parametric scaled sigmoid function to adaptively allocate positional capacity across varying input lengths. Meanwhile, LaMPE devises a novel multi-grained attention mechanism that strategically allocates positional resolution across different sequence regions to capture both fine-grained locality and long-range dependencies. Our method can be seamlessly applied to a wide range of RoPE-based LLMs without training. Extensive experiments on three representative LLMs across five mainstream long-context benchmarks demonstrate that LaMPE achieves significant performance improvements compared to existing length extrapolation methods.

## 30. ANCHOR: LLM-driven Subject Conditioning for Text-to-Image Synthesis

- Authors: Aashish Anantha Ramakrishnan, Sharon X Huang, Dongwon Lee
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.769334636602637
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.30/
- PDF: https://aclanthology.org/2026.findings-acl.30.pdf
- Local PDF: pdf/2026-08-18_30_ANCHOR_ LLM-driven Subject Conditioning for Text-to-Image Synthesis.pdf

Text-to-image (T2I) models have achieved remarkable progress in high-quality image synthesis, yet most benchmarks rely on simple, self-contained prompts, failing to capture the complexity of real-world captions. Human-written captions often involve multiple interacting subjects, rich contextual references, and abstractive phrasing, conditions under which current image-text encoders like CLIP struggle. To systematically study these deficiencies, we introduce ANCHOR, a large-scale dataset of 70K+ abstractive captions sourced from five major news media organizations. Analysis with ANCHOR reveals persistent failures in multi-subject understanding, context reasoning, and nuanced grounding. Motivated by these challenges, we propose Subject-Aware Fine-tuning (SAFE), which uses Large Language Models (LLMs) to extract key subjects and enhance their representation at the embedding-level. Experiments with contemporary models show that SAFE significantly improves image-caption consistency and human preference alignment, serving as a practical and scalable solution. The dataset and code will be released upon publication.
