# Paper Daily Reading - 2026-10-26

## 1. Recommendation system-inspired learning of crossmodal interaction patterns between chromatin accessibility and gene expression

- Authors: Xiaotang Wang, Xuanwei Lin, Qiaoyi Zhang, Xiaochen Bo, Hao Li, Yu Zhang
- Source: openalex
- Venue type: journal
- Journal: Nature Communications
- Publication status: published
- Publication date: 2026-10-24
- DOI: https://doi.org/10.1038/s41467-026-78646-y
- Categories: Single-cell and spatial transcriptomics, Genomics and Chromatin Dynamics, Gene Regulatory Network Analysis
- Relevance: 3.787987102622923
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://doi.org/10.1038/s41467-026-78646-y
- PDF: Unavailable
- Local PDF: Not downloaded

Abstract Despite the growing availability of crossmodal single-cell sequencing, existing approaches are limited by underutilization of biological attributes, sparse modality signals, and insufficient modeling of regulatory interactions, limiting generalization in data-scarce settings and the discovery of peak-gene-level relationships. Interestingly, such challenges mirror those in recommendation systems, where side information, high sparsity, binary interactions, and cold start problems are extensively studied. Inspired by recommender models that infer user-item preferences from incomplete interaction graphs, we present CrossRec, which reformulates scATAC and scRNA data as an interaction graph to learn regulatory patterns across single-cell tasks. Its biologically-driven bipartite graph transformer learns interpretable attention over ATAC-RNA pairs. CrossRec outperforms existing methods across various tasks, remains robust under data-scarce settings, generalizes to unseen cell types and datasets, and enhances prior-based methods. Its learned regulatory maps provide cell- and cell-type-specific insights, resolving dynamic regulatory rewiring during cortical neurogenesis and perturbation-specific rewiring of drug-induced regulation in melanoma resistance.

## 2. Democratizing reliable knowledge-seeking with MyGPT: a privacy-first, open-source retrieval-augmented generation platform

- Authors: Jaimin N Patel, Jude Downing, Hugh Ferguson, Thika You, Duccio Malinverni, Steve Mathew, Inês Chen, Madison Sluter, Beth Moorefield, Katalin Paréj, Mukundan Ragavan, Cindy Morris, Dinesh Keerthi, Desiree Becerra Armada, Bálint Mészáros, Vikas D. Trivedi, Shahinur Alam, Anthony Woodard, Dan Alford, Sagar Pathak, Cai Li, Renato Umeton, Carlos Rodríguez‐Galindo, Catherine G. Lam, Stephen M Gottschalk, Charalampos G. Kalodimos, M. Madan Babu
- Source: openalex
- Venue type: journal
- Journal: Nature Communications
- Publication status: published
- Publication date: 2026-10-24
- DOI: https://doi.org/10.1038/s41467-026-78509-6
- Categories: Topic Modeling, Artificial Intelligence in Healthcare and Education, Information Retrieval and Search Behavior
- Relevance: 2.776473996397108
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://doi.org/10.1038/s41467-026-78509-6
- PDF: Unavailable
- Local PDF: Not downloaded

Abstract Large language models (LLMs) have transformed knowledge discovery, but their use in sensitive domains is limited by privacy concerns and risks of data leakage. Moreover, LLMs may hallucinate when queried about information outside their training data, undermining their reliability for scientific, clinical, or policy-related tasks. We present MyGPT, a fully open-source, privacy-preserving retrieval-augmented-generation (RAG) platform that uses open-source LLMs and operates locally or within secure institutional environments. MyGPT empowers users to query user-defined libraries such as biomedical literature, confidential clinical documents, and multilingual global health policies, while ensuring that sensitive data never leaves the secure environment. We introduce confidence metrics, including “relevance scores” and “hallucination index,” and provide explicit source citation from the library within a single interface to assess contextual support for generated answers. MyGPT offers a cost-effective, modular, open-source alternative to commercial LLM services and democratizes knowledge-seeking across multiple domains, including use at remote facilities without internet access.

## 3. LLEOT: A Privacy-Enhancing Offsite Tuning Framework via Loss Landscape Elevation

- Authors: Jin Zhong, Jinglin Liang, Tongtong Yang, Zijian Xie, Shuangping Huang, Hanlin Gu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.6059149608346943
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1878/
- PDF: https://aclanthology.org/2026.findings-acl.1878.pdf
- Local PDF: pdf/2026-10-26_03_LLEOT_ A Privacy-Enhancing Offsite Tuning Framework via Loss Landscape Elevation.pdf

Adapting large language models (LLMs) to domain-specific tasks via fine-tuning is often infeasible: models are protected by intellectual property, while sensitive data cannot be shared due to privacy regulations. A promising paradigm, Offsite Tuning (OT), addresses this challenge by constructing an emulator of the original model. Data owners leverage the emulator to train an adapter on downstream data, which is then plugged back into the original model, enabling knowledge transfer without transmitting either the original model or the raw data. However, emulators constructed by existing OT-based methods often retain substantial inference capabilities, thereby exposing model capability privacy and posing risks of misuse. To address this, we propose Loss Landscape Elevation Offsite Tuning (LLEOT), a framework that secures data privacy as well as model parameter and capability privacy. At its core, Loss Landscape Elevation (LLE) enforces a fixed margin between the loss landscapes of the emulator and the original model. We theoretically demonstrate that LLE simultaneously (i) degrades emulator inference via perplexity amplification and (ii) preserves gradient alignment, ensuring consistent convergence for adapter training. Extensive experiments confirm that LLEOT achieves strong adaptation performance while effectively mitigating emulator misuse. Code is available at https://github.com/Z-eloto/LLEOT .

## 4. FLOP-Efficient Training: Early Stopping Based on Test-Time Compute Awareness

- Authors: Hossam Amer, Maryam Dialameh, Hossein Rajabzadeh, Walid Ahmed, Weiwei Zhang, Yang Liu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.6049248098716005
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1766/
- PDF: https://aclanthology.org/2026.findings-acl.1766.pdf
- Local PDF: pdf/2026-10-26_04_FLOP-Efficient Training_ Early Stopping Based on Test-Time Compute Awareness.pdf

