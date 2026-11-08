![Agentic AIGC Detection：分层风景图像、扫描检查区域，以及通过证据连线连接的放大细节。](assets/banner.svg)

[English](README.md) · **简体中文**

[简介](#intro) · [动态](#news) · [音频](#audio) · [视觉（图像与视频）](#visual) · [文本](#text) · [跨模态](#cross-modal) · **[技术对比 →](docs/COMPARISON_CN.md)** · [相关综述](#surveys) · [资源](#resources)

<a name="intro"></a>

## 简介 · Intro

本仓库整理面向 AI 生成内容与相关媒体篡改检测的智能体研究，关注工具调用、证据驱动推理与多智能体协作等方法。论文按输入模态分类，提供发表信息和官方实现的开放情况。固定工具流程与规则编排等边界方法单独标注，便于对比。

模型仅列鉴伪推理所用模型，目录名称省略 -Instruct 后缀；完整变体、工具训练、校准与检索记忆见[推理配置](docs/COMPARISON_CN.md#inference-setups)。

训练方式针对鉴伪智能体的任务适配：Training-free（免训练）、SFT（监督微调）或 RL（强化学习）。“未报告”表示论文未说明智能体是否进行任务适配，不代表底层工具未经训练。

<a name="news"></a>

## 动态 · News

- **2026‑11‑08**：补齐音频与跨模态工具推理，新增 FACT；单列固定多智能体与规则流程，补充专用取证模型及评测资源，更新 d1／Jev。区分历史补漏、新版本与新发布资源；同步中英文技术对比。
- **2026‑10‑23**：新增 Qwen–LangGraph 文本检测；补充两项明确区分的工具增强／规则编排相关工作，同步技术对比，补充智能体评测综述，更新 Qwen／System-1 模型资源，并核查代码状态。
- **2026‑10‑04**：上线[技术对比](docs/COMPARISON_CN.md)，从五个维度并列比较收录方法。
- **2026‑10‑04**：仓库上线，整理 Agentic AIGC 检测相关论文。

<a name="audio"></a>

## 音频

输入：<code>I</code> 图像 · <code>V</code> 视频 · <code>A</code> 音频 · <code>T</code> 文本<br>任务：<code>D</code> 检测 · <code>L</code> 定位 · <code>E</code> 解释

**[查看技术对比 →](docs/COMPARISON_CN.md#audio)**

<table>
<thead>
<tr>
<th width="400" align="left">论文<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</th>
<th width="115" align="left">发表</th>
<th width="64" align="left">日期</th>
<th width="70" align="left">标签</th>
<th width="180" align="left">模型与训练</th>
<th width="85" align="left">代码</th>
</tr>
</thead>
<tbody>
<tr>
<td width="400" valign="top"><a name="tooldf"></a><strong><a href="https://aclanthology.org/2026.findings-emnlp.842/">ToolDF: Tool-Integrated Reasoning for Mixed-Authenticity Audio Deepfake Detection</a></strong></td>
<td width="115" valign="top">Findings&nbsp;EMNLP<br>2026</td>
<td width="64" valign="top">26/10</td>
<td width="70" valign="top"><code>A</code><br><code>D</code>&nbsp;<code>L</code>&nbsp;<code>E</code></td>
<td width="180" valign="top">Qwen2.5‑Omni‑3B<br><sub>SFT</sub></td>
<td width="85" valign="top"><a href="https://github.com/rlataewoo/tooldf">代码</a></td>
</tr>
<tr>
<td width="400" valign="top"><a name="sear"></a><strong><a href="https://arxiv.org/abs/2609.39847">SEAR: Spoofing Evidence-Grounded Audio Reasoning Benchmark for Audio Language Models</a></strong> (BAEA)</td>
<td width="115" valign="top">arXiv&nbsp;2026<br><sub>预印本</sub></td>
<td width="64" valign="top">26/09</td>
<td width="70" valign="top"><code>A</code><br><code>D</code>&nbsp;<code>E</code></td>
<td width="180" valign="top">Qwen2.5‑Omni‑7B<br><sub>Training-free</sub></td>
<td width="85" valign="top"><a href="https://github.com/SEAR-benchmark/SEAR">代码</a></td>
</tr>
</tbody>
</table>

BAEA-Adaptive 在预算内选择声学特征类别；BAEA-Fixed 为确定性流程，论文中表现更好。[SEAR 标注](https://huggingface.co/datasets/SEAR-benchmark/SEAR)不含原始音频。ToolDF 提供代码及音频重建脚本；作者权重下载链接的文件未独立核验。

<a name="visual"></a>

## 视觉（图像与视频）

输入：<code>I</code> 图像 · <code>V</code> 视频 · <code>A</code> 音频 · <code>T</code> 文本<br>任务：<code>D</code> 检测 · <code>L</code> 定位 · <code>E</code> 解释

**[查看技术对比 →](docs/COMPARISON_CN.md#visual)**

<table>
<thead>
<tr>
<th width="400" align="left">论文<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</th>
<th width="115" align="left">发表</th>
<th width="64" align="left">日期</th>
<th width="70" align="left">标签</th>
<th width="180" align="left">模型与训练</th>
<th width="85" align="left">代码</th>
</tr>
</thead>
<tbody>
<tr>
<td width="400" valign="top"><a name="atar"></a><strong><a href="https://arxiv.org/abs/2609.39066">Agentic Tool-Augmented Reasoning for Explainable Image Forgery Detection</a></strong> (ATAR)</td>
<td width="115" valign="top">ACM&nbsp;MM&nbsp;2026<br><sub>口头报告 · 已录用</sub></td>
<td width="64" valign="top">26/09</td>
<td width="70" valign="top"><code>I</code><br><code>D</code>&nbsp;<code>L</code>&nbsp;<code>E</code></td>
<td width="180" valign="top">Qwen3‑VL‑8B<br><sub>SFT + RL</sub></td>
<td width="85" valign="top">—</td>
</tr>
<tr>
<td width="400" valign="top"><a name="forenagent"></a><strong><a href="https://arxiv.org/abs/2512.16300">Code-in-the-Loop Forensics: Agentic Tool Use for Image Forgery Detection</a></strong> (ForenAgent)</td>
<td width="115" valign="top">ECCV&nbsp;2026</td>
<td width="64" valign="top">26/09</td>
<td width="70" valign="top"><code>I</code><br><code>D</code>&nbsp;<code>E</code></td>
<td width="180" valign="top">Qwen2.5‑VL‑7B<br><sub>SFT + RL</sub></td>
<td width="85" valign="top"><a href="https://github.com/zfr00/ForenAgent">工具集</a></td>
</tr>
<tr>
<td width="400" valign="top"><a name="safeguard"></a><strong><a href="https://arxiv.org/abs/2607.03069">SafeGuard: A Multi-Agent Perception-Reasoning Framework for Social-Risk AI-Generated Video Detection</a></strong></td>
<td width="115" valign="top">ECCV&nbsp;2026</td>
<td width="64" valign="top">26/09</td>
<td width="70" valign="top"><code>V</code><br><code>D</code>&nbsp;<code>E</code></td>
<td width="180" valign="top">GPT‑4o<br>+ Gemini‑2.5‑Pro<br><sub>Training-free · 工具经调优</sub></td>
<td width="85" valign="top"><a href="https://github.com/williamw99/SafeGuard">待发布</a></td>
</tr>
<tr>
<td width="400" valign="top"><a name="fact"></a><strong><a href="https://arxiv.org/abs/2609.05876">FACT: A Forensic Agent with Compiled Tool-Use Trajectories for AI-Generated Image Detection</a></strong></td>
<td width="115" valign="top">arXiv&nbsp;2026<br><sub>预印本</sub></td>
<td width="64" valign="top">26/09</td>
<td width="70" valign="top"><code>I</code><br><code>D</code>&nbsp;<code>E</code></td>
<td width="180" valign="top">Qwen3‑VL‑8B<br><sub>SFT + RL</sub></td>
<td width="85" valign="top">—</td>
</tr>
<tr>
<td width="400" valign="top"><a name="defake-o3"></a><strong><a href="https://arxiv.org/abs/2608.16259">Defake-o3: From Speculative Rationales to Verifiable Evidence for Explainable AIGI Detection</a></strong></td>
<td width="115" valign="top">ACM&nbsp;MM&nbsp;2026<br><sub>已录用</sub></td>
<td width="64" valign="top">26/08</td>
<td width="70" valign="top"><code>I</code><br><code>D</code>&nbsp;<code>L</code>&nbsp;<code>E</code></td>
<td width="180" valign="top">Qwen3‑VL‑8B<br><sub>SFT + RL</sub></td>
<td width="85" valign="top">—</td>
</tr>
<tr>
<td width="400" valign="top"><a name="hermes"></a><strong><a href="https://proceedings.mlr.press/v306/li26be.html">Hermes: An Evidence-Driven Agentic Framework for Trustworthy and Explainable AI-Generated Video Detection</a></strong></td>
<td width="115" valign="top">ICML&nbsp;2026</td>
<td width="64" valign="top">26/07</td>
<td width="70" valign="top"><code>V</code><br><code>D</code>&nbsp;<code>E</code></td>
<td width="180" valign="top">Qwen3‑VL‑8B<br>+ ChatGPT‑5<br><sub>Training-free</sub></td>
<td width="85" valign="top">—</td>
</tr>
<tr>
<td width="400" valign="top"><a name="unishield"></a><strong><a href="https://arxiv.org/abs/2510.03161">UniShield: An Adaptive Multi-Agent Framework for Unified Forgery Image Detection and Localization</a></strong></td>
<td width="115" valign="top">CVPR&nbsp;Findings<br>2026</td>
<td width="64" valign="top">26/06</td>
<td width="70" valign="top"><code>I</code><br><code>D</code>&nbsp;<code>L</code>&nbsp;<code>E</code></td>
<td width="180" valign="top">Qwen2.5‑VL<br>+ GPT‑4o<br><sub>RL（路由器） · 工具经调优</sub></td>
<td width="85" valign="top">—</td>
</tr>
<tr>
<td width="400" valign="top"><a name="agentfox"></a><strong><a href="https://arxiv.org/abs/2603.23115">AgentFoX: LLM Agent-Guided Fusion with eXplainability for AI-Generated Image Detection</a></strong></td>
<td width="115" valign="top">arXiv&nbsp;2026<br><sub>预印本</sub></td>
<td width="64" valign="top">26/03</td>
<td width="70" valign="top"><code>I</code><br><code>D</code>&nbsp;<code>E</code></td>
<td width="180" valign="top">Qwen3‑32B<br>+ GPT‑4o<br><sub>Training-free · 需校准</sub></td>
<td width="85" valign="top"><a href="https://github.com/suncore946/AgentFoX">最小推理</a></td>
</tr>
<tr>
<td width="400" valign="top"><a name="evoguard"></a><strong><a href="https://arxiv.org/abs/2603.17343">EvoGuard: An Extensible Agentic RL-based Framework for Practical and Evolving AI-Generated Image Detection</a></strong></td>
<td width="115" valign="top">arXiv&nbsp;2026<br><sub>预印本</sub></td>
<td width="64" valign="top">26/03</td>
<td width="70" valign="top"><code>I</code><br><code>D</code></td>
<td width="180" valign="top">Qwen3‑VL‑4B<br><sub>RL</sub></td>
<td width="85" valign="top">—</td>
</tr>
<tr>
<td width="400" valign="top"><a name="forgeryvcr"></a><strong><a href="https://arxiv.org/abs/2602.14098">ForgeryVCR: Visual-Centric Reasoning via Efficient Forensic Tools in MLLMs for Image Forgery Detection and Localization</a></strong></td>
<td width="115" valign="top">ACM&nbsp;MM&nbsp;2026<br><sub>口头报告 · 已录用</sub></td>
<td width="64" valign="top">26/02</td>
<td width="70" valign="top"><code>I</code><br><code>D</code>&nbsp;<code>L</code></td>
<td width="180" valign="top">Qwen3‑VL‑4B<br><sub>SFT + RL</sub></td>
<td width="85" valign="top"><a href="https://github.com/youqiwong/ForgeryVCR">代码<br><sub>＋权重</sub></a></td>
</tr>
<tr>
<td width="400" valign="top"><a name="aifo"></a><strong><a href="https://arxiv.org/abs/2511.00181">From Evidence to Verdict: An Agent-Based Forensic Framework for AI-Generated Image Detection</a></strong> (AIFo)</td>
<td width="115" valign="top">arXiv&nbsp;2025<br><sub>预印本</sub></td>
<td width="64" valign="top">25/10</td>
<td width="70" valign="top"><code>I</code><br><code>D</code>&nbsp;<code>E</code></td>
<td width="180" valign="top">GPT‑4o<br><sub>Training-free</sub></td>
<td width="85" valign="top">—</td>
</tr>
</tbody>
</table>

### 相关固定工具与多智能体流程

以下采用预设检测器池、固定角色分工、辩论轮次或检索流程。证据仲裁和训练时自我改进不等于推理时自主选择工具。ForeAgent 与上方 ForenAgent 是不同工作。

**[查看技术对比 →](docs/COMPARISON_CN.md#related-visual)**

<table>
<thead>
<tr>
<th width="400" align="left">论文<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</th>
<th width="115" align="left">发表</th>
<th width="64" align="left">日期</th>
<th width="70" align="left">标签</th>
<th width="180" align="left">模型与训练</th>
<th width="85" align="left">代码</th>
</tr>
</thead>
<tbody>
<tr>
<td width="400" valign="top"><a name="dissecting-agentic-forensics"></a><strong><a href="https://arxiv.org/abs/2609.24359">Dissecting Agentic Forensics: The Role of Triage, Prompting, and Evidence Arbitration in Open-World Fake Image Detection</a></strong></td>
<td width="115" valign="top">ECCV&nbsp;2026<br><sub>AI4MFDD Workshop</sub></td>
<td width="64" valign="top">26/09</td>
<td width="70" valign="top"><code>I</code><br><code>D</code>&nbsp;<code>E</code></td>
<td width="180" valign="top">Gemma‑4‑26B‑A4B‑it<br>+ GPT‑5<br><sub>Training-free · 分数校准</sub></td>
<td width="85" valign="top">—</td>
</tr>
<tr>
<td width="400" valign="top"><a name="pate-forensics"></a><strong><a href="https://arxiv.org/abs/2608.18573">PATE-Forensics: Perception-as-Tool for Explainable Deepfake Forensics with General-Purpose MLLMs</a></strong></td>
<td width="115" valign="top">arXiv&nbsp;2026<br><sub>DDL-X 挑战报告</sub></td>
<td width="64" valign="top">26/08</td>
<td width="70" valign="top"><code>I</code><br><code>D</code>&nbsp;<code>L</code>&nbsp;<code>E</code></td>
<td width="180" valign="top">Qwen3.5‑Flash<br><sub>Training-free · 工具经训练</sub></td>
<td width="85" valign="top"><a href="https://github.com/yqli00000/CLASP">代码<br><sub>现名 CLASP</sub></a></td>
</tr>
<tr>
<td width="400" valign="top"><a name="argus"></a><strong><a href="https://arxiv.org/abs/2608.06865">Multi-Agent Forensic Reasoning for Generalizable Deepfake Video Detection</a></strong> (ARGUS)</td>
<td width="115" valign="top">arXiv&nbsp;2026<br><sub>预印本</sub></td>
<td width="64" valign="top">26/08</td>
<td width="70" valign="top"><code>V</code><br><code>D</code>&nbsp;<code>E</code></td>
<td width="180" valign="top">Qwen2.5‑VL‑7B<br><sub>SFT + RL · 固定 4+1 角色</sub></td>
<td width="85" valign="top"><a href="https://github.com/XavierJiezou/ARGUS">代码<br><sub>＋权重</sub></a></td>
</tr>
<tr>
<td width="400" valign="top"><a name="foreagent"></a><strong><a href="https://arxiv.org/abs/2606.26552">Perception, Verdict, and Evolution: Hindsight-Driven Self-Refining Forensics Agent for AI-Generated Image Detection</a></strong> (ForeAgent)</td>
<td width="115" valign="top">arXiv&nbsp;2026<br><sub>预印本</sub></td>
<td width="64" valign="top">26/06</td>
<td width="70" valign="top"><code>I</code><br><code>D</code>&nbsp;<code>E</code></td>
<td width="180" valign="top">Qwen3‑VL‑8B<br><sub>SFT · 训练时自改进</sub></td>
<td width="85" valign="top">—</td>
</tr>
<tr>
<td width="400" valign="top"><a name="vrag-dfd"></a><strong><a href="https://arxiv.org/abs/2604.13660">VRAG-DFD: Verifiable Retrieval-Augmentation for MLLM-based Deepfake Detection</a></strong></td>
<td width="115" valign="top">CVPR&nbsp;Findings<br>2026</td>
<td width="64" valign="top">26/06</td>
<td width="70" valign="top"><code>I</code><br><code>D</code>&nbsp;<code>E</code></td>
<td width="180" valign="top">MLLM<br><sub>具体规模未核验</sub><br><sub>SFT + RL · 固定 RAG</sub></td>
<td width="85" valign="top"><a href="https://github.com/abigcatcat/VRAG-DFD">代码<br><sub>＋权重</sub></a></td>
</tr>
<tr>
<td width="400" valign="top"><a name="dvar"></a><strong><a href="https://arxiv.org/abs/2604.16987">DVAR: Adversarial Multi-Agent Debate for Video Authenticity Detection</a></strong></td>
<td width="115" valign="top">ACM&nbsp;MM&nbsp;2026<br><sub>论文标注</sub></td>
<td width="64" valign="top">26/04<br><sub>预印本</sub></td>
<td width="70" valign="top"><code>V</code><br><code>D</code>&nbsp;<code>E</code></td>
<td width="180" valign="top">GPT‑5.4<br><sub>Training-free · 固定辩论</sub></td>
<td width="85" valign="top">—</td>
</tr>
</tbody>
</table>

Dissecting 的 Workshop 录用信息来自作者记录；表中列出其混合模型配置。DVAR 的会议归属来自论文，DOI 尚未独立核验；未找到其官方代码或知识库。ForeAgent 的[作者权重链接](https://huggingface.co/Shimin/qwen3_vl_8b_foreagent)尚未核验文件。

<a name="text"></a>

## 文本

输入：<code>I</code> 图像 · <code>V</code> 视频 · <code>A</code> 音频 · <code>T</code> 文本<br>任务：<code>D</code> 检测 · <code>L</code> 定位 · <code>E</code> 解释

**[查看技术对比 →](docs/COMPARISON_CN.md#text)**

<table>
<thead>
<tr>
<th width="400" align="left">论文<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</th>
<th width="115" align="left">发表</th>
<th width="64" align="left">日期</th>
<th width="70" align="left">标签</th>
<th width="180" align="left">模型与训练</th>
<th width="85" align="left">代码</th>
</tr>
</thead>
<tbody>
<tr>
<td width="400" valign="top"><a name="qwen-langgraph"></a><strong><a href="https://link.springer.com/article/10.1007/s10791-026-10710-z">Performance evaluation and interpretability of a Qwen LangGraph agent for AI written and AI rewritten text detection</a></strong></td>
<td width="115" valign="top">Discover<br>Computing&nbsp;2026</td>
<td width="64" valign="top">26/10</td>
<td width="70" valign="top"><code>T</code><br><code>D</code>&nbsp;<code>E</code></td>
<td width="180" valign="top">Qwen2.5‑1.5B<br><sub>未报告 · 工具经训练</sub></td>
<td width="85" valign="top"><a href="https://drive.google.com/drive/folders/14wU4r0-uRirkJ9aP3xI1lj2yHfWkj7DQ">作者链接<br><sub>内容未核验</sub></a></td>
</tr>
</tbody>
</table>

### 相关工具增强多角色流程

检测与搜索模块分别执行，搜索按精确匹配后模糊匹配的固定顺序回退，再汇总网页证据；不作为完全自主工具规划。

**[查看技术对比 →](docs/COMPARISON_CN.md#related-text)**

<table>
<thead>
<tr>
<th width="400" align="left">论文<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</th>
<th width="115" align="left">发表</th>
<th width="64" align="left">日期</th>
<th width="70" align="left">标签</th>
<th width="180" align="left">模型与训练</th>
<th width="85" align="left">代码</th>
</tr>
</thead>
<tbody>
<tr>
<td width="400" valign="top"><a name="aigt-agent"></a><strong><a href="https://aclanthology.org/2026.findings-emnlp.272/">Beyond Text-Intrinsic Features: An Agentic Framework for Evidence-Based AI-Generated Text Detection</a></strong> (AIGT-Agent)</td>
<td width="115" valign="top">Findings&nbsp;EMNLP<br>2026</td>
<td width="64" valign="top">26/10</td>
<td width="70" valign="top"><code>T</code><br><code>D</code>&nbsp;<code>E</code></td>
<td width="180" valign="top">GPT‑5‑mini<br><sub>Training-free · 提示词适配</sub></td>
<td width="85" valign="top"><a href="https://github.com/TrustAIRLab/AIGT-Agent">代码<br><sub>＋基准</sub></a></td>
</tr>
</tbody>
</table>

<a name="cross-modal"></a>

## 跨模态

输入：<code>I</code> 图像 · <code>V</code> 视频 · <code>A</code> 音频 · <code>T</code> 文本<br>任务：<code>D</code> 检测 · <code>L</code> 定位 · <code>E</code> 解释

**[查看技术对比 →](docs/COMPARISON_CN.md#cross-modal)**

<table>
<thead>
<tr>
<th width="400" align="left">论文<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</th>
<th width="115" align="left">发表</th>
<th width="64" align="left">日期</th>
<th width="70" align="left">标签</th>
<th width="180" align="left">模型与训练</th>
<th width="85" align="left">代码</th>
</tr>
</thead>
<tbody>
<tr>
<td width="400" valign="top"><a name="mm-veriagent"></a><strong><a href="https://arxiv.org/abs/2609.30698">MM-VeriAgent: Learning to Use Extensive Tools to Verify Multimodal Misinformation with Reinforcement Learning</a></strong></td>
<td width="115" valign="top">arXiv&nbsp;2026<br><sub>预印本</sub></td>
<td width="64" valign="top">26/09<br><sub>v2 26/11</sub></td>
<td width="70" valign="top"><code>T+I</code><br><code>D</code></td>
<td width="180" valign="top">Qwen2.5‑VL‑7B<br><sub>SFT + RL</sub></td>
<td width="85" valign="top">—</td>
</tr>
<tr>
<td width="400" valign="top"><a name="omnivl-guard-pro"></a><strong><a href="https://arxiv.org/abs/2605.16962">OmniVL-Guard Pro: A Tool-Augmented Agent for Omnibus Vision-Language Forensics</a></strong></td>
<td width="115" valign="top">arXiv&nbsp;2026<br><sub>预印本</sub></td>
<td width="64" valign="top">26/05</td>
<td width="70" valign="top"><code>T+I</code>&nbsp;/&nbsp;<code>T+V</code><br><code>D</code>&nbsp;<code>L</code></td>
<td width="180" valign="top">Qwen3‑VL‑8B<br><sub>SFT + RL</sub></td>
<td width="85" valign="top"><a href="https://github.com/shen8424/OmniVL-Guard-Pro">待发布</a></td>
</tr>
<tr>
<td width="400" valign="top"><a name="fakehunter"></a><strong><a href="https://arxiv.org/abs/2508.14581">Memory-Anchored Multimodal Reasoning for Explainable Video Forensics</a></strong> (FakeHunter)</td>
<td width="115" valign="top">arXiv&nbsp;2025<br><sub>预印本</sub></td>
<td width="64" valign="top">25/08</td>
<td width="70" valign="top"><code>A+V</code><br><code>D</code>&nbsp;<code>E</code></td>
<td width="180" valign="top">Qwen2.5‑Omni‑7B<br><sub>备选 MiniCPM‑o‑2_6</sub><br><sub>Training-free · 需构建记忆</sub></td>
<td width="85" valign="top">—</td>
</tr>
<tr>
<td width="400" valign="top"><a name="t2agent"></a><strong><a href="https://arxiv.org/abs/2505.19768">T²Agent: A Tool-augmented Multimodal Misinformation Detection Agent with Monte Carlo Tree Search</a></strong></td>
<td width="115" valign="top">AAAI&nbsp;2026<br><sub>Oral</sub></td>
<td width="64" valign="top">25/05<br><sub>预印本</sub></td>
<td width="70" valign="top"><code>T+I</code><br><code>D</code></td>
<td width="180" valign="top">GPT‑4o<br><sub>Training-free</sub></td>
<td width="85" valign="top"><a href="https://github.com/cuixing100876/T2Agent">代码<br><sub>部分缓存</sub></a></td>
</tr>
</tbody>
</table>

MM-VeriAgent 与 T²Agent 面向包含生成／篡改图像的广义图文虚假信息，不限于 AIGC 来源检测。T²Agent 的公开实现部分读取预计算工具结果，示例后端也与论文主实验不同；未验证全流程复现。

### 相关规则编排方法

以下通过固定阈值或确定性状态机升级检测，不使用 LLM 自主行动策略。ENF 的存在本身不能证明真实，仍需与可信独立电网参考等证据核对。

**[查看技术对比 →](docs/COMPARISON_CN.md#related-cross-modal)**

<table>
<thead>
<tr>
<th width="400" align="left">论文<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</th>
<th width="115" align="left">发表</th>
<th width="64" align="left">日期</th>
<th width="70" align="left">标签</th>
<th width="180" align="left">模型与训练</th>
<th width="85" align="left">代码</th>
</tr>
</thead>
<tbody>
<tr>
<td width="400" valign="top"><a name="adaptive-multi-agent"></a><strong><a href="https://doi.org/10.3390/informatics13100163">A Multi-Agent Framework with Adaptive Orchestration for Explainable Multi-Modal Deepfake Detection</a></strong></td>
<td width="115" valign="top">Informatics&nbsp;2026</td>
<td width="64" valign="top">26/10</td>
<td width="70" valign="top"><code>A+V</code><br><code>D</code>&nbsp;<code>E</code></td>
<td width="180" valign="top">Llama‑3‑70B<br>+ Gemini‑1.5‑Flash<br><sub>规则编排 · 检测器经训练</sub></td>
<td width="85" valign="top"><a href="https://github.com/saoirsebarry/multiagent-deepfake-detection">代码<br><sub>＋权重</sub></a></td>
</tr>
<tr>
<td width="400" valign="top"><a name="enf-framework"></a><strong><a href="https://arxiv.org/abs/2610.22440">An Agentic ENF Framework for Forensic Video Authentication Against Generative AI</a></strong></td>
<td width="115" valign="top">arXiv&nbsp;2026<br><sub>预印本</sub></td>
<td width="64" valign="top">26/10</td>
<td width="70" valign="top"><code>A+V</code><br><code>D</code></td>
<td width="180" valign="top">确定性状态机<br><sub>规则编排 · 检测器经训练</sub></td>
<td width="85" valign="top"><a href="https://github.com/RyanSolent95/enf-video-forensics">代码<br><sub>＋权重</sub></a></td>
</tr>
</tbody>
</table>

### 待进一步核验

- [FALCON: LLM as a forensic reasoner: Expert-guided video deepfake detection across modalities](https://doi.org/10.1016/j.patcog.2026.115240) · Pattern Recognition，2026‑10‑29 在线发表。摘要描述专家提取跨模态证据并交由 LLM 推理；全文访问受限，具体模型、训练、代码及自主性未核验，暂不加入技术对比。

<a name="surveys"></a>

## 相关综述

[智能体综述](#agent-surveys) · [检测综述](#detection-surveys)

<a name="agent-surveys"></a>

### 智能体综述

| 综述 | 发表位置 / 状态 | 主要内容 |
| --- | --- | --- |
| **[Large language model agent evaluation and benchmarking: a systematic survey, meta-taxonomy, and critical research roadmap](https://doi.org/10.1007/s10462-026-11678-4)** | Artificial Intelligence Review，2026 | 以有效性为核心的智能体评测；能力、评分方式与环境三维分类，以及数据污染、非确定性、可复现性和执行成本。 |
| **[A Survey on the Optimization of Large Language Model-based Agents](https://doi.org/10.1145/3789261)** | ACM Computing Surveys，2026 | 智能体的监督微调、强化学习与混合优化；轨迹数据构建、奖励设计、提示词优化及知识检索。 |
| **[A Survey on Agentic Multimodal Large Language Models](https://arxiv.org/abs/2510.10991)** | arXiv 2025 · 预印本 | 多模态推理、反思与记忆；工具调用和环境交互；训练框架与评测数据集。 |
| **[Evaluation and Benchmarking of LLM Agents: A Survey](https://doi.org/10.1145/3711896.3736570)** | KDD 2025 | 评测目标（行为、能力、可靠性与安全）、交互方式、基准、指标与工具，以及长程交互的部署挑战。 |
| **[Large Language Model Based Multi-agents: A Survey of Progress and Challenges](https://www.ijcai.org/proceedings/2024/890)** | IJCAI 2024 · Survey Track | 多智能体的环境接口、角色设定、通信协作与能力获取，以及协同问题求解和仿真的数据集与基准。 |
| **[A survey on large language model based autonomous agents](https://doi.org/10.1007/s11704-024-40231-1)** | Frontiers of Computer Science，2024 | 以角色设定、记忆、规划和行动构建统一架构，覆盖工具使用、能力获取、应用及评测。 |

<a name="detection-surveys"></a>

### 检测综述

| 综述 | 发表位置 / 状态 | 主要内容 |
| --- | --- | --- |
| **[AI-Generated Content Detection: A Cross-Modal Survey of Methods, Challenges, and Future Directions](https://www.researchsquare.com/article/rs-10864156/v1)** | Research Square 2026 · 预印本 | 跨模态 AI 生成内容检测的方法、挑战与未来方向。 |
| **[Detecting AI-Generated Video: A Vision–Language Dual-View Survey](https://aclanthology.org/2026.findings-acl.1613/)** | Findings of ACL 2026 | 四层视频检测分类：内在线索、时空一致性、跨模态一致性和语言引导的世界知识推理，包含工具增强的智能体流程。 |
| **[Explainable deepfake detection across different modalities: An overview of methods and challenges](https://doi.org/10.1016/j.imavis.2025.105738)** | Image and Vision Computing，2025 | 图像、视频、音频与文本的可解释伪造检测；显著性方法、局部代理模型与归因，以及数据集和评测。 |
| **[Survey on AI-Generated Media Detection: From Non-MLLM to MLLM](https://arxiv.org/abs/2502.05240)** | arXiv 2025‑02 · 预印本 | 跨模态比较专用检测器与 MLLM 检测器，围绕真实性分类、解释及伪造定位三类任务展开。 |
| **[Detecting Multimedia Generated by Large AI Models: A Survey](https://arxiv.org/abs/2402.00045)** | arXiv 2024 · 预印本；2025‑07 修订 | 覆盖文本、图像、视频、音频及多模态检测，区分检测性能与泛化性、鲁棒性、可解释性，并整理数据集和指标。 |

<a name="resources"></a>

## 资源

面向 Agentic 媒体取证研究的平台、模型基座与开发工具。使用前请确认访问条件、模型版本和数据处理条款。

下方区分当前可选模型与论文复现基座；列为资源不代表已经验证其取证性能。本轮新增／更新条目核查于 2026‑11‑08；其余条目沿用 2026‑10‑23 核查。公开文件可见不代表已下载全量数据或完成复现。

### Agentic 取证平台

- [Resemble Investigator](https://docs.resemble.ai/detect/agents) · **托管 API。** 执行媒体真实性调查，以流式形式返回证据与评估；需要已开通 Investigator 权限的账户。
- [Clyravision](https://en.merantix-momentum.com/clyravision) · **需联系开通的平台。** 基于 Agent 工作流，结合取证痕迹、元数据与来源／语境核查分析图像；产品页提供演示录像。

### 可接入 Agent 的检测服务

- [Reality Defender RealAPI](https://www.realitydefender.com/product/realapi) · **检测 API。** 分析图像、音频与视频中的操纵痕迹，返回可接入 Agent 证据流程的结构化结果。
- [Sightengine](https://www.sightengine.com/docs/ai-generated-image-detection) · **检测 API。** 提供 AI 生成图像评分，相关文档另含深度伪造与 AI 生成视频检测模型。

### 专用取证模型

- [VeriSpoof](https://arxiv.org/abs/2611.04634)（2026‑11‑03）· 基于 Qwen3-ASR-1.7B 编码器和 MiniCPM5-2B，覆盖音频检测、归因、录音条件、片段定位及来源验证，输出可核查解释。已提供[推理代码](https://github.com/swagshaw/verispoof)与 [Plus 权重](https://huggingface.co/AustinXiao/VeriSpoof-Plus)，训练代码待发布；代码／权重为 CC BY-NC 4.0。它是专用模型，没有自主选工具闭环。
- [Venus-DefakerOne2](https://arxiv.org/abs/2610.37918)（2026‑10‑27；11‑02 修订）· Qwen3.5-2B 图像／视频鉴伪专家，采用固定真假问答。已提供[权重](https://huggingface.co/qcf568/DefakerOne2)及[推理辅助脚本](https://github.com/inclusionAI/DefakerOne2)，不代表完整训练代码开放；复现论文使用 preview，release 使用更多训练数据。权重和数据许可细节仍需确认。

### 数据集与基准

- [SEAR](https://huggingface.co/datasets/SEAR-benchmark/SEAR) · 音频问答标注，覆盖真假判断、线索、数值测量与取证解释；配套 [BAEA 与评测代码](https://github.com/SEAR-benchmark/SEAR)，需另行获取 ASVspoof 原始音频。
- [VeriSpoof-Bench](https://huggingface.co/datasets/AustinXiao/VeriSpoof-Bench) · 提供标签、清单、元数据与重建材料；54 个子集、177,852 项，不含全部原始音频，需遵守各源语料许可。
- [RRVBench](https://www.modelscope.cn/models/DanceText/RRVBench) · DefakerOne2 配套视频基准，含 1,319 条真实视频、11 个生成器的 11,000 条合成视频；作者标注非商业研究使用，完整下载权限及许可条款未独立核验。
- [DeepfakeGenome](https://arxiv.org/abs/2611.06046)（2026‑11‑04）· 约 200 万图像、100 种人脸伪造算法，包含检索式归因评测。[数据](https://huggingface.co/datasets/DeepfakeGenome/DeepfakeGenome)和[训练／测试代码](https://huggingface.co/DeepfakeGenome/DeepfakeGenome_Codebase)已发布，部分原始数据须另从 FF++／DF40 等来源取得，使用限制依各来源而定。
- [WildFakeToolBench](https://github.com/TrustAIRLab/WildFakeToolBench)（[论文](https://arxiv.org/abs/2610.31152) 10‑22；代码 10‑28 发布）· 156 种图像后处理工具，用于真实传播条件下的检测鲁棒性评测。不是检测 Agent；不含全量测试图像、检测器权重或完整中间采集结果。作者限定学术用途。
- [WildAIGC-Bench V3](https://github.com/YuZijian/WildAIGC-Bench)（2026‑11‑03 更新）· 600 张 AI 图像、638 张真实照片，保留来源和证据。**待复核挑战集，勿直接作为严格金标准：**[实际样本](https://huggingface.co/datasets/yuzj1997yzj/WildAIGC-Bench)中部分 AI 标签仍含“真值待人工复核”等证据提示，例如 img_00e970e187abfbf5、img_024f0544ed6ff0f5、img_02760ab536eb47cc；使用前应逐条复核。

### 面向新实验的当前多模态基座

以下 Qwen 变体无需单独的 “-VL” 后缀即可支持视觉输入，但不同权重版本的输入模态与许可仍有差异，不能默认所有后续 Qwen 版本均为多模态。

- [Qwen3.5](https://github.com/QwenLM/Qwen3.8#qwen35)，尤其是 [Qwen3.5-9B](https://huggingface.co/Qwen/Qwen3.5-9B) · 原生支持图像/视频理解；9B 可作为本地工具调用型智能体的紧凑开放权重候选。
- [Qwen3.6-35B-A3B](https://huggingface.co/Qwen/Qwen3.6-35B-A3B) · 支持图像/视频的开放权重 MoE，总参数 35B、激活参数 3B，支持保留推理上下文，适合迭代式智能体流程。
- [Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B) · 更新一代的开放权重原生 VLM，支持图像/视频理解与多步智能体任务；采用 Apache-2.0 许可。
- [Qwen3.8-Flash-Next](https://github.com/QwenLM/Qwen3.8-Flash-Next)（[权重](https://huggingface.co/Qwen/Qwen3.8-Flash-Next)）· 支持图像/视频的开放权重多模态 MoE 架构预览；采用 Qwen Community 1.0 许可，并非 Apache-2.0。

### System-1 快速决策与感知模型

这里的 System-1 包含直接结构化决策与候选排序，并非单一架构，也不局限于 Jev 生态。以下是通用感知／决策资源，不是已验证的取证检测器；评分需要任务级校准，并行问题也不代表延迟严格不变。

- [Liquid d1](https://www.liquid.ai/blog/lfm3) · 2026‑10‑27 新增开放权重 [d1-2B](https://huggingface.co/LiquidAI/d1-2B)（文本／图像／视频）和 [d1-Omni-2B](https://huggingface.co/LiquidAI/d1-Omni-2B)（增加音频），均已看到权重及推理文件；长语音和部分语言仍有局限。[d1-ultra](https://www.liquid.ai/blog/d1-ultra) 提供文本／图像决策 API，早期 [d1-3B](https://huggingface.co/LiquidAI/d1-3B) 与实验性 [d1-omni-600M](https://huggingface.co/LiquidAI/d1-omni-600M) 仍可作对照。开放权重采用含商用营收限制的 LFM Open License v1.0；不是专用鉴伪模型。
- [Cloudflare Clef](https://blog.cloudflare.com/clef-faster-cheaper-multimodal/) · [Clef](https://huggingface.co/Cloudflare/clef)／[Clef-flash](https://huggingface.co/Cloudflare/clef-flash) 面向文本、图像、视频做结构化决策，[Clef-omni](https://huggingface.co/Cloudflare/clef-omni) 增加音频；提供 Apache-2.0 权重和托管 Workers AI 服务，多模态版本更新于 2026‑10‑09。
- [pplx-decider-v1.2](https://huggingface.co/perplexity-ai/pplx-decider-v1.2) · Perplexity 基于 Qwen3.8-27B 的文本／图像决策模型，并行读取多个问题标记；问题之间可互相注意，并非独立推理。已列出 Apache-2.0 权重与推理代码，但模型卡仍保留私有访问说明，实际下载权限未核验。
- [MetaEncoder-30B](https://huggingface.co/facebook/meta-encoder) · 将文本／图像／视频任务和候选编码为可缓存嵌入，直接进行候选排序；提供[评测代码](https://github.com/facebook/meta-encoder-eval)。权重已发布，但需要受限访问申请并接受模型条款。视频需用原生实现，vLLM 适配仅支持文本／图像；相似度不自动等于校准概率。
- [Intern-Decision](https://github.com/InternLM/Intern-Decision) · 文本加可选图像，单次前向输出多个类型化 JSON 决策；提供 [4B 权重](https://huggingface.co/internlm/Intern-Decision-4B)及 0.8B/2B 版本。Apache-2.0 代码与权重已发布，但训练数据及私有校准记录未完整公开。
- [Valen（万澜）](https://github.com/Valen-Team/Valen) · 共享状态的文本／图像／采样视频决策；提供 0.8B/2B/[4B 权重](https://huggingface.co/Valen-Team/Valen-4B)、Apache-2.0 许可及本地 ONNX/GGUF 选项。本地视频采样 16 帧，免费网页仅取中间一帧、免费 API 仅支持单问题，演示能力不等同于本地模型。
- [TypeSafe Jev](https://docs.typesafe.ai/models) · 托管式结构化决策 API：截至 2026‑11‑08，jev-latest 与 jev-preview 均指向 1.14.0，没有独立预览版本。[图像输入](https://docs.typesafe.ai/images)与 [Box 定位](https://docs.typesafe.ai/primitives/box)仍为实验功能；不列为开放权重或已验证的鉴伪模型。

### 所收录论文使用的基座

- [Qwen3-VL](https://github.com/QwenLM/Qwen3-VL) · 支持图像／视频推理与定位的视觉语言模型系列，包含多篇收录方法使用的 4B、8B 版本。
- [Qwen2.5-VL-7B-Instruct](https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct) · 图像／视频理解基座，用于 ForenAgent、ARGUS 和 MM-VeriAgent；UniShield 使用 Qwen2.5-VL 系列，但未注明参数规模。
- [Qwen3-32B](https://huggingface.co/Qwen/Qwen3-32B) · 文本推理模型，用于 AgentFoX 的 Agent 引导证据融合。
- [Qwen2.5-Omni-7B](https://huggingface.co/Qwen/Qwen2.5-Omni-7B) · 支持文本、图像、音频与视频理解的全模态基座，用于 FakeHunter 和 BAEA。
- [Qwen2.5-Omni-3B](https://huggingface.co/Qwen/Qwen2.5-Omni-3B) · ToolDF 的音频工具调用基座，使用 LoRA SFT 适配。
- [MiniCPM-o 2.6](https://huggingface.co/openbmb/MiniCPM-o-2_6) · 支持视觉、音频与语言的全模态模型，是 FakeHunter 评估的替代基座。

### 闭源模型服务

- [OpenAI API 模型](https://developers.openai.com/api/docs/models) · GPT 系列服务的官方模型目录，多篇收录方法使用该系列；复现时需核对论文中的具体模型或快照。
- [Google Gemini API](https://ai.google.dev/gemini-api/docs/models) · 官方多模态模型目录与 API 文档，涵盖 SafeGuard 使用的 Gemini 系列。
- [Qwen3.8-Omni-Flash](https://qwen.ai/blog?id=qwen3.8-omni-flash) · 托管式原生全模态模型，接收文本、图像、音频与视频，支持工具调用和长上下文视听推理；不列为开放权重。

### Agent 框架与工具执行

- [LangGraph](https://docs.langchain.com/oss/python/langgraph/overview) · 支持状态持久化与人工审核的工作流编排框架，可组织多步骤证据收集与仲裁。
- [Pydantic AI](https://pydantic.dev/docs/ai/overview/) · 提供类型化工具、结构化输出与依赖注入的 Python Agent 框架，适合定义清晰的检测器接口。
- [Codex SDK](https://learn.chatgpt.com/docs/codex-sdk) · 以编程方式管理代码 Agent 会话，可用于基于代码的实验与研究流程集成。
- [OpenHands Software Agent SDK](https://docs.openhands.dev/sdk) · 支持 Shell、文件、浏览器与 MCP 工具的自定义 Agent SDK，提供本地与远程执行方式。
- [Pi](https://pi.dev/docs/latest/sdk) · 可嵌入应用的代码 Agent SDK，支持会话配置与工具扩展，用于构建自定义执行流程。
- [reflex](https://github.com/kshetrajna12/reflex) · 结构化视觉判断的推理框架，默认使用冻结的 Qwen3.5-4B，共享前缀缓存并隔离批处理多个问题；当前稳定版不提供早期尝试的微调模型。
