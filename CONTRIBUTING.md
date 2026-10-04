# Contributing / 参与贡献

[English](#english) · [简体中文](#简体中文)

<a id="english"></a>

Contributions can add papers or correct publication details, links, and method descriptions.

## Propose a paper or correction

Open an issue or pull request with:

1. **Paper:** full title, stable primary-source link, and the version you read. Include publication status, venue, year, and a supporting proceedings, publisher, conference, or author announcement link; identify Findings and workshop tracks explicitly.
2. **Input modality and task scope:** audio, visual (images/videos), text, or cross-modal evidence; then distinguish generated-content detection from related tasks such as local editing, face manipulation, audio manipulation, or factual verification. Classify by the evidence examined, not the model name or a text instruction supplied to a VLM.
3. **Technical comparison:** agent organization, tool interface, what changes after feedback, training of the agent, and evidence output. Support each field with a source location. Distinguish more evidence acquisition from debate over existing evidence; mark unclear fields as not verified.
4. **Evidence:** the supporting section, figure, algorithm, or short source passage. Paraphrase in the README; do not copy abstracts.
5. **Table placement and date:** choose the input-modality section and insert the paper in descending date order. Published papers use the conference opening date; preprints and accepted papers without verified proceedings publication use the first arXiv submission date. Include the date source in your contribution and keep status explicit. The README links the full paper title once; venue and date remain plain text. Add a separate repository link only for a verified official repository.

Example submission:

- Paper and version: …
- Venue, year, status, and source: …
- Input modality and task scope: …
- Agent organization / tools / feedback-driven action / training / evidence output: …
- Official repository and authorship evidence: …
- Sorting date and source: …
- Observed evidence → next decision → possible action: …
- Evidence location: §… / Fig. … / Algorithm …
- What remains fixed or unclear: …
- Proposed table row (full linked title first): …

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
- [ ] Input modality, date source, descending order, task scope, and technical comparison fields are checked.
- [ ] There is one paper link per entry; any separate repository is verified as official.
- [ ] Training behavior is not presented as inference behavior.
- [ ] The change contains no unsupported performance claim.
- [ ] Both language versions are updated, or the missing translation is noted.

Please submit links and original summaries rather than uploading third-party papers or copyrighted figures. Paper and code licenses remain those of their respective owners.

## 简体中文

欢迎补充论文、修正链接或澄清某一步推理机制。可以用中文或英文提交；尚未同步的翻译请注明。

### 推荐论文或纠错

请通过 issue 或 pull request 提供：

1. **论文信息：**完整标题、稳定的一手来源链接，以及阅读的版本；注明发表状态、会议或期刊、年份，并附论文集、出版社、会议或作者公告的依据链接。Findings 和 workshop 必须明确标注。
2. **输入模态与任务范围：**按实际分析的证据归入音频、视觉（图像/视频）、文本或跨模态；再区分生成内容检测与局部编辑、人脸操纵、音频篡改、事实核查等相关任务。模型名称或提供给 VLM 的文字指令不构成跨模态归类依据。
3. **技术对比：**提供智能体组织、工具接口、反馈后改变的行动、智能体训练方式及证据输出，每项附具体依据。区分追加证据采集与围绕已有证据的讨论；不清楚的字段标为未核实。
4. **证据位置：**支持描述的章节、图、算法或简短原文。在 README 中请使用自己的概括，不要复制摘要。
5. **表格位置与日期：**选择输入模态章节，按日期倒序插入。已发表论文使用会议开幕日期；预印本及尚未核实正式出版的已录用论文使用 arXiv 首次提交日期。在贡献说明中附日期来源，并明确标注状态。README 中完整论文标题仅链接一次，发表位置与日期使用纯文本；另设仓库链接，仅收录已核实的官方仓库。

可参考以下格式：

- 论文及版本：…
- 会议或期刊、年份、状态及依据：…
- 输入模态与任务范围：…
- 智能体组织 / 工具 / 反馈后行动 / 训练 / 证据输出：…
- 官方仓库及归属依据：…
- 排序日期及来源：…
- 已观察证据 → 下一步决策 → 可能行动：…
- 证据位置：§… / 图 … / 算法 …
- 固定部分或待核实之处：…
- 建议表格行（完整论文标题及链接放在第一列）：…

### 编辑原则

- 描述机制，而非宣传标签。工具调用、多智能体和思维链本身不等于自适应证据采集。
- 将训练时的搜索、奖励计算和数据生成，与测试时行动区分开。
- 区分条件验证、档案查询和基于新观测的反复工具选择。
- 分类只用于导航，不是质量分级；调整归类不代表方法优劣。
- 优先引用原始论文和官方项目。添加仓库链接前，核实其确实属于该论文。
- 不添加无依据的“首个”“最佳”或全覆盖声明；不要求跑榜、性能排名或重跑实验。
- 保持简洁、中立。有争议的描述应注明论文版本与依据；机制尚不明确的工作可先保持讨论，待证据清楚后再收录。
- 尽量同步 README.md 与 README_CN.md；仅提交一种语言时，请注明待补翻译。

### 提交前检查

- [ ] 论文没有以其他标题或框架名重复收录。
- [ ] 一手链接可打开，标题与版本对应。
- [ ] 发表状态与会议或期刊有来源支持；仅有 arXiv 记录不代表已录用。
- [ ] 已核对输入模态、日期来源、倒序排列、任务范围及技术对比字段。
- [ ] 每篇论文仅有一个论文链接；单独列出的仓库已核实为官方仓库。
- [ ] 没有把训练行为写成推理行为。
- [ ] 没有无依据的性能声明。
- [ ] 两种语言已同步，或已注明待补翻译。

请提交链接与原创概括，不要上传第三方论文全文或受版权保护的图片。论文和代码的许可由各自权利人决定。