Scaling training compute, measured in FLOPs, has long been shown to improve the accuracy of large language models, yet training remains resource-intensive. Prior work shows that increasing test-time compute (TTC)—for example through iterative sampling—can allow smaller models to rival or surpass much larger ones at lower overall cost. We introduce TTC-aware training, where an intermediate checkpoint and a corresponding TTC configuration can together match or exceed the accuracy of a fully trained model while requiring substantially fewer training FLOPs. Building on this insight, we propose an early stopping algorithm that jointly selects a checkpoint and TTC configuration to minimize training compute without sacrificing accuracy. To make this practical, we develop an efficient TTC evaluation method that avoids exhaustive search, and we formalize a break-even bound that identifies when increased inference compute compensates for reduced training compute. Experiments demonstrate up to 92% reductions in training FLOPs while maintaining and sometimes remarkably improving accuracy. These results highlight a new perspective for balancing training and inference compute in model development, enabling faster deployment cycles and more frequent model refreshes.

## 5. Probing Semantic Alignment, Lexical Invariance, and Syntactic Influence in LLM Metaphor Processing

- Authors: Fengying Ye, Shanshan Wang, Lidia S. Chao, Derek F. Wong
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.604271142707905
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1286/
- PDF: https://aclanthology.org/2026.acl-long.1286.pdf
- Local PDF: pdf/2026-10-26_05_Probing Semantic Alignment, Lexical Invariance, and Syntactic Influence in LLM Metaphor Processing.pdf

Large language models (LLMs) achieve strong performance on metaphor detection and interpretation tasks, yet it remains unclear what such behavioral success actually reveals about metaphor processing. We present a diagnostic analysis that examines the limits of behavioral evidence by probing three complementary dimensions: semantic attribute alignment, lexical invariance, and syntactic sensitivity. Using geometric probing, we assess whether model-generated interpretations align with reference semantic attributes; through context-varying substitution, we analyze the stability of lexical associations between metaphorical and literal expressions; and via controlled syntactic perturbations, we examine sensitivity in metaphor detection. Our analysis reveals that LLM-generated interpretations can exhibit semantic drift relative to reference attributes; stable lexical anchors persist across contextual conditions, potentially supporting conventional metaphors while biasing novel metaphors requiring contextual integration; and detection performance is sensitive to syntactic irregularities. These findings suggest that strong behavioral performance may reflect heterogeneous underlying signals, highlighting the need for caution when interpreting metaphor benchmarks as evidence of robust, integrated semantic understanding.

## 6. Fusion Training for Mathematical Generalization in Large Language Models

- Authors: Congfeng Cao, Pengyu Zhang, Jelke Bloem
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.602988214396027
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-srw.64/
- PDF: https://aclanthology.org/2026.acl-srw.64.pdf
- Local PDF: pdf/2026-10-26_06_Fusion Training for Mathematical Generalization in Large Language Models.pdf

Thinking Mode Fusion (TMF) enables large language models to support both concise responses and long-form reasoning by unifying a non-thinking mode and a thinking mode within a single model. However, its training dynamics, including the data ratio and training schedule between the two modes, remain underexplored. In this work, we present a systematic study of TMF by analyzing the effects of the training schedule and data ratio between thinking and non-thinking modes. Focusing on mathematical problem solving, we construct a benchmark with multiple thinking-to-non-thinking data ratios and three training schedules. Our results reveal an asymmetric interaction between the two modes: increasing the ratio of non-thinking supervision reduces the accuracy of the thinking mode. We further show that different training schedules modulate this trade-off and that the optimal schedule depends on the data ratio. Finally, we quantify a negative correlation between non-thinking and thinking mode supervision, highlighting an inherent tension between these two modes. These findings provide practical guidance for designing effective TMF training settings. All code and data are released to support further research at: Fusion Bench.

## 7. Authorship Attribution in Multilingual Machine-Generated Texts

- Authors: Lucio La Cava, Dominik Macko, Robert Moro, Ivan Srba, Andrea Tagarelli
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.602673736714891
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.2091/
- PDF: https://aclanthology.org/2026.acl-long.2091.pdf
- Local PDF: pdf/2026-10-26_07_Authorship Attribution in Multilingual Machine-Generated Texts.pdf

As Large Language Models (LLMs) have reached human-like fluency and coherence, distinguishing machine-generated text (MGT) from human-written content becomes increasingly difficult. While early efforts in MGT detection have focused on binary classification, the growing landscape and diversity of LLMs require a more fine-grained yet challenging authorship attribution (AA), i.e., being able to identify the precise generator (LLM or human) behind a text. However, AA remains nowadays confined to a monolingual setting, with English being the most investigated one, overlooking the multilingual nature and usage of modern LLMs. In this work, we introduce the problem of Multilingual Authorship Attribution, which involves attributing texts to human or multiple LLM generators across diverse languages. Focusing on 18 languages—covering multiple families and writing scripts—and 8 generators (7 LLMs and the human-authored class), we investigate the multilingual suitability of monolingual AA methods in terms of their cross-lingual transferability, and the impact of generators on attribution performance. Our results reveal that while certain monolingual AA methods can be adapted to multilingual settings, significant limitations and challenges remain, particularly in transferring across diverse language families, underscoring the complexity of multilingual AA and the need for more robust approaches to better match real-world scenarios.

## 8. DPC: Training-Free Text-to-SQL Candidate Selection via Dual-Paradigm Consistency

- Authors: Boyan Li, Ou Ocean Kun Hei, Yue Yu, Yuyu Luo
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.6026100092824302
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.313/
- PDF: https://aclanthology.org/2026.acl-long.313.pdf
- Local PDF: pdf/2026-10-26_08_DPC_ Training-Free Text-to-SQL Candidate Selection via Dual-Paradigm Consistency.pdf

