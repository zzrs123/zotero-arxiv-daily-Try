# Paper Daily Reading - 2026-10-09

## 1. KGATE : a Knowledge Graph Embedding Training Environment

- Authors: Benjamin Loire, Galadriel Brière, Célia Brahimi, Antoine Toffano, Anaïs Baudot
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-07
- DOI: Unavailable
- Categories: cs.LG, cs.AI
- Relevance: 3.6500021066926944
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.09927v1
- PDF: https://arxiv.org/pdf/2610.09927v1
- Local PDF: pdf/2026-10-09_01_KGATE _ a Knowledge Graph Embedding Training Environment.pdf

Knowledge graph embedding (KGE) models encode the entities and relations of a knowledge graph into a low-dimensional latent space, enabling tasks such as classification or link prediction. Most KGE models follow an autoencoder architecture, in which an encoder projects the knowledge graph into the latent space and a decoder reconstruct it. Combining both encoder and decoder components is increasingly needed, yet existing libraries rarely support complete autoencoders, are often unmaintained, rely on undocumented default hyperparameters, and produce results that cannot be compared across libraries. Here we present KGATE (Knowledge Graph Autoencoder Training Environment), a modular Python library built on PyTorch Geometric and TorchKGE. KGATE lets users assemble initializers, encoders, decoders, losses, negative samplers, and evaluation metrics as building blocks, or plug in their own block. KGATE includes a preprocessing procedure that controls data leakage, a builtin training pipeline, and reproducibility by design. Benchmarks against six existing KGE libraries show that KGATE training time is comparable with the fastest libraries while offering a broader set of features.

## 2. Trustworthy Domain-Specific AI for Structured Knowledge Retrieval and Reasoning

- Authors: Ryan C. Barron
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-06
- DOI: Unavailable
- Categories: cs.IR, cs.AI
- Relevance: 3.436715279495469
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.08894v1
- PDF: https://arxiv.org/pdf/2610.08894v1
- Local PDF: pdf/2026-10-09_02_Trustworthy Domain-Specific AI for Structured Knowledge Retrieval and Reasoning.pdf

This dissertation presents a scalable architecture for transforming unstructured, domain-specific text into structured knowledge for retrieval and reasoning. It integrates semi-automatic corpus curation, semantic structuring, retrieval, and inference into an interpretable pipeline.
  The research introduces Binary Bleed, an adapted binary search method that reduces low-rank search complexity for Non-negative Matrix Factorization (NMF), and Hierarchical NMF with automatic latent feature selection (HNMFk), a depth-adaptive topic modeling method that produces interpretable taxonomies guided by subject matter experts. These representations populate a typed Knowledge Graph and a semantically aligned Vector Store containing extracted latent features, synchronized through an event-driven substrate.
  Tensor-Structured Retrieval-Augmented Generation (T-SRAG) dynamically routes queries across retrieval paths. Contrastive alignment maps document and query embeddings to hierarchical topic structures to improve semantic fidelity and reduce hallucinations. Beyond retrieval, tensor-based link prediction identifies and completes missing links in the Knowledge Graph, supporting inference grounded in citation structure.
  Applications across cybersecurity, law, materials science, and healthcare demonstrate improvements in retrieval precision, early trend detection, hypothesis generation, and hallucination mitigation. The dissertation provides a deployable, modular foundation for trustworthy, domain-specific AI systems that retrieve and reason over structured knowledge.

## 3. DSReg: Provably Recovering Individual World Latents without Reconstruction

- Authors: Yujia Zheng, David Klindt, Randall Balestriero, Bernhard Schölkopf
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-07
- DOI: Unavailable
- Categories: cs.LG, cs.AI, cs.RO, stat.ML
- Relevance: 3.303093915946304
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.09457v1
- PDF: https://arxiv.org/pdf/2610.09457v1
- Local PDF: pdf/2026-10-09_03_DSReg_ Provably Recovering Individual World Latents without Reconstruction.pdf

Methods that recover individual latent variables of the world, from nonlinear ICA to dictionary learning and causal representation learning, anchor the latents to observations through reconstruction, auxiliary supervision, or distributional asymmetries such as non-Gaussianity. Methods without these anchors, including joint-embedding predictive architectures (JEPAs), identify the latent state only up to a linear transformation, so individual latents remain mixed. We close this gap: individual world latents can be provably recovered with no reconstruction, no decoder, and no labels. The key condition is Structural Diversity: different latents leave distinct dependency footprints on observations, just as no two snowflakes are alike. Building on the linear identifiability that LeJEPA provides, we prove that under Structural Diversity, DSReg (Dependency-Sparsity Regularization) recovers individual world latents up to signed permutation, without reconstruction or a decoder. It applies post hoc to any linearly identified representation, reusing trained checkpoints at no loss over joint training, and establishes the first fully identifiable JEPA that recovers every world latent. Moreover, as a condition on dependency footprints, Structural Diversity is strictly weaker than all structural conditions of prior identifiable latent variable models. Across synthetic regimes, world model probes, learned visual encoders, and external renderers, DSReg preserves dense prediction while improving individual-latent recovery and downstream use with scales.

## 4. DisParQ: Self-Supervised Part Concepts for Interpretable Vision Foundation Models

- Authors: Adam Pardyl, Siddhartha Gairola, Sukrut Rao, Adam Wróbel, Bartosz Zieliński, Bernt Schiele, Dawid Rymarczyk
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-07
- DOI: Unavailable
- Categories: cs.CV, cs.AI, cs.LG
- Relevance: 3.2697307443524144
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.09802v1
- PDF: https://arxiv.org/pdf/2610.09802v1
- Local PDF: pdf/2026-10-09_04_DisParQ_ Self-Supervised Part Concepts for Interpretable Vision Foundation Models.pdf

Concept-based vision models represent images through an intermediate layer of human-inspectable concepts, so what a model relies on can be traced to those concepts. However, those models are often limited to fixed categories or depend on language to define their concepts. We introduce DisParQ (Discrete Parts with Quantized attributes), a method that learns spatially grounded, discrete concept representations from a powerful frozen vision-only self-supervised backbone. It requires no class labels and no language supervision. Each image patch is assigned to exactly one concept from a learnable prototype dictionary, and only a sparse subset of concepts may activate per image. To capture how each concept varies across images (e.g., the type of a "wheel"), we learn continuous residuals alongside the concepts and then quantize them into discrete attributes. A spatial decoder reconstructs the backbone's representation from the concepts and attributes alone, so successful reconstruction means that the discrete representation preserves the backbone's information. We evaluate DisParQ across seven datasets, from general recognition (ImageNet, PartImageNet, Places) to fine-grained benchmarks (CUB, Cars, Dogs, Flowers). We show that DisParQ closely matches its frozen DINOv2 teacher on ImageNet linear probing (83.2% top-1), achieves higher concept consistency than language-aligned models, remains competitive on fine-grained recognition, and enables cross-category part-based retrieval.

