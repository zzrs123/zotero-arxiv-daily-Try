# Researcher Tracking - 2026-08-27 (daily)

Total new tracked papers: 5
Highlighted papers: 5

## 1. Impact of Nuclear Level Density on $r$-Process Rare-Earth Peak Nucleosynthesis

- Authors: Hang Xu, Peng-Xiang Du, Jian Li, Dong-Liang Fang
- Source hits: arxiv
- Matched researchers: Hang Xu
- Matched groups: N/A
- Confidence: medium (author_alias)
- Topic keywords: N/A
- Journal/source: arxiv
- Publication date: 2026-08-26
- Article: http://arxiv.org/abs/2608.25440v1

The rare-earth peak ($A\sim164$) is a prominent feature of the $r$-process, and previous theoretical studies suggest that it is possibly linked to local nuclear structural effects. However, the nuclear level density (NLD), a physical quantity directly reflecting these properties, has been largely overlooked compared to other structural properties such as nuclear masses. To address this, we perform $r$-process simulations across three astrophysical scenarios using neutron-capture rates derived from six distinct NLD models. Our results reveal that microscopic models yield systematic deviations in NLD relative to phenomenological ones, leading to critical impacts on nucleosynthesis. Specifically, systematic NLD differences in even-$A$ nuclei redirect the nuclear flow, accelerating the early formation of the rare-earth peak and temporarily enhancing its magnitude. This underlying structural shift also fundamentally alters the $r$-process sensitivity to the neutron-capture rate, effectively eliminating its dependence on the odd-even nature of protons. Overall, these findings demonstrate that the internal nuclear structure encoded within NLDs can collectively induce a global redirection of the nucleosynthesis pathway, highlighting the critical need for self-consistent microscopic inputs in future simulations.

## 2. PaSta: Noisy Node Classification with Partial Label Learning

- Authors: Yujing Liu, Yixin Liu, Yu Zheng, Yue Tan, Alan Wee-Chung Liew, Shirui Pan
- Source hits: arxiv
- Matched researchers: Yixin Liu
- Matched groups: N/A
- Confidence: medium (author_alias)
- Topic keywords: N/A
- Journal/source: arxiv
- Publication date: 2026-08-26
- Article: http://arxiv.org/abs/2608.25365v1

Noisy node classification problem is a fundamental yet challenging task for real-world graph-related web services, where node labels are often corrupted or unreliable due to weak supervision or automatic annotation. However, existing methods typically train models based on one-hot labels, which not only makes models susceptible to overfitting on noisy labels, but also leads to error accumulation after pseudo-label-guided enhancement. In this paper, we propose a novel Partial label-based Self-training framework (PaSta for short) that leverages partial label learning technique to overcome the limitations of existing methods. Specifically, PaSta first trains multiple annotators to comprehensively capture the class distribution of nodes and aggregates their predictions to construct high-quality partial labels. Subsequently, we design a partial label-based classification model with two well-crafted loss functions to guide the model learning at both label and representation spaces. To further enhance the robustness against noisy labels, we introduce a self-training strategy where the labels refined by partial label learning are then used to further optimize the annotators in a closed-loop iterative manner. Extensive experiments on five datasets demonstrate that, compared with existing state-of-the-art methods, PaSta achieves an average improvement of 1.1% in classification performance under various noise settings.

## 3. Unfolding Scientific Papers into Multi-Turn Generation Trajectories for Continued Pre-Training

- Authors: Qiankai Xu, Qiguang Chen, Zixin Su, Wenhao Huang, Yue Gao, Jiaheng Liu, Ge Zhang
- Source hits: arxiv
- Matched researchers: Yue Gao
- Matched groups: N/A
- Confidence: medium (author_alias)
- Topic keywords: N/A
- Journal/source: arxiv
- Publication date: 2026-08-26
- Article: http://arxiv.org/abs/2608.25826v1