While Large Language Models (LLMs) demonstrate impressive proficiency in generating SQL queries, they fundamentally lack the capability to self-evaluate correctness without an execution oracle. This limitation creates a stark Generation-Selection Gap, where high potential accuracy (Pass@K) fails to translate into execution accuracy (Pass@1). Although supervised verifiers offer mitigation, they incur prohibitive annotation costs and suffer from domain fragility. Consequently, recent research has pivoted to the training-free setting. However, existing methods—such as Self-Consistency or LLM-as-a-Judge—remain hampered by systematic bias (consensus on hallucinations) and symbolic blindness (inability to simulate execution states). We introduce DPC (Dual-Paradigm Consistency), a multi-agent framework that reformulates SQL selection from a probabilistic guessing task on hidden data into a deterministic verification task on visible data. Specifically, DPC employs a Slicer and a Tester agent to collaboratively construct a Minimal Distinguishing Database (MDD)—an adversarial, fully observable micro-environment engineered to expose logical discrepancies between candidates. To break the self-correction bias, a Solver agent then verifies the SQL candidates by cross-referencing their execution against a parallel Python/Pandas solution. By validating execution consistency between declarative (SQL) and imperative (Python) paradigms, DPC robustly discriminates correct logic from systematic hallucinations. Experiments on BIRD and Spider across multiple LLMs demonstrate that our method consistently outperforms existing selection baselines, achieving absolute accuracy improvements of up to 2.2% over strong competitors like Self-Consistency.

## 9. Generating then Refining for Reliable Knowledge Base Question Answering

- Authors: Jianqi Gao, Hang Yu, Jian Cao, Ranran Bu, Jinghua Tang, Nengjun Zhu, Yonggang Zhang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.602597237031561
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1479/
- PDF: https://aclanthology.org/2026.acl-long.1479.pdf
- Local PDF: pdf/2026-10-26_09_Generating then Refining for Reliable Knowledge Base Question Answering.pdf

Knowledge Base Question Answering (KBQA) aims to retrieve accurate answers to natural language queries by retrieving and reasoning over large-scale structured knowledge bases (KBs). Advanced semantic parsing-based methods promoted by large language models (LLMs) demonstrate superior performance by transforming questions into structured queries, i.e., logical forms (LFs). However, LFs generated by LLMs could be non-executable due to the inherent semantic hallucination issue of LLMs and the complex graph retrieval characteristics of the KBQA task. To address this challenge, we propose a novel “generate-verify-refine” framework, termed Action-Reflection-Integrated KBQA (ARI-KBQA) for reliable LF generation. ARI-KBQA introduces a dual-module cooperative architecture: First, an action generator is trained to produce initial query paths based on a hop-by-hop reasoning strategy. Then a reflection verifier dynamically validates path feasibility by interacting with the KBs. Consequently, ARI-KBQA filters out invalid LFs and provides semantic correction feedback to the action generator for iteratively refining LFs. Evaluations on standard KBQA benchmarks show that the proposed ARI-KBQA significantly enhances model performance with a reduced search space, especially in complex multi-hop query scenarios.

## 10. Learning from Contrastive Prompts: An Automated Prompt Optimization Framework

- Authors: Mingqi Li, Karan Aggarwal, Yong Xie, Aitzaz Ahmad, Stephen Lau
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.602043790335915
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.9/
- PDF: https://aclanthology.org/2026.findings-acl.9.pdf
- Local PDF: pdf/2026-10-26_10_Learning from Contrastive Prompts_ An Automated Prompt Optimization Framework.pdf

As large language models (LLMs) continue to advance, significant effort is spent on manually crafting prompts to unlock their full potential. While existing prompt optimization methods automate this process, they often underperform due to their reliance on learning exclusively from incorrect samples. We propose the Learning from Contrastive Prompts (LCP) framework, which leverages contrastive prompts to distinguish between high- and low-performing cases. By identifying and amplifying the differences that make prompts effective, LCP systematically extracts principles underlying successful prompt design. On the Big-Bench Hard benchmark, LCP achieves an 87.5% win rate on Claude-3-Sonnet and 75.7% on Claude-4-Sonnet. Experiments on DeepSeek-R1 (88.2% win rate) and SuperGLUE further confirm that LCP generalizes across both proprietary and open-source models and diverse NLU benchmarks.The framework offers a principled and scalable foundation for automated prompt engineering, reducing manual intervention in adapting LLMs to diverse applications.

## 11. Gained in Translation: Privileged Pairwise Judges Enhance Multilingual Reasoning

- Authors: Lintang Sutawika, Gokul Swamy, Steven Wu, Graham Neubig
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.601943606410901
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.393/
- PDF: https://aclanthology.org/2026.acl-long.393.pdf
- Local PDF: pdf/2026-10-26_11_Gained in Translation_ Privileged Pairwise Judges Enhance Multilingual Reasoning.pdf

When asked a question in a language less seen in its training data, current reasoning large language models (RLMs) often exhibit dramatically lower performance than when asked the same question in English. In response, we introduce SP3F (Self-Play with Privileged Pairwise Feedback), a two-stage framework for enhancing multilingual reasoning without any data in the target language(s). First, we supervise fine-tune (SFT) on translated versions of English question-answer pairs to raise base model correctness. Second, we perform RL with feedback from a pairwise judge in a self-play fashion, with the judge receiving the English reference response as privileged information . Thus, even when none of the model’s responses are completely correct, the privileged pairwise judge can still tell which response is better. End-to-end, SP3F greatly improves base model performance, even outperforming fully post-trained models on multiple math and non-math tasks with less than 1/8 of the training data across the single-language, multilingual, and generalization to unseen language settings.

## 12. RSDA: Restoring Stale Data Affinity via Dynamic Renovation Strategy for Mitigating Data Scarcity