## 5. Automatically Building and Updating a Knowledge Graph of MLIP Models

- Authors: Alexis Beer, Liudmyla Klochko, Mathieu d'Aquin
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-07
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 3.251367698091414
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.09644v1
- PDF: https://arxiv.org/pdf/2610.09644v1
- Local PDF: pdf/2026-10-09_05_Automatically Building and Updating a Knowledge Graph of MLIP Models.pdf

Complementing the many efforts in providing semantic representations of concepts, notions, and entities in materials science, we report and illustrate a process by which we can automatically build a knowledge graph of the fast evolving field of machine learning applied to the prediction of material properties, focusing on MLIP (Machine Learning Interatomic Potential). This LLM-based process relies on multiple steps, from information extraction in documents and articles to a validation loop using SHACL constraints to detect and correct errors. It is carried out on a model-by-model basis, focusing on the consistency of representation, therefore enabling an iterative construction where the addition of new models is facilitated. We illustrate the process by showing a few interesting aspects that can be queried from a knowledge graph built from the models listed in the Matbench Discovery leaderboard.

## 6. ORCA: Hunting Compositional Failures in Text-to-Image Diffusion

- Authors: Arshia Hemmat, Amirhossein Vahidi, Amitis Shidani, Mohammad Vali Sanian, Hesam Asadollahzadeh, Aryan Yazdan Parast, Mohammad Lotfollahi
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-07
- DOI: Unavailable
- Categories: cs.CV, cs.LG
- Relevance: 3.241561367311694
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.09841v1
- PDF: https://arxiv.org/pdf/2610.09841v1
- Local PDF: pdf/2026-10-09_06_ORCA_ Hunting Compositional Failures in Text-to-Image Diffusion.pdf

Text-to-image diffusion models fail predictably on compositional prompts: attributes bind to the wrong objects, spatial relations invert, and multi-object scenes lose count. Recent architectures already augment CLIP with a T5 encoder precisely because CLIP's contrastive embedding loses compositional structure, yet these failures persist. We argue the binding problem is therefore not one of missing information but of misaligned information: a text encoder preserves compositional structure, but in a representation space shaped by language modelling rather than vision, and the denoising objective does not directly reward aligning the two. We show this correspondence can be supplied as an explicit training signal, that the relevant cross-modal information is concentrated in a low-rank subspace of self-supervised visual features, and that supplying it can be folded into diffusion training as a single auxiliary loss. Our method, ORCA (Orthogonal Residual Compositional Alignment), aligns the latent of a diffusion transformer with a low-rank target derived from a frozen visual encoder, through a predictor whose orthogonal basis is parameterised by a learned residual between T5 and CLIP embeddings, which provides a prompt-dependent signal for selecting the visual readout subspace. We prove that the cross-modal information recoverable at a given rank is bounded by the spectral mass of the visual encoder's covariance in the top components. Across three diffusion-transformer backbones (DiT-B/2, DiT-L/2, U-ViT-L), ORCA improves FID and GenEval over both vanilla and REPA baselines at zero inference-time cost; on DiT-L/2 it reaches FID 16.65 and GenEval 0.291 at 200K steps, exceeding the strongest 400K baseline at half the training cost, with the largest gains concentrated on attribute binding, spatial relations, and multi-object prompts.

## 7. Executing Causal Structure Learning with Linear-Attention Transformers

- Authors: Amartya Roy, Sayar Karmakar
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-07
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.23878939076049
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.10395v1
- PDF: https://arxiv.org/pdf/2610.10395v1
- Local PDF: pdf/2026-10-09_07_Executing Causal Structure Learning with Linear-Attention Transformers.pdf

Transformers can execute algorithms on data given in their input. We ask whether they can do the same for causal discovery. We study a standard continuous method that repeatedly updates a candidate causal graph while enforcing acyclicity. We explicitly construct a fixed-weight transformer whose forward pass exactly reproduces one update of this method, so repeated blocks reproduce its optimization trajectory. The transformer carries the current graph and the algorithm's multiplier between updates. We show that retaining the multiplier is essential for exact execution, since different multiplier values can lead to different next updates. We also give conditions under which, within a fixed stage, the number of updates needed to reach a target accuracy can be computed in advance and rounding errors stay bounded as depth grows. Experiments show that the constructed block agrees with a reference update to floating-point precision, while arithmetic replay on synthetic data and seven published benchmark network topologies inherits the reference solver's successes and failures. This separates accurate algorithm execution from accurate causal recovery. In contrast, the ordinary attention models tested under our training budgets do not reliably execute the update or transfer to larger graphs. Whether gradient training can learn an executor in the architecture class of the construction remains open.

## 8. Mixture of Layers: Dynamic Layer Routing for Visual Reasoning

- Authors: Jeonghwan Kim, Sofia Stoica, Jiwan Chung, Ansel Blume, Hyeonjeong Ha, Zhenhailong Wang, Xin Luna Dong, Heng Ji
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-07
- DOI: Unavailable
- Categories: cs.CV, cs.AI
- Relevance: 3.222706189230081
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.09440v1
- PDF: https://arxiv.org/pdf/2610.09440v1
- Local PDF: pdf/2026-10-09_08_Mixture of Layers_ Dynamic Layer Routing for Visual Reasoning.pdf

Pre-trained vision encoders contain layer-wise visual representations that differ in spatial granularity, semantic abstraction, and sensitivity to local details. However, most Multimodal Large Language Models (MLLMs) rely on only the final or penultimate vision encoder representations or fixed aggregation rules, making visual abstraction largely query-agnostic and limiting access to fine-grained cues such as small objects, spatial details, text, and subtle visual attributes. In this work, we propose Mixture of Layers (MoL), an instruction-conditioned layer routing approach at the visual patch level that dynamically aggregates query-relevant latent representations from intermediate vision encoder layers. Given a text query, MoL predicts routing probabilities over vision encoder layers and performs a top-k sparse aggregation over selected hidden states at either the image level, patch level, or through a hybrid routing mechanism. In doing so, MoL enables query-adaptive access to layer-specific visual features for fine-grained visual reasoning. Our experiments across 7 fine-grained visual reasoning tasks demonstrate substantial performance improvements, especially across fine-grained visual grounding and understanding tasks such as +18.9% improvement on V* in overall accuracy, +4.5% on HRBench4K, and +16.3% on CharXiv compared to the baseline MLLMs, without resorting to multi-resolution inputs, simple interleaving of multiple vision encoders, or increasing the number of patch tokens. We study vision encoders' receptive field scales across different layers and their sampling behaviors to provide an in-depth analysis of why layer-wise sampling is helpful, demonstrating that conditional visual representations are a key step towards better visual perception and reasoning in MLLMs. Our project page is available at https://wjdghks950.github.io/mol.github.io/.

