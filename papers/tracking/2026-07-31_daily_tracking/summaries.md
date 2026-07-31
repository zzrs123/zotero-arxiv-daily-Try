# Researcher Tracking - 2026-07-31 (daily)

Total new tracked papers: 2
Highlighted papers: 2

## 1. CORE: In-Context Reconstruction for Unified Tabular Anomaly Detection

- Authors: Yunfeng Zhao, Qingfeng Chen, Yue Tan, Shiyuan Li, Yili Wang, Yixin Liu, Shirui Pan
- Source hits: arxiv
- Matched researchers: Yixin Liu
- Matched groups: N/A
- Confidence: medium (author_alias)
- Topic keywords: N/A
- Journal/source: arxiv
- Publication date: 2026-07-30
- Article: http://arxiv.org/abs/2607.27615v1

Tabular anomaly detection (TAD), which focuses on identifying abnormal samples that deviate from the majority in tabular data, has received growing attention. Recently, there has been an emerging trend towards unified TAD, which seeks to detect anomalies across different datasets using a single generalizable model. In unified TAD, aligning heterogeneous data remains challenging. While existing methods often rely on distance-based unified feature construction, they may obscure the semantics of the original features. Moreover, existing approaches typically formulate anomaly detection as a binary classification task, which may overlook diverse anomaly patterns from various datasets and be misled by unrepresentative synthetic anomalies. To address these challenges, we propose an in-COntext REconstruction approach for unified TAD (CORE for short). It introduces a decorrelated feature alignment module to directly align heterogeneous features into a unified representation space, which retains their semantic information. Meanwhile, CORE formulates unified TAD as an in-context reconstruction problem, eliminating the need for labeled or synthesized anomalies. Specifically, the in-context reconstruction module reconstructs each sample by leveraging contextual normal samples to capture dataset-specific distributions, such that reconstruction errors reflect its deviation from normality, facilitating unified TAD on arbitrary unseen datasets.

## 2. Beyond KV Reconstruction: Functional Reconstruction for MLA Draft Models in Speculative Decoding

- Authors: Weiye Shi, Fanxu Meng, Muhan Zhang
- Source hits: arxiv
- Matched researchers: Muhan Zhang
- Matched groups: N/A
- Confidence: medium (author_alias)
- Topic keywords: N/A
- Journal/source: arxiv
- Publication date: 2026-07-29
- Article: http://arxiv.org/abs/2607.27269v1

Multi-head latent attention (MLA) is increasingly important for long-context LLM inference because compact latent states replace the growing key-value (KV) cache and reduce decoding memory traffic. Yet most capable open checkpoints use multi-head or grouped-query attention (MHA/GQA), so conversion is needed to obtain MLA's cache efficiency without retraining from scratch. Speculative decoding offers complementary acceleration, but its speedup depends on agreement between draft proposals and target verification. We find that direct MHA/GQA-to-MLA conversion can sharply reduce this agreement: low-rank factorization and RoPE handling introduce attention-function errors that may be tolerable for standalone generation but substantially lower draft-token acceptance. We therefore formulate MLA draft construction as functional reconstruction rather than cache compression. Our end-to-end (E2E) method optimizes each converted MLA attention module to reproduce the post-output-projection response of its original MHA/GQA counterpart on calibration hidden states. This converter-agnostic post-conversion procedure preserves the converted cache and inference graph and requires neither verifier logits nor verifier supervision. We evaluate 192 model-converter-backend-method-task configurations spanning four Llama/Qwen draft-target pairs, TransMLA and MHA2MLA, HF and vLLM, and four 200-prompt tasks. With a 0.5-percentage-point reporting tolerance, Functional Reconstruction materially improves acceptance in 37 of 64 matched task cells, leaves 26 practically unchanged, and materially decreases one. Code and evaluation artifacts are available at https://github.com/swyhahaha/FunctionalMLA.