- Authors: Yidan Liang, Jia Zhu, Weijie Shi, Hanghui Guo, Yue Cui, Jiawei Shen, Guoqing Ma, Jingjiang Liu, Qingyu Niu, Yilin Wang, Shimin Di, Jiajie Xu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.6004794209474884
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.375/
- PDF: https://aclanthology.org/2026.acl-long.375.pdf
- Local PDF: pdf/2026-10-26_12_RSDA_ Restoring Stale Data Affinity via Dynamic Renovation Strategy for Mitigating Data Scarcity.pdf

High-quality data is the cornerstone of advancing large language models. However, the field currently faces a critical dilemma: the supply of premium data is nearing depletion, while vast stale corpora remain underutilized. Our empirical analysis reveals that training models on such data directly often leads to performance degradation. We attribute this phenomenon to the data affinity gap, a misalignment stemming from the model’s inability to effectively comprehend the data or inherent quality defects. To bridge this gap, we propose Restoring Stale Data Affinity (RSDA) framework. First, utilizing our proposed potential entropy metric, RSDA quantifies the latent value of samples to effectively identify stale data with higher renovation potential. Subsequently, the framework employs a dynamic renovation strategy selection mechanism to determine the optimal component-level strategy for each instance, transforming low-affinity stale samples into high-quality training data. Comprehensive experimental results demonstrate that RSDA effectively enhances data affinity, achieving performance improvements using less than 10% of the data volume, thereby underscoring that the latent potential of stale corpora remains largely untapped. The code is available at https://github.com/wenfiii/RSDA .

## 13. Correct, Concise and Complete: Multi-stage Training For Adaptive Reasoning

- Authors: Nathanaël Carraz Rakotonirina, Ren Pang, Neha Anna John, Michael Bohlke-Schneider, Momchil Hardalov
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.5992239962398536
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.622/
- PDF: https://aclanthology.org/2026.findings-acl.622.pdf
- Local PDF: pdf/2026-10-26_13_Correct, Concise and Complete_ Multi-stage Training For Adaptive Reasoning.pdf

The reasoning capabilities of large language models (LLMs) have improved substantially through increased test-time computation, typically in the form of intermediate tokens known as chain-of-thought (CoT). However, CoT often becomes unnecessarily long, increasing computation costs without improving accuracy and sometimes even degrading performance, a phenomenon known as “ overthinking ”. We propose a multi-stage efficient reasoning method that combines supervised fine-tuning—via rejection sampling or reasoning trace reformatting—with reinforcement learning using an adaptive length penalty. We introduce a lightweight reward function that penalizes tokens generated after the first correct answer, encouraging the model to perform self-verification only when beneficial. We conduct a holistic evaluation across seven diverse reasoning tasks, analyzing the accuracy–response length trade-off. Our approach reduces response length by an average of 28% for 8B models and 40% for 32B models, while incurring only minor performance drops of 1.6 and 2.5 points, respectively. Despite its conceptual simplicity, it achieves a better trade-off than more complex state-of-the-art efficient reasoning methods, scoring 76.6 on the area under the Overthinking-Adjusted Accuracy curve ( AUC OAA )—5 points above the base model and 2.5 points above the second-best approach.

## 14. CiPO: Counterfactual Unlearning for Large Reasoning Models through Iterative Preference Optimization

- Authors: Junyi Li, Yongqiang Chen, Ningning Ding
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.599126622142654
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.143/
- PDF: https://aclanthology.org/2026.acl-long.143.pdf
- Local PDF: pdf/2026-10-26_14_CiPO_ Counterfactual Unlearning for Large Reasoning Models through Iterative Preference Optimization.pdf

Machine unlearning has gained increasing attention in recent years, as a promising technique to selectively remove unwanted privacy or copyrighted information from Large Language Models that are trained on a massive scale of human data. However, the emergence of Large Reasoning Models (LRMs), which emphasize long chain-of-thought (CoT) reasoning to address complex questions, presents a dilemma to unlearning: existing methods either struggle to completely eliminate undesired knowledge from the CoT traces or degrade the reasoning performances due to the interference with the reasoning process. To this end, we introduce Counterfactual Unlearning through iterative Preference Optimization (CiPO), a novel framework that redefines unlearning as the targeted intervention of the CoT reasoning in LRMs. More specifically, given a desired unlearning target answer, CiPO instructs LRMs to generate a logically valid counterfactual reasoning trace for preference tuning. As the LRM adjusts to the counterfactual trace, CiPO iteratively updates the preference learning data to increase the discrepancy from the original model. This iterative loop ensures both desirable unlearning and smooth optimization, effectively mitigating the dilemma. Experiments on challenging benchmarks demonstrate that CiPO excels at unlearning, completely removing knowledge from both the intermediate CoT steps and the final answer, while preserving the reasoning abilities of LRMs.

## 15. Agentic Memory: Learning Unified Long-Term and Short-Term Memory Management for Large Language Model Agents

- Authors: Yi Yu, Liuyi Yao, Yuexiang Xie, Qingquan Tan, Jiaqi Feng, Yaliang Li, Libing Wu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.5989032682183644
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.981/
- PDF: https://aclanthology.org/2026.acl-long.981.pdf
- Local PDF: pdf/2026-10-26_15_Agentic Memory_ Learning Unified Long-Term and Short-Term Memory Management for Large Language Model Agents.pdf

Large language model (LLM) agents face fundamental limitations in long-horizon reasoning due to finite context windows, making effective memory management critical. Existing methods typically handle long-term memory (LTM) and short-term memory (STM) as separate components, relying on heuristics or auxiliary controllers, which limits adaptability and end-to-end optimization. In this paper, we propose Agentic Memory (AgeMem), a unified framework that integrates LTM and STM management directly into the agent’s policy. AgeMem exposes memory operations as tool-based actions, enabling the LLM agent to autonomously decide what and when to store, retrieve, update, summarize, or discard information. To train such unified behaviors, we propose a three-stage progressive reinforcement learning strategy and design a step-wise GRPO to address sparse and discontinuous rewards induced by memory operations. Experiments on five long-horizon benchmarks demonstrate that AgeMem consistently outperforms strong memory-augmented baselines across multiple LLM backbones, achieving improved task performance, higher-quality long-term memory, and more efficient context usage.