## 9. The Dichotomy Between Pattern Recognition and Step-by-Step Reasoning

- Authors: Amrut Nadgir, Pratik Chaudhari, Vijay Balasubramanian
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-06
- DOI: Unavailable
- Categories: cs.LG, cond-mat.dis-nn
- Relevance: 3.1050538999383868
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.09186v1
- PDF: https://arxiv.org/pdf/2610.09186v1
- Local PDF: pdf/2026-10-09_09_The Dichotomy Between Pattern Recognition and Step-by-Step Reasoning.pdf

We argue that pattern recognition and step-by-step reasoning are two ends of a spectrum. A large language model (LLM) learns to reason step-by-step when data is structured such that the next token depends on a small amount of preceding context. Inference in LLMs resembles pattern recognition when the next token depends on a large amount of preceding context. If the next token depends on only the $c$ most recent tokens, reasoning traces are paths on a De Bruijn graph whose nodes are $c$-length contexts and edges are next-token transitions between contexts. The set of reasoning traces of a task forms a directed acyclic subgraph of the De Bruijn graph. An LLM that has learned all edges of this subgraph can compose them to solve longer, unseen tasks, i.e., it reasons step-by-step. We prove that the number of edges is vanishingly small compared to the number of reasoning traces. Empirically, the number of training samples a transformer needs is a power law in the number of edges, so learning to reason step-by-step is sample efficient. We can induce De Bruijn structure in any task by maintaining a ``state'' that makes future reasoning independent of the past. The frequency of states in the reasoning trace determines $c$. We show, by fine-tuning Qwen2.5-1.5B-Instruct to solve equations and answer questions about stories, that frequent states (small $c$) result in higher accuracy but greater fragility to perturbations at test time. LLMs trained with a large $c$ are only as good as models that perform pattern recognition without reasoning. A moderate density of states balances accuracy and robustness. We show that real-world data has De Bruijn structure: Qwen3-14B and Qwen3-32B retain over 75% of their accuracy on GSM8K, MATH-500 and GPQA-Diamond when attention is restricted to a sliding window less than 15% as long as the full reasoning trace.

## 10. DrugTargetWorld: A Synthetic Biobank for Training and Benchmarking AI Scientists

- Authors: Samuel Margolis, Paul Schmiedmayer, Alan Huang, Ethan Chen, Ishan Bhattacharjee, Atman Shah, Ben Viggiano, Fang Cao, Shriya Reddy, Roger Xia, Jack O'Sullivan, Daniel Katz, Matthew Wheeler, Euan Ashley, Bruna Gomes
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-07
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 3.0809786743715373
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.09558v1
- PDF: https://arxiv.org/pdf/2610.09558v1
- Local PDF: pdf/2026-10-09_10_DrugTargetWorld_ A Synthetic Biobank for Training and Benchmarking AI Scientists.pdf

Drug target discovery requires distinguishing molecules that causally drive disease from those that are merely associated with it. Training and evaluating AI agents to perform this workflow end-to-end is difficult because real world biobanks lack known causal ground truth and participant-level data is access controlled. We introduce DrugTargetWorld, a framework that procedurally generates simulated biobanks, or "worlds," with known but concealed causal structure. Each world contains genotypes, proteins, health records, outcomes, and synthetic magnetic resonance imaging (MRI) for 54,000 participants. Agents must construct a disease phenotype, identify causal driver proteins, infer the beneficial direction of modulation, and optionally conduct virtual 'wet lab' experiments. We evaluated nine agents in 540 episodes across 20 cardiovascular worlds and three experimental budgets. Opus 5 and GPT-5.6 Sol achieved the highest mean composite scores, 39.98 and 35.38 of 100, respectively, and both recovered 64% of causal drivers on average. However, no agent reliably distinguished misleading non-causal proteins, and performance remained limited by the integrative judgments required to connect phenotype construction, causal evidence, and intervention decisions. By making each world's causal structure known to the evaluator but hidden from the agent, DrugTargetWorld turns end-to-end drug target discovery into a scalable training and evaluation problem with verifiable reward.

## 11. RECAST: Learning to Compute the Right Context through Adaptive Evidence Routing

- Authors: Yilun Hao, Krishna Sayana, Isabella Ye, James S Ren, Sukhdeep Sodhi, Craig Boutilier, Chuchu Fan
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-07
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 3.067098143798664
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.10507v1
- PDF: https://arxiv.org/pdf/2610.10507v1
- Local PDF: pdf/2026-10-09_11_RECAST_ Learning to Compute the Right Context through Adaptive Evidence Routing.pdf

Large language models are increasingly applied to tasks grounded in long, heterogeneous information sources. Conventional Retrieval-Augmented Generation (RAG) relies on fixed similarity-based retrieval, while agentic variants adapt queries and tool use but remain largely retrieval-centric. However, in many tasks, the evidence required for a solution is not explicitly present in any single source item. Instead, it must be derived through filtering, aggregation, or computation across multiple source items. In this work, we introduce RECAST (Routing Evidence through Computation, Access, and Synthesized Tools), a learned framework that formulates evidence construction as a sequential decision process over heterogeneous retrieval and computation operations, allowing evidence to be actively derived rather than merely retrieved. A lightweight RouterLM iteratively selects and formulates primitive operations or specifies customized operations for a frozen CompilerLM to translate into executable code. Once it judges the evidence sufficient, RouterLM passes the accepted evidence to a frozen AnswerLM to produce the final solution. We train RouterLM with supervised fine-tuning (SFT) followed by group relative policy optimization (GRPO). Across six heterogeneous benchmark families, RECAST achieves a mean success rate of 75.6%, outperforming the strongest large-model baseline by 15.9%. Moreover, training enables the Qwen3.5-9B RouterLM to outperform a training-free Gemini 3.5 Flash RouterLM by 5.0%. On three held-out benchmarks, RECAST improves over the strongest baseline by 15.0% on average, demonstrating strong zero-shot generalization across tasks and heterogeneous source representations.

## 12. Performance at What Cost? A Sustainability-Aware Performance Index for Cell and Nucleus Instance Segmentation

- Authors: Eiram Mahera Sheikh, Alaa Tharwat, Wolfram Schenck
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-07
- DOI: Unavailable
- Categories: cs.CV, cs.AI
- Relevance: 3.059778813296438
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.10324v1
- PDF: https://arxiv.org/pdf/2610.10324v1
- Local PDF: pdf/2026-10-09_12_Performance at What Cost_ A Sustainability-Aware Performance Index for Cell and Nucleus Instance Segmentation.pdf

