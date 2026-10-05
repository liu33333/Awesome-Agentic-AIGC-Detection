# 技术对比

[返回论文列表](../README_CN.md) · [English](COMPARISON.md) · **简体中文**

对比各方法的推理模型、训练要求与智能体工作流程。

[推理配置](#inference-setups) · [智能体流程](#agent-workflows)

<a name="inference-setups"></a>

## 推理配置

任务标签对应明确输出：检⁠测（真伪判定）、定位（篡改区域/片段/掩码）、解释（面向读者的取证理由）。模型按鉴伪推理配置列出；“智能体免训练”按任务专用的智能体参数更新判断，工具训练、校准与记忆构建分别注明。

### 视觉（图像与视频）

| 方法 | 输入 / 任务范围 | 鉴伪推理模型 / 工具 | 智⁠能⁠体<br>免⁠训⁠练 | 训练 / 配置说明 |
| --- | --- | --- | --- | --- |
| **[ATAR](../README_CN.md#atar)** | 图像 · 生成检测；人脸/局部/文档篡改<br><sub>输出：检⁠测 · 定⁠位 · 解⁠释</sub> | Qwen3-VL-8B-Instruct<br><sub>工具：Grounded-SAM</sub> | 否 | SFT + GRPO；Grounded-SAM 将区域描述转为定位掩码。 |
| **[ForenAgent](../README_CN.md#forenagent)** | 图像 · 生成检测；局部篡改<br><sub>输出：检⁠测 · 解⁠释</sub> | Qwen2.5-VL-7B<br><sub>工具：12 个取证工具</sub> | 否 | 全参数 SFT + GRPO；基于伪造痕迹给出判断理由，裁剪用于辅助检查。 |
| **[SafeGuard](../README_CN.md#safeguard)** | 视频 · 社会风险生成内容<br><sub>输出：检⁠测 · 解⁠释</sub> | GPT-4o + Gemini-2.5-Pro<br><sub>工具：Grounding DINO；SAM 2；RAFT；Depth Anything V2；DINOv2；D3</sub> | 是 | 提示词智能体；D3 与 Depth Anything V2 经任务调优。掩码用于选择检查区域。 |
| **[Defake-o3](../README_CN.md#defake-o3)** | 图像 · 生成内容检测<br><sub>输出：检⁠测 · 定⁠位 · 解⁠释</sub> | Qwen3-VL-8B-Instruct<br><sub>工具：Zoom In 裁剪工具</sub> | 否 | SFT + GRPO；局部证据框为可选输出，Evidence Verifier 仅用于训练。 |
| **[Hermes](../README_CN.md#hermes)** | 视频 · 生成内容检测<br><sub>输出：检⁠测 · 解⁠释</sub> | Qwen3-VL-8B + ChatGPT-5<br><sub>工具：现成视觉工具</sub> | 是 | 无任务专用智能体训练；ChatGPT-5 参与推理时规划，ERG 时间戳用于证据定位。 |
| **[UniShield](../README_CN.md#unishield)** | 图像 · 生成检测；人脸/局部/文档篡改<br><sub>输出：检⁠测 · 定⁠位 · 解⁠释</sub> | Qwen2.5-VL + GPT-4o<br><sub>工具：IML-ViT；FakeShield；AscFormer；DMDL-R1 / GLaMM；CLIP；DFD-R1；AIDE；FakeVLM</sub> | 否 | 路由器 / DFD-R1 / DMDL-R1 使用 GRPO，GLaMM 经微调；自然图像/文档分支提供定位。Qwen 规模未注明。 |
| **[AgentFoX](../README_CN.md#agentfox)** | 图像 · 生成内容检测<br><sub>输出：检⁠测 · 解⁠释</sub> | Qwen3-32B + GPT-4o<br><sub>工具：DRCT；RINE；SPAI；PatchShuffle</sub> | 是 | 智能体与专家权重固定；分数校准器与参考数据先验需拟合。 |
| **[EvoGuard](../README_CN.md#evoguard)** | 图像 · 生成内容检测<br><sub>输出：检⁠测</sub> | Qwen3-VL-4B-Instruct<br><sub>工具：Effort；FakeVLM；MIRROR；AIDE</sub> | 否 | 策略经 GRPO 训练，工具冻结；免训练扩展指策略训练后添加工具。 |
| **[ForgeryVCR](../README_CN.md#forgeryvcr)** | 图像 · 篡改检测/定位<br><sub>输出：检⁠测 · 定⁠位</sub> | Qwen3-VL-4B-Instruct<br><sub>工具：NoisePrint++；SAM2；ELA / FFT / 放大</sub> | 否 | SFT + GRPO；预测框经 SAM2 转为掩码，主方法使用视觉中间结果。 |
| **[AIFo](../README_CN.md#aifo)** | 图像 · 生成内容检测<br><sub>输出：检⁠测 · 解⁠释</sub> | GPT-4o<br><sub>工具：5 个预训练分类器；可选 CLIP-ViT-B/32 检索</sub> | 是 | 提示词智能体与冻结分类器；可选案例记忆通过检索工作，无参数更新。 |

### 跨模态

| 方法 | 输入 / 任务范围 | 鉴伪推理模型 / 工具 | 智⁠能⁠体<br>免⁠训⁠练 | 训练 / 配置说明 |
| --- | --- | --- | --- | --- |
| **[OmniVL-Guard Pro](../README_CN.md#omnivl-guard-pro)** | 文图 / 文视频 · 伪造检测/定位/事实核查；兼容单模态<br><sub>输出：检⁠测 · 定⁠位</sub> | Qwen3-VL-8B<br><sub>工具：InsightFace；SAM3；检索 / 裁剪 / 视频帧工具</sub> | 否 | FSTR SFT + 结果/过程 RL；Checker 仅用于训练，任务输出包括类别与定位。 |
| **[FakeHunter](../README_CN.md#fakehunter)** | 音视频 · 篡改检测<br><sub>输出：检⁠测 · 解⁠释</sub> | Qwen2.5-Omni-7B<br><sub>另评测备选模型：MiniCPM-o-2_6</sub><br><sub>工具：CLIP + CLAP 编码器；FAISS 检索记忆</sub> | 是 | 智能体不微调；在训练集 CLIP/CLAP 嵌入上用 K-means 拟合检索记忆。 |

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

“组织”指推理阶段；“训练”指智能体适配，不代表底层工具未经预训练。工具未注明代码生成时均为预定义接口。

<a name="visual"></a>

### 视觉（图像与视频）

| 方法 | 智能体组织 | 工具接口 | 反馈后改变什么？ | 智能体训练 | 证据输出 |
| --- | --- | --- | --- | --- | --- |
| **[ATAR](../README_CN.md#atar)** | 单智能体 | 预定义裁剪 + 22 个取证工具 | 选择下一次裁剪/工具或停止 | SFT + GRPO；工具先验课程 | 判定 + 区域描述；Grounded-SAM 掩码 |
| **[ForenAgent](../README_CN.md#forenagent)** | 单智能体 | 生成处理代码 + 12 个固定取证工具 | 依据工具输出调整操作/裁剪 | SFT + GRPO | 判定 + 推理说明 + 工具可视化 |
| **[SafeGuard](../README_CN.md#safeguard)** | 感知求解器 + 验证器 | 预定义定位 + 四类取证工具 | 修订假设并重新采证（≤3 轮） | 智能体不微调；取证工具经调优 | 判定 + 置信度 + 局部证据 |
| **[Defake-o3](../README_CN.md#defake-o3)** | 单智能体 | 预定义 Zoom In | 选择继续裁剪或最终判定 | SFT + GRPO；验证器用于奖励 | 判定 + 全局描述；可选框/局部描述 |
| **[Hermes](../README_CN.md#hermes)** | 规划者 + 推理者 + 三角色讨论 | RAG 选择的问答检查 + 视觉工具 | 调用工具追加证据并修订图（≤3 轮） | 无任务专用智能体训练 | 判定/评分 + 时序证据图 |
| **[UniShield](../README_CN.md#unishield)** | 感知 → 检测 → 报告 | 预定义 8 检测器工具箱 | 每图单检测器；不回溯 | GRPO 任务路由器；提示词调度 | 判定 + 报告；按任务输出掩码 |
| **[AgentFoX](../README_CN.md#agentfox)** | 单推理核心 + 专家工具 | 预定义专家 + 可靠性档案 | 基于已采集证据调整融合/报告 | 未描述核心微调；拟合校准参数 | 判定 + 置信度 + 证据报告 |
| **[EvoGuard](../README_CN.md#evoguard)** | 单调度智能体 | 检测器 API + 能力档案 | 补充调用检测器或停止 | GRPO；检测器冻结 | 判定 + 多工具分析 |
| **[ForgeryVCR](../README_CN.md#forgeryvcr)** | 单智能体 | ELA / NoisePrint++ / FFT / 放大 | 依据视觉输出继续调用工具/定位 | SFT + GRPO | 判定 + 框 → SAM2 掩码 |
| **[AIFo](../README_CN.md#aifo)** | 采集者 / 推理者 / 辩手 / 裁判 | 检索 / 元数据 / 分类器 / VLM | 围绕已有证据辩论；裁判终止 | 提示词智能体；无权重训练 | 判定 + 溯源/元数据 + 理由 |

<a name="cross-modal"></a>

### 跨模态

| 方法 | 智能体组织 | 工具接口 | 反馈后改变什么？ | 智能体训练 | 证据输出 |
| --- | --- | --- | --- | --- | --- |
| **[OmniVL-Guard Pro](../README_CN.md#omnivl-guard-pro)** | 单推理策略 | 预定义检索 / 裁剪 / 视觉 / SAM3 | 依据观测/错误选择后续工具 | SFT + 结果 RL + Checker 引导过程 RL | 判定 + 轨迹 + 空间/文本/时序定位 |
| **[FakeHunter](../README_CN.md#fakehunter)** | 单提示词多模态模型 | 记忆检索 / 放大 / 梅尔频谱 | 低置信度触发视觉/音频复核 | 智能体不微调；训练集构建记忆 | 判定 + 篡改类型 + 解释 |

