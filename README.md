# Awesome Agentic AIGC Detection

[English](README.md) | [简体中文](README_CN.md)

Papers on agentic AIGC detection, organized by input modality, covering generated-content detection and related manipulation forensics.

## Contents

- [Images](#images)
- [Videos](#videos)
- [Images and videos](#images-and-videos)
- [Audio-video](#audio-video)
- [Contributing](#contributing)

Tables are ordered newest first: published papers use the conference opening date; preprints and accepted papers without verified proceedings publication use their first arXiv submission date; date and venue links provide sources, with status checked on 2026-10-04.

<a id="images"></a>

## Images

| Paper | Venue / status | Date | Task | Method tags |
| --- | --- | --- | --- | --- |
| <a id="atar"></a>**[Agentic Tool-Augmented Reasoning for Explainable Image Forgery Detection](https://arxiv.org/abs/2609.39066)** (ATAR) | [ACM Multimedia 2026 · Oral · accepted](https://arxiv.org/abs/2609.39066) | [2026-09-30](https://arxiv.org/abs/2609.39066) | Generated images · face/local/document manipulation | Adaptive tool use · cropping · forensic tools |
| <a id="forenagent"></a>**[Code-in-the-Loop Forensics: Agentic Tool Use for Image Forgery Detection](https://arxiv.org/abs/2512.16300)** (ForenAgent) | [ECCV 2026 · published](https://link.springer.com/chapter/10.1007/978-3-032-37592-6_12) | [2026-09-08](https://eccv.ecva.net/Conferences/2026/Venues) | Generated images · local edits | Code execution · tool-output feedback |
| <a id="defake-o3"></a>**[Defake-o3: From Speculative Rationales to Verifiable Evidence for Explainable AIGI Detection](https://arxiv.org/abs/2608.16259)** | [ACM Multimedia 2026 · accepted](https://arxiv.org/abs/2608.16259) | [2026-08-17](https://arxiv.org/abs/2608.16259) | Generated-image detection | Active perception · adaptive cropping |
| <a id="unishield"></a>**[UniShield: An Adaptive Multi-Agent Framework for Unified Forgery Image Detection and Localization](https://arxiv.org/abs/2510.03161)** | [CVPR Findings 2026 · published](https://openaccess.thecvf.com/content/CVPR2026F/html/Huang_UniShield_An_Adaptive_Multi-Agent_Framework_for_Unified_Forgery_Image_Detection_CVPRF_2026_paper.html) | [2026-06-03](https://cvpr.thecvf.com/Conferences/2026/Dates) | Generated images · face/local/document manipulation | Single-detector routing · result aggregation |
| <a id="agentfox"></a>**[AgentFoX: LLM Agent-Guided Fusion with eXplainability for AI-Generated Image Detection](https://arxiv.org/abs/2603.23115)** | arXiv 2026 · preprint | [2026-03-24](https://arxiv.org/abs/2603.23115) | Generated-image detection | Fixed expert calls · reliability-profile fusion |
| <a id="evoguard"></a>**[EvoGuard: An Extensible Agentic RL-based Framework for Practical and Evolving AI-Generated Image Detection](https://arxiv.org/abs/2603.17343)** | arXiv 2026 · preprint | [2026-03-18](https://arxiv.org/abs/2603.17343) | Generated-image detection | Profile-guided detector selection · adaptive stopping |
| <a id="forgeryvcr"></a>**[ForgeryVCR: Visual-Centric Reasoning via Efficient Forensic Tools in MLLMs for Image Forgery Detection and Localization](https://arxiv.org/abs/2602.14098)** | [ACM Multimedia 2026 · Oral · accepted](https://github.com/youqiwong/ForgeryVCR) | [2026-02-15](https://arxiv.org/abs/2602.14098) | Manipulation detection & localization | Active perception · forensic transforms · zoom |
| <a id="aifo"></a>**[From Evidence to Verdict: An Agent-Based Forensic Framework for AI-Generated Image Detection](https://arxiv.org/abs/2511.00181)** (AIFo) | arXiv 2025 · preprint | [2025-10-31](https://arxiv.org/abs/2511.00181) | Generated-image detection | Initial tool set · conditional multi-agent debate |

<a id="videos"></a>

## Videos

| Paper | Venue / status | Date | Task | Method tags |
| --- | --- | --- | --- | --- |
| <a id="safeguard"></a>**[SafeGuard: A Multi-Agent Perception-Reasoning Framework for Social-Risk AI-Generated Video Detection](https://arxiv.org/abs/2607.03069)** | [ECCV 2026 · published](https://link.springer.com/chapter/10.1007/978-3-032-37029-7_33) | [2026-09-08](https://eccv.ecva.net/Conferences/2026/Venues) | Generated-video detection · social risks | Multi-agent reasoning · hypothesis verification · re-perception |
| <a id="hermes"></a>**[Hermes: An Evidence-Driven Agentic Framework for Trustworthy and Explainable AI-Generated Video Detection](https://proceedings.mlr.press/v306/li26be.html)** | [ICML 2026 · published](https://proceedings.mlr.press/v306/li26be.html) | [2026-07-06](https://icml.cc/Conferences/2026/CallForPapers) | Generated-video detection | Plan retrieval · multi-agent deliberation · evidence-graph revision |

<a id="images-and-videos"></a>

## Images and videos

Methods supporting either image or video input.

| Paper | Venue / status | Date | Task | Method tags |
| --- | --- | --- | --- | --- |
| <a id="omnivl-guard-pro"></a>**[OmniVL-Guard Pro: A Tool-Augmented Agent for Omnibus Vision-Language Forensics](https://arxiv.org/abs/2605.16962)** | arXiv 2026 · preprint | [2026-05-16](https://arxiv.org/abs/2605.16962) | Generated images/videos · localization · fact-checking | Adaptive tool selection · parameter adjustment |

<a id="audio-video"></a>

## Audio-video

Methods examining both visual and audio evidence.

| Paper | Venue / status | Date | Task | Method tags |
| --- | --- | --- | --- | --- |
| <a id="fakehunter"></a>**[Memory-Anchored Multimodal Reasoning for Explainable Video Forensics](https://arxiv.org/abs/2508.14581)** (FakeHunter) | arXiv 2025 · preprint | [2025-08-20](https://arxiv.org/abs/2508.14581) | Video/audio manipulation | Reference retrieval · conditional visual/audio verification |

<a id="contributing"></a>

## Contributing

[Suggest a paper](https://github.com/liu33333/Awesome-Agentic-AIGC-Detection/issues/new?template=paper_suggestion.md) or [report a correction](https://github.com/liu33333/Awesome-Agentic-AIGC-Detection/issues/new?template=correction.md). Include the full title, input modality, venue/status, sorting date and sources, plus evidence for the task and method. See [CONTRIBUTING.md](CONTRIBUTING.md).
