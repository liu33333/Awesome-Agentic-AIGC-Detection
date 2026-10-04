# Awesome Agentic AIGC Detection

[English](README.md) | [简体中文](README_CN.md)

按输入模态整理的 Agentic AIGC 检测论文，涵盖生成内容检测及相关篡改取证任务。

## 目录

- [图像](#images)
- [视频](#videos)
- [图像与视频](#images-and-videos)
- [音视频](#audio-video)
- [补充与纠错](#contributing)

各表按日期倒序排列：已发表论文采用会议开幕日期，预印本及尚未核实正式出版的已录用论文采用 arXiv 首次提交日期；日期与发表信息均链接至依据，状态核实于 2026-10-04。

<a id="images"></a>

## 图像

| 论文 | 发表位置 / 状态 | 日期 | 任务 | 技术分类 |
| --- | --- | --- | --- | --- |
| <a id="atar"></a>**[Agentic Tool-Augmented Reasoning for Explainable Image Forgery Detection](https://arxiv.org/abs/2609.39066)** (ATAR) | [ACM Multimedia 2026 · 口头报告 · 已录用](https://arxiv.org/abs/2609.39066) | [2026-09-30](https://arxiv.org/abs/2609.39066) | 生成图像 · 人脸/局部/文档篡改 | 自适应工具调用 · 裁剪 · 取证工具 |
| <a id="forenagent"></a>**[Code-in-the-Loop Forensics: Agentic Tool Use for Image Forgery Detection](https://arxiv.org/abs/2512.16300)** (ForenAgent) | [ECCV 2026 · 已发表](https://link.springer.com/chapter/10.1007/978-3-032-37592-6_12) | [2026-09-08](https://eccv.ecva.net/Conferences/2026/Venues) | 生成图像 · 局部编辑 | 代码执行 · 工具结果反馈 |
| <a id="defake-o3"></a>**[Defake-o3: From Speculative Rationales to Verifiable Evidence for Explainable AIGI Detection](https://arxiv.org/abs/2608.16259)** | [ACM Multimedia 2026 · 已录用](https://arxiv.org/abs/2608.16259) | [2026-08-17](https://arxiv.org/abs/2608.16259) | 生成图像检测 | 主动视觉观察 · 自适应裁剪 |
| <a id="unishield"></a>**[UniShield: An Adaptive Multi-Agent Framework for Unified Forgery Image Detection and Localization](https://arxiv.org/abs/2510.03161)** | [CVPR Findings 2026 · 已发表](https://openaccess.thecvf.com/content/CVPR2026F/html/Huang_UniShield_An_Adaptive_Multi-Agent_Framework_for_Unified_Forgery_Image_Detection_CVPRF_2026_paper.html) | [2026-06-03](https://cvpr.thecvf.com/Conferences/2026/Dates) | 生成图像 · 人脸/局部/文档篡改 | 单检测器路由 · 结果汇总 |
| <a id="agentfox"></a>**[AgentFoX: LLM Agent-Guided Fusion with eXplainability for AI-Generated Image Detection](https://arxiv.org/abs/2603.23115)** | arXiv 2026 · 预印本 | [2026-03-24](https://arxiv.org/abs/2603.23115) | 生成图像检测 | 固定专家调用 · 可靠性档案融合 |
| <a id="evoguard"></a>**[EvoGuard: An Extensible Agentic RL-based Framework for Practical and Evolving AI-Generated Image Detection](https://arxiv.org/abs/2603.17343)** | arXiv 2026 · 预印本 | [2026-03-18](https://arxiv.org/abs/2603.17343) | 生成图像检测 | 档案引导检测器选择 · 自适应停止 |
| <a id="forgeryvcr"></a>**[ForgeryVCR: Visual-Centric Reasoning via Efficient Forensic Tools in MLLMs for Image Forgery Detection and Localization](https://arxiv.org/abs/2602.14098)** | [ACM Multimedia 2026 · 口头报告 · 已录用](https://github.com/youqiwong/ForgeryVCR) | [2026-02-15](https://arxiv.org/abs/2602.14098) | 篡改检测与定位 | 主动视觉观察 · 取证变换 · 局部放大 |
| <a id="aifo"></a>**[From Evidence to Verdict: An Agent-Based Forensic Framework for AI-Generated Image Detection](https://arxiv.org/abs/2511.00181)** (AIFo) | arXiv 2025 · 预印本 | [2025-10-31](https://arxiv.org/abs/2511.00181) | 生成图像检测 | 初始工具集 · 条件式多智能体讨论 |

<a id="videos"></a>

## 视频

| 论文 | 发表位置 / 状态 | 日期 | 任务 | 技术分类 |
| --- | --- | --- | --- | --- |
| <a id="safeguard"></a>**[SafeGuard: A Multi-Agent Perception-Reasoning Framework for Social-Risk AI-Generated Video Detection](https://arxiv.org/abs/2607.03069)** | [ECCV 2026 · 已发表](https://link.springer.com/chapter/10.1007/978-3-032-37029-7_33) | [2026-09-08](https://eccv.ecva.net/Conferences/2026/Venues) | 生成视频检测 · 社会风险 | 多智能体推理 · 假设验证 · 重新感知 |
| <a id="hermes"></a>**[Hermes: An Evidence-Driven Agentic Framework for Trustworthy and Explainable AI-Generated Video Detection](https://proceedings.mlr.press/v306/li26be.html)** | [ICML 2026 · 已发表](https://proceedings.mlr.press/v306/li26be.html) | [2026-07-06](https://icml.cc/Conferences/2026/CallForPapers) | 生成视频检测 | 计划检索 · 多智能体讨论 · 证据图修订 |

<a id="images-and-videos"></a>

## 图像与视频

支持图像或视频输入的方法。

| 论文 | 发表位置 / 状态 | 日期 | 任务 | 技术分类 |
| --- | --- | --- | --- | --- |
| <a id="omnivl-guard-pro"></a>**[OmniVL-Guard Pro: A Tool-Augmented Agent for Omnibus Vision-Language Forensics](https://arxiv.org/abs/2605.16962)** | arXiv 2026 · 预印本 | [2026-05-16](https://arxiv.org/abs/2605.16962) | 生成图像/视频 · 定位 · 事实核查 | 自适应工具选择 · 参数调整 |

<a id="audio-video"></a>

## 音视频

同时分析视觉与音频证据的方法。

| 论文 | 发表位置 / 状态 | 日期 | 任务 | 技术分类 |
| --- | --- | --- | --- | --- |
| <a id="fakehunter"></a>**[Memory-Anchored Multimodal Reasoning for Explainable Video Forensics](https://arxiv.org/abs/2508.14581)** (FakeHunter) | arXiv 2025 · 预印本 | [2025-08-20](https://arxiv.org/abs/2508.14581) | 视频/音频篡改 | 参考样例检索 · 条件式视觉/音频验证 |

<a id="contributing"></a>

## 补充与纠错

欢迎[推荐论文](https://github.com/liu33333/Awesome-Agentic-AIGC-Detection/issues/new?template=paper_suggestion.md)或[提交纠错](https://github.com/liu33333/Awesome-Agentic-AIGC-Detection/issues/new?template=correction.md)。请提供完整标题、输入模态、发表位置与状态、排序日期及来源，以及任务和方法的依据。详见 [CONTRIBUTING.md](CONTRIBUTING.md)。
