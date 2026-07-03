# Researcher Tracking - 2026-07-03 (daily)

Total new tracked papers: 1
Highlighted papers: 1

## 1. Rethinking Speech-LLM Integration for ASR: Effective Joint Speech-Text Training by Interleaving

- Authors: Ruchao Fan, Yiming Wang, Rui Zhao, Liliang Ren, Keqi Deng, Xiaoyang Chen, Ali Zare, Bo Ren, Yuxuan Hu, Junkun Chen, Yan Huang, Yelong Shen, Jinyu Li
- Source hits: arxiv
- Matched researchers: Yuxuan Hu
- Matched groups: N/A
- Confidence: medium (author_alias)
- Topic keywords: N/A
- Journal/source: arxiv
- Publication date: 2026-07-02
- Article: http://arxiv.org/abs/2607.01733v1

Speech-LLM integration has shown promising results by leveraging extensive textual pretraining, yet its specific benefits for automatic speech recognition (ASR) remain unclear. We observe that as supervised ASR training data increases, the contribution of LLM priors becomes less evident, and simple speech-text joint training under-utilizes textual knowledge. We therefore propose Joint Speech-Text Interleaved Pretraining (JSTIP), an ASR-oriented pretraining strategy that constructs word-level and segment-level interleaved speech-text sequences within aligned pairs for speech-LLM architectures that accept continuous inputs. Experiments on 38k hours of ASR data show consistent entity accuracy improvement compared to ASR-only and joint speech-text training baselines. JSTIP achieves on-par entity recognition performance using domain transcription text compared to synthetic speech-text pairs, simplifying domain adaptation. Benefiting from textual pretraining and domain text data, JSTIP is competitive with open-source ASR and Speech-LLM systems in medical entity recognition. The zero-shot speech question answering behaviors further suggest that interleaving reduces the speech-text modality gap and preserves the LLM generative prior, which is likely the reason for the entity improvements on the ASR task.
