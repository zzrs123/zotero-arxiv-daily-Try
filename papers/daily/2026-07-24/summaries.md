# Paper Daily Reading - 2026-07-24

## 1. HyGRL: Adaptive Hybrid Graph Reasoning for Multi-Entity Questions

- Authors: Junyi Wang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-04
- DOI: Unavailable
- Categories: cs.AI, cs.CL
- Relevance: 3.427162657086181
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.19398v1
- PDF: https://arxiv.org/pdf/2607.19398v1
- Local PDF: pdf/2026-07-24_01_HyGRL_ Adaptive Hybrid Graph Reasoning for Multi-Entity Questions.pdf

Multi-entity compositional questions pose significant challenges to existing retrieval-augmented language models. Conventional methods fall into a dilemma: standard RAG lacks dynamic reasoning, traditional Graph-RAG is limited by structural sparsity, and LLM-constructed Graph-RAG incurs prohibitive costs. We propose \textbf{\fwa}, a unified framework that embeds unstructured text into structured knowledge graphs, creating a heterogeneous network for flexible evidence retrieval. Reasoning is formulated as adaptive structure induction, learned via a robust two-stage process: (1) imitation learning distills heuristic expert signals, and (2) reinforcement learning refines the policy using LLM-driven preference rewards. Experiments demonstrate that {\fwa} effectively merges textual richness with structural knowledge, outperforming SOTA baselines in answer accuracy and reasoning fidelity while maintaining extremely low token costs and near real-time inference((code available at https://github.com/wjywjy123/HyGRL) .

## 2. Causal dictionary learning reveals and validates transcription-factor binding features in genomic language models

- Authors: Sarwan Ali
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-21
- DOI: Unavailable
- Categories: q-bio.GN, cs.AI, cs.LG
- Relevance: 3.3840513204836418
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.19618v1
- PDF: https://arxiv.org/pdf/2607.19618v1
- Local PDF: pdf/2026-07-24_02_Causal dictionary learning reveals and validates transcription-factor binding features in genomic language models.pdf

Genomic language models achieve strong performance across regulatory-genomics tasks, yet what these models internally represent remains opaque, and the field lacks a principled procedure for verifying that an apparent ``concept'' inside a model is real rather than an artifact of sequence composition. We introduce a framework that combines sparse dictionary learning with causal intervention to extract, validate, and causally test interpretable features in genomic foundation models. Training top-$k$ sparse autoencoders on the hidden activations of two architecturally distinct models, Nucleotide Transformer ($6$-mer tokenization) and DNABERT-2 (byte-pair encoding), we recover thousands of monosemantic features that map to transcription-factor (TF) sequence motifs. We show that the naive validation of such features against position weight matrices is severely confounded by GC composition and repetitive elements, producing hundreds of spurious ``TF features'', and we develop a composition-matched, binding-resolved protocol that removes these confounds. Critically, we move beyond correlation: by ablating individual dictionary directions during the model's forward pass and measuring the induced shift in the model's own predictive distribution, we establish that specific features are \emph{causally} used to represent cell-type-specific TF binding, not merely motif presence. Across three transcription factors (CTCF, GATA1, REST) and both architectures, causally validated binding features emerge reproducibly ($7$--$14$ of $15$ tested features per condition), while two classes of negative control, scrambled binding labels and randomly selected features, yield no detectable signal. The framework is purely computational, uses only public data, and provides a reusable standard for interpretability claims in genomic deep learning.

## 3. Plausibility-Driven Prioritization of Candidate Biomedical Annotations

- Authors: Emanuele Cavalleri, Miad Alavinezhad, Dario Malchiodi, Marco Mesiti
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-22
- DOI: Unavailable
- Categories: q-bio.QM, cs.DB, cs.LG
- Relevance: 3.340812140923288
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.20163v1
- PDF: https://arxiv.org/pdf/2607.20163v1
- Local PDF: pdf/2026-07-24_03_Plausibility-Driven Prioritization of Candidate Biomedical Annotations.pdf

The rapid growth of biomedical knowledge has made the validation of automatically generated biological annotations a major bottleneck in biomedical curation. While computational methods can rapidly produce large numbers of candidate annotations, determining which are biologically valid still requires costly expert review. Prioritizing these candidates before manual curation has therefore become a fundamental challenge. Machine learning techniques can support this process by exploiting biomedical knowledge graphs (bioKGs), which capture biological entities and their functional associations. In this work, we propose a framework that leverages bioKGs to estimate the plausibility of candidate annotations and guide expert curation. Starting from knowledge graph embeddings, we train relation-specific binary classifiers using a community-based negative sampling strategy to obtain reliable confidence estimates. We then introduce a family of plausibility measures that combine classifier confidence, classifier reliability, and the semantic context provided by alternative relationships involving the same pair of biological entities. Unlike conventional confidence estimation, the proposed approach explicitly accounts for multiple biologically meaningful relations that may coexist between the same entities. Experimental results on five large bioKGs demonstrate that the proposed negative sampling strategy consistently improves classifier robustness, increasing balanced accuracy by an average of 5.8%. Moreover, the plausibility measures outperform classifier confidence alone, enabling more effective prioritization of candidate annotations for expert review. Overall, our results show that the use of bioKGs improves the efficiency of AI-assisted biomedical curation while preserving expert control over the final annotation assessment.

## 4. Local Causal Structure Learning in the Presence of Latent Variables and Selection Bias

- Authors: Zheng Li, Hao Zhang, Ruxin Wang, Ruichu Cai, Kun Zhang, Feng Xie
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-22
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.3091146387890555
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.19866v1
- PDF: https://arxiv.org/pdf/2607.19866v1
- Local PDF: pdf/2026-07-24_04_Local Causal Structure Learning in the Presence of Latent Variables and Selection Bias.pdf

Discovering the direct causes and effects of a target variable from observational data is a fundamental problem in causal discovery, with broad applications in domains such as gene regulatory analysis and biomedical research. Existing causal discovery methods either learn a global causal structure, which incurs substantial computational cost, or assume the absence of latent variables and selection bias, assumptions that are often violated in real-world settings. Motivated by these challenges, we study local causal structure learning in the presence of latent variables and selection bias. Specifically, we first characterize a local region that enables target-specific causal discovery without recovering the entire global structure. We then establish a theoretical bridge between causal information learned from the observed distribution induced on this local region and the corresponding information in the global causal structure. Building on these foundations, we propose LoCaLS, a local causal structure learning algorithm that is sound and complete under standard assumptions and identifies the same direct causes and effects of a target variable as those identifiable by global causal discovery methods, while allowing for latent variables and selection bias. Extensive experiments on random and real-world structures demonstrate that the proposed method consistently achieves higher structural accuracy than existing local methods while requiring substantially less computational effort than state-of-the-art global methods. Furthermore, applications to two real-world gene expression datasets reveal biologically plausible target-specific causal structures, demonstrating its practical applicability in large-scale biological data analysis.

## 5. Profile-Graph Memory for LLM Agents: Implicit Cross-Entity Traversal through Narrative Profiles

- Authors: Shengtong Zhu
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-06-01
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 3.2826080003729903
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.19359v1
- PDF: https://arxiv.org/pdf/2607.19359v1
- Local PDF: pdf/2026-07-24_05_Profile-Graph Memory for LLM Agents_ Implicit Cross-Entity Traversal through Narrative Profiles.pdf

Long-term memory is essential for LLM agents that interact across sessions, yet current memory benchmarks primarily evaluate single-hop recall, leaving multi-hop association largely unmeasured. We make three contributions. First, we introduce MemHop, a multi-hop memory benchmark of 1,000 questions at hop depths 1-5 across 10 social-network scenarios, with per-hop evidence annotations. Second, we present Profile-Graph Memory (ProGraph), a two-layer memory architecture combining (i) profile expansion -- substring-matched traversal of entity names that naturally appear in LLM-written profile narratives, a minimal alternative to explicit knowledge-graph construction -- and (ii) compression residuals -- exact dates, quantities, and named items co-extracted with each profile update at zero extra API cost. Third, a full-grid ablation shows cross-benchmark mechanism specialization: profile expansion drives multi-hop reasoning (-22.6pp on MemHop when removed) while compression residuals drive precision recall (-8.6pp on LoCoMo when not co-extracted), with cross-effects under 3pp within a single architecture. ProGraph averages 80.1% on MemHop (matching the FullContext reference) and 78.4% on LoCoMo (exceeding FullContext by 11.3pp), outperforming Mem0, A-Mem, HippoRAG, and RAG on both. We release MemHop, ProGraph, and baseline implementations.

## 6. The Giant Hippocampus: From Structural Monoculture to a System of Systems

- Authors: Jaeho Seol
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-22
- DOI: Unavailable
- Categories: cs.AI, cs.LG, cs.NE, q-bio.NC
- Relevance: 3.240323918673276
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.19973v1
- PDF: https://arxiv.org/pdf/2607.19973v1
- Local PDF: pdf/2026-07-24_06_The Giant Hippocampus_ From Structural Monoculture to a System of Systems.pdf

AI researchers describe state-of-the-art models as one thing repeated at scale: the Transformer, wired identically for text, pixels, or speech. Neuroscientists describe the cortex as a mosaic - dense Layer 4 in visual cortex for spatial encoding, thick Layers 5/6 in motion cortex for temporal integration - different jobs solved by different structures. This paper argues the gap is a structural error, not a stylistic one, and is measurable. A century of cytoarchitecture, from Brodmann to single-cell Patch-seq, shows distinct cognitive functions are implemented by qualitatively different structures, not by rescaling one template. The convolutional neural network is the field's own proof: local receptive fields and hierarchical depth encoded this prior directly, reaching strong image recognition on far less data than later architectures needed. The paper traces how this lesson was discarded: the "Hardware Lottery" made the Transformer the path of least resistance, not the principled choice, and Mixture-of-Experts, often cited as diversity, in fact partitions parameters among identical experts. A functionalist analysis shows the Transformer is best understood as a functional analog of the hippocampal formation, not a general-purpose cortex - the same mistake as treating cortex as one giant Broca's area, except the field has now standardized on a giant hippocampus, applied to tasks it was never built for: audition, executive gating, working memory. The paper closes with an alternative: a Heterogeneous Topological Network, a System of Systems in which distinct modules keep the inductive bias their computation demands and communicate through standardized interfaces. This is a design discipline for AI architects, not cognitive science: specify modularity before training, using structural evidence as a design input rather than reverse-engineering architecture from a trained model's behavior.

## 7. Predictive single cell foundation model for gene regulation and aging with privacy-preserving tabular learning

- Authors: Jiayuan Ding, Jianhui Lin, Ziyang Miao, Nils Mechtel, Shiyu Jiang, Yixin Wang, Zhaoyu Fang, Jorge D. Martin-Rufino, Chen Weng, Reuben Saunders, Weize Xu, Jonathan S. Weissman, Min Li, Jiliang Tang, Wei Ouyang, Yuancheng Ryan Lu, Xiaojie Qiu
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-06
- DOI: Unavailable
- Categories: cs.LG, q-bio.GN
- Relevance: 3.239445834372861
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.19400v1
- PDF: https://arxiv.org/pdf/2607.19400v1
- Local PDF: pdf/2026-07-24_07_Predictive single cell foundation model for gene regulation and aging with privacy-preserving tabular learning.pdf

Pre-trained foundation models (FMs) have begun transforming single-cell genomics, but scaling them raises privacy concerns. Moreover, unlike text data, single-cell data is unordered and exhibits a unique tabular structure that current single-cell FMs overlook. We introduce Tabula, a privacy-preserving FM designed with federated learning (FL) that explicitly models the tabular structure of single-cell data. To deploy Tabula, we further developed Chiron, a decentralized AI agent-enabled platform for collaborative training across institutions without sharing raw data. Beyond strong performance across downstream benchmarks, Tabula reveals combinatorial regulatory logic across diverse biological systems, including hematopoiesis, pancreatic endogenesis, neurogenesis, and cardiogenesis. Using a new scRNA-seq dataset of paired young and aged human fibroblasts, Tabula nominates rejuvenation factors through age- and identity score-guided in silico prioritization, outperforming conventional approaches. Thus, Tabula represents an important advance in single-cell foundation modeling by integrating tabular learning with FL, paving the way toward privacy-preserving virtual cells for human health.

## 8. FedLSG: LLM-Enhanced Semantic Calibration for Federated Graph Backdoor Defense

- Authors: Chenyu Zhou, Yabin Peng, Wei Huang, Kunlin Li, Shuaishuai Zhang, Xinyuan Miao
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-22
- DOI: Unavailable
- Categories: cs.CR, cs.AI, cs.LG
- Relevance: 3.2030009810085924
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.19674v1
- PDF: https://arxiv.org/pdf/2607.19674v1
- Local PDF: pdf/2026-07-24_08_FedLSG_ LLM-Enhanced Semantic Calibration for Federated Graph Backdoor Defense.pdf

Federated Graph Neural Networks (FedGNNs) are highly vulnerable to backdoor poisoning, yet existing defenses typically rely on rule-based approaches that lack semantic understanding, making them vulnerable to stealthy triggers and harmful to benign structures. To solve this, we present FedLSG, the first framework that integrates large language models (LLMs) into federated graph backdoor defense. FedLSG introduces a graph and behavior to text grounding scheme that transforms local graph structures and client update behaviors into semantically rich natural language representations. The framework further adopts a lightweight student-teacher architecture. On the server side, a full scale LLM serves as a teacher, providing global contextual guidance and evaluating client updates during aggregation to identify potentially malicious participants. On the client side, a LoRA-based student is maintained to perform semantic reasoning, to suppress the influence of edges associated with backdoor triggers. By enabling semantic interpretation of both graph patterns and client behaviors, the framework adaptively incorporates rule-based signals into message passing and client aggregation for defense. Experiments demonstrate that FedLSG significantly improves resistance to backdoor attacks without compromising graph integrity.

## 9. Making Single-Cell Data Distillation Auditable: Traceable Real-Cell Coresets via Discrete Min-Max Selection

- Authors: Yaodi Luo, Peize He, Bowen Han, Lingbei Mengg
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-20
- DOI: Unavailable
- Categories: q-bio.GN, cs.AI, cs.LG
- Relevance: 3.192051066681127
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.19426v1
- PDF: https://arxiv.org/pdf/2607.19426v1
- Local PDF: pdf/2026-07-24_09_Making Single-Cell Data Distillation Auditable_ Traceable Real-Cell Coresets via Discrete Min-Max Selection.pdf

Single-cell datasets are increasingly costly to store, audit, and reuse for model training. Dimensionality reduction and dataset distillation can reduce this burden, but conventional distillation methods often produce synthetic expression profiles that cannot be traced to an assayed cell. We formulate traceable single-cell data distillation as retaining original cell identifiers and gene symbols under fixed cell and gene budgets. The resulting training subset remains connected to measured counts, labels, and assay metadata, so unexpected predictions can be checked against their source data. We propose two real-cell selectors. Fixed-CF uses static characteristic-function matching. Minmax-CF solves an entropy-regularized discrete min--max problem that upweights poorly preserved directions and adds only observed cells. Across donor-, technology-, and perturbation-level shifts on three datasets, Minmax-CF retains 96.52% of Full balanced accuracy on MS, approximately matches Full on average on hPancreas with a median $2.55\times$ GPU speedup in the all-gene setting, and obtains the lowest pathway error among compressed methods on Norman. Performance remains weaker for rare states, some technology shifts, unseen perturbation components, and settings where fidelity is weakly associated with downstream utility. Because the selected IDs refer to measured cells, these cases can be investigated by inspecting the corresponding training support, labels, and assay metadata. Minmax-CF consistently reduces worst-direction discrepancy, while downstream utility and cost vary across datasets and tasks.

## 10. Lifted Representation Hypothesis in Language Models

- Authors: Bumjin Park, Jaesik Choi
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-06-02
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 3.1761372632135245
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.19360v1
- PDF: https://arxiv.org/pdf/2607.19360v1
- Local PDF: pdf/2026-07-24_10_Lifted Representation Hypothesis in Language Models.pdf

Large language models (LLMs) often answer queries by mapping individual observations to more general rule-like structures. However, it remains unclear how these structures are stored, selected, and revised. To study this process, we propose thelifted representation hypothesis: LLMs update memory through shared latent structures rather than isolated instance-level facts. This view frames lifting as an efficient use of symmetry across instances, and shattering as the refinement of coarse lifted structures into more specific subtypes. We evaluate LLMs' lifting and shattering through controlled exception-learning experiments across in-context learning, LoRA, and full fine-tuning. We find that LLMs are vulnerable to shattering failures when data are governed by nested rules and exceptions, while lifting often occurs prematurely. These results highlight the need to study the relation between data and rule structures in LLMs.

## 11. The Mechanism Matters: When Knowledge Graphs Help Reinforcement Learning

- Authors: Mohammed Sameer Syed
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-21
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.1710790263885267
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.19616v1
- PDF: https://arxiv.org/pdf/2607.19616v1
- Local PDF: pdf/2026-07-24_11_The Mechanism Matters_ When Knowledge Graphs Help Reinforcement Learning.pdf

Knowledge graphs (KGs) are widely used to inject prior knowledge into reinforcement learning (RL), yet the literature is dominated by single-domain, positive-result method papers, so we lack a systematic account of when KG structure helps an agent, when it is neutral, and when it hurts. We conduct a controlled study that independently varies the RL task, the injection mechanism (state features, action masking, or potential-based reward shaping), and KG quality. Using a synthetic, fully controllable KG over MiniGrid environments, we report three findings. First, on compositional sparse-reward tasks structured KG guidance improves sample efficiency and solve reliability (70% to 97% of seeds), and a shuffle control that permutes the KG's edges while preserving their count collapses the benefit toward baseline (masking p=0.0001; shaping p=0.006), so the gain is structural rather than generic regularization. Second, KG value scales with the amount of task-relevant knowledge the graph contains. Third, and most consequential, safety depends on the mechanism: soft, optimality-preserving injection benefits from correct knowledge and harmlessly ignores incorrect knowledge, whereas hard masking is brittle, forbidding essential actions when the KG is incomplete or corrupted and making a wrong KG worse than none. A UMLS-derived clinical case study on sepsis management under offline RL is a careful null, underscoring that benefits require task structure the chosen mechanism can exploit. Our results give practitioners concrete guidance on how, and how much, to trust a KG when using it to guide RL.

## 12. CLARK: Closed-loop Learning for Adaptive Reasoning over Knowledge Graphs

- Authors: Yousef Khan, Luca Gherardini, Marco Maratea, Joel Arrais, Jose Sousa
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-22
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 3.1308297652556636
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.19996v1
- PDF: https://arxiv.org/pdf/2607.19996v1
- Local PDF: pdf/2026-07-24_12_CLARK_ Closed-loop Learning for Adaptive Reasoning over Knowledge Graphs.pdf

Machine Learning models are widely used for automating classification tasks by extracting statistical patterns from data. However, their performance deteriorates if the data distribution changes, making them ill-suited to handle uncertain and evolving information. Moreover, they provide limited support for integrating prior knowledge. To address these limitations, we present CLARK (Closed-loop Learning for Adaptive Reasoning over Knowledge Graphs), a framework that integrates knowledge graphs, symbolic rule mining, and probabilistic reasoning under the Logic Programs with Markov Logic Networks (LP$^{\text{MLN}}$) formalism. Starting from CACTUS-derived KGs, CLARK translates graph structure into an LP$^{\text{MLN}}$ program and iteratively enriches it with candidate rules proposed by symbolic learners. These rules are calibrated through probabilistic weight learning, enabling reasoning under uncertainty and refinement of the underlying graph structure. We evaluate CLARK on two medical datasets, analysing both rule quality and downstream classification performance. Results demonstrate that CLARK leads to improved classification performance and more generalisable inference. Overall, CLARK provides a principled approach to constructing adaptive, interpretable, knowledge-driven models for classification.

## 13. PoTRE: Test-Time Reasoning inspired by Cognitive Heterogeneity

- Authors: Anmol Kankariya, Sercan Ö. Arık
- Source: arxiv
- Venue type: preprint
- Journal: Transactions on Machine Learning Research, 2026
- Publication status: preprint
- Publication date: 2026-07-22
- DOI: Unavailable
- Categories: cs.AI, cs.CL
- Relevance: 3.1302383111744447
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.20268v1
- PDF: https://arxiv.org/pdf/2607.20268v1
- Local PDF: pdf/2026-07-24_13_PoTRE_ Test-Time Reasoning inspired by Cognitive Heterogeneity.pdf

While Large Language Models (LLMs) excel at many tasks, they frequently struggle with complex reasoning that requires long-horizon planning and iterative error correction. Furthermore, standard single-stream prompting proves brittle when models encounter novel abstractions or rigorous domain constraints. We introduce PoTRE (Poly-Topological Reasoning Ensembles), a heterogeneous framework that decouples inference into four agents: (1) Adversarial Refinement Agent, (2) Hierarchical strategic Planning Agent, (3) Spectrum Search Agent, and (4) Direct Chain Agent. A final Task-Adaptive Aggregation Layer dynamically reconciles these perspectives -- via final candidate selection, semantic synthesis, or neuro-symbolic verification -- to produce a robust global solution. We evaluate PoTRE on three frontier benchmarks: ARC-AGI-2, Humanity's Last Exam (HLE), and PRBench Finance. PoTRE achieves state-of-the-art accuracy of 49.92% on HLE, surpassing the previous best official score. We demonstrate that this architectural heterogeneity achieves improved reasoning performance using similar or fewer inference tokens compared to heavily scaled homogeneous baselines.

## 14. SoftReason: A Fully Differentiable Neuro-Soft-Symbolic Deductive Reasoning Architecture over High-Dimensional Perceptual Data

- Authors: Wael AbdAlmageed
- Source: arxiv
- Venue type: preprint
- Journal: Proceedings of Machine Learning Research vol 284:1-2, 2026 20th Conference on Neurosymbolic Learning and Reasoning
- Publication status: preprint
- Publication date: 2026-07-22
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 3.032528204880686
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.20402v1
- PDF: https://arxiv.org/pdf/2607.20402v1
- Local PDF: pdf/2026-07-24_14_SoftReason_ A Fully Differentiable Neuro-Soft-Symbolic Deductive Reasoning Architecture over High-Dimensional Perceptual.pdf

In many reasoning problems, the premises are not observed as discrete symbols, but must be inferred from high-dimensional inputs. Further, the predicate vocabulary, argument structure, and trusted evidence are supplied by a Knowledge Graph (KG), or rule definitions. Classical neuro-symbolic pipelines have a discrete interface between perception and deduction. We present a neuro-soft-symbolic architecture for differentiable deductive reasoning over latent perceptual facts and knowledge-provided predicates. SoftReason removes the gradient gap by representing the deductive state as a local soft interpretation tensor over candidate constants and predicates. Perception proposes probabilistic base facts, KG triples enter as high-confidence soft evidence, and every query anchor, predicate choice, and closure update remains differentiable. Our core innovation is a learned differentiable lift of the immediate-consequence operator. It uses predicate-definition embeddings and latent composition channels to form soft body-predicate mixtures, aggregate over all possible witnesses, propose query-conditioned head facts, and update the interpretation through a monotone probabilistic OR. We instantiate the framework on Knowledge-aware Visual Question Answering (KVQA), and demonstrates how SoftReason supports end-to-end perceptual grounding, KG evidence injection, and differentiable deductive closure in one trainable architecture.

## 15. Efficient Clustering with Provable Guardrails for LLM Inference at Scale

- Authors: Longshaokan Wang, Wai Tsang Keung, Punit Ghodasara, Roman Wang, Ali Dashti, Francesc Moreno-Noguer
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-22
- DOI: Unavailable
- Categories: cs.LG, stat.ML
- Relevance: 3.0164610592189103
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.19704v1
- PDF: https://arxiv.org/pdf/2607.19704v1
- Local PDF: pdf/2026-07-24_15_Efficient Clustering with Provable Guardrails for LLM Inference at Scale.pdf

Scaling LLM-based applications to millions of users is bottlenecked by the inference cost and latency of modern foundation models. A natural fix is to cluster the inputs and call the LLM only on cluster representatives, letting other members inherit the output -- but this is only safe if each member is measurably close to its representative. Existing clustering methods do not offer such per-sample quality control at scale: none jointly guarantee a minimal within-cluster similarity, exact matching of categorical attributes, and scalability to tens of millions of samples. We propose a two-stage algorithm that generates initial clusters with Mini-batch K-Means, then greedily selects representatives within each initial cluster -- a step equivalent to the Johnson-Chvatal heuristic for Set Cover over alpha-balls in embedding space. The algorithm enforces the similarity and attribute guardrails exactly by construction, and runs in $O(nd + n^2 d/K)$ time and $O(nd + n^2/K^2)$ memory for $n$ samples, feature dimension $d$, and $K$ initial clusters -- linear in $n$ when $K$ grows proportionally with $n$. We provide benchmarks against common clustering methods on internal and public datasets: our method not only delivers per-sample guardrails but also runs 10-1000x faster and scales to data sizes where most standard methods become intractable. Deployed on 38 million customers for a persona-based recommender, the clustering method cut downstream cost and latency by 50-fold while preserving personalization and unblocked the production launch.

## 16. Scaling Laws for Hypernetwork-Based Knowledge Injection in Large Language Models

- Authors: Nischay Dhankhar, Dos Baha, Abulhair Saparov
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-21
- DOI: Unavailable
- Categories: cs.CL, cs.LG
- Relevance: 3.0035745143195176
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.19604v1
- PDF: https://arxiv.org/pdf/2607.19604v1
- Local PDF: pdf/2026-07-24_16_Scaling Laws for Hypernetwork-Based Knowledge Injection in Large Language Models.pdf

Injecting factual knowledge into large language models (LLMs) reliably and at scale remains an open challenge. Hypernetworks provide a promising solution to large-scale knowledge injection. Although hypernetworks are typically applied for test-time adaptation, we explore their use in train-time knowledge injection, where, given a large corpus of facts, we train a hypernetwork to generate a fixed LoRA adapter that, when inserted into the target model, enable the model to answer questions about those facts. In this work, we investigate whether hypernetworks can be used to perform train-time knowledge injection and how this ability varies with scale. The scaling behavior of hypernetworks remains largely unstudied. Our design decouples the hypernetwork's injection capacity from the target model's general capability, enabling, for the first time, a rigorous study of scaling laws for hypernetwork architectures. We characterize how loss, reasoning accuracy, and out-of-distribution (OOD) generalization vary with hypernetwork depth, width, and target network size. We construct a large-scale dataset, called MegaWikiQA, containing tens of millions of multi-hop question-answer examples across 39 domains constructed from examples in Wikidata5M. Our results reveal: (i) hypernetwork-based injection exhibits broadly predictive power law scaling along all architecture axes; and (ii) hypernetworks are capable of reliable OOD generalization at increasing scales, suggesting that hypernetwork provides a promising alternative to other train-time adaptation methods such as LoRA finetuning and full fine-tuning, exhibiting steeper scaling exponents in all OOD evaluations. Together, these results establish hypernetworks as a principled and scalable substrate for train-time adaptation, and provide the first empirically grounded scaling laws to guide hypernetworks for factual reasoning in large language models.

## 17. Sentence Splitter: Uncovering Latent Factual Structure for Self-Supervised Learning

- Authors: Ahmad Pouramini, Mahsa Afsharizadeh
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-22
- DOI: Unavailable
- Categories: cs.CL, cs.AI
- Relevance: 2.9955722088582384
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.19845v1
- PDF: https://arxiv.org/pdf/2607.19845v1
- Local PDF: pdf/2026-07-24_17_Sentence Splitter_ Uncovering Latent Factual Structure for Self-Supervised Learning.pdf

This paper introduces Sentence Splitter, a self-supervised framework built upon a T5-based encoder--decoder architecture for uncovering the latent factual structure of natural language sentences. The proposed method identifies the semantic boundary between a descriptive prefix (head) and its factual completion (tail) by formulating sentence splitting as a discrete segmentation problem, where a sentence of length $N$ admits $N$ possible split points but only one recovers the intended head--tail structure. Rather than explicitly searching over all candidate boundaries, the model learns to recover the factual completion through probabilistic sequence generation. To eliminate the need for manual annotation, symbolic head--tail pairs are first verbalized into natural-language templates that provide supervision for training the Sentence Splitter. The trained splitter is then applied to raw text to extract aligned prefix--tail pairs, which are subsequently used to train a generative model that proposes additional plausible completions through a lightweight bootstrapping process. This unified pipeline provides a scalable and structure-aware approach to constructing self-supervised training data while bridging symbolic knowledge and natural language. Experiments on both structured and naturally occurring text demonstrate that the proposed splitter generalizes beyond synthetic templates and that the resulting structure-aware supervision consistently improves downstream performance on knowledge graph completion and commonsense question answering, highlighting the effectiveness of recovering latent factual structure for knowledge-centric NLP.

## 18. Auditing Retrieval-Augmented LLM Hypotheses for Longitudinal Cell Painting Morphology

- Authors: Gilchan Park, Guang Zhao, Byung-Jun Yoon, Shinjae Yoo
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-07-17
- DOI: 10.1145/3807503.3819448
- Categories: q-bio.QM, cs.AI, cs.CL
- Relevance: 2.952089006251193
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2607.19415v1
- PDF: https://arxiv.org/pdf/2607.19415v1
- Local PDF: pdf/2026-07-24_18_Auditing Retrieval-Augmented LLM Hypotheses for Longitudinal Cell Painting Morphology.pdf

High-content morphological profiling (Cell Painting) yields sensitive, high-dimensional signatures of cellular state, but translating longitudinal morphology trajectories into interpretable biology remains difficult, especially for weak, chronic perturbations such as low-dose-rate ionizing radiation. Large language models (LLMs) can synthesize heterogeneous evidence into biological narratives, yet their scientific use requires quantitative auditing. We present an evaluation-first, retrieval-augmented interpretation framework for longitudinal Cell Painting morphology, applied to a 9-week RPE-1 time course across five dose rates (0.003--6.0 mGy/hr). Week-matched treated-control morphology deltas are combined with retrieved perturbation neighbors, pathway context, and literature evidence through stable evidence identifiers, enabling an LLM to generate structured, evidence-linked hypotheses that are hierarchically summarized while preserving provenance. We introduce two quantitative auditing tests: V1 citation validity, which verifies that cited evidence identifiers exist in the prompt, and V2 proxy-based morphology compatibility, which evaluates consistency between predicted biological processes and the most altered morphology features. In our experiments, V1 detected no invalid evidence references, while V2 showed meaningful morphology compatibility that increased with perturbation strength and was positively associated with an independent morphology drift summary. The framework produces auditable, falsifiable biological hypotheses, including an adaptive phenotype involving metabolic reprogramming and proteostatic stress at lower dose rates (0.003--0.3 mGy/hr). Current limitations include proxy-based evaluation and the lack of ground-truth mechanism labels.

## 19. DREAM-S: Speculative Decoding with Searchable Drafting and Target-Aware Refinement for Multimodal Generation

- Authors: Zining Liu, Yunhai Hu, Tianhua Xia, BO Bao, Eric Sather, Vithursan Thangarasa, Sai Qian Zhang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.861318340267134
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.2177/
- PDF: https://aclanthology.org/2026.acl-long.2177.pdf
- Local PDF: pdf/2026-07-24_19_DREAM-S_ Speculative Decoding with Searchable Drafting and Target-Aware Refinement for Multimodal Generation.pdf

Speculative decoding (SD) has proven to be an effective technique for accelerating autoregressive generation in large language models (LLMs), however its application to vision-language models (VLMs) remains relatively unexplored. We propose DREAM-S, a novel SD framework designed specifically for fast and efficient decoding in VLMs. DREAM-S leverages a neural architecture search (NAS) framework with target-aware supernet training to automatically identify both the optimal interaction strategy between the draft and target models, and the most suitable draft model architecture for the underlying hardware implementation platform. DREAM-S additionally incorporates adaptive intermediate feature distillation, guided by attention entropy, to enable efficient draft training. Experiments on a range of well-established VLMs show that DREAM-S achieves up to a 3.85 × speedup compared to standard decoding approaches and significantly outperforms existing SD baselines.

## 20. Comparing Human and Large Language Model Interpretation of Implicit Information

- Authors: Antonio De Santis, Tommaso Bonetti, Andrea Tocchetti, Marco Brambilla
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.8609408162261984
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1111/
- PDF: https://aclanthology.org/2026.findings-acl.1111.pdf
- Local PDF: pdf/2026-07-24_20_Comparing Human and Large Language Model Interpretation of Implicit Information.pdf

The interpretation of implicit meanings is an integral aspect of human communication. However, this framework may not transfer to interactions with Large Language Models (LLMs). To investigate this, we introduce the task of Implicit Information Extraction (IIE) and propose an LLM-based IIE pipeline that builds a structured knowledge graph from a context sentence by extracting relational triplets, validating implicit inferences, and analyzing temporal relations. We evaluate two LLMs against crowdsourced human judgments on two datasets. We find that humans agree with most model triplets yet consistently propose many additions, indicating limited coverage in current LLM-based IIE. Moreover, in our experiments, models appear to be more conservative about implicit inferences than humans in socially rich contexts, whereas humans become more conservative in shorter, fact-oriented contexts. Our code is available at https://github.com/Antonio-Dee/IIE_from_LLM.

## 21. Can LLM Safety Be Ensured by Constraining Parameter Regions?

- Authors: Zongmin Li, Jian Su, Farah Benamara, Aixin Sun
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.860872544055188
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1616/
- PDF: https://aclanthology.org/2026.acl-long.1616.pdf
- Local PDF: pdf/2026-07-24_21_Can LLM Safety Be Ensured by Constraining Parameter Regions.pdf

Large language models (LLMs) are often assumed to contain "safety regions” - parameter subsets whose modification directly influences safety behaviors. We conduct a systematic evaluation of four safety region identification methods spanning different parameter granularities, from individual weights to entire Transformer layers, across four families of backbone LLMs with varying sizes. Using ten safety identification datasets, we find that the identified safety regions exhibit only low to moderate overlap, as measured by IoU. The overlap drops significantly when the safety regions are further refined using utility datasets (i.e. non-harmful queries). These results suggest that current techniques fail to reliably identify a stable, dataset-agnostic safety region.

## 22. QueryLink: Leveraging Query-Memory Alignment for Long-Term Reasoning in LLM Agents

- Authors: Xuxian Hu, Zhu Teng, Wei Zhang, Ming He, Jianping Fan
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.8607636705479376
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.765/
- PDF: https://aclanthology.org/2026.findings-acl.765.pdf
- Local PDF: pdf/2026-07-24_22_QueryLink_ Leveraging Query-Memory Alignment for Long-Term Reasoning in LLM Agents.pdf

Retrieval-Augmented Generation (RAG) systems are widely used to mitigate the stateless nature of Large Language Models (LLMs) in long-term and personalized interactions by incorporating external memory. However, existing approaches often prioritize memory organization, such as knowledge graphs, while overlooking a critical semantic gap between implicit, intent-driven queries and explicit, narrative-based memories. To bridge this gap, we propose QueryLink, a novel framework that leverages Query-Memory Alignment to project both queries and memories into a shared semantic space. It significantly boosts recall by facilitating multi-grained retrieval of semantically relevant information. To further enhance memory retrieval, we leverage Coherent Memory Chunking, a mechanism that processes memories in multi-turn dialogue units, preserving semantic integrity, rather than relying on fixed-size segments. Extensive experiments on the LoCoMo and LongMemEval benchmark demonstrate that QueryLink significantly outperforms SOTA methods, achieving at least a 7% improvement in reasoning accuracy (measured by LLM). Additionally, QueryLink can be integrated as a plug-and-play component to boost existing vector-based systems like A-MEM, leading to improvements of over 6% in both F1 and B1 scores.The code is available at https://github.com/Dontplay0112/querylink.

## 23. Compete to Complete: Co-opetition Adversarial Learning for Retrieval-Augmented Generation

- Authors: Xin Liu, Yu-An Liu, Ruqing Zhang, Yixing Fan, Lixin Su, Jiafeng Guo, Xueqi Cheng
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.860646518524118
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.258/
- PDF: https://aclanthology.org/2026.acl-long.258.pdf
- Local PDF: pdf/2026-07-24_23_Compete to Complete_ Co-opetition Adversarial Learning for Retrieval-Augmented Generation.pdf

Retrieval-augmented generation (RAG) has emerged as a promising paradigm for mitigating hallucinations in large language models (LLMs).However, the intrinsic heterogeneity between the retriever and the generator often leads to a mismatch between retrieved evidence and generation needs, hindering effective coordination.We argue that competition between discriminative retrieval and generative modeling can more effectively expose their mutual weaknesses and induce deeper interaction. Motivated by this insight, we propose CARL (Co-opetition AdveRsarial Learning), a framework that formulates retriever–generator training in RAG as a minimax game. In this game, the retriever is optimized to retrieve both useful and adversarially useless documents to challenge the generator, while the generator learns to identify useful evidence and remain robust to misleading retrievals to produce accurate answers.Experiments on seven benchmark datasets demonstrate that CARL consistently improves RAG performance, validating the effectiveness of adversarial co-opetition in enhancing retriever–generator synergy.

## 24. POP: Prefill-Only Pruning for Efficient Large Model Inference

- Authors: Junhui He, Zhihui Fu, Jun Wang, Qingan Li
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.8605731412330377
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.291/
- PDF: https://aclanthology.org/2026.findings-acl.291.pdf
- Local PDF: pdf/2026-07-24_24_POP_ Prefill-Only Pruning for Efficient Large Model Inference.pdf

Large Language Models (LLMs) and Vision-Language Models (VLMs) have demonstrated remarkable capabilities.However, their deployment is hindered by significant computational costs. Existing structured pruning methods, while hardware-efficient, often suffer from significant accuracy degradation. In this paper, we argue that this failure stems from a stage-agnostic pruning approach that overlooks the asymmetric roles between the prefill and decode stages. By introducing a virtual gate mechanism, our importance analysis reveals that deep layers are critical for next-token prediction (decode) but largely redundant for context encoding (prefill). Leveraging this insight, we propose Prefill-Only Pruning (POP), a stage-aware inference strategy that safely omits deep layers during the computationally intensive prefill stage while retaining the full model for the sensitive decode stage. To enable the transition between stages, we introduce independent Key-Value (KV) projections to maintain cache integrity, and a boundary handling strategy to ensure the accuracy of the first generated token. Extensive experiments on Llama-3.1, Qwen3-VL, and Gemma-3 across diverse modalities demonstrate that POP achieves up to 1.37 × speedup in prefill latency with minimal performance loss, effectively overcoming the accuracy-efficiency trade-off limitations of existing structured pruning methods.

## 25. KoCo: Conditioning Language Model Pre-training on Knowledge Coordinates

- Authors: Yudong Li, Jiawei Cai, Linlin Shen
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.859667468504517
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1111/
- PDF: https://aclanthology.org/2026.acl-long.1111.pdf
- Local PDF: pdf/2026-07-24_25_KoCo_ Conditioning Language Model Pre-training on Knowledge Coordinates.pdf

Standard Large Language Model (LLM) pre-training typically treats corpora as flattened token sequences, often overlooking the real-world context that humans naturally rely on to contextualize information. To bridge this gap, we introduce Knowledge Coordinate Conditioning (KoCo), a simple method that maps every document into a three-dimensional semantic coordinate. By prepending these coordinates as textual prefixes for pre-training, we aim to equip the model with explicit contextual awareness to learn the documents within the real-world knowledge structure. Experiment results demonstrate that KoCo significantly enhances performance across 10 downstream tasks and accelerates pre-training convergence by approximately 30%. Furthermore, our analysis indicates that explicitly modeling knowledge coordinates helps the model distinguish stable facts from noise, effectively mitigating hallucination in generated outputs.

## 26. DMHM: Density-aware Manifold Learning and Hybrid Mahalanobis Energy for LLMs-generated Text Detection

- Authors: Tianle Liu, Zhiliang Tian, Zhen Huang, Tianlun Liu, Jingyuan Huang, Zhaoning Zhang, Chengcheng Shao, Dongsheng Li
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.8592836807169855
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.180/
- PDF: https://aclanthology.org/2026.acl-long.180.pdf
- Local PDF: pdf/2026-07-24_26_DMHM_ Density-aware Manifold Learning and Hybrid Mahalanobis Energy for LLMs-generated Text Detection.pdf

As the text generated by large language models (LLMs) increasingly resembles human-written text (HWT), detecting LLM-generated text (LGT) is crucial to avoid malicious use of LGT. Recent research treats LGT detection as an out-of-distribution (OOD) detection problem and views HWT as the OOD. However, existing OOD detection methods assume that LGT is a single homogeneous distribution. In practice, LGT exhibits different characteristics under different generation conditions. Text from weaker LLMs tends to form distinct clusters and is easy to detect, whereas text from stronger models significantly overlaps with HWTs and is hard to detect. To address the issue, in this paper, we propose an LGT detection framework based on density-aware manifold learning and the construction of hybrid Mahalanobis energy. We apply density-aware manifold learning with Laplacian smoothness and density regularization in embedding space, amplifying differences between LGT and HWT. We further propose a density-adaptive hybrid Mahalanobis metric that combines global and local covariance via density weighting, enabling adaptation to the manifold-aware embedding space. Finally, based on the metric, we define the distribution energy as a measure of distribution discrepancy, and we employ energy learning and contrastive learning to separate distributions hierarchically, establishing a clear OOD decision boundary. Experiments show that our method outperforms strong baselines.

## 27. Rhombus: Incentivizing Coordination in Parallel Thinking through Reinforcement Learning

- Authors: Ziyuan Nan, Qi Yi, Di Huang, Yutong Wu, Guanhua Huang, Xue Gong, Kejiao Li, Yuhao Jiang, Chenchen Zhang, Zenan Xu, Xing Hu, Bo Zhou
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.857253820074024
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1956/
- PDF: https://aclanthology.org/2026.findings-acl.1956.pdf
- Local PDF: pdf/2026-07-24_27_Rhombus_ Incentivizing Coordination in Parallel Thinking through Reinforcement Learning.pdf

Parallel thinking offers a promising avenue for scaling test-time compute in Large Language Models (LLMs), enabling them to explore diverse solution paths simultaneously before aggregating them into a final answer. However, coordinating the exploration and aggregation stages remains challenging, as simple aggregation techniques often incur information loss, failing to preserve the subtle, decision-relevant signals generated during exploration. To overcome this, we propose Rhombus, a parallel thinking framework that explicitly incentivizes coordination between components via end-to-end reinforcement learning. Rhombus employs multiple parallel Proposers to generate compact, decision-focused reasoning cues and a central Synthesizer to integrate them into final predictions, utilizing co-training under a shared task reward to align their interaction. Across challenging mathematical reasoning benchmarks, Rhombus improves accuracy by 6.0% over long chain-of-thought baselines while reducing wall-clock latency by 39.4% under matched token budgets. Our work demonstrates that explicit communication optimization is essential for realizing the accuracy and efficiency gains of parallel reasoning.

## 28. CRAFTQA: A Code-Driven Adaptive Framework for Complex Structured Data Reasoning

- Authors: Chengtao Gan, Zhiqiang Liu, Long Jin, Yushan Zhu, Lei Liang, Wen Zhang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.856935774769492
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1387/
- PDF: https://aclanthology.org/2026.findings-acl.1387.pdf
- Local PDF: pdf/2026-07-24_28_CRAFTQA_ A Code-Driven Adaptive Framework for Complex Structured Data Reasoning.pdf

Real-world scenarios involve massive heterogeneous structured data (e.g., tables, knowledge graphs), making effective reasoning over such diverse data increasingly important. Unified structured data question answering has emerged as a prominent research trend, aiming to answer natural language questions across different structured data types within a single framework. However, existing unified methods share a common limitation: they rely on a set of predefined functions, which restricts their ability to perform complex reasoning beyond these predefined operations. To overcome this fundamental limitation, we propose CRAFTQA , a novel adaptive code-driven framework comprising two core modules, CodeSTEP and CRAFT. The CodeSTEP module is a paradigm that generates a complete executable Python code sequence, which contains step-by-step code-based reasoning operations based on the question.The CRAFT module dynamically generates custom code functions for operations beyond the predefined function set, and seamlessly integrates with CodeSTEP to significantly enhance flexibility in handling complex reasoning. Comprehensive experiments on multiple structured datasets demonstrate that CRAFTQA achieves remarkable improvements in complex reasoning scenarios compared to existing unified methods.

## 29. Lizard: An Efficient Linearization Framework for Large Language Models

- Authors: Chien Van Nguyen, Huy Huu Nguyen, Ruiyi Zhang, Hanieh Deilamsalehy, Puneet Mathur, Viet Dac Lai, Haoliang Wang, Jayakumar Subramanian, Ryan A. Rossi, Trung Bui, Nikos Vlassis, Franck Dernoncourt, Thien Huu Nguyen
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.8567099975198245
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1613/
- PDF: https://aclanthology.org/2026.acl-long.1613.pdf
- Local PDF: pdf/2026-07-24_29_Lizard_ An Efficient Linearization Framework for Large Language Models.pdf

We propose Lizard, a linearization framework that transforms pretrained Transformer-based Large Language Models (LLMs) into subquadratic architectures. Transformers faces severe computational and memory bottlenecks with long sequences due to the quadratic complexity of softmax attention and the growing Key-Value (KV) cache that makes inference memory-bound by context length. Lizard addresses these limitations by introducing a subquadratic attention mechanism that closely approximates softmax attention while preserving model quality. Unlike prior linearization methods constrained by fixed, non-adaptive structures, Lizard augments the architecture with compact, learnable modules that enable adaptive memory control and robust length generalization. Moreover, we introduce a hardware-aware algorithm that solves numerical instability in gated attention to accelerate training. Extensive experiments show that Lizard achieves near-lossless recovery of its teacher model’s performance, significantly outperforming previous methods by up to 9.4 - 24.5 points on the 5-shot MMLU benchmark and demonstrating superior associative recall.

## 30. Student Guides Teacher: Weak-to-Strong Inference via Spectral Orthogonal Exploration

- Authors: Dayu Wang, Jiaye Yang, Weikang Li, Jiahui Liang, Yang Li, Deguo Xia, Jizhou Huang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.8566368158193804
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.761/
- PDF: https://aclanthology.org/2026.acl-long.761.pdf
- Local PDF: pdf/2026-07-24_30_Student Guides Teacher_ Weak-to-Strong Inference via Spectral Orthogonal Exploration.pdf

Large Language Models (LLMs) often suffer from "Reasoning Collapse" on challenging mathematical reasoning tasks, where stochastic sampling produces lexical variations of the same erroneous logic rather than genuine semantic exploration. We observe that failed reasoning traces are often associated with a low-rank bias manifold in the model’s hidden-state geometry, which reduces exploration toward corrective solution directions. To address this, we propose Spectral Orthogonal Exploration (SOE), a geometric inference framework under a "Student Guides Teacher" paradigm. Instead of using a weak auxiliary agent for imitation, SOE uses it as an orthogonal probe to introduce semantically heterogeneous reasoning signals into the teacher’s orthogonal complement of its dominant subspace. This intervention steers the teacher toward more diverse reasoning trajectories and improves exploration beyond standard sampling. Experiments on mathematical benchmarks show that SOE improves average accuracy by 62.4% and average sampling efficiency by 113.7% over baseline methods, suggesting that geometric interventions can be effective for mitigating reasoning collapse in mathematical reasoning. We further provide preliminary evidence that SOE is also effective on logic and code generation benchmarks. Code is available at https://github.com/dayuwang401/spectral-orthogonal-exploration.