Pretrained models for cell and nuclear instance segmentation differ substantially in architecture, pretraining data and objectives, parameter count, inference strategy, adaptation requirements, postprocessing pipeline, and computational demand. Large pretrained and foundation models are increasingly adopted because of their strong zero-shot capabilities, but their use also imposes greater energy consumption, memory requirements, computational demands, adaptation costs, and operational carbon emissions. Whether these additional demands are justified by meaningful gains in segmentation performance remains unclear. We address this question by introducing the Sustainability-Aware Performance Index (SAPI), a configurable metric that combines segmentation performance, energy consumption, and model size. We benchmark 19 pretrained and foundation models across six CellBinDB datasets under zero-shot inference and evaluate 16 fine-tunable models using few-shot adaptation with both frozen encoder and full-model fine-tuning. We estimate energy consumption for GPU, CPU, and RAM using software-based monitoring tools. Our results show that larger and more computationally demanding models do not consistently achieve proportionate improvements in segmentation quality. While few-shot adaptation benefits several models, the gains and resource costs vary considerably across architectures, datasets, and adaptation strategies, causing SAPI-based rankings to differ from rankings based on performance alone. This study provides a practical framework for comparing segmentation models more comprehensively and supports more computationally accessible and environmentally responsible model selection in biomedical image analysis.

## 13. MUNITE: Unified Multimodal Latent Inference for Any-to-Any Multimodal Generation

- Authors: Kyeongmin Yeo, Minhyuk Sung
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-07
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.05267943617657
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.09866v1
- PDF: https://arxiv.org/pdf/2610.09866v1
- Local PDF: pdf/2026-10-09_13_MUNITE_ Unified Multimodal Latent Inference for Any-to-Any Multimodal Generation.pdf

We introduce MUNITE, a latent-variable framework for flexible any-to-any multimodal generation that treats encoding and latent generation as the same inference problem under different amounts of observed evidence. Given any subset of modalities, MUNITE models the conditional distribution over the latent representation associated with the complete observation. Full observation recovers deterministic encoding, no observation recovers the latent marginal, and intermediate subsets define conditional latent inference, all within a single conditional flow model. A shared latent sample captures variation that must remain consistent across generated targets, while modality-specific generative decoders model the remaining uncertainty independently. To learn these conditional distributions from incomplete training examples, we extend conditional flow matching through self-distillation: predictions conditioned on richer available observations supervise the same model conditioned on smaller subsets at the same intermediate latent state. When the richer-evidence trajectory follows the exact conditional flow, this provides the same expected learning signal as full-target denoising. Across PolyMNIST-D-Q, FFHQ64, and image-text-audio, MUNITE achieves competitive or better generation quality and source-target alignment, with higher joint-generation coherence. In particular, it attains the highest coherence in all one-to-many and unconditional image-text-audio comparisons, showing the effectiveness of unified latent inference across diverse multimodal settings.

## 14. Sequential Pretraining Favors Large Models

- Authors: Mohnish Harwani, Yujia Zheng
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-07
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 3.0501257645924333
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.09611v1
- PDF: https://arxiv.org/pdf/2610.09611v1
- Local PDF: pdf/2026-10-09_14_Sequential Pretraining Favors Large Models.pdf

Large neural networks often acquire capabilities that small models fail to learn. Does this stem from large models learning more representative features, or from being more robust to unaccounted-for adverse effects introduced during training? We define and quantify one such adverse effect, primacy bias, as the extent to which exposure to early data distributions impairs later learning. We show that small models can allocate learning capacity inefficiently toward early distributions, whereas sufficiently overparameterized models are robust to this effect. This inefficiency is particularly consequential in pretraining, where foundation models often encounter heterogeneous data distributions sequentially rather than jointly. As a result, small foundation models can struggle to learn distributions encountered late in training, which is particularly harmful when later data emphasizes desirable capabilities such as code, mathematics, and reasoning. Motivated by these findings, we introduce Exposure Therapy (ET), a simple regularization that promotes more efficient allocation of learning capacity during sequential pretraining. We demonstrate that ET improves foundation models' performance on late data distributions as well as overall capability in models up to the billion-parameter scale. Overall, our results suggest that some benefits of large foundation models may arise from greater robustness to adverse training effects, rather than from learning more representative features, and that improved training algorithms can recover some of these advantages in smaller models.

## 15. Unrolled Flow Models for Reasoning

- Authors: Faissal Izermine, Hanru Bai, Oscar Davis, T. Konstantin Rusch
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-07
- DOI: Unavailable
- Categories: cs.LG, cs.AI
- Relevance: 3.0461523501949275
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.09759v1
- PDF: https://arxiv.org/pdf/2610.09759v1
- Local PDF: pdf/2026-10-09_15_Unrolled Flow Models for Reasoning.pdf

Flow matching enables language generation in few steps, but whether additional integration steps improve reasoning remains unclear. We prove that a flow parameterized by a two-layer Transformer can solve graph reachability, with the required number of integration steps increasing with the target's distance from the root. Yet, standard flow language models can fail to benefit from additional steps on reasoning tasks. We attribute this limitation to objectives that supervise each time point independently, without explicitly training successive steps to build on one another. To address this, we instead train through the model's own latent rollout over a randomly sampled subinterval of [0, 1], decoding only at the endpoint. On ProsQA, this raises accuracy to 97% and enables performance to improve with additional integration steps. For the longer rollouts required by reasoning tasks such as Sudoku and Maze, retracting the latent state onto a sphere stabilizes the dynamics and yields substantial gains over baselines with more than three times as many parameters. Sampling multiple rollouts further improves performance when paired with a parameter-free selection score, although reliable selection remains challenging for longer answers. Together, these results establish a theoretical basis for reasoning with flows and show how rollout training, stable latent dynamics, and rollout selection help realize this capacity in practice.

## 16. Multimodal LLMs Can Learn to Read Brain Signals: A Vision--Language Model for Unified Multi-Task EEG Decoding

- Authors: Parastoo Azizeddin, Omid Sharafi, Maryam M. Shanechi
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-07
- DOI: Unavailable
- Categories: cs.LG, cs.AI, cs.CV
- Relevance: 3.022071086767704
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.09355v1
- PDF: https://arxiv.org/pdf/2610.09355v1
- Local PDF: pdf/2026-10-09_16_Multimodal LLMs Can Learn to Read Brain Signals_ A Vision--Language Model for Unified Multi-Task EEG Decoding.pdf

Learning EEG representations that generalize across cognitive tasks, subjects, and recording conditions remains a key challenge in electroencephalography (EEG) decoding. Recent advances in foundation models have improved EEG decoding performance, yet a fundamental open question remains: how to effectively interface neural signals with these models to enable multi-task learning across datasets. To investigate this question, we introduce BraVista, a visual-language framework that encodes multichannel EEG signals as structured images and enables multi-task learning through instruction-conditioned vision-language models (VLMs). Our approach relies on continued post-training of a general-domain VLM, leveraging its visual and linguistic priors to adapt to neural signals without a separate large-scale EEG-specific pretraining stage. We evaluate BraVista on four datasets spanning sleep staging, emotion recognition, cognitive workload classification, and abnormal EEG detection, showing strong performance across these tasks. Further analyses show that the choice of EEG-to-image representation is critical to performance. Moreover, through controlled perturbations of the EEG signal, we observe a gradual performance degradation under increasing noise, suggesting that the model relies on EEG-relevant information rather than superficial visual patterns. Together, these findings establish structured visual representations as an effective and scalable interface between neural signals and general-domain foundation models for unified multi-task EEG decoding.

