# Awesome Agentic AIGC Detection

[English](README.md) | [简体中文](README_CN.md)

面向 Agentic AIGC 检测的论文列表，按音频、视觉、文本和跨模态组织，并对比智能体组织、工具、反馈机制、训练方式与证据输出。

## 目录

- [音频](#audio)
- [视觉（图像与视频）](#visual)
- [文本](#text)
- [跨模态](#cross-modal)
- [技术对比](#technical-comparison)
- [补充与纠错](#contributing)

各表按日期倒序排列：已发表论文使用会议开幕日期；预印本及尚未核实正式出版的已录用论文使用 arXiv 首次提交日期。状态核实于 2026-10-04；“—”表示尚未核实官方仓库。

<a id="audio"></a>

## 音频

暂无已核实的独立条目。

<a id="visual"></a>

## 视觉（图像与视频）

| 论文 | 发表位置 / 状态 | 日期 | 输入 / 任务 | 官方仓库 |
| --- | --- | --- | --- | --- |
| <a id="atar"></a>**[Agentic Tool-Augmented Reasoning for Explainable Image Forgery Detection](https://arxiv.org/abs/2609.39066)** (ATAR) | ACM Multimedia 2026 · 口头报告 · 已录用 | 2026-09-30 | 图像 · 生成检测；人脸/局部/文档篡改 | — |
| <a id="forenagent"></a>**[Code-in-the-Loop Forensics: Agentic Tool Use for Image Forgery Detection](https://arxiv.org/abs/2512.16300)** (ForenAgent) | ECCV 2026 · 已发表 | 2026-09-08 | 图像 · 生成检测；局部篡改 | [仅工具集](https://github.com/zfr00/ForenAgent) |
| <a id="safeguard"></a>**[SafeGuard: A Multi-Agent Perception-Reasoning Framework for Social-Risk AI-Generated Video Detection](https://arxiv.org/abs/2607.03069)** | ECCV 2026 · 已发表 | 2026-09-08 | 视频 · 社会风险生成内容 | [项目；代码待发布](https://github.com/williamw99/SafeGuard) |
| <a id="defake-o3"></a>**[Defake-o3: From Speculative Rationales to Verifiable Evidence for Explainable AIGI Detection](https://arxiv.org/abs/2608.16259)** | ACM Multimedia 2026 · 已录用 | 2026-08-17 | 图像 · 生成内容检测 | — |
| <a id="hermes"></a>**[Hermes: An Evidence-Driven Agentic Framework for Trustworthy and Explainable AI-Generated Video Detection](https://proceedings.mlr.press/v306/li26be.html)** | ICML 2026 · 已发表 | 2026-07-06 | 视频 · 生成内容检测 | — |
| <a id="unishield"></a>**[UniShield: An Adaptive Multi-Agent Framework for Unified Forgery Image Detection and Localization](https://arxiv.org/abs/2510.03161)** | CVPR Findings 2026 · 已发表 | 2026-06-03 | 图像 · 生成检测；人脸/局部/文档篡改 | — |
| <a id="agentfox"></a>**[AgentFoX: LLM Agent-Guided Fusion with eXplainability for AI-Generated Image Detection](https://arxiv.org/abs/2603.23115)** | arXiv 2026 · 预印本 | 2026-03-24 | 图像 · 生成内容检测 | [最小推理实现](https://github.com/suncore946/AgentFoX) |
| <a id="evoguard"></a>**[EvoGuard: An Extensible Agentic RL-based Framework for Practical and Evolving AI-Generated Image Detection](https://arxiv.org/abs/2603.17343)** | arXiv 2026 · 预印本 | 2026-03-18 | 图像 · 生成内容检测 | — |
| <a id="forgeryvcr"></a>**[ForgeryVCR: Visual-Centric Reasoning via Efficient Forensic Tools in MLLMs for Image Forgery Detection and Localization](https://arxiv.org/abs/2602.14098)** | ACM Multimedia 2026 · 口头报告 · 已录用 | 2026-02-15 | 图像 · 篡改检测/定位 | [推理 + 权重](https://github.com/youqiwong/ForgeryVCR) |
| <a id="aifo"></a>**[From Evidence to Verdict: An Agent-Based Forensic Framework for AI-Generated Image Detection](https://arxiv.org/abs/2511.00181)** (AIFo) | arXiv 2025 · 预印本 | 2025-10-31 | 图像 · 生成内容检测 | — |

<a id="text"></a>

## 文本

暂无已核实的独立条目。

<a id="cross-modal"></a>

## 跨模态

按联合分析的媒体证据归类；文字指令本身不构成跨模态输入。

| 论文 | 发表位置 / 状态 | 日期 | 输入 / 任务 | 官方仓库 |
| --- | --- | --- | --- | --- |
| <a id="omnivl-guard-pro"></a>**[OmniVL-Guard Pro: A Tool-Augmented Agent for Omnibus Vision-Language Forensics](https://arxiv.org/abs/2605.16962)** | arXiv 2026 · 预印本 | 2026-05-16 | 文图 / 文视频 · 伪造检测/定位/事实核查；兼容单模态 | [项目；代码待发布](https://github.com/shen8424/OmniVL-Guard-Pro) |
| <a id="fakehunter"></a>**[Memory-Anchored Multimodal Reasoning for Explainable Video Forensics](https://arxiv.org/abs/2508.14581)** (FakeHunter) | arXiv 2025 · 预印本 | 2025-08-20 | 音视频 · 篡改检测 | — |

<a id="technical-comparison"></a>

## 技术对比

“组织”指推理阶段；“训练”指智能体适配，不代表底层工具未经预训练。工具未注明代码生成时均为预定义接口。

| 方法 | 智能体组织 | 工具接口 | 反馈后改变什么？ | 智能体训练 | 证据输出 |
| --- | --- | --- | --- | --- | --- |
| ATAR | 单智能体 | 预定义裁剪 + 22 个取证工具 | 选择下一次裁剪/工具或停止 | SFT + GRPO；工具先验课程 | 判定 + 区域描述；Grounded-SAM 掩码 |
| ForenAgent | 单智能体 | 生成处理代码 + 12 个固定取证工具 | 依据工具输出调整操作/裁剪 | SFT + GRPO | 判定 + 推理说明 + 工具可视化 |
| SafeGuard | 感知求解器 + 验证器 | 预定义定位 + 四类取证工具 | 修订假设并重新采证（≤3 轮） | 智能体不微调；取证工具经调优 | 判定 + 置信度 + 局部证据 |
| Defake-o3 | 单智能体 | 预定义 Zoom In | 选择继续裁剪或最终判定 | SFT + GRPO；验证器用于奖励 | 判定 + 全局描述；可选框/局部描述 |
| Hermes | 规划者 + 推理者 + 三角色讨论 | RAG 选择的问答检查 + 视觉工具 | 调用工具追加证据并修订图（≤3 轮） | 无任务专用智能体训练 | 判定/评分 + 时序证据图 |
| UniShield | 感知 → 检测 → 报告 | 预定义 8 检测器工具箱 | 每图单检测器；不回溯 | GRPO 任务路由器；提示词调度 | 判定 + 报告；按任务输出掩码 |
| AgentFoX | 单推理核心 + 专家工具 | 预定义专家 + 可靠性档案 | 基于已采集证据调整融合/报告 | 未描述核心微调；拟合校准参数 | 判定 + 置信度 + 证据报告 |
| EvoGuard | 单调度智能体 | 检测器 API + 能力档案 | 补充调用检测器或停止 | GRPO；检测器冻结 | 判定 + 多工具分析 |
| ForgeryVCR | 单智能体 | ELA / NoisePrint++ / FFT / 放大 | 依据视觉输出继续调用工具/定位 | SFT + GRPO | 判定 + 框 → SAM2 掩码 |
| AIFo | 采集者 / 推理者 / 辩手 / 裁判 | 检索 / 元数据 / 分类器 / VLM | 围绕已有证据辩论；裁判终止 | 提示词智能体；无权重训练 | 判定 + 溯源/元数据 + 理由 |
| OmniVL-Guard Pro | 单推理策略 | 预定义检索 / 裁剪 / 视觉 / SAM3 | 依据观测/错误选择后续工具 | SFT + 结果 RL + Checker 引导过程 RL | 判定 + 轨迹 + 空间/文本/时序定位 |
| FakeHunter | 单提示词多模态模型 | 记忆检索 / 放大 / 梅尔频谱 | 低置信度触发视觉/音频复核 | 智能体不微调；训练集构建记忆 | 判定 + 篡改类型 + 解释 |

<a id="contributing"></a>

## 补充与纠错

欢迎[推荐论文](https://github.com/liu33333/Awesome-Agentic-AIGC-Detection/issues/new?template=paper_suggestion.md)或[提交纠错](https://github.com/liu33333/Awesome-Agentic-AIGC-Detection/issues/new?template=correction.md)。请提供发表信息、日期依据、官方仓库及技术对比字段的具体来源。详见 [CONTRIBUTING.md](CONTRIBUTING.md)。
