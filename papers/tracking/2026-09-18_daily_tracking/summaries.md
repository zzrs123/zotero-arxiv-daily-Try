# Researcher Tracking - 2026-09-18 (daily)

Total new tracked papers: 1
Highlighted papers: 1

## 1. Position Anchor Tuning: Towards Efficient Adaptation of Pre-Trained Point Cloud Transformers

- Authors: Zheng Liu, Xin Gao, Jinchao Zhu, Gao Huang
- Source hits: arxiv
- Matched researchers: Xin Gao
- Matched groups: N/A
- Confidence: medium (author_alias)
- Topic keywords: N/A
- Journal/source: arxiv
- Publication date: 2026-09-16
- Article: http://arxiv.org/abs/2609.18056v1

Parameter-efficient fine-tuning (PEFT) has recently emerged as a pivotal research direction for adapting pre-trained point cloud transformers to diverse downstream tasks. Although existing methods achieve excellent fine-tuning performance with high parameter efficiency, they ignore inference efficiency. To tackle this problem, a novel PEFT method termed position anchor tuning (PAT) is proposed in this paper. As multi-head attention (MHA) and feed-forward network (FFN) are computation-heavy blocks in pre-trained transformers, PAT decreases their computational cost through token aggregation-expansion pairs. Each pair comprises a token aggregation module (TAM) and a token expansion module (TEM). For MHA and FFN blocks, TAMs extract representative tokens from their input tokens based on position anchors in 3D space. These extracted tokens, rather than the original input tokens, are processed by the blocks, thereby reducing the number of tokens involved in computation. Then, TEMs propagate the learned representations back to the original input tokens. Since TAMs are solely responsible for capturing task-specific representations, base-sharing low-rank adaptation (BSLoRA) is further introduced to enable them to learn such representations effectively with only a small number of trainable parameters. Extensive experiments on widely used benchmarks demonstrate that PAT performs comparably to state-of-the-art methods while incurring significantly lower computational overhead and fewer trainable parameters.
