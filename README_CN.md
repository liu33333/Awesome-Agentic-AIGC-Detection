![Evidence, tools, and adaptive investigation](assets/banner.svg)

# Awesome Agentic AIGC Detection

[English](README.md) | [简体中文](README_CN.md)

循证整理智能体检测 AI 生成图像与视频的机制。

[![Papers: 12](https://img.shields.io/badge/papers-12-0f766e?style=flat-square)](#feedback-loops) [![Languages: EN / 中文](https://img.shields.io/badge/languages-EN%20%2F%20中文-334155?style=flat-square)](README_CN.md)

[范围与阅读方式](#scope) · [覆盖 AIGC 的反馈循环](#feedback-loops) · [相关篡改取证](#related-forensics) · [限定流程中的自适应](#bounded-workflows) · [参与维护](#contributing)

<a id="scope"></a>

## 范围与阅读方式

聚焦生成图像与视频检测；局部编辑、人脸操纵、音频篡改和事实核查均明确标为相关任务。描述以所引论文为依据，不代表独立性能验证，也不是排行榜或复现项目。

<details>
<summary>清单如何组织</summary>

阅读时关注**什么会调整、在何时调整、面向什么任务**：选择检测器、观察局部区域、执行取证代码，或根据新证据调整判断。

当前收录 **12 篇论文**，按三个阅读入口组织（7 / 2 / 3）：

- **覆盖 AIGC 的反馈循环：**推理时，观测结果或验证反馈可以改变后续行动。
- **相关篡改取证：**相邻任务中的智能体机制；收录并不代表论文覆盖完整生成内容。
- **限定流程中的自适应：**通过辩论、档案查询或初始路由调整流程，不据此推断存在任意工具重规划。

这些是互补的阅读标签，不是质量分级。任务范围与控制流程是两个维度：篡改检测可以有反馈循环，AIGC 检测也可以使用限定流程。仅有最大步数限制，并不意味着属于这里所说的“限定流程”。

**证据标准：**机制描述来自所引论文，不代表独立验证了性能。这是一份选择性文献地图，不是排行榜或复现项目。方法名包含“Agent”、使用推理或调用多个模型，本身不足以证明存在测试时的证据—行动循环。训练阶段的迭代与推理阶段的反馈分开记录。

</details>

<a id="feedback-loops"></a>

## 覆盖 AIGC 的反馈循环

### [EvoGuard](https://arxiv.org/abs/2603.17343)

`图像` · **任务范围：** 生成图像

按能力档案选择检测工具；根据返回结果决定追加调用或结束。

<details>
<summary>论文依据</summary>

§3.2–3.3；图 2

</details>

### [Defake-o3](https://arxiv.org/abs/2608.16259)

`图像` · **任务范围：** 生成图像

观察当前图像或裁剪区域后，选择继续裁剪或输出结论。Evidence Verifier 用于训练奖励；推理时的循环是视觉搜索。

<details>
<summary>论文依据</summary>

§4.1–4.4；图 3

</details>

### [ForenAgent](https://arxiv.org/abs/2512.16300)，*Code-in-the-Loop Forensics*

`图像` · **任务范围：** 完整合成图像，兼及**相关局部编辑**

生成并执行 Python，利用返回的文本和视觉结果继续编写代码与推理。

<details>
<summary>论文依据</summary>

§3.2

</details>

### [ATAR](https://arxiv.org/abs/2609.39066)，*Agentic Tool-Augmented Reasoning*

`图像` · **任务范围：** 包含 AIGC 的混合图像取证；兼及**编辑、人脸和文档篡改**

在裁剪、22 种取证工具与输出决策之间切换，工具结果进入下一轮上下文。

<details>
<summary>论文依据</summary>

§3.1；图 2

</details>

### [OmniVL-Guard Pro](https://arxiv.org/abs/2605.16962)

`图像 / 视频` · **任务范围：** 混合媒体取证中的生成图像/视频；兼及**定位与事实核查**

利用已返回的观测选择后续工具及参数，包括裁剪、视频帧提取与搜索。Checker 引导训练是另一个组成部分。

<details>
<summary>论文依据</summary>

§2；附录 E；§4（训练）

</details>

### [SafeGuard](https://arxiv.org/abs/2607.03069)

`视频` · **任务范围：** 生成视频，侧重社会风险场景

验证器检查证据与假设的一致性；可靠性不足时修改假设，重新执行感知—推理循环。

<details>
<summary>论文依据</summary>

§3.2；图 2

</details>

### [Hermes](https://proceedings.mlr.press/v306/li26be.html)

`视频` · **任务范围：** 生成视频

检索针对当前视频的取证计划，构建证据图，再通过调用工具的多智能体讨论重新检查不确定证据；证据图修订与补充证据请求决定是否继续下一轮。

<details>
<summary>论文依据</summary>

§3.1–3.3；图 2–3。[论文 PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/li26be/li26be.pdf)

§3.3 描述了调用工具的讨论过程，以及超出初始计划的证据空间扩展。修订后的证据图进入下一轮；没有被接受的修订且不再需要更多证据，或达到轮数上限时结束。

</details>

<a id="related-forensics"></a>

## 相关篡改取证

### [ForgeryVCR](https://arxiv.org/abs/2602.14098)

`相关任务` · **任务范围：** **相关任务：**图像篡改检测与定位

按需调用取证变换和局部放大，将视觉工具输出加入推理上下文，再完成定位。

<details>
<summary>论文依据</summary>

§3.1–3.2；图 2

</details>

### [FakeHunter](https://arxiv.org/abs/2508.14581)，*Memory-Anchored Multimodal Reasoning for Explainable Video Forensics*

`相关任务` · **任务范围：** **相关任务：**视频与音频篡改

检索案例辅助推理；低置信度触发视觉/音频工具后再综合判断。该条件验证阶段不等同于任意工具重规划。

<details>
<summary>论文依据</summary>

“Tool-Augmented Verification” 小节

</details>

FakeHunter 使用框架名索引，上方列出链接论文的当前标题。标题与机制可能随论文版本变化。

<a id="bounded-workflows"></a>

## 限定流程中的自适应

### [AIFo](https://arxiv.org/abs/2511.00181)，*From Evidence to Verdict*

`图像` · **任务范围：** 生成图像

先执行初始工具集合；证据不足或冲突时触发辩论。辩论与结束条件自适应，所述核心流程不重新规划证据采集。

<details>
<summary>论文依据</summary>

“The AIFo Framework” 的 Overview；图 1

</details>

### [AgentFoX](https://arxiv.org/abs/2603.23115)

`图像` · **任务范围：** 生成图像

初始阶段查询全部专家；出现冲突后查询上下文可靠性/档案。应区分证据解释的自适应与重新选择检测器调用序列。

<details>
<summary>论文依据</summary>

§3.2，阶段 2–3；图 3

</details>

### [UniShield](https://arxiv.org/abs/2510.03161)

`图像` · **任务范围：** 生成图像，兼及**人脸、局部图像和文档篡改**

为输入路由选择一个检测器，再汇总结果；所述流程明确避免回溯与多工具协同。

<details>
<summary>论文依据</summary>

Methodology 的 Overview；图 2

</details>

<a id="contributing"></a>

## 参与维护

[推荐论文](https://github.com/liu33333/Awesome-Agentic-AIGC-Detection/issues/new?template=paper_suggestion.md) · [报告纠错](https://github.com/liu33333/Awesome-Agentic-AIGC-Detection/issues/new?template=correction.md)

欢迎通过 issue 或 pull request 补充论文、修正机制描述或澄清任务边界。请提供论文链接，以及支持描述的章节、图或算法位置。小而有据的修改尤其有帮助。详见 [CONTRIBUTING.md](CONTRIBUTING.md)。

无需重跑实验或提交性能排名。链接指向原始工作；收录不代表认可某方法适合用于高后果决策。
