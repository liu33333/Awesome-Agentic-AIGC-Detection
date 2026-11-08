# 技术对比

[返回论文列表](../README_CN.md) · [English](COMPARISON.md) · **简体中文**

对比各方法的推理模型、训练要求与智能体工作流程。

两个维度均仅按音频、视觉、文本、跨模态组织，并沿用目录的日期顺序；固定流程、规则编排与工具选择等差异在表内说明。

本页保留论文报告的模型版本；更新的候选模型见[资源](../README_CN.md#resources)。

[推理配置](#inference-setups) · [智能体流程](#agent-workflows)

<a name="inference-setups"></a>

## 推理配置

任务标签对应明确输出：检⁠测（真伪判定）、定位（篡改区域/片段/掩码）、解释（面向读者的取证理由）。模型按鉴伪推理配置列出；训练方式指鉴伪智能体的任务适配，工具训练、校准与记忆构建分别注明。

[音频](#inference-audio) · [视觉（图像与视频）](#inference-visual) · [文本](#inference-text) · [跨模态](#inference-cross-modal)

<a name="inference-audio"></a>

### 音频

| 方法 | 输入 / 任务范围 | 鉴伪推理模型 / 工具 | 智能体<br>训练方式 | 训练 / 配置说明 |
| --- | --- | --- | --- | --- |
| **[ToolDF](../README_CN.md#tooldf)**<br><sub>[Findings of EMNLP 2026](https://aclanthology.org/2026.findings-emnlp.842/)</sub> | 音频 · 深度伪造检测<br><sub>输出：检测 · 定位 · 解释</sub> | Qwen2.5-Omni-3B<br><sub>工具：Demucs 分离；XLSR-AASIST 专家</sub> | LoRA SFT | 基于工具调用轨迹进行 LoRA SFT；最终采用任一分支为假即判假的聚合。代码附音频重建脚本。 |
| **[SEAR / BAEA](../README_CN.md#sear)**<br><sub>arXiv 2026 预印本</sub> | 音频 · 深度伪造检测<br><sub>输出：检测 · 解释</sub> | 冻结的 Qwen2.5-Omni-7B<br><sub>工具：librosa，35 项声学测量</sub> | Training-free | 声学特征与真实音频的中位数／MAD 比较。Adaptive 在预算内选择特征组；Fixed 使用确定性证据采集。 |

<a name="inference-visual"></a>

### 视觉（图像与视频）

| 方法 | 输入 / 任务范围 | 鉴伪推理模型 / 工具 | 智能体<br>训练方式 | 训练 / 配置说明 |
| --- | --- | --- | --- | --- |
| **[ATAR](../README_CN.md#atar)**<br><sub>ACM Multimedia 2026 口头报告 · 已录用</sub> | 图像 · 生成检测；人脸/局部/文档篡改<br><sub>输出：检⁠测 · 定⁠位 · 解⁠释</sub> | Qwen3-VL-8B-Instruct<br><sub>工具：Grounded-SAM</sub> | SFT + RL | SFT + GRPO；Grounded-SAM 将区域描述转为定位掩码。 |
| **[Defake-o3](../README_CN.md#defake-o3)**<br><sub>ACM Multimedia 2026 已录用</sub> | 图像 · 生成内容检测<br><sub>输出：检⁠测 · 定⁠位 · 解⁠释</sub> | Qwen3-VL-8B-Instruct<br><sub>工具：Zoom In 裁剪工具</sub> | SFT + RL | LoRA SFT + GRPO；训练期 Evidence Verifier 提供奖励，推理可输出局部证据框。 |
| **[DVAR](../README_CN.md#dvar)**<br><sub>ACM Multimedia 2026</sub> | 视频 · 生成内容检测<br><sub>输出：检测 · 解释</sub> | GPT-5.4<br><sub>工具：GenVideoKB 检索</sub> | Training-free | 生成解释与自然解释智能体及裁决者采用两轮辩论；评测知识库冻结。 |
| **[ForgeryVCR](../README_CN.md#forgeryvcr)**<br><sub>ACM Multimedia 2026 口头报告 · 已录用</sub> | 图像 · 篡改检测/定位<br><sub>输出：检⁠测 · 定⁠位</sub> | Qwen3-VL-4B-Instruct<br><sub>工具：NoisePrint++；SAM2；ELA / FFT / 放大</sub> | SFT + RL | SFT + GRPO；策略使用视觉中间结果，预测框提示 SAM2 生成掩码。 |
| **[ForenAgent](../README_CN.md#forenagent)**<br><sub>ECCV 2026 已发表</sub> | 图像 · 生成检测；局部篡改<br><sub>输出：检⁠测 · 解⁠释</sub> | Qwen2.5-VL-7B<br><sub>工具：12 个取证工具</sub> | SFT + RL | 全参数 SFT + GRPO；Python 操作与取证工具输出引导迭代检查。 |
| **[SafeGuard](../README_CN.md#safeguard)**<br><sub>ECCV 2026 已发表</sub> | 视频 · 社会风险生成内容<br><sub>输出：检⁠测 · 解⁠释</sub> | GPT-4o + Gemini-2.5-Pro<br><sub>工具：Grounding DINO；SAM 2；RAFT；Depth Anything V2；DINOv2；D3</sub> | Training-free | 提示词智能体；D3 与 Depth Anything V2 经任务调优，掩码用于选择检查区域。 |
| **[Dissecting Agentic Forensics](../README_CN.md#dissecting-agentic-forensics)**<br><sub>ECCV 2026 AI4MFDD workshop</sub> | 图像 · 伪造检测<br><sub>输出：检测 · 解释</sub> | 七个检测器 → MLLM 审核者 + 裁判<br><sub>强混合配置：Gemma-4-26B-A4B-it 审核者 + GPT-5 裁判</sub> | 智能体免训练 | 七个检测器的校准分数输入审核者与裁判。所列混合配置使用 Gemma 审核者与 GPT-5 裁判。 |
| **[FACT](../README_CN.md#fact)**<br><sub>arXiv 2026 预印本</sub> | 图像 · 真伪检测<br><sub>输出：检测 · 解释</sub> | Qwen3-VL-8B-Instruct<br><sub>工具：五个冻结专家；八种探针</sub> | SFT + RL | SFT 后使用成本感知 GRPO；GPT-5.1 用于训练期技能演化与轨迹合成。 |
| **[PATE-Forensics](../README_CN.md#pate-forensics)**<br><sub>arXiv 2026 · DDL-X 挑战报告</sub> | 图像 · 人脸伪造<br><sub>输出：检测 · 定位 · 解释</sub> | Qwen3.5-Flash<br><sub>工具：DINOv3-L/16 取证检测/分割</sub> | 解释模型免训练 | 提示词驱动 Qwen3.5-Flash 解释取证感知结果；DINOv3 工具采用 LoRA 与监督检测／掩码损失。官方实现：CLASP。 |
| **[ARGUS](../README_CN.md#argus)**<br><sub>arXiv 2026 预印本</sub> | 视频 · 生成内容检测<br><sub>输出：检测 · 解释</sub> | Qwen2.5-VL-7B<br><sub>四个观察者：纹理 / 光照 / 运动 / 物理；裁判</sub> | SFT + RL | 各角色使用 LoRA SFT，裁判再经 GRPO；四个观察者分别报告纹理、光照、运动与物理证据。 |
| **[Hermes](../README_CN.md#hermes)**<br><sub>ICML 2026 已发表</sub> | 视频 · 生成内容检测<br><sub>输出：检⁠测 · 解⁠释</sub> | Qwen3-VL-8B + ChatGPT-5<br><sub>工具：现成视觉工具</sub> | Training-free | 免训练智能体流程；ChatGPT-5 参与推理时规划，Qwen3-VL-8B 执行感知、初始推理与讨论。 |
| **[ForeAgent](../README_CN.md#foreagent)**<br><sub>arXiv 2026 预印本</sub> | 图像 · 生成内容检测<br><sub>输出：检测 · 解释</sub> | Qwen3-VL-8B<br><sub>原图 + 频域视图；NPR 专家</sub> | LoRA + 迭代 SFT | LoRA 预训练 + 迭代自筛选 SFT；训练期自我改进支持感知 → 判定的推理流程。 |
| **[UniShield](../README_CN.md#unishield)**<br><sub>CVPR Findings 2026 已发表</sub> | 图像 · 生成检测；人脸/局部/文档篡改<br><sub>输出：检⁠测 · 定⁠位 · 解⁠释</sub> | Qwen2.5-VL + GPT-4o<br><sub>工具：IML-ViT；FakeShield；AscFormer；DMDL-R1 / GLaMM；CLIP；DFD-R1；AIDE；FakeVLM</sub> | RL（路由器） | 任务路由器、DFD-R1 与 DMDL-R1 使用 GRPO，GLaMM 经微调；自然图像与文档分支提供定位。 |
| **[VRAG-DFD](../README_CN.md#vrag-dfd)**<br><sub>CVPR Findings 2026</sub> | 图像 · 深度伪造检测<br><sub>输出：检测 · 解释</sub> | 多模态推理模型 | SFT + RL | 先检索证据，再交叉核验；采用 SFT + GRPO。 |
| **[AgentFoX](../README_CN.md#agentfox)**<br><sub>arXiv 2026 预印本</sub> | 图像 · 生成内容检测<br><sub>输出：检⁠测 · 解⁠释</sub> | Qwen3-32B + GPT-4o<br><sub>工具：DRCT；RINE；SPAI；PatchShuffle</sub> | Training-free | 智能体与专家权重冻结；拟合分数校准器与参考数据先验。 |
| **[EvoGuard](../README_CN.md#evoguard)**<br><sub>arXiv 2026 预印本</sub> | 图像 · 生成内容检测<br><sub>输出：检⁠测</sub> | Qwen3-VL-4B-Instruct<br><sub>工具：Effort；FakeVLM；MIRROR；AIDE</sub> | RL | 策略经 GRPO 训练，检测工具保持冻结；策略训练后可扩展工具。 |
| **[AIFo](../README_CN.md#aifo)**<br><sub>arXiv 2025 预印本</sub> | 图像 · 生成内容检测<br><sub>输出：检⁠测 · 解⁠释</sub> | GPT-4o<br><sub>工具：5 个预训练分类器；可选 CLIP-ViT-B/32 检索</sub> | Training-free | 提示词智能体与冻结分类器；可选案例记忆提供检索证据。 |

<a name="inference-text"></a>

### 文本

| 方法 | 输入 / 任务范围 | 鉴伪推理模型 / 工具 | 智能体<br>训练方式 | 训练 / 配置说明 |
| --- | --- | --- | --- | --- |
| **[AIGT-Agent](../README_CN.md#aigt-agent)**<br><sub>Findings of EMNLP 2026</sub> | 文本 · AI 生成文本检测<br><sub>输出：检测 · 解释</sub> | GPT-5-mini<br><sub>工具：MPU / Binoculars；Google Search；网页过滤/分析角色</sub> |  | 独立检测与搜索模块；先精确后模糊搜索，再聚合网页证据。 |
| **[Qwen–LangGraph](../README_CN.md#qwen-langgraph)**<br><sub>Discover Computing 2026 已发表</sub> | 文本 · 人工/AI 来源与 AI 生成/改写分类<br><sub>输出：检测 · 解释</sub> | Qwen2.5-1.5B-Instruct<br><sub>工具：DeBERTa-v3-xsmall；ELECTRA-small；词汇 SGD 分类器；文体诊断</sub> |  | 专用分类器经训练／微调；融合权重与路由阈值在验证集选定。 |

<a name="inference-cross-modal"></a>

### 跨模态

| 方法 | 输入 / 任务范围 | 鉴伪推理模型 / 工具 | 智能体<br>训练方式 | 训练 / 配置说明 |
| --- | --- | --- | --- | --- |
| **[FALCON](../README_CN.md#falcon)**<br><sub>Pattern Recognition 2026 · 期刊预校样</sub> | 音视频 · 深度伪造检测<br><sub>输出：检测 · 解释</sub> |  | 三阶段人在回路训练 | 专家提取符号化证据，由 LLM 综合进行取证推理。 |
| **[ENF framework](../README_CN.md#enf-framework)**<br><sub>arXiv 2026</sub> | 音视频 · 物理信号与深度伪造分析<br><sub>输出：检测</sub> | 音频 / 滚动快门视频的物理 ENF 分析<br><sub>空间 / rPPG / 唇音同步 / 元数据检查；经训练检测器</sub> |  | 确定性状态机结合物理 ENF 分析与经训练检测器；ENF 鉴真需要独立可信参考。 |
| **[Adaptive multi-agent framework](../README_CN.md#adaptive-multi-agent)**<br><sub>Informatics 2026 已发表</sub> | 音视频 · 深度伪造检测<br><sub>输出：检测 · 解释</sub> | Llama-3-70B（报告）+ Gemini-1.5-Flash（语境）<br><sub>检测器：Xception；FreqNet；MobileNetV2 + BiLSTM；EfficientNet-B0；ECAPA-TDNN + MLP</sub> |  | 检测器经监督训练／微调，ECAPA 主干冻结；分歧阈值触发第二阶段，融合权重在验证集选定。 |
| **[MM-VeriAgent](../README_CN.md#mm-veriagent)**<br><sub>arXiv 2026 预印本</sub> | 图文 · 更广泛的虚假信息，包含 AIGC<br><sub>输出：检测</sub> | Qwen2.5-VL-7B<br><sub>九个工具：检索 / 事实核查 / DFFreq / DDA / MVSS-Net / 描述生成 / 一致性</sub> | SFT + RL | SFT + GRPO，RL 使用缓存工具输出；策略在三轮内选择工具名或停止，当前样例采用固定工具参数。 |
| **[OmniVL-Guard Pro](../README_CN.md#omnivl-guard-pro)**<br><sub>arXiv 2026 预印本</sub> | 文图 / 文视频 · 伪造检测/定位/事实核查；兼容单模态<br><sub>输出：检⁠测 · 定⁠位</sub> | Qwen3-VL-8B<br><sub>工具：InsightFace；SAM3；检索 / 裁剪 / 视频帧工具</sub> | SFT + RL | FSTR SFT + 结果／过程 RL；训练期 Checker 引导过程奖励，输出包括类别与定位。 |
| **[T²Agent](../README_CN.md#t2agent)**<br><sub>AAAI 2026</sub> | 图文 · 更广泛的虚假信息检测<br><sub>输出：检测</sub> | GPT-4o<br><sub>工具：PSCC-NET；LLaVA-34B；网页 / 反向图片搜索</sub> | Training-free | MCTS 探索工具／证据路径；v2 加入贪心工具子集选择；公开实现使用缓存／预计算工具结果。 |
| **[FakeHunter](../README_CN.md#fakehunter)**<br><sub>arXiv 2025 预印本</sub> | 音视频 · 篡改检测<br><sub>输出：检⁠测 · 解⁠释</sub> | Qwen2.5-Omni-7B<br><sub>另评测备选模型：MiniCPM-o-2_6</sub><br><sub>工具：CLIP + CLAP 编码器；FAISS 检索记忆</sub> |  | K-means 在训练集 CLIP／CLAP 嵌入上构建检索记忆。 |


<details>
<summary>AIFo 分类器标识</summary>

- haywoodsloan/ai-image-detector-deploy
- Organika/sdxl-detector
- legekka/AI-Anime-Image-Detector-ViT
- Smogy/SMOGY-Ai-images-detector
- NYUAD-ComNets/NYUAD_AI-generated_images_detector

</details>

<a name="agent-workflows"></a>

## 智能体流程

“组织”指推理阶段；“训练”指智能体适配。工具训练与代码生成接口在相应条目说明。

[音频](#audio) · [视觉（图像与视频）](#visual) · [文本](#text) · [跨模态](#cross-modal)

<a name="audio"></a>

### 音频

| 方法 | 智能体组织 | 工具接口 | 反馈后改变什么？ | 训练 / 配置 | 证据输出 |
| --- | --- | --- | --- | --- | --- |
| **[ToolDF](../README_CN.md#tooldf)** | 单智能体 + 最终聚合器 | 音源分离 + 专用检测器 | 动态选择分离与检测工具 | LoRA SFT；训练观测由标签构造 | 判定 + 时间/音源证据 + 理由 |
| **[SEAR / BAEA](../README_CN.md#sear)** | Adaptive 智能体 / Fixed 基线 | 白名单声学特征组 | Adaptive 在预算内选组；Fixed 为确定性流程 | 模型冻结；真实音频参考统计量 | 判定 + 实测声学证据 + 理由 |

<a name="visual"></a>
<a name="related-visual"></a>

### 视觉（图像与视频）

| 方法 | 智能体组织 | 工具接口 | 反馈后改变什么？ | 训练 / 配置 | 证据输出 |
| --- | --- | --- | --- | --- | --- |
| **[ATAR](../README_CN.md#atar)** | 单智能体 | 预定义裁剪 + 22 个取证工具 | 选择下一次裁剪/工具或停止 | SFT + GRPO；工具先验课程 | 判定 + 区域描述；Grounded-SAM 掩码 |
| **[Defake-o3](../README_CN.md#defake-o3)** | 单智能体 | 预定义 Zoom In | 选择继续裁剪或最终判定 | SFT + GRPO；验证器用于奖励 | 判定 + 全局描述；可选框/局部描述 |
| **[DVAR](../README_CN.md#dvar)** | 生成 / 自然解释智能体 + 裁决者 | GenVideoKB 检索 | 固定两轮辩论修订解释 | 免训练；评测知识库冻结 | 判定 + 辩论解释 |
| **[ForgeryVCR](../README_CN.md#forgeryvcr)** | 单智能体 | ELA / NoisePrint++ / FFT / 放大 | 依据视觉输出继续调用工具/定位 | SFT + GRPO | 判定 + 框 → SAM2 掩码 |
| **[ForenAgent](../README_CN.md#forenagent)** | 单智能体 | 生成处理代码 + 12 个固定取证工具 | 依据工具输出调整操作/裁剪 | SFT + GRPO | 判定 + 推理说明 + 工具可视化 |
| **[SafeGuard](../README_CN.md#safeguard)** | 感知求解器 + 验证器 | 预定义定位 + 四类取证工具 | 修订假设并重新采证（≤3 轮） | 智能体免训练；取证工具经调优 | 判定 + 置信度 + 局部证据 |
| **[Dissecting Agentic Forensics](../README_CN.md#dissecting-agentic-forensics)** | 七个检测器 → 审核者 → 裁判 | 固定检测分数与视觉证据 | 审核已有证据，由裁判聚合 | 智能体免训练；检测分数经校准 | 判定 + 审核理由 |
| **[FACT](../README_CN.md#fact)** | 单智能体 | 五个冻结专家 + 八种探针 | 动态选择工具或停止 | SFT + 成本感知 GRPO；GPT-5.1 训练教师 | 判定 + 工具证据 |
| **[PATE-Forensics](../README_CN.md#pate-forensics)** | 固定感知工具 → 解释模型 | 检测概率 / 掩码 / 可疑区域裁剪 | 固定感知到解释流程 | 解释模型免训练；感知工具经训练 | 判定 + 掩码 + 证据约束解释 |
| **[ARGUS](../README_CN.md#argus)** | 四个观察者 → 裁判 | 固定纹理 / 光照 / 运动 / 物理观察 | 裁判聚合四份报告 | 全角色 LoRA SFT；裁判 GRPO | 判定 + 观察报告 |
| **[Hermes](../README_CN.md#hermes)** | 规划者 + 推理者 + 三角色讨论 | RAG 选择的问答检查 + 视觉工具 | 调用工具追加证据并修订图（≤3 轮） | 免训练 | 判定/评分 + 时序证据图 |
| **[ForeAgent](../README_CN.md#foreagent)** | 固定感知 → 判定 | 原图 / 频域视图 + NPR 专家 | 感知结果输入判定阶段 | LoRA 预训练 + 迭代自筛选 SFT | 判定 + 取证理由 |
| **[UniShield](../README_CN.md#unishield)** | 感知 → 检测 → 报告 | 预定义 8 检测器工具箱 | 每图单检测器 | GRPO 任务路由器；提示词调度 | 判定 + 报告；按任务输出掩码 |
| **[VRAG-DFD](../README_CN.md#vrag-dfd)** | 检索 → 交叉核验 | 固定 RAG 证据检索 | 在固定流程中交叉核验检索证据 | SFT + GRPO | 判定 + 检索证据 |
| **[AgentFoX](../README_CN.md#agentfox)** | 单推理核心 + 专家工具 | 预定义专家 + 可靠性档案 | 基于已采集证据调整融合/报告 | 核心冻结；拟合校准参数 | 判定 + 置信度 + 证据报告 |
| **[EvoGuard](../README_CN.md#evoguard)** | 单调度智能体 | 检测器 API + 能力档案 | 补充调用检测器或停止 | GRPO；检测器冻结 | 判定 + 多工具分析 |
| **[AIFo](../README_CN.md#aifo)** | 采集者 / 推理者 / 辩手 / 裁判 | 检索 / 元数据 / 分类器 / VLM | 围绕已有证据辩论；裁判终止 | 提示词智能体；权重冻结 | 判定 + 溯源/元数据 + 理由 |

<a name="text"></a>
<a name="related-text"></a>

### 文本

| 方法 | 智能体组织 | 工具接口 | 反馈后改变什么？ | 训练 / 配置 | 证据输出 |
| --- | --- | --- | --- | --- | --- |
| **[AIGT-Agent](../README_CN.md#aigt-agent)** | 独立检测与搜索模块 → 聚合 | MPU / Binoculars + 搜索 + 网页过滤/分析 | 固定先精确后模糊搜索 | 提示词角色 | 判定 + 检测与网页证据 |
| **[Qwen–LangGraph](../README_CN.md#qwen-langgraph)** | 局部融合 + 按需调用单控制器 | 预定义分类器 / 文体诊断 | 根据新增证据选择工具、停止或转人工（≤2 步，≤1 次专用模型调用） | 工具经训练，路由经校准 | 来源/改写概率 + 词汇/语言诊断 + 路由记录；概率来自分类器 |

<a name="cross-modal"></a>
<a name="related-cross-modal"></a>

### 跨模态

| 方法 | 智能体组织 | 工具接口 | 反馈后改变什么？ | 训练 / 配置 | 证据输出 |
| --- | --- | --- | --- | --- | --- |
| **[FALCON](../README_CN.md#falcon)** | 专用专家 + LLM 推理者 | 专家提取的符号化证据 |  | 三阶段人在回路训练 | 判定 + 取证理由 |
| **[ENF framework](../README_CN.md#enf-framework)** | 确定性状态机 | ENF + 空间 / rPPG / 唇音同步 / 元数据检测器 | 规则定义的状态转换 | 检测器经训练 | 信号 / 检测证据；ENF 鉴真需独立可信参考 |
| **[Adaptive multi-agent framework](../README_CN.md#adaptive-multi-agent)** | 规则编排的五检测器集合 + 报告模型 | 固定检测器 / XAI / 语境与转录 | 分歧触发第二阶段两个检测器 | 检测器经训练/微调 | 融合分数 + 显著性/SHAP/跨模态诊断 + 取证报告 |
| **[MM-VeriAgent](../README_CN.md#mm-veriagent)** | 单智能体 | 九个预定义工具 | 最多三轮选择工具名或停止；当前样例固定参数 | SFT + GRPO；基于缓存的 RL | 判定 + 工具证据 |
| **[OmniVL-Guard Pro](../README_CN.md#omnivl-guard-pro)** | 单推理策略 | 预定义检索 / 裁剪 / 视觉 / SAM3 | 依据观测/错误选择后续工具 | SFT + 结果 RL + Checker 引导过程 RL | 判定 + 轨迹 + 空间/文本/时序定位 |
| **[T²Agent](../README_CN.md#t2agent)** | MCTS 引导的智能体 | 取证 / VLM / 网页搜索工具 | 探索工具/证据路径；v2 贪心选择工具子集 | Training-free | 判定 + 搜索证据路径 |
| **[FakeHunter](../README_CN.md#fakehunter)** | 单提示词多模态模型 | 记忆检索 / 放大 / 梅尔频谱 | 低置信度触发视觉/音频复核 | 训练集构建记忆 | 判定 + 篡改类型 + 解释 |