## 16. On the Continued Value of Universal Dependencies in the Era of Large Language Models

- Authors: Wenxi Li, Jingyu Peng
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.5988645363999483
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.803/
- PDF: https://aclanthology.org/2026.acl-long.803.pdf
- Local PDF: pdf/2026-10-26_16_On the Continued Value of Universal Dependencies in the Era of Large Language Models.pdf

The necessity of explicit linguistic representations has been increasingly questioned in the era of large language models (LLMs). In this work, we revisit this issue using Universal Dependencies (UD) as a case study, examining whether and in what ways this cross-lingual syntactic framework can still benefit contemporary LLMs. We focus on a cross-lingual adversarial paraphrase identification task that is designed to foreground the role of syntactic structure in semantic interpretation across languages. Within this setting, we systematically evaluate three strategies for integrating UD into LLMs: UD-Prompt, UD-Tuning, and UD-Attention. Our experiments show that, although the magnitude of gains depends on how UD-based structural priors interact with model behavior and cross-lingual variation, UD-augmented models consistently outperform their syntax-agnostic counterparts. Across strategies, we observe average accuracy improvements of 2.67%, 8.24%, and 2.53%, respectively. These findings demonstrate that linguistic knowledge remains informative for LLMs, offering practical value in cross-lingual settings where structural alignment is challenging.

## 17. Beyond Noise: Characterizing Creative Potential in Unverifiable LLM Hallucinations

- Authors: Yu Yan, Chunhong Zhang, Haiyu Zhao, Ziyang Zeng, Zihao Liu, Yongkang Wu, Jianzhou Diao, YiJie Chen, Shujie Wang, Zheng Hu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.5987063728565074
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.554/
- PDF: https://aclanthology.org/2026.acl-long.554.pdf
- Local PDF: pdf/2026-10-26_17_Beyond Noise_ Characterizing Creative Potential in Unverifiable LLM Hallucinations.pdf

In knowledge-intensive creative tasks, Large Language Models (LLMs) often generate outputs that extend beyond established knowledge, making direct verification against current evidence impractical. Unlike factual hallucinations checked against ground truth, such outputs arise naturally in creative generation, where extending beyond current knowledge is often the goal. Yet prior work debates whether hallucination should be suppressed or embraced without empirically analyzing this unverifiable subclass. On the ideation evaluation side, existing work focuses on individual outputs without characterizing the unverifiable space as a whole. To address this gap, we propose a novelty-verifiability characterization that distinguishes Creative Synthesis (Region A) from Groundless Fabrication (Region B), and study it through a conceptual creation task where LLMs synthesize novel scientific concepts. Through 32,400 generations across three technical domains and 1,080 human judgments, we find that Region A is non-negligible (4.7%) and robust, persisting across generation strategies, models, domains, and embedding choices. A retrospective recovery experiment further shows that LLMs can approximate post-cutoff scientific concepts in controlled combinatorial settings. Our findings suggest that the unverifiable space is not uniformly noise but exhibits empirically distinguishable internal structure, providing an empirical basis for more selective hallucination governance.[ https://github.com/YuLab1/llm-concept-creation ]

## 18. Memory as Action: Autonomous Context Curation for Long-Horizon Agentic Tasks

- Authors: Yuxiang Zhang, Jiangming Shu, Ye Ma, Xueyuan Lin, Shangxi Wu, Jitao Sang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.5986643183825375
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.956/
- PDF: https://aclanthology.org/2026.findings-acl.956.pdf
- Local PDF: pdf/2026-10-26_18_Memory as Action_ Autonomous Context Curation for Long-Horizon Agentic Tasks.pdf

Long-context Large Language Models, despite their expanded capacity, require careful working memory management to mitigate attention dilution during long-horizon tasks. Yet existing approaches rely on external mechanisms that lack awareness of the agent’s reasoning state, leading to suboptimal decisions. We propose Memory-as-Action (MemAct), a framework that treats working memory management as learnable policy actions. By formulating context management as in-place editing operations (deletion, insertion), MemAct enables joint optimization of information retention and task performance through end-to-end reinforcement learning. To address the computational challenges of dynamic context updates, we introduce Dynamic Context Policy Optimization, which restores training efficiency without compromising reasoning integrity. Experiments show that MemAct-RL-14B matches the accuracy of models 16× larger while reducing average context length by 51%, with learned strategies that adapt to model capabilities and generalize across task complexities. The code and datasets are available at https://github.com/ADaM-BJTU/MemAct .

## 19. Too Long, Do Re-weighting for Efficient LLM Reasoning Compression

- Authors: Zhong-Zhi Li, Xiao Liang, Zihao Tang, Lei Ji, Peijie Wang, Haotian Xu, Xing W, Haizhen Huang, Weiwei Deng, Yeyun Gong, Zhijiang Guo, Xiao Liu, Fei Yin, Cheng-Lin Liu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.598116882979302
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1856/
- PDF: https://aclanthology.org/2026.acl-long.1856.pdf
- Local PDF: pdf/2026-10-26_19_Too Long, Do Re-weighting for Efficient LLM Reasoning Compression.pdf

Large Language Models (LLMs) have recently achieved remarkable progress on complex reasoning tasks by leveraging extended Chain-of-Thought (CoT) techniques. These reasoning processes can be roughly categorized into System-1 (fast and intuitive) and System-2 (slow and deliberate) paradigms. However, excessive reliance on lengthy System-2-style reasoning during inference can produce extremely long outputs, thereby reducing efficiency. In this work, we propose Thinking Length Data Re-weighting (TLDR), that does not rely on sophisticated data annotations or interpolation between multiple models. We continuously balance the weights between the model’s System-1 and System-2 data to eliminate redundant reasoning processes while preserving the model’s reasoning capability. We validate our method across multiple base models, including Deepseek-R1-Distilled Qwen models, as well as on a diverse benchmarks with varying difficulty levels. Our method significantly reduces the number of output tokens by nearly 40% while maintaining the accuracy of the reasoning.

## 20. Safe-FedLLM: Delving into the Safety of Federated Large Language Models

- Authors: Mingxiang Tao, Yu Tian, Wenxuan Tu, Yue Yang, Xue Yang, Xiangyan Tang
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.5978853550985614
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1120/
- PDF: https://aclanthology.org/2026.acl-long.1120.pdf
- Local PDF: pdf/2026-10-26_20_Safe-FedLLM_ Delving into the Safety of Federated Large Language Models.pdf

Federated learning (FL) addresses privacy and data-silo issues in the training of large language models (LLMs). Most prior work focuses on improving the efficiency of federated learning for LLMs (FedLLM). However, security in open federated environments, particularly defenses against malicious clients, remains underexplored. To investigate the security of FedLLM, we conduct a preliminary study to analyze potential attack surfaces and defensive characteristics from the perspective of LoRA updates. We find two key properties of FedLLM: 1) LLMs are vulnerable to attacks from malicious clients in FL, and 2) LoRA updates exhibit distinct behavioral patterns that can be effectively distinguished by lightweight classifiers. Based on these properties, we propose Safe-FedLLM, a probe-based defense framework for FedLLM, which constructs defenses across three levels: Step-Level, Client-Level, and Shadow-Level. The core concept of Safe-FedLLM is to perform probe-based discrimination on each client’s local LoRA updates, treating them as high-dimensional behavioral features and using a lightweight classifier to determine whether they are malicious. Extensive experiments demonstrate that Safe-FedLLM effectively improves FedLLM’s robustness against malicious clients while maintaining competitive performance on benign data. Notably, our method effectively suppresses the impact of malicious data without significantly affecting training speed, and remains effective even under high malicious client ratios.

