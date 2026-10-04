# Contributing / 参与贡献

[English](#english) · [简体中文](#简体中文)

<a id="english"></a>

Contributions can add papers or correct publication details, links, and method descriptions.

## Propose a paper or correction

Open an issue or pull request with:

1. **Paper:** full title, stable primary-source link, and the version you read. Include publication status, venue, year, and a supporting proceedings, publisher, conference, or author announcement link; identify Findings and workshop tracks explicitly.
2. **Task scope:** generated image/video detection, or a clearly identified related task such as local editing, face manipulation, audio manipulation, or factual verification.
3. **Inference mechanism:** what is observed, which decision follows, and what action can change. Note fixed tool calls and stopping conditions when relevant.
4. **Evidence:** the supporting section, figure, algorithm, or short source passage. Paraphrase in the README; do not copy abstracts.
5. **Suggested placement:** published/accepted papers or preprints, followed by an optional method-index tag. Keep papers under preprints when formal publication or acceptance has not been verified.

Example submission:

- Paper and version: …
- Venue, year, status, and source: …
- Scope: …
- Observed evidence → next decision → possible action: …
- Evidence location: §… / Fig. … / Algorithm …
- What remains fixed or unclear: …
- Proposed one-sentence entry: …

## Editorial principles

- Describe the mechanism, not the marketing label. Tool use, multiple agents, and chain-of-thought do not by themselves prove adaptive evidence acquisition.
- Separate training-time search, reward computation, and data generation from test-time actions.
- Distinguish conditional verification and profile lookup from repeated tool selection after new observations.
- Treat categories as navigation aids, not quality tiers. Corrections can change placement without implying that a method is better or worse.
- Prefer primary papers and official project links. Check that code belongs to the listed paper before adding a repository link.
- Do not add unsupported “first,” “best,” or exhaustive-coverage claims. We do not require benchmarks, rankings, or experiment reruns.
- Keep entries short and neutral. If a claim is disputed, cite the relevant paper version and evidence; papers with unresolved mechanisms can stay under discussion until the evidence is clear.
- Keep README.md and README_CN.md aligned where practical. A contribution in either language is welcome; flag any translation still needed.

## Before submitting

- [ ] The paper is not already listed under another title or framework name.
- [ ] The primary link opens and the title/version match.
- [ ] Publication status and venue have a source; an arXiv posting alone is not evidence of acceptance.
- [ ] Scope and inference behavior are supported by a specific source location.
- [ ] Training behavior is not presented as inference behavior.
- [ ] The change contains no unsupported performance claim.
- [ ] Both language versions are updated, or the missing translation is noted.

Please submit links and original summaries rather than uploading third-party papers or copyrighted figures. Paper and code licenses remain those of their respective owners.

## 简体中文

欢迎补充论文、修正链接或澄清某一步推理机制。可以用中文或英文提交；尚未同步的翻译请注明。

### 推荐论文或纠错

请通过 issue 或 pull request 提供：

1. **论文信息：**完整标题、稳定的一手来源链接，以及阅读的版本；注明发表状态、会议或期刊、年份，并附论文集、出版社、会议或作者公告的依据链接。Findings 和 workshop 必须明确标注。
2. **任务范围：**生成图像/视频检测，或明确标注的局部编辑、人脸操纵、音频篡改、事实核查等相关任务。
3. **推理机制：**观察到了什么，接下来作出什么决策，哪些行动可以改变；必要时说明固定工具调用和结束条件。
4. **证据位置：**支持描述的章节、图、算法或简短原文。在 README 中请使用自己的概括，不要复制摘要。
5. **建议位置：**已发表/已录用论文或预印本，可补充方法索引标签。正式发表或录用信息尚未核实的论文保留在预印本部分。

可参考以下格式：

- 论文及版本：…
- 会议或期刊、年份、状态及依据：…
- 任务范围：…
- 已观察证据 → 下一步决策 → 可能行动：…
- 证据位置：§… / 图 … / 算法 …
- 固定部分或待核实之处：…
- 建议的一句话描述：…

### 编辑原则

- 描述机制，而非宣传标签。工具调用、多智能体和思维链本身不等于自适应证据采集。
- 将训练时的搜索、奖励计算和数据生成，与测试时行动区分开。
- 区分条件验证、档案查询和基于新观测的反复工具选择。
- 分类只用于导航，不是质量分级；调整归类不代表方法优劣。
- 优先引用原始论文和官方项目。添加代码链接前，核实其确实属于该论文。
- 不添加无依据的“首个”“最佳”或全覆盖声明；不要求跑榜、性能排名或重跑实验。
- 保持简洁、中立。有争议的描述应注明论文版本与依据；机制尚不明确的工作可先保持讨论，待证据清楚后再收录。
- 尽量同步 README.md 与 README_CN.md；仅提交一种语言时，请注明待补翻译。

### 提交前检查

- [ ] 论文没有以其他标题或框架名重复收录。
- [ ] 一手链接可打开，标题与版本对应。
- [ ] 发表状态与会议或期刊有来源支持；仅有 arXiv 记录不代表已录用。
- [ ] 任务范围和推理行为有具体来源支持。
- [ ] 没有把训练行为写成推理行为。
- [ ] 没有无依据的性能声明。
- [ ] 两种语言已同步，或已注明待补翻译。

请提交链接与原创概括，不要上传第三方论文全文或受版权保护的图片。论文和代码的许可由各自权利人决定。
