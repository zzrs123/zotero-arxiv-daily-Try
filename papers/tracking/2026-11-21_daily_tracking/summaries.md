# Researcher Tracking - 2026-11-21 (daily)

Total new tracked papers: 1
Highlighted papers: 1

## 1. A Complete Geometric Message-Passing Architecture for Point Clouds

- Authors: Nadav Dym, Tal Amir, Gia Chi Dang, Christopher Morris
- Source hits: arxiv
- Matched researchers: Christopher Morris
- Matched groups: N/A
- Confidence: medium (author_alias)
- Topic keywords: N/A
- Journal/source: arxiv
- Publication date: 2026-11-19
- Article: http://arxiv.org/abs/2611.26384v1

Three-dimensional point clouds are a fundamental data modality, and a large family of machine learning architectures has been developed to respect their natural symmetries to rigid motions and permutations. A principled way to compare these architectures, which vary widely in complexity and cost, is through their expressive power. That is, an architecture is complete if it can distinguish any two inputs not related by the symmetries it respects. Simple distance-based message-passing networks are known to be incomplete, and while there exist complete alternatives, they typically rely on computationally intensive mechanisms like high-order representations of the rotation group or higher-order Weisfeiler-Leman-type tests.
  In this work, we devise a novel, simple, equivariant message-passing architecture for point clouds, and prove that it is complete. We complement our theoretical result with experiments showing that our architecture separates challenging point clouds that distance-based message passing provably cannot distinguish. Our results suggest that high-order equivariant features may not be necessary to enhance the expressivity of point cloud architectures, and can help settle completeness for other equivariant architectures for which such results are currently unknown. We give initial evidence for this by proving completeness of a slightly modified version of SEGNN.