## 21. On the Step Length Confounding in LLM Reasoning Data Selection

- Authors: Bing Wang, Rui Miao, Chen Shen, Shaotian Yan, Kaiyuan Liu, Ximing Li, Xiaosong Yuan, Sinan Fan, Jun Zhang, Jieping Ye
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.597472868803168
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.918/
- PDF: https://aclanthology.org/2026.findings-acl.918.pdf
- Local PDF: pdf/2026-10-26_21_On the Step Length Confounding in LLM Reasoning Data Selection.pdf

Large reasoning models have recently demonstrated strong performance on complex tasks that require long chain-of-thought reasoning, through supervised fine-tuning on large-scale and high-quality datasets. To construct such datasets, existing pipelines generate long reasoning data from more capable Large Language Models (LLMs) and apply manually heuristic or naturalness-based selection methods to filter high-quality samples. Despite the proven effectiveness of naturalness-based data selection, which ranks data by the average log probability assigned by LLMs, our analysis shows that, when applied to LLM reasoning datasets, it systematically prefers samples with longer reasoning steps (i.e., more tokens per step) rather than higher-quality ones, a phenomenon we term step length confounding. Through quantitative analysis, we attribute this phenomenon to low-probability first tokens in reasoning steps; longer steps dilute their influence, thereby inflating the average log probabilities. To address this issue, we propose two variant methods: ASLEC-DROP, which drops first-token probabilities when computing average log probability, and ASLEC-CASL, which applies a causal debiasing regression to remove the first tokens’ confounding effect. Experiments across four LLMs and five evaluation benchmarks demonstrate the effectiveness of our approach in mitigating the step length confounding problem.

## 22. Bridging SFT and RL: Dynamic Policy Optimization for Robust Reasoning

- Authors: Taojie Zhu, Dongyang Xu, Ding Zou, Sen Zhao, Qiaobo Hao, Zhiguo Yang, Yonghong He
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.5972576752785956
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.219/
- PDF: https://aclanthology.org/2026.findings-acl.219.pdf
- Local PDF: pdf/2026-10-26_22_Bridging SFT and RL_ Dynamic Policy Optimization for Robust Reasoning.pdf

Post-training paradigms for Large Language Models (LLMs), primarily Supervised Fine-Tuning (SFT) and Reinforcement Learning (RL), face a fundamental dilemma: SFT provides stability (low variance) but suffers from high fitting bias, while RL enables exploration (low bias) but grapples with high gradient variance. Existing unified optimization strategies often employ naive loss weighting, overlooking the statistical conflict between these distinct gradient signals. In this paper, we provide a rigorous theoretical analysis of this bias-variance trade-off and propose DYPO (Dynamic Policy Optimization), a unified framework designed to structurally mitigate this conflict. DYPO integrates three core components: (1) a Group Alignment Loss (GAL) that leverages intrinsic group dynamics to significantly reduce RL gradient variance; (2) a Multi-Teacher Distillation mechanism that corrects SFT fitting bias via diverse reasoning paths; and (3) a Dynamic Exploitation-Exploration Gating mechanism that adaptively arbitrates between stable SFT and exploratory RL based on reward feedback. Theoretical analysis confirms that DYPO linearly reduces fitting bias and minimizes overall variance. Extensive experiments demonstrate that DYPO significantly outperforms traditional sequential pipelines, achieving an average improvement of 4.8% on complex reasoning benchmarks and 13.3% on out-of-distribution tasks.

## 23. Thinking Like a Botanist: Challenging Multimodal Language Models with Intent Driven Chain-of-Inquiry

- Authors: Syed Nazmus Sakib, Nafiul Haque, Shahrear Bin Amin, Hasan Muhammad Abdullah, Md Mehedi Hasan, Mohammad Zabed Hossain, Shifat E. Arman
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.597057976020344
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.1741/
- PDF: https://aclanthology.org/2026.findings-acl.1741.pdf
- Local PDF: pdf/2026-10-26_23_Thinking Like a Botanist_ Challenging Multimodal Language Models with Intent Driven Chain-of-Inquiry.pdf

