# Awesome Agentic AIGC Detection

[English](README.md) | [简体中文](README_CN.md)

A focused reading list on agents that investigate AI-generated images and videos: selecting detectors, inspecting regions, executing forensic code, and revisiting conclusions with new evidence.

The aim is to make **what adapts, when it adapts, and which task it addresses** easy to find. Start with the mechanism that interests you, then follow the paper and evidence pointer. Suggestions and corrections are welcome.

## Scope and reading guide

The main focus is generated-image and generated-video detection. Local image editing, face manipulation, audio manipulation, and factual verification are related tasks, explicitly marked below rather than treated as equivalent to full-content generation detection.

Three browsing groups organize this initial collection:

- **AIGC-capable feedback loops:** observations or verifier feedback can change subsequent inference actions.
- **Related manipulation forensics:** useful agent mechanisms in adjacent tasks; their inclusion does not establish coverage of fully generated media.
- **Bounded adaptive workflows:** adaptation through debate, profile lookup, or initial routing, without assuming unrestricted tool replanning.

These are complementary browsing labels, not a quality hierarchy. Task scope and control flow are separate dimensions: a manipulation-focused method can have a feedback loop, and an AIGC detector can use a bounded workflow. A finite step budget does not itself make a method “bounded” in the narrower workflow sense used here.

**Evidence standard:** descriptions reflect the cited papers, not independent performance validation. This is a selective literature map, not a leaderboard or reproduction suite. “Agent,” “reasoning,” and multiple model calls alone do not establish a test-time evidence–action loop. Training-time refinement is recorded separately from inference behavior.

## AIGC-capable feedback loops

| Method / paper | Task scope | Inference mechanism | Where to read |
| --- | --- | --- | --- |
| [EvoGuard](https://arxiv.org/abs/2603.17343) | Generated images | Selects detector tools using capability profiles; returned results guide additional calls or stopping. | §3.2–3.3; Fig. 2 |
| [Defake-o3](https://arxiv.org/abs/2608.16259) | Generated images | Chooses another crop or a final output after observing the current image/patch. Its Evidence Verifier supplies training rewards; the inference loop is visual search. | §4.1–4.4; Fig. 3 |
| [ForenAgent](https://arxiv.org/abs/2512.16300), *Code-in-the-Loop Forensics* | Fully synthetic images **and related local editing** | Generates and executes Python; returned text and visual outputs inform further code and reasoning. | §3.2 |
| [ATAR](https://arxiv.org/abs/2609.39066), *Agentic Tool-Augmented Reasoning* | Mixed image forensics, including AIGC; **related editing, face and document manipulation** | Alternates crops, a 22-tool forensic library, and decisions; tool outputs feed the next turn. | §3.1; Fig. 2 |
| [OmniVL-Guard Pro](https://arxiv.org/abs/2605.16962) | Generated images/videos within mixed media forensics; **related localization and factual verification** | Uses returned observations to select subsequent tools and parameters, including crops, frame extraction, and search. Checker-guided training is a separate component. | §2; Appendix E; §4 (training) |
| [SafeGuard](https://arxiv.org/abs/2607.03069) | Generated videos, with a social-risk focus | A verifier checks evidence against hypotheses; low reliability triggers hypothesis revision and another perception–reasoning cycle. | §3.2; Fig. 2 |

## Related manipulation forensics

| Method / paper | Task scope | Inference mechanism | Where to read |
| --- | --- | --- | --- |
| [ForgeryVCR](https://arxiv.org/abs/2602.14098) | **Related:** image manipulation detection and localization | Selectively invokes forensic transforms and local zoom; visual tool outputs enter the reasoning context before localization. | §3.1–3.2; Fig. 2 |
| [FakeHunter](https://arxiv.org/abs/2508.14581), *Memory-Anchored Multimodal Reasoning for Explainable Video Forensics* | **Related:** video and audio manipulation | Retrieved examples support reasoning; low confidence triggers visual/audio tools before a final synthesis. This conditional verification stage should not be equated with unrestricted replanning. | “Tool-Augmented Verification” section |

FakeHunter is listed under its framework name; the linked paper's current title is shown above. Paper titles and mechanisms may change between versions.

## Bounded adaptive workflows

| Method / paper | Task scope | What adapts, and its boundary | Where to read |
| --- | --- | --- | --- |
| [AIFo](https://arxiv.org/abs/2511.00181), *From Evidence to Verdict* | Generated images | Executes the initial tool set, then conditionally debates conflicting or insufficient evidence. Debate and stopping adapt; the described core does not replan evidence acquisition. | “The AIFo Framework”: Overview; Fig. 1 |
| [AgentFoX](https://arxiv.org/abs/2603.23115) | Generated images | Initially queries each expert; conflict triggers contextual reliability/profile consultation. Distinguish adaptive evidence interpretation from choosing a fresh sequence of detectors. | §3.2, Stages 2–3; Fig. 3 |
| [UniShield](https://arxiv.org/abs/2510.03161) | Generated images **and related face, local-image and document manipulation** | Routes an image to one detector and summarizes its output. The described workflow intentionally avoids backtracking and multi-tool collaboration. | Methodology: Overview; Fig. 2 |

## Further reading

- [Hermes](https://proceedings.mlr.press/v306/li26be.html): pending detailed mechanism review. Kept outside the 11-entry categorized collection until its inference control flow and task scope have been documented with primary-source evidence.

## Contributing

Add a paper, correct a mechanism description, or clarify a boundary through an issue or pull request. Please include a paper link and the section, figure, or algorithm supporting the proposed description. Small, evidence-backed changes are especially useful. See [CONTRIBUTING.md](CONTRIBUTING.md).

No experiment reruns or performance rankings are required. Links point to the original works; inclusion is not an endorsement of a method's reliability for consequential decisions.
