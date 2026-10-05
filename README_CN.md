![Awesome Agentic AIGC Detection. 取证主题插画：图像、音频和文本线索连接智能体、局部放大检查与证据报告。](assets/banner.svg)

[English](README.md) · **简体中文**

[简介](#intro) · [动态](#news) · [音频](#audio) · [视觉（图像与视频）](#visual) · [文本](#text) · [跨模态](#cross-modal) · **[技术对比 →](docs/COMPARISON_CN.md)**

<a name="intro"></a>

## 简介 · Intro

本仓库整理面向 AI 生成内容与相关媒体篡改检测的智能体研究，关注工具调用、证据驱动推理与多智能体协作等方法。论文按输入模态分类，提供发表信息和官方实现的开放情况。

模型仅列鉴伪推理所用模型；“智能体免训练”指无需针对该任务更新智能体参数，工具训练、校准与检索记忆见[推理配置](docs/COMPARISON_CN.md#inference-setups)。

<a name="news"></a>

## 动态 · News

- **2026‑10‑04**：上线[技术对比](docs/COMPARISON_CN.md)，从五个维度并列比较收录方法。
- **2026‑10‑04**：仓库上线，整理 Agentic AIGC 检测相关论文。

<a name="audio"></a>

## 音频

暂无收录。

<a name="visual"></a>

## 视觉（图像与视频）

| 论文 / 任务 / 模型 | 发表位置 / 状态 | 日期 | 官方仓库 |
| --- | --- | --- | --- |
| <a name="atar"></a>**[Agentic Tool-Augmented Reasoning for Explainable Image Forgery Detection](https://arxiv.org/abs/2609.39066)** (ATAR)<br><sub>图像 · <b>检测 · 定位 · 解释</b></sub><br><sub>模型：Qwen3-VL-8B-Instruct<br>智能体免训练：否</sub> | ACM&nbsp;Multimedia<br>2026<br><sub>口头报告 · 已录用</sub> | 2026‑09‑30 | — |
| <a name="forenagent"></a>**[Code-in-the-Loop Forensics: Agentic Tool Use for Image Forgery Detection](https://arxiv.org/abs/2512.16300)** (ForenAgent)<br><sub>图像 · <b>检测 · 解释</b></sub><br><sub>模型：Qwen2.5-VL-7B<br>智能体免训练：否</sub> | ECCV&nbsp;2026<br><sub>已发表</sub> | 2026‑09‑08 | [仅⁠工⁠具⁠集](https://github.com/zfr00/ForenAgent) |
| <a name="safeguard"></a>**[SafeGuard: A Multi-Agent Perception-Reasoning Framework for Social-Risk AI-Generated Video Detection](https://arxiv.org/abs/2607.03069)**<br><sub>视频 · <b>检测 · 解释</b></sub><br><sub>模型：GPT-4o + Gemini-2.5-Pro<br>智能体免训练：是（工具经调优）</sub> | ECCV&nbsp;2026<br><sub>已发表</sub> | 2026‑09‑08 | [项目；<br>代⁠码⁠待⁠发⁠布](https://github.com/williamw99/SafeGuard) |
| <a name="defake-o3"></a>**[Defake-o3: From Speculative Rationales to Verifiable Evidence for Explainable AIGI Detection](https://arxiv.org/abs/2608.16259)**<br><sub>图像 · <b>检测 · 定位 · 解释</b></sub><br><sub>模型：Qwen3-VL-8B-Instruct<br>智能体免训练：否</sub> | ACM&nbsp;Multimedia<br>2026<br><sub>已录用</sub> | 2026‑08‑17 | — |
| <a name="hermes"></a>**[Hermes: An Evidence-Driven Agentic Framework for Trustworthy and Explainable AI-Generated Video Detection](https://proceedings.mlr.press/v306/li26be.html)**<br><sub>视频 · <b>检测 · 解释</b></sub><br><sub>模型：Qwen3-VL-8B + ChatGPT-5<br>智能体免训练：是</sub> | ICML&nbsp;2026<br><sub>已发表</sub> | 2026‑07‑06 | — |
| <a name="unishield"></a>**[UniShield: An Adaptive Multi-Agent Framework for Unified Forgery Image Detection and Localization](https://arxiv.org/abs/2510.03161)**<br><sub>图像 · <b>检测 · 定位 · 解释</b></sub><br><sub>模型：Qwen2.5-VL + GPT-4o<br>智能体免训练：否</sub> | CVPR&nbsp;Findings<br>2026<br><sub>已发表</sub> | 2026‑06‑03 | — |
| <a name="agentfox"></a>**[AgentFoX: LLM Agent-Guided Fusion with eXplainability for AI-Generated Image Detection](https://arxiv.org/abs/2603.23115)**<br><sub>图像 · <b>检测 · 解释</b></sub><br><sub>模型：Qwen3-32B + GPT-4o<br>智能体免训练：是（需校准）</sub> | arXiv&nbsp;2026<br><sub>预印本</sub> | 2026‑03‑24 | [最⁠小⁠推⁠理⁠实⁠现](https://github.com/suncore946/AgentFoX) |
| <a name="evoguard"></a>**[EvoGuard: An Extensible Agentic RL-based Framework for Practical and Evolving AI-Generated Image Detection](https://arxiv.org/abs/2603.17343)**<br><sub>图像 · <b>检测</b></sub><br><sub>模型：Qwen3-VL-4B-Instruct<br>智能体免训练：否</sub> | arXiv&nbsp;2026<br><sub>预印本</sub> | 2026‑03‑18 | — |
| <a name="forgeryvcr"></a>**[ForgeryVCR: Visual-Centric Reasoning via Efficient Forensic Tools in MLLMs for Image Forgery Detection and Localization](https://arxiv.org/abs/2602.14098)**<br><sub>图像 · <b>检测 · 定位</b></sub><br><sub>模型：Qwen3-VL-4B-Instruct<br>智能体免训练：否</sub> | ACM&nbsp;Multimedia<br>2026<br><sub>口头报告 · 已录用</sub> | 2026‑02‑15 | [推理 + 权重](https://github.com/youqiwong/ForgeryVCR) |
| <a name="aifo"></a>**[From Evidence to Verdict: An Agent-Based Forensic Framework for AI-Generated Image Detection](https://arxiv.org/abs/2511.00181)** (AIFo)<br><sub>图像 · <b>检测 · 解释</b></sub><br><sub>模型：GPT-4o<br>智能体免训练：是</sub> | arXiv&nbsp;2025<br><sub>预印本</sub> | 2025‑10‑31 | — |

<a name="text"></a>

## 文本

暂无收录。

<a name="cross-modal"></a>

## 跨模态

| 论文 / 任务 / 模型 | 发表位置 / 状态 | 日期 | 官方仓库 |
| --- | --- | --- | --- |
| <a name="omnivl-guard-pro"></a>**[OmniVL-Guard Pro: A Tool-Augmented Agent for Omnibus Vision-Language Forensics](https://arxiv.org/abs/2605.16962)**<br><sub>文图 / 文视频 · <b>检测 · 定位</b></sub><br><sub>模型：Qwen3-VL-8B<br>智能体免训练：否</sub> | arXiv&nbsp;2026<br><sub>预印本</sub> | 2026‑05‑16 | [项目；<br>代⁠码⁠待⁠发⁠布](https://github.com/shen8424/OmniVL-Guard-Pro) |
| <a name="fakehunter"></a>**[Memory-Anchored Multimodal Reasoning for Explainable Video Forensics](https://arxiv.org/abs/2508.14581)** (FakeHunter)<br><sub>音视频 · <b>检测 · 解释</b></sub><br><sub>模型：Qwen2.5-Omni-7B；备选 MiniCPM-o-2_6<br>智能体免训练：是（需构建记忆）</sub> | arXiv&nbsp;2025<br><sub>预印本</sub> | 2025‑08‑20 | — |


