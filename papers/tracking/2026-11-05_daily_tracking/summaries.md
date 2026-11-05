# Researcher Tracking - 2026-11-05 (daily)

Total new tracked papers: 3
Highlighted papers: 3

## 1. Sheaf-MPNN: A Library for Sheaf Neural Networks as Message Passing

- Authors: Alessio Borgi, Mario Severino, Luke Braithwaite, Steve Azzolin, Rémi Bourgerie, Olga Zaghen, Emanuele Mule, Riccardo Ali, Leo Minh Kustermann, Edoardo Coppola, Antonio Purificato, Stefano Fiorini, Christopher Irwin, Filippo Spiga, Fabrizio Silvestri, Michael Bronstein, Pietro Liò
- Source hits: arxiv
- Matched researchers: Michael Bronstein
- Matched groups: N/A
- Confidence: medium (author_alias)
- Topic keywords: diffusion
- Journal/source: arxiv
- Publication date: 2026-11-03
- Article: http://arxiv.org/abs/2611.04670v1

Standard Graph Neural Networks (GNNs) implicitly assume that neighboring nodes share the same feature space, which contributes to oversmoothing and poor performance on heterophilic graphs. Sheaf Neural Networks (SNNs) remove this assumption by giving each node and edge its own vector space and learning restriction maps that transform features as they move between neighbors. These maps define a sheaf Laplacian that drives diffusion over the graph, but existing implementations often assemble it explicitly as a global sparse block matrix, which adds memory and computational overhead and can hinder scalability. In this paper, we introduce Sheaf-MPNN, a PyTorch Geometric library that reformulates sheaf diffusion as local incidence-wise transport and aggregation, eliminating the need to construct the global Laplacian. Sheaf-MPNN implements fifteen families of SNNs under a unified message-passing framework, each supporting both homogeneous and heterogeneous graphs, and directed and undirected settings, with diagonal, general, orthogonal, and low-rank restriction maps and attention-based predictors. We further provide a unified benchmarking suite covering node- and graph-level tasks, heterogeneous graph learning, and computational efficiency, enabling systematic and reproducible comparisons across architectures. We establish theoretical equivalence between these message-passing formulations and their original counterparts and identify the architectural mechanisms needed to preserve their propagation dynamics. This unified perspective provides a principled foundation for implementing, comparing, and extending sheaf-based architectures within standard graph learning frameworks. Source code is available at https://github.com/alessioborgi/sheaf-mpnn.

## 2. ReListen: Training-Free Evidence Localization in Hour-Long Audio with Frozen Audio Language Models

- Authors: Ming-Hao Hsu, Shujie Liu, Yuxuan Hu, Yuxiang Wang, Yingda Shen, Jinyu Li, Zhizheng Wu
- Source hits: arxiv
- Matched researchers: Yuxuan Hu
- Matched groups: N/A
- Confidence: medium (author_alias)
- Topic keywords: N/A
- Journal/source: arxiv
- Publication date: 2026-11-03
- Article: http://arxiv.org/abs/2611.04480v1

Audio language models are meant to answer questions from the audio itself, but an hour-long recording rarely fits in their context, and the answer often depends on a few seconds of it. Transcribing the recording first makes it fit but discards sounds and voices, while systems that return to the audio must be trained for this behavior. We propose ReListen, a training-free method in which a frozen audio language model finds its own evidence before answering. In a Jev-style scan, the model scores each 20-second window by the probability that it helps answer the question, and it then answers from the highest-scoring minute. This minute overlaps the annotated evidence far more often than transcript retrieval, for 88.5% of VoiceGiraffe questions. Without any change, the same scan also grounds events on LAT-Bench as well as a model trained for temporal grounding. Answering from it matches or exceeds hearing the whole recording with a small fraction of the audio, and on VoiceGiraffe it exceeds a transcript of the whole recording by 9.2 points. The selected evidence is also worth hearing rather than reading. Given the same excerpts, reading their transcript matches listening on speech content, but listening is clearly more accurate on questions about sounds and voices. Moreover, ReListen answers faster than every transcript-based system, and its memory stays constant even for recordings too long to hear whole on one GPU. Therefore, a frozen audio language model can search hour-long recordings by itself, without a transcript or additional training.

## 3. OCR in the Foundation Model Era: From Specialist Models to Unified Models

- Authors: Zhiheng Li, Zongyang Ma, Jiaxian Chen, Cheng Cui, Yi Liu, Ziqi Zhang, Chunfeng Yuan, Bing Li, Xiang Bai, Weiming Hu
- Source hits: arxiv
- Matched researchers: Ziqi Zhang
- Matched groups: N/A
- Confidence: medium (author_alias)
- Topic keywords: foundation model
- Journal/source: arxiv
- Publication date: 2026-11-03
- Article: http://arxiv.org/abs/2611.04874v1

Optical Character Recognition (OCR) is among the oldest and most widely deployed applications of artificial intelligence. This survey reviews its development, focusing on the Foundation Model Era. We define OCR through faithful transcription: within a specified visual scope, OCR should completely reconstruct the text, notation, and document structure observable in the source image, and every textual, notational, or structural element in the output must be verifiable from visual evidence in that image. We trace the development from specialist OCR models toward unified models, examining joint text detection and recognition, structured sequence generation, and the use of pretrained vision-language models (VLMs). We organize contemporary OCR systems into five coexisting families: modular toolkits and task-specific models, specialized document VLMs, hybrid workflows, general-purpose VLMs, and commercial products and managed services. We compare their architectures, data, and training, examining hallucination and omission, insufficient spatial grounding, and inference cost in generative OCR. We review evaluation from character and scene text recognition to parsing individual structural elements and full-page transcription, highlighting gaps in consistent output definitions, attribution of performance to individual components, and coverage of real capture conditions and visible content and structure. Finally, we summarize the challenges facing OCR and discuss directions for future research. We continuously track related work at https://github.com/zhihengli-casia/Awesome-OCR-in-the-Foundation-Model-Era.