Vision evaluations are typically done through multi-step processes. In most contemporary fields, experts analyze images using structured, evidence-based adaptive questioning. In plant pathology, botanists inspect leaf images, identify visual cues, infer diagnostic intent, and probe further with targeted questions that adapt to species, symptoms, and severity. This structured probing is crucial for accurate disease diagnosis and treatment formulation. Yet current vision-language models are evaluated on single-turn question answering. To address this gap, we introduce PlantInquiryVQA, a benchmark for studying multi-step, intent-driven visual reasoning in botanical diagnosis. We formalize a Chain of Inquiry framework modeling diagnostic trajectories as ordered question-answer sequences conditioned on grounded visual cues and explicit epistemic intent. We release a dataset of 24,964 expert-curated plant images and 138,078 question-answer pairs annotated with visual grounding, severity labels, and domain-specific reasoning templates. Evaluations on top-tier Multimodal Large Language Models reveal that while they describe visual symptoms adequately, they struggle with safe clinical reasoning and accurate diagnosis. Importantly, structured question-guided inquiry significantly improves diagnostic correctness, reduces hallucination, and increases reasoning efficiency. PlantInquiryVQA provides a foundation for training diagnostic agents that reason like expert botanists rather than static classifiers.

## 24. From Selection to Refinement: Iterative Optimization for Instruction Data

- Authors: Hang Hu, Ziyan Liu, Rujie Wen, Ruihui Hou, Xueyan Wu, Mu Zhang, Jianxing Yu, Tong Ruan, Jingping Liu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.5970125447406085
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1889/
- PDF: https://aclanthology.org/2026.acl-long.1889.pdf
- Local PDF: pdf/2026-10-26_24_From Selection to Refinement_ Iterative Optimization for Instruction Data.pdf

Instruction tuning plays a crucial role in enhancing large language models (LLMs) to better understand complex user instructions. While various data selection and revision methods have been explored to optimize instruction tuning datasets, they face two main challenges: unreasonable pruning of potentially valuable low-quality data and the persistence of noise or semantic drift during revision. To address these issues, we propose a novel automated iterative framework for instruction data optimization. Our framework introduces Instruction Quality Differentiation to identify valuable high-quality and low-quality data across multiple dimensions. For low-quality data, we propose a Feedback-driven Iterative Refinement mechanism with an “evaluate-refine-review” process and design an Output Alignment module to improve data quality. Experiments on seven public benchmark datasets show that our framework outperforms state-of-the-art methods, achieving 2.09% and 2.60% improvements on the Alpaca and Dolly datasets, respectively, with high data efficiency. Our code and data are available at the anonymous link https://github.com/surihuhang/From-Selection-to-Refinement–-Iterative-Optimization-for-Instruction-Data .

## 25. DeepPlanner: Scaling Planning Capability for Deep Research Agents via Advantage Shaping

- Authors: Wei Fan, Wenlin Yao, Zheng Li, Feng Yao, Xin Liu, Liang Qiu, Qingyu Yin, Yangqiu Song, Bing Yin
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.596893241329096
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.370/
- PDF: https://aclanthology.org/2026.findings-acl.370.pdf
- Local PDF: pdf/2026-10-26_25_DeepPlanner_ Scaling Planning Capability for Deep Research Agents via Advantage Shaping.pdf

Large language models (LLMs) augmented with multi-step reasoning and action generation abilities have shown promise in leveraging external tools to tackle complex tasks that require long-horizon planning. However, existing approaches either rely on implicit planning in the reasoning stage or introduce explicit planners without systematically addressing how to optimize the planning stage. As evidence, we observe that under vanilla reinforcement learning (RL), planning tokens exhibit significantly higher entropy than other action tokens, revealing uncertain decision points that remain under-optimized. To address this, we introduce DeepPlanner, an end-to-end RL framework that effectively enhances the planning capabilities of deep research agents. Our approach shapes token-level advantage with an entropy-based term to allocate larger updates to high entropy tokens, and selectively upweights sample-level advantages for planning-intensive rollouts. Extensive experiments across seven deep research benchmarks demonstrate that DeepPlanner improves planning quality and achieves state-of-the-art results under a substantially lower training budget.

## 26. Right at My Level: A Unified Multilingual Framework for Proficiency-Aware Text Simplification

- Authors: Jinhong Jeong, Junghun Park, Youngjae Yu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.5967782946019726
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.1086/
- PDF: https://aclanthology.org/2026.acl-long.1086.pdf
- Local PDF: pdf/2026-10-26_26_Right at My Level_ A Unified Multilingual Framework for Proficiency-Aware Text Simplification.pdf

Text simplification supports second language (L2) learning by providing comprehensible input, consistent with the Input Hypothesis. However, constructing personalized parallel corpora is costly, while existing large language model (LLM)-based readability control methods rely on pre-labeled sentence corpora and primarily target English. We propose Re-RIGHT, a unified reinforcement learning framework for adaptive multilingual text simplification without parallel corpus supervision. We first show that prompting-based lexical simplification at target proficiency levels (CEFR, JLPT, TOPIK, and HSK) performs poorly at easier levels and for non-English languages, even with state-of-the-art LLMs such as GPT-5.2 and Gemini 2.5. To address this, we collect 43K vocabulary-level data across four languages (English, Japanese, Korean, and Chinese) and train a compact 4B policy model using Re-RIGHT, which integrates three reward modules: vocabulary coverage, semantic preservation, and coherence. Compared to the stronger LLM baselines, Re-RIGHT achieves higher lexical coverage at target proficiency levels while maintaining original meaning and fluency.

## 27. TempTool-R1: Tool-Augmented Reinforcement Learning for Temporal Knowledge Graph Question Answering

- Authors: Zicheng Huang, Yajuan Tong, Xinhui Tu, Tingting He
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.596735958494525
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.797/
- PDF: https://aclanthology.org/2026.findings-acl.797.pdf
- Local PDF: pdf/2026-10-26_27_TempTool-R1_ Tool-Augmented Reinforcement Learning for Temporal Knowledge Graph Question Answering.pdf