## 17. CircuitATLAS: Agentic reasoning over a systems neuroscience knowledge graph for target discovery in circuitopathies

- Authors: Gabriel Ocana-Santero, Marko Tvrdic
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-07
- DOI: Unavailable
- Categories: q-bio.QM, cs.AI, q-bio.NC
- Relevance: 3.018943044844506
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.09643v1
- PDF: https://arxiv.org/pdf/2610.09643v1
- Local PDF: pdf/2026-10-09_17_CircuitATLAS_ Agentic reasoning over a systems neuroscience knowledge graph for target discovery in circuitopathies.pdf

Drug discovery for neurological disease has traditionally centered on the molecules altered by disease. But the molecules that cause pathology are not necessarily the best points from which to reverse it. Here, we ask which otherwise unaltered molecular control points can be engaged to restore pathological neural circuits toward functional states. We present CircuitATLAS, a provenance-grounded systems-neuroscience knowledge graph and agentic framework for target discovery in circuitopathies. It structures literature-derived relationships across diseases, phenotypes, electrophysiology, circuits, brain regions, cell types and molecular effectors, while deliberately excluding direct disease-gene and disease-protein edges to reduce shortcut reasoning. The graph contains 3.83 million nodes and 7.66 million edges, including 5.31 million LLM-extracted relations, and incorporates structured datasets such as the Human Cell Atlas and new multimodal in vivo measurements. We then introduce an agentic workflow that reasons from measurable disease phenotypes through their circuit and cellular substrates to molecular interventions, therapeutic feasibility and clinical constraints. Finally, we introduce a human-governed in vivo lab-in-the-loop linking hypothesis generation to experimental iteration. Within this framework an agent nominated ATP1A3, the neuronal alpha3 Na+/K+-ATPase, as a control point on cortical excitability; interneuron-restricted expression of ATP1A3 abolished the beta- and gamma-band response to a focal 4-aminopyridine challenge in vivo, and the validated target was then carried into a structure-guided small-molecule campaign terminating in a defined assay to resolve the direction of modulation. CircuitATLAS thus provides a framework for discovering therapeutics based not only on what is molecularly disrupted in disease, but on what can be controlled to restore circuit function.

## 18. Frozen Models, Evolving Expertise: Model-Agnostic Learning from Deployment Experience for Multimodal Medical AI

- Authors: Yexiao He, Yucheng Tang, Pengfei Guo, Yufan He, Andriy Myronenko, Can Zhao, Ang Li, Daguang Xu, Dong Yang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-06
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 2.995925060415196
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.09146v1
- PDF: https://arxiv.org/pdf/2610.09146v1
- Local PDF: pdf/2026-10-09_18_Frozen Models, Evolving Expertise_ Model-Agnostic Learning from Deployment Experience for Multimodal Medical AI.pdf

Large language models (LLMs) and vision-language models (VLMs) are usually frozen after deployment, so they do not learn from the cases they solve. This is especially concerning in medicine, where new clinical evidence, updated guidelines, and new therapies can change established practice. Fine-tuning can update the model, but it requires access to model weights and additional training. Parameter-free methods avoid training, but they may overfit a fixed validation set, lack reliable domain knowledge, or lose visual details by saving experience only as text. To address these limitations, we present a model-agnostic framework that allows frozen LLMs and VLMs to learn from deployment experience through three forms of external expertise: a Skill that guides reasoning and tool use, a Knowledge Memory that stores reliable facts supported by earlier cases or trusted external evidence, and a Multimodal Knowledge Base that keeps visual examples and guides the model to relate each retrieved case to the current image. Instead of relying on a fixed validation set, a validation strategy keeps an update only if it helps on new cases without degrading performance on earlier ones. Across six benchmarks covering clinical diagnosis, clinical workflows, medical reasoning, and medical and non-medical visual reasoning, and with four open-weight and closed-source base models, our framework improves performance during online deployment by up to 34.2% over the base model on medical tasks, generalizes to unseen cases, transfers to other models without further optimization, and works in non-medical domains.

## 19. Thinking in Depth: Retrospective Inference for Tabular Foundation Models

- Authors: Hao-Run Cai, Si-Yang Liu, Zi-Jian Cheng, Kun-Yang Yu, Jin-Hao Sheng, Guo Yu, Chonghan Liu, Zhi Zhou, Jun-Peng Jiang, Lan-Zhe Guo, Han-Jia Ye
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-07
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 2.986056701197861
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.10317v1
- PDF: https://arxiv.org/pdf/2610.10317v1
- Local PDF: pdf/2026-10-09_19_Thinking in Depth_ Retrospective Inference for Tabular Foundation Models.pdf

Tabular foundation models (TFMs) are pretrained across diverse tabular tasks and make predictions on a new table at inference time using its labeled examples as context. Most recent TFMs perform such in-context prediction with stacked Transformer layers, repeatedly transforming how examples are represented and compared. By tracing individual queries through several strong TFMs, we find that predictive refinement is highly uneven across depth and is often concentrated in later layers. This uneven refinement motivates us to reconsider how intermediate representations are constructed and reused throughout the network. We introduce Retro, a tabular foundation model based on retrospective inference, where later stages can explicitly revisit and recombine intermediate information produced earlier in the network. Retro organizes this process around two complementary operations: which intermediate information to revisit, and how the resulting contextual update should be shaped for each query. Attention Residuals address the former by adaptively reweighting contributions from different depths, while query-conditioned Gated Attention addresses the latter by modulating the attention output element-wise across representation dimensions. Our analysis shows that Retro shifts predictive refinement earlier and more broadly across depth, with different stages revising different subsets of queries in a pattern suggestive of multi-view refinement. Across TabArena, TALENT, and RelArena, Retro ranks among the top three and lies on the Pareto frontier. These results indicate that directly reusing intermediate representations provides a practical way to better exploit depth in TFMs.

## 20. Think Before You Paint: Recursive Latent Reasoning for Diffusion Models

- Authors: Paweł Skierś, Małgorzata Grzanka, Wojciech Masarczyk, Jan-Willem van de Meent, Kamil Deja
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-07
- DOI: Unavailable
- Categories: cs.AI, cs.LG
- Relevance: 2.983622249619067
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.09876v1
- PDF: https://arxiv.org/pdf/2610.09876v1
- Local PDF: pdf/2026-10-09_20_Think Before You Paint_ Recursive Latent Reasoning for Diffusion Models.pdf

