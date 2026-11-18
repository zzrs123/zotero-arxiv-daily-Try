# Researcher Tracking - 2026-11-18 (daily)

Total new tracked papers: 4
Highlighted papers: 4

## 1. ST-FateFlow: Continuous Gene-Spatial Reconstruction with Differentiation-Potential Learning from Time-Resolved Spatial Transcriptomics

- Authors: Zhe Yu, Xiaobo Sun, Hao Wu
- Source hits: arxiv
- Matched researchers: Sun Xiaobo
- Matched groups: N/A
- Confidence: medium (author_alias)
- Topic keywords: framework, model, spatial transcriptomics, spatial-omics-computation
- Journal/source: arxiv
- Publication date: 2026-11-17
- Article: http://arxiv.org/abs/2611.22256v1

Time-resolved spatial transcriptomics provides a powerful view of dynamic biological processes by measuring cellular states together with their spatial organization across time. However, destructive profiling and experimental cost restrict observations to a few discrete time points collected from independent samples, with no known cell pairing across time. This makes it difficult to reconstruct gene expression and tissue organization at unobserved stages and to characterize differentiation-associated dynamics. Here, we introduce ST-FateFlow, a flow-matching framework for continuous gene-spatial dynamics and differentiation-potential learning. ST-FateFlow jointly learns gene-expression and spatial-coordinate velocity fields, enabling interpolation of missing time points and continuous modeling of transcriptional evolution and tissue remodeling. In parallel, it independently learns a time-conditioned differentiation potential, whose values organize cell states along inferred differentiation progressions and support the analysis of differentiation-associated transcriptional changes. Across multiple time-resolved spatial transcriptomics datasets, ST-FateFlow effectively captures coordinated gene-expression and spatial dynamics. Case studies further show that the learned potential landscapes are consistent with known developmental and regenerative trajectories and help identify candidate genes associated with differentiation progression.

## 2. Errpedia: Is Your Exact $k$-NN Vector Search Really Exact?

- Authors: Yinuo Deng, Ying Zhang, Hanchen Wang, Wenjie Zhang
- Source hits: arxiv
- Matched researchers: Hanchen Wang
- Matched groups: N/A
- Confidence: medium (author_alias)
- Topic keywords: N/A
- Journal/source: arxiv
- Publication date: 2026-11-17
- Article: http://arxiv.org/abs/2611.22474v1

Exact $k$-nearest-neighbor ($k$-NN) vector search is a common feature of vector libraries and database systems. It serves applications that require exact results and provides the ground truth for evaluating approximate search. However, floating-point rounding and overflow can cause an exact search to return mathematically incorrect top-$k$ result sets. These errors can go unnoticed and affect downstream tasks that rely on exact results. We present Errpedia, a purpose-built dataset for testing the numerical correctness of exact vector search. Errpedia contains 1,616 queries across 21 error categories, with ground truth independently verified using exact rational arithmetic. We evaluate 20 widely used library and database configurations and find that every tested configuration returns mathematically incorrect top-10 result sets on at least 1 applicable query. Failures include misranking nearly equidistant vectors and returning incomplete results: 1 library omits all 10 exact matches to a query, and several systems return fewer than $k$ neighbors. We release Errpedia as a reproducible benchmark for developers and researchers to test their implementations. The dataset is publicly available at https://github.com/dynos01/errpedia.

## 3. Sage S2.1 Flash Technical Report

