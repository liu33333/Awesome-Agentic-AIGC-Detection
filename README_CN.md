![Agentic AIGC Detection：概念性青色线框人脸、琥珀色检查区域与局部细节可视化。](assets/banner.svg)

[English](README.md) · **简体中文**

[简介](#intro) · [动态](#news) · [音频](#audio) · [视觉（图像与视频）](#visual) · [文本](#text) · [跨模态](#cross-modal) · **[技术对比 →](docs/COMPARISON_CN.md)** · [资源](#resources)

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

<table>
<thead>
<tr>
<th width="340" align="left">论文<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</th>
<th width="170" align="left">发表位置 / 状态</th>
<th width="112" align="left">日期</th>
<th width="150" align="left">输入 / 任务</th>
<th width="170" align="left">鉴伪模型&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</th>
<th width="145" align="left">智⁠能⁠体<br>免⁠训⁠练</th>
<th width="130" align="left">官方仓库</th>
</tr>
</thead>
<tbody>
<tr>
<td width="340" valign="top"><a name="atar"></a><strong><a href="https://arxiv.org/abs/2609.39066">Agentic Tool-Augmented Reasoning for Explainable Image Forgery Detection</a></strong> (ATAR)</td>
<td width="170" valign="top">ACM&nbsp;Multimedia<br>2026<br><sub>口头报告 · 已录用</sub></td>
<td width="112" valign="top">2026‑09‑30</td>
<td width="150" valign="top">图像<br><sub>检测&nbsp;·&nbsp;定位&nbsp;·&nbsp;解释</sub></td>
<td width="170" valign="top">Qwen3-VL-8B-Instruct</td>
<td width="145" valign="top">否</td>
<td width="130" valign="top">—</td>
</tr>
<tr>
<td width="340" valign="top"><a name="forenagent"></a><strong><a href="https://arxiv.org/abs/2512.16300">Code-in-the-Loop Forensics: Agentic Tool Use for Image Forgery Detection</a></strong> (ForenAgent)</td>
<td width="170" valign="top">ECCV&nbsp;2026<br><sub>已发表</sub></td>
<td width="112" valign="top">2026‑09‑08</td>
<td width="150" valign="top">图像<br><sub>检测&nbsp;·&nbsp;解释</sub></td>
<td width="170" valign="top">Qwen2.5-VL-7B</td>
<td width="145" valign="top">否</td>
<td width="130" valign="top"><a href="https://github.com/zfr00/ForenAgent">仅⁠工⁠具⁠集</a></td>
</tr>
<tr>
<td width="340" valign="top"><a name="safeguard"></a><strong><a href="https://arxiv.org/abs/2607.03069">SafeGuard: A Multi-Agent Perception-Reasoning Framework for Social-Risk AI-Generated Video Detection</a></strong></td>
<td width="170" valign="top">ECCV&nbsp;2026<br><sub>已发表</sub></td>
<td width="112" valign="top">2026‑09‑08</td>
<td width="150" valign="top">视频<br><sub>检测&nbsp;·&nbsp;解释</sub></td>
<td width="170" valign="top">GPT-4o + Gemini-2.5-Pro</td>
<td width="145" valign="top">是<br><sub>工具经调优</sub></td>
<td width="130" valign="top"><a href="https://github.com/williamw99/SafeGuard">项目；<br>代⁠码⁠待⁠发⁠布</a></td>
</tr>
<tr>
<td width="340" valign="top"><a name="defake-o3"></a><strong><a href="https://arxiv.org/abs/2608.16259">Defake-o3: From Speculative Rationales to Verifiable Evidence for Explainable AIGI Detection</a></strong></td>
<td width="170" valign="top">ACM&nbsp;Multimedia<br>2026<br><sub>已录用</sub></td>
<td width="112" valign="top">2026‑08‑17</td>
<td width="150" valign="top">图像<br><sub>检测&nbsp;·&nbsp;定位&nbsp;·&nbsp;解释</sub></td>
<td width="170" valign="top">Qwen3-VL-8B-Instruct</td>
<td width="145" valign="top">否</td>
<td width="130" valign="top">—</td>
</tr>
<tr>
<td width="340" valign="top"><a name="hermes"></a><strong><a href="https://proceedings.mlr.press/v306/li26be.html">Hermes: An Evidence-Driven Agentic Framework for Trustworthy and Explainable AI-Generated Video Detection</a></strong></td>
<td width="170" valign="top">ICML&nbsp;2026<br><sub>已发表</sub></td>
<td width="112" valign="top">2026‑07‑06</td>
<td width="150" valign="top">视频<br><sub>检测&nbsp;·&nbsp;解释</sub></td>
<td width="170" valign="top">Qwen3-VL-8B + ChatGPT-5</td>
<td width="145" valign="top">是</td>
<td width="130" valign="top">—</td>
</tr>
<tr>
<td width="340" valign="top"><a name="unishield"></a><strong><a href="https://arxiv.org/abs/2510.03161">UniShield: An Adaptive Multi-Agent Framework for Unified Forgery Image Detection and Localization</a></strong></td>
<td width="170" valign="top">CVPR&nbsp;Findings<br>2026<br><sub>已发表</sub></td>
<td width="112" valign="top">2026‑06‑03</td>
<td width="150" valign="top">图像<br><sub>检测&nbsp;·&nbsp;定位&nbsp;·&nbsp;解释</sub></td>
<td width="170" valign="top">Qwen2.5-VL + GPT-4o</td>
<td width="145" valign="top">否</td>
<td width="130" valign="top">—</td>
</tr>
<tr>
<td width="340" valign="top"><a name="agentfox"></a><strong><a href="https://arxiv.org/abs/2603.23115">AgentFoX: LLM Agent-Guided Fusion with eXplainability for AI-Generated Image Detection</a></strong></td>
<td width="170" valign="top">arXiv&nbsp;2026<br><sub>预印本</sub></td>
<td width="112" valign="top">2026‑03‑24</td>
<td width="150" valign="top">图像<br><sub>检测&nbsp;·&nbsp;解释</sub></td>
<td width="170" valign="top">Qwen3-32B + GPT-4o</td>
<td width="145" valign="top">是<br><sub>需校准</sub></td>
<td width="130" valign="top"><a href="https://github.com/suncore946/AgentFoX">最⁠小⁠推⁠理⁠实⁠现</a></td>
</tr>
<tr>
<td width="340" valign="top"><a name="evoguard"></a><strong><a href="https://arxiv.org/abs/2603.17343">EvoGuard: An Extensible Agentic RL-based Framework for Practical and Evolving AI-Generated Image Detection</a></strong></td>
<td width="170" valign="top">arXiv&nbsp;2026<br><sub>预印本</sub></td>
<td width="112" valign="top">2026‑03‑18</td>
<td width="150" valign="top">图像<br><sub>检测</sub></td>
<td width="170" valign="top">Qwen3-VL-4B-Instruct</td>
<td width="145" valign="top">否</td>
<td width="130" valign="top">—</td>
</tr>
<tr>
<td width="340" valign="top"><a name="forgeryvcr"></a><strong><a href="https://arxiv.org/abs/2602.14098">ForgeryVCR: Visual-Centric Reasoning via Efficient Forensic Tools in MLLMs for Image Forgery Detection and Localization</a></strong></td>
<td width="170" valign="top">ACM&nbsp;Multimedia<br>2026<br><sub>口头报告 · 已录用</sub></td>
<td width="112" valign="top">2026‑02‑15</td>
<td width="150" valign="top">图像<br><sub>检测&nbsp;·&nbsp;定位</sub></td>
<td width="170" valign="top">Qwen3-VL-4B-Instruct</td>
<td width="145" valign="top">否</td>
<td width="130" valign="top"><a href="https://github.com/youqiwong/ForgeryVCR">推理 + 权重</a></td>
</tr>
<tr>
<td width="340" valign="top"><a name="aifo"></a><strong><a href="https://arxiv.org/abs/2511.00181">From Evidence to Verdict: An Agent-Based Forensic Framework for AI-Generated Image Detection</a></strong> (AIFo)</td>
<td width="170" valign="top">arXiv&nbsp;2025<br><sub>预印本</sub></td>
<td width="112" valign="top">2025‑10‑31</td>
<td width="150" valign="top">图像<br><sub>检测&nbsp;·&nbsp;解释</sub></td>
<td width="170" valign="top">GPT-4o</td>
<td width="145" valign="top">是</td>
<td width="130" valign="top">—</td>
</tr>
</tbody>
</table>

<a name="text"></a>

## 文本

暂无收录。

<a name="cross-modal"></a>

## 跨模态

<table>
<thead>
<tr>
<th width="340" align="left">论文<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</th>
<th width="170" align="left">发表位置 / 状态</th>
<th width="112" align="left">日期</th>
<th width="150" align="left">输入 / 任务</th>
<th width="170" align="left">鉴伪模型&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</th>
<th width="145" align="left">智⁠能⁠体<br>免⁠训⁠练</th>
<th width="130" align="left">官方仓库</th>
</tr>
</thead>
<tbody>
<tr>
<td width="340" valign="top"><a name="omnivl-guard-pro"></a><strong><a href="https://arxiv.org/abs/2605.16962">OmniVL-Guard Pro: A Tool-Augmented Agent for Omnibus Vision-Language Forensics</a></strong></td>
<td width="170" valign="top">arXiv&nbsp;2026<br><sub>预印本</sub></td>
<td width="112" valign="top">2026‑05‑16</td>
<td width="150" valign="top">文图 / 文视频<br><sub>检测&nbsp;·&nbsp;定位</sub></td>
<td width="170" valign="top">Qwen3-VL-8B</td>
<td width="145" valign="top">否</td>
<td width="130" valign="top"><a href="https://github.com/shen8424/OmniVL-Guard-Pro">项目；<br>代⁠码⁠待⁠发⁠布</a></td>
</tr>
<tr>
<td width="340" valign="top"><a name="fakehunter"></a><strong><a href="https://arxiv.org/abs/2508.14581">Memory-Anchored Multimodal Reasoning for Explainable Video Forensics</a></strong> (FakeHunter)</td>
<td width="170" valign="top">arXiv&nbsp;2025<br><sub>预印本</sub></td>
<td width="112" valign="top">2025‑08‑20</td>
<td width="150" valign="top">音视频<br><sub>检测&nbsp;·&nbsp;解释</sub></td>
<td width="170" valign="top">Qwen2.5-Omni-7B；备选 MiniCPM-o-2_6</td>
<td width="145" valign="top">是<br><sub>需构建记忆</sub></td>
<td width="130" valign="top">—</td>
</tr>
</tbody>
</table>

<a name="resources"></a>

## 资源

面向 Agentic 媒体取证研究的平台、模型基座与开发工具。使用前请确认访问条件、模型版本和数据处理条款。

### Agentic 取证平台

- [Resemble Detect Agents](https://docs.resemble.ai/detect/agents) · **托管 API。** 执行媒体真实性调查，以流式形式返回证据与评估；需要已开通 Detect Agents 权限的账户。
- [Clyravision](https://en.merantix-momentum.com/clyravision) · **需联系开通的平台。** 基于 Agent 工作流，结合取证痕迹、元数据与来源／语境核查分析图像；产品页提供演示录像。

### 可接入 Agent 的检测服务

- [Reality Defender RealAPI](https://www.realitydefender.com/product/realapi) · **检测 API。** 分析图像、音频与视频中的操纵痕迹，返回可接入 Agent 证据流程的结构化结果。
- [Sightengine](https://www.sightengine.com/docs/ai-generated-image-detection) · **检测 API。** 提供 AI 生成图像评分，相关文档另含深度伪造与 AI 生成视频检测模型。

### 开放权重模型基座

- [Qwen3-VL](https://github.com/QwenLM/Qwen3-VL) · 支持图像／视频推理与定位的视觉语言模型系列，包含多篇收录方法使用的 4B、8B 版本。
- [Qwen2.5-VL-7B-Instruct](https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct) · 图像／视频理解基座，所属的 Qwen2.5-VL 系列用于 ForenAgent 与 UniShield。
- [Qwen3-32B](https://huggingface.co/Qwen/Qwen3-32B) · 文本推理模型，用于 AgentFoX 的 Agent 引导证据融合。
- [Qwen2.5-Omni-7B](https://huggingface.co/Qwen/Qwen2.5-Omni-7B) · 支持文本、图像、音频与视频理解的全模态基座，用于 FakeHunter。
- [MiniCPM-o 2.6](https://huggingface.co/openbmb/MiniCPM-o-2_6) · 支持视觉、音频与语言的全模态模型，是 FakeHunter 评估的替代基座。

### 闭源模型服务

- [OpenAI API 模型](https://developers.openai.com/api/docs/models) · GPT 系列服务的官方模型目录，多篇收录方法使用该系列；复现时需核对论文中的具体模型或快照。
- [Google Gemini API](https://ai.google.dev/gemini-api/docs/models) · 官方多模态模型目录与 API 文档，涵盖 SafeGuard 使用的 Gemini 系列。

### Agent 框架与工具执行

- [LangGraph](https://docs.langchain.com/oss/python/langgraph/overview) · 支持状态持久化与人工审核的工作流编排框架，可组织多步骤证据收集与仲裁。
- [Pydantic AI](https://pydantic.dev/docs/ai/overview/) · 提供类型化工具、结构化输出与依赖注入的 Python Agent 框架，适合定义清晰的检测器接口。
- [Codex SDK](https://learn.chatgpt.com/docs/codex-sdk) · 以编程方式管理代码 Agent 会话，可用于基于代码的实验与研究流程集成。
- [OpenHands Software Agent SDK](https://docs.openhands.dev/sdk) · 支持 Shell、文件、浏览器与 MCP 工具的自定义 Agent SDK，提供本地与远程执行方式。
- [Pi](https://pi.dev/docs/latest/sdk) · 可嵌入应用的代码 Agent SDK，支持会话配置与工具扩展，用于构建自定义执行流程。