Diffusion models generate realistic images but often fail on visual reasoning tasks, such as filling in a Sudoku or drawing the path through a maze. When a discrete symbolic representation is available, recursive methods such as the Tiny Recursive Model (TRM) solve even hard instances of these puzzles. We ask how such reasoning can be carried over to pixels, where no symbolic representation is available. We propose Painter-Thinker (PaTh): a small recursive network (the Thinker) reasons over a grid of learned tokens that encode the noisy image and the conditioning, refines a latent state within every denoising step, and steers a frozen diffusion model (the Painter) through ControlNet adapters. The Thinker is trained with the standard reconstruction loss alone, without symbolic targets, a solver, or a verifier. PaTh solves 92.5% of hard MNIST Sudoku puzzles (prior best 75%) and 71.2% of extreme ones (prior best 4.1%), with 10M parameters against 82M for a standard diffusion model. It also improves on mazes, Queens, and CLEVR scenes with specified spatial relations, and its advantage grows with problem size. Diagnostic experiments show that PaTh recovers from injected mistakes that the diffusion model cannot repair, especially when many cells are wrong. Together, these results show that reasoning mechanisms developed for symbolic data can be integrated into pixel-space diffusion without symbolic supervision, opening a path toward generating data under increasingly complex constraints.

## 21. From High Recall to High Utility: Dataset-Adaptive Post-Processing of LLM-Generated Customer Intents

- Authors: Mahesh Viswanathan, Joan Rossello, Leticia Fernandes, Paul Mutawe
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-06
- DOI: Unavailable
- Categories: cs.AI, cs.IR
- Relevance: 2.9763925423505055
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.09039v1
- PDF: https://arxiv.org/pdf/2610.09039v1
- Local PDF: pdf/2026-10-09_21_From High Recall to High Utility_ Dataset-Adaptive Post-Processing of LLM-Generated Customer Intents.pdf

Large language models can extract useful signals from heterogeneous enterprise data, but high-recall extraction often produces outputs that are duplicated, uneven in granularity, semantically overlapping, or too numerous for downstream systems and human reviewers to use effectively. We present a dataset-adaptive post-processing architecture developed for Customer Intent Extraction (CIE), where unstructured customer language is transformed into stable, traceable intent units. The approach separates recall-oriented extraction from utility-oriented reduction. Source-specific preprocessing first isolates evidence from multimodal plans, sparse operational records, and structured opportunity data. Candidate intents are then standardized and deduplicated, optionally enriched with metadata for embedding computation, represented in a shared semantic vector space, and grouped using a clustering strategy selected according to the candidate set's characteristics. Cluster-level keywords provide an explainability layer, while singleton reassignment requires agreement between embedding and keyword similarity. Finally, constrained language-model aggregation produces one concise intent per cluster without introducing unsupported concepts, and the resulting unit retains provenance, clustering, embedding, and generation metadata. This treats post-processing not as cosmetic cleanup, but as a semantic reduction layer converting high-recall LLM outputs into reusable enterprise intelligence. We also describe two downstream applications: Machine-Generated Intents, which infer likely objectives for customers lacking direct evidence from peer customers with similar profiles, and intent-guided semantic retrieval and mapping, which uses the stable intent as a query against a downstream decision space, illustrated here by mapping customer intents to business outcomes.

## 22. Multi-Label Topic Assignment via LLM Distillation: A Comparative Analysis of Generative vs. Discriminative Student Models

- Authors: Sourabh Kasliwal, Shubhranshu Singh
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-06
- DOI: Unavailable
- Categories: cs.LG, cs.CL
- Relevance: 2.9593234114194775
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.09063v1
- PDF: https://arxiv.org/pdf/2610.09063v1
- Local PDF: pdf/2026-10-09_22_Multi-Label Topic Assignment via LLM Distillation_ A Comparative Analysis of Generative vs. Discriminative Student Model.pdf

Multi-label topic assignment for user-generated content (UGC) -- including product reviews and buyer-seller conversations -- poses unique scalability challenges in large-scale e-commerce due to informal language, extreme label sparsity, and rapidly evolving taxonomies. While utilizing Large Language Models (LLMs) as labeling oracles to distill ground-truth data has emerged as an industry standard to bypass prohibitive manual annotation costs, determining the optimal, low-latency architecture for the resulting student models remains an open challenge. To address this, we conduct a comprehensive evaluation across Small Language Model (SLM) parameter scales (1B, 4B, and 8B) and architectural paradigms (causal generative versus bidirectional discriminative). Comparing generative text-to-label classifiers against discriminative baselines (DeBERTa-V3 and ModernBERT), our analysis reveals a crucial data-dependent trade-off: while discriminative models outperform ultra-lightweight generative models on structured product reviews, even the smallest 1B generative model surpasses discriminative baselines on complex, multi-turn conversational data. Furthermore, generative models maintain robust performance under massive label-set expansion (up to 112 topics) and severe long-tail distributions, whereas discriminative baselines suffer a 35% drop in Macro-F1 at scale. Finally, we detail the successful production deployment of these optimized models across both product review and conversational domains, demonstrating strict latency compliance and tangible business impact at a global marketplace scale.

## 23. Shared Low-rank Basis Factorization for Data-free Mixture-of-Experts Compression

- Authors: Tianxiao Cao, Jiahe Shao, Yuning Qiu, Kyohei Atarashi, Hisashi Kashima, Qibin Zhao
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-07
- DOI: Unavailable
- Categories: cs.LG, cs.AI
- Relevance: 2.9587253325621883
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.09342v1
- PDF: https://arxiv.org/pdf/2610.09342v1
- Local PDF: pdf/2026-10-09_23_Shared Low-rank Basis Factorization for Data-free Mixture-of-Experts Compression.pdf

Mixture-of-Experts (MoE) large language models decouple capacity from compute through sparse routing, but their large parameter count creates storage and serving challenges. We analyze three MoE compression families: expert pruning, expert merging, and weight reconstruction, and derive structural error bounds showing that pruning and merging can incur non-vanishing errors tied to routing and expert heterogeneity. In contrast, weight reconstruction avoids these structural costs by preserving expert structure and routing. Motivated by the analysis, we propose Shared Low-rank Basis Factorization (SLBF), a data-free weight reconstruction method that uses rank-$k$ bases shared among experts, enabling richer cross-expert sharing, faster convergence, and lower reconstruction error. A post-hoc gauge fixing removes redundant parameters at no representational cost. Across five MoE architectures spanning 16B to 122B parameters, SLBF consistently outperforms methods from all three compression families.

## 24. MorphCL: Morphological Contrastive Learning for Inertial-based Human Activity Recognition

