# Researcher Tracking - 2026-07-02 (daily)

Total new tracked papers: 1
Highlighted papers: 1

## 1. Dual Sparse Aggregation Transformer for Multispectral Object Detection

- Authors: Wencong Wu, Xiuwei Zhang, Hanlin Yin, Hongxi Zhang, Yanning Zhang
- Source hits: arxiv
- Matched researchers: Xiuwei Zhang
- Matched groups: N/A
- Confidence: medium (author_alias)
- Topic keywords: N/A
- Journal/source: arxiv
- Publication date: 2026-06-30
- Article: http://arxiv.org/abs/2606.31015v1

Transformer-based approaches have obtained excellent performance in multispectral object detection tasks due to their ability to model long-range dependencies and capture complementary information. However, previous transformer-based multispectral detection methods tend to use all available tokens for similarity calculation, which results in redundant information interaction from irrelevant areas, leading to degraded detection performance. To overcome this challenge, we propose a novel Dual Sparse Aggregation Transformer (DSAFormer) for multispectral object detection, which consists of a Dual Sparse Transformer (DSFormer) and a Learnable Addition Fusion Block (LAFB). Specifically, the DSFormer is designed to exploit and boost cross-modal complementary information, thereby improving detection performance. It incorporates three key components: A Spatial Sparse Multi-Head Cross-Attention (SSMHCA) mechanism selectively captures cross-modal relationships at the spatial level by reserving only the high query-key similarity scores, eliminating irrelevant interactions. A Channel Sparse Multi-Head Cross-Attention (CSMHCA) mechanism performs similar sparse calculations at the channel level to enhance feature representation and filter out low matching query-key. A Multi-Scale Feature Refinement Layer (MSFRL) is developed to aggregate hierarchical features and suppress redundant information. To effectively fuse multimodal features, the LAFB is introduced to aggregate intramodal and intermodal feature information by feature reweighting. Extensive experimental results have demonstrated that our proposed DSAFormer achieves better detection performance against state-of-the-art methods on four public datasets, including the MFAD, FLIR, M$^3$FD, and LLVIP. The source code of our DSAFormer will be released at https://github.com/WenCongWu/DSAFormer.