- Authors: Kun Cai, Haodong Chen, Guangran Cheng, Qingxiu Cheng, Xu Dai, Guanting Dong, Qiming Ge, Lixin Gu, Tao Gui, Honglin Guo, Yuyang Hu, Zixian Huang, Jiajie Jin, Alexander Lam, Jiaqiang Li, Yining Li, Jiahang Lin, Yanjiang Liu, Xinyu Lu, Haijun Lv, Ningsheng Ma, Zerun Ma, Minlong Peng, Jianmin Qian, Huayu Sha, Junlin Shang, Shuo Shen, Qisheng Su, Jiajun Sun, Yanan Sun, Zhichao Sun, Ran Tao, Zhongbo Tian, Guoqiang Wang, Hui Wang, Rui Wang, Yiding Wang, Zhecan Wang, Hao Xiang, Xinchen Xie, Shuhao Xing, Xiaoyu Xing, Wanghan Xu, Xinyu Yang, Yajie Yang, Dingbo Yuan, Yuhang Zang, Hongjie Zhang, Chengfeng Zhao, Haoran Zhao, Penghao Zhao, Ruojun Zhou, Dongsheng Zhu, Yicheng Zou, Qiye Cai, Yifei Cao, Xinmeng Che, Hongji Chen, Jiabei Chen, Jiadong Chen, Jiahao Chen, Jiayi Chen, Xinjie Chen, Yujia Chen, Xin Deng, Yi Dong, Yichen Dong, Wenjie Fu, Jianing Geng, Chenyang Gu, Ding Han, Han Han, Feiyang Hao, Haotan He, Qiushi He, Xufeng He, Xin Hong, Jie Hou, Binze Hu, Yongkang Hu, Zijian Hu, Enfu Huang, Junhao Huang, Changhao Jiang, Huicheng Jiang, Jiazhen Jiang, Shufan Jiang, Wenqing Jing, Jiahao Kuang, Bowen Lai, Bo Li, Qi Li, Qilong Li, Zhuoqun Li, Tianhao Liang, Jiaxiang Liu, Junzhang Liu, Shaofan Liu, Shuainan Liu, Tong Liu, Yi Liu, Ziyu Liu, Zhonghang Lu, Jianwen Luo, Xuan Luo, Yanyi Luo, Huijie Lv, Mingyu Ma, Houcheng Min, Hongjun Mo, Songhao Ni, Chengjun Pan, Qiyuan Peng, Xiaoxuan Peng, Wanying Ren, Runhui Ruan, Jifei Shan, Zixin Shang, Bing Shao, Zhuohui Sheng, Jiayang Shi, Qingyun Shi, Yang Shu, Aierpanjiang Simayi, Sirui Song, Yuxiao Song, Jiahao Sun, Zhe Sun, Wenzhe Tan, Guoxiang Wang, Hanchen Wang, Jie Wang, Pengbo Wang, Qing Wang, Rui Wang, Weihang Wang, Xiaotao Wang, Yuhui Wang, Zhekai Wang, Zihan Wang, Zile Wang, Jinke Wu, Liwei Wu, Xuansheng Wu, Yida Wu, Yihao Wu, Yinqi Wu, Yue Wu, Yuhan Wu, Yuwa Wu, Zhiheng Xi, Ying Xiao, Zhide Xie, Caijun Xu, Xingle Xu, Yichen Xu, Yongfeng Xu, Xiaolei Yang, Zhixiong Yang, Jiacheng Yao, Dingcheng Yi, Shihong Yi, Jinhui Yin, Peizhou Yu, Shan Yu, Hao Yuan, Junjie Yuan, Xiongyao Zha, Bo Zhang, Caixian Zhang, Kaicheng Zhang, Pengxiang Zhang, Qiuyinzhe Zhang, Wei Zhang, Xiaoqian Zhang, Xinsen Zhang, Jiyuan Zhao, Shuyu Zhao, Pujun Zheng, Zheyu Zheng, Xiaoxue Zhong, Peiheng Zhou, Xiaohao Zhou, Xinyu Zhou, Fangyi Zhu, Guanru Zhu, Yulun Zhu, Jiabao Zhuang, Pengfei Cao, Zhicheng Dou, Xianpei Han, Ben He, Guoxiu He, Xuanjing Huang, Tao Ji, Yu-Gang Jiang, Dahua Lin, Hongyu Lin, Kang Liu, Yaojie Lu, Le Sun, Ji-Rong Wen, Jun Zhao, Yutao Zhu, Qi Zhang, Bowen Zhou
- Source hits: arxiv
- Matched researchers: Hanchen Wang
- Matched groups: N/A
- Confidence: medium (author_alias)
- Topic keywords: N/A
- Journal/source: arxiv
- Publication date: 2026-11-16
- Article: http://arxiv.org/abs/2611.21072v1

We introduce Sage S1.5 Flash, a 320-billion-parameter general-purpose mixture-of-experts model designed to reason over scientific evidence and act in interactive environments. Sage Sci-Perception uses dedicated encoders for molecular graphs and biological sequences and represents spectra as ordered patches of measurements. Modality-specific projectors map these representations into the input space of a shared backbone, which processes them alongside text and images. To develop the model's agent capabilities, we construct verifiable environments for tool use, search, and coding, as well as specialized workflows involving machine learning experiments and scientific software. Task completion is checked against execution results, changes in environment state, or submitted artifacts. We evaluate Sage S1.5 Flash on 33 benchmarks across seven domains. In the primary comparison against five baselines, it ranks first on OfficeQA Pro (72.2), MLE-bench Lite (90.3 HumanRank), Harvey LAB, and SpreadsheetBench~2, and second on OSWorld-Verified (85.2), WebArena-Verified (67.6), and DeepResearch Bench~II (54.2). These results show particular strengths in using documentary evidence, producing verifiable workbooks, and carrying out machine learning tasks, alongside competitive performance in desktop and browser workflows that require the model to act on visual feedback.

## 4. PointZip: Statistically Lossless Compression for Climate Data with Pointwise Error Bounds

- Authors: Jiayong Li, Pratyai Mazumder, Yuejiang Yu, Langwen Huang, Alexandru Calotoiu, Torsten Hoefler
- Source hits: arxiv
- Matched researchers: Torsten Hoefler
- Matched groups: N/A
- Confidence: medium (author_alias)
- Topic keywords: N/A
- Journal/source: arxiv
- Publication date: 2026-11-16
- Article: http://arxiv.org/abs/2611.21312v1

High-resolution climate simulations generate data volumes that increasingly strain storage, I/O, and data dissemination. Error-bounded lossy compressors can reduce these costs, but their tolerances are usually user-chosen and difficult to standardize across heterogeneous climate datasets. We address this limitation with statistically lossless compression, where the pointwise compression error is bounded by the pointwise data uncertainty. We propose PointZip, a two-stage compressor that combines a rate-distortion-efficient base layer with error-bound-aware residual coding to enforce pointwise guarantees. On outputs from the widely used climate modeling framework ICON, PointZip makes 1km simulations practical by reducing storage bandwidth requirements by 72x. On the ERA5 climate dataset, PointZip reaches 69.3x on the most representative variables, reducing the commonly used subset to 4 TB. In downstream evaluations, PointZip preserves data spectra, extreme events, and air parcel trajectories, while increasing neural weather forecast RMSE by less than 1%, with negligible impact on the Fractions Skill Score (FSS).
