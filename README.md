# Awesome Agentic AIGC Detection

[English](README.md) | [简体中文](README_CN.md)

Papers on agentic detection of AI-generated images and videos, with related manipulation-forensics tasks marked separately.

## Contents

- [Published / accepted papers](#published-accepted)
  - [2026](#published-2026)
- [Preprints](#preprints)
  - [2026](#preprints-2026)
  - [2025](#preprints-2025)
- [Method index](#method-index)
- [Contributing](#contributing)

<a id="published-accepted"></a>

## Published / accepted papers

Publication and acceptance records checked on **2026-10-04**; venue links point to proceedings or acceptance evidence, with Findings labeled explicitly.

<a id="published-2026"></a>

### 2026

<a id="hermes"></a>

**[ICML 2026 · published](https://proceedings.mlr.press/v306/li26be.html)** [Hermes: An Evidence-Driven Agentic Framework for Trustworthy and Explainable AI-Generated Video Detection](https://proceedings.mlr.press/v306/li26be.html)

For generated-video detection, retrieves a forensic plan and uses tool-assisted multi-agent deliberation to revise an evidence graph and request further evidence.

<a id="forenagent"></a>

**[ECCV 2026 · published](https://link.springer.com/chapter/10.1007/978-3-032-37592-6_12)** [Code-in-the-Loop Forensics: Agentic Tool Use for Image Forgery Detection](https://arxiv.org/abs/2512.16300) (ForenAgent)

For synthetic images and local edits, generates and executes Python, using returned text and visual results to guide further analysis.

<a id="safeguard"></a>

**[ECCV 2026 · published](https://link.springer.com/chapter/10.1007/978-3-032-37029-7_33)** [SafeGuard: A Multi-Agent Perception-Reasoning Framework for Social-Risk AI-Generated Video Detection](https://arxiv.org/abs/2607.03069)

For generated videos with social risks, checks evidence against hypotheses and repeats perception and reasoning when the verifier finds insufficient support.

<a id="unishield"></a>

**[CVPR Findings 2026 · published](https://openaccess.thecvf.com/content/CVPR2026F/html/Huang_UniShield_An_Adaptive_Multi-Agent_Framework_for_Unified_Forgery_Image_Detection_CVPRF_2026_paper.html)** [UniShield: An Adaptive Multi-Agent Framework for Unified Forgery Image Detection and Localization](https://arxiv.org/abs/2510.03161)

For generated images and related face, local-image and document manipulation, routes each image to one detector and summarizes its output without backtracking or multi-tool collaboration.

<a id="defake-o3"></a>

**[ACM Multimedia 2026 · accepted](https://arxiv.org/abs/2608.16259)** [Defake-o3: From Speculative Rationales to Verifiable Evidence for Explainable AIGI Detection](https://arxiv.org/abs/2608.16259)

For generated-image detection, adaptively inspects crops before deciding; its Evidence Verifier provides training rewards rather than test-time verification.

<a id="atar"></a>

**[ACM Multimedia 2026 · Oral · accepted](https://arxiv.org/abs/2609.39066)** [Agentic Tool-Augmented Reasoning for Explainable Image Forgery Detection](https://arxiv.org/abs/2609.39066) (ATAR)

For AIGC detection and related image, face and document manipulation, alternates crops and forensic tools according to returned results.

<a id="forgeryvcr"></a>

**[ACM Multimedia 2026 · Oral · accepted](https://github.com/youqiwong/ForgeryVCR)** [ForgeryVCR: Visual-Centric Reasoning via Efficient Forensic Tools in MLLMs for Image Forgery Detection and Localization](https://arxiv.org/abs/2602.14098)

For image-manipulation detection and localization, selectively applies forensic transforms and local zoom, feeding the visual outputs into subsequent reasoning.

<a id="preprints"></a>

## Preprints

No formal publication or acceptance was verified for the following papers as of **2026-10-04**; years refer to the first arXiv submission, with newer submissions listed first.

<a id="preprints-2026"></a>

### 2026

<a id="omnivl-guard-pro"></a>

**[arXiv 2026 · preprint]** [OmniVL-Guard Pro: A Tool-Augmented Agent for Omnibus Vision-Language Forensics](https://arxiv.org/abs/2605.16962)

For generated images/videos and related localization and factual verification, selects subsequent tools and parameters from returned observations; checker-guided training is a separate component.

<a id="agentfox"></a>

**[arXiv 2026 · preprint]** [AgentFoX: LLM Agent-Guided Fusion with eXplainability for AI-Generated Image Detection](https://arxiv.org/abs/2603.23115)

For generated-image detection, initially queries every expert and consults reliability profiles when results conflict, adapting interpretation rather than replanning detector calls.

<a id="evoguard"></a>

**[arXiv 2026 · preprint]** [EvoGuard: An Extensible Agentic RL-based Framework for Practical and Evolving AI-Generated Image Detection](https://arxiv.org/abs/2603.17343)

For generated-image detection, selects detectors using capability profiles and uses their results to decide whether to call more tools or stop.

<a id="preprints-2025"></a>

### 2025

<a id="aifo"></a>

**[arXiv 2025 · preprint]** [From Evidence to Verdict: An Agent-Based Forensic Framework for AI-Generated Image Detection](https://arxiv.org/abs/2511.00181) (AIFo)

For generated-image detection, executes an initial tool set and conditionally debates insufficient or conflicting evidence, without replanning evidence acquisition.

<a id="fakehunter"></a>

**[arXiv 2025 · preprint]** [Memory-Anchored Multimodal Reasoning for Explainable Video Forensics](https://arxiv.org/abs/2508.14581) (FakeHunter)

For related video and audio manipulation, retrieves reference examples and conditionally invokes visual/audio tools when confidence is low before producing a final explanation.

<a id="method-index"></a>

## Method index

- **Adaptive tool use:** [EvoGuard](#evoguard), [ForenAgent](#forenagent), [ATAR](#atar), [OmniVL-Guard Pro](#omnivl-guard-pro).
- **Active perception:** [Defake-o3](#defake-o3), [ForgeryVCR](#forgeryvcr).
- **Multi-agent evidence reasoning:** [SafeGuard](#safeguard), [Hermes](#hermes), [AIFo](#aifo).
- **Expert routing and evidence fusion:** [UniShield](#unishield), [AgentFoX](#agentfox).
- **Retrieval and conditional verification:** [FakeHunter](#fakehunter).

<a id="contributing"></a>

## Contributing

[Suggest a paper](https://github.com/liu33333/Awesome-Agentic-AIGC-Detection/issues/new?template=paper_suggestion.md) or [report a correction](https://github.com/liu33333/Awesome-Agentic-AIGC-Detection/issues/new?template=correction.md). Include the full title, publication status, venue and source, plus a section or figure supporting the method description. See [CONTRIBUTING.md](CONTRIBUTING.md).