- Authors: Marius Bock, Yuwei Zhang, Juergen Gall, Michael Moeller, Kristof Van Laerhoven, Cecilia Mascolo
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-07
- DOI: Unavailable
- Categories: cs.LG, cs.HC
- Relevance: 2.9436216923685836
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.10245v1
- PDF: https://arxiv.org/pdf/2610.10245v1
- Local PDF: pdf/2026-10-09_24_MorphCL_ Morphological Contrastive Learning for Inertial-based Human Activity Recognition.pdf

Despite the ubiquity of sensors in wearable and mobile devices and the abundance of human movement data they generate, translating unlabeled recordings into foundational motion models remains an open challenge. Self-supervised learning (SSL) has alleviated the need for costly annotations, yet existing approaches leave the global structure of large-scale motion data largely untapped, relying on randomly sampled batches and local comparisons that become particularly problematic for in-the-wild inertial data dominated by stationary, low-variance behaviors. Here we introduce Morphological Contrastive Learning (MorphCL), a self-supervised pretraining framework that uses structure-aware grouping to inject explicit modeling of global structure into inertial-based SSL approaches. Building on two well-established pillars of motion analysis, the discovery of motion primitives, or motifs, and domain-specific feature descriptors, we show that MorphCL substantially improves linear probing and finetuning results of learned encoders by up to 15 percentage points in F1-score. In a comparison with existing foundation models, we demonstrate that MorphCL-pretrained encoders match or surpass them models in linear probing performance while trained on $4600\times$ less data. Qualitative analysis of the resulting embedding spaces further reveals morphologically meaningful cluster structure, with improved separation of kinematically similar activity classes.

## 25. From Pixel to Coding: Evaluating the Figure Reproduction Capabilities of MLLMs

- Authors: Zijian Chen, Zhengyu Chen, Bohan Liang, Lirong Deng, Yushuo Zheng, Yanwei Jiang, Qi Jia, Kaiwei Zhang, Wenjun Zhang, Guangtao Zhai
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-07
- DOI: Unavailable
- Categories: cs.CV, cs.AI
- Relevance: 2.9419267847890076
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.10066v1
- PDF: https://arxiv.org/pdf/2610.10066v1
- Local PDF: pdf/2026-10-09_25_From Pixel to Coding_ Evaluating the Figure Reproduction Capabilities of MLLMs.pdf

Multimodal Large Language Models (MLLMs) have demonstrated impressive capabilities in both visual understanding and code generation. However, existing benchmarks typically evaluate these two modalities in isolation, lacking a dedicated assessment of their unification, i.e., how a model can perceive complex visual structures and synthesize them into precise, executable code. Moreover, current visual code generation benchmarks often rely on simplified layouts within single programming environments, falling short of evaluating true unified multimodal reasoning. To bridge this gap, we propose FigCodeBench, a comprehensive framework for rigorously evaluating MLLMs on figure reproduction, integrating multimodal comprehension and generation. We first design a systematic dataset construction pipeline, resulting in a total of 6,194 instances that cover 7 functional categories and 4 types of programming languages. We further categorize figure reproduction into three tiers with visual and code complexity modeling, specifically targeting complex structural reasoning, varying aspect ratios, and dense geometric constraints. We introduce a multi-dimensional evaluation protocol, encompassing visual fidelity and syntactic isomorphism, that aligns highly with the Mean Machine Opinion Score (MMOS) and human preferences. Based on our framework, we conducted extensive experiments on 24 widely used proprietary and open-source MLLMs (e.g., Gemini 3.1 Pro, GPT-5.4, and Kimi-K2.5), where we observed a universal, non-linear performance cliff across different programming languages and difficulty scenarios for all models, and gained several insights, such as the significant metric decline in rigid declarative languages.

## 26. GraphOPD: Graph-Augmented On-Policy Distillation for LLM Agents

- Authors: Bohan Lin, Liyi Chen, Zhuoning Guo, Muyang Li, Qimeng Wang, Yan Gao, Yao Hu, Yudong Zhang
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-06
- DOI: Unavailable
- Categories: cs.LG, cs.AI
- Relevance: 2.9244481710472767
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.08959v1
- PDF: https://arxiv.org/pdf/2610.08959v1
- Local PDF: pdf/2026-10-09_26_GraphOPD_ Graph-Augmented On-Policy Distillation for LLM Agents.pdf

On-policy distillation post-trains large language model agents by supplying dense, step-level guidance from a teacher policy when the reinforcement-learning reward is sparse and arrives only once per trajectory. Existing instantiations allocate this guidance by the size of the teacher-student divergence at each step, on the single-turn intuition that a large disagreement marks a mistake worth correcting. Once decisions chain over many turns, that rule misfires, since an early drift enters every later context both policies condition on, leaving the teacher consistent with the drifted trajectory instead of flagging its cause, while interchangeable steps register large but outcome-irrelevant divergences. We demonstrate this on an agentic benchmark, where distilling the highest-divergence steps brings no consistent benefit over random selection. To this end, we introduce GraphOPD, the first method to bring graph-based structural augmentation into on-policy distillation for agent capabilities. It reads which steps enabled which later ones from the environment's own record of state changes, immune to the drift that corrupts the teacher-student gap, organizes them into a dependency graph, scores each step by a random-walk stationary distribution over it, and fuses that structural credit with the divergence signal into a trajectory-relative mask concentrating supervision on each rollout's highest-aptitude steps. Across three model scales and eleven baselines on ALFWorld, WebShop, and SearchQA, GraphOPD shows competitive performance throughout, improving over the strongest baseline by up to +5.8 pp. An executed-replay audit further shows that this structural credit score tracks true causal impact far above chance, that both fused signals are independently necessary, and that the same signal transfers to out-of-domain tool-integrated reasoning.

## 27. Reliability of LLM Judges for Evaluating Entity Alignment

- Authors: Vaibhava Lakshmi Ravideshik, Mayank Kejriwal
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-07
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 2.909337489400068
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.09554v1
- PDF: https://arxiv.org/pdf/2610.09554v1
- Local PDF: pdf/2026-10-09_27_Reliability of LLM Judges for Evaluating Entity Alignment.pdf

Entity Alignment (EA) identifies equivalent entities across knowledge graphs and is critical for knowledge base integration and ontology merging. Evaluating EA systems at scale requires expensive expert annotation, making systematic assessment across diverse domains practically infeasible. LLM-as-judge evaluation offers a potentially scalable alternative, yet its reliability for structured prediction tasks like EA remains unstudied. We present the first systematic benchmarking study across three frontier models, three datasets, and four EA systems, using perturbation bias diagnostics, meta-evaluation across all dataset-judge-prompt combinations, and counterfactual label-flip tests. We identify anchor bias, a failure mode in which judges invert discrimination when the system's decision label is visible. Label exposure causally collapses judge discrimination (J-ROC-AUC 0.12-0.87), while a label-free protocol recovers near-ceiling capability on distinctive-name datasets (0.93-1.00) and significant recovery on biomedical pairs (0.93-0.95). Counterfactual experiments confirm causality (FSR 53-99%) and reveal a frontier model paradox: stronger judges exhibit greater label sensitivity, not less. A blinded two-annotator human evaluation (102 pairs, Cohen's kappa=0.902) confirms this mechanism directly. We release the first biomedical EA benchmark (MeSH-SNOMED CT, 15K pairs) and a reproducible auditing framework for LLM judge reliability in EA. Code and data are available at https://github.com/vaibhavalakshmiravideshik/llm-as-a-judge-entity-alignment.