A recent line of synthetic-data work reconstructs the thinking behind existing text rather than rewriting the text itself, but it operates on short web passages, recovers only local thoughts, and leaves the structure of whole documents untouched. Scientific papers are written to a clear and largely uniform structure and make a natural substrate for lifting this paradigm to the document level. We present a pipeline that unfolds each paper into a multi-turn generation trajectory in which a teacher model reconstructs the writing process of the whole paper: a writing request, a global plan, and pre-writing deliberation for each section. All section texts and the abstract are kept verbatim from the source paper. We apply the pipeline to quality-filtered arXiv papers and obtain a corpus for continued pre-training (CPT) that is roughly twice the size of the source text. The same reverse construction extends to instruction data and evaluation. Treating real paper text as the answer yields an SFT dataset. Anchoring tasks in held-out papers yields PAW-Bench, an academic-writing benchmark whose tasks carry their own rubrics and checklists. In controlled experiments CPT on our corpus followed by supervised fine-tuning on public datasets improves writing benchmarks broadly while preserving general reasoning and improving long-document reading. The writing gain persists even when every model is fine-tuned on a dedicated writing SFT dataset. Mixing our SFT data into that recipe lifts academic writing further.

## 4. TRACE: An Evidence-Grounded Benchmark for Safety Evaluation of Large Reasoning Models

- Authors: Zhenyu Wu, Siyuan Chen, Changchun Yang, Jiaqi Dong, Min Zhou, Ali Almadan, Talal Hammad, Faisal Wahbo, Aminullah Tora, Mona Alshahrani, Xin Gao
- Source hits: arxiv
- Matched researchers: Xin Gao
- Matched groups: N/A
- Confidence: medium (author_alias)
- Topic keywords: N/A
- Journal/source: arxiv
- Publication date: 2026-08-25
- Article: http://arxiv.org/abs/2608.24232v1

Large Reasoning Models (LRMs) generate intermediate reasoning traces that may contain unsafe content, even when their final responses appear safe. Guardrail models are designed to detect and block unsafe content, yet existing benchmarks for unsafe content detection focus primarily on prompts and final responses, leaving reasoning traces largely unexamined. Moreover, these benchmarks typically provide only binary safety labels, without evidence annotations that justify the judgments. To address these limitations, we introduce TRACE, an evidence-grounded safety evaluation benchmark that covers the entire LRM inference pipeline: prompts, reasoning traces, and final responses. TRACE includes prompts in two languages spanning nine risk categories and ten attack strategies. For each prompt, four LRMs generate reasoning traces and final responses, and we annotate the safety of each component and extract supporting evidence from the corresponding source text. Evaluating 18 guardrail models on TRACE reveals that safety judgment for reasoning traces is substantially more challenging than for prompts or final responses, and that current models struggle to accurately extract supporting evidence. These findings highlight the need for guardrail models that can reliably detect and precisely localize unsafe content across the LRM inference pipeline.

## 5. Maia 200: A Software Defined Dataflow System for Large-scale AI Acceleration

- Authors: Sherry Xu, Marco Heddes, Jackson Peng, Tom Savell, Monica Tang, Prashant Ranjan, Jesse Benson, Ofer Dekel, Saurabh Dighe, Anupama Kurpad, Artour Levin, Matthew Mattina, George Petre, Cheng Tang, Yuan Yu, Li Zhang, Torsten Hoefler
- Source hits: arxiv
- Matched researchers: Torsten Hoefler
- Matched groups: N/A
- Confidence: medium (author_alias)
- Topic keywords: N/A
- Journal/source: arxiv
- Publication date: 2026-08-25
- Article: http://arxiv.org/abs/2608.24664v1

We introduce Maia 200, an advanced AI accelerator delivering high performance-10 145 Tflop/s FP4 and 5072 Tflop/s FP8 within a 750W TDP and 7 TB/s HBM bandwidth. Maia exemplifies a new class of Software Defined Locally Accessed Dataflow Architectures (SDLA), which explicitly program dataflow engines to orchestrate highly specialized memories and data movement engines. This approach shifts the focus from today's thread-centric to data-movement-centric architecture, improving efficiency and scalability. Our taxonomy of data management, inspired by Flynn's classification, highlights how SDLA addresses challenges in modern AI computing. Maia 200 achieves significant cost and energy savings while supporting massive parallelism for AI inference workloads, making it a compelling solution for next-generation high-performance computing systems.
