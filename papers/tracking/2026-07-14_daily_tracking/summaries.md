# Researcher Tracking - 2026-07-14 (daily)

Total new tracked papers: 3
Highlighted papers: 3

## 1. Beyond the Eye: Efficient Multimodal Reasoning via Self-Regulated Implicit Visual Tools

- Authors: Xiuwei Chen, Quanlin Chen, Wentao Hu, Zisheng Chen, Kun Xiang, Zehua Ma, Mingyang Zhang, Jianhua Han, Hanhui Li, Hang Xu, Xiaodan Liang
- Source hits: arxiv
- Matched researchers: Hang Xu
- Matched groups: N/A
- Confidence: medium (author_alias)
- Topic keywords: large language model, multimodal large language model
- Journal/source: arxiv
- Publication date: 2026-07-13
- Article: http://arxiv.org/abs/2607.11106v1

Recent multimodal large language models (MLLMs) have made remarkable progress on fine-grained perception tasks under the "Thinking with Images" (TwI) paradigm by iteratively performing various visual tool operations. However, this paradigm relies heavily on frequent external tool calls and repeated image re-encoding, which leads to substantial computational overhead and inference latency. To address these issues, we propose Beyond the Eye (BEE), a novel implicit visual tool paradigm centered on self-regulated capability. BEE directly incorporates visual tool invocation behaviors into the training objective and encourages the model to develop a self-regulated invocation mechanism. This design enables the model to adaptively balance internal knowledge and implicit tools, avoiding redundant tool usage while substantially reducing inference latency. Specifically, BEE involves a two-stage training process: (1) Formalized Chain-of-Thought (CoT) Supervised Fine-tuning (SFT). We construct CoT trajectories with structured tool slots and mixed invocation states. This stage activates the model's implicit tool representations and adaptive switching capability. (2) Self-regulated Reward-Driven Alignment. To address redundant tool usage caused by ambiguous cognitive boundaries, we first introduce the Net Tool Gain (NTG) metric to quantify this phenomenon. Based on this observation, we further propose a self-regulated reward mechanism. This mechanism penalizes ineffective tool dependency and encourages the model to perform knowledge routing, ensuring that implicit tools are invoked only when the model's internal knowledge is insufficient. BEE achieves state-of-the-art performance in fine-grained visual perception while remaining competitive in general reasoning tasks and achieving substantial gains in inference efficiency.

## 2. FastTPS: An Optimized Method for LLM Token Phase for AI accelerators

- Authors: Wenzong Yang, Danyang Zhang, Kun Cao, Tejus Siddagangaiah, Rajeev Patwari, Zhanxing Pu, Siyin Kong, Zijiang Yang, Hao Zhu, Varun Sharma, Yue Gao, Tianping Li, Fan Yang, Jicheng Chen, Yushan Chen, Fennian Zhao, Aaron Ng, Elliott Delaye, Ashish Sirasao, Sudip Nag
- Source hits: arxiv
- Matched researchers: Yue Gao
- Matched groups: N/A
- Confidence: medium (author_alias)
- Topic keywords: large language model
- Journal/source: arxiv
- Publication date: 2026-07-13
- Article: http://arxiv.org/abs/2607.11211v1

The popularity of large language models (LLMs) escalates an ongoing demand for effective inference. However, due to the sequential processing of tokens during the token phase in decoder-only LLMs inference, the inherent low parallelism leads to reduced throughput and suboptimal utilization of the computing units on artificial intelligence (AI) accelerators, particularly when handling long-sequence inputs that impose significant memory overhead. Recently, many reported methods have been developed as potential solutions, since they emerge with numeric deviation. This paper presents FastTPS, a high performance and low-precision loss method for accelerating the token-phase in LLM inference on general AI accelerators which includes three key components: (1) AI accelerator-enabled reloading-free KV Cache concatenation which decreases memory access overhead as well as enables full fusion of Attention, (2) high-efficiency and high-accuracy 'RoPE' attention based on the tiling optimized FLAT, and (3) highly-fused MLP with fine-grain pipeline scheduling. Our results confirm that FastTPS significantly alleviates memory bottlenecks in the token phase, delivering a 6x speed improvement (compared to none-fusion) on an AMD Ryzen AI 300 series NPU with BF16 precision while sustaining 93% peak memory bandwidth utilization during Phi3-mini-4k-instruct inference.

## 3. MUX-USCT: A Noise-Robust Neural Network for Ultrasound Computed Tomography

- Authors: Yuchen Yuan, Hanhan Wu, Jinyang Li, Hanchen Wang, Yixuan Wu, Youzuo Lin, Lei Yang
- Source hits: arxiv
- Matched researchers: Hanchen Wang
- Matched groups: N/A
- Confidence: medium (author_alias)
- Topic keywords: N/A
- Journal/source: arxiv
- Publication date: 2026-07-12
- Article: http://arxiv.org/abs/2607.10648v1

Deep neural networks (DNNs) have shown strong potential for ultrasound computed tomography (USCT) reconstruction in ideal noise-free environments, yet existing DNNs are vulnerable to the noisy conditions in clinical practice, as they equally treat inputs that suffer mild, moderate, or severe noise. More challenging, the distributions of noise shift along with the environment, indicating the less effectiveness of noise-aware training, which injects a specific noise distribution into the training data. We rethink these challenges and observe that the DNN models can become more robust to noise if we know the noise sources and filter them out. This filtering operation is very alike the Multiplexers (or MUX), a fundamental combinational circuit in digital logic design. However, the challenge here is that noise can happen randomly during inference; as a result, the manually predefined MUX cannot work. To address these challenges, we propose MUX-USCT, a novel encoder-decoder DNN architecture that encodes the known acoustic acquisition geometry with an "adaptive MUX" that can automatically identify and filter noise, where the attention mechanism is applied in reconstructing the speed-of-sound map. On the OpenPros benchmark, MUX-USCT reaches 6.88 m/s MAE with 17% fewer parameters than the leading baseline with 7.65 m/s of MAE. Under simulated clinical noise, it remains stable across diverse degradation types that cause geometry-agnostic baselines to fail. Results show that the attention distributions in MUX-USCT provide interpretable indicators of the signal quality between pairs of transducers.
