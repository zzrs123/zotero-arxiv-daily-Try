# Researcher Tracking - 2026-10-21 (daily)

Total new tracked papers: 2
Highlighted papers: 2

## 1. Parallel Language Models via Variational Decoding

- Authors: Felix Draxler, Robin C. Geyer, Daniel Geyfman, Farrin Marouf Sofian, Justus Will, Philipp Hildebrandt, Giosue Migliorini, Prakhar Srivastava, Gagan Sai Trinadh Duggaraju Peddiraju, Kushagra Pandey, Jorge da Silva Gonçalves, Elijah Tavares, Jan Niklas Groeneveld, Yang Meng, Julia E. Vogt, Stephan Mandt
- Source hits: arxiv
- Matched researchers: Jorge Goncalves
- Matched groups: N/A
- Confidence: medium (author_alias)
- Topic keywords: diffusion
- Journal/source: arxiv
- Publication date: 2026-10-19
- Article: http://arxiv.org/abs/2610.26693v1

Autoregressive language models emit one token per forward pass. This causes high inference latency, in particular as models are scaled up for quality. In this paper, we introduce Parallel Language Models (PLMs), which generate mutually consistent tokens in one forward pass by routing dependencies through latent auxiliary variables. PLMs are trained using a variational bound that reduces to an autoregressive loss plus a parallel decoding loss. Empirically, PLMs are on a faster and better Pareto frontier than autoregressive and discrete diffusion baselines. Pretrained PLMs achieve near-autoregressive pretraining loss on model scales of 80M to 3B parameters, and speedup follows a power law in model size. When post-trained, our 1.3B model matches or exceeds an identically trained autoregressive model on math, coding, and instruction-following benchmarks, speeding up inference $2.3\text{-}5.7\times$. Together, we show that parallel generation can be trained from a single training objective at autoregressive quality. We will make our code available at https://github.com/mandt-lab/plm.

## 2. Logit Averaging During Training Sets a New State of the Art for Non-Invasive Speech BCI

- Authors: Miran Özdogan, Gereon Elvers, Michael Bronstein, Oiwi Parker Jones
- Source hits: arxiv
- Matched researchers: Michael Bronstein
- Matched groups: N/A
- Confidence: medium (author_alias)
- Topic keywords: N/A
- Journal/source: arxiv
- Publication date: 2026-10-19
- Article: http://arxiv.org/abs/2610.26347v1

Non-invasive brain-computer interfaces are in practice limited by signal-to-noise ratio, and recent state-of-the-art methods address this limitation by aggregating over repeated trials of the same stimulus. Yet multi-trial aggregation has been treated inconsistently across the literature: some work averages brain signals at the model's input, other work averages predictions at the model's output, and neither treats aggregation as an architectural choice in its own right. We provide the first systematic comparison of aggregation strategies for non-invasive neural decoding, evaluating six paradigms (including logit averaging during training and three attention-based variants we introduce) across three datasets, four tasks, and two group sizes. We find that aggregation choice matters substantially: training-time logit averaging, the simplest method we propose, outperforms all others in 6 of 7 settings. On the phoneme classification setting of the 2025 PNPL competition, it sets a new state of the art, significantly outperforming the competition winner by 17.4 absolute percentage points in balanced accuracy. We further draw a theoretical connection between logit averaging and joint ensemble training, which has been shown to underperform independent ensembling in the deep learning literature; our results call into question recent explanations of why joint ensemble training fails. Together, these findings establish multi-trial aggregation as a key design choice for non-invasive neural decoding and identify training-time logit averaging as a simple, effective default.
