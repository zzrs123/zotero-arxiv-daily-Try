# Researcher Tracking - 2026-10-22 (daily)

Total new tracked papers: 2
Highlighted papers: 2

## 1. Where Does Timbre Hide? Localizing Speaker Information in Speech Signals

- Authors: Yiquan Zhou, Yixuan Wang, Xiaozhe Qi, Xin Gao, Shihao Li
- Source hits: arxiv
- Matched researchers: Xin Gao
- Matched groups: N/A
- Confidence: medium (author_alias)
- Topic keywords: N/A
- Journal/source: arxiv
- Publication date: 2026-10-21
- Article: http://arxiv.org/abs/2610.29150v1

Timbre similarity is a key evaluation target for generative speech systems, including voice conversion, speaker-cloning text-to-speech, and zero-shot speech models. When the generated voice does not match the target speaker, the problem often reflects imperfect separation of speaker-related timbre from content, making it important to identify where timbre information resides and which representations still carry it. Using speaker identity as a measurable proxy, we probe frequency bands, phase/magnitude structure, WORLD source/filter decomposition, voiced/unvoiced regions, self-supervised learning (SSL) layers, EnCodec/HuBERT tokens, and a 45-listener test across Mandarin, English, and Japanese speech/singing data. Speaker information is distributed: 1--8 kHz magnitude and vocal-tract spectral-envelope structure dominate perception, above-8 kHz bands remain machine-discriminative, shallow SSL layers expose compact speaker information, and token leakage depends on tokenizer/layer choice. These findings indicate where generation systems should condition on or transform speaker information, and where content, codec, and token pipelines should audit residual speaker leakage.

## 2. Seeing through Denoising: Frequency-guided One-step Denoising for Infrared Small Target Detection

- Authors: Xuelin Qian, Zixuan Wang, Chang Xu, Dingwen Zhang, Junwei Han
- Source hits: arxiv
- Matched researchers: Junwei Han
- Matched groups: N/A
- Confidence: medium (author_alias)
- Topic keywords: diffusion
- Journal/source: arxiv
- Publication date: 2026-10-21
- Article: http://arxiv.org/abs/2610.29361v1

Infrared small target detection (IRSTD) is a challenging task due to the extremely small size of targets, low signal-to-noise ratios, and heavy background clutter in infrared imagery. While the progress of deep learning has advanced this field, existing methods primarily adopt discriminative paradigms that directly map images to target masks, overlooking the potential of generative modeling. In this paper, we propose DiffIRSTD, a novel generative framework that reformulates infrared small target detection as a background reconstruction problem. Instead of explicitly predicting target regions, we reinterpret small targets as noise-like signals and leverage a diffusion-based model to recover a clean, target-free background from a perturbed input image. The residual between the reconstructed background and the original image is then exploited to highlight candidate target regions, providing explicit cues for subsequent detection. To address the computational cost typically associated with diffusion sampling, we introduce a one-step denoising strategy that enables efficient background reconstruction while maintaining practical inference speed. Furthermore, we present a frequency-guided perception loss to preserve high-frequency background details and focus more on the reconstruction quality of target regions. More importantly, our DiffIRSTD operates as a plug-and-play framework, compatible with existing IRSTD models without increasing the computational complexity of detectors. Extensive experiments on IRSTD-1K, NUAA-SIRST, and NUDT-SIRST datasets demonstrate the superiority of our method, achieving state-of-the-art performance across three benchmarks.
