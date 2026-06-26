# Researcher Tracking - 2026-06-26 (daily)

Total new tracked papers: 2
Highlighted papers: 2

## 1. Anatomy-Guided Residual Motion Diffusion for Controllable 4D Cardiac MRI Synthesis

- Authors: Yiheng Cao, Gustavo Andrade-Miranda, Jiatian Zhang, Lingxiao Zhao, Xin Gao
- Source hits: arxiv
- Matched researchers: Xin Gao
- Matched groups: N/A
- Confidence: medium (author_alias)
- Topic keywords: diffusion, variational autoencoder
- Journal/source: arxiv
- Publication date: 2026-06-25
- Article: http://arxiv.org/abs/2606.26764v1

Developing robust artificial intelligence models for 4D (3D + time) medical imaging is constrained by limited annotated data, inter-device domain shifts, and privacy restrictions. To address this, we propose a 4D controllable generative framework for anatomically consistent data augmentation. A semi-supervised variational autoencoder learns a compact latent representation of anatomical volumes while jointly predicting aligned segmentation masks in a unified framework. Anatomical structure is then disentangled from temporal dynamics through a cascaded latent diffusion model (LDM). A static LDM generates subject-specific anatomy conditioned on clinical priors (diagnosis and volumes measures) and a subsequent motion LDM estimates residual latent motions, ensuring strict temporal coherence across the 4D sequence. The proposed approach was evaluated on cine cardiac MRI as a representative 4D imaging application. Experiments across multiple datasets demonstrate high controllability of static anatomy (Pearson r > 0.8) and strong temporal coherence (FVD = 288.08). In cross-vendor generalization experiments, augmenting training sets with synthetic 4D sequences significantly improves downstream segmentation performance. Using nnU-Net, the proposed augmentation strategy improves the average Dice score by 1.4% and reduces the Hausdorff Distance by 3.0mm compared to training on real data alone, for the left ventricle, Dice improves by 2.8% with a 5.4mm reduction in boundary error. Overall, this framework provides a scalable and controllable solution for 4D medical image synthesis, supporting the development of more robust models with limited annotations and cross-vendor variability. Code available on https://github.com/cyiheng/4DCardiacMRISynthesis.

## 2. Decoupling Semantics and Geometric Grounding: Spatial Visual Prompts for Language-Conditioned Imitation Learning

- Authors: Yanzhe Tang, Xinyu Shao, Yuxuan Hu, Siyu Chen, Bowen Yang, Yajun Gao, Tongtong Cao, Xiu Li, Long Zeng
- Source hits: arxiv
- Matched researchers: Yuxuan Hu
- Matched groups: N/A
- Confidence: medium (author_alias)
- Topic keywords: foundation model
- Journal/source: arxiv
- Publication date: 2026-06-24
- Article: http://arxiv.org/abs/2606.25360v1

While end-to-end Vision-Language-Action (VLA) models show promise in robotic manipulation, their monolithic paradigm inherently couples semantic reasoning and spatial control. This creates a severe alignment bottleneck, limiting precise target disambiguation in data-constrained imitation learning. To overcome this, we propose SVP-IL, a decoupled architecture that explicitly extracts spatial visual grounding from the action generation loop. By leveraging vision-language foundation models, we parse instructions into zero-shot geometric masks, translating language into explicit Spatial Visual Prompts (SVP). These priors are injected into a continuous action generator via a lightweight direct feature-level fusion mechanism. This integration provides explicit and uncorrupted spatial gradient guidance while ensuring highly stable optimization under low-data regimes. Extensive experiments demonstrate that SVP-IL significantly outperforms state-of-the-art VLAs and pure visuomotor baselines. Trained on as few as 50 to 100 demonstrations, SVP-IL improves average success rates on highly ambiguous language-conditioned tasks from 24.0% to 39.5%, achieving 67.8% on standard benchmarks. Real-world robotic experiments further validate its robustness and data efficiency in unstructured physical environments.
