# Researcher Tracking - 2026-10-17 (daily)

Total new tracked papers: 4
Highlighted papers: 4

## 1. DK-VLM: Geometry as Position for Spatial Reasoning in Vision-Language Models

- Authors: Han Su, Meng Tian, Tianyu Huang, Mingyu Gao, Lennox Wei, Dongxu Li, Jianhua Han, Hang Xu, Xiaohe Wu, Wangmeng Zuo
- Source hits: arxiv
- Matched researchers: Hang Xu
- Matched groups: N/A
- Confidence: medium (author_alias)
- Topic keywords: N/A
- Journal/source: arxiv
- Publication date: 2026-10-15
- Article: http://arxiv.org/abs/2610.22356v1

Vision-language models still struggle to understand 3D spatial relations across views and update spatial judgments as the observer moves. A common approach fuses 3D reconstruction features into visual tokens, but aligning these features with pretrained semantic representations remains challenging under limited spatial supervision. We propose DK-VLM with Dual-Kernel Attention, which computes attention from both a visual token's input position and its geometric position in the scene. A semantic kernel retains the pretrained model's native attention and positional encoding, while a separate geometric kernel uses estimated 3D points and camera poses to directly modulate attention through point displacements and relative view transformations. Then, a learned gate fuses their outputs. Geometry thus enters attention as position rather than as fused reconstruction features. We further introduce Reference-Frame Composition (RC) supervision to train the model to update its reference frame across successive judgments. It provides stepwise turn and heading targets derived from verified single-step annotations. Among the compared methods, DK-VLM-8B achieves the highest average score across six spatial benchmarks and the highest overall scores on VSI-Bench (74.33) and ReVSI-32 (58.28). RC supervision further improves multi-step spatial reasoning, while the full model preserves general video understanding. Project page: https://sumuru789.github.io/DK-VLM-website/.

## 2. Memorilla: Latent Semantic Memory for LLMs

- Authors: Adibvafa Fallahpour, Parsa Idehpour, Vignesh Kothapalli, Nikita Mounier, Shirley Wu, Shayan Pardis, Jure Leskovec
- Source hits: arxiv
- Matched researchers: Jure Leskovec
- Matched groups: N/A
- Confidence: medium (author_alias)
- Topic keywords: large language model
- Journal/source: arxiv
- Publication date: 2026-10-15
- Article: http://arxiv.org/abs/2610.21375v1

Memory enables large language models (LLMs) to use information beyond their parameters, such as past user conversations, long documents, or an agent's earlier actions. For a frozen LLM, access to this accumulated knowledge is limited to what a memory system places in its context window. However, gathering and combining relevant information needed for each query while keeping the model's context short remains challenging for existing systems. Here we introduce Memorilla, a memory system that gathers information from an entire document collection into a fixed number of query-dependent 'memory tokens' for a frozen LLM. Memorilla encodes documents (such as user chats, book chapters) once into reusable embeddings, then learns to retrieve and place query-specific information in the LLM's input embedding space. Using only 16 memory tokens, Memorilla achieves the best performance against baselines including Mem0 and MemoRAG on five of eight benchmarks spanning personalization, long-document and knowledge-intensive question answering. Notably, on FactKG, it reaches 84.33% accuracy versus 80.43% with full-context inference, while using 108x fewer tokens to represent the source documents. Furthermore, Memorilla can facilitate continual learning in agentic systems where the document count (the agent's past turns) increases throughout the trajectory. In a TextWorld environment, we show that Memorilla reduces the agent's tendency to wander between rooms it has already explored, and improves its average success rate from 18.6% with full-history in-context learning to 24.2%. Overall, Memorilla aids frozen LLMs in accumulating and using knowledge effectively across long-context interactions and takes a step towards building continually learning AI systems.

## 3. Interfaces and Modules: A Scalable Representation for Weight-Space Learning across Architectures

- Authors: Michał Kozyra, Michael Bronstein
- Source hits: arxiv
- Matched researchers: Michael Bronstein
- Matched groups: N/A
- Confidence: medium (author_alias)
- Topic keywords: N/A
- Journal/source: arxiv
- Publication date: 2026-10-15
- Article: http://arxiv.org/abs/2610.21995v1

Weight-space learning across architectures requires representations that respect parameter symmetries and scale to large networks. Existing equivariant tensor encoders require architecture-specific symmetry specifications, while neuron graphs make global attention costly. We introduce a typed graph organized around shared coordinate-permutation actions. Its nodes, called interfaces, represent coordinate spaces whose bound tensor axes must be permuted jointly; operation occurrences, called modules, form typed hyperedges. A compiler derives this graph from supported PyTorch models, with exact recovery of the permutation factors defined by its constraints. The Universal Weight Encoder (UWE) combines local equivariant updates to parameter features with global attention over invariant interface summaries. The small number of interfaces makes global attention practical, and a single encoder processes different supported architectures. UWE is competitive with architecture-specific state-of-the-art methods on established benchmarks. On a new zoo of 1,200 transformers spanning 100 architectures, it outperforms the evaluated baselines at ranking networks within unseen architectures, including architectures larger than those used for training, while using substantially less memory.

## 4. BiShield-TEE: On the (In-)Security of Unilateral Weight Obfuscation in On-Device TEE-Shielded LLM Partition

- Authors: Zhiyuan Wang, Yuezhi Zhou, Ziqi Zhang, Zhu Zhang, Zhixing Tan, Yongheng Deng
- Source hits: arxiv
- Matched researchers: Ziqi Zhang
- Matched groups: N/A
- Confidence: medium (author_alias)
- Topic keywords: large language model
- Journal/source: arxiv
- Publication date: 2026-10-15
- Article: http://arxiv.org/abs/2610.21565v1

On-device deployment of large language models (LLMs) is increasingly adopted due to latency and privacy requirements, but exposes proprietary models to reverse engineering and intellectual property theft. Trusted Execution Environments (TEEs) provide hardware-enforced isolation for on-device inference, yet most TEE-based parameter obfuscation relies on unilateral matrix transformations that obfuscate only output side. We identify a vulnerability in this design, termed the \emph{Solution Determinacy Property (SDP)}: the obfuscation secret is uniquely determined, exposing the structure of the true key and enabling attackers to break the protection. Under our attacks, representative methods \textsc{GroupCover} and \textsc{ArrowCloak} are reduced to negligible protection, with attack accuracy reaching over $2.4\times$ the full-shielding black-box baseline and recovering near-complete model functionality.To address this vulnerability, we propose \textsc{BiShield-TEE}, a bilateral framework that induces \emph{Ambiguous Solutions} through joint obfuscation of input and output dimensions, hiding the true key among many equally valid candidates. Experiments across diverse models and datasets show that \textsc{BiShield-TEE} confines attack accuracy to the full-shielding black-box baseline, while achieving higher inference efficiency than prior methods on real hardware.Our code is available at https://github.com/laduiw/BiShield-TEE.
