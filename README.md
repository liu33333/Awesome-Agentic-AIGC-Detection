![Evidence, tools, and adaptive investigation](assets/banner.svg)

# Awesome Agentic AIGC Detection

[English](README.md) | [简体中文](README_CN.md)

An evidence-led guide to agentic detection of AI-generated images and videos.

[![Papers: 12](https://img.shields.io/badge/papers-12-0f766e?style=flat-square)](#feedback-loops) [![Languages: EN / 中文](https://img.shields.io/badge/languages-EN%20%2F%20中文-334155?style=flat-square)](README_CN.md)

[Scope and reading guide](#scope) · [AIGC-capable feedback loops](#feedback-loops) · [Related manipulation forensics](#related-forensics) · [Bounded adaptive workflows](#bounded-workflows) · [Contributing](#contributing)

<a id="scope"></a>

## Scope and reading guide

Focused on generated-image and generated-video detection, with local editing, face manipulation, audio manipulation, and factual verification explicitly marked as related tasks. Descriptions follow the cited papers; this is not independent performance validation, a leaderboard, or a reproduction suite.

<details>
<summary>How this list is organized</summary>

Follow **what adapts, when it adapts, and which task it addresses**: selecting detectors, inspecting regions, executing forensic code, or revisiting conclusions with new evidence.

**12 papers**, organized into three browsing groups (7 / 2 / 3):

- **AIGC-capable feedback loops:** observations or verifier feedback can change subsequent inference actions.
- **Related manipulation forensics:** useful agent mechanisms in adjacent tasks; their inclusion does not establish coverage of fully generated media.
- **Bounded adaptive workflows:** adaptation through debate, profile lookup, or initial routing, without assuming unrestricted tool replanning.

These are complementary browsing labels, not a quality hierarchy. Task scope and control flow are separate dimensions: a manipulation-focused method can have a feedback loop, and an AIGC detector can use a bounded workflow. A finite step budget does not itself make a method “bounded” in the narrower workflow sense used here.

**Evidence standard:** descriptions reflect the cited papers, not independent performance validation. This is a selective literature map, not a leaderboard or reproduction suite. “Agent,” “reasoning,” and multiple model calls alone do not establish a test-time evidence–action loop. Training-time refinement is recorded separately from inference behavior.

</details>

<a id="feedback-loops"></a>

## AIGC-capable feedback loops

### [EvoGuard](https://arxiv.org/abs/2603.17343)

`Images` · **Scope:** Generated images

Selects detector tools using capability profiles; returned results guide additional calls or stopping.

<details>
<summary>Evidence pointer</summary>

§3.2–3.3; Fig. 2

</details>

### [Defake-o3](https://arxiv.org/abs/2608.16259)

`Images` · **Scope:** Generated images

Chooses another crop or a final output after observing the current image/patch. Its Evidence Verifier supplies training rewards; the inference loop is visual search.

<details>
<summary>Evidence pointer</summary>

§4.1–4.4; Fig. 3

</details>

### [ForenAgent](https://arxiv.org/abs/2512.16300), *Code-in-the-Loop Forensics*

`Images` · **Scope:** Fully synthetic images **and related local editing**

Generates and executes Python; returned text and visual outputs inform further code and reasoning.

<details>
<summary>Evidence pointer</summary>

§3.2

</details>

### [ATAR](https://arxiv.org/abs/2609.39066), *Agentic Tool-Augmented Reasoning*

`Images` · **Scope:** Mixed image forensics, including AIGC; **related editing, face and document manipulation**

Alternates crops, a 22-tool forensic library, and decisions; tool outputs feed the next turn.

<details>
<summary>Evidence pointer</summary>

§3.1; Fig. 2

</details>

### [OmniVL-Guard Pro](https://arxiv.org/abs/2605.16962)

`Images / videos` · **Scope:** Generated images/videos within mixed media forensics; **related localization and factual verification**

Uses returned observations to select subsequent tools and parameters, including crops, frame extraction, and search. Checker-guided training is a separate component.

<details>
<summary>Evidence pointer</summary>

§2; Appendix E; §4 (training)

</details>

### [SafeGuard](https://arxiv.org/abs/2607.03069)

`Video` · **Scope:** Generated videos, with a social-risk focus

A verifier checks evidence against hypotheses; low reliability triggers hypothesis revision and another perception–reasoning cycle.

<details>
<summary>Evidence pointer</summary>

§3.2; Fig. 2

</details>

### [Hermes](https://proceedings.mlr.press/v306/li26be.html)

`Video` · **Scope:** Generated videos

Retrieves a video-specific forensic plan, builds an evidence graph, then revisits uncertain evidence with tool-assisted multi-agent deliberation; graph revisions and requests for more evidence control further rounds.

<details>
<summary>Evidence pointer</summary>

§3.1–3.3; Figs. 2–3. [Paper PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/li26be/li26be.pdf)

§3.3 describes tool-assisted deliberation and evidence-space expansion beyond the initial plan. The revised evidence graph feeds the next round; the loop stops when no revision is accepted and no more evidence is requested, or the round limit is reached.

</details>

<a id="related-forensics"></a>

## Related manipulation forensics

### [ForgeryVCR](https://arxiv.org/abs/2602.14098)

`Related task` · **Scope:** **Related:** image manipulation detection and localization

Selectively invokes forensic transforms and local zoom; visual tool outputs enter the reasoning context before localization.

<details>
<summary>Evidence pointer</summary>

§3.1–3.2; Fig. 2

</details>

### [FakeHunter](https://arxiv.org/abs/2508.14581), *Memory-Anchored Multimodal Reasoning for Explainable Video Forensics*

`Related task` · **Scope:** **Related:** video and audio manipulation

Retrieved examples support reasoning; low confidence triggers visual/audio tools before a final synthesis. This conditional verification stage should not be equated with unrestricted replanning.

<details>
<summary>Evidence pointer</summary>

“Tool-Augmented Verification” section

</details>

FakeHunter is listed under its framework name; the linked paper's current title is shown above. Paper titles and mechanisms may change between versions.

<a id="bounded-workflows"></a>

## Bounded adaptive workflows

### [AIFo](https://arxiv.org/abs/2511.00181), *From Evidence to Verdict*

`Images` · **Scope:** Generated images

Executes the initial tool set, then conditionally debates conflicting or insufficient evidence. Debate and stopping adapt; the described core does not replan evidence acquisition.

<details>
<summary>Evidence pointer</summary>

“The AIFo Framework”: Overview; Fig. 1

</details>

### [AgentFoX](https://arxiv.org/abs/2603.23115)

`Images` · **Scope:** Generated images

Initially queries each expert; conflict triggers contextual reliability/profile consultation. Distinguish adaptive evidence interpretation from choosing a fresh sequence of detectors.

<details>
<summary>Evidence pointer</summary>

§3.2, Stages 2–3; Fig. 3

</details>

### [UniShield](https://arxiv.org/abs/2510.03161)

`Images` · **Scope:** Generated images **and related face, local-image and document manipulation**

Routes an image to one detector and summarizes its output. The described workflow intentionally avoids backtracking and multi-tool collaboration.

<details>
<summary>Evidence pointer</summary>

Methodology: Overview; Fig. 2

</details>

<a id="contributing"></a>

## Contributing

[Suggest a paper](https://github.com/liu33333/Awesome-Agentic-AIGC-Detection/issues/new?template=paper_suggestion.md) · [Report a correction](https://github.com/liu33333/Awesome-Agentic-AIGC-Detection/issues/new?template=correction.md)

Add a paper, correct a mechanism description, or clarify a boundary through an issue or pull request. Please include a paper link and the section, figure, or algorithm supporting the proposed description. Small, evidence-backed changes are especially useful. See [CONTRIBUTING.md](CONTRIBUTING.md).

No experiment reruns or performance rankings are required. Links point to the original works; inclusion is not an endorsement of a method's reliability for consequential decisions.
