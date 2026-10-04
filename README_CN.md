# Awesome Agentic AIGC Detection

[English](README.md) | [简体中文](README_CN.md)

整理面向生成图像与视频检测的智能体相关论文，并注明图像编辑、音频篡改等相关任务。

## 目录

- [已发表 / 已录用论文](#published-accepted)
  - [2026](#published-2026)
- [预印本](#preprints)
  - [2026](#preprints-2026)
  - [2025](#preprints-2025)
- [方法索引](#method-index)
- [补充与纠错](#contributing)

<a id="published-accepted"></a>

## 已发表 / 已录用论文

发表与录用信息核实日期为 **2026-10-04**；会议名称链接至论文集或录用依据，Findings 与主会分开标注。

<a id="published-2026"></a>

### 2026

<a id="hermes"></a>

**[ICML 2026 · 已发表](https://proceedings.mlr.press/v306/li26be.html)** [Hermes: An Evidence-Driven Agentic Framework for Trustworthy and Explainable AI-Generated Video Detection](https://proceedings.mlr.press/v306/li26be.html)

面向生成视频检测，检索取证计划，再通过工具辅助的多智能体讨论修订证据图并请求补充证据。

<a id="forenagent"></a>

**[ECCV 2026 · 已发表](https://link.springer.com/chapter/10.1007/978-3-032-37592-6_12)** [Code-in-the-Loop Forensics: Agentic Tool Use for Image Forgery Detection](https://arxiv.org/abs/2512.16300) (ForenAgent)

面向生成图像及局部编辑，生成并执行 Python 代码，根据返回的文本和可视化结果继续分析。

<a id="safeguard"></a>

**[ECCV 2026 · 已发表](https://link.springer.com/chapter/10.1007/978-3-032-37029-7_33)** [SafeGuard: A Multi-Agent Perception-Reasoning Framework for Social-Risk AI-Generated Video Detection](https://arxiv.org/abs/2607.03069)

面向具有社会风险的生成视频，核查证据对假设的支持程度，并在验证不足时修订假设、重新感知与推理。

<a id="unishield"></a>

**[CVPR Findings 2026 · 已发表](https://openaccess.thecvf.com/content/CVPR2026F/html/Huang_UniShield_An_Adaptive_Multi-Agent_Framework_for_Unified_Forgery_Image_Detection_CVPRF_2026_paper.html)** [UniShield: An Adaptive Multi-Agent Framework for Unified Forgery Image Detection and Localization](https://arxiv.org/abs/2510.03161)

覆盖生成图像及人脸、局部图像和文档篡改，将输入路由至单个检测器并汇总结果，不采用回溯或多工具协作。

<a id="defake-o3"></a>

**[ACM Multimedia 2026 · 已录用](https://arxiv.org/abs/2608.16259)** [Defake-o3: From Speculative Rationales to Verifiable Evidence for Explainable AIGI Detection](https://arxiv.org/abs/2608.16259)

面向生成图像检测，自适应选择局部区域进行观察后作出判断；Evidence Verifier 用于训练奖励，并非测试时的验证环节。

<a id="atar"></a>

**[ACM Multimedia 2026 · 口头报告 · 已录用](https://arxiv.org/abs/2609.39066)** [Agentic Tool-Augmented Reasoning for Explainable Image Forgery Detection](https://arxiv.org/abs/2609.39066) (ATAR)

覆盖 AIGC 检测及图像编辑、人脸和文档篡改，根据返回结果交替调用裁剪与取证工具。

<a id="forgeryvcr"></a>

**[ACM Multimedia 2026 · 口头报告 · 已录用](https://github.com/youqiwong/ForgeryVCR)** [ForgeryVCR: Visual-Centric Reasoning via Efficient Forensic Tools in MLLMs for Image Forgery Detection and Localization](https://arxiv.org/abs/2602.14098)

面向相关的图像篡改检测与定位，选择性调用取证变换和局部放大，并将可视化结果用于后续推理。

<a id="preprints"></a>

## 预印本

以下论文截至 **2026-10-04** 尚未核实正式发表或录用信息；按 arXiv 首次提交年份归档，同年按时间倒序排列。

<a id="preprints-2026"></a>

### 2026

<a id="omnivl-guard-pro"></a>

**[arXiv 2026 · 预印本]** [OmniVL-Guard Pro: A Tool-Augmented Agent for Omnibus Vision-Language Forensics](https://arxiv.org/abs/2605.16962)

覆盖生成图像/视频及相关的定位、事实核查任务，根据已有观测选择后续工具与参数；检查器引导的训练属于独立环节。

<a id="agentfox"></a>

**[arXiv 2026 · 预印本]** [AgentFoX: LLM Agent-Guided Fusion with eXplainability for AI-Generated Image Detection](https://arxiv.org/abs/2603.23115)

面向生成图像检测，先调用各个专家，再在结果冲突时查询可靠性档案，调整证据解释而非重新规划检测器调用。

<a id="evoguard"></a>

**[arXiv 2026 · 预印本]** [EvoGuard: An Extensible Agentic RL-based Framework for Practical and Evolving AI-Generated Image Detection](https://arxiv.org/abs/2603.17343)

面向生成图像检测，依据能力档案选择检测器，并根据结果决定继续调用工具或停止。

<a id="preprints-2025"></a>

### 2025

<a id="aifo"></a>

**[arXiv 2025 · 预印本]** [From Evidence to Verdict: An Agent-Based Forensic Framework for AI-Generated Image Detection](https://arxiv.org/abs/2511.00181) (AIFo)

面向生成图像检测，执行初始工具集后，在证据不足或冲突时启动讨论，不重新规划证据采集。

<a id="fakehunter"></a>

**[arXiv 2025 · 预印本]** [Memory-Anchored Multimodal Reasoning for Explainable Video Forensics](https://arxiv.org/abs/2508.14581) (FakeHunter)

面向相关的视频和音频篡改，检索参考样例，并在置信度不足时调用视觉或音频工具进行条件验证，随后给出解释。

<a id="method-index"></a>

## 方法索引

- **自适应工具调用：** [EvoGuard](#evoguard)、[ForenAgent](#forenagent)、[ATAR](#atar)、[OmniVL-Guard Pro](#omnivl-guard-pro)。
- **主动视觉观察：** [Defake-o3](#defake-o3)、[ForgeryVCR](#forgeryvcr)。
- **多智能体证据推理：** [SafeGuard](#safeguard)、[Hermes](#hermes)、[AIFo](#aifo)。
- **专家路由与证据融合：** [UniShield](#unishield)、[AgentFoX](#agentfox)。
- **检索与条件验证：** [FakeHunter](#fakehunter)。

<a id="contributing"></a>

## 补充与纠错

欢迎[推荐论文](https://github.com/liu33333/Awesome-Agentic-AIGC-Detection/issues/new?template=paper_suggestion.md)或[提交纠错](https://github.com/liu33333/Awesome-Agentic-AIGC-Detection/issues/new?template=correction.md)。请提供完整标题、发表状态、会议或期刊及来源，以及支持方法描述的章节或图。详见 [CONTRIBUTING.md](CONTRIBUTING.md)。