## 28. Pretraining Shapes Spectral Structure: Architecture- and Strategy-Conditional Prediction of OOD Robustness in Foundation Models

- Authors: Sangyoon Bae, Sk Miraj Ahmed, Shinjae Yoo, Jiook Cha
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-07
- DOI: Unavailable
- Categories: cs.LG
- Relevance: 2.9044612951757074
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.09709v1
- PDF: https://arxiv.org/pdf/2610.09709v1
- Local PDF: pdf/2026-10-09_28_Pretraining Shapes Spectral Structure_ Architecture- and Strategy-Conditional Prediction of OOD Robustness in Foundation.pdf

Can we determine whether a foundation model will generalize out-of-distribution (OOD) before any target data is available? Existing diagnostics require source or target data, which rules them out before a target domain exists. Those that use the weights alone apply one statistic to every architecture, and do not separate robust models from fragile ones. We show the answer is encoded in the spectral structure of pretrained weights. Two forces shape that structure. Architecture determines how information is stored in weight matrices. Pretraining strategy determines what is rewarded. Together they set a spectral geometry that governs OOD robustness. We prove that the OOD accuracy gap is bounded by how tightly the source representations concentrate. A statistic computed from the pretrained weights alone serves as a proxy for that concentration. The direction of that proxy reverses between architecture families. We operationalize it: the direction is stable within one (architecture X strategy) combination, the finest grouping we test, which we call a cell. Pooled over 116 models spanning 7 modalities, a single statistic ranks OOD robustness weakly, because cells of opposite direction cancel. Within a cell, the statistic selected for it orders 92% of model pairs by OOD robustness in-sample. The selection does not leak the target: for each model family outside the matrix we logged the cell, metric and sign before running its OOD evaluation, and the predicted direction held in every case: EEG, genomic and protein. Acting on spectral concentration narrows the OOD gap by 24% at 87.5% ID retention. The diagnostic operates on released weights alone, so OOD robustness becomes checkable at model-selection time, before data or compute is committed to a target domain.

## 29. Open-MMUnlearning: Unifying Methods and Evaluation for MLLM Unlearning

- Authors: Junkai Chen, Yuhao He, Qianshan Wei, Junxiang You, Jingwen Shao, Junkai Lin, Zhongkai Yue, Xiaotian Ye, Zhengbo Jiao, Jiali Cheng, Zhijie Deng, Kening Zheng, Ruiqi Liu, Hadi Amiri, Yi Yu, Zhenan Sun, Qi Li, Ka-Ho Chow, Sijia Liu, Liang Wang, Jiaqi Li, Shu Wu
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-07
- DOI: Unavailable
- Categories: cs.AI
- Relevance: 2.888242790576851
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.10358v1
- PDF: https://arxiv.org/pdf/2610.10358v1
- Local PDF: pdf/2026-10-09_29_Open-MMUnlearning_ Unifying Methods and Evaluation for MLLM Unlearning.pdf

As multimodal large language models (MLLMs) become more capable and widely deployed, concerns about privacy and safety have become increasingly pressing. Machine unlearning offers one approach to addressing these concerns by removing designated information from trained models while preserving unrelated capabilities. However, fragmented implementations and evaluation protocols, incomplete robustness testing, and limited understanding of metric reliability make progress in MLLM unlearning difficult to assess systematically. We introduce Open-MMUnlearning, an open-source, extensible framework that integrates target-model preparation, multimodal data processing, unlearning, and evaluation through shared interfaces and structured configurations. The framework supports five benchmarks spanning privacy, safety, and copyright, eight MLLMs from four model families, and twelve unlearning methods. Its evaluation suite jointly assesses forgetting effectiveness, retained utility, and robustness to model interventions, adversarial inputs, and membership inference attacks. Using a common evaluation protocol, we compare ten representative unlearning methods. In this comparison, GD and MIP-Editor tie for the highest overall score: GD achieves the highest Forget Quality, while MIP-Editor preserves more Model Utility. We further introduce a metric meta-evaluation protocol that tests faithfulness using models with controlled exposure to target knowledge and robustness under quantization and relearning. Among the thirteen evaluated metrics, BLEU achieves the highest aggregate reliability score. KS-Test attains the highest faithfulness AUC but performs less well on robustness. Together, the framework and these findings support reproducible comparison of MLLM unlearning methods and systematic assessment of evaluation reliability.

## 30. AdaPS-LiNGAM: Adaptive Predecessor Selection for Linear Non-Gaussian Acyclic Models under Small-Sample Settings

- Authors: Shun Yanashima, Kentaro Kanamori, Hirofumi Suzuki
- Source: arxiv
- Venue type: preprint
- Journal: Unknown
- Publication status: preprint
- Publication date: 2026-10-07
- DOI: Unavailable
- Categories: cs.LG, stat.ML
- Relevance: 2.868644438925826
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: http://arxiv.org/abs/2610.09782v1
- PDF: https://arxiv.org/pdf/2610.09782v1
- Local PDF: pdf/2026-10-09_30_AdaPS-LiNGAM_ Adaptive Predecessor Selection for Linear Non-Gaussian Acyclic Models under Small-Sample Settings.pdf

Causal discovery becomes particularly challenging when the available sample size is small relative to the number of variables. This challenge also arises in the linear non-Gaussian acyclic model (LiNGAM), an identifiable framework for causal discovery from observational data. DirectLiNGAM estimates a causal order, which arranges variables so that causes precede their effects, by sequentially identifying an exogenous variable and removing its linear effect from the remaining variables. We establish a structural limitation of this procedure: when the number of variables exceeds the sample size, repeated residualization necessarily becomes degenerate before the full causal order can be determined. Our analysis further reveals that each residual can be reconstructed using only a graph-determined subset of variables already placed earlier in the causal order, termed the active boundary. This result motivates AdaPS-LiNGAM (Adaptive Predecessor Selection LiNGAM), which reconstructs each residual directly from the original observations using an adaptively chosen sparse subset of those earlier variables. The same subset-selection principle is also applied to the final pruning step for edge estimation. Experiments on synthetic data demonstrate that AdaPS-LiNGAM provides accurate causal-structure recovery in sample-limited settings and degrades more gradually as the sample size decreases.