Temporal knowledge graph question answering (TKGQA) addresses time-sensitive queries over temporal knowledge graphs, but existing approaches struggle with multi-hop reasoning and implicit temporal constraints. We introduce TempTool-R1, a novel tool-integrated reasoning framework that enables large language models to explicitly use temporal tools for precise reasoning. First, we design a unified temporal tool-based API capable of transforming implicit temporal cues into executable operations, establishing the structural foundation for tool interaction. In the second stage, supervised fine-tuning teaches the model to interweave chain-of-thought reasoning with think-then-tool usage, allowing it to call temporal tools during inference. Finally, we apply reinforcement learning with fine-grained, order-sensitive reward functions tailored for temporal tool use, further refining the model’s tool-use policy. Experiments on three challenging TKGQA benchmarks demonstrate that TempTool-R1 significantly outperforms existing methods. In particular, our approach excels on complex questions requiring multi-hop temporal reasoning, highlighting the effectiveness of temporal tool integration and reward optimization in improving TKGQA performance.

## 28. ReasMark: A Robust Watermark for Attributing LLM Reasoning Under Knowledge Distillation Attacks

- Authors: Peizhuo Lv, Ruihua Zhou, Yunpeng Li, Ruigang Liang, Xingshuo Han, XiaoFeng Wang, Wei Dong, Yuling Liu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.5965434488236925
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-long.2185/
- PDF: https://aclanthology.org/2026.acl-long.2185.pdf
- Local PDF: pdf/2026-10-26_28_ReasMark_ A Robust Watermark for Attributing LLM Reasoning Under Knowledge Distillation Attacks.pdf

Reasoning-enhanced large language models rely on intermediate reasoning signals to solve complex, multi-step tasks, making reasoning behavior a valuable form of intellectual property. Meanwhile, knowledge distillation enables an adversary to replicate this behavior in a realistic black-box setting by repeatedly querying a deployed model on a target domain and training a local student to imitate its outputs, including reasoning traces. Existing LLM watermarks primarily operate on surface text and decoding-time token biases, and thus fail to provide reliable attribution of reasoning behavior once it is transferred through knowledge distillation. ReasMark entangles the watermark with the target-domain input distribution by selecting watermark tokens from high-frequency prompts, so distillation queries naturally activate it. It then embeds the watermark by score-conditioned losses that create a detectable reasoning-length gap for black-box verification. Comprehensive experiments across multiple LLMs, datasets, and distillation settings demonstrate that ReasMark consistently outperforms existing baselines while preserving task utility.

## 29. Beyond Uniform SVD: Dual-Level Optimization across Columns and Modules for LLM Compression

- Authors: Lin Xv, Xian Gao, Ting Liu, Yuzhuo fu
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.5965040094274867
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.findings-acl.912/
- PDF: https://aclanthology.org/2026.findings-acl.912.pdf
- Local PDF: pdf/2026-10-26_29_Beyond Uniform SVD_ Dual-Level Optimization across Columns and Modules for LLM Compression.pdf

Low-rank decomposition, particularly Singular Value Decomposition (SVD), is a pivotal technique for mitigating the storage and computational demands of Large Language Models (LLMs). However, prevalent SVD-based approaches overlook the critical phenomenon that decomposition errors exhibit significant disparity across different components of the parameter matrix, often leading to suboptimal approximation. Furthermore, existing methods lack a direct metric to evaluate the importance of individual weight matrices. To address these limitations, we propose Duo-SVD ( Du al-level O ptimization SVD ), a novel training-free framework that synergizes optimization at both the column and the module levels. First, Duo-SVD incorporates a Column-Preserving Strategy that explicitly retains columns exhibiting high decomposition errors, while applying low-rank approximation solely to those with lower errors. Second, at the module level, we employ a Module-Adaptive Allocation Strategy that formulates ratio allocation as a global constrained optimization problem based on perturbation-induced model deviation. Extensive experiments demonstrate that Duo-SVD consistently outperforms state-of-the-art SVD-based baselines and structured pruning methods, establishing it as a superior paradigm for efficient LLM compression.

## 30. Motivating Next-Gen Accelerators with Flexible N:M Activation Sparsity via Benchmarking Lightweight Post-Training Sparsification Approaches

- Authors: Shirin Alanova, Kristina Kazistova, Ekaterina Galaeva, Alina Kostromina, Vladimir Smirnov, Redko Dmitry, Alexey Dontsov, Maxim Zhelnin, Evgeny Burnaev, Egor Shvetsov
- Source: acl_anthology
- Venue type: conference
- Journal: ACL
- Publication status: formally_published
- Publication date: 2026-01-01
- DOI: Unavailable
- Categories: Unknown
- Relevance: 2.5964489028979325
- Tracking confidence: N/A
- Source hits: N/A
- Matched researchers: N/A
- Matched groups: N/A
- Article: https://aclanthology.org/2026.acl-industry.17/
- PDF: https://aclanthology.org/2026.acl-industry.17.pdf
- Local PDF: pdf/2026-10-26_30_Motivating Next-Gen Accelerators with Flexible N_M Activation Sparsity via Benchmarking Lightweight Post-Training Sparsi.pdf

The demand for efficient large language model inference has spurred interest in sparsification, yet current hardware support remains narrowly focused on 2:4 weight sparsity. In this work, we argue that activation sparsity despite being overlooked in hardware design offers a promising path for dynamic, input-adaptive compression with significant I/O and memory benefits. We present a comprehensive post-training study of N:M activation pruning across four LLMs (Llama2-7B-chat, Llama3.1-8B-Instruct, Qwen2.5-7B-Instruct, Gemma3-4B-Instruct), demonstrating that activation pruning consistently outperforms weight pruning at matched sparsity levels. We evaluate lightweight, plug-and-play error mitigation and selection strategies that require minimal or no calibration data across four sparsity patterns: 2:4, 4:8, 8:16, and 16:32. Among these, 16:32 approaches the performance of unstructured 50% sparsity and is is approximately 2.7 × better than 2:4, while 8:16 offers an optimal balance of accuracy and practicality. Our results provide evidence that next-generation accelerators should consider native support for N:M activation sparsity and can serve as a strong baseline for the future methods.
