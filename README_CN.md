![Agentic AIGC Detection：分层风景图像、扫描检查区域，以及通过证据连线连接的放大细节。](assets/banner.svg)

[English](README.md) · **简体中文**

[简介](#intro) · [动态](#news) · [音频](#audio) · [视觉（图像与视频）](#visual) · [文本](#text) · [跨模态](#cross-modal) · **[技术对比 →](docs/COMPARISON_CN.md)** · [相关综述](#surveys) · [资源](#resources) · [链接检查](#link-checks)

<a name="intro"></a>

## 简介 · Intro

本仓库整理面向 AI 生成内容与相关媒体篡改检测的智能体研究，关注工具调用、证据驱动推理与多智能体协作等方法。论文按输入模态分类，提供发表信息和官方实现的开放情况。目录仅按音频、视觉、文本、跨模态四种输入模态组织；各方法的工具使用与协作流程在表内说明。

模型仅列鉴伪推理所用模型，目录名称省略 -Instruct 后缀；完整变体、工具训练、校准与检索记忆见[推理配置](docs/COMPARISON_CN.md#inference-setups)。

训练方式针对鉴伪智能体的任务适配：Training-free（免训练）、SFT（监督微调）或 RL（强化学习）。工具训练、校准与记忆构建分别说明。

各表按日期栏的主日期倒序排列，修订日期另注。流程说明描述各论文的具体实现；代码、权重与数据链接采用并列格式。

<a name="news"></a>

## 动态 · News

- **2026‑11‑08**：补齐音频与跨模态工具推理，新增 FACT；统一按模态编排，将工具使用与协作流程纳入表格，补充专用取证模型及评测资源，更新 d1／Jev。同步中英文技术对比，加入自动链接审计。
- **2026‑10‑23**：新增 Qwen–LangGraph 文本检测；补充两项工具增强／规则编排相关工作，同步技术对比，补充智能体评测综述，更新 Qwen／System-1 模型资源。
- **2026‑10‑04**：上线[技术对比](docs/COMPARISON_CN.md)，从五个维度并列比较收录方法。
- **2026‑10‑04**：仓库上线，整理 Agentic AIGC 检测相关论文。

<a name="audio"></a>

## 音频

输入：<code>I</code> 图像 · <code>V</code> 视频 · <code>A</code> 音频 · <code>T</code> 文本<br>任务：<code>D</code> 检测 · <code>L</code> 定位 · <code>E</code> 解释

**[查看技术对比 →](docs/COMPARISON_CN.md#audio)**

<table>
<thead>
<tr>
<th width="50%" align="left">论文与流程</th>
<th width="12%" align="left">发表 / 日期</th>
<th width="24%" align="left">标签 · 模型 · 训练</th>
<th width="14%" align="left">资源</th>
</tr>
</thead>
<tbody>
<tr>
<td width="50%" valign="top"><a name="tooldf"></a><strong><a href="https://aclanthology.org/2026.findings-emnlp.842/">ToolDF: Tool-Integrated Reasoning for Mixed-Authenticity Audio Deepfake Detection</a></strong><br><sub>选择音源分离／专用检测工具，再聚合判定。</sub></td>
<td width="12%" valign="top">Findings EMNLP<br>2026<br>26/10</td>
<td width="24%" valign="top"><code>A</code> · <code>D</code>&nbsp;<code>L</code>&nbsp;<code>E</code><br>Qwen2.5‑Omni‑3B<br><sub>LoRA SFT</sub></td>
<td width="14%" valign="top"><a href="https://github.com/rlataewoo/tooldf">代码</a><br><sub>含音频重建脚本</sub></td>
</tr>
<tr>
<td width="50%" valign="top"><a name="sear"></a><strong><a href="https://arxiv.org/abs/2609.39847">SEAR: Spoofing Evidence-Grounded Audio Reasoning Benchmark for Audio Language Models</a></strong> (BAEA)<br><sub>BAEA-Adaptive 在预算内选择声学特征组；确定性 BAEA-Fixed 在论文中表现更好。</sub></td>
<td width="12%" valign="top">arXiv 2026<br><sub>预印本</sub><br>26/09</td>
<td width="24%" valign="top"><code>A</code> · <code>D</code>&nbsp;<code>E</code><br>Qwen2.5‑Omni‑7B<br><sub>Training-free</sub></td>
<td width="14%" valign="top"><a href="https://github.com/SEAR-benchmark/SEAR">代码</a><br><a href="https://huggingface.co/datasets/SEAR-benchmark/SEAR">标注</a><br><sub>原始音频另行获取</sub></td>
</tr>
</tbody>
</table>

<a name="visual"></a>
<a name="相关固定工具与多智能体流程"></a>

## 视觉（图像与视频）

输入：<code>I</code> 图像 · <code>V</code> 视频 · <code>A</code> 音频 · <code>T</code> 文本<br>任务：<code>D</code> 检测 · <code>L</code> 定位 · <code>E</code> 解释

**[查看技术对比 →](docs/COMPARISON_CN.md#visual)**

<table>
<thead>
<tr>
<th width="50%" align="left">论文与流程</th>
<th width="12%" align="left">发表 / 日期</th>
<th width="24%" align="left">标签 · 模型 · 训练</th>
<th width="14%" align="left">资源</th>
</tr>
</thead>
<tbody>
<tr>
<td width="50%" valign="top"><a name="atar"></a><strong><a href="https://arxiv.org/abs/2609.39066">Agentic Tool-Augmented Reasoning for Explainable Image Forgery Detection</a></strong> (ATAR)<br><sub>选择下一次裁剪／取证工具或停止；Grounded-SAM 生成掩码。</sub></td>
<td width="12%" valign="top">ACM MM 2026<br><sub>口头报告 · 已录用</sub><br>26/09</td>
<td width="24%" valign="top"><code>I</code> · <code>D</code>&nbsp;<code>L</code>&nbsp;<code>E</code><br>Qwen3‑VL‑8B<br><sub>SFT + RL</sub></td>
<td width="14%" valign="top"></td>
</tr>
<tr>
<td width="50%" valign="top"><a name="forenagent"></a><strong><a href="https://arxiv.org/abs/2512.16300">Code-in-the-Loop Forensics: Agentic Tool Use for Image Forgery Detection</a></strong> (ForenAgent)<br><sub>生成处理代码并调用 12 个取证工具，依据反馈调整操作。</sub></td>
<td width="12%" valign="top">ECCV 2026<br>26/09</td>
<td width="24%" valign="top"><code>I</code> · <code>D</code>&nbsp;<code>E</code><br>Qwen2.5‑VL‑7B<br><sub>SFT + RL</sub></td>
<td width="14%" valign="top"><a href="https://github.com/zfr00/ForenAgent">工具集</a></td>
</tr>
<tr>
<td width="50%" valign="top"><a name="safeguard"></a><strong><a href="https://arxiv.org/abs/2607.03069">SafeGuard: A Multi-Agent Perception-Reasoning Framework for Social-Risk AI-Generated Video Detection</a></strong><br><sub>感知求解器与验证器修订假设并重新采证（≤3 轮）。</sub></td>
<td width="12%" valign="top">ECCV 2026<br>26/09</td>
<td width="24%" valign="top"><code>V</code> · <code>D</code>&nbsp;<code>E</code><br>GPT‑4o<br>+ Gemini‑2.5‑Pro<br><sub>Training-free · 工具经调优</sub></td>
<td width="14%" valign="top"><a href="https://github.com/williamw99/SafeGuard">项目</a></td>
</tr>
<tr>
<td width="50%" valign="top"><a name="fact"></a><strong><a href="https://arxiv.org/abs/2609.05876">FACT: A Forensic Agent with Compiled Tool-Use Trajectories for AI-Generated Image Detection</a></strong><br><sub>选择五个专家／八种探针或停止；GPT-5.1 仅作训练教师。</sub></td>
<td width="12%" valign="top">arXiv 2026<br><sub>预印本</sub><br>26/09</td>
<td width="24%" valign="top"><code>I</code> · <code>D</code>&nbsp;<code>E</code><br>Qwen3‑VL‑8B<br><sub>SFT + RL</sub></td>
<td width="14%" valign="top"></td>
</tr>
<tr>
<td width="50%" valign="top"><a name="dissecting-agentic-forensics"></a><strong><a href="https://arxiv.org/abs/2609.24359">Dissecting Agentic Forensics: The Role of Triage, Prompting, and Evidence Arbitration in Open-World Fake Image Detection</a></strong><br><sub>七个预设检测器 → 审核者 → 裁判；所列模型为混合配置。</sub></td>
<td width="12%" valign="top">ECCV 2026<br><sub>AI4MFDD Workshop</sub><br>26/09</td>
<td width="24%" valign="top"><code>I</code> · <code>D</code>&nbsp;<code>E</code><br>Gemma‑4‑26B‑A4B‑it<br>+ GPT‑5<br><sub>Training-free · 分数校准</sub></td>
<td width="14%" valign="top"></td>
</tr>
<tr>
<td width="50%" valign="top"><a name="defake-o3"></a><strong><a href="https://arxiv.org/abs/2608.16259">Defake-o3: From Speculative Rationales to Verifiable Evidence for Explainable AIGI Detection</a></strong><br><sub>继续检查裁剪区域或给出判定；证据验证器仅用于训练。</sub></td>
<td width="12%" valign="top">ACM MM 2026<br><sub>已录用</sub><br>26/08</td>
<td width="24%" valign="top"><code>I</code> · <code>D</code>&nbsp;<code>L</code>&nbsp;<code>E</code><br>Qwen3‑VL‑8B<br><sub>SFT + RL</sub></td>
<td width="14%" valign="top"></td>
</tr>
<tr>
<td width="50%" valign="top"><a name="pate-forensics"></a><strong><a href="https://arxiv.org/abs/2608.18573">PATE-Forensics: Perception-as-Tool for Explainable Deepfake Forensics with General-Purpose MLLMs</a></strong><br><sub>固定感知 → 解释流程。</sub></td>
<td width="12%" valign="top">arXiv 2026<br><sub>DDL-X 挑战报告</sub><br>26/08</td>
<td width="24%" valign="top"><code>I</code> · <code>D</code>&nbsp;<code>L</code>&nbsp;<code>E</code><br>Qwen3.5‑Flash<br><sub>Training-free · 工具经训练</sub></td>
<td width="14%" valign="top"><a href="https://github.com/yqli00000/CLASP">代码<br><sub>现名 CLASP</sub></a></td>
</tr>
<tr>
<td width="50%" valign="top"><a name="argus"></a><strong><a href="https://arxiv.org/abs/2608.06865">Multi-Agent Forensic Reasoning for Generalizable Deepfake Video Detection</a></strong> (ARGUS)<br><sub>固定四观察者（纹理／光照／运动／物理）→ 裁判。</sub></td>
<td width="12%" valign="top">arXiv 2026<br><sub>预印本</sub><br>26/08</td>
<td width="24%" valign="top"><code>V</code> · <code>D</code>&nbsp;<code>E</code><br>Qwen2.5‑VL‑7B<br><sub>SFT + RL</sub></td>
<td width="14%" valign="top"><a href="https://github.com/XavierJiezou/ARGUS">代码</a><br><a href="https://huggingface.co/XavierJiezou/argus-models">权重</a></td>
</tr>
<tr>
<td width="50%" valign="top"><a name="hermes"></a><strong><a href="https://proceedings.mlr.press/v306/li26be.html">Hermes: An Evidence-Driven Agentic Framework for Trustworthy and Explainable AI-Generated Video Detection</a></strong><br><sub>规划、推理与讨论角色更新时序证据图（≤3 轮）。</sub></td>
<td width="12%" valign="top">ICML 2026<br>26/07</td>
<td width="24%" valign="top"><code>V</code> · <code>D</code>&nbsp;<code>E</code><br>Qwen3‑VL‑8B<br>+ ChatGPT‑5<br><sub>Training-free</sub></td>
<td width="14%" valign="top"></td>
</tr>
<tr>
<td width="50%" valign="top"><a name="unishield"></a><strong><a href="https://arxiv.org/abs/2510.03161">UniShield: An Adaptive Multi-Agent Framework for Unified Forgery Image Detection and Localization</a></strong><br><sub>每张图像路由至一个检测器，再生成报告。</sub></td>
<td width="12%" valign="top">CVPR Findings<br>2026<br>26/06</td>
<td width="24%" valign="top"><code>I</code> · <code>D</code>&nbsp;<code>L</code>&nbsp;<code>E</code><br>Qwen2.5‑VL<br>+ GPT‑4o<br><sub>RL（路由器） · 工具经调优</sub></td>
<td width="14%" valign="top"></td>
</tr>
<tr>
<td width="50%" valign="top"><a name="foreagent"></a><strong><a href="https://arxiv.org/abs/2606.26552">Perception, Verdict, and Evolution: Hindsight-Driven Self-Refining Forensics Agent for AI-Generated Image Detection</a></strong> (ForeAgent)<br><sub>推理采用感知 → 判定流程；自我改进发生于训练期。</sub></td>
<td width="12%" valign="top">arXiv 2026<br><sub>预印本</sub><br>26/06</td>
<td width="24%" valign="top"><code>I</code> · <code>D</code>&nbsp;<code>E</code><br>Qwen3‑VL‑8B<br><sub>SFT · 训练时自改进</sub></td>
<td width="14%" valign="top"><a href="https://huggingface.co/Shimin/qwen3_vl_8b_foreagent">权重</a></td>
</tr>
<tr>
<td width="50%" valign="top"><a name="vrag-dfd"></a><strong><a href="https://arxiv.org/abs/2604.13660">VRAG-DFD: Verifiable Retrieval-Augmentation for MLLM-based Deepfake Detection</a></strong><br><sub>先检索，再交叉核验证据。</sub></td>
<td width="12%" valign="top">CVPR Findings<br>2026<br>26/06</td>
<td width="24%" valign="top"><code>I</code> · <code>D</code>&nbsp;<code>E</code><br>MLLM<br><sub>SFT + RL</sub></td>
<td width="14%" valign="top"><a href="https://github.com/abigcatcat/VRAG-DFD">代码</a><br><a href="https://huggingface.co/abigcatcat/VRAG-DFD">权重</a></td>
</tr>
<tr>
<td width="50%" valign="top"><a name="dvar"></a><strong><a href="https://arxiv.org/abs/2604.16987">DVAR: Adversarial Multi-Agent Debate for Video Authenticity Detection</a></strong><br><sub>GenVideoKB 检索 + 固定两轮辩论与裁决；评测知识库冻结。</sub></td>
<td width="12%" valign="top">ACM MM 2026<br>26/04<br><sub>预印本</sub></td>
<td width="24%" valign="top"><code>V</code> · <code>D</code>&nbsp;<code>E</code><br>GPT‑5.4<br><sub>Training-free</sub></td>
<td width="14%" valign="top"></td>
</tr>
<tr>
<td width="50%" valign="top"><a name="agentfox"></a><strong><a href="https://arxiv.org/abs/2603.23115">AgentFoX: LLM-Driven Agentic Multi-Expert Fusion with Explainability for AI-Generated Image Detection</a></strong><br><sub>结合经校准的可靠性档案，融合已采集的专家证据。</sub></td>
<td width="12%" valign="top">arXiv 2026<br><sub>预印本</sub><br>26/03</td>
<td width="24%" valign="top"><code>I</code> · <code>D</code>&nbsp;<code>E</code><br>Qwen3‑32B<br>+ GPT‑4o<br><sub>Training-free · 需校准</sub></td>
<td width="14%" valign="top"><a href="https://github.com/suncore946/AgentFoX">最小推理</a></td>
</tr>
<tr>
<td width="50%" valign="top"><a name="evoguard"></a><strong><a href="https://arxiv.org/abs/2603.17343">EvoGuard: An Extensible Agentic RL-based Framework for Practical and Evolving AI-Generated Image Detection</a></strong><br><sub>选择互补检测器 API 或停止；检测工具保持冻结。</sub></td>
<td width="12%" valign="top">arXiv 2026<br><sub>预印本</sub><br>26/03</td>
<td width="24%" valign="top"><code>I</code> · <code>D</code><br>Qwen3‑VL‑4B<br><sub>RL</sub></td>
<td width="14%" valign="top"></td>
</tr>
<tr>
<td width="50%" valign="top"><a name="forgeryvcr"></a><strong><a href="https://arxiv.org/abs/2602.14098">ForgeryVCR: Visual-Centric Reasoning via Efficient Forensic Tools in MLLMs for Image Forgery Detection and Localization</a></strong><br><sub>依据工具视觉输出继续检查；预测框经 SAM2 转为掩码。</sub></td>
<td width="12%" valign="top">ACM MM 2026<br><sub>口头报告 · 已录用</sub><br>26/02</td>
<td width="24%" valign="top"><code>I</code> · <code>D</code>&nbsp;<code>L</code><br>Qwen3‑VL‑4B<br><sub>SFT + RL</sub></td>
<td width="14%" valign="top"><a href="https://github.com/youqiwong/ForgeryVCR">代码</a><br><a href="https://huggingface.co/youqiwong/ForgeryVCR">权重</a></td>
</tr>
<tr>
<td width="50%" valign="top"><a name="aifo"></a><strong><a href="https://arxiv.org/abs/2511.00181">From Evidence to Verdict: An Agent-Based Forensic Framework for AI-Generated Image Detection</a></strong> (AIFo)<br><sub>采集证据、推理并辩论，由裁判决定终止。</sub></td>
<td width="12%" valign="top">arXiv 2025<br><sub>预印本</sub><br>25/10</td>
<td width="24%" valign="top"><code>I</code> · <code>D</code>&nbsp;<code>E</code><br>GPT‑4o<br><sub>Training-free</sub></td>
<td width="14%" valign="top"></td>
</tr>
</tbody>
</table>

<a name="text"></a>
<a name="相关工具增强多角色流程"></a>

## 文本

输入：<code>I</code> 图像 · <code>V</code> 视频 · <code>A</code> 音频 · <code>T</code> 文本<br>任务：<code>D</code> 检测 · <code>L</code> 定位 · <code>E</code> 解释

**[查看技术对比 →](docs/COMPARISON_CN.md#text)**

<table>
<thead>
<tr>
<th width="50%" align="left">论文与流程</th>
<th width="12%" align="left">发表 / 日期</th>
<th width="24%" align="left">标签 · 模型 · 训练</th>
<th width="14%" align="left">资源</th>
</tr>
</thead>
<tbody>
<tr>
<td width="50%" valign="top"><a name="qwen-langgraph"></a><strong><a href="https://link.springer.com/article/10.1007/s10791-026-10710-z">Performance evaluation and interpretability of a Qwen LangGraph agent for AI written and AI rewritten text detection</a></strong><br><sub>融合 + 按需调用控制器：选择工具、停止或转人工（≤2 步，≤1 次专用模型调用）。</sub></td>
<td width="12%" valign="top">Discover<br>Computing 2026<br>26/10</td>
<td width="24%" valign="top"><code>T</code> · <code>D</code>&nbsp;<code>E</code><br>Qwen2.5‑1.5B<br><sub>工具经训练</sub></td>
<td width="14%" valign="top"><a href="https://drive.google.com/drive/folders/14wU4r0-uRirkJ9aP3xI1lj2yHfWkj7DQ">作者资源</a></td>
</tr>
<tr>
<td width="50%" valign="top"><a name="aigt-agent"></a><strong><a href="https://aclanthology.org/2026.findings-emnlp.272/">Beyond Text-Intrinsic Features: An Agentic Framework for Evidence-Based AI-Generated Text Detection</a></strong> (AIGT-Agent)<br><sub>检测与搜索模块分别执行；固定先精确后模糊搜索，再聚合网页证据。</sub></td>
<td width="12%" valign="top">Findings EMNLP<br>2026<br>26/10</td>
<td width="24%" valign="top"><code>T</code> · <code>D</code>&nbsp;<code>E</code><br>GPT‑5‑mini</td>
<td width="14%" valign="top"><a href="https://github.com/TrustAIRLab/AIGT-Agent">代码</a><br><a href="https://github.com/TrustAIRLab/AIGT-Agent/tree/main/data/benchmark_4k">基准</a></td>
</tr>
</tbody>
</table>

<a name="cross-modal"></a>
<a name="相关规则编排方法"></a>
<a name="待进一步核验"></a>

## 跨模态

输入：<code>I</code> 图像 · <code>V</code> 视频 · <code>A</code> 音频 · <code>T</code> 文本<br>任务：<code>D</code> 检测 · <code>L</code> 定位 · <code>E</code> 解释

**[查看技术对比 →](docs/COMPARISON_CN.md#cross-modal)**

<table>
<thead>
<tr>
<th width="50%" align="left">论文与流程</th>
<th width="12%" align="left">发表 / 日期</th>
<th width="24%" align="left">标签 · 模型 · 训练</th>
<th width="14%" align="left">资源</th>
</tr>
</thead>
<tbody>
<tr>
<td width="50%" valign="top"><a name="falcon"></a><strong><a href="https://doi.org/10.1016/j.patcog.2026.115240">LLM as a forensic reasoner: Expert-guided video deepfake detection across modalities</a></strong> (FALCON)<br><sub>专用专家提取符号化证据，交由 LLM 进行取证推理。</sub></td>
<td width="12%" valign="top">Pattern Recognition<br>2026<br><sub>期刊预校样</sub><br>26/10<br><sub>在线 10-29</sub></td>
<td width="24%" valign="top"><code>A+V</code> · <code>D</code>&nbsp;<code>E</code><br><sub>三阶段人在回路训练</sub></td>
<td width="14%" valign="top"></td>
</tr>
<tr>
<td width="50%" valign="top"><a name="adaptive-multi-agent"></a><strong><a href="https://doi.org/10.3390/informatics13100163">A Multi-Agent Framework with Adaptive Orchestration for Explainable Multi-Modal Deepfake Detection</a></strong><br><sub>固定分歧阈值触发额外检测器，再融合并报告。</sub></td>
<td width="12%" valign="top">Informatics 2026<br>26/10</td>
<td width="24%" valign="top"><code>A+V</code> · <code>D</code>&nbsp;<code>E</code><br>Llama‑3‑70B<br>+ Gemini‑1.5‑Flash<br><sub>规则编排 · 检测器经训练</sub></td>
<td width="14%" valign="top"><a href="https://github.com/saoirsebarry/multiagent-deepfake-detection">代码</a><br><a href="https://github.com/saoirsebarry/multiagent-deepfake-detection/tree/main/checkpoints">权重</a></td>
</tr>
<tr>
<td width="50%" valign="top"><a name="enf-framework"></a><strong><a href="https://arxiv.org/abs/2610.22440">An Agentic ENF Framework for Forensic Video Authentication Against Generative AI</a></strong><br><sub>围绕 ENF 与检测证据作确定性状态转换；ENF 鉴真需独立可信参考。</sub></td>
<td width="12%" valign="top">arXiv 2026<br><sub>预印本</sub><br>26/10</td>
<td width="24%" valign="top"><code>A+V</code> · <code>D</code><br>确定性状态机<br><sub>规则编排 · 检测器经训练</sub></td>
<td width="14%" valign="top"><a href="https://github.com/RyanSolent95/enf-video-forensics">代码</a><br><a href="https://github.com/RyanSolent95/enf-video-forensics/tree/main/outputs">权重</a></td>
</tr>
<tr>
<td width="50%" valign="top"><a name="mm-veriagent"></a><strong><a href="https://arxiv.org/abs/2609.30698">MM-VeriAgent: Learning to Use Extensive Tools to Verify Multimodal Misinformation with Reinforcement Learning</a></strong><br><sub>选择九个工具之一或停止（≤3 轮）；当前样例固定参数。面向包含 AIGC 的广义图文虚假信息。</sub></td>
<td width="12%" valign="top">arXiv 2026<br><sub>预印本</sub><br>26/09<br><sub>v2 26/11</sub></td>
<td width="24%" valign="top"><code>T+I</code> · <code>D</code><br>Qwen2.5‑VL‑7B<br><sub>SFT + RL</sub></td>
<td width="14%" valign="top"></td>
</tr>
<tr>
<td width="50%" valign="top"><a name="omnivl-guard-pro"></a><strong><a href="https://arxiv.org/abs/2605.16962">OmniVL-Guard Pro: A Tool-Augmented Agent for Omnibus Vision-Language Forensics</a></strong><br><sub>依据观测或错误选择检索／裁剪／视觉工具。</sub></td>
<td width="12%" valign="top">arXiv 2026<br><sub>预印本</sub><br>26/05</td>
<td width="24%" valign="top"><code>T+I</code>&nbsp;/&nbsp;<code>T+V</code> · <code>D</code>&nbsp;<code>L</code><br>Qwen3‑VL‑8B<br><sub>SFT + RL</sub></td>
<td width="14%" valign="top"><a href="https://github.com/shen8424/OmniVL-Guard-Pro">项目</a></td>
</tr>
<tr>
<td width="50%" valign="top"><a name="fakehunter"></a><strong><a href="https://arxiv.org/abs/2508.14581">Memory-Anchored Multimodal Reasoning for Explainable Video Forensics</a></strong> (FakeHunter)<br><sub>检索记忆；低置信度触发视觉／音频复核。</sub></td>
<td width="12%" valign="top">arXiv 2025<br><sub>预印本</sub><br>25/08</td>
<td width="24%" valign="top"><code>A+V</code> · <code>D</code>&nbsp;<code>E</code><br>Qwen2.5‑Omni‑7B<br><sub>备选 MiniCPM‑o‑2_6</sub><br><sub>K-means 记忆</sub></td>
<td width="14%" valign="top"></td>
</tr>
<tr>
<td width="50%" valign="top"><a name="t2agent"></a><strong><a href="https://arxiv.org/abs/2505.19768">T²Agent: A Tool-augmented Multimodal Misinformation Detection Agent with Monte Carlo Tree Search</a></strong><br><sub>MCTS 探索工具／证据路径；v2 加入贪心工具子集选择。面向包含 AIGC 的广义图文虚假信息。</sub></td>
<td width="12%" valign="top">AAAI 2026<br>25/05<br><sub>预印本</sub></td>
<td width="24%" valign="top"><code>T+I</code> · <code>D</code><br>GPT‑4o<br><sub>Training-free</sub></td>
<td width="14%" valign="top"><a href="https://github.com/cuixing100876/T2Agent">代码<br><sub>部分缓存</sub></a></td>
</tr>
</tbody>
</table>

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

下方分别列出当前可选模型与论文复现基座；候选模型需结合具体取证任务开展评测。

### Agentic 取证平台

- [Resemble Investigator](https://docs.resemble.ai/detect/agents) · **托管 API。** 执行媒体真实性调查，以流式形式返回证据与评估；需要已开通 Investigator 权限的账户。
- [Clyravision](https://en.merantix-momentum.com/clyravision) · **需联系开通的平台。** 基于 Agent 工作流，结合取证痕迹、元数据与来源／语境核查分析图像；产品页提供演示录像。

### 可接入 Agent 的检测服务

- [Reality Defender RealAPI](https://www.realitydefender.com/product/realapi) · **检测 API。** 分析图像、音频与视频中的操纵痕迹，返回可接入 Agent 证据流程的结构化结果。
- [Sightengine](https://www.sightengine.com/docs/ai-generated-image-detection) · **检测 API。** 提供 AI 生成图像评分，相关文档另含深度伪造与 AI 生成视频检测模型。

### 专用取证模型

- [VeriSpoof](https://arxiv.org/abs/2611.04634)（2026‑11‑03）· 基于 Qwen3-ASR-1.7B 编码器和 MiniCPM5-2B，覆盖音频检测、归因、录音条件、片段定位及来源验证，输出可核查解释。已提供[推理代码](https://github.com/swagshaw/verispoof)与 [Plus 权重](https://huggingface.co/AustinXiao/VeriSpoof-Plus)；代码与权重采用 CC BY-NC 4.0。
- [Venus-DefakerOne2](https://arxiv.org/abs/2610.37918)（2026‑10‑27；11‑02 修订）· Qwen3.5-2B 图像／视频鉴伪专家，采用固定真假问答。已提供[权重](https://huggingface.co/qcf568/DefakerOne2)及[推理辅助脚本](https://github.com/inclusionAI/DefakerOne2)；复现论文使用 preview，release 使用更多训练数据。

### 数据集与基准

- [SEAR](https://huggingface.co/datasets/SEAR-benchmark/SEAR) · 音频问答标注，覆盖真假判断、线索、数值测量与取证解释；配套 [BAEA 与评测代码](https://github.com/SEAR-benchmark/SEAR)，需另行获取 ASVspoof 原始音频。
- [VeriSpoof-Bench](https://huggingface.co/datasets/AustinXiao/VeriSpoof-Bench) · 提供 54 个子集、177,852 项的标签、清单、元数据与重建材料；原始音频从各源语料获取，遵守对应许可。
- [RRVBench](https://www.modelscope.cn/models/DanceText/RRVBench) · DefakerOne2 配套视频基准，含 1,319 条真实视频、11 个生成器的 11,000 条合成视频；作者标注非商业研究使用。
- [DeepfakeGenome](https://arxiv.org/abs/2611.06046)（2026‑11‑04）· 约 200 万图像、100 种人脸伪造算法，包含检索式归因评测。[数据](https://huggingface.co/datasets/DeepfakeGenome/DeepfakeGenome)和[训练／测试代码](https://huggingface.co/DeepfakeGenome/DeepfakeGenome_Codebase)已发布，部分原始数据须另从 FF++／DF40 等来源取得，使用限制依各来源而定。
- [WildFakeToolBench](https://github.com/TrustAIRLab/WildFakeToolBench)（[论文](https://arxiv.org/abs/2610.31152) 10‑22；代码 10‑28 发布）· 156 种图像后处理工具，用于真实传播条件下的检测鲁棒性评测。作者限定学术用途。
- [WildAIGC-Bench V3](https://github.com/YuZijian/WildAIGC-Bench)（2026‑11‑03 更新）· 包含 600 张标注为 AI 生成、638 张标注为真实的图像及来源证据。评测前请核对[样本](https://huggingface.co/datasets/yuzj1997yzj/WildAIGC-Bench)附带的标签与证据。

### 面向新实验的当前多模态基座

以下 Qwen 变体支持视觉输入；输入模态与许可按具体权重版本区分。

- [Qwen3.5](https://github.com/QwenLM/Qwen3.8#qwen35)，尤其是 [Qwen3.5-9B](https://huggingface.co/Qwen/Qwen3.5-9B) · 原生支持图像/视频理解；9B 可作为本地工具调用型智能体的紧凑开放权重候选。
- [Qwen3.6-35B-A3B](https://huggingface.co/Qwen/Qwen3.6-35B-A3B) · 支持图像/视频的开放权重 MoE，总参数 35B、激活参数 3B，支持保留推理上下文，适合迭代式智能体流程。
- [Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B) · 更新一代的开放权重原生 VLM，支持图像/视频理解与多步智能体任务；采用 Apache-2.0 许可。
- [Qwen3.8-Flash-Next](https://github.com/QwenLM/Qwen3.8-Flash-Next)（[权重](https://huggingface.co/Qwen/Qwen3.8-Flash-Next)）· 支持图像/视频的开放权重多模态 MoE 架构预览；采用 Qwen Community 1.0 许可。

### System-1 快速决策与感知模型

这里的 System-1 包含直接结构化决策与候选排序；这些通用感知／决策资源用于取证任务时，需要任务级校准与评测。

- [Liquid d1](https://www.liquid.ai/blog/lfm3) · 2026‑10‑27 新增开放权重 [d1-2B](https://huggingface.co/LiquidAI/d1-2B)（文本／图像／视频）和 [d1-Omni-2B](https://huggingface.co/LiquidAI/d1-Omni-2B)（增加音频），提供权重与推理代码。[d1-ultra](https://www.liquid.ai/blog/d1-ultra) 提供文本／图像决策 API，早期 [d1-3B](https://huggingface.co/LiquidAI/d1-3B) 与实验性 [d1-omni-600M](https://huggingface.co/LiquidAI/d1-omni-600M) 仍可作对照。开放权重采用含商用营收限制的 LFM Open License v1.0。
- [Cloudflare Clef](https://blog.cloudflare.com/clef-faster-cheaper-multimodal/) · [Clef](https://huggingface.co/Cloudflare/clef)／[Clef-flash](https://huggingface.co/Cloudflare/clef-flash) 面向文本、图像、视频做结构化决策，[Clef-omni](https://huggingface.co/Cloudflare/clef-omni) 增加音频；提供 Apache-2.0 权重和托管 Workers AI 服务，多模态版本更新于 2026‑10‑09。
- [pplx-decider-v1.2](https://huggingface.co/perplexity-ai/pplx-decider-v1.2) · Perplexity 基于 Qwen3.8-27B 的文本／图像决策模型，并行读取多个问题标记；问题之间可互相注意。模型卡列出 Apache-2.0 权重与推理代码，并说明私有访问方式。
- [MetaEncoder-30B](https://huggingface.co/facebook/meta-encoder) · 将文本／图像／视频任务和候选编码为可缓存嵌入，直接进行候选排序；提供[评测代码](https://github.com/facebook/meta-encoder-eval)。权重访问需要申请并接受模型条款。视频使用原生实现，vLLM 适配器支持文本／图像；相似度分数需按目标任务校准。
- [Intern-Decision](https://github.com/InternLM/Intern-Decision) · 文本加可选图像，单次前向输出多个类型化 JSON 决策；提供 [4B 权重](https://huggingface.co/internlm/Intern-Decision-4B)及 0.8B/2B 版本。代码与权重采用 Apache-2.0。
- [Valen（万澜）](https://github.com/Valen-Team/Valen) · 共享状态的文本／图像／采样视频决策；提供 0.8B/2B/[4B 权重](https://huggingface.co/Valen-Team/Valen-4B)、Apache-2.0 许可及本地 ONNX/GGUF 选项。本地视频采样 16 帧，免费网页取中间一帧；SystemOne 与 Decisions API 每次请求最多支持 8 个问题和 1 张图像。
- [TypeSafe Jev](https://docs.typesafe.ai/models) · 托管式结构化决策 API：截至 2026‑11‑08，jev-latest 与 jev-preview 均指向 1.14.0。[图像输入](https://docs.typesafe.ai/images)与 [Box 定位](https://docs.typesafe.ai/primitives/box)仍为实验功能。

### 所收录论文使用的基座

- [Qwen3-VL](https://github.com/QwenLM/Qwen3-VL) · 支持图像／视频推理与定位的视觉语言模型系列，包含多篇收录方法使用的 4B、8B 版本。
- [Qwen2.5-VL-7B-Instruct](https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct) · 图像／视频理解基座，用于 ForenAgent、ARGUS 和 MM-VeriAgent；UniShield 使用 Qwen2.5-VL 系列。
- [Qwen3-32B](https://huggingface.co/Qwen/Qwen3-32B) · 文本推理模型，用于 AgentFoX 的 Agent 引导证据融合。
- [Qwen2.5-Omni-7B](https://huggingface.co/Qwen/Qwen2.5-Omni-7B) · 支持文本、图像、音频与视频理解的全模态基座，用于 FakeHunter 和 BAEA。
- [Qwen2.5-Omni-3B](https://huggingface.co/Qwen/Qwen2.5-Omni-3B) · ToolDF 的音频工具调用基座，使用 LoRA SFT 适配。
- [MiniCPM-o 2.6](https://huggingface.co/openbmb/MiniCPM-o-2_6) · 支持视觉、音频与语言的全模态模型，是 FakeHunter 评估的替代基座。

### 闭源模型服务

- [OpenAI API 模型](https://developers.openai.com/api/docs/models) · GPT 系列服务的官方模型目录，多篇收录方法使用该系列；复现时需核对论文中的具体模型或快照。
- [Google Gemini API](https://ai.google.dev/gemini-api/docs/models) · 官方多模态模型目录与 API 文档，涵盖 SafeGuard 使用的 Gemini 系列。
- [Qwen3.8-Omni-Flash](https://qwen.ai/blog?id=qwen3.8-omni-flash) · 托管式原生全模态模型，接收文本、图像、音频与视频，支持工具调用和长上下文视听推理。

### Agent 框架与工具执行

- [LangGraph](https://docs.langchain.com/oss/python/langgraph/overview) · 支持状态持久化与人工审核的工作流编排框架，可组织多步骤证据收集与仲裁。
- [Pydantic AI](https://pydantic.dev/docs/ai/overview/) · 提供类型化工具、结构化输出与依赖注入的 Python Agent 框架，适合定义清晰的检测器接口。
- [Codex SDK](https://learn.chatgpt.com/docs/codex-sdk) · 以编程方式管理代码 Agent 会话，可用于基于代码的实验与研究流程集成。
- [OpenHands Software Agent SDK](https://docs.openhands.dev/sdk) · 支持 Shell、文件、浏览器与 MCP 工具的自定义 Agent SDK，提供本地与远程执行方式。
- [Pi](https://pi.dev/docs/latest/sdk) · 可嵌入应用的代码 Agent SDK，支持会话配置与工具扩展，用于构建自定义执行流程。
- [reflex](https://github.com/kshetrajna12/reflex) · 结构化视觉判断的推理框架，默认使用冻结的 Qwen3.5-4B，共享前缀缓存并隔离批处理多个问题。

<a name="link-checks"></a>

## 链接检查

[链接审计工作流](.github/workflows/link-audit.yml)每周一 06:23 UTC 及 main 分支相关内容更新时运行，也可在 GitHub Actions 中手动触发。报告记录重定向链与目标地址，并分别列出 HTTP 404/410、访问限制、暂时性错误和本地文件／锚点问题，供人工核查。使用方式与报告说明见[链接审计指南](scripts/LINK_AUDIT.md)。
